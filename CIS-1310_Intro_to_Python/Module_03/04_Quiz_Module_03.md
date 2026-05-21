# Quiz: Module 03 - Variables and Basic I/O
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
What is the return type of the `input()` function?
*   A) int
*   B) float
*   C) string
*   D) boolean
*   **Correct Answer:** C) `input()` always returns a string. You must explicitly cast it if you need a numeric value.
*   **Distractor Analysis:**
    *   *Why correct:* `input()` always returns a string. You must explicitly cast it if you need a numeric value.
    *   Dynamic typing does not automatically convert text input to integers or floats.

---

**Question 2**
Which of the following best describes **type casting** in Python?
*   A) The automatic conversion Python performs when assigning a value of one type to a variable previously holding a different type
*   B) The explicit conversion of a value from one data type to another using a constructor function such as `int()`, `float()`, or `str()`
*   C) A compiler optimization that replaces slow dynamic type checks with faster static type inferences at runtime
*   D) The process of checking whether a variable name follows Python's identifier rules before the interpreter binds the name to a value
*   **Correct Answer:** B) The explicit conversion of a value from one data type to another using a constructor function such as `int()`, `float()`, or `str()`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Python does not automatically coerce types on assignment — you must perform explicit conversions yourself; implicit conversion happens only in a few narrow arithmetic contexts.
    *   *Why B is correct:* Type casting means manually calling `int()`, `float()`, `str()`, etc. to convert a value to the desired type before using it in an operation.
    *   *Why C is incorrect:* Python has no ahead-of-time compiler that replaces type checks; it is an interpreted, dynamically typed language and type information is managed at runtime.
    *   *Why D is incorrect:* Checking identifier rules is part of the parsing/lexing step, not type casting; those are two separate concerns in Python's execution model.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
C) python3 -m venv .venv
A) pip install -r requirements.txt
B) pytest
D) git commit -m 'update'
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Variables and Basic I/O** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
A) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Variables and Basic I/O**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Validate that user input contains only alphanumeric characters and raise a ValueError for anything else.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* Input allowlisting can reduce the attack surface but is an incomplete control — parameterized queries are the definitive defense because they prevent SQL injection regardless of what characters are in the input.
