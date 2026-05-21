# Quiz: Module 02 - Literals, Operators, and Expressions
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
What is the result of `print(11 // 3)` in Python?
*   A) 3.666
*   B) 3
*   C) 2
*   D) 4
*   **Correct Answer:** B) The double slash `//` operator performs floor division, rounding down to the nearest integer.
*   **Distractor Analysis:**
    *   *Why correct:* The double slash `//` operator performs floor division, rounding down to the nearest integer.
    *   A is the result of single slash `/`. C is the remainder from modulo `%`.

---

**Question 2**
Which of the following best describes Python's **int** data type?
*   A) A whole-number type that can represent arbitrarily large integers without overflow, unlike fixed-size integers in languages like C
*   B) A numeric type that stores values as IEEE 754 double-precision floating-point, introducing small rounding errors for some decimals
*   C) An immutable sequence of digits that must be explicitly converted before arithmetic operations can be performed on it
*   D) A numeric type limited to values between -2,147,483,648 and 2,147,483,647 on all Python platforms
*   **Correct Answer:** A) A whole-number type that can represent arbitrarily large integers without overflow, unlike fixed-size integers in languages like C.
*   **Distractor Analysis:**
    *   *Why A is correct:* Python's `int` is an arbitrary-precision integer; it grows as needed and never overflows, which is a key difference from C/Java integer types.
    *   *Why B is incorrect:* That describes the `float` type, not `int`; floats use IEEE 754 and have rounding issues, while `int` is exact.
    *   *Why C is incorrect:* That describes the `str` type; a string of digits like `"42"` must be converted with `int()`, but the `int` type itself is a numeric value, not a sequence.
    *   *Why D is incorrect:* Python `int` has no fixed-size limit — the range limitation described belongs to 32-bit integers in languages like Java or C.


---

**Question 3**
A systems administrator or developer needs to **install all external project dependencies specified in the requirements manifest**. Which of the following commands is the most appropriate to execute?
D) pytest
A) pip install -r requirements.txt
C) git commit -m 'update'
B) python3 -m venv .venv
*   **Correct Answer:** A) pip install -r requirements.txt
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `pip install -r requirements.txt` command is directly designed to install all external project dependencies specified in the requirements manifest.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Literals, Operators, and Expressions** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Perform explicit type casting (e.g. str() or int()) before executing operations on mixed data types.
C) Ensure the requested key exists in the dictionary, or use the .get() method to return a default value.
D) Reboot the physical machine and wait for services to reload.
A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Correct Answer:** A) Verify that the index is within the valid range of 0 to len(list)-1.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why C is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why D is incorrect:* This action does not resolve the root cause of IndexError.
    * *Why A is correct:* Because The code attempted to access an element of a sequence using an out-of-bounds index. The appropriate fix is to Verify that the index is within the valid range of 0 to len(list)-1..


---

**Question 5**
When designing a system for **Literals, Operators, and Expressions**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement parameterized queries and prepared statements rather than raw string concatenation.
C) Enable full disk encryption on all client endpoints.
A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
D) Log all login attempts including the submitted password to a plain-text audit file for forensic review.
*   **Correct Answer:** A) Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Sensitive Data Exposure.
    * *Why A is correct:* Implementing Encrypt sensitive variables and user passwords using high-entropy hashing algorithms like bcrypt. mitigates the risk of Storing user credentials in plain text, making them vulnerable to database breaches..
    * *Why D is incorrect:* Logging submitted passwords creates a second plain-text credential store and dramatically worsens the exposure risk rather than mitigating it.
