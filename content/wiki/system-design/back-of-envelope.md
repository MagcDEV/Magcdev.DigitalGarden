---
title: "Back-of-Envelope Numbers"
tags:
  - wiki
  - system-design
  - estimation
  - interview
date_created: 2026-10-05
date_modified: 2026-10-05
---

# Back-of-envelope numbers

The interviewer gives you a few numbers, such as users, actions and rates. You turn them into requests a second, storage and people. Then you say what those figures decide. This note gives the constants, the four calculations, the thresholds that turn a number into a decision, and three worked prompts.

> [!abstract] The one rule
> Every number ends in a decision. "150,000 a day" is half an answer. "150,000 a day is under 2 writes a second, so one database is enough, and the hard part is correctness" is a full answer.

## The constants to memorise

You need only a few constants. Round them so that the mental arithmetic stays easy.

| Fact | Exact | Use |
|---|---|---|
| Seconds in a day | 86,400 | **≈ 100,000** (10⁵) |
| Seconds in a month | 2,592,000 | **≈ 2.5 million** |
| Seconds in a year | 31.5 million | **≈ 30 million** |
| 1 million a day | 11.6 a second | **≈ 12 a second** |
| 1 billion a month | 386 a second | **≈ 400 a second** |
| Peak over average | depends | **×10**, unless the interviewer gives one |

Rounding 86,400 up to 100,000 makes the result about 15% low. Say this once if the number is close to a threshold. Otherwise, ignore it.

The sizes follow the same powers of ten. A thousand bytes is a KB, a million is a MB, a billion is a GB, and a trillion is a TB. So "2 million files of 2 MB" is 4 million MB, which is 4 TB.

## How to do the arithmetic aloud

Write powers of ten, not long numbers. "3 billion times 0.15%" becomes 3 × 10⁹ × 1.5 × 10⁻³. Multiply the fronts (3 × 1.5 = 4.5) and add the exponents (9 − 3 = 6). The result is 4.5 × 10⁶, which is 4.5 million.

Turn a percentage into a fraction first:

- 1% = 1 in 100 = 10⁻²
- 0.1% = 1 in 1,000 = 10⁻³
- 0.15% = 1.5 in 1,000 = 1.5 × 10⁻³

Write each step on the board as you say it. If the interviewer follows along, they catch a mistake early. In the October 2026 mock, a misheard rate (0.5% for 0.15%) cost three corrections, because the steps were not on the board.

## The four calculations

### 1. Rate: from users to writes a second

Use this chain, and say each step:

1. Users × the share that is active × the actions each one does in a day = actions a day.
2. Actions a day ÷ 100,000 = the average a second.
3. Average × 10 = the peak a second.
4. If one action writes several rows, multiply by the rows. For example, a transfer writes two postings.

When the interviewer gives a monthly figure, divide by 2.5 million to get the average a second. Do not go through the day.

### 2. Storage: from items to bytes

Items a month × the size of one item × the months you keep it = the total.

| Item | Rough size |
|---|---|
| A small row or a JSON event | 1 KB |
| A photo or a screenshot | 1–2 MB |
| A scanned PDF | 2–10 MB |
| A minute of video | about 50 MB |

Keep the rows and the files apart. Rows go in the database. Files go in object storage, always, whatever the total.

### 3. Bandwidth: only for media

Bandwidth = requests a second × the size of one response. This calculation matters only when the system serves files, images or video. For a system of small JSON requests, skip it and say why.

### 4. People: the number that machines don't fix

Cases a day that need a human ÷ the cases one person handles in a day = the people you need. One reviewer handles about 30–60 cases a day. Use 40 if nobody gives you a figure.

People don't scale like machines. So when the people number is large, the design answer is automation, and the rollout answer is shadow mode.

## From a number to a decision

This table is the point of the whole exercise. Find the row your peak number falls in, then say its decision.

| Peak writes a second | What it decides |
|---|---|
| Under 100 | One relational database. This is not a throughput problem. Spend the design on correctness. |
| 100 to 1,000 | Still one primary. Index the hot queries. Batch where you can. |
| 1,000 to 10,000 | Close to one primary's limit. Choose the partition key now, such as the account id. |
| Over 10,000 | Partition from day one. Watch for hot keys, such as one large merchant. |

The other numbers decide other things:

| Number | Threshold | What it decides |
|---|---|---|
| Reads to writes | Over 10 to 1 | Read replicas, or a cache if a stale read is safe |
| Rows a year | A few TB | One database is still fine. Partition only for failover size. |
| Files | Any size | Object storage, with short-lived upload URLs |
| Latency budget | Under 100 ms | No cross-region call and no external call on the request path |
| People | Hundreds or more | Operations is the ceiling. Automate with policy, proven in shadow mode. |

### Reference capacities

These figures are orders of magnitude, not benchmarks. Say "roughly" when you use them.

| Thing | Rough number |
|---|---|
| One Postgres primary | Thousands of simple writes a second, tens of thousands of indexed reads, a few TB |
| One Redis node | About 100,000 simple operations a second |
| One Kafka partition | Tens of thousands of small messages a second |
| One stateless app server | 1,000 to 10,000 simple requests a second |
| Network hop | About 1 ms in one region, 50–150 ms across regions |
| Disk commit | 1–10 ms |

