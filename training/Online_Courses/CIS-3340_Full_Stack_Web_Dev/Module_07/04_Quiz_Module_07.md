# Quiz: Module 07 - Node.js & Express Server
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which code snippet initializes a basic Express application instance?
*   A) const app = express()
*   B) const app = new express.App()
*   C) const app = require('express').start()
*   D) const app = Express.init()
*   **Correct Answer:** A) Invoking the required express module function creates an application instance.
*   **Distractor Analysis:**
    *   *Why correct:* Invoking the required express module function creates an application instance.
    *   The other options show incorrect module instantiation syntax.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Node event loop**?
D) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
C) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
B) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Node event loop**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Node event loop**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Node event loop**.
    * *Why A is correct:* This describes the exact role and function of **Node event loop**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
D) git commit -m 'update'
B) pytest
C) python3 -m venv .venv
A) pip install -r requirements.txt
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.


---

**Question 4**
While working on **Node.js & Express Server** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Node.js & Express Server**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

