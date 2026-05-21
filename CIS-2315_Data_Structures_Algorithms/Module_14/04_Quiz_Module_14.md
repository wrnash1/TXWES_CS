# Quiz: Module 14 – Greedy Algorithms
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
In the Activity Selection problem (choose maximum non-overlapping intervals), what is the correct greedy strategy?
*   A) Always select the interval with the earliest start time.
*   B) Always select the shortest interval (smallest duration).
*   C) Always select the interval with the earliest end time.
*   D) Always select the interval with the latest start time.
*   **Correct Answer:** C) Always select the interval with the earliest end time.
*   **Distractor Analysis:**
    *   *Why correct:* Picking the interval that finishes earliest leaves the maximum remaining time for future intervals. This is provably optimal via the exchange argument: any solution that picks a later-ending interval can swap it for the earliest-ending non-conflicting interval without losing optimality.
    *   A is incorrect: Earliest start time does not guarantee maximizing count — a very long interval starting earliest may block many short later intervals.
    *   B is incorrect: Shortest duration can be suboptimal; a short interval might overlap two others, while a longer interval that ends earlier would block fewer future intervals.
    *   D is incorrect: Latest start time maximizes unused time at the beginning but does not help maximize the count of selected intervals.

---

**Question 2**
Which of the following is the most accurate definition of the **exchange argument** proof technique for greedy algorithms?
*   A) A technique that proves greedy correctness by induction: showing the greedy choice is optimal for n=1, then assuming it holds for n=k and proving it holds for n=k+1.
*   B) A technique that proves greedy correctness by assuming an optimal solution exists that differs from the greedy solution, then demonstrating that any non-greedy choice in that solution can be swapped for the greedy choice without increasing the total cost — converting it to the greedy solution.
*   C) A technique that proves a greedy algorithm is incorrect by constructing a counterexample where the greedy choice leads to a suboptimal solution, forcing the use of dynamic programming instead.
*   D) A technique that compares the greedy algorithm's output to a brute-force solution on random inputs, establishing empirical equivalence through statistical testing.
*   **Correct Answer:** B) A technique that proves greedy correctness by assuming an optimal solution exists that differs from the greedy solution, then demonstrating that any non-greedy choice in that solution can be swapped for the greedy choice without increasing the total cost — converting it to the greedy solution.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes mathematical induction, a separate proof technique. While related in spirit, the exchange argument specifically involves swapping choices between two solution candidates, not a base-case/inductive-step structure.
    *   *Why B is correct:* The exchange argument starts with any optimal solution OPT, systematically swaps its non-greedy choices for greedy ones while showing the cost does not worsen, and concludes OPT can be transformed into the greedy solution — proving greedy is also optimal.
    *   *Why C is incorrect:* That describes disproving a greedy algorithm, not proving one. The exchange argument is a proof of correctness, not incorrectness.
    *   *Why D is incorrect:* Empirical testing can suggest correctness but never proves it; a single counterexample not covered by random testing would invalidate the claim.

---

