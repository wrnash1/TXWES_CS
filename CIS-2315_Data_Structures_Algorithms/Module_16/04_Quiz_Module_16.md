# Quiz: Module 16 – Final Exam Prep & Coding Interview Practice
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
You are given an unsorted integer array and must find two numbers that sum to a target. Which approach has the best time and space complexity?
*   A) Nested loops — O(n²) time, O(1) space.
*   B) Sort the array, then use two pointers — O(n log n) time, O(1) space.
*   C) Use a hash set: iterate once, storing complements; check for each element whether its complement already exists — O(n) time, O(n) space.
*   D) Recursively try all pairs using backtracking — O(2ⁿ) time, O(n) space.
*   **Correct Answer:** C) Use a hash set: iterate once, storing complements; check for each element whether its complement already exists — O(n) time, O(n) space.
*   **Distractor Analysis:**
    *   *Why correct:* The hash set approach is optimal in time: one pass, O(1) average lookup per element. The O(n) space cost is the standard time-space tradeoff for achieving O(n) time on an unsorted input.
    *   A is incorrect: O(n²) is correct but not the best approach — interviewers expect you to optimize beyond brute force.
    *   B is incorrect: O(n log n) time with two pointers is better than O(n²) and uses O(1) space, but the hash approach gives O(n) time. Both are acceptable; the hash map approach is faster.
    *   D is incorrect: Backtracking for this problem is O(2ⁿ) — exponential time with no pruning advantage over simpler approaches.

---

**Question 2**
Which of the following is the most accurate description of the **time-space tradeoff** as it applies to algorithm design in coding interviews?
*   A) The principle that an algorithm's time complexity and space complexity must always multiply to O(n²) as a fundamental constraint of computational hardware.
*   B) The design decision to consume additional memory (e.g., a hash map or DP table) in order to reduce the number of computations, accepting higher space usage in exchange for lower time complexity.
*   C) The observation that recursive algorithms always use more space than iterative algorithms because the call stack grows with recursion depth.
*   D) The rule that in-place algorithms (O(1) space) are always preferred in interviews because interviewers prioritize memory efficiency over runtime.
*   **Correct Answer:** B) The design decision to consume additional memory (e.g., a hash map or DP table) in order to reduce the number of computations, accepting higher space usage in exchange for lower time complexity.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* There is no multiplicative relationship between time and space complexity. An O(n) time algorithm can use O(1), O(n), or O(n²) space depending on the approach.
    *   *Why B is correct:* Classic examples: Two Sum uses O(n) space for a hash map to achieve O(n) time (vs. O(n²) with O(1) space). DP uses O(n) or O(n²) tables to avoid exponential recursive recomputation. This tradeoff is fundamental to interview optimization.
    *   *Why C is incorrect:* While recursion does use O(depth) stack space, the general principle of time-space tradeoff is broader than recursion vs. iteration and is not a universal truth about all recursive vs. iterative comparisons.
    *   *Why D is incorrect:* Interviewers care about both time and space. A solution with O(1) space but O(n²) time is not always preferred over O(n) time with O(n) space. The question asks which is better depends on the context and constraints.

---

**Question 3**
You are in a live coding interview and cannot immediately think of an optimal solution to a medium-difficulty problem. What is the best approach?
*   A) Stay silent and keep thinking until you find the optimal solution, then present it fully formed.
*   B) Ask the interviewer to give you the answer so you can explain how it works.
*   C) State a brute-force approach, explain its complexity, code it correctly, and then work toward optimizing it — narrating your reasoning throughout.
*   D) Tell the interviewer the problem is too hard and ask for an easier one.
*   **Correct Answer:** C) State a brute-force approach, explain its complexity, code it correctly, and then work toward optimizing it — narrating your reasoning throughout.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Silence is one of the worst interview behaviors. Interviewers are evaluating communication and problem-solving process, not just the final answer. Staying silent under pressure signals poor collaboration skills.
    *   *Why B is incorrect:* Asking for the answer is not acceptable in a live coding interview. Interviewers may offer hints, but you must demonstrate your own reasoning.
    *   *Why C is correct:* A working brute-force solution demonstrates problem understanding and coding ability. Iterating from brute force to optimized — with verbal narration — shows systematic thinking. Many interviewers accept a correct brute force and discuss optimization verbally.
    *   *Why D is incorrect:* Asking for a different problem is not an option in a real interview. Difficulty is an opportunity to show resilience and systematic thinking.

---

**Question 4**
You solve a graph problem using BFS and your solution passes all test cases. The interviewer asks: "Can you reduce the space complexity?" The graph has V vertices and E edges. Your BFS currently uses O(V) space for the visited set and queue. What is the minimum additional information needed to determine if space reduction is possible?
*   A) The number of edges E — if E < V, space can be reduced.
*   B) Whether the graph is a tree (acyclic) — in a tree, the BFS queue never holds more than O(width) nodes, potentially reducing max queue size.
*   C) Whether the graph is directed or undirected — directed graphs can use O(V/2) space by processing only outgoing edges.
*   D) The target node's position — if it is near the source, early termination reduces average space usage.
*   **Correct Answer:** B) Whether the graph is a tree (acyclic) — in a tree, the BFS queue never holds more than O(width) nodes, potentially reducing max queue size.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Edge count alone does not determine whether BFS space can be reduced. A path graph (E = V-1) requires O(V) space in BFS; a wide tree may use less.
    *   *Why B is correct:* For general graphs, BFS requires O(V) space for the visited set (to prevent cycles). In a tree (acyclic), no visited set is needed; space reduces to O(width of the tree) for the queue, which can be much less than O(V) for balanced or narrow trees.
    *   *Why C is incorrect:* Directed vs. undirected affects the visited set behavior but does not enable O(V/2) space — the visited set must still track all V nodes in the worst case for both types.
    *   *Why D is incorrect:* Early termination reduces average runtime but not worst-case space complexity. Big-O analysis captures the worst case.

---

**Question 5**
Which of the following is the correct priority order for selecting an algorithm when solving an interview problem, from first consideration to last?
*   A) Correctness → Time complexity → Space complexity → Code simplicity
*   B) Code simplicity → Correctness → Space complexity → Time complexity
*   C) Time complexity → Correctness → Space complexity → Code simplicity
*   D) Space complexity → Time complexity → Code simplicity → Correctness
*   **Correct Answer:** A) Correctness → Time complexity → Space complexity → Code simplicity
*   **Distractor Analysis:**
    *   *Why A is correct:* A solution that is fast but incorrect is worthless. After ensuring correctness, minimize time complexity (usually the primary optimization goal). Space complexity is secondary. Code simplicity (readability, avoiding over-engineering) matters for maintainability and interview clarity but comes last. This ordering reflects how every good engineer and interviewer evaluates solutions.
    *   *Why B is incorrect:* Prioritizing simplicity over correctness means accepting bugs for the sake of shorter code — an unacceptable engineering tradeoff.
    *   *Why C is incorrect:* Prioritizing time complexity over correctness is fundamentally wrong: an O(1) incorrect algorithm is worse than an O(n²) correct one.
    *   *Why D is incorrect:* Prioritizing space complexity over both correctness and time complexity is backwards. Correctness is always the non-negotiable first priority.
