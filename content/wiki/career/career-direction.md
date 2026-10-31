---
title: "Career Direction: Where the Pay Is (October 2026)"
tags:
  - wiki
  - career
date_created: 2026-10-31
date_modified: 2026-10-31
---

# Career direction: where the pay is (October 2026)

This note answers one question. For a senior .NET/Azure backend engineer in Argentina, which direction raises pay the most? The candidates are quant finance, applied AI, forward deployed engineering, and more of the same .NET work.

> [!abstract] The short answer
> Don't become a quant. Become a **senior backend engineer who ships AI features in financial systems**. Keep **forward deployed engineer (FDE)** as the high-pay option. Keep .NET and Azure as the base. The biggest single lever is not a new direction. It is to **pass the AI coding round** (see [[wiki/career/ai-coding-practice-plan|the practice plan]]).

## What the market says

*Research from 2026-10-27. Is the demand real, and what does it pay?*

The data has three signals. Senior roles and AI roles drive almost all new hiring. AI work pays more than plain backend work in Argentina. FDE roles grew fastest of all.

| Signal | Data | Source quality |
|---|---|---|
| Senior and AI roles drive hiring | Senior roles were 71% of the increase in US software postings (May 2025 → May 2026). AI-titled postings were 37% of the increase. Entry-level hiring collapsed. | Indeed via CNBC, cited by [Hatchworks](https://hatchworks.com/blog/gen-ai/software-engineer-shortage/) and [Talmatic](https://talmatic.com/blog/trends/software-developer-job-market-outlook/) (B) |
| AI pays more in Argentina | Senior AI/ML in Argentina: USD 85–100k/yr. Senior Go/Rust: 80–100k. React/Node full stack: 65–85k. Overall senior average: about 51–63k. | [Howdy, Aug 2026](https://www.howdy.com/blog/argentina-software-engineer-salary-hiring-cost-benchmarks-2026) (C: vendor) |
| Remote AI roles from LatAm | Senior remote AI engineers: about USD 82–120k/yr. Remote median about 96k, senior about 115k. | [RemotelyTalents](https://www.remotelytalents.com/blog/ai-engineer-salaries-2026-us-vs-europe-vs-latin-america), [Hirify](https://hirify.me/en/salaries/ai-engineering/latam), [RemoteRocketship](https://www.remoterocketship.com/country/latin-america/jobs/ai-engineer/) (C) |
| FDE boom | FDE postings up about 800–1,000% in 2026. Pay about 30–50% above backend at the same company. The median FDE spends 47% of the time with customers and 31% coding. | [Paraform](https://www.paraform.com/insights/forward-deployed-engineer-demand-quadrupled), [Perspective survey of 1,500 FDEs](https://getperspective.ai/blog/state-of-forward-deployed-engineering-2026-survey-report-1500-fdes), [Bloomberry](https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/) (C) |
| FDE in Buenos Aires | Salesforce "AI Engineer – Forward Deployed" (BA hybrid) and HappyRobot "Forward Deployed Engineer" (Argentina hybrid) were open in October 2026. | LinkedIn, 2026-10-26 (A) |
| Quant in Argentina | Almost no local quant market. Top quant pay (US base 175–250k) is at firms in the US, London and Amsterdam, and they hire on-site. | [Glassdoor BA](https://www.glassdoor.com/Salaries/buenos-aires-quantitative-analyst-salary-SRCH_IL.0,12_IM963_KO13,33.htm) (8 salaries), [Tradermath](https://www.tradermath.org/salaries/quant-developer) (C) |
| Switch to quant | Quant *developer* is the easiest path for a software engineer. It needs finance knowledge, C++ or Python, and hard algorithm interviews. Most moves to quant *researcher* need a graduate degree. A realistic timeline is 12–24 months. | [techinterview.org](https://www.techinterview.org/post/3233474730/cs-to-quant-transition-timeline/), [QuantNet](https://quantnet.com/threads/software-engineer-to-quant.53869/latest) (C, forums) |

Source quality: A = first-hand, B = reported data, C = vendor or forum.

## The options, scored

*Which direction fits a .NET/Azure backend engineer with a fintech past?*

Applied AI and FDE score best. Both pay well from Argentina, and both build on work already done. Quant pays well too, but the gap is too wide for now.

| Direction | Pay ceiling from Argentina | Fit | Time to get there | Verdict |
|---|---|---|---|---|
| **Quant developer or researcher** | High, but mostly on-site abroad | Low: no degree, no C++ or Python numerics, no derivatives experience. Economics helps a little. | 12–24+ months, with a degree filter | **No, not as the main path.** Take quant-adjacent roles (asset-management software, brokers, exchanges) when they appear. |
| **Applied AI on top of backend** (LLM features, agents, evals, in production) | USD 85–120k/yr remote | **High.** Existing AI work: an LLM metadata pipeline, orchestrated Claude Code agents, AI-readiness checks. The market now tests AI-assisted coding anyway. | 3–6 months to have proof | **Yes, the main direction.** |
| **Forward deployed engineer** | Highest: 30–50% over backend | **High.** Consulting background, C2 English, economics, and a habit of explaining trade-offs. | 3–6 months (the same proof, plus customer stories) | **Yes, the high-pay option.** |
| **Senior .NET/Azure, as now** | Lower in Argentina (most .NET jobs are at consultancies) | Exact fit | Now | **Keep it as the base.** |
| **Go or Java fintech backend** | USD 80–100k (Go) | Medium: Go is side projects only | 6–12 months | **Secondary.** Keep Go warm for interviews. Don't make it the identity. |

> [!tip] The positioning, in one line
> *Senior backend engineer (.NET/Azure) who ships AI features in financial systems.*
> This line joins the three things the market pays for (senior, AI, fintech) with what you can prove.

### What applied AI and FDE mean

An **applied AI engineer** builds product features on top of language models. The work is mostly backend work: APIs, queues, data, tests. The new parts are prompts, tool calls, retrieval and evals. An **eval** is a repeatable test of how good the model's answers are.

A **forward deployed engineer** builds the same kind of system, but inside a customer's environment. About half of the job is with the customer. So the role rewards consulting experience and clear English as much as code.

## The 90-day plan

*What do you do this quarter, in order?*

The plan has four tracks. They overlap, but the first track comes first, because it fixes the step where offers are lost.

### Weeks 1–4: fix the conversion

1. **Drill the AI coding round.** Follow [[wiki/career/ai-coding-practice-plan|the practice plan]]: three timed mocks a week, recorded, mostly in C#. A better CV does not help if the last round fails.
2. **Push for the Senior title** where you work now. The title raises the band of every later offer.
3. **Keep applying:** five to eight applications a week.

### Weeks 2–8: get AI work in production

4. Ask to work on the LLM features of your current product, or propose the next one. Good candidates: plain-language explanations of a score, LLM search over a catalog, evals for generated text. One production AI bullet on a CV is worth more than five side projects.

### Weeks 4–12: one public proof project

5. Build **one** serious project, not many. A suggestion: **an AI agent for card disputes (chargebacks), in .NET.**
   - A tool-calling agent (Anthropic or Azure OpenAI) reads a transaction history and drafts a dispute decision.
   - An idempotent API, event-driven steps on a queue, and an audit trail.
   - **Evals:** a test set with expected decisions, plus accuracy, cost and latency per case.
   - Observability: one dashboard and a log line per agent step.
   - A README with the architecture, trade-offs and numbers. Then a LinkedIn post and a note in this garden.

   This one project is proof for AI engineer, FDE and fintech backend roles at the same time.

### Ongoing: visibility

6. Post on LinkedIn once a month about real work: an architecture decision, the AI coding drill, the dispute agent.
7. Keep job alerts on for "AI Engineer" and "Forward Deployed Engineer", in Argentina and in Latin America remote.

## What not to do

- **Don't start a quant pivot now.** It costs one to two years and hits a degree filter. The best-paid quant jobs are not remote from Argentina. Come back to it only if derivatives maths becomes a passion, and then do a master's first.
- **Don't spread across Go, Java, Python and Rust.** Depth in one language (C#) plus AI beats shallow coverage.
- **Don't build five small demos.** Build one deep project with evals and numbers.

## Reading list

The books for this plan are in [[wiki/career/reading-list|the reading list]]. Read one technical book at a time, and apply it to the proof project.

## Related

- [[wiki/career/ai-coding-practice-plan|AI coding round: the practice plan]]
- [[wiki/career/questions-to-ask|Questions to ask the interviewer]]
- [[wiki/ai-coding/index|AI-Assisted Coding]]
- [[wiki/system-design/index|System Design]]
