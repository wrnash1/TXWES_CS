# Lab Activity: Module 14 — Dynamic Programming Basics

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has four parts:

- **Part 1** — Fibonacci: naive, memoization, tabulation, space-optimized
- **Part 2** — Coin Change and Climbing Stairs
- **Part 3** — House Robber and 0/1 Knapsack
- **Part 4** — Longest Common Subsequence

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Fibonacci

**File:** `lab14_dp.py`

### 1.1 — Naive, Memoization, Tabulation

```python
import functools

# Naive recursive — O(2^n) — only safe for small n
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# Memoization using functools.lru_cache
@functools.lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

# Tabulation — bottom-up, O(n) time, O(n) space
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space-optimized — O(n) time, O(1) space
def fib_opt(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```

Test:

```python
for f in [fib_naive, fib_memo, fib_tab, fib_opt]:
    assert f(0) == 0
    assert f(1) == 1
    assert f(10) == 55
    assert f(20) == 6765

print('Fibonacci: all assertions passed.')
```

**Checkpoint:** All four implementations return `fib(10) = 55` and `fib(20) = 6765`.

---

### 1.2 — Recursion Tree Observation

```python
import time

# Compare naive vs memoized for n=35
start = time.time()
result_naive = fib_naive(35)
print(f'fib_naive(35) = {result_naive}, time = {time.time()-start:.4f}s')

start = time.time()
result_memo = fib_memo(35)
print(f'fib_memo(35)  = {result_memo}, time = {time.time()-start:.6f}s')
```

**Checkpoint:** `fib_naive(35)` is measurably slower. `fib_memo(35)` is nearly instantaneous. Both return `9227465`.

---

## Part 2 — Coin Change and Climbing Stairs

### 2.1 — Coin Change (LeetCode #322)

