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

---

### Question 11

**Each question is worth 5 points.**

In backtracking, what is the purpose of sorting the input before running the algorithm when the problem requires avoiding duplicate results?

- A) Sorting allows binary search to be used inside the backtracking loop, reducing time complexity
- B) Sorting groups identical elements together so duplicate branches can be detected and skipped with a simple index comparison
- C) Sorting guarantees the base case is reached faster by ordering elements from smallest to largest
- D) Sorting is required to ensure the `used` set works correctly

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Binary search is not used inside backtracking — the algorithm iterates through choices sequentially. Sorting does not enable binary search within the backtracking loop.
- *Why B is correct:* When elements are sorted, duplicates are adjacent. The condition `if i > start and candidates[i] == candidates[i-1]: continue` detects when the same value would be chosen at the same recursion level as the previous iteration. Without sorting, duplicates may not be adjacent, and this simple index comparison would not work correctly.
- *Why C is incorrect:* The base case condition (target reached, or length limit met) is not affected by element order. Sorting does not change when the base case is triggered.
- *Why D is incorrect:* The `used` set tracks which indices are in the current path — sorting does not affect its correctness. Duplicate elimination requires a different mechanism (the skip condition), not the `used` set.

---

### Question 12

What does the following recursive function compute?

```python
def mystery(n):
    if n <= 1:
        return 1
    return n * mystery(n - 1)
```

- A) The nth Fibonacci number
- B) The sum of integers from 1 to n
- C) n factorial (n!)
- D) The nth power of 2 (2ⁿ)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Fibonacci is computed as `mystery(n-1) + mystery(n-2)` with base cases `mystery(0)=0, mystery(1)=1`. This function multiplies, not adds, and has only one recursive call.
- *Why B is incorrect:* Sum 1..n would use `mystery(n-1) + n` (addition, not multiplication). The sum of 1+2+3+4 = 10; the factorial of 4 = 24 — different values.
- *Why C is correct:* This is the textbook recursive factorial implementation. `mystery(5) = 5 × mystery(4) = 5 × 4 × mystery(3) = 5 × 4 × 3 × 2 × 1 × 1 = 120 = 5!`. Base case: `mystery(1) = 1` (1! = 1).
- *Why D is incorrect:* Powers of 2 would use `2 * mystery(n-1)` with base case `mystery(0)=1` (2⁰=1). Multiplying by `n` (a variable) produces factorial growth, not exponential base-2 growth.

---

### Question 13

A backtracking algorithm for the combination sum problem adds a pruning condition `if target < 0: return` before recursing. How does this affect performance?

- A) It has no effect — the base case `target == 0` would eventually be reached anyway
- B) It eliminates entire subtrees where the remaining target has already gone negative, reducing unnecessary recursive calls
- C) It converts the algorithm from exponential to polynomial time
- D) It ensures the algorithm only explores sorted branches, preventing duplicate combinations

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Without the pruning, the algorithm would continue recursing even after the running sum has exceeded the target, exploring many branches that cannot produce valid results. The `target < 0` check terminates these branches immediately instead of at a deeper level.
- *Why B is correct:* When `target` goes negative, no additional elements (which are all positive) can bring it back to zero. Continuing would only waste work. Returning immediately prunes the entire subtree rooted at this call. This is the classic branch-and-bound pruning that separates practical backtracking implementations from their worst-case theoretical performance.
- *Why C is incorrect:* Pruning reduces the constant factor and average-case performance, but the worst-case remains exponential (the problem of enumerating all valid combinations is inherently exponential in the output size). Pruning does not change the asymptotic class.
- *Why D is incorrect:* Pruning on a negative target is about eliminating over-budget branches — it has nothing to do with sorted order or duplicate prevention. Duplicate prevention requires a separate skip condition.

---

### Question 14

What is the output of the following code?

```python
def count_paths(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return count_paths(n - 1) + count_paths(n - 2)

print(count_paths(6))
```

