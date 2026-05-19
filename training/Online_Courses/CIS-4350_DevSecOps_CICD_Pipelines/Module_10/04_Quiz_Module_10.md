# Quiz: Module 10 - Automated Cloud Deployment
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Which deployment strategy maintains two identical environments, routing traffic to one while updating and testing the other?
*   A) Direct Cutover
*   B) Blue-Green Deployment
*   C) Rolling Update
*   D) Shadow Deployment
*   **Correct Answer:** B) Blue-green deployment minimizes downtime and risk; if the new environment (green) fails, routing redirects to the old (blue).
*   **Distractor Analysis:**
    *   *Why correct:* Blue-green deployment minimizes downtime and risk; if the new environment (green) fails, routing redirects to the old (blue).
    *   Canary releases slowly roll out updates to a small subset of users.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **blue-green deployment**?
C) HTML tags that convey the meaning and structure of the enclosed content to both the browser and search engines (e.g., <header>, <article>, <footer>) instead of generic containers.
B) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
D) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **blue-green deployment**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **blue-green deployment**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **blue-green deployment**.
    * *Why A is correct:* This describes the exact role and function of **blue-green deployment**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
C) pytest
A) pip install -r requirements.txt
B) git commit -m 'update'
D) python3 -m venv .venv
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Automated Cloud Deployment** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Verify that the index is within the valid range of 0 to len(list)-1.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Automated Cloud Deployment**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

