# Lab Activity: Module 07 — Heaps & Priority Queues

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Implement a min-heap from scratch with push and pop
- **Part 2** — Use Python's `heapq` for the K-th largest pattern
- **Part 3** — LeetCode interview patterns: Kth Largest in Stream and Array

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Min-Heap from Scratch

**File:** `lab07_heap.py`

### 1.1 — Index Formula Verification

```python
# Array index formulas for a 0-indexed heap:
# Left child of node at index i:  2*i + 1
# Right child of node at index i: 2*i + 2
# Parent of node at index i:      (i - 1) // 2

def parent(i):
    return (i - 1) // 2

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2
```

Test:

```python
# For the heap [1, 3, 5, 4, 8, 7, 6]:
#          1 (i=0)
#         / \
#        3   5  (i=1, i=2)
#       / \ / \
#      4  8 7  6  (i=3, i=4, i=5, i=6)

print(left_child(0))   # 1 — left child of root
print(right_child(0))  # 2 — right child of root
print(parent(3))       # 1 — parent of index 3
print(parent(4))       # 1 — parent of index 4
print(parent(1))       # 0 — parent of index 1 is root
```

**Checkpoint:** All outputs match expected values.

---

### 1.2 — Heap Push (Sift Up)

```python
def heap_push(heap, val):
    """
    Insert val into the heap.
    Append to end, then sift up.
    Time: O(log n)
    """
    heap.append(val)
    i = len(heap) - 1
    while i > 0:
        p = parent(i)
        if heap[p] > heap[i]:      # min-heap violation: parent > child
            heap[p], heap[i] = heap[i], heap[p]
            i = p
        else:
            break
```

Test:

```python
h = []
for v in [5, 3, 8, 1, 9, 2, 7]:
    heap_push(h, v)

print(h)        # Min at h[0]; exact array order depends on insertion
print(h[0])     # 1 — always the minimum
```

**Checkpoint:** `h[0]` is `1` (the minimum). The array satisfies the heap property.

---

### 1.3 — Heap Pop (Extract-Min, Sift Down)

```python
def heap_pop(heap):
    """
    Remove and return the minimum element.
    Swap root with last, remove last, sift down.
    Time: O(log n)
    """
    if not heap:
        raise IndexError('pop from empty heap')
    if len(heap) == 1:
        return heap.pop()

    min_val = heap[0]
    heap[0] = heap.pop()    # last element becomes new root
    i = 0
    n = len(heap)

    while True:
        lc = left_child(i)
        rc = right_child(i)
        smallest = i

        if lc < n and heap[lc] < heap[smallest]:
            smallest = lc
        if rc < n and heap[rc] < heap[smallest]:
            smallest = rc

        if smallest == i:
            break     # heap property restored

        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest

    return min_val
```

Test:

```python
h = []
for v in [5, 3, 8, 1, 9, 2, 7]:
    heap_push(h, v)

print(heap_pop(h))  # 1
print(heap_pop(h))  # 2
print(heap_pop(h))  # 3
print(heap_pop(h))  # 5
print(heap_pop(h))  # 7
print(heap_pop(h))  # 8
print(heap_pop(h))  # 9
```

**Checkpoint:** Values pop in ascending order: `1, 2, 3, 5, 7, 8, 9`.

---

### 1.4 — Max-Heap Using Negation

```python
def max_heap_push(heap, val):
    heap_push(heap, -val)    # negate on push

def max_heap_pop(heap):
    return -heap_pop(heap)   # negate on pop
```

Test:

```python
mh = []
for v in [5, 3, 8, 1, 9, 2, 7]:
    max_heap_push(mh, v)

print(max_heap_pop(mh))  # 9 — largest first
print(max_heap_pop(mh))  # 8
print(max_heap_pop(mh))  # 7
```

**Checkpoint:** Values pop in descending order.

---

## Part 2 — Python heapq Patterns

**File:** `lab07_heapq.py`

### 2.1 — heapq Basics

```python
import heapq

# Build heap from list
data = [5, 3, 8, 1, 9, 2, 7]
heapq.heapify(data)          # O(n) — modifies in place
print(data[0])               # 1 — minimum

# Push and pop
heapq.heappush(data, 0)      # O(log n)
print(heapq.heappop(data))   # 0 — new minimum

# heapreplace: pop min and push new value in one O(log n) call
print(heapq.heapreplace(data, 100))  # returns old min, inserts 100
print(data[0])               # new minimum after replacement
```

---

### 2.2 — K-th Largest Element (LeetCode #215)

```python
def kth_largest(nums, k):
    """
    Return the k-th largest element in nums.
    Maintain a min-heap of size k.
    Time: O(n log k), Space: O(k)
    """
    heap = nums[:k]
    heapq.heapify(heap)           # min-heap of first k elements

    for num in nums[k:]:
        if num > heap[0]:         # larger than k-th largest so far
            heapq.heapreplace(heap, num)   # discard k-th, add new

    return heap[0]                # k-th largest is the heap minimum
```

