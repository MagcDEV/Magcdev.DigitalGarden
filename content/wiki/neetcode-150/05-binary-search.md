---
title: "NeetCode 150, stage 5: Binary Search"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - binary-search
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 5: Binary Search

[[wiki/neetcode-150/04-stack|← Stack]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/06-linked-list|Linked List →]]

Binary search cuts the range of candidates in half at each step, so it needs O(log n) steps. This stage trains two loop shapes and the rule of each one: what the range means, and how each step makes it smaller. The same loop also searches a range of possible answers, not only the indexes of a slice.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 5: The sort package with binary search|the Go syntax for this stage]], [[wiki/dsa/binary-search|Binary Search]], [[wiki/dsa/sorting|Sorting]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/05-binary-search#704. Binary Search\|704. Binary Search]] | Easy | Binary search, exact value | [[wiki/neetcode-150/05-binary-search#Template A: Exact value\|A: Exact value]] |
| 2 | [[wiki/neetcode-150/05-binary-search#74. Search a 2D Matrix\|74. Search a 2D Matrix]] | Medium | Binary search, exact value | [[wiki/neetcode-150/05-binary-search#Template A: Exact value\|A: Exact value]] |
| 3 | [[wiki/neetcode-150/05-binary-search#875. Koko Eating Bananas\|875. Koko Eating Bananas]] | Medium | Binary search on the answer | [[wiki/neetcode-150/05-binary-search#Template B: First true\|B: First true]] |
| 4 | [[wiki/neetcode-150/05-binary-search#153. Find Minimum in Rotated Sorted Array\|153. Find Minimum in Rotated Sorted Array]] | Medium | First true on a rotated slice | [[wiki/neetcode-150/05-binary-search#Template B: First true\|B: First true]] |
| 5 | [[wiki/neetcode-150/05-binary-search#33. Search in Rotated Sorted Array\|33. Search in Rotated Sorted Array]] | Medium | Binary search on a rotated slice | [[wiki/neetcode-150/05-binary-search#Template C: Rotated sorted slice\|C: Rotated sorted slice]] |
| 6 | [[wiki/neetcode-150/05-binary-search#981. Time Based Key-Value Store\|981. Time Based Key-Value Store]] | Medium | Map of sorted slices, first true | [[wiki/neetcode-150/05-binary-search#Template B: First true\|B: First true]] |
| 7 | [[wiki/neetcode-150/05-binary-search#4. Median of Two Sorted Arrays\|4. Median of Two Sorted Arrays]] | Hard | Binary search on a partition | [[wiki/neetcode-150/05-binary-search#Template D: Partition of two sorted slices\|D: Partition of two sorted slices]] |

## Templates to memorize

### Template A: Exact value

> [!tip] Signal
> The slice is sorted, and the problem looks for one value. The result is an index, or "not there".

```go
// TEMPLATE A: exact value. The range lo..hi is inclusive at the two ends.
func indexOf(nums []int, target int) int {
    lo, hi := 0, len(nums)-1
    for lo <= hi { // the range still has one item or more
        mid := lo + (hi-lo)/2 // 1. MIDDLE
        switch {              // 2. COMPARE
        case nums[mid] == target:
            return mid
        case nums[mid] < target:
            lo = mid + 1 // 3. DROP HALF: mid and all the items on its left
        default:
            hi = mid - 1 // mid and all the items on its right
        }
    }
    return -1 // the range is empty: the target is not there
}
```

The moves are MIDDLE, COMPARE, then DROP HALF. The two ends `lo` and `hi` are inclusive, so the loop condition is `lo <= hi`. Each move skips `mid`, with `mid + 1` or `mid - 1`, because the comparison already tested it. A move to `mid` itself can loop forever.

> [!quote] Say it
> "The slice is sorted, so one comparison with the middle drops half of the range. That gives O(log n) time and O(1) space."

### Template B: First true

> [!tip] Signal
> A test is false for the small candidates and true for the large ones, and the problem wants the boundary. Typical words are "minimum speed", "smallest capacity", "first item larger than X". When the candidates are values and not indexes, this is a search on the answer.

```go
// TEMPLATE B: first true. ok is false, false, ..., true, true on lo..hi.
// It returns the smallest x for which ok(x) is true. ok(hi) must be true.
func firstTrue(lo, hi int, ok func(int) bool) int {
    for lo < hi { // the range still has two candidates or more
        mid := lo + (hi-lo)/2 // 1. MIDDLE: it is always less than hi
        if ok(mid) {          // 2. TEST
            hi = mid // 3. KEEP mid: it can be the answer
        } else {
            lo = mid + 1 // DROP mid and all the candidates on its left
        }
    }
    return lo // lo == hi: one candidate stays, and it is the answer
}
```

The moves are MIDDLE, TEST, then KEEP or DROP. A true `mid` can be the answer, so keep it with `hi = mid`. A false `mid` cannot, so drop it with `lo = mid + 1`. The loop condition is `lo < hi`, and the loop ends with one candidate. Choose `hi` so that the test is true there. In Go, `sort.Search(n, f)` is this template for the indexes 0 to `n-1`.

> [!quote] Say it
> "If a speed works, each faster speed works too, so the candidates are false, then true, and I binary search for the first true. Each test costs O(n), so the total is O(n log m)."

### Template C: Rotated sorted slice

> [!tip] Signal
> The input is a sorted slice after a rotation, with different values, and the problem wants O(log n). The slice has two sorted parts.

```go
// TEMPLATE C: rotated sorted slice. One half of lo..hi is always sorted.
func indexInRotated(nums []int, target int) int {
    lo, hi := 0, len(nums)-1
    for lo <= hi {
        mid := lo + (hi-lo)/2 // 1. MIDDLE
        if nums[mid] == target {
            return mid
        }
        // 2. FIND THE SORTED HALF: here it is lo..mid
        if nums[lo] <= nums[mid] {
            // 3. TEST ITS RANGE
            if nums[lo] <= target && target < nums[mid] {
                // 4. DROP HALF: the target is in the sorted half
                hi = mid - 1
            } else {
                // the target is not there, so go to the other half
                lo = mid + 1
            }
        } else { // the sorted half is mid..hi
            if nums[mid] < target && target <= nums[hi] {
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
    }
    return -1
}
```

The moves are MIDDLE, FIND THE SORTED HALF, TEST ITS RANGE, then DROP HALF. One half of the range is always sorted, and only a sorted half has a range that you can test. Write `nums[lo] <= nums[mid]` with `<=`, because `lo` equals `mid` when two items stay. The loop itself is Template A.

> [!quote] Say it
> "After a rotation, one half around the middle is still sorted. I check if the target is inside the range of that half, and if it is not, I search the other half, so it is still O(log n)."

### Template D: Partition of two sorted slices

> [!tip] Signal
> The input is two sorted slices, and the problem wants the median or the k-th item in logarithmic time. A merge costs O(m + n), which is too slow.

```go
// TEMPLATE D: partition of two sorted slices. a must be the shorter slice.
// It returns i and j: the left half of the merged slice is a[:i] plus
// b[:j].
func splitTwoSorted(a, b []int) (int, int) {
    half := (len(a) + len(b) + 1) / 2 // the size of the left half
    lo, hi := 0, len(a)               // i can be 0, 1, ..., len(a)
    for lo <= hi {
        i := lo + (hi-lo)/2 // 1. CUT a after i items
        j := half - i       // 2. DERIVE the cut in b
        switch {            // 3. CHECK the two borders
        case i > 0 && j < len(b) && a[i-1] > b[j]:
            hi = i - 1 // 4. MOVE: a gives too many items to the left half
        case j > 0 && i < len(a) && b[j-1] > a[i]:
            lo = i + 1 // a gives too few items
        default:
            return i, j // each left item <= each right item
        }
    }
    return 0, half // not reached when a and b are sorted
}
```

The moves are CUT, DERIVE, CHECK, then MOVE. Search the cut in the shorter slice, so the cut in the other slice never becomes negative. A cut at index 0 or at the end has no item on one side. Test the index before you read the item.

> [!quote] Say it
> "I do not merge: I binary search a cut in the shorter array, and the cut in the other array follows from the half size. The cut is right when the left borders are not larger than the right borders, which takes O(log of the shorter length)."

> [!warning] Mistakes in this stage
> - A mix of the two shapes loops forever: `lo <= hi` goes with `mid ± 1`, and `lo < hi` goes with `hi = mid`.
> - `(lo + hi) / 2` can overflow a 32-bit integer. Write `lo + (hi-lo)/2` as a habit.
> - `sort.Search` returns `n` when no index passes the test. Check the result before you use it as an index.
> - In a search on the answer, `lo` and `hi` are values, not indexes. A speed of 0 causes a division by zero, so start at 1.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 704. Binary Search

[LeetCode 704](https://leetcode.com/problems/binary-search/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Binary search, exact value
> - **Template:** [[#Template A: Exact value|A: Exact value]]

> [!tip]- Step 2: the idea
> **Idea.** Compare the target with the middle item. The slice is sorted, so one comparison tells which half cannot contain the target. Drop that half and repeat.
>
> **Complexity.** Time O(log n), space O(1).
>
> **Go lesson.** `lo + (hi-lo)/2` is the middle with no overflow. Integer division rounds down, so `mid` is never larger than `hi`.

> [!example]- Step 3: the Go solution
> ```go
> // search solves LC 704. Time O(log n), space O(1).
> // The range lo..hi is inclusive, so the loop runs while lo <= hi.
> func search(nums []int, target int) int {
>     lo, hi := 0, len(nums)-1
>     for lo <= hi { // the range still has one item or more
>         mid := lo + (hi-lo)/2 // MIDDLE
>         switch {              // COMPARE
>         case nums[mid] == target:
>             return mid
>         case nums[mid] < target:
>             // DROP HALF: the target is on the right of mid
>             lo = mid + 1
>         default:
>             // DROP HALF: the target is on the left of mid
>             hi = mid - 1
>         }
>     }
>     return -1 // the range is empty
> }
> ```

### 74. Search a 2D Matrix

[LeetCode 74](https://leetcode.com/problems/search-a-2d-matrix/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Binary search, exact value
> - **Template:** [[#Template A: Exact value|A: Exact value]]

> [!tip]- Step 2: the idea
> **Idea.** Each row starts after the last value of the row before it. So the rows, read one after the other, are one sorted slice of m * n items. Run a binary search on that slice, and change the index to a row and a column.
>
> **Complexity.** Time O(log(m * n)) for m rows and n columns, space O(1).
>
> **Go lesson.** Integer division and remainder change one index to two: `mid / cols` is the row and `mid % cols` is the column.

> [!example]- Step 3: the Go solution
> ```go
> // searchMatrix solves LC 74. Time O(log(m * n)), space O(1).
> // Index k of the virtual slice is the cell matrix[k/cols][k%cols].
> func searchMatrix(matrix [][]int, target int) bool {
>     if len(matrix) == 0 || len(matrix[0]) == 0 {
>         return false
>     }
>     rows, cols := len(matrix), len(matrix[0])
>     lo, hi := 0, rows*cols-1 // the indexes of the virtual slice
>     for lo <= hi {
>         mid := lo + (hi-lo)/2 // MIDDLE
>         // row = mid / cols, column = mid % cols
>         val := matrix[mid/cols][mid%cols]
>         switch { // COMPARE
>         case val == target:
>             return true
>         case val < target:
>             lo = mid + 1 // DROP HALF: the left part
>         default:
>             hi = mid - 1 // DROP HALF: the right part
>         }
>     }
>     return false
> }
> ```

### 875. Koko Eating Bananas

[LeetCode 875](https://leetcode.com/problems/koko-eating-bananas/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Binary search on the answer
> - **Template:** [[#Template B: First true|B: First true]]

> [!tip]- Step 2: the idea
> **Idea.** Do not search the piles. Search the speed. If a speed is fast enough, each larger speed is fast enough too. So the speeds are false, false, ..., true, true, and the answer is the first true.
>
> **Complexity.** Time O(n log m) for n piles and a largest pile of m, space O(1).
>
> **Go lesson.** `(p + speed - 1) / speed` is the ceiling of `p / speed` with integer arithmetic only. No float conversion is necessary.

> [!example]- Step 3: the Go solution
> ```go
> // minEatingSpeed solves LC 875. Time O(n log m), space O(1).
> // The candidates are the speeds 1..max(piles). It returns the first
> // speed
> // that is fast enough.
> func minEatingSpeed(piles []int, h int) int {
>     lo, hi := 1, 1 // the range of speeds, not of indexes
>     for _, p := range piles {
>         // the largest pile as speed needs one hour for each pile
>         hi = max(hi, p)
>     }
>     for lo < hi { // two candidates or more
>         mid := lo + (hi-lo)/2 // MIDDLE
>         // TEST: is the speed mid fast enough?
>         if hoursAt(piles, mid) <= h {
>             hi = mid // KEEP mid: it can be the answer
>         } else {
>             lo = mid + 1 // DROP mid and all the slower speeds
>         }
>     }
>     return lo // lo == hi: the first speed that is fast enough
> }
>
> // hoursAt returns the hours that Koko needs at the given speed.
> func hoursAt(piles []int, speed int) int {
>     hours := 0
>     for _, p := range piles {
>         hours += (p + speed - 1) / speed // the ceiling of p / speed
>     }
>     return hours
> }
> ```

### 153. Find Minimum in Rotated Sorted Array

[LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** First true on a rotated slice
> - **Template:** [[#Template B: First true|B: First true]]

> [!tip]- Step 2: the idea
> **Idea.** A rotation makes two sorted parts. Each item of the first part is larger than the last item of the slice. Each item of the second part is not. So the test "nums[i] <= last item" is false, then true, and the first true is the minimum.
>
> **Complexity.** Time O(log n), space O(1).
>
> **Go lesson.** The loop `for lo < hi` with `hi = mid` always ends, because integer division rounds down and `mid` is always less than `hi`.

> [!example]- Step 3: the Go solution
> ```go
> // findMin solves LC 153. Time O(log n), space O(1).
> // The minimum is the first item that is not larger than the last
> // item.
> func findMin(nums []int) int {
>     last := nums[len(nums)-1] // the fixed value for the test
>     // the test is true at hi, so an answer exists
>     lo, hi := 0, len(nums)-1
>     for lo < hi { // two candidates or more
>         mid := lo + (hi-lo)/2 // MIDDLE
>         // TEST: mid is in the part that contains the minimum
>         if nums[mid] <= last {
>             hi = mid // KEEP mid: it can be the minimum
>         } else {
>             // DROP mid: it is in the first part, with the large
>             // values
>             lo = mid + 1
>         }
>     }
>     return nums[lo] // lo == hi: the first true
> }
> ```

### 33. Search in Rotated Sorted Array

[LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Binary search on a rotated slice
> - **Template:** [[#Template C: Rotated sorted slice|C: Rotated sorted slice]]

> [!tip]- Step 2: the idea
> **Idea.** Cut the range at the middle. One of the two halves is always sorted. A sorted half has a clear range of values, so one test tells if the target is in it. If it is not, the target can only be in the other half.
>
> **Complexity.** Time O(log n), space O(1).
>
> **Go lesson.** `a <= x && x < b` is how Go writes a range test. Go has no chained comparison such as `a <= x < b`.

> [!example]- Step 3: the Go solution
> ```go
> // search solves LC 33. Time O(log n), space O(1).
> // At each step one half of lo..hi is sorted. Test the target
> // against that
> // half.
> func search(nums []int, target int) int {
>     lo, hi := 0, len(nums)-1
>     for lo <= hi {
>         mid := lo + (hi-lo)/2 // MIDDLE
>         if nums[mid] == target {
>             return mid
>         }
>         // FIND THE SORTED HALF. The <= is necessary: lo == mid when
>         // two
>         // items stay.
>         if nums[lo] <= nums[mid] { // lo..mid is sorted
>             // TEST ITS RANGE
>             if nums[lo] <= target && target < nums[mid] {
>                 // DROP HALF: the target is in lo..mid-1
>                 hi = mid - 1
>             } else {
>                 lo = mid + 1 // the target is not in the sorted half
>             }
>         } else { // mid..hi is sorted
>             // TEST ITS RANGE
>             if nums[mid] < target && target <= nums[hi] {
>                 // DROP HALF: the target is in mid+1..hi
>                 lo = mid + 1
>             } else {
>                 hi = mid - 1
>             }
>         }
>     }
>     return -1
> }
> ```

### 981. Time Based Key-Value Store

[LeetCode 981](https://leetcode.com/problems/time-based-key-value-store/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Map of sorted slices, first true
> - **Template:** [[#Template B: First true|B: First true]]

> [!tip]- Step 2: the idea
> **Idea.** The timestamps of one key only increase, so the slice of each key is sorted with no work. Get needs the last entry at or before the timestamp. Find the first entry that is after the timestamp, and step one back.
>
> **Complexity.** Time O(1) for Set, O(log n) for Get, for n values of one key, space O(n) for all the values.
>
> **Go lesson.** `sort.Search(n, f)` is Template B in the standard library. It returns the first index in 0..n-1 for which `f` is true, and it returns `n` when there is none.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `sort`
>
> ```go
> // TimeMap solves LC 981. Time O(1) for Set and O(log n) for Get,
> // space
> // O(n).
> // Each key has a slice of entries, in the order of their
> // timestamps.
> type TimeMap struct {
>     data map[string][]entry
> }
>
> // entry is one value with the time of its Set call.
> type entry struct {
>     time  int
>     value string
> }
>
> func Constructor() TimeMap {
>     // a nil map panics on a write
>     return TimeMap{data: make(map[string][]entry)}
> }
>
> func (this *TimeMap) Set(key string, value string, timestamp int) {
>     // The problem guarantees larger timestamps on each call,
>     // so append keeps the slice sorted.
>     this.data[key] = append(this.data[key], entry{timestamp, value})
> }
>
> func (this *TimeMap) Get(key string, timestamp int) string {
>     // a missing key gives a nil slice, with length 0
>     entries := this.data[key]
>     // TEST: "is this entry after the timestamp?" is false, ...,
>     // true, ...
>     // sort.Search does the MIDDLE, KEEP and DROP moves and returns
>     // the
>     // first true.
>     i := sort.Search(len(entries), func(i int) bool {
>         return entries[i].time > timestamp
>     })
>     if i == 0 {
>         return "" // no entry at or before the timestamp
>     }
>     // one step back: the last entry at or before it
>     return entries[i-1].value
> }
> ```

### 4. Median of Two Sorted Arrays

[LeetCode 4](https://leetcode.com/problems/median-of-two-sorted-arrays/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Binary search on a partition
> - **Template:** [[#Template D: Partition of two sorted slices|D: Partition of two sorted slices]]

> [!tip]- Step 2: the idea
> **Idea.** Do not merge. Cut the two slices so that the left parts together contain half of all the items. The cut is correct when each left item is not larger than each right item. Then the median is at the borders of the cut. Search the cut position in the shorter slice only.
>
> **Complexity.** Time O(log(min(m, n))), space O(1).
>
> **Go lesson.** `nums1, nums2 = nums2, nums1` swaps two slices with no temporary variable. `float64(x)` converts an int, and the `/ 2` after it is then a float division.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `math`
>
> ```go
> // findMedianSortedArrays solves LC 4. Time O(log(min(m, n))), space
> // O(1).
> // Left half = nums1[:i] plus nums2[:j]. The search finds the i that
> // makes
> // each left item <= each right item.
> func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
>     if len(nums1) > len(nums2) {
>         // search the shorter slice: j is then never negative
>         nums1, nums2 = nums2, nums1
>     }
>     m, n := len(nums1), len(nums2)
>     // the size of the left half (one more when the total is odd)
>     half := (m + n + 1) / 2
>     lo, hi := 0, m // i can be 0, 1, ..., m
>     for lo <= hi {
>         i := lo + (hi-lo)/2 // CUT nums1 after i items
>         j := half - i       // DERIVE the cut in nums2
>         // CHECK the two borders. The index tests come first.
>         switch {
>         case i > 0 && j < n && nums1[i-1] > nums2[j]:
>             // MOVE: nums1 gives too many items to the left half
>             hi = i - 1
>         case j > 0 && i < m && nums2[j-1] > nums1[i]:
>             lo = i + 1 // MOVE: nums1 gives too few items
>         default: // the cut is correct
>             // the largest item of the left half
>             maxLeft := math.MinInt
>             if i > 0 {
>                 maxLeft = nums1[i-1]
>             }
>             if j > 0 {
>                 maxLeft = max(maxLeft, nums2[j-1])
>             }
>             if (m+n)%2 == 1 {
>                 // odd total: the left half has the middle item
>                 return float64(maxLeft)
>             }
>             // the smallest item of the right half
>             minRight := math.MaxInt
>             if i < m {
>                 minRight = nums1[i]
>             }
>             if j < n {
>                 minRight = min(minRight, nums2[j])
>             }
>             // even total: the mean of the two
>             return float64(maxLeft+minRight) / 2
>         }
>     }
>     return 0 // not reached when the two slices are sorted
> }
> ```

---

[[wiki/neetcode-150/04-stack|← Stack]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/06-linked-list|Linked List →]]
