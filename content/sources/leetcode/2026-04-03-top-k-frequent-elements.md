---
title: "LC-0347: Top K Frequent Elements"
source_type: leetcode
source_url: https://leetcode.com/problems/top-k-frequent-elements/
difficulty: medium
tags:
  - source
  - leetcode
  - arrays-and-hashing
  - hash-map
  - bucket-sort
  - top-k
  - heap
date: 2026-04-03
processed: true
compiled_to:
  - "[[wiki/patterns/arrays-and-hashing]]"
  - "[[wiki/patterns/top-k]]"
  - "[[wiki/dsa/hash-tables]]"
  - "[[wiki/dsa/sorting]]"
  - "[[wiki/go/leetcode-snippets]]"
---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order. The answer is guaranteed to be unique.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`

**Follow-up:** Your algorithm's time complexity must be better than `O(n log n)`.

## My Solution (Go)

```go
func topKFrequent(nums []int, k int) []int {
    // Step 1: count each number's frequency
    count := make(map[int]int)
    for _, num := range nums {
        count[num]++
    }
    // Step 2: bucket by frequency (index = frequency count)
    freq := make([][]int, len(nums)+1)
    for num, cnt := range count {
        freq[cnt] = append(freq[cnt], num)
    }
    // Step 3: scan from highest freq down, collect k elements
    result := []int{}
    for i := len(freq) - 1; i >= 0 && len(result) < k; i-- {
        result = append(result, freq[i]...)
    }
    return result[:k]
}
```

## Approach

Bucket sort approach:
1. Count frequencies with a hash map — O(n)
2. Create an array of buckets where index = frequency, value = list of numbers with that frequency
3. Walk backwards from highest frequency, collecting elements until we have k

This avoids the O(n log k) heap approach entirely by exploiting the fact that frequency is bounded by array length.

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
- The bucket array size is `len(nums)+1` because the maximum possible frequency equals the array length
- `result[:k]` handles the case where the last bucket appended more elements than needed
- Alternative approaches: min-heap (O(n log k)), quickselect (O(n) avg, O(n²) worst)
