# Quiz: Module 08 - Functions and Parameter Passing
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
How are multiple values returned from a Python function?
*   A) Using multiple return statements
*   B) Returned as a tuple
*   C) Python functions can only return one value
*   D) Using the yield keyword
*   **Correct Answer:** B) Returning multiple items separated by commas in Python automatically packages them into a tuple.
*   **Distractor Analysis:**
    *   *Why correct:* Returning multiple items separated by commas in Python automatically packages them into a tuple.
    *   A is invalid (execution stops at first return). yield makes it a generator, not a standard function return.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **positional vs keyword arguments**?
B) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The descendant node connected to the right branch of a parent node in a binary tree structure.
D) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **positional vs keyword arguments**.
    * *Why A is correct:* This describes the exact role and function of **positional vs keyword arguments**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **positional vs keyword arguments**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **positional vs keyword arguments**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
D) pytest
B) pip install -r requirements.txt
C) git commit -m 'update'
A) python3 -m venv .venv
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.


---

**Question 4**
While working on **Functions and Parameter Passing** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
C) Verify that the index is within the valid range of 0 to len(list)-1.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Functions and Parameter Passing**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..

