---
title: "Arrays & Strings"
tags:
  - wiki
  - dsa
  - arrays
  - strings
  - slices
date_created: 2026-04-04
date_modified: 2026-04-04
sources:
  - "[[sources/leetcode/2026-04-04-longest-palindromic-substring]]"
---

# Arrays & Strings

The most fundamental data structures. In Go, arrays are fixed-size and rarely used directly — **slices** are the standard dynamic array. Strings are immutable byte sequences with special handling for Unicode.

## Go Slices (Dynamic Arrays)

### Creation & Basics

```go
// Literal
nums := []int{1, 2, 3}

// make(type, length, capacity)
nums := make([]int, 0, 10) // len=0, cap=10

// Append (may reallocate if cap exceeded)
nums = append(nums, 4)

// Slice of a slice (shares underlying array!)
sub := nums[1:3] // elements at index 1, 2
```

### Complexity

| Operation | Time | Notes |
|-----------|------|-------|
| Access by index | O(1) | `nums[i]` |
| Append | O(1) amortized | O(n) when capacity doubles |
| Insert at index | O(n) | Must shift elements right |
| Delete at index | O(n) | Must shift elements left |
| Search (unsorted) | O(n) | Linear scan |
| Search (sorted) | O(log n) | [[wiki/dsa/binary-search\|Binary search]] |
| Copy | O(n) | `copy(dst, src)` |

### Internals

A slice header is a struct with three fields:

```go
type slice struct {
    array unsafe.Pointer // pointer to underlying array
    len   int            // current length
    cap   int            // capacity before reallocation
}
```

> [!warning] Slice gotcha: shared backing array
> Slicing (`a[1:3]`) creates a new slice header pointing to the **same** underlying array. Modifying one modifies the other. Use `copy()` if you need independence:
> ```go
> independent := make([]int, len(original))
> copy(independent, original)
> ```

### Growth Strategy

When `append` exceeds capacity, Go allocates a new array. The growth factor is roughly 2x for small slices, tapering off for large ones. Never rely on the exact capacity — always reassign: `nums = append(nums, val)`.

## Strings in Go

Strings are **immutable sequences of bytes** (not characters). For Unicode text, you need to work with runes.

```go
s := "hello"

// Byte access (ASCII only safe)
b := s[0] // byte 'h'

// Rune iteration (Unicode safe)
for i, r := range s {
    // i = byte offset, r = rune (Unicode code point)
}

// String → byte slice (mutable copy)
bytes := []byte(s)
bytes[0] = 'H'
s2 := string(bytes) // "Hello"

// String → rune slice (for Unicode manipulation)
runes := []rune(s)
```

> [!tip] Bytes vs Runes rule of thumb
> - **ASCII-only problems** (LeetCode typically): `s[i]` is fine, `len(s)` gives character count
> - **Unicode problems**: convert to `[]rune` first, or use `range` which decodes runes automatically

### String Builder (efficient concatenation)

```go
var sb strings.Builder
for _, word := range words {
    sb.WriteString(word)
}
result := sb.String()
```

Never concatenate strings in a loop with `+` — it allocates a new string every time (O(n²) total).

## Common Array/String Patterns

- **[[wiki/patterns/two-pointers|Two Pointers]]** — converging, expanding, or same-direction traversal
- **[[wiki/patterns/sliding-window|Sliding Window]]** — maintain a window over a subarray/substring
- **[[wiki/dsa/hash-tables|Hash Tables]]** — frequency counting, complement lookup
- **[[wiki/dsa/sorting|Sorting]]** — sort then apply two pointers or binary search
- **[[wiki/dsa/binary-search|Binary Search]]** — O(log n) search in sorted arrays

## Related

- [[wiki/go/slices|Slices (Go deep-dive)]] — internals, capacity, and advanced idioms
- [[wiki/go/strings|Strings, Runes & Bytes]] — Unicode handling in Go
- [[wiki/patterns/two-pointers|Two Pointers]] — the most common pattern on arrays
- [[wiki/patterns/sliding-window|Sliding Window]] — subarray/substring problems
