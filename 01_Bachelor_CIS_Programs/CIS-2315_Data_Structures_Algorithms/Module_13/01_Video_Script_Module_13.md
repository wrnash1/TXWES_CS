# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 13 — Greedy Algorithms

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - The key concept: greedy makes locally optimal choices. Emphasize that greedy only works when local optimality guarantees global optimality — this requires a correctness proof, usually exchange argument.
> - Walk through the exchange argument for Activity Selection explicitly: "suppose the optimal solution doesn't take the earliest-finishing activity — swap it in, the result is no worse."
> - Jump Game I and II are the canonical greedy LeetCode problems. Trace both carefully.
> - Common mistakes: applying greedy to a DP problem (the 0/1 knapsack is NOT greedy), not sorting correctly before a greedy pass.
> - Distinguish greedy (one pass, locally optimal) from DP (all subproblems, globally optimal via table).

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 13 | Greedy Algorithms | CIS-2315"]**

"A greedy algorithm makes the locally optimal choice at each step and never reconsiders past decisions. When greedy works, it is remarkably simple and fast — often O(n) or O(n log n). The challenge is proving that greedy works for a given problem. This module covers three canonical greedy algorithms: activity selection, interval scheduling, and the Jump Game. It also clarifies when greedy fails — specifically, why the 0/1 knapsack problem requires dynamic programming instead."

---

## [01:30 – 08:00] Part 1 — Activity Selection and Interval Scheduling

**[SHOW SLIDE: "Activity Selection — Greedy by Earliest Finish Time"]**

"Given a list of activities with start and finish times, select the maximum number of non-overlapping activities.

**[SHOW DIAGRAM: activities as horizontal bars on a timeline]**

```text
Activity:  A   B   C   D   E   F
Start:     1   3   0   5   3   5
Finish:    2   4   6   7   5   9
```

Greedy strategy: always pick the activity that finishes earliest. This leaves the most room for future activities.

[PAUSE]

```python
def activity_selection(activities):
    """
    Select maximum non-overlapping activities.
    activities: list of (start, finish) tuples.
    Returns list of selected (start, finish) tuples.
    Time: O(n log n) for sort, O(n) for selection.
    """
    # Sort by finish time
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_finish = activities[0][1]

    for start, finish in activities[1:]:
        if start >= last_finish:    # no overlap
            selected.append((start, finish))
            last_finish = finish

    return selected
```

**[DEMO: trace on activities above — sorted by finish: A(1,2), B(3,4), E(3,5), D(5,7), C(0,6), F(5,9)]**

Wait — let me sort correctly: A(1,2), B(3,4), E(3,5), C(0,6), D(5,7), F(5,9).

Selected: A(finish=2). Next B: start=3 >= 2 → select B(finish=4). Next E: start=3 < 4 → skip. Next C: start=0 < 4 → skip. Next D: start=5 >= 4 → select D(finish=7). Next F: start=5 < 7 → skip.

Result: A, B, D — 3 activities. This is optimal.

[PAUSE]

**Why does earliest-finish greedy work?** Exchange argument: suppose an optimal solution selects activity X as its first choice instead of the earliest-finishing activity A. Since A finishes no later than X, we can replace X with A in the optimal solution — the remaining available activities don't decrease. So any optimal solution can be converted to one that starts with A, without reducing the total count."

---

## [08:00 – 14:00] Part 2 — Jump Game I and II

**[SHOW SLIDE: "Jump Game — Greedy Reachability"]**

"**Jump Game I (LeetCode #55):** Given an array where each element is the maximum jump length, return True if you can reach the last index from index 0.

Greedy: track the furthest index reachable from any position seen so far.

```python
def can_jump(nums):
    """
    Return True if we can reach the last index.
    Time: O(n), Space: O(1)
    """
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False    # can't reach this position
        max_reach = max(max_reach, i + jump)
    return True
```

**[DEMO: `can_jump([2,3,1,1,4])` — trace: max_reach=0;i=0,jump=2,reach=2;i=1,jump=3,reach=4;i=2,reach=3 no update;i=3,reach=4;i=4,reach=8 → return True]**

**[DEMO: `can_jump([3,2,1,0,4])` — trace: i=3,max_reach=3;i=4,i>max_reach → return False]**

[PAUSE]

