---
title: "NeetCode 150, stage 11: Graphs"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - graphs
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 11: Graphs

[[wiki/neetcode-150/10-backtracking|← Backtracking]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/12-advanced-graphs|Advanced Graphs →]]

A graph problem is a search problem. You start at a node, and you visit each node that you can reach. This stage trains the three tools that do the visit: DFS, BFS and union-find. A grid is also a graph, because each cell is a node and its four neighbours are its edges.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 10: Grids and graphs|the Go syntax for this stage]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/11-graphs#200. Number of Islands\|200. Number of Islands]] | Medium | Grid DFS (flood fill) | [[wiki/neetcode-150/11-graphs#Template A: Grid DFS (flood fill)\|A: Grid DFS (flood fill)]] |
| 2 | [[wiki/neetcode-150/11-graphs#133. Clone Graph\|133. Clone Graph]] | Medium | DFS with a clone map | [[wiki/neetcode-150/11-graphs#Template C: Clone with a map\|C: Clone with a map]] |
| 3 | [[wiki/neetcode-150/11-graphs#695. Max Area of Island\|695. Max Area of Island]] | Medium | Grid DFS (flood fill) | [[wiki/neetcode-150/11-graphs#Template A: Grid DFS (flood fill)\|A: Grid DFS (flood fill)]] |
| 4 | [[wiki/neetcode-150/11-graphs#417. Pacific Atlantic Water Flow\|417. Pacific Atlantic Water Flow]] | Medium | DFS from the borders | [[wiki/neetcode-150/11-graphs#Template A: Grid DFS (flood fill)\|A: Grid DFS (flood fill)]] |
| 5 | [[wiki/neetcode-150/11-graphs#130. Surrounded Regions\|130. Surrounded Regions]] | Medium | DFS from the borders | [[wiki/neetcode-150/11-graphs#Template A: Grid DFS (flood fill)\|A: Grid DFS (flood fill)]] |
| 6 | [[wiki/neetcode-150/11-graphs#994. Rotting Oranges\|994. Rotting Oranges]] | Medium | Multi-source BFS by level | [[wiki/neetcode-150/11-graphs#Template B: BFS by level from many sources\|B: BFS by level from many sources]] |
| 7 | [[wiki/neetcode-150/11-graphs#286. Walls and Gates\|286. Walls and Gates]] | Medium | Multi-source BFS by level | [[wiki/neetcode-150/11-graphs#Template B: BFS by level from many sources\|B: BFS by level from many sources]] |
| 8 | [[wiki/neetcode-150/11-graphs#207. Course Schedule\|207. Course Schedule]] | Medium | Topological sort (Kahn) | [[wiki/neetcode-150/11-graphs#Template D: Topological sort\|D: Topological sort]] |
| 9 | [[wiki/neetcode-150/11-graphs#210. Course Schedule II\|210. Course Schedule II]] | Medium | Topological sort (Kahn) | [[wiki/neetcode-150/11-graphs#Template D: Topological sort\|D: Topological sort]] |
| 10 | [[wiki/neetcode-150/11-graphs#684. Redundant Connection\|684. Redundant Connection]] | Medium | Union-find, cycle detection | [[wiki/neetcode-150/11-graphs#Template E: Union-find\|E: Union-find]] |
| 11 | [[wiki/neetcode-150/11-graphs#323. Number of Connected Components in an Undirected Graph\|323. Number of Connected Components in an Undirected Graph]] | Medium | Union-find, count the groups | [[wiki/neetcode-150/11-graphs#Template E: Union-find\|E: Union-find]] |
| 12 | [[wiki/neetcode-150/11-graphs#261. Graph Valid Tree\|261. Graph Valid Tree]] | Medium | Union-find, cycle detection | [[wiki/neetcode-150/11-graphs#Template E: Union-find\|E: Union-find]] |
| 13 | [[wiki/neetcode-150/11-graphs#127. Word Ladder\|127. Word Ladder]] | Hard | BFS on an implicit graph | [[wiki/neetcode-150/11-graphs#Template F: BFS on an implicit graph\|F: BFS on an implicit graph]] |

## Templates to memorize

### Template A: Grid DFS (flood fill)

> [!tip] Signal
> The input is a grid, and the problem says island, region, area or "connected". You must count the groups of cells, measure them or change them.

```go
// TEMPLATE A: grid DFS (flood fill). It counts the groups of connected 1
// cells.
func countGroups(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    // down, up, right, left
    dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

    var fill func(r, c int) // declare first, so the closure can call itself
    fill = func(r, c int) {
        // 1. BOUNDS: outside the grid
        if r < 0 || r >= rows || c < 0 || c >= cols {
            return
        }
        if grid[r][c] != 1 { // 2. CHECK: not land, or already filled
            return
        }
        // 3. MARK before the calls, or the fill never stops
        grid[r][c] = 0
        for _, d := range dirs { // 4. SPREAD to the four neighbours
            fill(r+d[0], c+d[1])
        }
    }

    count := 0
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            // START: a 1 that no fill reached is a new group
            if grid[r][c] == 1 {
                count++
                fill(r, c)
            }
        }
    }
    return count
}
```

The moves are BOUNDS, CHECK, MARK, then SPREAD. Mark the cell before the recursive calls. If you mark the cell after the calls, two neighbours call each other without end. Some problems ask which cells can reach the border. For these problems, start the fill at the border cells. Then the cells that the fill did not mark are the surrounded cells.

> [!quote] Say it
> "Each cell is a node with four neighbours. I flood-fill from every land cell I have not visited, and I mark cells as I go, so each cell is visited once: O(m times n)."

### Template B: BFS by level from many sources

> [!tip] Signal
> The problem asks for the minimum time or the shortest distance in a grid, and many cells start at the same moment. The words "each minute", "nearest" and "spreads" are the signal.

```go
// TEMPLATE B: BFS by level from many sources. The 2 cells spread to the 1
// cells.
// It returns the number of levels until the spread stops.
func levelsToSpread(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    queue := [][2]int{} // a cell is a [2]int: row, column
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if grid[r][c] == 2 {
                // 1. SEED: all the sources go in first
                queue = append(queue, [2]int{r, c})
            }
        }
    }
    levels := 0
    for len(queue) > 0 {
        // 2. LEVEL: only the cells in the queue now
        for n := len(queue); n > 0; n-- {
            cell := queue[0]
            queue = queue[1:] // POP from the front
            for _, d := range dirs {
                r, c := cell[0]+d[0], cell[1]+d[1]
                if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != 1 {
                    continue
                }
                // 3. MARK when you push, not when you pop
                grid[r][c] = 2
                // 4. PUSH for the next level
                queue = append(queue, [2]int{r, c})
            }
        }
        if len(queue) > 0 {
            levels++ // 5. COUNT a level only if it reached new cells
        }
    }
    return levels
}
```

The moves are SEED, LEVEL, MARK, then PUSH. Put all the sources in the queue before the loop starts. Then one BFS gives each cell its distance to the nearest source. Mark a cell when you push it. If you mark a cell when you pop it, the same cell enters the queue many times.

> [!quote] Say it
> "I put all the sources in the queue first and run one BFS, level by level. Each level is one minute, and each cell enters the queue once, so it's O(m times n)."

### Template C: Clone with a map

> [!tip] Signal
> You must make a deep copy of a structure that has pointers, and the pointers can make a cycle.

```go
// TEMPLATE C: copy a graph with a map from each old node to its copy.
type graphNode struct {
    val   int
    edges []*graphNode
}

func copyGraph(start *graphNode) *graphNode {
    // old node -> copy, also the visited set
    copies := make(map[*graphNode]*graphNode)

    var copyNode func(old *graphNode) *graphNode
    copyNode = func(old *graphNode) *graphNode {
        if old == nil {
            return nil
        }
        // 1. CHECK: this node already has a copy
        if c, ok := copies[old]; ok {
            return c
        }
        c := &graphNode{val: old.val}
        // 2. STORE before the calls, so a cycle finds the copy
        copies[old] = c
        // 3. LINK the copy of each neighbour
        for _, next := range old.edges {
            c.edges = append(c.edges, copyNode(next))
        }
        return c
    }
    return copyNode(start)
}
```

The moves are CHECK, STORE, then LINK. The map has two jobs. It is the visited set, and it gives you the copy of each old node. Store the copy in the map before you copy its neighbours. If you store the copy later, a cycle makes the recursion run without end.

> [!quote] Say it
> "I keep a map from each original node to its clone. The map is also my visited set, so the DFS copies every node once: O(V + E)."

### Template D: Topological sort

> [!tip] Signal
> The problem says prerequisite, dependency, "before" or "order of tasks". The edges have a direction, and you must find a valid order or find a cycle.

```go
// TEMPLATE D: topological sort with Kahn's algorithm. An edge [a, b] means
// "a before b".
// It returns an order of all the n nodes, or nil if the graph has a cycle.
func topoOrder(n int, edges [][]int) []int {
    adj := make([][]int, n) // adj[a] = the nodes that wait for a
    // indegree[b] = the number of nodes that b waits for
    indegree := make([]int, n)
    for _, e := range edges { // 1. BUILD the lists and the counts
        adj[e[0]] = append(adj[e[0]], e[1])
        indegree[e[1]]++
    }
    queue := []int{}
    for v := 0; v < n; v++ {
        if indegree[v] == 0 { // 2. SEED: the nodes that wait for nothing
            queue = append(queue, v)
        }
    }
    order := make([]int, 0, n)
    for len(queue) > 0 {
        v := queue[0]
        queue = queue[1:]
        order = append(order, v) // 3. TAKE a node that is ready
        for _, w := range adj[v] {
            indegree[w]-- // 4. RELEASE: w waits for one node less
            if indegree[w] == 0 {
                queue = append(queue, w)
            }
        }
    }
    if len(order) < n { // 5. CYCLE CHECK: a node in a cycle never gets to 0
        return nil
    }
    return order
}
```

The moves are BUILD, SEED, TAKE, RELEASE, then CYCLE CHECK. This is Kahn's algorithm. The indegree of a node is the number of nodes that it waits for. A node in a cycle never gets to indegree 0. So if the order has fewer than `n` nodes, the graph has a cycle. Read the direction of each edge with care: in the course problems, the pair `[a, b]` means that `b` comes first.

> [!quote] Say it
> "I count the incoming edges of each node and start with the nodes that have none. Each node I take releases its neighbours. If I take fewer than n nodes, there is a cycle. It's O(V + E)."

### Template E: Union-find

> [!tip] Signal
> The edges have no direction, and they come one at a time. The problem asks if two nodes are connected, how many groups exist, or which edge closes a cycle.

```go
// TEMPLATE E: union-find. Each group of connected nodes has one root.
type unionFind struct {
    parent []int // parent[x] == x means that x is a root
    size   []int // size[root] = the number of nodes in the group
}

func newUnionFind(n int) *unionFind {
    u := &unionFind{parent: make([]int, n), size: make([]int, n)}
    for i := 0; i < n; i++ {
        u.parent[i] = i // each node starts as its own root
        u.size[i] = 1
    }
    return u
}

// find returns the root of the group of x.
func (u *unionFind) find(x int) int {
    if u.parent[x] != x {
        // PATH COMPRESSION: point x at the root
        u.parent[x] = u.find(u.parent[x])
    }
    return u.parent[x]
}

// union joins the groups of a and b. It returns false if they were one
// group already.
func (u *unionFind) union(a, b int) bool {
    ra, rb := u.find(a), u.find(b) // always work on the roots
    if ra == rb {
        return false // the edge a-b closes a cycle
    }
    if u.size[ra] < u.size[rb] {
        ra, rb = rb, ra // UNION BY SIZE: ra is the larger group
    }
    u.parent[rb] = ra // the smaller group goes below the larger group
    u.size[ra] += u.size[rb]
    return true
}
```

The moves are FIND with path compression, then UNION by size. The `union` method returns false when the two nodes are already in one group. That result tells you that the edge closes a cycle. Always join the roots, not the nodes. The line `parent[a] = b` is a frequent mistake, because it moves one node and not its group.

> [!quote] Say it
> "Union-find keeps one root per group. With path compression and union by size, each operation is almost O(1), so n edges cost about O(n)."

### Template F: BFS on an implicit graph

> [!tip] Signal
> The problem asks for the minimum number of steps to change one state into another state. The input has no edges. A rule tells you which states are one step apart.

```go
// TEMPLATE F: BFS on an implicit graph. A node is a state, and a function
// makes
// the neighbours of a state. It returns the number of steps to the goal, or
// -1.
func stepsToGoal(start, goal string, neighbours func(string) []string) int {
    seen := map[string]bool{start: true}
    queue := []string{start}
    for steps := 0; len(queue) > 0; steps++ {
        for n := len(queue); n > 0; n-- { // one level = one step
            state := queue[0]
            queue = queue[1:]
            // 1. GOAL: the first time that BFS sees it is the shortest
            if state == goal {
                return steps
            }
            // 2. GENERATE the neighbours now
            for _, next := range neighbours(state) {
                if !seen[next] {
                    seen[next] = true // 3. MARK when you push
                    queue = append(queue, next)
                }
            }
        }
    }
    return -1 // the queue is empty: no path
}
```

The moves are GOAL, GENERATE, then MARK. You do not build the graph. You make the neighbours of a state when you pop the state. For words, change one letter at a time and keep the results that are in the word set. This costs 26 tries for each letter, and that is cheaper than a comparison with each other word.

> [!quote] Say it
> "The words are nodes, and two words that differ by one letter share an edge. I don't build the edges; I generate the neighbours during a BFS. BFS finds the shortest chain."

> [!warning] Mistakes in this stage
> - `fill := func(r, c int) { ... }` cannot call itself. Declare `var fill func(r, c int)` first, then assign the function.
> - `grid[r][c] == 1` is always false on a `[][]byte` grid. The cells hold the characters `'0'` and `'1'`.
> - `make([][]bool, rows)` gives `rows` nil slices. Make each row in a loop before you write to it.
> - An index outside the grid is a panic in Go. Check the bounds before you read `grid[r][c]`.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 200. Number of Islands

[LeetCode 200](https://leetcode.com/problems/number-of-islands/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Grid DFS (flood fill)
> - **Template:** [[#Template A: Grid DFS (flood fill)|A: Grid DFS (flood fill)]]

> [!tip]- Step 2: the idea
> **Idea.** Scan the grid. Each land cell that no DFS reached is a new island. Count it, then sink the full island with a DFS, so no later cell counts it again.
>
> **Complexity.** Time O(m * n) for m rows and n columns, space O(m * n) for the call stack in the worst case.
>
> **Go lesson.** A closure that calls itself needs `var sink func(r, c int)` first and the assignment second. The cells of a `[][]byte` grid are characters, so compare with `'1'` and not with `1`.

> [!example]- Step 3: the Go solution
> ```go
> // numIslands solves LC 200. Time O(m * n), space O(m * n) for the
> // recursion.
> // The function changes the grid: each land cell that it counts
> // becomes
> // water.
> func numIslands(grid [][]byte) int {
>     rows, cols := len(grid), len(grid[0])
>     // down, up, right, left
>     dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
>
>     // declare first, so the closure can call itself
>     var sink func(r, c int)
>     sink = func(r, c int) {
>         // BOUNDS: outside the grid
>         if r < 0 || r >= rows || c < 0 || c >= cols {
>             return
>         }
>         // CHECK: water, or land that is already sunk
>         if grid[r][c] != '1' {
>             return
>         }
>         // MARK before the calls, or two cells call each other
>         // forever
>         grid[r][c] = '0'
>         for _, d := range dirs { // SPREAD to the four neighbours
>             sink(r+d[0], c+d[1])
>         }
>     }
>
>     count := 0
>     for r := 0; r < rows; r++ {
>         for c := 0; c < cols; c++ {
>             // START: land that no DFS reached is a new island
>             if grid[r][c] == '1' {
>                 count++
>                 sink(r, c)
>             }
>         }
>     }
>     return count
> }
> ```

### 133. Clone Graph

[LeetCode 133](https://leetcode.com/problems/clone-graph/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DFS with a clone map
> - **Template:** [[#Template C: Clone with a map|C: Clone with a map]]

> [!tip]- Step 2: the idea
> **Idea.** Keep a map from each old node to its copy. The DFS makes the copy the first time it sees a node, and it reads the map each later time. So a cycle does not make a second copy.
>
> **Complexity.** Time O(V + E) for V nodes and E edges, space O(V).
>
> **Go lesson.** A pointer is a valid map key. `map[*Node]*Node` compares addresses, so two nodes with the same `Val` are two keys.

> [!example]- Step 3: the Go solution
> ```go
> // cloneGraph solves LC 133. Time O(V + E), space O(V).
> // The map is the visited set, and it also holds the copy of each
> // node.
> func cloneGraph(node *Node) *Node {
>     clones := make(map[*Node]*Node) // old node -> its copy
>
>     var clone func(old *Node) *Node
>     clone = func(old *Node) *Node {
>         if old == nil { // an empty graph
>             return nil
>         }
>         // CHECK: this node already has a copy
>         if c, ok := clones[old]; ok {
>             return c
>         }
>         // Copy the value now. The neighbours come next, so make an
>         // empty
>         // slice for them.
>         c := &Node{Val: old.Val, Neighbors: make([]*Node, 0, len(old.Neighbors))}
>         // STORE before the calls, so a cycle finds the copy
>         clones[old] = c
>         for _, nb := range old.Neighbors {
>             // LINK the copy of each neighbour
>             c.Neighbors = append(c.Neighbors, clone(nb))
>         }
>         return c
>     }
>     return clone(node)
> }
> ```

### 695. Max Area of Island

[LeetCode 695](https://leetcode.com/problems/max-area-of-island/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Grid DFS (flood fill)
> - **Template:** [[#Template A: Grid DFS (flood fill)|A: Grid DFS (flood fill)]]

> [!tip]- Step 2: the idea
> **Idea.** The DFS of an island returns its area: 1 for the cell plus the areas that the four neighbours return. Keep the largest area.
>
> **Complexity.** Time O(m * n) for m rows and n columns, space O(m * n) for the call stack in the worst case.
>
> **Go lesson.** A recursive closure can return a value. Declare its full type first: `var area func(r, c int) int`.

> [!example]- Step 3: the Go solution
> ```go
> // maxAreaOfIsland solves LC 695. Time O(m * n), space O(m * n) for
> // the
> // recursion.
> // The function changes the grid: each land cell that it counts
> // becomes
> // water.
> func maxAreaOfIsland(grid [][]int) int {
>     rows, cols := len(grid), len(grid[0])
>     // down, up, right, left
>     dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
>
>     // returns the area of the island part that starts here
>     var area func(r, c int) int
>     area = func(r, c int) int {
>         if r < 0 || r >= rows || c < 0 || c >= cols { // BOUNDS
>             return 0
>         }
>         // CHECK: water, or land that is already counted
>         if grid[r][c] != 1 {
>             return 0
>         }
>         grid[r][c] = 0 // MARK, so no cell is counted two times
>         total := 1     // this cell
>         // SPREAD, and add what each neighbour finds
>         for _, d := range dirs {
>             total += area(r+d[0], c+d[1])
>         }
>         return total
>     }
>
>     best := 0
>     for r := 0; r < rows; r++ {
>         for c := 0; c < cols; c++ {
>             if grid[r][c] == 1 { // START a new island
>                 best = max(best, area(r, c))
>             }
>         }
>     }
>     return best
> }
> ```

### 417. Pacific Atlantic Water Flow

[LeetCode 417](https://leetcode.com/problems/pacific-atlantic-water-flow/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DFS from the borders
> - **Template:** [[#Template A: Grid DFS (flood fill)|A: Grid DFS (flood fill)]]

> [!tip]- Step 2: the idea
> **Idea.** Do not follow the water down from each cell. Start at each ocean border and climb to cells that are equal or higher. A cell that the two searches mark can reach the two oceans.
>
> **Complexity.** Time O(m * n) for m rows and n columns, space O(m * n).
>
> **Go lesson.** `make([][]bool, rows)` gives `rows` nil slices, so make each row in a loop. A slice parameter such as `seen [][]bool` shares its data with the caller, so the closure can mark it.

> [!example]- Step 3: the Go solution
> ```go
> // pacificAtlantic solves LC 417. Time O(m * n), space O(m * n).
> // Water flows down to an ocean. The search goes the opposite way:
> // it starts at the border of each ocean and climbs up.
> func pacificAtlantic(heights [][]int) [][]int {
>     rows, cols := len(heights), len(heights[0])
>     dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
>
>     // pacific[r][c]: the cell can reach the Pacific
>     pacific := make([][]bool, rows)
>     // atlantic[r][c]: the cell can reach the Atlantic
>     atlantic := make([][]bool, rows)
>     for r := 0; r < rows; r++ {
>         // each row needs its own make
>         pacific[r] = make([]bool, cols)
>         atlantic[r] = make([]bool, cols)
>     }
>
>     // seen is the grid of one ocean
>     var climb func(r, c int, seen [][]bool)
>     climb = func(r, c int, seen [][]bool) {
>         seen[r][c] = true        // MARK
>         for _, d := range dirs { // SPREAD
>             nr, nc := r+d[0], c+d[1]
>             // BOUNDS
>             if nr < 0 || nr >= rows || nc < 0 || nc >= cols {
>                 continue
>             }
>             // CHECK: done, or lower
>             if seen[nr][nc] || heights[nr][nc] < heights[r][c] {
>                 // water cannot flow from a lower cell to this cell
>                 continue
>             }
>             climb(nr, nc, seen)
>         }
>     }
>
>     for r := 0; r < rows; r++ { // START at the border cells
>         climb(r, 0, pacific)       // left border
>         climb(r, cols-1, atlantic) // right border
>     }
>     for c := 0; c < cols; c++ {
>         climb(0, c, pacific)       // top border
>         climb(rows-1, c, atlantic) // bottom border
>     }
>
>     res := [][]int{}
>     for r := 0; r < rows; r++ {
>         for c := 0; c < cols; c++ {
>             // the two searches reached this cell
>             if pacific[r][c] && atlantic[r][c] {
>                 res = append(res, []int{r, c})
>             }
>         }
>     }
>     return res
> }
> ```

### 130. Surrounded Regions

[LeetCode 130](https://leetcode.com/problems/surrounded-regions/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DFS from the borders
> - **Template:** [[#Template A: Grid DFS (flood fill)|A: Grid DFS (flood fill)]]

> [!tip]- Step 2: the idea
> **Idea.** An 'O' region is safe only if it touches the border. So mark each 'O' that a DFS from the border reaches. Then each 'O' without a mark is surrounded, and you change it to 'X'.
>
> **Complexity.** Time O(m * n) for m rows and n columns, space O(m * n) for the call stack in the worst case.
>
> **Go lesson.** The function returns nothing: a slice holds a pointer to its data, so the writes to `board[r][c]` change the board of the caller. A `switch` needs no `break`, because a Go `case` does not fall through.

> [!example]- Step 3: the Go solution
> ```go
> // solve solves LC 130. Time O(m * n), space O(m * n) for the
> // recursion.
> // It changes the board in place: each 'O' region that does not
> // touch the
> // border becomes 'X'.
> func solve(board [][]byte) {
>     rows, cols := len(board), len(board[0])
>     dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
>
>     // marks the 'O' region that contains (r, c) as safe
>     var keep func(r, c int)
>     keep = func(r, c int) {
>         if r < 0 || r >= rows || c < 0 || c >= cols { // BOUNDS
>             return
>         }
>         // CHECK: an 'X', or a cell that is already safe
>         if board[r][c] != 'O' {
>             return
>         }
>         // MARK: '#' means "an O that touches the border"
>         board[r][c] = '#'
>         for _, d := range dirs { // SPREAD
>             keep(r+d[0], c+d[1])
>         }
>     }
>
>     // START at the border cells, not at each cell
>     for r := 0; r < rows; r++ {
>         keep(r, 0)
>         keep(r, cols-1)
>     }
>     for c := 0; c < cols; c++ {
>         keep(0, c)
>         keep(rows-1, c)
>     }
>
>     for r := 0; r < rows; r++ {
>         for c := 0; c < cols; c++ {
>             switch board[r][c] {
>             case 'O': // no DFS reached it, so it is surrounded
>                 board[r][c] = 'X'
>             case '#': // safe: put the 'O' back
>                 board[r][c] = 'O'
>             }
>         }
>     }
> }
> ```

### 994. Rotting Oranges

[LeetCode 994](https://leetcode.com/problems/rotting-oranges/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Multi-source BFS by level
> - **Template:** [[#Template B: BFS by level from many sources|B: BFS by level from many sources]]

> [!tip]- Step 2: the idea
> **Idea.** All the rotten oranges start at the same time, so put all of them in the queue first. Each BFS level is one minute. Count the fresh oranges, and if some stay fresh at the end, the answer is -1.
>
> **Complexity.** Time O(m * n) for m rows and n columns, space O(m * n) for the queue.
>
> **Go lesson.** Go has no queue type, so a slice is the queue: `append` pushes at the end, and `q[0]` with `q = q[1:]` pops from the front. A `[2]int` array holds a cell with no extra type.

> [!example]- Step 3: the Go solution
> ```go
> // orangesRotting solves LC 994. Time O(m * n), space O(m * n).
> // One BFS starts from all the rotten oranges together. One level is
> // one
> // minute.
> func orangesRotting(grid [][]int) int {
>     rows, cols := len(grid), len(grid[0])
>     dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
>
>     queue := [][2]int{} // a cell is a [2]int: row, column
>     fresh := 0
>     for r := 0; r < rows; r++ {
>         for c := 0; c < cols; c++ {
>             switch grid[r][c] {
>             case 2:
>                 // SEED: each rotten orange is a source
>                 queue = append(queue, [2]int{r, c})
>             case 1:
>                 fresh++
>             }
>         }
>     }
>
>     minutes := 0
>     // stop when no fresh orange is left
>     for len(queue) > 0 && fresh > 0 {
>         minutes++
>         // LEVEL: only the cells in the queue now
>         for n := len(queue); n > 0; n-- {
>             cell := queue[0]
>             queue = queue[1:] // POP from the front
>             for _, d := range dirs {
>                 r, c := cell[0]+d[0], cell[1]+d[1]
>                 if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != 1 {
>                     continue // outside, empty, or already rotten
>                 }
>                 // MARK when you push, so a cell enters the queue
>                 // one time
>                 grid[r][c] = 2
>                 fresh--
>                 // PUSH: it spreads in the next minute
>                 queue = append(queue, [2]int{r, c})
>             }
>         }
>     }
>
>     if fresh > 0 { // an orange that no rotten orange can reach
>         return -1
>     }
>     return minutes
> }
> ```

### 286. Walls and Gates

[LeetCode 286](https://leetcode.com/problems/walls-and-gates/) (premium) · [free on NeetCode](https://neetcode.io/problems/islands-and-treasure) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Multi-source BFS by level
> - **Template:** [[#Template B: BFS by level from many sources|B: BFS by level from many sources]]

> [!tip]- Step 2: the idea
> **Idea.** Do not search from each room. Start one BFS from all the gates together. The first time the BFS reaches a room, the distance is the shortest, because BFS visits the cells in order of distance.
>
> **Complexity.** Time O(m * n) for m rows and n columns, space O(m * n) for the queue.
>
> **Go lesson.** The value `2147483647` is `math.MaxInt32`. A constant in Go has no fixed type until you use it, so `const inf = math.MaxInt32` compares with an `int` cell without a conversion.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `math`
>
> ```go
> // wallsAndGates solves LC 286. Time O(m * n), space O(m * n).
> // It fills each empty room with the distance to its nearest gate,
> // in place.
> func wallsAndGates(rooms [][]int) {
>     const inf = math.MaxInt32 // 2147483647 marks an empty room
>     rows, cols := len(rooms), len(rooms[0])
>     dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
>
>     queue := [][2]int{} // a cell is a [2]int: row, column
>     for r := 0; r < rows; r++ {
>         for c := 0; c < cols; c++ {
>             if rooms[r][c] == 0 {
>                 // SEED: each gate is a source
>                 queue = append(queue, [2]int{r, c})
>             }
>         }
>     }
>
>     // No level counter is necessary here: the value of the cell is
>     // its
>     // level.
>     for len(queue) > 0 {
>         cell := queue[0]
>         queue = queue[1:] // POP from the front
>         for _, d := range dirs {
>             r, c := cell[0]+d[0], cell[1]+d[1]
>             if r < 0 || r >= rows || c < 0 || c >= cols || rooms[r][c] != inf {
>                 // outside, a wall, a gate, or a room that already
>                 // has its
>                 // distance
>                 continue
>             }
>             // MARK: one step more than the cell before
>             rooms[r][c] = rooms[cell[0]][cell[1]] + 1
>             queue = append(queue, [2]int{r, c}) // PUSH
>         }
>     }
> }
> ```

### 207. Course Schedule

[LeetCode 207](https://leetcode.com/problems/course-schedule/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Topological sort (Kahn)
> - **Template:** [[#Template D: Topological sort|D: Topological sort]]

> [!tip]- Step 2: the idea
> **Idea.** Count the prerequisites of each course. Take each course that has a count of 0, and decrease the count of the courses that wait for it. If a cycle exists, its courses never get to 0, so you take fewer than all the courses.
>
> **Complexity.** Time O(V + E) for V courses and E prerequisites, space O(V + E).
>
> **Go lesson.** `make([][]int, n)` gives n nil slices, and `append` accepts a nil slice. So the adjacency list needs no second `make`.

> [!example]- Step 3: the Go solution
> ```go
> // canFinish solves LC 207. Time O(V + E), space O(V + E).
> // You can finish all the courses if the prerequisite graph has no
> // cycle.
> func canFinish(numCourses int, prerequisites [][]int) bool {
>     // adj[b] = the courses that wait for b
>     adj := make([][]int, numCourses)
>     // indegree[a] = the prerequisites that a still needs
>     indegree := make([]int, numCourses)
>     // BUILD: [a, b] means "b before a", the edge is b -> a
>     for _, p := range prerequisites {
>         course, pre := p[0], p[1]
>         adj[pre] = append(adj[pre], course)
>         indegree[course]++
>     }
>
>     queue := []int{}
>     for c := 0; c < numCourses; c++ {
>         // SEED: the courses with no prerequisite
>         if indegree[c] == 0 {
>             queue = append(queue, c)
>         }
>     }
>
>     taken := 0
>     for len(queue) > 0 {
>         c := queue[0]
>         queue = queue[1:]
>         taken++ // TAKE the course
>         for _, next := range adj[c] {
>             // RELEASE: next needs one prerequisite less
>             indegree[next]--
>             if indegree[next] == 0 {
>                 queue = append(queue, next)
>             }
>         }
>     }
>     // CYCLE CHECK: the courses in a cycle are never taken
>     return taken == numCourses
> }
> ```

### 210. Course Schedule II

[LeetCode 210](https://leetcode.com/problems/course-schedule-ii/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Topological sort (Kahn)
> - **Template:** [[#Template D: Topological sort|D: Topological sort]]

> [!tip]- Step 2: the idea
> **Idea.** This is Course Schedule with one change: record each course when you take it. The record is a valid order. If the record has fewer than all the courses, a cycle exists and the answer is empty.
>
> **Complexity.** Time O(V + E) for V courses and E prerequisites, space O(V + E).
>
> **Go lesson.** `make([]int, 0, n)` makes a slice with length 0 and capacity n, so `append` starts at index 0 and never copies. `[]int{}` is an empty slice that is not nil.

> [!example]- Step 3: the Go solution
> ```go
> // findOrder solves LC 210. Time O(V + E), space O(V + E).
> // It returns one valid order of the courses, or an empty slice if a
> // cycle
> // exists.
> func findOrder(numCourses int, prerequisites [][]int) []int {
>     // adj[b] = the courses that wait for b
>     adj := make([][]int, numCourses)
>     // indegree[a] = the prerequisites that a still needs
>     indegree := make([]int, numCourses)
>     // BUILD: [a, b] means "b before a", the edge is b -> a
>     for _, p := range prerequisites {
>         course, pre := p[0], p[1]
>         adj[pre] = append(adj[pre], course)
>         indegree[course]++
>     }
>
>     queue := []int{}
>     for c := 0; c < numCourses; c++ {
>         // SEED: the courses with no prerequisite
>         if indegree[c] == 0 {
>             queue = append(queue, c)
>         }
>     }
>
>     order := make([]int, 0, numCourses)
>     for len(queue) > 0 {
>         c := queue[0]
>         queue = queue[1:]
>         // TAKE the course: it goes next in the order
>         order = append(order, c)
>         for _, next := range adj[c] {
>             // RELEASE: next needs one prerequisite less
>             indegree[next]--
>             if indegree[next] == 0 {
>                 queue = append(queue, next)
>             }
>         }
>     }
>
>     // CYCLE CHECK: some courses never got to 0
>     if len(order) < numCourses {
>         return []int{}
>     }
>     return order
> }
> ```

### 684. Redundant Connection

[LeetCode 684](https://leetcode.com/problems/redundant-connection/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Union-find, cycle detection
> - **Template:** [[#Template E: Union-find|E: Union-find]]

> [!tip]- Step 2: the idea
> **Idea.** Add the edges one at a time. If the two ends of an edge are already in one group, a path between them exists, so this edge closes the cycle. It is also the last such edge in the input.
>
> **Complexity.** Time O(n * α(n)) for n edges, which is almost O(n), space O(n).
>
> **Go lesson.** A method with a pointer receiver, `func (u *unionFind) find`, can change the fields of the struct. The constructor returns `*unionFind`, so all the calls share one struct.

> [!example]- Step 3: the Go solution
> ```go
> // findRedundantConnection solves LC 684. Time O(n * α(n)), space
> // O(n).
> // The first edge that connects two nodes of one group is the
> // answer.
> func findRedundantConnection(edges [][]int) []int {
>     // the nodes are 1..n, so index 0 stays unused
>     uf := newUnionFind(len(edges) + 1)
>     for _, e := range edges {
>         // UNION fails: the two ends were connected already
>         if !uf.union(e[0], e[1]) {
>             return e
>         }
>     }
>     // the problem always has an answer, so this line does not run
>     return nil
> }
>
> // unionFind keeps one root for each group of connected nodes.
> type unionFind struct {
>     parent []int // parent[x] == x means that x is a root
>     size   []int // size[root] = the number of nodes in the group
> }
>
> func newUnionFind(n int) *unionFind {
>     u := &unionFind{parent: make([]int, n), size: make([]int, n)}
>     for i := 0; i < n; i++ {
>         u.parent[i] = i // each node starts as its own root
>         u.size[i] = 1
>     }
>     return u
> }
>
> // find returns the root of the group of x.
> func (u *unionFind) find(x int) int {
>     if u.parent[x] != x {
>         // PATH COMPRESSION: point x at the root
>         u.parent[x] = u.find(u.parent[x])
>     }
>     return u.parent[x]
> }
>
> // union joins the groups of a and b. It returns false if they were
> // one
> // group already.
> func (u *unionFind) union(a, b int) bool {
>     ra, rb := u.find(a), u.find(b) // always work on the roots
>     if ra == rb {
>         return false
>     }
>     if u.size[ra] < u.size[rb] {
>         ra, rb = rb, ra // UNION BY SIZE: ra is the larger group
>     }
>     // the smaller group goes below the larger group
>     u.parent[rb] = ra
>     u.size[ra] += u.size[rb]
>     return true
> }
> ```

### 323. Number of Connected Components in an Undirected Graph

[LeetCode 323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (premium) · [free on NeetCode](https://neetcode.io/problems/count-connected-components) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Union-find, count the groups
> - **Template:** [[#Template E: Union-find|E: Union-find]]

> [!tip]- Step 2: the idea
> **Idea.** Start with n groups, one for each node. Each edge that joins two different groups makes the count one less. An edge inside one group changes nothing.
>
> **Complexity.** Time O((n + e) * α(n)) for n nodes and e edges, which is almost O(n + e), space O(n).
>
> **Go lesson.** A method that returns `bool` goes directly in an `if`: `if uf.union(a, b) { ... }`. The condition has no parentheses in Go.

> [!example]- Step 3: the Go solution
> ```go
> // countComponents solves LC 323. Time O((n + e) * α(n)), space
> // O(n).
> // Each union that succeeds merges two groups, so the count goes
> // down by
> // one.
> func countComponents(n int, edges [][]int) int {
>     uf := newUnionFind(n)
>     count := n // each node is a group of one
>     for _, e := range edges {
>         if uf.union(e[0], e[1]) { // UNION: two groups became one
>             count--
>         }
>     }
>     return count
> }
>
> // unionFind keeps one root for each group of connected nodes.
> type unionFind struct {
>     parent []int // parent[x] == x means that x is a root
>     size   []int // size[root] = the number of nodes in the group
> }
>
> func newUnionFind(n int) *unionFind {
>     u := &unionFind{parent: make([]int, n), size: make([]int, n)}
>     for i := 0; i < n; i++ {
>         u.parent[i] = i // each node starts as its own root
>         u.size[i] = 1
>     }
>     return u
> }
>
> // find returns the root of the group of x.
> func (u *unionFind) find(x int) int {
>     if u.parent[x] != x {
>         // PATH COMPRESSION: point x at the root
>         u.parent[x] = u.find(u.parent[x])
>     }
>     return u.parent[x]
> }
>
> // union joins the groups of a and b. It returns false if they were
> // one
> // group already.
> func (u *unionFind) union(a, b int) bool {
>     ra, rb := u.find(a), u.find(b) // always work on the roots
>     if ra == rb {
>         return false
>     }
>     if u.size[ra] < u.size[rb] {
>         ra, rb = rb, ra // UNION BY SIZE: ra is the larger group
>     }
>     // the smaller group goes below the larger group
>     u.parent[rb] = ra
>     u.size[ra] += u.size[rb]
>     return true
> }
> ```

### 261. Graph Valid Tree

[LeetCode 261](https://leetcode.com/problems/graph-valid-tree/) (premium) · [free on NeetCode](https://neetcode.io/problems/valid-tree) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Union-find, cycle detection
> - **Template:** [[#Template E: Union-find|E: Union-find]]

> [!tip]- Step 2: the idea
> **Idea.** A tree with n nodes has exactly n - 1 edges and no cycle. Check the edge count first. Then add the edges to a union-find: if an edge connects two nodes of one group, it closes a cycle.
>
> **Complexity.** Time O(n * α(n)) for n nodes, which is almost O(n), space O(n).
>
> **Go lesson.** Return early for the simple case. `len(edges) != n-1` costs O(1), and it removes the connectivity check: n - 1 edges with no cycle always connect all the nodes.

> [!example]- Step 3: the Go solution
> ```go
> // validTree solves LC 261. Time O(n * α(n)), space O(n).
> // A graph is a tree if it has n - 1 edges and no cycle. Then it is
> // also
> // connected.
> func validTree(n int, edges [][]int) bool {
>     // too few edges: not connected. Too many: a cycle
>     if len(edges) != n-1 {
>         return false
>     }
>     uf := newUnionFind(n)
>     for _, e := range edges {
>         // UNION fails: this edge closes a cycle
>         if !uf.union(e[0], e[1]) {
>             return false
>         }
>     }
>     return true
> }
>
> // unionFind keeps one root for each group of connected nodes.
> type unionFind struct {
>     parent []int // parent[x] == x means that x is a root
>     size   []int // size[root] = the number of nodes in the group
> }
>
> func newUnionFind(n int) *unionFind {
>     u := &unionFind{parent: make([]int, n), size: make([]int, n)}
>     for i := 0; i < n; i++ {
>         u.parent[i] = i // each node starts as its own root
>         u.size[i] = 1
>     }
>     return u
> }
>
> // find returns the root of the group of x.
> func (u *unionFind) find(x int) int {
>     if u.parent[x] != x {
>         // PATH COMPRESSION: point x at the root
>         u.parent[x] = u.find(u.parent[x])
>     }
>     return u.parent[x]
> }
>
> // union joins the groups of a and b. It returns false if they were
> // one
> // group already.
> func (u *unionFind) union(a, b int) bool {
>     ra, rb := u.find(a), u.find(b) // always work on the roots
>     if ra == rb {
>         return false
>     }
>     if u.size[ra] < u.size[rb] {
>         ra, rb = rb, ra // UNION BY SIZE: ra is the larger group
>     }
>     // the smaller group goes below the larger group
>     u.parent[rb] = ra
>     u.size[ra] += u.size[rb]
>     return true
> }
> ```

### 127. Word Ladder

[LeetCode 127](https://leetcode.com/problems/word-ladder/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** BFS on an implicit graph
> - **Template:** [[#Template F: BFS on an implicit graph|F: BFS on an implicit graph]]

> [!tip]- Step 2: the idea
> **Idea.** Each word is a node, and two words that differ by one letter have an edge. BFS from the first word gives the shortest chain. To find the neighbours of a word, change each letter to 'a'..'z' and keep the results that are in the word set.
>
> **Complexity.** Time O(n * L²) for n words of length L (26 * L candidates for each word, O(L) to build each one), space O(n * L).
>
> **Go lesson.** A string is immutable, so convert it with `[]byte(word)`, change one byte, and convert back with `string(buf)`. The conversion makes a copy, so the map key is safe.

> [!example]- Step 3: the Go solution
> ```go
> // ladderLength solves LC 127. Time O(n * L²), space O(n * L).
> // It returns the number of words in the shortest chain, or 0 if no
> // chain
> // exists.
> func ladderLength(beginWord string, endWord string, wordList []string) int {
>     // the words that BFS did not use yet
>     words := make(map[string]bool, len(wordList))
>     for _, w := range wordList {
>         words[w] = true
>     }
>     if !words[endWord] { // the last word must be in the list
>         return 0
>     }
>
>     queue := []string{beginWord}
>     // deleting a key that is not there is safe
>     delete(words, beginWord)
>     for length := 1; len(queue) > 0; length++ {
>         // one level = one more word in the chain
>         for n := len(queue); n > 0; n-- {
>             word := queue[0]
>             queue = queue[1:]
>             // GOAL: the first time that BFS sees it is the shortest
>             if word == endWord {
>                 return length
>             }
>             buf := []byte(word) // a copy that we can change
>             // GENERATE: change one letter at a time
>             for i := 0; i < len(buf); i++ {
>                 old := buf[i]
>                 for ch := byte('a'); ch <= 'z'; ch++ {
>                     buf[i] = ch
>                     next := string(buf)
>                     // a real word that BFS did not use
>                     if words[next] {
>                         delete(words, next) // MARK when you push
>                         queue = append(queue, next)
>                     }
>                 }
>                 // put the letter back before the next position
>                 buf[i] = old
>             }
>         }
>     }
>     return 0 // the queue is empty: no chain
> }
> ```

---

[[wiki/neetcode-150/10-backtracking|← Backtracking]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/12-advanced-graphs|Advanced Graphs →]]
