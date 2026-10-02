---
title: "Nubank's system design round: what the web says (October 2026)"
source_type: article
source_url: https://jobs.ashbyhq.com/nubank
author: "Web research compiled by Claude for Manuel"
tags:
  - source
  - articles
  - system-design
  - nubank
  - interview
date: 2026-10-02
processed: true
compiled_to:
  - "[[wiki/system-design/nubank-study-notes]]"
---

Web research on Nubank's whiteboard system design round, done on 2 October 2026. The goal is a Lead or Senior Software Engineer interview at the new Buenos Aires hub. The question was simple: what does the round look like, and which prompts come up?

## The answer in five lines

1. **The format is stable.** One whiteboard round of about an hour, on Miro or Excalidraw, with one or two engineers. The round sits inside a five- or six-stage loop.
2. **The prompts come from Nubank's own domains.** Chargebacks is the only prompt with a dated, named candidate report. A ledger, a fraud pipeline, a credit limit or authorisation service, and payments (PIX) follow. Those mostly come from prep sites that cite nothing.
3. **Candidates and one employee call the round easy.** That points to a bar on communication and fundamentals, not on exotic architecture. At Lead level, earlier research found a rejection over scalability and performance.
4. **Buenos Aires is a development hub, not a new bank yet.** Nubank compares it to its Berlin office. So Argentine engineers will build for the existing products in Brazil, Mexico and Colombia. The interview will draw on those products.
5. **Nothing here changes the plan.** Chargebacks first, the ledger second, and the pivot guide for the rest.

## How much to trust each source

| Grade | Meaning | Examples |
|---|---|---|
| A | Nubank itself, or a first-hand report with a date | Nubank job postings, Nubank's PR statement, Blind replies from candidates and an employee |
| B | A first-hand report seen only as a title or a search snippet, because the page needs a login | The 1Point3Acres chargeback thread, Glassdoor reviews |
| C | A prep site that states prompts without citing any candidate | designgurus, techprep, finalroundai, ophyai |

Reddit, Glassdoor and 1Point3Acres block automated reading from this environment. Searches for Nubank interview threads in r/devsarg, r/brdev, r/cscareerquestions and r/ExperiencedDev returned nothing that the search engine had indexed. A manual look at r/devsarg and r/brdev may still find something.

## The format of the round

- **Whiteboard, about 60 minutes.** The architecture round "typically lasts 60 minutes" in the 1Point3Acres chargeback report (B, [1Point3Acres][p3a]). Nubank's own prep document, already decoded in this garden, gives the 60-minute split. See [[wiki/system-design/nubank-study-notes]].
- **Online whiteboard.** Prep sites agree on Miro or Excalidraw (C, [designgurus][dg], [techprep][tp]).
- **Collaborative tone.** A Glassdoor review in Portuguese says Nubank sends a technical challenge first, then schedules a design interview "numa lousa" (on a whiteboard). It names the topics to know: asynchronous communication, some key AWS services, fault-tolerance techniques, batch or stream, and sync or async (B, Glassdoor snippet, [Senior SWE, Brazil][gd-br]).
- **Another Glassdoor snippet** names three technical topics: concurrency, distributed systems and parallelism (B, [Glassdoor][gd]).

## The loop around it, 2025 to 2026

- **Recruiter screen, coding, system design, pair programming, behavioural or manager.** Prep sites describe five or six stages over five to seven weeks (C, [techprep][tp], [ophyai][oa]).
- **Senior roles add leadership rounds.** A Brazilian Glassdoor review lists a recruiter chat, a system design interview, a leadership interview, two engineering-management rounds, and the challenge presentation (B, [Glassdoor Brazil][gd-br]).
- **The take-home is changing.** A Blind reply on an IC6 thread (posted 5 July) lists "take home light coding assignment, easy system design, behavioral, then one interview discussing your take home". A second reply on the same thread says that "now take home assignment is replaced with pair programing session with AI" (A, [Blind, IC5/IC6 thread][blind-ic6]). The year of these replies is not shown. The thread appears on a company page last updated in September 2026.

## The difficulty

- **"Easy" from two directions.** The IC6 candidate above called the system design round "easy". A Nubank employee on a Blind thread about a machine learning role wrote that "the system design here it's super easy really, no need to worry" (A, [Blind, MLE thread][blind-mle], posted 25 April, year not shown).
- **The Lead bar is higher.** Earlier research in this garden recorded a Lead candidate who did not pass and reported many questions about scalability and performance. That report was not re-checked today.
- **Reading the two together.** The round is not a trick. The score comes from structure, numbers, trade-offs and failure handling, which is what Nubank's own prep document grades.

