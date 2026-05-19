# Quiz: Module 08 - Hash Tables & Hash Collisions
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
What is the average-case time complexity of searching for a key in a well-distributed Hash Table?
*   A) O(1)
*   B) O(log N)
*   C) O(N)
*   D) O(N log N)
*   **Correct Answer:** A) If the hash function distributes keys evenly, finding a key via constant hash mapping takes O(1) time.
*   **Distractor Analysis:**
    *   *Why correct:* If the hash function distributes keys evenly, finding a key via constant hash mapping takes O(1) time.
    *   O(N) is the worst-case hash table lookup (when all keys collide into a single chain).

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **chaining**?
B) The process of restructuring existing computer code without changing its external behavior to improve readability and reduce complexity.
C) A key object-oriented programming concept where a child class derives attributes and behaviors from a parent class.
D) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **chaining**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **chaining**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **chaining**.
    * *Why A is correct:* This describes the exact role and function of **chaining**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
B) git commit -m 'update'
A) pip install -r requirements.txt
C) pytest
D) python3 -m venv .venv
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Hash Tables & Hash Collisions** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Verify that the index is within the valid range of 0 to len(list)-1.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Hash Tables & Hash Collisions**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
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

