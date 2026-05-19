# Quiz: Module 07 - Heaps & Priority Queues
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
Which array index represents the parent of a node located at index i in a 0-indexed binary heap?
*   A) 2*i + 1
*   B) 2*i + 2
*   C) (i - 1) // 2
*   D) i // 2
*   **Correct Answer:** C) For any 0-indexed element i, its parent is located at index floor((i-1)/2).
*   **Distractor Analysis:**
    *   *Why correct:* For any 0-indexed element i, its parent is located at index floor((i-1)/2).
    *   2*i+1 is left child. 2*i+2 is right child.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **max-heap**?
D) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
B) CSS properties (like block, inline, flex, grid) that determine how an element is rendered and how it behaves relative to surrounding elements.
C) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
A) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
*   **Correct Answer:** A) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **max-heap**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **max-heap**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **max-heap**.
    * *Why A is correct:* This describes the exact role and function of **max-heap**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
D) pytest
A) pip install -r requirements.txt
B) python3 -m venv .venv
C) git commit -m 'update'
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Heaps & Priority Queues** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..


---

**Question 5**
When designing a system for **Heaps & Priority Queues**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

