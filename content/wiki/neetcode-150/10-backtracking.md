---
title: "NeetCode 150, stage 10: Backtracking"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - backtracking
date_created: 2026-11-11
date_modified: 2026-11-11
---

# NeetCode 150, stage 10: Backtracking

[[wiki/neetcode-150/09-heap-priority-queue|← Heap and Priority Queue]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/11-graphs|Graphs →]]

Backtracking builds each answer one choice at a time, and it goes back when a choice cannot lead to an answer. This stage trains the problems that say "all subsets", "all combinations" or "all permutations". Each solution has the same three moves: choose, explore, undo. In Go, this stage also teaches when a saved slice needs a copy.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 9: Slice copies with backtracking|the Go syntax for this stage]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/10-backtracking#78. Subsets\|78. Subsets]] | Medium | Backtracking with a start index | [[wiki/neetcode-150/10-backtracking#Template A: Choose, explore, undo with a start index\|A: Choose, explore, undo with a start index]] |
| 2 | [[wiki/neetcode-150/10-backtracking#39. Combination Sum\|39. Combination Sum]] | Medium | Backtracking with reuse | [[wiki/neetcode-150/10-backtracking#Template A: Choose, explore, undo with a start index\|A: Choose, explore, undo with a start index]] |
| 3 | [[wiki/neetcode-150/10-backtracking#46. Permutations\|46. Permutations]] | Medium | Backtracking with a used slice | [[wiki/neetcode-150/10-backtracking#Template C: Permutations with a used slice\|C: Permutations with a used slice]] |
| 4 | [[wiki/neetcode-150/10-backtracking#90. Subsets II\|90. Subsets II]] | Medium | Backtracking, skip duplicates | [[wiki/neetcode-150/10-backtracking#Template A: Choose, explore, undo with a start index\|A: Choose, explore, undo with a start index]], [[wiki/neetcode-150/10-backtracking#Template B: Skip duplicates after a sort\|B: Skip duplicates after a sort]] |
| 5 | [[wiki/neetcode-150/10-backtracking#40. Combination Sum II\|40. Combination Sum II]] | Medium | Backtracking, skip duplicates | [[wiki/neetcode-150/10-backtracking#Template A: Choose, explore, undo with a start index\|A: Choose, explore, undo with a start index]], [[wiki/neetcode-150/10-backtracking#Template B: Skip duplicates after a sort\|B: Skip duplicates after a sort]] |
| 6 | [[wiki/neetcode-150/10-backtracking#79. Word Search\|79. Word Search]] | Medium | Grid backtracking, mark and unmark | [[wiki/neetcode-150/10-backtracking#Template D: Grid path with mark and unmark\|D: Grid path with mark and unmark]] |
| 7 | [[wiki/neetcode-150/10-backtracking#131. Palindrome Partitioning\|131. Palindrome Partitioning]] | Medium | Backtracking, cut a string | [[wiki/neetcode-150/10-backtracking#Template E: Cut a string into parts\|E: Cut a string into parts]] |
| 8 | [[wiki/neetcode-150/10-backtracking#17. Letter Combinations of a Phone Number\|17. Letter Combinations of a Phone Number]] | Medium | Backtracking, one choice for each position | [[wiki/neetcode-150/10-backtracking#Template F: One choice for each position, with sets\|F: One choice for each position, with sets]] |
| 9 | [[wiki/neetcode-150/10-backtracking#51. N-Queens\|51. N-Queens]] | Hard | Backtracking with constraint sets | [[wiki/neetcode-150/10-backtracking#Template F: One choice for each position, with sets\|F: One choice for each position, with sets]] |

## Templates to memorize

### Template A: Choose, explore, undo with a start index

> [!tip] Signal
> The problem asks for all subsets or all combinations. The order of the items in one answer does not matter, so `[1, 2]` and `[2, 1]` are the same answer.

```go
// TEMPLATE A: choose, explore, undo with a start index.
// This example builds each group of k items. The order in a group does not
// matter.
func groupsOfK(items []int, k int) [][]int {
    res := [][]int{}
    path := []int{} // the choices so far
    var dfs func(start int)
    dfs = func(start int) {
        if len(path) == k { // GOAL
            // SAVE a copy, never the path itself
            res = append(res, slices.Clone(path))
            return
        }
        for i := start; i < len(items); i++ {
            path = append(path, items[i]) // 1. CHOOSE
            // 2. EXPLORE. i+1: no reuse. i: reuse is allowed
            dfs(i + 1)
            path = path[:len(path)-1] // 3. UNDO
        }
    }
    dfs(0)
    return res
}
```

The moves are CHOOSE, EXPLORE, then UNDO. The start index gives each answer one fixed order, so no answer appears two times. Pass `i + 1` when each item can be used one time, and pass `i` when an item can repeat. Save `slices.Clone(path)`, not `path`. All the saved slices would share one backing array, and the later appends would write over them.

> [!quote] Say it
> "I build the answer one item at a time: choose, recurse, undo. A start index stops duplicates, and I copy the path before I save it."

### Template B: Skip duplicates after a sort

> [!tip] Signal
> The input can contain equal values, and the answer must not contain the same subset or combination two times.

```go
// TEMPLATE B: the input has equal values. Sort, then skip an equal value in
// the same loop.
func uniqueGroupsOfK(items []int, k int) [][]int {
    sort.Ints(items) // 1. SORT: equal values become neighbors
    res := [][]int{}
    path := []int{}
    var dfs func(start int)
    dfs = func(start int) {
        if len(path) == k {
            res = append(res, slices.Clone(path))
            return
        }
        for i := start; i < len(items); i++ {
            if i > start && items[i] == items[i-1] {
                // 2. SKIP: this value already opened a branch in this loop
                continue
            }
            path = append(path, items[i])
            dfs(i + 1)
            path = path[:len(path)-1]
        }
    }
    dfs(0)
    return res
}
```

The moves are SORT, then SKIP. The rest is Template A. The test is `i > start`, not `i > 0`. It stops a second equal value in the same loop, at the same depth. A deeper call can still choose the next equal value, so `[2, 2]` stays possible.

> [!quote] Say it
> "I sort first, so equal values are neighbors. At each depth I use a value only one time, and that removes the duplicate answers without a set."

### Template C: Permutations with a used slice

> [!tip] Signal
> The problem asks for all orders or all arrangements. The order matters, so `[1, 2]` and `[2, 1]` are different answers.

```go
// TEMPLATE C: permutations. The order matters, so each call looks at all
// the items.
func allOrders(items []int) [][]int {
    res := [][]int{}
    path := []int{}
    used := make([]bool, len(items)) // used[i]: items[i] is in the path
    var dfs func()
    dfs = func() {
        if len(path) == len(items) { // GOAL
            res = append(res, slices.Clone(path)) // SAVE a copy
            return
        }
        for i := 0; i < len(items); i++ {
            if used[i] {
                continue // 1. CHECK: each item one time
            }
            used[i] = true // 2. CHOOSE
            path = append(path, items[i])
            dfs()                     // 3. EXPLORE
            path = path[:len(path)-1] // 4. UNDO the two changes
            used[i] = false
        }
    }
    dfs()
    return res
}
```

The moves are CHECK, CHOOSE, EXPLORE, then UNDO. There is no start index, because a later position can take an earlier item. The `used` slice replaces it. The undo has two parts: remove the item from the path, and set `used[i]` back to `false`.

> [!quote] Say it
> "Each position can take each item that is not used. A boolean slice records the used items. There are n factorial permutations, so the time is O(n times n factorial)."

### Template D: Grid path with mark and unmark

> [!tip] Signal
> You must find a path of neighbor cells in a grid, and the path cannot use a cell two times. The path must match a word or a rule, step by step.

```go
// TEMPLATE D: a path in a grid. The DFS marks a cell while the cell is in
// the path.
// Call it from each cell with k = 0.
func pathFrom(grid [][]byte, r, c int, word string, k int) bool {
    if k == len(word) {
        return true // GOAL: all the letters matched
    }
    if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) || grid[r][c] != word[k] {
        return false // 1. CHECK: in the grid, and the letter is correct
    }
    grid[r][c] = '#' // 2. MARK: this path cannot use the cell again
    found := pathFrom(grid, r+1, c, word, k+1) || pathFrom(grid, r-1, c, word, k+1) ||
        // 3. EXPLORE
        pathFrom(grid, r, c+1, word, k+1) || pathFrom(grid, r, c-1, word, k+1)
    grid[r][c] = word[k] // 4. UNMARK
    return found
}
```

The moves are CHECK, MARK, EXPLORE, then UNMARK. The mark is a change of the cell, so the grid is its own visited set. Always unmark before the return. If you return early when a neighbor finds the word, the grid stays damaged for the caller.

> [!quote] Say it
> "I run a DFS from each cell. I mark the cell while it is on the path and restore it when I come back, so the extra space is only the recursion."

### Template E: Cut a string into parts

> [!tip] Signal
> You must split a string into parts, each part must pass a test, and the problem asks for all the ways. The test can be "is a palindrome" or "is a valid number".

```go
// TEMPLATE E: cut a string into parts. Each part must pass the valid
// function.
func cutAll(s string, valid func(part string) bool) [][]string {
    res := [][]string{}
    path := []string{}
    var dfs func(start int)
    dfs = func(start int) {
        if start == len(s) { // GOAL: the parts cover the full string
            res = append(res, slices.Clone(path)) // SAVE a copy
            return
        }
        for end := start + 1; end <= len(s); end++ {
            if !valid(s[start:end]) {
                continue // 1. CHECK the part s[start:end]
            }
            // 2. CHOOSE where this part ends
            path = append(path, s[start:end])
            dfs(end)                  // 3. EXPLORE: cut the rest
            path = path[:len(path)-1] // 4. UNDO
        }
    }
    dfs(0)
    return res
}
```

The moves are CHECK, CHOOSE, EXPLORE, then UNDO. The choice is the place where the next part ends. The index `end` is exclusive, so the loop goes up to `len(s)` with `<=`. The goal is `start == len(s)`: the parts then cover the full string.

> [!quote] Say it
> "At each index I try each end for the next part. If the part is valid, I recurse on the rest of the string."

### Template F: One choice for each position, with sets

> [!tip] Signal
> The answer has a fixed number of positions, and each position gets one of a few options. A rule can forbid some pairs of choices, as in N-Queens.

```go
// TEMPLATE F: one choice for each position. Here a position is a row of a
// chess board,
// and three sets tell in O(1) if a queen can go in column c.
func countQueens(n int) int {
    cols := make([]bool, n)   // cols[c]: a queen is in column c
    diag := make([]bool, 2*n) // diag[r+c]: r+c is the same on one "/" line
    // anti[r-c+n]: r-c is the same on one "\" line
    anti := make([]bool, 2*n)
    count := 0
    var dfs func(r int)
    dfs = func(r int) {
        if r == n { // GOAL: each position has its choice
            count++
            return
        }
        for c := 0; c < n; c++ {
            if cols[c] || diag[r+c] || anti[r-c+n] {
                continue // 1. CHECK the sets
            }
            // 2. PLACE
            cols[c], diag[r+c], anti[r-c+n] = true, true, true
            // 3. EXPLORE the next position
            dfs(r + 1)
            // 4. REMOVE
            cols[c], diag[r+c], anti[r-c+n] = false, false, false
        }
    }
    dfs(0)
    return count
}
```

The moves are CHECK, PLACE, EXPLORE, then REMOVE. The DFS index is the position, and the loop goes through the options for that position. The sets make the check O(1). On a chess board, `r + c` identifies one diagonal and `r - c` identifies the other. If no rule connects the positions, remove the sets and keep the rest.

> [!quote] Say it
> "I place one queen in each row. Three sets, for the column and the two diagonals, tell me in constant time if a cell is safe."

> [!warning] Mistakes in this stage
> - `res = append(res, path)` saves a slice header that points to the memory of `path`. Save `slices.Clone(path)` or `append([]int(nil), path...)`.
> - A recursive closure needs two lines: `var dfs func(start int)` first, then `dfs = func(start int) {...}`. With `:=`, the name does not exist inside its own body.
> - `path[:len(path)-1]` removes the last item, but it keeps the memory. The next `append` writes to the same place.
> - The undo must be the exact opposite of the choice. If it is not, the next branch starts from a wrong state.

## Solved with comments

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 78. Subsets

[LeetCode 78](https://leetcode.com/problems/subsets/) · Medium

- **Pattern:** Backtracking with a start index
- **Template:** [[#Template A: Choose, explore, undo with a start index|A: Choose, explore, undo with a start index]]
- **Complexity:** time O(n * 2^n), space O(n) for the path and the recursion, without the output
- **Imports for a local file:** `slices`

**Idea.** Build each subset one item at a time. Each call saves the current path, then adds one of the later items and goes deeper. The start index makes sure that an item only joins items that come before it.

**Go lesson.** `append(res, path)` saves the slice header, not the items. All the saved subsets would share one backing array, so save `slices.Clone(path)`.

```go
// subsets solves LC 78. Time O(n * 2^n), space O(n) without the output.
// Each node of the recursion tree is one subset: the path from the root to
// that node.
func subsets(nums []int) [][]int {
    res := [][]int{}
    path := []int{} // the items chosen so far
    var dfs func(start int)
    dfs = func(start int) {
        // SAVE a copy. The path changes after this line, and a saved slice
        // shares its backing array with the path. Without the copy, the
        // later
        // appends write over the subsets that are already in res.
        res = append(res, slices.Clone(path))
        for i := start; i < len(nums); i++ {
            path = append(path, nums[i]) // CHOOSE nums[i]
            // EXPLORE with the items after i only
            dfs(i + 1)
            path = path[:len(path)-1] // UNDO: remove the last item
        }
    }
    dfs(0)
    return res
}
```

### 39. Combination Sum

[LeetCode 39](https://leetcode.com/problems/combination-sum/) · Medium

- **Pattern:** Backtracking with reuse
- **Template:** [[#Template A: Choose, explore, undo with a start index|A: Choose, explore, undo with a start index]]
- **Complexity:** time O(n^(T/m)) for target T and smallest candidate m, space O(T/m) for the path and the recursion, without the output
- **Imports for a local file:** `slices`, `sort`

**Idea.** Choose a candidate, subtract it from the target and go deeper. The next call starts at the same index, so the same candidate can repeat. It never goes back to an earlier index, so each combination appears one time.

**Go lesson.** `sort.Ints` sorts a slice in place. After the sort, `break` stops the loop at the first candidate that is too large, because all the later ones are larger.

```go
// combinationSum solves LC 39. Time O(n^(T/m)) for target T and smallest
// candidate m.
// The start index stays at i after a choice, so a candidate can repeat.
func combinationSum(candidates []int, target int) [][]int {
    sort.Ints(candidates) // sorted, so the loop can stop early
    res := [][]int{}
    path := []int{}
    var dfs func(start, remain int)
    dfs = func(start, remain int) {
        if remain == 0 { // GOAL: the path adds up to the target
            // SAVE a copy: the path changes later, and res must not share
            // its memory.
            res = append(res, slices.Clone(path))
            return
        }
        for i := start; i < len(candidates); i++ {
            if candidates[i] > remain {
                // PRUNE: this candidate and all the later ones are too
                // large
                break
            }
            path = append(path, candidates[i]) // CHOOSE
            // EXPLORE from i, not i+1: reuse is allowed
            dfs(i, remain-candidates[i])
            path = path[:len(path)-1] // UNDO
        }
    }
    dfs(0, target)
    return res
}
```

### 46. Permutations

[LeetCode 46](https://leetcode.com/problems/permutations/) · Medium

- **Pattern:** Backtracking with a used slice
- **Template:** [[#Template C: Permutations with a used slice|C: Permutations with a used slice]]
- **Complexity:** time O(n * n!), space O(n) for the path, the used slice and the recursion, without the output
- **Imports for a local file:** `slices`

**Idea.** A permutation uses each item one time, in any order. So each call can choose each item that is not in the path. A slice of booleans records the items that the path uses.

**Go lesson.** `make([]bool, n)` gives n values that are all `false`. Go sets new memory to the zero value, so no loop is necessary.

```go
// permute solves LC 46. Time O(n * n!), space O(n) without the output.
// The order matters, so each call looks at all the items, not only the
// later ones.
func permute(nums []int) [][]int {
    res := [][]int{}
    path := make([]int, 0, len(nums))
    // used[i] is true when nums[i] is in the path
    used := make([]bool, len(nums))
    var dfs func()
    dfs = func() {
        if len(path) == len(nums) { // GOAL: each item is in the path
            // SAVE a copy: all the permutations would share the memory of
            // the path.
            res = append(res, slices.Clone(path))
            return
        }
        for i := 0; i < len(nums); i++ {
            if used[i] {
                continue // nums[i] is already in the path
            }
            used[i] = true // CHOOSE nums[i]
            path = append(path, nums[i])
            dfs()                     // EXPLORE the next position
            path = path[:len(path)-1] // UNDO the two changes
            used[i] = false
        }
    }
    dfs()
    return res
}
```

### 90. Subsets II

[LeetCode 90](https://leetcode.com/problems/subsets-ii/) · Medium

- **Pattern:** Backtracking, skip duplicates
- **Template:** [[#Template A: Choose, explore, undo with a start index|A: Choose, explore, undo with a start index]], [[#Template B: Skip duplicates after a sort|B: Skip duplicates after a sort]]
- **Complexity:** time O(n * 2^n), space O(n) for the path and the recursion, without the output
- **Imports for a local file:** `slices`, `sort`

**Idea.** Sort the input, so equal values are neighbors. In one loop, each value can open a branch only one time. A second equal value in the same loop would build the same subsets again, so skip it.

**Go lesson.** The test is `i > start`, not `i > 0`, so it skips an equal value only in the same loop. A deeper call can still take the next equal value.

```go
// subsetsWithDup solves LC 90. Time O(n * 2^n), space O(n) without the
// output.
// It is LC 78 plus two lines: a sort, and a skip of equal values in the
// same loop.
func subsetsWithDup(nums []int) [][]int {
    sort.Ints(nums) // SORT: equal values become neighbors
    res := [][]int{}
    path := []int{}
    var dfs func(start int)
    dfs = func(start int) {
        // SAVE a copy: the path changes later, and res must not share its
        // memory.
        res = append(res, slices.Clone(path))
        for i := start; i < len(nums); i++ {
            // SKIP: nums[i-1] already opened a branch in this loop. The
            // same value
            // here gives the same subsets. i > start keeps the first one of
            // a group.
            if i > start && nums[i] == nums[i-1] {
                continue
            }
            path = append(path, nums[i]) // CHOOSE
            dfs(i + 1)                   // EXPLORE with the items after i
            path = path[:len(path)-1]    // UNDO
        }
    }
    dfs(0)
    return res
}
```

### 40. Combination Sum II

[LeetCode 40](https://leetcode.com/problems/combination-sum-ii/) · Medium

- **Pattern:** Backtracking, skip duplicates
- **Template:** [[#Template A: Choose, explore, undo with a start index|A: Choose, explore, undo with a start index]], [[#Template B: Skip duplicates after a sort|B: Skip duplicates after a sort]]
- **Complexity:** time O(n * 2^n), space O(n) for the path and the recursion, without the output
- **Imports for a local file:** `slices`, `sort`

**Idea.** A combination can use each candidate one time, so the next call starts at i+1. The input can have equal values. Sort it, then skip a value that is equal to the one before it in the same loop.

**Go lesson.** `continue` goes to the next loop pass and `break` stops the loop. The skip of a duplicate uses `continue`, and the prune of a large value uses `break`.

```go
// combinationSum2 solves LC 40. Time O(n * 2^n), space O(n) without the
// output.
// It differs from LC 39 in two places: no reuse (i+1), and a skip of equal
// values.
func combinationSum2(candidates []int, target int) [][]int {
    // SORT: equal values become neighbors, and the loop can stop early
    sort.Ints(candidates)
    res := [][]int{}
    path := []int{}
    var dfs func(start, remain int)
    dfs = func(start, remain int) {
        if remain == 0 { // GOAL: the path adds up to the target
            // SAVE a copy: the path changes later, and res must not share
            // its memory.
            res = append(res, slices.Clone(path))
            return
        }
        for i := start; i < len(candidates); i++ {
            if candidates[i] > remain {
                // PRUNE: this value and all the later ones are too large
                break
            }
            if i > start && candidates[i] == candidates[i-1] {
                // SKIP: the same value already opened a branch in this loop
                continue
            }
            path = append(path, candidates[i]) // CHOOSE
            // EXPLORE from i+1: each item one time
            dfs(i+1, remain-candidates[i])
            path = path[:len(path)-1] // UNDO
        }
    }
    dfs(0, target)
    return res
}
```

### 79. Word Search

[LeetCode 79](https://leetcode.com/problems/word-search/) · Medium

- **Pattern:** Grid backtracking, mark and unmark
- **Template:** [[#Template D: Grid path with mark and unmark|D: Grid path with mark and unmark]]
- **Complexity:** time O(R * C * 4 * 3^(L-1)) for an R x C board and a word of L letters, space O(L) for the recursion

**Idea.** Start a DFS at each cell. Each step must match the next letter of the word. Mark the cell while it is in the path, so the path cannot use it again, and restore it when the DFS comes back.

**Go lesson.** The logical OR operator stops at the first `true` value. So the chain of four DFS calls stops when one direction finds the word.

```go
// exist solves LC 79. Time O(R * C * 4 * 3^(L-1)), space O(L) for the
// recursion.
// The board itself records the cells of the current path, so no visited set
// is necessary.
func exist(board [][]byte, word string) bool {
    rows, cols := len(board), len(board[0])
    var dfs func(r, c, k int) bool // k is the index of the letter to match
    dfs = func(r, c, k int) bool {
        if k == len(word) {
            return true // GOAL: all the letters matched
        }
        if r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[k] {
            // out of the board, a different letter, or a marked cell
            return false
        }
        board[r][c] = '#' // MARK: '#' is not a letter, so it never matches
        // EXPLORE the four neighbors. The || operator stops at the first
        // true.
        found := dfs(r+1, c, k+1) || dfs(r-1, c, k+1) ||
            dfs(r, c+1, k+1) || dfs(r, c-1, k+1)
        // UNMARK: put the letter back for the other paths
        board[r][c] = word[k]
        return found
    }
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if dfs(r, c, 0) { // each cell can be the first letter
                return true
            }
        }
    }
    return false
}
```

### 131. Palindrome Partitioning

[LeetCode 131](https://leetcode.com/problems/palindrome-partitioning/) · Medium

- **Pattern:** Backtracking, cut a string
- **Template:** [[#Template E: Cut a string into parts|E: Cut a string into parts]]
- **Complexity:** time O(n * 2^n), space O(n) for the path and the recursion, without the output
- **Imports for a local file:** `slices`

**Idea.** Choose where the first part ends. If that part is a palindrome, keep it and cut the rest of the string in the same way. When the start index is at the end of the string, the path is one full answer.

**Go lesson.** `s[start:end]` is a substring that shares the memory of `s`, so the slice operation is O(1). The end index is exclusive, so `end` goes up to `len(s)`.

```go
// partition solves LC 131. Time O(n * 2^n), space O(n) without the output.
// Each call chooses the end of the next part. The part must be a
// palindrome.
func partition(s string) [][]string {
    res := [][]string{}
    path := []string{} // the parts chosen so far
    var dfs func(start int)
    dfs = func(start int) {
        if start == len(s) { // GOAL: the parts cover the full string
            // SAVE a copy: the path changes later, and res must not share
            // its memory.
            res = append(res, slices.Clone(path))
            return
        }
        // the part is s[start:end]
        for end := start + 1; end <= len(s); end++ {
            if !isPalindrome(s[start:end]) {
                continue // CHECK: only a valid part can open a branch
            }
            path = append(path, s[start:end]) // CHOOSE this part
            // EXPLORE: cut the rest, from end
            dfs(end)
            path = path[:len(path)-1] // UNDO
        }
    }
    dfs(0)
    return res
}

// isPalindrome compares the two ends and moves to the middle.
func isPalindrome(s string) bool {
    for l, r := 0, len(s)-1; l < r; l, r = l+1, r-1 {
        if s[l] != s[r] {
            return false
        }
    }
    return true
}
```

### 17. Letter Combinations of a Phone Number

[LeetCode 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) · Medium

- **Pattern:** Backtracking, one choice for each position
- **Template:** [[#Template F: One choice for each position, with sets|F: One choice for each position, with sets]]
- **Complexity:** time O(n * 4^n) for n digits, space O(n) for the path and the recursion, without the output

**Idea.** Each digit is one position, and its letters are the choices for that position. Choose a letter, go to the next digit, then undo. No rule connects two positions, so this problem needs no check before a choice.

**Go lesson.** `string(path)` copies the bytes into a new string. So a save of `string(path)` is safe, and it does not need `slices.Clone`.

```go
// letterCombinations solves LC 17. Time O(n * 4^n) for n digits.
// Position pos of the answer comes from digit pos. A digit has 3 or 4
// letters.
func letterCombinations(digits string) []string {
    if digits == "" {
        return []string{} // LeetCode wants an empty list here, not [""]
    }
    // The index is the digit. Digits 0 and 1 have no letters.
    letters := []string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
    res := []string{}
    path := make([]byte, 0, len(digits)) // the letters chosen so far
    var dfs func(pos int)
    dfs = func(pos int) {
        if pos == len(digits) { // GOAL: one letter for each digit
            // SAVE: string(path) makes a copy of the bytes
            res = append(res, string(path))
            return
        }
        options := letters[digits[pos]-'0'] // '2' - '0' = 2
        for i := 0; i < len(options); i++ {
            // CHOOSE a letter for this position
            path = append(path, options[i])
            dfs(pos + 1)              // EXPLORE the next digit
            path = path[:len(path)-1] // UNDO
        }
    }
    dfs(0)
    return res
}
```

### 51. N-Queens

[LeetCode 51](https://leetcode.com/problems/n-queens/) · Hard

- **Pattern:** Backtracking with constraint sets
- **Template:** [[#Template F: One choice for each position, with sets|F: One choice for each position, with sets]]
- **Complexity:** time O(n!), space O(n²) for the board, without the output
- **Imports for a local file:** `strings`

**Idea.** Put one queen in each row, from the top row down. A column is free when no queen is in that column or on its two diagonals. Three sets answer that question in O(1): the column c, the diagonal r+c and the diagonal r-c.

**Go lesson.** A string cannot change, so the board is a `[][]byte`. `string(board[r])` copies one row into a new string when a solution is complete.

```go
// solveNQueens solves LC 51. Time O(n!), space O(n²) without the output.
// Each row gets one queen. Three sets tell in O(1) if a cell is attacked.
func solveNQueens(n int) [][]string {
    board := make([][]byte, n)
    for r := 0; r < n; r++ {
        // one row of n dots, as bytes
        board[r] = []byte(strings.Repeat(".", n))
    }
    cols := make([]bool, n) // cols[c]: a queen is in column c
    // diag[r+c]: r+c is the same for all the cells of one "/" line
    diag := make([]bool, 2*n)
    // anti[r-c+n]: r-c is the same for one "\" line; +n keeps it >= 0
    anti := make([]bool, 2*n)
    res := [][]string{}

    var dfs func(r int)
    dfs = func(r int) {
        if r == n { // GOAL: each row has a queen
            rows := make([]string, n)
            for i := 0; i < n; i++ {
                // SAVE: string() copies the bytes of the row
                rows[i] = string(board[i])
            }
            res = append(res, rows)
            return
        }
        for c := 0; c < n; c++ {
            if cols[c] || diag[r+c] || anti[r-c+n] {
                continue // CHECK: a queen attacks this cell
            }
            // PLACE the queen
            cols[c], diag[r+c], anti[r-c+n] = true, true, true
            board[r][c] = 'Q'
            dfs(r + 1) // EXPLORE the next row
            board[r][c] = '.'
            // REMOVE the queen
            cols[c], diag[r+c], anti[r-c+n] = false, false, false
        }
    }
    dfs(0)
    return res
}
```

---

[[wiki/neetcode-150/09-heap-priority-queue|← Heap and Priority Queue]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/11-graphs|Graphs →]]