Test:

```python
print(kth_largest([3, 2, 1, 5, 6, 4], 2))   # 5
print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
```

Trace the heap for `[3, 2, 1, 5, 6, 4]`, k=2:

```python
# Initial heap: heapify([3, 2]) → [2, 3]  (min-heap of size 2)
# num=1:  1 < heap[0]=2 → skip
# num=5:  5 > heap[0]=2 → heapreplace → heap=[3,5]
# num=6:  6 > heap[0]=3 → heapreplace → heap=[5,6]
# num=4:  4 < heap[0]=5 → skip
# Return heap[0] = 5 ✓
```

**Checkpoint:** Both tests pass. Submit to LeetCode #215.

---

### 2.3 — K-th Largest in a Stream (LeetCode #703)

```python
class KthLargest:
    """
    Maintains a min-heap of size k.
    add() inserts a new value and returns the k-th largest seen so far.
    """
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)   # discard smallest — not in top k
        return self.heap[0]
```

Test:

```python
obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))    # 4 — stream: [2,3,4,5,8], k=3, 3rd largest = 4
print(obj.add(5))    # 5
print(obj.add(10))   # 5
print(obj.add(9))    # 8
print(obj.add(4))    # 8
```

**Checkpoint:** Outputs match expected values. Submit to LeetCode #703.

---

## Part 3 — Integration Test

**File:** (add to `lab07_heapq.py`)

```python
def test_all():
    # Custom heap
    h = []
    for v in [5, 3, 8, 1]:
        heap_push(h, v)
    assert heap_pop(h) == 1
    assert heap_pop(h) == 3

    # heapq nlargest / nsmallest
    data = [5, 3, 8, 1, 9, 2, 7]
    assert heapq.nlargest(3, data) == [9, 8, 7]
    assert heapq.nsmallest(3, data) == [1, 2, 3]

    # K-th largest
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    print('All assertions passed.')

test_all()
```

**Checkpoint:** All assertions pass. LeetCode #215 and #703 submitted.

---

## Deliverables

Submit to Canvas:

1. `lab07_heap.py` — custom heap_push, heap_pop, max-heap tests
2. `lab07_heapq.py` — heapq patterns, K-th largest, KthLargest class, integration test
3. LeetCode submission screenshots for #703 and #215

---

## Summary

| Concept | Key Point |
|---|---|
| Min-heap property | Parent ≤ children at every node |
| Array indices | Left: 2i+1, Right: 2i+2, Parent: (i-1)//2 |
| Push (sift up) | Append, swap with parent while violation — O(log n) |
| Pop (sift down) | Swap root with last, remove, swap with smaller child — O(log n) |
| heapify | Bottom-up sift-down — O(n) |
| Max-heap in Python | Negate values: push `-val`, negate on pop |
| K-th largest | Min-heap of size K; discard elements ≤ heap[0] |
| heapreplace | Pop + push in one O(log n) call — use for K-th largest |
| Peek | heap[0] — O(1), no pop needed |

---

## Part 9 — Challenge Exercise

These steps are **optional** and ungraded. They are designed for students who want to deepen their understanding beyond the core lab.

### 9.1 — Median of a Data Stream (LeetCode #295)

Maintain a running median as integers arrive one at a time. The optimal O(log n) per insertion solution uses two heaps: a max-heap for the lower half and a min-heap for the upper half. After each insertion, rebalance so the two heaps differ in size by at most 1. `find_median()` returns `max_heap[0]` if sizes differ, or the average of both tops if equal. Implement `MedianFinder` with `add_num(val)` and `find_median()`, verify on the sequence `[1, 2, 3, 4, 5]` (medians: 1, 1.5, 2, 2.5, 3), and write a comment explaining why the two-heap approach is superior to sorting the entire array after each insertion.

### 9.2 — Task Scheduler (LeetCode #621)

Given a list of CPU tasks and a cooldown period `n`, find the minimum number of intervals to finish all tasks, where a task of the same type cannot be repeated within `n` intervals. The key insight is that the most frequent task dictates the minimum schedule length. Use a max-heap to always execute the most frequent available task, and a queue to track tasks in cooldown. Implement the greedy simulation, verify it returns 8 for `tasks = ['A','A','A','B','B','B'], n = 2`, and add a comment explaining why a greedy max-frequency strategy is optimal here.

### 9.3 — O(n) Heapify Proof by Analysis

The `heapq.heapify` function is O(n) despite appearing to call `sift_down` n/2 times (each O(log n)). The key is that most nodes are near the bottom and perform little work. Write a Python script that counts the actual number of sift-down comparisons performed during `heapify` for arrays of sizes n = 100, 1,000, 10,000, and 100,000 (constructed with worst-case reverse-sorted input). Compute the ratio `comparisons / n` for each and verify empirically that it converges to a constant — confirming O(n) behavior. Add a mathematical comment explaining that the sum Σ (h × n/2^h) from h=0 to log n converges to 2n, proving O(n).
