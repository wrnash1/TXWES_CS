# Reading Guide: Module 13 – Dynamic Programming: Memoization and Tabulation
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 13 – Dynamic Programming: Memoization and Tabulation**! Dynamic programming (DP) is the topic that most separates junior candidates from mid-level engineers in technical interviews. DP problems appear on every FAANG-style interview track and are consistently rated as the hardest category on LeetCode. The key insight is that DP is not a mysterious technique — it is recursion with caching, applied to problems that have overlapping subproblems and an optimal substructure. Once you recognize these two properties, the solution approach becomes systematic.

This module covers the two DP implementations (top-down memoization and bottom-up tabulation), the conditions that identify a DP problem, and the most common DP problem patterns.

---

### 1. High-Yield Glossary

*   **Dynamic programming (DP)**: An optimization technique that solves problems by breaking them into overlapping subproblems, solving each subproblem once, and storing the result — eliminating redundant recomputation. Applicable when the problem has optimal substructure and overlapping subproblems.

*   **Overlapping subproblems**: A property of problems where the same smaller subproblem is solved multiple times during a naive recursive solution. For example, computing Fibonacci(5) naively recomputes Fibonacci(3) twice — this redundancy is what DP eliminates.

*   **Optimal substructure**: A property where the optimal solution to a problem can be constructed from optimal solutions to its subproblems. DP requires both overlapping subproblems AND optimal substructure; divide-and-conquer requires only the latter.

*   **Memoization (top-down DP)**: Implementing DP by writing a recursive solution and caching function results in a dictionary or array. On each call, check the cache first; compute and store only on a cache miss. Natural for problems with recursive structure.

*   **Tabulation (bottom-up DP)**: Implementing DP iteratively by filling a table of subproblem results in dependency order — smallest subproblems first, building up to the full problem. Avoids recursion overhead and stack limits. Often more space-efficient (1D/2D rolling array optimization).

*   **State**: The set of parameters that uniquely identifies a subproblem in a DP solution. Defining the state is the hardest step — once the state is clear, the recurrence relation and base cases follow naturally.

*   **Recurrence relation**: A mathematical equation expressing the solution to a DP problem in terms of solutions to smaller subproblems. For Fibonacci: `dp[n] = dp[n-1] + dp[n-2]`. Writing the recurrence is the core step in formulating a DP solution.

---

### 2. Certification Exam Tips
*   **Identify DP with two questions:** (1) "Does the problem ask for a maximum, minimum, or count of ways?" (2) "Do subproblems repeat?" If both are yes, it's likely DP. These heuristics identify 90% of interview DP problems.
*   **Start with memoization, then optimize to tabulation:** Memoization is easier to write correctly under pressure. Once it passes, ask "can I convert this to a bottom-up table?" for potential space optimization.
*   **Master the 5 classic DP patterns:** 1D DP (climbing stairs, house robber); 2D DP (grid paths, LCS); Knapsack (0/1 knapsack, partition equal subset); String DP (edit distance, palindromes); Interval DP (burst balloons, matrix chain).
*   **Space optimization — rolling array:** Many 2D DP tables only look back one or two rows. Replace the full 2D table with a 1D array and update in place or with a second row, reducing space from O(n²) to O(n).
*   **LeetCode "Easy DP" builds muscle memory:** #70 (Climbing Stairs), #198 (House Robber), #322 (Coin Change). Solve them until they feel trivial. Then attack medium DP: #300 (LIS), #1143 (LCS), #416 (Partition Equal Subset Sum).
*   **Study Resource:** [Dynamic Programming Patterns – LeetCode Discuss](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns) — a community-created guide organizing DP problems into 14 recurring patterns with example problems for each, essential for systematic interview preparation.

---

### Required Readings & Videos
*   **Required Reading:** [Dynamic Programming – Algorithms (Jeff Erickson), Chapter 3](https://jeffe.cs.illinois.edu/teaching/algorithms/book/03-dynprog.pdf) — a free open-access chapter with rigorous treatment of DP, recurrence formulation, and classic problems including Fibonacci, edit distance, and knapsack.
*   **Required Video:** [Dynamic Programming – NeetCode on YouTube](https://www.youtube.com/watch?v=oBt53YbR9Kk) — a 5-hour comprehensive video covering the major DP patterns with full LeetCode solutions. Watch in sections across multiple study sessions.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement Fibonacci** using naive recursion, memoization, and tabulation — measure and compare actual runtime for n=40.
*   **Solve LeetCode #70 (Climbing Stairs)** — 1D DP with O(1) space optimization.
*   **Solve LeetCode #322 (Coin Change)** — 1D tabulation, classic unbounded knapsack pattern.
*   **Solve LeetCode #1143 (Longest Common Subsequence)** — 2D tabulation with rolling row optimization.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 3 of Algorithms by Jeff Erickson.
- [ ] Watch the relevant sections of the NeetCode DP video.
- [ ] Implement Fibonacci three ways and benchmark them.
- [ ] Solve LeetCode #70, #322, and #1143.
- [ ] Proceed to the Module 13 Quiz.