**Question 3**
Why does the greedy algorithm fail for the 0/1 Knapsack problem but succeed for the Fractional Knapsack problem?
*   A) Because 0/1 knapsack involves integers while fractional knapsack involves floats, and greedy algorithms only work correctly with floating-point values.
*   B) Because in fractional knapsack, items can be split so taking the maximum value-to-weight ratio fraction is always optimal; in 0/1 knapsack, items must be taken whole, and greedily taking the highest ratio item may prevent a better combination of remaining items.
*   C) Because 0/1 knapsack has O(n²) state space while fractional knapsack has O(n log n) state space, and greedy is only efficient enough for the smaller state space.
*   D) Because fractional knapsack can be solved in O(1) per item by direct calculation, while 0/1 knapsack requires at least O(log n) per item due to its integer constraints.
*   **Correct Answer:** B) Because in fractional knapsack, items can be split so taking the maximum value-to-weight ratio fraction is always optimal; in 0/1 knapsack, items must be taken whole, and greedily taking the highest ratio item may prevent a better combination of remaining items.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The integer/float distinction is not the reason. The issue is whether items are divisible, not the data type of their weights or values.
    *   *Why B is correct:* In fractional knapsack, taking more of the highest-value-per-weight item never hurts — you can always adjust the fraction. In 0/1 knapsack, a greedy choice of a heavy high-ratio item may fill the knapsack and exclude a combination of lighter items with higher total value (classic counterexample: capacity 10, items (6, value 12) and (5, value 10) and (5, value 10)).
    *   *Why C is incorrect:* The state space sizes are related to the DP table, not to whether greedy works. Greedy correctness depends on problem structure, not state space size.
    *   *Why D is incorrect:* Fractional knapsack is O(n log n) due to sorting, not O(1) per item. Per-item time complexity is irrelevant to the correctness of the greedy strategy.

---

**Question 4**
In the Jump Game (LeetCode #55), you are given an array where `nums[i]` is the maximum jump length from position i. What does the greedy algorithm track to determine reachability?
*   A) The sum of all values in the array — if it exceeds n, you can always reach the end.
*   B) The maximum index reachable so far (`max_reach`), updated at each index i as `max(max_reach, i + nums[i])`; if i ever exceeds `max_reach`, the end is unreachable.
*   C) A stack of positions that have been visited — if the stack contains index n-1 at any point, the end is reachable.
*   D) The minimum value in the array — if no value is 0, you can always reach the end; otherwise DP is required.
*   **Correct Answer:** B) The maximum index reachable so far (`max_reach`), updated at each index i as `max(max_reach, i + nums[i])`; if i ever exceeds `max_reach`, the end is unreachable.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Array sum does not model reachability; a single 0 in the middle of an otherwise large-sum array can block all progress.
    *   *Why B is correct:* Tracking the farthest reachable index captures exactly what matters: from every position up to `max_reach`, can we extend further? If the current index i exceeds `max_reach`, we are stranded. This is O(n) and provably optimal.
    *   *Why C is incorrect:* A stack-based approach models DFS path tracking, not greedy reachability. It is also not how the greedy jump game solution works.
    *   *Why D is incorrect:* A 0 value only blocks progress if that position is unavoidable. Whether a 0 blocks you depends on the positions and values of other elements — the minimum value alone cannot determine reachability.

---

**Question 5**
You need to merge overlapping intervals from the list `[[1,3],[2,6],[8,10],[15,18]]`. After sorting by start time, what is the correct greedy merge step?
*   A) Remove all intervals that overlap with the first interval and replace them with a single interval spanning all removed intervals.
*   B) For each interval in sorted order, if it overlaps with the last interval in the result (current start ≤ last end), merge by extending the last end to max(last end, current end); otherwise add it as a new interval.
*   C) Use a stack: push each interval; if the top two intervals overlap, pop both and push their union.
*   D) Binary search for the correct insertion position of each interval in a sorted result list, then check neighbors for overlap and merge if needed.
*   **Correct Answer:** B) For each interval in sorted order, if it overlaps with the last interval in the result (current start ≤ last end), merge by extending the last end to max(last end, current end); otherwise add it as a new interval.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Removing all intervals overlapping the first would be O(n²) and does not produce a complete merged result in one step.
    *   *Why B is correct:* After sorting by start, overlapping intervals are adjacent. The greedy one-pass merge checks only the last interval in the result, since earlier intervals cannot overlap with the current one (they were processed in start-time order).
    *   *Why C is incorrect:* A stack approach works but is equivalent to B with extra complexity; the standard Merge Intervals solution uses a simple list, not a stack.
    *   *Why D is incorrect:* Binary search insertion is O(log n) per interval but O(n) per shift in a list, giving O(n²) total — worse than the O(n log n) sort-then-scan approach.
