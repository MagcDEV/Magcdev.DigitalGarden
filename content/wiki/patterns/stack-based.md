---
title: "Stack-Based Pattern"
tags:
  - wiki
  - patterns
  - leetcode
  - stack
date_created: 2026-04-04
date_modified: 2026-04-04
sources:
  - "[[sources/leetcode/2026-04-04-valid-parentheses]]"
---

# Stack-Based Pattern

## What is Stack-Based Pattern?

The **stack-based pattern** uses a LIFO (Last-In-First-Out) data structure to solve problems where:
- Elements need to be matched, nested, or processed in reverse order
- You need to remember state and "backtrack" (pop) when conditions change
- Pairs or groups must be validated in a specific order

## Recognition Signals

Use this pattern when you see:

> [!tip] Key Indicators
> - **Parentheses/bracket matching** — Valid parentheses, nested structures
> - **Upcoming greater/smaller elements** — Next greater/smaller element problems
> - **Decreasing/increasing sequences** — Monotonic stack variations
> - **Expression evaluation** — Calculator problems, postfix notation
> - **Undo/backtrack semantics** — Browser history, undo operations

## Template Code (Go)

### Basic Stack Pattern

```go
stack := []T{}  // T is the element type (int, rune, string, etc.)

for _, elem := range input {
    // Decision: push or check
    if shouldPush(elem) {
        stack = append(stack, elem)  // O(1) amortized
    } else {
        // Pop and validate
        if len(stack) == 0 {
            // Handle empty stack
            return false
        }
        top := stack[len(stack)-1]
        stack = stack[:len(stack)-1]  // Pop
        // Process top and elem together
    }
}

// Final validation
return len(stack) == 0  // All elements processed
```

### With Map for O(1) Lookup

For problems like bracket matching, use a map to avoid if-else chains:

```go
pairs := map[rune]rune{
    ')': '(',
    '}': '{',
    ']': '[',
}

for _, ch := range s {
    if isOpening(ch) {
        stack = append(stack, ch)
    } else {
        if len(stack) == 0 || stack[len(stack)-1] != pairs[ch] {
            return false
        }
        stack = stack[:len(stack)-1]
    }
}
```

## Approach Patterns

### 1. Matching/Validation (No Computation)
Check if elements satisfy a property:
- **Valid Parentheses** — Do brackets match in correct order?
- **Valid Parentheses String** — Do valid bracket subsets form a valid string?

**Time:** O(n), **Space:** O(n)

### 2. Next Greater/Smaller Element
For each element, find the next element satisfying a condition:
- **Next Greater Element** — First element to the right that is > current
- **Daily Temperatures** — Days until warmer temperature
- Uses **monotonic stack** (stack stays in increasing/decreasing order)

**Time:** O(n), **Space:** O(n)

### 3. Expression Evaluation
Evaluate infix/postfix expressions:
- **Evaluate Reverse Polish Notation** — Postfix expression evaluation
- **Basic Calculator** — Handles +, -, *, / and parentheses

**Time:** O(n), **Space:** O(n) for operator/operand stacks

### 4. Removing Duplicates/Optimization
Remove elements based on current state:
- **Remove K Digits** — Remove k digits to get smallest number
- **Remove All Adjacent Duplicates** — Iteratively remove "AA" from string
- Uses monotonic stack + greedy

**Time:** O(n), **Space:** O(n)

## Common Gotchas in Go

> [!warning] Go-Specific Issues
> - **Slicing to pop:** `stack[:len(stack)-1]` creates a new slice, doesn't panic if empty — always check `len(stack) > 0` first
> - **Slice capacity vs length:** Popping doesn't reduce capacity; memory is reclaimed when slice goes out of scope
> - **Type assertions:** If storing `interface{}`, cast back to original type (e.g., `val.(int)`)
> - **String iteration:** `for _, ch := range s` gives runes, not bytes; use `s[i]` for byte access if needed

## Problem Set

| # | Problem | Difficulty | Key Insight |
|---|---------|------------|-------------|
| 20 | [[sources/leetcode/2026-04-04-valid-parentheses\|Valid Parentheses]] | Easy | Map-based pair matching |
| 155 | Min Stack | Easy | Track min while pushing/popping |
| 739 | Daily Temperatures | Medium | Monotonic decreasing stack |
| 496 | Next Greater Element I | Medium | Monotonic stack + hashmap |
| 503 | Next Greater Element II | Medium | Circular array + monotonic stack |
| 901 | Online Stock Span | Medium | Monotonic stack tracks indices |
| 316 | Remove Duplicate Letters | Hard | Monotonic + greedy + frequency |
| 321 | Create Maximum Number | Hard | Greedy selection + merge |
| 456 | 132 Pattern | Medium | Multiple stacks for bounds |
| 42 | Trapping Rain Water | Hard | Monotonic stack or two pointers |

## Related Patterns

- [[wiki/patterns/two-pointers|Two Pointers]] — Alternative for some sequence matching problems
- [[wiki/patterns/bfs|Tree/Graph BFS]] — Queue (opposite of stack) for level-order traversal
- [[wiki/patterns/dfs|Tree/Graph DFS]] — Implicit stack via recursion

## Strategy Notes

**When to use Stack vs. Recursion:**
- **Stack (iterative):** Explicit control, avoid stack overflow on deep inputs
- **Recursion:** Cleaner code, natural for tree/graph problems, risk of stack overflow

**When to use Monotonic Stack:**
- Problem asks for "next X" or "previous X" for all elements
- Brute force would be O(n²); stack reduces to O(n)
