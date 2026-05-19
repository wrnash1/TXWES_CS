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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **pivot selection.**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
B) A two-dimensional CSS layout system that allows developers to design complex grid-based user interfaces with rows and columns, offering precise control over alignment.
D) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **pivot selection.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **pivot selection.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **pivot selection.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **pivot selection.**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
D) pip install -r requirements.txt
B) python3 -m venv .venv
C) git commit -m 'update'
A) pytest
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.


---

**Question 4**
While working on **Divide & Conquer** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
C) Verify that the index is within the valid range of 0 to len(list)-1.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Divide & Conquer**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

