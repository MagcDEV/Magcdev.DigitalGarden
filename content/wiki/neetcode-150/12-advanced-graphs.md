---
title: "NeetCode 150, stage 12: Advanced Graphs"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - graphs
date_created: 2026-11-11
date_modified: 2026-11-11
---

# NeetCode 150, stage 12: Advanced Graphs

[[wiki/neetcode-150/11-graphs|← Graphs]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/13-dp-1d|1-D Dynamic Programming →]]

In this stage the edges have a cost, or the problem puts a rule on the path. The question changes from "can I reach the node" to "what is the cheapest way". You learn five classic algorithms. Each one is a small change to the DFS, the BFS or the heap that you already know.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 10: Grids and graphs|the Go syntax for this stage]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/12-advanced-graphs#332. Reconstruct Itinerary\|332. Reconstruct Itinerary]] | Hard | Eulerian path (Hierholzer) | [[wiki/neetcode-150/12-advanced-graphs#Template D: Hierholzer's algorithm\|D: Hierholzer's algorithm]] |
| 2 | [[wiki/neetcode-150/12-advanced-graphs#1584. Min Cost to Connect All Points\|1584. Min Cost to Connect All Points]] | Medium | Minimum spanning tree (Prim) | [[wiki/neetcode-150/12-advanced-graphs#Template B: Prim with a heap\|B: Prim with a heap]], [[wiki/neetcode-150/12-advanced-graphs#Template F: Min-heap of items\|F: Min-heap of items]] |
| 3 | [[wiki/neetcode-150/12-advanced-graphs#743. Network Delay Time\|743. Network Delay Time]] | Medium | Dijkstra with a heap | [[wiki/neetcode-150/12-advanced-graphs#Template A: Dijkstra with a heap\|A: Dijkstra with a heap]], [[wiki/neetcode-150/12-advanced-graphs#Template F: Min-heap of items\|F: Min-heap of items]] |
| 4 | [[wiki/neetcode-150/12-advanced-graphs#778. Swim in Rising Water\|778. Swim in Rising Water]] | Hard | Dijkstra, minimise the maximum | [[wiki/neetcode-150/12-advanced-graphs#Template A: Dijkstra with a heap\|A: Dijkstra with a heap]], [[wiki/neetcode-150/12-advanced-graphs#Template F: Min-heap of items\|F: Min-heap of items]] |
| 5 | [[wiki/neetcode-150/12-advanced-graphs#269. Alien Dictionary\|269. Alien Dictionary]] | Hard | Topological sort from comparisons | [[wiki/neetcode-150/12-advanced-graphs#Template E: Topological sort from comparisons\|E: Topological sort from comparisons]] |
| 6 | [[wiki/neetcode-150/12-advanced-graphs#787. Cheapest Flights Within K Stops\|787. Cheapest Flights Within K Stops]] | Medium | Bellman-Ford with a round limit | [[wiki/neetcode-150/12-advanced-graphs#Template C: Bellman-Ford with a round limit\|C: Bellman-Ford with a round limit]] |

## Templates to memorize

### Template A: Dijkstra with a heap

> [!tip] Signal
> The edges have costs that are not negative. The problem asks for the shortest path, the minimum time or the lowest cost from one start node. A variant asks you to make the largest value on the path as small as possible.

```go
// TEMPLATE A: Dijkstra with a heap. adj[v] holds the edges of v as items
// {cost of the edge, neighbour}. It returns the lowest cost from src to
// each node.
// item and minHeap are the types of Template F.
func shortestPaths(adj [][]item, src int) []int {
    dist := make([]int, len(adj))
    for i := range dist {
        dist[i] = -1 // -1 = no final cost yet
    }
    h := &minHeap{{cost: 0, node: src}} // 1. SEED: the start node costs 0
    for h.Len() > 0 {
        cur := heap.Pop(h).(item) // 2. POP the item with the lowest cost
        // 3. SKIP: this node is final, the item is old
        if dist[cur.node] != -1 {
            continue
        }
        // 4. FINAL: the first pop of a node is its lowest cost
        dist[cur.node] = cur.cost
        for _, e := range adj[cur.node] {
            // 5. PUSH the cost of the full path through cur
            if dist[e.node] == -1 {
                heap.Push(h, item{cost: cur.cost + e.cost, node: e.node})
            }
        }
    }
    return dist // -1 stays for a node that src cannot reach
}
```

The moves are SEED, POP, SKIP, FINAL, then PUSH. The heap can hold many items for one node, and only the first pop of a node counts. This is why the SKIP check is necessary. For the "minimise the maximum" variant, change only the PUSH. The new cost is the larger of the current cost and the cost of the next cell.

> [!quote] Say it
> "Dijkstra always finalises the closest node next, and a min-heap gives me that node. Each edge goes into the heap at most once, so it's O(E log V)."

### Template B: Prim with a heap

> [!tip] Signal
> The problem asks for the minimum cost to connect all the points, all the cities or all the computers. The answer is a minimum spanning tree.

```go
// TEMPLATE B: Prim with a heap. It returns the cost of the minimum spanning
// tree
// of a connected graph. item and minHeap are the types of Template F.
func spanningTreeCost(adj [][]item) int {
    inTree := make([]bool, len(adj))
    // 1. SEED: start at node 0, and pay 0 for it
    h := &minHeap{{cost: 0, node: 0}}
    total, joined := 0, 0
    for h.Len() > 0 && joined < len(adj) {
        // 2. POP the cheapest edge that leaves the tree
        cur := heap.Pop(h).(item)
        // 3. SKIP: a cheaper edge already connected this node
        if inTree[cur.node] {
            continue
        }
        // 4. JOIN: the node enters the tree, pay for the edge
        inTree[cur.node] = true
        total += cur.cost
        joined++
        for _, e := range adj[cur.node] {
            if !inTree[e.node] {
                // 5. PUSH the cost of the edge only, not of the path
                heap.Push(h, e)
            }
        }
    }
    return total
}
```

The moves are SEED, POP, SKIP, JOIN, then PUSH. These are the moves of Dijkstra with one difference: the cost that you push. Dijkstra pushes the cost of the full path from the start. Prim pushes the cost of one edge only. If you push the cost of the path, you get a wrong tree.

> [!quote] Say it
> "Prim grows one tree from any node and always adds the cheapest edge that leaves the tree. With a heap that's O(E log V). Here every pair of points is an edge, so E is n squared."

### Template C: Bellman-Ford with a round limit

> [!tip] Signal
> The problem asks for the cheapest path with at most `k` stops, or with a limit on the number of edges. Plain Dijkstra fails here, because the cheapest path to a node can use too many edges.

```go
// TEMPLATE C: Bellman-Ford with a round limit. An edge is [from, to, cost].
// It returns the lowest cost from src to dst with at most maxEdges edges,
// or -1.
func cheapestWithLimit(n int, edges [][]int, src, dst, maxEdges int) int {
    const inf = math.MaxInt32
    dist := make([]int, n)
    for i := range dist {
        dist[i] = inf
    }
    dist[src] = 0
    // 1. ROUND: each path can get one more edge
    for round := 0; round < maxEdges; round++ {
        next := make([]int, n)
        // 2. COPY: read the last round, write the new round
        copy(next, dist)
        for _, e := range edges {
            from, to, cost := e[0], e[1], e[2]
            if dist[from] != inf && dist[from]+cost < next[to] {
                // 3. RELAX: a cheaper path to the node "to"
                next[to] = dist[from] + cost
            }
        }
        dist = next
    }
    if dist[dst] == inf {
        return -1
    }
    return dist[dst]
}
```

The moves are ROUND, COPY, then RELAX. After round `i`, the slice holds the lowest cost with at most `i` edges. A path with `k` stops has `k + 1` edges, so run `k + 1` rounds. Read from the slice of the last round and write to the copy. Without the copy, one round can use two edges in a row, and the limit does not hold.

> [!quote] Say it
> "K stops means k plus one flights. I relax every edge k plus one times, and each round reads the previous round's costs from a copy. That's O(k times E)."

### Template D: Hierholzer's algorithm

> [!tip] Signal
> You must use each edge exactly one time: each ticket, each domino or each street. The answer is an Eulerian path.

```go
// TEMPLATE D: Hierholzer's algorithm. It returns a path that uses each edge
// one time.
// adj[v] lists the neighbours of v. Sort each list first if the order is
// important.
func eulerPath(adj map[string][]string, start string) []string {
    path := []string{}
    var visit func(v string)
    visit = func(v string) {
        for len(adj[v]) > 0 {
            next := adj[v][0]
            // 1. USE the edge: remove it before the call
            adj[v] = adj[v][1:]
            visit(next)
        }
        path = append(path, v) // 2. ADD v only after all its edges are used
    }
    visit(start)
    slices.Reverse(path) // 3. REVERSE: the path was built from its end
    return path
}
```

The moves are USE, ADD, then REVERSE. Add a node to the path only after all its edges are used. So a dead end goes into the path first, and the reverse puts the dead end last. A plain greedy walk fails, because the smallest next node can be a dead end. If the problem wants the smallest path in dictionary order, sort each list of neighbours first.

> [!quote] Say it
> "Using every ticket once is an Eulerian path. I run a DFS that removes each edge as it uses it and adds each node in post-order, then I reverse the result. Sorting the destinations first gives the smallest order."

### Template E: Topological sort from comparisons

> [!tip] Signal
> The input is a list that is already sorted by a rule that you do not know, and you must find the rule. The input has no edges. You get the edges when you compare adjacent items.

```go
// TEMPLATE E: topological sort built from comparisons. The words are in
// sorted order.
// orderRules returns each rule "x comes before y" as the edge [2]byte{x,
// y}.
func orderRules(words []string) (rules [][2]byte, ok bool) {
    // 1. COMPARE each word with the next word only
    for i := 0; i+1 < len(words); i++ {
        a, b := words[i], words[i+1]
        j := 0
        // 2. SKIP the common prefix
        for j < len(a) && j < len(b) && a[j] == b[j] {
            j++
        }
        if j < len(a) && j < len(b) {
            // 3. EDGE: the first different letters
            rules = append(rules, [2]byte{a[j], b[j]})
        } else if len(a) > len(b) {
            // 4. PREFIX CHECK: "abc" before "ab" is never valid
            return nil, false
        }
    }
    // 5. KAHN: sort the letters with these edges. A cycle is not valid
    return rules, true
}
```

The moves are COMPARE, SKIP, EDGE, PREFIX CHECK, then KAHN. Compare each word with the next word only. The first different letter gives one rule, and the letters after that position give no rule. Then sort the letters with Kahn's algorithm, which is [[wiki/neetcode-150/11-graphs#Template D: Topological sort|Template D on the Graphs page]]. Two results mean that no order is valid: a longer word before its own prefix, and a cycle in the rules.

> [!quote] Say it
> "Each pair of adjacent words gives at most one edge: the first letters that differ. Then it's a topological sort of at most 26 letters. A cycle, or a word before its own prefix, means the input is invalid."

### Template F: Min-heap of items

> [!tip] Signal
> You need the item with the lowest cost many times, and new items arrive during the search. Dijkstra and Prim use this type.

```go
// TEMPLATE F: a min-heap of items for container/heap. Go has no built-in
// priority queue.
// one entry: a node and the cost to get there
type item struct{ cost, node int }

// a slice type with the five methods that container/heap needs
type minHeap []item

func (h minHeap) Len() int { return len(h) }

// lowest cost on top
func (h minHeap) Less(i, j int) bool { return h[i].cost < h[j].cost }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// pointer: the length changes
func (h *minHeap) Push(x any) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() any {
    old := *h
    // container/heap moves the top item to the end first
    x := old[len(old)-1]
    *h = old[:len(old)-1]
    return x
}

// Use the heap with heap.Push(h, x) and heap.Pop(h).(item), never with
// h.Push or h.Pop.
func cheapestNode(items []item) int {
    h := &minHeap{}
    for _, it := range items {
        heap.Push(h, it) // O(log n)
    }
    // O(log n): Pop returns any, so assert the type
    return heap.Pop(h).(item).node
}
```

The moves are the five methods: LEN, LESS, SWAP, PUSH and POP. The `Less` method sets the order, so change only `Less` for a max-heap. The `Push` and `Pop` methods have a pointer receiver, because they change the length of the slice. Always call `heap.Push(h, x)` and `heap.Pop(h)`. A direct call such as `h.Push(x)` only appends, and the heap order breaks.

> [!quote] Say it
> "Go has no built-in priority queue. I define a slice type with Len, Less, Swap, Push and Pop, and container/heap does the rest. Push and pop are O(log n)."

> [!warning] Mistakes in this stage
> - `h.Push(x)` only appends to the slice. Call `heap.Push(h, x)` and `heap.Pop(h)` to keep the heap order.
> - `heap.Pop(h)` returns `any`. Add the type assertion: `heap.Pop(h).(item)`.
> - `next := dist` does not copy a slice, because the two names share one array. Use `make` and `copy`.
> - Dijkstra is not correct if an edge has a negative cost. Use Bellman-Ford for such a graph.

## Solved with comments

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 332. Reconstruct Itinerary

[LeetCode 332](https://leetcode.com/problems/reconstruct-itinerary/) · Hard

- **Pattern:** Eulerian path (Hierholzer)
- **Template:** [[#Template D: Hierholzer's algorithm|D: Hierholzer's algorithm]]
- **Complexity:** time O(E log E) for E tickets (the sort costs the most), space O(E)
- **Imports for a local file:** `slices`, `sort`

**Idea.** The itinerary uses each ticket one time, so it is an Eulerian path. Always fly to the smallest destination that has a ticket left. Add an airport to the route only when it has no ticket left, then reverse the route, so a dead end goes last.

**Go lesson.** `sort.Strings` sorts a slice of strings in place, and `slices.Reverse` reverses a slice in place. `s = s[1:]` removes the first item in O(1).

```go
// findItinerary solves LC 332. Time O(E log E), space O(E).
// A DFS removes each ticket when it uses it, and adds the airport in
// post-order.
func findItinerary(tickets [][]string) []string {
    // airport -> destinations of its tickets
    adj := make(map[string][]string)
    for _, t := range tickets {
        adj[t[0]] = append(adj[t[0]], t[1])
    }
    for from := range adj {
        sort.Strings(adj[from]) // the smallest destination comes first
    }

    // E tickets visit E + 1 airports
    route := make([]string, 0, len(tickets)+1)
    var visit func(airport string)
    visit = func(airport string) {
        for len(adj[airport]) > 0 { // a missing key reads as an empty slice
            next := adj[airport][0]
            // USE the ticket: remove it before the call
            adj[airport] = adj[airport][1:]
            visit(next)
        }
        // ADD the airport only when no ticket is left
        route = append(route, airport)
    }
    visit("JFK")

    slices.Reverse(route) // REVERSE: the route was built from its end
    return route
}
```

### 1584. Min Cost to Connect All Points

[LeetCode 1584](https://leetcode.com/problems/min-cost-to-connect-all-points/) · Medium

- **Pattern:** Minimum spanning tree (Prim)
- **Template:** [[#Template B: Prim with a heap|B: Prim with a heap]], [[#Template F: Min-heap of items|F: Min-heap of items]]
- **Complexity:** time O(n² log n) for n points, because each pair of points is an edge, space O(n²) for the heap
- **Imports for a local file:** `container/heap`

**Idea.** Grow one tree from point 0. The heap holds the edges that leave the tree. Always take the cheapest edge that goes to a point outside the tree, until all the points are in the tree.

**Go lesson.** Go has no built-in priority queue. A slice type with the five methods `Len`, `Less`, `Swap`, `Push` and `Pop` becomes a heap when you call `heap.Push(h, x)` and `heap.Pop(h)` from `container/heap`.

```go
// minCostConnectPoints solves LC 1584. Time O(n² log n), space O(n²).
// Prim's algorithm: the tree grows by the cheapest edge that leaves it.
func minCostConnectPoints(points [][]int) int {
    n := len(points)
    inTree := make([]bool, n)
    // SEED: start at point 0, and pay 0 for it
    h := &minHeap{{cost: 0, node: 0}}
    total, joined := 0, 0
    for h.Len() > 0 && joined < n {
        // POP the cheapest edge. Pop returns any, so assert the type
        cur := heap.Pop(h).(item)
        // SKIP: a cheaper edge already connected this point
        if inTree[cur.node] {
            continue
        }
        // JOIN: the point enters the tree, pay for the edge
        inTree[cur.node] = true
        total += cur.cost
        joined++
        for next := 0; next < n; next++ { // each other point is a neighbour
            if !inTree[next] {
                // PUSH the cost of the edge only, not the cost of the path.
                heap.Push(h, item{cost: distance(points[cur.node], points[next]), node: next})
            }
        }
    }
    return total
}

// distance returns the Manhattan distance between two points.
func distance(a, b []int) int {
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
}

func abs(x int) int { // the math package has Abs only for float64
    if x < 0 {
        return -x
    }
    return x
}

// item is one entry of the heap: a node and the cost to get there.
type item struct{ cost, node int }

// minHeap is a priority queue of items. The item with the lowest cost is on
// top.
// container/heap needs these five methods.
type minHeap []item

func (h minHeap) Len() int { return len(h) }

// min-heap by cost
func (h minHeap) Less(i, j int) bool { return h[i].cost < h[j].cost }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// pointer: the length changes
func (h *minHeap) Push(x any) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() any {
    old := *h
    // container/heap moves the top item to the end first
    x := old[len(old)-1]
    *h = old[:len(old)-1]
    return x
}
```

### 743. Network Delay Time

[LeetCode 743](https://leetcode.com/problems/network-delay-time/) · Medium

- **Pattern:** Dijkstra with a heap
- **Template:** [[#Template A: Dijkstra with a heap|A: Dijkstra with a heap]], [[#Template F: Min-heap of items|F: Min-heap of items]]
- **Complexity:** time O(E log E) for E edges, which is the same as O(E log V), space O(V + E)
- **Imports for a local file:** `container/heap`

**Idea.** The signal gets to each node by its shortest path from k. Dijkstra makes the nodes final in order of distance, so the last node that becomes final is the farthest. If some node never becomes final, the answer is -1.

**Go lesson.** `Push` and `Pop` have a pointer receiver because they change the length of the slice. `heap.Pop(h).(item)` is a type assertion from `any` to `item`.

```go
// networkDelayTime solves LC 743. Time O(E log E), space O(V + E).
// The answer is the distance to the farthest node, or -1 if a node gets no
// signal.
func networkDelayTime(times [][]int, n int, k int) int {
    // the nodes are 1..n, so index 0 stays unused
    adj := make([][]item, n+1)
    for _, t := range times { // t = [from, to, time]
        adj[t[0]] = append(adj[t[0]], item{cost: t[2], node: t[1]})
    }

    done := make([]bool, n+1)         // done[v]: the distance to v is final
    h := &minHeap{{cost: 0, node: k}} // SEED: the start node costs 0
    reached, last := 0, 0
    for h.Len() > 0 {
        cur := heap.Pop(h).(item) // POP the item with the lowest cost
        // SKIP: this node is final, the item is old
        if done[cur.node] {
            continue
        }
        // FINAL: the first pop of a node is its shortest distance
        done[cur.node] = true
        reached++
        // the pops come in order of cost, so the last one is the largest
        last = cur.cost
        for _, e := range adj[cur.node] {
            if !done[e.node] { // PUSH the cost of the full path through cur
                heap.Push(h, item{cost: cur.cost + e.cost, node: e.node})
            }
        }
    }

    if reached < n { // some node gets no signal
        return -1
    }
    return last
}

// item is one entry of the heap: a node and the cost to get there.
type item struct{ cost, node int }

// minHeap is a priority queue of items. The item with the lowest cost is on
// top.
// container/heap needs these five methods.
type minHeap []item

func (h minHeap) Len() int { return len(h) }

// min-heap by cost
func (h minHeap) Less(i, j int) bool { return h[i].cost < h[j].cost }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// pointer: the length changes
func (h *minHeap) Push(x any) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() any {
    old := *h
    // container/heap moves the top item to the end first
    x := old[len(old)-1]
    *h = old[:len(old)-1]
    return x
}
```

### 778. Swim in Rising Water

[LeetCode 778](https://leetcode.com/problems/swim-in-rising-water/) · Hard

- **Pattern:** Dijkstra, minimise the maximum
- **Template:** [[#Template A: Dijkstra with a heap|A: Dijkstra with a heap]], [[#Template F: Min-heap of items|F: Min-heap of items]]
- **Complexity:** time O(n² log n) for an n x n grid, space O(n²)
- **Imports for a local file:** `container/heap`

**Idea.** The cost of a path is its highest cell, not the sum of its cells. Run Dijkstra with this cost: the cost to enter a neighbour is the larger of the current cost and the height of the neighbour. The first time the last cell leaves the heap, its cost is the answer.

**Go lesson.** The heap item is a small struct with three fields. A composite literal with field names, such as `item{cost: 3, r: 0, c: 1}`, is clear and safe if the fields change order.

```go
// swimInWater solves LC 778. Time O(n² log n), space O(n²).
// Dijkstra where the cost of a path is the highest cell on it.
func swimInWater(grid [][]int) int {
    n := len(grid)
    dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    done := make([][]bool, n) // done[r][c]: the cost of this cell is final
    for r := 0; r < n; r++ {
        done[r] = make([]bool, n)
    }

    // SEED: you stand on the first cell
    h := &minHeap{{cost: grid[0][0], r: 0, c: 0}}
    for h.Len() > 0 {
        // POP the cell that you can reach at the lowest water level
        cur := heap.Pop(h).(item)
        // SKIP: this cell is final, the item is old
        if done[cur.r][cur.c] {
            continue
        }
        done[cur.r][cur.c] = true // FINAL
        // the first pop of the last cell is the answer
        if cur.r == n-1 && cur.c == n-1 {
            return cur.cost
        }
        for _, d := range dirs {
            r, c := cur.r+d[0], cur.c+d[1]
            if r < 0 || r >= n || c < 0 || c >= n || done[r][c] {
                continue
            }
            // PUSH: the path costs its highest cell, so use max and not +.
            heap.Push(h, item{cost: max(cur.cost, grid[r][c]), r: r, c: c})
        }
    }
    // the last cell is always reachable, so this line does not run
    return -1
}

// item is one entry of the heap: a cell and the water level that you need
// to reach it.
type item struct{ cost, r, c int }

// minHeap is a priority queue of items. The item with the lowest cost is on
// top.
// container/heap needs these five methods.
type minHeap []item

func (h minHeap) Len() int { return len(h) }

// min-heap by cost
func (h minHeap) Less(i, j int) bool { return h[i].cost < h[j].cost }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// pointer: the length changes
func (h *minHeap) Push(x any) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() any {
    old := *h
    // container/heap moves the top item to the end first
    x := old[len(old)-1]
    *h = old[:len(old)-1]
    return x
}
```

### 269. Alien Dictionary

[LeetCode 269](https://leetcode.com/problems/alien-dictionary/) (premium) · [free on NeetCode](https://neetcode.io/problems/foreign-dictionary) · Hard

- **Pattern:** Topological sort from comparisons
- **Template:** [[#Template E: Topological sort from comparisons|E: Topological sort from comparisons]]
- **Complexity:** time O(C) for C letters in all the words (the alphabet has 26 letters at most), space O(n) for n words (26 letters, and at most one rule for each pair of adjacent words)

**Idea.** At the first position where two adjacent words differ, the letter of the first word comes before the letter of the second word. These rules are the edges of a graph. Kahn's algorithm gives an order, and a cycle or a word before its own prefix means that no order is valid.

**Go lesson.** An array has a fixed size and its zero value is ready to use, so `var indegree [26]int` needs no `make`. The index `w[i]-'a'` maps a letter to 0..25, and `string(order)` converts a `[]byte` to a string.

```go
// alienOrder solves LC 269. Time O(C) for C letters in the input, space
// O(n) for n words.
// It builds the rules "x before y" from adjacent words, then sorts with
// Kahn's algorithm.
func alienOrder(words []string) string {
    var after [26][]int  // after[x] = the letters that come after x
    var indegree [26]int // indegree[y] = the number of rules "x before y"
    var used [26]bool    // used[x]: the letter is in some word
    letters := 0
    for _, w := range words {
        for i := 0; i < len(w); i++ {
            if !used[w[i]-'a'] {
                used[w[i]-'a'] = true
                letters++
            }
        }
    }

    // COMPARE each word with the next word only
    for i := 0; i+1 < len(words); i++ {
        a, b := words[i], words[i+1]
        j := 0
        // SKIP the common prefix
        for j < len(a) && j < len(b) && a[j] == b[j] {
            j++
        }
        // EDGE: the first different letters give one rule
        if j < len(a) && j < len(b) {
            x, y := int(a[j]-'a'), int(b[j]-'a')
            after[x] = append(after[x], y)
            indegree[y]++
        } else if len(a) > len(b) {
            // PREFIX CHECK: "abc" before "ab" is never valid
            return ""
        }
    }

    // KAHN: start with the letters that have no letter before them.
    queue := []int{}
    for x := 0; x < 26; x++ {
        if used[x] && indegree[x] == 0 {
            queue = append(queue, x)
        }
    }
    order := make([]byte, 0, letters)
    for len(queue) > 0 {
        x := queue[0]
        queue = queue[1:]
        order = append(order, byte('a'+x)) // TAKE the letter
        for _, y := range after[x] {
            indegree[y]-- // RELEASE: one rule about y is done
            if indegree[y] == 0 {
                queue = append(queue, y)
            }
        }
    }

    // CYCLE CHECK: the rules contradict each other
    if len(order) < letters {
        return ""
    }
    return string(order)
}
```

### 787. Cheapest Flights Within K Stops

[LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) · Medium

- **Pattern:** Bellman-Ford with a round limit
- **Template:** [[#Template C: Bellman-Ford with a round limit|C: Bellman-Ford with a round limit]]
- **Complexity:** time O(k * E) for E flights, space O(n)
- **Imports for a local file:** `math`

**Idea.** At most k stops means at most k + 1 flights, so run k + 1 rounds. Each round lets each route use one more flight. Read the costs of the round before and write to a copy, so one round never uses two flights in a row.

**Go lesson.** `next := cost` does not copy a slice: the two names share one array. Make a new slice and use the built-in `copy(dst, src)`.

```go
// findCheapestPrice solves LC 787. Time O(k * E), space O(n).
// After round i, cost[c] is the lowest price to city c with at most i
// flights.
func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
    const inf = math.MaxInt32 // larger than each possible price
    cost := make([]int, n)
    for i := range cost {
        cost[i] = inf // no route yet
    }
    cost[src] = 0

    for round := 0; round <= k; round++ { // ROUND: k stops = k + 1 flights
        next := make([]int, n)
        copy(next, cost) // COPY: read the round before, write the new round
        for _, f := range flights {
            from, to, price := f[0], f[1], f[2]
            if cost[from] == inf { // no route to the city "from" yet
                continue
            }
            if cost[from]+price < next[to] { // RELAX: read cost, write next
                next[to] = cost[from] + price
            }
        }
        cost = next
    }

    if cost[dst] == inf {
        return -1
    }
    return cost[dst]
}
```

---

[[wiki/neetcode-150/11-graphs|← Graphs]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/13-dp-1d|1-D Dynamic Programming →]]