```python
def coin_change(coins, amount):
    """
    Return minimum coins to make amount, or -1 if impossible.
    Time: O(amount * len(coins)), Space: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

Test:

```python
print(coin_change([1, 5, 6, 9], 11))    # 2 (5+6)
print(coin_change([1, 2, 5], 11))        # 3 (5+5+1)
print(coin_change([2], 3))               # -1 — impossible
print(coin_change([1], 0))               # 0 — amount is zero
```

**Trace `coin_change([1,5,6,9], 11)`:**

```text
dp[0]=0
dp[1]: coin=1 → dp[0]+1=1 → dp[1]=1
dp[2]: coin=1 → dp[1]+1=2 → dp[2]=2
dp[3]: coin=1 → dp[2]+1=3 → dp[3]=3
dp[4]: coin=1 → dp[3]+1=4 → dp[4]=4
dp[5]: coin=1 → 5; coin=5 → dp[0]+1=1 → dp[5]=1
dp[6]: coin=1 → dp[5]+1=2; coin=5 → dp[1]+1=2; coin=6 → dp[0]+1=1 → dp[6]=1
dp[9]: coin=9 → dp[0]+1=1 → dp[9]=1
dp[10]: coin=1 → dp[9]+1=2; coin=5 → dp[5]+1=2 → dp[10]=2
dp[11]: coin=1 → dp[10]+1=3; coin=5 → dp[6]+1=2; coin=6 → dp[5]+1=2 → dp[11]=2
```

Result: 2 (5+6 or 6+5). Greedy (9+1+1) gives 3 — suboptimal.

**Checkpoint:** All four tests correct. Submit to LeetCode #322.

---

### 2.2 — Coin Change II: Count Ways (LeetCode #518)

```python
def change(amount, coins):
    """
    Return number of combinations to make amount.
    Outer loop: coins (not amounts) to avoid counting permutations.
    Time: O(amount * len(coins)), Space: O(amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1    # one way to make amount 0: take nothing

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
```

Test:

```python
print(change(5, [1,2,5]))    # 4 — (5), (2+2+1), (2+1+1+1), (1+1+1+1+1)
print(change(3, [2]))         # 0 — impossible
print(change(10, [10]))       # 1 — only one coin
```

**Why coins as outer loop?** Iterating coins in the outer loop ensures each coin can be used in any combination but combinations are unordered — (1,2) and (2,1) count as one. If amounts were the outer loop, both orders would be counted as distinct (permutations, not combinations).

**Checkpoint:** All three tests correct.

---

### 2.3 — Climbing Stairs (LeetCode #70)

```python
def climb_stairs(n):
    """
    Number of ways to reach the nth stair climbing 1 or 2 steps at a time.
    Time: O(n), Space: O(1)
    """
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```

Test:

```python
print(climb_stairs(1))    # 1
print(climb_stairs(2))    # 2
print(climb_stairs(5))    # 8
print(climb_stairs(10))   # 89
```

**Verify by hand for n=5:** dp=[1,2,3,5,8]. `dp[5]=8`. Enumerate: (1,1,1,1,1), (2,1,1,1), (1,2,1,1), (1,1,2,1), (1,1,1,2), (2,2,1), (2,1,2), (1,2,2) = 8 ways. ✓

**Checkpoint:** All four tests correct. Submit to LeetCode #70.

---

## Part 3 — House Robber and 0/1 Knapsack

### 3.1 — House Robber (LeetCode #198)

```python
def rob(nums):
    """
    Maximum money robbing non-adjacent houses.
    Time: O(n), Space: O(1)
    """
    prev2, prev1 = 0, 0
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2, prev1 = prev1, curr
    return prev1
```

Test:

```python
print(rob([1,2,3,1]))       # 4 — rob houses 0 and 2 (1+3)
print(rob([2,7,9,3,1]))     # 12 — rob houses 0,2,4 (2+9+1)
print(rob([0]))              # 0
print(rob([2,1,1,2]))        # 4 — rob houses 0 and 3 (2+2)
```

**Trace `rob([2,7,9,3,1])`:**

```text
prev2=0, prev1=0

num=2: curr=max(0, 0+2)=2;  prev2=0,  prev1=2
num=7: curr=max(2, 0+7)=7;  prev2=2,  prev1=7
num=9: curr=max(7, 2+9)=11; prev2=7,  prev1=11
num=3: curr=max(11,7+3)=11; prev2=11, prev1=11
num=1: curr=max(11,11+1)=12; prev2=11, prev1=12

Return 12 ✓
```

**Checkpoint:** All four tests correct. Submit to LeetCode #198.

---

### 3.2 — 0/1 Knapsack

```python
def knapsack_01(items, capacity):
    """
    items: list of (value, weight) tuples.
    Returns maximum value without exceeding capacity.
    Time: O(n * capacity), Space: O(n * capacity)
    """
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i-1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]                          # don't take item i
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weight] + value)

    return dp[n][capacity]
```

Test:

```python
# Module 13 counterexample — greedy gave 160, DP gives 220
items = [(60, 10), (100, 20), (120, 30)]
print(knapsack_01(items, 50))    # 220

# Additional tests
print(knapsack_01([(1,1),(2,1),(3,2)], 2))    # 4 (items 1+2)
print(knapsack_01([], 10))                    # 0 — no items
print(knapsack_01([(5,5)], 4))               # 0 — item too heavy
```

**Checkpoint:** All four tests correct. First test confirms DP beats greedy for 0/1 knapsack.

---

## Part 4 — Longest Common Subsequence

### 4.1 — LCS Implementation (LeetCode #1143)

```python
def longest_common_subsequence(text1, text2):
    """
    Return length of longest common subsequence.
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

Test:

```python
print(longest_common_subsequence('abcde', 'ace'))       # 3
print(longest_common_subsequence('abc', 'abc'))          # 3
print(longest_common_subsequence('abc', 'def'))          # 0
print(longest_common_subsequence('', 'abc'))             # 0
```

**Print the table for `'abcde'` / `'ace'`:**

```python
def lcs_with_table(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    header = '    ' + '  '.join([' '] + list(text2))
    print(header)
    rows = [' '] + list(text1)
    for i, row_label in enumerate(rows):
        print(f'{row_label}  ', ' '.join(str(dp[i][j]) for j in range(n+1)))
    return dp[m][n]

lcs_with_table('abcde', 'ace')
```

**Expected output:**

```text
      a  c  e
   0  0  0  0
a  0  1  1  1
b  0  1  1  1
c  0  1  2  2
d  0  1  2  2
e  0  1  2  3
```

**Checkpoint:** All four tests correct. Table matches expected. Submit to LeetCode #1143.

