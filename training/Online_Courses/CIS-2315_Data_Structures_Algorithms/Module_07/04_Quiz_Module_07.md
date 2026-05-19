# Quiz: Module 07 - Heaps & Priority Queues
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

### Question 1
Which array index represents the parent of a node located at index i in a 0-indexed binary heap?

*   A) 2*i + 1
*   B) 2*i + 2
*   C) (i - 1) // 2
*   D) i // 2

---

### Answer Key
*   **Correct Option:** **C**

---

### Explanation
For any 0-indexed element i, its parent is located at index floor((i-1)/2).

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    2*i+1 is left child. 2*i+2 is right child.
