# Quiz: Module 15 - String Algorithms & Trie
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
Which data structure is most suitable for implementing autocomplete systems or dictionary prefix matching?
*   A) AVL Tree
*   B) Hash Table
*   C) Trie (Prefix Tree)
*   D) Max Heap
*   **Correct Answer:** C) Tries store characters along branches, sharing common prefixes which allows rapid string prefix searches.
*   **Distractor Analysis:**
    *   *Why correct:* Tries store characters along branches, sharing common prefixes which allows rapid string prefix searches.
    *   Hash Table can find exact keys, but cannot efficiently match prefixes.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Trie node.**?
C) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
D) The descendant node connected to the left branch of a parent node in a binary tree structure.
B) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Trie node.**.
    * *Why A is correct:* This describes the exact role and function of **Trie node.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Trie node.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Trie node.**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
B) pytest
C) python3 -m venv .venv
D) git commit -m 'update'
A) pip install -r requirements.txt
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.


---

**Question 4**
While working on **String Algorithms & Trie** in a production environment, you encounter a system alert indicating a **KeyError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Verify that the index is within the valid range of 0 to len(list)-1.
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why B is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why D is incorrect:* This action does not resolve the root cause of KeyError.
    * *Why A is correct:* Because The code attempted to access a dictionary key that is not defined in the object. The appropriate fix is to Ensure the requested key exists in the dictionary, or use the .get() method to return a default value..


---

**Question 5**
When designing a system for **String Algorithms & Trie**, you must mitigate the risk of **Allowing attackers to execute arbitrary SQL commands on the backend database via input forms.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
B) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement parameterized queries and prepared statements rather than raw string concatenation.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement parameterized queries and prepared statements rather than raw string concatenation. mitigates the risk of Allowing attackers to execute arbitrary SQL commands on the backend database via input forms..
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Prevention.

