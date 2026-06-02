# Quiz: Module 14 — Dynamic Programming Basics

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What are the two structural properties that a problem must have for dynamic programming to apply?

- A) Greedy choice property and polynomial time solvability
- B) Optimal substructure and overlapping subproblems
- C) Divide-and-conquer structure and logarithmic recursion depth
- D) Monotone feasibility function and bounded search range

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The greedy choice property is the condition for greedy algorithms, not DP. Many DP problems lack a greedy choice property — that's precisely why they require DP. Polynomial time solvability is about complexity, not a structural property of the problem.
- *Why B is correct:* Optimal substructure means the optimal solution to the problem contains optimal solutions to its subproblems — so we can build up from smaller solutions. Overlapping subproblems means the same subproblems recur multiple times in the naive recursive solution — so caching them saves exponential recomputation. Together, these two properties define when DP is applicable.
- *Why C is incorrect:* Divide-and-conquer (Module 12) requires independent, non-overlapping subproblems. DP specifically requires overlapping subproblems. "Logarithmic recursion depth" is a property of binary search, not a DP prerequisite.
- *Why D is incorrect:* Monotone feasibility function and bounded search range describe the binary search on answer pattern (Module 12). These are entirely separate from dynamic programming.

---

### Question 2

What is the time complexity of the naive recursive Fibonacci implementation, and what causes it?

- A) O(n) — each call reduces n by 1
- B) O(n log n) — the recursion tree has log n levels
- C) O(2^n) — each call branches into two sub-calls, and many subproblems are recomputed
- D) O(n²) — the algorithm fills an n×n table

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(n) would require each subproblem to be computed once. The naive recursion recomputes `fib(k)` exponentially many times — `fib(3)` is called once from `fib(5)` and again from `fib(4)`, and so on down the tree.
- *Why B is correct:* O(n log n) would apply to a divide-and-conquer algorithm with O(n) combination cost. Fibonacci's recursion tree grows exponentially: `fib(n)` spawns `fib(n-1)` and `fib(n-2)`, which each spawn two more calls, leading to approximately 2^n total calls.
- *Why C is correct:* The recursion tree has O(2^n) nodes because each call branches into two and the tree has depth n. Many subtrees are identical — `fib(3)` is computed as a whole subtree every time it is needed. This exponential redundancy is precisely why memoization reduces it to O(n).
- *Why D is incorrect:* O(n²) is associated with 2D DP problems like LCS. Fibonacci uses a 1D structure (or just two variables). There is no n×n table.

---

### Question 3

What is the correct base case and recurrence for the Coin Change problem (`dp[i]` = minimum coins to make amount `i`)?

- A) `dp[0] = 1`; `dp[i] = min(dp[i-c] + 1)` for each coin c ≤ i
- B) `dp[0] = 0`; `dp[i] = min(dp[i-c] + 1)` for each coin c ≤ i
- C) `dp[0] = 0`; `dp[i] = dp[i-1] + dp[i-2]`
- D) `dp[1] = 1`; `dp[i] = max(dp[i-1], dp[i-2] + i)`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `dp[0] = 1` would mean "one coin is needed to make amount 0," which is wrong. Amount 0 requires zero coins — `dp[0] = 0`. With `dp[0] = 1`, the count for every amount would be off by one.
- *Why B is correct:* `dp[0] = 0` because zero coins are needed to make amount zero. The recurrence `dp[i] = min(dp[i-c] + 1)` says: for each coin `c` that fits in amount `i`, the cost is one coin (taking `c`) plus the minimum coins to make the remaining amount `i-c`. Taking the minimum over all valid coins gives the optimal.
- *Why C is incorrect:* `dp[i] = dp[i-1] + dp[i-2]` is the Fibonacci / Climbing Stairs recurrence. Coin Change uses a loop over coin denominations, not a fixed two-predecessor formula.
- *Why D is incorrect:* `dp[i] = max(dp[i-1], dp[i-2] + i)` is the House Robber recurrence (with `i` playing the role of the house value). Coin Change minimizes, not maximizes, and uses coin denominations, not array indices.

---

### Question 4

In the Climbing Stairs problem, why is `dp[i] = dp[i-1] + dp[i-2]`?

