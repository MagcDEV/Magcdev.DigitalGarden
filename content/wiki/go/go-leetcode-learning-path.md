---
title: "Learn Go with LeetCode: a learning path"
tags:
  - wiki
  - go
  - leetcode
  - learning-path
  - patterns
  - templates
date_created: 2026-11-09
date_modified: 2026-11-11
---

# Learn Go with LeetCode: a learning path

This path teaches Go syntax and DSA patterns at the same time. Each stage pairs one part of Go with one pattern that uses it. You learn the syntax because the problem needs it, so it stays in memory.

Each stage has the same four parts:

1. **Go you need**: the syntax for this stage, as code with comments.
2. **Template to memorize**: the short code shape that solves the full family of problems.
3. **Solved with comments**: real LeetCode solutions. The comments explain the idea and the Go.
4. **Practice**: a graded list of problems to solve in Go.

> [!success] The code runs
> All the code on this page was compiled and tested with Go 1.27 on 2026-11-09 (`go vet` and `go test`). Each function has the name and signature that LeetCode uses, so you can paste it there.

## The path on one page

| Stage | Go you learn | Pattern | Template to memorize |
|---|---|---|---|
| [0](#stage-0-setup) | `go mod`, files, `go test` | none | The table-driven test |
| [1](#stage-1-slices-and-maps-with-arrays-and-hashing) | Slices, maps, `range`, arrays as keys | Arrays and hashing | Count map, "seen" map |
| [2](#stage-2-strings-with-two-pointers) | Strings, bytes, runes, `strings.Builder` | Two pointers | Converging pointers |
| [3](#stage-3-loops-with-the-sliding-window) | The four `for` forms, `min` and `max`, counter arrays | Sliding window | Grow, shrink, record |
| [4](#stage-4-slices-as-a-stack) | Slice as stack and queue, `switch`, methods | Stack, monotonic stack | Indexes that wait |
| [5](#stage-5-the-sort-package-with-binary-search) | `sort`, `slices`, function values | Binary search, intervals | Exact value, first true |
| [6](#stage-6-pointers-with-linked-lists) | Structs, pointers, `nil`, multiple assignment | Linked list | Reverse, dummy head, fast and slow |
| [7](#stage-7-recursion-and-closures-with-trees) | Recursion, closures, multiple returns | Tree DFS and BFS | Recursive DFS, BFS by level |
| [8](#stage-8-interfaces-with-the-heap) | Interfaces, pointer receivers, `any` | Heap, top K | The five heap methods |
| [9](#stage-9-slice-copies-with-backtracking) | Slice aliasing, `slices.Clone` | Backtracking | Choose, explore, undo |
| [10](#stage-10-grids-and-graphs) | 2D slices, `[2]int`, adjacency lists | Graph DFS, BFS, topological sort | Grid DFS, BFS by level, Kahn |
| [11](#stage-11-tables-with-dynamic-programming) | `make` for tables, `math.MaxInt` | Dynamic programming | State, base case, transition, answer |

One stage for each week is a good speed. That is one problem for each day, with two days to repeat the templates.

After this path, continue with [[wiki/neetcode-150/index|NeetCode 150 in Go]]. It has the full list of 150 problems, with the pattern, the template and a commented Go solution for each one.

## How to use this path

### The loop for each problem

1. Read the problem. Name the pattern before you write code. The [[#Signals: which template to use|signal table]] helps.
2. Set a timer for 20 minutes. Try the problem in Go, in your editor.
3. If you are blocked, read the solved example. Read each comment.
4. Close the page. Type the solution from memory. Do not paste it.
5. Run the tests. Fix each compile error yourself, because compile errors teach the syntax.
6. Say the idea aloud in two sentences. Then say the time and space complexity.
7. Write the solution again after 1 day, 3 days and 7 days.

Step 4 is the most important one. To read a solution feels like progress, but only recall builds memory.

### How to memorize a template

- **Memorize templates, not problems.** This page has about 20 templates. LeetCode has thousands of problems.
- **Learn the moves first.** Each template has three or four named moves, for example GROW, SHRINK, RECORD. Say the moves, then write the code.
- **Write one template each day from memory.** Use an empty file and five minutes. Compile it. Compare it with this page.
- **Change one thing.** After you know a template, solve a second problem with it. The changed lines show what the template really is.
- **Keep a mistake list.** Write each compile error and each wrong answer in one file. Read it before each session.

### What LeetCode gives you in Go

- LeetCode gives you the function signature. You write no `package` line and no `main` function.
- LeetCode adds the standard library imports for you. Your local file needs them.
- LeetCode gives the types `ListNode` and `TreeNode`. Do not paste them in your answer.
- `int` is 64 bits there, so most sums do not overflow.
- An unused variable or an unused import is a compile error in Go. Delete it, or assign it to `_`.

## Stage 0: Setup

Make one module for all your solutions. Use one file for each problem and one test file next to it.

```bash
mkdir leetcode-go && cd leetcode-go
go mod init leetcode
# Files: lc0217_contains_duplicate.go and lc0217_contains_duplicate_test.go
go test ./...                          # run all the tests
go test -run TestContainsDuplicate -v  # run one test, with details
gofmt -w .                             # format the code
go vet ./...                           # find common mistakes
```

The solution file. The first line of each file is `package leetcode`.

```go
// containsDuplicate solves LC 217.
// It returns true when a value appears two or more times.
func containsDuplicate(nums []int) bool {
    seen := make(map[int]bool) // a map used as a set
    for _, x := range nums {   // _ drops the index, x is the value
        if seen[x] { // a missing key reads as false
            return true
        }
        seen[x] = true
    }
    return false
}
```

### Template to memorize: the table-driven test

This is the standard test shape in Go. Each new case is one new row. Interviewers who know Go expect this shape.

```go
import "testing"

func TestContainsDuplicate(t *testing.T) {
    // One row for each case: a name, the input and the expected answer.
    tests := []struct {
        name string
        nums []int
        want bool
    }{
        {"has a duplicate", []int{1, 2, 3, 1}, true},
        {"all different", []int{1, 2, 3, 4}, false},
        {"empty", nil, false},
    }
    for _, tc := range tests {
        t.Run(tc.name, func(t *testing.T) {
            got := containsDuplicate(tc.nums)
            if got != tc.want {
                t.Errorf("containsDuplicate(%v) = %v, want %v", tc.nums, got, tc.want)
            }
        })
    }
}
```

> [!tip] Local tests first
> Use the examples from the problem statement as the first rows. Then add the edge cases: empty input, one item, all items equal, negative numbers.

## Stage 1: Slices and maps with arrays and hashing

**Why this pair:** almost every problem uses a slice, and the hash map is the most common tool to remove a nested loop.

Garden notes: [[wiki/patterns/arrays-and-hashing|Arrays and Hashing pattern]], [[wiki/dsa/arrays|Arrays]], [[wiki/dsa/hash-tables|Hash Tables]].

### Go you need

```go
func sliceAndMapBasics() {
    // --- Slices: the Go list ---
    nums := []int{3, 1, 2}   // a slice literal
    nums = append(nums, 5)   // append returns the slice: always assign the result
    n := len(nums)           // 4
    last := nums[n-1]        // 5 (there is no nums[-1] in Go)
    part := nums[1:3]        // [1 2]: start is included, end is not
    zeros := make([]int, n)  // [0 0 0 0]: length n, all zero values
    buf := make([]int, 0, n) // length 0, capacity n: ready for append

    for i, x := range nums { // index and value
        zeros[i] = x * 2
    }
    for i := range nums { // index only
        buf = append(buf, nums[i])
    }

    // --- Maps: the Go hash table ---
    count := map[string]int{} // an empty map (same as make(map[string]int))
    count["go"]++             // a missing key reads as 0, so ++ works
    v, ok := count["rust"]    // v = 0, ok = false: the "comma ok" form
    delete(count, "go")       // remove a key (no error if it is missing)

    set := map[int]struct{}{} // a set that uses no memory for values
    set[7] = struct{}{}
    _, inSet := set[7] // true

    for key, value := range count { // the order is random on each run
        fmt.Println(key, value)
    }

    // An array (fixed size) can be a map key. A slice cannot.
    byLetters := map[[26]int]string{}
    var key [26]int // 26 zeros
    key['c'-'a']++  // 'c' - 'a' = 2: the index of the letter c
    byLetters[key] = "c"

    fmt.Println(last, part, zeros, buf, v, ok, inSet, len(byLetters))
}
```

> [!warning] Mistakes in this stage
> - `append(nums, 5)` with no assignment does not compile. Write `nums = append(nums, 5)`.
> - A write to a `nil` map panics. `var m map[string]int` is `nil`. Use `make` or `map[string]int{}`.
> - `make([]int, n)` then `append` gives n zeros first, then your values. Use `make([]int, 0, n)` before `append`.

### Template to memorize

> [!tip] Signal
> The problem says count, duplicate, group, or "find a pair". A brute-force answer needs two nested loops over the same slice.

```go
// TEMPLATE A: count with a map. Ask: "how many times does each value appear?"
func countValues(nums []int) map[int]int {
    count := make(map[int]int, len(nums)) // the size hint avoids regrowth
    for _, x := range nums {
        count[x]++
    }
    return count
}

// TEMPLATE B: one pass with a "seen" map. Ask: "did I already see what I need?"
// twoSum solves LC 1. Time O(n), space O(n).
func twoSum(nums []int, target int) []int {
    seen := make(map[int]int, len(nums)) // value -> index of that value
    for i, x := range nums {
        need := target - x           // the partner that completes the pair
        if j, ok := seen[need]; ok { // was the partner seen before?
            return []int{j, i}
        }
        seen[x] = i // store x only after the check, so x is not its own partner
    }
    return nil // nil is a valid empty slice
}
```

> [!quote] Say it
> "I trade memory for time. One pass with a hash map gives O(n) time and O(n) space."

### Solved with comments

**LC 49, Group Anagrams.** The Go lesson: an array can be a map key, and `append` works on a missing key.

```go
// groupAnagrams solves LC 49. Time O(n * k) for n words of length k.
// Idea: two words are anagrams when their letter counts are equal.
// So the letter count is the map key.
func groupAnagrams(strs []string) [][]string {
    groups := make(map[[26]int][]string) // letter counts -> words with those counts
    for _, s := range strs {
        var key [26]int               // starts as 26 zeros
        for i := 0; i < len(s); i++ { // s[i] is a byte
            key[s[i]-'a']++ // 'a' -> 0, 'b' -> 1, and so on
        }
        // append works on a nil slice, so there is no "if key not in map".
        groups[key] = append(groups[key], s)
    }

    res := make([][]string, 0, len(groups)) // length 0, capacity = number of groups
    for _, g := range groups {
        res = append(res, g)
    }
    return res
}
```

**LC 238, Product of Array Except Self.** The Go lesson: `make` and the two loop directions.

```go
// productExceptSelf solves LC 238 with no division. Time O(n), extra space O(1).
// Idea: answer[i] = (product of all items to the left) * (product of all to the right).
func productExceptSelf(nums []int) []int {
    n := len(nums)
    res := make([]int, n)

    // Pass 1, left to right: res[i] = product of nums[0..i-1].
    left := 1
    for i := 0; i < n; i++ {
        res[i] = left
        left *= nums[i]
    }

    // Pass 2, right to left: multiply by the product of nums[i+1..n-1].
    right := 1
    for i := n - 1; i >= 0; i-- {
        res[i] *= right
        right *= nums[i]
    }
    return res
}
```

The garden also has a full note for [[sources/leetcode/2026-04-03-top-k-frequent-elements|LC 347, Top K Frequent Elements]].

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Map as a set (solved in stage 0) |
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | `[26]int` counter |
| [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | "Seen" map (template B) |
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Array as a map key (solved above) |
| [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Count map, then bucket sort |
| [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix and suffix passes (solved above) |
| [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Set, start only at the first number of a run |

## Stage 2: Strings with two pointers

**Why this pair:** two-pointer problems index into strings all the time. So you must know what `s[i]` is in Go.

Garden notes: [[wiki/patterns/two-pointers|Two Pointers pattern]], [[sources/leetcode/2026-04-04-longest-palindromic-substring|LC 5 solved]].

### Go you need

```go
func stringBasics() {
    s := "héllo"
    fmt.Println(len(s)) // 6, not 5: len counts bytes, and é uses 2 bytes
    fmt.Println(s[0])   // 104: s[i] is a byte (a number), not a string

    // A string cannot change. Convert it to change it.
    b := []byte("hello") // a copy that you can change (ASCII input)
    b[0] = 'j'           // single quotes: one byte or rune. Double quotes: a string
    t := string(b)       // "jello"

    for i, r := range s { // range gives runes (full characters) and byte offsets
        fmt.Println(i, string(r), unicode.IsLetter(r))
    }
    runes := []rune(s)      // use this when the input is not ASCII
    fmt.Println(len(runes)) // 5

    // Build a string in a loop with strings.Builder. s += x in a loop is O(n²).
    var sb strings.Builder
    sb.WriteByte('a')
    sb.WriteString("bc")
    built := sb.String() // "abc"

    // Character arithmetic.
    digit := int('7' - '0') // 7: the value of a digit character
    index := int('d' - 'a') // 3: the position of a letter

    // Numbers and text.
    text := strconv.Itoa(42)       // "42"
    num, err := strconv.Atoi("42") // 42, nil

    words := strings.Fields(" go is  fun ") // [go is fun]: split on spaces
    sub := s[0:1]                           // "h": a substring by byte index
    fmt.Println(t, built, digit, index, text, num, err, words, sub)
}
```

> [!warning] Mistakes in this stage
> - `s[i]` is a `byte`, not a string. `string(s[i])` converts it.
> - `"a"` is a string and `'a'` is a rune. `s[i] == "a"` does not compile.
> - LeetCode strings are almost always ASCII. Then bytes are safe and fast. Use `[]rune` only when the problem says Unicode.

### Template to memorize

> [!tip] Signal
> The input is sorted, or the problem is about a palindrome or a pair. You compare items from the two ends.

```go
// TEMPLATE: converging pointers on a sorted slice.
// twoSumSorted solves LC 167. Time O(n), space O(1).
func twoSumSorted(numbers []int, target int) []int {
    l, r := 0, len(numbers)-1 // one pointer at each end
    for l < r {               // Go has no "while": a for with one condition does it
        sum := numbers[l] + numbers[r]
        switch { // a switch with no value works as an if / else if chain
        case sum == target:
            return []int{l + 1, r + 1} // LC 167 wants 1-based indexes
        case sum < target:
            l++ // the sum is too small: only a larger left value can help
        default:
            r-- // the sum is too large: only a smaller right value can help
        }
    }
    return nil
}
```

The moves are START at the two ends, COMPARE, and MOVE the pointer that can improve the result.

> [!quote] Say it
> "The array is sorted, so I use two pointers. Each step removes one candidate, so the time is O(n)."

### Solved with comments

**LC 125, Valid Palindrome.** The Go lesson: byte comparisons and small helper functions.

```go
// isPalindrome solves LC 125. Time O(n), space O(1).
// Compare letters and digits only, and ignore case.
func isPalindrome(s string) bool {
    l, r := 0, len(s)-1
    for l < r {
        // Skip the characters that do not count.
        for l < r && !isAlnum(s[l]) {
            l++
        }
        for l < r && !isAlnum(s[r]) {
            r--
        }
        if toLower(s[l]) != toLower(s[r]) {
            return false
        }
        l++ // Go has no "l++, r--" on one line with a comma
        r--
    }
    return true
}

// isAlnum reports whether c is an ASCII letter or digit.
func isAlnum(c byte) bool {
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')
}

// toLower changes an ASCII upper-case letter to lower case.
func toLower(c byte) byte {
    if c >= 'A' && c <= 'Z' {
        return c + ('a' - 'A') // the distance between the two cases is 32
    }
    return c
}
```

**LC 15, 3Sum.** The Go lesson: `sort.Ints`, a `switch` with no value, and `continue`.

```go
// threeSum solves LC 15. Time O(n²), space O(1) plus the sort.
// Idea: sort, fix one number, then run converging pointers on the rest.
func threeSum(nums []int) [][]int {
    sort.Ints(nums) // sorts in place, ascending
    var res [][]int // a nil slice: append works on it

    for i := 0; i < len(nums)-2; i++ {
        if i > 0 && nums[i] == nums[i-1] {
            continue // same first number as before: it gives duplicate triplets
        }
        if nums[i] > 0 {
            break // the smallest number is positive, so no sum can be 0
        }

        l, r := i+1, len(nums)-1
        for l < r {
            sum := nums[i] + nums[l] + nums[r]
            switch {
            case sum < 0:
                l++
            case sum > 0:
                r--
            default:
                res = append(res, []int{nums[i], nums[l], nums[r]})
                l++
                r--
                // Skip equal values, so the same triplet is not added again.
                for l < r && nums[l] == nums[l-1] {
                    l++
                }
                for l < r && nums[r] == nums[r+1] {
                    r--
                }
            }
        }
    }
    return res
}
```

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [344. Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | Swap with `s[l], s[r] = s[r], s[l]` |
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Converging pointers (solved above) |
| [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | The template |
| [15. 3Sum](https://leetcode.com/problems/3sum/) | Medium | Sort, then the template (solved above) |
| [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Move the shorter side |
| [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | Expand from the center |

## Stage 3: Loops with the sliding window

**Why this pair:** a sliding window is two loops that share one index pair. It is the best practice for the `for` forms.

### Go you need

```go
func loopBasics() {
    // Go has one loop keyword. It has four forms.
    for i := 0; i < 3; i++ { // 1. the classic form
    }
    n := 3
    for n > 0 { // 2. the "while" form
        n--
    }
    for { // 3. the endless form: leave with break or return
        break
    }
    for i := range 3 { // 4. range over an integer (Go 1.22+): 0, 1, 2
        _ = i
    }

    // min and max are built in from Go 1.21. They take two or more values.
    best := max(3, 7)     // 7
    small := min(4, 2, 9) // 2

    // A fixed array as a counter is faster than a map for bytes.
    var count [128]int // one counter for each ASCII character, all zero
    count['a']++

    // Two arrays are equal when all their items are equal. Slices have no ==.
    var a, b [26]int
    same := a == b // true

    fmt.Println(best, small, count['a'], same)
}
```

### Template to memorize

> [!tip] Signal
> The problem asks for the longest, shortest or best **contiguous** part of a slice or string, with a condition.

```go
// TEMPLATE: window of variable size.
// lengthOfLongestSubstring solves LC 3. Time O(n), space O(1).
func lengthOfLongestSubstring(s string) int {
    var count [128]int // count of each character inside the window
    best, left := 0, 0 // the window is s[left..right]
    for right := 0; right < len(s); right++ {
        count[s[right]]++ // 1. GROW: take s[right] into the window

        for count[s[right]] > 1 { // 2. SHRINK while the window is not valid
            count[s[left]]--
            left++
        }

        best = max(best, right-left+1) // 3. RECORD: the window is valid here
    }
    return best
}
```

The moves are GROW, SHRINK, RECORD. For a "shortest" problem, record inside the shrink loop, while the window is still valid.

> [!quote] Say it
> "Each index enters the window one time and leaves one time. So the time is O(n), not O(n²)."

### Solved with comments

**LC 567, Permutation in String.** This window has a fixed size. The Go lesson: arrays compare with `==`.

```go
// checkInclusion solves LC 567. Time O(n), space O(1).
// Problem: does s2 contain a permutation of s1?
// Idea: a window of fixed size len(s1) slides on s2. Compare letter counts.
func checkInclusion(s1 string, s2 string) bool {
    if len(s1) > len(s2) {
        return false
    }
    var need, have [26]int // letter counts of s1 and of the window
    for i := 0; i < len(s1); i++ {
        need[s1[i]-'a']++
        have[s2[i]-'a']++ // the first window is s2[0..len(s1)-1]
    }
    if need == have { // arrays compare with ==
        return true
    }
    for right := len(s1); right < len(s2); right++ {
        have[s2[right]-'a']++         // one letter enters on the right
        have[s2[right-len(s1)]-'a']-- // one letter leaves on the left
        if need == have {
            return true
        }
    }
    return false
}
```

**LC 424, Longest Repeating Character Replacement.** The same template with a different "valid" rule.

```go
// characterReplacement solves LC 424. Time O(n), space O(1).
// Problem: longest substring of one letter, with at most k replacements.
// Idea: a window is valid when (size - count of its most frequent letter) <= k.
func characterReplacement(s string, k int) int {
    var count [26]int
    best, left, maxFreq := 0, 0, 0
    for right := 0; right < len(s); right++ {
        count[s[right]-'A']++
        maxFreq = max(maxFreq, count[s[right]-'A']) // best frequency seen so far

        // The letters to replace are the ones that are not the top letter.
        for (right-left+1)-maxFreq > k {
            count[s[left]-'A']--
            left++
        }
        best = max(best, right-left+1)
    }
    return best
}
```

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | One pass, keep the minimum so far |
| [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | The template |
| [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | A "shortest" window |
| [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | Fixed window (solved above) |
| [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | A different "valid" rule (solved above) |
| [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Two counters and a "shortest" window |

## Stage 4: Slices as a stack

**Why this pair:** Go has no stack type. You build the stack from a slice, so you practice `append` and slice expressions.

Garden notes: [[wiki/patterns/stack-based|Stack-Based pattern]], [[wiki/dsa/stacks|Stacks]], [[sources/leetcode/2026-04-04-valid-parentheses|LC 20 solved]].

### Go you need

```go
func stackAndQueueBasics() {
    // A slice is the stack. Go has no Stack type.
    stack := []int{}
    stack = append(stack, 4)     // push
    stack = append(stack, 9)     // push
    top := stack[len(stack)-1]   // peek: 9
    stack = stack[:len(stack)-1] // pop: cut the last item off
    empty := len(stack) == 0     // false

    // A slice is also the queue.
    queue := []int{1, 2, 3}
    front := queue[0] // peek
    queue = queue[1:] // dequeue
    queue = append(queue, 4)

    // A stack of pairs: use a small struct, or a [2]int array.
    type pair struct{ val, idx int }
    pairs := []pair{{val: 5, idx: 0}}

    fmt.Println(top, empty, front, queue, pairs[0].val)
}
```

> [!warning] Mistakes in this stage
> - Check `len(stack) > 0` before you read the top. An index on an empty slice panics.
> - Put the length check first in the condition. `&&` stops at the first false part.

### Template to memorize

> [!tip] Signal
> The problem asks for the next greater or next smaller item. Or the most recent open item must close first, as with brackets.

```go
// TEMPLATE: monotonic stack. The stack keeps indexes that wait for an answer.
// dailyTemperatures solves LC 739. Time O(n), space O(n).
// Problem: for each day, how many days until a warmer day?
func dailyTemperatures(temperatures []int) []int {
    res := make([]int, len(temperatures)) // zeros: 0 means "no warmer day"
    stack := []int{}                      // indexes of days with no answer yet

    for i, t := range temperatures {
        // Today is warmer than the day on top of the stack: that day has its answer.
        for len(stack) > 0 && t > temperatures[stack[len(stack)-1]] {
            j := stack[len(stack)-1]     // peek
            stack = stack[:len(stack)-1] // pop
            res[j] = i - j               // days waited
        }
        stack = append(stack, i) // today waits for its warmer day
    }
    return res
}
```

The moves are: while the new item beats the top, POP and ANSWER. Then PUSH the new index.

> [!quote] Say it
> "Each index is pushed one time and popped one time. So the two loops together are O(n)."

### Solved with comments

**LC 150, Evaluate Reverse Polish Notation.** The Go lesson: `switch` on a string and `strconv.Atoi`.

```go
// evalRPN solves LC 150. Time O(n), space O(n).
// Idea: push numbers. On an operator, pop two numbers and push the result.
func evalRPN(tokens []string) int {
    stack := []int{}
    for _, tok := range tokens {
        switch tok { // no "break" is necessary: a Go case does not fall through
        case "+", "-", "*", "/": // one case can list many values
            b := stack[len(stack)-1] // the right operand is on top
            a := stack[len(stack)-2] // the left operand is below it
            stack = stack[:len(stack)-2]
            switch tok {
            case "+":
                stack = append(stack, a+b)
            case "-":
                stack = append(stack, a-b)
            case "*":
                stack = append(stack, a*b)
            case "/":
                stack = append(stack, a/b) // int division truncates toward zero
            }
        default:
            n, _ := strconv.Atoi(tok) // LC guarantees valid numbers, so drop the error
            stack = append(stack, n)
        }
    }
    return stack[0]
}
```

**LC 155, Min Stack.** The Go lesson: a struct with methods. This is how you write a class in Go.

```go
// MinStack solves LC 155. Every operation is O(1).
// Idea: each item stores the minimum of the stack at the time of its push.
type MinStack struct {
    items []minItem
}

type minItem struct {
    val, min int
}

// NewMinStack is the constructor. On LeetCode its name is Constructor.
func NewMinStack() MinStack {
    return MinStack{}
}

// The receiver is a pointer (*MinStack), because Push changes the stack.
func (s *MinStack) Push(val int) {
    m := val
    if len(s.items) > 0 {
        m = min(m, s.items[len(s.items)-1].min)
    }
    s.items = append(s.items, minItem{val: val, min: m})
}

func (s *MinStack) Pop()        { s.items = s.items[:len(s.items)-1] }
func (s *MinStack) Top() int    { return s.items[len(s.items)-1].val }
func (s *MinStack) GetMin() int { return s.items[len(s.items)-1].min }
```

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Stack of bytes, map of pairs |
| [155. Min Stack](https://leetcode.com/problems/min-stack/) | Medium | Struct and methods (solved above) |
| [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | `switch`, `strconv` (solved above) |
| [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | The template |
| [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | Preview of backtracking |
| [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Monotonic stack with widths |

## Stage 5: The sort package with binary search

**Why this pair:** the two topics need function values. You give a function to `sort.Slice`, and binary search on the answer is a search on a function.

Garden notes: [[wiki/dsa/binary-search|Binary Search]], [[wiki/dsa/sorting|Sorting]].

### Go you need

```go
func sortBasics() {
    nums := []int{3, 1, 2}
    sort.Ints(nums) // [1 2 3], in place
    names := []string{"b", "a"}
    sort.Strings(names) // [a b]

    // Custom order: give a "less" function. i and j are indexes.
    people := [][]int{{30, 1}, {25, 2}}
    sort.Slice(people, func(i, j int) bool {
        return people[i][0] < people[j][0] // ascending by the first value
    })

    // The newer package (Go 1.21+). The function gets values, not indexes.
    slices.Sort(nums)
    slices.SortFunc(people, func(a, b []int) int {
        return cmp.Compare(b[0], a[0]) // b before a: descending
    })

    // Binary search from the standard library.
    i := sort.SearchInts(nums, 2) // 1: the first index with nums[i] >= 2
    // sort.Search finds the first index in [0, n) where the function is true.
    j := sort.Search(len(nums), func(k int) bool { return nums[k] >= 3 }) // 2

    fmt.Println(nums, names, people, i, j)
}
```

### Template to memorize

> [!tip] Signal
> The input is sorted, or the problem wants O(log n). Or the problem asks for the minimum value that is "enough", and a check function is easy to write.

```go
// TEMPLATE A: find an exact value. The range [lo, hi] includes both ends.
// search solves LC 704. Time O(log n).
func search(nums []int, target int) int {
    lo, hi := 0, len(nums)-1
    for lo <= hi { // <= because a range of one item is still a candidate
        mid := lo + (hi-lo)/2 // the same as (lo+hi)/2, but it cannot overflow
        switch {
        case nums[mid] == target:
            return mid
        case nums[mid] < target:
            lo = mid + 1 // the target is on the right
        default:
            hi = mid - 1 // the target is on the left
        }
    }
    return -1
}

// TEMPLATE B: find the first index where a condition becomes true.
// The answer is in [lo, hi]. hi = len(nums) means "no index".
// lowerBound returns the first index with nums[i] >= target (LC 35).
func lowerBound(nums []int, target int) int {
    lo, hi := 0, len(nums)
    for lo < hi { // stop when the range has one candidate
        mid := lo + (hi-lo)/2
        if nums[mid] >= target {
            hi = mid // mid can be the answer: keep it
        } else {
            lo = mid + 1 // mid is not the answer: drop it
        }
    }
    return lo
}
```

The two templates are different in three places: the start value of `hi`, the loop condition, and the update of `hi`. Memorize them as two separate sets. A mix of the two causes an endless loop.

| | Template A: exact value | Template B: first true |
|---|---|---|
| Start | `hi = len(nums) - 1` | `hi = len(nums)` |
| Loop | `lo <= hi` | `lo < hi` |
| Go left | `hi = mid - 1` | `hi = mid` |
| Go right | `lo = mid + 1` | `lo = mid + 1` |
| Result | `mid`, or -1 | `lo` |

> [!quote] Say it
> "The condition is false, false, then true, true. So I can binary search for the first true."

### Solved with comments

**LC 875, Koko Eating Bananas.** This is binary search on the answer, with template B.

```go
// minEatingSpeed solves LC 875. Time O(n log m), m = the largest pile.
// Idea: binary search on the ANSWER (the speed), not on the slice.
// If speed k is fast enough, each speed above k is also fast enough.
// So the problem is "the first speed that is fast enough": template B.
func minEatingSpeed(piles []int, h int) int {
    lo, hi := 1, slices.Max(piles) // the slowest and the fastest useful speed
    for lo < hi {
        mid := lo + (hi-lo)/2
        if hoursNeeded(piles, mid) <= h {
            hi = mid // fast enough: try a slower speed, but keep mid
        } else {
            lo = mid + 1 // too slow
        }
    }
    return lo
}

// hoursNeeded returns the hours to eat all piles at the given speed.
func hoursNeeded(piles []int, speed int) int {
    hours := 0
    for _, p := range piles {
        hours += (p + speed - 1) / speed // integer ceiling of p / speed
    }
    return hours
}
```

**LC 153, Find Minimum in Rotated Sorted Array.** Template B again, with a different condition.

```go
// findMin solves LC 153. Time O(log n).
// Idea: compare mid with the right end to know which half holds the minimum.
func findMin(nums []int) int {
    lo, hi := 0, len(nums)-1
    for lo < hi {
        mid := lo + (hi-lo)/2
        if nums[mid] > nums[hi] {
            lo = mid + 1 // the drop is to the right of mid
        } else {
            hi = mid // mid can be the minimum
        }
    }
    return nums[lo]
}
```

**LC 56, Merge Intervals.** The Go lesson: `sort.Slice`, and a slice value that points to shared data.

```go
// merge solves LC 56. Time O(n log n) for the sort.
// Idea: sort by start. Then each interval overlaps the last result or starts a new one.
func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })

    res := [][]int{intervals[0]}
    for _, cur := range intervals[1:] { // each interval after the first
        last := res[len(res)-1] // a slice header: it points to the same data
        if cur[0] <= last[1] {  // overlap: cur starts before last ends
            last[1] = max(last[1], cur[1]) // this write changes res too
        } else {
            res = append(res, cur)
        }
    }
    return res
}
```

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Template A |
| [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Template B |
| [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | Index arithmetic: `mid / cols`, `mid % cols` |
| [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Search on the answer (solved above) |
| [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Compare with the right end (solved above) |
| [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Find the sorted half first |
| [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | `sort.Slice` (solved above) |
| [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Sort by end, greedy |

## Stage 6: Pointers with linked lists

**Why this pair:** a linked list is the smallest program that needs pointers. If you can reverse a list, you understand pointers in Go.

### Go you need

```go
// ListNode is the type that LeetCode gives you. Do not paste it in your answer.
type ListNode struct {
    Val  int
    Next *ListNode // a pointer to the next node, or nil at the end
}

func pointerBasics() {
    // &T{...} makes a value and returns a pointer to it.
    c := &ListNode{Val: 3}
    b := &ListNode{Val: 2, Next: c}
    a := &ListNode{Val: 1, Next: b} // 1 -> 2 -> 3

    // Go follows the pointer for you: a.Val, not a->Val or (*a).Val.
    fmt.Println(a.Val, a.Next.Val)

    // Walk a list.
    for cur := a; cur != nil; cur = cur.Next {
        fmt.Println(cur.Val)
    }

    // var gives the zero value. The zero value of a pointer is nil.
    var prev *ListNode
    fmt.Println(prev == nil) // true. prev.Val here causes a panic.

    // Multiple assignment: the right side is evaluated first, then assigned.
    x, y := 1, 2
    x, y = y, x // swap with no temporary variable
    fmt.Println(x, y)
}
```

> [!warning] Mistakes in this stage
> - A read of `node.Next` when `node` is `nil` panics. Check `node != nil` first.
> - In the reverse template, save `cur.Next` before you change it. If you do not, the rest of the list is lost.

### Template to memorize

> [!tip] Signal
> The input is a `*ListNode`. Three templates solve almost every list problem: reverse, dummy head, and fast and slow pointers.

```go
// TEMPLATE A: reverse the pointers one node at a time.
// reverseList solves LC 206. Time O(n), space O(1).
func reverseList(head *ListNode) *ListNode {
    var prev *ListNode // nil: the new tail points to nothing
    cur := head
    for cur != nil {
        next := cur.Next // 1. save the rest of the list
        cur.Next = prev  // 2. turn the pointer back
        prev = cur       // 3. move prev forward
        cur = next       // 4. move cur forward
    }
    return prev // cur is nil, so prev is the new head
}
```

```go
// TEMPLATE B: dummy head. It removes the special case for the first node.
// mergeTwoLists solves LC 21. Time O(n + m), space O(1).
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    dummy := &ListNode{} // a node with no meaning, before the real head
    tail := dummy        // the last node of the result
    for list1 != nil && list2 != nil {
        if list1.Val <= list2.Val {
            tail.Next = list1
            list1 = list1.Next
        } else {
            tail.Next = list2
            list2 = list2.Next
        }
        tail = tail.Next
    }
    // One list is empty. Attach the rest of the other list.
    if list1 != nil {
        tail.Next = list1
    } else {
        tail.Next = list2
    }
    return dummy.Next // the real head
}
```

```go
// TEMPLATE C: fast and slow pointers.
// hasCycle solves LC 141. Time O(n), space O(1).
func hasCycle(head *ListNode) bool {
    slow, fast := head, head
    for fast != nil && fast.Next != nil { // check both, or fast.Next.Next panics
        slow = slow.Next      // one step
        fast = fast.Next.Next // two steps
        if slow == fast {     // pointers compare by address: the same node
            return true
        }
    }
    return false // fast reached the end, so there is no cycle
}
```

The moves of the reverse template are SAVE, TURN, MOVE, MOVE. Draw three boxes on paper and follow the four lines one time.

> [!quote] Say it
> "I use a dummy head, so the first node needs no special case."

### Solved with comments

**LC 19, Remove Nth Node From End of List.** It uses two of the templates together: the dummy head, and two pointers with a gap.

```go
// removeNthFromEnd solves LC 19 in one pass. Time O(n), space O(1).
// Idea: keep a gap of n nodes between two pointers. Use a dummy head,
// because the node to remove can be the head.
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{Next: head}
    slow, fast := dummy, dummy
    for i := 0; i < n; i++ { // move fast n nodes ahead
        fast = fast.Next
    }
    for fast.Next != nil { // move both until fast is the last node
        slow = slow.Next
        fast = fast.Next
    }
    slow.Next = slow.Next.Next // slow is before the target: skip the target
    return dummy.Next
}
```

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Template A |
| [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Template B |
| [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Template C |
| [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | Template C, return `slow` |
| [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Dummy head and a gap (solved above) |
| [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | Dummy head and a carry |
| [143. Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | All three templates in one problem |

## Stage 7: Recursion and closures with trees

**Why this pair:** tree problems are recursive. In Go, the cleanest recursive helper is a closure that keeps the result in an outer variable.

### Go you need

```go
// TreeNode is the type that LeetCode gives you.
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

func closureBasics() {
    // A function can return two or more values.
    divmod := func(a, b int) (int, int) { return a / b, a % b }
    q, r := divmod(7, 2) // 3, 1

    // A closure is a function value that can read and change outer variables.
    total := 0
    add := func(x int) { total += x }
    add(5)

    // A closure that calls itself: declare the variable first, then assign.
    var fact func(n int) int
    fact = func(n int) int {
        if n <= 1 {
            return 1
        }
        return n * fact(n-1) // fact is already declared, so this compiles
    }

    fmt.Println(q, r, total, fact(5), math.MaxInt, math.MinInt)
}
```

> [!warning] Mistakes in this stage
> - `dfs := func(...) { dfs(...) }` does not compile. Declare `var dfs func(...)` first, then assign with `=`.
> - A queue of `*TreeNode` must not contain `nil`. Check the child before you append it.

### Template to memorize

> [!tip] Signal
> For depth, height, path or "is it valid", use DFS. For levels, or the shortest number of steps, use BFS.

```go
// TEMPLATE A: recursive DFS. Ask the children, then combine their answers.
// maxDepth solves LC 104. Time O(n), space O(height).
func maxDepth(root *TreeNode) int {
    if root == nil { // base case: an empty tree has depth 0
        return 0
    }
    left := maxDepth(root.Left)   // the answer for the left subtree
    right := maxDepth(root.Right) // the answer for the right subtree
    return 1 + max(left, right)   // this node adds one level
}
```

```go
// TEMPLATE B: BFS level by level, with a slice as the queue.
// levelOrder solves LC 102. Time O(n), space O(n).
func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return nil
    }
    var res [][]int
    queue := []*TreeNode{root}
    for len(queue) > 0 {
        size := len(queue) // the number of nodes in this level
        level := make([]int, 0, size)
        for i := 0; i < size; i++ { // take exactly one level out
            node := queue[0]
            queue = queue[1:]
            level = append(level, node.Val)
            if node.Left != nil {
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

The DFS moves are BASE CASE, ASK LEFT, ASK RIGHT, COMBINE. The BFS moves are TAKE THE SIZE, EMPTY ONE LEVEL, ADD THE CHILDREN.

> [!quote] Say it
> "I trust the recursion. I decide what one node does with the answers from its two children."

### Solved with comments

**LC 543, Diameter of Binary Tree.** The DFS returns one value and records a different one. This shape solves many "best path" problems.

```go
// diameterOfBinaryTree solves LC 543. Time O(n), space O(height).
// Idea: the longest path through a node = left height + right height.
// The DFS returns the height, and a closure records the best path.
func diameterOfBinaryTree(root *TreeNode) int {
    best := 0
    var height func(node *TreeNode) int
    height = func(node *TreeNode) int {
        if node == nil {
            return 0
        }
        l := height(node.Left)
        r := height(node.Right)
        best = max(best, l+r) // the closure changes the outer variable
        return 1 + max(l, r)  // the parent gets the height
    }
    height(root)
    return best
}
```

**LC 98, Validate Binary Search Tree.** The DFS passes limits down the tree.

```go
// isValidBST solves LC 98. Time O(n), space O(height).
// Idea: each node must be inside a range (lo, hi) that its ancestors set.
// A common wrong answer compares a node with its two children only.
func isValidBST(root *TreeNode) bool {
    var valid func(node *TreeNode, lo, hi int) bool
    valid = func(node *TreeNode, lo, hi int) bool {
        if node == nil {
            return true
        }
        if node.Val <= lo || node.Val >= hi {
            return false
        }
        // Go left: this value is the new upper limit. Go right: the new lower limit.
        return valid(node.Left, lo, node.Val) && valid(node.Right, node.Val, hi)
    }
    // int is 64 bits on LeetCode, so these limits are outside the int32 input range.
    return valid(root, math.MinInt, math.MaxInt)
}
```

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | DFS and a swap |
| [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Template A |
| [100. Same Tree](https://leetcode.com/problems/same-tree/) | Easy | DFS on two trees |
| [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | Closure that records the best (solved above) |
| [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | Template B |
| [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | Template B, keep the last of each level |
| [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | Limits passed down (solved above) |
| [235. Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | Use the BST order |

## Stage 8: Interfaces with the heap

**Why this pair:** Go has no ready priority queue. You write five methods to satisfy `heap.Interface`. This is the best small lesson on Go interfaces.

Garden notes: [[wiki/patterns/top-k|Top-K Elements pattern]], [[wiki/go/leetcode-snippets|Go LeetCode Snippets]].

### Go you need

- An **interface** is a list of methods. A type satisfies it when the type has those methods.
- A **value receiver** `(h IntHeap)` gets a copy of the slice header. It can read and swap items.
- A **pointer receiver** `(h *IntHeap)` can change the length. `Push` and `Pop` need it.
- `any` is the empty interface. It can hold a value of each type.
- `x.(int)` is a **type assertion**. It gets the `int` back from an `any` value.

### Template to memorize

> [!tip] Signal
> The problem asks for the K largest, K smallest or K closest items. Or you need the minimum again and again while the data changes.

```go
// TEMPLATE: a min-heap of ints. Write these five methods from memory.
// A type satisfies an interface when it has the methods. There is no "implements".
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] } // change to > for a max-heap
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// Push and Pop change the length of the slice, so the receiver is a pointer.
func (h *IntHeap) Push(x any) { *h = append(*h, x.(int)) } // x.(int): any -> int

func (h *IntHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]  // the heap package moves the minimum to the end first
    *h = old[:n-1] // cut it off
    return x
}
```

Memorize the five methods in this order: `Len`, `Less`, `Swap`, `Push`, `Pop`. Only `Less` and the item type change between problems.

> [!warning] Mistakes in this stage
> - Call `heap.Push(h, x)` and `heap.Pop(h)`. The methods `h.Push` and `h.Pop` do not keep the heap order.
> - The K **largest** items need a **min**-heap of size K. The root is the smallest of the top K, so it leaves first.

> [!quote] Say it
> "A heap of size K gives O(n log K). That is better than a full sort when K is small."

### Solved with comments

**LC 215, Kth Largest Element in an Array.**

```go
// findKthLargest solves LC 215. Time O(n log k), space O(k).
// Idea: keep a min-heap with the k largest values seen so far.
// Its minimum (the root) is the k-th largest.
func findKthLargest(nums []int, k int) int {
    h := &IntHeap{} // a pointer, because Push and Pop need *IntHeap
    for _, x := range nums {
        heap.Push(h, x) // call heap.Push(h, x), not h.Push(x)
        if h.Len() > k {
            heap.Pop(h) // drop the smallest: it cannot be in the top k
        }
    }
    return (*h)[0] // the root is at index 0
}
```

**LC 973, K Closest Points to Origin.** The same template, with a different item type and a max-heap.

```go
// kClosest solves LC 973. Time O(n log k), space O(k).
// Idea: a MAX-heap of size k by distance. Remove the farthest point when it grows.
type PointHeap [][]int

func dist(p []int) int { return p[0]*p[0] + p[1]*p[1] } // no square root is necessary

func (h PointHeap) Len() int           { return len(h) }
func (h PointHeap) Less(i, j int) bool { return dist(h[i]) > dist(h[j]) } // > makes a max-heap
func (h PointHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *PointHeap) Push(x any)        { *h = append(*h, x.([]int)) }
func (h *PointHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func kClosest(points [][]int, k int) [][]int {
    h := &PointHeap{}
    for _, p := range points {
        heap.Push(h, p)
        if h.Len() > k {
            heap.Pop(h) // removes the farthest point
        }
    }
    return *h // the k points that stay (any order is accepted)
}
```

**LC 23, Merge k Sorted Lists.** A heap of pointers. It reuses the dummy head from stage 6.

```go
// mergeKLists solves LC 23. Time O(n log k) for n nodes in k lists.
// Idea: a min-heap holds the current head of each list.
// Pop the smallest node, attach it, and push its next node.
type NodeHeap []*ListNode

func (h NodeHeap) Len() int           { return len(h) }
func (h NodeHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h NodeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *NodeHeap) Push(x any)        { *h = append(*h, x.(*ListNode)) }
func (h *NodeHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func mergeKLists(lists []*ListNode) *ListNode {
    h := &NodeHeap{}
    for _, l := range lists {
        if l != nil { // an empty list has no head to push
            heap.Push(h, l)
        }
    }
    dummy := &ListNode{}
    tail := dummy
    for h.Len() > 0 {
        node := heap.Pop(h).(*ListNode) // Pop returns any: assert the type
        tail.Next = node
        tail = node
        if node.Next != nil {
            heap.Push(h, node.Next)
        }
    }
    return dummy.Next
}
```

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | The template inside a struct |
| [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | Max-heap |
| [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Min-heap of size K (solved above) |
| [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | Custom `Less` (solved above) |
| [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Count map, then a heap |
| [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Heap of nodes (solved above) |

## Stage 9: Slice copies with backtracking

**Why this pair:** backtracking changes one slice all the time. If you save that slice with no copy, each saved result changes later. This is the most common Go bug in interviews.

### Go you need

```go
func aliasGotcha() {
    // Two slices can share one backing array.
    path := make([]int, 0, 4)
    path = append(path, 1, 2)

    saved := path      // NOT a copy: the same backing array
    path[0] = 99       // this write changes saved too
    fmt.Println(saved) // [99 2]

    // Three ways to make a real copy.
    c1 := append([]int(nil), path...) // append to a nil slice
    c2 := slices.Clone(path)          // Go 1.21+
    c3 := make([]int, len(path))
    copy(c3, path)

    path[0] = 1
    fmt.Println(c1, c2, c3) // all still [99 2]

    // x... spreads a slice into separate arguments.
    path = append(path, c1...)
    fmt.Println(path)
}
```

### Template to memorize

> [!tip] Signal
> The problem says "all subsets", "all permutations", "all combinations" or "each possible". The input is small, for example n ≤ 20.

```go
// TEMPLATE: backtracking = choose, explore, undo.
// subsets solves LC 78. Time O(n * 2^n).
func subsets(nums []int) [][]int {
    var res [][]int
    path := []int{} // the choices made so far

    var backtrack func(start int)
    backtrack = func(start int) {
        // Each path is one answer. Save a COPY: path changes later.
        res = append(res, slices.Clone(path))

        for i := start; i < len(nums); i++ {
            path = append(path, nums[i]) // 1. choose
            backtrack(i + 1)             // 2. explore (i + 1: do not reuse nums[i])
            path = path[:len(path)-1]    // 3. undo
        }
    }
    backtrack(0)
    return res
}
```

The moves are CHOOSE, EXPLORE, UNDO. The undo line is always the opposite of the choose line.

> [!quote] Say it
> "I build one path, and I undo each choice when I go back. I copy the path when I save it."

### Solved with comments

**LC 46, Permutations.** The change from the template: a `used` slice, because order matters.

```go
// permute solves LC 46. Time O(n * n!).
// Difference from subsets: order matters, so each level can take any unused number.
func permute(nums []int) [][]int {
    var res [][]int
    path := make([]int, 0, len(nums))
    used := make([]bool, len(nums)) // used[i]: nums[i] is in the path

    var backtrack func()
    backtrack = func() {
        if len(path) == len(nums) { // base case: a full permutation
            res = append(res, slices.Clone(path))
            return
        }
        for i := range nums {
            if used[i] {
                continue
            }
            used[i] = true // choose
            path = append(path, nums[i])
            backtrack() // explore
            path = path[:len(path)-1]
            used[i] = false // undo
        }
    }
    backtrack()
    return res
}
```

**LC 39, Combination Sum.** The change from the template: recurse with `i`, so a number can repeat.

```go
// combinationSum solves LC 39.
// Difference from subsets: a number can be used again, so recurse with i, not i + 1.
func combinationSum(candidates []int, target int) [][]int {
    var res [][]int
    path := []int{}

    var backtrack func(start, remain int)
    backtrack = func(start, remain int) {
        if remain == 0 { // the path adds up to the target
            res = append(res, slices.Clone(path))
            return
        }
        for i := start; i < len(candidates); i++ {
            if candidates[i] > remain {
                continue // prune: this number is too large
            }
            path = append(path, candidates[i])
            backtrack(i, remain-candidates[i]) // i again: reuse is permitted
            path = path[:len(path)-1]
        }
    }
    backtrack(0, target)
    return res
}
```

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [78. Subsets](https://leetcode.com/problems/subsets/) | Medium | The template |
| [46. Permutations](https://leetcode.com/problems/permutations/) | Medium | `used` slice (solved above) |
| [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | Reuse and pruning (solved above) |
| [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | A `[]byte` path |
| [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | Choose only valid moves |
| [79. Word Search](https://leetcode.com/problems/word-search/) | Medium | Backtracking on a grid |

## Stage 10: Grids and graphs

**Why this pair:** graph problems need 2D slices, small fixed arrays and slices of slices. It is the stage with the most Go data shapes.

### Go you need

```go
func gridAndGraphBasics() {
    // A grid is a slice of slices. Make each row separately.
    rows, cols := 2, 3
    grid := make([][]int, rows)
    for r := range grid {
        grid[r] = make([]int, cols)
    }

    // The four directions as a slice of fixed arrays.
    dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    r, c := 0, 0
    for _, d := range dirs {
        nr, nc := r+d[0], c+d[1]
        if nr < 0 || nr >= rows || nc < 0 || nc >= cols {
            continue // outside the grid
        }
        grid[nr][nc] = 1
    }

    // A graph as an adjacency list: adj[a] holds the neighbors of a.
    n := 4
    edges := [][]int{{0, 1}, {1, 2}}
    adj := make([][]int, n)
    for _, e := range edges {
        adj[e[0]] = append(adj[e[0]], e[1])
        adj[e[1]] = append(adj[e[1]], e[0]) // remove this line for a directed graph
    }

    // A queue of cells for BFS.
    queue := [][2]int{{0, 0}}
    cell := queue[0]
    fmt.Println(grid, adj, cell[0], cell[1])
}
```

### Template to memorize

> [!tip] Signal
> A grid of cells, or "n nodes and a list of edges". Connected groups need DFS. The fewest steps need BFS. An order with dependencies needs topological sort.

```go
// TEMPLATE A: DFS on a grid. Mark a cell when you visit it.
// numIslands solves LC 200. Time O(rows * cols).
func numIslands(grid [][]byte) int {
    rows, cols := len(grid), len(grid[0])

    var sink func(r, c int)
    sink = func(r, c int) {
        // Stop outside the grid, or on water.
        if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1' {
            return
        }
        grid[r][c] = '0' // mark as visited: change the land to water
        sink(r+1, c)
        sink(r-1, c)
        sink(r, c+1)
        sink(r, c-1)
    }

    count := 0
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if grid[r][c] == '1' { // land that no DFS reached: a new island
                count++
                sink(r, c) // remove the full island
            }
        }
    }
    return count
}
```

```go
// TEMPLATE B: BFS from many sources. Each level of the BFS is one unit of time.
// orangesRotting solves LC 994. Time O(rows * cols).
func orangesRotting(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    queue := [][2]int{} // cells that are rotten now
    fresh := 0
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            switch grid[r][c] {
            case 2:
                queue = append(queue, [2]int{r, c}) // each rotten orange is a source
            case 1:
                fresh++
            }
        }
    }

    dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    minutes := 0
    for len(queue) > 0 && fresh > 0 {
        minutes++
        for size := len(queue); size > 0; size-- { // one level = one minute
            cell := queue[0]
            queue = queue[1:]
            for _, d := range dirs {
                nr, nc := cell[0]+d[0], cell[1]+d[1]
                if nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] != 1 {
                    continue
                }
                grid[nr][nc] = 2 // mark when you ADD to the queue, not when you remove
                fresh--
                queue = append(queue, [2]int{nr, nc})
            }
        }
    }
    if fresh > 0 {
        return -1 // some orange cannot be reached
    }
    return minutes
}
```

```go
// TEMPLATE C: topological sort (Kahn's algorithm).
// canFinish solves LC 207. Time O(V + E).
// Idea: take the courses with no pending prerequisite, again and again.
// If a cycle exists, its courses never reach zero.
func canFinish(numCourses int, prerequisites [][]int) bool {
    adj := make([][]int, numCourses)    // adj[b] = courses that need b
    indegree := make([]int, numCourses) // number of prerequisites still pending
    for _, p := range prerequisites {
        course, pre := p[0], p[1]
        adj[pre] = append(adj[pre], course)
        indegree[course]++
    }

    queue := []int{}
    for c, d := range indegree {
        if d == 0 {
            queue = append(queue, c) // ready to take
        }
    }

    taken := 0
    for len(queue) > 0 {
        c := queue[0]
        queue = queue[1:]
        taken++
        for _, next := range adj[c] {
            indegree[next]-- // one prerequisite is done
            if indegree[next] == 0 {
                queue = append(queue, next)
            }
        }
    }
    return taken == numCourses
}
```

> [!warning] Mistakes in this stage
> - In BFS, mark a cell as visited when you add it to the queue. If you mark it later, the same cell enters the queue many times.
> - `make([][]int, rows)` makes `nil` rows. Make each row before you write to it.

> [!quote] Say it
> "BFS visits cells in order of distance. So the first time I reach a cell is the shortest path to it."

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Template A |
| [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | Template A that returns a count |
| [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Template B |
| [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | Map from old node to new node |
| [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Template C |
| [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | Template C, keep the order |

## Stage 11: Tables with dynamic programming

**Why this pair:** a DP solution is a table and a loop. The Go part is small, so this stage is mostly about the four steps.

### Go you need

```go
func dpTableBasics() {
    n, m := 3, 4

    // One dimension: n+1 zeros. Index 0 is the empty case.
    dp := make([]int, n+1)

    // Fill with a start value. There is no built-in "fill".
    for i := range dp {
        dp[i] = math.MaxInt // means "not reachable"
    }
    // math.MaxInt + 1 overflows to a negative number. Check before you add.

    // Two dimensions: (n+1) rows of (m+1) zeros.
    table := make([][]int, n+1)
    for i := range table {
        table[i] = make([]int, m+1)
    }

    // A map as a memo for top-down DP. A struct or an array can be the key.
    memo := map[[2]int]int{}
    memo[[2]int{1, 2}] = 7

    fmt.Println(len(dp), len(table), len(table[0]), memo)
}
```

### Template to memorize

> [!tip] Signal
> The problem asks for a count, a minimum or a maximum, not for the list of results. A choice at each step changes what stays for later steps.

```go
// TEMPLATE: bottom-up DP in four steps.
// coinChange solves LC 322. Time O(amount * coins), space O(amount).
func coinChange(coins []int, amount int) int {
    // 1. STATE: dp[a] = the fewest coins that make the amount a.
    dp := make([]int, amount+1)
    for a := range dp {
        dp[a] = amount + 1 // "infinity": more coins than any real answer
    }

    // 2. BASE CASE: zero coins make the amount 0.
    dp[0] = 0

    // 3. TRANSITION: the last coin is c, so dp[a] = dp[a-c] + 1. Take the best c.
    for a := 1; a <= amount; a++ {
        for _, c := range coins {
            if c <= a {
                dp[a] = min(dp[a], dp[a-c]+1)
            }
        }
    }

    // 4. ANSWER: dp[amount], if it was reached.
    if dp[amount] > amount {
        return -1
    }
    return dp[amount]
}
```

The moves are STATE, BASE CASE, TRANSITION, ANSWER. Write the state as a comment in plain words before you write code. If you cannot write that sentence, you are not ready to code.

> [!quote] Say it
> "The state is the best result for a smaller input. I build the table from small to large."

### Solved with comments

**LC 198, House Robber.** The table becomes two variables.

```go
// rob solves LC 198. Time O(n), space O(1).
// State: best(i) = the most money from the first i houses.
// Transition: best(i) = max(skip house i, rob house i) = max(best(i-1), best(i-2) + nums[i]).
// Only the last two values are necessary, so two variables replace the slice.
func rob(nums []int) int {
    prev2, prev1 := 0, 0 // best(i-2) and best(i-1)
    for _, x := range nums {
        prev2, prev1 = prev1, max(prev1, prev2+x) // both update at the same time
    }
    return prev1
}
```

**LC 1143, Longest Common Subsequence.** A table with two dimensions.

```go
// longestCommonSubsequence solves LC 1143. Time O(n * m), space O(n * m).
// State: dp[i][j] = the LCS length of the first i bytes of text1
// and the first j bytes of text2. Row 0 and column 0 are the empty string.
func longestCommonSubsequence(text1 string, text2 string) int {
    n, m := len(text1), len(text2)
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, m+1)
    }

    for i := 1; i <= n; i++ {
        for j := 1; j <= m; j++ {
            if text1[i-1] == text2[j-1] { // dp index i is string index i-1
                dp[i][j] = dp[i-1][j-1] + 1 // the equal byte extends the LCS
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) // drop one byte from one string
            }
        }
    }
    return dp[n][m]
}
```

**LC 300, Longest Increasing Subsequence.** The state is "the best result that ends at index i".

```go
// lengthOfLIS solves LC 300 with the O(n²) DP. Space O(n).
// State: dp[i] = the length of the longest increasing subsequence that ENDS at i.
func lengthOfLIS(nums []int) int {
    dp := make([]int, len(nums))
    best := 0
    for i := range nums {
        dp[i] = 1 // the number alone
        for j := 0; j < i; j++ {
            if nums[j] < nums[i] { // nums[i] can extend the subsequence that ends at j
                dp[i] = max(dp[i], dp[j]+1)
            }
        }
        best = max(best, dp[i])
    }
    return best
}
```

### Practice

| Problem | Level | What it trains |
|---|---|---|
| [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | Two variables |
| [198. House Robber](https://leetcode.com/problems/house-robber/) | Medium | Take or skip (solved above) |
| [322. Coin Change](https://leetcode.com/problems/coin-change/) | Medium | The template |
| [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | "Ends at i" state (solved above) |
| [62. Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | Grid table |
| [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | Two strings (solved above) |
| [139. Word Break](https://leetcode.com/problems/word-break/) | Medium | A `[]bool` table and a set |

## Signals: which template to use

Read the problem and look for these words first. This table is the first thing to memorize.

| Signal in the problem | Pattern | Stage |
|---|---|---|
| Count, duplicate, group, find a pair in unsorted data | Hash map | 1 |
| Sorted input and a pair, or a palindrome | Two pointers | 2 |
| Longest or shortest contiguous part with a condition | Sliding window | 3 |
| Brackets, or the next greater or smaller item | Stack | 4 |
| Sorted input and O(log n), or "the minimum value that is enough" | Binary search | 5 |
| Intervals that overlap | Sort by start, then merge | 5 |
| A linked list: reverse, merge, cycle, middle | Reverse, dummy head, fast and slow | 6 |
| Tree depth, path or validity | DFS | 7 |
| Tree levels, or the fewest steps | BFS | 7, 10 |
| The K largest, smallest or closest | Heap of size K | 8 |
| All subsets, permutations or combinations | Backtracking | 9 |
| Islands, regions, connected groups | Grid DFS | 10 |
| An order with dependencies | Topological sort | 10 |
| Count the ways, or the minimum or maximum over choices | Dynamic programming | 11 |

## Go mistakes that cost time in an interview

| Mistake | What happens | Correct form |
|---|---|---|
| `append(s, x)` with no assignment | Compile error: the value is not used | `s = append(s, x)` |
| Write to a `nil` map | Panic at run time | `m := map[string]int{}` |
| Save `path` in backtracking with no copy | All results change later | `slices.Clone(path)` |
| `dfs := func() { dfs() }` | Compile error: `dfs` is not defined | `var dfs func()` then `dfs = func() {...}` |
| `s[i] == "a"` | Compile error: byte against string | `s[i] == 'a'` |
| `len(s)` for text that is not ASCII | Counts bytes, not characters | `len([]rune(s))` |
| `x := cond ? a : b` | Go has no ternary operator | An `if` and an `else` |
| `y := i++` | `i++` is a statement, not a value | `i++` on its own line |
| `a == b` for two slices | Compile error | `slices.Equal(a, b)` |
| Unused variable or import | Compile error | Delete it, or use `_` |
| `h.Push(x)` on a heap | The heap order breaks | `heap.Push(h, x)` |

## When is a stage complete

- [ ] You can write each template of the stage from memory in less than five minutes, and it compiles.
- [ ] You solved the practice problems in Go, and at least two of them a second time.
- [ ] You can say the signal, the moves and the complexity aloud.

## Related

- [[wiki/neetcode-150/index|NeetCode 150 in Go]]: the next step. All 150 problems, each with its pattern, its template and a commented Go solution.
- [[wiki/go/index|Go Programming]]: the area this note belongs to.
- [[wiki/go/leetcode-snippets|Go LeetCode Snippets & Templates]]: short pieces of code to copy.
- [[wiki/patterns/index|LeetCode Patterns]]: the pattern notes and the progress tracker.
- [[wiki/dsa/index|Data Structures & Algorithms]]: the theory behind each structure.
- [[wiki/ai-coding/nubank-ai-coding-interview#Go for the interview|Go for the AI coding interview]]: errors, tests and project code, which this path does not cover.
