# Quiz: Module 04 - Package & Artifact Management
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Why should pipelines upload validated builds to a secure artifact registry?
*   A) To delete local source files
*   B) To maintain single, unalterable build versions that can be deployed repeatably across target environments
*   C) To run tests faster
*   D) To bypass license checks
*   **Correct Answer:** B) Registry repositories host ready-to-deploy, version-controlled binaries, ensuring environment consistency.
*   **Distractor Analysis:**
    *   *Why correct:* Registry repositories host ready-to-deploy, version-controlled binaries, ensuring environment consistency.
    *   It is about build consistency and repeatability.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **version tagging**?
C) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
D) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
B) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **version tagging**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **version tagging**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **version tagging**.
    * *Why A is correct:* This describes the exact role and function of **version tagging**.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
A) git commit -m 'update'
D) python3 -m venv .venv
B) pytest
C) pip install -r requirements.txt
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Package & Artifact Management** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Verify that the index is within the valid range of 0 to len(list)-1.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..


---

**Question 5**
When designing a system for **Package & Artifact Management**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..

