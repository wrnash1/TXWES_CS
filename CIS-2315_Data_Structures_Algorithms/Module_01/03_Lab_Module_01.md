# Lab Activity: Module 01 — Big-O Notation and Complexity Analysis

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Benchmark complexity classes with Python timing code
- **Part 2** — Complexity analysis by inspection
- **Part 3** — LeetCode integration: solve, analyze, annotate

**Lab environment:** Python 3 (VS Code terminal or any Python REPL). No external packages are required — only the standard library.

---

## Part 1 — Benchmarking Complexity Classes

**File:** `lab01_benchmark.py`

### 1.1 — Setup

Create `lab01_benchmark.py`. The goal is to measure actual runtime across multiple input sizes and observe how it scales.

```python
import time
import random

def time_it(fn, *args):
    """Run fn(*args) and return elapsed time in milliseconds."""
    start = time.perf_counter()
    fn(*args)
    return (time.perf_counter() - start) * 1000

SIZES = [1_000, 5_000, 10_000, 50_000, 100_000]
```

### 1.2 — O(1): Constant Time

```python
def constant(arr):
    return arr[0] + arr[-1]   # two array accesses regardless of size

print("=== O(1): Array Access ===")
for n in SIZES:
    arr = list(range(n))
    ms = time_it(constant, arr)
    print(f"  n={n:>7}: {ms:.4f}ms")
```

**What to observe:** The time stays essentially flat regardless of n. This is constant time.

---

### 1.3 — O(n): Linear Time

```python
def linear_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print("\n=== O(n): Linear Sum ===")
for n in SIZES:
    arr = list(range(n))
    ms = time_it(linear_sum, arr)
    print(f"  n={n:>7}: {ms:.4f}ms")
```

**What to observe:** When n doubles (1,000 → 2,000), time approximately doubles. This is linear growth.

---

### 1.4 — O(n²): Quadratic Time

```python
def quadratic_pairs(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == 0:   # dummy work
                count += 1
    return count

print("\n=== O(n²): Quadratic Pairs ===")
small_sizes = [500, 1_000, 2_000, 3_000]   # use smaller sizes — O(n²) is slow
for n in small_sizes:
    arr = list(range(-n//2, n//2))
    ms = time_it(quadratic_pairs, arr)
    print(f"  n={n:>7}: {ms:.2f}ms")
```

**What to observe:** When n doubles (1,000 → 2,000), time quadruples. This is quadratic growth.

---

### 1.5 — O(n log n): Log-Linear Time

```python
def nlogn_sort(arr):
    return sorted(arr)   # Python's Timsort — O(n log n)

print("\n=== O(n log n): Built-in Sort ===")
for n in SIZES:
    arr = list(range(n))
    random.shuffle(arr)
    ms = time_it(nlogn_sort, arr)
    print(f"  n={n:>7}: {ms:.4f}ms")
```

**What to observe:** When n doubles, time grows by a little more than double — slightly faster than O(n²), clearly faster than O(n²), slower growth than would be expected for O(n). This is the characteristic of O(n log n).

---

### 1.6 — Comparison Summary

After running all sections, answer these questions in a comment at the top of your file:

```python
# ANALYSIS:
# 1. For n=1000 vs n=2000, what was the approximate ratio of times for O(n)?
# 2. For n=1000 vs n=2000, what was the approximate ratio of times for O(n²)?
# 3. Which function took the longest for n=100,000 and why?
# 4. Did O(1) time change at all? Why or why not?
```

**Checkpoint:** Your output should show clearly distinguishable scaling behavior across the four complexity classes. O(n²) should be dramatically slower than O(n) for the same input size.

---

## Part 2 — Complexity Analysis by Inspection

**File:** `lab01_analysis.py`

For each function below, determine the time complexity and space complexity. Write your answers as comments.

