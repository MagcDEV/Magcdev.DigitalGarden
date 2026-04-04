---
title: "Stacks (LIFO Data Structure)"
tags:
  - wiki
  - dsa
  - data-structures
date_created: 2026-04-04
date_modified: 2026-04-04
sources:
  - "[[sources/leetcode/2026-04-04-valid-parentheses]]"
---

# Stacks (LIFO Data Structure)

## What is a Stack?

A **stack** is a linear data structure that follows the **LIFO (Last-In-First-Out)** principle: the last element added is the first one removed. Think of a stack of plates — you add to the top and remove from the top.

## Core Operations

| Operation | Time | Space | Go Code |
|-----------|------|-------|---------|
| Push | O(1) amortized | O(1) | `stack = append(stack, x)` |
| Pop | O(1) | O(1) | `stack = stack[:len(stack)-1]` |
| Peek (Top) | O(1) | O(0) | `top := stack[len(stack)-1]` |
| IsEmpty | O(1) | O(0) | `len(stack) == 0` |
| Size | O(1) | O(0) | `len(stack)` |

## Go Implementation

### Using Slices (Recommended)

```go
// Generic stack using slices
type Stack []int

func (s *Stack) Push(x int) {
    *s = append(*s, x)
}

func (s *Stack) Pop() int {
    if len(*s) == 0 {
        panic("pop from empty stack")
    }
    x := (*s)[len(*s)-1]
    *s = (*s)[:len(*s)-1]
    return x
}

func (s *Stack) Peek() int {
    if len(*s) == 0 {
        panic("peek on empty stack")
    }
    return (*s)[len(*s)-1]
}

func (s *Stack) IsEmpty() bool {
    return len(*s) == 0
}

// Usage
var stack Stack
stack.Push(1)
stack.Push(2)
val := stack.Pop()  // 2
```

### Using Interface{} for Generic Types

```go
// For heterogeneous types
stack := []interface{}{}
stack = append(stack, "hello")
stack = append(stack, 42)

top := stack[len(stack)-1].(interface{})
stack = stack[:len(stack)-1]
```

### Using Linked List (Less Common)

```go
// From container/list package
import "container/list"

s := list.New()
s.PushBack(1)      // O(1)
front := s.Back()  // O(1)
s.Remove(front)    // O(1)
```

## Memory Characteristics in Go

> [!info] Go Slice Internals
> - **Push (append):** Amortized O(1) — capacity grows geometrically (usually 2x)
> - **Pop (reslice):** O(1) — does NOT deallocate; capacity remains
> - **Large stacks:** If you frequently pop all elements, consider creating a new slice to reclaim memory
> - **Example:** `stack = stack[:0]` clears but keeps capacity; `stack = nil` deallocates

```go
// Example: memory efficiency
stack := make([]int, 0, 10)  // Pre-allocate for 10 elements
for i := 0; i < 10; i++ {
    stack = append(stack, i)  // No reallocations
}
// After popping, capacity is still 10
stack = stack[:0]  // Clear but keep capacity
```

## Common Use Cases

### 1. Bracket Matching
Check if parentheses/brackets are valid and properly nested.

```go
func isValid(s string) bool {
    pairs := map[rune]rune{')': '(', '}': '{', ']': '['}
    var stack []rune
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

**Related:** LC-20 (Valid Parentheses), LC-32 (Longest Valid Parentheses)

### 2. Expression Evaluation
Evaluate postfix expressions or handle operator precedence.

```go
// Postfix evaluation: "3 4 + 2 *" → 14
func evalRPN(tokens []string) int {
    stack := []int{}
    ops := map[string]bool{"+": true, "-": true, "*": true, "/": true}

    for _, token := range tokens {
        if ops[token] {
            b := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            a := stack[len(stack)-1]
            stack = stack[:len(stack)-1]

            var result int
            switch token {
            case "+": result = a + b
            case "-": result = a - b
            case "*": result = a * b
            case "/": result = a / b
            }
            stack = append(stack, result)
        } else {
            num, _ := strconv.Atoi(token)
            stack = append(stack, num)
        }
    }
    return stack[0]
}
```

**Related:** LC-150 (Evaluate Reverse Polish Notation), LC-224 (Basic Calculator)

### 3. Monotonic Stack
Maintain stack in increasing/decreasing order to find next/previous element efficiently.

```go
// Next Greater Element
func nextGreaterElement(nums []int) []int {
    stack := []int{}
    result := make([]int, len(nums))
    res := make(map[int]int)

    for i := len(nums) - 1; i >= 0; i-- {
        for len(stack) > 0 && stack[len(stack)-1] <= nums[i] {
            stack = stack[:len(stack)-1]
        }
        if len(stack) == 0 {
            res[nums[i]] = -1
        } else {
            res[nums[i]] = stack[len(stack)-1]
        }
        stack = append(stack, nums[i])
    }

    for i, num := range nums {
        result[i] = res[num]
    }
    return result
}
```

**Related:** LC-496 (Next Greater Element), LC-739 (Daily Temperatures)

### 4. Undo/Redo Operations
Model undo as popping from primary stack, redo as popping from secondary stack.

```go
type UndoRedo struct {
    undo []string
    redo []string
}

func (u *UndoRedo) Do(action string) {
    u.undo = append(u.undo, action)
    u.redo = nil  // Clear redo on new action
}

func (u *UndoRedo) Undo() {
    if len(u.undo) > 0 {
        action := u.undo[len(u.undo)-1]
        u.undo = u.undo[:len(u.undo)-1]
        u.redo = append(u.redo, action)
    }
}

func (u *UndoRedo) Redo() {
    if len(u.redo) > 0 {
        action := u.redo[len(u.redo)-1]
        u.redo = u.redo[:len(u.redo)-1]
        u.undo = append(u.undo, action)
    }
}
```

## Comparison with Other Data Structures

| DS | Access | Insert | Delete | Use Case |
|----|---------|---------|---------|----|
| **Stack** | O(1) top | O(1) | O(1) | LIFO, function calls, undo |
| **Queue** | O(1) front | O(1) | O(1) | FIFO, BFS, job scheduling |
| **Array** | O(1) any | O(n) middle | O(n) middle | Random access, caching |
| **Heap** | O(1) root | O(log n) | O(log n) | Priority queues, top-k |

## Related Patterns

- [[wiki/patterns/stack-based|Stack-Based Pattern]] — Comprehensive pattern guide
- [[wiki/patterns/monotonic-stack|Monotonic Stack]] — Specific optimization technique
- [[wiki/dsa/hash-tables|Hash Tables]] — Often paired with stacks for O(1) lookups
