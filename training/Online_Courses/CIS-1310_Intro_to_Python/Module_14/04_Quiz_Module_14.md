# Quiz: Module 14 - Object-Oriented Programming (OOP) Basics
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
What is the purpose of the `self` parameter in Python class methods?
*   A) It represents the class definition
*   B) It refers to the specific object instance
*   C) It is a global variable
*   D) It is a keyword that cannot be renamed
*   **Correct Answer:** B) `self` represents the specific instance of the object being operated on, allowing access to instance attributes.
*   **Distractor Analysis:**
    *   *Why correct:* `self` represents the specific instance of the object being operated on, allowing access to instance attributes.
    *   It represents the instance, not the class. Technically it is a naming convention, not a reserved keyword.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **instance variables vs class variables**?
C) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
B) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
D) The practice of hiding the internal state and representation of an object, exposing access only through public methods.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **instance variables vs class variables**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **instance variables vs class variables**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **instance variables vs class variables**.
    * *Why A is correct:* This describes the exact role and function of **instance variables vs class variables**.


---

**Question 3**
A systems administrator or developer needs to **record staged code modifications into the repository version history**. Which of the following commands is the most appropriate to execute?
B) pytest
C) python3 -m venv .venv
A) git commit -m 'update'
D) pip install -r requirements.txt
*   **Correct Answer:** A) git commit -m 'update'
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git commit -m 'update'` command is directly designed to record staged code modifications into the repository version history.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Object-Oriented Programming (OOP) Basics** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **Object-Oriented Programming (OOP) Basics**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
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

