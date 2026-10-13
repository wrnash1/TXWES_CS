# Reading Guide: Module 14 — Dynamic Programming Basics

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2315 &BULL; DATA STRUCTURES & ALGORITHM ANALYSIS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

Dynamic programming (DP) is a method for solving optimization and counting problems by breaking them into overlapping subproblems, solving each subproblem once, and combining the results. It is the correct approach when two structural properties hold: **optimal substructure** and **overlapping subproblems**. Where greedy makes one local choice and never revisits it, DP considers all choices and picks the best via stored subproblem answers. This module covers the foundations of DP: the two required properties, memoization versus tabulation, and four canonical problems — Fibonacci, Coin Change, House Robber, and Longest Common Subsequence — plus the 0/1 knapsack problem that greedy (Module 13) cannot solve.

---

## 1. Two Properties Required for DP

### Optimal Substructure

The optimal solution to the problem contains optimal solutions to its subproblems.

- Shortest path: the shortest path A→C through B consists of the shortest A→B path and the shortest B→C path.
- Coin change: the minimum coins for amount `i` using coin `c` is `1 + minimum coins for amount i-c`.

If optimal substructure does not hold, DP cannot be applied.

### Overlapping Subproblems

The same subproblems recur multiple times in a naive recursive solution.

- Fibonacci: `fib(5)` calls `fib(4)` and `fib(3)`; `fib(4)` calls `fib(3)` again. Without caching, `fib(3)` is recomputed.
- Merge sort does NOT have overlapping subproblems — each recursive call operates on a distinct subarray.

DP stores subproblem answers (memoization or tabulation) to avoid recomputation.

---

## 2. Two DP Styles: Memoization and Tabulation

### Memoization (Top-Down)

Write the natural recursive solution, then add a cache. Check the cache before computing; store the result after computing.

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

- Computes only the subproblems that are actually needed.
- Preserves the recursive structure — easier to write from the recurrence.
- Risk: deep recursion may hit Python's default limit (~1000 calls).

### Tabulation (Bottom-Up)

Fill a table iteratively from the smallest subproblems to the largest.

