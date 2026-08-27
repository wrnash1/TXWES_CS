# Lab Activity: Module 13 — Greedy Algorithms

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Activity selection and interval scheduling
- **Part 2** — Jump Game I and II
- **Part 3** — Gas Station and fractional vs. 0/1 knapsack comparison

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Activity Selection

**File:** `lab13_greedy.py`

### 1.1 — Activity Selection Implementation

```python
def activity_selection(activities):
    """
    Select maximum non-overlapping activities.
    activities: list of (start, finish) tuples.
    Returns list of selected (start, finish) tuples.
    Time: O(n log n)
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

Test:

```python
acts = [(1,2), (3,4), (0,6), (5,7), (3,5), (5,9)]
result = activity_selection(acts)
print(result)    # [(1, 2), (3, 4), (5, 7)]

# Edge cases
print(activity_selection([(0,10)]))          # [(0, 10)] — single activity
print(activity_selection([(1,2), (2,3)]))    # [(1, 2), (2, 3)] — touching but not overlapping
print(activity_selection([(0,5), (1,6)]))    # [(0, 5)] — fully nested, only first selected
```

**Checkpoint:** Result for the main test is `[(1, 2), (3, 4), (5, 7)]` — three non-overlapping activities. Touching activities (`start == last_finish`) are allowed.

---

### 1.2 — Interval Scheduling: Minimum Removals (LeetCode #435)

Find the minimum number of intervals to remove to make the rest non-overlapping.

```python
def erase_overlap_intervals(intervals):
    """
    Return minimum number of intervals to remove to make non-overlapping.
    Greedy: sort by finish time, count overlaps.
    Time: O(n log n)
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    removals = 0
    last_finish = intervals[0][1]

    for start, finish in intervals[1:]:
        if start < last_finish:    # overlap — remove this interval
            removals += 1
            # Keep the one that finishes earlier (last_finish is already the smaller)
        else:
            last_finish = finish    # no overlap — advance

    return removals
```

Test:

```python
print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))    # 1 — remove [1,3]
print(erase_overlap_intervals([[1,2],[1,2],[1,2]]))          # 2 — remove two duplicates
print(erase_overlap_intervals([[1,2],[2,3]]))                # 0 — already non-overlapping
```

**Checkpoint:** All three tests match expected values. The key insight: the maximum non-overlapping set (activity selection) gives `n - max_non_overlapping = removals`.

---

## Part 2 — Jump Game

### 2.1 — Jump Game I (LeetCode #55)

```python
def can_jump(nums):
    """
    Return True if we can reach the last index.
    Greedy: track the farthest reachable index.
    Time: O(n), Space: O(1)
    """
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False    # current position unreachable
        max_reach = max(max_reach, i + jump)
    return True
```

Test:

```python
print(can_jump([2,3,1,1,4]))    # True
print(can_jump([3,2,1,0,4]))    # False
print(can_jump([0]))            # True — already at last index
print(can_jump([1,0,0]))        # False — stuck at index 1
print(can_jump([2,0,0]))        # True — jump over zeros
```

**Trace `can_jump([3,2,1,0,4])`:**

```text
i=0, jump=3: max_reach=3
i=1, jump=2: max_reach=max(3,3)=3
i=2, jump=1: max_reach=max(3,3)=3
i=3, jump=0: max_reach=max(3,3)=3
i=4: 4 > max_reach(3) → return False ✓
```

**Checkpoint:** All five tests pass.

---

### 2.2 — Jump Game II (LeetCode #45)

```python
def jump(nums):
    """
    Return minimum number of jumps to reach the last index.
    Guaranteed reachable. Greedy BFS-level approach.
    Time: O(n), Space: O(1)
    """
    jumps = 0
    current_end = 0    # end of current jump's reachable range
    farthest = 0       # farthest reachable from positions in current range

    for i in range(len(nums) - 1):    # no jump needed from the last position
        farthest = max(farthest, i + nums[i])
        if i == current_end:    # exhausted this range — must take a jump
            jumps += 1
            current_end = farthest

    return jumps
```

Test:

```python
print(jump([2,3,1,1,4]))    # 2
print(jump([2,3,0,1,4]))    # 2
print(jump([1,2,3]))        # 2
print(jump([0]))            # 0 — already at the end
```

**Trace `jump([2,3,1,1,4])`:**

```text
jumps=0, current_end=0, farthest=0

i=0: nums[0]=2 → farthest=max(0,0+2)=2; i==current_end(0) → jumps=1, current_end=2
i=1: nums[1]=3 → farthest=max(2,1+3)=4
i=2: nums[2]=1 → farthest=max(4,2+1)=4; i==current_end(2) → jumps=2, current_end=4
i=3: (loop ends at len-2=3, current_end=4 already covers index 4)

Return 2 ✓
```

**Checkpoint:** All four tests pass. Submit `can_jump` and `jump` to LeetCode #55 and #45.

---

## Part 3 — Gas Station and Knapsack

### 3.1 — Gas Station (LeetCode #134)

```python
def can_complete_circuit(gas, cost):
    """
    Returns starting station index to complete circuit, or -1 if impossible.
    Key insight: if total(gas) >= total(cost), a solution exists.
    Greedy reset: when running total goes negative, reset start to next station.
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
            start = i + 1      # stations 0..i cannot be the start
            current_tank = 0

    return start if total_tank >= 0 else -1
