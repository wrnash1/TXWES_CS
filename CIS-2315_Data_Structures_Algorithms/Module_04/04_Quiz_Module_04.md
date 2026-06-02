# Quiz: Module 04 — Recursion & Backtracking

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the minimum requirement for a recursive function to terminate?

- A) The function must include a `return` statement in every branch
- B) The function must have at least one base case that does not make a recursive call
- C) The function must be called with a positive integer argument
- D) The function must use a loop to count down before the recursive call

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Missing `return` in a branch causes a Python `None` return, which is a logic bug — but it does not prevent termination. A function with no base case will recurse forever regardless of whether every branch has `return`.
- *Why B is correct:* A base case is the condition under which the function returns immediately without making another recursive call. Without at least one base case, the function recurses infinitely until Python raises `RecursionError: maximum recursion depth exceeded`.
- *Why C is incorrect:* Recursive functions operate on many types: strings (getting shorter), lists (getting smaller), trees (going deeper). There is no requirement for a positive integer argument — only that progress is made toward the base case with each call.
- *Why D is incorrect:* A countdown loop is not a requirement of recursion. The recursive function itself provides the counting mechanism through the argument passed to each recursive call. Adding a redundant loop would change the algorithm.

---

### Question 2

What is the time complexity of the naive recursive Fibonacci function `fib(n) = fib(n-1) + fib(n-2)`?

- A) O(n)
- B) O(n log n)
- C) O(2ⁿ)
- D) O(n²)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(n) would mean each value from 1 to n is computed exactly once. In naive Fibonacci, `fib(n-2)` recomputes every value that `fib(n-1)` computed — the overlap is exponential.
- *Why B is incorrect:* O(n log n) is the complexity of efficient sorting algorithms. There is no halving or logarithmic reduction in naive Fibonacci — both `fib(n-1)` and `fib(n-2)` are nearly the same size.
- *Why C is correct:* The call tree of naive Fibonacci is a binary tree of depth n. At each level the number of nodes approximately doubles: 1, 2, 4, 8, ..., 2ⁿ. Total nodes ≈ 2ⁿ, each doing O(1) work. Time: O(2ⁿ). This is why `fib(50)` takes over a trillion operations without memoization.
- *Why D is incorrect:* O(n²) would require a nested structure — a loop inside a loop, both running n times. The recursion branches into two calls, not n calls, producing exponential rather than quadratic growth.

---

### Question 3

A developer adds `@lru_cache(maxsize=None)` to the naive Fibonacci function. What does this change?

- A) It changes the algorithm from recursive to iterative, eliminating the call stack
- B) It adds automatic memoization so each unique input is computed at most once, reducing time from O(2ⁿ) to O(n)
- C) It limits the function to inputs of size at most 128 by default
- D) It parallelizes the two recursive calls, halving the wall-clock time

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `@lru_cache` does not change the structure of the function. It is still recursive — frames are still pushed to the call stack. The decorator wraps the function to cache return values, but the recursion itself is unchanged.
- *Why B is correct:* `lru_cache` stores the return value for each unique argument. When `fib(n-2)` is called for the second time, the cached value is returned immediately in O(1) instead of recomputing the entire subtree. Each value from 0 to n is computed exactly once. Total work: O(n).
- *Why C is incorrect:* `maxsize=None` means unlimited cache size. `maxsize=128` (the default when `@lru_cache` is used without arguments) means only the 128 most recent unique inputs are cached, but `maxsize=None` disables this limit entirely.
- *Why D is incorrect:* `lru_cache` is a synchronous caching decorator. It does not parallelize recursive calls, create threads, or use async execution. Both recursive calls still execute sequentially.

---

### Question 4

In the backtracking template below, what would happen if the `current.pop()` line were removed?

```python
for choice in choices:
    current.append(choice)    # choose
    backtrack(current)        # recurse
    current.pop()             # unchoose  ← removed
```

