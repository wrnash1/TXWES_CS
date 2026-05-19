# Quiz: Module 13 - Modules and Packages
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

**Question 1**
What does `import math` do?
*   A) Copies math functions directly into your file
*   B) Imports the math module namespace
*   C) Exposes all functions without the math prefix
*   D) Compiles the math module
*   **Correct Answer:** B) It imports the module, keeping its functions under the `math.` namespace to avoid name collisions.
*   **Distractor Analysis:**
    *   *Why correct:* It imports the module, keeping its functions under the `math.` namespace to avoid name collisions.
    *   from math import * exposes functions without prefix, which can overwrite existing names.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **namespaces (import math vs from math import *)**?
D) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
C) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
B) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within programming operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **namespaces (import math vs from math import *)**.
    * *Why A is correct:* This describes the exact role and function of **namespaces (import math vs from math import *)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **namespaces (import math vs from math import *)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **namespaces (import math vs from math import *)**.


---

**Question 3**
A systems administrator or developer needs to **create a sandboxed Python virtual environment to manage dependencies locally**. Which of the following commands is the most appropriate to execute?
B) git commit -m 'update'
D) pytest
C) pip install -r requirements.txt
A) python3 -m venv .venv
*   **Correct Answer:** A) python3 -m venv .venv
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `python3 -m venv .venv` command is directly designed to create a sandboxed Python virtual environment to manage dependencies locally.


---

**Question 4**
While working on **Modules and Packages** in a production environment, you encounter a system alert indicating a **IndexError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **Modules and Packages**, you must mitigate the risk of **Storing user credentials in plain text, making them vulnerable to database breaches.**. Which of the following security configurations or controls represents the best practice to implement?
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

