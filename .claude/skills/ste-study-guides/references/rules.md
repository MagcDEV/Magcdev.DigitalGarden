# ASD-STE100 Issue 9, mapped to study guides

Each rule of the standard, in our own words, with what this notebook does with it. "Keep" means the rule applies to explanation prose. "Relax" means a softer form applies. "Drop" means the rule does not apply, with the reason.

Source: ASD-STE100 Simplified Technical English, Issue 9 (2025-01-15), Part 1, Writing rules. <https://asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf>. The standard's text and examples are not reproduced here. Every example below comes from this notebook.

## Section 1: Words

| Rule | Topic | Here | How |
|---|---|---|---|
| 1.1–1.4 | Use only dictionary words, as the listed part of speech, with the listed meaning and forms | Drop | The STE dictionary is built for maintenance manuals. It has no words for software design. Rule 12 in SKILL.md keeps the spirit: choose the shorter, more common word. |
| 1.5, 1.6 | Technical nouns may come from outside the dictionary | Keep | Field terms are welcome: idempotency key, outbox, projection, shard. |
| 1.7 | A technical noun is not a verb | Relax | Established tech verbs are fine: shard, cache, deploy. Do not coin new ones. Write "send it to the outbox", not "outbox it". |
| 1.8, 1.9 | Use the field's accepted term; prefer a short one | Keep | Use the term the interviewer and the source documents use. |
| 1.10 | No slang or regional terms as technical nouns | Keep | Write "the first version", not "the MVP-ish thing". |
| 1.11 | One technical noun per item | Keep | SKILL.md rule 8. This rule matters most in a set of sibling guides. |
| 1.12, 1.13 | Technical verbs; a technical verb is not a noun | Keep | Write "when the ledger posts", not "on ledger posting". |
| 1.14 | American spelling | Drop | The notebook keeps the spelling it already uses. Consistency inside one guide is what counts. |

## Section 2: Multi-word nouns

| Rule | Topic | Here | How |
|---|---|---|---|
| 2.1 | At most three words in a noun stack | Keep | "deadline row status" is fine. "case deadline row sweeper query index" is not. Write "the index on the sweeper's query of deadline rows". |
| 2.2 | Write a longer technical noun in full once, then shorten it or hyphenate it | Keep | "Provisional credit (the credit)" on first use, then "the credit". |

## Section 3: Verbs

| Rule | Topic | Here | How |
|---|---|---|---|
| 3.1 | Only dictionary verb forms | Drop | Follows from dropping the dictionary. |
| 3.2 | Simple tenses only: infinitive, imperative, simple present, simple past, simple future | Relax | Use these by default. The present perfect is allowed when it carries real meaning: "has the network answered yet?" |
| 3.3 | A past participle may work as an adjective | Keep | "the committed event", "a signed key". |
| 3.4 | No complex verb constructions with auxiliaries | Keep | "The worker retries", not "the call is to be retried by the worker". |
| 3.5 | The "-ing" form only inside a technical noun | Relax | "the sending service" and "retrying is safe" are fine. Avoid "-ing" openings that hide the actor: "Having committed, the service…". |
| 3.6 | Active voice. In descriptions, the passive only when the actor is unknown | Keep, slightly relaxed | Also allow the passive when the actor does not matter to the point: "the row is written in the same commit". |
| 3.7 | A verb for the action, not a noun | Keep | "Before you remove the unit", not "before the removal of the unit". "The ledger confirms", not "confirmation is given by the ledger". |

## Section 4: Sentences

| Rule | Topic | Here | How |
|---|---|---|---|
| 4.1 | Short, clear sentences | Keep | The base of everything else. |
| 4.2 | Do not drop words or contract to shorten | Relax | Keep articles and "that" in prose. Contractions are allowed. Fragments are allowed in tables, labels and diagrams. |
| 4.3 | A vertical list for complex text | Keep | Use one for any sentence with three or more parallel parts. |
| 4.4 | Connecting words between related sentences | Keep | and, but, so, then, thus, as a result, at the same time. |
| 4.5 | Use an article or "this/these" before a noun | Keep | In prose. Not in labels or table cells. |

## Section 5: Procedural writing

Procedures here are drills, practice steps, "how to run the mock", and the steps of a recovery playbook.

| Rule | Topic | Here | How |
|---|---|---|---|
| 5.1 | At most 20 words per instruction | Keep | Checked on numbered lists. |
| 5.2 | One instruction per sentence, unless the actions happen at the same time | Keep | "Set a timer. Run the mock. Name each step as you enter it." |
| 5.3 | The imperative | Keep | "Draw the commit first", not "the commit should be drawn first". |
| 5.4 | Condition first, a comma, then the instruction | Keep | "If the interviewer asks about scale, start with the arithmetic." |
| 5.5 | Notes give information, not instructions | Keep | A "trap" box explains the danger. The instruction goes in the steps. |

## Section 6: Descriptive writing