- A) The algorithm would run faster because fewer operations are performed
- B) The base case would never be reached, causing infinite recursion
- C) The `current` list would accumulate all choices across all branches, producing incorrect results
- D) Python would raise an `IndexError` when the next loop iteration begins

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Removing `pop()` does not reduce work — it increases it. Every recursive branch appends to the same growing list, and the accumulated incorrect state is recorded instead of the intended subset or permutation.
- *Why B is incorrect:* The base case is still reached — the recursion terminates when `start >= len(nums)` or `len(current) == len(nums)`. The problem is that the values recorded at the base case are wrong, not that the base case is skipped.
- *Why C is correct:* Without `pop()`, `current` is never restored to its pre-choice state. After the first recursive subtree completes, `current` contains all the choices made in that subtree. The next loop iteration appends another choice on top, so `current` grows unbounded and every recorded result contains all previously chosen values.
- *Why D is incorrect:* `append()` never raises `IndexError` — Python lists grow dynamically. `pop()` would raise `IndexError` on an empty list, but `append()` on any list is always safe. The bug is logical corruption, not an exception.

---

### Question 5

How many subsets does `subsets([1, 2, 3, 4])` return?

- A) 4
- B) 8
- C) 12
- D) 16

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* 4 is the number of elements in the input. The number of subsets is not equal to the input length — it is 2 raised to the input length.
- *Why B is incorrect:* 8 = 2³ is the number of subsets for a 3-element input. For `[1, 2, 3]`, the answer is 8. For `[1, 2, 3, 4]`, the answer is 2⁴ = 16.
- *Why C is incorrect:* 12 has no relationship to the subset count formula. The subset count is always a power of 2 because each element is either included or excluded — two independent choices per element.
- *Why D is correct:* For a set of n elements, the power set contains 2ⁿ subsets (including the empty set). For n=4: 2⁴ = 16. Each element is independently included or excluded, producing 2×2×2×2 = 16 combinations.

---

### Question 6

What is the space complexity of `factorial(n)` counting only the call stack?

- A) O(1) — only one frame exists at any time
- B) O(log n) — the recursion depth is logarithmic
- C) O(n) — one stack frame is pushed per recursive call, to a depth of n
- D) O(n²) — each frame stores the entire computation history

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Python does not reuse stack frames for recursion — each call creates a new frame. When `factorial(0)` is executing, frames for `factorial(n)` through `factorial(0)` are all simultaneously live on the call stack.
- *Why B is incorrect:* O(log n) call stack depth occurs when each recursive call eliminates half the input — like recursive binary search. Factorial makes one call per decrement: `n, n-1, ..., 0`. That is n+1 frames — O(n).
- *Why C is correct:* `factorial(n)` calls `factorial(n-1)` which calls `factorial(n-2)` … down to `factorial(0)`. At maximum depth, there are n+1 simultaneous live frames. Each frame stores only the local variable `n` — O(1) per frame. Total space: O(n).
- *Why D is incorrect:* Each stack frame stores only the local variable `n` and the return address — O(1) per frame. Frames do not accumulate history. The total space is O(1) × O(n) frames = O(n).

---

### Question 7

The Generate Parentheses algorithm uses the constraint `if close_count < open_count` before adding `)`. What does this guarantee?

- A) That the total length of the string never exceeds 2n
- B) That the string always begins with `(`
- C) That every `)` in the result has a matching `(` that was opened before it
- D) That equal numbers of `(` and `)` are added in every recursive call

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The length is controlled by the separate base case `if len(s) == 2 * n`. The `close_count < open_count` constraint controls correctness of nesting, not length.
- *Why B is incorrect:* The string always begins with `(` because the first call only allows `(` (since `close_count == open_count == 0` makes the `)` branch inactive). But this is a consequence, not the primary property being enforced.
- *Why C is correct:* `close_count < open_count` means there is at least one unmatched open parenthesis. Adding `)` closes that unmatched `(`. This is precisely the condition that makes every `)` valid — it can never appear without a corresponding earlier `(`.
- *Why D is incorrect:* The algorithm does not add both types in pairs. Each recursive call adds exactly one character — either `(` or `)`. The constraint determines which type is legal at each position.

