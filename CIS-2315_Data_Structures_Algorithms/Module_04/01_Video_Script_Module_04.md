# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 04 — Recursion & Backtracking

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Recursion is the hardest mental leap in the first half of this course. Spend time on the call stack diagram — draw it vertically with each frame labeled. Students who can draw the call stack for `factorial(4)` have understood recursion.
> - The three-question framework (base case? progress toward base case? trust the return value?) is the practical anchor. Return to it for every recursive function written.
> - Backtracking is the most interview-dense topic in the module. The template — choose, recurse, unchoose — applies directly to Subsets, Permutations, and Generate Parentheses. Make the template explicit before showing any code.
> - Memoization: show the naive Fibonacci call tree first (draw it), then show how memoization collapses it. The visual is essential.
> - Common mistakes: missing base case (infinite recursion), not returning the recursive result, mutating shared state without undoing it in backtracking.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 04 | Recursion & Backtracking | CIS-2315"]**

"Modules 01 through 03 gave you the foundational data structures. This module introduces recursion — the technique that powers most tree traversal, divide-and-conquer, and backtracking algorithms you will encounter in interviews. Recursion is hard at first because it requires trusting a function you are still writing. Once that trust clicks, it becomes one of the most powerful tools in your kit.

By the end of this module, you will be able to write recursive functions correctly, analyze their complexity, apply memoization to remove redundant work, and implement the backtracking template to solve combinatorial problems like Subsets, Permutations, and Generate Parentheses."

---

## [01:30 – 06:30] Part 1 — Recursion Fundamentals

**[SHOW SLIDE: "What Is Recursion?"]**

"A recursive function is a function that calls itself. That sounds circular — and it is — unless two conditions hold:

1. There is a **base case** that terminates the recursion.
2. Every recursive call makes progress toward the base case.

Without a base case, the function calls itself forever until Python raises `RecursionError: maximum recursion depth exceeded`. Without progress, you hit the same condition forever.

[PAUSE]

**[DEMO — Factorial]**

```python
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case — progress: n-1 < n, approaching 0
    return n * factorial(n - 1)
```

Let me trace the call stack for `factorial(4)`:

```text
factorial(4)
  → 4 * factorial(3)
       → 3 * factorial(2)
            → 2 * factorial(1)
                 → 1 * factorial(0)
                          → return 1
                 → return 1 * 1 = 1
            → return 2 * 1 = 2
       → return 3 * 2 = 6
  → return 4 * 6 = 24
```

**[SHOW DIAGRAM: call stack growing down, then unwinding]**

Each function call creates a new stack frame containing the local variable `n`. Python pushes a new frame when `factorial` calls itself, and pops the frame when the call returns. The stack grows 5 frames deep for `factorial(4)`.

[PAUSE]

**The three questions to ask when writing any recursive function:**

1. What is the base case — the smallest input where the answer is immediate?
2. Does each recursive call move closer to the base case?
3. Assuming the recursive call returns the correct answer for the smaller input, does my expression assemble the correct answer for the current input?

If you can answer all three, the recursion is correct."

---

## [06:30 – 10:30] Part 2 — Memoization

**[SHOW SLIDE: "Naive Fibonacci and Exponential Blowup"]**

"Fibonacci is the classic example of why naive recursion is sometimes disastrously slow.

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

**[SHOW DIAGRAM: call tree for fib(5)]**

```text
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2) ← computed AGAIN
│   │   └── fib(1)
│   └── fib(2)     ← computed AGAIN
│       ├── fib(1)
│       └── fib(0)
└── fib(3)         ← computed AGAIN
    ├── fib(2)     ← computed AGAIN
    └── fib(1)
```

`fib(3)` is called twice. `fib(2)` is called three times. For `fib(50)`, the call tree has over a trillion nodes. Time complexity: O(2ⁿ).

[PAUSE]

**Memoization** stores previously computed results in a dictionary so each subproblem is solved only once.

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

With memoization, the call tree becomes a straight chain — each value from 0 to n is computed exactly once. Time: O(n). Space: O(n) for the memo dictionary.

[PAUSE]

Python also provides `functools.lru_cache` as a decorator that handles memoization automatically:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

`@lru_cache` caches by input argument. It is O(n) time and O(n) space — identical to the manual memo approach."

---

## [10:30 – 16:00] Part 3 — Backtracking Template

**[SHOW SLIDE: "Backtracking — Explore, Then Undo"]**

