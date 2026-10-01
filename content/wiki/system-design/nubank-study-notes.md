---
title: "Nubank System Design Study Notes"
tags:
  - wiki
  - system-design
  - nubank
date_created: 2026-09-06
date_modified: 2026-10-01
cssclasses:
  - nubank-guides
---

Original HTML study guides for a Nubank lead system design interview, plus a timed mock round and a decoding of Nubank's own candidate prep document. The documents are embedded as-is — layout, diagrams, and wording are unchanged. Each guide follows the garden's light or dark theme and has its own toggle in the top-right corner.

Each guide also has an **Open full page** button. That loads the original HTML as a standalone document, which is the most accurate way to read it (sticky table of contents, full width, original type).

> [!tip] Reading order for the last six days
> Start with **Nubank's prep document, decoded**: it re-weights everything else. It says the round grades rough numbers that end in a decision, a visible v1 that you break yourself before v2, a named single point of failure with a degradation story, security and abuse, and polite pushback on the interviewer's suggestions. The four older guides were updated on 29 September 2026 so each of those now has a home: numbers and the v1 storyline in the chargeback guide (sections 3 and 6) and in the mock at 4:30 and 13:00; the degradation matrix and security table in the chargeback guide (section 11) and the ledger guide (section 11); schema evolution and caching in the ledger follow-ups (section 10); the ride-hailing and ad-click sketches in the pivot guide (section 6). The day-by-day plan is section 9 of the decoded document, and Friday's reading is its section 11: four Nubank posts, each with a sentence ready to cite.

## Nubank's prep document, decoded

They sent the rubric. This guide explains every concept the candidate PDF names in plain terms, shows how each one already lives in the chargeback and ledger designs, and adds the two things those designs didn't stress: rough numbers, and a v1-then-iterate storyline. Includes the seven evaluation signals, the ten keys with a sentence for each, the arithmetic table to memorise, a graceful degradation matrix, a security and abuse table, two generic-prompt sketches, a six-day plan, the questions to ask at the end, and, in sections 11 and 12, a reading list in Nubank's own words (four engineering posts with a citation sentence each, the Datomic trade-off, the video they recommend) plus six small edges for the last days.

<form class="guide-open" action="../../assets/nubank-guides/nubank-prep-doc-decoded.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-prep-doc-decoded.html" type="text/html" title="Nubank's prep document, decoded">

## The chargeback platform, end to end

How a multi-country card dispute platform fits together: cases, evidence, deadlines, network submissions, and the money it asks the ledger to move. Written to be understood first, then practised backwards through the seven interview stages. Now opens the architecture with a v1 sketch and its four flaws, carries the chargeback arithmetic in section 3, and closes the failures section with the single point of failure, the degradation matrix and the security table.

<form class="guide-open" action="../../assets/nubank-guides/nubank-chargeback-study-notes.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-chargeback-study-notes.html" type="text/html" title="The chargeback platform, end to end">

## Mock interview: the chargeback platform, minute by minute

A full simulated system design round for the Nubank Lead role, with every interviewer question, every candidate answer, and what goes on the whiteboard at each step. Interruptions arrive roughly every ten minutes, the way candidates report them. Now includes the numbers and scope sentence at 4:30, the v1 sketch at 13:00 before the v2 write path, a pushback exchange when the interviewer suggests caching the case, and the single-point-of-failure and insider-abuse questions in the failures block. Companion to the chargeback guide above.

<form class="guide-open" action="../../assets/nubank-guides/nubank-chargeback-mock-interview.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-chargeback-mock-interview.html" type="text/html" title="Mock interview: the chargeback platform, minute by minute">

## The ledger, end to end

How every piece of Nubank's authoritative-ledger design fits together, written to be understood first and then practised backwards through the seven interview stages. Section 11 now works the ledger numbers out loud (this is the design that does outgrow one primary) and names the single point of failure with its degradation matrix; section 10 adds schema evolution and what you cache versus never cache.

<form class="guide-open" action="../../assets/nubank-guides/nubank-ledger-study-notes.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-ledger-study-notes.html" type="text/html" title="The ledger, end to end">

## Pivot insurance: authoriser, credit limit, fraud, PIX, and two generic prompts

Nubank says you "design a system from scratch". The reported prompts cluster around chargebacks and the ledger, but the round also produces card authorisation, credit limits, real-time fraud and PIX. This guide gets each one to a confident stage-1 sentence and a drawn stage-4 diagram in ten minutes of prep, by reusing the pieces you already have. Section 6 now adds the two prompts from Nubank's own PDF, ride-hailing and an ad-click aggregator, as ten-minute sketches, and the authoriser deep dive carries its latency budget in numbers.

<form class="guide-open" action="../../assets/nubank-guides/nubank-pivot-insurance-study-notes.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-pivot-insurance-study-notes.html" type="text/html" title="Pivot insurance: authoriser, credit limit, fraud, PIX">
