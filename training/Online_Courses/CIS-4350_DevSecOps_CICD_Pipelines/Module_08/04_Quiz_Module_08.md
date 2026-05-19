# Quiz: Module 08 - Software Composition Analysis
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the primary function of a Software Composition Analysis (SCA) tool?
*   A) To design UI screens
*   B) To identify open-source third-party dependencies with known security vulnerabilities (CVEs)
*   C) To speed up network links
*   D) To compile python packages
*   **Correct Answer:** B) SCA scans dependency definition files (e.g. package.json, requirements.txt) against vulnerability databases.
*   **Distractor Analysis:**
    *   *Why correct:* SCA scans dependency definition files (e.g. package.json, requirements.txt) against vulnerability databases.
    *   It maps external package risks, not local code logic or compilation.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **dependency trees**?
D) The descendant node connected to the left branch of a parent node in a binary tree structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
B) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
C) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **dependency trees**.
    * *Why A is correct:* This describes the exact role and function of **dependency trees**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **dependency trees**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **dependency trees**.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
A) git commit -m 'update'
C) python3 -m venv .venv
D) pytest
B) pip install -r requirements.txt
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Software Composition Analysis** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
C) Verify that the index is within the valid range of 0 to len(list)-1.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..


---

**Question 5**
When designing a system for **Software Composition Analysis**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

