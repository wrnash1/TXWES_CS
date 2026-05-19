# Quiz: Module 09 - Graph Representations
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
Which representation is most memory-efficient for a sparse graph with N vertices and few edges?
*   A) Adjacency Matrix
*   B) Adjacency List
*   C) Edge List
*   D) Hash Matrix
*   **Correct Answer:** B) Adjacency lists only store actual links, bypassing the O(N^2) memory footprint of adjacency matrices.
*   **Distractor Analysis:**
    *   *Why correct:* Adjacency lists only store actual links, bypassing the O(N^2) memory footprint of adjacency matrices.
    *   Adjacency matrix always uses O(V^2) memory space regardless of edge density.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **adjacency list**?
D) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
B) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **adjacency list**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **adjacency list**.
    * *Why A is correct:* This describes the exact role and function of **adjacency list**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **adjacency list**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
C) git commit -m 'update'
B) pytest
A) python3 -m venv .venv
D) pip install -r requirements.txt
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Graph Representations** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
C) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Graph Representations**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
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