**Jump Game II (LeetCode #45):** Minimum number of jumps to reach the last index (guaranteed reachable).

Greedy: at each jump, choose the option that extends the furthest reach.

```python
def jump(nums):
    """
    Return minimum number of jumps to reach the last index.
    Time: O(n), Space: O(1)
    """
    jumps = 0
    current_end = 0    # end of current jump's range
    farthest = 0       # farthest reachable from current range

    for i in range(len(nums) - 1):    # don't need to jump from last position
        farthest = max(farthest, i + nums[i])
        if i == current_end:    # exhausted current jump range
            jumps += 1
            current_end = farthest

    return jumps
```

**[DEMO: `jump([2,3,1,1,4])` — trace:]**

```text
i=0: farthest=max(0,0+2)=2; i==current_end(0) → jumps=1, current_end=2
i=1: farthest=max(2,1+3)=4
i=2: farthest=max(4,2+1)=4; i==current_end(2) → jumps=2, current_end=4
Return jumps=2 ✓
```"

---

## [14:00 – 19:00] Part 3 — When Greedy Fails

**[SHOW SLIDE: "Greedy Failure: 0/1 Knapsack"]**

"Greedy works when local optimality implies global optimality. It fails when taking the best current choice forecloses a better future choice.

**Fractional Knapsack** (greedy works): items can be divided. Sort by value/weight ratio; take the most valuable fraction first.

```python
def fractional_knapsack(items, capacity):
    """
    items: list of (value, weight) tuples.
    Returns maximum value for given capacity.
    """
    # Sort by value-to-weight ratio descending
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    total = 0
    for value, weight in items:
        if capacity >= weight:
            total += value
            capacity -= weight
        else:
            total += value * (capacity / weight)    # take fraction
            break
    return total
```

**0/1 Knapsack** (greedy fails): items cannot be divided; you take all or nothing.

```text
Capacity: 50kg
Items: A(60, 10kg), B(100, 20kg), C(120, 30kg)

Greedy by ratio: A=6/kg, C=4/kg, B=5/kg → take A(10kg), B(20kg), remainder 20kg → C can't fit (30kg needed)
Total: 60 + 100 = 160

Optimal: take B(20kg) + C(30kg) = 50kg → total 220

Greedy gives 160; optimal is 220. Greedy fails.
```

[PAUSE]

The reason: taking the highest-ratio item (A) fills space and prevents the combination B+C that has better total value. Without fractional option, greedy cannot see this.

**0/1 Knapsack requires dynamic programming** — see Module 14."

---

## [19:00 – 23:00] Part 4 — Gas Station (LeetCode #134)

**[SHOW SLIDE: "Gas Station — Circular Greedy"]**

"Given gas stations arranged in a circle, each with `gas[i]` liters of fuel and `cost[i]` to reach the next station, find the starting station index to complete the circuit, or -1 if impossible.

```python
def can_complete_circuit(gas, cost):
    """
    Returns starting index or -1.
    Key insight: if total gas >= total cost, a solution exists.
    Start greedily: reset whenever running total goes negative.
    Time: O(n)
    """
    total_tank = 0
    current_tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_tank += diff
        current_tank += diff

        if current_tank < 0:
            start = i + 1    # can't start at or before i — try next
            current_tank = 0

    return start if total_tank >= 0 else -1
```

**[DEMO: gas=[1,2,3,4,5], cost=[3,4,5,1,2]]**

```text
i=0: diff=-2, total=-2, curr=-2 < 0 → start=1, curr=0
i=1: diff=-2, total=-4, curr=-2 < 0 → start=2, curr=0
i=2: diff=-2, total=-6, curr=-2 < 0 → start=3, curr=0
i=3: diff=3, total=-3, curr=3
i=4: diff=3, total=0, curr=6
total >= 0 → return start=3 ✓
```

The greedy insight: if total gas >= total cost, a solution always exists and is unique. When the running tank goes negative at station i, none of stations 0..i can be the start — reset to i+1.

The Module 13 lab covers activity selection, Jump Game I and II, and the Gas Station problem, plus a comparison of fractional vs 0/1 knapsack. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 13 — Greedy Algorithms]**

---

## Additional Resources

- [NeetCode — Greedy Algorithms Playlist](https://www.youtube.com/watch?v=3GT1d7rCZ_s)
- [LeetCode #55 — Jump Game](https://leetcode.com/problems/jump-game/)
- [LeetCode #45 — Jump Game II](https://leetcode.com/problems/jump-game-ii/)
- [LeetCode #134 — Gas Station](https://leetcode.com/problems/gas-station/)
- [LeetCode #435 — Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