```python
# For each function, write:
# Time: O(?)  —  Reason: (explain in one sentence)
# Space: O(?)  —  Reason: (explain in one sentence)

# --- Function A ---
def fn_a(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Time: O(?)
# Space: O(?)

# --- Function B ---
def fn_b(arr):
    result = []
    for item in arr:
        result.append(item * 2)
    return result

# Time: O(?)
# Space: O(?)

# --- Function C ---
def fn_c(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False

# Time: O(?)
# Space: O(?)

# --- Function D ---
def fn_d(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:
                return True
    return False

# Time: O(?)
# Space: O(?)

# --- Function E ---
def fn_e(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Time: O(?)
# Space: O(?)

# --- Function F ---
def fn_f(n):
    if n <= 1:
        return n
    return fn_f(n - 1) + fn_f(n - 2)   # naive Fibonacci

# Time: O(?)   (hint: draw the recursion tree for small n)
# Space: O(?)

# --- Function G ---
def fn_g(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += matrix[i][j] * matrix[j][k]
    return total

# Time: O(?)
# Space: O(?)

# --- Function H ---
def fn_h(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left  = fn_h(arr[:mid])
    right = fn_h(arr[mid:])
    return sorted(left + right)   # O(n) merge at each level

# Time: O(?)
# Space: O(?)
```

**Answers to verify your work:**

```text
A: Time O(n), Space O(1)
B: Time O(n), Space O(n)
C: Time O(n), Space O(n)
D: Time O(n²), Space O(1)
E: Time O(log n), Space O(1)
F: Time O(2ⁿ), Space O(n) — recursion depth n
G: Time O(n³), Space O(1)
H: Time O(n log n), Space O(n log n) — new arrays at each level
```

**Checkpoint:** You should be able to explain each answer in one sentence without reference to the answer key.

---

## Part 3 — LeetCode Integration

### 3.1 — Solve Two Sum (LeetCode #1)

Navigate to [LeetCode #1 — Two Sum](https://leetcode.com/problems/two-sum/). Read the problem statement carefully.

Implement the brute-force solution first in `lab01_leetcode.py`:

```python
# Brute force — O(n²) time, O(1) space
def two_sum_brute(nums, target):
    # YOUR IMPLEMENTATION
    pass

# Optimized — O(n) time, O(n) space
def two_sum_optimized(nums, target):
    # YOUR IMPLEMENTATION
    pass
```

Verify both solutions pass the LeetCode test cases by submitting the optimized version.

### 3.2 — Complexity Annotation

Add complexity annotations to your solution file:

```python
# two_sum_brute:
#   Time: O(n²)  — two nested loops, each 0..n
#   Space: O(1)  — no extra data structures, only index variables
#
# two_sum_optimized:
#   Time: O(n)   — single pass; dict lookup/insert is O(1) amortized
#   Space: O(n)  — seen dict holds up to n key-value pairs
#
# Trade-off: optimized version uses O(n) extra memory to reduce time by a
# factor of n. For n=10,000, that is 10,000x speedup at the cost of
# negligible memory in practice.
```

### 3.3 — Benchmark Both Solutions

Add timing code to measure both approaches:

```python
import time

test_cases = [
    ([2, 7, 11, 15], 9),
    (list(range(10_000)), 19_997),   # worst case: answer is near end
]

for nums, target in test_cases:
    for fn, label in [(two_sum_brute, 'brute'), (two_sum_optimized, 'optimized')]:
        if label == 'brute' and len(nums) > 1000:
            print(f"  {label} (n={len(nums)}): skipped — too slow")
            continue
        start = time.perf_counter()
        result = fn(nums[:], target)
        ms = (time.perf_counter() - start) * 1000
        print(f"  {label} (n={len(nums)}): {ms:.3f}ms → {result}")
```

**Checkpoint:** The optimized solution handles n=10,000 in under 5ms. The brute force should be noticeably slower even for n=1,000.

---

## Deliverables

Submit to Canvas:

1. `lab01_benchmark.py` — with analysis comments filled in (Section 1.6)
2. `lab01_analysis.py` — with complexity annotations for all 8 functions
3. `lab01_leetcode.py` — with both Two Sum implementations, complexity annotations, and timing output
4. A screenshot or terminal paste showing your benchmark output from Part 1

---

## Summary

| Concept | Key Point |
|---|---|
| Big-O | Upper bound on growth rate; drop constants and lower-order terms |
| O(1) | Constant — array access, hash lookup |
| O(log n) | Halving — binary search |
| O(n) | Linear — single loop |
| O(n log n) | Log-linear — efficient sort |
| O(n²) | Quadratic — nested loops |
| O(2ⁿ) | Exponential — naive recursion without memoization |
| Space complexity | Count extra memory only; recursion depth counts |
| Amortized O(1) | `list.append()` — occasional resize amortized over n ops |
| Time-space tradeoff | Hash map buys O(n) → O(n) time at cost of O(n) space |
