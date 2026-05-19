# Quiz: Module 06 - Design Patterns (Creational)
## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

**Question 1**
What is the primary purpose of the Singleton design pattern?
*   A) To abstract subclass creation
*   B) To ensure a class has only one instance and provides a global point of access to it
*   C) To convert interface structures
*   D) To monitor runtime events
*   **Correct Answer:** B) Singleton restricts class instantiation to a single object, routing all calls through a shared instance reference.
*   **Distractor Analysis:**
    *   *Why correct:* Singleton restricts class instantiation to a single object, routing all calls through a shared instance reference.
    *   Factory Method handles subclass creation without specifying exact types.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Singleton pattern**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
B) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
D) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Singleton pattern**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Singleton pattern**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Singleton pattern**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Singleton pattern**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
C) git commit -m 'update'
D) pip install -r requirements.txt
B) python3 -m venv .venv
A) pytest
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.


---

**Question 4**
While working on **Design Patterns (Creational)** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.


---

**Question 5**
When designing a system for **Design Patterns (Creational)**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..

