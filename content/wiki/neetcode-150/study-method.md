---
title: "LeetCode study method: fewer problems, repeated"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - study-method
  - learning-path
date_created: 2026-11-11
date_modified: 2026-11-12
---

# LeetCode study method: fewer problems, repeated

This page is the method to use with [[wiki/neetcode-150/index|NeetCode 150 in Go]]. It answers one question: how do you practice so that the problems stay in memory?

Most people solve a problem one time and go to the next one. A week later the solution is gone. After 200 problems they still freeze on a new one, and they think that they are not good enough. The cause is the method, not the person.

The method on this page has three ideas:

- **Fewer problems.** 150 problems that you can solve again are worth more than 500 that you saw one time.
- **Repeats.** You solve each problem four times, with more days between the repeats.
- **Patterns.** You learn a small number of templates, and each problem is one more use of a template.

> [!info] Why this works
> Two results from the research on learning are behind this method. To recall an answer from memory teaches more than to read it again. Practice with days between the sessions teaches more than the same hours in one day.

## The seven rules

### 1. Stop after 20 minutes

Give a problem 20 minutes. Give a hard problem 35 minutes. If you are blocked at the end of that time, read the solution.

To read the solution is not a failure. The first time you see a pattern, you cannot invent it. The solution shows it to you, and the next rules make it stay.

### 2. Close the solution and type it from memory

This is the most important rule. Read the solution until you understand each line. Then close the page and type the solution in an empty file. Do not paste it, and do not look.

If you cannot type it, you did not learn it yet. Read it one more time, close it, and try again. To read a solution feels like progress, but only recall builds memory.

### 3. Repeat after 1 day, 3 days and 7 days

