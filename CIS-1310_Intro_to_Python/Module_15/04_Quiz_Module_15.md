# Quiz: Module 15 - Advanced OOP: Inheritance and Polymorphism
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
How do you call a method in the parent class from a child class?
*   A) parent.method()
*   B) super().method()
*   C) base.method()
*   D) self.method()
*   **Correct Answer:** B) The `super()` function returns a proxy object that delegates method calls to a parent or sibling class.
*   **Distractor Analysis:**
    *   *Why correct:* The `super()` function returns a proxy object that delegates method calls to a parent or sibling class.
    *   parent and base are not built-in functions or keywords for resolving parent class references.

---

**Question 2**
Which of the following best describes the **`super()` function** in Python?
*   A) `super()` returns the parent class object itself, allowing you to call any class method or access any class variable defined in the parent without needing an instance
*   B) `super()` returns a proxy that delegates attribute lookups to the next class in the Method Resolution Order, most commonly used in `__init__` to call the parent's initializer without hardcoding the parent class name
*   C) `super()` is only valid inside `__init__` methods; using it in any other method raises a `TypeError` because Python cannot determine the MRO outside of constructors
*   D) `super()` always calls the method from the immediate parent class regardless of the inheritance hierarchy, making it equivalent to writing `ParentClass.method(self)` explicitly
*   **Correct Answer:** B) `super()` returns a proxy that delegates attribute lookups to the next class in the Method Resolution Order, most commonly used in `__init__` to call the parent's initializer without hardcoding the parent class name.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `super()` does not return the parent class object — it returns a proxy that forwards calls following the MRO; it also requires an instance context (or explicit arguments in Python 2), not class-level access.
    *   *Why B is correct:* `super()` follows the MRO, making it safe for multiple inheritance where hardcoding the parent name would skip sibling classes in the chain; calling `super().__init__(...)` ensures the full initialization chain runs correctly.
    *   *Why C is incorrect:* `super()` can be used in any instance method, not just `__init__` — it is commonly used in overridden methods like `__str__`, `save()`, or any other method where the child wants to extend rather than fully replace the parent's behavior.
    *   *Why D is incorrect:* In multiple inheritance, `super()` does not necessarily call the immediate parent — it calls the next class in the MRO, which may be a sibling class before reaching the declared parent; this is the key difference from `ParentClass.method(self)`.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
B) git commit -m 'update'
C) pytest
A) pip install -r requirements.txt
D) python3 -m venv .venv
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Advanced OOP: Inheritance and Polymorphism** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
A) Verify that the index is within the valid range of 0 to len(list)-1.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Advanced OOP: Inheritance and Polymorphism**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Create a base `Repository` class with a `find_by_id(self, id)` method that builds SQL using f-string interpolation, and have all model classes inherit this behavior.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing parameterized queries and prepared statements rather than raw string concatenation mitigates the risk of allowing attackers to execute arbitrary SQL commands on the backend database via input forms.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* Inheriting an f-string SQL builder propagates the injection vulnerability to every subclass — using inheritance to share unsafe query construction makes the problem worse, not better; the base class itself must use parameterized queries for all subclasses to be safe.
