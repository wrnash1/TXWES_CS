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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Node pointer**?
B) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
C) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
D) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
A) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
*   **Correct Answer:** A) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Node pointer**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Node pointer**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Node pointer**.
    * *Why A is correct:* This describes the exact role and function of **Node pointer**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
C) python3 -m venv .venv
D) pytest
A) pip install -r requirements.txt
B) git commit -m 'update'
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Singly & Doubly Linked Lists** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
B) Verify that the index is within the valid range of 0 to len(list)-1.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..


---

**Question 5**
When designing a system for **Singly & Doubly Linked Lists**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

