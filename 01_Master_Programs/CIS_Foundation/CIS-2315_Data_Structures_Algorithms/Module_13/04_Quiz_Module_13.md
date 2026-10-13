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

---

### Question 11

What is the time complexity of `activity_selection` on n activities, and what step dominates the runtime?

- A) O(n) — the single-pass selection loop is the bottleneck
- B) O(n log n) — sorting by finish time dominates; the selection pass is O(n)
- C) O(n²) — each activity is compared with all others
- D) O(log n) — binary search is used to find compatible activities

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n) describes only the selection loop after sorting. The full algorithm includes a sort step, which costs O(n log n). Because O(n log n) > O(n), the sort dominates.
- *Why B is correct:* Sorting n activities by finish time costs O(n log n) using comparison sort. The subsequent greedy selection pass makes a single left-to-right scan in O(n). Total: O(n log n) + O(n) = O(n log n). This is tight — you cannot avoid the sort when activities are given in arbitrary order.
- *Why C is incorrect:* O(n²) would arise from a nested loop comparing every pair of activities. The greedy selection avoids this by using the sorted order — at each step only one comparison (start ≥ last_finish) is needed.
- *Why D is incorrect:* There is no binary search in the standard activity selection algorithm. All compatibility checks are sequential against a single `last_finish` value.

---

### Question 12

For `jump([1,1,1,1])`, what is the minimum number of jumps returned by the Jump Game II greedy algorithm?

- A) 1
- B) 2
- C) 3
- D) 4

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* With `nums[0]=1`, the farthest reachable from index 0 is index 1. One jump reaches index 1, not the last index (3). At least 3 jumps are required.
- *Why B is incorrect:* Two jumps can reach at most index 2 (jump from 0→1→2). The last index is 3. Two jumps are insufficient.
- *Why C is correct:* Trace: i=0, farthest=1, i==current_end(0) → jumps=1, current_end=1. i=1, farthest=2, i==current_end(1) → jumps=2, current_end=2. i=2, farthest=3, i==current_end(2) → jumps=3, current_end=3. Loop ends at len-2=2. Return 3. Each step advances one index; three jumps are needed.
- *Why D is incorrect:* 4 jumps would be needed if we also jumped from the last index, but the loop runs to `range(len(nums)-1)` = `range(3)`, so i goes 0,1,2 — the last index is never jumped from. The answer is 3, not 4.

---

### Question 13

In `can_complete_circuit`, what is the value of `start` returned for `gas=[2,3,4], cost=[3,4,3]`?

- A) 0
- B) -1
- C) 2
- D) 1

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Starting at station 0: diff = 2−3 = −1. current_tank = −1 < 0 immediately. Station 0 is invalid. Additionally, total_tank = (2−3)+(3−4)+(4−3) = −1+−1+1 = −1 < 0. No circuit is possible.
- *Why B is correct:* total_tank = sum(gas) − sum(cost) = (2+3+4) − (3+4+3) = 9 − 10 = −1 < 0. The total fuel deficit means no starting station can complete the circuit. The function returns −1 regardless of where `start` ended up during the loop.
- *Why C is incorrect:* Station 2 has a surplus (4−3=+1) but the circuit cannot be completed because there is not enough total gas. The global feasibility check (total_tank ≥ 0) fails, so −1 is returned.
- *Why D is incorrect:* `start` may advance to 1 or 2 during the loop (due to resets), but the final return value is determined by `total_tank >= 0`, which is False. Return value is −1.

---

### Question 14

Which statement correctly describes the `erase_overlap_intervals` algorithm (LeetCode #435)?

- A) It uses earliest-start greedy and counts activities that start before the previous activity ends
- B) It sorts by finish time, keeps the earliest-finishing activity when overlap occurs, and counts the removed (overlapping) intervals
- C) It sorts by interval length and removes the longest intervals first
- D) It uses a stack to detect and remove nested intervals

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Earliest-start is not the correct greedy criterion here. The algorithm sorts by finish time. If sorted by start time, an activity that starts early but ends late could incorrectly be kept over one that starts later but ends sooner — blocking more future activities.
- *Why B is correct:* After sorting by finish time, the algorithm iterates through intervals. When an overlap is detected (`start < last_finish`), the current interval is removed (it overlaps with an earlier-finishing one that was already kept). `last_finish` is not updated — effectively keeping the interval that finishes earlier. The count of removals equals `n − max_non_overlapping_set_size`.
- *Why C is incorrect:* Removing the longest intervals first is not optimal. A single long interval might not overlap anything, while several shorter ones could all overlap each other. Duration is irrelevant; finish time is the correct sort key.
- *Why D is incorrect:* There is no stack involved. The algorithm uses a single variable `last_finish` and a counter `removals` — it is O(1) extra space (beyond the sort).

