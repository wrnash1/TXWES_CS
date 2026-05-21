# Quiz: Module 13 – Dynamic Programming: Memoization and Tabulation
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the time complexity of computing the n-th Fibonacci number using memoization (top-down DP), compared to naive recursion?
*   A) Memoization: O(n²); Naive recursion: O(2ⁿ)
*   B) Memoization: O(n); Naive recursion: O(2ⁿ)
*   C) Memoization: O(log n); Naive recursion: O(n)
*   D) Memoization: O(1); Naive recursion: O(n²)
*   **Correct Answer:** B) Memoization: O(n); Naive recursion: O(2ⁿ)
*   **Distractor Analysis:**
    *   *Why correct:* Memoization computes each unique subproblem fib(k) exactly once for k from 0 to n — O(n) total calls. Naive recursion recomputes each fib(k) exponentially many times, producing a recursion tree of size O(2^n).
    *   A is incorrect: Memoized Fibonacci is O(n), not O(n²). There is no nested loop or quadratic structure.
    *   C is incorrect: O(log n) Fibonacci is possible with matrix exponentiation, not simple memoization. Naive recursion is O(2ⁿ), not O(n).
    *   D is incorrect: O(1) is impossible for Fibonacci without precomputation; the result depends on n and must compute at least the n-th value.

---

**Question 2**
Which of the following is the most accurate definition of **optimal substructure** as a property of dynamic programming problems?
*   A) A property where the problem's solution space can be divided into non-overlapping independent subproblems that are solved separately and combined, as in merge sort.
*   B) A property where the optimal solution to the overall problem can be constructed directly from the optimal solutions to its subproblems, meaning locally optimal sub-solutions compose into a globally optimal solution.
*   C) A property where the problem requires examining all 2^n subsets or n! permutations to find the best answer, making exhaustive search necessary but cacheable.
*   D) A property where each subproblem has a unique solution that does not depend on how the problem was divided, ensuring memoization always produces correct results regardless of call order.
*   **Correct Answer:** B) A property where the optimal solution to the overall problem can be constructed directly from the optimal solutions to its subproblems, meaning locally optimal sub-solutions compose into a globally optimal solution.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Non-overlapping independent subproblems describe divide-and-conquer (like merge sort), not DP. DP requires overlapping subproblems; divide-and-conquer does not.
    *   *Why B is correct:* Optimal substructure means: if you know the optimal answer to each subproblem, you can combine them to get the optimal answer to the full problem. Without this, even knowing subproblem optima, you cannot guarantee the combined solution is optimal.
    *   *Why C is incorrect:* That describes exponential brute force, not optimal substructure. Problems with optimal substructure avoid exhaustive search through directed recurrence.
    *   *Why D is incorrect:* That vaguely describes subproblem independence, which is a property of divide-and-conquer, and conflates it with memoization correctness, which is a separate concern.

---

**Question 3**
In the Coin Change problem (LeetCode #322), you want to find the minimum number of coins to make amount n using coins of given denominations. Which approach gives the correct bottom-up DP solution?
*   A) Sort coins in descending order and greedily take the largest coin that fits at each step.
*   B) Initialize `dp[0] = 0` and `dp[i] = infinity` for i > 0; for each amount i from 1 to n, try each coin c and update `dp[i] = min(dp[i], dp[i-c] + 1)` if `i >= c`.
*   C) Use BFS where each state is a remaining amount; level count equals minimum coins needed since BFS finds shortest paths.
*   D) Recursively try all combinations of coins for each amount, memoizing the minimum result — but also try each coin denomination once before recursing to reduce branching.
*   **Correct Answer:** B) Initialize `dp[0] = 0` and `dp[i] = infinity` for i > 0; for each amount i from 1 to n, try each coin c and update `dp[i] = min(dp[i], dp[i-c] + 1)` if `i >= c`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Greedy coin change is incorrect for arbitrary denominations (e.g., coins [1,3,4], amount 6: greedy gives 4+1+1=3 coins, but DP gives 3+3=2 coins). Greedy only works for canonical coin systems.
    *   *Why B is correct:* This is the standard unbounded knapsack DP for coin change. Building dp[i] from dp[i-c] uses optimal substructure: the minimum coins for amount i equals 1 (one coin of value c) plus the minimum coins for the remaining amount.
    *   *Why C is incorrect:* BFS works for unweighted shortest path (each coin has "cost" 1), but building a BFS state space for this problem is less efficient than DP and harder to implement correctly.
    *   *Why D is incorrect:* Trying each coin once before recursing is not a valid optimization; it would prune valid solutions where a coin is used more than once.

