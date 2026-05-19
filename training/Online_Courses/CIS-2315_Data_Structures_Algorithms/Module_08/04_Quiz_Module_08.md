# Quiz: Module 08 - Hash Tables & Hash Collisions
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

### Question 1
What is the average-case time complexity of searching for a key in a well-distributed Hash Table?

*   A) O(1)
*   B) O(log N)
*   C) O(N)
*   D) O(N log N)

---

### Answer Key
*   **Correct Option:** **A**

---

### Explanation
If the hash function distributes keys evenly, finding a key via constant hash mapping takes O(1) time.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    O(N) is the worst-case hash table lookup (when all keys collide into a single chain).
