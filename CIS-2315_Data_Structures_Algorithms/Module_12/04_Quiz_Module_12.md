# Quiz: Module 12 – Recursion and Backtracking
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the space complexity of a recursive function with n levels of recursion and O(1) work per call frame?
*   A) O(1) — recursion uses no extra memory.
*   B) O(n) — each active call frame occupies stack space proportional to recursion depth.
*   C) O(n²) — each call frame stores all previous results.
*   D) O(log n) — the call stack shrinks as calls return.
*   **Correct Answer:** B) O(n) — each active call frame occupies stack space proportional to recursion depth.
*   **Distractor Analysis:**
    *   *Why correct:* Each recursive call pushes a new frame onto the call stack. With n levels of recursion simultaneously active, O(n) stack frames are held in memory at peak depth.
    *   A is incorrect: Recursion does use memory — the call stack grows with each nested call. A tail-recursive function optimized by the compiler might use O(1) space, but Python does not perform tail call optimization.
    *   C is incorrect: O(n²) would require each frame to store O(n) data. With O(1) data per frame, depth n gives O(n) total.
    *   D is incorrect: O(log n) stack depth applies to recursion that halves its input (like binary search or merge sort recursion), not to recursion that decrements by 1.

---

**Question 2**
Which of the following most accurately describes the **backtracking technique**?
*   A) A dynamic programming approach that stores previously computed subproblem results in a table to avoid recomputation, reducing exponential recursive time to polynomial.
*   B) A recursive strategy that builds a solution incrementally by making one choice at a time, checks if the partial solution can still lead to a valid result, and undoes the last choice (backtracks) when a constraint is violated — then tries the next alternative.
*   C) A divide-and-conquer method that splits the problem into independent halves, solves each recursively, and combines their results — discarding partial solutions that are smaller than the current best.
*   D) A greedy approach that always makes the locally optimal choice at each step without reconsidering earlier decisions, building the solution in a single forward pass.
*   **Correct Answer:** B) A recursive strategy that builds a solution incrementally by making one choice at a time, checks if the partial solution can still lead to a valid result, and undoes the last choice (backtracks) when a constraint is violated — then tries the next alternative.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes memoization (top-down dynamic programming). Backtracking does not cache subproblem results.
    *   *Why B is correct:* The "choose → recurse → undo" cycle is the defining structure of backtracking. Pruning (checking constraints before recursing deeper) is what separates backtracking from brute-force enumeration.
    *   *Why C is incorrect:* That describes divide-and-conquer (e.g., merge sort, quick sort). Divide-and-conquer produces and combines partial results; it does not "undo" choices.
    *   *Why D is incorrect:* That describes greedy algorithms. Greedy never revisits choices; backtracking explicitly does.

---

**Question 3**
In generating all permutations of `[1, 2, 3]` using backtracking, you maintain a `used` boolean array. When is the result array appended to the output?
*   A) Every time any element is added to the current partial permutation.
*   B) Only when the partial permutation's length equals the input array length (all elements have been placed).
*   C) Only when the first element of the partial permutation is the smallest available element.
*   D) When the recursive call stack depth reaches n/2, indicating the halfway point of the search.
*   **Correct Answer:** B) Only when the partial permutation's length equals the input array length (all elements have been placed).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Appending at every step would add incomplete (partial) permutations to the result, producing wrong output.
    *   *Why B is correct:* A permutation is complete only when every element has been placed. The base case is `len(current) == len(nums)` — at this point the complete permutation is copied and added to results.
    *   *Why C is incorrect:* The order of the first element has no bearing on when to record a result; all complete permutations are valid regardless of the first element's value.
    *   *Why D is incorrect:* Recursion depth n/2 means only half the elements have been placed — the permutation is incomplete and should not be recorded.

---

**Question 4**
What is the key difference between generating **subsets** (LeetCode #78) and generating **permutations** (LeetCode #46) using backtracking?
*   A) Subsets use a stack while permutations use a queue.
*   B) Subsets record every partial state (including empty and intermediate results) and use an index to avoid re-including earlier elements; permutations record only complete results and use a `used` array to track which elements have been included regardless of position.
*   C) Subsets require sorting the input; permutations do not.
*   D) Subsets use memoization to avoid recomputing identical subsets; permutations avoid memoization because permutations of the same elements are distinct.
*   **Correct Answer:** B) Subsets record every partial state (including empty and intermediate results) and use an index to avoid re-including earlier elements; permutations record only complete results and use a `used` array to track which elements have been included regardless of position.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Both subset and permutation backtracking use the call stack via recursion, not explicit stack/queue data structures.
    *   *Why B is correct:* In subsets, order does not matter and each element can appear at most once — controlled by a start index. In permutations, order matters and each element must appear exactly once — controlled by a `used` boolean array.
    *   *Why C is incorrect:* Sorting helps with deduplication (for problems with duplicate input), but it is not required for the fundamental subset or permutation generation.
    *   *Why D is incorrect:* Neither standard subsets nor permutations use memoization because their subproblems are not overlapping in the DP sense.

---

**Question 5**
In a word search backtracking problem (LeetCode #79), you mark a cell as visited before recursing into it and unmark it after returning. What goes wrong if you forget the "unmark" step?
*   A) The algorithm runs faster because it skips cells it has already seen.
*   B) The algorithm incorrectly treats cells used in one search path as permanently unavailable, causing it to miss valid words that reuse those cells in a different path.
*   C) The algorithm produces duplicate results because the same cell is counted multiple times.
*   D) Nothing — cells in a grid are never revisited, so the unmark step is optional.
*   **Correct Answer:** B) The algorithm incorrectly treats cells used in one search path as permanently unavailable, causing it to miss valid words that reuse those cells in a different path.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Forgetting to unmark does not speed up the algorithm; it produces incorrect results, not performance gains.
    *   *Why B is correct:* The "unmark" step is the undo of backtracking. Without it, a cell visited on one recursive branch is marked used forever, so other branches that need that cell cannot use it — producing missed valid paths (false negatives).
    *   *Why C is incorrect:* Forgetting to unmark causes missed results (false negatives), not duplicates. Duplicates would occur if marking were skipped entirely so cells could be revisited in the same path.
    *   *Why D is incorrect:* Grid cells absolutely can be revisited across different search paths (though not within the same path). The unmark step restores availability for sibling branches.
