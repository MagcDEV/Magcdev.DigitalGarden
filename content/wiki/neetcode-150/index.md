---
title: "NeetCode 150 in Go: a learning path"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - learning-path
  - patterns
  - templates
date_created: 2026-11-11
date_modified: 2026-11-11
---

# NeetCode 150 in Go: a learning path

This path solves the 150 problems of the [NeetCode 150](https://neetcode.io/practice?tab=neetcode150) list in Go. It follows the same idea as [[wiki/go/go-leetcode-learning-path|Learn Go with LeetCode]]: you memorize a small number of templates, and each problem is one more use of a template.

Each problem has the same five parts:

1. **The link to LeetCode**, so you can read the statement and submit your answer.
2. **The pattern**: the name of the technique that solves the problem.
3. **The template to memorize**: the short code shape behind the solution. The link opens the template.
4. **The idea**: the key insight in one to three sentences, with the time and the space complexity.
5. **The Go solution with comments**. The comments explain the idea and the Go. They name the moves of the template in capitals, for example GROW, SHRINK, RECORD.

> [!success] The code runs
> Work in progress: stage 1 is published, and the other stages follow. All published solutions and templates were compiled and tested on 2026-11-11 with Go 1.24.7 (`gofmt`, `go vet` and `go test`). The tests use the examples from each problem statement and edge cases. The harder problems also have a comparison with a brute-force answer on random inputs. Each solution has the function name and the signature that LeetCode gives for Go, so you can paste it there.

> [!info] If you are new to Go
> Start with [[wiki/go/go-leetcode-learning-path|Learn Go with LeetCode]]. It teaches the Go syntax stage by stage, with about 60 of these problems. Then use this path for the full list. Each stage page links to the Go syntax that it needs.

## The path on one page

| Stage | Category | Problems | Templates to memorize |
|---|---|---|---|
| 1 | [[wiki/neetcode-150/01-arrays-and-hashing\|Arrays and Hashing]] | 9 | A: Seen set; B: Count array or count map; C: Bucket by count; D: Prefix and suffix passes; E: Length prefix |

The path has 5 templates for 150 problems.

## All 150 problems

The **Go** column opens the commented solution. The **Template** column opens the template to memorize.

### Stage 1: Arrays and Hashing

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 1 | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Hash set | [[wiki/neetcode-150/01-arrays-and-hashing#Template A: Seen set\|A: Seen set]] | [[wiki/neetcode-150/01-arrays-and-hashing#217. Contains Duplicate\|solution]] |
| 2 | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Letter count | [[wiki/neetcode-150/01-arrays-and-hashing#Template B: Count array or count map\|B: Count array or count map]] | [[wiki/neetcode-150/01-arrays-and-hashing#242. Valid Anagram\|solution]] |
| 3 | [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Hash map of value to index | [[wiki/neetcode-150/01-arrays-and-hashing#Template A: Seen set\|A: Seen set]] | [[wiki/neetcode-150/01-arrays-and-hashing#1. Two Sum\|solution]] |
| 4 | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Hash map with a count key | [[wiki/neetcode-150/01-arrays-and-hashing#Template B: Count array or count map\|B: Count array or count map]] | [[wiki/neetcode-150/01-arrays-and-hashing#49. Group Anagrams\|solution]] |
| 5 | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Count map, then bucket sort | [[wiki/neetcode-150/01-arrays-and-hashing#Template C: Bucket by count\|C: Bucket by count]] | [[wiki/neetcode-150/01-arrays-and-hashing#347. Top K Frequent Elements\|solution]] |
| 6 | [271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) ([free](https://neetcode.io/problems/string-encode-and-decode)) | Medium | Length-prefix encoding | [[wiki/neetcode-150/01-arrays-and-hashing#Template E: Length prefix\|E: Length prefix]] | [[wiki/neetcode-150/01-arrays-and-hashing#271. Encode and Decode Strings\|solution]] |
| 7 | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix and suffix products | [[wiki/neetcode-150/01-arrays-and-hashing#Template D: Prefix and suffix passes\|D: Prefix and suffix passes]] | [[wiki/neetcode-150/01-arrays-and-hashing#238. Product of Array Except Self\|solution]] |
| 8 | [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | Seen sets for rows, columns and boxes | [[wiki/neetcode-150/01-arrays-and-hashing#Template A: Seen set\|A: Seen set]] | [[wiki/neetcode-150/01-arrays-and-hashing#36. Valid Sudoku\|solution]] |
| 9 | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Hash set, count from the start of each run | [[wiki/neetcode-150/01-arrays-and-hashing#Template A: Seen set\|A: Seen set]] | [[wiki/neetcode-150/01-arrays-and-hashing#128. Longest Consecutive Sequence\|solution]] |

## How to use this path

### The order

Follow the stages in order. Stage 1 to stage 7 are the base: each later stage uses them. In a stage, solve the problems in the order of the table. This order goes from the direct use of a template to the problems that combine two templates.

Two problems for each day is a good speed. That speed completes the list in about 11 weeks, with one day each week to repeat the templates.

### The loop for each stage

1. Open the stage page. Read the templates and their signals.
2. Write each template from memory in an empty file. Compile it. Compare it with the page.
3. Solve the problems of the stage with the loop below.
4. At the end of the stage, write each template one more time from memory.

### The loop for each problem

1. Open the LeetCode link. Read the problem. Name the pattern and the template before you write code.
2. Compare your guess with the **Pattern** and **Template** columns. A wrong guess is useful: read the signal of the correct template again.
3. Set a timer for 20 minutes for an easy or medium problem, and 35 minutes for a hard problem. Write the solution in Go, in your editor.
4. If you are blocked, read the idea first. Read the code only if the idea is not enough.
5. Close the page. Type the solution from memory. Do not paste it.
6. Say the idea aloud in two sentences. Then say the time and the space complexity.
7. Write the solution again after 1 day, 3 days and 7 days.

Step 5 is the most important one. To read a solution feels like progress, but only recall builds memory.

### The premium problems

Seven problems are premium on LeetCode: 271, 286, 323, 261, 269, 252 and 253. Each of them has a **free** link that opens the same problem on NeetCode. The solutions on this path use the LeetCode signature for Go.

## Signals: which stage to open

Read the problem and look for these words first.

| Signal in the problem | Pattern | Stage |
|---|---|---|
| Count, duplicate, group, find a pair in unsorted data | Hash map or hash set | [[wiki/neetcode-150/01-arrays-and-hashing\|1]] |
| Sorted input and a pair, or a palindrome | Two pointers | [[wiki/neetcode-150/02-two-pointers\|2]] |
| Longest or shortest contiguous part with a condition | Sliding window | [[wiki/neetcode-150/03-sliding-window\|3]] |
| Brackets, or the next greater or smaller item | Stack, monotonic stack | [[wiki/neetcode-150/04-stack\|4]] |
| Sorted input and O(log n), or "the minimum value that is enough" | Binary search | [[wiki/neetcode-150/05-binary-search\|5]] |
| A linked list: reverse, merge, cycle, middle | Reverse, dummy head, fast and slow | [[wiki/neetcode-150/06-linked-list\|6]] |
| Tree depth, path, validity or levels | DFS, BFS by level | [[wiki/neetcode-150/07-trees\|7]] |
| Words with a shared prefix, or a search with wildcards | Trie | [[wiki/neetcode-150/08-tries\|8]] |
| The K largest, smallest or closest, or a median of a stream | Heap | [[wiki/neetcode-150/09-heap-priority-queue\|9]] |
| All subsets, permutations, combinations or boards | Backtracking | [[wiki/neetcode-150/10-backtracking\|10]] |
| Islands, regions, connected groups, an order with dependencies | Grid DFS, BFS, topological sort, union-find | [[wiki/neetcode-150/11-graphs\|11]] |
| Shortest path with weights, or the cheapest way to connect all nodes | Dijkstra, Bellman-Ford, Prim | [[wiki/neetcode-150/12-advanced-graphs\|12]] |
| Count the ways, or the best value over choices, on one sequence | 1-D dynamic programming | [[wiki/neetcode-150/13-dp-1d\|13]] |
| The same, on two strings, a grid, or an index and a second value | 2-D dynamic programming | [[wiki/neetcode-150/14-dp-2d\|14]] |
| A local best choice that is always safe | Greedy | [[wiki/neetcode-150/15-greedy\|15]] |
| Intervals that overlap, meetings, rooms | Sort, then merge or sweep | [[wiki/neetcode-150/16-intervals\|16]] |
| A matrix to change in place, digits, powers | Math and geometry | [[wiki/neetcode-150/17-math-and-geometry\|17]] |
| "With no extra memory", single bits, XOR | Bit manipulation | [[wiki/neetcode-150/18-bit-manipulation\|18]] |

## Progress

Mark a stage when you can do the three things in the list below it.

- [ ] Stage 1: Arrays and Hashing (9)
- [ ] Stage 2: Two Pointers (5)
- [ ] Stage 3: Sliding Window (6)
- [ ] Stage 4: Stack (7)
- [ ] Stage 5: Binary Search (7)
- [ ] Stage 6: Linked List (11)
- [ ] Stage 7: Trees (15)
- [ ] Stage 8: Tries (3)
- [ ] Stage 9: Heap and Priority Queue (7)
- [ ] Stage 10: Backtracking (9)
- [ ] Stage 11: Graphs (13)
- [ ] Stage 12: Advanced Graphs (6)
- [ ] Stage 13: 1-D Dynamic Programming (12)
- [ ] Stage 14: 2-D Dynamic Programming (11)
- [ ] Stage 15: Greedy (8)
- [ ] Stage 16: Intervals (6)
- [ ] Stage 17: Math and Geometry (8)
- [ ] Stage 18: Bit Manipulation (7)

A stage is complete when these three things are true:

- You can write each template of the stage from memory in less than five minutes, and it compiles.
- You solved each problem of the stage in Go, and the hard ones a second time.
- You can say the signal, the moves and the complexity of each template aloud.

## Related

- [[wiki/go/go-leetcode-learning-path|Learn Go with LeetCode: a learning path]]: the Go syntax for each pattern, in 12 stages.
- [[wiki/go/leetcode-snippets|Go LeetCode Snippets & Templates]]: short pieces of code to copy.
- [[wiki/patterns/index|LeetCode Patterns]]: the pattern notes and the progress tracker.
- [[wiki/dsa/index|Data Structures & Algorithms]]: the theory behind each structure.
- [[wiki/go/index|Go Programming]]: the Go area of the notebook.
