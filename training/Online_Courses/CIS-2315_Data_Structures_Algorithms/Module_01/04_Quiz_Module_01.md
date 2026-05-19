# Quiz: Module 01 - Time & Space Complexity
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

### Question 1
What is the worst-case time complexity of inserting an element into a standard dynamic array (ArrayList) when it needs resizing?

*   A) O(1)
*   B) O(log N)
*   C) O(N)
*   D) O(N log N)

---

### Answer Key
*   **Correct Option:** **C**

---

### Explanation
When a dynamic array runs out of capacity, it must allocate a new larger array and copy all N elements, taking O(N) time.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    O(1) is the amortized insertion time when no resize is needed. O(log N) is typical for binary search trees. O(N log N) represents comparison sorting.
