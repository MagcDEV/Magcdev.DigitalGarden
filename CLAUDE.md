# CLAUDE.md — Operating Instructions for This Notebook

Read this every time you work on this project.

## What This Is

Manuel's study notebook for his software engineering career, rendered with **Quartz** (Obsidian-flavored markdown → static site) and readable in **Obsidian** locally. Any topic that helps the career belongs here: system design, Go and other languages, DSA and LeetCode, tools, architecture, a specific company's interview, career topics. Manuel decides what goes in; the LLM writes it up clearly and links it. There is no fixed syllabus and no required pipeline.

The `digital-garden` skill in `.claude/skills/` carries the operations (add, study, capture, review, build a guide, condense, quiz, enhance, what next) and the writing rules. This file holds the layout and conventions.

## Layout

```
content/
├── wiki/             ← THE NOTES (LLM writes, Manuel reads)
│   ├── dsa/          ← Data structures & algorithms
│   ├── patterns/     ← LeetCode patterns
│   ├── system-design/← System design concepts, problems, company-specific prep
│   ├── go/           ← Go language
│   ├── concepts/     ← Cross-cutting SWE concepts
│   └── <new area>/   ← add a folder when a topic needs one
│
├── sources/          ← OPTIONAL INBOX for raw material (Manuel writes, LLM reads)
│   ├── leetcode/  books/  articles/  videos/  courses/
│
├── posts/            ← MANUEL'S OWN WRITING
│                       Never rewrite the prose. Touch only when asked
│                       (typo fixes, formatting, frontmatter).
│
├── assets/           ← Images, and standalone HTML study guides in a folder per subject
└── index.md          ← Homepage
```

**Standalone HTML guides.** Long, designed material (diagrams, mock interviews, one-card summaries) lives as a self-contained HTML page under `content/assets/<subject>/`, embedded from a wiki page that sets `cssclasses: [<subject>]`. `content/wiki/system-design/nubank-study-notes.md` is the model. Everything else is markdown.

**Sources are optional.** A note may be written directly with no source file behind it. When a source file exists it carries `processed` and `compiled_to` so the inbox can be swept.

## Frontmatter Conventions

### Source files
```yaml
---
title: "LC-0001: Two Sum"
source_type: leetcode | book | article | video | course
source_url: https://...
difficulty: easy | medium | hard  # for leetcode
tags:
  - source
  - topic-area
date: 2026-04-03
processed: false
compiled_to: []  # filled by LLM after processing
---
```

### Wiki files
```yaml
---
title: "Two Pointers Pattern"
tags:
  - wiki
  - patterns
date_created: 2026-04-03
date_modified: 2026-04-03
sources:   # optional
  - "[[sources/leetcode/2026-04-03-two-sum]]"
---
```

### Post files (Manuel's blog)
```yaml
---
title: "Post Title"
author: "Manuel"
date: 2026-05-17
tags:
  - post
  - topic-area
description: "One-line summary used in listings and OG cards."
---
```

## Quartz Compatibility Rules

- Use `[[wikilinks]]` for internal links (Quartz resolves shortest-path)
- Use `> [!type]` callout syntax (tip, info, warning, abstract, etc.)
- Mermaid diagrams work inside ` ```mermaid ` code blocks
- LaTeX works with `$inline$` and `$$block$$` (KaTeX engine)
- Files in `templates/` and `private/` are ignored by Quartz
- Tags go in frontmatter YAML arrays, not inline `#tags`
- Code syntax highlighting: use ` ```go ` for Go code blocks

## Writing Standards

- **Self-contained notes.** Readable without any other page open; links let the reader go deeper.
- **Plain, tight prose.** One idea per sentence, 20 words or fewer for instructions and 25 for explanation, active voice, present tense. One term per concept; use the term the existing notes use.
- **Spoken lines stay spoken.** Scripts, "say it" boxes and "never say" lists keep their rhythm.
- **Code that runs.** Go by default; the topic's own language when the topic is another language or tool.
- **Depth over breadth.** One thorough note beats five shallow ones.
- **Trade-offs on design topics.** Compare alternatives and say what each costs.
- **Recognition signals on pattern notes.** "Use this when you see…", a Go template, a graded problem list.
- **Links everywhere.** The notebook's value is the graph.