---

**Question 4**
What is the key difference between **top-down memoization** and **bottom-up tabulation** as DP implementation strategies?
*   A) Memoization is always more space-efficient because it only computes subproblems that are actually needed, while tabulation always computes all subproblems including unnecessary ones.
*   B) Memoization uses recursion and caches results on demand (lazy evaluation); tabulation fills a table iteratively in dependency order (eager evaluation) — tabulation avoids call stack overhead and enables rolling-array space optimization.
*   C) Memoization is only applicable to 1D DP problems; tabulation is required for 2D problems like LCS and grid traversal.
*   D) Tabulation requires identifying all subproblems before starting, while memoization automatically discovers subproblems during execution — making tabulation impossible without a full mathematical analysis of the problem.
*   **Correct Answer:** B) Memoization uses recursion and caches results on demand (lazy evaluation); tabulation fills a table iteratively in dependency order (eager evaluation) — tabulation avoids call stack overhead and enables rolling-array space optimization.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Memoization does save work by computing only needed subproblems, but this advantage is often marginal. In practice, both have the same asymptotic time and space for most DP problems.
    *   *Why B is correct:* The structural distinction (recursive vs. iterative) has practical consequences: memoization may hit Python's recursion limit for large n; tabulation is iterative and immune to stack overflow. Tabulation also makes rolling-array space optimization natural.
    *   *Why C is incorrect:* Both strategies apply to 1D and 2D DP problems. LCS can be solved with both memoization and tabulation; the dimensionality of the state does not restrict which strategy can be used.
    *   *Why D is incorrect:* Tabulation does require understanding the dependency order of subproblems, but this is established by the recurrence relation — the same analysis needed for memoization. It does not require exhaustive mathematical analysis beyond what memoization needs.

---

**Question 5**
You are solving the Longest Common Subsequence (LCS) problem with two strings of lengths m and n. The standard 2D DP table uses O(m·n) space. Which optimization reduces this to O(min(m, n)) space?
*   A) Sort both strings before running DP so the table becomes triangular, reducing half the cells.
*   B) Use only two rows of the table at a time (the current row and the previous row), since each dp[i][j] only depends on dp[i-1][j], dp[i][j-1], and dp[i-1][j-1].
*   C) Apply memoization instead of tabulation — memoization automatically prunes unused cells, reducing memory to the number of unique subproblems called.
*   D) Convert the 2D table to a 1D hash map indexed by (i, j) tuples, which uses less memory because Python dicts only store populated entries.
*   **Correct Answer:** B) Use only two rows of the table at a time (the current row and the previous row), since each dp[i][j] only depends on dp[i-1][j], dp[i][j-1], and dp[i-1][j-1].
*   **Distractor Analysis:**
    *   *Why A is incorrect:* LCS does not use sorted strings; sorting changes the subsequence problem. Even if you did, sorting would not produce a triangular table.
    *   *Why B is correct:* The LCS recurrence only looks at the previous row (i-1). Keeping only the current and previous row reduces space from O(m·n) to O(n) — or O(min(m, n)) by iterating over the shorter string.
    *   *Why C is incorrect:* Memoization in Python stores all unique (i, j) pairs, which is still O(m·n) — no pruning occurs since all subproblems are needed to compute LCS.
    *   *Why D is incorrect:* A dict of (i, j) tuples uses more memory than a 2D list due to Python dict overhead per entry. It does not save space and is slower due to hash overhead.
