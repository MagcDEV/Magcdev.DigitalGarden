---
title: "NeetCode 150, stage 9: Heap and Priority Queue"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - heap
date_created: 2026-11-11
date_modified: 2026-11-11
---

# NeetCode 150, stage 9: Heap and Priority Queue

[[wiki/neetcode-150/08-tries|← Tries]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/10-backtracking|Backtracking →]]

A heap gives the smallest or the largest item in O(log n), and it does not sort the other items. This stage trains the questions that say "top K", "Kth" or "next smallest", and the streams where values arrive one at a time. Go has no priority queue type, so you also learn the five methods that `container/heap` needs.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 8: Interfaces with the heap|the Go syntax for this stage]], [[wiki/patterns/top-k|Top-K Elements pattern]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/09-heap-priority-queue#703. Kth Largest Element in a Stream\|703. Kth Largest Element in a Stream]] | Easy | Min-heap of size K | [[wiki/neetcode-150/09-heap-priority-queue#Template A: The five heap methods\|A: The five heap methods]], [[wiki/neetcode-150/09-heap-priority-queue#Template B: Heap of size K\|B: Heap of size K]] |
| 2 | [[wiki/neetcode-150/09-heap-priority-queue#1046. Last Stone Weight\|1046. Last Stone Weight]] | Easy | Max-heap simulation | [[wiki/neetcode-150/09-heap-priority-queue#Template C: Max-heap by a different Less\|C: Max-heap by a different Less]] |
| 3 | [[wiki/neetcode-150/09-heap-priority-queue#973. K Closest Points to Origin\|973. K Closest Points to Origin]] | Medium | Max-heap of size K | [[wiki/neetcode-150/09-heap-priority-queue#Template B: Heap of size K\|B: Heap of size K]], [[wiki/neetcode-150/09-heap-priority-queue#Template C: Max-heap by a different Less\|C: Max-heap by a different Less]] |
| 4 | [[wiki/neetcode-150/09-heap-priority-queue#215. Kth Largest Element in an Array\|215. Kth Largest Element in an Array]] | Medium | Min-heap of size K | [[wiki/neetcode-150/09-heap-priority-queue#Template A: The five heap methods\|A: The five heap methods]], [[wiki/neetcode-150/09-heap-priority-queue#Template B: Heap of size K\|B: Heap of size K]] |
| 5 | [[wiki/neetcode-150/09-heap-priority-queue#621. Task Scheduler\|621. Task Scheduler]] | Medium | Max-heap plus cooldown queue | [[wiki/neetcode-150/09-heap-priority-queue#Template C: Max-heap by a different Less\|C: Max-heap by a different Less]], [[wiki/neetcode-150/09-heap-priority-queue#Template E: Max-heap plus cooldown queue\|E: Max-heap plus cooldown queue]] |
| 6 | [[wiki/neetcode-150/09-heap-priority-queue#355. Design Twitter\|355. Design Twitter]] | Medium | K-way merge with a heap | [[wiki/neetcode-150/09-heap-priority-queue#Template F: K-way merge with a heap\|F: K-way merge with a heap]] |
| 7 | [[wiki/neetcode-150/09-heap-priority-queue#295. Find Median from Data Stream\|295. Find Median from Data Stream]] | Hard | Two heaps | [[wiki/neetcode-150/09-heap-priority-queue#Template D: Two heaps for the median\|D: Two heaps for the median]] |

## Templates to memorize

### Template A: The five heap methods

> [!tip] Signal
> You need the smallest item again and again while new items arrive. A sort after each change is too slow.

```go
// TEMPLATE A: the five methods that container/heap needs. This type is a
// min-heap of int.
type minHeap []int

func (h minHeap) Len() int { return len(h) }

// the item that is "less" is on top
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// Push and Pop change the length of the slice, so they need a pointer
// receiver.
func (h *minHeap) Push(x any) { *h = append(*h, x.(int)) } // add at the END
func (h *minHeap) Pop() any { // remove from the END
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

// Call the functions heap.Init, heap.Push and heap.Pop. Do not call h.Push
// and h.Pop.
func sortedWithHeap(nums []int) []int {
    // a copy of nums, converted to the heap type
    h := minHeap(slices.Clone(nums))
    heap.Init(&h) // BUILD the heap in O(n)
    res := make([]int, 0, len(nums))
    for len(h) > 0 { // h[0] is the top: PEEK is O(1)
        // POP the smallest in O(log n)
        res = append(res, heap.Pop(&h).(int))
    }
    return res
}
```

The moves are BUILD or PUSH, PEEK at `h[0]`, then POP. `Len`, `Less` and `Swap` have a value receiver. `Push` and `Pop` have a pointer receiver, because they change the length. Your `Pop` removes the last item, not the first one: `heap.Pop` moves the top to the end before it calls your method.

> [!quote] Say it
> "Go has no built-in priority queue, so I implement heap.Interface with five methods. Push and pop are O(log n), and the top is O(1)."

### Template B: Heap of size K

> [!tip] Signal
> The problem asks for the K largest, the K closest or the Kth item. K is much smaller than n, or the values come from a stream.

```go
// TEMPLATE B: a heap of size k. For the k LARGEST values, use a MIN-heap.
func kLargest(nums []int, k int) []int {
    h := minHeap{}
    for _, x := range nums {
        heap.Push(&h, x) // 1. PUSH each value
        if len(h) > k {
            // 2. TRIM: remove the smallest, it is not in the top k
            heap.Pop(&h)
        }
    }
    return h // 3. the k largest values. h[0] is the kth largest
}
```

The moves are PUSH, then TRIM when the heap has more than `k` items. The heap type is the opposite of the question. For the K largest values, use a min-heap, so the trim removes the smallest one. For the K smallest values, use a max-heap.

> [!quote] Say it
> "I keep a min-heap of size k. Each value costs O(log k), so the total is O(n log k) time and O(k) space."

### Template C: Max-heap by a different Less

> [!tip] Signal
> Each step takes the largest item, changes it and puts a result back. The problem is a simulation.

```go
// TEMPLATE C: a max-heap. Only Less changes: > in place of <.
type maxHeap []int

func (h maxHeap) Len() int { return len(h) }

// the largest value is on top
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

// Simulation: take the two largest values, put one new value back.
func combineLargest(h *maxHeap) {
    a := heap.Pop(h).(int) // POP the largest
    b := heap.Pop(h).(int) // POP the second largest
    heap.Push(h, a-b)      // PUSH the result
}
```

The moves are POP the largest items, then PUSH the result. Only `Less` is different from Template A. For a heap of points or structs, `Less` compares one property of the two items. Do not negate the values to get a max-heap when a correct `Less` does the same.

> [!quote] Say it
> "A max-heap in Go is the same five methods with the comparison in Less turned around."

### Template D: Two heaps for the median

> [!tip] Signal
> You must give the median, or the middle items, of a stream after each new value.

```go
// TEMPLATE D: two heaps cut a stream in the middle.
type halves struct {
    // the smaller half: its top is the largest value of this half
    small maxHeap
    // the larger half: its top is the smallest value of this half
    large minHeap
}

func (s *halves) add(x int) {
    heap.Push(&s.small, x) // 1. ADD to small
    // 2. MOVE the top of small to large
    heap.Push(&s.large, heap.Pop(&s.small))
    // 3. BALANCE: small has the same size or one more
    if len(s.large) > len(s.small) {
        heap.Push(&s.small, heap.Pop(&s.large))
    }
}

func (s *halves) median() float64 {
    if len(s.small) > len(s.large) {
        return float64(s.small[0]) // odd count
    }
    return float64(s.small[0]+s.large[0]) / 2 // even count
}
```

The moves are ADD, MOVE, then BALANCE. The move through `small` makes sure that each value in `small` is less than or equal to each value in `large`. The balance keeps the two sizes equal, or gives `small` one more. Then the median is always at the tops.

> [!quote] Say it
> "A max-heap holds the smaller half and a min-heap holds the larger half. An insert is O(log n) and the median is O(1) from the two tops."

### Template E: Max-heap plus cooldown queue

> [!tip] Signal
> You schedule tasks, and the same type of task must wait some time before it runs again. The problem asks for the least total time.

```go
// TEMPLATE E: greedy with a max-heap and a cooldown queue.
// counts[i] is the number of tasks of type i (1 or more). A type waits gap
// units between runs.
func timeToRunAll(counts []int, gap int) int {
    h := maxHeap(slices.Clone(counts))
    heap.Init(&h)
    type waiting struct{ left, readyAt int }
    // the types that cool down, in the order they become ready
    queue := []waiting{}
    now := 0
    for len(h) > 0 || len(queue) > 0 {
        if len(h) == 0 {
            // IDLE: jump to the end of the first wait
            now = queue[0].readyAt
        } else {
            now++
            // 1. RUN the type with the most tasks left
            left := heap.Pop(&h).(int) - 1
            if left > 0 {
                // 2. COOL DOWN
                queue = append(queue, waiting{left, now + gap})
            }
        }
        if len(queue) > 0 && queue[0].readyAt == now {
            heap.Push(&h, queue[0].left) // 3. RELEASE back into the heap
            queue = queue[1:]
        }
    }
    return now
}
```

The moves are RUN, COOL DOWN, then RELEASE. The heap gives the type with the most tasks left, because that type is the one that causes idle time. The queue holds the types that wait. The queue is already in time order, so it does not need a heap.

> [!quote] Say it
> "I always run the most frequent task that is ready. A max-heap gives that task, and a queue holds the tasks in cooldown until they can go back."

### Template F: K-way merge with a heap

> [!tip] Signal
> You have K sorted lists, and you want the items of all the lists in order. Frequently you need only the first few items.

```go
// TEMPLATE F: merge K sorted lists. The heap holds one cursor for each
// list.
type cursor struct{ value, list, index int }

type cursorHeap []cursor

// Len, Swap, Push and Pop are the same as in Template A, with cursor in
// place of int.
func (h cursorHeap) Less(i, j int) bool { return h[i].value < h[j].value }

func mergeSorted(lists [][]int) []int {
    h := cursorHeap{}
    for i, l := range lists {
        if len(l) > 0 {
            // 1. START: the first item of each list
            h = append(h, cursor{l[0], i, 0})
        }
    }
    heap.Init(&h)
    res := []int{}
    for len(h) > 0 {
        // 2. POP the smallest item of all the lists
        top := heap.Pop(&h).(cursor)
        res = append(res, top.value)
        // 3. ADVANCE in the same list
        if next := top.index + 1; next < len(lists[top.list]) {
            heap.Push(&h, cursor{lists[top.list][next], top.list, next})
        }
    }
    return res
}
```

The moves are START with the first item of each list, POP the best item, then ADVANCE in the list that it came from. The heap never holds more than K items. Each heap item must know its list and its index, or you cannot advance.

> [!quote] Say it
> "The heap holds one item from each list. I pop the smallest and push the next item from the same list, so each step is O(log K)."

> [!warning] Mistakes in this stage
> - `h.Push(x)` calls your method, and it only appends. Call `heap.Push(&h, x)` to keep the heap order.
> - `heap.Pop` returns `any`. Add a type assertion, as in `heap.Pop(&h).(int)`.
> - A slice that you fill with `append` is not a heap. Call `heap.Init` before the first pop.
> - A read of `h[0]` on an empty heap panics. Test `len(h) > 0` before you peek.

## Solved with comments

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 703. Kth Largest Element in a Stream

[LeetCode 703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · Easy

- **Pattern:** Min-heap of size K
- **Template:** [[#Template A: The five heap methods|A: The five heap methods]], [[#Template B: Heap of size K|B: Heap of size K]]
- **Complexity:** time O(log k) for each Add, O(n log k) for the constructor, space O(k)
- **Imports for a local file:** `container/heap`

**Idea.** Keep only the k largest values in a min-heap. The top of the heap is the smallest of them, and that value is the kth largest of the stream.

**Go lesson.** Go has no priority queue type. You write five methods on your type, and the functions `heap.Push` and `heap.Pop` of `container/heap` keep the order.

```go
// KthLargest solves LC 703. Add is O(log k) time. The space is O(k).
// The min-heap holds the k largest values. Its top is the kth largest
// value.
type minHeap []int

func (h minHeap) Len() int { return len(h) }

// min-heap: smallest on top
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// Push and Pop change the length of the slice, so they need a pointer
// receiver.
// x.(int): from any back to int
func (h *minHeap) Push(x any) { *h = append(*h, x.(int)) }
func (h *minHeap) Pop() any {
    old := *h
    n := len(old)
    // container/heap moves the top to the end before it calls Pop
    x := old[n-1]
    *h = old[:n-1]
    return x
}

type KthLargest struct {
    k int
    h minHeap
}

func Constructor(k int, nums []int) KthLargest {
    this := KthLargest{k: k}
    for _, x := range nums {
        this.Add(x) // the same rule for the first values and for the stream
    }
    return this
}

func (this *KthLargest) Add(val int) int {
    heap.Push(&this.h, val) // PUSH: call heap.Push, not this.h.Push
    if len(this.h) > this.k {
        // TRIM: remove the smallest, it cannot be the kth largest
        heap.Pop(&this.h)
    }
    return this.h[0] // PEEK: index 0 is always the top of the heap
}
```

### 1046. Last Stone Weight

[LeetCode 1046](https://leetcode.com/problems/last-stone-weight/) · Easy

- **Pattern:** Max-heap simulation
- **Template:** [[#Template C: Max-heap by a different Less|C: Max-heap by a different Less]]
- **Complexity:** time O(n log n), space O(n)
- **Imports for a local file:** `container/heap`, `slices`

**Idea.** Each turn needs the two heaviest stones. A max-heap gives them in O(log n). Push the difference back when it is not zero.

**Go lesson.** `maxHeap(x)` is a type conversion, not a function call. It works because `maxHeap` and `[]int` have the same underlying type.

```go
// lastStoneWeight solves LC 1046. Time O(n log n), space O(n).
// A max-heap is the min-heap with the opposite Less.
type maxHeap []int

func (h maxHeap) Len() int { return len(h) }

// max-heap: largest on top
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func lastStoneWeight(stones []int) int {
    // a copy, so the input keeps its order
    h := maxHeap(slices.Clone(stones))
    heap.Init(&h) // BUILD the heap in O(n)
    for len(h) > 1 {
        // POP the heaviest stone. .(int) converts from any
        a := heap.Pop(&h).(int)
        b := heap.Pop(&h).(int) // POP the second heaviest stone
        if a != b {
            // PUSH the rest back. a >= b, so a-b is positive
            heap.Push(&h, a-b)
        }
    }
    if len(h) == 0 {
        return 0 // all the stones are gone
    }
    return h[0]
}
```

### 973. K Closest Points to Origin

[LeetCode 973](https://leetcode.com/problems/k-closest-points-to-origin/) · Medium

- **Pattern:** Max-heap of size K
- **Template:** [[#Template B: Heap of size K|B: Heap of size K]], [[#Template C: Max-heap by a different Less|C: Max-heap by a different Less]]
- **Complexity:** time O(n log k), space O(k)
- **Imports for a local file:** `container/heap`

**Idea.** Keep the k closest points in a max-heap by distance. When the heap has more than k points, remove the farthest one. Compare squared distances, so no square root is necessary.

**Go lesson.** `Less` can compare any property of the items. Here the heap holds `[]int` points, and `Less` compares their squared distances.

```go
// kClosest solves LC 973. Time O(n log k), space O(k).
// A max-heap of size k keeps the k closest points. Its top is the farthest
// of them.
type pointHeap [][]int

// dist is the squared distance to the origin. The order is the same as for
// the real distance.
func dist(p []int) int { return p[0]*p[0] + p[1]*p[1] }

func (h pointHeap) Len() int { return len(h) }

// farthest on top
func (h pointHeap) Less(i, j int) bool { return dist(h[i]) > dist(h[j]) }
func (h pointHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *pointHeap) Push(x any)        { *h = append(*h, x.([]int)) }
func (h *pointHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func kClosest(points [][]int, k int) [][]int {
    h := pointHeap{}
    for _, p := range points {
        heap.Push(&h, p) // PUSH each point
        if len(h) > k {
            heap.Pop(&h) // TRIM: the farthest point cannot be in the answer
        }
    }
    return h // the k points that stay. LeetCode accepts any order
}
```

### 215. Kth Largest Element in an Array

[LeetCode 215](https://leetcode.com/problems/kth-largest-element-in-an-array/) · Medium

- **Pattern:** Min-heap of size K
- **Template:** [[#Template A: The five heap methods|A: The five heap methods]], [[#Template B: Heap of size K|B: Heap of size K]]
- **Complexity:** time O(n log k), space O(k)
- **Imports for a local file:** `container/heap`

**Idea.** Keep the k largest values in a min-heap. After the last value, the top of the heap is the smallest of the k largest. That value is the answer.

**Go lesson.** `h[0]` reads the top of the heap with no pop. The heap is a slice, and `container/heap` keeps the smallest item at index 0.

```go
// findKthLargest solves LC 215. Time O(n log k), space O(k).
// A min-heap of size k holds the k largest values. Its top is the kth
// largest.
// Quickselect is the other standard answer: O(n) average time, O(n²) in the
// worst case.
type minHeap []int

func (h minHeap) Len() int { return len(h) }

// min-heap: smallest on top
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *minHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func findKthLargest(nums []int, k int) int {
    h := minHeap{}
    for _, x := range nums {
        heap.Push(&h, x) // PUSH each value
        if len(h) > k {
            // TRIM: remove the smallest, so only the k largest stay
            heap.Pop(&h)
        }
    }
    return h[0] // PEEK: the smallest of the k largest values
}
```

### 621. Task Scheduler

[LeetCode 621](https://leetcode.com/problems/task-scheduler/) · Medium

- **Pattern:** Max-heap plus cooldown queue
- **Template:** [[#Template C: Max-heap by a different Less|C: Max-heap by a different Less]], [[#Template E: Max-heap plus cooldown queue|E: Max-heap plus cooldown queue]]
- **Complexity:** time O(m) for m tasks, space O(1)
- **Imports for a local file:** `container/heap`

**Idea.** Always run the task type that has the most tasks left, so the frequent types do not pile up at the end. After a run, the type waits in a queue until its cooldown ends. Then it goes back into the heap.

**Go lesson.** A type declared inside a function, such as `waiting`, is visible only in that function. A slice is the queue: `append` adds at the back and `queue[1:]` removes the front.

```go
// leastInterval solves LC 621. Time O(m) for m tasks, space O(1): 26 types
// or fewer.
// The max-heap holds the counts of the task types that can run now.
// The queue holds the types that wait for their cooldown, in the order they
// become ready.
// There is also an O(m) formula with no heap: max(m, (maxCount-1)*(n+1) +
// typesWithMaxCount).
type maxHeap []int

func (h maxHeap) Len() int { return len(h) }

// max-heap: largest count on top
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func leastInterval(tasks []byte, n int) int {
    var count [26]int
    for _, t := range tasks {
        count[t-'A']++ // COUNT the tasks of each type
    }
    h := maxHeap{}
    for _, c := range count {
        if c > 0 {
            h = append(h, c) // only the count matters, not the letter
        }
    }
    heap.Init(&h)

    // tasks left, and the last time unit of the wait
    type waiting struct{ left, readyAt int }
    queue := []waiting{}
    now := 0 // the number of time units used so far
    for len(h) > 0 || len(queue) > 0 {
        if len(h) == 0 {
            // IDLE: no type can run, so jump to the end of the wait
            now = queue[0].readyAt
        } else {
            now++
            // RUN the type with the most tasks left
            left := heap.Pop(&h).(int) - 1
            if left > 0 {
                // COOL DOWN for n units
                queue = append(queue, waiting{left, now + n})
            }
        }
        if len(queue) > 0 && queue[0].readyAt == now {
            heap.Push(&h, queue[0].left) // RELEASE: the wait is over
            queue = queue[1:]
        }
    }
    return now
}
```

### 355. Design Twitter

[LeetCode 355](https://leetcode.com/problems/design-twitter/) · Medium

- **Pattern:** K-way merge with a heap
- **Template:** [[#Template F: K-way merge with a heap|F: K-way merge with a heap]]
- **Complexity:** time O(F + 10 log F) for a feed of F users, O(1) for the rest, space O(P + T) for P follow pairs and T tweets
- **Imports for a local file:** `container/heap`

**Idea.** Each user has a list of tweets in time order, so a feed is a merge of sorted lists. Put the newest tweet of each list in a max-heap. Pop a tweet, push the tweet before it from the same list, and stop after 10 tweets.

**Go lesson.** A read of a missing map key gives the zero value. So `append` to a missing key and `delete` on a missing inner map are safe, but a write to a `nil` inner map panics.

```go
// Twitter solves LC 355. A feed is O(F + 10 log F) time for F followed
// users.
// A feed is a K-way merge: each user's tweets are one list in time order.
type tweet struct{ time, id int }

// feedItem is one tweet in the heap, with the list and the index that it
// came from.
type feedItem struct{ time, id, user, index int }

type feedHeap []feedItem

func (h feedHeap) Len() int { return len(h) }

// newest on top
func (h feedHeap) Less(i, j int) bool { return h[i].time > h[j].time }
func (h feedHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *feedHeap) Push(x any)        { *h = append(*h, x.(feedItem)) }
func (h *feedHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

type Twitter struct {
    clock int // goes up by one for each tweet
    // user -> the tweets of that user, oldest first
    tweets map[int][]tweet
    // user -> the set of users that this user follows
    following map[int]map[int]struct{}
}

func Constructor() Twitter {
    return Twitter{tweets: map[int][]tweet{}, following: map[int]map[int]struct{}{}}
}

func (this *Twitter) PostTweet(userId int, tweetId int) {
    this.clock++
    // append works on a missing key: the zero value of a slice is nil.
    this.tweets[userId] = append(this.tweets[userId], tweet{this.clock, tweetId})
}

func (this *Twitter) GetNewsFeed(userId int) []int {
    h := feedHeap{}
    start := func(user int) { // START: take the newest tweet of one list
        list := this.tweets[user]
        if last := len(list) - 1; last >= 0 {
            h = append(h, feedItem{list[last].time, list[last].id, user, last})
        }
    }
    start(userId) // a user also sees their own tweets
    for followee := range this.following[userId] {
        if followee != userId {
            start(followee)
        }
    }
    heap.Init(&h)

    feed := []int{}
    for len(h) > 0 && len(feed) < 10 {
        // POP the newest tweet of all the lists
        top := heap.Pop(&h).(feedItem)
        feed = append(feed, top.id)
        // ADVANCE: push the tweet before it from the same list
        if top.index > 0 {
            prev := this.tweets[top.user][top.index-1]
            heap.Push(&h, feedItem{prev.time, prev.id, top.user, top.index - 1})
        }
    }
    return feed
}

func (this *Twitter) Follow(followerId int, followeeId int) {
    if this.following[followerId] == nil {
        // make the inner set on first use
        this.following[followerId] = map[int]struct{}{}
    }
    this.following[followerId][followeeId] = struct{}{}
}

func (this *Twitter) Unfollow(followerId int, followeeId int) {
    // delete on a nil map does nothing
    delete(this.following[followerId], followeeId)
}
```

### 295. Find Median from Data Stream

[LeetCode 295](https://leetcode.com/problems/find-median-from-data-stream/) · Hard

- **Pattern:** Two heaps
- **Template:** [[#Template D: Two heaps for the median|D: Two heaps for the median]]
- **Complexity:** time O(log n) for AddNum, O(1) for FindMedian, space O(n)
- **Imports for a local file:** `container/heap`

**Idea.** Split the values into a small half and a large half. A max-heap holds the small half and a min-heap holds the large half, so the two tops are the middle values. Keep the sizes equal, or give the small half one more.

**Go lesson.** `heap.Pop` returns `any` and `heap.Push` accepts `any`. So a value moves from one heap to the other with no type assertion.

```go
// MedianFinder solves LC 295. AddNum is O(log n) time, FindMedian is O(1).
// small is a max-heap with the smaller half. large is a min-heap with the
// larger half.
// The median is the top of small, or the average of the two tops.
type minHeap []int

func (h minHeap) Len() int { return len(h) }

// min-heap: smallest on top
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *minHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

// maxHeap is the same type with the opposite Less.
type maxHeap []int

func (h maxHeap) Len() int { return len(h) }

// max-heap: largest on top
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

type MedianFinder struct {
    // the smaller half: its top is the largest value of this half
    small maxHeap
    // the larger half: its top is the smallest value of this half
    large minHeap
}

func Constructor() MedianFinder {
    return MedianFinder{} // the zero value of a slice is an empty heap
}

func (this *MedianFinder) AddNum(num int) {
    heap.Push(&this.small, num) // 1. ADD to the small half
    // 2. MOVE the largest value of small to large.
    // Now each value in small is less than or equal to each value in large.
    heap.Push(&this.large, heap.Pop(&this.small))
    if len(this.large) > len(this.small) {
        // 3. BALANCE: small has the same size as large, or one more.
        heap.Push(&this.small, heap.Pop(&this.large))
    }
}

func (this *MedianFinder) FindMedian() float64 {
    if len(this.small) > len(this.large) {
        // odd count: the middle value is the top of small
        return float64(this.small[0])
    }
    // Even count: the average of the two middle values. Convert before you
    // divide,
    // because int division drops the fraction.
    return float64(this.small[0]+this.large[0]) / 2
}
```

---

[[wiki/neetcode-150/08-tries|← Tries]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/10-backtracking|Backtracking →]]
