# Quiz: Module 16 - Final Exam Prep & Certification Exam
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
Which of the following is the correct syntax to define a class `Animal` that inherits from a class `LivingThing`?
*   A) class Animal extends LivingThing:
*   B) class Animal(LivingThing):
*   C) class Animal inherits LivingThing:
*   D) def Animal(LivingThing):
*   **Correct Answer:** B) Python uses parentheses after the class name to specify the parent class — `class Animal(LivingThing):`.
*   **Distractor Analysis:**
    *   *Why correct:* Python uses parentheses after the class name to specify the parent class — `class Animal(LivingThing):`.
    *   `extends` and `inherits` are keywords from other languages (Java, Ruby) not used in Python. `def` defines a function, not a class.

---

**Question 2**
Which of the following best describes a key **PCAP exam trap** that a student preparing for the certification should know about regarding Python functions?
*   A) Python functions must always include a `return` statement; omitting it causes a `SyntaxError` at parse time before the program even runs
*   B) A mutable default argument such as `def func(data=[])` is evaluated once at function definition time and shared across all calls that use the default, so appending to `data` inside the function causes it to grow on every call
*   C) Keyword arguments must always be listed before positional arguments in a function call; Python raises a `SyntaxError` if any positional argument appears after a keyword argument in the function definition
*   D) The `global` keyword is required any time a function reads a module-level variable; without it, Python raises a `NameError` when the function tries to access the global name
*   **Correct Answer:** B) A mutable default argument such as `def func(data=[])` is evaluated once at function definition time and shared across all calls that use the default, so appending to `data` inside the function causes it to grow on every call.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A function without a `return` statement (or with a bare `return`) simply returns `None` implicitly — there is no `SyntaxError`; this is valid and commonly used for functions that perform actions rather than compute values.
    *   *Why B is correct:* The mutable default argument trap is one of the most frequently tested PCAP gotchas — the list is created once and reused, so `func()` called three times without an argument will have a data list of length 0, 1, then 2; the fix is to use `None` as the default and create a new list inside the function body.
    *   *Why C is incorrect:* The rule applies to function calls, not definitions — in a call, positional arguments must come before keyword arguments; but in the function definition, parameter order does not have this restriction in the same way, and default parameters must follow non-default ones.
    *   *Why D is incorrect:* A function can read a global variable without the `global` keyword — Python's LEGB rule finds it automatically; `global` is only required when the function needs to rebind (assign to) the global name, not merely read it.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
A) git commit -m 'update'
C) pip install -r requirements.txt
B) python3 -m venv .venv
D) pytest
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Final Exam Prep & Certification Exam** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Verify that the index is within the valid range of 0 to len(list)-1.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..


---

**Question 5**
When designing a system for **Final Exam Prep & Certification Exam**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Store exam scores and user passwords together in the same Python dictionary and protect the entire structure with a module-level password variable.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing high-entropy hashing algorithms like bcrypt mitigates the risk of storing user credentials in plain text, making them vulnerable to database breaches.
    * *Why D is incorrect:* Protecting a dictionary with a module-level variable is security through obscurity — anyone with read access to the source code or memory dump can retrieve the password and the plaintext credentials it guards; proper hashing stores only a one-way hash so that even a full database breach does not expose usable passwords.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