---

### Question 15

In the fractional knapsack with `items=[(60,10),(100,20),(120,30)]` and `capacity=50`, what is the maximum total value?

- A) 160.0 — take items A and B (greedy by ratio, only 30 kg used)
- B) 220.0 — take items B and C (optimal for 0/1 knapsack)
- C) 240.0 — take A, B, and a fraction of C
- D) 200.0 — take B and half of C

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* 160 is the greedy 0/1 knapsack result (items A + B = 30 kg), which fails because C doesn't fit in the remaining 20 kg. In the fractional knapsack, you can take a fraction of C — there is no reason to stop at 30 kg when 20 kg of capacity remain.
- *Why B is correct for 0/1 but wrong here:* 220 is the optimal 0/1 knapsack answer (B+C = 50 kg, value=220). But the fractional knapsack allows splitting, so we can do better: take A (ratio 6/kg), B (ratio 5/kg), and 20/30 of C (ratio 4/kg), giving 60+100+80 = 240.
- *Why C is correct:* Fractional knapsack sorts by ratio: A(6/kg), B(5/kg), C(4/kg). Take A (10 kg, value 60, cap left=40). Take B (20 kg, value 100, cap left=20). Take 20/30 of C (value = 120 × 20/30 = 80, cap left=0). Total = 60+100+80 = 240.
- *Why D is incorrect:* Taking B(20 kg=100) + half of C(15 kg=60) = 35 kg and value=160 — this does not fill capacity and ignores A which has a higher ratio than C.

---

### Question 16

What does the exchange argument prove about the activity selection algorithm, and what structural property of the problem does it rely on?

- A) It proves the algorithm runs in O(n log n) by showing the sort is unavoidable
- B) It proves correctness by showing any optimal solution that does not start with the earliest-finishing activity can be modified to do so, since the earliest-finishing activity is compatible with at least as many future activities as any alternative
- C) It proves the algorithm is stable by showing equal finish times are broken by start time
- D) It proves the algorithm terminates in at most n iterations without revisiting any activity

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The exchange argument proves correctness, not time complexity. The O(n log n) bound comes from the sorting analysis, which is separate from the exchange argument.
- *Why B is correct:* The exchange argument for activity selection: take any optimal set O. If O does not begin with the earliest-finishing activity A, identify the first activity X in O that conflicts with A. Replace X with A — since A finishes no later than X, every activity that was compatible with X is also compatible with A. The modified solution has the same count, so it is still optimal. Repeating this transformation yields the greedy solution, proving it is optimal.
- *Why C is incorrect:* Stability is a property of sorting algorithms, not greedy correctness. The exchange argument does not address tie-breaking. Activity selection with equal finish times still works correctly regardless of tie-breaking order.
- *Why D is incorrect:* Termination is guaranteed by the finite loop — it does not need a separate proof. The exchange argument specifically addresses optimality (solution quality), not termination.

---

### Question 17

What would `can_jump([0, 1])` return, and why?

- A) True — index 0 is the starting position, which is always reachable
- B) False — `max_reach` starts at 0, and `nums[0]=0` means we can only stay at index 0; index 1 is unreachable
- C) True — a jump of 0 at index 0 reaches the adjacent cell
- D) True — the last index is always reachable from the first

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Index 0 being reachable is trivially true, but that is not sufficient to reach the last index. `can_jump` must determine whether the *last* index is reachable. Starting at index 0 with `nums[0]=0` means no forward movement is possible.
- *Why B is correct:* Trace: i=0, jump=0, `max_reach = max(0, 0+0) = 0`. i=1: `1 > max_reach(0)` → return False. With a jump of 0, you cannot advance from index 0. Index 1 is unreachable.
- *Why C is incorrect:* A jump of 0 means zero steps forward — you remain at the same position. It does not reach any adjacent cell.
- *Why D is incorrect:* This is false as a general claim. `[3,2,1,0,4]` is a standard counterexample. Reachability depends entirely on the array values.

