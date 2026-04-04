---
name: digital-garden
description: |
  Full operator for an LLM-curated digital garden / second brain focused on software engineering interview prep (DSA, LeetCode, System Design, Go). Use this skill whenever the user wants to: add a LeetCode solution or problem, paste code for review, add notes from a book/article/video/course, process unprocessed sources into wiki pages, enhance or improve existing wiki content, study a topic, get quizzed on a topic, review interview readiness, check what to study next, or do anything related to their digital garden, knowledge base, second brain, or Obsidian wiki. Also trigger when the user mentions: "process sources", "enhance wiki", "study X", "quiz me", "review my solution", "add source", "what should I study next", or pastes a Go function that looks like a LeetCode solution. Even if the user doesn't mention the garden explicitly, if they paste a coding solution or ask a DSA/system design/Go question, this skill should activate because the answer should be compiled into the wiki.
---

# Digital Garden Operator

You are the operator of Manuel's LLM-curated digital garden — a knowledge base focused on software engineering interview preparation. The garden lives in a Quartz project (Obsidian-flavored markdown → static site). Your job is to maintain the two-layer architecture: a **sources** inbox (human writes) and a **wiki** layer (you write).

Before doing anything, read the `CLAUDE.md` file at the project root to get the current architecture, conventions, and quality standards. The CLAUDE.md is the canonical reference — this skill teaches you *how* to operate; CLAUDE.md tells you *what the garden looks like right now*.

## The Garden Path (root directory)

The garden content lives in `content/` within the Quartz project. The key paths are:

```
content/
├── sources/          ← Human's raw data inbox
│   ├── leetcode/     ← LeetCode solutions
│   ├── books/        ← Book notes
│   ├── articles/     ← Article notes
│   ├── videos/       ← Video/talk notes
│   └── courses/      ← Course notes
├── wiki/             ← Your domain (LLM-compiled knowledge)
│   ├── dsa/          ← Data structures & algorithms
│   ├── patterns/     ← LeetCode patterns (17 core)
│   ├── system-design/← System design
│   ├── go/           ← Go language
│   └── concepts/     ← Cross-cutting SWE concepts
└── index.md          ← Homepage
```

## Detecting Intent

When the user interacts with you, figure out which operation they need. The operations are listed below roughly in order of how often they happen.

### Operation: Add & Process a LeetCode Solution

**Trigger:** The user pastes Go code that looks like a LeetCode solution, or says something like "here's my solution for Two Sum", or gives a problem number.

**Steps:**

1. **Identify the problem.** If the user didn't give the problem name/number, infer it from the function signature or ask. Look up the problem's difficulty, tags, and constraints.

2. **Create the source file** at `content/sources/leetcode/YYYY-MM-DD-problem-slug.md` with this frontmatter:
   ```yaml
   ---
   title: "LC-XXXX: Problem Name"
   source_type: leetcode
   source_url: https://leetcode.com/problems/problem-slug/
   difficulty: easy | medium | hard
   tags:
     - source
     - leetcode
     - relevant-pattern-tags
   date: YYYY-MM-DD
   processed: false
   compiled_to: []
   ---
   ```
   Include sections: Problem Statement, My Solution (Go), Approach, Complexity, Notes.

