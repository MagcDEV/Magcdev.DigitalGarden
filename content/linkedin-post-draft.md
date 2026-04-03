---
title: "LinkedIn Post Draft — LLM-Curated Digital Garden"
draft: true
---

I stopped taking notes the traditional way. Now an LLM does it for me.

Inspired by Andrej Karpathy's recent post on LLM Knowledge Bases (https://x.com/karpathy/status/2039805659525644595), I built a digital garden where I barely touch the wiki — it's the LLM's domain.

Here's how it works:

I'm preparing for software engineering interviews (DSA, System Design, Go), and I needed a system that compounds knowledge instead of losing it across scattered notes.

So I built a two-layer architecture:

→ Sources layer: I drop raw data — LeetCode solutions, book highlights, article notes, video transcripts — into an inbox.

→ Wiki layer: An LLM reads unprocessed sources, extracts key concepts, and compiles them into structured, interlinked markdown pages. It adds Go code examples, complexity analysis, recognition heuristics for patterns, and Mermaid diagrams for system design.

The result is a growing knowledge graph with 100+ planned wiki pages across 5 areas: Data Structures & Algorithms, LeetCode Patterns (17 core patterns with templates), System Design, Go deep-dives, and core SWE concepts.

Everything is viewable in Obsidian locally and published as a static site via Quartz. Every concept links to related concepts. Every source traces to the wiki pages it generated.

As Karpathy put it: "raw data from sources is collected, compiled by an LLM into a .md wiki, then operated on to do Q&A and to incrementally enhance the wiki." That's exactly the workflow.

The best part? Each study session makes the entire knowledge base smarter. My explorations and solutions always "add up."

The garden is open source — check it out and feel free to fork it as a template for your own learning journey.

#SoftwareEngineering #LLM #DigitalGarden #CodingInterviews #Go #DSA #SystemDesign #SecondBrain #BuildInPublic
