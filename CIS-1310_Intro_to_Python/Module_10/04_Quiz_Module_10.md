# Quiz: Module 10 - Tuples and Dictionaries
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
Which dictionary method returns both keys and values as tuples?
*   A) keys()
*   B) values()
*   C) items()
*   D) get()
*   **Correct Answer:** C) The `.items()` method returns a view object containing key-value tuples.
*   **Distractor Analysis:**
    *   *Why correct:* The `.items()` method returns a view object containing key-value tuples.
    *   keys() only returns keys. values() only returns values. get() returns the value of a specific key.

---

**Question 2**
Which of the following best describes **Tuple immutability** in Python?
*   A) Tuples are mutable sequences like lists, but they use parentheses instead of brackets; elements can be reassigned or removed using standard index assignment
*   B) Once a tuple is created its elements cannot be changed, added, or removed; any attempt to modify a tuple element raises a TypeError
*   C) Tuples are immutable only when they contain exclusively numeric values; tuples that contain strings or lists can be modified after creation
*   D) Tuples become immutable only after they are assigned to a variable; the literal `(1, 2, 3)` before assignment is a temporary mutable structure
*   **Correct Answer:** B) Once a tuple is created its elements cannot be changed, added, or removed; any attempt to modify a tuple element raises a TypeError.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Tuples are not mutable — `t[0] = 99` on any tuple raises `TypeError: 'tuple' object does not support item assignment`; the parenthesis syntax is a secondary difference, but immutability is the defining characteristic.
    *   *Why B is correct:* Immutability is a permanent, unconditional property of tuples; it applies from the moment the tuple is created regardless of what it contains or whether it is assigned to a variable.
    *   *Why C is incorrect:* Tuple immutability applies to all tuples regardless of their element types; a tuple that contains a list can have the list mutated in place, but the tuple slot itself cannot be reassigned to a different object.
    *   *Why D is incorrect:* Immutability is not tied to assignment; the tuple object itself is immutable as soon as it is constructed, whether or not it is bound to a name.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
D) pytest
C) python3 -m venv .venv
A) git commit -m 'update'
B) pip install -r requirements.txt
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Tuples and Dictionaries** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Verify that the index is within the valid range of 0 to len(list)-1.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Tuples and Dictionaries**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Store query parameters in a tuple and pass the tuple directly into a raw SQL string using Python's `%` string formatting operator.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing parameterized queries and prepared statements rather than raw string concatenation mitigates the risk of allowing attackers to execute arbitrary SQL commands on the backend database via input forms.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* Passing a tuple of values into a raw SQL string with `%` formatting is still string interpolation — the database driver does not treat the values as bound parameters, so SQL injection remains possible; true parameterized queries use the database API's placeholder syntax (e.g., `cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))`).
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
