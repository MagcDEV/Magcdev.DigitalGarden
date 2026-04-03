---
title: "Hash Tables"
tags:
  - wiki
  - dsa
  - hash-table
  - hash-map
date_created: 2026-04-03
date_modified: 2026-04-03
sources:
  - "[[sources/leetcode/2026-04-03-top-k-frequent-elements]]"
---

# Hash Tables

A hash table (hash map) maps keys to values using a hash function to compute an index into an array of buckets. In Go, the built-in `map` type is the standard hash table.

## Go Implementation

```go
// Create
m := make(map[string]int)

// Insert / update
m["key"] = 42

// Lookup (with existence check)
val, ok := m["key"]
if !ok {
    // key not present
}

// Delete
delete(m, "key")

// Iterate (order is NOT guaranteed)
for k, v := range m {
    fmt.Println(k, v)
}
```

## Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Insert    | O(1)    | O(n)       |
| Lookup    | O(1)    | O(n)       |
| Delete    | O(1)    | O(n)       |
| Space     | O(n)    | O(n)       |

Worst case happens when all keys hash to the same bucket (hash collision). In practice with Go's built-in map, this is extremely rare.

## Common Patterns

### Frequency Counting

The most fundamental hash map pattern — count occurrences of elements.

```go
count := make(map[int]int)
for _, num := range nums {
    count[num]++
}
```

> [!tip] Recognition Signal
> Whenever a problem says "frequency", "count occurrences", "most common", or "top K" — reach for a frequency map first.

Used in: [[wiki/patterns/top-k|Top-K Elements]], [[wiki/patterns/sliding-window|Sliding Window]] (character counts)

### Two-Sum Pattern (Complement Lookup)

Store seen values and check for complements.

```go
seen := make(map[int]int) // value → index
for i, num := range nums {
    if j, ok := seen[target-num]; ok {
        return []int{j, i}
    }
    seen[num] = i
}
```

### Grouping / Bucketing

Group elements by some computed key.

```go
groups := make(map[string][]string)
for _, word := range words {
    key := computeKey(word) // e.g., sorted characters for anagrams
    groups[key] = append(groups[key], word)
}
```

## Go-Specific Gotchas

- **Maps are reference types** — passing a map to a function does not copy it
- **Zero value on missing key** — `m["missing"]` returns the zero value for the value type (0 for int, "" for string), not an error. Always use the two-value form `val, ok := m[key]` when existence matters
- **Not concurrency-safe** — use `sync.Map` or a `sync.Mutex` for concurrent access
- **Iteration order is randomized** — never rely on map iteration order

## Related

- [[wiki/dsa/arrays|Arrays & Strings]] — often used together
- [[wiki/patterns/top-k|Top-K Elements]] — frequency map + bucket sort or heap
- [[wiki/patterns/sliding-window|Sliding Window]] — hash maps for character/element counts
- [[wiki/dsa/tries|Tries]] — alternative for string-key lookups with prefix queries
