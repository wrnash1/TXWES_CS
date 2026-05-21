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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **best-case**?
A) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
D) The descendant node connected to the left branch of a parent node in a binary tree structure.
B) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
C) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
*   **Correct Answer:** A) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **best-case**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **best-case**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **best-case**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **best-case**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
C) git commit -m 'update'
A) pip install -r requirements.txt
B) pytest
D) python3 -m venv .venv
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Time & Space Complexity** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Verify that the index is within the valid range of 0 to len(list)-1.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Time & Space Complexity**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

