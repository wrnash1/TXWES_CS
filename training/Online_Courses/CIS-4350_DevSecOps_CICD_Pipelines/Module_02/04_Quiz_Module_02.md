# Quiz: Module 02 - Continuous Integration Concepts
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the primary function of a linter tool in a Continuous Integration pipeline?
*   A) To compile binaries
*   B) To analyze source code for programmatic errors, code smells, and style guide violations
*   C) To host REST APIs
*   D) To decrypt database keys
*   **Correct Answer:** B) Linters check code syntax and styling against standard formats (e.g. PEP 8 for Python), catching basic errors early.
*   **Distractor Analysis:**
    *   *Why correct:* Linters check code syntax and styling against standard formats (e.g. PEP 8 for Python), catching basic errors early.
    *   Compilers convert code. Linters analyze source text.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **local commit hooks**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
D) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
B) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **local commit hooks**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **local commit hooks**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **local commit hooks**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **local commit hooks**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
B) python3 -m venv .venv
C) pip install -r requirements.txt
A) pytest
D) git commit -m 'update'
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Continuous Integration Concepts** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
C) Verify that the index is within the valid range of 0 to len(list)-1.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Continuous Integration Concepts**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
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

