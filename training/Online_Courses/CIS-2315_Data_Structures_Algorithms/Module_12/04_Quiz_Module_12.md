# Quiz: Module 12 - Divide & Conquer
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

### Question 1
What is the average and worst-case time complexity of the Quick Sort algorithm?

*   A) Average: O(N log N), Worst: O(N^2)
*   B) Average: O(N), Worst: O(N log N)
*   C) Average: O(N log N), Worst: O(N log N)
*   D) Average: O(N^2), Worst: O(N^2)

---

### Answer Key
*   **Correct Option:** **A**

---

### Explanation
Quick Sort runs in O(N log N) on average, but degrades to O(N^2) if the pivot splits the array highly unevenly (e.g. sorted arrays).

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Merge Sort guarantees O(N log N) in both average and worst cases but requires O(N) extra memory space.
