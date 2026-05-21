# Quiz: Module 09 - Scopes, Namespaces, and Recursion
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
What keyword is required to modify a variable defined at the module level from inside a function?
*   A) nonlocal
*   B) global
*   C) static
*   D) public
*   **Correct Answer:** B) The `global` keyword declares that a variable inside the function refers to the module-level namespace.
*   **Distractor Analysis:**
    *   *Why correct:* The `global` keyword declares that a variable inside the function refers to the module-level namespace.
    *   nonlocal is for nested/closure scopes. static and public are not used in Python variable scoping.

---

**Question 2**
Which of the following best describes **Global vs local scope** in Python?
*   A) Every name in a Python program belongs to exactly one namespace; once defined globally, a name is permanently immutable and cannot be rebound inside any function
*   B) A variable assigned inside a function is local to that function by default and shadows any global variable with the same name; the global variable remains unchanged unless the `global` keyword is used
*   C) Python places all variables — whether defined inside or outside functions — into a single shared namespace, so any assignment anywhere in the module is immediately visible everywhere else
*   D) The local scope of a function persists after the function returns, so local variables can be read by other functions that run afterward in the same script
*   **Correct Answer:** B) A variable assigned inside a function is local to that function by default and shadows any global variable with the same name; the global variable remains unchanged unless the `global` keyword is used.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Global names can be rebound at module level at any point, and the `global` keyword inside a function allows rebinding them from within a function; immutability is a property of certain data types, not of variable names.
    *   *Why B is correct:* Python's LEGB rule searches Local before Global; assigning to a name inside a function creates a local binding that shadows the global without affecting it, unless `global` is explicitly declared.
    *   *Why C is incorrect:* Python does not use a single flat namespace — each function call creates its own local namespace, and names assigned there are not visible at module level or in other functions.
    *   *Why D is incorrect:* A function's local namespace is destroyed when the function returns; local variables do not persist and are not accessible after the call completes.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
C) pip install -r requirements.txt
D) git commit -m 'update'
B) pytest
A) python3 -m venv .venv
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.


---

**Question 4**
While working on **Scopes, Namespaces, and Recursion** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Verify that the index is within the valid range of 0 to len(list)-1.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Scopes, Namespaces, and Recursion**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Declare database connection strings as global variables at module level so all functions can reuse a single connection object.
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* Sharing a connection object via a global variable is a scope-management pattern, not a security control; it does not prevent SQL injection because the query strings themselves are still vulnerable to injection if built by string concatenation.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing parameterized queries and prepared statements rather than raw string concatenation mitigates the risk of allowing attackers to execute arbitrary SQL commands on the backend database via input forms.
