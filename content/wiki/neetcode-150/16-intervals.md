---
title: "NeetCode 150, stage 16: Intervals"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - intervals
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 16: Intervals

[[wiki/neetcode-150/15-greedy|← Greedy]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/17-math-and-geometry|Math and Geometry →]]

An interval is a pair of numbers: a start and an end. This stage trains one habit: sort first, then make one pass. After the sort, each interval needs a comparison with only one neighbor or with the top of a heap. The choice of the sort key, start or end, is the important decision in each problem.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 5: The sort package with binary search|the Go syntax for this stage]], [[wiki/dsa/sorting|Sorting]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/16-intervals#57. Insert Interval\|57. Insert Interval]] | Medium | Three-phase insert | [[wiki/neetcode-150/16-intervals#Template B: Three-phase insert\|B: Three-phase insert]] |
| 2 | [[wiki/neetcode-150/16-intervals#56. Merge Intervals\|56. Merge Intervals]] | Medium | Sort by start, then merge | [[wiki/neetcode-150/16-intervals#Template A: Sort by start, then merge\|A: Sort by start, then merge]] |
| 3 | [[wiki/neetcode-150/16-intervals#435. Non-overlapping Intervals\|435. Non-overlapping Intervals]] | Medium | Sort by end, greedy keep | [[wiki/neetcode-150/16-intervals#Template C: Sort by end, then greedy keep\|C: Sort by end, then greedy keep]] |
| 4 | [[wiki/neetcode-150/16-intervals#252. Meeting Rooms\|252. Meeting Rooms]] | Easy | Sort by start, compare neighbors | [[wiki/neetcode-150/16-intervals#Template A: Sort by start, then merge\|A: Sort by start, then merge]] |
| 5 | [[wiki/neetcode-150/16-intervals#253. Meeting Rooms II\|253. Meeting Rooms II]] | Medium | Sweep of sorted starts and ends | [[wiki/neetcode-150/16-intervals#Template D: Sweep of sorted starts and ends\|D: Sweep of sorted starts and ends]] |
| 6 | [[wiki/neetcode-150/16-intervals#1851. Minimum Interval to Include Each Query\|1851. Minimum Interval to Include Each Query]] | Hard | Offline queries, sort plus min-heap | [[wiki/neetcode-150/16-intervals#Template E: Offline queries with a sort and a min-heap\|E: Offline queries with a sort and a min-heap]] |

## Templates to memorize

### Template A: Sort by start, then merge

> [!tip] Signal
> The problem says merge, overlap, "combine the ranges" or "can a person attend all the meetings". The intervals come in any order.

```go
// TEMPLATE A: sort by start, then compare each interval with the last one
// of the result.
func mergeOverlaps(intervals [][]int) [][]int {
    sort.Slice(intervals, func(i, j int) bool { // 1. SORT by start
        return intervals[i][0] < intervals[j][0]
    })
    res := [][]int{}
    for _, cur := range intervals {
        last := len(res) - 1
        // 2. COMPARE: cur starts before last ends
        if last >= 0 && cur[0] <= res[last][1] {
            // 3. EXTEND the last interval
            res[last][1] = max(res[last][1], cur[1])
        } else {
            // 4. APPEND: a new group starts
            res = append(res, []int{cur[0], cur[1]})
        }
    }
    return res
}
```

The moves are SORT, COMPARE, then EXTEND or APPEND. After the sort, an interval can overlap only the last interval of the result. Extend with `max`, because the current interval can be inside the last one. Read the statement for the tie: if `[1,4]` and `[4,5]` must merge, compare with `<=`.

> [!quote] Say it
> "I sort by start. Then each interval either extends the last merged interval or starts a new one. The sort makes it O(n log n)."

### Template B: Three-phase insert

> [!tip] Signal
> The intervals are already sorted and do not overlap. You must add one interval and keep the two properties.

```go
// TEMPLATE B: insert into intervals that are sorted and do not overlap. One
// pass, three phases.
func insertSorted(intervals [][]int, start, end int) [][]int {
    res := [][]int{}
    i, n := 0, len(intervals)
    // 1. BEFORE: ends before the new one starts
    for i < n && intervals[i][1] < start {
        res = append(res, intervals[i])
        i++
    }
    // 2. MERGE: starts before the new one ends
    for i < n && intervals[i][0] <= end {
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i++
    }
    res = append(res, []int{start, end})
    return append(res, intervals[i:]...) // 3. AFTER: the rest
}
```

The moves are BEFORE, MERGE, then AFTER. The first loop copies the intervals that end before the new one starts. The second loop grows the new interval while an interval starts at or before its end. Do not sort again: the input is sorted, so one pass gives O(n).

> [!quote] Say it
> "The input is sorted, so I do one pass in three phases: copy what is before, merge what overlaps, copy what is after. That is O(n)."

### Template C: Sort by end, then greedy keep

> [!tip] Signal
> The problem asks for the least number of intervals to remove, or the most intervals that fit with no overlap. You choose which intervals stay.

```go
// TEMPLATE C: sort by END, then keep each interval that starts at or after
// the last kept end.
// It returns the largest number of intervals that do not overlap.
func mostWithoutOverlap(intervals [][]int) int {
    if len(intervals) == 0 {
        return 0
    }
    sort.Slice(intervals, func(i, j int) bool { // 1. SORT by end
        return intervals[i][1] < intervals[j][1]
    })
    kept := 1
    // the first interval ends first: always keep it
    prevEnd := intervals[0][1]
    for _, cur := range intervals[1:] {
        // 2. KEEP: no overlap with the last kept interval
        if cur[0] >= prevEnd {
            kept++
            prevEnd = cur[1]
        } // 3. if not, REMOVE cur: nothing to do
    }
    return kept
}
```

The moves are SORT by end, KEEP, then REMOVE. The interval that ends first leaves the most room for the others, so it is always safe to keep it. A sort by start is the common mistake here. One long interval that starts first can then block many short ones.

> [!quote] Say it
> "This is activity selection. I sort by end time and keep each interval that starts after the last kept end. The answer is n minus the number that I keep."

### Template D: Sweep of sorted starts and ends

> [!tip] Signal
> The problem asks how many intervals are active at the same time: rooms, platforms or servers. The identity of each interval does not matter.

```go
// TEMPLATE D: sweep. Sort the starts and the ends separately, then walk
// them in time order.
// It returns the largest number of intervals that are open at the same
// time.
func mostOpen(intervals [][]int) int {
    n := len(intervals)
    starts, ends := make([]int, n), make([]int, n)
    for i, iv := range intervals {
        starts[i], ends[i] = iv[0], iv[1]
    }
    sort.Ints(starts)
    sort.Ints(ends)
    open, most := 0, 0
    s, e := 0, 0
    for s < n {
        if starts[s] < ends[e] { // 1. START comes first: one more is open
            open++
            s++
            most = max(most, open)
        } else { // 2. END comes first (or a tie): one less is open
            open--
            e++
        }
    }
    return most
}
```

The moves are START and END. Two sorted slices and two indexes replace an event list. On a tie, the end goes first, so a room that becomes free at time 10 serves a meeting that starts at time 10. A min-heap of end times gives the same answer. The heap is the better tool when you must also know which room each meeting gets.

> [!quote] Say it
> "I sort the start times and the end times separately and sweep them in order. A start adds a room and an end frees one. The peak is the answer."

### Template E: Offline queries with a sort and a min-heap

> [!tip] Signal
> You get many query points and many intervals, and each query asks for the best interval that contains it. A scan of all the intervals for each query is too slow.

```go
// TEMPLATE E: offline queries. Answer the queries in sorted order, so one
// sweep serves all.
// For each query point, it gives the size of the smallest interval that
// contains the point.
type span struct{ size, end int } // sizeHeap is a min-heap of span, by size

func smallestCover(intervals [][]int, queries []int) []int {
    sort.Slice(intervals, func(i, j int) bool { return intervals[i][0] < intervals[j][0] })
    // 1. SORT THE QUERIES: sort their indexes by value
    order := make([]int, len(queries))
    for i := range order {
        order[i] = i
    }
    sort.Slice(order, func(a, b int) bool { return queries[order[a]] < queries[order[b]] })
    res := make([]int, len(queries))
    h := sizeHeap{}
    next := 0
    for _, qi := range order {
        q := queries[qi]
        // 2. ADD: starts <= q
        for ; next < len(intervals) && intervals[next][0] <= q; next++ {
            heap.Push(&h, span{intervals[next][1] - intervals[next][0] + 1, intervals[next][1]})
        }
        for len(h) > 0 && h[0].end < q { // 3. DROP: ends before q
            heap.Pop(&h)
        }
        res[qi] = -1 // 4. ANSWER at the original index
        if len(h) > 0 {
            res[qi] = h[0].size
        }
    }
    return res
}
```

The moves are SORT THE QUERIES, ADD, DROP, then ANSWER. Because the queries arrive in sorted order, an interval that ends before one query also ends before all the later ones. So each interval enters the heap one time and leaves it one time. Sort a slice of indexes, not the queries, because each answer must go back to its original position. The heap type has the five methods from [[wiki/neetcode-150/09-heap-priority-queue#Template A: The five heap methods|the Heap stage]].

> [!quote] Say it
> "I answer the queries offline, in sorted order. A min-heap by size holds the intervals that started, and I pop the ones that already ended. That gives O(n log n plus q log q)."

> [!warning] Mistakes in this stage
> - `sort.Slice` changes the slice in place. Its function gets two indexes, not two items, so compare `intervals[i]` with `intervals[j]`.
> - Decide `<` or `<=` from the statement. Two meetings that touch do not overlap, but LeetCode 56 merges `[1,4]` and `[4,5]`.
> - A `range` loop gives the same inner slice, not a copy. A write to `cur[1]` changes the input row.
> - A sort of the queries loses their positions. Sort a slice of indexes and write each answer at `res[qi]`.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 57. Insert Interval

[LeetCode 57](https://leetcode.com/problems/insert-interval/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Three-phase insert
> - **Template:** [[#Template B: Three-phase insert|B: Three-phase insert]]

> [!tip]- Step 2: the idea
> **Idea.** The input is already sorted, so one pass is enough. Copy the intervals that end before the new one starts, merge each interval that overlaps the new one, then copy the rest.
>
> **Complexity.** Time O(n), space O(n) for the output.
>
> **Go lesson.** `append(res, intervals[i:]...)` adds all the items of a slice in one call. The three dots spread the slice into separate arguments.

> [!example]- Step 3: the Go solution
> ```go
> // insert solves LC 57. Time O(n), space O(n) for the output.
> // The intervals are sorted and do not overlap, so the pass has
> // three
> // phases.
> func insert(intervals [][]int, newInterval []int) [][]int {
>     res := make([][]int, 0, len(intervals)+1)
>     start, end := newInterval[0], newInterval[1]
>     i, n := 0, len(intervals)
>
>     // 1. BEFORE: these intervals end before the new one starts.
>     for i < n && intervals[i][1] < start {
>         res = append(res, intervals[i])
>         i++
>     }
>     // 2. MERGE: these intervals start before the new one ends, so
>     // they
>     // overlap it.
>     // <= because [1,3] and [3,5] touch, and LeetCode merges them.
>     for i < n && intervals[i][0] <= end {
>         // grow the new interval to cover both
>         start = min(start, intervals[i][0])
>         end = max(end, intervals[i][1])
>         i++
>     }
>     res = append(res, []int{start, end})
>     // 3. AFTER: the rest starts after the new interval ends.
>     res = append(res, intervals[i:]...)
>     return res
> }
> ```

### 56. Merge Intervals

[LeetCode 56](https://leetcode.com/problems/merge-intervals/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Sort by start, then merge
> - **Template:** [[#Template A: Sort by start, then merge|A: Sort by start, then merge]]

> [!tip]- Step 2: the idea
> **Idea.** Sort the intervals by start. Then each interval can overlap only the last interval of the result. If it overlaps, extend that last interval, and if not, append the interval.
>
> **Complexity.** Time O(n log n), space O(n) for the output.
>
> **Go lesson.** `sort.Slice` sorts any slice with a function that says if item i comes before item j. The function reads the slice from the outer scope.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `sort`
>
> ```go
> // merge solves LC 56. Time O(n log n) for the sort, space O(n) for
> // the
> // output.
> // After the sort by start, an interval can overlap only the last
> // interval
> // of the result.
> func merge(intervals [][]int) [][]int {
>     // SORT by start. The function returns true when item i must
>     // come before
>     // item j.
>     sort.Slice(intervals, func(i, j int) bool {
>         return intervals[i][0] < intervals[j][0]
>     })
>     res := [][]int{}
>     for _, cur := range intervals {
>         last := len(res) - 1
>         // COMPARE with the last result. <= because [1,4] and [4,5]
>         // touch
>         // and merge.
>         if last >= 0 && cur[0] <= res[last][1] {
>             // EXTEND: max, cur can be inside last
>             res[last][1] = max(res[last][1], cur[1])
>         } else {
>             // APPEND a copy, the input row stays
>             res = append(res, []int{cur[0], cur[1]})
>         }
>     }
>     return res
> }
> ```

### 435. Non-overlapping Intervals

[LeetCode 435](https://leetcode.com/problems/non-overlapping-intervals/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Sort by end, greedy keep
> - **Template:** [[#Template C: Sort by end, then greedy keep|C: Sort by end, then greedy keep]]

> [!tip]- Step 2: the idea
> **Idea.** Count the largest set of intervals that do not overlap. The answer is the total minus that count. To keep the most, always keep the interval that ends first, because it leaves the most room for the others.
>
> **Complexity.** Time O(n log n), space O(1) without the sort.
>
> **Go lesson.** The loop keeps only one `int`, the end of the last interval that stays. Start it at `math.MinInt`, the smallest `int`, so the first interval always passes the test.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `math`, `sort`
>
> ```go
> // eraseOverlapIntervals solves LC 435. Time O(n log n), space O(1).
> // Greedy: keep the interval that ends first, and remove each one
> // that
> // overlaps it.
> func eraseOverlapIntervals(intervals [][]int) int {
>     // SORT by end. The interval that ends first leaves the most
>     // room.
>     sort.Slice(intervals, func(i, j int) bool {
>         return intervals[i][1] < intervals[j][1]
>     })
>     removed := 0
>     // the end of the last interval that stays
>     prevEnd := math.MinInt
>     for _, cur := range intervals {
>         // >= because [1,2] and [2,3] only touch: no overlap
>         if cur[0] >= prevEnd {
>             prevEnd = cur[1] // KEEP cur
>         } else {
>             // REMOVE cur: it starts before the kept interval ends
>             removed++
>         }
>     }
>     return removed
> }
> ```

### 252. Meeting Rooms

[LeetCode 252](https://leetcode.com/problems/meeting-rooms/) (premium) · [free on NeetCode](https://neetcode.io/problems/meeting-schedule) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Sort by start, compare neighbors
> - **Template:** [[#Template A: Sort by start, then merge|A: Sort by start, then merge]]

> [!tip]- Step 2: the idea
> **Idea.** Sort the meetings by start time. If two meetings overlap, then two neighbors in the sorted order also overlap. So compare each meeting only with the one before it.
>
> **Complexity.** Time O(n log n), space O(1) without the sort.
>
> **Go lesson.** The loop starts at index 1, so `intervals[i-1]` is always valid. With zero or one meeting the loop does not run, and the answer is `true`.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `sort`
>
> ```go
> // canAttendMeetings solves LC 252. Time O(n log n), space O(1).
> // After the sort by start, an overlap always shows between two
> // neighbors.
> func canAttendMeetings(intervals [][]int) bool {
>     // SORT by start time.
>     sort.Slice(intervals, func(i, j int) bool {
>         return intervals[i][0] < intervals[j][0]
>     })
>     for i := 1; i < len(intervals); i++ {
>         // COMPARE with the meeting before. < because a meeting can
>         // start
>         // at the time when the one before ends.
>         if intervals[i][0] < intervals[i-1][1] {
>             // this meeting starts before the last one ends
>             return false
>         }
>     }
>     return true
> }
> ```

### 253. Meeting Rooms II

[LeetCode 253](https://leetcode.com/problems/meeting-rooms-ii/) (premium) · [free on NeetCode](https://neetcode.io/problems/meeting-schedule-ii) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Sweep of sorted starts and ends
> - **Template:** [[#Template D: Sweep of sorted starts and ends|D: Sweep of sorted starts and ends]]

> [!tip]- Step 2: the idea
> **Idea.** Sort the start times and the end times separately, because only the times matter. Walk the two slices in time order: a start opens a room and an end frees a room. The answer is the largest number of open rooms.
>
> **Complexity.** Time O(n log n), space O(n).
>
> **Go lesson.** `sort.Ints` sorts a slice of `int` in place. `make([]int, n)` gives a slice with n zeros that the loop fills by index.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `sort`
>
> ```go
> // minMeetingRooms solves LC 253. Time O(n log n), space O(n).
> // A sweep in time order: each start opens a room, each end frees a
> // room.
> // The other standard answer sorts by start and keeps a min-heap of
> // end
> // times.
> func minMeetingRooms(intervals [][]int) int {
>     n := len(intervals)
>     starts := make([]int, n)
>     ends := make([]int, n)
>     for i, iv := range intervals {
>         starts[i] = iv[0]
>         ends[i] = iv[1]
>     }
>     sort.Ints(starts) // SORT the two slices separately
>     sort.Ints(ends)
>
>     // the rooms in use now, and the largest value so far
>     open, most := 0, 0
>     s, e := 0, 0 // the next start and the next end
>     // after the last start, the count can only go down
>     for s < n {
>         if starts[s] < ends[e] {
>             // START: a meeting begins before the next one ends
>             open++
>             s++
>             most = max(most, open)
>         } else {
>             // END: a room is free. On a tie the end goes first,
>             open--
>             e++ // so a meeting can start when another one ends
>         }
>     }
>     return most
> }
> ```

### 1851. Minimum Interval to Include Each Query

[LeetCode 1851](https://leetcode.com/problems/minimum-interval-to-include-each-query/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Offline queries, sort plus min-heap
> - **Template:** [[#Template E: Offline queries with a sort and a min-heap|E: Offline queries with a sort and a min-heap]]

> [!tip]- Step 2: the idea
> **Idea.** Answer the queries from the smallest to the largest. For each query, push the intervals that start at or before it into a min-heap by size, and pop the ones that end before it. The top is then the smallest interval that contains the query.
>
> **Complexity.** Time O(n log n + q log q) for n intervals and q queries, space O(n + q).
>
> **Go lesson.** To sort the queries and keep their positions, sort a slice of indexes. The function of `sort.Slice` compares `queries[order[a]]` with `queries[order[b]]`.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `container/heap`, `sort`
>
> ```go
> // minInterval solves LC 1851. Time O(n log n + q log q), space O(n
> // + q).
> // The loop answers the queries in sorted order, so each interval
> // enters the
> // heap
> // one time and leaves it one time.
> type span struct{ size, end int }
>
> // sizeHeap is a min-heap of spans: the smallest size is on top.
> type sizeHeap []span
>
> func (h sizeHeap) Len() int           { return len(h) }
> func (h sizeHeap) Less(i, j int) bool { return h[i].size < h[j].size }
> func (h sizeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
> func (h *sizeHeap) Push(x any)        { *h = append(*h, x.(span)) }
> func (h *sizeHeap) Pop() any {
>     old := *h
>     n := len(old)
>     x := old[n-1]
>     *h = old[:n-1]
>     return x
> }
>
> func minInterval(intervals [][]int, queries []int) []int {
>     // SORT the intervals by start.
>     sort.Slice(intervals, func(i, j int) bool {
>         return intervals[i][0] < intervals[j][0]
>     })
>     // SORT THE QUERIES by value, but keep their positions: order
>     // holds
>     // indexes.
>     order := make([]int, len(queries))
>     for i := range order {
>         order[i] = i
>     }
>     sort.Slice(order, func(a, b int) bool {
>         return queries[order[a]] < queries[order[b]]
>     })
>
>     res := make([]int, len(queries))
>     h := sizeHeap{}
>     next := 0 // the first interval that is not in the heap yet
>     for _, qi := range order {
>         q := queries[qi]
>         // ADD each interval that starts at or before q.
>         for next < len(intervals) && intervals[next][0] <= q {
>             left, right := intervals[next][0], intervals[next][1]
>             heap.Push(&h, span{right - left + 1, right})
>             next++
>         }
>         // DROP the intervals that end before q. They also end
>         // before all
>         // the later queries.
>         for len(h) > 0 && h[0].end < q {
>             heap.Pop(&h)
>         }
>         // ANSWER at the original index. All the spans in the heap
>         // start at
>         // or before q,
>         // and the top ends at or after q, so the top contains q.
>         if len(h) > 0 {
>             res[qi] = h[0].size
>         } else {
>             res[qi] = -1
>         }
>     }
>     return res
> }
> ```

---

[[wiki/neetcode-150/15-greedy|← Greedy]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/17-math-and-geometry|Math and Geometry →]]
