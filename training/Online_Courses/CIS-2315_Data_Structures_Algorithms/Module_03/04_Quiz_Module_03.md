# Quiz: Module 03 - Stacks & Queues
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
Which data structure follows the LIFO (Last-In-First-Out) principle?
*   A) Queue
*   B) Priority Queue
*   C) Stack
*   D) Hash Table
*   **Correct Answer:** C) A Stack works by inserting and removing from the same end, matching Last-In-First-Out behavior.
*   **Distractor Analysis:**
    *   *Why correct:* A Stack works by inserting and removing from the same end, matching Last-In-First-Out behavior.
    *   Queue is FIFO (First-In-First-Out). Priority Queue removes based on key value, not order. Hash Table uses direct keys.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **push/pop**?
B) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
D) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
C) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
A) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
*   **Correct Answer:** A) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **push/pop**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **push/pop**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **push/pop**.
    * *Why A is correct:* This describes the exact role and function of **push/pop**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
B) python3 -m venv .venv
D) pytest
C) git commit -m 'update'
A) pip install -r requirements.txt
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.


---

**Question 4**
While working on **Stacks & Queues** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
A) Verify that the index is within the valid range of 0 to len(list)-1.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Stacks & Queues**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..

