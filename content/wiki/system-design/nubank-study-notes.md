---
title: "Nubank System Design Study Notes"
tags:
  - wiki
  - system-design
  - nubank
date_created: 2026-09-06
date_modified: 2026-10-02
cssclasses:
  - nubank-guides
---

Original HTML study guides for a Nubank lead system design interview, plus a timed mock round and a decoding of Nubank's own candidate prep document. The documents are embedded as-is — layout, diagrams, and wording are unchanged. Each guide follows the garden's light or dark theme and has its own toggle in the top-right corner.

Each guide also has an **Open full page** button. That loads the original HTML as a standalone document, which is the most accurate way to read it (sticky table of contents, full width, original type).

> [!tip] Reading order for the last six days
> Start with **Nubank's prep document, decoded**: it re-weights everything else. It says the round grades rough numbers that end in a decision, a visible v1 that you break yourself before v2, a named single point of failure with a degradation story, security and abuse, and polite pushback on the interviewer's suggestions. The four older guides were updated on 29 September 2026 so each of those now has a home: numbers and the v1 storyline in the chargeback guide (sections 3 and 6) and in the mock at 4:30 and 13:00; the degradation matrix and security table in the chargeback guide (section 11) and the ledger guide (section 11); schema evolution and caching in the ledger follow-ups (section 13); the ride-hailing and ad-click sketches in the pivot guide (section 6). The day-by-day plan is section 9 of the decoded document, and Friday's reading is its section 11: four Nubank posts, each with a sentence ready to cite. Then read **The Hello Interview method, applied to Nubank's hour**: Nubank's interviewers recommended that video as the way to run the round, and the guide turns its four steps into the step names you say aloud, with chargebacks and the ledger scripted minute by minute in section 7.

## Chargebacks on one card

The chargeback material condensed to what is worth memorising, in plain words and in the order you say it: the one sentence, the hour in four steps, the five questions, the numbers, the seven rules, the six nouns and three operations, the drawing with the key on every arrow, Ana's case narrated end to end on a numbered diagram, the three money endings, the failure table, the tenfold answer, rollout, and the things never to say. Four pages. Read this before the big guide, and go to the big guide only where a line here feels thin.

<form class="guide-open" action="../../assets/nubank-guides/nubank-chargeback-one-card.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-chargeback-one-card.html" type="text/html" title="Chargebacks on one card">

## The chargeback workflow, animated

Ana's R$300 dispute from section 6 of the card, played step by step on the same diagram. A dot travels each wire with the key it carries, and side panels show the case state, the money, the outbox rows, the deadline rows and the event history after every step. Pick the ending (Ana wins, loses, or wins R$200 of 300) and turn on retries to watch a lost answer and a ledger timeout resolve with the same key. Play it once before reading the card, then step through it with the arrow keys while saying each step aloud.

<form class="guide-open" action="../../assets/nubank-guides/nubank-chargeback-animated.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-chargeback-animated.html" type="text/html" title="The chargeback workflow, animated">

## The ledger on one card

The ledger guide condensed to what is worth memorising, in the same shape as the chargeback card: the one sentence, the hour in four steps, the boundary question, features, numbers and six rules, the six nouns, three operations and the table schema of the five rows written in one commit, the drawing, Ana's R$10 transfer to Bruno narrated end to end on a numbered diagram (including the cross-shard legs through clearing), the three timeouts and the one rule, the failure table, the tenfold answer, rollout, and the things never to say.

<form class="guide-open" action="../../assets/nubank-guides/nubank-ledger-one-card.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-ledger-one-card.html" type="text/html" title="The ledger on one card">

## Nubank's prep document, decoded

They sent the rubric. This guide explains every concept the candidate PDF names in plain terms, shows how each one already lives in the chargeback and ledger designs, and adds the two things those designs didn't stress: rough numbers, and a v1-then-iterate storyline. Includes the seven evaluation signals, the ten keys with a sentence for each, the arithmetic table to memorise, a graceful degradation matrix, a security and abuse table, two generic-prompt sketches, a six-day plan, the questions to ask at the end, and, in sections 11 and 12, a reading list in Nubank's own words (four engineering posts with a citation sentence each, the Datomic trade-off, the video they recommend) plus six small edges for the last days.

