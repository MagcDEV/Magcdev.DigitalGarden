---
title: "NeetCode 150, stage 8: Tries"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - tries
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 8: Tries

[[wiki/neetcode-150/07-trees|← Trees]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/09-heap-priority-queue|Heap and Priority Queue →]]

A trie stores strings letter by letter, so words with the same prefix share nodes. This stage trains prefix questions. A lookup costs O(L) for a word of L letters, and the number of stored words does not change that cost. The last problem joins a trie with grid backtracking.

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/08-tries#208. Implement Trie (Prefix Tree)\|208. Implement Trie (Prefix Tree)]] | Medium | Trie (prefix tree) | [[wiki/neetcode-150/08-tries#Template A: Trie node, insert and walk\|A: Trie node, insert and walk]] |
| 2 | [[wiki/neetcode-150/08-tries#211. Design Add and Search Words Data Structure\|211. Design Add and Search Words Data Structure]] | Medium | Trie with wildcard DFS | [[wiki/neetcode-150/08-tries#Template A: Trie node, insert and walk\|A: Trie node, insert and walk]], [[wiki/neetcode-150/08-tries#Template B: DFS on the trie for wildcards\|B: DFS on the trie for wildcards]] |
| 3 | [[wiki/neetcode-150/08-tries#212. Word Search II\|212. Word Search II]] | Hard | Trie plus grid backtracking | [[wiki/neetcode-150/08-tries#Template A: Trie node, insert and walk\|A: Trie node, insert and walk]], [[wiki/neetcode-150/08-tries#Template C: Trie plus grid backtracking\|C: Trie plus grid backtracking]] |

## Templates to memorize

### Template A: Trie node, insert and walk

> [!tip] Signal
> The problem says prefix, "starts with", autocomplete or dictionary of words. You must answer many lookups on the same set of strings.

```go
// TEMPLATE A: the trie node, INSERT and WALK.
type trieNode struct {
    // one slot for each lower-case letter; nil means "no child"
    children [26]*trieNode
    end      bool // true when a word ends at this node
}

func (root *trieNode) insert(word string) {
    node := root
    for i := 0; i < len(word); i++ {
        c := word[i] - 'a'
        if node.children[c] == nil {
            // 1. CREATE the child on first use
            node.children[c] = &trieNode{}
        }
        node = node.children[c] // 2. STEP down one letter
    }
    node.end = true // 3. MARK the end of the word
}

// walk returns the node at the end of s, or nil when the path stops.
// Search a word: the node is not nil AND node.end is true. Search a prefix:
// the node is not nil.
func (root *trieNode) walk(s string) *trieNode {
    node := root
    for i := 0; i < len(s); i++ {
        node = node.children[s[i]-'a'] // STEP down
        if node == nil {
            return nil
        }
    }
    return node
}
```

The moves are CREATE, STEP, then MARK for an insert, and STEP for a lookup. A word search and a prefix search use the same walk. Only the last test is different: a word search also needs `node.end`. If you forget that test, a search finds "app" after you insert only "apple".

> [!quote] Say it
> "Each node is one letter, and a flag marks the end of a word. Insert and search are O(L) for a word of length L, and the number of words does not matter."

### Template B: DFS on the trie for wildcards

> [!tip] Signal
> The search pattern has a wildcard such as `.` that can be each letter. A hash set cannot answer that, because you cannot hash an unknown letter.

```go
// TEMPLATE B: DFS on the trie. A '.' in the pattern can be each letter.
func matchFrom(node *trieNode, pattern string, i int) bool {
    if node == nil {
        return false // 1. STOP: the path ended before the pattern
    }
    if i == len(pattern) {
        return node.end // 2. END: a word must end exactly here
    }
    if pattern[i] != '.' {
        // 3. a letter: ONE path
        return matchFrom(node.children[pattern[i]-'a'], pattern, i+1)
    }
    for _, child := range node.children { // 4. a dot: BRANCH to each child
        if matchFrom(child, pattern, i+1) {
            return true
        }
    }
    return false
}
```

The moves are STOP on `nil`, test the END, follow ONE path for a letter, and BRANCH for a dot. Put the `nil` test first. Then the loop can pass each child with no test of its own.

> [!quote] Say it
> "A letter follows one child. A dot tries all 26 children with a DFS. With no dots the search stays O(L)."

### Template C: Trie plus grid backtracking

> [!tip] Signal
> You must find many words in one grid of letters. A separate grid search for each word repeats the same walks.

```go
// TEMPLATE C: the trie holds all the words, and one DFS walks the grid and
// the trie together.
type wordNode struct {
    children [26]*wordNode
    word     string // the full word when a word ends here, "" when not
}

func wordsInGrid(grid [][]byte, root *wordNode) []string {
    found := []string{}
    var dfs func(r, c int, parent *wordNode)
    dfs = func(r, c int, parent *wordNode) {
        if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) || grid[r][c] == '#' {
            return // out of the grid, or the cell is already in this path
        }
        letter := grid[r][c]
        node := parent.children[letter-'a']
        if node == nil {
            return // 1. PRUNE: no word continues with this letter
        }
        if node.word != "" {
            found = append(found, node.word) // 2. COLLECT
            node.word = ""                   // one time for each word
        }
        grid[r][c] = '#'  // 3. MARK
        dfs(r+1, c, node) // 4. EXPLORE the four neighbors
        dfs(r-1, c, node)
        dfs(r, c+1, node)
        dfs(r, c-1, node)
        grid[r][c] = letter // 5. UNMARK
    }
    for r := 0; r < len(grid); r++ {
        for c := 0; c < len(grid[0]); c++ {
            dfs(r, c, root) // each cell can be the first letter
        }
    }
    return found
}
```

The moves are PRUNE, COLLECT, MARK, EXPLORE, then UNMARK. The DFS moves in the grid and in the trie at the same time. The trie stops a path when no word continues with that letter. Clear `node.word` after you collect it, or the result gets the same word again from another path. The mark and unmark moves are the grid template of [[wiki/neetcode-150/10-backtracking#Template D: Grid path with mark and unmark|the Backtracking stage]].

> [!quote] Say it
> "I put all the words in a trie and run one backtracking DFS from each cell. The trie prunes each path that is not a prefix of some word."

> [!warning] Mistakes in this stage
> - `word[i]` is a `byte`, not a letter index. Subtract `'a'` before you use it as an index.
> - A `[26]*trieNode` array works only for lower-case letters. For other characters, use a `map[rune]*trieNode`.
> - A method on a `nil` node pointer panics when it reads a field. Test for `nil` before you read `node.end`.
> - The mark `'#'` is not a lower-case letter. Test for it before you compute `letter-'a'`.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 208. Implement Trie (Prefix Tree)

[LeetCode 208](https://leetcode.com/problems/implement-trie-prefix-tree/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Trie (prefix tree)
> - **Template:** [[#Template A: Trie node, insert and walk|A: Trie node, insert and walk]]

> [!tip]- Step 2: the idea
> **Idea.** Each node is one letter on a path from the root. Words with the same prefix share their first nodes. A flag marks each node where a word ends.
>
> **Complexity.** Time O(L) for each operation on a word of L letters, space O(N) for N letters in all the inserted words.
>
> **Go lesson.** A `[26]*trieNode` array starts as 26 `nil` pointers, so a new node needs no setup. `&trieNode{}` makes a node and gives its pointer.

> [!example]- Step 3: the Go solution
> ```go
> // Trie solves LC 208. Each operation is O(L) time for a word of L
> // letters.
> // The path from the root to a node spells a prefix. Each node has
> // one slot
> // for each letter.
> type trieNode struct {
>     children [26]*trieNode // nil means "no child for this letter"
>     end      bool          // true when a word ends at this node
> }
>
> type Trie struct {
>     root *trieNode
> }
>
> func Constructor() Trie {
>     return Trie{root: &trieNode{}} // the root is the empty prefix
> }
>
> func (this *Trie) Insert(word string) {
>     node := this.root
>     for i := 0; i < len(word); i++ {
>         c := word[i] - 'a' // 'a' -> 0, 'b' -> 1, and so on
>         if node.children[c] == nil {
>             // CREATE the child on first use
>             node.children[c] = &trieNode{}
>         }
>         node = node.children[c] // STEP down one letter
>     }
>     node.end = true // MARK: a word ends here
> }
>
> func (this *Trie) Search(word string) bool {
>     node := this.walk(word)
>     // the path must exist AND a word must end there
>     return node != nil && node.end
> }
>
> func (this *Trie) StartsWith(prefix string) bool {
>     return this.walk(prefix) != nil // the path alone is enough
> }
>
> // walk follows s from the root. It returns the last node, or nil
> // when the
> // path stops.
> func (this *Trie) walk(s string) *trieNode {
>     node := this.root
>     for i := 0; i < len(s); i++ {
>         node = node.children[s[i]-'a'] // STEP down
>         if node == nil {
>             return nil // no word has this prefix
>         }
>     }
>     return node
> }
> ```

### 211. Design Add and Search Words Data Structure

[LeetCode 211](https://leetcode.com/problems/design-add-and-search-words-data-structure/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Trie with wildcard DFS
> - **Template:** [[#Template A: Trie node, insert and walk|A: Trie node, insert and walk]], [[#Template B: DFS on the trie for wildcards|B: DFS on the trie for wildcards]]

> [!tip]- Step 2: the idea
> **Idea.** Store the words in a trie. A letter follows one child. A dot can be each letter, so the search tries all the children at that position.
>
> **Complexity.** Time O(L), or O(26^d * L) for a search with d dots, space O(N) for N stored letters.
>
> **Go lesson.** A `range` over an array gives each element in index order. Here it gives the 26 child pointers, and the `nil` ones stop in the first line of `match`.

> [!example]- Step 3: the Go solution
> ```go
> // WordDictionary solves LC 211. AddWord is O(L). Search is O(L)
> // when the
> // word has no dot.
> // The words go into a trie. In a search, a '.' branches to all the
> // children
> // of the node.
> type trieNode struct {
>     children [26]*trieNode // nil means "no child for this letter"
>     end      bool          // true when a word ends at this node
> }
>
> type WordDictionary struct {
>     root *trieNode
> }
>
> func Constructor() WordDictionary {
>     return WordDictionary{root: &trieNode{}}
> }
>
> func (this *WordDictionary) AddWord(word string) {
>     node := this.root
>     for i := 0; i < len(word); i++ {
>         c := word[i] - 'a'
>         if node.children[c] == nil {
>             // CREATE the child on first use
>             node.children[c] = &trieNode{}
>         }
>         node = node.children[c] // STEP down one letter
>     }
>     node.end = true // MARK: a word ends here
> }
>
> func (this *WordDictionary) Search(word string) bool {
>     return match(this.root, word, 0)
> }
>
> // match reports if word[i:] matches a path that starts at node.
> func match(node *trieNode, word string, i int) bool {
>     if node == nil {
>         return false // the path stopped before the word ended
>     }
>     if i == len(word) {
>         // all the characters are used: a word must end here
>         return node.end
>     }
>     if word[i] != '.' {
>         // a letter: ONE path
>         return match(node.children[word[i]-'a'], word, i+1)
>     }
>     // a dot: BRANCH to each child
>     for _, child := range node.children {
>         if match(child, word, i+1) {
>             return true // one path that matches is enough
>         }
>     }
>     return false
> }
> ```

### 212. Word Search II

[LeetCode 212](https://leetcode.com/problems/word-search-ii/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Trie plus grid backtracking
> - **Template:** [[#Template A: Trie node, insert and walk|A: Trie node, insert and walk]], [[#Template C: Trie plus grid backtracking|C: Trie plus grid backtracking]]

> [!tip]- Step 2: the idea
> **Idea.** A search for each word alone repeats the same walks. Put all the words in a trie. Then one DFS from each cell follows the board and the trie together, and it stops when the trie has no child.
>
> **Complexity.** Time O(R * C * 4 * 3^(L-1)) for words of L letters or fewer, space O(N) for N letters in the words.
>
> **Go lesson.** A closure such as `dfs` reads and changes `board` and `res` from the outer function. Declare it with `var` first, so that it can call itself.

> [!example]- Step 3: the Go solution
> ```go
> // findWords solves LC 212. Time O(R * C * 4 * 3^(L-1)) for words of
> // length
> // L or less.
> // The trie holds all the words, so one DFS from each cell searches
> // for all
> // of them.
> type trieNode struct {
>     children [26]*trieNode
>     // the full word when a word ends here, "" when not
>     word string
> }
>
> func findWords(board [][]byte, words []string) []string {
>     root := &trieNode{}
>     for _, w := range words { // BUILD the trie
>         node := root
>         for i := 0; i < len(w); i++ {
>             c := w[i] - 'a'
>             if node.children[c] == nil {
>                 node.children[c] = &trieNode{}
>             }
>             node = node.children[c]
>         }
>         // the node keeps the word, so the DFS does not build
>         // strings
>         node.word = w
>     }
>
>     rows, cols := len(board), len(board[0])
>     res := []string{}
>     var dfs func(r, c int, parent *trieNode)
>     dfs = func(r, c int, parent *trieNode) {
>         // Do the '#' check before the trie step: '#' is not a
>         // letter index.
>         if r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] == '#' {
>             // out of the board, or the cell is already in this path
>             return
>         }
>         letter := board[r][c]
>         node := parent.children[letter-'a']
>         if node == nil {
>             return // PRUNE: no word continues with this letter
>         }
>         if node.word != "" {
>             res = append(res, node.word) // COLLECT
>             // clear it, so each word is in the result one time
>             node.word = ""
>         }
>         board[r][c] = '#' // MARK the cell as used in this path
>         dfs(r+1, c, node) // EXPLORE the four neighbors
>         dfs(r-1, c, node)
>         dfs(r, c+1, node)
>         dfs(r, c-1, node)
>         board[r][c] = letter // UNMARK: other paths can use the cell
>     }
>     for r := 0; r < rows; r++ {
>         for c := 0; c < cols; c++ {
>             dfs(r, c, root) // each cell can be the first letter
>         }
>     }
>     // A common speedup: remove a trie node when it has no children
>     // and no
>     // word.
>     return res
> }
> ```

---

[[wiki/neetcode-150/07-trees|← Trees]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/09-heap-priority-queue|Heap and Priority Queue →]]
