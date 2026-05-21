# Quiz: Module 06 - Bitwise Operations and Lists
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
How do you access the last element of a list named `my_list`?
*   A) my_list[0]
*   B) my_list[len(my_list)]
*   C) my_list[-1]
*   D) my_list[last]
*   **Correct Answer:** C) Negative indexing starts from the end of the list. `my_list[-1]` retrieves the last element.
*   **Distractor Analysis:**
    *   *Why correct:* Negative indexing starts from the end of the list. `my_list[-1]` retrieves the last element.
    *   A is the first element. B causes an IndexError because indices are 0-indexed. D is undefined.

---

**Question 2**
Which of the following best describes the **Bitwise AND** operator (`&`) in Python?
*   A) An operator that compares each corresponding bit of two integers and returns 1 only where both bits are 1, performing the operation simultaneously on all bit positions
*   B) An operator that returns True if both operands are truthy values, using short-circuit evaluation to skip the second operand when the first is False
*   C) An operator that combines two integers by setting each output bit to 1 wherever at least one of the corresponding input bits is 1
*   D) An operator that flips all bits of an integer, converting each 0 to 1 and each 1 to 0, equivalent to computing -(n+1) for a signed integer
*   **Correct Answer:** A) An operator that compares each corresponding bit of two integers and returns 1 only where both bits are 1, performing the operation simultaneously on all bit positions.
*   **Distractor Analysis:**
    *   *Why A is correct:* `&` is the bitwise AND — it operates on individual bits and outputs 1 only for positions where both operands have a 1 bit; `5 & 3` (binary `101 & 011`) yields `1` (binary `001`).
    *   *Why B is incorrect:* That describes the logical `and` keyword, which operates on whole truth values and short-circuits; bitwise `&` does not short-circuit and always evaluates both operands fully.
    *   *Why C is incorrect:* That describes the bitwise OR operator (`|`), not AND; OR outputs 1 wherever either operand has a 1 bit.
    *   *Why D is incorrect:* That describes the bitwise NOT operator (`~`), which inverts all bits; it is a unary operator applied to a single integer, not a binary operator combining two integers.


---

**Question 3**
A systems administrator or developer needs to **run the automated unit testing suite to verify system functionality**. Which of the following commands is the most appropriate to execute?
A) pytest
B) git commit -m 'update'
C) pip install -r requirements.txt
D) python3 -m venv .venv
*   **Correct Answer:** A) pytest
*   **Distractor Analysis:**
    * *Why A is correct:* The `pytest` command is directly designed to run the automated unit testing suite to verify system functionality.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Bitwise Operations and Lists** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
C) Verify that the index is within the valid range of 0 to len(list)-1.
D) Reboot the physical machine and wait for services to reload.
B) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
*   **Correct Answer:** A) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
*   **Distractor Analysis:**
    * *Why A is correct:* Because An operation or function was applied to an object of an inappropriate data type. The appropriate fix is to Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types..
    * *Why C is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why D is incorrect:* This action does not resolve the root cause of TypeError.
    * *Why B is incorrect:* This action does not resolve the root cause of TypeError.


---

**Question 5**
When designing a system for **Bitwise Operations and Lists**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
C) Enable full disk encryption on all client endpoints.
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
D) Use a list to store hashed tokens in memory and clear the list after each session ends.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why D is incorrect:* Clearing in-memory lists mitigates exposure during a session but does not protect credentials at rest in the database; hashing with bcrypt before storage is the required control.
