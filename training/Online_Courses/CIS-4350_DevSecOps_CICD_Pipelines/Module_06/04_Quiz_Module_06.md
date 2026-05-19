# Quiz: Module 06 - Static Application Security Testing
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the characteristic behavior of a SAST (Static Application Security Testing) tool?
*   A) It scans code by executing the application in a test sandbox
*   B) It analyzes source code files statically without running the application
*   C) It monitors CPU fan speeds
*   D) It blocks network ports dynamically
*   **Correct Answer:** B) SAST scanners evaluate source files against known vulnerability patterns (e.g. hardcoded keys, SQL concatenation).
*   **Distractor Analysis:**
    *   *Why correct:* SAST scanners evaluate source files against known vulnerability patterns (e.g. hardcoded keys, SQL concatenation).
    *   Dynamic testing (DAST) requires executing the code.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **pattern matching**?
C) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
B) An undesired resource consumption where a program fails to release allocated memory that is no longer needed.
D) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **pattern matching**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **pattern matching**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **pattern matching**.
    * *Why A is correct:* This describes the exact role and function of **pattern matching**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
C) git commit -m 'update'
D) pip install -r requirements.txt
A) python3 -m venv .venv
B) pytest
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Static Application Security Testing** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Verify that the index is within the valid range of 0 to len(list)-1.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
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
When designing a system for **Static Application Security Testing**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

