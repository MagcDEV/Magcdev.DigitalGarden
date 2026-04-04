---
title: "Go LeetCode Snippets & Templates"
tags:
  - wiki
  - go
  - leetcode
  - templates
date_created: 2026-04-03
date_modified: 2026-04-04
sources:
  - "[[sources/leetcode/2026-04-03-top-k-frequent-elements]]"
  - "[[sources/leetcode/2026-04-04-valid-parentheses]]"
  - "[[sources/leetcode/2026-04-04-longest-palindromic-substring]]"
---

# Go LeetCode Snippets & Templates

Reusable Go code patterns that come up repeatedly in LeetCode problems.

## Frequency Map

```go
count := make(map[int]int)
for _, num := range nums {
    count[num]++
}
```

Used in: [[wiki/patterns/top-k|Top-K Elements]], [[wiki/patterns/sliding-window|Sliding Window]]

## Min / Max Helpers

Go has no built-in generic min/max before 1.21. For older versions:

```go
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

From Go 1.21+, use the built-in `min()` and `max()`.

## Heap Interface Boilerplate

Go's `container/heap` requires implementing the `heap.Interface`:

```go
type MinHeap []int

func (h MinHeap) Len() int            { return len(h) }
func (h MinHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x any)         { *h = append(*h, x.(any).(int)) }
func (h *MinHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}
```

> [!warning] Common Mistake
> `Push` and `Pop` use pointer receivers (`*MinHeap`), but `Len`, `Less`, and `Swap` use value receivers (`MinHeap`). Getting this wrong causes subtle bugs.

Used in: [[wiki/patterns/top-k|Top-K Elements]], [[wiki/patterns/two-heaps|Two Heaps]], [[wiki/patterns/k-way-merge|K-Way Merge]]

## Bucket Sort by Frequency

```go
freq := make([][]int, len(nums)+1)
for val, cnt := range count {
    freq[cnt] = append(freq[cnt], val)
}
for i := len(freq) - 1; i >= 0; i-- {
    // freq[i] contains all values that appeared i times
}
```

Used in: [[wiki/patterns/top-k|Top-K Elements]]

## Slice as Stack

```go
stack := []int{}
stack = append(stack, val)          // push
top := stack[len(stack)-1]          // peek
stack = stack[:len(stack)-1]        // pop
```

### Bracket Matching with Map

For problems like Valid Parentheses, use a map to eliminate if-else chains:

```go
pairs := map[rune]rune{')': '(', '}': '{', ']': '['}
stack := []rune{}

for _, ch := range s {
    if ch == '(' || ch == '{' || ch == '[' {
        stack = append(stack, ch)
    } else {
        if len(stack) == 0 || stack[len(stack)-1] != pairs[ch] {
            return false
        }
        stack = stack[:len(stack)-1]
    }
}
return len(stack) == 0
```

Used in: [[wiki/patterns/stack-based|Stack-Based Pattern]], LC-20 (Valid Parentheses)

## Expand from Center (Palindromes)

```go
expand := func(s string, left, right int) (int, int) {
    for left >= 0 && right < len(s) && s[left] == s[right] {
        left--
        right++
    }
    return left + 1, right - 1
}

// For each index, check both odd and even palindromes
for i := 0; i < len(s); i++ {
    lo1, hi1 := expand(s, i, i)   // odd-length
    lo2, hi2 := expand(s, i, i+1) // even-length
}
```

Used in: [[wiki/patterns/two-pointers|Two Pointers (expand from center)]], LC-5 (Longest Palindromic Substring), LC-647 (Palindromic Substrings)

## Queue via Slice

```go
queue := []int{}
queue = append(queue, val)          // enqueue
front := queue[0]                   // peek
queue = queue[1:]                   // dequeue (note: doesn't free memory)
```

> [!tip] For performance-critical queues, use a ring buffer or `container/list`.

## Related

- [[wiki/go/slices|Slices]] — internals and gotchas
- [[wiki/go/go-vs-python-dsa|Go vs Python for DSA]] — trade-offs
- [[wiki/dsa/hash-tables|Hash Tables]] — Go map patterns