<form class="guide-open" action="../../assets/nubank-guides/nubank-prep-doc-decoded.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-prep-doc-decoded.html" type="text/html" title="Nubank's prep document, decoded">

## The Hello Interview method, applied to Nubank's hour

Nubank's interviewers recommended Evan King's ad-click aggregator walkthrough as the reference for how to run the round. This guide takes the road map he follows, requirements, then a bridge of entities and API (or interface and data flow for a pipeline), then a high-level design that serves only the features, then deep dives one quality at a time, and shows every move he makes in the 56 minutes and why the interviewer in him rewards it: the "below the line" list, asking scale before the qualities, the bad/good/great ladder, the planted pushback against checkpointing, the Lambda/Kappa hybrid, the bar at each level. Then it runs the same steps over the chargeback and ledger designs minute by minute, so you walk in with one method, not two. Built from the video transcript and the written answer key.

<form class="guide-open" action="../../assets/nubank-guides/nubank-hello-interview-method.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-hello-interview-method.html" type="text/html" title="The Hello Interview method, applied to Nubank's hour">

## The chargeback platform, end to end

How a multi-country card dispute platform fits together: cases, evidence, deadlines, network submissions, and the money it asks the ledger to move. Written to be understood first, then practised in the four steps of the method Nubank's interviewers recommend: requirements (sections 3 and 4, with the features, the arithmetic and the qualities), entities and API (section 5), a high-level design that starts at the rung a Lead draws, with the one-table rung named in a sentence and not drawn (section 6), and deep dives one quality at a time (sections 7 to 12, closing with the single point of failure, the degradation matrix and the security table).

<form class="guide-open" action="../../assets/nubank-guides/nubank-chargeback-study-notes.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-chargeback-study-notes.html" type="text/html" title="The chargeback platform, end to end">

## Mock interview: the chargeback platform, minute by minute

A full simulated system design round for the Nubank Lead role, with every interviewer question, every candidate answer, and what goes on the whiteboard at each step. Interruptions arrive roughly every ten minutes, the way candidates report them. Now run in the four steps of the recommended video: the road map said at minute 0, features and a below-the-line list at 3:30, the numbers and scope at 4:30, the qualities with a number each at 5:30, the entities and API at 8:00, the one-table version named in a sentence and not drawn at 13:00, the first version on the board at 16:00 with its gaps as the deep-dive menu, the candidate choosing the dives, a pushback exchange when the interviewer suggests caching the case, the single-point-of-failure and insider-abuse questions in the failures block, and the video's level bar at the end. Companion to the chargeback guide above.

<form class="guide-open" action="../../assets/nubank-guides/nubank-chargeback-mock-interview.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-chargeback-mock-interview.html" type="text/html" title="Mock interview: the chargeback platform, minute by minute">

## The ledger, end to end

How every piece of Nubank's authoritative-ledger design fits together, written to be understood first and then practised in the same four steps. Section 2 works the numbers out loud (this is the design that does outgrow one primary) and states the qualities; section 3 is the command and the API; section 4 starts the design at the rung a Lead draws; sections 8 to 11 are the deep dives, with the single point of failure and its degradation matrix in 11; section 13 adds schema evolution and what you cache versus never cache.

<form class="guide-open" action="../../assets/nubank-guides/nubank-ledger-study-notes.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-ledger-study-notes.html" type="text/html" title="The ledger, end to end">

## Pivot insurance: authoriser, credit limit, fraud, PIX, and two generic prompts

Nubank says you "design a system from scratch". The reported prompts cluster around chargebacks and the ledger, but the round also produces card authorisation, credit limits, real-time fraud and PIX. This guide gets each one to a confident step-1 sentence and a drawn first version in ten minutes of prep, by reusing the pieces you already have, in the same four steps as the other guides: requirements, entities and API (or interface and data flow for the pipeline-shaped ones), a first version with the rung below it named and not drawn, and the deep dives. Section 6 now adds the two prompts from Nubank's own PDF, ride-hailing and an ad-click aggregator, as ten-minute sketches, and the authoriser deep dive carries its latency budget in numbers.

<form class="guide-open" action="../../assets/nubank-guides/nubank-pivot-insurance-study-notes.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/nubank-guides/nubank-pivot-insurance-study-notes.html" type="text/html" title="Pivot insurance: authoriser, credit limit, fraud, PIX">
