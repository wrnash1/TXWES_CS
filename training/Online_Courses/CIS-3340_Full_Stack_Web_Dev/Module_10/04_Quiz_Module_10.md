# Quiz: Module 10 - NoSQL Databases with MongoDB
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which data format does MongoDB use natively to store documents in collections?
*   A) XML
*   B) CSV
*   C) BSON (Binary JSON)
*   D) SQL Table Structure
*   **Correct Answer:** C) MongoDB processes data objects as BSON, an optimized binary representation of JSON files.
*   **Distractor Analysis:**
    *   *Why correct:* MongoDB processes data objects as BSON, an optimized binary representation of JSON files.
    *   BSON supports more data types (such as dates) than plain JSON.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Document database**?
D) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
C) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
B) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Document database**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Document database**.
    * *Why A is correct:* This describes the exact role and function of **Document database**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Document database**.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
D) python3 -m venv .venv
C) pytest
A) git commit -m 'update'
B) pip install -r requirements.txt
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **NoSQL Databases with MongoDB** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
B) Verify that the index is within the valid range of 0 to len(list)-1.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..


---

**Question 5**
When designing a system for **NoSQL Databases with MongoDB**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..

