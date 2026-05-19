# Quiz: Module 13 - Modules and Packages
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Question 1
What does `import math` do?

*   A) Copies math functions directly into your file
*   B) Imports the math module namespace
*   C) Exposes all functions without the math prefix
*   D) Compiles the math module

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
It imports the module, keeping its functions under the `math.` namespace to avoid name collisions.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    from math import * exposes functions without prefix, which can overwrite existing names.
