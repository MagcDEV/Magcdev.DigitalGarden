---
title: "NeetCode 150, stage 1: Arrays and Hashing"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - arrays-and-hashing
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 1: Arrays and Hashing

[[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/02-two-pointers|Two Pointers →]]

Almost every problem starts with a slice, and the hash map is the first tool that removes a nested loop. This stage trains one trade: you use more memory, and the time goes from O(n²) to O(n).

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 1: Slices and maps with arrays and hashing|the Go syntax for this stage]], [[wiki/patterns/arrays-and-hashing|Arrays and Hashing pattern]], [[wiki/dsa/arrays|Arrays]], [[wiki/dsa/hash-tables|Hash Tables]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/01-arrays-and-hashing#217. Contains Duplicate\|217. Contains Duplicate]] | Easy | Hash set | [[wiki/neetcode-150/01-arrays-and-hashing#Template A: Seen set\|A: Seen set]] |
| 2 | [[wiki/neetcode-150/01-arrays-and-hashing#242. Valid Anagram\|242. Valid Anagram]] | Easy | Letter count | [[wiki/neetcode-150/01-arrays-and-hashing#Template B: Count array or count map\|B: Count array or count map]] |
| 3 | [[wiki/neetcode-150/01-arrays-and-hashing#1. Two Sum\|1. Two Sum]] | Easy | Hash map of value to index | [[wiki/neetcode-150/01-arrays-and-hashing#Template A: Seen set\|A: Seen set]] |
| 4 | [[wiki/neetcode-150/01-arrays-and-hashing#49. Group Anagrams\|49. Group Anagrams]] | Medium | Hash map with a count key | [[wiki/neetcode-150/01-arrays-and-hashing#Template B: Count array or count map\|B: Count array or count map]] |
| 5 | [[wiki/neetcode-150/01-arrays-and-hashing#347. Top K Frequent Elements\|347. Top K Frequent Elements]] | Medium | Count map, then bucket sort | [[wiki/neetcode-150/01-arrays-and-hashing#Template C: Bucket by count\|C: Bucket by count]] |
| 6 | [[wiki/neetcode-150/01-arrays-and-hashing#271. Encode and Decode Strings\|271. Encode and Decode Strings]] | Medium | Length-prefix encoding | [[wiki/neetcode-150/01-arrays-and-hashing#Template E: Length prefix\|E: Length prefix]] |
| 7 | [[wiki/neetcode-150/01-arrays-and-hashing#238. Product of Array Except Self\|238. Product of Array Except Self]] | Medium | Prefix and suffix products | [[wiki/neetcode-150/01-arrays-and-hashing#Template D: Prefix and suffix passes\|D: Prefix and suffix passes]] |
| 8 | [[wiki/neetcode-150/01-arrays-and-hashing#36. Valid Sudoku\|36. Valid Sudoku]] | Medium | Seen sets for rows, columns and boxes | [[wiki/neetcode-150/01-arrays-and-hashing#Template A: Seen set\|A: Seen set]] |
| 9 | [[wiki/neetcode-150/01-arrays-and-hashing#128. Longest Consecutive Sequence\|128. Longest Consecutive Sequence]] | Medium | Hash set, count from the start of each run | [[wiki/neetcode-150/01-arrays-and-hashing#Template A: Seen set\|A: Seen set]] |

## Templates to memorize

### Template A: Seen set

> [!tip] Signal
> The problem says duplicate, "already seen", pair or "find the partner". A brute-force answer compares each item with each other item.

```go
// TEMPLATE A: one pass with a "seen" set or map.
// Ask at each item: "did I already see what I need?"
func hasPairWithSum(nums []int, target int) bool {
    // a set: the value type uses no memory
    seen := make(map[int]struct{}, len(nums))
    for _, x := range nums {
        if _, ok := seen[target-x]; ok { // 1. CHECK for the partner first
            return true
        }
        seen[x] = struct{}{} // 2. STORE x after the check
    }
    return false
}
```

The moves are CHECK, then STORE. Do the check before the store, so an item is never its own partner. Use a set when the fact "it is there" is enough. Use a map when you also need the index.

> [!quote] Say it
> "I trade memory for time. One pass with a hash map gives O(n) time and O(n) space."

### Template B: Count array or count map

> [!tip] Signal
> The problem says anagram, frequency, "how many times" or "same letters". The order of the items does not matter, only the counts.

```go
// TEMPLATE B: count the items, then compare the counts or use them as a
// key.
func letterCount(s string) [26]int {
    var count [26]int // 26 zeros: one counter for each lower-case letter
    for i := 0; i < len(s); i++ {
        count[s[i]-'a']++ // 'a' -> 0, 'b' -> 1, and so on
    }
    return count // arrays compare with ==, and an array can be a map key
}

// For values that are not letters, count with a map.
func countValues(nums []int) map[int]int {
    count := make(map[int]int, len(nums))
    for _, x := range nums {
        count[x]++ // a missing key reads as 0, so ++ works
    }
    return count
}
```

The moves are COUNT, then COMPARE or USE AS A KEY. A `[26]int` array is faster than a map for lower-case letters. An array is also a valid map key, and a slice is not.

> [!quote] Say it
> "Two words are anagrams when their letter counts are equal, so I compare 26 counters."

### Template C: Bucket by count

> [!tip] Signal
> The problem asks for the K most frequent items, and it wants better than O(n log n).

```go
// TEMPLATE C: bucket by count. buckets[c] holds the values that appear c
// times.
func mostFrequentFirst(nums []int) []int {
    count := make(map[int]int)
    for _, x := range nums { // 1. COUNT
        count[x]++
    }
    // a count is between 1 and len(nums)
    buckets := make([][]int, len(nums)+1)
    // 2. BUCKET: the count is the index
    for x, c := range count {
        buckets[c] = append(buckets[c], x)
    }
    res := make([]int, 0, len(count))
    // 3. READ from the largest count down
    for c := len(buckets) - 1; c >= 1; c-- {
        res = append(res, buckets[c]...)
    }
    return res
}
```

The moves are COUNT, BUCKET, then READ FROM THE END. The bucket index is a count, and a count is at most `n`. So the buckets replace the sort.

> [!quote] Say it
> "A count is at most n, so I use the count as an index. That gives O(n) with no sort and no heap."

### Template D: Prefix and suffix passes

> [!tip] Signal
> The answer at index `i` needs all the items before `i` and all the items after `i`. The problem forbids division, or division does not help.

```go
// TEMPLATE D: two passes. res[i] = (sum of the items before i) + (sum of
// the items after i).
// Change + to * (and the start value 0 to 1) for a product.
func sumOfOthers(nums []int) []int {
    n := len(nums)
    res := make([]int, n)
    left := 0
    for i := 0; i < n; i++ { // 1. left to right
        res[i] = left   // write first: left does not include nums[i]
        left += nums[i] // then take nums[i] into the running value
    }
    right := 0
    for i := n - 1; i >= 0; i-- { // 2. right to left
        res[i] += right
        right += nums[i]
    }
    return res
}
```

The moves are PASS LEFT TO RIGHT with a running value, then PASS RIGHT TO LEFT with a second running value. Each pass writes the value before it includes the item at `i`.

> [!quote] Say it
> "The answer at i is the product of the left part times the product of the right part. Two passes give the two parts."

### Template E: Length prefix

> [!tip] Signal
> You must put many strings in one string and get them back. The strings can contain each character, so no separator is safe.

```go
// TEMPLATE E: length prefix. "go" becomes "2#go".
func encodeOne(s string) string {
    // WRITE the length, the marker, the text
    return strconv.Itoa(len(s)) + "#" + s
}

// decodeOne reads one string that starts at index i.
// It returns the string and the index of the next one.
func decodeOne(data string, i int) (string, int) {
    j := i
    for data[j] != '#' { // FIND the marker after the digits
        j++
    }
    n, _ := strconv.Atoi(data[i:j]) // PARSE the length
    start := j + 1
    return data[start : start+n], start + n // CUT exactly n bytes
}
```

The moves are WRITE the length, a marker and the text. To read, FIND the marker, PARSE the length, then CUT exactly that many bytes. The reader never searches inside the text, so the text can contain the marker.

> [!quote] Say it
> "I write the length before each string, so the decoder never looks for a separator inside the data."

> [!warning] Mistakes in this stage
> - A write to a `nil` map panics. Make the map with `make` or with a literal.
> - The order of a `range` over a map is random. Sort the result if the order matters.
> - `make([]int, n)` then `append` gives `n` zeros first. Use `make([]int, 0, n)` before `append`.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 217. Contains Duplicate

[LeetCode 217](https://leetcode.com/problems/contains-duplicate/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Hash set
> - **Template:** [[#Template A: Seen set|A: Seen set]]

> [!tip]- Step 2: the idea
> **Idea.** Keep a set of the values that you saw. If the next value is already in the set, it is a duplicate.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** Go has no set type. A `map[int]struct{}` is the set, and the "comma ok" form tests membership.

> [!example]- Step 3: the Go solution
> ```go
> // containsDuplicate solves LC 217. Time O(n), space O(n).
> // It returns true when a value appears two or more times.
> func containsDuplicate(nums []int) bool {
>     // the size hint avoids regrowth
>     seen := make(map[int]struct{}, len(nums))
>     // _ drops the index, x is the value
>     for _, x := range nums {
>         // CHECK: ok is true when the key is in the map
>         if _, ok := seen[x]; ok {
>             return true
>         }
>         seen[x] = struct{}{} // STORE: struct{}{} is the empty value
>     }
>     return false
> }
> ```

### 242. Valid Anagram

[LeetCode 242](https://leetcode.com/problems/valid-anagram/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Letter count
> - **Template:** [[#Template B: Count array or count map|B: Count array or count map]]

> [!tip]- Step 2: the idea
> **Idea.** Count the letters of `s` up and the letters of `t` down in one counter. The two strings are anagrams when each counter is zero at the end.
>
> **Complexity.** Time O(n), space O(1), because the counter has 26 items.
>
> **Go lesson.** `s[i]` is a byte, and `s[i]-'a'` is the index of the letter. A `[26]int` array starts as 26 zeros.

> [!example]- Step 3: the Go solution
> ```go
> // isAnagram solves LC 242. Time O(n), space O(1).
> func isAnagram(s string, t string) bool {
>     // different lengths cannot have equal counts
>     if len(s) != len(t) {
>         return false
>     }
>     // COUNT: one counter for each lower-case letter
>     var count [26]int
>     for i := 0; i < len(s); i++ {
>         count[s[i]-'a']++ // a letter of s adds one
>         count[t[i]-'a']-- // a letter of t removes one
>     }
>     // COMPARE: the zero array is the "all counters are zero" value.
>     return count == [26]int{}
> }
> ```

### 1. Two Sum

[LeetCode 1](https://leetcode.com/problems/two-sum/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Hash map of value to index
> - **Template:** [[#Template A: Seen set|A: Seen set]]

> [!tip]- Step 2: the idea
> **Idea.** For each number, the partner is `target - x`. A map from value to index tells you in O(1) if the partner came before.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** `if j, ok := seen[need]; ok` reads the map and tests the key in one line. `j` and `ok` exist only inside the `if`.

> [!example]- Step 3: the Go solution
> ```go
> // twoSum solves LC 1. Time O(n), space O(n).
> func twoSum(nums []int, target int) []int {
>     // value -> index of that value
>     seen := make(map[int]int, len(nums))
>     for i, x := range nums {
>         // the partner that completes the pair
>         need := target - x
>         // CHECK: was the partner seen before?
>         if j, ok := seen[need]; ok {
>             return []int{j, i}
>         }
>         // STORE after the check, so x is not its own partner
>         seen[x] = i
>     }
>     // LeetCode guarantees one answer, so this line does not run
>     return nil
> }
> ```

### 49. Group Anagrams

[LeetCode 49](https://leetcode.com/problems/group-anagrams/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Hash map with a count key
> - **Template:** [[#Template B: Count array or count map|B: Count array or count map]]

> [!tip]- Step 2: the idea
> **Idea.** Two words are anagrams when their letter counts are equal. So the letter count is the map key, and each key collects its words.
>
> **Complexity.** Time O(n * k) for n words of length k, space O(n * k).
>
> **Go lesson.** An array such as `[26]int` can be a map key, because arrays compare with `==`. A slice cannot be a key.

> [!example]- Step 3: the Go solution
> ```go
> // groupAnagrams solves LC 49. Time O(n * k) for n words of length
> // k.
> func groupAnagrams(strs []string) [][]string {
>     // letter counts -> the words with those counts
>     groups := make(map[[26]int][]string)
>     for _, s := range strs {
>         var key [26]int               // COUNT: starts as 26 zeros
>         for i := 0; i < len(s); i++ { // s[i] is a byte
>             key[s[i]-'a']++ // 'a' -> 0, 'b' -> 1, and so on
>         }
>         // USE AS A KEY. append works on a missing key, because the
>         // zero value of a slice is nil and append accepts nil.
>         groups[key] = append(groups[key], s)
>     }
>
>     // length 0, capacity = number of groups
>     res := make([][]string, 0, len(groups))
>     // the order of the groups is random
>     for _, g := range groups {
>         res = append(res, g)
>     }
>     return res
> }
> ```

### 347. Top K Frequent Elements

[LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Count map, then bucket sort
> - **Template:** [[#Template C: Bucket by count|C: Bucket by count]]

> [!tip]- Step 2: the idea
> **Idea.** Count each value. Then put each value in the bucket of its count. Read the buckets from the largest count down until you have k values.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** `append(res, bucket...)` spreads a slice into separate arguments. `res[:k]` cuts the result to k items.

> [!example]- Step 3: the Go solution
> ```go
> // topKFrequent solves LC 347. Time O(n), space O(n).
> // A heap of size k also works, in O(n log k). The buckets are
> // faster.
> func topKFrequent(nums []int, k int) []int {
>     count := make(map[int]int)
>     for _, x := range nums { // 1. COUNT
>         count[x]++
>     }
>
>     // 2. BUCKET: buckets[c] holds the values that appear exactly c
>     // times.
>     // A value appears at most len(nums) times, so len(nums)+1
>     // buckets are
>     // enough.
>     buckets := make([][]int, len(nums)+1)
>     for x, c := range count {
>         buckets[c] = append(buckets[c], x)
>     }
>
>     // 3. READ from the largest count down.
>     res := make([]int, 0, k)
>     for c := len(buckets) - 1; c >= 1 && len(res) < k; c-- {
>         res = append(res, buckets[c]...) // ... spreads the bucket
>     }
>     // the answer is unique, so the last bucket never adds too many
>     return res[:k]
> }
> ```

### 271. Encode and Decode Strings

[LeetCode 271](https://leetcode.com/problems/encode-and-decode-strings/) (premium) · [free on NeetCode](https://neetcode.io/problems/string-encode-and-decode) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Length-prefix encoding
> - **Template:** [[#Template E: Length prefix|E: Length prefix]]

> [!tip]- Step 2: the idea
> **Idea.** Write each string as its length, then `#`, then the text. The decoder reads the length and cuts exactly that many bytes, so the text can contain `#` or digits.
>
> **Complexity.** Time O(n) for n bytes in total, space O(n).
>
> **Go lesson.** `strings.Builder` builds a string in a loop in O(n). `s += x` in a loop is O(n²), because each `+=` copies the string.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `strconv`, `strings`
>
> ```go
> // Codec solves LC 271. Encode and Decode are O(n) for n bytes in
> // total.
> // Format: ["go", "", "a#b"] becomes "2#go0#3#a#b".
> type Codec struct{}
>
> // Encode joins the strings into one string.
> func (codec *Codec) Encode(strs []string) string {
>     // appends with no copy of the earlier text
>     var sb strings.Builder
>     for _, s := range strs {
>         // WRITE the length in bytes
>         sb.WriteString(strconv.Itoa(len(s)))
>         // the marker ends the digits
>         sb.WriteByte('#')
>         sb.WriteString(s) // the text, unchanged
>     }
>     return sb.String()
> }
>
> // Decode splits the encoded string into the original strings.
> func (codec *Codec) Decode(strs string) []string {
>     // not nil: an empty list must decode to an empty list
>     res := []string{}
>     i := 0
>     for i < len(strs) {
>         j := i
>         // FIND the marker: the digits are strs[i:j]
>         for strs[j] != '#' {
>             j++
>         }
>         // PARSE the length (we wrote it, so it is valid)
>         n, _ := strconv.Atoi(strs[i:j])
>         start := j + 1 // the text starts after the marker
>         res = append(res, strs[start:start+n])
>         i = start + n // CUT: the next length starts here
>     }
>     return res
> }
> ```

### 238. Product of Array Except Self

[LeetCode 238](https://leetcode.com/problems/product-of-array-except-self/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Prefix and suffix products
> - **Template:** [[#Template D: Prefix and suffix passes|D: Prefix and suffix passes]]

> [!tip]- Step 2: the idea
> **Idea.** The answer at `i` is the product of all the items to the left times the product of all the items to the right. One pass gives the left products, and a second pass multiplies by the right products.
>
> **Complexity.** Time O(n), space O(1) extra, because the result slice does not count.
>
> **Go lesson.** `make([]int, n)` gives n zeros that you write by index. A loop can also run down, with `i--`.

> [!example]- Step 3: the Go solution
> ```go
> // productExceptSelf solves LC 238 with no division. Time O(n),
> // extra space
> // O(1).
> func productExceptSelf(nums []int) []int {
>     n := len(nums)
>     res := make([]int, n)
>
>     // PASS 1, left to right: res[i] = product of nums[0..i-1].
>     left := 1 // the product of zero items is 1
>     for i := 0; i < n; i++ {
>         // write first: left does not include nums[i]
>         res[i] = left
>         // then take nums[i] into the running product
>         left *= nums[i]
>     }
>
>     // PASS 2, right to left: multiply by the product of
>     // nums[i+1..n-1].
>     right := 1
>     for i := n - 1; i >= 0; i-- {
>         res[i] *= right
>         right *= nums[i]
>     }
>     return res
> }
> ```

### 36. Valid Sudoku

[LeetCode 36](https://leetcode.com/problems/valid-sudoku/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Seen sets for rows, columns and boxes
> - **Template:** [[#Template A: Seen set|A: Seen set]]

> [!tip]- Step 2: the idea
> **Idea.** A digit is not valid if the same digit is already in its row, its column or its 3x3 box. Keep one "seen" table for each of the three, and check them in one pass over the board.
>
> **Complexity.** Time O(1), because the board always has 81 cells, space O(1).
>
> **Go lesson.** A fixed 2D array such as `[9][9]bool` is a fast set when the keys are small numbers. The box of a cell is `(r/3)*3 + c/3`, because integer division drops the remainder.

> [!example]- Step 3: the Go solution
> ```go
> // isValidSudoku solves LC 36. The board is 9 x 9, so time and space
> // are
> // O(1).
> // Only the filled cells are checked. The board does not have to be
> // solvable.
> func isValidSudoku(board [][]byte) bool {
>     // rows[r][d] is true when digit d is already in row r. Same for
>     // cols
>     // and boxes.
>     var rows, cols, boxes [9][9]bool
>
>     for r := 0; r < 9; r++ {
>         for c := 0; c < 9; c++ {
>             if board[r][c] == '.' {
>                 continue // an empty cell has nothing to check
>             }
>             // '1'..'9' -> 0..8: the index of the digit
>             d := board[r][c] - '1'
>             // boxes are numbered 0..8, row by row
>             b := (r/3)*3 + c/3
>
>             // CHECK the three sets
>             if rows[r][d] || cols[c][d] || boxes[b][d] {
>                 return false
>             }
>             // STORE in the three sets
>             rows[r][d], cols[c][d], boxes[b][d] = true, true, true
>         }
>     }
>     return true
> }
> ```

### 128. Longest Consecutive Sequence

[LeetCode 128](https://leetcode.com/problems/longest-consecutive-sequence/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Hash set, count from the start of each run
> - **Template:** [[#Template A: Seen set|A: Seen set]]

> [!tip]- Step 2: the idea
> **Idea.** Put all the numbers in a set. A number `x` starts a run only when `x-1` is not in the set. Count up from each start. Each number is then visited at most two times, so the time is O(n).
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** A `range` over a map gives each key one time, so duplicates in the input cost nothing.

> [!example]- Step 3: the Go solution
> ```go
> // longestConsecutive solves LC 128 with no sort. Time O(n), space
> // O(n).
> func longestConsecutive(nums []int) int {
>     set := make(map[int]struct{}, len(nums))
>     for _, x := range nums { // STORE all the numbers first
>         set[x] = struct{}{}
>     }
>
>     best := 0
>     // range over the set, not nums: no duplicate work
>     for x := range set {
>         // CHECK: x-1 exists, so x is not the start of a run
>         if _, ok := set[x-1]; ok {
>             continue
>         }
>         // x is the first number of a run. Count how far the run
>         // goes.
>         length := 1
>         for {
>             if _, ok := set[x+length]; !ok {
>                 break
>             }
>             length++
>         }
>         best = max(best, length)
>     }
>     return best
> }
> ```

---

[[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/02-two-pointers|Two Pointers →]]
