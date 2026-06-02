# Discussion Forum: Module 14 — Dynamic Programming Basics

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Background

Dynamic programming is where algorithm design gets interesting. The technique is not about memorizing a formula — it is about recognizing that a problem has overlapping subproblems and optimal substructure, then defining a clean subproblem, writing the recurrence, establishing base cases, and filling the table. The hard part is always the recurrence: what does `dp[i]` mean, and how does `dp[i]` depend on smaller subproblems? Getting that definition right is 90% of the work. Students who can articulate the subproblem definition before touching code are ready for DP interview questions. Students who start coding immediately — copying a formula they half-remember — will get stuck when the interviewer asks "why does that recurrence work?"

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — Memoization vs. Tabulation: Understanding the Two Styles

Both memoization and tabulation solve DP problems by storing subproblem results. They differ in direction (top-down vs. bottom-up), recursion structure, and space trade-offs. Understanding both styles is essential for adapting to interview constraints.

In 175–225 words, respond to the following:

- From the Module 14 lab (Part 1), you implemented Fibonacci using both `fib_memo` and `fib_tab`. Describe what happens when `fib_memo(5)` executes: trace the recursive calls made, state which ones hit the cache after the first full computation, and explain why the total number of distinct calls is O(n) rather than O(2^n).
- The reading guide explains that tabulation avoids Python's recursion depth limit. For a problem requiring `fib(10000)`, which implementation would you choose and why? What would happen if you used `fib_memo` with n=10000?
- For Coin Change, the reading guide implements tabulation (filling `dp[0]` through `dp[amount]` in order). Explain why tabulation is natural here: specifically, when computing `dp[11]` for `coin_change([1,5,6,9], 11)`, which earlier `dp` values must already be filled, and why the left-to-right fill order guarantees they are?

Reference the lab or reading guide in your response.

---

### Scenario B — Coin Change and the Recurrence

Coin Change is the canonical DP interview problem. The recurrence is simple but requires careful understanding: `dp[i] = min(dp[i-c] + 1)` for each coin `c ≤ i`. Deriving that recurrence from scratch — rather than memorizing it — is the skill that transfers to new problems.

In 175–225 words, respond to the following:

- From the Module 14 lab (Part 2, Section 2.1), trace `coin_change([1,5,6,9], 11)`. For each of `dp[5]`, `dp[6]`, `dp[9]`, `dp[10]`, and `dp[11]`, state the coin choice(s) that determine the minimum and explain why the optimal combination is 5+6 (2 coins) rather than 9+1+1 (3 coins).
- The reading guide explains that greedy fails for this problem (Module 13 counterexample), while DP succeeds. In your own words, explain what structural property DP exploits that greedy cannot: what information does `dp[i]` encode that greedy discards?
- Coin Change II (LeetCode #518) counts combinations rather than minimizing count. The lab (Section 2.2) explains that the coin is the outer loop rather than the amount. Explain in your own words why this ordering produces combinations (unordered) rather than permutations (ordered). Use a concrete small example — such as amount=3 with coins=[1,2] — to show the difference.

Reference the lab or reading guide in your response.

---

### Scenario C — LCS and 2D DP Table

Longest Common Subsequence is the standard 2D DP problem. The key skill is filling a table correctly and explaining why each cell is computed the way it is. In interviews, you will be asked to trace the table — not just state the answer.

In 175–225 words, respond to the following:

- From the Module 14 lab (Part 4), you filled the LCS table for `'abcde'` and `'ace'`. Write out the full 6×4 table (including the zero row and column). For each cell where the value increased by 1 from the diagonal, identify which characters matched. For each cell where the value came from the max of left/up, state which direction dominated and why.
- The reading guide gives two cases for the recurrence: match (`dp[i][j] = dp[i-1][j-1] + 1`) and mismatch (`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`). Explain the mismatch case: what does `dp[i-1][j]` represent and what does `dp[i][j-1]` represent? Why is the answer the max of the two rather than, say, their sum?
- Describe a real-world scenario where LCS would be practically useful. Be specific: what are the two sequences, what does a "common subsequence" represent in that context, and what practical decision would the LCS length inform? (DNA comparison, version control diff, and plagiarism detection are all valid starting points — but add specifics.)

Reference the lab or reading guide in your response.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 14 lab or reading guide at least once

---

## Peer Response Requirements

- **Due:** Sunday at 11:59 PM CST
- Respond to **at least two classmates** who chose **different scenarios**
- Each response: minimum **60 words**, must add substance
- Acceptable contributions: add a second example, challenge a claim with a counter-case, extend the concept to a harder LeetCode problem, or describe how the concept in your classmate's scenario connects to greedy (Module 13) or divide-and-conquer (Module 12)

---

## Grading Rubric — 10 Points Total

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 5–6 pts | Scenario answered fully with specific, concrete examples. Reference to lab or reading guide. 175–225 words. Complete sentences. |
| 3–4 pts | Mostly addressed but vague or generic. Close to word count. |
| 1–2 pts | Significant parts missing or well below word count. |
| 0 pts | Not submitted. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 pts | Two responses to classmates with different scenarios. Each 60+ words and adds genuine value. |
| 2 pts | One peer response only, or responses lack substance. |
| 0 pts | No peer responses. |

---

## A Note from Professor Nash

The single most important thing you can do when approaching a DP problem is to define the subproblem before writing a single line of code. "dp[i] = minimum coins to make amount i" is a complete, precise definition. Once you have that, the recurrence almost writes itself: to make amount i, try each coin c — you spend one coin and need dp[i-c] more. Base case: dp[0] = 0. That's the entire algorithm. Students who struggle with DP are almost always struggling with the subproblem definition, not the code. For LCS, the subproblem is "the length of the longest common subsequence of the first i characters of text1 and the first j characters of text2." Once you have that definition and draw the table on a whiteboard, the two-case recurrence is a direct consequence of the definition. Practice defining the subproblem in one sentence for each problem you solve. That is the DP skill that transfers to problems you have never seen before.
