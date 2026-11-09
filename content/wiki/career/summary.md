---
title: "Career Summary: Direction, Jobs, Books and Tips"
tags:
  - wiki
  - career
date_created: 2026-10-31
date_modified: 2026-10-31
---

# Career summary: direction, jobs, books and tips

This page is the one-screen version of the career direction for a senior .NET/Azure backend engineer in Argentina. It says where to go, which jobs to chase, what to read, and how to start. The details live in [[wiki/career/career-direction|the career direction]].

> [!abstract] The direction in three lines
> 1. **Become a senior backend engineer who ships AI features in financial systems.** Keep .NET and Azure as the base.
> 2. **Chase applied AI engineer roles first, and forward deployed engineer (FDE) roles for the highest pay.** Senior .NET roles are the safe fallback.
> 3. **Fix the AI coding round before anything else.** That round is where offers are lost.

## Why this direction fits Argentina in 2026

*What does the market reward, from where you live?*

Four facts shape the plan:

- **Senior and AI roles drive hiring.** Senior roles were 71% of the rise in US software postings in the year to May 2026. AI-titled postings were 37% of the rise. Entry-level hiring collapsed.
- **US companies keep hiring in Latin America.** One 2026 report says that 98% of those engineering hires were mid-level or senior. The same report says that demand for software engineers grew 250% in 2025. The lane is also more crowded, so a clear profile matters.
- **AI work pays more.** Senior AI engineers in Argentina earn about USD 85–100k a year. A general senior backend role earns about USD 65–75k. Remote AI roles from Latin America reach about USD 82–120k.
- **Dollar pay protects you.** Peso salaries lose value fast. So most senior engineers look for USD pay, through a foreign employer, an employer of record (EOR), or a contract.

Most salary data comes from hiring vendors. So treat each number as a range, not a fact.

## The jobs to pursue

*Which titles, in which order?*

| Priority | Role | Why it fits | Search for |
|---|---|---|---|
| 1 | **Applied AI engineer** (AI product engineer) | Backend work plus LLM features, agents and evals. Most of the job is backend work. | "AI Engineer", "AI Product Engineer", "LLM Engineer", Argentina and LatAm remote |
| 2 | **Forward deployed engineer** | The highest pay: about 30–50% above backend. Consulting experience, strong English and clear trade-offs are the core of the job. | "Forward Deployed Engineer", "AI Solutions Engineer" |
| 3 | **Senior .NET/Azure backend, with AI** | The safe fit for a .NET engineer. Look for postings that add AI to .NET, for example "Senior .NET Developer – AI & Azure". | "Senior .NET", "C# Backend", "Azure" |
| 4 | **Fintech backend** (Go or Java) | A banking background helps. If Go is side-project experience only, these roles come later. | "Senior Backend", fintech names |

> [!warning] Skip for now
> **Quant roles.** The switch takes one to two years, most roles ask for a quantitative degree, and the best-paid quant jobs are on-site in the US or Europe. Take a quant-adjacent role only when one appears with a good fit.

## How to start

*What are the first moves?*

1. Read Anthropic's short essay [Building effective agents](https://www.anthropic.com/research/building-effective-agents).
2. Start *AI Engineering* by Chip Huyen: 30 minutes a day.
3. Do one AI coding mock: 60 minutes, recorded, out loud. Follow [[wiki/career/ai-coding-practice-plan|the practice plan]].
4. Do one system design a week, out loud, with fintech prompts first.
5. Start one proof project with evals. See the project ideas below.

## The books, in order

1. **AI Engineering**, Chip Huyen: the map of the field.
2. **Evals for AI Engineers**, Shreya Shankar and Hamel Husain: how to test AI systems.
3. **Designing Data-Intensive Applications, 2nd edition**, Kleppmann and Riccomini: system design and fintech backbone.
4. **LLM Engineer's Handbook**, Iusztin and Labonne: a production LLM system from end to end.

For the career side, read **The Staff Engineer's Path** (Tanya Reilly) and **Never Split the Difference** (Chris Voss). The reasons and the optional books are in [[wiki/career/reading-list|the reading list]].

## Tips

### For the AI coding round

- **The grader scores judgment, not typing speed.** Explain what you ask the AI, why you ask it, and what you check in its answer.
- **Talk all the time.** Silence reads as lost control.
- **If an approach fails, move on.** Name the trade-off out loud, then change course.
- **Ask the recruiter for the format.** Some companies allow AI tools, some forbid them, and some run pilots. Meta, Shopify, Rippling, LinkedIn and Canva have AI-assisted rounds in some loops.

### For FDE interviews

