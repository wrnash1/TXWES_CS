# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 14 — Dynamic Programming Basics

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / MIT &bull; Data Structures and Algorithms Full Course &bull; Module 14</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=8hly31xKli0" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/8hly31xKli0" title="freeCodeCamp / MIT &bull; Data Structures and Algorithms Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp / MIT &bull; Data Structures and Algorithms Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Estimated Duration:** 24–28 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Opening

Dynamic programming — DP for short — is the technique behind some of the most important interview questions in software engineering. Where greedy makes one locally optimal choice and moves on, DP systematically solves every subproblem and stores the results, combining them to solve the original problem. It applies when two properties hold: the problem has optimal substructure — the optimal solution to the problem contains optimal solutions to subproblems — and overlapping subproblems — the same subproblems arise repeatedly. This module covers the foundations: memoization versus tabulation, and four canonical DP problems — Fibonacci, Coin Change, House Robber, and Longest Common Subsequence.

---

## Part 1 — What Makes a Problem DP

Every DP problem has two properties.

**Property 1 — Optimal Substructure:** The optimal solution to the problem can be built from optimal solutions to its subproblems.

Example: the shortest path from A to C through B consists of the shortest path from A to B plus the shortest path from B to C. If either sub-path were not optimal, we could improve the whole path. This holds for Dijkstra's algorithm too — that's why Dijkstra works.

**Property 2 — Overlapping Subproblems:** The same subproblems are solved repeatedly in a naive recursive solution.

Example: Fibonacci. `fib(5)` calls `fib(4)` and `fib(3)`. `fib(4)` calls `fib(3)` and `fib(2)`. `fib(3)` is computed multiple times. A pure divide-and-conquer algorithm (like merge sort) does NOT have overlapping subproblems — the subproblems are independent.

The naive recursive Fibonacci has exponential time — O(2^n) — because of this repeated work. DP eliminates it.

There are two styles:

- **Memoization (top-down):** Write the recursive solution, add a cache dictionary. On each call, check the cache first. Return the cached value if present; compute and store it otherwise.

- **Tabulation (bottom-up):** Fill a table iteratively from the smallest subproblems to the largest. No recursion. No cache.

Both styles give the same answer. Tabulation avoids Python's recursion depth limit (1000 by default) and is usually preferred for larger inputs.

---

## Part 2 — Fibonacci and Coin Change

Let's start with Fibonacci.

```python
# Naive recursive — O(2^n)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# Memoization — O(n) time, O(n) space
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Tabulation — O(n) time, O(n) space
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space-optimized tabulation — O(n) time, O(1) space
def fib_opt(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```

**]**

\"Given coins of certain denominations and a target amount, return the minimum number of coins needed. Return -1 if impossible.

**Recurrence:** `dp[i] = min(dp[i-c] + 1)` for each coin `c` where `i >= c`.

**Base case:** `dp[0] = 0` (zero coins needed for amount 0). All other `dp[i] = infinity` initially.

```python
def coin_change(coins, amount):
    \"\"\"
    Return minimum coins to make amount, or -1 if impossible.
    Time: O(amount * len(coins)), Space: O(amount)
    \"\"\"
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

**, 11)` — trace the dp array]**

```text
coins=[1,5,6,9], amount=11
dp = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

dp[1]:  coin=1: dp[0]+1=1  → dp[1]=1
dp[5]:  coin=1: dp[4]+1=5; coin=5: dp[0]+1=1 → dp[5]=1
dp[6]:  coin=1: dp[5]+1=2; coin=5: dp[1]+1=2; coin=6: dp[0]+1=1 → dp[6]=1
dp[9]:  coin=1: dp[8]+1; coin=5: dp[4]+1=5; coin=6: dp[3]+1; coin=9: dp[0]+1=1 → dp[9]=1
dp[10]: coin=1: dp[9]+1=2; coin=5: dp[5]+1=2 → dp[10]=2
dp[11]: coin=1: dp[10]+1=3; coin=5: dp[6]+1=2; coin=6: dp[5]+1=2 → dp[11]=2
```

Result: 2 coins (5+6 or 6+5). Greedy (largest coin first: 9+1+1 = 3) would give 3 coins — suboptimal.\"

---

## Part 3 — Climbing Stairs and House Robber

\"You can climb 1 or 2 stairs at a time. How many distinct ways to reach the nth stair?

