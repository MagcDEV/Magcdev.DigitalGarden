---
title: "AI Coding Round: The Practice Plan"
tags:
  - wiki
  - career
  - ai-coding
date_created: 2026-10-31
date_modified: 2026-10-31
---

# AI coding round: the practice plan

The AI-assisted coding round is the main gap in 2026 interviews. Many senior engineers pass the recruiter screen and the system design round, and then lose the offer in the AI coding round. More companies now use this round, so it is worth four weeks of practice.

The method already exists in [[wiki/ai-coding/nubank-ai-coding-interview|the Nubank AI coding playbook]]: run sheet, cheat sheet, prompt templates and the Go guide. The gap is not knowledge. The gap is **reps under time pressure.**

## The drill

*What does one practice session look like?*

Each session copies the real round. Use these five rules every time:

1. Set a 60-minute timer.
2. Pick a problem that you have not seen.
3. Use Claude Code in the terminal.
4. Turn on screen recording.
5. Talk out loud in English for the whole hour.

## Four weeks

| Week | Sessions | Focus |
|---|---|---|
| 1 | 3 mocks | The first 10 minutes only: restate the problem, ask questions, write the plan in `NOTES.md`, agree the plan. Stop at minute 15 and review the recording. |
| 2 | 3 mocks, full hour | Test first for each step. Read every diff aloud. Reject at least one AI suggestion per session, with a reason. |
| 3 | 3 mocks, full hour, plus a change of requirements at minute 30 | Recovery: park, trade-off, move on. Integration test before minute 50. |
| 4 | 2 mocks with a human (a friend, an ex-colleague, or a paid mock on interviewing.io or Hello Interview) | The real thing: a stranger watches. |

## Problems to practise

These problems have a banking and backend flavour:

- CSV reconciliation with duplicates
- A key-value store with TTL
- A token-bucket rate limiter
- A bill-payment scheduler
- An idempotent payment API
- A ledger with balance checks
- A bank account system that grows in levels
- An LRU cache
- Order-book matching
- Event deduplication with ordering

## Which language

*Go or C#?*

Use the language whose AI output you read fastest and debug fastest. For a .NET engineer, that language is **C#**, because it is the production language. Go is side-project experience. So default to C# when the company allows any language, and do half of the mocks in C#.

## After every mock

Write three lines in the log: what went well, where the time went, and one change for next time.

| Date | Problem | Lang | Finished? | Tests? | Time sink | One change |
|---|---|---|---|---|---|---|

## The other rounds

- **System design:** keep it warm, but don't over-invest. Do one design a week from [[wiki/system-design/index|the system design notes]], out loud, in 45 minutes. Start with fintech prompts: ledger, payments with idempotency, chargebacks, fraud pipeline, card authorisation, rate limiter, notifications.
- **Classic live coding:** two LeetCode mediums a week from [[wiki/patterns/index|the patterns]], in the interview language, explained out loud.
- **Behavioural and Lead signals:** Lead roles score trade-offs, influence across teams, and owning failures. Each story needs a number and a "what I'd do differently".

## Related

- [[wiki/career/career-direction|Career direction]]
- [[wiki/ai-coding/index|AI-Assisted Coding]]