## Three worked prompts

### Chargebacks: a correctness problem

These are the numbers from the October 2026 mock.

| Input | Value |
|---|---|
| Card transactions | 3 billion a month |
| Disputed | 0.15% |
| Events in one case | 20, of 1 KB each |
| Files in one case | 2, of 2 MB each |
| Cases that need a human | one third |

| Step | Calculation | Result |
|---|---|---|
| Cases | 3 × 10⁹ × 1.5 × 10⁻³ | 4.5 million a month |
| A day | 4.5 million ÷ 30 | 150,000 a day |
| Average rate | 4.5 million ÷ 2.5 million | under 2 a second |
| Peak rate | × 10 | under 20 a second |
| Events | 4.5 million × 20 × 1 KB | 90 GB a month, about 1 TB a year |
| Files | 4.5 million × 2 × 2 MB | 18 TB a month |
| People | 150,000 ÷ 3 ÷ 40 | about 1,250 reviewers |

> [!quote] Say it
> "Under two writes a second, twenty at peak. One relational database handles that, and would at ten times. So this isn't a throughput problem. It's a correctness, deadline and people problem: twelve hundred reviewers today, twelve thousand at ten times. The files go in object storage, eighteen terabytes a month."

### PIX transfers: partition by account

| Input | Value |
|---|---|
| Active users | 50 million |
| Transfers per user | 30 a month |
| Postings per transfer | 2 (debit and credit) |

| Step | Calculation | Result |
|---|---|---|
| Transfers | 50 × 10⁶ × 30 | 1.5 billion a month |
| Average rate | 1.5 billion ÷ 2.5 million | 600 a second |
| Peak rate | × 10, on payday | 6,000 a second |
| Writes at peak | × 2 postings | 12,000 postings a second |

> [!quote] Say it
> "Six thousand transfers a second at peak is twelve thousand postings. That's past one primary, so I'd partition the ledger by account from day one. The hard part is a hot account, like a big merchant receiving thousands a second."

### Card authorisation: a latency problem

| Input | Value |
|---|---|
| Card transactions | 3 billion a month |
| Answer budget | about 100 ms, set by the card network |

| Step | Calculation | Result |
|---|---|---|
| Average rate | 3 billion ÷ 2.5 million | 1,200 a second |
| Peak rate | × 10, Black Friday | 12,000 a second |
| Budget | 100 ms | no cross-region hop, no slow external call |

> [!quote] Say it
> "Twelve thousand a second at peak, with a hundred milliseconds to answer. That's a throughput and latency problem, unlike chargebacks. I'd partition by account, keep the balance check in one region, and move everything that isn't the yes-or-no decision after the answer."

The same input, 3 billion card transactions a month, gives two different systems. Chargebacks take 0.15% of them over weeks. Authorisation takes all of them in 100 ms. The arithmetic shows which system you are in.

## Mistakes that cost points

- **Using numbers from memory.** The interviewer changes the inputs. Do the arithmetic again from their numbers every time.
- **Mixing a day and a month.** Write the unit after every figure: "a day", "a month", "a second".
- **Forgetting the peak.** The average is never the design number. Say the peak factor out loud.
- **Stopping at the number.** Always say the decision from the table above.
- **"We need something scalable."** Say the number and what it decides, not an adjective.

## Drill

Do each drill in 60 seconds, aloud. Say the rate, the peak, the storage or the people, and the decision.

1. 20 million users. 10% place one food order a day. Each order writes 5 rows.
2. 200 million card holders. Each gets 1 statement PDF a month, of 500 KB.
3. 5 million loan applications a month. 20% need a human. One analyst handles 25 a day.
4. A notification system sends 2 billion pushes a day.
5. 1 million drivers send a GPS point every 4 seconds while online, and half are online at peak.

> [!example]- Answers
> | # | Numbers, then the decision |
> |---|---|
> | 1 | 2 million orders a day ≈ 20 a second, 200 at peak. 1,000 row writes a second at peak. One primary, index the hot queries. |
> | 2 | 200 million × 500 KB = 100 TB a month of files. Object storage. 200 million ÷ 2.5 million ≈ 80 a second if spread over the month, so generate them in a batch. |
> | 3 | 1 million need a human each month, about 33,000 a day. ÷ 25 = about 1,300 analysts. Operations is the ceiling, so automate the clear cases. |
> | 4 | 2 billion ÷ 100,000 = 20,000 a second, 200,000 at peak. A queue partitioned across many consumers, and the push providers' rate limits become the limit. |
> | 5 | 500,000 ÷ 4 = 125,000 points a second at peak. Over 10,000: partition by region, keep only the latest point in memory, and don't write every point to the main database. |

## Related

- [[wiki/system-design/nubank-study-notes|Nubank lead system design study notes]]: the chargeback and ledger guides, where these numbers end in a design
- [[wiki/system-design/scalability|Scalability]]
- [[wiki/system-design/database-sharding|Database Sharding]]
- [[wiki/system-design/caching|Caching Strategies]]
