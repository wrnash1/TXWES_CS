# Quiz: Module 12 - Exception Handling
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Question 1
Which block runs regardless of whether an exception was raised or not?

*   A) except
*   B) else
*   C) finally
*   D) try

---

### Answer Key
*   **Correct Option:** **C**

---

### Explanation
The `finally` block is guaranteed to execute at the end of the try-except chain, making it perfect for cleanup.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    except only runs if an exception occurs. else only runs if no exception occurs.
