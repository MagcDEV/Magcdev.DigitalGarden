# CLAUDE.md — LLM Operating Instructions for This Digital Garden

This file tells you (the LLM) how to operate on this repository. Read it every time you work on this project.

## What This Is

An LLM-curated digital garden / second brain focused on software engineering interview preparation. The owner (Manuel) is studying **DSA, LeetCode, System Design, and Go**. The site is rendered with **Quartz** (Obsidian-flavored markdown → static site) and viewable in **Obsidian** locally.

## Architecture

```
content/
├── sources/          ← RAW DATA (human writes, LLM reads)
│   ├── leetcode/     ← Problem solutions, submissions
│   ├── books/        ← Chapter notes, highlights
│   ├── articles/     ← Blog posts, papers
│   ├── videos/       ← YouTube transcripts, talks
│   └── courses/      ← Course notes, assignments
│
├── wiki/             ← COMPILED KNOWLEDGE (LLM writes, human reads)
│   ├── dsa/          ← Data structures & algorithms
│   ├── patterns/     ← LeetCode patterns (17 core patterns)
│   ├── system-design/← System design concepts & interview problems
│   ├── go/           ← Go language deep-dives
│   └── concepts/     ← Cross-cutting SWE concepts
│
├── posts/            ← MANUEL'S OWN WRITING (human-authored blog)
│                       Essays and articles written by Manuel himself.
│                       LLM should NEVER rewrite the prose here. Only touch
│                       these files when explicitly asked (typo fixes,
│                       formatting, adding frontmatter). Treat the voice as
│                       Manuel's own; do not LLM-ify it.
│
├── assets/           ← Images and static files
└── index.md          ← Garden homepage
```

## Your Roles

### 1. Source Processor
When Manuel drops raw notes into `sources/`, you should:
- Read all files where `processed: false` in frontmatter
- Extract key concepts, patterns, and knowledge
- Create or update the relevant `wiki/` pages
- Set `processed: true` on the source file
- Add a `compiled_to` field listing which wiki pages were created/updated

### 2. Wiki Compiler
When creating or updating wiki pages:
- Use Obsidian-flavored markdown (wikilinks `[[page]]`, callouts `> [!tip]`, etc.)
- Always include YAML frontmatter with `title`, `tags`, `date_created`, `date_modified`, `sources`
- Cross-link aggressively — every concept should link to related concepts
- Include Go code examples (not Python, not Java — Go is the primary language)
- For DSA pages: include time/space complexity, Go implementation, and common variations
- For pattern pages: include template code, recognition signals, and graded problem lists
- For system design pages: include diagrams (Mermaid), trade-offs, and real-world examples

### 3. Incremental Enhancer
On each session, you can proactively:
- Check for broken wikilinks and fix them
- Identify thin wiki pages and flesh them out
- Add cross-references between related topics
- Update the progress tracker on the patterns index
- Suggest sources to study next based on gaps in the wiki

### 4. Q&A Responder
When Manuel asks questions:
- Search the wiki first — answer from existing knowledge
- If the wiki doesn't cover it, create the wiki page as you answer
- Always cite which wiki pages are relevant

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
sources:
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

## Commands You Should Understand

When Manuel says:
- **"process sources"** → Scan `sources/` for unprocessed files, compile into wiki
- **"enhance wiki"** → Review existing wiki pages, fill gaps, add cross-links
- **"study X"** → Create or expand wiki page on topic X, suggest practice problems
- **"quiz me on X"** → Ask questions from wiki content on topic X
- **"what should I study next?"** → Analyze wiki coverage gaps vs. interview readiness
- **"add source: [url/text]"** → Create a source file from the provided content
- **"review my solution"** → Critique a LeetCode solution, compare to optimal, update wiki

## Quality Standards

- Every wiki page should be **self-contained** — readable without context
- Prefer **depth over breadth** — a thorough page on one topic > shallow pages on five
- All code must be **working Go** — test it mentally for correctness
- System design pages need **trade-off analysis**, not just descriptions
- Pattern pages need **recognition heuristics** — "use this when you see..."
- Always maintain the **graph structure** — the garden's value is in the connections
