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

---

### Question 11

What is the time and space complexity of the tabulation solution for `coin_change(coins, amount)` as shown in this module?

- A) Time O(amount), Space O(coins)
- B) Time O(amount × len(coins)), Space O(amount)
- C) Time O(2^amount), Space O(amount)
- D) Time O(amount log amount), Space O(1)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(amount) time would require processing each amount in constant time — but for each amount `i`, the algorithm loops over all `len(coins)` denominations. The outer loop is O(amount) and the inner loop is O(len(coins)), giving O(amount × len(coins)) total.
- *Why B is correct:* The tabulation fills a 1D array of size `amount+1`. For each index `i` (O(amount) iterations), it tries every coin denomination (O(len(coins)) iterations). Total time: O(amount × len(coins)). Space: O(amount) for the `dp` array. This is pseudo-polynomial — polynomial in `amount` but `amount` can be exponentially large in the number of input bits.
- *Why C is incorrect:* O(2^amount) would be the naive recursion without memoization — exploring all possible combinations. Tabulation eliminates this by caching each subproblem result exactly once.
- *Why D is incorrect:* O(amount log amount) would suggest a binary search or divide-and-conquer approach. No such technique is used here. The inner loop over coins is linear, not logarithmic.

---

### Question 12

`climb_stairs(6)` should return 13. Which description correctly implements the space-optimized version for this call?

- A) Use naive recursive Fibonacci: return `fib(6) + fib(5)`
- B) Initialize `prev2=1, prev1=2`; loop from 3 to 6 doing `curr=prev1+prev2; prev2=prev1; prev1=curr`; return `prev1`
- C) Initialize `dp=[0]*7; dp[1]=1; dp[2]=2`; return `dp[6]` after filling by Fibonacci loop — this is the O(n) space version
- D) Return `2**6 // 6` using the Fibonacci approximation formula

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Naive recursive Fibonacci is O(2^n) — not the space-optimized version. It is also the wrong function: Climbing Stairs uses the same recurrence as Fibonacci but with different base cases (cs(1)=1, cs(2)=2).
- *Why B is correct:* The space-optimized loop starts with base cases `prev2=1 (dp[1])`, `prev1=2 (dp[2])` and iterates from 3 to n. For n=6: i=3→curr=3; i=4→curr=5; i=5→curr=8; i=6→curr=13. Return 13. O(n) time, O(1) space.
- *Why C is incorrect:* The array-based tabulation (O(n) space) also returns 13 correctly, but it is not the space-optimized version. The question asks specifically for the space-optimized implementation.
- *Why D is incorrect:* `2**6 // 6 = 64 // 6 = 10` — this is wrong. There is no simple closed-form integer expression for the Fibonacci sequence like this.

---

### Question 13

In House Robber, what is `rob([2,7,9,3,1])` and which houses are robbed to achieve the maximum?

- A) 11 — houses at indices 0 and 2 (2+9)
- B) 12 — houses at indices 0, 2, and 4 (2+9+1)
- C) 11 — houses at indices 1 and 3 (7+3+1 is invalid; 7+3=10)
- D) 14 — houses at indices 1 and 2 (7+9, but these are adjacent)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Robbing indices 0 and 2 gives 2+9=11. But index 4 (value 1) is non-adjacent to index 2 — it can also be robbed. 2+9+1=12 > 11. Option A misses the additional non-adjacent house.
- *Why B is correct:* Indices 0, 2, 4 are all non-adjacent (each pair differs by 2). Values: 2+9+1=12. The trace confirms this: prev2=0,p1=0→num=2:p1=2→num=7:curr=max(2,7)=7,p2=2,p1=7→num=9:curr=max(7,2+9)=11,p2=7,p1=11→num=3:curr=max(11,7+3)=11,p2=11,p1=11→num=1:curr=max(11,11+1)=12. Return 12. Houses robbed: 0(2), 2(9), 4(1).
- *Why C is incorrect:* Indices 1 and 3 give 7+3=10 < 12. This is not the maximum. The listed arithmetic "7+3+1" includes index 4 (value 1) but indices 1,3,4 — where 3 and 4 are adjacent — violates the constraint.
- *Why D is incorrect:* Indices 1 and 2 (values 7 and 9) are adjacent — robbing both violates the constraint. This option is invalid regardless of the value.

---

### Question 14

In the 0/1 knapsack DP, `dp[i][w]` is defined as the maximum value using the first `i` items with capacity `w`. What is `dp[2][20]` for `items=[(60,10),(100,20),(120,30)]` and `capacity=50`?

