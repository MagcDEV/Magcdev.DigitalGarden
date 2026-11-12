---
title: "NeetCode 150, stage 15: Greedy"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - greedy
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 15: Greedy

[[wiki/neetcode-150/14-dp-2d|← 2-D Dynamic Programming]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/16-intervals|Intervals →]]

A greedy algorithm makes the best local choice at each step and never goes back. This stage trains you to find that choice and to say why it is safe. Most answers are one pass with one or two variables, so the proof is the hard part, not the code.

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/15-greedy#53. Maximum Subarray\|53. Maximum Subarray]] | Medium | Kadane's running sum | [[wiki/neetcode-150/15-greedy#Template A: Running sum with a reset\|A: Running sum with a reset]] |
| 2 | [[wiki/neetcode-150/15-greedy#55. Jump Game\|55. Jump Game]] | Medium | Greedy farthest reach | [[wiki/neetcode-150/15-greedy#Template B: Farthest reach\|B: Farthest reach]] |
| 3 | [[wiki/neetcode-150/15-greedy#45. Jump Game II\|45. Jump Game II]] | Medium | Greedy levels, as in BFS | [[wiki/neetcode-150/15-greedy#Template B: Farthest reach\|B: Farthest reach]] |
| 4 | [[wiki/neetcode-150/15-greedy#134. Gas Station\|134. Gas Station]] | Medium | Greedy running total with a reset | [[wiki/neetcode-150/15-greedy#Template A: Running sum with a reset\|A: Running sum with a reset]] |
| 5 | [[wiki/neetcode-150/15-greedy#846. Hand of Straights\|846. Hand of Straights]] | Medium | Sort, then take the smallest first | [[wiki/neetcode-150/15-greedy#Template C: Sort, then take the smallest first\|C: Sort, then take the smallest first]] |
| 6 | [[wiki/neetcode-150/15-greedy#1899. Merge Triplets to Form Target Triplet\|1899. Merge Triplets to Form Target Triplet]] | Medium | Greedy filter, then combine | [[wiki/neetcode-150/15-greedy#Template D: Filter, then combine\|D: Filter, then combine]] |
| 7 | [[wiki/neetcode-150/15-greedy#763. Partition Labels\|763. Partition Labels]] | Medium | Last index, then extend the end | [[wiki/neetcode-150/15-greedy#Template E: Last index, then extend the end\|E: Last index, then extend the end]] |
| 8 | [[wiki/neetcode-150/15-greedy#678. Valid Parenthesis String\|678. Valid Parenthesis String]] | Medium | Greedy range of open counts | [[wiki/neetcode-150/15-greedy#Template F: Range of possible counts\|F: Range of possible counts]] |

## Templates to memorize

### Template A: Running sum with a reset

> [!tip] Signal
> The problem asks for the best contiguous sum, or for a start point on a circle. A running total that goes below zero is of no use to the items after it.

```go
// TEMPLATE A: running sum with a reset. A sum below zero cannot help the
// items after it.
func bestRunSum(nums []int) int {
    // not 0: the answer is negative when all the items are negative
    best := nums[0]
    sum := 0
    for _, x := range nums {
        if sum < 0 { // 1. RESET: drop a prefix that makes the sum smaller
            sum = 0
        }
        sum += x              // 2. ADD the item
        best = max(best, sum) // 3. KEEP the best sum
    }
    return best
}

// The same shape with a start index. When the sum goes below zero at i,
// no start from the old start to i can work, so the next candidate is i+1.
func firstGoodStart(gain []int) int {
    start, sum := 0, 0
    for i, g := range gain {
        sum += g
        if sum < 0 {
            start, sum = i+1, 0 // RESET the sum and move the start
        }
    }
    return start
}
```

The moves are RESET, ADD, then KEEP. Start `best` with the first item and not with 0. If all the items are negative, the answer is negative too. For a circle, the reset also moves the start to `i+1`.

> [!quote] Say it
> "A negative running sum can only hurt what comes next, so I drop it and start again. One pass, O(n) time and O(1) space."

### Template B: Farthest reach

> [!tip] Signal
> Each item tells you how far you can go from its index. The problem asks "can you reach the end" or "in how few jumps".

```go
// TEMPLATE B: farthest reach. Do not build the path. Keep the farthest
// index in reach.
func canReachEnd(jumps []int) bool {
    farthest := 0
    for i := 0; i < len(jumps); i++ {
        if i > farthest { // 1. CHECK: index i is out of reach
            return false
        }
        farthest = max(farthest, i+jumps[i]) // 2. EXTEND the reach
    }
    return true
}

// To count the jumps, read the indexes as BFS levels. The level ends at
// end.
func fewestJumps(jumps []int) int {
    count, end, farthest := 0, 0, 0
    for i := 0; i < len(jumps)-1; i++ { // stop before the last index
        farthest = max(farthest, i+jumps[i]) // EXTEND the next level
        // LEVEL DONE: jump, and start the next level
        if i == end {
            count++
            end = farthest
        }
    }
    return count
}
```

The moves are CHECK, then EXTEND. To count the jumps, add LEVEL DONE: when the scan reaches the end of the level, count one jump. Stop that loop before the last index. If you do not, the code counts one jump too many.

> [!quote] Say it
> "I don't need the path, only the farthest index I can reach. For the minimum jumps I treat the indexes as BFS levels. It's O(n) time and O(1) space."

### Template C: Sort, then take the smallest first

> [!tip] Signal
> The problem asks you to split the items into groups of consecutive values. The smallest item that is left has only one possible role.

```go
// TEMPLATE C: sort, then take the smallest item first. A count map shows
// what is left.
func canSplitIntoRuns(nums []int, size int) bool {
    if len(nums)%size != 0 {
        return false
    }
    count := make(map[int]int, len(nums))
    for _, x := range nums { // 1. COUNT
        count[x]++
    }
    // 2. SORT: the smallest value that is left must start a run
    sort.Ints(nums)
    for _, x := range nums {
        if count[x] == 0 { // earlier runs used all the copies of x
            continue
        }
        // 3. TAKE the run x, x+1, ... x+size-1
        for v := x; v < x+size; v++ {
            if count[v] == 0 {
                return false
            }
            count[v]--
        }
    }
    return true
}
```

The moves are COUNT, SORT, then TAKE. The smallest value that is left has no smaller neighbor. So it must be the first item of a group, and the choice is forced. Skip a value when its count is already zero.

> [!quote] Say it
> "The smallest card left must start a group, so I sort and build each run from there. The sort makes it O(n log n)."

### Template D: Filter, then combine

> [!tip] Signal
> An operation such as `max` only moves values in one direction. Some items can never be in a good answer, and the other items do no harm.

```go
// TEMPLATE D: filter, then combine. Drop the items that can never be in a
// good
// answer. The items that stay are safe to use together.
func canBuild(items [][]int, target []int) bool {
    found := make([]bool, len(target))
    for _, item := range items {
        safe := true
        // 1. FILTER: one bad value drops the item
        for k := 0; k < len(target); k++ {
            if item[k] > target[k] {
                safe = false
            }
        }
        if !safe {
            continue
        }
        // 2. COMBINE: record what the item gives
        for k := 0; k < len(target); k++ {
            if item[k] == target[k] {
                found[k] = true
            }
        }
    }
    for _, ok := range found { // 3. CHECK that each position has a source
        if !ok {
            return false
        }
    }
    return true
}
```

The moves are FILTER, COMBINE, then CHECK. The filter removes each item that breaks the goal. After the filter, it is safe to use all the other items together. So you do not search for the best subset.

> [!quote] Say it
> "A max never goes down, so any triplet above the target is out. I merge all the rest and check that each target value appears."

### Template E: Last index, then extend the end

> [!tip] Signal
> Each letter or value must stay in one part. The problem asks for as many parts as possible.

```go
// TEMPLATE E: last index, then extend the end. Cut when the scan reaches
// the end.
func partSizes(s string) []int {
    var last [26]int
    for i := 0; i < len(s); i++ { // 1. LAST INDEX of each letter
        last[s[i]-'a'] = i
    }
    var sizes []int
    start, end := 0, 0
    for i := 0; i < len(s); i++ {
        end = max(end, last[s[i]-'a']) // 2. EXTEND the end of the part
        // 3. CUT: nothing in the part appears later
        if i == end {
            sizes = append(sizes, end-start+1)
            start = i + 1
        }
    }
    return sizes
}
```

The moves are LAST INDEX, EXTEND, then CUT. The end of the part is the farthest last index of the letters that the scan saw. When the index `i` is equal to the end, cut. This is the interval merge idea with no interval slice.

> [!quote] Say it
> "A part has to hold the last occurrence of every letter in it. I push the end out as I scan and cut when I catch up with it."

### Template F: Range of possible counts

> [!tip] Signal
> A wildcard can have more than one meaning, and a brute-force answer tries each meaning. You only need to know if one valid choice exists.

```go
// TEMPLATE F: range of counts. A wildcard makes the count a range from low
// to high.
func validWithWildcard(s string) bool {
    low, high := 0, 0 // the smallest and the largest possible open count
    for i := 0; i < len(s); i++ {
        switch s[i] {
        case '(':
            low, high = low+1, high+1
        case ')':
            low, high = low-1, high-1
        default: // 1. WIDEN: the wildcard is '(' or ')' or nothing
            low, high = low-1, high+1
        }
        if high < 0 { // 2. FAIL: too many ')' in the best case
            return false
        }
        low = max(low, 0) // 3. CLAMP: a count is never negative
    }
    return low == 0
}
```

The moves are WIDEN, FAIL, then CLAMP. Keep the smallest and the largest possible count, not one count. Fail when `high` goes below zero. Clamp `low` at zero, because a negative count is not a valid choice.

> [!quote] Say it
> "With a star the open count is a range, so I track its low and high ends. It's valid if high never drops below zero and low can end at zero."

> [!warning] Mistakes in this stage
> - `best := 0` is wrong for Kadane when all the items are negative. Start with `nums[0]`.
> - `sort.Ints` sorts the slice in place, so the caller sees the new order. Copy the slice first if the caller needs the old order.
> - In Jump Game II, the loop condition is `i < len(nums)-1`. With `i < len(nums)`, the code can count one more jump.
> - A greedy choice needs a reason. Say why the local choice is safe before you write the code.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 53. Maximum Subarray

[LeetCode 53](https://leetcode.com/problems/maximum-subarray/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Kadane's running sum
> - **Template:** [[#Template A: Running sum with a reset|A: Running sum with a reset]]

> [!tip]- Step 2: the idea
> **Idea.** Keep the best sum of a subarray that ends at the current item. If the running sum is negative, it cannot help the next item, so start again from zero.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** The built-in `max` (Go 1.21) replaces the `if` that updates the best value.

> [!example]- Step 3: the Go solution
> ```go
> // maxSubArray solves LC 53. Time O(n), space O(1).
> // This is Kadane's algorithm: a negative running sum never helps,
> // so drop
> // it.
> func maxSubArray(nums []int) int {
>     // not 0: when all the values are negative, the answer is
>     // negative
>     best := nums[0]
>     // the best sum of a subarray that ends at the previous item
>     sum := 0
>     for _, x := range nums {
>         // RESET: a negative prefix makes each later sum smaller
>         if sum < 0 {
>             sum = 0
>         }
>         sum += x              // ADD: the subarray now ends at x
>         best = max(best, sum) // KEEP the best sum
>     }
>     return best
> }
> ```

### 55. Jump Game

[LeetCode 55](https://leetcode.com/problems/jump-game/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Greedy farthest reach
> - **Template:** [[#Template B: Farthest reach|B: Farthest reach]]

> [!tip]- Step 2: the idea
> **Idea.** Keep the farthest index that you can reach. If the loop arrives at an index after that reach, the end is not reachable.
>
> **Complexity.** Time O(n), space O(1).

> [!example]- Step 3: the Go solution
> ```go
> // canJump solves LC 55. Time O(n), space O(1).
> // You do not need the path. You only need the farthest index that
> // some path
> // reaches.
> func canJump(nums []int) bool {
>     farthest := 0 // the farthest index that is reachable so far
>     for i := 0; i < len(nums); i++ {
>         // CHECK: no jump reaches index i, so the end is out of
>         // reach
>         if i > farthest {
>             return false
>         }
>         // EXTEND: the best jump from index i
>         farthest = max(farthest, i+nums[i])
>     }
>     // the loop reached each index, the last one included
>     return true
> }
> ```

### 45. Jump Game II

[LeetCode 45](https://leetcode.com/problems/jump-game-ii/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Greedy levels, as in BFS
> - **Template:** [[#Template B: Farthest reach|B: Farthest reach]]

> [!tip]- Step 2: the idea
> **Idea.** The indexes that k jumps can reach make one level, as in BFS. Scan a level, keep the farthest index of the next level, and count one jump at the end of each level.
>
> **Complexity.** Time O(n), space O(1).

> [!example]- Step 3: the Go solution
> ```go
> // jump solves LC 45. Time O(n), space O(1).
> // The indexes up to end are the level that the current number of
> // jumps
> // reaches.
> // The problem guarantees that the last index is reachable.
> func jump(nums []int) int {
>     jumps := 0
>     end := 0      // the last index of the current level
>     farthest := 0 // the farthest index that one more jump reaches
>     // Stop before the last index: a jump from the last index is not
>     // necessary.
>     for i := 0; i < len(nums)-1; i++ {
>         farthest = max(farthest, i+nums[i]) // EXTEND the next level
>         // LEVEL DONE: all its indexes are scanned
>         if i == end {
>             jumps++        // one more jump is necessary
>             end = farthest // the next level ends here
>         }
>     }
>     return jumps
> }
> ```

### 134. Gas Station

[LeetCode 134](https://leetcode.com/problems/gas-station/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Greedy running total with a reset
> - **Template:** [[#Template A: Running sum with a reset|A: Running sum with a reset]]

> [!tip]- Step 2: the idea
> **Idea.** If the total gas is less than the total cost, there is no answer. If not, an answer exists. When the tank goes below zero at station i, no station from the start to i can be the start, so try i+1.
>
> **Complexity.** Time O(n), space O(1).

> [!example]- Step 3: the Go solution
> ```go
> // canCompleteCircuit solves LC 134. Time O(n), space O(1).
> // One pass keeps two sums: the total for the full circle and the
> // tank since
> // the start.
> func canCompleteCircuit(gas []int, cost []int) int {
>     total := 0 // gas minus cost for the full circle
>     tank := 0  // gas minus cost since the candidate start
>     start := 0 // the candidate start
>     for i := 0; i < len(gas); i++ {
>         // what station i adds after the drive to i+1
>         gain := gas[i] - cost[i]
>         total += gain
>         tank += gain  // ADD
>         if tank < 0 { // RESET: the car stops between i and i+1
>             // A start between the old start and i arrives at i with
>             // less
>             // gas,
>             // so it also fails. The next candidate is i+1.
>             start = i + 1
>             tank = 0
>         }
>     }
>     // the circle costs more gas than the stations give
>     if total < 0 {
>         return -1
>     }
>     // total >= 0, so the last candidate completes the circle
>     return start
> }
> ```

### 846. Hand of Straights

[LeetCode 846](https://leetcode.com/problems/hand-of-straights/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Sort, then take the smallest first
> - **Template:** [[#Template C: Sort, then take the smallest first|C: Sort, then take the smallest first]]

> [!tip]- Step 2: the idea
> **Idea.** The smallest card that is left can only be the first card of a group. So sort the cards, and for each card that is left, take the full run that starts there.
>
> **Complexity.** Time O(n log n), space O(n).
>
> **Go lesson.** `sort.Ints` sorts the slice in place. A count map reads 0 for a missing key, so `count[v] == 0` also means "not there".

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `sort`
>
> ```go
> // isNStraightHand solves LC 846. Time O(n log n), space O(n).
> // A min-heap of the distinct values also works. The sort is shorter
> // to
> // write.
> func isNStraightHand(hand []int, groupSize int) bool {
>     // the groups cannot use all the cards
>     if len(hand)%groupSize != 0 {
>         return false
>     }
>     // COUNT: card value -> copies that are left
>     count := make(map[int]int, len(hand))
>     for _, card := range hand {
>         count[card]++
>     }
>     // SORT: the loop sees the smallest card that is left first
>     sort.Ints(hand)
>
>     for _, card := range hand {
>         // earlier groups used all the copies of this card
>         if count[card] == 0 {
>             continue
>         }
>         // TAKE the run card, card+1, ... card+groupSize-1.
>         // The smallest card has no smaller neighbor, so it must
>         // start a
>         // group.
>         for v := card; v < card+groupSize; v++ {
>             if count[v] == 0 { // the run has a gap
>                 return false
>             }
>             count[v]--
>         }
>     }
>     return true
> }
> ```

### 1899. Merge Triplets to Form Target Triplet

[LeetCode 1899](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Greedy filter, then combine
> - **Template:** [[#Template D: Filter, then combine|D: Filter, then combine]]

> [!tip]- Step 2: the idea
> **Idea.** A merge takes the maximum, so a value never goes down. Drop each triplet that has a value above the target. Then the target is possible when the other triplets give each of its three values.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `[3]bool` is an array, not a slice. It has a fixed size, starts as three `false` values, and needs no `make`.

> [!example]- Step 3: the Go solution
> ```go
> // mergeTriplets solves LC 1899. Time O(n), space O(1).
> // The triplets that pass the filter are all safe to merge together.
> func mergeTriplets(triplets [][]int, target []int) bool {
>     // found[k]: a safe triplet has the value target[k] at position
>     // k
>     var found [3]bool
>     for _, t := range triplets {
>         // FILTER: max never makes a value smaller. A triplet with a
>         // value
>         // above the target puts the result above the target for
>         // good.
>         if t[0] > target[0] || t[1] > target[1] || t[2] > target[2] {
>             continue
>         }
>         // COMBINE: this triplet is safe. Record the positions where
>         // it is
>         // equal.
>         for k := 0; k < 3; k++ {
>             if t[k] == target[k] {
>                 found[k] = true
>             }
>         }
>     }
>     // CHECK: each position has a source
>     return found[0] && found[1] && found[2]
> }
> ```

### 763. Partition Labels

[LeetCode 763](https://leetcode.com/problems/partition-labels/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Last index, then extend the end
> - **Template:** [[#Template E: Last index, then extend the end|E: Last index, then extend the end]]

> [!tip]- Step 2: the idea
> **Idea.** A part must contain the last occurrence of each letter in it. Record the last index of each letter. Then scan and move the end of the part to the farthest last index. Cut when the scan reaches the end.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `s[i]` is a byte, and `s[i]-'a'` is an index from 0 to 25. A `[26]int` array replaces a map for lower-case letters.

> [!example]- Step 3: the Go solution
> ```go
> // partitionLabels solves LC 763. Time O(n), space O(1) without the
> // result.
> // To cut as early as possible gives the largest number of parts.
> func partitionLabels(s string) []int {
>     var last [26]int // LAST INDEX: the last position of each letter
>     for i := 0; i < len(s); i++ {
>         // a later position overwrites an earlier one
>         last[s[i]-'a'] = i
>     }
>
>     var sizes []int    // a nil slice: append makes the memory
>     start, end := 0, 0 // the current part is s[start..end]
>     for i := 0; i < len(s); i++ {
>         // EXTEND: the part must include this letter's last index
>         end = max(end, last[s[i]-'a'])
>         // CUT: no letter of the part appears after i
>         if i == end {
>             sizes = append(sizes, end-start+1)
>             start = i + 1 // the next part starts after the cut
>         }
>     }
>     return sizes
> }
> ```

### 678. Valid Parenthesis String

[LeetCode 678](https://leetcode.com/problems/valid-parenthesis-string/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Greedy range of open counts
> - **Template:** [[#Template F: Range of possible counts|F: Range of possible counts]]

> [!tip]- Step 2: the idea
> **Idea.** A star gives three choices, so the number of open brackets is a range, not one number. Keep the smallest and the largest possible count. The string is valid when the largest never goes below zero and the smallest can end at zero.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** A `switch` on a byte needs no `break`. Each `case` stops by itself, and `default` takes the star.

> [!example]- Step 3: the Go solution
> ```go
> // checkValidString solves LC 678. Time O(n), space O(1).
> // low and high are the smallest and the largest possible number of
> // open
> // brackets.
> func checkValidString(s string) bool {
>     low, high := 0, 0
>     for i := 0; i < len(s); i++ {
>         switch s[i] {
>         case '(':
>             low++ // one more open bracket in each case
>             high++
>         case ')':
>             low-- // one open bracket less in each case
>             high--
>         default: // '*' WIDENS the range:
>             low--  // as ')' it closes one bracket
>             high++ // as '(' it opens one bracket
>         }
>         // FAIL: too many ')' even when each star is '('
>         if high < 0 {
>             return false
>         }
>         // CLAMP: a count below zero is not a valid choice
>         if low < 0 {
>             low = 0
>         }
>     }
>     // zero open brackets must be one of the possible counts
>     return low == 0
> }
> ```

---

[[wiki/neetcode-150/14-dp-2d|← 2-D Dynamic Programming]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/16-intervals|Intervals →]]
