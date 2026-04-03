# Magcdev's Digital Garden

An LLM-curated digital garden focused on software engineering interview preparation. Built with [Quartz](https://quartz.jzhao.xyz/) and viewable in [Obsidian](https://obsidian.md/).

## How It Works

```
Raw Sources → LLM Processing → Wiki Pages → Quartz/Obsidian
```

1. **Sources** (`content/sources/`): Raw notes from LeetCode, books, articles, videos, and courses
2. **Wiki** (`content/wiki/`): Structured, interlinked knowledge pages compiled by an LLM
3. **Rendering**: Quartz builds a static site; Obsidian provides local browsing with graph view

The wiki is the LLM's domain — it processes raw sources into structured knowledge and incrementally refines it over time. See `CLAUDE.md` for the full operating instructions.

## Topics

- **Data Structures & Algorithms** — Core CS, complexity analysis, problem-solving
- **LeetCode Patterns** — 17 recurring patterns with Go templates
- **System Design** — Distributed systems, scalability, classic interview problems
- **Go Programming** — Language deep-dives, concurrency, standard library
- **Core Concepts** — Design patterns, SOLID, clean code, testing

## Local Development

```bash
npm install
npx quartz build --serve
```

## License

[MIT](LICENSE.txt)