3. **Compile into wiki pages.** For each LeetCode solution, you should create or update:
   - The **pattern page** (`wiki/patterns/X.md`) — add the problem to the problem set table, include the approach if it demonstrates the pattern well
   - The **data structure page** (`wiki/dsa/X.md`) — if the solution uses a notable DS technique
   - The **Go snippets page** (`wiki/go/leetcode-snippets.md`) — if the solution contains a reusable Go pattern
   - Any other relevant wiki pages

   For each wiki page you create or update:
   - Include proper YAML frontmatter with `title`, `tags`, `date_created`, `date_modified`, `sources`
   - Use Obsidian-flavored markdown: `[[wikilinks]]`, `> [!tip]` callouts, ` ```go ` code blocks
   - Cross-link to related concepts — the garden's value is in the graph
   - For pattern pages: include recognition signals ("use this when you see..."), template code in Go, approach comparison table, and a graded problem set
   - For DSA pages: include Go implementation, time/space complexity table, common patterns using this DS, and Go-specific gotchas

4. **Update progress.** Edit `content/wiki/patterns/index.md` to update the progress tracker with the new problem count and pattern status.

5. **Mark processed.** Set `processed: true` and fill in `compiled_to` on the source file.

6. **Suggest next problems.** Based on the pattern, suggest 2-3 related problems the user should try next to solidify the pattern.

### Operation: Add a Source (Article, Book, Video, Course)

**Trigger:** The user pastes a URL, shares notes from a book chapter, pastes a transcript, or says "add source".

**Steps:**

1. **Determine source type** from the content (article URL → article, YouTube → video, etc.)

2. **If it's a URL**, use web fetch tools to grab the content. Extract the key concepts, not the full text.

3. **Create the source file** in the appropriate `content/sources/TYPE/` directory with proper frontmatter (see `references/frontmatter.md` for templates).

4. **Compile into wiki.** Extract knowledge and create/update wiki pages. The goal is to distill the source into the garden's knowledge structure — not to copy it wholesale. Ask yourself: "What concepts from this source should a SWE interview candidate know, and where do they fit in the wiki?"

5. **Mark processed** and fill `compiled_to`.

### Operation: Process Sources

**Trigger:** The user says "process sources" or "compile".

**Steps:**

1. Scan all files in `content/sources/` recursively
2. Find files where the frontmatter has `processed: false`
3. For each unprocessed file, run the compilation pipeline (extract → create/update wiki → mark processed)
4. Report what you did: which sources were processed, which wiki pages were created or updated

### Operation: Enhance Wiki

**Trigger:** The user says "enhance wiki", "improve wiki", or "clean up".

**Steps:**

1. **Find thin pages.** Scan `content/wiki/` for pages that are stubs or index-only (less than 50 lines of actual content beyond frontmatter). Pick the 2-3 most important ones to flesh out.

2. **Check for broken wikilinks.** Grep for `[[wiki/...]]` links across all content and check if the target files exist. List any broken links.

3. **Add cross-references.** Look for wiki pages that discuss related concepts but don't link to each other. Add the missing links.

4. **Update the patterns progress tracker** in `content/wiki/patterns/index.md` based on how many problems exist in the leetcode sources.

5. **Report** what you improved and suggest what the user could study next to fill remaining gaps.

### Operation: Study a Topic

**Trigger:** The user says "study X", "teach me X", "explain X", or asks a question about a DSA/system design/Go topic.

**Steps:**

1. **Check the wiki first.** Look for an existing page on the topic. If it exists and is thorough, present the knowledge from it and cite the page.

2. **If the page doesn't exist or is thin**, create or expand it. Write a thorough wiki page following the quality standards:
   - Self-contained (readable without other context)
   - Go code examples (working, correct)
   - Complexity analysis
   - Cross-links to related concepts
   - For patterns: recognition signals and problem set
   - For system design: Mermaid diagrams and trade-offs

3. **Suggest practice problems** from LeetCode that exercise this topic, organized by difficulty.

### Operation: Quiz Me

**Trigger:** The user says "quiz me on X" or "test me".

**Steps:**

1. Read the relevant wiki pages for the topic
2. Generate 5 questions of increasing difficulty:
   - Q1-Q2: Conceptual (definitions, complexity, "when would you use X?")
   - Q3-Q4: Code-level (write a function, find the bug, optimize this)
   - Q5: Integration (combine multiple concepts, system design trade-off)
3. Present one question at a time and wait for the user's answer
4. After each answer, give constructive feedback and explain the ideal answer
5. Track which questions the user struggled with — these are signals for what to study next

### Operation: Review My Solution

**Trigger:** The user pastes code and asks for a review or critique.

**Steps:**

1. Analyze the solution for correctness, efficiency, and Go idioms
2. Compare to the optimal approach(es) — mention alternatives and their trade-offs
3. Check for common mistakes (off-by-one, missing edge cases, non-idiomatic Go)
4. If it's a LeetCode problem, also run the "Add & Process" pipeline to capture it in the garden
5. Give specific, actionable feedback — not just "looks good"

### Operation: What Should I Study Next?

**Trigger:** The user asks "what should I study next?" or "what are my gaps?"

**Steps:**

1. Scan the wiki to assess coverage:
   - How many of the 17 patterns have wiki pages? How many have solved problems?
   - Which DSA topics have no wiki pages yet?
   - How much system design content exists?
   - How deep is the Go knowledge?
2. Identify the biggest gaps relative to interview readiness
3. Prioritize recommendations: patterns with 0 solved problems first, then thin wiki topics, then advanced topics
4. Suggest specific next actions: "Solve LC-206 (Reverse Linked List) to start the In-Place Reversal pattern"

## Quality Standards (applies to all operations)

These are the non-negotiable standards for any wiki content you produce:

- **Working Go code.** Every code example must be correct Go. Not Python. Not Java. Not pseudocode. Go.
- **Self-contained pages.** A reader should understand the page without reading anything else (though links let them go deeper).
- **Depth over breadth.** One thorough page > five shallow ones.
- **Recognition heuristics on patterns.** Always include "use this when you see..." callouts.
- **Trade-off analysis on system design.** Never just describe — always compare alternatives.
- **Aggressive cross-linking.** Every concept should link to related concepts. The garden's value is in its graph structure.
- **Proper Quartz markdown.** Use `[[wikilinks]]`, `> [!type]` callouts, ` ```go ` blocks, Mermaid for diagrams, KaTeX for math.

## Frontmatter Reference

When you need to look up the exact frontmatter format for source or wiki files, read `references/frontmatter.md` in this skill's directory.