```python
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

- No recursion — no stack depth limit.
- Slightly less intuitive but preferred for production code and large inputs.
- Can often be space-optimized by keeping only the last few values.

### Comparison

| Property | Memoization | Tabulation |
|---|---|---|
| Approach | Top-down, recursive | Bottom-up, iterative |
| Cache | Dictionary or array | Array (dp table) |
| Subproblems computed | Only needed ones | All subproblems |
| Recursion depth risk | Yes (Python limit) | No |
| Space optimization | Harder | Usually straightforward |

---

## 3. Fibonacci

```python
# Space-optimized tabulation — O(n) time, O(1) space
def fib(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```

**Recurrence:** `fib(n) = fib(n-1) + fib(n-2)`, base cases `fib(0)=0`, `fib(1)=1`.

Naive recursion is O(2^n). Memoization reduces it to O(n) by caching. Tabulation is O(n) time, O(n) space. Space-optimized tabulation is O(n) time, O(1) space — keep only the previous two values.

---

## 4. Coin Change (LeetCode #322)

**Problem:** Minimum number of coins to make a target amount. Return -1 if impossible.

**Recurrence:** `dp[i] = min(dp[i-c] + 1)` for each coin `c ≤ i`.

**Base case:** `dp[0] = 0`.

```python
def coin_change(coins, amount):
    """
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

**Key insight:** For each amount `i`, we try every coin and take the minimum. The table is built left to right — by the time we compute `dp[i]`, `dp[i-c]` for all coins `c` is already computed.

**Coin Change II (LeetCode #518):** Number of ways (not minimum count) to make the amount. Different recurrence: `dp[i] += dp[i-c]`. Initialize `dp[0] = 1`.

---

## 5. Climbing Stairs (LeetCode #70)

**Problem:** `n` stairs; each step can climb 1 or 2. How many distinct ways to reach the top?

**Recurrence:** `dp[i] = dp[i-1] + dp[i-2]` (Fibonacci variant).

```python
def climb_stairs(n):
    """Time: O(n), Space: O(1)"""
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```

This is identical to Fibonacci with `dp[1]=1, dp[2]=2`. Every distinct way to reach stair `i` either comes from stair `i-1` (one step) or stair `i-2` (two steps).

---

## 6. House Robber (LeetCode #198)

**Problem:** Houses in a line with amounts. Cannot rob adjacent houses. Maximize total.

**Recurrence:** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.

At each house: either skip it (best result without this house) or rob it (best result from two houses back, plus this house's value).

```python
def rob(nums):
    """Time: O(n), Space: O(1)"""
    prev2, prev1 = 0, 0
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2, prev1 = prev1, curr
    return prev1
```

**House Robber II (LeetCode #213):** Houses arranged in a circle — first and last are adjacent. Solution: run House Robber I twice: once on `nums[:-1]` and once on `nums[1:]`, take the max.

---

## 7. Longest Common Subsequence (LeetCode #1143)

**Problem:** Length of the longest subsequence common to two strings (maintains order, not necessarily contiguous).

**Recurrence:**

```text
dp[i][j] = dp[i-1][j-1] + 1        if text1[i-1] == text2[j-1]
dp[i][j] = max(dp[i-1][j], dp[i][j-1])    otherwise
```

```python
def longest_common_subsequence(text1, text2):
    """Time: O(m*n), Space: O(m*n)"""
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

**Table for `'abcde'` / `'ace'`:**

```text
    ''  a  c  e
''   0  0  0  0
a    0  1  1  1
b    0  1  1  1
c    0  1  2  2
d    0  1  2  2
e    0  1  2  3
```

LCS length = 3 (`'ace'`).

---

## 8. 0/1 Knapsack

**Subproblem:** `dp[i][w]` = maximum value using the first `i` items with weight capacity `w`.

**Recurrence:**

```text
dp[i][w] = dp[i-1][w]                                   if items[i-1].weight > w
dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)   otherwise
```

```python
def knapsack_01(items, capacity):
    """
    items: list of (value, weight) tuples.
    Time: O(n * capacity), Space: O(n * capacity)
    """
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        value, weight = items[i-1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weight] + value)
    return dp[n][capacity]
```

This correctly finds B+C = 220 for the Module 13 counterexample (capacity=50, items A(60,10), B(100,20), C(120,30)).

---

## 9. Interview Exam Tips

1. **Identify the subproblem first** — define `dp[i]` (or `dp[i][j]`) precisely before writing code. "dp[i] = minimum coins to make amount i" is a complete definition. "dp[i] = something about coins" is not.

2. **State the recurrence explicitly** — write `dp[i] = ...` as a formula before coding. If you cannot state the recurrence, you do not yet understand the problem.

3. **Base cases are not optional** — missing a base case is the single most common DP bug. For 1D DP: `dp[0]`. For 2D DP: the entire first row and first column.

4. **Memoization for interviews, tabulation for production** — in an interview, memoization is faster to write and easier to explain from the recurrence. In production code, tabulation avoids recursion depth issues.

5. **Coin Change vs Climbing Stairs** — both are 1D DP, but different recurrences. Coin Change minimizes count: `dp[i] = min(dp[i-c]+1)`. Climbing Stairs counts ways: `dp[i] = dp[i-1] + dp[i-2]`. Don't conflate them.

6. **LCS is the canonical 2D DP problem** — interviewers use it to test whether candidates can build a 2D table and trace the recurrence correctly. Practice filling the table by hand.

7. **Space optimization** — most 1D DP can be reduced to O(1) (Fibonacci, House Robber, Climbing Stairs). 2D DP can often be reduced to O(n) (LCS: keep only two rows). Mention this in interviews.

8. **DP vs. greedy** — when you see "minimum," "maximum," or "number of ways" with interdependent choices, think DP. When you see "schedule," "select maximum non-overlapping," or "first fit," think greedy first. If greedy has a simple correctness argument, use it. If not, use DP.

---

## 10. Complexity Summary

| Problem | Time | Space | Notes |
|---|---|---|---|
| Fibonacci | O(n) | O(1) | Space-optimized tabulation |
| Coin Change | O(amount × coins) | O(amount) | LeetCode #322 |
| Climbing Stairs | O(n) | O(1) | Fibonacci variant |
| House Robber | O(n) | O(1) | Two-variable rolling |
| LCS | O(m×n) | O(m×n) | Reducible to O(n) rows |
| 0/1 Knapsack | O(n × W) | O(n × W) | Reducible to O(W) one row |

---

## 11. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Dynamic Programming Visualizations** — [https://visualgo.net/en/dp](https://visualgo.net/en/dp)
   Animated step-by-step visualizations of classic DP problems including Fibonacci, Coin Change, and LCS. Use the table-fill mode to watch the recurrence execute one cell at a time — especially useful for building intuition for 2D DP tables.

2. **OpenDSA — Dynamic Programming Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/DynamicProgramming.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/DynamicProgramming.html)
   Free interactive OER textbook covering optimal substructure, overlapping subproblems, the Fibonacci sequence as a DP example, and the 0/1 knapsack problem. Includes embedded exercises and correctness proofs.

3. **NeetCode — Dynamic Programming Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI](https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI)
   Free video walkthroughs for Climbing Stairs, House Robber, Coin Change, LCS, and 0/1 Knapsack. Each video includes a recurrence derivation, table trace, and Python solution with time/space analysis.

4. **MIT OCW 6.006 — Dynamic Programming Lectures** — [https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
   MIT lecture notes on DP covering memoization, the subproblem DAG, and the guessing framework. Lectures 19–22 cover 1D DP, 2D DP, and advanced DP problems. Free PDF notes and video lectures available.

5. **Python `functools.lru_cache` Documentation** — [https://docs.python.org/3/library/functools.html#functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)
   Official Python documentation for `lru_cache` — the decorator used in this course for memoization. Explains cache size options, `cache_info()`, `cache_clear()`, and the `@cache` shorthand added in Python 3.9.

---

## 12. Study Checklist

- [ ] Watch the Module 14 video lecture by Professor Nash.
- [ ] Implement `fib_memo` and `fib_tab` from scratch. Verify `fib(10) = 55`.
- [ ] Implement `coin_change` and trace `coin_change([1,5,6,9], 11)`.
- [ ] Implement `climb_stairs` and verify `climb_stairs(5) = 8`.
- [ ] Implement `rob` and trace `rob([2,7,9,3,1]) = 12`.
- [ ] Implement `longest_common_subsequence` and fill the table for `'abcde'`/`'ace'`.
- [ ] Implement `knapsack_01` and verify it returns 220 for the Module 13 counterexample.
- [ ] Complete the Module 14 Lab.
- [ ] Complete the Module 14 Quiz.
- [ ] Solve LeetCode #70, #322, #198, #1143.
