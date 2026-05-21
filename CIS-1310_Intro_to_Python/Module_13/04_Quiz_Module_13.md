# Quiz: Module 13 - Modules and Packages
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
What does `import math` do?
*   A) Copies math functions directly into your file
*   B) Imports the math module namespace
*   C) Exposes all functions without the math prefix
*   D) Compiles the math module
*   **Correct Answer:** B) It imports the module, keeping its functions under the `math.` namespace to avoid name collisions.
*   **Distractor Analysis:**
    *   *Why correct:* It imports the module, keeping its functions under the `math.` namespace to avoid name collisions.
    *   from math import * exposes functions without prefix, which can overwrite existing names.

---

**Question 2**
Which of the following best describes **creating custom modules** in Python?
*   A) A custom module must be registered with pip and installed into the virtual environment before it can be imported; Python does not search the current directory for unregistered modules
*   B) Any `.py` file saved in the same directory as the importing script (or on `sys.path`) can be imported as a module; the `__name__` variable equals `"__main__"` when run directly and the module name when imported
*   C) A custom module must contain a class with the same name as the file; Python raises `ImportError` if no matching class is found when the module is imported
*   D) Importing a custom module re-executes all its top-level code every time it is imported in the same program, so module-level side effects occur once per import statement
*   **Correct Answer:** B) Any `.py` file saved in the same directory as the importing script (or on `sys.path`) can be imported as a module; the `__name__` variable equals `"__main__"` when run directly and the module name when imported.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Python searches `sys.path` automatically, which includes the current directory by default; local `.py` files are importable without pip registration — pip is only needed for third-party packages not already on the path.
    *   *Why B is correct:* Any `.py` file is a valid module; the `__name__ == "__main__"` guard is the standard pattern to prevent test or script code from running when the file is used as a library by another script.
    *   *Why C is incorrect:* A module does not need to contain any class at all — it can contain functions, constants, or any Python code; there is no requirement for a class matching the filename.
    *   *Why D is incorrect:* Python caches imported modules in `sys.modules` and executes their top-level code only once per interpreter session, regardless of how many times `import` is called — subsequent imports return the cached module object.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
B) pytest
C) git commit -m 'update'
D) python3 -m venv .venv
A) pip install -r requirements.txt
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.


---

**Question 4**
While working on **Modules and Packages** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
C) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Modules and Packages**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Use `from config import *` to load database credentials into module-level variables so all modules share a single connection string.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing parameterized queries and prepared statements rather than raw string concatenation mitigates the risk of allowing attackers to execute arbitrary SQL commands on the backend database via input forms.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* Sharing database credentials via a wildcard module import makes them globally accessible throughout the application, increasing the attack surface; it does not prevent SQL injection and is itself a security anti-pattern that exposes credentials to any module that performs the import.
