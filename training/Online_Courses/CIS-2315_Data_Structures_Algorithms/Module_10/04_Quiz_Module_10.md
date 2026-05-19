# Quiz: Module 10 - Breadth-First & Depth-First Search
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
Which traversal algorithm uses a queue to visit all nodes at the current depth level before moving to the next level?
*   A) Depth-First Search (DFS)
*   B) Breadth-First Search (BFS)
*   C) Preorder traversal
*   D) Postorder traversal
*   **Correct Answer:** B) BFS processes nodes level by level using a FIFO queue to store discovered frontier vertices.
*   **Distractor Analysis:**
    *   *Why correct:* BFS processes nodes level by level using a FIFO queue to store discovered frontier vertices.
    *   DFS travels deep along a branch first, typically implemented using a LIFO stack.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **queue frontier**?
D) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
B) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
C) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **queue frontier**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **queue frontier**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **queue frontier**.
    * *Why A is correct:* This describes the exact role and function of **queue frontier**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
A) python3 -m venv .venv
C) pytest
B) pip install -r requirements.txt
D) git commit -m 'update'
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Breadth-First & Depth-First Search** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
B) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Breadth-First & Depth-First Search**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
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