```

Test:

```python
print(can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]))    # 3
print(can_complete_circuit([2,3,4], [3,4,3]))             # -1
print(can_complete_circuit([5], [4]))                     # 0
print(can_complete_circuit([1,2], [2,1]))                 # 1
```

**Trace `gas=[1,2,3,4,5], cost=[3,4,5,1,2]`:**

```text
i=0: diff=-2, total=-2, curr=-2 < 0 → start=1, curr=0
i=1: diff=-2, total=-4, curr=-2 < 0 → start=2, curr=0
i=2: diff=-2, total=-6, curr=-2 < 0 → start=3, curr=0
i=3: diff=3,  total=-3, curr=3
i=4: diff=3,  total=0,  curr=6
total=0 >= 0 → return start=3 ✓
```

**Checkpoint:** All four tests pass. Submit to LeetCode #134.

---

### 3.2 — Fractional Knapsack

```python
def fractional_knapsack(items, capacity):
    """
    items: list of (value, weight) tuples.
    Returns maximum value for given capacity. Items can be split.
    Time: O(n log n)
    """
    items.sort(key=lambda x: x[0] / x[1], reverse=True)    # sort by ratio
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

Test:

```python
items = [(60, 10), (100, 20), (120, 30)]
print(fractional_knapsack(items, 50))    # 240.0
# Ratios: A=6/kg, B=5/kg, C=4/kg
# Take A(10kg)=60, B(20kg)=100, C(20/30 of 120)=80 → total=240
```

---

### 3.3 — 0/1 Knapsack Counterexample (Greedy Fails)

```python
def greedy_01_knapsack_wrong(items, capacity):
    """
    INCORRECT greedy approach for 0/1 knapsack.
    Shows why greedy fails: demonstrates the counterexample.
    """
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total = 0
    for value, weight in items:
        if capacity >= weight:    # must take whole item
            total += value
            capacity -= weight
    return total

# Compare greedy (wrong) vs optimal (manual inspection)
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

greedy_result = greedy_01_knapsack_wrong(items[:], capacity)
print(f'Greedy result: {greedy_result}')    # 160 — takes A(60) + B(100), C doesn't fit

# Optimal: take B(20kg) + C(30kg) = 50kg → 220
print(f'Optimal result: 220')
print(f'Greedy is suboptimal by: {220 - greedy_result}')    # 60
```

**Checkpoint output:**

```text
Greedy result: 160
Optimal result: 220
Greedy is suboptimal by: 60
```

**Why greedy fails here:** Taking A (ratio 6/kg) fills 10 kg and leaves 40 kg. B takes 20 kg (now 20 kg left). C needs 30 kg — doesn't fit. But B+C fills all 50 kg for 220. The high-ratio item A blocked the better combination.

---

### 3.4 — Integration Test

