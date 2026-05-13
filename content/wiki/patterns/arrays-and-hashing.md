---
title: "Arrays & Hashing Pattern"
tags:
  - wiki
  - patterns
  - arrays
  - hash-map
  - hash-set
date_created: 2026-05-13
date_modified: 2026-05-13
sources:
  - "[[sources/leetcode/2026-04-03-top-k-frequent-elements]]"
---

# Arrays & Hashing Pattern

The foundational interview pattern: solve array problems by trading **space for time** with a hash map or hash set. Most "find / count / group / dedupe" problems on unsorted arrays collapse to O(n) once you allow yourself O(n) auxiliary memory.

## Recognition Signals

> [!tip] Use this pattern when you see:
> - "Find a pair / triple that sums to..." → hash map of complements
> - "Does X contain duplicates?" → hash set membership
> - "Are X and Y anagrams / permutations?" → character frequency map
> - "Group / cluster items by some key" → `map[key][]item`
> - "Count occurrences" or "most frequent" → frequency map
> - "Product / prefix / suffix without division" → precomputed arrays
> - "Longest consecutive sequence / streak" → hash set + linear scan from boundaries
> - Anything with the brute force being O(n²) nested loops over an array

## Core Techniques

### 1. Frequency map — `map[T]int`

Count how many times each element appears. The foundation of anagrams, top-K, majority element, etc.

```go
count := make(map[int]int)
for _, x := range nums {
    count[x]++
}
```

### 2. Complement lookup — `map[T]int` (value → index)

For "find pair that sums to target", store seen values keyed by what would complete the pair.

```go
seen := make(map[int]int)
for i, x := range nums {
    if j, ok := seen[target-x]; ok {
        return []int{j, i}
    }
    seen[x] = i
}
```

### 3. Group by key — `map[K][]V`

Partition items into buckets keyed by something derived (sorted string, frequency, signature).

```go
groups := make(map[string][]string)
for _, s := range strs {
    key := canonicalize(s)
    groups[key] = append(groups[key], s)
}
```

### 4. Hash set for membership — `map[T]struct{}`

When you only need "is X present?" use a set. `struct{}` takes zero bytes vs. `bool`.

```go
set := make(map[int]struct{})
for _, x := range nums {
    set[x] = struct{}{}
}
_, exists := set[42]
```

### 5. Prefix / suffix arrays — no hashing, just precomputation

For "result at i depends on everything except i", build prefix and suffix scans in two passes.

```go
prefix := make([]int, n)
suffix := make([]int, n)
// fill them, then combine
```

## Approach Comparison

| Technique | When to use | Time | Space |
|-----------|------------|------|-------|
| Frequency map | Counting, anagrams, majority | O(n) | O(k) unique |
| Complement lookup | Pair sum problems | O(n) | O(n) |
| Group by key | Bucket / cluster | O(n · k) | O(n) |
| Hash set | Membership, deduplication | O(n) | O(n) |
| Prefix/suffix arrays | "All except self" patterns | O(n) | O(n) |
| Sort + dedupe | When O(n log n) is acceptable and you want O(1) extra | O(n log n) | O(1) |

## Problem Set

| #   | Problem | Difficulty | Core Technique | Status |
|-----|---------|-----------|----------------|--------|
| 1   | Two Sum | Easy | Complement lookup (hash map) | ⬜ |
| 217 | Contains Duplicate | Easy | Hash set membership | ⬜ |
| 242 | Valid Anagram | Easy | Frequency map (or sort) | ⬜ |
| 49  | Group Anagrams | Medium | Group by sorted-string key | ⬜ |
| 347 | [[sources/leetcode/2026-04-03-top-k-frequent-elements\|Top K Frequent Elements]] | Medium | Frequency map + bucket sort | ✅ |
| 238 | Product of Array Except Self | Medium | Prefix + suffix products | ⬜ |
| 128 | Longest Consecutive Sequence | Medium | Hash set + start-of-streak scan | ⬜ |
| 36  | Valid Sudoku | Medium | Hash sets per row/col/box | ⬜ |
| 560 | Subarray Sum Equals K | Medium | Prefix sum + frequency map | ⬜ |
| 169 | Majority Element | Easy | Frequency map (or Boyer–Moore) | ⬜ |

