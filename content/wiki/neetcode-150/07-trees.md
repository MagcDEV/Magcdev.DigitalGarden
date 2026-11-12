---
title: "NeetCode 150, stage 7: Trees"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - trees
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 7: Trees

[[wiki/neetcode-150/06-linked-list|← Linked List]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/08-tries|Tries →]]

A tree problem is a small question that each node answers for its own subtree. This stage trains recursion: a base case, one call for each child, and one line that combines the answers. It also trains closures, which let a recursive function in Go keep a result outside its return value.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 7: Recursion and closures with trees|the Go syntax for this stage]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/07-trees#226. Invert Binary Tree\|226. Invert Binary Tree]] | Easy | Recursive DFS, swap the children | [[wiki/neetcode-150/07-trees#Template A: DFS that returns a value\|A: DFS that returns a value]] |
| 2 | [[wiki/neetcode-150/07-trees#104. Maximum Depth of Binary Tree\|104. Maximum Depth of Binary Tree]] | Easy | Recursive DFS that returns the height | [[wiki/neetcode-150/07-trees#Template A: DFS that returns a value\|A: DFS that returns a value]] |
| 3 | [[wiki/neetcode-150/07-trees#543. Diameter of Binary Tree\|543. Diameter of Binary Tree]] | Easy | DFS returns the height, records the diameter | [[wiki/neetcode-150/07-trees#Template B: DFS that returns one value and records another\|B: DFS that returns one value and records another]] |
| 4 | [[wiki/neetcode-150/07-trees#110. Balanced Binary Tree\|110. Balanced Binary Tree]] | Easy | DFS returns the height, records the balance | [[wiki/neetcode-150/07-trees#Template B: DFS that returns one value and records another\|B: DFS that returns one value and records another]] |
| 5 | [[wiki/neetcode-150/07-trees#100. Same Tree\|100. Same Tree]] | Easy | Recursive DFS on two trees | [[wiki/neetcode-150/07-trees#Template A: DFS that returns a value\|A: DFS that returns a value]] |
| 6 | [[wiki/neetcode-150/07-trees#572. Subtree of Another Tree\|572. Subtree of Another Tree]] | Easy | DFS with a same-tree test | [[wiki/neetcode-150/07-trees#Template A: DFS that returns a value\|A: DFS that returns a value]] |
| 7 | [[wiki/neetcode-150/07-trees#235. Lowest Common Ancestor of a Binary Search Tree\|235. Lowest Common Ancestor of a Binary Search Tree]] | Medium | BST walk to the split point | [[wiki/neetcode-150/07-trees#Template E: BST walk that uses the order\|E: BST walk that uses the order]] |
| 8 | [[wiki/neetcode-150/07-trees#102. Binary Tree Level Order Traversal\|102. Binary Tree Level Order Traversal]] | Medium | BFS by level | [[wiki/neetcode-150/07-trees#Template D: BFS by level\|D: BFS by level]] |
| 9 | [[wiki/neetcode-150/07-trees#199. Binary Tree Right Side View\|199. Binary Tree Right Side View]] | Medium | BFS by level, keep the last node | [[wiki/neetcode-150/07-trees#Template D: BFS by level\|D: BFS by level]] |
| 10 | [[wiki/neetcode-150/07-trees#1448. Count Good Nodes in Binary Tree\|1448. Count Good Nodes in Binary Tree]] | Medium | DFS that passes the path maximum down | [[wiki/neetcode-150/07-trees#Template C: DFS that passes state down\|C: DFS that passes state down]] |
| 11 | [[wiki/neetcode-150/07-trees#98. Validate Binary Search Tree\|98. Validate Binary Search Tree]] | Medium | DFS that passes the limits down | [[wiki/neetcode-150/07-trees#Template C: DFS that passes state down\|C: DFS that passes state down]] |
| 12 | [[wiki/neetcode-150/07-trees#230. Kth Smallest Element in a BST\|230. Kth Smallest Element in a BST]] | Medium | Inorder walk of a BST with a stack | [[wiki/neetcode-150/07-trees#Template E: BST walk that uses the order\|E: BST walk that uses the order]] |
| 13 | [[wiki/neetcode-150/07-trees#105. Construct Binary Tree from Preorder and Inorder Traversal\|105. Construct Binary Tree from Preorder and Inorder Traversal]] | Medium | Preorder cursor plus inorder index map | [[wiki/neetcode-150/07-trees#Template F: Preorder build with a cursor\|F: Preorder build with a cursor]] |
| 14 | [[wiki/neetcode-150/07-trees#124. Binary Tree Maximum Path Sum\|124. Binary Tree Maximum Path Sum]] | Hard | DFS returns one branch, records the full path | [[wiki/neetcode-150/07-trees#Template B: DFS that returns one value and records another\|B: DFS that returns one value and records another]] |
| 15 | [[wiki/neetcode-150/07-trees#297. Serialize and Deserialize Binary Tree\|297. Serialize and Deserialize Binary Tree]] | Hard | Preorder DFS with null markers | [[wiki/neetcode-150/07-trees#Template F: Preorder build with a cursor\|F: Preorder build with a cursor]] |

## Templates to memorize

### Template A: DFS that returns a value

> [!tip] Signal
> The answer for a tree comes from the answers for its two subtrees. For example: depth, "same tree", "invert", "is a subtree".

```go
// TEMPLATE A: DFS that returns a value. Each node answers for its own
// subtree.
func height(root *TreeNode) int {
    if root == nil { // 1. BASE CASE: an empty tree
        return 0
    }
    left := height(root.Left)   // 2. ASK the left subtree
    right := height(root.Right) // 3. ASK the right subtree
    return 1 + max(left, right) // 4. COMBINE the two answers with this node
}
```

The moves are BASE CASE, ASK LEFT, ASK RIGHT, COMBINE. Trust the recursive call: assume that it gives the correct answer for a subtree, and write only the combine step. Write the `nil` test first, or the code panics on an empty child.

> [!quote] Say it
> "I solve it bottom-up. Each node asks its two children and combines their answers, so every node is visited once. That is O(n) time and O(h) space for the call stack."

### Template B: DFS that returns one value and records another

> [!tip] Signal
> The answer can be anywhere in the tree, not only at the root: diameter, maximum path sum, "balanced at each node". The value that a parent needs is different from the answer.

```go
// TEMPLATE B: DFS that returns one value and records another.
// The return value goes to the parent. The closure variable keeps the best
// answer.
func longestPath(root *TreeNode) int {
    // the closure below can read and write best
    best := 0
    // declare first, so the function can call itself
    var dfs func(node *TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return 0
        }
        left := dfs(node.Left)   // ASK
        right := dfs(node.Right) // ASK
        // RECORD: the path that turns at this node
        best = max(best, left+right)
        // RETURN: only one side continues to the parent
        return 1 + max(left, right)
    }
    dfs(root)
    return best
}
```

The moves are ASK LEFT, ASK RIGHT, RECORD, RETURN. The recorded value uses the two sides. The returned value uses only one side, because a path cannot go down two branches and also up to the parent. Declare the function variable with `var` before you assign it, or the closure cannot call itself.

> [!quote] Say it
> "The helper returns the height, which is what the parent needs. On the way up it updates the best answer in a variable outside. One pass, O(n)."

### Template C: DFS that passes state down

> [!tip] Signal
> A node cannot decide alone. It needs a fact from its ancestors: the limits for a BST, the largest value on the path, the sum from the root.

```go
// TEMPLATE C: DFS that passes state down. The parameter carries what the
// ancestors know.
// Here the state is the sum that is necessary below this node.
func hasPathSum(node *TreeNode, remaining int) bool {
    if node == nil { // BASE CASE
        return false
    }
    // UPDATE the state with this node
    remaining -= node.Val
    // USE the state: a leaf decides
    if node.Left == nil && node.Right == nil {
        return remaining == 0
    }
    // PASS DOWN: each child gets its own copy of the state.
    return hasPathSum(node.Left, remaining) || hasPathSum(node.Right, remaining)
}
```

The moves are BASE CASE, UPDATE or USE the state, PASS DOWN. The state is a parameter, and Go copies a parameter for each call. So a change for the left child does not reach the right child.

> [!quote] Say it
> "I pass what the ancestors know down as a parameter, so each node decides in O(1). The total is O(n)."

### Template D: BFS by level

> [!tip] Signal
> The problem says level, row, "depth by depth", "right side view" or the minimum number of steps.

```go
// TEMPLATE D: BFS by level. One turn of the outer loop is one level of the
// tree.
func levels(root *TreeNode) [][]int {
    var res [][]int
    if root == nil {
        return res
    }
    queue := []*TreeNode{root}
    for len(queue) > 0 {
        size := len(queue) // 1. FREEZE: these nodes are exactly one level
        level := make([]int, 0, size)
        for i := 0; i < size; i++ {
            node := queue[0] // 2. POP from the front
            queue = queue[1:]
            level = append(level, node.Val)
            if node.Left != nil { // 3. PUSH the children: the next level
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        res = append(res, level)
    }
    return res
}
```

The moves are FREEZE the size of the queue, POP that number of nodes, PUSH their children. The frozen size is the number of nodes in the current level. Do not read `len(queue)` in the condition of the inner loop, because the queue grows inside that loop.

> [!quote] Say it
> "I use a queue and process one level per loop. I read the queue size first, and that many nodes are exactly one level. It is O(n) time, and the queue holds at most one level."

### Template E: BST walk that uses the order

> [!tip] Signal
> The tree is a binary search tree. The problem asks for a search, a lowest common ancestor, or the kth value in sorted order.

```go
// TEMPLATE E: use the order of a BST: left subtree < node < right subtree.
// Tool 1: one comparison at each node chooses one side. Time O(h).
func search(root *TreeNode, target int) *TreeNode {
    node := root
    for node != nil && node.Val != target {
        if target < node.Val { // COMPARE, then GO to one side only
            node = node.Left
        } else {
            node = node.Right
        }
    }
    return node
}

// Tool 2: inorder (left, node, right) visits the values in sorted order.
func sortedValues(root *TreeNode) []int {
    var res []int
    stack := []*TreeNode{} // the nodes that wait for their visit
    node := root
    for node != nil || len(stack) > 0 {
        for node != nil { // 1. GO LEFT as far as possible
            stack = append(stack, node)
            node = node.Left
        }
        // 2. POP and VISIT: the smallest value that waits
        node = stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        res = append(res, node.Val)
        node = node.Right // 3. GO RIGHT one step
    }
    return res
}
```

A BST gives two tools. One comparison at each node chooses one side, so a search costs O(h). An inorder walk visits the values in sorted order, so the kth node that you visit is the kth smallest. The moves of the inorder walk are GO LEFT, POP and VISIT, GO RIGHT.

> [!quote] Say it
> "Because it is a BST, I compare with the node and go to one side only, so it is O(h). When I need sorted order, I do an inorder walk."

### Template F: Preorder build with a cursor

> [!tip] Signal
> The problem asks you to build a tree from a sequence. The sequence is a preorder walk plus an inorder walk, or a string that your own code wrote.

```go
// TEMPLATE F: build a tree from a preorder sequence with a cursor.
// "N" marks an empty child: "1,2,N,N,3,N,N" is the root 1 with the children
// 2 and 3.
func fromPreorder(tokens []string) *TreeNode {
    // CURSOR: the index of the next token. All the calls share it.
    next := 0
    var build func() *TreeNode
    build = func() *TreeNode {
        tok := tokens[next] // READ one token and move the cursor
        next++
        if tok == "N" { // EMPTY: this subtree has no nodes
            return nil
        }
        val, _ := strconv.Atoi(tok)
        node := &TreeNode{Val: val} // the ROOT comes first in preorder
        node.Left = build()         // then the full LEFT subtree
        node.Right = build()        // then the full RIGHT subtree
        return node
    }
    return build()
}
```

The moves are READ the root at the cursor, test for EMPTY, build LEFT, build RIGHT. All the calls share one cursor, and each call reads exactly the tokens of its subtree. Build the left subtree before the right subtree, because preorder gives it first.

> [!quote] Say it
> "Preorder gives me the root first. I keep one index into the sequence, read the root, then build the left subtree and the right subtree recursively. Each node costs O(1)."

> [!warning] Mistakes in this stage
> - A closure that calls itself needs `var dfs func(*TreeNode) int` first, then `dfs = func...`. With `dfs := func...`, the name does not exist in the body.
> - `node.Left.Val` panics when `node.Left` is `nil`. Test for `nil` at the top of the function.
> - `i < len(queue)` in the inner loop of a BFS mixes two levels. Save `size := len(queue)` first.
> - A BST test that compares a node only with its two children is wrong. Each node must be inside the limits from all its ancestors.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 226. Invert Binary Tree

[LeetCode 226](https://leetcode.com/problems/invert-binary-tree/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Recursive DFS, swap the children
> - **Template:** [[#Template A: DFS that returns a value|A: DFS that returns a value]]

> [!tip]- Step 2: the idea
> **Idea.** To invert a tree, invert its left subtree, invert its right subtree, and swap the two. An empty tree is already inverted.
>
> **Complexity.** Time O(n), space O(h) for a tree of height h.
>
> **Go lesson.** `a, b = b, a` swaps two values with no temporary variable. Go computes the right side fully before it assigns.

> [!example]- Step 3: the Go solution
> ```go
> // invertTree solves LC 226. Time O(n), space O(h) for the call
> // stack.
> func invertTree(root *TreeNode) *TreeNode {
>     if root == nil { // BASE CASE: an empty tree
>         return nil
>     }
>     // ASK: the left subtree, inverted
>     left := invertTree(root.Left)
>     // ASK: the right subtree, inverted
>     right := invertTree(root.Right)
>     // COMBINE: swap the two children
>     root.Left, root.Right = right, left
>     return root
> }
> ```

### 104. Maximum Depth of Binary Tree

[LeetCode 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Recursive DFS that returns the height
> - **Template:** [[#Template A: DFS that returns a value|A: DFS that returns a value]]

> [!tip]- Step 2: the idea
> **Idea.** The depth of a tree is 1 for the root plus the depth of its deeper subtree. An empty tree has depth 0.
>
> **Complexity.** Time O(n), space O(h) for a tree of height h.
>
> **Go lesson.** `max` is a built-in function since Go 1.21. A recursive function in Go needs no special keyword.

> [!example]- Step 3: the Go solution
> ```go
> // maxDepth solves LC 104. Time O(n), space O(h) for the call stack.
> func maxDepth(root *TreeNode) int {
>     if root == nil { // BASE CASE: an empty tree has depth 0
>         return 0
>     }
>     left := maxDepth(root.Left)   // ASK the left subtree
>     right := maxDepth(root.Right) // ASK the right subtree
>     // COMBINE: this node plus the deeper side
>     return 1 + max(left, right)
> }
> ```

### 543. Diameter of Binary Tree

[LeetCode 543](https://leetcode.com/problems/diameter-of-binary-tree/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DFS returns the height, records the diameter
> - **Template:** [[#Template B: DFS that returns one value and records another|B: DFS that returns one value and records another]]

> [!tip]- Step 2: the idea
> **Idea.** The longest path that turns at a node has length left height plus right height. Calculate the height of each node one time, and record the best sum on the way.
>
> **Complexity.** Time O(n), space O(h) for a tree of height h.
>
> **Go lesson.** A closure can read and change a variable of the function around it. A closure that calls itself needs `var dfs func(...)` before the assignment.

> [!example]- Step 3: the Go solution
> ```go
> // diameterOfBinaryTree solves LC 543. Time O(n), space O(h).
> // The diameter is a number of edges. The longest path does not
> // always
> // include the root.
> func diameterOfBinaryTree(root *TreeNode) int {
>     best := 0 // the longest path so far, in edges
>
>     // height returns the number of nodes on the longest path down
>     // from
>     // node.
>     // declare first: the body uses the name
>     var height func(node *TreeNode) int
>     height = func(node *TreeNode) int {
>         if node == nil { // BASE CASE
>             return 0
>         }
>         left := height(node.Left)   // ASK
>         right := height(node.Right) // ASK
>         // RECORD: left edges + right edges through this node
>         best = max(best, left+right)
>         // RETURN: the parent can use only one side
>         return 1 + max(left, right)
>     }
>     height(root)
>     return best
> }
> ```

### 110. Balanced Binary Tree

[LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DFS returns the height, records the balance
> - **Template:** [[#Template B: DFS that returns one value and records another|B: DFS that returns one value and records another]]

> [!tip]- Step 2: the idea
> **Idea.** A tree is balanced when, at each node, the two heights differ by 1 at most. Calculate each height one time from the bottom, and record a failure when you see one.
>
> **Complexity.** Time O(n), space O(h) for a tree of height h.
>
> **Go lesson.** A `bool` variable outside the closure keeps the result, so the closure can return the height only. A function that returns two values, `(int, bool)`, is the other usual form.

> [!example]- Step 3: the Go solution
> ```go
> // isBalanced solves LC 110. Time O(n), space O(h).
> // A height function that starts again at each node is O(n²). This
> // one
> // visits each node one time.
> func isBalanced(root *TreeNode) bool {
>     balanced := true // becomes false when one node is not balanced
>
>     var height func(node *TreeNode) int
>     height = func(node *TreeNode) int {
>         // BASE CASE. Also stop early after a failure.
>         if node == nil || !balanced {
>             return 0
>         }
>         left := height(node.Left)   // ASK
>         right := height(node.Right) // ASK
>         // RECORD: the heights differ by 2 or more
>         if left-right > 1 || right-left > 1 {
>             balanced = false
>         }
>         // RETURN the height to the parent
>         return 1 + max(left, right)
>     }
>     height(root)
>     return balanced
> }
> ```

### 100. Same Tree

[LeetCode 100](https://leetcode.com/problems/same-tree/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Recursive DFS on two trees
> - **Template:** [[#Template A: DFS that returns a value|A: DFS that returns a value]]

> [!tip]- Step 2: the idea
> **Idea.** Two trees are the same when the roots are equal, the left subtrees are the same and the right subtrees are the same. Go down the two trees together.
>
> **Complexity.** Time O(n), space O(h) for a tree of height h.
>
> **Go lesson.** `&&` stops at the first false value. So the second recursive call does not run when the left subtrees are different.

> [!example]- Step 3: the Go solution
> ```go
> // isSameTree solves LC 100. Time O(n), space O(h).
> func isSameTree(p *TreeNode, q *TreeNode) bool {
>     // BASE CASE 1: two empty trees are the same
>     if p == nil && q == nil {
>         return true
>     }
>     // BASE CASE 2: one is empty, or the values differ
>     if p == nil || q == nil || p.Val != q.Val {
>         return false
>     }
>     // ASK the two sides, and COMBINE the answers with &&.
>     return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
> }
> ```

### 572. Subtree of Another Tree

[LeetCode 572](https://leetcode.com/problems/subtree-of-another-tree/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DFS with a same-tree test
> - **Template:** [[#Template A: DFS that returns a value|A: DFS that returns a value]]

> [!tip]- Step 2: the idea
> **Idea.** The subtree can start at each node of the big tree. So visit each node, and at each one ask: is the tree from here the same as subRoot?
>
> **Complexity.** Time O(n * m) for n nodes in root and m nodes in subRoot, space O(h) for a tree of height h.
>
> **Go lesson.** `||` stops at the first true value. A helper function below the caller is fine in Go, because the order of the declarations in a file does not matter.

> [!example]- Step 3: the Go solution
> ```go
> // isSubtree solves LC 572. Time O(n * m), space O(h).
> // It is template A two times: one DFS visits each node, and one DFS
> // compares two trees.
> func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
>     if subRoot == nil { // an empty tree is a subtree of each tree
>         return true
>     }
>     // BASE CASE: no nodes are left, and subRoot is not empty
>     if root == nil {
>         return false
>     }
>     if sameTree(root, subRoot) { // the subtree starts at this node
>         return true
>     }
>     // ASK the two sides: the subtree can start lower in the tree.
>     return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
> }
>
> // sameTree is LC 100: the two trees have the same shape and the
> // same
> // values.
> func sameTree(p, q *TreeNode) bool {
>     if p == nil && q == nil {
>         return true
>     }
>     if p == nil || q == nil || p.Val != q.Val {
>         return false
>     }
>     return sameTree(p.Left, q.Left) && sameTree(p.Right, q.Right)
> }
> ```

### 235. Lowest Common Ancestor of a Binary Search Tree

[LeetCode 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** BST walk to the split point
> - **Template:** [[#Template E: BST walk that uses the order|E: BST walk that uses the order]]

> [!tip]- Step 2: the idea
> **Idea.** Start at the root. If p and q are both smaller than the node, go left. If both are larger, go right. The first node where they go to different sides, or where one of them is the node, is the answer.
>
> **Complexity.** Time O(h) for a tree of height h, space O(1).
>
> **Go lesson.** `func f(root, p, q *TreeNode)` gives one type to three parameters. A loop replaces the recursion, so the solution uses no call stack.

> [!example]- Step 3: the Go solution
> ```go
> // lowestCommonAncestor solves LC 235. Time O(h), space O(1).
> // It uses the order of the BST. It does not search the full tree.
> func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
>     node := root
>     for node != nil {
>         // COMPARE: p and q are in the left subtree
>         if p.Val < node.Val && q.Val < node.Val {
>             node = node.Left // GO left
>         } else if p.Val > node.Val && q.Val > node.Val {
>             // p and q are in the right subtree
>             node = node.Right // GO right
>         } else {
>             // SPLIT: p and q are on different sides, or node is p
>             // or q.
>             return node
>         }
>     }
>     return nil // not possible when p and q are in the tree
> }
> ```

### 102. Binary Tree Level Order Traversal

[LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** BFS by level
> - **Template:** [[#Template D: BFS by level|D: BFS by level]]

> [!tip]- Step 2: the idea
> **Idea.** A queue holds the nodes of one level. Read the size of the queue first. Then pop that number of nodes and push their children, which are the next level.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** A slice is the queue: `append` pushes to the back and `queue = queue[1:]` pops from the front. `[][]int` is a slice of slices.

> [!example]- Step 3: the Go solution
> ```go
> // levelOrder solves LC 102. Time O(n), space O(n).
> func levelOrder(root *TreeNode) [][]int {
>     var res [][]int // nil, and LeetCode shows a nil slice as []
>     if root == nil {
>         return res
>     }
>     queue := []*TreeNode{root} // the queue starts with level 0
>     for len(queue) > 0 {
>         // FREEZE: the queue holds exactly one level now
>         size := len(queue)
>         level := make([]int, 0, size) // length 0, capacity size
>         for i := 0; i < size; i++ {
>             node := queue[0] // POP from the front
>             queue = queue[1:]
>             level = append(level, node.Val)
>             // PUSH the children. Never push nil.
>             if node.Left != nil {
>                 queue = append(queue, node.Left)
>             }
>             if node.Right != nil {
>                 queue = append(queue, node.Right)
>             }
>         }
>         res = append(res, level)
>     }
>     return res
> }
> ```

### 199. Binary Tree Right Side View

[LeetCode 199](https://leetcode.com/problems/binary-tree-right-side-view/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** BFS by level, keep the last node
> - **Template:** [[#Template D: BFS by level|D: BFS by level]]

> [!tip]- Step 2: the idea
> **Idea.** From the right side you see the last node of each level. Do a BFS by level and keep the value of the last node that you pop in each level.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** The index `i` of the inner loop tells you the position in the level. `i == size-1` is the last node.

> [!example]- Step 3: the Go solution
> ```go
> // rightSideView solves LC 199. Time O(n), space O(n).
> // The node that you see is not always a right child: a left node
> // shows when
> // the level ends there.
> func rightSideView(root *TreeNode) []int {
>     var res []int
>     if root == nil {
>         return res
>     }
>     queue := []*TreeNode{root}
>     for len(queue) > 0 {
>         // FREEZE: the number of nodes in this level
>         size := len(queue)
>         for i := 0; i < size; i++ {
>             node := queue[0] // POP from the front
>             queue = queue[1:]
>             // the last node of the level is the one that you see
>             if i == size-1 {
>                 res = append(res, node.Val)
>             }
>             // PUSH the children, left before right
>             if node.Left != nil {
>                 queue = append(queue, node.Left)
>             }
>             if node.Right != nil {
>                 queue = append(queue, node.Right)
>             }
>         }
>     }
>     return res
> }
> ```

### 1448. Count Good Nodes in Binary Tree

[LeetCode 1448](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DFS that passes the path maximum down
> - **Template:** [[#Template C: DFS that passes state down|C: DFS that passes state down]]

> [!tip]- Step 2: the idea
> **Idea.** A node is good when no node above it on the path from the root has a larger value. So pass the largest value of the path down, and compare each node with it.
>
> **Complexity.** Time O(n), space O(h) for a tree of height h.
>
> **Go lesson.** Go passes an `int` parameter by value. Each call has its own copy of `maxAbove`, so a change for one child does not reach the other child.

> [!example]- Step 3: the Go solution
> ```go
> // goodNodes solves LC 1448. Time O(n), space O(h).
> func goodNodes(root *TreeNode) int {
>     if root == nil {
>         return 0
>     }
>     // the root has no node above it, so it is good
>     return countGood(root, root.Val)
> }
>
> // countGood counts the good nodes in the subtree of node.
> // maxAbove is the largest value on the path from the root to the
> // parent of
> // node.
> func countGood(node *TreeNode, maxAbove int) int {
>     if node == nil { // BASE CASE
>         return 0
>     }
>     count := 0
>     // USE the state: no node above is larger
>     if node.Val >= maxAbove {
>         count = 1
>         maxAbove = node.Val // UPDATE the state for the children
>     }
>     // PASS DOWN: each child gets a copy of maxAbove.
>     return count + countGood(node.Left, maxAbove) + countGood(node.Right, maxAbove)
> }
> ```

### 98. Validate Binary Search Tree

[LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DFS that passes the limits down
> - **Template:** [[#Template C: DFS that passes state down|C: DFS that passes state down]]

> [!tip]- Step 2: the idea
> **Idea.** Each node must be between two limits that come from its ancestors. A step to the left makes the node the new upper limit. A step to the right makes it the new lower limit.
>
> **Complexity.** Time O(n), space O(h) for a tree of height h.
>
> **Go lesson.** `int` has 64 bits on LeetCode, and a node value has 32 bits. So `math.MinInt64` and `math.MaxInt64` are safe start limits that no value can equal.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `math`
>
> ```go
> // isValidBST solves LC 98. Time O(n), space O(h).
> // A test of a node against its two children only is wrong: the
> // limits come
> // from all ancestors.
> func isValidBST(root *TreeNode) bool {
>     // the root has no limits
>     return inLimits(root, math.MinInt64, math.MaxInt64)
> }
>
> // inLimits is true when each value in the subtree is between low
> // and high,
> // not equal to them.
> func inLimits(node *TreeNode, low, high int) bool {
>     if node == nil { // BASE CASE: an empty tree is a valid BST
>         return true
>     }
>     // USE the state: equal values are not valid
>     if node.Val <= low || node.Val >= high {
>         return false
>     }
>     // PASS DOWN: the left side gets a new upper limit, the right
>     // side a new
>     // lower limit.
>     return inLimits(node.Left, low, node.Val) && inLimits(node.Right, node.Val, high)
> }
> ```

### 230. Kth Smallest Element in a BST

[LeetCode 230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Inorder walk of a BST with a stack
> - **Template:** [[#Template E: BST walk that uses the order|E: BST walk that uses the order]]

> [!tip]- Step 2: the idea
> **Idea.** An inorder walk of a BST visits the values from the smallest to the largest. So the k-th node that you visit is the answer, and the walk can stop there.
>
> **Complexity.** Time O(h + k) for a tree of height h, space O(h).
>
> **Go lesson.** A slice is the stack: `append` pushes, `s[len(s)-1]` reads the top, and `s = s[:len(s)-1]` pops.

> [!example]- Step 3: the Go solution
> ```go
> // kthSmallest solves LC 230. Time O(h + k), space O(h).
> // The loop with a stack can stop at the k-th node. It does not
> // visit the
> // rest of the tree.
> func kthSmallest(root *TreeNode, k int) int {
>     stack := []*TreeNode{} // the nodes that wait for their visit
>     node := root
>     for node != nil || len(stack) > 0 {
>         // GO LEFT as far as possible: smaller values come first
>         for node != nil {
>             stack = append(stack, node)
>             node = node.Left
>         }
>         // POP: the smallest value that is not visited
>         node = stack[len(stack)-1]
>         stack = stack[:len(stack)-1]
>         k-- // VISIT: count this node
>         if k == 0 {
>             return node.Val
>         }
>         // GO RIGHT: the values between this node and its parent
>         node = node.Right
>     }
>     return -1 // not possible when 1 <= k <= number of nodes
> }
> ```

### 105. Construct Binary Tree from Preorder and Inorder Traversal

[LeetCode 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Preorder cursor plus inorder index map
> - **Template:** [[#Template F: Preorder build with a cursor|F: Preorder build with a cursor]]

> [!tip]- Step 2: the idea
> **Idea.** The first value in preorder is the root. In inorder, the values before the root are the left subtree and the values after it are the right subtree. A map finds the root in inorder in O(1).
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** The closure shares the cursor `next` and the map with all its recursive calls. The parameters `lo, hi int` have one type for two names.

> [!example]- Step 3: the Go solution
> ```go
> // buildTree solves LC 105. Time O(n), space O(n).
> // It moves two indexes. It makes no copy of a slice.
> func buildTree(preorder []int, inorder []int) *TreeNode {
>     // value -> its index in inorder
>     indexOf := make(map[int]int, len(inorder))
>     for i, v := range inorder {
>         indexOf[v] = i
>     }
>
>     // CURSOR: the index of the next root in preorder. All the calls
>     // share
>     // it.
>     next := 0
>
>     // build makes the subtree whose values are inorder[lo..hi].
>     var build func(lo, hi int) *TreeNode
>     build = func(lo, hi int) *TreeNode {
>         if lo > hi { // EMPTY: no values are left for this subtree
>             return nil
>         }
>         val := preorder[next] // READ the root and move the cursor
>         next++
>         node := &TreeNode{Val: val}
>         // the root divides inorder into left and right
>         mid := indexOf[val]
>         // LEFT first: preorder gives the left subtree first
>         node.Left = build(lo, mid-1)
>         node.Right = build(mid+1, hi) // then RIGHT
>         return node
>     }
>     return build(0, len(inorder)-1)
> }
> ```

### 124. Binary Tree Maximum Path Sum

[LeetCode 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DFS returns one branch, records the full path
> - **Template:** [[#Template B: DFS that returns one value and records another|B: DFS that returns one value and records another]]

> [!tip]- Step 2: the idea
> **Idea.** The best path that turns at a node is its value plus the best branch on each side. A branch with a negative sum is not used. The parent gets only one branch, because a path cannot divide.
>
> **Complexity.** Time O(n), space O(h) for a tree of height h.
>
> **Go lesson.** `max(x, 0)` drops a negative branch in one expression. The closure changes `best`, which is a variable of the function around it.

> [!example]- Step 3: the Go solution
> ```go
> // maxPathSum solves LC 124. Time O(n), space O(h).
> func maxPathSum(root *TreeNode) int {
>     // The tree has one node or more. Do not start at 0: all the
>     // values can
>     // be negative.
>     best := root.Val
>
>     // gain returns the best sum of a path that starts at node and
>     // goes down
>     // one side.
>     var gain func(node *TreeNode) int
>     gain = func(node *TreeNode) int {
>         if node == nil { // BASE CASE
>             return 0
>         }
>         // ASK. A negative branch is dropped: use 0.
>         left := max(gain(node.Left), 0)
>         right := max(gain(node.Right), 0) // ASK
>         // RECORD: the path that turns at this node
>         best = max(best, node.Val+left+right)
>         // RETURN: one branch only for the parent
>         return node.Val + max(left, right)
>     }
>     gain(root)
>     return best
> }
> ```

### 297. Serialize and Deserialize Binary Tree

[LeetCode 297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Preorder DFS with null markers
> - **Template:** [[#Template F: Preorder build with a cursor|F: Preorder build with a cursor]]

> [!tip]- Step 2: the idea
> **Idea.** Write the tree in preorder and write a marker for each empty child. With the markers, the preorder text describes one tree only. To read it, use the same order: root, left subtree, right subtree.
>
> **Complexity.** Time O(n) for serialize and for deserialize, space O(n).
>
> **Go lesson.** `strconv.Itoa` and `strconv.Atoi` convert between `int` and `string`. `strings.Join` and `strings.Split` convert between a slice of strings and one string.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `strconv`, `strings`
>
> ```go
> // Codec solves LC 297. Time O(n) and space O(n) for each direction.
> // The tree 1 -> (2, 3) becomes "1,2,N,N,3,N,N".
> type Codec struct{}
>
> func Constructor() Codec {
>     return Codec{}
> }
>
> // Serializes a tree to a single string.
> func (this *Codec) serialize(root *TreeNode) string {
>     var tokens []string
>     var walk func(node *TreeNode)
>     walk = func(node *TreeNode) {
>         if node == nil {
>             // WRITE a marker for an empty child
>             tokens = append(tokens, "N")
>             return
>         }
>         // WRITE the root first
>         tokens = append(tokens, strconv.Itoa(node.Val))
>         // then the left subtree
>         walk(node.Left)
>         // then the right subtree
>         walk(node.Right)
>     }
>     walk(root)
>     // the comma divides the values: "12" is not "1,2"
>     return strings.Join(tokens, ",")
> }
>
> // Deserializes your encoded data to tree.
> func (this *Codec) deserialize(data string) *TreeNode {
>     tokens := strings.Split(data, ",")
>     // CURSOR: the index of the next token. All the calls share it.
>     next := 0
>
>     var build func() *TreeNode
>     build = func() *TreeNode {
>         tok := tokens[next] // READ one token and move the cursor
>         next++
>         if tok == "N" { // EMPTY: this subtree has no nodes
>             return nil
>         }
>         // the text is our own output, so the error is ignored
>         val, _ := strconv.Atoi(tok)
>         node := &TreeNode{Val: val}
>         // LEFT first, the same order as serialize
>         node.Left = build()
>         node.Right = build() // then RIGHT
>         return node
>     }
>     return build()
> }
> ```

---

[[wiki/neetcode-150/06-linked-list|← Linked List]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/08-tries|Tries →]]
