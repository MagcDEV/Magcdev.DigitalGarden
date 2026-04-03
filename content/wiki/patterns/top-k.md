---
title: "Top-K Elements Pattern"
tags:
  - wiki
  - patterns
  - top-k
  - heap
  - bucket-sort
date_created: 2026-04-03
date_modified: 2026-04-03
sources:
  - "[[sources/leetcode/2026-04-03-top-k-frequent-elements]]"
---

# Top-K Elements Pattern

Find the K largest, smallest, or most frequent elements in a collection.

## Recognition Signals

> [!tip] Use this pattern when you see:
> - "K largest / smallest / most frequent"
> - "K closest points"
> - "K most common"
> - "Kth largest element"
> - Any problem asking for a subset ranked by some metric

## Three Approaches

### 1. Bucket Sort — O(n) time, O(n) space

**Best when:** frequency is bounded (e.g., frequency ≤ array length). This is the optimal approach for "top K frequent" problems.

```go
func topKFrequent(nums []int, k int) []int {
    // Count frequencies
    count := make(map[int]int)
    for _, num := range nums {
        count[num]++
    }

    // Bucket by frequency: index = freq, value = elements with that freq
    freq := make([][]int, len(nums)+1)
    for num, cnt := range count {
        freq[cnt] = append(freq[cnt], num)
    }

    // Scan from highest frequency down
    result := []int{}
    for i := len(freq) - 1; i >= 0 && len(result) < k; i-- {
        result = append(result, freq[i]...)
    }
    return result[:k]
}
```

**Why it works:** The maximum possible frequency of any element is `len(nums)`, so we can use frequency as an array index. Walking backwards gives us elements in descending frequency order.

### 2. Min-Heap — O(n log k) time, O(k) space

**Best when:** K is much smaller than N, or you need a streaming solution.

```go
import "container/heap"

type Item struct {
    val  int
    freq int
}

type MinHeap []Item

func (h MinHeap) Len() int            { return len(h) }
func (h MinHeap) Less(i, j int) bool  { return h[i].freq < h[j].freq }
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x any)         { *h = append(*h, x.(Item)) }
func (h *MinHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func topKFrequent(nums []int, k int) []int {
    count := make(map[int]int)
    for _, num := range nums {
        count[num]++
    }

    h := &MinHeap{}
    for num, freq := range count {
        heap.Push(h, Item{num, freq})
        if h.Len() > k {
            heap.Pop(h) // remove least frequent
        }
    }

    result := make([]int, k)
    for i := 0; i < k; i++ {
        result[i] = heap.Pop(h).(Item).val
    }
    return result
}
```

**Why min-heap, not max-heap:** We maintain a heap of size K. The min-heap lets us efficiently evict the least frequent element when the heap exceeds size K.

### 3. Quickselect — O(n) average, O(n²) worst

**Best when:** you need average-case O(n) without extra space for buckets. Same idea as `nth_element` in C++. Rarely the best choice in interviews because worst case is bad and the code is complex.

## Approach Comparison

| Approach | Time | Space | When to Use |
|----------|------|-------|-------------|
| Bucket sort | O(n) | O(n) | Bounded frequency range (most interview problems) |
| Min-heap | O(n log k) | O(k) | K << N, streaming data, unbounded values |
| Quickselect | O(n) avg | O(1) extra | Need in-place, accept worst-case risk |

## Problem Set

| Problem | Difficulty | Approach | Status |
|---------|-----------|----------|--------|
| [[sources/leetcode/2026-04-03-top-k-frequent-elements\|LC-347: Top K Frequent Elements]] | Medium | Bucket sort | ✅ |
| LC-215: Kth Largest Element in an Array | Medium | Min-heap / Quickselect | ⬜ |
| LC-692: Top K Frequent Words | Medium | Min-heap (custom comparator) | ⬜ |
| LC-973: K Closest Points to Origin | Medium | Max-heap / Quickselect | ⬜ |
| LC-703: Kth Largest Element in a Stream | Easy | Min-heap of size K | ⬜ |
| LC-658: Find K Closest Elements | Medium | Binary search + two pointers | ⬜ |
| LC-895: Maximum Frequency Stack | Hard | Frequency map + stack per freq | ⬜ |

## Related

- [[wiki/dsa/hash-tables|Hash Tables]] — frequency counting is always step 1
- [[wiki/dsa/heaps|Heaps & Priority Queues]] — Go's `container/heap` interface
- [[wiki/dsa/sorting|Sorting Algorithms]] — bucket sort as a technique
- [[wiki/patterns/two-heaps|Two Heaps]] — related heap pattern for median finding
