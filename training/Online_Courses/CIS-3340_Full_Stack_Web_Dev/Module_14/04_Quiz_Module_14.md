# Quiz: Module 14 - Deployment to AWS
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which AWS compute service provides resizable, raw virtual machines for hosting backend applications?
*   A) Amazon S3
*   B) Amazon EC2
*   C) AWS Lambda
*   D) Amazon RDS
*   **Correct Answer:** B) EC2 (Elastic Compute Cloud) provides virtual machines (instances) for running backend service code.
*   **Distractor Analysis:**
    *   *Why correct:* EC2 (Elastic Compute Cloud) provides virtual machines (instances) for running backend service code.
    *   S3 is object storage. Lambda is serverless function execution.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **public ports**?
D) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
B) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
C) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **public ports**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **public ports**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **public ports**.
    * *Why A is correct:* This describes the exact role and function of **public ports**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
D) pip install -r requirements.txt
B) git commit -m 'update'
A) pytest
C) python3 -m venv .venv
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Deployment to AWS** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Deployment to AWS**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

