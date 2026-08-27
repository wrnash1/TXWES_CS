# Reading Guide: Module 13 — Greedy Algorithms

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

A greedy algorithm builds a solution by making the locally optimal choice at each step and never revising past decisions. When greedy works, it is fast and elegant — often O(n) or O(n log n). The difficulty is proving correctness. Not every problem admits a greedy solution; the 0/1 knapsack problem is a canonical example where greedy fails and dynamic programming is required. This module covers three canonical greedy problems — activity selection, Jump Game, and Gas Station — along with the exchange argument proof technique and the contrast with dynamic programming.

---

## 1. The Greedy Strategy

Every greedy algorithm has the same structure:

1. **Sort** (if necessary) to impose an order that makes the locally optimal choice obvious.
2. **Iterate** through the candidates, always taking the locally best option.
3. **Never backtrack** — past decisions are not reconsidered.

The key design question: what is the "locally optimal" criterion, and does it guarantee global optimality?

### When Greedy Works

Greedy is provably correct when the problem exhibits the **greedy choice property**: a globally optimal solution can always be constructed by making locally optimal choices. This is established via an **exchange argument**.

### Exchange Argument Template

To prove that a greedy algorithm is correct:

1. Take any optimal solution O.
2. If O already agrees with the greedy choice, we are done.
3. If O does not make the greedy choice at some step, swap the greedy choice in: replace O's first differing decision with the greedy one.
4. Show that the modified solution is no worse than O.
5. By repeated exchange, the greedy solution is as good as any optimal solution.

---

## 2. Activity Selection

**Problem:** Given activities with start and finish times, select the maximum number of non-overlapping activities.

**Greedy criterion:** Always pick the activity that finishes earliest.

**Why it works:** The earliest-finishing activity leaves the most remaining time for future activities. Exchange argument: if an optimal solution starts with some activity X rather than the earliest-finishing activity A, swap X for A — since A finishes no later than X, the activities compatible with A are a superset of those compatible with X. The count cannot decrease.

```python
def activity_selection(activities):
    """
    Select maximum non-overlapping activities.
    activities: list of (start, finish) tuples.
    Returns list of selected (start, finish) tuples.
    Time: O(n log n) for sort, O(n) for selection.
    """
    activities.sort(key=lambda x: x[1])    # sort by finish time

    selected = [activities[0]]
    last_finish = activities[0][1]

    for start, finish in activities[1:]:
        if start >= last_finish:    # no overlap
            selected.append((start, finish))
            last_finish = finish

    return selected
```

**Trace example:**

```text
Activities: A(1,2), B(3,4), C(0,6), D(5,7), E(3,5), F(5,9)
Sorted by finish: A(1,2), B(3,4), E(3,5), C(0,6), D(5,7), F(5,9)

Select A(finish=2).
B: start=3 >= 2 → select (finish=4).
E: start=3 < 4 → skip.
C: start=0 < 4 → skip.
D: start=5 >= 4 → select (finish=7).
F: start=5 < 7 → skip.

Result: A, B, D — 3 activities. Optimal.
```

