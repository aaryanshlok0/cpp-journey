# Weird Algorithm

**CSES Problem:** [Weird Algorithm](https://cses.fi/problemset/task/1068/)

## Approach

Start with a positive integer `n`.

* If `n` is odd, replace it with `3n + 1`.
* If `n` is even, replace it with `n / 2`.
* Continue until `n` becomes `1`.

The program prints every value in the sequence.

## Complexity

* **Time:** O(k), where `k` is the number of values generated in the sequence.
* **Space:** O(1)

## Language

C++
