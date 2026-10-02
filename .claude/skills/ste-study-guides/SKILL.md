---
name: ste-study-guides
description: |
  Simplified Technical English (ASD-STE100 Issue 9) at about 80% strictness, for study guides and explanations in Manuel's notebook. Use when writing or rewriting a study guide, interview prep material (a company's round, a mock interview, a one-card summary), or any explanation meant to be studied. Also use when asked to make text clearer, plainer, shorter or "STE", and before finishing a guide built by the digital-garden skill.
---

# Simplified Technical English for study guides

Write study material with the structural rules of ASD-STE100 Issue 9, and skip its controlled dictionary. The reader is Manuel, the night before an interview: every sentence must land on the first read. "80%" means the rules hold firmly for explanation prose and relax where the text is spoken, quoted or tabular.

The numbers in brackets are ASD-STE100 rule numbers. `references/rules.md` maps every rule in the standard to keep, relax or drop, with the reason.

## The rules

**Sentences**

1. One idea per sentence. Explanations stay at 25 words or fewer [6.3]. Steps and drills the reader performs stay at 20 [5.1]. Count each number, key, identifier, code span, quotation, name or parenthesis as one word [8.5–8.7].
2. Active voice, with the actor named: "The worker retries with the same key." Use the passive only when the actor is unknown or truly does not matter [3.6].
3. Simple tenses: present, simple past, future. "The ledger posted it" beats "the ledger has posted it". "Adjust the limit" beats "the limit must be adjusted" [3.2, 3.4].
4. A verb for the action: "before you remove the unit", not "before the removal of the unit" [3.7].
5. The imperative for what the reader does: drills, steps, what to say, what to draw. One instruction per sentence [5.2, 5.3].
6. Condition first, then a comma, then the action: "If the ledger times out, retry with the same key." [5.4]
7. Full sentences in prose. Keep the articles, and keep "that" after say, show, mean and make sure [4.2, 4.5, GR-1]. Fragments belong in tables, labels and diagram text.

**Words**

8. One term for one concept, everywhere: in the guide, its sibling guides and its condensed card [1.11, 6.2, 9.4]. Choose the term before drafting and put it in the glossary. A second name for the same thing reads as a second thing.
9. Noun stacks of three words at most. Break a longer one with "of", a verb or a relative clause [2.1, 2.2].
10. Name the referent whenever "it", "this" or "they" could point to two things. Write "this key" or "this timeout", not a bare "this" [GR-3, GR-4].
11. "For example", "that is" and "and so on", never e.g., i.e. or etc. [GR-6]
12. Field vocabulary is welcome: idempotency, outbox, sharding. Between two plain words, choose the shorter and more common one: use, about, show, need, so.

**Structure**

13. Give information gradually. Define a term before its first use, then use it [6.1].
14. One topic per paragraph, topic sentence first, six sentences at most [6.4, 6.5, 6.6]. Read alone, the topic sentences of a section outline that section.
15. Connecting words carry the logic between short sentences [4.4, 6.2]. Use and, but, so, then, thus, as a result, at the same time. Short sentences without them read like a telegram.
16. A vertical list for parallel items, for steps, and for any sentence that would carry three or more clauses [4.3].
17. Periods in prose. Semicolons stay in table cells and spoken lines [8.1].

## The other 20%: what stays outside the rules

- **Spoken lines.** "Say it" boxes, interview sentences, mock-interview dialogue, scripted answers and "never say" lists keep the rhythm of speech. Contractions, semicolons and long sentences are fine there. Mark them so that the checker skips them. In HTML, use class `say`, `cheat` or `turn`, or the attribute `data-ste="spoken"`. In markdown, use a `> [!quote]` callout.
- **Quotations** from interviewers, documents and transcripts stay word for word.
- **Code, identifiers, diagram labels and table cells.** Fragments are fine.
- **The STE dictionary.** Its approved-word list, its banned words and its one-meaning-per-word rule do not apply.
- **Contractions** are allowed. They keep the voice human and cost no clarity.

## Writing a guide

1. **Fix the terms.** List the key nouns of the subject, with one name each, in a glossary at the end of the guide. Done when each concept has exactly one name and the sibling guides use the same one.
2. **Outline with topic sentences.** Write each section heading, its one-line question, and the topic sentence of each paragraph. Done when the topic sentences alone tell the story in order.
3. **Draft gradually** under the rules. Mark each spoken line as you write it.
4. **Check.** Run the checker on every file you wrote:

   ```bash
   python3 .claude/skills/ste-study-guides/scripts/ste_check.py --list FILE...
   python3 .claude/skills/ste-study-guides/scripts/ste_check.py --terms "chosen|synonym|synonym" FILE...
   ```

   Fix each listed sentence, or keep it for a stated reason. Valid reasons: a list would read worse, or the line is speech or a quotation that the checker did not recognise. Run `--terms` for each glossary entry that has tempting synonyms. Done when every target shows PASS and every remaining flag has a reason.

The targets that define "80%":

- Prose averages 16 words or fewer per sentence.
- At most 10% of prose sentences pass 25 words.
- At most 10% of steps pass 20 words.
- No paragraph passes six sentences.
- No Latin abbreviations.
- At most 5% of prose sentences carry a semicolon.

## Rewriting an existing guide

Apply the same rules and the same check, under three constraints:

- Every number, key, identifier and claim stays exactly as it was.
- Spoken lines, quotations and diagrams stay untouched.
- Each edit is an exact-match replacement that fails loudly when its source text has moved. Afterwards, confirm that the HTML still parses and that the page renders.

Splitting sentences can push a paragraph past six sentences. Split that paragraph at its second topic.

## Before and after

From the October 2026 rewrite of the Nubank guides:

> **Before** (34 words, two clauses joined by a semicolon): Synchronous network and ledger calls hold a database transaction open across a slow external hop; a timeout leaves the case in a state that doesn't match reality, and a retry can credit twice.
>
> **After** (rules 1 and 17): Synchronous network and ledger calls hold a database transaction open across a slow external hop. A timeout leaves the case in a state that doesn't match reality. A retry can credit twice.

> **Before** (a stacked sentence): It checks that both accounts exist, the currency matches, Ana has BRL 10 available (not just posted), and her account version is the one it read.
>
> **After** (rules 13 and 16): It checks four things. Both accounts exist. The currency matches. Ana has BRL 10 available, not just posted. Her account version is the one it read.

> **Before** (two names for one thing): the method guide called the ledger's per-account row a "balance snapshot", and the ledger guide called it the "account aggregate".
>
> **After** (rule 8): "account aggregate" in both guides, confirmed with `--terms "account aggregate|balance snapshot"`.

More pairs, one for each rule, are in `references/rules.md`.