## Reported prompts

| Prompt | Evidence | Grade |
|---|---|---|
| **Chargeback ingest system.** Store transactions in CSV, send them by FTP to Mastercard, at most four files a day. | A 1Point3Acres thread titled "Nubank System Design for Chargeback Ingest System", and its search snippet ([1Point3Acres][p3a]). Earlier research in this garden found three 2026 candidates who named chargebacks. | B |
| **Ledger or double-entry system.** The ledger is the source of truth, and read models derive from it. | Prep sites ([designgurus][dg], [techprep][tp]). Earlier research in this garden also found it in candidate reports. | C, B |
| **Real-time fraud detection pipeline.** Millions of transactions a day, under 100 ms. | Prep sites ([finalroundai][fr], [techprep][tp]) | C |
| **Credit limit service** | A prep site ([techprep][tp]) | C |
| **Event sourcing for PIX payments,** with an immutable audit trail | A prep site ([finalroundai][fr]) | C |
| **Idempotent payment processing for credit card transactions** | A prep site's practice problem, presented as a candidate example without a source | C |
| **Real-time credit decision engine** | A search summary of a prep site | C |
| **Generic prompts: ride-hailing, ad-click aggregator** | Nubank's own prep document and the video it recommends. Already decoded in this garden. | A |

The prep sites were checked directly. Neither [techprep][tp] nor [finalroundai][fr] links a single first-hand report. Their specific prompts lead to their own practice pages. Treat their list as a guess about Nubank's domains, not as evidence.

## What the Buenos Aires hiring tells us

- **Two open roles, both hybrid.** A Senior Software Engineer role, posted 28 July 2026, and a Lead Software Engineer role, posted 31 August 2026. Both require two to three days a week in the Buenos Aires office (A, Nubank postings on Ashby, mirrored at [freehire, Senior][fh-sr] and [freehire, Lead][fh-lead]).
- **The Senior role.** Four or more years of experience. Distributed systems, microservices and cloud. Leading technical initiatives across teams. C1 English. Stack: Clojure, Finagle, Kafka, AWS, Kubernetes, Datomic, DynamoDB, Prometheus ([freehire, Senior][fh-sr]).
- **The Lead role.** Eight or more years of experience. Defining long-term architecture across a business area. "Mastery of distributed systems design". "Exceptional communication skills with the ability to articulate complex technical trade-offs". Observability, failure-domain isolation and disaster recovery as team practices ([freehire, Lead][fh-lead]).
- **What the hub is for.** Nubank's statement, given through its PR agency, compares the centre to its Berlin office: a place for local engineers and technology staff (A, [iupana, 30 January 2026][iupana]). The Digital Banker reads it as "a regional talent and development base rather than the launch of full retail banking operations" ([The Digital Banker, 9 February 2026][tdb]). Argentine press adds that the hub exports services to the 127 million customers in Brazil, Mexico and Colombia (search summary of [iProUP][iproup] and others).
- **The investment.** About USD 475 million over five years. The Digital Banker attaches this figure to the global office expansion. Argentine press attaches it to Argentina ([The Digital Banker][tdb], [Agroempresario][agro]).
- **A change from 2025.** A 2025 Glassdoor review said that the Buenos Aires office had stopped hiring and growing (B, search snippet, [Glassdoor Buenos Aires][gd-ba]). The 2026 postings show that this has reversed.

**The consequence for the interview.** Buenos Aires engineers will work on Nubank's existing products: cards, chargebacks, the ledger, PIX and credit. So expect a prompt from those domains, asked in English, and graded against the Lead description: trade-offs said out loud, failure domains, and observability.

## What this changes in the study plan

Nothing structural. The research confirms the order already in [[wiki/system-design/nubank-study-notes]]:

1. Chargebacks, including the batch-file variant over FTP.
2. The ledger.
3. The pivot guide for card authorisation, credit limit, fraud and PIX.
4. The two generic sketches, ride-hailing and the ad-click aggregator.

Two small additions:

- **Expect the round to feel easy, and do not relax.** Candidates who call it easy are describing the prompt, not the bar. At Lead level, the deep dives on scalability, failure and trade-offs decide the result.
- **Be ready to explain your take-home or pair-programming code** in a separate round. Reports say that this round now runs as a pair-programming session with AI.

## Sources

