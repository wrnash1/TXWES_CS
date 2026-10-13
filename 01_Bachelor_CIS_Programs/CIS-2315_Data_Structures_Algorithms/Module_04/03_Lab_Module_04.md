# Lab Activity: Module 04 — Recursion & Backtracking

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Recursive foundations: factorial, binary search, Fibonacci with and without memoization
- **Part 2** — Backtracking template: Subsets and Permutations
- **Part 3** — Backtracking with constraints: Generate Parentheses on LeetCode

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Recursive Foundations

**File:** `lab04_recursion.py`

### 1.1 — Factorial

```python
def factorial(n):
    """
    Compute n! recursively.
    Base case: 0! = 1.
    Time: O(n), Space: O(n) call stack.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Test:

```python
print(factorial(0))   # 1
print(factorial(1))   # 1
print(factorial(5))   # 120
print(factorial(10))  # 3628800
```

Call stack trace — fill this in by hand before running:

```python
# factorial(4):
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 * factorial(0)
# factorial(0) = 1  ← base case
# unwind: 1 → 1 → 2 → 6 → 24
```

**Checkpoint:** All outputs match. Trace matches the unwind pattern above.

---

### 1.2 — Recursive Binary Search

```python
def binary_search(arr, target, lo=None, hi=None):
    """
    Search for target in sorted array.
    Returns index if found, -1 if not.
    Time: O(log n), Space: O(log n) call stack.
    """
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(arr) - 1

    if lo > hi:          # base case: search space empty
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)
    else:
        return binary_search(arr, target, lo, mid - 1)
```

Test:

```python
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))    # 3
print(binary_search(arr, 1))    # 0
print(binary_search(arr, 13))   # 6
print(binary_search(arr, 6))    # -1  (not in list)
```

**Checkpoint:** All four tests return the expected index or -1.

---

### 1.3 — Fibonacci: Naive vs Memoized

```python
import time

