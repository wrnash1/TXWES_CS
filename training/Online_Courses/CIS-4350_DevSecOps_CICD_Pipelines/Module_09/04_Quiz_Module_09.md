# Quiz: Module 09 - Infrastructure as Code CI/CD Integration
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What does a tool like Checkov or tfsec scan for in a DevSecOps pipeline?
*   A) Variable name typos
*   B) Misconfigured cloud resources and security violations in IaC templates
*   C) Operating system crashes
*   D) Hard drive block sizes
*   **Correct Answer:** B) IaC scanners flag security risks (such as open S3 buckets or unencrypted disks) before the cloud resources are built.
*   **Distractor Analysis:**
    *   *Why correct:* IaC scanners flag security risks (such as open S3 buckets or unencrypted disks) before the cloud resources are built.
    *   They target IaC configurations, not compiled software errors.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **security scanning (checkov**?
C) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
B) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
D) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **security scanning (checkov**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **security scanning (checkov**.
    * *Why A is correct:* This describes the exact role and function of **security scanning (checkov**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **security scanning (checkov**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
C) python3 -m venv .venv
B) pip install -r requirements.txt
D) git commit -m 'update'
A) pytest
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.


---

**Question 4**
While working on **Infrastructure as Code CI/CD Integration** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Verify that the index is within the valid range of 0 to len(list)-1.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Infrastructure as Code CI/CD Integration**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

