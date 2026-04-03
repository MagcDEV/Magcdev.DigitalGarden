---
title: "Sources Inbox"
tags:
  - meta
  - sources
---

# Sources Inbox

This is the **raw data layer** of the garden. Content here is collected from various sources and awaits processing by the LLM into the [[wiki/index|Wiki]].

## How It Works

1. **You** drop raw notes, links, transcripts, solutions, or highlights into the appropriate subfolder
2. **The LLM** reads these sources, extracts knowledge, and compiles it into structured wiki pages
3. **Sources are kept** as a permanent record of where knowledge came from

## Source Categories

- [[sources/leetcode/index|LeetCode]] — Problem solutions, submissions, editorial notes
- [[sources/books/index|Books]] — Highlights, chapter notes, key takeaways
- [[sources/articles/index|Articles]] — Blog posts, papers, technical write-ups
- [[sources/videos/index|Videos]] — YouTube transcripts, conference talks
- [[sources/courses/index|Courses]] — Course notes, assignments, lecture summaries

## Conventions

- File names: `YYYY-MM-DD-descriptive-slug.md`
- Always include `source_url` in frontmatter when applicable
- Tag with the topic area so the LLM knows where to route it