def fib_naive(n):
    """
    Naive recursive Fibonacci — O(2^n) time.
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    """
    Memoized Fibonacci — O(n) time, O(n) space.
    """
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


from functools import lru_cache

@lru_cache(maxsize=None)
def fib_lru(n):
    """
    LRU-cached Fibonacci — O(n) time, O(n) space.
    """
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)
```

Benchmark:

```python
# Correctness check
for i in range(10):
    assert fib_naive(i) == fib_memo(i) == fib_lru(i), f'Mismatch at n={i}'
print('Correctness: all three agree for n=0..9')

# Performance comparison
n = 35
t0 = time.perf_counter()
fib_naive(n)
t1 = time.perf_counter()
fib_memo(n)
t2 = time.perf_counter()
fib_lru(n)
t3 = time.perf_counter()

print(f'fib_naive({n}): {t1-t0:.4f}s')
print(f'fib_memo({n}):  {t2-t1:.6f}s')
print(f'fib_lru({n}):   {t3-t2:.6f}s')
```

**Checkpoint:** `fib_naive(35)` is noticeably slower than `fib_memo(35)` and `fib_lru(35)`. All three return the same value. Comment: what is the value of `fib(35)`?

---

## Part 2 — Backtracking Template

**File:** `lab04_backtracking.py`

### 2.1 — Subsets (LeetCode #78)

```python
def subsets(nums):
    """
    Return all subsets of nums (power set).
    Time: O(n * 2^n), Space: O(n) call stack.
    """
    result = []

    def backtrack(start, current):
        result.append(list(current))      # record current subset
        for i in range(start, len(nums)):
            current.append(nums[i])        # choose
            backtrack(i + 1, current)      # recurse
            current.pop()                  # unchoose

    backtrack(0, [])
    return result
```

Test:

```python
print(subsets([1, 2, 3]))
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
# 2^3 = 8 subsets

print(len(subsets([1, 2, 3, 4])))
# 2^4 = 16 subsets
```

Trace the first three recursive calls manually:

```python
# Call 1: backtrack(0, [])   → record []
#   i=0: append 1 → current=[1]
#   Call 2: backtrack(1, [1]) → record [1]
#     i=1: append 2 → current=[1,2]
#     Call 3: backtrack(2, [1,2]) → record [1,2]
#       i=2: append 3 → current=[1,2,3]
#       Call 4: backtrack(3, [1,2,3]) → record [1,2,3]; range(3,3) empty → return
#       pop → current=[1,2]
#     return from Call 3
#     pop → current=[1]
#   ...
```

**Checkpoint:** Output matches expected. Submit to LeetCode #78.

---

### 2.2 — Permutations (LeetCode #46)

```python
def permute(nums):
    """
    Return all permutations of nums.
    Time: O(n * n!), Space: O(n) call stack.
    """
    result = []

    def backtrack(current, used):
        if len(current) == len(nums):
            result.append(list(current))
            return
        for i, num in enumerate(nums):
            if i in used:
                continue
            current.append(num)        # choose
            used.add(i)
            backtrack(current, used)   # recurse
            current.pop()              # unchoose
            used.remove(i)

    backtrack([], set())
    return result
```

Test:

```python
print(permute([1, 2, 3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 3! = 6 permutations

print(len(permute([1, 2, 3, 4])))
# 4! = 24 permutations
```

Key question — answer in a comment:

```python
# Q: Why does the algorithm need both `used.add(i)` before the recursive call
#    AND `used.remove(i)` after it?
#
# A: Before recursion, add i to mark this index as 'in use' so deeper calls
#    don't choose the same element again. After recursion, remove i to restore
#    the `used` set to the state it was in before this loop iteration, so the
#    next iteration can correctly consider all other indices.
#    This is the choose → recurse → unchoose pattern.
```

**Checkpoint:** Correct count of permutations for n=3 and n=4. Submit to LeetCode #46.

---

## Part 3 — Backtracking with Constraints

**File:** `lab04_advanced.py`

### 3.1 — Generate Parentheses (LeetCode #22)

```python
def generate_parentheses(n):
    """
    Generate all valid combinations of n pairs of parentheses.
    Constraint pruning: only add '(' if open_count < n;
                        only add ')' if close_count < open_count.
    """
    result = []

    def backtrack(s, open_count, close_count):
        if len(s) == 2 * n:
            result.append(s)
            return
        if open_count < n:
            backtrack(s + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(s + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result
```

Test:

```python
print(generate_parentheses(1))
# ['()']

print(generate_parentheses(2))
# ['(())', '()()']

print(generate_parentheses(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']

print(len(generate_parentheses(4)))
# 14 — the 4th Catalan number
```

Explain the constraint in a comment:

```python
# Q: Why does `close_count < open_count` ensure all outputs are valid?
#
# A: A ')' can only be added if there is a matching unmatched '(' already open.
#    `close_count < open_count` enforces this: it means at least one '(' has
#    been opened that has not yet been closed. This prevents ')' from ever
#    appearing before its matching '(', which is the only way parentheses
#    can be invalid. Combined with `open_count < n`, this prunes all invalid
#    paths without needing any post-generation validity check.
```

**Checkpoint:** Correct counts for n=1,2,3,4. Submit to LeetCode #22.

---

### 3.2 — Integration Test

```python
if __name__ == '__main__':
    # Factorial
    assert factorial(5) == 120
    assert factorial(0) == 1

    # Binary search
    arr = sorted([4, 2, 7, 1, 9, 5])
    assert binary_search(arr, 7) == arr.index(7)

    # Fibonacci
    assert fib_memo(10) == 55
    assert fib_lru(10) == 55

    # Subsets
    assert len(subsets([1, 2, 3])) == 8
    assert [] in subsets([1, 2, 3])

    # Permutations
    assert len(permute([1, 2, 3])) == 6

    # Generate parentheses
    assert generate_parentheses(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']

    print('All assertions passed.')
```

**Checkpoint:** Script runs without assertion errors. All four LeetCode problems submitted.

---

## Deliverables

Submit to Canvas:

1. `lab04_recursion.py` — factorial, binary search, Fibonacci benchmark with timing output
2. `lab04_backtracking.py` — subsets and permutations with trace comments
3. `lab04_advanced.py` — generate parentheses with constraint explanation comment
4. LeetCode submission screenshots for #78, #46, and #22

---

## Summary

| Concept | Key Point |
|---|---|
| Base case | Required — terminates recursion; write it first |
| Progress | Each call must move toward base case |
| Call stack depth | = recursion depth; O(n) for linear recursion |
| Memoization | Cache subproblem results; converts O(2ⁿ) to O(n) for Fibonacci |
| `@lru_cache` | Python decorator; one line of memoization |
| Backtracking template | choose → recurse → unchoose |
| Unchoose step | `current.pop()` after recursion — restores state for next iteration |
| Subsets | 2ⁿ results; record current at every recursive call |
| Permutations | n! results; use `used` set to prevent reuse |
| Constraint pruning | Add validity check before recurse; prunes invalid branches early |

---

## Part 9 — Challenge Exercise

These steps are **optional** and ungraded. They are designed for students who want to deepen their understanding beyond the core lab.

### 9.1 — N-Queens (LeetCode #51)

Solve the N-Queens problem: place n queens on an n×n chessboard so no two queens share the same row, column, or diagonal. Use backtracking: iterate over columns in each row; before placing a queen, check that no previously placed queen attacks the candidate position using three sets (`cols`, `pos_diag` = row+col, `neg_diag` = row−col). When a complete board is formed, format it as a list of strings and append to results. Return all valid configurations. Implement the solution, verify it returns 2 solutions for n=4 and 92 solutions for n=8, and add a comment explaining why the three sets (`cols`, `pos_diag`, `neg_diag`) suffice to check all attack directions.

### 9.2 — Combination Sum with Duplicate Elimination

LeetCode #40 (Combination Sum II) gives an array with possible duplicates and asks for all unique combinations that sum to a target, where each number may be used at most once. The key insight is sorting the input and skipping duplicate elements at the same recursion level (`if i > start and candidates[i] == candidates[i-1]: continue`). Implement the solution, trace it on `candidates = [2, 5, 2, 1, 2], target = 5`, and write a detailed comment explaining why the skip condition `i > start` (rather than `i > 0`) is critical — specifically, why it allows the same value to appear at different levels of the recursion tree but not twice at the same level.

### 9.3 — Memoization vs Tabulation Performance Comparison

Implement three versions of the `coin_change` problem (LeetCode #322 — find minimum coins to make an amount): (1) naive recursive with no memoization, (2) top-down recursive with `@lru_cache`, and (3) bottom-up iterative tabulation with a `dp` array. Benchmark all three on `coins = [1, 5, 10, 25]` for amounts 50, 100, 200, and 500. Record runtimes. Confirm that the naive version becomes infeasibly slow, and that the memoized and tabulation versions are both O(amount × len(coins)) but differ in constant factors and stack depth. Document your findings as comments.
