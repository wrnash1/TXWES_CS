# Quiz: Module 06 - RESTful API Principles
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which HTTP status code class indicates a server-side processing error occurred?
*   A) 2xx
*   B) 3xx
*   C) 4xx
*   D) 5xx
*   **Correct Answer:** D) 5xx status codes (e.g. 500 Internal Server Error) represent backend processing failures.
*   **Distractor Analysis:**
    *   *Why correct:* 5xx status codes (e.g. 500 Internal Server Error) represent backend processing failures.
    *   4xx is for client-side input errors (e.g. 404 Not Found).

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **endpoints**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
D) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
B) A two-dimensional CSS layout system that allows developers to design complex grid-based user interfaces with rows and columns, offering precise control over alignment.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **endpoints**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **endpoints**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **endpoints**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **endpoints**.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
A) pip install -r requirements.txt
C) python3 -m venv .venv
D) git commit -m 'update'
B) pytest
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **RESTful API Principles** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
D) Reboot the physical machine and wait for services to reload.
A) Verify that the index is within the valid range of 0 to len(list)-1.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.


---

**Question 5**
When designing a system for **RESTful API Principles**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.

