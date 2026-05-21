# Quiz: Module 12 - Container Security & Scan
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Which base image is preferred in container security to minimize vulnerability footprints?
*   A) Ubuntu Desktop
*   B) Alpine Linux (minimal)
*   C) Windows Server Core
*   D) Debian Bullseye (Full)
*   **Correct Answer:** B) Alpine is a lightweight Linux distribution containing minimal binaries, reducing the attack surface.
*   **Distractor Analysis:**
    *   *Why correct:* Alpine is a lightweight Linux distribution containing minimal binaries, reducing the attack surface.
    *   Standard distributions package hundreds of packages, raising vulnerability risks.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **image scanning (Trivy)**?
B) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
D) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **image scanning (Trivy)**.
    * *Why A is correct:* This describes the exact role and function of **image scanning (Trivy)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **image scanning (Trivy)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **image scanning (Trivy)**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
C) python3 -m venv .venv
B) git commit -m 'update'
D) pip install -r requirements.txt
A) pytest
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.


---

**Question 4**
While working on **Container Security & Scan** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
C) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Container Security & Scan**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..

