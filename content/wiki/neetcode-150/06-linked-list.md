---
title: "NeetCode 150, stage 6: Linked List"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - linked-list
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 6: Linked List

[[wiki/neetcode-150/05-binary-search|← Binary Search]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/07-trees|Trees →]]

A linked list has no index, so each problem here is about pointers: which pointer to save, which pointer to change, and in which order. This stage trains those pointer moves in Go, where `nil` is the end of a list. Draw the nodes and the arrows on paper before you write the code.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 6: Pointers with linked lists|the Go syntax for this stage]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/06-linked-list#206. Reverse Linked List\|206. Reverse Linked List]] | Easy | Reverse the pointers in place | [[wiki/neetcode-150/06-linked-list#Template A: Reverse a list\|A: Reverse a list]] |
| 2 | [[wiki/neetcode-150/06-linked-list#21. Merge Two Sorted Lists\|21. Merge Two Sorted Lists]] | Easy | Dummy head and merge | [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]] |
| 3 | [[wiki/neetcode-150/06-linked-list#143. Reorder List\|143. Reorder List]] | Medium | Middle, reverse, then weave | [[wiki/neetcode-150/06-linked-list#Template C: Fast and slow pointers\|C: Fast and slow pointers]], [[wiki/neetcode-150/06-linked-list#Template A: Reverse a list\|A: Reverse a list]] |
| 4 | [[wiki/neetcode-150/06-linked-list#19. Remove Nth Node From End of List\|19. Remove Nth Node From End of List]] | Medium | Dummy head, two pointers with a gap | [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]], [[wiki/neetcode-150/06-linked-list#Template C: Fast and slow pointers\|C: Fast and slow pointers]] |
| 5 | [[wiki/neetcode-150/06-linked-list#138. Copy List with Random Pointer\|138. Copy List with Random Pointer]] | Medium | Hash map from old node to copy | [[wiki/neetcode-150/06-linked-list#Template F: Map from old node to new node\|F: Map from old node to new node]] |
| 6 | [[wiki/neetcode-150/06-linked-list#2. Add Two Numbers\|2. Add Two Numbers]] | Medium | Dummy head with a carry | [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]] |
| 7 | [[wiki/neetcode-150/06-linked-list#141. Linked List Cycle\|141. Linked List Cycle]] | Easy | Fast and slow pointers | [[wiki/neetcode-150/06-linked-list#Template C: Fast and slow pointers\|C: Fast and slow pointers]] |
| 8 | [[wiki/neetcode-150/06-linked-list#287. Find the Duplicate Number\|287. Find the Duplicate Number]] | Medium | Floyd's cycle start on indexes | [[wiki/neetcode-150/06-linked-list#Template C: Fast and slow pointers\|C: Fast and slow pointers]] |
| 9 | [[wiki/neetcode-150/06-linked-list#146. LRU Cache\|146. LRU Cache]] | Medium | Hash map plus doubly linked list | [[wiki/neetcode-150/06-linked-list#Template D: Hash map plus doubly linked list\|D: Hash map plus doubly linked list]] |
| 10 | [[wiki/neetcode-150/06-linked-list#23. Merge k Sorted Lists\|23. Merge k Sorted Lists]] | Hard | Min-heap of list heads | [[wiki/neetcode-150/06-linked-list#Template E: Heap of nodes\|E: Heap of nodes]], [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]] |
| 11 | [[wiki/neetcode-150/06-linked-list#25. Reverse Nodes in k-Group\|25. Reverse Nodes in k-Group]] | Hard | Reverse one group at a time | [[wiki/neetcode-150/06-linked-list#Template A: Reverse a list\|A: Reverse a list]], [[wiki/neetcode-150/06-linked-list#Template B: Dummy head\|B: Dummy head]] |

## Templates to memorize

### Template A: Reverse a list

> [!tip] Signal
> The problem says reverse, or it needs the nodes from the back: "reorder", "palindrome", "groups of k". The space limit is O(1), so a copy into a slice is not permitted.

```go
// TEMPLATE A: reverse a list in place. Four moves for each node.
func reverse(head *ListNode) *ListNode {
    var prev *ListNode // nil: the old head becomes the tail
    cur := head
    for cur != nil {
        next := cur.Next // 1. SAVE the rest of the list
        cur.Next = prev  // 2. TURN the pointer back
        prev = cur       // 3. MOVE prev
        cur = next       // 4. MOVE cur
    }
    return prev // cur is nil here, and prev is the new head
}
```

The moves are SAVE, TURN, MOVE, MOVE. Save `cur.Next` before you turn the pointer, because the turn loses the rest of the list. Return `prev`, not `cur`: `cur` is `nil` when the loop stops.

> [!quote] Say it
> "I reverse the pointers in one pass with three variables: prev, cur and next. That is O(n) time and O(1) space."

### Template B: Dummy head

> [!tip] Signal
> The solution builds a new list, or it can remove the first node. For example: merge, add, remove, partition.

```go
// TEMPLATE B: dummy head. Build a list with no special case for the first
// node.
func mergeSorted(a, b *ListNode) *ListNode {
    dummy := &ListNode{} // DUMMY: a node before the real head
    tail := dummy        // the last node of the result
    for a != nil && b != nil {
        if a.Val <= b.Val { // CHOOSE the smaller front node
            tail.Next = a // LINK it after the tail
            a = a.Next
        } else {
            tail.Next = b
            b = b.Next
        }
        tail = tail.Next // ADVANCE the tail
    }
    if a != nil { // LINK THE REST: one list can have nodes left
        tail.Next = a
    } else {
        tail.Next = b
    }
    return dummy.Next // the real head is after the dummy
}
```

The moves are DUMMY, LINK, ADVANCE, then return `dummy.Next`. The dummy node gives each real node a node before it, so the first node is not a special case. Advance the tail after each link, or the next link replaces the node that you added.

> [!quote] Say it
> "I put a dummy node before the head, so I never need a special case for the first node. At the end I return dummy.Next."

### Template C: Fast and slow pointers

> [!tip] Signal
> The problem asks for the middle, a cycle, the start of a cycle or the nth node from the end. It also wants O(1) space, so a set of the nodes that you saw is not permitted.

```go
// TEMPLATE C: fast and slow pointers. fast moves two steps, slow moves one
// step.
func middle(head *ListNode) *ListNode {
    slow, fast := head, head
    for fast != nil && fast.Next != nil { // CHECK two nodes before the jump
        slow = slow.Next      // STEP 1
        fast = fast.Next.Next // STEP 2
    }
    // STOP: the middle (the second middle when the length is even)
    return slow
}

// cycleStart returns the node where the cycle starts, or nil (Floyd's
// algorithm).
func cycleStart(head *ListNode) *ListNode {
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
        if slow == fast { // MEET: the two pointers are in a cycle
            p := head // RESTART one pointer from the head
            // both move one step, and they meet at the start
            for p != slow {
                p = p.Next
                slow = slow.Next
            }
            return p
        }
    }
    return nil // fast found the end, so there is no cycle
}
```

The moves are STEP 1 for the slow pointer and STEP 2 for the fast pointer, then MEET or STOP. Test `fast != nil && fast.Next != nil` before each jump, in that order, or the code panics on `nil`. To find the start of a cycle, restart one pointer from the head after the two pointers meet. A related form puts the fast pointer `n` nodes ahead, then moves the two pointers at the same speed.

> [!quote] Say it
> "The fast pointer moves two steps and the slow pointer moves one. If there is a cycle they must meet. If there is none, the fast pointer reaches the end. O(n) time, O(1) space."

### Template D: Hash map plus doubly linked list

> [!tip] Signal
> A design problem wants `get` and `put` in O(1), and it also needs an order: least recently used, oldest first, newest first.

```go
// TEMPLATE D: hash map plus doubly linked list. The map finds a node in
// O(1).
// The list keeps the order. Two sentinel nodes remove all the nil tests.
type dnode struct {
    key, val   int
    prev, next *dnode
}

type orderedMap struct {
    nodes map[int]*dnode // key -> its node in the list
    // SENTINELS: head.next is the newest, tail.prev is the oldest
    head, tail *dnode
}

func newOrderedMap() *orderedMap {
    m := &orderedMap{nodes: map[int]*dnode{}, head: &dnode{}, tail: &dnode{}}
    m.head.next = m.tail // an empty list is head <-> tail
    m.tail.prev = m.head
    return m
}

// unlink removes n from the list: its two neighbors skip it.
func (m *orderedMap) unlink(n *dnode) {
    n.prev.next = n.next
    n.next.prev = n.prev
}

// pushFront puts n after the head sentinel. Set the pointers of n first.
func (m *orderedMap) pushFront(n *dnode) {
    n.prev = m.head
    n.next = m.head.next
    m.head.next.prev = n
    m.head.next = n
}
```

The moves are FIND the node in the map, UNLINK it, and PUSH it to the front. The map gives the node in O(1), and the two pointers of the node let you remove it in O(1). With the two sentinel nodes, each real node always has a neighbor on each side. Keep the key in the node, because an eviction must also delete the key from the map.

> [!quote] Say it
> "A hash map gives me the node in O(1), and a doubly linked list keeps the order of use. So get and put are both O(1)."

### Template E: Heap of nodes

> [!tip] Signal
> The problem gives `k` sorted lists or `k` sorted streams and asks for one sorted result. At each step you need the smallest of `k` front items.

```go
// TEMPLATE E: a min-heap of list nodes. The top is always the smallest
// front node.
type minHeap []*ListNode

func (h minHeap) Len() int { return len(h) }

// smallest on top
func (h minHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x any)        { *h = append(*h, x.(*ListNode)) }
func (h *minHeap) Pop() any {
    old := *h
    last := old[len(old)-1] // container/heap moves the top to the end first
    *h = old[:len(old)-1]
    return last
}

func valuesInOrder(lists []*ListNode) []int {
    h := &minHeap{}
    for _, node := range lists {
        if node != nil {
            heap.Push(h, node) // 1. SEED: the head of each list
        }
    }
    var res []int
    for h.Len() > 0 {
        node := heap.Pop(h).(*ListNode) // 2. POP the smallest node
        res = append(res, node.Val)
        if node.Next != nil {
            heap.Push(h, node.Next) // 3. PUSH the node after it
        }
    }
    return res
}
```

The moves are SEED the heap with the head of each list, POP the smallest node, and PUSH the node after it. The heap holds `k` nodes at most, so each operation costs O(log k). Do not push a `nil` node, because `Less` reads `Val` and the code panics.

> [!quote] Say it
> "I keep the head of each list in a min-heap. I pop the smallest node and push the node after it, so the total is O(N log k)."

### Template F: Map from old node to new node

> [!tip] Signal
> The problem says deep copy or clone, and a node has an extra pointer that can go to any other node.

```go
// TEMPLATE F: copy linked nodes with a map from each old node to its copy.
func deepCopy(head *Node) *Node {
    copyOf := make(map[*Node]*Node) // old node -> new node
    for cur := head; cur != nil; cur = cur.Next {
        // PASS 1: CREATE each copy, with no links
        copyOf[cur] = &Node{Val: cur.Val}
    }
    for cur := head; cur != nil; cur = cur.Next {
        // PASS 2: LINK through the map
        copyOf[cur].Next = copyOf[cur.Next]
        // a nil key is not in the map: the result is nil
        copyOf[cur].Random = copyOf[cur.Random]
    }
    return copyOf[head]
}
```

The moves are CREATE all the copies in the first pass, then LINK them in the second pass. The map answers one question: where is the copy of this node? Do not point a copy to an old node. Each pointer of a copy must come from the map.

> [!quote] Say it
> "I make every copy first and keep a map from each original node to its copy. The second pass sets next and random through the map, so it is O(n) time and O(n) space."

> [!warning] Mistakes in this stage
> - `fast.Next.Next` panics when `fast.Next` is `nil`. Test `fast != nil && fast.Next != nil` first.
> - Save `cur.Next` before the turn. If not, you lose the rest of the list.
> - `var dummy *ListNode` is a `nil` pointer, and `dummy.Next` panics. Write `dummy := &ListNode{}`.
> - `==` on two `*ListNode` values compares the addresses. It does not compare `Val`.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 206. Reverse Linked List

[LeetCode 206](https://leetcode.com/problems/reverse-linked-list/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Reverse the pointers in place
> - **Template:** [[#Template A: Reverse a list|A: Reverse a list]]

> [!tip]- Step 2: the idea
> **Idea.** Go through the list one time. At each node, turn its `Next` pointer back to the node before it. The last node becomes the new head.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `var prev *ListNode` declares a nil pointer. In Go, nil is the zero value of a pointer, and it is also the end of a list.

> [!example]- Step 3: the Go solution
> ```go
> // reverseList solves LC 206. Time O(n), space O(1).
> // Four moves for each node: SAVE, TURN, MOVE, MOVE.
> func reverseList(head *ListNode) *ListNode {
>     // nil: the old head becomes the tail, and the tail points to
>     // nil
>     var prev *ListNode
>     cur := head
>     for cur != nil {
>         // SAVE: the turn below loses the rest of the list
>         next := cur.Next
>         cur.Next = prev // TURN: this node now points back
>         prev = cur      // MOVE prev one node forward
>         cur = next      // MOVE cur one node forward
>     }
>     // cur is nil here, and prev is the last node: the new head
>     return prev
> }
> ```

### 21. Merge Two Sorted Lists

[LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Dummy head and merge
> - **Template:** [[#Template B: Dummy head|B: Dummy head]]

> [!tip]- Step 2: the idea
> **Idea.** Compare the two front nodes and link the smaller one after the tail of the result. A dummy node before the result removes the special case for the first node.
>
> **Complexity.** Time O(n + m), space O(1).
>
> **Go lesson.** `&ListNode{}` makes a node with zero values and gives its address. The solution moves the nodes that exist. It does not copy them.

> [!example]- Step 3: the Go solution
> ```go
> // mergeTwoLists solves LC 21. Time O(n + m), space O(1).
> // It links the nodes of the two lists again. It makes no new node
> // except
> // the dummy.
> func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
>     dummy := &ListNode{} // DUMMY: a node before the real head
>     tail := dummy        // the last node of the merged list
>     for list1 != nil && list2 != nil {
>         if list1.Val <= list2.Val { // CHOOSE the smaller front node
>             tail.Next = list1 // LINK it after the tail
>             list1 = list1.Next
>         } else {
>             tail.Next = list2
>             list2 = list2.Next
>         }
>         tail = tail.Next // ADVANCE the tail
>     }
>     // LINK THE REST: one list is empty, and the other is already
>     // sorted.
>     if list1 != nil {
>         tail.Next = list1
>     } else {
>         tail.Next = list2
>     }
>     return dummy.Next // the real head is after the dummy
> }
> ```

### 143. Reorder List

[LeetCode 143](https://leetcode.com/problems/reorder-list/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Middle, reverse, then weave
> - **Template:** [[#Template C: Fast and slow pointers|C: Fast and slow pointers]], [[#Template A: Reverse a list|A: Reverse a list]]

> [!tip]- Step 2: the idea
> **Idea.** The answer takes one node from the front, then one node from the back, and so on. So find the middle, reverse the second half, and weave the two halves together.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** This function returns nothing. It changes the list through the pointers. `a, b = x, y` assigns two variables in one statement.

> [!example]- Step 3: the Go solution
> ```go
> // reorderList solves LC 143. Time O(n), space O(1).
> // Three steps: find the middle, reverse the second half, weave the
> // two
> // halves.
> func reorderList(head *ListNode) {
>     if head == nil {
>         return
>     }
>     // 1. MIDDLE (template C): slow stops at the middle node.
>     slow, fast := head, head
>     for fast != nil && fast.Next != nil {
>         slow = slow.Next      // STEP 1
>         fast = fast.Next.Next // STEP 2
>     }
>
>     // 2. CUT the list after the middle, then REVERSE the second
>     // half
>     // (template A).
>     cur := slow.Next
>     slow.Next = nil // the first half now ends at the middle node
>     var prev *ListNode
>     for cur != nil {
>         next := cur.Next // SAVE
>         cur.Next = prev  // TURN
>         prev = cur       // MOVE
>         cur = next       // MOVE
>     }
>
>     // 3. WEAVE: one node of the first half, then one node of the
>     // reversed
>     // half.
>     // The second half is shorter than the first half, so it ends
>     // first.
>     first, second := head, prev
>     for second != nil {
>         // SAVE the two next nodes
>         next1, next2 := first.Next, second.Next
>         first.Next = second // first -> second
>         // second -> the old next of first
>         second.Next = next1
>         first, second = next1, next2 // MOVE the two pointers
>     }
> }
> ```

### 19. Remove Nth Node From End of List

[LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Dummy head, two pointers with a gap
> - **Template:** [[#Template B: Dummy head|B: Dummy head]], [[#Template C: Fast and slow pointers|C: Fast and slow pointers]]

> [!tip]- Step 2: the idea
> **Idea.** Put the fast pointer n nodes ahead of the slow pointer, then move the two at the same speed. When the fast pointer is at the last node, the slow pointer is immediately before the node to remove.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** Go has a garbage collector. To delete a node, make the list skip it. There is no `free`.

> [!example]- Step 3: the Go solution
> ```go
> // removeNthFromEnd solves LC 19. Time O(n), space O(1), one pass.
> func removeNthFromEnd(head *ListNode, n int) *ListNode {
>     // DUMMY: the head itself can be the node to remove
>     dummy := &ListNode{Next: head}
>     slow, fast := dummy, dummy
>     for i := 0; i < n; i++ { // GAP: fast goes n nodes ahead of slow
>         fast = fast.Next
>     }
>     // move the two pointers until fast is the last node
>     for fast.Next != nil {
>         slow = slow.Next
>         fast = fast.Next
>     }
>     // SKIP: slow is the node before the one to remove
>     slow.Next = slow.Next.Next
>     // not head: the old head is possibly not in the list now
>     return dummy.Next
> }
> ```

### 138. Copy List with Random Pointer

[LeetCode 138](https://leetcode.com/problems/copy-list-with-random-pointer/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Hash map from old node to copy
> - **Template:** [[#Template F: Map from old node to new node|F: Map from old node to new node]]

> [!tip]- Step 2: the idea
> **Idea.** A random pointer can point to a node that has no copy yet. So make all the copies first and keep them in a map. Then set the pointers through the map.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** A pointer can be a map key: `map[*Node]*Node`. A lookup of a key that is not in the map gives the zero value, which is nil here.

> [!example]- Step 3: the Go solution
> ```go
> // copyRandomList solves LC 138. Time O(n), space O(n).
> // Two passes: create the copies, then link them through the map.
> func copyRandomList(head *Node) *Node {
>     copyOf := make(map[*Node]*Node) // old node -> its copy
>
>     // PASS 1: CREATE a copy of each node. The copies have no links
>     // yet.
>     for cur := head; cur != nil; cur = cur.Next {
>         copyOf[cur] = &Node{Val: cur.Val}
>     }
>     // PASS 2: LINK. Each old pointer becomes a pointer to the copy.
>     for cur := head; cur != nil; cur = cur.Next {
>         // nil is not a key, so the lookup gives nil
>         copyOf[cur].Next = copyOf[cur.Next]
>         // the same for a nil random pointer
>         copyOf[cur].Random = copyOf[cur.Random]
>     }
>     return copyOf[head] // nil when the list is empty
> }
> ```

### 2. Add Two Numbers

[LeetCode 2](https://leetcode.com/problems/add-two-numbers/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Dummy head with a carry
> - **Template:** [[#Template B: Dummy head|B: Dummy head]]

> [!tip]- Step 2: the idea
> **Idea.** The digits are in reverse order, so each list starts at the ones digit. Add digit by digit as you do on paper, and keep the carry for the next digit.
>
> **Complexity.** Time O(max(n, m)), space O(1) extra, the result has max(n, m) + 1 nodes at most.
>
> **Go lesson.** `/` on two `int` values is integer division and `%` is the remainder. So `sum / 10` is the carry and `sum % 10` is the digit.

> [!example]- Step 3: the Go solution
> ```go
> // addTwoNumbers solves LC 2. Time O(max(n, m)), space O(1) extra.
> func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
>     dummy := &ListNode{} // DUMMY: a node before the real head
>     tail := dummy
>     carry := 0
>     // Continue while a list has digits or a carry waits (99 + 1
>     // needs a
>     // third node).
>     for l1 != nil || l2 != nil || carry > 0 {
>         sum := carry
>         if l1 != nil { // a list that ended counts as 0
>             sum += l1.Val
>             l1 = l1.Next
>         }
>         if l2 != nil {
>             sum += l2.Val
>             l2 = l2.Next
>         }
>         carry = sum / 10 // 0 or 1
>         // LINK a new node with the digit
>         tail.Next = &ListNode{Val: sum % 10}
>         tail = tail.Next // ADVANCE the tail
>     }
>     return dummy.Next
> }
> ```

### 141. Linked List Cycle

[LeetCode 141](https://leetcode.com/problems/linked-list-cycle/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Fast and slow pointers
> - **Template:** [[#Template C: Fast and slow pointers|C: Fast and slow pointers]]

> [!tip]- Step 2: the idea
> **Idea.** Move one pointer one step and the other pointer two steps. If the list has a cycle, the fast pointer goes around and meets the slow pointer. If the list has no cycle, the fast pointer finds the end.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `==` on two pointers compares the addresses, not the values. Two different nodes with the same `Val` are not equal.

> [!example]- Step 3: the Go solution
> ```go
> // hasCycle solves LC 141. Time O(n), space O(1).
> func hasCycle(head *ListNode) bool {
>     slow, fast := head, head
>     // CHECK two nodes before the jump
>     for fast != nil && fast.Next != nil {
>         slow = slow.Next      // STEP 1
>         fast = fast.Next.Next // STEP 2
>         // MEET: the same node, so the list has a cycle
>         if slow == fast {
>             return true
>         }
>     }
>     return false // STOP: fast found the end of the list
> }
> ```

### 287. Find the Duplicate Number

[LeetCode 287](https://leetcode.com/problems/find-the-duplicate-number/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Floyd's cycle start on indexes
> - **Template:** [[#Template C: Fast and slow pointers|C: Fast and slow pointers]]

> [!tip]- Step 2: the idea
> **Idea.** Read the slice as a linked list: index i points to index nums[i]. Two indexes point to the duplicate value, so that value is the start of a cycle. Floyd's algorithm finds the start.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** There is no node type here. `slow = nums[slow]` is the same move as `slow = slow.Next`.

> [!example]- Step 3: the Go solution
> ```go
> // findDuplicate solves LC 287. Time O(n), space O(1). It does not
> // change
> // nums.
> // The values are 1..n, so no value points to index 0. Index 0 is
> // the head
> // of the list.
> func findDuplicate(nums []int) int {
>     // Phase 1: MEET. slow moves one step and fast moves two steps.
>     slow, fast := 0, 0
>     for {
>         slow = nums[slow]       // STEP 1
>         fast = nums[nums[fast]] // STEP 2
>         if slow == fast {       // the two pointers are in the cycle
>             break
>         }
>     }
>     // Phase 2: RESTART one pointer from the head. Now the two move
>     // one
>     // step.
>     // They meet at the start of the cycle, and that index is the
>     // duplicate
>     // value.
>     p := 0
>     for p != slow {
>         p = nums[p]
>         slow = nums[slow]
>     }
>     return p
> }
> ```

### 146. LRU Cache

[LeetCode 146](https://leetcode.com/problems/lru-cache/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Hash map plus doubly linked list
> - **Template:** [[#Template D: Hash map plus doubly linked list|D: Hash map plus doubly linked list]]

> [!tip]- Step 2: the idea
> **Idea.** The map finds the node of a key in O(1). The list keeps the nodes in order of use: the newest at the front, the oldest at the back. Each use moves the node to the front, and a full cache drops the node at the back.
>
> **Complexity.** Time O(1) for Get and for Put, space O(capacity).
>
> **Go lesson.** A method with a pointer receiver, `func (this *LRUCache)`, can change the struct. `delete(m, key)` removes a map entry.

> [!example]- Step 3: the Go solution
> ```go
> // node is one entry of the doubly linked list.
> // It keeps the key also, because the eviction must delete the key
> // from the
> // map.
> type node struct {
>     key, val   int
>     prev, next *node
> }
>
> // LRUCache solves LC 146. Get and Put are O(1).
> type LRUCache struct {
>     capacity int
>     nodes    map[int]*node // key -> its node
>     // SENTINELS: head.next is the newest, tail.prev is the oldest
>     head, tail *node
> }
>
> func Constructor(capacity int) LRUCache {
>     head, tail := &node{}, &node{}
>     head.next = tail // an empty list is head <-> tail
>     tail.prev = head
>     return LRUCache{
>         capacity: capacity,
>         nodes:    make(map[int]*node, capacity),
>         head:     head,
>         tail:     tail,
>     }
> }
>
> // unlink removes n from the list. The sentinels mean that prev and
> // next are
> // never nil.
> func (this *LRUCache) unlink(n *node) {
>     n.prev.next = n.next
>     n.next.prev = n.prev
> }
>
> // pushFront puts n immediately after the head sentinel: n is now
> // the
> // newest.
> func (this *LRUCache) pushFront(n *node) {
>     n.prev = this.head // set the two pointers of n first
>     n.next = this.head.next
>     this.head.next.prev = n // then the two neighbors point to n
>     this.head.next = n
> }
>
> func (this *LRUCache) Get(key int) int {
>     n, ok := this.nodes[key] // FIND the node in the map
>     if !ok {
>         return -1
>     }
>     // a read is a use: UNLINK the node and PUSH it to the front
>     this.unlink(n)
>     this.pushFront(n)
>     return n.val
> }
>
> func (this *LRUCache) Put(key int, value int) {
>     // the key exists: change the value, move to the front
>     if n, ok := this.nodes[key]; ok {
>         n.val = value
>         this.unlink(n)
>         this.pushFront(n)
>         return
>     }
>     // full: EVICT the oldest node
>     if len(this.nodes) == this.capacity {
>         oldest := this.tail.prev
>         this.unlink(oldest)
>         // this line is why the node keeps its key
>         delete(this.nodes, oldest.key)
>     }
>     n := &node{key: key, val: value}
>     this.nodes[key] = n // STORE in the map and in the list
>     this.pushFront(n)
> }
> ```

### 23. Merge k Sorted Lists

[LeetCode 23](https://leetcode.com/problems/merge-k-sorted-lists/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Min-heap of list heads
> - **Template:** [[#Template E: Heap of nodes|E: Heap of nodes]], [[#Template B: Dummy head|B: Dummy head]]

> [!tip]- Step 2: the idea
> **Idea.** The next node of the result is always the smallest of the k front nodes. A min-heap gives that node in O(log k). After you take a node, push the node after it.
>
> **Complexity.** Time O(N log k) for N nodes in k lists, space O(k).
>
> **Go lesson.** `container/heap` needs a type with five methods: `Len`, `Less`, `Swap`, `Push` and `Pop`. `heap.Pop` returns `any`, so `.(*ListNode)` converts the value back.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `container/heap`
>
> ```go
> // nodeHeap is a min-heap of list nodes. It implements
> // heap.Interface.
> type nodeHeap []*ListNode
>
> func (h nodeHeap) Len() int { return len(h) }
>
> // smallest on top
> func (h nodeHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
> func (h nodeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
>
> // Push and Pop have a pointer receiver, because they change the
> // length of
> // the slice.
> func (h *nodeHeap) Push(x any) { *h = append(*h, x.(*ListNode)) }
> func (h *nodeHeap) Pop() any {
>     old := *h
>     // container/heap moves the top to the end first
>     last := old[len(old)-1]
>     *h = old[:len(old)-1]
>     return last
> }
>
> // mergeKLists solves LC 23. Time O(N log k) for N nodes in k lists,
> // space
> // O(k).
> func mergeKLists(lists []*ListNode) *ListNode {
>     h := &nodeHeap{}
>     for _, node := range lists {
>         if node != nil { // an empty list gives no node
>             heap.Push(h, node) // SEED: the head of each list
>         }
>     }
>
>     dummy := &ListNode{} // DUMMY head for the result (template B)
>     tail := dummy
>     for h.Len() > 0 {
>         // POP the smallest of the front nodes
>         node := heap.Pop(h).(*ListNode)
>         tail.Next = node // LINK it after the tail
>         tail = tail.Next // ADVANCE the tail
>         if node.Next != nil {
>             // PUSH the node after it in the same list
>             heap.Push(h, node.Next)
>         }
>     }
>     return dummy.Next
> }
> ```

### 25. Reverse Nodes in k-Group

[LeetCode 25](https://leetcode.com/problems/reverse-nodes-in-k-group/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Reverse one group at a time
> - **Template:** [[#Template A: Reverse a list|A: Reverse a list]], [[#Template B: Dummy head|B: Dummy head]]

> [!tip]- Step 2: the idea
> **Idea.** Find the k-th node of the group first. If the group is not complete, stop. If it is complete, reverse only that group and connect it to the node before it and to the node after it.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `for { ... }` with no condition is an infinite loop, and `break` stops it. Use it when the stop test is in the middle of the loop.

> [!example]- Step 3: the Go solution
> ```go
> // reverseKGroup solves LC 25. Time O(n), space O(1).
> // groupPrev is always the node before the group that you reverse
> // next.
> func reverseKGroup(head *ListNode, k int) *ListNode {
>     // DUMMY: the first group also has a node before it
>     dummy := &ListNode{Next: head}
>     groupPrev := dummy
>     for {
>         // FIND the k-th node of the group: k steps from groupPrev.
>         kth := groupPrev
>         for i := 0; i < k && kth != nil; i++ {
>             kth = kth.Next
>         }
>         // fewer than k nodes are left: they stay as they are
>         if kth == nil {
>             break
>         }
>         groupNext := kth.Next // the first node after the group
>
>         // REVERSE the group (template A). prev starts at groupNext,
>         // not at
>         // nil,
>         // so the old first node points to the rest of the list.
>         prev, cur := groupNext, groupPrev.Next
>         for cur != groupNext {
>             next := cur.Next // SAVE
>             cur.Next = prev  // TURN
>             prev = cur       // MOVE
>             cur = next       // MOVE
>         }
>
>         // CONNECT: the k-th node is now the first node of the
>         // group.
>         // the old first node is now the last node of the group
>         first := groupPrev.Next
>         groupPrev.Next = kth
>         groupPrev = first // the next group starts after this node
>     }
>     return dummy.Next
> }
> ```

---

[[wiki/neetcode-150/05-binary-search|← Binary Search]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/07-trees|Trees →]]