"Backtracking is recursion applied to decision-making. At each step, you make a choice, recurse to explore all consequences of that choice, then undo the choice (backtrack) and try the next option. The goal is to enumerate all valid combinations, permutations, or paths in a problem.

The template is always the same three lines:

```text
choose   # add something to the current state
recurse  # explore all consequences
unchoose # undo the choice, restore previous state
```

[PAUSE]

**[DEMO — Subsets (LeetCode #78)]**

Given a list of integers with no duplicates, return all possible subsets.

```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(list(current))   # record current subset
        for i in range(start, len(nums)):
            current.append(nums[i])    # choose
            backtrack(i + 1, current)  # recurse
            current.pop()              # unchoose

    backtrack(0, [])
    return result
```

For `nums = [1, 2, 3]`:

- Start: `current=[]`, record `[]`
- Choose 1: `current=[1]`, record `[1]`
  - Choose 2: `current=[1,2]`, record `[1,2]`
    - Choose 3: `current=[1,2,3]`, record `[1,2,3]`; pop → `[1,2]`
    - End inner loop; pop → `[1]`
  - Choose 3: `current=[1,3]`, record `[1,3]`; pop → `[1]`; pop → `[]`
- Choose 2: `current=[2]`, record `[2]`
  - ...and so on

Final result: `[[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]` — all 2³ = 8 subsets.

[PAUSE]

Notice the `current.pop()` after the recursive call. This is the 'unchoose' step — it restores `current` to the state it was in before this iteration, so the next loop iteration starts from the same clean state. Forgetting `pop()` is the most common backtracking bug."

---

## [16:00 – 20:30] Part 4 — Permutations and Generate Parentheses

**[SHOW SLIDE: "LeetCode #46 — Permutations"]**

"Permutations require choosing every element for every position, without reuse. The approach: track which elements have been used with a `used` set or by swapping.

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
            current.append(num)   # choose
            used.add(i)
            backtrack(current, used)  # recurse
            current.pop()         # unchoose
            used.remove(i)

    backtrack([], set())
    return result
```

For `[1, 2, 3]`, this generates all 3! = 6 permutations.

[PAUSE]

**[DEMO — Generate Parentheses (LeetCode #22)]**

Given `n` pairs of parentheses, generate all valid combinations.

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

The two constraints — `open_count < n` and `close_count < open_count` — enforce validity without needing to check the result. For `n=3`: `['((()))', '(()())', '(())()', '()(())', '()()()']`.

Note: this version builds a new string at each step (strings are immutable in Python), so there is no explicit `unchoose` step. The parent function's string `s` is unchanged on return."

---

## [20:30 – 24:00] Part 5 — Complexity and Closing

**[SHOW SLIDE: "Recursion and Backtracking Complexity"]**

"Analyzing the complexity of recursive and backtracking algorithms uses the tools from Module 01.

For simple recursion:

- Factorial: T(n) = T(n-1) + O(1) = O(n) time, O(n) space (call stack depth).
- Naive Fibonacci: T(n) = T(n-1) + T(n-2) ≈ O(2ⁿ) time, O(n) space.
- Memoized Fibonacci: O(n) time, O(n) space.

For backtracking:

- Subsets of n elements: 2ⁿ subsets, each recorded in O(n) — O(n · 2ⁿ) time.
- Permutations of n elements: n! permutations — O(n · n!) time.
- Generate Parentheses of n pairs: Catalan number Cₙ solutions — roughly O(4ⁿ / √n).

These exponential complexities are unavoidable when the problem requires enumerating all solutions. Backtracking is correct for these problems — pruning invalid paths (like the constraints in Generate Parentheses) reduces the constant factor but not the asymptotic class.

[PAUSE]

The Module 04 lab has you implement factorial, memoized Fibonacci, and the three backtracking problems: Subsets, Permutations, and Generate Parentheses. The quiz covers base cases, memoization, the backtracking template, and complexity analysis of recursive algorithms. Draw the call stack. Draw the decision tree. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 04 — Recursion & Backtracking]**

---

## Additional Resources

- [VisuAlgo — Recursion Visualization](https://visualgo.net/en/recursion)
- [NeetCode — Backtracking Playlist](https://www.youtube.com/watch?v=pfiQ_PS1g8E)
- [LeetCode #78 — Subsets](https://leetcode.com/problems/subsets/)
- [LeetCode #46 — Permutations](https://leetcode.com/problems/permutations/)
- [LeetCode #22 — Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [LeetCode #51 — N-Queens](https://leetcode.com/problems/n-queens/)
