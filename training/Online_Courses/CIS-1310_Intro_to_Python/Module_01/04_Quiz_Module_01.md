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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **indentation rules.**?
B) The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disaster.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
D) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **indentation rules.**.
    * *Why A is correct:* This describes the exact role and function of **indentation rules.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **indentation rules.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **indentation rules.**.


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
While working on **Python Basics & Local Environment** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Verify that the index is within the valid range of 0 to len(list)-1.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Python Basics & Local Environment**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

