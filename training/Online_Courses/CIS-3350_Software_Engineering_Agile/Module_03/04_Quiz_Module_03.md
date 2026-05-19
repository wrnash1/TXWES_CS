# Quiz: Module 03 - Clean Code & Refactoring
## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

**Question 1**
What software design principle is violated when you copy and paste identical blocks of code across multiple parts of a program?
*   A) SOLID
*   B) DRY (Don't Repeat Yourself)
*   C) KISS (Keep It Simple, Stupid)
*   D) YAGNI (You Aren't Gonna Need It)
*   **Correct Answer:** B) DRY demands that every piece of knowledge must have a single, unambiguous representation within a system.
*   **Distractor Analysis:**
    *   *Why correct:* DRY demands that every piece of knowledge must have a single, unambiguous representation within a system.
    *   YAGNI cautions against building unused features ahead of time.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **comment overhead.**?
C) The descendant node connected to the left branch of a parent node in a binary tree structure.
D) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
B) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **comment overhead.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **comment overhead.**.
    * *Why A is correct:* This describes the exact role and function of **comment overhead.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **comment overhead.**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
A) python3 -m venv .venv
C) pytest
D) pip install -r requirements.txt
B) git commit -m 'update'
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Clean Code & Refactoring** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Verify that the index is within the valid range of 0 to len(list)-1.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Clean Code & Refactoring**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

