# Quiz: Module 09 - Test-Driven Development (TDD)
## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

**Question 1**
What is the correct sequence of phases in the Test-Driven Development (TDD) cycle?
*   A) Refactor, Write Code, Verify Test
*   B) Write Test (Red), Implement Code (Green), Refactor
*   C) Design, Code, Test, Release
*   D) Assert, Clean, Deploy
*   **Correct Answer:** B) TDD operates in a tight loop: write a failing test (Red), implement code just enough to pass (Green), then clean up/refactor structure.
*   **Distractor Analysis:**
    *   *Why correct:* TDD operates in a tight loop: write a failing test (Red), implement code just enough to pass (Green), then clean up/refactor structure.
    *   Writing code before test cases violates the core philosophy of TDD.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **test suites**?
D) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
B) The practice of hiding the internal state and representation of an object, exposing access only through public methods.
C) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **test suites**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **test suites**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **test suites**.
    * *Why A is correct:* This describes the exact role and function of **test suites**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
C) python3 -m venv .venv
D) pip install -r requirements.txt
B) git commit -m 'update'
A) pytest
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.


---

**Question 4**
While working on **Test-Driven Development (TDD)** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Verify that the index is within the valid range of 0 to len(list)-1.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Test-Driven Development (TDD)**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
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

