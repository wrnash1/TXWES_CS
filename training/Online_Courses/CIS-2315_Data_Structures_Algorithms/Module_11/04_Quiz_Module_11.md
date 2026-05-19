# Quiz: Module 11 - Dijkstra's Shortest Path
## Course: CIS-2315_Data_Structures_Algorithms (Technical Interview Readiness (LeetCode / HackerRank))

---

**Question 1**
Why is Dijkstra's algorithm unable to guarantee correct shortest paths in graphs with negative edge weights?
*   A) It uses a queue instead of stack
*   B) Once a vertex is visited/relaxed, the algorithm assumes its shortest path is permanently solved
*   C) It only works on binary trees
*   D) It runs in O(N^3) time
*   **Correct Answer:** B) Dijkstra's greedy choice assumes that paths can only increase in cost; a negative edge can invalidate earlier evaluations.
*   **Distractor Analysis:**
    *   *Why correct:* Dijkstra's greedy choice assumes that paths can only increase in cost; a negative edge can invalidate earlier evaluations.
    *   Bellman-Ford is used for graphs with negative weights because it repeatedly relaxes all edges.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **priority queue**?
D) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
B) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
C) CSS properties (like block, inline, flex, grid) that determine how an element is rendered and how it behaves relative to surrounding elements.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **priority queue**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **priority queue**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **priority queue**.
    * *Why A is correct:* This describes the exact role and function of **priority queue**.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
B) python3 -m venv .venv
D) pip install -r requirements.txt
C) git commit -m 'update'
A) pytest
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.


---

**Question 4**
While working on **Dijkstra's Shortest Path** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **Dijkstra's Shortest Path**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

