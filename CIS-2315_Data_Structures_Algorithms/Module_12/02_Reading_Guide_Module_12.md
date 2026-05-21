# Reading Guide: Module 12 – Recursion and Backtracking
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 12 – Recursion and Backtracking**! Recursion is the fundamental technique underlying tree traversal, divide-and-conquer, dynamic programming, and backtracking. Many candidates struggle with recursion in interviews because they try to trace every call mentally instead of trusting the inductive assumption. Backtracking is recursion applied to constraint-satisfaction problems: build a solution step by step, abandon ("backtrack") as soon as a constraint is violated, and explore the next candidate.

This module covers the recursion mental model, call stack mechanics, and the backtracking template used in permutations, subsets, N-queens, and Sudoku problems.

---

### 1. High-Yield Glossary

*   **Recursion**: A function that calls itself with a smaller or simpler version of its input, progressing toward a base case that stops further calls. Correct recursive thinking requires identifying: (1) the base case, (2) the recursive case, and (3) the inductive hypothesis (what the recursive call is trusted to return).

*   **Base case**: The condition under which a recursive function returns a direct result without making further recursive calls. Every recursive function must have at least one base case to prevent infinite recursion and stack overflow.

*   **Call stack**: The region of memory that stores each active function call frame, including local variables and the return address. Each recursive call pushes a new frame; returning pops it. Deep recursion with no base case causes a stack overflow.

*   **Backtracking**: A recursive problem-solving strategy that builds a solution incrementally and abandons partial solutions that violate constraints, "backtracking" to the last valid state to try the next option. Used for permutations, subsets, N-queens, and word search problems.

*   **State space tree**: The implicit tree of all partial solutions that backtracking explores. Each node is a partial solution; each edge is a choice. Backtracking prunes subtrees that cannot lead to valid complete solutions.

*   **Pruning**: Detecting early that a partial solution cannot lead to a valid complete solution and abandoning it without exploring further. Pruning is what makes backtracking efficient — it avoids the exhaustive O(n!) search of all possibilities.

*   **Memoization in recursion**: Caching the return value of a recursive call indexed by its arguments, so repeated calls with the same arguments return immediately from cache. Transforms overlapping-subproblem recursion from exponential to polynomial time. (Covered deeply in Module 13.)

---

### 2. Certification Exam Tips
*   **Trust the inductive hypothesis:** When writing a recursive function, assume the recursive call returns the correct answer for its smaller input. Do not trace through it mentally — write the base case, write what the recursive call should return, combine results. This is how experts think about recursion.
*   **Backtracking template: choose → recurse → undo:** Every backtracking solution follows: add the current choice to your partial solution, recurse deeper, remove the choice (undo) after returning. The "undo" step is what makes backtracking correct.
*   **LeetCode #78 (Subsets), #46 (Permutations), #39 (Combination Sum) are the canonical trio:** Learn these three problem types. Each uses a slightly different backtracking variant (with/without reuse, with/without duplicates).
*   **Recognize exponential without pruning:** The full state space for permutations is O(n!) and for subsets O(2^n). Without pruning, backtracking is not faster than brute force. Always ask: what constraint can I check early to prune invalid branches?
*   **Draw the recursion tree on paper:** For interviews, sketching the first two levels of the recursion tree clarifies base cases, reduces bugs, and demonstrates structured thinking to the interviewer.
*   **Study Resource:** [Backtracking – NeetCode.io Roadmap](https://neetcode.io/roadmap) — the backtracking section lists the 10 most common interview backtracking problems with video solutions, organized by difficulty.

---

### Required Readings & Videos
*   **Required Reading:** [Recursion – How to Think Like a Computer Scientist (Allen Downey), Chapter 5](https://greenteapress.com/wp/think-python-2e/) — free open-access textbook covering recursive function design, the three-step model, and classic recursive problems.
*   **Required Video:** [Backtracking – NeetCode on YouTube](https://www.youtube.com/watch?v=A80YzvNwqXA) — a 30-minute interview-focused video covering the backtracking template, state space trees, and solving Subsets, Permutations, and Combination Sum from scratch.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement recursive solutions** for factorial, Fibonacci, and power(x, n) — tracing call stacks and identifying base cases.
*   **Solve LeetCode #78 (Subsets)** using backtracking — generate all 2^n subsets of an integer set.
*   **Solve LeetCode #46 (Permutations)** — generate all n! permutations with a `used` boolean array to track which elements have been added.
*   **Solve LeetCode #79 (Word Search)** — 2D grid backtracking with in-place visited marking.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 5 of Think Python (How to Think Like a Computer Scientist).
- [ ] Watch the NeetCode Backtracking video.
- [ ] Implement factorial, Fibonacci, and power(x, n) recursively.
- [ ] Solve LeetCode #78, #46, and #79.
- [ ] Proceed to the Module 12 Quiz.
