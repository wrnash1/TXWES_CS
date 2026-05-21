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
Which of the following best describes **instance variables vs class variables** in Python?
*   A) Instance variables are defined in the class body outside any method and are shared by all objects of the class; class variables are defined inside `__init__` and belong exclusively to one object
*   B) Instance variables are defined by assigning to `self.attribute` inside a method and belong to each individual object; class variables are defined in the class body and shared by all instances until overridden on a specific object
*   C) There is no practical difference between instance and class variables in Python — both are stored in the same namespace and any change made through one instance is automatically reflected in all other instances
*   D) Instance variables are read-only once set by `__init__`; class variables are mutable and serve as the only way to share writable state between methods of the same class
*   **Correct Answer:** B) Instance variables are defined by assigning to `self.attribute` inside a method and belong to each individual object; class variables are defined in the class body and shared by all instances until overridden on a specific object.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The descriptions are swapped — variables assigned in the class body (outside methods) are class variables shared by all instances; variables assigned via `self.x = value` inside a method are instance variables unique to each object.
    *   *Why B is correct:* `self.attribute = value` creates an instance variable in the object's own `__dict__`; a class variable defined at class level is shared until an assignment like `obj.class_var = new_value` creates a shadowing instance variable on that specific object.
    *   *Why C is incorrect:* Instance and class variables occupy different namespaces — assigning `obj.x = 5` creates or updates only that object's instance variable and does not change the class variable or other instances; mutating a mutable class variable in place (e.g., `obj.class_list.append(x)`) is the exception that does affect all instances.
    *   *Why D is incorrect:* Instance variables are not read-only — they can be reassigned at any time with `obj.attribute = new_value`; the read-only constraint would require explicit enforcement via properties or `__slots__`, which are not the default behavior.


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
D) Define a database helper class with a `query(self, sql)` method that accepts raw SQL strings and executes them directly, centralizing all database access in one place.
C) Enable full disk encryption on all client endpoints.
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why D is incorrect:* Centralizing database access in a class is good design practice, but a `query(self, sql)` method that accepts and executes raw SQL strings still passes unsanitized input directly to the database — the injection vulnerability exists in the query string itself, regardless of which class or method executes it.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why A is correct:* Implementing parameterized queries and prepared statements rather than raw string concatenation mitigates the risk of allowing attackers to execute arbitrary SQL commands on the backend database via input forms.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
