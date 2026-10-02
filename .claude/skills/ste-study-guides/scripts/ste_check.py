#!/usr/bin/env python3
"""Measure study-guide prose against Simplified Technical English at about 80%.

Reads HTML guides and Quartz markdown notes. Explanation prose is measured.
Spoken lines, quotations, code, tables, headings and diagrams are left out:

  HTML      class "say", "cheat" or "turn" (mock dialogue), attribute data-ste="spoken",
            <blockquote>, <q>,
            a container whose label starts with "Say", "The sentence" or "Interview sentence",
            and any block that opens with a quotation mark.
  Markdown  > [!quote] and > [!say] callouts, and any block that opens with a quotation mark.

Word count follows ASD-STE100 rules 8.5 to 8.7: a parenthesis, a quotation, a code
span, a number and a hyphenated word each count as one word.

Usage:
  ste_check.py FILE...                 summary per file
  ste_check.py --list FILE...          also list each sentence over its limit
  ste_check.py --terms "a|b|c" FILE... count a preferred term (a) against its synonyms
  ste_check.py --strict FILE...        exit 1 when a target is missed
"""
import argparse
import html
import re
import sys
from html.parser import HTMLParser

PROSE_LIMIT = 25        # ASD-STE100 rule 6.3, descriptive writing
STEP_LIMIT = 20         # ASD-STE100 rule 5.1, procedures
PARAGRAPH_LIMIT = 6     # ASD-STE100 rule 6.6

TARGETS = {
    "average words per prose sentence": ("avg", 16.0),
    "prose sentences over 25 words": ("over_prose_pct", 10.0),
    "steps over 20 words": ("over_step_pct", 10.0),
    "paragraphs over 6 sentences": ("long_paragraphs", 0),
    "Latin abbreviations": ("latin", 0),
    "prose sentences with a semicolon": ("semicolon_pct", 5.0),
}

SPOKEN_CLASSES = {"say", "cheat", "turn"}
SPOKEN_LABEL = re.compile(r"^(say\b|the sentence|interview sentence)", re.I)
BLOCK_TAGS = {"p", "li", "td", "th", "figcaption", "h1", "h2", "h3", "h4", "h5", "h6",
              "dt", "dd", "blockquote", "footer", "summary", "caption"}
SKIP_TAGS = {"style", "script", "svg", "pre", "nav", "button", "select", "title", "head"}
VOID_TAGS = {"br", "hr", "img", "input", "meta", "link", "embed", "source", "wbr", "col", "area"}
QUOTE_OPEN = ('"', "“", "‘", "'")
LATIN = re.compile(r"\b(e\.g\.|i\.e\.|etc\.|viz\.|cf\.)", re.I)
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?\w+(ed|en)\b", re.I)
SPLIT = re.compile(r"(?<=[.!?])[\"”’)]?\s+(?=[A-Z0-9\"“(])")


def count_words(sentence):
    s = re.sub(r"\([^()]*\)", " P ", sentence)
    s = re.sub(r"\"[^\"]{1,160}\"|“[^”]{1,160}”", " Q ", s)
    return len([t for t in s.split() if re.search(r"[\w$€£%]", t)])


def sentences(text):
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    return [s.strip() for s in SPLIT.split(text) if count_words(s.strip()) >= 3]


class Block:
    def __init__(self, kind, line, text):
        self.kind, self.line, self.text = kind, line, text


