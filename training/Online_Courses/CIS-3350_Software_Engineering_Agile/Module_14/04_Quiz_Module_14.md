# Quiz: Module 14 - Software Security & Coding Standards
## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

**Question 1**
Which security practice is most critical to prevent buffer overflows or injection vulnerability issues?
*   A) Writing verbose comments
*   B) Input validation and sanitization
*   C) Reducing compiler speed
*   D) Disabling firewalls
*   **Correct Answer:** B) Validating input parameters against type and length boundaries stops malicious payloads from executing.
*   **Distractor Analysis:**
    *   *Why correct:* Validating input parameters against type and length boundaries stops malicious payloads from executing.
    *   Comments or compiler configurations do not alter security execution characteristics.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **OWASP standards**?
D) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
B) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
C) The core CSS layout block consisting of margins, borders, padding, and the actual content area, defining the sizing and spacing of every page element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **OWASP standards**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **OWASP standards**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **OWASP standards**.
    * *Why A is correct:* This describes the exact role and function of **OWASP standards**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
B) pytest
C) git commit -m 'update'
D) pip install -r requirements.txt
A) python3 -m venv .venv
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.


---

**Question 4**
While working on **Software Security & Coding Standards** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
C) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Software Security & Coding Standards**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