- A) `8`
- B) `13`
- C) `5`
- D) `21`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `count_paths` computes the nth Fibonacci-like sequence with `f(1)=1, f(2)=f(1)+f(0)=1+0=1, f(3)=1+1=2, f(4)=2+1=3, f(5)=3+2=5, f(6)=5+3=8`. Note: `f(0)=0`. The result for n=6 is 8.
- *Why B is incorrect:* 13 is `count_paths(7)`. For n=7: `f(7) = f(6) + f(5) = 8 + 5 = 13`. The question asks for n=6.
- *Why C is incorrect:* 5 is `count_paths(5)`. `f(5) = f(4) + f(3) = 3 + 2 = 5`. The question asks for n=6.
- *Why D is incorrect:* 21 is `count_paths(8)`. `f(8) = f(7) + f(6) = 13 + 8 = 21`. The question asks for n=6.

---

### Question 15

In a recursion tree for `fib(5)`, how many times is `fib(2)` called?

- A) 1
- B) 2
- C) 3
- D) 5

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* If `fib(2)` were called only once, memoization would have minimal impact. The problem with naive Fibonacci is that `fib(2)` and smaller values are called many times.
- *Why B is incorrect:* Tracing the recursion tree: `fib(5)` calls `fib(4)` and `fib(3)`. `fib(4)` calls `fib(3)` and `fib(2)`. `fib(3)` (from `fib(5)`) calls `fib(2)` and `fib(1)`. `fib(3)` (from `fib(4)`) calls `fib(2)` and `fib(1)`. Count of `fib(2)` calls: one from `fib(4)`, one from `fib(3)` under `fib(5)`, one from `fib(3)` under `fib(4)` = 3 total.
- *Why C is correct:* Drawing the full recursion tree for `fib(5)`, `fib(2)` is called 3 times. This illustrates why memoization helps — each redundant call to `fib(2)` can be avoided after the first computation.
- *Why D is incorrect:* 5 is the total number of unique Fibonacci values computed for `fib(5)` (fib(0) through fib(4)), not the count of `fib(2)` calls specifically.

---

### Question 16

Which of the following correctly describes tail recursion?

- A) A recursive function that calls itself with a larger input each time
- B) A recursive function where the recursive call is the very last operation before returning, with no pending computation after it
- C) A recursive function that uses two base cases instead of one
- D) A recursive function that makes two recursive calls per invocation

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Recursive calls with larger inputs do not converge toward a base case and would cause infinite recursion. Tail recursion describes a structural property of where the recursive call appears, not the size of the input.
- *Why B is correct:* Tail recursion means the function's last action is the recursive call — the return value of the recursive call is immediately returned without any further computation. Example: `return factorial_tail(n-1, acc * n)` is tail-recursive; `return n * factorial(n-1)` is not (the multiplication happens after the call returns). Some languages and compilers can optimize tail recursion into a loop, eliminating stack frame overhead.
- *Why C is incorrect:* The number of base cases is a correctness concern, not the definition of tail recursion. A function with two base cases and a non-tail recursive call is not tail-recursive.
- *Why D is incorrect:* Making two recursive calls per invocation (like Fibonacci) is generally the opposite of efficient tail recursion — it produces binary recursion trees with exponential call counts.

---

### Question 17

What is the total number of recursive calls made by `subsets([1, 2, 3])`  in the standard backtracking implementation (include the initial call)?

- A) 8
- B) 15
- C) 16
- D) 7

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* 8 is the number of subsets (2³), not the number of recursive calls. Each call to `backtrack` records one subset, but the function is called more times than the number of results.
- *Why B is correct:* The recursion tree for `subsets([1,2,3])` makes one call per node in a binary decision tree of depth 3. The total nodes in a complete binary tree of depth n is 2^(n+1) − 1. For n=3: 2⁴ − 1 = 15. At each level, each node spawns calls for each remaining element. The total is 1 + 3 + (3×2) + (3×2×1) ... accounting for the path structure = 15 nodes (1 root + 3 at depth 1 + 6 at depth 2 + 5 calls at leaves... the exact count via the recursion structure is 15).
- *Why C is incorrect:* 16 = 2⁴ would be the count for a balanced binary tree of depth 4. The subsets tree for 3 elements has depth 3 and does not form a complete binary tree.
- *Why D is incorrect:* 7 = 2³ − 1 is the number of internal nodes (non-leaf) in a complete binary tree of depth 3. The total call count includes both internal nodes and leaf nodes.