class HtmlBlocks(HTMLParser):
    """Collects text blocks with their kind: prose, step, paragraph, spoken, table, heading."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # entries: [tag, classes, spoken_flag, attrs]
        self.buf, self.buf_line = [], None
        self.blocks = []
        self.skip = 0

    def _context(self):
        tags = [e[0] for e in self.stack]
        spoken = any(e[2] for e in self.stack)
        return tags, spoken

    def flush(self):
        text = html.unescape("".join(self.buf)).strip()
        line = self.buf_line
        self.buf, self.buf_line = [], None
        if not text:
            return
        tags, spoken = self._context()
        top = self.stack[-1] if self.stack else None
        if top and "label" in top[1] and SPOKEN_LABEL.match(text):
            for e in reversed(self.stack[:-1]):
                if e[0] in ("div", "aside", "section"):
                    e[2] = True
                    break
        if top and ("label" in top[1] or "who" in top[1] or "clock" in top[1]):
            kind = "heading"
        elif any(t in ("h1", "h2", "h3", "h4", "h5", "h6", "summary", "caption") for t in tags):
            kind = "heading"
        elif spoken or text.startswith(QUOTE_OPEN):
            kind = "spoken"
        elif any(t in ("td", "th") for t in tags):
            kind = "table"
        elif "li" in tags:
            parents = [t for t in tags if t in ("ol", "ul")]
            kind = "step" if parents and parents[-1] == "ol" else "prose"
        elif "p" in tags:
            kind = "paragraph"
        else:
            kind = "prose"
        self.blocks.append(Block(kind, line, text))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP_TAGS:
            self.skip += 1
        if tag in VOID_TAGS:
            if tag == "br":
                self.buf.append(" ")
            return
        if tag in BLOCK_TAGS or tag in ("div", "ol", "ul", "table", "tr", "section", "aside", "figure"):
            self.flush()
        classes = set((a.get("class") or "").split())
        spoken = bool(classes & SPOKEN_CLASSES) or a.get("data-ste") == "spoken" or tag in ("blockquote", "q")
        self.stack.append([tag, classes, spoken, a])
        if tag == "code" and not self.skip:
            self.buf.append(" CODE ")
            self.skip += 1
            self.stack[-1].append("code-skip")

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        if tag in BLOCK_TAGS or tag in ("div", "ol", "ul", "table", "tr", "section", "aside", "figure"):
            self.flush()
        while self.stack:
            e = self.stack.pop()
            if e[0] in SKIP_TAGS:
                self.skip -= 1
            if len(e) > 4 and e[4] == "code-skip":
                self.skip -= 1
            if e[0] == tag:
                break

    def handle_data(self, data):
        if self.skip:
            return
        if self.buf_line is None and data.strip():
            self.buf_line = self.getpos()[0]
        self.buf.append(data)


def html_blocks(src):
    p = HtmlBlocks()
    p.feed(src)
    p.flush()
    return p.blocks


def md_blocks(src):
    lines = src.split("\n")
    i, blocks = 0, []
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    para, para_line, para_kind = [], None, None
    in_code = False
    spoken_callout = False

    def clean(t):
        t = re.sub(r"`[^`]*`", " CODE ", t)
        t = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", t)
        t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", t)
        return t

    def flush():
        nonlocal para, para_line, para_kind
        if para:
            text = clean(" ".join(para)).strip()
            kind = para_kind
            if text.startswith(QUOTE_OPEN):
                kind = "spoken"
            blocks.append(Block(kind, para_line, text))
        para, para_line, para_kind = [], None, None

    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        n = i + 1
        i += 1
        if s.startswith("```"):
            flush()
            in_code = not in_code
            continue
        if in_code:
            continue
        if not s:
            flush()
            spoken_callout = False
            continue
        if re.match(r"\[[^\]]+\]:\s*\S+", s):
            flush()
            continue
        if s.startswith("<") or s.startswith("#") or s.startswith("|"):
            flush()
            if s.startswith("|"):
                blocks.append(Block("table", n, clean(s)))
            continue
        if s.startswith(">"):
            body = s.lstrip(">").strip()
            m = re.match(r"\[!(\w+)\][-+]?\s*(.*)", body)
            if m:
                flush()
                spoken_callout = m.group(1).lower() in ("quote", "say")
                body = m.group(2)
                if not body:
                    continue
                kind = "spoken" if spoken_callout else "heading"
                blocks.append(Block(kind, n, clean(body)))
                continue
            kind = "spoken" if spoken_callout else "paragraph"
            if para and para_kind != kind:
                flush()
            if not para:
                para_line, para_kind = n, kind
            para.append(body)
            continue
        m = re.match(r"([-*+]|\d+[.)])\s+(.*)", s)
        if m:
            flush()
            kind = "step" if m.group(1)[0].isdigit() else "prose"
            para, para_line, para_kind = [m.group(2)], n, kind
            continue
        if not para:
            para_line, para_kind = n, "paragraph"
        para.append(s)
    flush()
    return blocks


def analyse(path):
    src = open(path, encoding="utf-8").read()
    blocks = html_blocks(src) if path.endswith((".html", ".htm")) else md_blocks(src)
    r = {"prose": 0, "words": 0, "over_prose": 0, "steps": 0, "over_step": 0,
         "long_paragraphs": 0, "latin": 0, "semicolons": 0, "passive": 0,
         "spoken": 0, "list": []}
    for b in blocks:
        if b.kind in ("heading", "table"):
            continue
        if b.kind == "spoken":
            r["spoken"] += max(1, len(SPLIT.split(b.text.strip())))
            continue
        sents = sentences(b.text)
        if b.kind == "paragraph" and len(sents) > PARAGRAPH_LIMIT:
            r["long_paragraphs"] += 1
            r["list"].append((b.line, "paragraph", len(sents), b.text[:120] + "…"))
        for s in sents:
            w = count_words(s)
            if LATIN.search(s):
                r["latin"] += 1
                r["list"].append((b.line, "latin", w, s))
            if b.kind == "step":
                r["steps"] += 1
                if w > STEP_LIMIT:
                    r["over_step"] += 1
                    r["list"].append((b.line, "step", w, s))
                continue
            r["prose"] += 1
            r["words"] += w
            if PASSIVE.search(s):
                r["passive"] += 1
            if ";" in s:
                r["semicolons"] += 1
                r["list"].append((b.line, "semicolon", w, s))
            if w > PROSE_LIMIT:
                r["over_prose"] += 1
                r["list"].append((b.line, "prose", w, s))
    pct = lambda a, b: 100.0 * a / b if b else 0.0
    r["avg"] = r["words"] / r["prose"] if r["prose"] else 0.0
    r["over_prose_pct"] = pct(r["over_prose"], r["prose"])
    r["over_step_pct"] = pct(r["over_step"], r["steps"])
    r["semicolon_pct"] = pct(r["semicolons"], r["prose"])
    r["passive_pct"] = pct(r["passive"], r["prose"])
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--list", action="store_true", help="list each sentence over its limit")
    ap.add_argument("--terms", action="append", default=[], metavar="PREFERRED|SYNONYM|...",
                    help="count a preferred term against its synonyms (case-insensitive)")
    ap.add_argument("--strict", action="store_true", help="exit 1 when any target is missed")
    args = ap.parse_args()

    missed = False
    for path in args.files:
        r = analyse(path)
        print(f"\n{path}")
        print(f"  prose sentences {r['prose']}, steps {r['steps']}, spoken lines skipped {r['spoken']}")
        print(f"  passive voice (heuristic): {r['passive_pct']:.0f}% of prose sentences")
        for name, (key, limit) in TARGETS.items():
            value = r[key]
            ok = value <= limit
            missed |= not ok
            shown = f"{value:.1f}" if isinstance(value, float) else str(value)
            unit = "%" if key.endswith("pct") else ""
            print(f"  {'PASS' if ok else 'MISS'}  {name}: {shown}{unit} (target {limit}{unit} or less)")
        if args.list and r["list"]:
            print("  to fix or justify:")
            for line, kind, w, text in sorted(r["list"], key=lambda x: x[0] or 0):
                text = re.sub(r"\s+", " ", text)
                print(f"    line {line}  [{kind} {w}]  {text}")

    if args.terms:
        print("\nterms")
        for group in args.terms:
            variants = [v.strip() for v in group.split("|") if v.strip()]
            for path in args.files:
                src = open(path, encoding="utf-8").read()
                src = re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", src, flags=re.S)
                counts = [len(re.findall(r"\b" + re.escape(v) + r"\b", src, re.I)) for v in variants]
                drift = sum(counts[1:])
                flag = "DRIFT" if drift and counts[0] else ("ONLY-SYNONYM" if drift else "ok")
                pairs = ", ".join(f"{v}={c}" for v, c in zip(variants, counts))
                print(f"  {flag:12s} {path}: {pairs}")

    sys.exit(1 if (args.strict and missed) else 0)


if __name__ == "__main__":
    main()
