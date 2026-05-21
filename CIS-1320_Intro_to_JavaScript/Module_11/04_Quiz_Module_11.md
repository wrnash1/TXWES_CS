# Quiz: Module 11 - DOM Manipulation & Styling
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
What is the recommended method to add a new CSS class to an element without overwriting existing classes?
*   A) element.className = 'new-class'
*   B) element.classList.add('new-class')
*   C) element.setAttribute('class', 'new-class')
*   D) element.style.class = 'new-class'
*   **Correct Answer:** B) The `classList.add()` method appends the new class, preserving existing classes.
*   **Distractor Analysis:**
    *   *Why correct:* The `classList.add()` method appends the new class, preserving existing classes.
    *   className assignment and setAttribute overwrite the entire class attribute. style.class is invalid syntax.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **createElement**?
C) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
B) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
D) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **createElement**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **createElement**.
    * *Why A is correct:* This describes the exact role and function of **createElement**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **createElement**.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
B) pip install -r requirements.txt
A) git commit -m 'update'
D) python3 -m venv .venv
C) pytest
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **DOM Manipulation & Styling** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Verify that the index is within the valid range of 0 to len(list)-1.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **DOM Manipulation & Styling**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

