# CSES – Increasing Array

- **Problem Link:** https://cses.fi/problemset/task/1094
- **Topic:** Greedy, Arrays
- **Difficulty:** Introductory
- **Status:** Solved ✅

## Approach

Traverse the array from left to right and compare each element with the previous element.

- If the current element is greater than or equal to the previous element, no operation is needed.
- If the current element is smaller, increase it to match the previous element.
- Add the required increments to the total number of moves.

The greedy approach works because making the smallest necessary correction at each position ensures the array remains non-decreasing while minimizing the total increments.

## Complexity Analysis

- **Time Complexity:** \(O(n)\)
- **Space Complexity:** \(O(n)\) for storing the array.

## Key Takeaway

A basic greedy problem that demonstrates how local decisions can produce an optimal solution. Using `long long` prevents integer overflow when the total number of moves is large.