- **Expect a case study.** The signature round gives you a vague customer problem. You scope it, ask questions, and split it into steps. Many candidates fail this round, because they prepare only for algorithms.
- **Practise a customer conversation.** A strong backend engineer who freezes in front of a customer fails this job. Prepare stories from client work.
- **Some companies end with a paid trial sprint** of one to two weeks. Be ready to deliver fast in an unfamiliar codebase.

### For the portfolio

- **Ship in public.** Hiring teams value shipped projects and clear writing more than certificates.
- **Evals are the signal.** A project with a test set, accuracy, cost and latency numbers stands out from a demo.
- **One deep project beats five small ones.**

### For offers in Argentina

- **Ask about the contract at the first call:** relación de dependencia, EOR, or contractor. The contract decides the real pay.
- **Compare net pay, not gross.** Convert every offer to net USD a month before you compare it.
- **A contract role must pay much more** than a salaried role, because it carries no aguinaldo, no paid leave and no prepaga.
- **Ask whether the prepaga covers the family.**

## Ideas

### Project ideas (pick one)

- **Card-dispute agent in Go** (the main pick). A tool-calling agent drafts a chargeback decision from a transaction history. Add an idempotent API, a queue, an audit trail and an eval set.
- **An eval harness for .NET LLM apps.** A small library that runs a test set against a prompt and reports accuracy, cost and latency. It is useful to other .NET developers, so it can grow stars.
- **An MCP server for a banking-style API.** It exposes accounts and transfers as tools for an agent, with permission checks. MCP (Model Context Protocol) is the standard way to give agents tools.

### Content ideas

- "How I drill the AI coding interview": the method, the mistakes and the mock log.
- "Durable Functions orchestration: the trade-offs": from a real architecture decision.
- "Evals for a dispute agent": the numbers from the proof project.

### Network ideas

- Ask former colleagues for referrals. A referral moves a CV to the top of the pile.
- Follow AI-first companies that hire FDEs in Buenos Aires, and connect with their engineers before you apply.

## Sources

Market and pay data:

- [Howdy: Argentina salary benchmarks 2026](https://www.howdy.com/blog/argentina-software-engineer-salary-hiring-cost-benchmarks-2026)
- [La Pieza: 2026 LatAm developer salary guide](https://blog.lapieza.io/the-2026-latam-developer-salary-guide-what-us-canadian-companies-pay-to-hire-in-latin-america/)
- [Near: 2026 state of LatAm hiring report](https://lifestyle.thedam.fm/story/7597/near-releases-2026-state-of-latam-hiring-report-as-demand-for-software-engineers-surges-250/)
- [Stacker: five trends in US companies hiring in Latin America](https://stacker.com/stories/business-economy/five-trends-shaping-rise-us-companies-hiring-latin-america)
- [Remote Stack: remote jobs for Argentinians 2026](https://remotestack.in/blog/remote-jobs-for-argentinians-2026)

AI engineer path:

- [Codebasics: software engineer to AI engineer, 2026](https://codebasics.io/blog/software-engineer-to-ai-engineer-complete-roadmap-for-2026)
- [DEV: from backend engineer to AI engineer, a practical roadmap](https://dev.to/tinhtinhcd/from-backend-engineer-to-ai-engineer-a-practical-roadmap-no-hype-4kl)
- [Interview Kickstart: AI skills for backend engineers](https://interviewkickstart.com/blogs/articles/ai-skills-for-backend-engineers)

FDE interviews:

- [Harvard FAS career services: FDE interview guide 2026](https://careerservices.fas.harvard.edu/blog/2026/08/01/forward-deployed-engineer-interview-the-definitive-2026-guide-fde/)
- [Medium: the FDE interview has six rounds](https://medium.com/@shivanathd/the-forward-deployed-engineer-interview-has-six-rounds-365df0544e2c)
- [Perspective: how to hire an FDE, 2026 playbook](https://getperspective.ai/blog/how-to-hire-an-fde-the-2026-forward-deployed-engineer-hiring-playbook)

AI coding interviews:

- [interviewing.io: AI in Meta's AI-assisted coding interview](https://interviewing.io/blog/how-to-use-ai-in-meta-s-ai-assisted-coding-interview-with-real-prompts-and-examples)
- [Formation: preparing for AI-assisted technical screens](https://formation.dev/blog/the-coding-interview-is-changing-how-to-prepare-for-ai-assisted-technical-screens)
- [PracHub: AI coding interview guide](https://prachub.com/resources/ai-coding-interview-guide)

Most of these sources are vendor or prep-company content. Their numbers vary, so use them as ranges.

## Related

- [[wiki/career/career-direction|Career direction (October 2026)]]
- [[wiki/career/reading-list|Reading list]]
- [[wiki/career/ai-coding-practice-plan|AI coding round: the practice plan]]
- [[wiki/career/questions-to-ask|Questions to ask the interviewer]]
