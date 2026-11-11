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
> All 150 solutions and all the templates were compiled and tested on 2026-11-11 with Go 1.24.7 (`gofmt`, `go vet` and `go test`). The tests use the examples from each problem statement and edge cases. The harder problems also have a comparison with a brute-force answer on random inputs. Each solution has the function name and the signature that LeetCode gives for Go, so you can paste it there.

> [!info] If you are new to Go
> Start with [[wiki/go/go-leetcode-learning-path|Learn Go with LeetCode]]. It teaches the Go syntax stage by stage, with about 60 of these problems. Then use this path for the full list. Each stage page links to the Go syntax that it needs.

## The path on one page

| Stage | Category | Problems | Templates to memorize |
|---|---|---|---|
| 1 | [[wiki/neetcode-150/01-arrays-and-hashing\|Arrays and Hashing]] | 9 | A: Seen set; B: Count array or count map; C: Bucket by count; D: Prefix and suffix passes; E: Length prefix |
| 2 | [[wiki/neetcode-150/02-two-pointers\|Two Pointers]] | 5 | A: Converging pointers; B: Sort, fix one, converge; C: Two pointers with a running maximum |
| 3 | [[wiki/neetcode-150/03-sliding-window\|Sliding Window]] | 6 | A: Best so far in one pass; B: Variable window, longest; C: Fixed window; D: Shortest window with a need counter; E: Monotonic deque |
| 4 | [[wiki/neetcode-150/04-stack\|Stack]] | 7 | A: Matching stack; B: Paired stack; C: Stack as evaluator; D: Backtracking with counters; E: Monotonic stack |
| 5 | [[wiki/neetcode-150/05-binary-search\|Binary Search]] | 7 | A: Exact value; B: First true; C: Rotated sorted slice; D: Partition of two sorted slices |
| 6 | [[wiki/neetcode-150/06-linked-list\|Linked List]] | 11 | A: Reverse a list; B: Dummy head; C: Fast and slow pointers; D: Hash map plus doubly linked list; E: Heap of nodes; F: Map from old node to new node |
| 7 | [[wiki/neetcode-150/07-trees\|Trees]] | 15 | A: DFS that returns a value; B: DFS that returns one value and records another; C: DFS that passes state down; D: BFS by level; E: BST walk that uses the order; F: Preorder build with a cursor |
| 8 | [[wiki/neetcode-150/08-tries\|Tries]] | 3 | A: Trie node, insert and walk; B: DFS on the trie for wildcards; C: Trie plus grid backtracking |
| 9 | [[wiki/neetcode-150/09-heap-priority-queue\|Heap and Priority Queue]] | 7 | A: The five heap methods; B: Heap of size K; C: Max-heap by a different Less; D: Two heaps for the median; E: Max-heap plus cooldown queue; F: K-way merge with a heap |
| 10 | [[wiki/neetcode-150/10-backtracking\|Backtracking]] | 9 | A: Choose, explore, undo with a start index; B: Skip duplicates after a sort; C: Permutations with a used slice; D: Grid path with mark and unmark; E: Cut a string into parts; F: One choice for each position, with sets |
| 11 | [[wiki/neetcode-150/11-graphs\|Graphs]] | 13 | A: Grid DFS (flood fill); B: BFS by level from many sources; C: Clone with a map; D: Topological sort; E: Union-find; F: BFS on an implicit graph |
| 12 | [[wiki/neetcode-150/12-advanced-graphs\|Advanced Graphs]] | 6 | A: Dijkstra with a heap; B: Prim with a heap; C: Bellman-Ford with a round limit; D: Hierholzer's algorithm; E: Topological sort from comparisons; F: Min-heap of items |
| 13 | [[wiki/neetcode-150/13-dp-1d\|1-D Dynamic Programming]] | 12 | A: Two variables; B: Table over a prefix or an amount; C: Best that ends at i; D: 0/1 knapsack on a boolean row; E: Expand from the centre |
| 14 | [[wiki/neetcode-150/14-dp-2d\|2-D Dynamic Programming]] | 11 | A: Grid paths; B: Two strings table; C: Knapsack count on one row; D: State machine by day; E: Interval DP; F: DFS with memo on a grid |
| 15 | [[wiki/neetcode-150/15-greedy\|Greedy]] | 8 | A: Running sum with a reset; B: Farthest reach; C: Sort, then take the smallest first; D: Filter, then combine; E: Last index, then extend the end; F: Range of possible counts |
| 16 | [[wiki/neetcode-150/16-intervals\|Intervals]] | 6 | A: Sort by start, then merge; B: Three-phase insert; C: Sort by end, then greedy keep; D: Sweep of sorted starts and ends; E: Offline queries with a sort and a min-heap |
| 17 | [[wiki/neetcode-150/17-math-and-geometry\|Math and Geometry]] | 8 | A: Transpose, then reverse; B: Four boundaries that shrink; C: Markers in the first row and column; D: Digit loop with a carry; E: Fast power by squaring; F: Count map of points |
| 18 | [[wiki/neetcode-150/18-bit-manipulation\|Bit Manipulation]] | 7 | A: XOR cancels pairs; B: Remove the lowest set bit; C: DP on bits; D: Shift in and shift out; E: Add with XOR and carry; F: Digit loop with an overflow check |

The path has 95 templates for 150 problems.

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

