---
title: "Nubank AI Coding Interview Playbook"
tags:
  - wiki
  - ai-coding
  - nubank
  - interview
date_created: 2026-10-14
date_modified: 2026-10-14
cssclasses:
  - nubank-guides
---

This is the playbook for Nubank's AI coding round. You get sixty minutes in a browser VS Code, with Claude Code in the terminal. The interviewer watches how you think. The round comes after the [[wiki/system-design/nubank-study-notes|system design round]]. The guide is embedded as-is. It follows the garden's light or dark theme and has its own toggle in the top-right corner.

The **Open full page** button loads the guide as a standalone document. Keep that version on your phone during the call. The shared screen shows only the editor and `NOTES.md`.

> [!abstract] The one idea
> They do not grade the program. They grade the engineer who directed it. Each move in the playbook maps to one of four criteria: decomposition, AI steering, readable code, and communication.

> [!tip] What to reread 20 minutes before the call
> Section 3 is the opening script. Section 5 has the six prompt templates (kickoff, slice, correction, tests, debug, final review). Section 8 is the debug protocol: read the error aloud, state a hypothesis, verify it, then fix.

## How the hour runs

1. **0–10: understand and plan.** Write no code. Ask 3–4 clarifying questions, write a plan of 3–5 testable steps in `NOTES.md`, and list the edge cases.
2. **10–15: brief Claude Code.** Send the kickoff prompt, read its plan aloud, then say "go". Only the skeleton and a failing test land.
3. **15–40: build in slices.** Send one plan step per prompt, under about 50 lines of change. Read each diff aloud before you accept it.
4. **40–52: tests on the hard cases.** Ask for table-driven tests on the edge-case list. Delete the tests that check only the happy path.
5. **52–60: final pass and handoff.** Walk the solution top to bottom, name what is fragile, and ask your questions.

> [!warning] What fails the round
> Going quiet, accepting code you did not read, skipping tests, and getting stuck without asking for a hint. Re-prompting three times with different words and hoping is the debug behaviour the guide calls out by name.

The interviewer works on reliability, so the follow-ups come from that side. Mention idempotency, the choice between fail-fast and skip on a malformed record, crash recovery, and one metric while you plan. The same ideas carry the payment designs in the system design notes, so you can reuse their wording.

## The playbook

The guide is the full script, in eleven sections:

- the four scored criteria, the setup before the call, and the opening
- the 60-minute timeline and the six prompt templates
- a narration bank, the review checklist for AI output, and the debug protocol
- recovery moves, notes on the interviewer, and the questions to ask
- a practice plan of four timed mocks: CSV reconciliation, a key-value store with TTL, a bill payment scheduler, and a token-bucket rate limiter

<form class="guide-open" action="../../assets/nubank-guides/nubank-ai-coding-playbook.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-ai-coding-playbook.html" type="text/html" title="Nubank AI Coding Interview Playbook">

## Related

- [[wiki/ai-coding/index|AI-Assisted Coding]]: the area this note belongs to.
- [[wiki/system-design/nubank-study-notes|Nubank system design study notes]]: the previous round, with the idempotency and failure stories that the follow-ups reuse.
- [[wiki/go/index|Go Programming]]: the language for the round. Use the standard library only, return explicit errors, and write table-driven tests.
- [[wiki/system-design/back-of-envelope|Back-of-envelope numbers]]: for the "fits in memory, or stream it?" question during planning.
