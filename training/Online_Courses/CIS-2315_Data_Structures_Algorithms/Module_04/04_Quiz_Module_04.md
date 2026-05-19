# Quiz: Module 04 - Recursion & Backtracking
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

### Question 1
What must every functional recursive function include to avoid infinite recursion and stack overflow?

*   A) A global loop variable
*   B) A base case that terminates recursion
*   C) A try-except error wrapper
*   D) A class destructor

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
The base case acts as the exit condition where the recursion stops calling itself.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Loops are not required for recursion. Error wrappers only capture crashes but don't prevent them. Destructors manage memory deallocation but not logical call structures.
