# Quiz: Module 05 - Binary Trees & BSTs
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
In a valid Binary Search Tree (BST), what property must be true for every node N?
*   A) All left descendants <= N, and all right descendants > N
*   B) Left child and right child must have equal height
*   C) Every node must have exactly two child nodes
*   D) The tree must be balanced
*   **Correct Answer:** A) The BST invariant requires all values in the left subtree of N to be less than or equal to N, and all values in the right subtree to be greater.
*   **Distractor Analysis:**
    *   *Why correct:* The BST invariant requires all values in the left subtree of N to be less than or equal to N, and all values in the right subtree to be greater.
    *   Equal height defines balanced trees. Node count properties define strict binary trees.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Root node**?
C) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
D) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
A) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
B) The descendant node connected to the left branch of a parent node in a binary tree structure.
*   **Correct Answer:** A) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Root node**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Root node**.
    * *Why A is correct:* This describes the exact role and function of **Root node**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Root node**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
B) pip install -r requirements.txt
C) git commit -m 'update'
A) python3 -m venv .venv
D) pytest
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Binary Trees & BSTs** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
C) Verify that the index is within the valid range of 0 to len(list)-1.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Binary Trees & BSTs**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

