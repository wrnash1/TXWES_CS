# Quiz: Module 06 - AVL Trees & Red-Black Trees
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
What is the maximum height of an AVL tree containing N nodes?
*   A) O(1)
*   B) O(log N)
*   C) O(N)
*   D) O(N^2)
*   **Correct Answer:** B) AVL trees guarantee a logarithmic height by maintaining a strict balance factor difference of at most 1.
*   **Distractor Analysis:**
    *   *Why correct:* AVL trees guarantee a logarithmic height by maintaining a strict balance factor difference of at most 1.
    *   O(N) is the height of an unbalanced degenerate tree (linked list).

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Self-balancing tree**?
B) The process of restructuring existing computer code without changing its external behavior to improve readability and reduce complexity.
A) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
C) An undesired resource consumption where a program fails to release allocated memory that is no longer needed.
D) The descendant node connected to the right branch of a parent node in a binary tree structure.
*   **Correct Answer:** A) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Self-balancing tree**.
    * *Why A is correct:* This describes the exact role and function of **Self-balancing tree**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Self-balancing tree**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Self-balancing tree**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
B) pytest
A) pip install -r requirements.txt
D) git commit -m 'update'
C) python3 -m venv .venv
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **AVL Trees & Red-Black Trees** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Verify that the index is within the valid range of 0 to len(list)-1.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **AVL Trees & Red-Black Trees**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