- A) 60 — only item A (weight 10) is included; item B does not fit alongside A in 20 kg
- B) 100 — item B (weight 20) fills the capacity exactly; this is better than taking only A
- C) 160 — items A and B both fit in 20 kg
- D) 0 — neither item fits in 20 kg

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* While A (weight=10) does fit in capacity 20, item B (weight=20) alone yields value 100 > 60. The DP takes the maximum of skip B (`dp[1][20]=60`) and take B (`dp[1][0]+100=100`). The maximum is 100, not 60.
- *Why B is correct:* `dp[2][20]`: item B has weight=20 which equals the capacity. Taking only B: `dp[1][20-20]+100 = dp[1][0]+100 = 0+100 = 100`. Skipping B: `dp[1][20]=60` (item A alone). `max(100, 60) = 100`. So `dp[2][20]=100`.
- *Why C is incorrect:* Items A and B together weigh 10+20=30 kg, which exceeds capacity 20. They cannot both be included in `dp[2][20]`.
- *Why D is incorrect:* Item A weighs 10 ≤ 20 and item B weighs 20 ≤ 20 — both fit individually. `dp[2][20]` is at minimum 60 (just item A).

---

### Question 15

Why does Coin Change II (LeetCode #518) iterate coins in the outer loop and amounts in the inner loop, rather than amounts outer and coins inner?

- A) Iterating coins outer is faster — it reduces the number of inner loop iterations
- B) Iterating coins outer counts unordered combinations: once a coin type is processed, it cannot be "re-introduced" in a different order. Iterating amounts outer would count ordered permutations instead
- C) Iterating amounts outer would cause an index out of bounds for large coin values
- D) The order of loops does not matter — both give the same result for Coin Change II

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both loop orders perform exactly O(amount × len(coins)) iterations total. The speed is identical. The difference is correctness, not performance.
- *Why B is correct:* With coins outer and amounts inner: when processing coin `c`, all previous coins are already "locked in" to earlier positions in the `dp` array. Coin `c` can only extend combinations that were built without considering later coins. This prevents counting (1,2) and (2,1) as separate combinations. With amounts outer, for each amount `i` you add all coins — so (1 at i=1, then 2 at i=3) and (2 at i=2, then 1 at i=3) are counted separately as distinct orderings.
- *Why C is incorrect:* Both loop orders access `dp[i-coin]` only when `coin <= i`, so there is no out-of-bounds risk in either order.
- *Why D is incorrect:* The loop order does matter for Coin Change II. Amounts outer gives the number of ordered sequences (permutations); coins outer gives the number of unordered combinations. For target=3 with coins [1,2]: combinations = 2 ({1,2},{1,1,1}); permutations = 3 ({1,2},{2,1},{1,1,1}).

---

### Question 16

`rob([2,1,1,2])` returns 4. Which pair of non-adjacent houses is robbed?

- A) Houses 0 and 1 (values 2+1=3)
- B) Houses 1 and 3 (values 1+2=3)
- C) Houses 0 and 2 (values 2+1=3)
- D) Houses 0 and 3 (values 2+2=4)

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Houses 0 and 1 are adjacent — robbing both violates the constraint. Additionally, 2+1=3 < 4.
- *Why B is incorrect:* Houses 1 and 3 are non-adjacent (differ by 2), so the constraint is satisfied. But 1+2=3 < 4. This is not the maximum.
- *Why C is incorrect:* Houses 0 and 2 are non-adjacent (differ by 2). 2+1=3 < 4. Not the maximum.
- *Why D is correct:* Houses 0 and 3 differ by 3 — they are non-adjacent. Values 2+2=4. Trace `rob([2,1,1,2])`: p2=0,p1=0→num=2:curr=2,p2=0,p1=2→num=1:curr=max(2,0+1)=2,p2=2,p1=2→num=1:curr=max(2,2+1)=3,p2=2,p1=3→num=2:curr=max(3,2+2)=4,p2=3,p1=4. Return 4.

---

### Question 17

In the LCS recurrence, when `text1[i-1] != text2[j-1]`, why is `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` instead of `dp[i-1][j-1]`?

- A) `dp[i-1][j-1]` is always zero when characters don't match
- B) When characters don't match, the LCS of the two full prefixes is the best achievable by skipping one character from either string — `dp[i-1][j]` skips the last of `text1`; `dp[i][j-1]` skips the last of `text2`; we take the maximum
- C) `dp[i-1][j-1]` would double-count characters in the two strings
- D) The diagonal cell is only used during the matching step to avoid overwriting already-computed values

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `dp[i-1][j-1]` is not necessarily zero when characters don't match. It holds the LCS of both strings each shortened by one character, which can be any non-negative integer.
- *Why B is correct:* When the current characters don't match, neither can be the "last matched character" of the LCS. We either skip `text1[i-1]` (giving `dp[i-1][j]`) or skip `text2[j-1]` (giving `dp[i][j-1]`). We take the maximum of these two options. `dp[i-1][j-1]` ≤ both options so it is never chosen.
- *Why C is incorrect:* The concern about double-counting does not apply here. Using `max(dp[i-1][j], dp[i][j-1])` does not double-count — each cell represents a distinct subproblem.
- *Why D is incorrect:* The reason for not using the diagonal cell is logical (it is never the maximum in the non-match case), not implementation-related.