- A) Because climbing stairs is equivalent to sorting — each pair of stairs requires two comparisons
- B) Every way to reach stair `i` either came from stair `i-1` (one step) or stair `i-2` (two steps) — these are disjoint sets, so the total count is their sum
- C) Because Fibonacci always gives the answer to counting problems — the recurrence applies universally
- D) Because the number of ways to climb 10 stairs is the product of ways for 5 stairs and ways for 5 stairs

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Sorting is unrelated to stair climbing. There is no comparison operation in the Climbing Stairs problem.
- *Why B is correct:* The last step to reach stair `i` is either a one-step from stair `i-1` or a two-step from stair `i-2`. These are mutually exclusive and exhaustive cases. The number of ways to reach `i` via `i-1` is exactly `dp[i-1]` (all ways to reach `i-1`); via `i-2` is exactly `dp[i-2]`. Summing disjoint cases gives `dp[i] = dp[i-1] + dp[i-2]`.
- *Why C is incorrect:* The Fibonacci recurrence applies here because of the problem's specific structure (two choices per step), not universally. Many counting problems have entirely different recurrences. Applying Fibonacci blindly without understanding why would be incorrect for other problems.
- *Why D is incorrect:* The number of ways is not multiplicative here — the problem cannot be split into two independent halves. This is exactly the overlapping subproblems property: subproblems share structure and must be combined additively.

---

### Question 5

