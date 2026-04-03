---
title: "Sorting Algorithms"
tags:
  - wiki
  - dsa
  - sorting
  - bucket-sort
date_created: 2026-04-03
date_modified: 2026-04-03
sources:
  - "[[sources/leetcode/2026-04-03-top-k-frequent-elements]]"
---

# Sorting Algorithms

## Overview

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n) | Yes |

Where `k` is the range of input values for counting/bucket sort.

## Go's Built-in Sort

```go
import "sort"

// Sort a slice of ints
sort.Ints(nums)

// Sort with custom comparator (Go 1.21+)
slices.SortFunc(items, func(a, b Item) int {
    return a.Priority - b.Priority
})

// Sort with custom comparator (pre-1.21)
sort.Slice(items, func(i, j int) bool {
    return items[i].Priority < items[j].Priority
})
```

Go's `sort.Sort` uses **introsort** (quicksort + heapsort fallback), guaranteeing O(n log n) worst case.

## Bucket Sort

Bucket sort distributes elements into buckets by some key, then collects them in order. It achieves O(n) when the key space is bounded.

```go
// Example: sort elements by frequency using bucket sort
freq := make([][]int, maxFreq+1) // index = frequency
for val, count := range freqMap {
    freq[count] = append(freq[count], val)
}
// Scan buckets in desired order
for i := len(freq) - 1; i >= 0; i-- {
    for _, val := range freq[i] {
        // process in descending frequency order
    }
}
```

> [!info] When to Use Bucket Sort
> - The "key" you're sorting by has a known, bounded range
> - You need O(n) time (comparison sorts can't beat O(n log n))
> - Common in: frequency problems, digit-based sorting, distributing into ranges

Used in: [[wiki/patterns/top-k|Top-K Elements]] (bucket by frequency)

## Related

- [[wiki/dsa/heaps|Heaps & Priority Queues]] — partial sorting via heap
- [[wiki/dsa/arrays|Arrays & Strings]] — in-place sorting techniques
- [[wiki/patterns/merge-intervals|Merge Intervals]] — sort by start time first
