# Quiz: Module 13 — Greedy Algorithms

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the greedy criterion for the activity selection problem, and why does it produce an optimal solution?

- A) Always select the activity that starts earliest, because starting early maximizes time available
- B) Always select the activity that finishes earliest, because it leaves the most remaining time for future activities
- C) Always select the shortest activity (smallest finish − start), because short activities waste less time
- D) Always select the activity with the latest start time, to avoid conflicts with earlier activities

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Earliest-start greedy fails. Consider A=(0,10) and B=(1,2). Earliest-start picks A, which blocks B and all later activities. Earliest-finish picks B, leaving more room. Start time is irrelevant; what matters is when the slot is freed.
- *Why B is correct:* The earliest-finishing activity leaves the longest remaining time for subsequent activities. This is provably optimal via exchange argument: any optimal solution that does not start with the earliest-finishing activity can be modified to do so without reducing the total count — since the earliest-finishing activity vacates the slot at least as early as any alternative.
- *Why C is incorrect:* Shortest activity greedy also fails. A short activity that finishes late (e.g., (8,9) when sorted by duration but (4,5) finishes earlier) blocks later activities that the duration-based criterion would miss. Finish time, not duration, is the correct sort key.
- *Why D is incorrect:* Latest-start greedy would pick activities that begin late, ignoring the current state of occupancy. This is not a valid greedy criterion and produces suboptimal results.

---

### Question 2

In `can_jump`, what does `max_reach` represent, and what condition causes the function to return `False`?

```python
def can_jump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True
```

- A) `max_reach` is the number of jumps taken; `False` is returned when jumps exceed the array length
- B) `max_reach` is the farthest index reachable from any position seen so far; `False` is returned when the current index is beyond that reach
- C) `max_reach` is the index of the last jump; `False` is returned when `max_reach` equals the array length
- D) `max_reach` is the total fuel remaining; `False` is returned when fuel drops to zero

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `max_reach` is not a jump counter. The algorithm does not count jumps — it tracks the farthest reachable position. Jump Game II counts jumps; Jump Game I only needs reachability.
- *Why B is correct:* `max_reach` stores the maximum of `i + nums[i]` for all visited positions. If the current index `i` exceeds `max_reach`, no visited position can reach index `i` — it is permanently blocked. The condition `i > max_reach` catches exactly this.
- *Why C is incorrect:* The function does not check `max_reach == len(nums)`. It returns `True` at the end of the loop if every position was reachable (never triggered the `False` branch). The last index is implicitly covered if `max_reach >= len(nums) - 1`.
- *Why D is incorrect:* This conflates Jump Game I with Gas Station. Gas Station tracks fuel (running tank); Jump Game I tracks reachable position. The two algorithms solve different problems with different variables.

---

### Question 3

In Jump Game II, what do `current_end` and `farthest` represent, and when does `jumps` increment?

```python
def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
```

- A) `current_end` is the current position; `farthest` is the jump limit; `jumps` increments every step
- B) `current_end` is the end of the current BFS level (jump range); `farthest` is the farthest position reachable from that level; `jumps` increments when the current level is exhausted
- C) `current_end` is the last index; `farthest` tracks the minimum position; `jumps` increments when backtracking is needed
- D) `current_end` and `farthest` are both pointers into a priority queue; `jumps` increments when the queue is empty

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `current_end` is not the current position — it is the boundary of the current jump's reachable range. `jumps` does not increment at every step; it increments only when the range boundary is crossed.
- *Why B is correct:* The algorithm is a BFS-level metaphor. `current_end` is the rightmost position reachable with the current number of jumps (one BFS level). `farthest` is the farthest position reachable from any position in that level (the next BFS level's boundary). When `i == current_end`, the level is exhausted — one more jump is needed, and `current_end` advances to `farthest`.
- *Why C is incorrect:* The last index is fixed — it does not change. There is no backtracking in this greedy algorithm. Jump Game II never revises decisions.
- *Why D is incorrect:* There is no priority queue in Jump Game II. The algorithm uses only three integer variables and runs in O(n) time with O(1) space.

---

### Question 4

For `can_jump([3,2,1,0,4])`, trace the algorithm. What is `max_reach` just before returning False?

- A) 0
- B) 3
- C) 4
- D) 5

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `max_reach` starts at 0 but updates at i=0 to `max(0, 0+3)=3`. It does not stay at 0.
- *Why B is correct:* Trace: i=0,jump=3,max_reach=3; i=1,jump=2,max_reach=max(3,3)=3; i=2,jump=1,max_reach=max(3,3)=3; i=3,jump=0,max_reach=max(3,3)=3; i=4: `4 > 3` → return False. `max_reach` is 3 at the point of return.
- *Why C is incorrect:* `max_reach` would reach 4 if we could get to index 1 and use its jump of 3. But index 3 has jump 0, which means `max_reach` can never advance past 3. Index 4 is unreachable.
- *Why D is incorrect:* 5 would exceed the array bounds and cannot be a valid `max_reach` in this trace. `i + jump` at i=0 gives 3, the maximum in this example.