Descriptions are explanations of a design, a concept, a trade-off or a failure.

| Rule | Topic | Here | How |
|---|---|---|---|
| 6.1 | Give information gradually, one subject per sentence | Keep | Define a term before its first use. Introduce one new idea per sentence. |
| 6.2 | Key words give the text its structure, and they do not change | Keep | Repeat the same key word on purpose. Never swap it for a synonym for variety. |
| 6.3 | At most 25 words per sentence | Keep | Checked on prose. |
| 6.4 | Paragraphs group related information | Keep | |
| 6.5 | One topic per paragraph, with a topic sentence first | Keep | The topic sentences of a section, read alone, give its outline. |
| 6.6 | At most six sentences per paragraph | Keep | After splitting sentences, re-split the paragraph at its second topic. |

## Section 7: Safety instructions

| Rule | Topic | Here | How |
|---|---|---|---|
| 7.1–7.3 | Signal word, command first, then the risk | Relax | Use the same shape for interview traps: what to avoid, then why. "Never cache the case for a decision. A cached case lets two operators decide twice." |

## Section 8: Punctuation and word count

| Rule | Topic | Here | How |
|---|---|---|---|
| 8.1 | No semicolons | Relax | No semicolons in prose. Allowed in table cells and spoken lines. Target: 5% of prose sentences or fewer. |
| 8.2 | Hyphens join directly related words | Keep | "client-generated key", "cross-shard transfer". |
| 8.3 | Parentheses for references, identifiers, abbreviations, short explanations, alternatives | Keep | Keep each one short. A long aside becomes its own sentence. |
| 8.4 | In a vertical list, a colon ends a sentence for counting | Keep | |
| 8.5 | A parenthesis counts as one word | Keep | The checker counts it this way. |
| 8.6 | Numbers, units, abbreviations, identifiers, quotations, titles and names count as one word each | Keep | So `CB-812:PROVISIONAL_CREDIT:v1` counts as one word. |
| 8.7 | A hyphenated word counts as one word | Keep | |

## Section 9: Writing practices

| Rule | Topic | Here | How |
|---|---|---|---|
| 9.1 | Rebuild the sentence when a word swap is not enough | Keep | When a sentence resists shortening, change its subject or split it. Do not only delete words. |
| 9.2 | Use each word correctly | Keep | |
| 9.3 | No phrasal verbs | Relax | Common ones are fine: set up, roll back, fall back. Prefer a single verb when one exists: "remove", not "take out". |
| 9.4 | A consistent style for terms and wording | Keep | The glossary and `--terms` enforce it. |
| GR-1 | Keep "that" after verbs such as make sure, show, recommend | Keep | "Make sure that the key is stored in the same commit." |
| GR-2 | Use "with" carefully, because it can attach to more than one word | Keep | "Retry the call with the same key" is clear. "The worker with the key from the outbox" is not. |
| GR-3, GR-4 | Pronouns, and "this", must have one clear referent | Keep | Repeat the noun when two candidates exist. |
| GR-5 | False friends | Keep | When a word looks like a word in another language, check that it carries its English meaning. For example, "actual" means real, not current. |
| GR-6 | No Latin abbreviations | Keep | Write "for example", "that is", "and so on". |
| GR-7 | Inclusive language | Keep | Use they/them for a person whose pronouns are unknown. |
| GR-8 | Possessives | Keep | "The case's version" and "the version of the case" are both fine. Choose the clearer one. |

## One example per main rule

| Rule | Before | After |
|---|---|---|
| 1 Length | "Thirty thousand writes per second at peak is beyond one comfortable Postgres primary (…), so partitioning by customer is on the roadmap from day one, and the failover time of each partition is the availability ceiling." | "Thirty thousand writes per second at peak is beyond one comfortable Postgres primary. So partitioning by customer is on the roadmap from day one. The failover time of each partition is the availability ceiling." |
| 2 Active voice | "The cache is marked after the stream has been written to." | "Write to the stream first. Then mark the cache." |
| 4 Verb for the action | "The rejection of the debit happens during failover." | "During failover, the ledger rejects the debit." |
| 6 Condition first | "Retry with the same key if the call times out." | "If the call times out, retry with the same key." |
| 8 One term | "balance snapshot" in one guide, "account aggregate" in its sibling | "account aggregate" in both |
| 10 Clear referent | "The worker calls the ledger and it times out. This means unknown." | "The worker calls the ledger, and the call times out. This timeout means unknown." |
| 14 Topic sentence first | A paragraph that opens with a number and states its point in sentence four | A paragraph whose first sentence is its point. The number follows as support. |
| 15 Connecting words | "The commit succeeds. The worker publishes later. Kafka can be down." | "The commit succeeds. Then the worker publishes, so Kafka can be down without losing a fact." |
| 16 Vertical list | "It reconciles the network award, the case decision and the ledger posting, and it alerts on age and on amount." | "It reconciles three truths: the network award, the case decision, the ledger posting. It alerts on age and on amount." |
