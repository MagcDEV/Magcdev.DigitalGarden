---
title: "NeetCode 150, stage 18: Bit Manipulation"
tags:
  - wiki
  - neetcode-150
  - leetcode
  - go
  - patterns
  - templates
  - bit-manipulation
date_created: 2026-11-11
date_modified: 2026-11-12
---

# NeetCode 150, stage 18: Bit Manipulation

[[wiki/neetcode-150/17-math-and-geometry|← Math and Geometry]] · [[wiki/neetcode-150/index|All 150 problems]]

An integer is a row of bits, and a few operators change those bits directly. This stage trains five small tricks with XOR, AND and the shifts, and one digit loop that stays in the 32-bit range. Each trick is a short loop, so you must know why it works and not only its code.

## Problems on this page

| # | Problem | Level | Pattern | Template |
|---|---|---|---|---|
| 1 | [[wiki/neetcode-150/18-bit-manipulation#136. Single Number\|136. Single Number]] | Easy | XOR cancels pairs | [[wiki/neetcode-150/18-bit-manipulation#Template A: XOR cancels pairs\|A: XOR cancels pairs]] |
| 2 | [[wiki/neetcode-150/18-bit-manipulation#191. Number of 1 Bits\|191. Number of 1 Bits]] | Easy | Remove the lowest set bit | [[wiki/neetcode-150/18-bit-manipulation#Template B: Remove the lowest set bit\|B: Remove the lowest set bit]] |
| 3 | [[wiki/neetcode-150/18-bit-manipulation#338. Counting Bits\|338. Counting Bits]] | Easy | DP on bits | [[wiki/neetcode-150/18-bit-manipulation#Template C: DP on bits\|C: DP on bits]] |
| 4 | [[wiki/neetcode-150/18-bit-manipulation#190. Reverse Bits\|190. Reverse Bits]] | Easy | Shift in and shift out | [[wiki/neetcode-150/18-bit-manipulation#Template D: Shift in and shift out\|D: Shift in and shift out]] |
| 5 | [[wiki/neetcode-150/18-bit-manipulation#268. Missing Number\|268. Missing Number]] | Easy | XOR of indexes and values | [[wiki/neetcode-150/18-bit-manipulation#Template A: XOR cancels pairs\|A: XOR cancels pairs]] |
| 6 | [[wiki/neetcode-150/18-bit-manipulation#371. Sum of Two Integers\|371. Sum of Two Integers]] | Medium | Add with XOR and carry | [[wiki/neetcode-150/18-bit-manipulation#Template E: Add with XOR and carry\|E: Add with XOR and carry]] |
| 7 | [[wiki/neetcode-150/18-bit-manipulation#7. Reverse Integer\|7. Reverse Integer]] | Medium | Digit loop with an overflow check | [[wiki/neetcode-150/18-bit-manipulation#Template F: Digit loop with an overflow check\|F: Digit loop with an overflow check]] |

## Templates to memorize

### Template A: XOR cancels pairs

> [!tip] Signal
> Each value appears two times, and one value appears only one time. Or one number of a full range is missing. The problem asks for O(1) extra space, so a hash map is not permitted.

```go
// TEMPLATE A: XOR cancels pairs. x ^ x == 0, x ^ 0 == x, and the order does
// not matter.
func xorAll(nums []int) int {
    res := 0 // 1. START at 0, the value that changes nothing
    for _, x := range nums {
        res ^= x // 2. FOLD: the second copy of a value removes the first
    }
    return res // only the value with no partner is left
}

// To find the missing number of 0..n, the indexes are the partners:
// start at n, and fold each index with each value.
func missingFromRange(nums []int) int {
    res := len(nums)
    for i, x := range nums {
        res ^= i ^ x
    }
    return res
}
```

The moves are START at 0, then FOLD each value with XOR. Equal values cancel, and the order does not matter. For a missing number, the indexes are the partners of the values. Start at `n`, because the loop does not give the index `n`.

> [!quote] Say it
> "XOR of a number with itself is zero, so every pair cancels and the single one is left. One pass, O(n) time and O(1) space."

### Template B: Remove the lowest set bit

> [!tip] Signal
> The problem counts the 1 bits of a number, or asks if a number is a power of two.

```go
// TEMPLATE B: n & (n-1) removes the lowest set bit. 1100 & 1011 == 1000.
func countSetBits(n int) int {
    count := 0
    for n != 0 {
        n &= n - 1 // 1. REMOVE the lowest set bit
        count++    // 2. COUNT the removal
    }
    return count
}

// A power of two has exactly one set bit, so one removal gives 0.
func isPowerOfTwo(n int) bool {
    return n > 0 && n&(n-1) == 0
}
```

The moves are REMOVE, then COUNT. The subtraction `n - 1` changes the lowest 1 bit to 0 and the zeros after it to 1. The AND then clears all those positions. The loop runs one time for each set bit, not one time for each bit.

> [!quote] Say it
> "n and n minus one clears the lowest set bit, so the loop runs once per set bit instead of 32 times."

### Template C: DP on bits

> [!tip] Signal
> The problem asks for the bit count of each number from 0 to n, in O(n) time.

```go
// TEMPLATE C: DP on bits. The answer for i comes from a smaller number.
func bitCounts(n int) []int {
    bits := make([]int, n+1) // 1. BASE: bits[0] == 0
    for i := 1; i <= n; i++ {
        // 2. REUSE the answer for i >> 1, which is i with no last bit.
        // 3. ADD the last bit, i & 1.
        bits[i] = bits[i>>1] + (i & 1)
    }
    return bits
}
```

The moves are BASE, REUSE, then ADD. The number `i >> 1` is `i` with no last bit, and it is smaller than `i`. So its answer is already in the slice. Add `i & 1`, which is the last bit.

> [!quote] Say it
> "The bit count of i is the bit count of i shifted right by one, plus its last bit. That's one lookup per number, so O(n) in total."

### Template D: Shift in and shift out

> [!tip] Signal
> The problem asks you to reverse the bits of a number, or to build a number from the bits of a second number.

```go
// TEMPLATE D: shift in and shift out. Move the bits from n to res, one at a
// time.
func reverse32(n uint32) uint32 {
    var res uint32
    for i := 0; i < 32; i++ { // a fixed count: the leading zeros move too
        // 1. SHIFT IN: make room, then take the last bit of n
        res = res<<1 | n&1
        n >>= 1 // 2. SHIFT OUT: drop that bit from n
    }
    return res
}
```

The moves are SHIFT IN, then SHIFT OUT. Use a fixed count of 32 steps and not `for n != 0`. If the loop stops early, the leading zeros of `n` do not move to the result.

> [!quote] Say it
> "I pop the lowest bit of n and push it onto the result, 32 times. The first bit out ends up as the highest bit."

### Template E: Add with XOR and carry

> [!tip] Signal
> The problem asks for a sum, and the operators `+` and `-` are not permitted.

```go
// TEMPLATE E: add with XOR and carry, on 32 bits.
func addBits(a, b uint32) uint32 {
    for b != 0 { // b is the carry that is not yet added
        // 1. CARRY: where the two bits are 1, moved left
        carry := (a & b) << 1
        a ^= b    // 2. SUM of the bits with no carry
        b = carry // 3. REPEAT until no carry is left
    }
    return a
}
```

The moves are CARRY, SUM, then REPEAT. XOR is addition with no carry. AND finds the carry, and the shift moves it one position to the left. In Go, do the loop on `uint32` and convert the result with `int(int32(x))`.

> [!quote] Say it
> "XOR adds without carrying, AND shifted left is the carry, and I repeat until the carry is zero. On 32 bits that's at most 32 rounds."

### Template F: Digit loop with an overflow check

> [!tip] Signal
> The problem builds a number digit by digit, and the result must stay in the 32-bit range. The problem says that 64-bit storage is not permitted.

```go
// TEMPLATE F: digit loop with an overflow check. Build a number digit by
// digit
// and stay in the int32 range. Returns 0 when the result does not fit.
func reverseDigits(x int) int {
    res := 0
    for x != 0 {
        digit := x % 10 // 1. POP the last digit (it has the sign of x)
        x /= 10
        // 2. CHECK before the multiplication, with the limit divided by 10.
        if res > math.MaxInt32/10 || (res == math.MaxInt32/10 && digit > math.MaxInt32%10) {
            return 0
        }
        if res < math.MinInt32/10 || (res == math.MinInt32/10 && digit < math.MinInt32%10) {
            return 0
        }
        res = res*10 + digit // 3. PUSH the digit
    }
    return res
}
```

The moves are POP, CHECK, then PUSH. Do the check before the multiplication, and compare with the limit divided by 10. A check after the multiplication is too late in a 32-bit language, because the value already wrapped around.

> [!quote] Say it
> "Before I multiply by ten I compare the result with MaxInt32 over ten, so the overflow never happens. It's the usual pop and push digit loop."

> [!warning] Mistakes in this stage
> - Go has no `~` operator. Write `^x` for NOT, and `a &^ b` for "a AND NOT b".
> - `&` and `<<` have a higher precedence than `+` in Go, and in C they are lower. Add parentheses when you mix them.
> - `>>` on a negative `int` keeps the sign bit. So the loop `for n != 0 { n >>= 1 }` never stops for a negative `n`.
> - Go's `int` has 64 bits on LeetCode. A 32-bit overflow does not occur by itself, so convert through `uint32` and `int32` when the problem needs it.

## Solved with comments

Each problem hides its answer in three steps, so the page works as a test. Read the problem on LeetCode first. Then open the steps in order, and only as far as you need:

1. **Which pattern?** Say the pattern and the template aloud. Then open step 1 to check.
2. **The idea.** If you are blocked, open step 2. It has the key idea and the complexity, and no code.
3. **The Go solution.** Open step 3 last. Then close it and type the solution from memory.

Each solution has the function name and the signature that LeetCode gives you. The code does not show the given types (`ListNode`, `TreeNode`, `Node`) or the imports. LeetCode adds the standard library imports for you. For a local file, each solution lists the imports that it needs.

### 136. Single Number

[LeetCode 136](https://leetcode.com/problems/single-number/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** XOR cancels pairs
> - **Template:** [[#Template A: XOR cancels pairs|A: XOR cancels pairs]]

> [!tip]- Step 2: the idea
> **Idea.** XOR of a value with itself is 0, and XOR with 0 changes nothing. The order does not matter. So the XOR of all the values cancels each pair and leaves the single value.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** In Go, `^` between two values is XOR. Go has no `~` operator: `^x` with one operand is NOT.

> [!example]- Step 3: the Go solution
> ```go
> // singleNumber solves LC 136. Time O(n), space O(1).
> // Each value appears two times, but one value appears one time.
> func singleNumber(nums []int) int {
>     res := 0 // START at 0: x ^ 0 == x
>     for _, x := range nums {
>         // FOLD: x ^ x == 0, so the second copy removes the first
>         res ^= x
>     }
>     return res // only the value with no partner is left
> }
> ```

### 191. Number of 1 Bits

[LeetCode 191](https://leetcode.com/problems/number-of-1-bits/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Remove the lowest set bit
> - **Template:** [[#Template B: Remove the lowest set bit|B: Remove the lowest set bit]]

> [!tip]- Step 2: the idea
> **Idea.** `n & (n-1)` removes the lowest set bit of n. Count how many times you can do that before n is 0.
>
> **Complexity.** Time O(k) for k set bits, space O(1).
>
> **Go lesson.** `n &= n - 1` is the short form of `n = n & (n - 1)`. Go has the same short form for OR, XOR and the two shifts.

> [!example]- Step 3: the Go solution
> ```go
> // hammingWeight solves LC 191. Time O(k) for k set bits, space
> // O(1).
> // Example: n = 1100, n-1 = 1011, n & (n-1) = 1000. The lowest set
> // bit is
> // gone.
> func hammingWeight(n int) int {
>     count := 0
>     for n != 0 {
>         n &= n - 1 // REMOVE the lowest set bit
>         count++    // COUNT one bit for each removal
>     }
>     return count
> }
> ```

### 338. Counting Bits

[LeetCode 338](https://leetcode.com/problems/counting-bits/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** DP on bits
> - **Template:** [[#Template C: DP on bits|C: DP on bits]]

> [!tip]- Step 2: the idea
> **Idea.** The number i is i >> 1 with one more bit at the end. So the bit count of i is the bit count of i >> 1 plus the last bit of i. The smaller answer is already in the slice.
>
> **Complexity.** Time O(n), space O(1) without the result.
>
> **Go lesson.** In Go, `&` has a higher precedence than `+`, and that is not the same as in C. The parentheses in `(i & 1)` are for the reader.

> [!example]- Step 3: the Go solution
> ```go
> // countBits solves LC 338. Time O(n), space O(1) without the
> // result.
> // Example: 6 is 110. 6 >> 1 is 11 (two bits) and the last bit is 0,
> // so 6
> // has two bits.
> func countBits(n int) []int {
>     // BASE: bits[0] is 0, and make gives zeros
>     bits := make([]int, n+1)
>     for i := 1; i <= n; i++ {
>         // REUSE: i >> 1 is smaller than i, so bits[i>>1] is ready.
>         // ADD: i & 1 is the last bit of i, 0 or 1.
>         bits[i] = bits[i>>1] + (i & 1)
>     }
>     return bits
> }
> ```

### 190. Reverse Bits

[LeetCode 190](https://leetcode.com/problems/reverse-bits/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Shift in and shift out
> - **Template:** [[#Template D: Shift in and shift out|D: Shift in and shift out]]

> [!tip]- Step 2: the idea
> **Idea.** Take the last bit of n and put it at the end of the result. Shift the result left and n right, 32 times. The first bit that leaves n ends at the top of the result.
>
> **Complexity.** Time O(1), always 32 steps, space O(1).
>
> **Go lesson.** In Go, the OR operator has a lower precedence than `<<` and `&`. So the SHIFT IN line needs no parentheses, and gofmt shows the two groups with its spaces.

> [!example]- Step 3: the Go solution
> ```go
> // reverseBits solves LC 190. Time O(1), space O(1).
> // An older LeetCode stub was func reverseBits(num uint32) uint32.
> // The loop
> // is the same.
> func reverseBits(n int) int {
>     res := 0
>     // exactly 32 steps: the leading zeros of n count too
>     for i := 0; i < 32; i++ {
>         // SHIFT IN: make room at the end of res, then put the last
>         // bit of n
>         // there.
>         res = res<<1 | n&1
>         n >>= 1 // SHIFT OUT: drop the last bit of n
>     }
>     return res
> }
> ```

### 268. Missing Number

[LeetCode 268](https://leetcode.com/problems/missing-number/) · Easy

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** XOR of indexes and values
> - **Template:** [[#Template A: XOR cancels pairs|A: XOR cancels pairs]]

> [!tip]- Step 2: the idea
> **Idea.** The full range is 0 to n, and the slice has all of it but one number. XOR each index, each value and n. Each number that is there cancels with its index, and the missing number stays.
>
> **Complexity.** Time O(n), space O(1).
>
> **Go lesson.** `for i, x := range nums` gives the index and the value together, so one loop does the two XOR operations.

> [!example]- Step 3: the Go solution
> ```go
> // missingNumber solves LC 268. Time O(n), space O(1).
> // The sum formula n*(n+1)/2 minus the sum of the values also works.
> func missingNumber(nums []int) int {
>     // START with n: the loop gives the indexes 0 to n-1 only
>     res := len(nums)
>     for i, x := range nums {
>         // FOLD: the index i cancels the value that is equal to i
>         res ^= i ^ x
>     }
>     return res // the number from 0 to n that has no partner
> }
> ```

### 371. Sum of Two Integers

[LeetCode 371](https://leetcode.com/problems/sum-of-two-integers/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Add with XOR and carry
> - **Template:** [[#Template E: Add with XOR and carry|E: Add with XOR and carry]]

> [!tip]- Step 2: the idea
> **Idea.** XOR adds two bits with no carry. AND finds the positions where the two bits are 1, and a shift to the left moves that carry to the next position. Repeat until no carry is left.
>
> **Complexity.** Time O(1), at most 32 steps, space O(1).
>
> **Go lesson.** Go's `int` has 64 bits, and LeetCode expects 32-bit behavior. `uint32(a)` keeps the low 32 bits. `int32(x)` reads the same bits as a signed number, and `int(...)` then keeps the sign.

> [!example]- Step 3: the Go solution
> ```go
> // getSum solves LC 371. Time O(1), space O(1). It uses no + and no
> // -.
> // The loop works on 32 bits, so a carry that leaves bit 31 drops
> // out and
> // the loop stops.
> func getSum(a int, b int) int {
>     // TO 32 BITS: the conversion keeps the low 32 bits of each
>     // number.
>     // For a negative number, those bits are its 32-bit two's
>     // complement
>     // form.
>     x, y := uint32(a), uint32(b)
>     for y != 0 { // y holds the carry that is not yet added
>         // CARRY: where the two bits are 1, moved one position left
>         carry := (x & y) << 1
>         x ^= y    // SUM of the bits with no carry
>         y = carry // REPEAT with the carry
>     }
>     // BACK TO int: int32(x) reads the 32 bits as a signed number,
>     // so the
>     // top bit is the sign again. int(...) then extends the sign to
>     // 64 bits.
>     // int(x) with no int32 gives a large positive number for a
>     // negative
>     // sum.
>     return int(int32(x))
> }
> ```

### 7. Reverse Integer

[LeetCode 7](https://leetcode.com/problems/reverse-integer/) · Medium

> [!question]- Step 1: which pattern, which template?
> - **Pattern:** Digit loop with an overflow check
> - **Template:** [[#Template F: Digit loop with an overflow check|F: Digit loop with an overflow check]]

> [!tip]- Step 2: the idea
> **Idea.** Pop the last digit of x and push it at the end of the result. Before each push, compare the result with the limit divided by 10. Then the multiplication never leaves the 32-bit range.
>
> **Complexity.** Time O(log x), at most 10 digits, space O(1).
>
> **Go lesson.** In Go, `%` keeps the sign of the first number and `/` cuts toward zero. So `-123 % 10` is `-3`, and one loop is correct for positive and negative numbers.

> [!example]- Step 3: the Go solution
> **Imports for a local file:** `math`
>
> ```go
> // reverse solves LC 7. Time O(log x), space O(1).
> // The problem forbids 64-bit storage. Go's int has 64 bits, so this
> // code
> // checks the limit BEFORE the multiplication, as 32-bit code must.
> func reverse(x int) int {
>     res := 0
>     for x != 0 {
>         digit := x % 10 // POP: the last digit, with the sign of x
>         x /= 10         // DROP: cut toward zero, so -12 becomes -1
>
>         // CHECK: would res*10 + digit go above the largest int32?
>         // math.MaxInt32 is 2147483647, so the limits are 214748364
>         // and 7.
>         if res > math.MaxInt32/10 || (res == math.MaxInt32/10 && digit > math.MaxInt32%10) {
>             return 0
>         }
>         // CHECK: would it go below the smallest int32? The limits
>         // are
>         // -214748364 and -8.
>         if res < math.MinInt32/10 || (res == math.MinInt32/10 && digit < math.MinInt32%10) {
>             return 0
>         }
>         res = res*10 + digit // PUSH: safe now
>     }
>     return res
> }
> ```

---

[[wiki/neetcode-150/17-math-and-geometry|← Math and Geometry]] · [[wiki/neetcode-150/index|All 150 problems]]
