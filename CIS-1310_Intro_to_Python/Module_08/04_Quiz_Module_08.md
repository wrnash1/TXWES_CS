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
Which of the following best describes the **return statement** in a Python function?
*   A) A statement that pauses a function and saves its state so it can be resumed later, yielding one value per pause to an external iterator
*   B) A statement that immediately exits the function and optionally sends a value back to the caller; a function with no return implicitly returns None
*   C) A statement that marks the end of the function body and must appear as the last line; Python raises a SyntaxError if any code follows a return
*   D) A statement used only inside class methods; stand-alone functions use the `output` keyword instead to send values back to the caller
*   **Correct Answer:** B) A statement that immediately exits the function and optionally sends a value back to the caller; a function with no return implicitly returns None.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes the `yield` statement used in generator functions; `return` exits the function entirely and does not preserve local state for resumption.
    *   *Why B is correct:* `return` stops function execution immediately, passes the specified value back to the caller, and causes the function to return `None` if the value is omitted or `return` is absent.
    *   *Why C is incorrect:* A `return` can appear anywhere in a function body, not just at the end; code after an unconditional `return` is unreachable but not a SyntaxError, and many functions have multiple `return` statements in different branches.
    *   *Why D is incorrect:* `return` works identically in stand-alone functions and class methods; there is no `output` keyword in Python.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
C) python3 -m venv .venv
B) git commit -m 'update'
A) pip install -r requirements.txt
D) pytest
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Functions and Parameter Passing** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Verify that the index is within the valid range of 0 to len(list)-1.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Functions and Parameter Passing**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
D) Wrap all database-calling functions in a try-except block that catches exceptions and displays a generic error message to the user.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* Catching exceptions and hiding error messages reduces information leakage but does not prevent the SQL injection from executing; parameterized queries prevent the malicious SQL from being interpreted in the first place.