In House Robber, `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. What do the two alternatives represent?

- A) Whether to sort the array before or after robbing
- B) Two choices: skip house `i` (best result without `i`) or rob house `i` (best result two houses back, plus this house's value)
- C) Whether the total is odd or even — even totals are maximized differently
- D) Whether to use memoization (first term) or tabulation (second term)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* House Robber processes the array as-is — no sorting involved. The order of houses is fixed.
- *Why B is correct:* `dp[i-1]` is the maximum amount you can rob from the first `i-1` houses (skipping house `i`). `dp[i-2] + nums[i]` is the maximum from the first `i-2` houses plus robbing house `i` directly. Since house `i-1` and house `i` are adjacent, robbing house `i` requires that house `i-1` was skipped, hence looking back two steps (`dp[i-2]`).
- *Why C is incorrect:* Parity of the total has no role in the House Robber recurrence. The two alternatives represent skip vs. rob, not an arithmetic property of the result.
- *Why D is incorrect:* Both terms in the recurrence are from the DP table — the recurrence is the same regardless of whether you implement it as memoization or tabulation.

---

### Question 6

In the LCS recurrence, when `text1[i-1] == text2[j-1]`, why is `dp[i][j] = dp[i-1][j-1] + 1` (not `dp[i-1][j] + 1` or `dp[i][j-1] + 1`)?

- A) Because `dp[i-1][j-1]` is always the largest value in the table
- B) Because matching the current characters extends the LCS found in both strings without those characters — the matched character is added to the end of that common subsequence
- C) Because adding 1 to a diagonal cell avoids double-counting characters from the same string
- D) Because `dp[i-1][j]` and `dp[i][j-1]` are used only when characters don't match

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `dp[i-1][j-1]` is not always the largest value — `dp[i-1][j]` or `dp[i][j-1]` could be larger. The reason is structural, not numerical.
- *Why B is correct:* When `text1[i-1] == text2[j-1]`, we have found a matching character. The longest common subsequence of `text1[0..i-1]` and `text2[0..j-1]` is the longest common subsequence of their prefixes without those characters (`dp[i-1][j-1]`), extended by one (the matched character). Using `dp[i-1][j]` or `dp[i][j-1]` would mean extending a subsequence that still includes the current character of one string — potentially counting that character twice.
- *Why C is incorrect:* The "avoiding double-counting" framing is imprecise. The correct explanation is about what subproblem `dp[i-1][j-1]` represents: the LCS of the two strings each shortened by one character.
- *Why D is incorrect:* `dp[i-1][j]` and `dp[i][j-1]` are not restricted to the non-matching case — they simply represent the LCS when skipping one character from either string. In the matching case, `dp[i-1][j-1]+1` is always at least as large as `max(dp[i-1][j], dp[i][j-1])`, so it is used.

---

### Question 7

What is the difference between Coin Change (LeetCode #322) and Coin Change II (LeetCode #518)?

- A) Coin Change uses memoization; Coin Change II uses tabulation
- B) Coin Change returns the minimum number of coins; Coin Change II returns the number of distinct combinations
- C) Coin Change II requires sorting the coins first; Coin Change does not
- D) Coin Change allows each coin to be used once; Coin Change II allows unlimited use

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both problems can be solved with either memoization or tabulation. The implementation style is not what distinguishes them.
- *Why B is correct:* Coin Change (#322) minimizes — find the fewest coins to make the target, or return -1 if impossible. Coin Change II (#518) counts — find the number of distinct coin combinations (unordered) that sum to the target. The recurrences are different: `dp[i] = min(dp[i-c]+1)` vs. `dp[i] += dp[i-c]`.
- *Why C is incorrect:* Neither problem requires sorting. Coin Change II iterates coins in the outer loop (not for sorting reasons but to count combinations rather than permutations), but this is not a sort operation.
- *Why D is incorrect:* Both problems allow each coin denomination to be used unlimited times (unbounded knapsack). If coins were restricted to one use each, the problem would be a bounded variant requiring a different approach.

---

### Question 8

Why does the 0/1 knapsack DP use `dp[i-1][w - weight]` (looking at the previous row) rather than `dp[i][w - weight]` (current row)?

- A) The previous row is larger and gives better values
- B) Using the previous row ensures each item is counted at most once — the current row already reflects item `i`, so looking at it would allow using item `i` multiple times
- C) Using the current row causes an index out of bounds error
- D) The previous row is used because the table is filled right to left

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The previous row is not always larger. The reason is logical, not numerical.
- *Why B is correct:* `dp[i][w - weight]` would represent the best value using items 1 through `i` with capacity `w - weight`. If item `i` was already included in `dp[i][w - weight]`, adding item `i` again would use it twice — violating the 0/1 constraint (each item used at most once). Using `dp[i-1][w - weight]` ensures the inclusion decision for item `i` considers only the previous set of items.
- *Why C is incorrect:* Both `dp[i-1][...]` and `dp[i][...]` are within bounds. The distinction is about correctness, not index validity.
- *Why D is incorrect:* The 0/1 knapsack DP table as written is filled left to right within each row. The reason for using the previous row is the 0/1 constraint, not fill order.

---

### Question 9

`coin_change([1,5,6,9], 11)` returns 2 (coins 5+6). If greedy (largest coin first) were applied, what would it return, and why is that result suboptimal?

- A) 2 — greedy also finds 5+6 by coincidence
- B) 3 — greedy picks 9+1+1, missing the 5+6 combination
- C) -1 — greedy cannot make 11 from these coins
- D) 4 — greedy picks four 1-coins after 9 fails

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Greedy by largest coin first: 11 ≥ 9, take 9 → remaining 2. 2 < 6, 2 < 5, take 1 → remaining 1. Take 1 → remaining 0. Total: 3 coins. Greedy does not find 5+6.
- *Why B is correct:* Greedy takes the largest coin ≤ remaining: 9 (leaving 2), then 1 (leaving 1), then 1 (done). Total: 3 coins. DP finds dp[5]=1, dp[6]=1, dp[11]=dp[6]+1=2 (take coin 5 from dp[6]) — 2 coins. Greedy's choice of 9 blocks the better 5+6 combination.
- *Why C is incorrect:* 11 = 9 + 1 + 1 is achievable — greedy finds it in 3 coins. The result is suboptimal (3 > 2), not impossible.
- *Why D is incorrect:* Greedy would take 9 first (the largest coin ≤ 11), not immediately fall to 1-coins. Four 1-coins would be 9+1+1 only uses three coins total — the trace in B is correct.

---

### Question 10

In the LCS table for `text1='abcde'` and `text2='ace'`, what is `dp[3][2]` and what does it represent?

- A) `dp[3][2] = 1` — the LCS of 'abc' and 'a' is 'a'
- B) `dp[3][2] = 2` — the LCS of 'abc' and 'ac' is 'ac'
- C) `dp[3][2] = 3` — the LCS of 'abc' and 'ace' is 'ace'
- D) `dp[3][2] = 0` — no common subsequence exists between these prefixes

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `dp[3][2]` represents the LCS of `text1[0..2]='abc'` and `text2[0..1]='ac'`, not `text2[0..0]='a'`. The second index is 2, which corresponds to the first 2 characters of `text2='ace'`, i.e., `'ac'`.
- *Why B is correct:* `dp[3][2]` = LCS of `text1[0..2]='abc'` and `text2[0..1]='ac'`. Both 'a' and 'c' appear in both strings in order ('a' at index 0, 'c' at index 2 in 'abc'; 'a' at 0, 'c' at 1 in 'ac'). LCS is 'ac', length 2. Reading the table: `dp[1][1]=1` (match 'a'), `dp[3][2]=2` (match 'c' at text1[2] and text2[1], extending `dp[2][1]=1`).
- *Why C is incorrect:* `dp[3][2]` covers only the first 2 characters of `text2` ('ac'), not all 3 ('ace'). 'e' is not yet included at column index 2.
- *Why D is incorrect:* 'abc' and 'ac' share 'a' and 'c' as a common subsequence. `dp[3][2]` is 2, not 0.
