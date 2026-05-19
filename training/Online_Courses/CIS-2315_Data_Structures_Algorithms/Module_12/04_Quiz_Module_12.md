# Quiz: Module 12 - Divide & Conquer
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
What is the average and worst-case time complexity of the Quick Sort algorithm?
*   A) Average: O(N log N), Worst: O(N^2)
*   B) Average: O(N), Worst: O(N log N)
*   C) Average: O(N log N), Worst: O(N log N)
*   D) Average: O(N^2), Worst: O(N^2)
*   **Correct Answer:** A) Quick Sort runs in O(N log N) on average, but degrades to O(N^2) if the pivot splits the array highly unevenly (e.g. sorted arrays).
*   **Distractor Analysis:**
    *   *Why correct:* Quick Sort runs in O(N log N) on average, but degrades to O(N^2) if the pivot splits the array highly unevenly (e.g. sorted arrays).
    *   Merge Sort guarantees O(N log N) in both average and worst cases but requires O(N) extra memory space.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **conquer combining**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
D) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
B) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **conquer combining**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **conquer combining**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **conquer combining**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **conquer combining**.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
A) git commit -m 'update'
D) pytest
C) pip install -r requirements.txt
B) python3 -m venv .venv
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Divide & Conquer** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Verify that the index is within the valid range of 0 to len(list)-1.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Divide & Conquer**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

