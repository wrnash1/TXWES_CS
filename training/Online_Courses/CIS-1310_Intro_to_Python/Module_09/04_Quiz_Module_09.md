# Quiz: Module 09 - Scopes, Namespaces, and Recursion
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
What keyword is required to modify a variable defined at the module level from inside a function?
*   A) nonlocal
*   B) global
*   C) static
*   D) public
*   **Correct Answer:** B) The `global` keyword declares that a variable inside the function refers to the module-level namespace.
*   **Distractor Analysis:**
    *   *Why correct:* The `global` keyword declares that a variable inside the function refers to the module-level namespace.
    *   nonlocal is for nested/closure scopes. static and public are not used in Python variable scoping.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Global vs local scope**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
B) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
C) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
D) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Global vs local scope**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Global vs local scope**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Global vs local scope**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Global vs local scope**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
B) git commit -m 'update'
A) pip install -r requirements.txt
D) pytest
C) python3 -m venv .venv
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Scopes, Namespaces, and Recursion** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..


---

**Question 5**
When designing a system for **Scopes, Namespaces, and Recursion**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..

