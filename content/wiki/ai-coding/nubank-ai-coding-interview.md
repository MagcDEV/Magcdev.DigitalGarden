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
date_modified: 2026-10-19
cssclasses:
  - nubank-guides
---

This is the playbook for Nubank's AI coding round. You get sixty minutes in a browser VS Code, with Claude Code in the terminal. The interviewer watches how you think. The round comes after the [[wiki/system-design/nubank-study-notes|system design round]]. The guide is embedded as-is. It follows the garden's light or dark theme and has its own toggle in the top-right corner.

The **Open full page** button loads the guide as a standalone document. Keep that version on your phone during the call. The shared screen shows only the editor and `NOTES.md`.

> [!abstract] The one idea
> They do not grade the program. They grade the engineer who directed it. Each move in the playbook maps to one of four criteria: decomposition, AI steering, readable code, and communication.

> [!tip] What to reread 20 minutes before the call
> Read the run sheet below once, top to bottom. Then, in the playbook, section 0 is what the panel asked for. Section 3 is the opening script. Section 5 has the prompt templates, in test-first order. Section 8 is the debug protocol: read the error aloud, state a hypothesis, verify it, then fix.

## The cheat sheet, for a second screen

Everything to remember, on one dense page, in cards that fill the width of a landscape screen. It holds the hour with its times, the key lines, the ten parts of the plan, the five failure modes and every prompt. It also has the `NOTES.md` shorthand, the diff checks, the debug order, tests and Go idioms. The last cards are the glossary, the rescue moves, the likely banking problem and the close. Keep it off the screen that you share. Glance at it, and don't read from it.

<form class="guide-open" action="../../assets/nubank-guides/nubank-ai-coding-cheat-sheet.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-ai-coding-cheat-sheet.html" type="text/html" title="Nubank AI Coding: cheat sheet">

## What the panel asked for

Ahead of the session, Nubank's recruiter sent six recommendations on top of the preparation guide. Section 0 of the playbook holds them, and the rest of the playbook now follows them.

1. **Decompose before you prompt.** Agree the breakdown with the interviewer before Claude Code writes a line. Ask for a minute of silence if you need it.
2. **Bring the tests yourself.** Name TDD and do it: the test first, then the code. Add at least one integration test without being asked. Say what each test protects against.
3. **Steer, don't follow.** Read every output. Reject buggy or overcomplicated code out loud, with the reason.
4. **Raise failure modes unprompted.** Name concurrency, retries and idempotency, error handling, and resource limits. Then name one log line and one metric for production.
5. **Structure over volume.** A small, tested, well-layered solution beats a large one. Not finishing in 60 minutes is not penalised.
6. **Narrate and manage the clock.** If one piece eats the session, name the trade-off, park it, and move on.

They also recommend the video *AI Coding Interview w/ Meta* as a picture of the session. Any language is fine, and the environment is ready at the start of the call.

## How the hour runs

1. **0–10: understand and plan.** Write no code. Ask 3–4 clarifying questions, type a plan of 3–5 testable steps, and list the edge cases. Name the failure modes, let Claude Code look for gaps, then agree the breakdown.
2. **10–15: brief Claude Code.** Send the kickoff prompt, read its plan aloud, then say "go". Only the skeleton and a failing test land.
3. **15–40: build in slices, test first.** For each step, get the failing test first, then the code that makes it pass. Read each diff aloud.
4. **40–52: integration test and the hard cases.** Add one integration test through the entry point. Then cover each edge case still without a test.
5. **52–60: final pass and handoff.** Walk the solution top to bottom, name what is fragile and how you'd observe it, and ask your questions.

> [!warning] What fails the round
> Prompting before the problem is scoped, going quiet, accepting code you did not read, skipping tests, and getting stuck without asking for a hint. Re-prompting three times with different words and hoping is the debug behaviour the guide calls out by name.

The interviewer works on reliability, so the follow-ups come from that side. Mention concurrency, idempotency, the choice between fail-fast and skip on a malformed record, and resource limits while you plan. Close with one log line and one metric. The same ideas carry the payment designs in the system design notes, so you can reuse their wording.

## The run sheet, step by step

The run sheet turns the playbook into 39 numbered actions, from joining the call to your last question. Each step says what to open, type, prompt, run and say, and when the step is done. Tags on each step name the scored point that it shows. A table at the end maps every scored point to its steps, so a practice run can check that it covered each one.

> [!tip] The plan is yours, and Claude Code is the scribe
> Claude Code types the empty `NOTES.md` headings, and later it looks for gaps in your plan. It never writes the plan. You type the decisions in shorthand while you talk. Then you accept, reject or park each of its suggestions out loud, with a reason.

Three sections after the steps help you remember and say it:

- **The memory list.** The five failure modes, remembered as "Can Retries Ever Lose Orders?" (concurrency, retries, errors, limits, observability). Each one has what it is, the question to ask, the fix, a line to say, and what it means in six likely problems. A glossary explains every term, such as fail fast, idempotent and race condition. A worked box explains the integration test.
- **Owning the plan.** A ten-part formula to say in order, from "restate it" and "one example by hand" to "what could go wrong" and "agree". It also has the lines for each AI moment and the lines that give the plan away.
- **Five scenarios.** Each one shows the full scope phase, typed and said. They cover a banking system that grows in levels, a key-value store with expiry and existing code with a bug. The last two are a new requirement at minute 30 and a vague prompt.

The phases follow the clock:

- **0:00–0:02, orient.** Hands off the keyboard, say the opening line, and ask for a minute to read.
- **0:02–0:10, scope in `NOTES.md`.** Let Claude Code type the empty headings. Then type the problem, questions, assumptions, plan, layout, edge cases and the five failure modes yourself. Ask Claude Code for gaps, decide on each one out loud, and get the breakdown agreed.
- **0:10–0:15, brief Claude Code.** Send the kickoff prompt, correct its plan, and get a skeleton with one failing test.
- **0:15–0:40, the test-first loop.** For each plan step, announce the cases, get the test, read it, and see red. Then get the code, review the diff with six checks, see green, and tick the step with the time.
- **0:40–0:52, integration test and edge cases.** Write the integration test without being asked, then fill the edge-case gaps and run the full check.
- **0:52–1:00, review and handoff.** Get a read-only review, walk the code, say the logs and metrics for production, name what is not done, and ask your questions.

<form class="guide-open" action="../../assets/nubank-guides/nubank-ai-coding-run-sheet.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-ai-coding-run-sheet.html" type="text/html" title="Nubank AI Coding Interview: the run sheet">

## The playbook

The guide is the full script, in twelve sections:

- the panel's six asks, and the five failure modes to name before anyone asks
- the four scored criteria, the setup before the call, and the opening
- the 60-minute timeline and the test-first prompt templates
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
- worked code for duplicate detection with its integration test, the TTL store, and the token bucket
- the mistakes that give you away, and the phrases that signal seniority

> [!success] The code runs
> The worked code (parsing, duplicate detection, the integration test, the TTL store and the token bucket) was compiled and run on Go 1.24 with `go vet` and `go test -race`, on 14 and 16 October 2026. Two fixes came out of that run, and the guide now shows both.

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