- [p3a]: https://www.1point3acres.com/interview/thread/1179822 — 1Point3Acres, "Nubank System Design for Chargeback Ingest System" (login required, title and snippet only)
- [gd]: https://www.glassdoor.com/Interview/Nubank-Interview-Questions-E827975.htm — Glassdoor, Nubank interviews (blocked, snippets only)
- [gd-br]: https://www.glassdoor.com.br/Entrevista/Nubank-Senior-Software-Engineer-Perguntas-entrevista-EI_IE827975.0,6_KO7,31.htm — Glassdoor Brazil, Senior Software Engineer (blocked, snippets only)
- [gd-ba]: https://www.glassdoor.sg/Location/Nubank-Brasil-Buenos-Aires-Location-EI_IE827975.0,13_IL.14,26_IC2242084.htm — Glassdoor, Buenos Aires office (blocked, snippet only)
- [blind-ic6]: https://www.teamblind.com/post/nubank-ic5ic6-staff-engineer-interview-experience-3tnxvtup — Blind, "Nubank IC5/IC6 Staff Engineer Interview Experience?"
- [blind-mle]: https://www.teamblind.com/post/nubank-mle-role-zn01luwa — Blind, "Nubank MLE role"
- [fh-sr]: https://freehire.me/jobs/senior-software-engineer-buenos-aires-argentina-hybrid-nubank-gd5oywhu — mirror of the Ashby posting, Senior Software Engineer, Buenos Aires
- [fh-lead]: https://freehire.me/jobs/lead-software-engineer-buenos-aires-argentina-hybrid-nubank-7ertai5j — mirror of the Ashby posting, Lead Software Engineer, Buenos Aires
- [iupana]: https://iupana.com/2026/01/30/nubank-quiere-entrar-argentina-probando-hub/ — iupana, 30 January 2026
- [tdb]: https://thedigitalbanker.com/nubank-confirms-argentina-presence-with-buenos-aires-hub/ — The Digital Banker, 9 February 2026
- [iproup]: https://www.iproup.com/empleo/72003-nubank-contrata-ingenieros-y-desarrolladores-argentinos-en-el-pais — iProUP (body not retrieved, search summary only)
- [agro]: https://agroempresario.com/publicacion/115205/nubank-confirma-su-regreso-a-la-argentina-en-2026-y-prepara-una-ofensiva-millonaria-contra-mercado-pago/ — Agroempresario (search summary only)
- [dg]: https://www.designgurus.io/answers/detail/what-to-expect-in-the-nubank-system-design-interview — designgurus (prep site, no citations)
- [tp]: https://www.techprep.app/blog/nubank-interview-process — techprep (prep site, checked: no first-hand citations)
- [fr]: https://www.finalroundai.com/blog/nubank-interview-process — finalroundai (prep site, checked: no first-hand citations)
- [oa]: https://ophyai.com/blog/company-guides/nubank-interview-guide — ophyai (prep site)

[p3a]: https://www.1point3acres.com/interview/thread/1179822
[gd]: https://www.glassdoor.com/Interview/Nubank-Interview-Questions-E827975.htm
[gd-br]: https://www.glassdoor.com.br/Entrevista/Nubank-Senior-Software-Engineer-Perguntas-entrevista-EI_IE827975.0,6_KO7,31.htm
[gd-ba]: https://www.glassdoor.sg/Location/Nubank-Brasil-Buenos-Aires-Location-EI_IE827975.0,13_IL.14,26_IC2242084.htm
[blind-ic6]: https://www.teamblind.com/post/nubank-ic5ic6-staff-engineer-interview-experience-3tnxvtup
[blind-mle]: https://www.teamblind.com/post/nubank-mle-role-zn01luwa
[fh-sr]: https://freehire.me/jobs/senior-software-engineer-buenos-aires-argentina-hybrid-nubank-gd5oywhu
[fh-lead]: https://freehire.me/jobs/lead-software-engineer-buenos-aires-argentina-hybrid-nubank-7ertai5j
[iupana]: https://iupana.com/2026/01/30/nubank-quiere-entrar-argentina-probando-hub/
[tdb]: https://thedigitalbanker.com/nubank-confirms-argentina-presence-with-buenos-aires-hub/
[iproup]: https://www.iproup.com/empleo/72003-nubank-contrata-ingenieros-y-desarrolladores-argentinos-en-el-pais
[agro]: https://agroempresario.com/publicacion/115205/nubank-confirma-su-regreso-a-la-argentina-en-2026-y-prepara-una-ofensiva-millonaria-contra-mercado-pago/
[dg]: https://www.designgurus.io/answers/detail/what-to-expect-in-the-nubank-system-design-interview
[tp]: https://www.techprep.app/blog/nubank-interview-process
[fr]: https://www.finalroundai.com/blog/nubank-interview-process
[oa]: https://ophyai.com/blog/company-guides/nubank-interview-guide
