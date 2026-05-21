# Quiz: Module 04 - Control Flow - Conditional Statements
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
Which keyword is used to represent 'else if' in Python?
*   A) elseif
*   B) else if
*   C) elif
*   D) otherwise
*   **Correct Answer:** C) Python uses `elif` as the syntax-defined keyword for secondary conditional branches.
*   **Distractor Analysis:**
    *   *Why correct:* Python uses `elif` as the syntax-defined keyword for secondary conditional branches.
    *   elseif and else if are syntax errors in Python. otherwise is not a Python keyword.

---

**Question 2**
Which of the following best describes Python's **if-elif-else** structure?
*   A) A loop construct that repeatedly tests a condition and executes a block until the condition becomes False, then runs the else clause once
*   B) A branching construct that evaluates conditions top-to-bottom and executes only the first block whose condition is truthy, skipping all remaining branches
*   C) A pattern-matching construct that tests a value against multiple literal patterns and executes the matching case, similar to `switch` in other languages
*   D) A construct that evaluates all conditions in parallel and executes every block whose condition is True, allowing multiple branches to run in the same pass
*   **Correct Answer:** B) A branching construct that evaluates conditions top-to-bottom and executes only the first block whose condition is truthy, skipping all remaining branches.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes a `while` loop with an `else` clause, not an `if-elif-else` conditional; `while-else` is a separate Python construct.
    *   *Why B is correct:* `if-elif-else` checks conditions in order and stops at the first match — exactly one branch executes (or none if all conditions are False and there is no `else`).
    *   *Why C is incorrect:* Python's structural pattern matching (`match-case`) was added in Python 3.10 as a separate construct; `if-elif-else` is not pattern matching.
    *   *Why D is incorrect:* Only one branch of `if-elif-else` ever executes per evaluation; if you need multiple blocks to run you would use separate `if` statements, not `elif`.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
D) python3 -m venv .venv
C) pytest
B) pip install -r requirements.txt
A) git commit -m 'update'
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.


---

**Question 4**
While working on **Control Flow - Conditional Statements** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..


---

**Question 5**
When designing a system for **Control Flow - Conditional Statements**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
D) Use if-elif-else logic in Python to reject input strings that contain SQL keywords like SELECT or DROP.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* Keyword blocklisting with conditional logic is an unreliable defense; attackers use obfuscation techniques (e.g., case variation, encoding) to bypass keyword filters, whereas parameterized queries eliminate the injection vector entirely.
