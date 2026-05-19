# Quiz: Module 09 - Graph Representations
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

### Question 1
Which representation is most memory-efficient for a sparse graph with N vertices and few edges?

*   A) Adjacency Matrix
*   B) Adjacency List
*   C) Edge List
*   D) Hash Matrix

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Adjacency lists only store actual links, bypassing the O(N^2) memory footprint of adjacency matrices.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Adjacency matrix always uses O(V^2) memory space regardless of edge density.
