# Quiz: Module 15 - DevSecOps Compliance & Audit
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
How does automated pipeline logging support regulatory compliance audits?
*   A) It compiles python scripts
*   B) It provides unalterable audit trails proving that every code release was tested, scanned, and authorized
*   C) It deletes code history
*   D) It speeds up database speeds
*   **Correct Answer:** B) Auditors require proof that release procedures are followed; CI/CD logs serve as immutable operational logs.
*   **Distractor Analysis:**
    *   *Why correct:* Auditors require proof that release procedures are followed; CI/CD logs serve as immutable operational logs.
    *   It supports regulatory audit checks, not compiler execution.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **signed commits**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) Electrostatic Discharge protection; tools (like wrist straps, grounding mats) used to prevent static electricity from destroying sensitive microchips when handling hardware.
B) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
D) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **signed commits**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **signed commits**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **signed commits**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **signed commits**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
C) pip install -r requirements.txt
B) git commit -m 'update'
D) pytest
A) python3 -m venv .venv
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.


---

**Question 4**
While working on **DevSecOps Compliance & Audit** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **DevSecOps Compliance & Audit**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

