# Reading Guide: Module 04 — Recursion & Backtracking

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2315 &BULL; DATA STRUCTURES & ALGORITHM ANALYSIS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **NeetCode — Backtracking Problems Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg](https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg)
   Free video solutions for the most common backtracking interview problems including Subsets, Permutations, Combinations, and N-Queens. Each video draws the decision tree before writing code, matching the learning strategy in this module.

2. **OpenDSA — Recursion Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/RecursionIntro.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/RecursionIntro.html)
   Free interactive textbook chapter with visualizations of the call stack during recursive execution, embedded practice problems, and complexity analysis of factorial and Fibonacci.

3. **Python `functools.lru_cache` Documentation** — [https://docs.python.org/3/library/functools.html#functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)
   Official Python documentation for `@lru_cache` and `@cache` (Python 3.9+). Explains the `maxsize` parameter, thread safety, and how to inspect cache statistics with `.cache_info()`.

4. **VisuAlgo — Recursion Tree Visualizer** — [https://visualgo.net/en/recursion](https://visualgo.net/en/recursion)
   Animates the recursive call tree for Fibonacci and other classic recursive algorithms, showing how the call stack grows and unwinds. Excellent for visualizing why naive Fibonacci is O(2ⁿ).

5. **Algorithms Illuminated Part 1 (Tim Roughgarden — Free Lecture Videos)** — [https://www.algorithmsilluminated.org/](https://www.algorithmsilluminated.org/)
   Free lecture videos by Stanford professor Tim Roughgarden covering recursion, divide-and-conquer, and the Master Theorem. The mathematical treatment of recurrences complements this module's practical focus.

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