---

### Question 18

In the N-Queens backtracking solution, which three sets are maintained to check if a position `(row, col)` is under attack?

- A) `rows`, `cols`, `diagonals`
- B) `cols`, `pos_diag` (row + col), `neg_diag` (row − col)
- C) `rows`, `pos_diag`, `corners`
- D) `queens`, `attacked`, `safe`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The N-Queens algorithm places exactly one queen per row (iterating row by row), so no two queens share a row by construction. A `rows` set is unnecessary — the row is already guaranteed unique.
- *Why B is correct:* Since one queen is placed per row, only columns and diagonals need checking. A queen at `(r, c)` attacks: all cells in column `c` (tracked by `cols`), all cells on the diagonal going down-right where `row + col` is constant (tracked by `pos_diag`), and all cells on the diagonal going down-left where `row - col` is constant (tracked by `neg_diag`). These three sets fully cover all attack directions in O(1) per check.
- *Why C is incorrect:* There is no concept of "corners" in the N-Queens attack check. The two diagonal directions are fully described by `row+col` and `row-col`.
- *Why D is incorrect:* These are vague placeholder names. The specific mathematical properties `row+col` and `row-col` are what make diagonal detection work in O(1) — abstract labels like `attacked` and `safe` do not describe the underlying mechanism.

---

### Question 19

A recursive function is called with `n = 1000`. Python's default recursion limit is 1000. What happens?

- A) The function runs successfully — the limit is checked after execution
- B) Python automatically increases the recursion limit when needed
- C) The function likely raises `RecursionError` because the call chain reaches or exceeds the system limit
- D) The function silently truncates at depth 1000 and returns `None`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Python checks the recursion depth at each call, not after execution. If depth reaches the limit before the base case is reached, `RecursionError` is raised immediately.
- *Why B is incorrect:* Python does not automatically increase the recursion limit. The limit exists to prevent stack overflow from consuming all available memory. It can be manually increased with `sys.setrecursionlimit(n)`, but Python never does this automatically.
- *Why C is correct:* Python's default recursion limit is 1000 (sys.getrecursionlimit() = 1000). With n = 1000, the call chain is `f(1000) → f(999) → ... → f(0)` — approximately 1001 frames. This meets or exceeds the limit. Python raises `RecursionError: maximum recursion depth exceeded`. The exact behavior depends on overhead frames, but n=1000 is dangerously close to the limit.
- *Why D is incorrect:* Python does not silently truncate recursion. Reaching the limit raises an explicit exception that propagates up the call stack unless caught.

---

### Question 20

What is the time complexity of generating all permutations of a list of n distinct elements using backtracking?

- A) O(n²)
- B) O(n · 2ⁿ)
- C) O(n · n!)
- D) O(2ⁿ)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(n²) would be appropriate for an algorithm with two nested loops each of size n. Generating all permutations requires producing n! outputs — exponentially more than n² for large n.
- *Why B is incorrect:* O(n · 2ⁿ) is the complexity of generating all subsets. Subsets have 2ⁿ outputs of up to length n. Permutations have n! outputs of exactly length n. For n ≥ 3, n! > 2ⁿ.
- *Why C is correct:* There are exactly n! distinct permutations of n elements. Each permutation has length n, and recording it (copying the current list) costs O(n). Total time: O(n · n!). The backtracking tree work (pushes and pops) is also O(n · n!) — each of the n! leaf nodes required O(n) work to reach.
- *Why D is incorrect:* O(2ⁿ) counts the number of subsets, not permutations. n! grows far faster than 2ⁿ for large n: 10! = 3,628,800 vs 2¹⁰ = 1,024.
