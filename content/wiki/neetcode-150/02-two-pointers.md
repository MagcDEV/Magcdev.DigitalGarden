---
title: "NeetCode 150, stage 2: Two Pointers"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - two-pointers
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 2: Two Pointers

[[wiki/neetcode-150/01-arrays-and-hashing|← Arrays and Hashing]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/03-sliding-window|Sliding Window →]]

Two pointers replace a nested loop when the input has an order. This stage trains one decision: which pointer moves, and why that move is safe. Each move drops candidates that cannot be the answer, so one pass is enough.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 2: Strings with two pointers|the Go syntax for this stage]], [[wiki/patterns/two-pointers|Two Pointers pattern]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/02-two-pointers#125. Valid Palindrome\|125. Valid Palindrome]] | Easy | Converging pointers | [[wiki/neetcode-150/02-two-pointers#Template A: Converging pointers\|A: Converging pointers]] |
| 2 | [[wiki/neetcode-150/02-two-pointers#167. Two Sum II - Input Array Is Sorted\|167. Two Sum II - Input Array Is Sorted]] | Medium | Converging pointers | [[wiki/neetcode-150/02-two-pointers#Template A: Converging pointers\|A: Converging pointers]] |
| 3 | [[wiki/neetcode-150/02-two-pointers#15. 3Sum\|15. 3Sum]] | Medium | Sort, then converging pointers | [[wiki/neetcode-150/02-two-pointers#Template B: Sort, fix one, converge\|B: Sort, fix one, converge]] |
| 4 | [[wiki/neetcode-150/02-two-pointers#11. Container With Most Water\|11. Container With Most Water]] | Medium | Converging pointers | [[wiki/neetcode-150/02-two-pointers#Template A: Converging pointers\|A: Converging pointers]] |
| 5 | [[wiki/neetcode-150/02-two-pointers#42. Trapping Rain Water\|42. Trapping Rain Water]] | Hard | Two pointers with running maximums | [[wiki/neetcode-150/02-two-pointers#Template C: Two pointers with a running maximum\|C: Two pointers with a running maximum]] |

## Templates to memorize

### Template A: Converging pointers

> [!tip] Signal
> The slice is sorted, or the problem compares the two ends: a pair with a sum, a palindrome, the widest container. A brute-force answer tries each pair.

```go
// TEMPLATE A: converging pointers on a sorted slice.
// Each step drops one item that cannot be in the answer.
func pairWithSum(sorted []int, target int) (int, int) {
    left, right := 0, len(sorted)-1 // 1. START at the two ends
    for left < right {              // stop before the pointers meet
        sum := sorted[left] + sorted[right] // 2. COMPARE
        switch {
        case sum == target:
            return left, right
        case sum < target:
            left++ // 3. MOVE: too small, only a larger left value can help
        default:
            right-- // too large, only a smaller right value can help
        }
    }
    return -1, -1 // no pair
}
```

The moves are START AT THE ENDS, COMPARE, then MOVE ONE SIDE. Move the side that cannot be part of a better answer. The loop condition is `left < right`, so one item is never its own partner.

> [!quote] Say it
> "The slice is sorted, so I put a pointer at each end. A sum that is too small moves the left pointer, a sum that is too large moves the right one, so it is O(n) time and O(1) space."

### Template B: Sort, fix one, converge

> [!tip] Signal
> The problem asks for three values that reach a target sum, with no duplicate result. The answer contains values, not indexes, so you can sort the input.

```go
// TEMPLATE B: sort, fix one value, then converge on the items after it.
func tripletsWithSum(nums []int, target int) [][]int {
    sort.Ints(nums) // 1. SORT: equal values are now neighbors
    res := [][]int{}
    for i := 0; i < len(nums)-2; i++ { // 2. FIX nums[i] as the first value
        if i > 0 && nums[i] == nums[i-1] {
            continue // 4. SKIP: this first value already gave its triplets
        }
        left, right := i+1, len(nums)-1
        for left < right { // 3. CONVERGE, as in Template A
            sum := nums[i] + nums[left] + nums[right]
            switch {
            case sum < target:
                left++
            case sum > target:
                right--
            default:
                res = append(res, []int{nums[i], nums[left], nums[right]})
                left++
                right--
                for left < right && nums[left] == nums[left-1] {
                    left++ // 4. SKIP an equal second value
                }
            }
        }
    }
    return res
}
```

The moves are SORT, FIX, CONVERGE, then SKIP. The sort costs O(n log n), and the two loops cost O(n²). Skip a value only after its first use. The test `i > 0 && nums[i] == nums[i-1]` does that, and it keeps results such as `[-1, -1, 2]`.

> [!quote] Say it
> "I sort, then I fix one value and run two pointers on the rest, which is O(n²). Equal values are neighbors after the sort, so I skip them to avoid duplicates."

### Template C: Two pointers with a running maximum

> [!tip] Signal
> The answer at each index depends on the highest value on its left and the highest value on its right. Trapped water is the model problem.

```go
// TEMPLATE C: two pointers with a running maximum on each side.
// The lower side is safe to settle: the other side has a wall at least as
// high.
func trappedWater(height []int) int {
    left, right := 0, len(height)-1
    leftMax, rightMax := 0, 0 // highest wall seen from each end
    water := 0
    for left < right {
        // 1. COMPARE the ends: the left side is lower
        if height[left] < height[right] {
            // 2. UPDATE the maximum of that side
            leftMax = max(leftMax, height[left])
            // 3. ADD the water above this index
            water += leftMax - height[left]
            left++ // 4. MOVE that side
        } else {
            rightMax = max(rightMax, height[right])
            water += rightMax - height[right]
            right--
        }
    }
    return water
}
```

The moves are COMPARE THE ENDS, UPDATE THE MAXIMUM, ADD, then MOVE. All four moves apply to the lower side. That side is safe to settle, because the other side has a wall that is at least as high. Update the maximum before you add, so the result is never negative.

> [!quote] Say it
> "The water above a bar is the lower of the two highest walls around it, minus the bar. I always move the lower side, because its own running maximum decides the water there, so it is one pass and O(1) space."

> [!warning] Mistakes in this stage
> - `for left <= right` in a pair problem compares one item with itself. Use `left < right`.
> - `sort.Ints` sorts in place and changes the caller's slice. If the problem needs the original indexes, do not sort.
> - `s[i]` is a byte, not a character. For text that is not ASCII, convert the string to `[]rune` first.
> - `len(nums)-1` is -1 for an empty slice. The condition `left < right` then stops the loop before a read.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 125. Valid Palindrome

[LeetCode 125](https://leetcode.com/problems/valid-palindrome/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Converging pointers
> - **Template:** [[#Template A: Converging pointers|A: Converging pointers]]

> [!tip]- Step 2: the idea
> **Idea.** Put one pointer at each end. Skip each byte that is not a letter or a digit, then compare the two bytes in lower case. One difference makes the answer false.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `s[i]` gives a byte, not a character. For ASCII text the byte is the character, so byte arithmetic is enough. A `switch` with no value is a clean if-else chain.

> [!example]- Step 3: the Go solution
> ```go
> // isPalindrome solves LC 125. Time O(n), space O(1).
> // Two pointers move from the ends to the middle. They compare
> // letters and
> // digits only.
> func isPalindrome(s string) bool {
>     left, right := 0, len(s)-1 // START at the two ends
>     for left < right {
>         // the first case that is true runs, and there is no
>         // fall-through
>         switch {
>         case !isAlnum(s[left]): // SKIP a byte that does not count
>             left++
>         case !isAlnum(s[right]):
>             right--
>         // COMPARE without the case
>         case lower(s[left]) != lower(s[right]):
>             return false
>         default: // equal: MOVE the two pointers in
>             left++
>             right--
>         }
>     }
>     return true // the pointers met with no difference
> }
>
> // isAlnum reports whether c is an ASCII letter or digit.
> func isAlnum(c byte) bool {
>     return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')
> }
>
> // lower changes an upper-case ASCII letter to lower case.
> func lower(c byte) byte {
>     if c >= 'A' && c <= 'Z' {
>         // the two cases are 32 apart in ASCII
>         return c + ('a' - 'A')
>     }
>     return c
> }
> ```

### 167. Two Sum II - Input Array Is Sorted

[LeetCode 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Converging pointers
> - **Template:** [[#Template A: Converging pointers|A: Converging pointers]]

> [!tip]- Step 2: the idea
> **Idea.** The slice is sorted. If the sum of the two ends is too small, only a larger left value can help. If the sum is too large, only a smaller right value can help.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `[]int{left + 1, right + 1}` is a slice literal. It makes and fills the result in one expression.

> [!example]- Step 3: the Go solution
> ```go
> // twoSum solves LC 167. Time O(n), space O(1).
> // The input is sorted, so two pointers replace the hash map of LC
> // 1.
> func twoSum(numbers []int, target int) []int {
>     left, right := 0, len(numbers)-1 // START at the two ends
>     // left < right: one item is never used two times
>     for left < right {
>         // COMPARE the sum with the target
>         sum := numbers[left] + numbers[right]
>         switch {
>         case sum == target:
>             // LeetCode wants 1-based indexes here
>             return []int{left + 1, right + 1}
>         case sum < target:
>             left++ // MOVE left: the sum must grow
>         default:
>             right-- // MOVE right: the sum must shrink
>         }
>     }
>     return nil // not reached: the problem guarantees one answer
> }
> ```

### 15. 3Sum

[LeetCode 15](https://leetcode.com/problems/3sum/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Sort, then converging pointers
> - **Template:** [[#Template B: Sort, fix one, converge|B: Sort, fix one, converge]]

> [!tip]- Step 2: the idea
> **Idea.** Sort the slice. Fix each value as the first one, then find the other two with converging pointers. Equal values are neighbors after the sort, so you can skip them and get no duplicate triplet.
>
> **Complexity.** Time O(n²), space O(1) extra, plus the memory of the sort.
>
> **Go lesson.** `sort.Ints` sorts in place, so it changes the caller's slice. `[][]int{}` is an empty slice of slices that is not nil.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `sort`
>
> ```go
> // threeSum solves LC 15. Time O(n²), space O(1) extra.
> // After the sort, each first value needs one two-pointer pass on
> // the items
> // after it.
> func threeSum(nums []int) [][]int {
>     sort.Ints(nums) // SORT: equal values are now neighbors
>     res := [][]int{}
>     // FIX nums[i] as the first value
>     for i := 0; i < len(nums)-2; i++ {
>         if nums[i] > 0 {
>             break // three positive values cannot sum to 0
>         }
>         if i > 0 && nums[i] == nums[i-1] {
>             // SKIP: this first value already gave its triplets
>             continue
>         }
>         left, right := i+1, len(nums)-1
>         for left < right { // CONVERGE on the items after i
>             sum := nums[i] + nums[left] + nums[right]
>             switch {
>             case sum < 0:
>                 left++ // the sum must grow
>             case sum > 0:
>                 right-- // the sum must shrink
>             default:
>                 res = append(res, []int{nums[i], nums[left], nums[right]})
>                 left++
>                 right--
>                 // SKIP an equal second value. The third value then
>                 // changes
>                 // too.
>                 for left < right && nums[left] == nums[left-1] {
>                     left++
>                 }
>             }
>         }
>     }
>     return res
> }
> ```

### 11. Container With Most Water

[LeetCode 11](https://leetcode.com/problems/container-with-most-water/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Converging pointers
> - **Template:** [[#Template A: Converging pointers|A: Converging pointers]]

> [!tip]- Step 2: the idea
> **Idea.** Start with the widest container. The shorter line limits the water, so a move of the taller line can only make the area smaller. Move the shorter line each time.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `min` and `max` are built-in functions from Go 1.21. They need no import.

> [!example]- Step 3: the Go solution
> ```go
> // maxArea solves LC 11. Time O(n), space O(1).
> // The area is the width times the shorter of the two lines.
> func maxArea(height []int) int {
>     // START with the widest container
>     left, right := 0, len(height)-1
>     best := 0
>     for left < right {
>         width := right - left
>         // RECORD this area
>         best = max(best, width*min(height[left], height[right]))
>         // MOVE the shorter line. With the taller line moved, the
>         // width
>         // decreases and the shorter line is still the limit.
>         if height[left] < height[right] {
>             left++
>         } else {
>             right--
>         }
>     }
>     return best
> }
> ```

### 42. Trapping Rain Water

[LeetCode 42](https://leetcode.com/problems/trapping-rain-water/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Two pointers with running maximums
> - **Template:** [[#Template C: Two pointers with a running maximum|C: Two pointers with a running maximum]]

> [!tip]- Step 2: the idea
> **Idea.** The water above an index is the lower of the two highest walls around it, minus its own height. Work on the lower end first. The other end proves that a wall at least as high exists there, so the maximum of the lower side decides the water.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `left, right := 0, len(height)-1` declares two variables in one statement. On an empty slice `right` is -1, so the loop does not run.

> [!example]- Step 3: the Go solution
> ```go
> // trap solves LC 42. Time O(n), space O(1).
> // water at i = min(highest wall on the left, highest wall on the
> // right) -
> // height[i].
> func trap(height []int) int {
>     left, right := 0, len(height)-1
>     leftMax, rightMax := 0, 0 // the highest wall seen from each end
>     water := 0
>     for left < right {
>         // COMPARE the ends: the left side is lower
>         if height[left] < height[right] {
>             // A wall at least as high as height[left] exists on the
>             // right,
>             // so leftMax alone decides the water above left.
>             // UPDATE the maximum of this side
>             leftMax = max(leftMax, height[left])
>             // ADD: 0 when this bar is the new maximum
>             water += leftMax - height[left]
>             left++ // MOVE this side
>         } else { // the same steps, seen from the right
>             rightMax = max(rightMax, height[right])
>             water += rightMax - height[right]
>             right--
>         }
>     }
>     return water
> }
> ```

---

[[wiki/neetcode-150/01-arrays-and-hashing|← Arrays and Hashing]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/03-sliding-window|Sliding Window →]]