This is Fibonacci in disguise: `dp[i] = dp[i-1] + dp[i-2]`.

```python
def climb_stairs(n):
    \"\"\"
    Return number of ways to climb n stairs (1 or 2 at a time).
    Time: O(n), Space: O(1)
    \"\"\"
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```

** → 8 ways]**

\"You are a robber. Houses in a line, each with some money. You cannot rob two adjacent houses (alarm triggers). Maximize the total amount robbed.

**Recurrence:** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

At each house, you either skip it (take dp[i-1]) or rob it (take dp[i-2] + nums[i]).

```python
def rob(nums):
    \"\"\"
    Return maximum money without robbing adjacent houses.
    Time: O(n), Space: O(1)
    \"\"\"
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, 0
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2, prev1 = prev1, curr
    return prev1
```

**)` — trace:]**

```text
nums = [2,7,9,3,1]
prev2=0, prev1=0

num=2: curr=max(0, 0+2)=2; prev2=0, prev1=2
num=7: curr=max(2, 0+7)=7; prev2=2, prev1=7
num=9: curr=max(7, 2+9)=11; prev2=7, prev1=11
num=3: curr=max(11, 7+3)=11; prev2=11, prev1=11  (tie — either works)
num=1: curr=max(11, 11+1)=12; prev2=11, prev1=12

Return 12 ✓ (rob houses 0,2,4: 2+9+1=12)
```\"

---

## Part 4 — Longest Common Subsequence

\"Given two strings, return the length of their longest common subsequence. A subsequence maintains relative order but need not be contiguous.

**Recurrence:**

```text
If s1[i-1] == s2[j-1]:  dp[i][j] = dp[i-1][j-1] + 1
Else:                   dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

```python
def longest_common_subsequence(text1, text2):
    \"\"\"
    Return length of longest common subsequence.
    Time: O(m*n), Space: O(m*n)
    m=len(text1), n=len(text2)
    \"\"\"
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

```text
    ''  a  c  e
''   0  0  0  0
a    0  1  1  1
b    0  1  1  1
c    0  1  2  2
d    0  1  2  2
e    0  1  2  3

dp[5][3] = 3. LCS is 'ace'. ✓
```

**Why both recurrences?** When characters match, we extend the LCS from both strings minus those characters: `dp[i-1][j-1] + 1`. When they don't match, we take the best we can get by either skipping the current character of text1 (`dp[i-1][j]`) or text2 (`dp[i][j-1]`).\

---

## Part 5 — 0/1 Knapsack

\"In Module 13 we saw greedy fails for 0/1 knapsack. Here's the DP solution.

**Subproblem:** `dp[i][w]` = maximum value using the first `i` items with capacity `w`.

**Recurrence:**

```text
dp[i][w] = dp[i-1][w]                              if items[i-1].weight > w
dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)   otherwise
```

```python
def knapsack_01(items, capacity):
    \"\"\"
    items: list of (value, weight) tuples.
    Returns maximum value without exceeding capacity.
    Time: O(n * capacity), Space: O(n * capacity)
    \"\"\"
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i-1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]    # don't take item i
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weight] + value)

    return dp[n][capacity]
```

**, capacity=50]**

```text
Items: A(60,10), B(100,20), C(120,30)
dp[3][50]:

dp[1][w]: for w>=10, dp[1][w]=60; else 0.
dp[2][w]: for w>=20, can add B(100); dp[2][20]=100, dp[2][30]=160, dp[2][50]=160
dp[3][w]: for w>=30, can add C(120);
  dp[3][30] = max(dp[2][30]=160, dp[2][0]+120=120) = 160
  dp[3][50] = max(dp[2][50]=160, dp[2][20]+120=220) = 220

Return 220 ✓ (B+C, matching the optimal from Module 13)
```

The Module 14 lab covers all four canonical DP problems, plus 0/1 knapsack. Fibonacci is the entry point — trace it both ways. Coin Change is the LeetCode interview staple. Good luck.\

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 14 — Dynamic Programming Basics]**

---

## Additional Resources

- [NeetCode — Dynamic Programming Playlist](https://www.youtube.com/watch?v=mBNrRy2_hVs)
- [LeetCode #70 — Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [LeetCode #322 — Coin Change](https://leetcode.com/problems/coin-change/)
- [LeetCode #198 — House Robber](https://leetcode.com/problems/house-robber/)
- [LeetCode #1143 — Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