---

### Question 5

In the Gas Station problem, why does the algorithm reset `start = i + 1` whenever `current_tank < 0`?

- A) Because the station at `i` has no fuel — skipping it is always correct
- B) Because if the running total from `start` goes negative at station `i`, then no station in the range `[start, i]` can be a valid starting point — they all fail at or before station `i`
- C) Because `i + 1` is always the station with the most surplus fuel
- D) Because the circuit must start from the midpoint of the array

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The issue is not about any single station's fuel level — it is about the cumulative deficit from the current start to station `i`. Even a station with positive fuel could still fail if the running total from that station reaches zero at some later point.
- *Why B is correct:* This is the key correctness argument. If starting at `start` results in `current_tank < 0` by station `i`, then any intermediate starting station `start+1`, `start+2`, ..., `i` would have an even worse running total at station `i` (they start with less accumulated surplus). So none of them can be valid starts. The algorithm jumps ahead to `i+1` — the first station not yet proven invalid.
- *Why C is incorrect:* The algorithm does not look ahead at fuel levels. It resets to `i+1` purely because stations `0..i` have been eliminated, not because `i+1` is known to be rich in fuel.
- *Why D is incorrect:* There is no midpoint rule in the Gas Station algorithm. The starting point is determined dynamically by where the running total goes negative.

---

### Question 6

Why does greedy by value-per-weight ratio fail for the 0/1 knapsack, but work for the fractional knapsack?

- A) Greedy works for both; the 0/1 version requires a different sort order (by value, not ratio)
- B) In the fractional knapsack, any unused capacity can be filled with a partial item, so no item is "wasted." In the 0/1 knapsack, taking a high-ratio item may consume capacity that would be better used by a combination of whole items with higher total value
- C) The fractional knapsack requires O(n²) time so it can explore more combinations; greedy only works because it is faster
- D) Greedy fails for both problems — both require dynamic programming

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* No sort by value alone is correct for 0/1 knapsack. Even sorting by total value fails for the same reason — a high-value heavy item may block a better combination of smaller items. The problem requires DP, not a different sort.
- *Why B is correct:* In the fractional knapsack, if the highest-ratio item does not fill the capacity exactly, you fill the remainder with a fraction of the next best item — no capacity is wasted. This makes the greedy locally optimal decision globally optimal. In the 0/1 version, you cannot take fractions, so a high-ratio item that fills part of the capacity may block a better combination (e.g., in the counterexample, A at 6/kg blocks B+C at 4.4/kg average but 220 total vs. 160).
- *Why C is incorrect:* The fractional knapsack runs in O(n log n) — the same as the greedy 0/1 attempt. Speed has nothing to do with the correctness difference. The distinction is structural: divisibility of items.
- *Why D is incorrect:* Greedy is provably optimal for fractional knapsack. The exchange argument holds because any solution that takes less of the highest-ratio item and more of a lower-ratio item can be improved by swapping proportions.

---

### Question 7

In `can_complete_circuit`, what does `total_tank` track and what does its sign indicate?

- A) `total_tank` tracks the fuel at the starting station; negative means the starting station has no fuel
- B) `total_tank` tracks the net surplus/deficit across all stations combined; negative means no valid circuit is possible
- C) `total_tank` tracks the number of stations visited; negative is impossible
- D) `total_tank` tracks the current running fuel; negative means the algorithm must stop

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `total_tank` accumulates `gas[i] - cost[i]` across all stations — it is not the fuel at any individual station. At the end of the loop, it holds the total net surplus (or deficit) for the entire circuit.
- *Why B is correct:* `total_tank = sum(gas[i] - cost[i] for all i)`. If this total is negative, there is not enough gas in the entire circuit to complete it — no starting position can work. If it is non-negative, a valid starting position always exists (and the greedy reset gives it). This is the global feasibility check.
- *Why C is incorrect:* `total_tank` is a fuel quantity, not a count. Counts cannot be negative in this context.
- *Why D is incorrect:* `current_tank` is the running fuel (which can go negative and trigger a reset). `total_tank` is the cumulative global sum — it is not used as a stopping condition mid-loop.