### Stage 2: Two Pointers

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 10 | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Converging pointers | [[wiki/neetcode-150/02-two-pointers#Template A: Converging pointers\|A: Converging pointers]] | [[wiki/neetcode-150/02-two-pointers#125. Valid Palindrome\|solution]] |
| 11 | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | Converging pointers | [[wiki/neetcode-150/02-two-pointers#Template A: Converging pointers\|A: Converging pointers]] | [[wiki/neetcode-150/02-two-pointers#167. Two Sum II - Input Array Is Sorted\|solution]] |
| 12 | [15. 3Sum](https://leetcode.com/problems/3sum/) | Medium | Sort, then converging pointers | [[wiki/neetcode-150/02-two-pointers#Template B: Sort, fix one, converge\|B: Sort, fix one, converge]] | [[wiki/neetcode-150/02-two-pointers#15. 3Sum\|solution]] |
| 13 | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Converging pointers | [[wiki/neetcode-150/02-two-pointers#Template A: Converging pointers\|A: Converging pointers]] | [[wiki/neetcode-150/02-two-pointers#11. Container With Most Water\|solution]] |
| 14 | [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | Two pointers with running maximums | [[wiki/neetcode-150/02-two-pointers#Template C: Two pointers with a running maximum\|C: Two pointers with a running maximum]] | [[wiki/neetcode-150/02-two-pointers#42. Trapping Rain Water\|solution]] |

### Stage 3: Sliding Window

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 15 | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Best so far, one pass | [[wiki/neetcode-150/03-sliding-window#Template A: Best so far in one pass\|A: Best so far in one pass]] | [[wiki/neetcode-150/03-sliding-window#121. Best Time to Buy and Sell Stock\|solution]] |
| 16 | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Variable window, longest | [[wiki/neetcode-150/03-sliding-window#Template B: Variable window, longest\|B: Variable window, longest]] | [[wiki/neetcode-150/03-sliding-window#3. Longest Substring Without Repeating Characters\|solution]] |
| 17 | [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Variable window, longest | [[wiki/neetcode-150/03-sliding-window#Template B: Variable window, longest\|B: Variable window, longest]] | [[wiki/neetcode-150/03-sliding-window#424. Longest Repeating Character Replacement\|solution]] |
| 18 | [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | Fixed window with letter counts | [[wiki/neetcode-150/03-sliding-window#Template C: Fixed window\|C: Fixed window]] | [[wiki/neetcode-150/03-sliding-window#567. Permutation in String\|solution]] |
| 19 | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Shortest window with a need counter | [[wiki/neetcode-150/03-sliding-window#Template D: Shortest window with a need counter\|D: Shortest window with a need counter]] | [[wiki/neetcode-150/03-sliding-window#76. Minimum Window Substring\|solution]] |
| 20 | [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Monotonic deque | [[wiki/neetcode-150/03-sliding-window#Template E: Monotonic deque\|E: Monotonic deque]] | [[wiki/neetcode-150/03-sliding-window#239. Sliding Window Maximum\|solution]] |

### Stage 4: Stack

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 21 | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Matching stack | [[wiki/neetcode-150/04-stack#Template A: Matching stack\|A: Matching stack]] | [[wiki/neetcode-150/04-stack#20. Valid Parentheses\|solution]] |
| 22 | [155. Min Stack](https://leetcode.com/problems/min-stack/) | Medium | Paired stack | [[wiki/neetcode-150/04-stack#Template B: Paired stack\|B: Paired stack]] | [[wiki/neetcode-150/04-stack#155. Min Stack\|solution]] |
| 23 | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Stack as evaluator | [[wiki/neetcode-150/04-stack#Template C: Stack as evaluator\|C: Stack as evaluator]] | [[wiki/neetcode-150/04-stack#150. Evaluate Reverse Polish Notation\|solution]] |
| 24 | [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | Backtracking with counters | [[wiki/neetcode-150/04-stack#Template D: Backtracking with counters\|D: Backtracking with counters]] | [[wiki/neetcode-150/04-stack#22. Generate Parentheses\|solution]] |
| 25 | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Monotonic stack | [[wiki/neetcode-150/04-stack#Template E: Monotonic stack\|E: Monotonic stack]] | [[wiki/neetcode-150/04-stack#739. Daily Temperatures\|solution]] |
| 26 | [853. Car Fleet](https://leetcode.com/problems/car-fleet/) | Medium | Sort, then monotonic stack | [[wiki/neetcode-150/04-stack#Template E: Monotonic stack\|E: Monotonic stack]] | [[wiki/neetcode-150/04-stack#853. Car Fleet\|solution]] |
| 27 | [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Monotonic stack | [[wiki/neetcode-150/04-stack#Template E: Monotonic stack\|E: Monotonic stack]] | [[wiki/neetcode-150/04-stack#84. Largest Rectangle in Histogram\|solution]] |

### Stage 5: Binary Search

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 28 | [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Binary search, exact value | [[wiki/neetcode-150/05-binary-search#Template A: Exact value\|A: Exact value]] | [[wiki/neetcode-150/05-binary-search#704. Binary Search\|solution]] |
| 29 | [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | Binary search, exact value | [[wiki/neetcode-150/05-binary-search#Template A: Exact value\|A: Exact value]] | [[wiki/neetcode-150/05-binary-search#74. Search a 2D Matrix\|solution]] |
| 30 | [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Binary search on the answer | [[wiki/neetcode-150/05-binary-search#Template B: First true\|B: First true]] | [[wiki/neetcode-150/05-binary-search#875. Koko Eating Bananas\|solution]] |
| 31 | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | First true on a rotated slice | [[wiki/neetcode-150/05-binary-search#Template B: First true\|B: First true]] | [[wiki/neetcode-150/05-binary-search#153. Find Minimum in Rotated Sorted Array\|solution]] |
| 32 | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Binary search on a rotated slice | [[wiki/neetcode-150/05-binary-search#Template C: Rotated sorted slice\|C: Rotated sorted slice]] | [[wiki/neetcode-150/05-binary-search#33. Search in Rotated Sorted Array\|solution]] |
| 33 | [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | Map of sorted slices, first true | [[wiki/neetcode-150/05-binary-search#Template B: First true\|B: First true]] | [[wiki/neetcode-150/05-binary-search#981. Time Based Key-Value Store\|solution]] |
| 34 | [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | Binary search on a partition | [[wiki/neetcode-150/05-binary-search#Template D: Partition of two sorted slices\|D: Partition of two sorted slices]] | [[wiki/neetcode-150/05-binary-search#4. Median of Two Sorted Arrays\|solution]] |

### Stage 6: Linked List

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 35 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Reverse the pointers in place | [[wiki/neetcode-150/06-linked-list#Template A: Reverse a list\|A: Reverse a list]] | [[wiki/neetcode-150/06-linked-list#206. Reverse Linked List\|solution]] |
| 36 | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Dummy head and merge | [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]] | [[wiki/neetcode-150/06-linked-list#21. Merge Two Sorted Lists\|solution]] |
| 37 | [143. Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Middle, reverse, then weave | [[wiki/neetcode-150/06-linked-list#Template C: Fast and slow pointers\|C: Fast and slow pointers]], [[wiki/neetcode-150/06-linked-list#Template A: Reverse a list\|A: Reverse a list]] | [[wiki/neetcode-150/06-linked-list#143. Reorder List\|solution]] |
| 38 | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Dummy head, two pointers with a gap | [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]], [[wiki/neetcode-150/06-linked-list#Template C: Fast and slow pointers\|C: Fast and slow pointers]] | [[wiki/neetcode-150/06-linked-list#19. Remove Nth Node From End of List\|solution]] |
| 39 | [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | Hash map from old node to copy | [[wiki/neetcode-150/06-linked-list#Template F: Map from old node to new node\|F: Map from old node to new node]] | [[wiki/neetcode-150/06-linked-list#138. Copy List with Random Pointer\|solution]] |
| 40 | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | Dummy head with a carry | [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]] | [[wiki/neetcode-150/06-linked-list#2. Add Two Numbers\|solution]] |
| 41 | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Fast and slow pointers | [[wiki/neetcode-150/06-linked-list#Template C: Fast and slow pointers\|C: Fast and slow pointers]] | [[wiki/neetcode-150/06-linked-list#141. Linked List Cycle\|solution]] |
| 42 | [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | Floyd's cycle start on indexes | [[wiki/neetcode-150/06-linked-list#Template C: Fast and slow pointers\|C: Fast and slow pointers]] | [[wiki/neetcode-150/06-linked-list#287. Find the Duplicate Number\|solution]] |
| 43 | [146. LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | Hash map plus doubly linked list | [[wiki/neetcode-150/06-linked-list#Template D: Hash map plus doubly linked list\|D: Hash map plus doubly linked list]] | [[wiki/neetcode-150/06-linked-list#146. LRU Cache\|solution]] |
| 44 | [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Min-heap of list heads | [[wiki/neetcode-150/06-linked-list#Template E: Heap of nodes\|E: Heap of nodes]], [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]] | [[wiki/neetcode-150/06-linked-list#23. Merge k Sorted Lists\|solution]] |
| 45 | [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | Reverse one group at a time | [[wiki/neetcode-150/06-linked-list#Template A: Reverse a list\|A: Reverse a list]], [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]] | [[wiki/neetcode-150/06-linked-list#25. Reverse Nodes in k-Group\|solution]] |

### Stage 7: Trees

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 46 | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Recursive DFS, swap the children | [[wiki/neetcode-150/07-trees#Template A: DFS that returns a value\|A: DFS that returns a value]] | [[wiki/neetcode-150/07-trees#226. Invert Binary Tree\|solution]] |
| 47 | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Recursive DFS that returns the height | [[wiki/neetcode-150/07-trees#Template A: DFS that returns a value\|A: DFS that returns a value]] | [[wiki/neetcode-150/07-trees#104. Maximum Depth of Binary Tree\|solution]] |
| 48 | [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | DFS returns the height, records the diameter | [[wiki/neetcode-150/07-trees#Template B: DFS that returns one value and records another\|B: DFS that returns one value and records another]] | [[wiki/neetcode-150/07-trees#543. Diameter of Binary Tree\|solution]] |
| 49 | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | DFS returns the height, records the balance | [[wiki/neetcode-150/07-trees#Template B: DFS that returns one value and records another\|B: DFS that returns one value and records another]] | [[wiki/neetcode-150/07-trees#110. Balanced Binary Tree\|solution]] |
| 50 | [100. Same Tree](https://leetcode.com/problems/same-tree/) | Easy | Recursive DFS on two trees | [[wiki/neetcode-150/07-trees#Template A: DFS that returns a value\|A: DFS that returns a value]] | [[wiki/neetcode-150/07-trees#100. Same Tree\|solution]] |
| 51 | [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy | DFS with a same-tree test | [[wiki/neetcode-150/07-trees#Template A: DFS that returns a value\|A: DFS that returns a value]] | [[wiki/neetcode-150/07-trees#572. Subtree of Another Tree\|solution]] |
| 52 | [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | BST walk to the split point | [[wiki/neetcode-150/07-trees#Template E: BST walk that uses the order\|E: BST walk that uses the order]] | [[wiki/neetcode-150/07-trees#235. Lowest Common Ancestor of a Binary Search Tree\|solution]] |
| 53 | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS by level | [[wiki/neetcode-150/07-trees#Template D: BFS by level\|D: BFS by level]] | [[wiki/neetcode-150/07-trees#102. Binary Tree Level Order Traversal\|solution]] |
| 54 | [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | BFS by level, keep the last node | [[wiki/neetcode-150/07-trees#Template D: BFS by level\|D: BFS by level]] | [[wiki/neetcode-150/07-trees#199. Binary Tree Right Side View\|solution]] |
| 55 | [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium | DFS that passes the path maximum down | [[wiki/neetcode-150/07-trees#Template C: DFS that passes state down\|C: DFS that passes state down]] | [[wiki/neetcode-150/07-trees#1448. Count Good Nodes in Binary Tree\|solution]] |
| 56 | [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | DFS that passes the limits down | [[wiki/neetcode-150/07-trees#Template C: DFS that passes state down\|C: DFS that passes state down]] | [[wiki/neetcode-150/07-trees#98. Validate Binary Search Tree\|solution]] |
| 57 | [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | Inorder walk of a BST with a stack | [[wiki/neetcode-150/07-trees#Template E: BST walk that uses the order\|E: BST walk that uses the order]] | [[wiki/neetcode-150/07-trees#230. Kth Smallest Element in a BST\|solution]] |
| 58 | [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | Preorder cursor plus inorder index map | [[wiki/neetcode-150/07-trees#Template F: Preorder build with a cursor\|F: Preorder build with a cursor]] | [[wiki/neetcode-150/07-trees#105. Construct Binary Tree from Preorder and Inorder Traversal\|solution]] |
| 59 | [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | DFS returns one branch, records the full path | [[wiki/neetcode-150/07-trees#Template B: DFS that returns one value and records another\|B: DFS that returns one value and records another]] | [[wiki/neetcode-150/07-trees#124. Binary Tree Maximum Path Sum\|solution]] |
| 60 | [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | Preorder DFS with null markers | [[wiki/neetcode-150/07-trees#Template F: Preorder build with a cursor\|F: Preorder build with a cursor]] | [[wiki/neetcode-150/07-trees#297. Serialize and Deserialize Binary Tree\|solution]] |

### Stage 8: Tries

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 61 | [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Trie (prefix tree) | [[wiki/neetcode-150/08-tries#Template A: Trie node, insert and walk\|A: Trie node, insert and walk]] | [[wiki/neetcode-150/08-tries#208. Implement Trie (Prefix Tree)\|solution]] |
| 62 | [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Trie with wildcard DFS | [[wiki/neetcode-150/08-tries#Template A: Trie node, insert and walk\|A: Trie node, insert and walk]], [[wiki/neetcode-150/08-tries#Template B: DFS on the trie for wildcards\|B: DFS on the trie for wildcards]] | [[wiki/neetcode-150/08-tries#211. Design Add and Search Words Data Structure\|solution]] |
| 63 | [212. Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Trie plus grid backtracking | [[wiki/neetcode-150/08-tries#Template A: Trie node, insert and walk\|A: Trie node, insert and walk]], [[wiki/neetcode-150/08-tries#Template C: Trie plus grid backtracking\|C: Trie plus grid backtracking]] | [[wiki/neetcode-150/08-tries#212. Word Search II\|solution]] |

### Stage 9: Heap and Priority Queue

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 64 | [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | Min-heap of size K | [[wiki/neetcode-150/09-heap-priority-queue#Template A: The five heap methods\|A: The five heap methods]], [[wiki/neetcode-150/09-heap-priority-queue#Template B: Heap of size K\|B: Heap of size K]] | [[wiki/neetcode-150/09-heap-priority-queue#703. Kth Largest Element in a Stream\|solution]] |
| 65 | [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | Max-heap simulation | [[wiki/neetcode-150/09-heap-priority-queue#Template C: Max-heap by a different Less\|C: Max-heap by a different Less]] | [[wiki/neetcode-150/09-heap-priority-queue#1046. Last Stone Weight\|solution]] |
| 66 | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | Max-heap of size K | [[wiki/neetcode-150/09-heap-priority-queue#Template B: Heap of size K\|B: Heap of size K]], [[wiki/neetcode-150/09-heap-priority-queue#Template C: Max-heap by a different Less\|C: Max-heap by a different Less]] | [[wiki/neetcode-150/09-heap-priority-queue#973. K Closest Points to Origin\|solution]] |
| 67 | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Min-heap of size K | [[wiki/neetcode-150/09-heap-priority-queue#Template A: The five heap methods\|A: The five heap methods]], [[wiki/neetcode-150/09-heap-priority-queue#Template B: Heap of size K\|B: Heap of size K]] | [[wiki/neetcode-150/09-heap-priority-queue#215. Kth Largest Element in an Array\|solution]] |
| 68 | [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | Max-heap plus cooldown queue | [[wiki/neetcode-150/09-heap-priority-queue#Template C: Max-heap by a different Less\|C: Max-heap by a different Less]], [[wiki/neetcode-150/09-heap-priority-queue#Template E: Max-heap plus cooldown queue\|E: Max-heap plus cooldown queue]] | [[wiki/neetcode-150/09-heap-priority-queue#621. Task Scheduler\|solution]] |
| 69 | [355. Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | K-way merge with a heap | [[wiki/neetcode-150/09-heap-priority-queue#Template F: K-way merge with a heap\|F: K-way merge with a heap]] | [[wiki/neetcode-150/09-heap-priority-queue#355. Design Twitter\|solution]] |
| 70 | [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | Two heaps | [[wiki/neetcode-150/09-heap-priority-queue#Template D: Two heaps for the median\|D: Two heaps for the median]] | [[wiki/neetcode-150/09-heap-priority-queue#295. Find Median from Data Stream\|solution]] |

### Stage 10: Backtracking

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 71 | [78. Subsets](https://leetcode.com/problems/subsets/) | Medium | Backtracking with a start index | [[wiki/neetcode-150/10-backtracking#Template A: Choose, explore, undo with a start index\|A: Choose, explore, undo with a start index]] | [[wiki/neetcode-150/10-backtracking#78. Subsets\|solution]] |
| 72 | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | Backtracking with reuse | [[wiki/neetcode-150/10-backtracking#Template A: Choose, explore, undo with a start index\|A: Choose, explore, undo with a start index]] | [[wiki/neetcode-150/10-backtracking#39. Combination Sum\|solution]] |
| 73 | [46. Permutations](https://leetcode.com/problems/permutations/) | Medium | Backtracking with a used slice | [[wiki/neetcode-150/10-backtracking#Template C: Permutations with a used slice\|C: Permutations with a used slice]] | [[wiki/neetcode-150/10-backtracking#46. Permutations\|solution]] |
| 74 | [90. Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium | Backtracking, skip duplicates | [[wiki/neetcode-150/10-backtracking#Template A: Choose, explore, undo with a start index\|A: Choose, explore, undo with a start index]], [[wiki/neetcode-150/10-backtracking#Template B: Skip duplicates after a sort\|B: Skip duplicates after a sort]] | [[wiki/neetcode-150/10-backtracking#90. Subsets II\|solution]] |
| 75 | [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Medium | Backtracking, skip duplicates | [[wiki/neetcode-150/10-backtracking#Template A: Choose, explore, undo with a start index\|A: Choose, explore, undo with a start index]], [[wiki/neetcode-150/10-backtracking#Template B: Skip duplicates after a sort\|B: Skip duplicates after a sort]] | [[wiki/neetcode-150/10-backtracking#40. Combination Sum II\|solution]] |
| 76 | [79. Word Search](https://leetcode.com/problems/word-search/) | Medium | Grid backtracking, mark and unmark | [[wiki/neetcode-150/10-backtracking#Template D: Grid path with mark and unmark\|D: Grid path with mark and unmark]] | [[wiki/neetcode-150/10-backtracking#79. Word Search\|solution]] |
| 77 | [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium | Backtracking, cut a string | [[wiki/neetcode-150/10-backtracking#Template E: Cut a string into parts\|E: Cut a string into parts]] | [[wiki/neetcode-150/10-backtracking#131. Palindrome Partitioning\|solution]] |
| 78 | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | Backtracking, one choice for each position | [[wiki/neetcode-150/10-backtracking#Template F: One choice for each position, with sets\|F: One choice for each position, with sets]] | [[wiki/neetcode-150/10-backtracking#17. Letter Combinations of a Phone Number\|solution]] |
| 79 | [51. N-Queens](https://leetcode.com/problems/n-queens/) | Hard | Backtracking with constraint sets | [[wiki/neetcode-150/10-backtracking#Template F: One choice for each position, with sets\|F: One choice for each position, with sets]] | [[wiki/neetcode-150/10-backtracking#51. N-Queens\|solution]] |

### Stage 11: Graphs

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 80 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Grid DFS (flood fill) | [[wiki/neetcode-150/11-graphs#Template A: Grid DFS (flood fill)\|A: Grid DFS (flood fill)]] | [[wiki/neetcode-150/11-graphs#200. Number of Islands\|solution]] |
| 81 | [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | DFS with a clone map | [[wiki/neetcode-150/11-graphs#Template C: Clone with a map\|C: Clone with a map]] | [[wiki/neetcode-150/11-graphs#133. Clone Graph\|solution]] |
| 82 | [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | Grid DFS (flood fill) | [[wiki/neetcode-150/11-graphs#Template A: Grid DFS (flood fill)\|A: Grid DFS (flood fill)]] | [[wiki/neetcode-150/11-graphs#695. Max Area of Island\|solution]] |
| 83 | [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | DFS from the borders | [[wiki/neetcode-150/11-graphs#Template A: Grid DFS (flood fill)\|A: Grid DFS (flood fill)]] | [[wiki/neetcode-150/11-graphs#417. Pacific Atlantic Water Flow\|solution]] |
| 84 | [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | DFS from the borders | [[wiki/neetcode-150/11-graphs#Template A: Grid DFS (flood fill)\|A: Grid DFS (flood fill)]] | [[wiki/neetcode-150/11-graphs#130. Surrounded Regions\|solution]] |
| 85 | [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Multi-source BFS by level | [[wiki/neetcode-150/11-graphs#Template B: BFS by level from many sources\|B: BFS by level from many sources]] | [[wiki/neetcode-150/11-graphs#994. Rotting Oranges\|solution]] |
| 86 | [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/) ([free](https://neetcode.io/problems/islands-and-treasure)) | Medium | Multi-source BFS by level | [[wiki/neetcode-150/11-graphs#Template B: BFS by level from many sources\|B: BFS by level from many sources]] | [[wiki/neetcode-150/11-graphs#286. Walls and Gates\|solution]] |
| 87 | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Topological sort (Kahn) | [[wiki/neetcode-150/11-graphs#Template D: Topological sort\|D: Topological sort]] | [[wiki/neetcode-150/11-graphs#207. Course Schedule\|solution]] |
| 88 | [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | Topological sort (Kahn) | [[wiki/neetcode-150/11-graphs#Template D: Topological sort\|D: Topological sort]] | [[wiki/neetcode-150/11-graphs#210. Course Schedule II\|solution]] |
| 89 | [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | Union-find, cycle detection | [[wiki/neetcode-150/11-graphs#Template E: Union-find\|E: Union-find]] | [[wiki/neetcode-150/11-graphs#684. Redundant Connection\|solution]] |
| 90 | [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) ([free](https://neetcode.io/problems/count-connected-components)) | Medium | Union-find, count the groups | [[wiki/neetcode-150/11-graphs#Template E: Union-find\|E: Union-find]] | [[wiki/neetcode-150/11-graphs#323. Number of Connected Components in an Undirected Graph\|solution]] |
| 91 | [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) ([free](https://neetcode.io/problems/valid-tree)) | Medium | Union-find, cycle detection | [[wiki/neetcode-150/11-graphs#Template E: Union-find\|E: Union-find]] | [[wiki/neetcode-150/11-graphs#261. Graph Valid Tree\|solution]] |
| 92 | [127. Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | BFS on an implicit graph | [[wiki/neetcode-150/11-graphs#Template F: BFS on an implicit graph\|F: BFS on an implicit graph]] | [[wiki/neetcode-150/11-graphs#127. Word Ladder\|solution]] |

### Stage 12: Advanced Graphs

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 93 | [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard | Eulerian path (Hierholzer) | [[wiki/neetcode-150/12-advanced-graphs#Template D: Hierholzer's algorithm\|D: Hierholzer's algorithm]] | [[wiki/neetcode-150/12-advanced-graphs#332. Reconstruct Itinerary\|solution]] |
| 94 | [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Minimum spanning tree (Prim) | [[wiki/neetcode-150/12-advanced-graphs#Template B: Prim with a heap\|B: Prim with a heap]], [[wiki/neetcode-150/12-advanced-graphs#Template F: Min-heap of items\|F: Min-heap of items]] | [[wiki/neetcode-150/12-advanced-graphs#1584. Min Cost to Connect All Points\|solution]] |
| 95 | [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Dijkstra with a heap | [[wiki/neetcode-150/12-advanced-graphs#Template A: Dijkstra with a heap\|A: Dijkstra with a heap]], [[wiki/neetcode-150/12-advanced-graphs#Template F: Min-heap of items\|F: Min-heap of items]] | [[wiki/neetcode-150/12-advanced-graphs#743. Network Delay Time\|solution]] |
| 96 | [778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | Dijkstra, minimise the maximum | [[wiki/neetcode-150/12-advanced-graphs#Template A: Dijkstra with a heap\|A: Dijkstra with a heap]], [[wiki/neetcode-150/12-advanced-graphs#Template F: Min-heap of items\|F: Min-heap of items]] | [[wiki/neetcode-150/12-advanced-graphs#778. Swim in Rising Water\|solution]] |
| 97 | [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) ([free](https://neetcode.io/problems/foreign-dictionary)) | Hard | Topological sort from comparisons | [[wiki/neetcode-150/12-advanced-graphs#Template E: Topological sort from comparisons\|E: Topological sort from comparisons]] | [[wiki/neetcode-150/12-advanced-graphs#269. Alien Dictionary\|solution]] |
| 98 | [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Bellman-Ford with a round limit | [[wiki/neetcode-150/12-advanced-graphs#Template C: Bellman-Ford with a round limit\|C: Bellman-Ford with a round limit]] | [[wiki/neetcode-150/12-advanced-graphs#787. Cheapest Flights Within K Stops\|solution]] |

### Stage 13: 1-D Dynamic Programming

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 99 | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | Fibonacci with two variables | [[wiki/neetcode-150/13-dp-1d#Template A: Two variables\|A: Two variables]] | [[wiki/neetcode-150/13-dp-1d#70. Climbing Stairs\|solution]] |
| 100 | [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy | Two variables, minimum cost | [[wiki/neetcode-150/13-dp-1d#Template A: Two variables\|A: Two variables]] | [[wiki/neetcode-150/13-dp-1d#746. Min Cost Climbing Stairs\|solution]] |
| 101 | [198. House Robber](https://leetcode.com/problems/house-robber/) | Medium | Take or skip, two variables | [[wiki/neetcode-150/13-dp-1d#Template A: Two variables\|A: Two variables]] | [[wiki/neetcode-150/13-dp-1d#198. House Robber\|solution]] |
| 102 | [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium | Take or skip on a circle | [[wiki/neetcode-150/13-dp-1d#Template A: Two variables\|A: Two variables]] | [[wiki/neetcode-150/13-dp-1d#213. House Robber II\|solution]] |
| 103 | [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | Expand from the centre | [[wiki/neetcode-150/13-dp-1d#Template E: Expand from the centre\|E: Expand from the centre]] | [[wiki/neetcode-150/13-dp-1d#5. Longest Palindromic Substring\|solution]] |
| 104 | [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | Expand from the centre | [[wiki/neetcode-150/13-dp-1d#Template E: Expand from the centre\|E: Expand from the centre]] | [[wiki/neetcode-150/13-dp-1d#647. Palindromic Substrings\|solution]] |
| 105 | [91. Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | Table over a prefix, count | [[wiki/neetcode-150/13-dp-1d#Template B: Table over a prefix or an amount\|B: Table over a prefix or an amount]] | [[wiki/neetcode-150/13-dp-1d#91. Decode Ways\|solution]] |
| 106 | [322. Coin Change](https://leetcode.com/problems/coin-change/) | Medium | Table over an amount, minimum | [[wiki/neetcode-150/13-dp-1d#Template B: Table over a prefix or an amount\|B: Table over a prefix or an amount]] | [[wiki/neetcode-150/13-dp-1d#322. Coin Change\|solution]] |
| 107 | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | Best that ends at i, max and min | [[wiki/neetcode-150/13-dp-1d#Template C: Best that ends at i\|C: Best that ends at i]] | [[wiki/neetcode-150/13-dp-1d#152. Maximum Product Subarray\|solution]] |
| 108 | [139. Word Break](https://leetcode.com/problems/word-break/) | Medium | Table over a prefix, yes or no | [[wiki/neetcode-150/13-dp-1d#Template B: Table over a prefix or an amount\|B: Table over a prefix or an amount]] | [[wiki/neetcode-150/13-dp-1d#139. Word Break\|solution]] |
| 109 | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | Best that ends at i | [[wiki/neetcode-150/13-dp-1d#Template C: Best that ends at i\|C: Best that ends at i]] | [[wiki/neetcode-150/13-dp-1d#300. Longest Increasing Subsequence\|solution]] |
| 110 | [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 0/1 knapsack, subset sum | [[wiki/neetcode-150/13-dp-1d#Template D: 0/1 knapsack on a boolean row\|D: 0/1 knapsack on a boolean row]] | [[wiki/neetcode-150/13-dp-1d#416. Partition Equal Subset Sum\|solution]] |

### Stage 14: 2-D Dynamic Programming

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 111 | [62. Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | Grid paths, one row | [[wiki/neetcode-150/14-dp-2d#Template A: Grid paths\|A: Grid paths]] | [[wiki/neetcode-150/14-dp-2d#62. Unique Paths\|solution]] |
| 112 | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | Two strings table | [[wiki/neetcode-150/14-dp-2d#Template B: Two strings table\|B: Two strings table]] | [[wiki/neetcode-150/14-dp-2d#1143. Longest Common Subsequence\|solution]] |
| 113 | [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | State machine by day | [[wiki/neetcode-150/14-dp-2d#Template D: State machine by day\|D: State machine by day]] | [[wiki/neetcode-150/14-dp-2d#309. Best Time to Buy and Sell Stock with Cooldown\|solution]] |
| 114 | [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Medium | Unbounded knapsack, count | [[wiki/neetcode-150/14-dp-2d#Template C: Knapsack count on one row\|C: Knapsack count on one row]] | [[wiki/neetcode-150/14-dp-2d#518. Coin Change II\|solution]] |
| 115 | [494. Target Sum](https://leetcode.com/problems/target-sum/) | Medium | 0/1 knapsack count, subset sum | [[wiki/neetcode-150/14-dp-2d#Template C: Knapsack count on one row\|C: Knapsack count on one row]] | [[wiki/neetcode-150/14-dp-2d#494. Target Sum\|solution]] |
| 116 | [97. Interleaving String](https://leetcode.com/problems/interleaving-string/) | Medium | Two strings table, yes or no | [[wiki/neetcode-150/14-dp-2d#Template B: Two strings table\|B: Two strings table]] | [[wiki/neetcode-150/14-dp-2d#97. Interleaving String\|solution]] |
| 117 | [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Hard | DFS with memo on a grid | [[wiki/neetcode-150/14-dp-2d#Template F: DFS with memo on a grid\|F: DFS with memo on a grid]] | [[wiki/neetcode-150/14-dp-2d#329. Longest Increasing Path in a Matrix\|solution]] |
| 118 | [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | Hard | Two strings table, count | [[wiki/neetcode-150/14-dp-2d#Template B: Two strings table\|B: Two strings table]] | [[wiki/neetcode-150/14-dp-2d#115. Distinct Subsequences\|solution]] |
| 119 | [72. Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | Two strings table, minimum | [[wiki/neetcode-150/14-dp-2d#Template B: Two strings table\|B: Two strings table]] | [[wiki/neetcode-150/14-dp-2d#72. Edit Distance\|solution]] |
| 120 | [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | Interval DP, last to burst | [[wiki/neetcode-150/14-dp-2d#Template E: Interval DP\|E: Interval DP]] | [[wiki/neetcode-150/14-dp-2d#312. Burst Balloons\|solution]] |
| 121 | [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard | Two strings table, pattern match | [[wiki/neetcode-150/14-dp-2d#Template B: Two strings table\|B: Two strings table]] | [[wiki/neetcode-150/14-dp-2d#10. Regular Expression Matching\|solution]] |

### Stage 15: Greedy

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 122 | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Kadane's running sum | [[wiki/neetcode-150/15-greedy#Template A: Running sum with a reset\|A: Running sum with a reset]] | [[wiki/neetcode-150/15-greedy#53. Maximum Subarray\|solution]] |
| 123 | [55. Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Greedy farthest reach | [[wiki/neetcode-150/15-greedy#Template B: Farthest reach\|B: Farthest reach]] | [[wiki/neetcode-150/15-greedy#55. Jump Game\|solution]] |
| 124 | [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | Greedy levels, as in BFS | [[wiki/neetcode-150/15-greedy#Template B: Farthest reach\|B: Farthest reach]] | [[wiki/neetcode-150/15-greedy#45. Jump Game II\|solution]] |
| 125 | [134. Gas Station](https://leetcode.com/problems/gas-station/) | Medium | Greedy running total with a reset | [[wiki/neetcode-150/15-greedy#Template A: Running sum with a reset\|A: Running sum with a reset]] | [[wiki/neetcode-150/15-greedy#134. Gas Station\|solution]] |
| 126 | [846. Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Medium | Sort, then take the smallest first | [[wiki/neetcode-150/15-greedy#Template C: Sort, then take the smallest first\|C: Sort, then take the smallest first]] | [[wiki/neetcode-150/15-greedy#846. Hand of Straights\|solution]] |
| 127 | [1899. Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Medium | Greedy filter, then combine | [[wiki/neetcode-150/15-greedy#Template D: Filter, then combine\|D: Filter, then combine]] | [[wiki/neetcode-150/15-greedy#1899. Merge Triplets to Form Target Triplet\|solution]] |
| 128 | [763. Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | Last index, then extend the end | [[wiki/neetcode-150/15-greedy#Template E: Last index, then extend the end\|E: Last index, then extend the end]] | [[wiki/neetcode-150/15-greedy#763. Partition Labels\|solution]] |
| 129 | [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Medium | Greedy range of open counts | [[wiki/neetcode-150/15-greedy#Template F: Range of possible counts\|F: Range of possible counts]] | [[wiki/neetcode-150/15-greedy#678. Valid Parenthesis String\|solution]] |

### Stage 16: Intervals

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 130 | [57. Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Three-phase insert | [[wiki/neetcode-150/16-intervals#Template B: Three-phase insert\|B: Three-phase insert]] | [[wiki/neetcode-150/16-intervals#57. Insert Interval\|solution]] |
| 131 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Sort by start, then merge | [[wiki/neetcode-150/16-intervals#Template A: Sort by start, then merge\|A: Sort by start, then merge]] | [[wiki/neetcode-150/16-intervals#56. Merge Intervals\|solution]] |
| 132 | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Sort by end, greedy keep | [[wiki/neetcode-150/16-intervals#Template C: Sort by end, then greedy keep\|C: Sort by end, then greedy keep]] | [[wiki/neetcode-150/16-intervals#435. Non-overlapping Intervals\|solution]] |
| 133 | [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) ([free](https://neetcode.io/problems/meeting-schedule)) | Easy | Sort by start, compare neighbors | [[wiki/neetcode-150/16-intervals#Template A: Sort by start, then merge\|A: Sort by start, then merge]] | [[wiki/neetcode-150/16-intervals#252. Meeting Rooms\|solution]] |
| 134 | [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) ([free](https://neetcode.io/problems/meeting-schedule-ii)) | Medium | Sweep of sorted starts and ends | [[wiki/neetcode-150/16-intervals#Template D: Sweep of sorted starts and ends\|D: Sweep of sorted starts and ends]] | [[wiki/neetcode-150/16-intervals#253. Meeting Rooms II\|solution]] |
| 135 | [1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Hard | Offline queries, sort plus min-heap | [[wiki/neetcode-150/16-intervals#Template E: Offline queries with a sort and a min-heap\|E: Offline queries with a sort and a min-heap]] | [[wiki/neetcode-150/16-intervals#1851. Minimum Interval to Include Each Query\|solution]] |

### Stage 17: Math and Geometry

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 136 | [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | Transpose, then reverse the rows | [[wiki/neetcode-150/17-math-and-geometry#Template A: Transpose, then reverse\|A: Transpose, then reverse]] | [[wiki/neetcode-150/17-math-and-geometry#48. Rotate Image\|solution]] |
| 137 | [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | Four boundaries that shrink | [[wiki/neetcode-150/17-math-and-geometry#Template B: Four boundaries that shrink\|B: Four boundaries that shrink]] | [[wiki/neetcode-150/17-math-and-geometry#54. Spiral Matrix\|solution]] |
| 138 | [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | First row and column as markers | [[wiki/neetcode-150/17-math-and-geometry#Template C: Markers in the first row and column\|C: Markers in the first row and column]] | [[wiki/neetcode-150/17-math-and-geometry#73. Set Matrix Zeroes\|solution]] |
| 139 | [202. Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Digit loop with cycle detection | [[wiki/neetcode-150/17-math-and-geometry#Template D: Digit loop with a carry\|D: Digit loop with a carry]] | [[wiki/neetcode-150/17-math-and-geometry#202. Happy Number\|solution]] |
| 140 | [66. Plus One](https://leetcode.com/problems/plus-one/) | Easy | Digit loop with a carry | [[wiki/neetcode-150/17-math-and-geometry#Template D: Digit loop with a carry\|D: Digit loop with a carry]] | [[wiki/neetcode-150/17-math-and-geometry#66. Plus One\|solution]] |
| 141 | [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | Fast power by squaring | [[wiki/neetcode-150/17-math-and-geometry#Template E: Fast power by squaring\|E: Fast power by squaring]] | [[wiki/neetcode-150/17-math-and-geometry#50. Pow(x, n)\|solution]] |
| 142 | [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Medium | Grade-school multiplication with digits | [[wiki/neetcode-150/17-math-and-geometry#Template D: Digit loop with a carry\|D: Digit loop with a carry]] | [[wiki/neetcode-150/17-math-and-geometry#43. Multiply Strings\|solution]] |
| 143 | [2013. Detect Squares](https://leetcode.com/problems/detect-squares/) | Medium | Count map of points | [[wiki/neetcode-150/17-math-and-geometry#Template F: Count map of points\|F: Count map of points]] | [[wiki/neetcode-150/17-math-and-geometry#2013. Detect Squares\|solution]] |

### Stage 18: Bit Manipulation

| # | Problem | Level | Pattern | Template | Go |
|---|---|---|---|---|---|
| 144 | [136. Single Number](https://leetcode.com/problems/single-number/) | Easy | XOR cancels pairs | [[wiki/neetcode-150/18-bit-manipulation#Template A: XOR cancels pairs\|A: XOR cancels pairs]] | [[wiki/neetcode-150/18-bit-manipulation#136. Single Number\|solution]] |
| 145 | [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | Remove the lowest set bit | [[wiki/neetcode-150/18-bit-manipulation#Template B: Remove the lowest set bit\|B: Remove the lowest set bit]] | [[wiki/neetcode-150/18-bit-manipulation#191. Number of 1 Bits\|solution]] |
| 146 | [338. Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | DP on bits | [[wiki/neetcode-150/18-bit-manipulation#Template C: DP on bits\|C: DP on bits]] | [[wiki/neetcode-150/18-bit-manipulation#338. Counting Bits\|solution]] |
| 147 | [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | Shift in and shift out | [[wiki/neetcode-150/18-bit-manipulation#Template D: Shift in and shift out\|D: Shift in and shift out]] | [[wiki/neetcode-150/18-bit-manipulation#190. Reverse Bits\|solution]] |
| 148 | [268. Missing Number](https://leetcode.com/problems/missing-number/) | Easy | XOR of indexes and values | [[wiki/neetcode-150/18-bit-manipulation#Template A: XOR cancels pairs\|A: XOR cancels pairs]] | [[wiki/neetcode-150/18-bit-manipulation#268. Missing Number\|solution]] |
| 149 | [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | Add with XOR and carry | [[wiki/neetcode-150/18-bit-manipulation#Template E: Add with XOR and carry\|E: Add with XOR and carry]] | [[wiki/neetcode-150/18-bit-manipulation#371. Sum of Two Integers\|solution]] |
| 150 | [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium | Digit loop with an overflow check | [[wiki/neetcode-150/18-bit-manipulation#Template F: Digit loop with an overflow check\|F: Digit loop with an overflow check]] | [[wiki/neetcode-150/18-bit-manipulation#7. Reverse Integer\|solution]] |

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