## Approach Hints per Problem

> [!abstract] Spoiler-light hints — try the brute force first, then come back
>
> - **LC-1 Two Sum**: store `value → index` as you go; look for `target - x` before inserting.
> - **LC-217 Contains Duplicate**: add to a set; if already there, return true. One pass.
> - **LC-242 Valid Anagram**: same length + same character counts. Either sort both strings or use one `[26]int` frequency array.
> - **LC-49 Group Anagrams**: key each string by its sorted form (or a `[26]int` signature stringified). Group into a `map[string][]string`.
> - **LC-347 Top K Frequent Elements**: count, then bucket sort by frequency — see [[wiki/patterns/top-k|Top-K pattern]] for the three approaches.
> - **LC-238 Product Except Self**: two passes — prefix product left-to-right, then multiply by suffix product right-to-left. O(1) extra space if the output array doesn't count.
> - **LC-128 Longest Consecutive Sequence**: dump into a set; only start counting a streak when `x-1` is NOT in the set (that's the streak's start). O(n) amortized.
> - **LC-36 Valid Sudoku**: 9 sets for rows + 9 for cols + 9 for boxes. Box index: `(r/3)*3 + c/3`.
> - **LC-560 Subarray Sum Equals K**: running prefix sum, count occurrences of `prefix - k` in a `map[int]int`. Seed with `map[0]=1` to count subarrays starting at index 0.
> - **LC-169 Majority Element**: frequency map gives O(n)/O(n). Boyer–Moore voting gives O(n)/O(1) — keep a candidate and a count.

## Go Templates

### Frequency-based anagram check

```go
func isAnagram(s, t string) bool {
    if len(s) != len(t) {
        return false
    }
    var count [26]int
    for i := 0; i < len(s); i++ {
        count[s[i]-'a']++
        count[t[i]-'a']--
    }
    for _, c := range count {
        if c != 0 {
            return false
        }
    }
    return true
}
```

### Prefix sum with frequency map (LC-560 shape)

```go
func subarraySum(nums []int, k int) int {
    prefixCount := map[int]int{0: 1}
    sum, result := 0, 0
    for _, x := range nums {
        sum += x
        if c, ok := prefixCount[sum-k]; ok {
            result += c
        }
        prefixCount[sum]++
    }
    return result
}
```

### Hash set for longest streak (LC-128 shape)

```go
func longestConsecutive(nums []int) int {
    set := make(map[int]struct{}, len(nums))
    for _, x := range nums {
        set[x] = struct{}{}
    }
    best := 0
    for x := range set {
        if _, ok := set[x-1]; ok {
            continue // not the start of a streak
        }
        length := 1
        for {
            if _, ok := set[x+length]; !ok {
                break
            }
            length++
        }
        if length > best {
            best = length
        }
    }
    return best
}
```

## Common Pitfalls

> [!warning] Watch for these
> - **Iteration order on maps is randomized in Go.** Don't depend on it for output — sort or use a slice if you need stability.
> - **`map[K]struct{}` vs `map[K]bool`** — both work as sets, but `struct{}` uses zero bytes. Idiomatic choice for set semantics.
> - **Off-by-one in prefix sums** — seed `prefixCount[0] = 1` so subarrays starting at index 0 are counted.
> - **Anagram with Unicode** — `[26]int` only works for lowercase ASCII. Use `map[rune]int` for general Unicode.
> - **Modifying input** — sorting in place mutates the caller's slice. Copy first if the contract forbids mutation.

## Related

- [[wiki/dsa/hash-tables|Hash Tables]] — the underlying data structure
- [[wiki/dsa/arrays|Arrays & Strings]] — prefix/suffix and slice idioms
- [[wiki/patterns/two-pointers|Two Pointers]] — alternative for sorted-array pair problems
- [[wiki/patterns/sliding-window|Sliding Window]] — when the subarray is contiguous and you need to "shrink" it
- [[wiki/patterns/top-k|Top-K Elements]] — bucket sort variant used by LC-347
