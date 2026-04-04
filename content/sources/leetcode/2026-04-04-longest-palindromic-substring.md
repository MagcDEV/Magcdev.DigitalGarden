---
title: "LC-0005: Longest Palindromic Substring"
source_type: leetcode
source_url: https://leetcode.com/problems/longest-palindromic-substring/
difficulty: medium
tags:
  - source
  - leetcode
  - two-pointers
  - string
  - dynamic-programming
  - expand-from-center
date: 2026-04-04
processed: true
compiled_to:
  - "[[wiki/patterns/two-pointers]]"
  - "[[wiki/dsa/arrays]]"
  - "[[wiki/go/leetcode-snippets]]"
---

## Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

**Constraints:**
- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters

**Examples:**
- Input: `"babad"` → Output: `"bab"` (or `"aba"`)
- Input: `"cbbd"` → Output: `"bb"`

## My Solution (Go)

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
        expand(i, i)   // odd-length palindromes
        expand(i, i+1) // even-length palindromes
    }
    return s[start : start+maxLen]
}
```

## Approach

Expand-from-center technique:
1. For each character in the string, treat it as the center of a potential palindrome
2. Expand outward while characters match on both sides
3. Handle both odd-length (single center) and even-length (two adjacent centers) palindromes
4. Track the longest palindrome found via `start` and `maxLen`

This is a two-pointer variant — two pointers move outward from a center rather than inward from the edges.

## Complexity
- Time: O(n²) — for each of n centers, expansion is O(n) worst case
- Space: O(1) — only tracking start index and max length, no extra data structures

## Notes
- The closure `expand` captures `start` and `maxLen` from the outer scope — idiomatic Go pattern for avoiding repeated return values
- Two calls per index (`expand(i, i)` and `expand(i, i+1)`) cleanly handle both odd and even palindromes without special-casing
- Alternative approaches: DP (O(n²) time, O(n²) space — worse), Manacher's algorithm (O(n) time — optimal but complex, rarely expected in interviews)
- String indexing with `s[i]` is safe here because the problem guarantees ASCII digits and letters only. For Unicode strings, you'd need to work with `[]rune`
