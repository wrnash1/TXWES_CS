# Quiz: Module 07 - Dynamic Application Security Testing
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
How does DAST (Dynamic Application Security Testing) scan for security vulnerabilities?
*   A) By reading source code files
*   B) By testing the running application, simulating real attacks from an external perspective
*   C) By analyzing database backups on disk
*   D) By scanning the developer's laptop
*   **Correct Answer:** B) DAST scanners send requests (like SQL injection tests) to active endpoints to evaluate responses.
*   **Distractor Analysis:**
    *   *Why correct:* DAST scanners send requests (like SQL injection tests) to active endpoints to evaluate responses.
    *   SAST reads code text; DAST tests live responses.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **OWASP ZAP**?
B) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
D) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
C) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **OWASP ZAP**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **OWASP ZAP**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **OWASP ZAP**.
    * *Why A is correct:* This describes the exact role and function of **OWASP ZAP**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
D) pytest
A) python3 -m venv .venv
B) git commit -m 'update'
C) pip install -r requirements.txt
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Dynamic Application Security Testing** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Verify that the index is within the valid range of 0 to len(list)-1.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Dynamic Application Security Testing**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

