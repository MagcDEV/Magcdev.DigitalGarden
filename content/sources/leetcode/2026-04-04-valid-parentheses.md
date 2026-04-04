---
title: "LC-0020: Valid Parentheses"
source_type: leetcode
source_url: https://leetcode.com/problems/valid-parentheses/
difficulty: easy
tags:
  - source
  - leetcode
  - stack
  - string
date: 2026-04-04
processed: true
compiled_to:
  - "[[wiki/patterns/stack-based]]"
  - "[[wiki/dsa/stacks]]"
  - "[[wiki/go/leetcode-snippets]]"
  - "[[wiki/patterns/index]]"
  - "[[wiki/dsa/index]]"
---

# LC-0020: Valid Parentheses

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of closing bracket.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "([)]"
Output: false
```

**Constraints:**
- 1 ≤ s.length ≤ 10^4
- s consists of parentheses only '()[]{}'

## My Solution (Go)

```go
func isValid(s string) bool {
    stack := []rune{}
    pairs := map[rune]rune{')': '(', '}': '{', ']': '['}
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
}
```

## Approach

**Stack-based matching:**
- Use a stack to track opening brackets as we encounter them
- When we see a closing bracket, pop from the stack and verify it matches
- Use a map to quickly look up the expected opening bracket for each closing bracket
- At the end, the stack must be empty (all brackets closed)

**Why this works:**
- Brackets must be closed in LIFO order (last opened = first closed)
- A stack naturally enforces this ordering
- The map eliminates the need for if-else chains when checking pair compatibility

## Complexity Analysis

| Metric | Value |
|--------|-------|
| Time Complexity | O(n) - single pass through string, stack ops are O(1) |
| Space Complexity | O(n) - worst case: all opening brackets e.g. "(((" |

## Notes

- Edge case: empty string after stripping opening brackets → we check `len(stack) == 0` at end
- The map approach is more scalable than hardcoded if-else chains
- In Go, slicing to pop (`stack[:len(stack)-1]`) is cleaner than manual pop functions
- The check `len(stack) == 0` before popping prevents panic on mismatched closing bracket