---

### Question 8

Given activities: `(0,3), (1,4), (3,6), (4,7), (6,9)`. Applying the earliest-finish greedy, which activities are selected?

- A) (0,3), (1,4), (3,6)
- B) (0,3), (3,6), (6,9)
- C) (1,4), (4,7), (6,9)
- D) (0,3), (4,7)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* After selecting (0,3), (1,4) cannot be selected because start=1 < last_finish=3 (overlap). After (0,3), the next selectable activity is (3,6) (start=3 >= 3 — touching is allowed). Then (6,9) with start=6 >= 6. Result is (0,3), (3,6), (6,9) — not (1,4).
- *Why B is correct:* Sort by finish time: (0,3),(1,4),(3,6),(4,7),(6,9). Select (0,3), last_finish=3. Next: (1,4) — start=1 < 3, skip. Next: (3,6) — start=3 >= 3, select, last_finish=6. Next: (4,7) — start=4 < 6, skip. Next: (6,9) — start=6 >= 6, select. Result: (0,3),(3,6),(6,9) — 3 activities.
- *Why C is incorrect:* This would be the result if greedy started with (1,4) instead of (0,3). But (0,3) finishes first (finish=3 < 4), so it is selected first. Starting with (1,4) is not what earliest-finish greedy does.
- *Why D is incorrect:* Only 2 activities — this is suboptimal. (0,3) + (4,7) skips (3,6) which is compatible with (0,3) and (6,9).

---

### Question 9

What is the exchange argument, and why is it the standard correctness proof technique for greedy algorithms?

- A) The exchange argument swaps two elements in an array to sort it — it is the basis of bubble sort
- B) The exchange argument shows that any optimal solution that does not make the greedy choice at some step can be modified to make the greedy choice at that step without reducing solution quality — proving greedy solutions are always at least as good as optimal
- C) The exchange argument counts the number of inversions in a solution and shows greedy minimizes them
- D) The exchange argument proves that greedy algorithms always run faster than dynamic programming by comparing their recurrence relations

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The exchange argument in algorithm analysis is a proof technique, not a sorting operation. Bubble sort does perform adjacent swaps, but that is a coincidence of terminology — the exchange argument is a general proof strategy.
- *Why B is correct:* The exchange argument proceeds by contradiction: assume an optimal solution O does not follow the greedy choice. Identify the first step where they differ, swap the optimal's choice for the greedy choice, and show the modified solution is no worse. Repeating this transformation shows any optimal solution can be converted to the greedy solution step by step, proving greedy is optimal.
- *Why C is incorrect:* Inversion counting is a property of merge sort (Module 12), not the exchange argument. The exchange argument is not about counting inversions — it is about demonstrating that swapping in the greedy choice cannot hurt quality.
- *Why D is incorrect:* The exchange argument says nothing about speed; it only proves correctness. The performance comparison between greedy and DP is separate from the correctness argument.

---

### Question 10

A problem requires finding the minimum number of coins to make change for a given amount. The greedy approach (always pick the largest coin ≤ remaining amount) works for US coin denominations {1, 5, 10, 25} but fails for {1, 3, 4} with target 6. Why?

- A) Greedy fails for all coin systems — change-making always requires dynamic programming
- B) For {1,3,4} with target 6, greedy picks 4+1+1=3 coins, but the optimal is 3+3=2 coins. Greedy fails because the denominations lack the property that each coin's value divides the next — local optimality does not guarantee global optimality
- C) The greedy algorithm fails because 6 is not divisible by 4
- D) Greedy works for {1,3,4} — both give 2 coins; the question contains an error

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Greedy works for canonical coin systems like US denominations. The specific structure of the denomination set determines whether greedy is correct. For well-chosen denominations (like powers of a base), greedy is provably optimal.
- *Why B is correct:* With {1,3,4} and target 6: greedy picks 4 (largest ≤ 6, leaving 2), then 1 (largest ≤ 2, leaving 1), then 1 — total 3 coins. Optimal is 3+3 = 2 coins. The local choice of 4 blocks the globally better pair. US denominations have the "canonical" property (each denomination is approximately a multiple of the previous), which makes greedy work; {1,3,4} lacks this.
- *Why C is incorrect:* Divisibility of the target by the coin value is irrelevant to greedy correctness. The failure is due to the relationship between denominations, not the specific target value.
- *Why D is incorrect:* Greedy gives 3 coins (4+1+1), not 2. The example is correct — it is a well-known counterexample to greedy coin change.
