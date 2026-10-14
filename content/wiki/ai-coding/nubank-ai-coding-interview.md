---
title: "Nubank AI Coding Interview Playbook"
aliases:
  - "Go for the Nubank AI coding interview"
tags:
  - wiki
  - ai-coding
  - nubank
  - interview
  - go
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

## Go for the interview

The companion guide teaches enough Go to read every line that Claude Code writes, reject the wrong ones, and explain your choices. It is built around the four practice problems in the playbook. It has fifteen sections:

- reading Go in ten minutes, the project setup, and the commands to run
- errors the senior way: return, wrap with `%w`, sentinel errors, and the `run()` pattern
- money as `int64` cents, named types, time, and slices and maps without surprises
- parsing input from an `io.Reader`, table-driven tests, and an injected clock
- just enough concurrency, and the reliability patterns (idempotency, fail-fast or skip, atomic output)
- worked code for duplicate detection, the TTL store, and the token bucket
- the mistakes that give you away, and the phrases that signal seniority

> [!success] The code runs
> The worked code (parsing, duplicate detection, the TTL store and the token bucket) was compiled and run on Go 1.24 with `go vet` and `go test -race`, on 14 October 2026. Two fixes came out of that run, and the guide now shows both.

`parseCents` now rejects `""`, `".5"` and `"--5"`. Before the fix, the empty string parsed as 0 with no error. So the guide's own `"empty"` test failed.

The token bucket now clamps a negative `elapsed` to zero. Before the fix, a test with a fixed past clock drained the bucket on the first call.

<form class="guide-open" action="../../assets/nubank-guides/nubank-ai-coding-go.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-ai-coding-go.html" type="text/html" title="Go for the Nubank AI Coding Interview">

## Related

- [[wiki/ai-coding/index|AI-Assisted Coding]]: the area this note belongs to.
- [[wiki/system-design/nubank-study-notes|Nubank system design study notes]]: the previous round, with the idempotency and failure stories that the follow-ups reuse.
- [[wiki/go/index|Go Programming]]: the language for the round. The Go guide above is the interview-sized version.
- [[wiki/go/leetcode-snippets|Go LeetCode snippets]]: the idioms for maps, slices and sorting in algorithm code.
- [[wiki/system-design/back-of-envelope|Back-of-envelope numbers]]: for the "fits in memory, or stream it?" question during planning.
