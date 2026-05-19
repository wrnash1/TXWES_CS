# Quiz: Module 03 - Embedded Programming C/C++
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Question 1
Why is static memory allocation preferred over dynamic allocation (malloc) in high-reliability embedded systems?

*   A) Static memory runs slower
*   B) Dynamic allocation risks heap fragmentation and runtime memory exhaustion (out-of-memory crashes)
*   C) C does not support dynamic allocation
*   D) Pointers are not allowed

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Microcontrollers have tiny RAM capacities; heap fragmentation can trigger unpredictable system crashes during long-term runs.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Dynamic memory is supported in C but highly restricted in embedded code.
