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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **registry configurations.**?
D) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
B) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
C) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **registry configurations.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **registry configurations.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **registry configurations.**.
    * *Why A is correct:* This describes the exact role and function of **registry configurations.**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
A) pytest
C) pip install -r requirements.txt
B) git commit -m 'update'
D) python3 -m venv .venv
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Container Security & Scan** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
B) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Container Security & Scan**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