**Interval scheduling minimization (LeetCode #435):** Minimum number of intervals to remove to make the rest non-overlapping. Greedy by earliest finish, count the overlapping ones — complement of activity selection.

---

## 3. Jump Game

### Jump Game I (LeetCode #55)

**Problem:** Array where each element is the max jump length. Return True if you can reach the last index from index 0.

**Greedy insight:** Track the farthest index reachable from any position seen so far. If the current index exceeds the farthest reach, you are stuck.

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

**Trace:** `can_jump([2,3,1,1,4])`

```text
i=0, jump=2: max_reach = max(0, 2) = 2
i=1, jump=3: max_reach = max(2, 4) = 4
i=2, jump=1: max_reach = max(4, 3) = 4
i=3, jump=1: max_reach = max(4, 4) = 4
i=4, jump=4: max_reach = max(4, 8) = 8
Return True ✓
```

**Trace:** `can_jump([3,2,1,0,4])`

```text
i=0, jump=3: max_reach = 3
i=1, jump=2: max_reach = 3
i=2, jump=1: max_reach = 3
i=3, jump=0: max_reach = 3
i=4: i(4) > max_reach(3) → return False ✓
```

### Jump Game II (LeetCode #45)

**Problem:** Minimum jumps to reach the last index (guaranteed reachable).

**Greedy insight:** Use a BFS-level metaphor. `current_end` is the end of the current jump's range. `farthest` is the farthest point reachable from anywhere in the current range. When you exhaust the current range (reach `current_end`), you must use a jump — set `current_end = farthest`.

```python
def jump(nums):
    """
    Return minimum number of jumps to reach the last index.
    Time: O(n), Space: O(1)
    """
    jumps = 0
    current_end = 0    # end of current jump's reachable range
    farthest = 0       # farthest reachable from current range

    for i in range(len(nums) - 1):    # don't jump from last position
        farthest = max(farthest, i + nums[i])
        if i == current_end:    # exhausted current range — must jump
            jumps += 1
            current_end = farthest

    return jumps
```

**Trace:** `jump([2,3,1,1,4])`

```text
i=0: farthest=max(0,2)=2; i==current_end(0) → jumps=1, current_end=2
i=1: farthest=max(2,4)=4
i=2: farthest=max(4,3)=4; i==current_end(2) → jumps=2, current_end=4
Loop ends (i goes to len-2=3, but current_end=4 already covers last).
Return 2 ✓
```

---

## 4. Gas Station (LeetCode #134)

**Problem:** Gas stations in a circle; `gas[i]` fuel available, `cost[i]` fuel to reach next station. Find starting station to complete the circuit, or return -1 if impossible.

**Greedy insight (two key observations):**

1. If `sum(gas) >= sum(cost)`, a solution always exists (and is unique).
2. If the running tank goes negative starting from `start`, then `start` cannot be within the range that caused the deficit — reset to the next station.

```python
def can_complete_circuit(gas, cost):
    """
    Returns starting index or -1.
    Time: O(n), Space: O(1)
    """
    total_tank = 0
    current_tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_tank += diff
        current_tank += diff

        if current_tank < 0:
            start = i + 1    # stations 0..i cannot be the start
            current_tank = 0

    return start if total_tank >= 0 else -1
```

**Why resetting start works:** If the running total from `start` goes negative at station `i`, then no station between `start` and `i` (inclusive) can be the starting point — they would all fail at or before station `i`. So the candidate must be `i+1`.

**Trace:** `gas=[1,2,3,4,5]`, `cost=[3,4,5,1,2]`

```text
i=0: diff=-2, total=-2, curr=-2 < 0 → start=1, curr=0
i=1: diff=-2, total=-4, curr=-2 < 0 → start=2, curr=0
i=2: diff=-2, total=-6, curr=-2 < 0 → start=3, curr=0
i=3: diff=3,  total=-3, curr=3
i=4: diff=3,  total=0,  curr=6
total >= 0 → return start=3 ✓
```

---

## 5. When Greedy Fails: Fractional vs. 0/1 Knapsack

### Fractional Knapsack (greedy works)

Items can be split. Greedy criterion: sort by value-per-weight ratio (descending); take the most valuable fraction first.

```python
def fractional_knapsack(items, capacity):
    """
    items: list of (value, weight) tuples.
    Returns maximum value achievable within capacity.
    Time: O(n log n)
    """
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total = 0.0
    for value, weight in items:
        if capacity >= weight:
            total += value
            capacity -= weight
        else:
            total += value * (capacity / weight)    # take fraction
            break
    return total
```

### 0/1 Knapsack (greedy fails)

Items cannot be split; you take all or nothing. Greedy by ratio gives a suboptimal result:

```text
Capacity: 50 kg
Items: A(value=60, weight=10), B(value=100, weight=20), C(value=120, weight=30)
Ratios: A=6/kg, B=5/kg, C=4/kg

Greedy: take A(10kg), then B(20kg) = 30kg used; C needs 30kg but only 20kg remain.
Greedy total: 60 + 100 = 160

Optimal: take B(20kg) + C(30kg) = 50kg exactly.
Optimal total: 100 + 120 = 220

Greedy fails — ratio-optimal item A blocks the B+C combination.
```

**Why greedy fails:** Taking A (highest ratio) fills 10 kg and blocks the B+C combination that uses all 50 kg more efficiently. Without the ability to take fractions, greedy cannot anticipate this interaction. The 0/1 knapsack requires dynamic programming (Module 14).

---

## 6. Greedy vs. Dynamic Programming

| Property | Greedy | Dynamic Programming |
|---|---|---|
| Decision | One locally optimal choice | All choices explored via table |
| Revisit decisions | Never | Subproblems solved once, reused |
| Correctness proof | Exchange argument | Optimal substructure + overlap |
| Complexity | Usually O(n) or O(n log n) | Often O(n²) or O(n·W) |
| Activity selection | Works | Overkill |
| 0/1 Knapsack | Fails | Required |
| Shortest path (non-negative) | Dijkstra (greedy) | Bellman-Ford (DP) |

---

## 7. Interview Exam Tips

1. **Always sort before greedy** — most greedy algorithms require a sort to define the order of choices. State the sort criterion explicitly in interviews.

2. **State the greedy invariant** — for activity selection: "the selected set contains non-overlapping activities with the earliest finish times seen so far." This communicates correctness.

3. **Know the exchange argument** — the standard correctness proof for greedy. In interviews, saying "by exchange argument, any optimal solution that doesn't make the greedy choice can be modified to do so without reducing quality" demonstrates theoretical grounding.

4. **Jump Game II is a hidden BFS** — `current_end` and `farthest` mimic BFS levels. Recognizing this helps reconstruct the algorithm from memory.

5. **Gas Station reset insight** — the key observation is that if you cannot reach station i from some start, then no station in that entire failed range can be the start. This immediately gives an O(n) algorithm.

6. **Fractional vs. 0/1 knapsack** — greedy works for fractional (divide items); greedy fails for 0/1 (all or nothing). When you see "items cannot be split," the answer is dynamic programming.

7. **Greedy ≠ always correct** — a common mistake is applying greedy to a DP problem. The test: does the locally optimal choice at each step guarantee a globally optimal result? If in doubt, try a small counterexample.

8. **Jump Game I is O(n) with one variable** — just track `max_reach`. No sorting. No DP table. The moment `i > max_reach`, return False. This simplicity is what makes it a canonical greedy pattern.

---

## 8. Complexity Summary

| Algorithm | Time | Space | Notes |
|---|---|---|---|
| Activity selection | O(n log n) | O(n) | Sort by finish time |
| Jump Game I | O(n) | O(1) | Track max_reach |
| Jump Game II | O(n) | O(1) | Track current_end, farthest |
| Gas Station | O(n) | O(1) | Reset on negative tank |
| Fractional knapsack | O(n log n) | O(1) | Sort by value/weight |
| 0/1 knapsack (DP) | O(n·W) | O(n·W) | See Module 14 |

---

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Greedy Algorithms Visualization** — [https://visualgo.net/en/sorting](https://visualgo.net/en/sorting)
   VisuAlgo's sorting section includes animated visualizations of greedy sorting strategies. Use the step-through mode to observe how earliest-finish selection works and compare with other orderings.

2. **OpenDSA — Greedy Algorithms Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Greedy.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Greedy.html)
   Free interactive OER textbook chapter on greedy algorithms covering activity selection, Huffman coding, and Prim's/Kruskal's MST. Includes embedded exercises and correctness proofs using exchange arguments.

3. **NeetCode — Greedy Algorithms Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53leVF-FAN7fo0HmL2S9-Emvo](https://www.youtube.com/playlist?list=PLot-Xpze53leVF-FAN7fo0HmL2S9-Emvo)
   Free video walkthroughs for Jump Game I & II, Gas Station, and interval scheduling problems. Each video includes the greedy intuition, trace, and submitted LeetCode solution.

4. **MIT OCW 6.006 — Greedy Algorithms (Lecture Notes)** — [https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
   MIT lecture notes covering greedy algorithm design and exchange argument proofs. Includes worked examples with activity selection, interval graph coloring, and connections to Dijkstra's algorithm (a greedy shortest-path method).

5. **Algorithms Illuminated (Roughgarden) — Part 3 Free Chapters** — [https://www.algorithmsilluminated.org/](https://www.algorithmsilluminated.org/)
   Tim Roughgarden's free online textbook chapters covering greedy algorithms, scheduling problems, and the exchange argument proof technique. Companion to the Stanford Algorithms MOOC on Coursera (free to audit).

---

## 10. Study Checklist

- [ ] Watch the Module 13 video lecture by Professor Nash.
- [ ] Implement `activity_selection` and trace the example from the video.
- [ ] Implement `can_jump` and trace both examples (reachable and blocked).
- [ ] Implement `jump` and trace `[2,3,1,1,4]`.
- [ ] Implement `can_complete_circuit` and verify the reset logic.
- [ ] Implement `fractional_knapsack` and contrast with the 0/1 knapsack counterexample.
- [ ] Articulate the exchange argument for activity selection in your own words.
- [ ] Complete the Module 13 Lab.
- [ ] Complete the Module 13 Quiz.
- [ ] Solve LeetCode #55, #45, #134.
