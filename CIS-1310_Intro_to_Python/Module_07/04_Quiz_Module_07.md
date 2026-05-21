# Quiz: Module 07 - Advanced List Operations
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
Which method adds an item to the end of a Python list?
*   A) add()
*   B) append()
*   C) push()
*   D) insert()
*   **Correct Answer:** B) The `.append()` method inserts the passed element at the end of the list.
*   **Distractor Analysis:**
    *   *Why correct:* The `.append()` method inserts the passed element at the end of the list.
    *   add() is for sets. push() is not a list method. insert() requires a specific index.

---

**Question 2**
Which of the following best describes **list copying vs. referencing** in Python?
*   A) Assigning a list to a new variable creates an independent copy; any changes to the new variable leave the original list unchanged
*   B) Assigning a list to a new variable creates a reference to the same object; to get an independent copy you must explicitly use `.copy()`, `list()`, or a full slice `[:]`
*   C) Python automatically deep-copies all nested structures when you use `.copy()`, so changes to inner objects in the copy will never affect the original
*   D) List references only apply to global variables; local variables always receive their own independent copy when assigned from another list
*   **Correct Answer:** B) Assigning a list to a new variable creates a reference to the same object; to get an independent copy you must explicitly use `.copy()`, `list()`, or a full slice `[:]`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Python assignment does not copy by default — `b = a` makes both names point to the same list object in memory, so modifying `b` also changes `a`.
    *   *Why B is correct:* List assignment is reference semantics; `.copy()` creates a shallow copy where the new list is a separate object, though nested mutable objects inside it are still shared.
    *   *Why C is incorrect:* `.copy()` produces a shallow copy, not a deep copy; nested lists or objects inside the list are still shared. Use `copy.deepcopy()` from the `copy` module for full independence.
    *   *Why D is incorrect:* Python's reference semantics apply equally to local and global variables; scope does not change copy vs. reference behavior.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
A) git commit -m 'update'
B) python3 -m venv .venv
D) pip install -r requirements.txt
C) pytest
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Advanced List Operations** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
B) Verify that the index is within the valid range of 0 to len(list)-1.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..


---

**Question 5**
When designing a system for **Advanced List Operations**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Store passwords in a Python list in memory and delete the list variable with `del` immediately after login verification.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* Deleting an in-memory list with `del` removes the reference but does not guarantee memory is wiped immediately, and it does not protect credentials stored in a database; proper hashing at storage time is the correct control.