---

### Question 18

Which of the following correctly describes the difference between the 0/1 knapsack and the unbounded knapsack (Coin Change)?

- A) 0/1 knapsack allows fractional items; unbounded knapsack requires whole items
- B) 0/1 knapsack uses each item at most once; unbounded knapsack allows each item type to be used unlimited times
- C) 0/1 knapsack is solved with a 2D table; unbounded knapsack always requires a 1D table
- D) Unbounded knapsack is always faster because it has fewer constraints

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Fractional items describe the fractional knapsack (greedy, Module 13). Both 0/1 and unbounded knapsack require whole items. The distinction is about the count allowed per item type, not divisibility.
- *Why B is correct:* In 0/1 knapsack, each item is unique — it can be taken (1 time) or left (0 times). The DP uses the previous row (`dp[i-1]`) to prevent reuse. In unbounded knapsack (like Coin Change), each item type can be used any number of times — the DP references `dp[i-coin]` in the current state to allow reuse.
- *Why C is incorrect:* 0/1 knapsack can be implemented with a 1D rolling array; unbounded knapsack is also naturally 1D. Dimensionality is an implementation detail, not a defining property.
- *Why D is incorrect:* Both 0/1 and unbounded knapsack are O(n × W) — the same asymptotic complexity. "Fewer constraints" does not imply faster runtime.

---

### Question 19

What is the value of `fib_opt(0)`, `fib_opt(1)`, and `fib_opt(2)` according to the space-optimized Fibonacci in the reading guide?

- A) 0, 1, 1
- B) 1, 1, 2
- C) 0, 1, 2
- D) 1, 2, 3

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The Fibonacci sequence: fib(0)=0, fib(1)=1, fib(2)=1. In `fib_opt`: `if n <= 1: return n` handles n=0→0 and n=1→1. For n=2: prev2=0, prev1=1; loop range(2,3) runs once: curr=0+1=1, prev2=1, prev1=1; return 1. All three values: 0, 1, 1.
- *Why B is incorrect:* 1, 1, 2 is a 1-indexed Fibonacci sequence (fib(1)=1, fib(2)=1, fib(3)=2). The module's implementation is 0-indexed: fib(0)=0.
- *Why C is incorrect:* fib(2)=1, not 2. `fib(2)=fib(1)+fib(0)=1+0=1`. The value 2 belongs to fib(3).
- *Why D is incorrect:* 1, 2, 3 would be an arithmetic sequence. Fibonacci never produces this as fib(0), fib(1), fib(2).

---

### Question 20

In `longest_common_subsequence('abc', 'abc')`, the function returns 3. Why does `dp[i][j]` reach the value 3 only at `dp[3][3]` and not at an earlier cell?

- A) Because the matching condition `text1[i-1]==text2[j-1]` is only true for `i=j=3`
- B) Because `dp[i][j]` is defined as the LCS of the first `i` characters of `text1` and the first `j` characters of `text2` — a value of 3 requires all 3 characters of both strings to be considered, which only occurs at `dp[3][3]`
- C) Because the table is filled diagonally and only reaches the bottom-right cell last
- D) Because all off-diagonal cells are set to zero by default

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The matching condition is true at (1,1) for 'a', (2,2) for 'b', and (3,3) for 'c'. The match at (1,1) gives `dp[1][1]=1`; the match at (2,2) gives `dp[2][2]=2`; the match at (3,3) gives `dp[3][3]=3`. The value 3 accumulates step by step.
- *Why B is correct:* `dp[i][j]` represents the LCS of `text1[0..i-1]` and `text2[0..j-1]`. An LCS of length 3 requires at least 3 characters in each string, meaning `i >= 3` and `j >= 3`. The first (and only) cell satisfying both is `dp[3][3]`.
- *Why C is incorrect:* The table is filled row by row, left to right — not diagonally. The value 3 is not seen earlier because of the subproblem definition (answer B), not the fill order.
- *Why D is incorrect:* Off-diagonal cells are not zero for identical strings. For 'abc'/'abc': `dp[1][2]=1`, `dp[2][1]=1`, `dp[2][3]=2`, etc. Many non-diagonal cells have positive values.
