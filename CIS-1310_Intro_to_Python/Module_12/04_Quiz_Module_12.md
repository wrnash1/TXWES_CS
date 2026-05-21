# Quiz: Module 12 - Exception Handling
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
Which block runs regardless of whether an exception was raised or not?
*   A) except
*   B) else
*   C) finally
*   D) try
*   **Correct Answer:** C) The `finally` block is guaranteed to execute at the end of the try-except chain, making it perfect for cleanup.
*   **Distractor Analysis:**
    *   *Why correct:* The `finally` block is guaranteed to execute at the end of the try-except chain, making it perfect for cleanup.
    *   except only runs if an exception occurs. else only runs if no exception occurs.

---

**Question 2**
Which of the following best describes the **`else` and `finally` clauses** in a Python try-except structure?
*   A) The `else` clause runs when an exception is caught; the `finally` clause runs only when no exception occurs, serving as the success path for the block
*   B) The `else` clause runs only when no exception was raised in the `try` block; the `finally` clause always runs regardless of whether an exception occurred or was handled
*   C) Both `else` and `finally` are optional aliases for the same behavior — each runs unconditionally after the `try` block completes, whether or not an exception was raised
*   D) The `else` clause catches any exception not handled by a named `except` clause; the `finally` clause re-raises the most recent exception after cleanup code executes
*   **Correct Answer:** B) The `else` clause runs only when no exception was raised in the `try` block; the `finally` clause always runs regardless of whether an exception occurred or was handled.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The roles are reversed — `else` is the success path (no exception), not the caught-exception path; `finally` runs unconditionally, not only on success.
    *   *Why B is correct:* `else` is the right place for code that should execute only when the `try` block succeeded without error; `finally` is guaranteed to run in all cases, even if a `return` or unhandled exception exits the block.
    *   *Why C is incorrect:* `else` and `finally` have distinct, non-interchangeable behaviors; `else` skips on any exception while `finally` never skips — treating them as aliases would silently swallow errors that `else` is designed to avoid executing on.
    *   *Why D is incorrect:* `else` does not catch exceptions — it is skipped entirely if any exception occurs in `try`; exception catching is the job of `except` clauses, not `else`.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
B) python3 -m venv .venv
A) git commit -m 'update'
D) pip install -r requirements.txt
C) pytest
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Exception Handling** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Exception Handling**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Wrap all database calls in a broad `except Exception: pass` block to suppress any SQL errors before they reach the user.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing parameterized queries and prepared statements rather than raw string concatenation mitigates the risk of allowing attackers to execute arbitrary SQL commands on the backend database via input forms.
    * *Why D is incorrect:* Suppressing SQL errors with a broad `except` block hides symptoms but does not prevent the injection — the malicious SQL still executes against the database; parameterized queries stop the attack before the query reaches the database engine.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
