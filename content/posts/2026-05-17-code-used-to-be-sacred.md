---
title: "Code Used to Be Sacred. Now It's Cheap."
author: "Manuel"
date: 2026-05-17
tags:
  - post
  - ai
  - software-engineering
  - career
description: "LLMs broke the foundational assumption that code is expensive. The culture our profession built around its cost is now suspect — and the bar on what makes a senior engineer just went up."
---

Every software engineer learns the same lesson early, sometimes the hard way: code is expensive.

Not in dollars — in consequences. Production code that's actually making money in the real world is dangerous. It deserves respect. You don't change it on a whim. You don't change it because you have a hunch. To touch live code you need a real reason, and even then you follow the ritual: write tests, get reviews, stage it, monitor it, roll back if anything looks off. The cost of a bug isn't measured in compile errors; it's measured in pages at 3 AM, lost revenue, and trust that takes months to rebuild.

This is why our entire profession built itself around process. RFCs before features. Two-approver code reviews. Staging environments. Feature flags. Postmortems. Senior engineers acting as gatekeepers — not because they're territorial, but because someone has to be the last line of defense between a tired junior dev and the production database. Treating code with something close to reverence wasn't paranoia. It was how the industry stayed sane.

All of that was correct. And as of about a year ago, most of it is suddenly wrong.

## What changed

LLMs broke the foundational assumption. Not because they made coding "faster" — IDEs did that, autocomplete did that, Stack Overflow did that. LLMs broke it because they can produce working code at a speed and scale that wasn't physically possible before. Not just snippets. Whole services. Whole prototypes. Whole alternative implementations of the same feature running side by side. Overnight. In a loop.

The keyword there is "working." Not "quality." Not "scalable." Not "tasteful." Working. Code that compiles, passes the tests it was given, and does the thing the prompt asked for. That's the new baseline, and the new baseline is roughly free.

This is a different magnitude of change than most engineers have processed. It's not "I can ship a feature 30% faster." It's "I can throw away ten implementations before lunch and pick the one I like." Code stops being the artifact you protect and starts being the byproduct you generate.

## The real consequences

Once code is cheap, the entire culture built around its expense becomes suspect. Not wrong — suspect. Worth re-examining.

Code review still matters, but reviewing AI-generated code is a different cognitive task than reviewing a teammate's PR. The bugs are different. The failure modes are different. Tribal knowledge about "Maria always forgets the null check" doesn't apply when the author is a stochastic process.

Refactoring stops being a major investment. You used to lobby for a two-week refactor sprint. Now you can ask for three different refactors of the same module by morning and decide which direction you actually want.

Prototyping stops being a separate phase. The thing you used to build to "see if it works" is now indistinguishable in effort from the real thing — which is dangerous, because the temptation to ship the prototype is real.

And — this is the part most people miss — the bar on what makes a senior engineer goes up, not down. When anyone can generate working code, the scarce skill is no longer writing it. It's knowing which of the ten implementations is actually correct. Which one will survive contact with scale. Which one a future engineer can read. Which one is tasteful, in the sense that good code is tasteful: simple where it can be, explicit where it must be, honest about what it's doing.

Taste, judgment, and the ability to say "throw this out and try again" are the new differentiators. Not typing speed. Not memorizing the standard library. Certainly not gatekeeping commits.

## What stays sacred

It's worth being precise about what didn't change. Production systems are still dangerous. Outages still cost money. Customers still leave when things break. The blast radius of a bad change is, if anything, larger than ever, because systems are more interconnected.

What changed is the cost of generating code, not the cost of running it. Those used to be tightly coupled — every line you wrote was a line someone had to maintain — so we treated both as expensive. Now they've decoupled. Generation is cheap. Operation is not. Maintenance is not. The consequence of being wrong is not.

This is why "code is cheap now" is not the same as "engineering is easy now." It's the opposite. The expensive part of the job — knowing what to build, judging what's good, protecting what's live — was always the hard part. We just used to be able to hide behind how long it took to type. That cover is gone.

The engineers who internalize this early are going to look like they have superpowers. The ones who keep treating code generation as the bottleneck will look, increasingly, like they're solving last year's problem with last year's tools.
