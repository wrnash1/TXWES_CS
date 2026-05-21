# Quiz: Module 05 - Loops - Iteration with While and For
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
What does the `break` statement do inside a loop?
*   A) Skips the current iteration
*   B) Terminates the loop immediately
*   C) Restarts the loop
*   D) Exits the entire program
*   **Correct Answer:** B) The `break` statement exits the innermost loop immediately, bypassing any remaining iterations.
*   **Distractor Analysis:**
    *   *Why correct:* The `break` statement exits the innermost loop immediately, bypassing any remaining iterations.
    *   A describes the `continue` statement. D describes `exit()` or `sys.exit()`.

---

**Question 2**
Which of the following best describes **loop control statements** (`break` and `continue`) in Python?
*   A) Keywords that define the start and end of a loop body, replacing the indentation-based block structure used elsewhere in Python
*   B) Statements that alter the normal flow of a loop — `break` exits the loop immediately while `continue` skips the rest of the current iteration and jumps to the next
*   C) Functions inherited from the `itertools` module that must be imported before use; they return iterator objects rather than modifying loop flow directly
*   D) Statements that apply only to `while` loops; `for` loops must use `return` to exit early and `pass` to skip an iteration
*   **Correct Answer:** B) Statements that alter the normal flow of a loop — `break` exits the loop immediately while `continue` skips the rest of the current iteration and jumps to the next.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Python uses indentation to define block structure; `break` and `continue` do not define blocks — they are flow-control statements executed inside an already-defined loop body.
    *   *Why B is correct:* Both `break` and `continue` are built-in keywords that modify loop execution: `break` ends the loop, `continue` restarts it at the next iteration without finishing the current one.
    *   *Why C is incorrect:* `break` and `continue` are Python keywords, not functions, and they require no import; `itertools` provides iterator utilities but is unrelated to these flow-control keywords.
    *   *Why D is incorrect:* Both `break` and `continue` work in both `while` and `for` loops; using `return` inside a loop exits the entire function, not just the loop, and `pass` is a no-operation placeholder, not an iteration-skip tool.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
D) git commit -m 'update'
A) python3 -m venv .venv
B) pytest
C) pip install -r requirements.txt
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Loops - Iteration with While and For** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Loops - Iteration with While and For**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
D) Use a loop to iterate over each character of a password and validate that it meets minimum complexity rules before storing it.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* Complexity validation ensures passwords meet strength requirements but does not address how they are stored; a strong password stored in plain text is still fully exposed in a breach.
