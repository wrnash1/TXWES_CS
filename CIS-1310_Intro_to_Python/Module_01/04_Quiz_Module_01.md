# Quiz: Module 01 - Python Basics & Local Environment
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
What is Python's execution model?
*   A) Compiled before running
*   B) Interpreted line-by-line
*   C) Assembled to machine code
*   D) None of the above
*   **Correct Answer:** B) Python is executed by an interpreter that reads and processes code line-by-line.
*   **Distractor Analysis:**
    *   *Why correct:* Python is executed by an interpreter that reads and processes code line-by-line.
    *   Compiled languages compile source code all at once. Python reads and executes code dynamically.

---

**Question 2**
Which of the following best describes **script mode** in Python?
*   A) Running Python statements one at a time in an interactive session that immediately prints results
*   B) Executing a saved `.py` file from top to bottom through the interpreter
*   C) A special debugging mode that pauses execution after every line
*   D) A mode that compiles Python code into bytecode and stores it as a standalone executable
*   **Correct Answer:** B) Executing a saved `.py` file from top to bottom through the interpreter.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes the REPL (interactive shell), not script mode — in script mode you run a complete file, not one statement at a time.
    *   *Why B is correct:* Script mode means passing a `.py` file to the interpreter (e.g., `python3 myscript.py`), which executes all statements sequentially.
    *   *Why C is incorrect:* Python has no built-in "pause after every line" mode by default; that would require a debugger like `pdb`.
    *   *Why D is incorrect:* Python does compile to `.pyc` bytecode internally, but that is transparent to the user and does not produce a standalone executable.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
D) python3 -m venv .venv
C) git commit -m 'update'
B) pip install -r requirements.txt
A) pytest
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.


---

**Question 4**
While working on **Python Basics & Local Environment** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..


---

**Question 5**
When designing a system for **Python Basics & Local Environment**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
D) Store passwords using reversible symmetric encryption so they can be recovered if needed.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why C is incorrect:* Full disk encryption protects data at rest on the physical drive but does not prevent a running application from reading plain-text credentials from a database.
    * *Why D is incorrect:* Reversible encryption is dangerous for passwords because if the encryption key is compromised, all passwords are exposed; one-way hashing with bcrypt is the correct approach.
