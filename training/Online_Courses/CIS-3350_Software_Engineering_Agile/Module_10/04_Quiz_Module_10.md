# Quiz: Module 10 - CI/CD Foundations
## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

**Question 1**
What is the primary goal of Continuous Integration (CI)?
*   A) To manually deploy builds to production servers
*   B) To automatically build, lint, and run tests on code changes whenever developer merges to shared branches
*   C) To write project charters
*   D) To backup database files
*   **Correct Answer:** B) CI automatically verifies new changes pushed to repositories using automation pipelines, detecting compilation and test failures early.
*   **Distractor Analysis:**
    *   *Why correct:* CI automatically verifies new changes pushed to repositories using automation pipelines, detecting compilation and test failures early.
    *   Continuous Delivery/Deployment (CD) handles the automation of software releases to targets.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Continuous Deployment**?
C) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
D) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
B) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Continuous Deployment**.
    * *Why A is correct:* This describes the exact role and function of **Continuous Deployment**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Continuous Deployment**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Continuous Deployment**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
A) pytest
D) git commit -m 'update'
B) pip install -r requirements.txt
C) python3 -m venv .venv
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **CI/CD Foundations** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..


---

**Question 5**
When designing a system for **CI/CD Foundations**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