```python
def test_all():
    # Activity selection
    assert activity_selection([(1,2),(3,4),(0,6),(5,7),(3,5),(5,9)]) == [(1,2),(3,4),(5,7)]

    # Interval removal
    assert erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert erase_overlap_intervals([[1,2],[2,3]]) == 0

    # Jump Game I
    assert can_jump([2,3,1,1,4]) == True
    assert can_jump([3,2,1,0,4]) == False

    # Jump Game II
    assert jump([2,3,1,1,4]) == 2
    assert jump([2,3,0,1,4]) == 2

    # Gas Station
    assert can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]) == 3
    assert can_complete_circuit([2,3,4], [3,4,3]) == -1

    # Fractional knapsack
    result = fractional_knapsack([(60,10),(100,20),(120,30)], 50)
    assert abs(result - 240.0) < 1e-9

    # 0/1 knapsack greedy failure
    assert greedy_01_knapsack_wrong([(60,10),(100,20),(120,30)], 50) == 160

    print('All assertions passed.')

test_all()
```

**Checkpoint:** All assertions pass.

---

## Deliverables

Submit to Canvas:

1. `lab13_greedy.py` — all implementations and integration test
2. LeetCode submission screenshots for #55, #45, and #134
3. Short written answer (3–5 sentences): Explain why greedy works for activity selection but fails for 0/1 knapsack. Your answer must include the phrase "exchange argument" when explaining activity selection, and must give a concrete counterexample (with numbers) showing where greedy goes wrong for 0/1 knapsack.

---

## Summary

| Concept | Key Point |
|---|---|
| Activity selection | Sort by finish time; earliest-finish greedy is optimal — exchange argument |
| Interval removal | Complement: n minus max non-overlapping |
| Jump Game I | Track `max_reach`; return False when `i > max_reach` |
| Jump Game II | BFS-level metaphor: `current_end` / `farthest` / `jumps` |
| Gas Station | Reset `start = i+1` when `current_tank < 0`; return -1 if `total_tank < 0` |
| Fractional knapsack | Greedy by value/weight ratio — optimal |
| 0/1 knapsack | Greedy fails — requires DP (Module 14) |

---

## Part 9 — Challenge Exercise

These steps are **optional** and ungraded. They are designed for students who want to deepen their understanding beyond the core lab.

### 9.1 — Non-Overlapping Intervals with Meeting Rooms (LeetCode #252 / #253)

LeetCode #252 (Meeting Rooms) asks whether a person can attend all meetings given a list of time intervals. LeetCode #253 (Meeting Rooms II) asks the minimum number of conference rooms required. Solve both problems. For #252, sort by start time and check consecutive overlap in O(n log n). For #253, use a min-heap to track when rooms free up: push end times onto the heap; if the next meeting's start is after `heap[0]`, pop the earliest ending room and reuse it; otherwise push a new room. Verify that your #253 solution handles overlapping intervals, back-to-back intervals (touching is allowed), and a single interval. Explain why a greedy min-heap is optimal for #253 and state the time complexity.

### 9.2 — Task Scheduler (LeetCode #621)

Given a list of CPU tasks (each labeled A–Z) and a cooldown period `n`, find the minimum time to complete all tasks. The greedy insight is to always schedule the most frequent remaining task, using idle slots when no valid task exists. Implement the solution using a max-heap (negate counts for Python's min-heap) and a cooldown queue of `(count, available_at_time)` tuples. Trace through `tasks=["A","A","A","B","B","B"], n=2` step by step, showing the heap state after each scheduling decision. Verify the output is 8, and explain why greedy by frequency is optimal here whereas a different ordering could produce a longer schedule.

### 9.3 — Huffman Encoding (Greedy + Priority Queue)

Huffman coding is a classic greedy algorithm for lossless data compression. Given a frequency table for characters, build an optimal prefix-free binary encoding tree: repeatedly merge the two lowest-frequency nodes into a parent node (using a min-heap), until only one root remains. Implement `build_huffman_tree(freq_table)` that returns a dict mapping each character to its binary code string. Verify on `{'a':5, 'b':9, 'c':12, 'd':13, 'e':16, 'f':45}` — character 'f' should have the shortest code (1 bit) and 'a' the longest. Prove the exchange argument: if any two leaves at equal depth are swapped, the total weighted path length cannot decrease, confirming the greedy merge is optimal.
