# Counting Divisors

**Platform:** CSES  
**Category:** Mathematics / Number Theory  
**Problem:** Counting Divisors

## Approach

For each number `x`, iterate from `1` to `sqrt(x)`.

If `i` divides `x`, then both `i` and `x/i` are divisors.

So instead of checking all numbers from `1` to `x`, we only check up to `sqrt(x)`.

## Complexity

For each number:

- Time: `O(√x)`
- Space: `O(1)`

For `n` test cases:

- Time: `O(Σ√xi)`
- Space: `O(1)`
