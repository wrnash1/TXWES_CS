# Quiz: Module 02 - Singly & Doubly Linked Lists
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
What is the primary advantage of a doubly linked list over a singly linked list?
*   A) Requires less memory per node
*   B) Allows traversal in both directions (forward and backward)
*   C) O(1) random index access
*   D) Faster sorting speed
*   **Correct Answer:** B) Each node in a doubly linked list contains pointers to both the next and previous nodes, allowing bidirectional traversal.
*   **Distractor Analysis:**
    *   *Why correct:* Each node in a doubly linked list contains pointers to both the next and previous nodes, allowing bidirectional traversal.
    *   A is incorrect because the previous pointer increases memory. C is wrong because linked lists require O(N) traversal to reach an index. D is false since list node link-rebuilding doesn't change algorithm bounds.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **head node**?
D) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
B) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
C) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
A) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
*   **Correct Answer:** A) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **head node**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **head node**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **head node**.
    * *Why A is correct:* This describes the exact role and function of **head node**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
D) pip install -r requirements.txt
B) git commit -m 'update'
C) pytest
A) python3 -m venv .venv
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.


---

**Question 4**
While working on **Singly & Doubly Linked Lists** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Verify that the index is within the valid range of 0 to len(list)-1.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Singly & Doubly Linked Lists**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

