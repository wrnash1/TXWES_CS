# Quiz: Module 11 - Dijkstra's Shortest Path
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

### Question 1
Why is Dijkstra's algorithm unable to guarantee correct shortest paths in graphs with negative edge weights?

*   A) It uses a queue instead of stack
*   B) Once a vertex is visited/relaxed, the algorithm assumes its shortest path is permanently solved
*   C) It only works on binary trees
*   D) It runs in O(N^3) time

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Dijkstra's greedy choice assumes that paths can only increase in cost; a negative edge can invalidate earlier evaluations.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Bellman-Ford is used for graphs with negative weights because it repeatedly relaxes all edges.
