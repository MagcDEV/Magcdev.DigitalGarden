---
title: "Binary Search"
tags:
  - wiki
  - dsa
  - algorithms
  - searching
date_created: 2026-04-04
date_modified: 2026-04-04
sources: []
---

# Binary Search

Binary search is a **O(log n)** algorithm for finding a target value in a **sorted array**. It works by repeatedly dividing the search interval in half, eliminating half of the remaining candidates with each comparison.

> [!tip] Core Recognition Signal
> Use binary search when:
> - The array is **sorted** (or has some monotonic property)
> - You need to find an element, first/last occurrence, or a specific condition
> - You want to avoid O(n) linear scan
> - The problem asks "find minimum/maximum that satisfies condition X"

## The Left vs Right Boundary Dilemma

The **most confusing part** of binary search is choosing between two main template styles:

| Template | Condition | Use When | Loop Ends With |
|----------|-----------|----------|-----------------|
| **Inclusive** `left <= right` | Searches until pointers cross | Finding exact matches | `left == right + 1` |
| **Exclusive** `left < right` | Searches while pointers don't touch | Finding boundaries | `left == right` |

### Template 1: Inclusive (Classic, `left <= right`)

This template treats the search space as a closed interval `[left, right]`. The loop **continues while the pointers haven't crossed**.

```go
func binarySearchInclusive(arr []int, target int) int {
    left, right := 0, len(arr)-1

    for left <= right {  // KEY: includes the case where left == right
        mid := left + (right-left)/2

        if arr[mid] == target {
            return mid  // Found!
        } else if arr[mid] < target {
            left = mid + 1  // Search right half
        } else {
            right = mid - 1  // Search left half
        }
    }

    return -1  // Not found
}
```

**When to use:** Finding an exact match in an unrotated sorted array. The loop ends when `left > right`, meaning the target doesn't exist.

**Why `left <= right`?** Because when `left == right`, that single element might be the target. We must check it before concluding it's not there.

### Template 2: Exclusive (`left < right`)

This template treats the search space as `[left, right)` — left inclusive, right exclusive. The loop **continues while there's at least one element left to examine**.

```go
func binarySearchExclusive(arr []int, target int) int {
    left, right := 0, len(arr)  // NOTE: right = len(arr), not len-1

    for left < right {  // KEY: stops when left == right
        mid := left + (right-left)/2

        if arr[mid] < target {
            left = mid + 1  // Search right half
        } else {
            right = mid  // Search left half (includes mid)
        }
    }

    // At this point, left == right points to the first element >= target
    if left < len(arr) && arr[left] == target {
        return left
    }
    return -1  // Not found
}
```

**When to use:** Finding boundaries — first occurrence, last occurrence, or insert position. The loop ends when `left == right`, which is the **boundary point**.

**Why `left < right`?** Because once `left == right`, that point is already determined to satisfy some property; we don't need to check it again.

## When to Use Each Template

### Use Inclusive (`left <= right`) When:

1. **Looking for an exact match** in an unmodified sorted array
   - LC-704: Binary Search
   - LC-34 (but need to modify to find boundaries)

2. **Simple, textbook binary search** on a sorted array
   - No complex boundary conditions
   - You're just asking "is X in the array?"

### Use Exclusive (`left < right`) When:

1. **Finding first/last occurrence** of a target
   - LC-34: First and Last Position of Element in Sorted Array
   - Returns the boundary point when loop ends

2. **Finding insert position** (left boundary)
   - LC-35: Search Insert Position
   - When loop ends, `left` is where the element should go

3. **Finding the smallest value that satisfies a condition**
   - LC-1011: Capacity to Ship Packages Within D Days
   - LC-875: Koko Eating Bananas
   - Pattern: `if condition: right = mid else: left = mid + 1`

4. **Handling rotated or modified sorted arrays**
   - LC-33: Search in Rotated Sorted Array
   - The exclusive template makes boundary logic clearer

## Side-by-Side Comparison: Finding First Occurrence

Here's the exact same problem solved both ways to see the difference:

