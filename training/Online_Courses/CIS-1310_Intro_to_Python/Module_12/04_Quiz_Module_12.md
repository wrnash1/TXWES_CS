# Quiz: Module 12 - Exception Handling
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
Which block runs regardless of whether an exception was raised or not?
*   A) except
*   B) else
*   C) finally
*   D) try
*   **Correct Answer:** C) The `finally` block is guaranteed to execute at the end of the try-except chain, making it perfect for cleanup.
*   **Distractor Analysis:**
    *   *Why correct:* The `finally` block is guaranteed to execute at the end of the try-except chain, making it perfect for cleanup.
    *   except only runs if an exception occurs. else only runs if no exception occurs.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **else and finally clauses**?
C) The process of restructuring existing computer code without changing its external behavior to improve readability and reduce complexity.
D) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
B) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **else and finally clauses**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **else and finally clauses**.
    * *Why A is correct:* This describes the exact role and function of **else and finally clauses**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **else and finally clauses**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
A) python3 -m venv .venv
B) pip install -r requirements.txt
C) git commit -m 'update'
D) pytest
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Exception Handling** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..


---

**Question 5**
When designing a system for **Exception Handling**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