Solve the same problem again on three later days. The [[#The repeat schedule|repeat schedule]] below gives the dates. A problem is learned after the third clean repeat, not after the first solve.

The repeats are fast. A problem that took 40 minutes on the first day takes 10 minutes on day 3 and 5 minutes on day 7.

### 4. Work on one pattern at a time

Do not choose problems at random. Stay in one stage of the path until you recognise its problems. Then go to the next stage.

Random practice hides the patterns. Six sliding window problems in one week show you what they have in common.

### 5. Name the pattern before you write code

Read the problem and say the pattern aloud, with the reason. For example: "This is a sliding window, because the problem asks for the longest contiguous part with a condition."

Then open step 1 of the problem on the stage page, and compare. Most people fail an interview at this step, not at the code. So train this step each time. The [[wiki/neetcode-150/pattern-drill|pattern drill]] trains only this step, with ten problems in five minutes.

### 6. Write one template from memory each day

Open an empty file. Write one template of the stage in five minutes. Compile it. Compare it with the page.

The path has 95 templates, and LeetCode has thousands of problems. If the templates are automatic, your attention is free for the part of the problem that is new.

### 7. Keep a mistake list

Write each bug and each wrong pattern guess in one file. Read the file before each session. The [[#The mistake list|mistake list]] below shows the format.

After two weeks, the list shows that you make the same five mistakes. Those five mistakes are your real study plan.

## The daily hour

One hour each day is enough. One hour each day is better than six hours on Sunday, because the repeats need separate days.

| Minutes | What you do |
|---|---|
| 5 | Write one template from memory. Compile it. |
| 15 | Solve the repeats that are due today. |
| 35 | Solve one new problem with the 20-minute limit. Then type it from memory. |
| 5 | Say the idea and the complexity aloud. Update the tracker and the mistake list. |

If you have two hours, solve two new problems. If you have 20 minutes, do only the repeats. Do not skip the repeats to solve a new problem: a new problem with no repeats is lost work.

One day each week, solve no new problem. Use that day for the repeats, the templates and the mistake list.

## The loop for one new problem

1. Open the LeetCode link. Read the problem and the examples.
2. Say the pattern and the template aloud, with the reason.
3. Open **step 1** of the problem on the stage page, and compare. If your guess is wrong, read the signal of the correct template again.
4. Start the timer. Write the solution in Go, in your editor, with a test.
5. If the timer ends and you are blocked, open **step 2**, the idea. Try for five more minutes.
6. If you are still blocked, open **step 3**. Read the code and each comment.
7. Close the page. Type the solution from memory. Run the tests.
8. Say the idea in two sentences. Then say the time and the space complexity.
9. Write the date in the tracker.

> [!tip] Open the steps in order
> Each problem on a stage page hides its answer in three steps: the pattern, the idea and the Go solution. The idea is one to three sentences. Often it is enough, and then you write the code yourself. That is worth much more than a full read of the solution.

## The repeat schedule

Each problem goes through four sessions.

| Session | When | What counts as clean |
|---|---|---|
| First solve | Day 0 | You typed the solution from memory, and the tests pass. |
| Repeat 1 | Day 1 | You solved it with no look at the solution. |
| Repeat 2 | Day 3 | The same, in less time. |
| Repeat 3 | Day 7 | The same, and you can say the idea and the complexity aloud. |

If a repeat is not clean, do the first solve again and start the three repeats from that day. This is normal for about one problem in four.

After repeat 3 the problem is learned. Solve it one more time a month later, on the weekly review day.

The [[wiki/neetcode-150/repeat-tracker|repeat tracker]] has one row for each of the 150 problems. A row looks like this:

| Problem | First | +1 | +3 | +7 |
|---|---|---|---|---|
| 3. Longest Substring Without Repeating Characters | 11-12 | 11-13 | 11-15 | 11-19 |
| 76. Minimum Window Substring | 11-13 | x 11-14 | | |

The first row is learned: the **+7** cell has a date and no `x`. The second row has an `x` in the first repeat. That repeat was not clean, so the first solve starts again on 11-14.

## The mistake list

Keep one file for all your mistakes. Each mistake is one line with four parts.

| Date | Problem | What went wrong | Rule for the next time |
|---|---|---|---|
| 11-12 | 3. Longest Substring | I moved `left` one time, with an `if`. | Shrink with a `for` loop while the window is not valid. |
| 11-13 | 15. 3Sum | I guessed "hash map". The pattern was two pointers. | Sorted input, or input that I can sort, and a pair: two pointers. |
| 11-13 | 78. Subsets | All the results were the same slice. | Copy the path with `slices.Clone` before you save it. |

Write the rule as an instruction. A rule such as "be more careful" does not help. A rule such as "check `len(stack) > 0` before you read the top" helps.

Mistakes have three types. Mark each one, so you see where your time goes:

- **Pattern:** you chose the wrong template. Read the signals of the stage again.
- **Logic:** the template was correct, but an edge case failed. Add that case to your tests.
- **Go:** the idea was correct, but the syntax was wrong. Read [[wiki/go/go-leetcode-learning-path#Go mistakes that cost time in an interview|the Go mistakes table]].

## The naming drill

Use this drill on a day when you are tired, or when you have five minutes. The [[wiki/neetcode-150/pattern-drill|pattern drill]] does it for you.

1. Open the drill. Choose the stages that you studied.
2. Read each statement. Write no code.
3. Say the pattern aloud, with the reason. Then choose the family.
4. Read the signal that the drill shows after each answer.

Seven correct answers out of ten is a good result. For each wrong answer, read the signal of the correct template. This drill trains the step where people freeze.

You can also do the drill on paper. Open ten problems that you did not solve yet, and write the pattern of each one. Then compare your answers with the **Pattern** column in [[wiki/neetcode-150/index#All 150 problems|the list of all 150 problems]].

## What to expect

The progress is not constant. Know the shape, so that the slow weeks do not stop you.

| Weeks | What it feels like |
|---|---|
| 1 to 3 | Slow. You read many solutions. The repeats are hard. This is the method at work, not a sign that you fail. |
| 4 to 6 | The repeats are fast. You start to recognise the pattern of a problem that you did not see before. |
| 7 to 11 | You solve most medium problems of the early stages in the time limit. The later stages are new again, but you learn them faster. |

Easy and medium problems of stages 1 to 7 cover most of what an interview asks. Do the hard problems last, and do not measure yourself with them.

## What does not help

- **Hours on one problem.** After 20 or 35 minutes, more time gives little. The solution and the repeats give more.
- **Only new problems.** A count of solved problems is not a measure of skill. A count of learned problems is.
- **To read solutions with no retype.** It feels good, and almost nothing stays.
- **Random problems.** Stay in one stage until its signals are automatic.
- **Silent practice.** An interview is spoken. Say the idea aloud each time, also when you are alone.
- **Long sessions one time a week.** The repeats need separate days.

## Related

- [[wiki/neetcode-150/index|NeetCode 150 in Go]]: the 18 stages, with all the problems, the patterns and the templates.
- [[wiki/neetcode-150/repeat-tracker|LeetCode repeat tracker]]: one row for each problem, with the dates of the four sessions.
- [[wiki/neetcode-150/pattern-drill|LeetCode pattern drill]]: read a problem, name the pattern, see the signal.
- [[wiki/go/go-leetcode-learning-path|Learn Go with LeetCode]]: the Go syntax for each pattern.
- [[wiki/patterns/index|LeetCode Patterns]]: the pattern notes of the notebook.
