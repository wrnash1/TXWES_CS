# Quiz: Module 08 - Server-Side Routing & Middleware
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
What function must be invoked at the end of a custom Express middleware handler to pass control to the next function in line?
*   A) end()
*   B) send()
*   C) next()
*   D) forward()
*   **Correct Answer:** C) Invoking the next() callback tells Express to progress to the subsequent handler in the pipeline.
*   **Distractor Analysis:**
    *   *Why correct:* Invoking the next() callback tells Express to progress to the subsequent handler in the pipeline.
    *   Failing to call next() will cause the request to hang.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **routing parameters**?
B) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
C) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
D) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **routing parameters**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **routing parameters**.
    * *Why A is correct:* This describes the exact role and function of **routing parameters**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **routing parameters**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
C) pytest
B) git commit -m 'update'
A) pip install -r requirements.txt
D) python3 -m venv .venv
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Server-Side Routing & Middleware** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
C) Verify that the index is within the valid range of 0 to len(list)-1.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Server-Side Routing & Middleware**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

