# Quiz: Module 11 - Secret Management in Pipelines
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Why should API keys and database passwords never be hardcoded in Git source files?
*   A) Git cannot compile files with secrets
*   B) Once pushed, keys are saved in history logs and can be exposed to unauthorized parties
*   C) Secrets slow down code execution
*   D) Secrets cause network routing loops
*   **Correct Answer:** B) Git histories are persistent; exposing keys allows attackers to scrape repositories and compromise systems.
*   **Distractor Analysis:**
    *   *Why correct:* Git histories are persistent; exposing keys allows attackers to scrape repositories and compromise systems.
    *   It is a severe security risk, not a compilation or speed constraint.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Secret scanning**?
B) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
C) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
D) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Secret scanning**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Secret scanning**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Secret scanning**.
    * *Why A is correct:* This describes the exact role and function of **Secret scanning**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
B) pip install -r requirements.txt
D) pytest
C) git commit -m 'update'
A) python3 -m venv .venv
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.


---

**Question 4**
While working on **Secret Management in Pipelines** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..


---

**Question 5**
When designing a system for **Secret Management in Pipelines**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

