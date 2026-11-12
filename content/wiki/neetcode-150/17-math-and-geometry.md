---
title: "NeetCode 150, stage 17: Math and Geometry"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - math
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 17: Math and Geometry

[[wiki/neetcode-150/16-intervals|← Intervals]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/18-bit-manipulation|Bit Manipulation →]]

These problems have no special data structure. They train exact index work on a matrix and exact arithmetic on digits. A small error in a boundary or in a carry gives a wrong answer, so each template names its moves in a fixed order.

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/17-math-and-geometry#48. Rotate Image\|48. Rotate Image]] | Medium | Transpose, then reverse the rows | [[wiki/neetcode-150/17-math-and-geometry#Template A: Transpose, then reverse\|A: Transpose, then reverse]] |
| 2 | [[wiki/neetcode-150/17-math-and-geometry#54. Spiral Matrix\|54. Spiral Matrix]] | Medium | Four boundaries that shrink | [[wiki/neetcode-150/17-math-and-geometry#Template B: Four boundaries that shrink\|B: Four boundaries that shrink]] |
| 3 | [[wiki/neetcode-150/17-math-and-geometry#73. Set Matrix Zeroes\|73. Set Matrix Zeroes]] | Medium | First row and column as markers | [[wiki/neetcode-150/17-math-and-geometry#Template C: Markers in the first row and column\|C: Markers in the first row and column]] |
| 4 | [[wiki/neetcode-150/17-math-and-geometry#202. Happy Number\|202. Happy Number]] | Easy | Digit loop with cycle detection | [[wiki/neetcode-150/17-math-and-geometry#Template D: Digit loop with a carry\|D: Digit loop with a carry]] |
| 5 | [[wiki/neetcode-150/17-math-and-geometry#66. Plus One\|66. Plus One]] | Easy | Digit loop with a carry | [[wiki/neetcode-150/17-math-and-geometry#Template D: Digit loop with a carry\|D: Digit loop with a carry]] |
| 6 | [[wiki/neetcode-150/17-math-and-geometry#50. Pow(x, n)\|50. Pow(x, n)]] | Medium | Fast power by squaring | [[wiki/neetcode-150/17-math-and-geometry#Template E: Fast power by squaring\|E: Fast power by squaring]] |
| 7 | [[wiki/neetcode-150/17-math-and-geometry#43. Multiply Strings\|43. Multiply Strings]] | Medium | Grade-school multiplication with digits | [[wiki/neetcode-150/17-math-and-geometry#Template D: Digit loop with a carry\|D: Digit loop with a carry]] |
| 8 | [[wiki/neetcode-150/17-math-and-geometry#2013. Detect Squares\|2013. Detect Squares]] | Medium | Count map of points | [[wiki/neetcode-150/17-math-and-geometry#Template F: Count map of points\|F: Count map of points]] |

## Templates to memorize

### Template A: Transpose, then reverse

> [!tip] Signal
> The problem asks you to rotate a square matrix in place, with no second matrix.

```go
// TEMPLATE A: turn a square matrix 90 degrees to the right, in place.
func rotateRight(m [][]int) {
    n := len(m)
    for i := 0; i < n; i++ { // 1. TRANSPOSE: mirror on the main diagonal
        for j := i + 1; j < n; j++ { // j > i, or each pair swaps two times
            m[i][j], m[j][i] = m[j][i], m[i][j]
        }
    }
    for _, row := range m { // 2. REVERSE each row
        for l, r := 0, n-1; l < r; l, r = l+1, r-1 {
            row[l], row[r] = row[r], row[l]
        }
    }
}
```

The moves are TRANSPOSE, then REVERSE each row. In the transpose, start `j` at `i+1`. If `j` starts at 0, each pair swaps two times and the matrix does not change. For a turn to the left, reverse each column and not each row.

> [!quote] Say it
> "A 90 degree turn to the right is a transpose followed by a reverse of each row. Both are in-place swaps, so it's O(n²) time and O(1) space."

### Template B: Four boundaries that shrink

> [!tip] Signal
> The problem asks for the cells of a matrix in spiral order, or layer by layer from the outside.

```go
// TEMPLATE B: four boundaries. Walk one side, then move its boundary in.
func spiral(m [][]int) []int {
    top, bottom := 0, len(m)-1
    left, right := 0, len(m[0])-1
    res := make([]int, 0, len(m)*len(m[0]))
    for top <= bottom && left <= right {
        for c := left; c <= right; c++ { // 1. RIGHT on the top row
            res = append(res, m[top][c])
        }
        top++
        for r := top; r <= bottom; r++ { // 2. DOWN on the right column
            res = append(res, m[r][right])
        }
        right--
        if top <= bottom { // CHECK AGAIN: a row is left
            for c := right; c >= left; c-- { // 3. LEFT on the bottom row
                res = append(res, m[bottom][c])
            }
            bottom--
        }
        if left <= right { // CHECK AGAIN: a column is left
            for r := bottom; r >= top; r-- { // 4. UP on the left column
                res = append(res, m[r][left])
            }
            left++
        }
    }
    return res
}
```

The moves are RIGHT, DOWN, LEFT, UP, and each one moves its boundary in. Before LEFT and before UP, do the CHECK AGAIN. Without it, a matrix with one row or one column gives the same cells two times.

> [!quote] Say it
> "I keep top, bottom, left and right. I walk one side, pull that boundary in, and stop when the boundaries cross. Every cell is read once, so it's O(m times n)."

### Template C: Markers in the first row and column

> [!tip] Signal
> You must record a fact for each row and each column, and the problem asks for O(1) extra space.

```go
// TEMPLATE C: the first row and the first column hold the markers.
func zeroRowsAndCols(m [][]int) {
    rows, cols := len(m), len(m[0])
    // 1. SAVE: is a zero in the first row or column?
    rowZero, colZero := false, false
    for c := 0; c < cols; c++ {
        rowZero = rowZero || m[0][c] == 0
    }
    for r := 0; r < rows; r++ {
        colZero = colZero || m[r][0] == 0
    }
    // 2. MARK: a zero marks the start of its row and column
    for r := 1; r < rows; r++ {
        for c := 1; c < cols; c++ {
            if m[r][c] == 0 {
                m[r][0], m[0][c] = 0, 0
            }
        }
    }
    for r := 1; r < rows; r++ { // 3. APPLY the markers to the inner cells
        for c := 1; c < cols; c++ {
            if m[r][0] == 0 || m[0][c] == 0 {
                m[r][c] = 0
            }
        }
    }
    if rowZero { // 4. LAST: the first row, then the first column
        for c := 0; c < cols; c++ {
            m[0][c] = 0
        }
    }
    if colZero {
        for r := 0; r < rows; r++ {
            m[r][0] = 0
        }
    }
}
```

The moves are SAVE, MARK, APPLY, then LAST. The first row and the first column are the marker memory. Save two flags before you mark, because the markers overwrite those two lines. Set the first row and the first column last.

> [!quote] Say it
> "I use the first row and the first column as my marker arrays, plus two flags for those two lines themselves. That brings the extra space from O(m plus n) down to O(1)."

### Template D: Digit loop with a carry

> [!tip] Signal
> The problem works on the digits of a number. The number is an `int`, a slice of digits or a string that is too long for an `int`.

```go
// TEMPLATE D: digit loop. n % 10 reads the last digit, and n / 10 removes
// it.
func digitSum(n int) int {
    sum := 0
    for n > 0 {
        sum += n % 10 // 1. POP: read the last digit
        n /= 10       // 2. DROP: remove it
    }
    return sum
}

// With a slice of digits, start at the last digit and move a carry to the
// left.
// addDigit adds a one-digit number k to the number in digits.
func addDigit(digits []int, k int) []int {
    carry := k
    for i := len(digits) - 1; i >= 0 && carry > 0; i-- {
        sum := digits[i] + carry
        digits[i] = sum % 10 // KEEP one digit
        carry = sum / 10     // CARRY the rest to the left
    }
    if carry > 0 { // the number has one more digit now
        digits = append([]int{carry}, digits...)
    }
    return digits
}
```

The moves are POP and DROP for an `int`. The moves are KEEP and CARRY for a slice of digits. Go from the last digit to the first, because the carry moves to the left. After the loop, check if a carry is left.

> [!quote] Say it
> "Mod 10 gives me the last digit and divide by 10 removes it. With digit arrays I work right to left and push the carry along."

### Template E: Fast power by squaring

> [!tip] Signal
> The problem asks for a power with a large exponent. A loop that multiplies `n` times is too slow.

```go
// TEMPLATE E: fast power. Read the bits of n. Needs n >= 0.
func power(x float64, n int) float64 {
    res := 1.0
    for n > 0 {
        if n&1 == 1 { // 1. USE this power when the lowest bit of n is 1
            res *= x
        }
        x *= x  // 2. SQUARE: x, x², x⁴, x⁸ and so on
        n >>= 1 // 3. HALVE: drop the lowest bit
    }
    return res
}
```

The moves are USE, SQUARE, then HALVE. The loop reads the bits of `n` from the lowest bit. It runs about 31 times for a 32-bit exponent and not 2 billion times. For a negative exponent, change `x` to `1/x` first.

> [!quote] Say it
> "I square the base and halve the exponent, and I multiply the result in whenever the current bit is set. That's O(log n) multiplications."

### Template F: Count map of points

> [!tip] Signal
> A design problem adds points and then asks how many shapes a query point makes. The same point can come more than one time.

```go
// TEMPLATE F: count map of points. The key is the array [2]int{x, y}.
type pointCounter struct {
    count map[[2]int]int
}

func newPointCounter() *pointCounter {
    return &pointCounter{count: make(map[[2]int]int)}
}

func (pc *pointCounter) add(x, y int) {
    pc.count[[2]int{x, y}]++ // 1. COUNT: a duplicate is one more point
}

// squaresAt counts the axis-aligned squares with a corner at (x, y).
func (pc *pointCounter) squaresAt(x, y int) int {
    total := 0
    // 2. DIAGONAL: each stored point is a candidate
    for p, c := range pc.count {
        dx, dy := p[0]-x, p[1]-y
        if dx == 0 || (dx != dy && dx != -dy) {
            continue // not on a diagonal, or a square with no area
        }
        // 3. LOOK UP the two other corners and MULTIPLY the counts.
        total += c * pc.count[[2]int{x, p[1]}] * pc.count[[2]int{p[0], y}]
    }
    return total
}
```

The moves are COUNT, DIAGONAL, LOOK UP, then MULTIPLY. Two corners on a diagonal fix the full square, so the loop needs only one stored point. The map gives the counts of the two other corners in O(1).

> [!quote] Say it
> "I store a count per point. For a query I try every stored point as the diagonal corner, look up the other two corners, and multiply the three counts."

> [!warning] Mistakes in this stage
> - `row := matrix[i]` is not a copy. The row shares its memory with the matrix, so a write to `row` changes the matrix.
> - A slice cannot be a map key. Use the array `[2]int{x, y}` for a point.
> - In Go, `-7 % 10` is `-3` and `-7 / 10` is `0`. The remainder has the sign of the first number.
> - `num[i]` of a string is a byte with an ASCII code. Subtract `'0'` and convert to `int` before you multiply.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 48. Rotate Image

[LeetCode 48](https://leetcode.com/problems/rotate-image/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Transpose, then reverse the rows
> - **Template:** [[#Template A: Transpose, then reverse|A: Transpose, then reverse]]

> [!tip]- Step 2: the idea
> **Idea.** A turn of 90 degrees to the right is two simple steps. First mirror the matrix on its main diagonal. Then reverse each row.
>
> **Complexity.** Time O(n²), space O(1).
>
> **Go lesson.** A tuple assignment such as `a, b = b, a` swaps two values with no temporary variable. A row is a slice that shares its memory with the matrix, so a write to `row` changes the matrix.

> [!example]- Step 3: the Go solution
> ```go
> // rotate solves LC 48. Time O(n²), space O(1).
> // It changes the matrix in place, so it returns nothing.
> func rotate(matrix [][]int) {
>     n := len(matrix)
>     // TRANSPOSE: swap matrix[i][j] with matrix[j][i]. Rows become
>     // columns.
>     for i := 0; i < n; i++ {
>         // j starts at i+1: only the cells above the diagonal.
>         // With j from 0, each pair swaps two times and nothing
>         // changes.
>         for j := i + 1; j < n; j++ {
>             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
>         }
>     }
>     // REVERSE each row with two indexes that move to the middle.
>     // row shares its memory with the matrix
>     for _, row := range matrix {
>         for l, r := 0, n-1; l < r; l, r = l+1, r-1 {
>             row[l], row[r] = row[r], row[l]
>         }
>     }
> }
> ```

### 54. Spiral Matrix

[LeetCode 54](https://leetcode.com/problems/spiral-matrix/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Four boundaries that shrink
> - **Template:** [[#Template B: Four boundaries that shrink|B: Four boundaries that shrink]]

> [!tip]- Step 2: the idea
> **Idea.** Keep four boundaries: top, bottom, left and right. Walk one side of the rectangle, then move that boundary in. Stop when the boundaries cross.
>
> **Complexity.** Time O(m * n) for m rows and n columns, space O(1) without the result.
>
> **Go lesson.** `make([]int, 0, size)` gives length 0 and a known capacity, so `append` never copies the slice.

> [!example]- Step 3: the Go solution
> ```go
> // spiralOrder solves LC 54. Time O(m * n), space O(1) without the
> // result.
> // Each turn of the loop walks one layer: right, down, left, then
> // up.
> func spiralOrder(matrix [][]int) []int {
>     top, bottom := 0, len(matrix)-1
>     left, right := 0, len(matrix[0])-1
>     // length 0, capacity m*n
>     res := make([]int, 0, len(matrix)*len(matrix[0]))
>
>     for top <= bottom && left <= right { // some cells are left
>         // WALK RIGHT on the top row
>         for c := left; c <= right; c++ {
>             res = append(res, matrix[top][c])
>         }
>         top++ // SHRINK: the top row is done
>
>         // WALK DOWN on the right column
>         for r := top; r <= bottom; r++ {
>             res = append(res, matrix[r][right])
>         }
>         right-- // SHRINK: the right column is done
>
>         // CHECK AGAIN: top and right changed. If only one row or
>         // one column
>         // was left, the walk back must not read it a second time.
>         if top <= bottom {
>             // WALK LEFT on the bottom row
>             for c := right; c >= left; c-- {
>                 res = append(res, matrix[bottom][c])
>             }
>             bottom--
>         }
>         if left <= right {
>             // WALK UP on the left column
>             for r := bottom; r >= top; r-- {
>                 res = append(res, matrix[r][left])
>             }
>             left++
>         }
>     }
>     return res
> }
> ```

### 73. Set Matrix Zeroes

[LeetCode 73](https://leetcode.com/problems/set-matrix-zeroes/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** First row and column as markers
> - **Template:** [[#Template C: Markers in the first row and column|C: Markers in the first row and column]]

> [!tip]- Step 2: the idea
> **Idea.** Use the first row and the first column of the matrix as the marker memory. Save two flags first, because the markers overwrite those two lines. Set the first row and the first column last.
>
> **Complexity.** Time O(m * n) for m rows and n columns, space O(1).

> [!example]- Step 3: the Go solution
> ```go
> // setZeroes solves LC 73. Time O(m * n), space O(1).
> // matrix[r][0] == 0 means "set row r to zero".
> // matrix[0][c] == 0 means "set column c to zero".
> func setZeroes(matrix [][]int) {
>     rows, cols := len(matrix), len(matrix[0])
>
>     // SAVE: does the first row or the first column have a zero of
>     // its own?
>     // The markers overwrite these two lines, so read them before
>     // the marks.
>     firstRowZero, firstColZero := false, false
>     for c := 0; c < cols; c++ {
>         if matrix[0][c] == 0 {
>             firstRowZero = true
>         }
>     }
>     for r := 0; r < rows; r++ {
>         if matrix[r][0] == 0 {
>             firstColZero = true
>         }
>     }
>
>     // MARK: a zero in an inner cell marks the start of its row and
>     // its
>     // column.
>     for r := 1; r < rows; r++ {
>         for c := 1; c < cols; c++ {
>             if matrix[r][c] == 0 {
>                 matrix[r][0] = 0
>                 matrix[0][c] = 0
>             }
>         }
>     }
>
>     // APPLY: an inner cell becomes zero when its row or its column
>     // has a
>     // marker.
>     for r := 1; r < rows; r++ {
>         for c := 1; c < cols; c++ {
>             if matrix[r][0] == 0 || matrix[0][c] == 0 {
>                 matrix[r][c] = 0
>             }
>         }
>     }
>
>     // LAST: the first row and the first column. If you set them
>     // earlier,
>     // the APPLY step reads them as markers and sets too many cells.
>     if firstRowZero {
>         for c := 0; c < cols; c++ {
>             matrix[0][c] = 0
>         }
>     }
>     if firstColZero {
>         for r := 0; r < rows; r++ {
>             matrix[r][0] = 0
>         }
>     }
> }
> ```

### 202. Happy Number

[LeetCode 202](https://leetcode.com/problems/happy-number/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Digit loop with cycle detection
> - **Template:** [[#Template D: Digit loop with a carry|D: Digit loop with a carry]]

> [!tip]- Step 2: the idea
> **Idea.** Replace the number with the sum of the squares of its digits, again and again. The values either reach 1 or go around a cycle. A set of the values that you saw finds the cycle.
>
> **Complexity.** Time O(log n), space O(log n).
>
> **Go lesson.** Go has no set type. A `map[int]struct{}` is the set, and the "comma ok" form tests membership.

> [!example]- Step 3: the Go solution
> ```go
> // isHappy solves LC 202. Time O(log n), space O(log n).
> // For a 32-bit input the first sum is below 1000, so the set stays
> // small.
> // The fast and slow pointers of the linked-list cycle problem also
> // work,
> // with O(1) space.
> func isHappy(n int) bool {
>     // the values that the loop already visited
>     seen := make(map[int]struct{})
>     for n != 1 {
>         // CYCLE: this value came back, so 1 never comes
>         if _, ok := seen[n]; ok {
>             return false
>         }
>         seen[n] = struct{}{}
>         n = sumOfSquares(n) // NEXT value
>     }
>     return true
> }
>
> // sumOfSquares returns the sum of the squares of the digits of n.
> func sumOfSquares(n int) int {
>     sum := 0
>     for n > 0 {
>         digit := n % 10 // POP: the last digit
>         n /= 10         // DROP: remove the last digit
>         sum += digit * digit
>     }
>     return sum
> }
> ```

### 66. Plus One

[LeetCode 66](https://leetcode.com/problems/plus-one/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Digit loop with a carry
> - **Template:** [[#Template D: Digit loop with a carry|D: Digit loop with a carry]]

> [!tip]- Step 2: the idea
> **Idea.** Add one at the last digit. A digit below 9 takes the one and the work stops. A 9 becomes 0 and the carry moves to the left. If all the digits are 9, the result is a 1 and then zeros.
>
> **Complexity.** Time O(n), space O(1), or O(n) when all the digits are 9.
>
> **Go lesson.** `make([]int, n)` gives a slice of `n` zeros. So the "all nines" result needs only one write.

> [!example]- Step 3: the Go solution
> ```go
> // plusOne solves LC 66. Time O(n), space O(1) when some digit is
> // not 9.
> func plusOne(digits []int) []int {
>     // from the last digit to the first
>     for i := len(digits) - 1; i >= 0; i-- {
>         if digits[i] < 9 {
>             digits[i]++   // no carry: this digit takes the one
>             return digits // the digits on the left do not change
>         }
>         digits[i] = 0 // 9 + 1 = 10: KEEP 0 and CARRY 1 to the left
>     }
>     // The loop ended, so each digit was 9. For example 999 + 1 =
>     // 1000.
>     res := make([]int, len(digits)+1) // one more digit, all zeros
>     res[0] = 1
>     return res
> }
> ```

### 50. Pow(x, n)

[LeetCode 50](https://leetcode.com/problems/powx-n/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Fast power by squaring
> - **Template:** [[#Template E: Fast power by squaring|E: Fast power by squaring]]

> [!tip]- Step 2: the idea
> **Idea.** Read the exponent bit by bit. Square x at each step to get x, x², x⁴ and so on. Multiply the result by the current power when the bit is 1. A negative exponent uses 1/x.
>
> **Complexity.** Time O(log n), space O(1).
>
> **Go lesson.** Go's `int` has 64 bits on LeetCode, so `-n` is safe for n = -2³¹. In a 32-bit language this line overflows.

> [!example]- Step 3: the Go solution
> ```go
> // myPow solves LC 50. Time O(log n), space O(1).
> // Example: x¹³ = x⁸ * x⁴ * x¹, because 13 is 1101 in binary.
> func myPow(x float64, n int) float64 {
>     if n < 0 { // NEGATIVE exponent: x^(-n) is (1/x)^n
>         x = 1 / x
>         n = -n // safe: int has 64 bits, and n is at least -2³¹
>     }
>     res := 1.0 // 1.0 is a float64 constant. x⁰ is 1
>     for n > 0 {
>         // USE: the lowest bit of n is 1, so this power is in the
>         // answer
>         if n&1 == 1 {
>             res *= x
>         }
>         x *= x  // SQUARE: the power for the next bit
>         n >>= 1 // HALVE: drop the lowest bit
>     }
>     return res
> }
> ```

### 43. Multiply Strings

[LeetCode 43](https://leetcode.com/problems/multiply-strings/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Grade-school multiplication with digits
> - **Template:** [[#Template D: Digit loop with a carry|D: Digit loop with a carry]]

> [!tip]- Step 2: the idea
> **Idea.** Multiply each pair of digits, as on paper. The product of the digits at i and j goes to the positions i+j and i+j+1 of the result. Keep one digit with % 10 and carry the rest with / 10.
>
> **Complexity.** Time O(m * n) for m and n digits, space O(m + n).
>
> **Go lesson.** `num1[i]` is a byte with the ASCII code of the digit. `int(num1[i]-'0')` gives its value. Build the result as a `[]byte` and convert it to a string one time at the end.

> [!example]- Step 3: the Go solution
> ```go
> // multiply solves LC 43. Time O(m * n), space O(m + n).
> // It never converts the full input to an integer: the inputs have
> // up to 200
> // digits.
> func multiply(num1 string, num2 string) string {
>     // without this, the result is "000"
>     if num1 == "0" || num2 == "0" {
>         return "0"
>     }
>     m, n := len(num1), len(num2)
>     // m digits times n digits has at most m+n digits
>     res := make([]int, m+n)
>
>     // from the last digit of each number
>     for i := m - 1; i >= 0; i-- {
>         for j := n - 1; j >= 0; j-- {
>             product := int(num1[i]-'0') * int(num2[j]-'0')
>             // ADD what the low position already holds
>             sum := product + res[i+j+1]
>             // KEEP one digit in the low position
>             res[i+j+1] = sum % 10
>             // CARRY the rest to the position on the left
>             res[i+j] += sum / 10
>         }
>     }
>
>     start := 0
>     // SKIP: the product has only m+n-1 digits, so res[0] is a
>     // leading zero
>     if res[0] == 0 {
>         start = 1
>     }
>     out := make([]byte, 0, m+n)
>     for _, d := range res[start:] {
>         // the digit 7 becomes the character '7'
>         out = append(out, byte(d)+'0')
>     }
>     return string(out)
> }
> ```

### 2013. Detect Squares

[LeetCode 2013](https://leetcode.com/problems/detect-squares/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Count map of points
> - **Template:** [[#Template F: Count map of points|F: Count map of points]]

> [!tip]- Step 2: the idea
> **Idea.** Count how many times each point was added. For a query, each stored point on a diagonal fixes one square. Look up the other two corners and multiply the three counts.
>
> **Complexity.** Time O(1) for Add, O(p) for Count with p distinct points, space O(p).
>
> **Go lesson.** An array such as `[2]int` can be a map key, and a slice cannot. A read of a missing key gives 0 and adds no entry, so it is safe inside a `range` over the map.

> [!example]- Step 3: the Go solution
> ```go
> // DetectSquares solves LC 2013. Add is O(1). Count is O(p) for p
> // distinct
> // points.
> type DetectSquares struct {
>     // the point (x, y) -> how many times it was added
>     count map[[2]int]int
> }
>
> func Constructor() DetectSquares {
>     // a nil map panics on a write
>     return DetectSquares{count: make(map[[2]int]int)}
> }
>
> // Add stores one more copy of the point.
> func (this *DetectSquares) Add(point []int) {
>     // COUNT: duplicates are different points
>     this.count[[2]int{point[0], point[1]}]++
> }
>
> // Count returns the number of squares with one corner at the query
> // point.
> func (this *DetectSquares) Count(point []int) int {
>     x, y := point[0], point[1]
>     total := 0
>     // p is a candidate for the DIAGONAL corner
>     for p, c := range this.count {
>         px, py := p[0], p[1]
>         // The diagonal corner of a square is as far in x as in y.
>         // px == x gives a square with no area, so skip it.
>         if px == x || abs(px-x) != abs(py-y) {
>             continue
>         }
>         // LOOK UP the two other corners: (x, py) and (px, y).
>         // MULTIPLY: each copy of each corner gives a different
>         // square.
>         total += c * this.count[[2]int{x, py}] * this.count[[2]int{px, y}]
>     }
>     return total
> }
>
> // abs returns the absolute value. The math package has only a
> // float64
> // version.
> func abs(a int) int {
>     if a < 0 {
>         return -a
>     }
>     return a
> }
> ```

---

[[wiki/neetcode-150/16-intervals|← Intervals]] · [[wiki/neetcode-150/index|All 150 problems]] · [[wiki/neetcode-150/18-bit-manipulation|Bit Manipulation →]]