---

### Question 18

Why is greedy by earliest finish time correct for activity selection, but greedy by earliest start time incorrect?

- A) Both strategies give the same result; earliest-start is just slower to implement
- B) Earliest-start may select a long activity that blocks many compatible ones; earliest-finish guarantees the selected activity frees the resource as soon as possible, leaving the maximum time for future selections
- C) Earliest-start fails only when activities have equal start times; earliest-finish handles ties correctly
- D) Earliest-start is O(n²) while earliest-finish is O(n log n), so finish-time greedy is preferred for performance

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Earliest-start gives a different and suboptimal result in many cases. Consider A=(0,10) and B=(1,2), C=(3,4). Earliest-start picks A (start=0), blocking B and C — only 1 activity. Earliest-finish picks B then C — 2 activities.
- *Why B is correct:* The key invariant is that we want to free the resource (finish the current activity) as early as possible. Early finish leaves the longest contiguous remaining window for future activities. An early-starting but late-finishing activity monopolizes the resource, blocking alternatives. The exchange argument formalizes this: earliest-finish leaves at least as many options as any other choice.
- *Why C is incorrect:* Earliest-start fails on basic examples regardless of tie-breaking. The fundamental problem is not about ties — it is that start time has no bearing on when the resource becomes available.
- *Why D is incorrect:* Both strategies sort — either by start or finish time — costing O(n log n). The selection pass is O(n) for either. The difference is correctness, not performance.

---

### Question 19

Given `gas=[5,1,2,3,4]` and `cost=[4,4,1,5,1]`, what does `can_complete_circuit` return?

- A) 0
- B) 4
- C) -1
- D) 3

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* At station 0: diff=5−4=+1, current_tank=1. Station 1: diff=1−4=−3, current_tank=−2 < 0 → start=2, current_tank=0. Station 0 is eliminated as a valid start.
- *Why B is correct:* Trace: i=0: diff=1, total=1, curr=1. i=1: diff=−3, total=−2, curr=−2<0 → start=2, curr=0. i=2: diff=1, total=−1, curr=1. i=3: diff=−2, total=−3, curr=−1<0 → start=4, curr=0. i=4: diff=3, total=0, curr=3. total=0 ≥ 0 → return start=4. Starting at station 4: surplus 3, go to 0 (surplus+1=4), to 1 (4−3=1), to 2 (1+1=2), to 3 (2−2=0→fails?). Verify: 4(5−1=+4)→0(+1=5)→1(−3=2)→2(+1=3)→3(−2=1)→4 — completes! Answer is 4.
- *Why C is incorrect:* total_tank = (5+1+2+3+4)−(4+4+1+5+1) = 15−15 = 0 ≥ 0, so a valid circuit exists. The function does not return −1.
- *Why D is incorrect:* Station 3 is eliminated at i=3 when current_tank goes negative there, causing start to advance to 4. Station 3 cannot be the answer.

---

### Question 20

In Jump Game II, why does the loop run to `range(len(nums) - 1)` rather than `range(len(nums))`?

- A) To avoid an index-out-of-bounds error when accessing `nums[i+1]`
- B) Because once you reach the last index, no further jump is needed — the loop only needs to decide when to jump, not whether to jump from the end
- C) To handle the edge case where `nums` has only one element
- D) Because `farthest` always equals `len(nums) - 1` before the loop would reach the last index

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The loop body accesses `nums[i]` (not `nums[i+1]`), so there is no out-of-bounds risk even if iterating to `len(nums)`. The bound `len(nums)-1` is a logical choice, not a safety check.
- *Why B is correct:* The purpose of the loop is to count the number of jumps needed to reach the last index. If you are already at or past the last index, no more jumps are needed. Jumping "from" the last index is never counted — you stop when you arrive. Running to `len(nums)-1` excludes the last element from consideration as a jump source, which correctly avoids counting an unnecessary extra jump.
- *Why C is incorrect:* The single-element edge case is handled naturally: `range(len([x]) - 1) = range(0)` — the loop body never executes, and `jumps=0` is returned. This is correct (already at the last index). But this is a consequence of the bound, not the reason for it.
- *Why D is incorrect:* `farthest` may or may not equal `len(nums)-1` before the loop ends. The loop terminates when `i` reaches `len(nums)-2`, not when `farthest` hits any particular value. The claim is not generally true.
