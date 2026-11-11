---
title: "NeetCode 150, stage 3: Sliding Window"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - sliding-window
date_created: 2026-11-11
date_modified: 2026-11-11
---

# NeetCode 150, stage 3: Sliding Window

[[wiki/neetcode-150/02-two-pointers|← Two Pointers]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/04-stack|Stack →]]

A window is a range `[left, right]` that moves across a slice or a string. This stage trains you to keep a small state for the window and to update it in O(1) when an item enters or leaves. That update removes the inner loop, so O(n²) becomes O(n).

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 3: Loops with the sliding window|the Go syntax for this stage]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/03-sliding-window#121. Best Time to Buy and Sell Stock\|121. Best Time to Buy and Sell Stock]] | Easy | Best so far, one pass | [[wiki/neetcode-150/03-sliding-window#Template A: Best so far in one pass\|A: Best so far in one pass]] |
| 2 | [[wiki/neetcode-150/03-sliding-window#3. Longest Substring Without Repeating Characters\|3. Longest Substring Without Repeating Characters]] | Medium | Variable window, longest | [[wiki/neetcode-150/03-sliding-window#Template B: Variable window, longest\|B: Variable window, longest]] |
| 3 | [[wiki/neetcode-150/03-sliding-window#424. Longest Repeating Character Replacement\|424. Longest Repeating Character Replacement]] | Medium | Variable window, longest | [[wiki/neetcode-150/03-sliding-window#Template B: Variable window, longest\|B: Variable window, longest]] |
| 4 | [[wiki/neetcode-150/03-sliding-window#567. Permutation in String\|567. Permutation in String]] | Medium | Fixed window with letter counts | [[wiki/neetcode-150/03-sliding-window#Template C: Fixed window\|C: Fixed window]] |
| 5 | [[wiki/neetcode-150/03-sliding-window#76. Minimum Window Substring\|76. Minimum Window Substring]] | Hard | Shortest window with a need counter | [[wiki/neetcode-150/03-sliding-window#Template D: Shortest window with a need counter\|D: Shortest window with a need counter]] |
| 6 | [[wiki/neetcode-150/03-sliding-window#239. Sliding Window Maximum\|239. Sliding Window Maximum]] | Hard | Monotonic deque | [[wiki/neetcode-150/03-sliding-window#Template E: Monotonic deque\|E: Monotonic deque]] |

## Templates to memorize

### Template A: Best so far in one pass

> [!tip] Signal
> The problem asks for the best pair of two positions, with the first before the second: buy, then sell. For each position, the best earlier partner is one value, such as the lowest value before it.

```go
// TEMPLATE A: best so far in one pass.
// For each item, the best earlier partner is one value: the lowest value
// before it.
func bestGain(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    lowest := nums[0] // the lowest value before the current item
    best := 0
    for _, x := range nums {
        // 1. RECORD: pair x with the best earlier value
        best = max(best, x-lowest)
        // 2. UPDATE the earlier value for the next items
        lowest = min(lowest, x)
    }
    return best
}
```

The moves are RECORD, then UPDATE. Record first, so the earlier value always comes from a position before the current one. This is a window whose left side jumps to the best start.

> [!quote] Say it
> "For each day I only need the lowest price before it. I keep that minimum while I scan, so it is one pass, O(n) time and O(1) space."

### Template B: Variable window, longest

> [!tip] Signal
> The problem asks for the longest substring or subarray that obeys a rule: no repeat, at most K replacements, at most K different values.

```go
// TEMPLATE B: variable window, longest. The window is nums[left..right].
// Here the rule is "no value appears two times".
func longestValidWindow(nums []int) int {
    count := make(map[int]int) // the state of the window
    best, left := 0, 0
    for right := 0; right < len(nums); right++ {
        count[nums[right]]++ // 1. GROW: nums[right] enters
        // 2. SHRINK while the window breaks the rule
        for count[nums[right]] > 1 {
            count[nums[left]]--
            left++
        }
        // 3. RECORD: the window is valid here
        best = max(best, right-left+1)
    }
    return best
}
```

The moves are GROW, SHRINK, then RECORD. Shrink with a `for` loop until the window obeys the rule again. Record after the shrink, when the window is valid. Each index enters one time and leaves one time, so the two loops together cost O(n).

> [!quote] Say it
> "I grow the window to the right, and when it breaks the rule I shrink it from the left until it is valid again. Each index enters and leaves once, so the time is O(n)."

### Template C: Fixed window

> [!tip] Signal
> The problem gives the size of the window, or the size is the length of a word. Examples are a permutation of a word, an anagram in a text, and each window of size K.

```go
// TEMPLATE C: fixed window of size k. One item enters, one item leaves.
func maxWindowSum(nums []int, k int) int {
    best := math.MinInt
    sum := 0 // the state of the window
    for right := 0; right < len(nums); right++ {
        sum += nums[right] // 1. ADD the item that enters
        if right >= k {
            sum -= nums[right-k] // 2. REMOVE the item that leaves
        }
        if right >= k-1 { // 3. CHECK only when the window is full
            best = max(best, sum)
        }
    }
    return best
}
```

The moves are ADD, REMOVE, then CHECK. The item that leaves is at index `right-k`. Check only when the window is full, that is from `right = k-1`. For letter counts, the state is a `[26]int` array, and `==` compares two arrays.

> [!quote] Say it
> "The window has a fixed size, so each step adds one item and removes one item. I update the state in O(1) and I never recount the window."

### Template D: Shortest window with a need counter

> [!tip] Signal
> The problem asks for the minimum window that contains all the required items.

```go
// TEMPLATE D: shortest window that contains all the required values.
// It returns the length of that window, or 0 when no window has them all.
func shortestCover(nums []int, required []int) int {
    // need[x] > 0: the window still needs x that many times
    need := make(map[int]int)
    for _, x := range required {
        need[x]++
    }
    // how many required items the window still needs
    missing := len(required)
    best, left := 0, 0
    for right := 0; right < len(nums); right++ {
        if need[nums[right]] > 0 { // 1. GROW: this item fills a need
            missing--
        }
        need[nums[right]]-- // below 0: the window has more than it needs
        for missing == 0 {  // the window is valid
            if best == 0 || right-left+1 < best {
                best = right - left + 1 // 2. RECORD each valid window
            }
            need[nums[left]]++ // 3. SHRINK: nums[left] leaves
            if need[nums[left]] > 0 {
                missing++ // the window needs that value again
            }
            left++
        }
    }
    return best
}
```

The moves are GROW, then RECORD and SHRINK while the window is valid. This is the opposite of Template B: the record is inside the shrink loop, because each valid window is a candidate. The integer `missing` tells in O(1) if the window is valid, so you never compare two count tables.

> [!quote] Say it
> "I count what I need, and one integer tells me how many items the window still lacks. When it reaches zero I record the window and shrink it from the left, so the time is O(m + n)."

### Template E: Monotonic deque

> [!tip] Signal
> The problem asks for the maximum or the minimum of each window, in O(n).

```go
// TEMPLATE E: monotonic deque. It holds indexes. Their values decrease from
// front to back, so the front is the maximum of the window.
func windowMaximums(nums []int, k int) []int {
    res := []int{}
    deque := []int{}
    for right := 0; right < len(nums); right++ {
        // 1. POP BACK: a value that is not larger than the new one cannot
        // win again
        for len(deque) > 0 && nums[deque[len(deque)-1]] <= nums[right] {
            deque = deque[:len(deque)-1]
        }
        deque = append(deque, right) // 2. PUSH BACK the new index
        // 3. POP FRONT: that index left the window
        if deque[0] <= right-k {
            deque = deque[1:]
        }
        if right >= k-1 { // 4. RECORD when the window is full
            res = append(res, nums[deque[0]])
        }
    }
    return res
}
```

The moves are POP BACK, PUSH BACK, POP FRONT, then RECORD. Store indexes, not values. The index tells you when the front is out of the window. Use `<=` in the pop at the back, so equal values do not collect in the deque.

> [!quote] Say it
> "I keep a deque of indexes with decreasing values, so the front is the maximum of the window. A new value removes the smaller ones behind it, because they can never be the maximum again, and the total time is O(n)."

> [!warning] Mistakes in this stage
> - `len(s)` counts bytes and `s[i]` is a byte. A byte window is correct for ASCII input only.
> - The size of the window is `right - left + 1`. Without the `+ 1`, each answer is one too small.
> - An array such as `[26]int` compares with `==`. A slice or a map does not compile with `==`.
> - `deque[0]` on an empty slice panics. In Template E the push comes before the read of the front, so the deque is never empty there.

## Solved with comments

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 121. Best Time to Buy and Sell Stock

[LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · Easy

- **Pattern:** Best so far, one pass
- **Template:** [[#Template A: Best so far in one pass|A: Best so far in one pass]]
- **Complexity:** time O(n), space O(1)

**Idea.** For each day, the best day to buy is the lowest price before it. Keep that lowest price while you scan, and record the best profit.

**Go lesson.** `for _, price := range prices` gives the value of each item. The `_` drops the index.

```go
// maxProfit solves LC 121. Time O(n), space O(1).
// For each day: profit = price today - lowest price before today.
func maxProfit(prices []int) int {
    if len(prices) == 0 {
        return 0
    }
    lowest := prices[0] // the lowest price before the current day
    best := 0           // 0 is the answer when no trade makes a profit
    for _, price := range prices {
        // RECORD: sell today, buy at the lowest price
        best = max(best, price-lowest)
        // UPDATE the lowest price for the days after
        lowest = min(lowest, price)
    }
    return best
}
```

### 3. Longest Substring Without Repeating Characters

[LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · Medium

- **Pattern:** Variable window, longest
- **Template:** [[#Template B: Variable window, longest|B: Variable window, longest]]
- **Complexity:** time O(n), space O(1), a fixed array of 256 counters

**Idea.** Grow the window to the right. If the new byte is in the window two times, move the left side until it is there one time. The window is then valid, so record its length.

**Go lesson.** `var count [256]int` is an array, not a slice. Its size is fixed, it starts with zeros, and a byte is always a valid index.

```go
// lengthOfLongestSubstring solves LC 3. Time O(n), space O(1).
// The window s[left..right] never has a byte two times when its length is
// recorded.
func lengthOfLongestSubstring(s string) int {
    var count [256]int // count[c]: how many times byte c is in the window
    best, left := 0, 0
    for right := 0; right < len(s); right++ {
        count[s[right]]++         // GROW: s[right] enters the window
        for count[s[right]] > 1 { // SHRINK while the new byte is a repeat
            count[s[left]]-- // s[left] leaves the window
            left++
        }
        // RECORD: the window has no repeat here
        best = max(best, right-left+1)
    }
    return best
}
```

### 424. Longest Repeating Character Replacement

[LeetCode 424](https://leetcode.com/problems/longest-repeating-character-replacement/) · Medium

- **Pattern:** Variable window, longest
- **Template:** [[#Template B: Variable window, longest|B: Variable window, longest]]
- **Complexity:** time O(n), space O(1), an array of 26 counters

**Idea.** A window is valid when its length minus the count of its most frequent letter is k or less. Those other letters are the ones that you replace. Grow the window, and shrink it when it needs more than k replacements.

**Go lesson.** `s[right]-'A'` changes an upper-case letter to an index from 0 to 25. Byte arithmetic needs no conversion.

```go
// characterReplacement solves LC 424. Time O(n), space O(1).
// Valid window: (length of the window) - (count of its most frequent
// letter) <= k.
func characterReplacement(s string, k int) int {
    var count [26]int // count of each letter in the window
    best, left := 0, 0
    maxCount := 0 // the largest count of one letter that a window had
    for right := 0; right < len(s); right++ {
        count[s[right]-'A']++ // GROW: s[right] enters
        maxCount = max(maxCount, count[s[right]-'A'])
        // SHRINK while the window needs more than k replacements.
        // maxCount does not decrease here, so it can be too high. That is
        // safe: only a larger maxCount can give a longer answer.
        for right-left+1-maxCount > k {
            count[s[left]-'A']--
            left++
        }
        best = max(best, right-left+1) // RECORD
    }
    return best
}
```

### 567. Permutation in String

[LeetCode 567](https://leetcode.com/problems/permutation-in-string/) · Medium

- **Pattern:** Fixed window with letter counts
- **Template:** [[#Template C: Fixed window|C: Fixed window]]
- **Complexity:** time O(n) for n = len(s2), with 26 comparisons for each window, space O(1), two arrays of 26 counters

**Idea.** A permutation of s1 has the same letter counts as s1 and the same length. Slide a window of that length across s2 and compare the counts.

**Go lesson.** Arrays compare with `==`, so `window == need` compares all 26 counters. Slices and maps do not compare that way.

```go
// checkInclusion solves LC 567. Time O(n), space O(1).
// A window of len(s1) letters in s2 is a permutation of s1 when the counts
// are equal.
func checkInclusion(s1 string, s2 string) bool {
    k := len(s1) // the fixed size of the window
    if k > len(s2) {
        return false
    }
    // need: the counts of s1. window: the counts of the window
    var need, window [26]int
    for i := 0; i < k; i++ {
        need[s1[i]-'a']++
    }
    for right := 0; right < len(s2); right++ {
        window[s2[right]-'a']++ // ADD the letter that enters
        if right >= k {
            window[s2[right-k]-'a']-- // REMOVE the letter that leaves
        }
        if right >= k-1 && window == need { // CHECK when the window is full
            return true
        }
    }
    return false
}
```

### 76. Minimum Window Substring

[LeetCode 76](https://leetcode.com/problems/minimum-window-substring/) · Hard

- **Pattern:** Shortest window with a need counter
- **Template:** [[#Template D: Shortest window with a need counter|D: Shortest window with a need counter]]
- **Complexity:** time O(m + n) for m = len(s) and n = len(t), space O(1), a fixed array of 256 counters

**Idea.** Count what t needs. Grow the window until it has all of t. Then shrink it from the left while it stays valid, and record each valid window. One integer, `missing`, tells if the window is valid.

**Go lesson.** `s[start : start+length]` is a substring that shares the memory of `s`. It makes no copy.

```go
// minWindow solves LC 76. Time O(m + n), space O(1).
// need[c] > 0 means that the window still needs byte c that many times.
func minWindow(s string, t string) string {
    var need [256]int // one counter for each byte value
    for i := 0; i < len(t); i++ {
        need[t[i]]++
    }
    // how many letters of t the window still needs
    missing := len(t)
    bestStart, bestLen := 0, len(s)+1 // len(s)+1 means "no window found"
    left := 0
    for right := 0; right < len(s); right++ {
        if need[s[right]] > 0 { // GROW: this letter fills a need
            missing--
        }
        // below 0: the window has more of it than t needs
        need[s[right]]--
        for missing == 0 { // the window has all of t
            if right-left+1 < bestLen { // RECORD each valid window
                bestStart, bestLen = left, right-left+1
            }
            need[s[left]]++ // SHRINK: s[left] leaves the window
            if need[s[left]] > 0 {
                missing++ // the window needs that letter again
            }
            left++
        }
    }
    if bestLen > len(s) {
        return ""
    }
    return s[bestStart : bestStart+bestLen]
}
```

### 239. Sliding Window Maximum

[LeetCode 239](https://leetcode.com/problems/sliding-window-maximum/) · Hard

- **Pattern:** Monotonic deque
- **Template:** [[#Template E: Monotonic deque|E: Monotonic deque]]
- **Complexity:** time O(n), space O(k)

**Idea.** Keep a deque of indexes whose values decrease from front to back. A new value removes each smaller value at the back, because that value can never be a maximum again. The front is always the maximum of the window.

**Go lesson.** A slice is the deque. `deque[1:]` removes the front and `deque[:len(deque)-1]` removes the back. The two operations move a slice border and copy nothing.

```go
// maxSlidingWindow solves LC 239. Time O(n), space O(k).
// The deque holds indexes. Each index enters one time and leaves one time.
func maxSlidingWindow(nums []int, k int) []int {
    res := make([]int, 0, len(nums)-k+1) // one answer for each full window
    // indexes: their values decrease from front to back
    deque := []int{}
    for right := 0; right < len(nums); right++ {
        // POP BACK: an older value that is not larger than nums[right]
        // leaves the window first, so it cannot be a maximum again.
        for len(deque) > 0 && nums[deque[len(deque)-1]] <= nums[right] {
            deque = deque[:len(deque)-1]
        }
        deque = append(deque, right) // PUSH BACK the new index
        // POP FRONT: that index left the window
        if deque[0] <= right-k {
            deque = deque[1:]
        }
        // RECORD when the window is full: the front is the maximum
        if right >= k-1 {
            res = append(res, nums[deque[0]])
        }
    }
    return res
}
```

---

[[wiki/neetcode-150/02-two-pointers|← Two Pointers]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/04-stack|Stack →]]
