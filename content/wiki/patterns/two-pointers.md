---
title: "Two Pointers Pattern"
tags:
  - wiki
  - patterns
  - two-pointers
  - palindrome
  - sorted-array
date_created: 2026-04-04
date_modified: 2026-04-04
sources:
  - "[[sources/leetcode/2026-04-04-longest-palindromic-substring]]"
---

# Two Pointers Pattern

Use two pointers to traverse a data structure in a coordinated way, reducing brute-force O(n²) approaches to O(n).

## Recognition Signals

> [!tip] Use this pattern when you see:
> - A **sorted** array/string and you need to find a pair
> - "Find two elements that sum to X" in a sorted array
> - **Palindrome** checking or finding
> - Removing duplicates from a sorted array in-place
> - Container with most water / trapping rain water
> - Any problem where processing from **both ends** toward the middle helps
> - **Expand from center** — a variant where pointers move outward

## Variants

Two pointers isn't a single technique — it's a family of approaches. The variant you need depends on the problem structure.

### 1. Converging Pointers (left + right moving inward)

The classic. One pointer at the start, one at the end, moving toward each other.

**Template:**

```go
func twoPointerConverge(arr []int, target int) []int {
    left, right := 0, len(arr)-1
    for left < right {
        sum := arr[left] + arr[right]
        if sum == target {
            return []int{left, right}
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
    return nil // no pair found
}
```

**When to use:** Sorted arrays, pair finding, container problems, palindrome validation.

**Complexity:** O(n) time, O(1) space.

### 2. Expand from Center (pointers moving outward)

Reverse of converging — start at a center point and expand outward. Crucial for palindrome problems.

**Template:**

```go
func expandFromCenter(s string, left, right int) (int, int) {
    for left >= 0 && right < len(s) && s[left] == s[right] {
        left--
        right++
    }
    // left+1 and right-1 are the palindrome boundaries
    return left + 1, right - 1
}
```

**When to use:** Finding palindromic substrings, expanding a window from a known center.

**Complexity:** O(n) per expansion, O(n²) total when expanding from every center.

### 3. Same-Direction (fast + slow, or read/write)

Both pointers move in the same direction, often at different speeds. Overlaps with [[wiki/patterns/fast-slow-pointers|Fast & Slow Pointers]] for linked lists.

**Template (remove duplicates):**

```go
func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    write := 1 // slow pointer (write position)
    for read := 1; read < len(nums); read++ { // fast pointer
        if nums[read] != nums[read-1] {
            nums[write] = nums[read]
            write++
        }
    }
    return write
}
```

**When to use:** In-place array transformations, removing elements, partitioning.

**Complexity:** O(n) time, O(1) space.

## Full Example: Longest Palindromic Substring (LC-5)

This problem combines the expand-from-center variant with iteration over all possible centers:

```go
func longestPalindrome(s string) string {
    if len(s) < 2 {
        return s
    }
    start, maxLen := 0, 1

    expand := func(left, right int) {
        for left >= 0 && right < len(s) && s[left] == s[right] {
            if right-left+1 > maxLen {
                start = left
                maxLen = right - left + 1
            }
            left--
            right++
        }
    }

    for i := 0; i < len(s); i++ {
        expand(i, i)   // odd-length palindromes (single center)
        expand(i, i+1) // even-length palindromes (double center)
    }
    return s[start : start+maxLen]
}
```

**Why two calls per index:** A palindrome can have a single center character (`"aba"`) or a double center (`"abba"`). Calling `expand(i, i)` handles odd-length; `expand(i, i+1)` handles even-length. This eliminates the need for any special-case logic.

> [!info] Closure trick
> The `expand` closure captures `start` and `maxLen` from the outer scope. This is idiomatic Go — it avoids returning multiple values from the expansion and keeps the code clean.

## Approach Comparison

| Variant | Use Case | Time | Space |
|---------|----------|------|-------|
| Converging | Sorted pair finding, palindrome validation | O(n) | O(1) |
| Expand from center | Palindromic substrings, expanding windows | O(n²) | O(1) |
| Same-direction | In-place transforms, remove duplicates | O(n) | O(1) |

## Common Pitfalls

> [!warning] Watch out for these
> - **Forgetting even-length palindromes** — always expand from both `(i, i)` and `(i, i+1)`
> - **Off-by-one on converging pointers** — use `left < right` (not `<=`) to avoid processing the same element twice
> - **Sorted array assumption** — converging pointers only work on sorted data. If unsorted, sort first (O(n log n)) or use a hash map instead
> - **Comparing bytes vs runes** — `s[i]` gives bytes in Go. For Unicode, convert to `[]rune` first

## Problem Set

| Problem | Difficulty | Variant | Status |
|---------|-----------|---------|--------|
| [[sources/leetcode/2026-04-04-longest-palindromic-substring\|LC-5: Longest Palindromic Substring]] | Medium | Expand from center | ✅ |
| LC-125: Valid Palindrome | Easy | Converging | ⬜ |
| LC-167: Two Sum II | Medium | Converging | ⬜ |
| LC-11: Container With Most Water | Medium | Converging | ⬜ |
| LC-15: 3Sum | Medium | Converging (nested) | ⬜ |
| LC-26: Remove Duplicates from Sorted Array | Easy | Same-direction | ⬜ |
| LC-42: Trapping Rain Water | Hard | Converging | ⬜ |
| LC-680: Valid Palindrome II | Easy | Converging + skip | ⬜ |
| LC-647: Palindromic Substrings | Medium | Expand from center | ⬜ |
| LC-344: Reverse String | Easy | Converging | ⬜ |

## Related

- [[wiki/patterns/sliding-window|Sliding Window]] — another two-pointer variant where the window slides right
- [[wiki/patterns/fast-slow-pointers|Fast & Slow Pointers]] — same-direction variant for linked lists
- [[wiki/dsa/arrays|Arrays & Strings]] — the data structures these pointers operate on
- [[wiki/dsa/hash-tables|Hash Tables]] — alternative to converging pointers when data is unsorted
