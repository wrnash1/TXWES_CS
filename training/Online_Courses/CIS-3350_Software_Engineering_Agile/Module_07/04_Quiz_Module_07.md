# Quiz: Module 07 - Design Patterns (Structural & Behavioral)
## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

**Question 1**
Which behavioral design pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified?
*   A) Adapter Pattern
*   B) Decorator Pattern
*   C) Observer Pattern
*   D) Strategy Pattern
*   **Correct Answer:** C) The Observer pattern enables decoupling pub-sub mechanisms where subjects notify observers without tight linkages.
*   **Distractor Analysis:**
    *   *Why correct:* The Observer pattern enables decoupling pub-sub mechanisms where subjects notify observers without tight linkages.
    *   Adapter links mismatched interfaces. Decorator adds behavior dynamically.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **decoupled components**?
D) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
C) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
B) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **decoupled components**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **decoupled components**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **decoupled components**.
    * *Why A is correct:* This describes the exact role and function of **decoupled components**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
A) pip install -r requirements.txt
D) python3 -m venv .venv
B) pytest
C) git commit -m 'update'
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Design Patterns (Structural & Behavioral)** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Verify that the index is within the valid range of 0 to len(list)-1.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Design Patterns (Structural & Behavioral)**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

