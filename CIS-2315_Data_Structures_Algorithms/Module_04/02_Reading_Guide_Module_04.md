# Reading Guide: Module 04 — Recursion & Backtracking

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

Recursion is the technique of solving a problem by solving smaller instances of the same problem. Backtracking is recursion applied to decision search: you build a solution piece by piece, abandoning partial solutions as soon as a constraint is violated. Together, these two techniques solve almost every combinatorial interview problem — subsets, permutations, combinations, N-Queens, Sudoku — and form the basis of tree traversal, divide-and-conquer, and dynamic programming.

---

## 1. Recursion Fundamentals

### The Three Requirements

Every correct recursive function satisfies three properties:

1. **Base case** — an input small enough that the answer is known immediately, requiring no further recursion.
2. **Progress** — each recursive call is made on a strictly smaller input, guaranteeing termination.
3. **Correct assembly** — assuming the recursive call returns the correct answer for the smaller input, the expression around it assembles the correct answer for the current input.

If all three hold, the function is correct by induction.

### Factorial

```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case; progress: n-1 < n
```

Call stack depth: n + 1 frames. Space: O(n).

### Recursive Binary Search

```python
def binary_search(arr, target, lo, hi):
    if lo > hi:                  # base case: search space empty
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)
    else:
        return binary_search(arr, target, lo, mid - 1)
```

Time: O(log n). Space: O(log n) call stack depth.

---

## 2. Memoization

### Naive Fibonacci — O(2ⁿ)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

The call tree is a binary tree of depth n. Each node's computation is O(1) but there are O(2ⁿ) nodes. `fib(n-2)` is recomputed every time — exponential blowup.

### Memoized Fibonacci — O(n)

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

Each unique input from 0 to n is computed exactly once. Time: O(n). Space: O(n).

**Warning:** Using a mutable default argument `memo={}` persists across calls in Python. For production code, use `memo=None` and initialize inside the function, or use `@lru_cache`.

### `@lru_cache` Decorator

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

`lru_cache` memoizes automatically. `maxsize=None` means unlimited cache size. This is the idiomatic Python approach for memoization.

---

## 3. Backtracking

### The Template

Backtracking builds a solution incrementally, exploring all possibilities and abandoning partial solutions that cannot lead to a valid result.

```python
def backtrack(state, choices):
    if goal_reached(state):
        record_solution(state)
        return
    for choice in choices:
        if is_valid(state, choice):
            make_choice(state, choice)      # choose
            backtrack(state, next_choices)  # recurse
            undo_choice(state, choice)      # unchoose
```

The `undo_choice` step is critical. It restores `state` to what it was before the choice, so the next iteration of the loop starts from the same clean state.

### Subsets (LeetCode #78)

```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(list(current))
        for i in range(start, len(nums)):
            current.append(nums[i])    # choose
            backtrack(i + 1, current)  # recurse
            current.pop()              # unchoose

    backtrack(0, [])
    return result
```

Time: O(n · 2ⁿ) — 2ⁿ subsets, each copied in O(n).
Space: O(n) call stack depth + O(n · 2ⁿ) for result storage.

### Permutations (LeetCode #46)

```python
def permute(nums):
    result = []

    def backtrack(current, used):
        if len(current) == len(nums):
            result.append(list(current))
            return
        for i, num in enumerate(nums):
            if i in used:
                continue
            current.append(num)       # choose
            used.add(i)
            backtrack(current, used)  # recurse
            current.pop()             # unchoose
            used.remove(i)

    backtrack([], set())
    return result
```

Time: O(n · n!) — n! permutations, each copied in O(n).

### Generate Parentheses (LeetCode #22)

```python
def generate_parentheses(n):
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

Constraints prune invalid paths: never add `)` when it would exceed `(` count. This is constraint-based pruning — the most powerful backtracking optimization.

---

## 4. Complexity Summary

| Algorithm | Time | Space (call stack) | Notes |
|---|---|---|---|
| Factorial | O(n) | O(n) | Linear recursion |
| Naive Fibonacci | O(2ⁿ) | O(n) | Each call branches twice |
| Memoized Fibonacci | O(n) | O(n) | Each value computed once |
| Recursive binary search | O(log n) | O(log n) | Halving eliminates half at each step |
| Subsets | O(n · 2ⁿ) | O(n) | 2ⁿ choices, n depth |
| Permutations | O(n · n!) | O(n) | n! arrangements, n depth |
| Generate Parentheses | O(4ⁿ / √n) | O(n) | Catalan number of results |

---

## 5. Interview Exam Tips

1. **Always write the base case first** — recursive functions without a base case cause infinite recursion and `RecursionError`. The base case is the contract that makes the function safe to call.

2. **The unchoose step is mandatory in backtracking** — `current.pop()` after the recursive call restores state. Forgetting it means every recursive branch shares state, producing incorrect results.

3. **Use `@lru_cache` in interviews** — Python's decorator handles memoization in one line. Always mention it as an optimization when naive recursion has overlapping subproblems.

4. **Space complexity includes the call stack** — a recursion of depth n uses O(n) stack space even if no other data is stored. Mention this explicitly when asked about space complexity.

5. **Draw the decision tree, not the code** — backtracking problems are understood by drawing the tree of choices at each step. Draw it first; the code follows naturally.

6. **Constraint pruning reduces constant factors** — adding `if not is_valid(state, choice): continue` before recursing prunes branches early. This is the difference between LeetCode TLE and AC on hard backtracking problems.

7. **Subsets vs combinations vs permutations** — subsets include all partial choices including the empty set; combinations choose k items without order; permutations choose all items with order. They use the same backtracking frame with different stopping conditions.

8. **Recursive binary search has O(log n) space** — the iterative version uses O(1) space. On interviews, prefer iterative binary search unless recursion is explicitly required.

---

## 6. Study Checklist

- [ ] Watch the Module 04 video lecture by Professor Nash.
- [ ] Implement `factorial` and `binary_search` recursively.
- [ ] Implement `fib` with and without memoization; compare performance.
- [ ] Implement `@lru_cache` version of Fibonacci.
- [ ] Solve LeetCode #78 (Subsets).
- [ ] Solve LeetCode #46 (Permutations).
- [ ] Solve LeetCode #22 (Generate Parentheses).
- [ ] Attempt LeetCode #51 (N-Queens) as a stretch goal.
- [ ] Complete the Module 04 Lab.
- [ ] Complete the Module 04 Quiz.
