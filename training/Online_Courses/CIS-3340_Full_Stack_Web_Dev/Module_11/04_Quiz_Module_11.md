# Quiz: Module 11 - Frontend Frameworks (React)
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
How does React's Virtual DOM improve application rendering performance?
*   A) It updates all page elements on every interaction
*   B) It compiles javascript to machine code
*   C) It computes changes in memory first and only updates altered elements in the real DOM
*   D) It bypasses CSS parsing
*   **Correct Answer:** C) React compares changes in a virtual DOM tree (reconciliation) and updates only the necessary elements, avoiding expensive global repaints.
*   **Distractor Analysis:**
    *   *Why correct:* React compares changes in a virtual DOM tree (reconciliation) and updates only the necessary elements, avoiding expensive global repaints.
    *   Bypassing calculations or writing machine code is not how React operates.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Single Page Application (SPA)**?
B) The process of restructuring existing computer code without changing its external behavior to improve readability and reduce complexity.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
D) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Single Page Application (SPA)**.
    * *Why A is correct:* This describes the exact role and function of **Single Page Application (SPA)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Single Page Application (SPA)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Single Page Application (SPA)**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
A) python3 -m venv .venv
D) pip install -r requirements.txt
C) git commit -m 'update'
B) pytest
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Frontend Frameworks (React)** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
B) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Frontend Frameworks (React)**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..

