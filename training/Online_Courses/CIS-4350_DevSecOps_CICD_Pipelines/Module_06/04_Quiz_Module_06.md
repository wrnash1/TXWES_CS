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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **static analysis**?
B) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
D) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
C) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **static analysis**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **static analysis**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **static analysis**.
    * *Why A is correct:* This describes the exact role and function of **static analysis**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
C) python3 -m venv .venv
D) pytest
B) git commit -m 'update'
A) pip install -r requirements.txt
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.


---

**Question 4**
While working on **Static Application Security Testing** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
A) Verify that the index is within the valid range of 0 to len(list)-1.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Static Application Security Testing**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