---

### Question 8

Which statement correctly describes the difference between `subsets` and `permutations` backtracking algorithms?

- A) Both use the same backtracking template, but subsets records at every call while permutations records only at the base case
- B) Subsets uses iteration; permutations uses recursion
- C) Subsets is O(n²) and permutations is O(n log n)
- D) Permutations require a sorted input; subsets work on any list

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Both algorithms use the choose → recurse → unchoose template. The difference is when results are recorded. Subsets appends `list(current)` at the start of every call — because every prefix is a valid subset. Permutations appends only at the base case (`len(current) == len(nums)`) because only complete arrangements are valid permutations.
- *Why B is incorrect:* Both use recursion (backtracking). Neither is purely iterative.
- *Why C is incorrect:* Subsets is O(n · 2ⁿ) and permutations is O(n · n!). Both are exponential — unavoidable when enumerating all solutions.
- *Why D is incorrect:* Neither algorithm requires sorted input for correctness. Sorted input changes the order of output but not the completeness or correctness of the results.

---

### Question 9

What does the `used` set track in the Permutations backtracking algorithm, and why is `used.remove(i)` required after the recursive call?

- A) It tracks indices already written to `result`; `remove` clears it between result recordings
- B) It tracks which indices are currently in `current`; `remove` undoes the choice so the next loop iteration can try different combinations
- C) It tracks which values have appeared in any permutation so far to avoid global duplicates
- D) It tracks the recursion depth; `remove` decrements the counter after each level

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `used` tracks live elements in the current partial permutation, not indices written to the final result. Adding to `result` happens inside the base case and is separate from the `used` set management.
- *Why B is correct:* At any point during recursion, `used` contains exactly the indices of elements currently in `current`. This prevents the same element from appearing twice in one permutation. After the recursive call returns, `used.remove(i)` undoes the choice — restoring `used` so the next loop iteration can try a different element from the same starting state.
- *Why C is incorrect:* `used` does not track values across all permutations — that would prevent generating permutations that reuse elements across different result entries. Each permutation uses every element exactly once, but different permutations share elements freely.
- *Why D is incorrect:* Recursion depth is tracked implicitly by the call stack. The `used` set contains index values, not a counter.

---

### Question 10

What is the key insight that allows memoization to reduce Fibonacci from O(2ⁿ) to O(n)?

- A) Fibonacci numbers grow exponentially, so memoization stores only the last two values
- B) The recursive Fibonacci function has overlapping subproblems — `fib(k)` is recomputed many times, and caching eliminates redundant work
- C) Memoization converts the recursive algorithm to an iterative bottom-up loop
- D) Memoization reduces the recursion depth from n to log n by skipping already-computed steps

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Storing only the last two values is the space optimization for iterative Fibonacci — it reduces space from O(n) to O(1). Memoization in the recursive version stores all computed values, not just the last two.
- *Why B is correct:* The naive recursive call tree for `fib(n)` recomputes `fib(k)` exponentially many times for each k < n. Memoization stores the return value of each unique call after the first computation. Every subsequent call for the same argument returns the cached result in O(1). Each value from 0 to n is computed exactly once — total O(n) work.
- *Why C is incorrect:* Memoization does not convert the recursion to iteration. The function is still recursive with stack frames. Bottom-up dynamic programming does convert to iteration, but that is a separate technique covered in Module 14.
- *Why D is incorrect:* The recursion depth in memoized Fibonacci is still O(n) — the first call chain `fib(n) → fib(n-1) → ... → fib(0)` runs to full depth n. Subsequent calls are short-circuited by the cache, but the maximum stack depth at any one moment is still O(n).