---

### 4.2 — Integration Test

```python
def test_all():
    # Fibonacci
    assert fib_opt(10) == 55
    assert fib_tab(20) == 6765

    # Coin change
    assert coin_change([1,2,5], 11) == 3
    assert coin_change([2], 3) == -1

    # Coin change II
    assert change(5, [1,2,5]) == 4

    # Climbing stairs
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89

    # House robber
    assert rob([2,7,9,3,1]) == 12
    assert rob([1,2,3,1]) == 4

    # Knapsack
    assert knapsack_01([(60,10),(100,20),(120,30)], 50) == 220

    # LCS
    assert longest_common_subsequence('abcde', 'ace') == 3
    assert longest_common_subsequence('abc', 'def') == 0

    print('All assertions passed.')

test_all()
```

---

## Deliverables

Submit to Canvas:

1. `lab14_dp.py` — all implementations and integration test
2. LeetCode submission screenshots for #70, #322, #198, #1143
3. Short written answer (3–5 sentences): Explain the difference between memoization and tabulation. For Coin Change, which style did you implement, and why? Identify the base case and explain what goes wrong if it is missing.

---

## Summary

| Concept | Key Point |
|---|---|
| Memoization | Top-down; cache recursive calls in dict |
| Tabulation | Bottom-up; fill array left to right |
| Fibonacci | `dp[i] = dp[i-1] + dp[i-2]`; O(1) space with two variables |
| Coin Change | `dp[i] = min(dp[i-c]+1)`; O(amount × coins) |
| Climbing Stairs | Fibonacci variant; dp[1]=1, dp[2]=2 |
| House Robber | `dp[i] = max(dp[i-1], dp[i-2]+nums[i])` |
| LCS | 2D table; match → `dp[i-1][j-1]+1`; else → `max(up, left)` |
| 0/1 Knapsack | `dp[i][w] = max(skip, take)`; O(n×W) |

---

## Part 9 — Challenge Exercise

These steps are **optional** and ungraded. They are designed for students who want to deepen their understanding beyond the core lab.

### 9.1 — Longest Increasing Subsequence (LeetCode #300)

Given an unsorted array of integers, find the length of the longest strictly increasing subsequence. The O(n²) DP solution defines `dp[i]` as the length of the LIS ending at index `i`: `dp[i] = max(dp[j]+1 for j < i if nums[j] < nums[i])`, base case `dp[i]=1`. Implement this solution, verify it returns 4 for `[10,9,2,5,3,7,101,18]` (LIS = [2,3,7,101] or [2,3,7,18] or [2,5,7,18]). Then implement the O(n log n) patience sorting solution using `bisect_left` to maintain a sorted `tails` array, where `tails[i]` stores the smallest tail element of all increasing subsequences of length `i+1`. Verify both give the same answer and explain why the O(n log n) approach does not directly recover the subsequence (only its length).

### 9.2 — Edit Distance (LeetCode #72)

Given two strings `word1` and `word2`, return the minimum number of operations (insert, delete, replace) to convert `word1` to `word2` — known as Levenshtein distance. Define `dp[i][j]` as the edit distance between `word1[0..i-1]` and `word2[0..j-1]`. Recurrence: if characters match, `dp[i][j] = dp[i-1][j-1]`; otherwise, `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` (delete, insert, replace). Base cases: `dp[i][0]=i`, `dp[0][j]=j`. Implement the solution, verify `edit_distance('horse','ros')=3` and `edit_distance('intention','execution')=5`, and fill the full DP table by hand for a short pair (e.g., 'cat'/'cut'). Explain how the three recurrence terms correspond to the three edit operations.

### 9.3 — Space-Optimized LCS and Backtracking

The standard LCS implementation uses O(m×n) space for the full DP table. Implement a space-optimized version that uses only O(n) space (two rows at a time), and verify it returns the same LCS length as the full table. Then, separately, implement a `recover_lcs(text1, text2)` function that backtracks through the full DP table to return the actual LCS string (not just its length). Verify that `recover_lcs('abcde', 'ace') == 'ace'` and `recover_lcs('AGGTAB', 'GXTXAYB') == 'GTAB'`. Explain why backtracking requires the full O(m×n) table and cannot be done with the two-row space optimization.
