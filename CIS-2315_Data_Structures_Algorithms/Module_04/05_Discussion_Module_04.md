# Discussion Forum: Module 04 — Recursion & Backtracking

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Background

Recursion is the hardest conceptual leap in this course — not because the code is complex, but because it requires trusting a function you are in the middle of writing. The base-case/recursive-case structure is the contract that makes that trust safe. Memoization shows how the same technique that makes naive Fibonacci catastrophically slow can be transformed by a single caching layer into linear time. Backtracking extends recursion into decision-making, and the choose → recurse → unchoose template is one of the most universally applicable patterns in technical interviews. This discussion asks you to reason about why these techniques work and what goes wrong when they are applied incorrectly.

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — The Base Case Contract

Every correct recursive function satisfies a three-part contract: there is a base case, every recursive call makes progress toward the base case, and the expression around the recursive call correctly assembles the answer. Violating any one of these three parts breaks the function — sometimes silently.

In 175–225 words, respond to the following:

- From the Module 04 lab (Part 1, Section 1.1), you implemented and traced `factorial(n)`. Trace `factorial(4)` manually — show the state of the call stack at maximum depth (when `factorial(0)` is executing) and the return value at each frame as it unwinds. How many frames are simultaneously live at maximum depth?
- The reading guide identifies three requirements for a correct recursive function. Describe what goes wrong — specifically — if each is violated. What happens at runtime if there is no base case? What happens if the recursive call does not make progress? What happens if the assembly expression is wrong?
- The reading guide notes that recursive binary search has O(log n) space (call stack) while iterative binary search has O(1) space. Given that the time complexity is the same, when would you choose the recursive version and when would you choose the iterative version?

Reference the lab or reading guide in your response.

---

### Scenario B — Memoization and Overlapping Subproblems

The naive recursive Fibonacci algorithm is O(2ⁿ) not because each individual operation is expensive, but because it recomputes the same subproblems exponentially many times. Adding a cache reduces this to O(n) because each unique input is computed at most once. The concept of overlapping subproblems is the key property that makes memoization — and eventually dynamic programming — applicable.

In 175–225 words, respond to the following:

- From the Module 04 lab (Part 1, Section 1.3), you benchmarked `fib_naive`, `fib_memo`, and `fib_lru` at n=35. Describe the performance difference you observed. Draw (in text) the call tree for `fib(5)` and annotate which nodes are computed redundantly in the naive version.
- The reading guide explains that `@lru_cache(maxsize=None)` wraps the function but does not change its recursive structure. If the recursion is still happening, why does memoization change the time complexity from O(2ⁿ) to O(n)? What is the key difference in how the call tree is traversed?
- Identify a problem other than Fibonacci where naive recursion has overlapping subproblems and memoization would help. Describe the overlapping structure — what is the subproblem that gets recomputed?

Reference the lab or reading guide in your response.

---

### Scenario C — The Unchoose Step in Backtracking

The backtracking template's third step — `current.pop()` after the recursive call — is the most commonly forgotten step in interview implementations. Its purpose is to restore state: the `current` list must be in the same condition after a loop iteration as before it, so the next iteration starts from a clean slate. Without this restore step, the algorithm produces incorrect results in a way that is easy to miss unless you trace the execution.

In 175–225 words, respond to the following:

- From the Module 04 lab (Part 2, Section 2.1), you implemented `subsets([1, 2, 3])`. Trace the first four calls to `backtrack` — show the state of `current` at the start of each call and what is recorded. Which specific call demonstrates the unchoose step restoring state?
- The reading guide describes the unchoose step as "restoring state." Describe precisely what would be in the `result` list for `subsets([1, 2])` if `current.pop()` were removed. Show the incorrect output and explain why each incorrect entry appears.
- The Generate Parentheses algorithm does not have an explicit `current.pop()` because strings are immutable in Python — the expression `s + '('` creates a new string without modifying `s`. Explain why immutable string concatenation automatically provides the "unchoose" behavior. What is the tradeoff compared to using a mutable list with `append`/`pop`?

Reference the lab or reading guide in your response.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 04 lab or reading guide at least once

---

## Peer Response Requirements

- **Due:** Sunday at 11:59 PM CST
- Respond to **at least two classmates** who chose **different scenarios**
- Each response: minimum **60 words**, must add substance
- Acceptable contributions: add a second example, challenge a claim with a counter-case, extend the concept to a harder problem, or describe a real-world application that illustrates the point

---

## Grading Rubric — 10 Points Total

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 5–6 pts | Scenario answered fully with specific, concrete examples. Reference to lab or reading guide. 175–225 words. Complete sentences. |
| 3–4 pts | Mostly addressed but vague or generic. Close to word count. |
| 1–2 pts | Significant parts missing or well below word count. |
| 0 pts | Not submitted. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 pts | Two responses to classmates with different scenarios. Each 60+ words and adds genuine value. |
| 2 pts | One peer response only, or responses lack substance. |
| 0 pts | No peer responses. |

---

## A Note from Professor Nash

Recursion trips up even experienced developers because it requires holding an incomplete computation in your head and trusting it to complete correctly. The trick is to stop simulating the whole call tree and start reading the function as a specification: base case returns the known answer; recursive case assumes the sub-answer is correct and assembles from there. If you can articulate those two things clearly, you understand recursion. The backtracking template — choose, recurse, unchoose — is a direct application of this thinking to decision problems. Master it this week; you will use it again in trees, graphs, and dynamic programming. I look forward to your posts.
