---
title: "NeetCode 150, stage 4: Stack"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - stack
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 4: Stack

[[wiki/neetcode-150/03-sliding-window|← Sliding Window]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/05-binary-search|Binary Search →]]

A stack keeps the items that are not complete, with the most recent item on top. In Go a slice is the stack: `append` pushes, and a new slice expression pops. This stage trains you to see which items must wait, and which event resolves them.

Garden notes: [[wiki/go/go-leetcode-learning-path#Stage 4: Slices as a stack|the Go syntax for this stage]], [[wiki/patterns/stack-based|Stack-Based pattern]], [[wiki/dsa/stacks|Stacks]].

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/04-stack#20. Valid Parentheses\|20. Valid Parentheses]] | Easy | Matching stack | [[wiki/neetcode-150/04-stack#Template A: Matching stack\|A: Matching stack]] |
| 2 | [[wiki/neetcode-150/04-stack#155. Min Stack\|155. Min Stack]] | Medium | Paired stack | [[wiki/neetcode-150/04-stack#Template B: Paired stack\|B: Paired stack]] |
| 3 | [[wiki/neetcode-150/04-stack#150. Evaluate Reverse Polish Notation\|150. Evaluate Reverse Polish Notation]] | Medium | Stack as evaluator | [[wiki/neetcode-150/04-stack#Template C: Stack as evaluator\|C: Stack as evaluator]] |
| 4 | [[wiki/neetcode-150/04-stack#22. Generate Parentheses\|22. Generate Parentheses]] | Medium | Backtracking with counters | [[wiki/neetcode-150/04-stack#Template D: Backtracking with counters\|D: Backtracking with counters]] |
| 5 | [[wiki/neetcode-150/04-stack#739. Daily Temperatures\|739. Daily Temperatures]] | Medium | Monotonic stack | [[wiki/neetcode-150/04-stack#Template E: Monotonic stack\|E: Monotonic stack]] |
| 6 | [[wiki/neetcode-150/04-stack#853. Car Fleet\|853. Car Fleet]] | Medium | Sort, then monotonic stack | [[wiki/neetcode-150/04-stack#Template E: Monotonic stack\|E: Monotonic stack]] |
| 7 | [[wiki/neetcode-150/04-stack#84. Largest Rectangle in Histogram\|84. Largest Rectangle in Histogram]] | Hard | Monotonic stack | [[wiki/neetcode-150/04-stack#Template E: Monotonic stack\|E: Monotonic stack]] |

## Templates to memorize

### Template A: Matching stack

> [!tip] Signal
> The input has items that open and close, and the pairs nest: brackets, tags, directory paths. The most recent opener must close first.

```go
// TEMPLATE A: matching stack. An opener waits on the stack for its closer.
func balanced(s string) bool {
    pairs := map[byte]byte{')': '(', ']': '['} // closer -> its opener
    stack := []byte{}
    for i := 0; i < len(s); i++ {
        open, isCloser := pairs[s[i]]
        if !isCloser {
            stack = append(stack, s[i]) // 1. PUSH an opener
            continue
        }
        // 2. MATCH the top
        if len(stack) == 0 || stack[len(stack)-1] != open {
            return false
        }
        stack = stack[:len(stack)-1] // 3. POP the opener
    }
    return len(stack) == 0 // 4. LEFTOVER openers make the answer false
}
```

The moves are PUSH, MATCH, POP, then the LEFTOVER test. Test `len(stack) == 0` before you read the top. Do the leftover test at the end, because `"(("` has no wrong closer and is still not valid.

> [!quote] Say it
> "The last bracket that I open is the first one that I must close, and that is a stack. I push openers, I match each closer with the top, and the stack must be empty at the end."

### Template B: Paired stack

> [!tip] Signal
> A design problem wants push, pop and one more query, such as the minimum, and each operation must be O(1).

```go
// TEMPLATE B: paired stack. best[i] is the answer for the items vals[0..i].
type maxStack struct {
    vals []int // the values
    best []int // best[i]: the maximum of vals[0..i]
}

func (s *maxStack) push(x int) {
    top := x
    if len(s.best) > 0 {
        // compare with the answer below
        top = max(top, s.best[len(s.best)-1])
    }
    s.vals = append(s.vals, x) // 1. PUSH BOTH
    s.best = append(s.best, top)
}

func (s *maxStack) pop() {
    // 2. POP BOTH: the old answer is on top again
    s.vals = s.vals[:len(s.vals)-1]
    s.best = s.best[:len(s.best)-1]
}

// 3. READ THE TOP
func (s *maxStack) max() int { return s.best[len(s.best)-1] }
```

The moves are PUSH BOTH, POP BOTH, then READ THE TOP. The second stack stores the answer to the query for each height of the first stack. A pop then brings back the answer from before, with no search. Keep the two stacks at the same length.

> [!quote] Say it
> "I keep a second stack that stores the minimum at each height. A pop removes one item from each stack, so the minimum from before is on top again, and each operation is O(1)."

### Template C: Stack as evaluator

> [!tip] Signal
> The input is an expression in postfix notation (Reverse Polish notation). More generally, each token applies to the most recent results.

```go
// TEMPLATE C: the stack as an evaluator of postfix tokens.
// The stack holds the results that wait for an operator.
func evalPostfix(tokens []string) int {
    stack := []int{}
    for _, tok := range tokens {
        if n, err := strconv.Atoi(tok); err == nil {
            stack = append(stack, n) // 1. PUSH a number
            continue
        }
        b := stack[len(stack)-1] // 2. POP TWO: the top is the right operand
        a := stack[len(stack)-2]
        stack = stack[:len(stack)-2]
        res := a + b // 3. APPLY the operator
        if tok == "-" {
            res = a - b
        }
        stack = append(stack, res) // 4. PUSH the result
    }
    return stack[0]
}
```

The moves are PUSH a number, POP TWO, APPLY, then PUSH the result. The first value that you pop is the right operand. That order changes the result of `-` and `/`.

> [!quote] Say it
> "Numbers wait on the stack. An operator pops two values, the right operand first, and pushes the result, so it is one pass and O(n)."

### Template D: Backtracking with counters

> [!tip] Signal
> The problem says "generate all" the valid strings or combinations. The number of results grows exponentially, so the task is to build only the valid ones.

```go
// TEMPLATE D: backtracking with counters. The call stack is the stack.
// It builds each string of n pairs of brackets that is balanced.
func allBalanced(n int) []string {
    res := []string{}
    path := make([]byte, 0, 2*n) // the string that the recursion builds
    var build func(open, closed int)
    build = func(open, closed int) {
        if len(path) == 2*n {
            res = append(res, string(path)) // RECORD a copy of the path
            return
        }
        if open < n { // the counters permit only valid choices
            path = append(path, '(')  // 1. CHOOSE
            build(open+1, closed)     // 2. EXPLORE
            path = path[:len(path)-1] // 3. UNDO
        }
        if closed < open {
            path = append(path, ')')
            build(open, closed+1)
            path = path[:len(path)-1]
        }
    }
    build(0, 0)
    return res
}
```

The moves are CHOOSE, EXPLORE, then UNDO. Here the call stack is the stack. The two counters stop a bad branch before it starts: `open < n` permits an opener, and `closed < open` permits a closer. Record `string(path)`, which is a copy, because the recursion changes `path` after that.

> [!quote] Say it
> "I can open while I have openers left, and I can close only while something is open. So each string that reaches full length is valid, and I never filter."

### Template E: Monotonic stack

> [!tip] Signal
> The problem asks, for each item, for the next larger item, the next smaller item, or how far the item can extend. A brute-force answer scans to the right from each index.

```go
// TEMPLATE E: monotonic stack. It holds the indexes that wait for an
// answer.
// Here the answer is the index of the next larger value, or -1.
func nextGreater(nums []int) []int {
    res := make([]int, len(nums))
    for i := range res {
        res[i] = -1 // the default: no larger value comes
    }
    // indexes that wait: their values decrease from the bottom up
    stack := []int{}
    for i, x := range nums {
        // 1. RESOLVE: x is the answer for each smaller value on the top
        for len(stack) > 0 && nums[stack[len(stack)-1]] < x {
            j := stack[len(stack)-1]
            // POP the index that has its answer
            stack = stack[:len(stack)-1]
            res[j] = i
        }
        stack = append(stack, i) // 2. PUSH: index i waits now
    }
    return res
}
```

The moves are RESOLVE, then PUSH. The stack holds the indexes that wait for an answer. The current item resolves each index on the top that it answers, and then it waits too. The loop pushes each index one time and pops it one time at most, so the total is O(n). Store indexes, not values, because the answer is usually a distance.

> [!quote] Say it
> "The stack holds the indexes that still wait for a larger value, and each new value pops the smaller ones and becomes their answer. Each index is pushed and popped once, so it is O(n) although there is a nested loop."

> [!warning] Mistakes in this stage
> - `stack[len(stack)-1]` on an empty stack panics. Test `len(stack) > 0` first, on the left of `&&`.
> - `stack[:len(stack)-1]` alone does not pop. Assign the result: `stack = stack[:len(stack)-1]`.
> - In Go, `/` on two ints truncates toward zero, and `float64(a) / float64(b)` keeps the fraction. Convert before you divide.
> - A `[]byte` path in a recursion is shared memory. Append `string(path)` to the result, not the slice.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 20. Valid Parentheses

[LeetCode 20](https://leetcode.com/problems/valid-parentheses/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Matching stack
> - **Template:** [[#Template A: Matching stack|A: Matching stack]]

> [!tip]- Step 2: the idea
> **Idea.** Push each opener. A closer must match the opener on the top, because the most recent opener closes first. At the end the stack must be empty.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** A `[]byte` slice is the stack. `append` pushes, and `stack[:len(stack)-1]` pops. A map lookup with two results tells if the key is in the map.

> [!example]- Step 3: the Go solution
> ```go
> // isValid solves LC 20. Time O(n), space O(n).
> // The most recent opener must close first, and that is the top of a
> // stack.
> func isValid(s string) bool {
>     // closer -> its opener
>     pairs := map[byte]byte{')': '(', ']': '[', '}': '{'}
>     // the openers that wait
>     stack := []byte{}
>     for i := 0; i < len(s); i++ {
>         c := s[i]
>         // isCloser is true when c is a key of the map
>         open, isCloser := pairs[c]
>         if !isCloser {
>             stack = append(stack, c) // PUSH an opener
>             continue
>         }
>         // MATCH: the top must be the opener of this closer.
>         // The len test comes first, so an empty stack causes no
>         // panic.
>         if len(stack) == 0 || stack[len(stack)-1] != open {
>             return false
>         }
>         stack = stack[:len(stack)-1] // POP the opener
>     }
>     // LEFTOVER openers make the string not valid
>     return len(stack) == 0
> }
> ```

### 155. Min Stack

[LeetCode 155](https://leetcode.com/problems/min-stack/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Paired stack
> - **Template:** [[#Template B: Paired stack|B: Paired stack]]

> [!tip]- Step 2: the idea
> **Idea.** Keep a second stack with the same height. Its top is the minimum of all the values that are in the first stack now. A pop removes one item from each stack, so the minimum from before comes back with no search.
>
> **Complexity.** Time O(1) for each operation, space O(n).
>
> **Go lesson.** LeetCode names the receiver `this`. A pointer receiver, `*MinStack`, lets a method change the struct. `MinStack{}` is ready to use, because `append` works on a nil slice.

> [!example]- Step 3: the Go solution
> ```go
> // MinStack solves LC 155. Time O(1) for each operation, space O(n).
> // mins[i] is the minimum of vals[0..i], so the two slices always
> // have the
> // same length.
> type MinStack struct {
>     vals []int // the values
>     mins []int // mins[i]: the minimum of vals[0..i]
> }
>
> // Constructor returns an empty stack. The two slices start as nil.
> func Constructor() MinStack {
>     return MinStack{}
> }
>
> func (this *MinStack) Push(val int) {
>     low := val
>     if len(this.mins) > 0 {
>         // compare with the minimum below
>         low = min(low, this.mins[len(this.mins)-1])
>     }
>     this.vals = append(this.vals, val) // PUSH BOTH
>     this.mins = append(this.mins, low)
> }
>
> func (this *MinStack) Pop() {
>     // POP BOTH: the minimum from before is on top
>     this.vals = this.vals[:len(this.vals)-1]
>     this.mins = this.mins[:len(this.mins)-1]
> }
>
> func (this *MinStack) Top() int {
>     return this.vals[len(this.vals)-1]
> }
>
> func (this *MinStack) GetMin() int {
>     // READ THE TOP of the second stack
>     return this.mins[len(this.mins)-1]
> }
> ```

### 150. Evaluate Reverse Polish Notation

[LeetCode 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Stack as evaluator
> - **Template:** [[#Template C: Stack as evaluator|C: Stack as evaluator]]

> [!tip]- Step 2: the idea
> **Idea.** A number waits on the stack. An operator uses the two most recent results, so pop two values, apply the operator, and push the result. The last value on the stack is the answer.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** `strconv.Atoi` returns a value and an error. An error that is not nil means that the token is an operator. Integer division in Go truncates toward zero, which is the rule of this problem.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `strconv`
>
> ```go
> // evalRPN solves LC 150. Time O(n), space O(n).
> // In postfix notation an operator comes after its two operands.
> func evalRPN(tokens []string) int {
>     // the results that wait for an operator
>     stack := make([]int, 0, len(tokens))
>     for _, tok := range tokens {
>         // Atoi parses "-11" as a number. It fails on "-", so "-" is
>         // an
>         // operator.
>         if n, err := strconv.Atoi(tok); err == nil {
>             stack = append(stack, n) // PUSH a number
>             continue
>         }
>         // POP TWO: the top is the RIGHT operand
>         b := stack[len(stack)-1]
>         // the value below it is the left operand
>         a := stack[len(stack)-2]
>         stack = stack[:len(stack)-2]
>         var res int
>         switch tok { // APPLY the operator
>         case "+":
>             res = a + b
>         case "-":
>             res = a - b // the order matters: a - b, not b - a
>         case "*":
>             res = a * b
>         case "/":
>             res = a / b // integer division truncates toward zero
>         }
>         stack = append(stack, res) // PUSH the result
>     }
>     return stack[0] // a valid expression leaves one value
> }
> ```

### 22. Generate Parentheses

[LeetCode 22](https://leetcode.com/problems/generate-parentheses/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Backtracking with counters
> - **Template:** [[#Template D: Backtracking with counters|D: Backtracking with counters]]

> [!tip]- Step 2: the idea
> **Idea.** Build the string one character at a time. Add `(` while fewer than n are open. Add `)` only while it has an opener to close. With these two rules, each string that reaches length 2n is valid.
>
> **Complexity.** Time O(4ⁿ / √n) strings, and each string costs O(n) to copy, space O(n) for the recursion, plus the output.
>
> **Go lesson.** A function literal that calls itself needs a `var` declaration first. `string(path)` copies the bytes, so later changes to `path` do not change the result.

> [!example]- Step 3: the Go solution
> ```go
> // generateParenthesis solves LC 22. Time O(4ⁿ / √n) strings, space
> // O(n) for
> // the recursion.
> // Two counters keep each prefix valid, so no string needs a check
> // at the
> // end.
> func generateParenthesis(n int) []string {
>     res := []string{}
>     // the string that the recursion builds
>     path := make([]byte, 0, 2*n)
>
>     // Declare build first: the function body refers to its own
>     // name.
>     var build func(open, closed int)
>     // open and closed count the brackets in path
>     build = func(open, closed int) {
>         if len(path) == 2*n {
>             // RECORD: string(path) is a copy
>             res = append(res, string(path))
>             return
>         }
>         // an opener is permitted while fewer than n are used
>         if open < n {
>             path = append(path, '(')  // CHOOSE
>             build(open+1, closed)     // EXPLORE
>             path = path[:len(path)-1] // UNDO
>         }
>         // a closer is permitted only when an opener waits
>         if closed < open {
>             path = append(path, ')')
>             build(open, closed+1)
>             path = path[:len(path)-1]
>         }
>     }
>     build(0, 0)
>     return res
> }
> ```

### 739. Daily Temperatures

[LeetCode 739](https://leetcode.com/problems/daily-temperatures/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Monotonic stack
> - **Template:** [[#Template E: Monotonic stack|E: Monotonic stack]]

> [!tip]- Step 2: the idea
> **Idea.** A day waits on the stack until a warmer day comes. Each new day resolves all the colder days on the top of the stack. The stack holds indexes, so the answer is the difference of two indexes.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** `make([]int, n)` gives n zeros. Zero is the answer for a day with no warmer day, so the days that stay on the stack need no work.

> [!example]- Step 3: the Go solution
> ```go
> // dailyTemperatures solves LC 739. Time O(n), space O(n).
> // Each index enters the stack one time and leaves it one time at
> // most.
> func dailyTemperatures(temperatures []int) []int {
>     // zeros: "no warmer day" is the default
>     res := make([]int, len(temperatures))
>     // indexes of the days that wait for a warmer day
>     stack := []int{}
>     for i, t := range temperatures {
>         // RESOLVE: day i is the first warmer day for each colder
>         // day on the
>         // top.
>         for len(stack) > 0 && temperatures[stack[len(stack)-1]] < t {
>             j := stack[len(stack)-1]
>             // POP the day that has its answer
>             stack = stack[:len(stack)-1]
>             // the number of days between the two
>             res[j] = i - j
>         }
>         stack = append(stack, i) // PUSH: day i waits now
>     }
>     return res
> }
> ```

### 853. Car Fleet

[LeetCode 853](https://leetcode.com/problems/car-fleet/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Sort, then monotonic stack
> - **Template:** [[#Template E: Monotonic stack|E: Monotonic stack]]

> [!tip]- Step 2: the idea
> **Idea.** Find the time that each car needs to reach the target on an empty road. Sort the cars by position. A car that needs the same time or less than a car ahead of it catches that car and joins its fleet. The cars that stay on the stack lead the fleets.
>
> **Complexity.** Time O(n log n) for the sort, space O(n).
>
> **Go lesson.** `sort.Slice` sorts a slice of structs with a "less" function. `float64(x)` is necessary before the division, because the division of two ints drops the fraction.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `sort`
>
> ```go
> // carFleet solves LC 853. Time O(n log n), space O(n).
> // A car on the stack waits for a slower car ahead. If one comes,
> // the car
> // joins it.
> func carFleet(target int, position []int, speed []int) int {
>     type car struct {
>         pos  int
>         time float64 // hours to reach the target on an empty road
>     }
>     cars := make([]car, len(position))
>     for i := 0; i < len(position); i++ {
>         // Convert to float64 first: 7 / 2 is 3, and 7.0 / 2.0 is
>         // 3.5.
>         cars[i] = car{position[i], float64(target-position[i]) / float64(speed[i])}
>     }
>     // SORT by position: the car nearest to the start line comes
>     // first.
>     sort.Slice(cars, func(a, b int) bool { return cars[a].pos < cars[b].pos })
>
>     // times of the cars that wait: they decrease from the bottom up
>     stack := []float64{}
>     for _, c := range cars {
>         // RESOLVE: car c is ahead of the cars on the stack. A car
>         // behind
>         // that
>         // needs the same time or less catches c, so it joins the
>         // fleet of
>         // c.
>         for len(stack) > 0 && stack[len(stack)-1] <= c.time {
>             stack = stack[:len(stack)-1] // POP the car that joined
>         }
>         // PUSH: car c leads a fleet for now
>         stack = append(stack, c.time)
>     }
>     return len(stack) // each car that stays leads one fleet
> }
> ```

### 84. Largest Rectangle in Histogram

[LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/) · Hard

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Monotonic stack
> - **Template:** [[#Template E: Monotonic stack|E: Monotonic stack]]

> [!tip]- Step 2: the idea
> **Idea.** Each bar is the lowest bar of one largest rectangle. That rectangle goes from the first lower bar on the left to the first lower bar on the right. A lower bar on the right pops the bar, and the new top of the stack is the first lower bar on the left.
>
> **Complexity.** Time O(n), space O(n).
>
> **Go lesson.** The loop runs to `i == len(heights)` with a height of 0. That extra step resolves each bar that still waits, so no second loop is necessary.

> [!example]- Step 3: the Go solution
> ```go
> // largestRectangleArea solves LC 84. Time O(n), space O(n).
> // A bar waits on the stack until a lower bar comes on its right.
> func largestRectangleArea(heights []int) int {
>     best := 0
>     // indexes of the bars that wait: their heights increase from
>     // the bottom
>     // up
>     stack := []int{}
>     for i := 0; i <= len(heights); i++ {
>         // at i == len(heights): a bar of height 0 resolves all the
>         // bars
>         h := 0
>         if i < len(heights) {
>             h = heights[i]
>         }
>         // RESOLVE: bar i is the first lower bar on the right of the
>         // top.
>         for len(stack) > 0 && heights[stack[len(stack)-1]] > h {
>             top := stack[len(stack)-1]
>             // POP the bar that has its right border
>             stack = stack[:len(stack)-1]
>             // index of the first lower bar on the left
>             left := -1
>             if len(stack) > 0 {
>                 // the new top is that bar
>                 left = stack[len(stack)-1]
>             }
>             // the bars between left and i, without the two
>             width := i - left - 1
>             best = max(best, heights[top]*width)
>         }
>         stack = append(stack, i) // PUSH: bar i waits now
>     }
>     return best
> }
> ```

---

[[wiki/neetcode-150/03-sliding-window|← Sliding Window]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/05-binary-search|Binary Search →]]