```go
// Problem: Find the first occurrence of target in sorted array
// Input: [5, 7, 7, 8, 8, 10], target = 8
// Output: 3

// INCLUSIVE APPROACH
func findFirstInclusive(arr []int, target int) int {
    left, right := 0, len(arr)-1
    result := -1

    for left <= right {
        mid := left + (right-left)/2
        if arr[mid] == target {
            result = mid  // Remember this, but keep searching left
            right = mid - 1
        } else if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return result
}

// EXCLUSIVE APPROACH
func findFirstExclusive(arr []int, target int) int {
    left, right := 0, len(arr)

    for left < right {
        mid := left + (right-left)/2
        if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid  // Include mid in next iteration
        }
    }

    if left < len(arr) && arr[left] == target {
        return left
    }
    return -1
}
```

Notice:
- **Inclusive** continues searching even after finding the target (to confirm it's the first)
- **Exclusive** naturally converges to the first occurrence through the boundary logic

## Common Pitfalls

### Pitfall 1: Mixing the Two Templates

```go
// WRONG - mixes inclusive and exclusive
left, right := 0, len(arr)-1  // Inclusive style
for left < right { ... }       // Exclusive loop condition
```

**Fix:** Choose one approach and stick with it. Set `right = len(arr)-1` for inclusive, `right = len(arr)` for exclusive.

### Pitfall 2: Infinite Loop on Inclusive

```go
// WRONG - infinite loop if target not in [1,2,3] and you search [2,3]
left, right := 1, 2
for left <= right {
    mid := (left + right) / 2  // Overflow risk (use left + (right-left)/2)
    if arr[mid] < target {
        left = mid  // Should be mid + 1!
    } else {
        right = mid - 1
    }
}
```

**Fix:** Always use `left = mid + 1` and `right = mid - 1` in inclusive approach.

### Pitfall 3: Off-by-One on Exclusive

```go
// WRONG - right should be len(arr), not len(arr)-1
left, right := 0, len(arr)-1
for left < right {
    // ...
}
```

**Fix:** For exclusive, initialize `right = len(arr)`.

## Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(log n) — halve the search space each iteration |
| **Space Complexity** | O(1) — only pointers, no recursion (iterative) |
| **Prerequisite** | Array must be sorted (or have monotonic property) |

## Decision Tree: Which Template Should I Use?

```
Is this a "find exact match" problem?
├─ YES → Use Inclusive (left <= right)
└─ NO (boundary/first/last/condition)?
   ├─ Finding first/last occurrence → Use Exclusive (left < right)
   ├─ Finding insert position → Use Exclusive (left < right)
   └─ Finding min that satisfies condition → Use Exclusive (left < right)
```

## Practice Problems (Graded)

### Easy

- **LC-704: Binary Search** — Simple exact match. **Inclusive template is perfect for this.**
- **LC-35: Search Insert Position** — Find where to insert. Uses exclusive template to land on the insertion point.
- **LC-278: First Bad Version** — First occurrence where condition is true. Exclusive template shines.

### Medium

- **LC-34: Find First and Last Position of Element in Sorted Array** — Two binary searches for boundaries. Good test of exclusive template.
- **LC-33: Search in Rotated Sorted Array** — Rotated array with boundary logic. Exclusive avoids fence-post errors.
- **LC-875: Koko Eating Bananas** — Binary search on the answer space. Example of "find minimum that satisfies condition."
- **LC-1011: Capacity to Ship Packages Within D Days** — Same pattern as Koko.

### Hard

- **LC-4: Median of Two Sorted Arrays** — Partition-based binary search. Tricky boundary logic.
- **LC-154: Find Minimum in Rotated Sorted Array II** — With duplicates, harder boundary analysis.
- **LC-1847: Closest Room** — Binary search combined with sorting.

## Key Takeaways

> [!warning] Boundary Condition is Everything
>
> 80% of binary search bugs are boundary conditions. Decide on your template **first**, then be **consistent**:
> - Inclusive (`left <= right`) uses `mid - 1` and `mid + 1`
> - Exclusive (`left < right`) uses `mid` and `mid + 1`

> [!abstract] Template Selection Rule
>
> **When unsure, use exclusive (`left < right`)** for finding boundaries. It's more commonly used in real interviews because most problems ask "find the first X" or "find where to insert X", not "does X exist?"

---

## See Also

- [[wiki/dsa/arrays|Arrays & Strings]] — Data structure foundation
- [[wiki/patterns/binary-search-modified|Modified Binary Search Pattern]] — Extended patterns for rotated arrays
- [[wiki/dsa/big-o|Big-O Notation]] — Complexity analysis
- [[wiki/go/leetcode-snippets|Go Snippets]] — Idiomatic Go implementations
