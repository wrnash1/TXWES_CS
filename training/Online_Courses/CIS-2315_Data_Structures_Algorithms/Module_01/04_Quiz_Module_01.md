# Quiz: Module 01 - Time & Space Complexity
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
What is the worst-case time complexity of inserting an element into a standard dynamic array (ArrayList) when it needs resizing?
*   A) O(1)
*   B) O(log N)
*   C) O(N)
*   D) O(N log N)
*   **Correct Answer:** C) When a dynamic array runs out of capacity, it must allocate a new larger array and copy all N elements, taking O(N) time.
*   **Distractor Analysis:**
    *   *Why correct:* When a dynamic array runs out of capacity, it must allocate a new larger array and copy all N elements, taking O(N) time.
    *   O(1) is the amortized insertion time when no resize is needed. O(log N) is typical for binary search trees. O(N log N) represents comparison sorting.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **space complexity**?
A) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
C) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
B) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
D) An undesired resource consumption where a program fails to release allocated memory that is no longer needed.
*   **Correct Answer:** A) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **space complexity**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **space complexity**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **space complexity**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **space complexity**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
A) pip install -r requirements.txt
B) python3 -m venv .venv
C) git commit -m 'update'
D) pytest
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Time & Space Complexity** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
B) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Time & Space Complexity**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..

