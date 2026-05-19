# Quiz: Module 13 - Monitoring, Logging & Telemetry
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the purpose of centralized logging in DevOps?
*   A) To write code logic
*   B) To aggregate system and application logs from all servers into a single queried portal
*   C) To host DNS domains
*   D) To execute unit tests
*   **Correct Answer:** B) Centralized logs permit rapid query searches across microservices during system failures, debugging issues quickly.
*   **Distractor Analysis:**
    *   *Why correct:* Centralized logs permit rapid query searches across microservices during system failures, debugging issues quickly.
    *   It targets operations management, not software compilation.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Log aggregates**?
B) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
D) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
C) The descendant node connected to the left branch of a parent node in a binary tree structure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Log aggregates**.
    * *Why A is correct:* This describes the exact role and function of **Log aggregates**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Log aggregates**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Log aggregates**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
D) git commit -m 'update'
B) python3 -m venv .venv
C) pip install -r requirements.txt
A) pytest
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.


---

**Question 4**
While working on **Monitoring, Logging & Telemetry** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Verify that the index is within the valid range of 0 to len(list)-1.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Monitoring, Logging & Telemetry**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

