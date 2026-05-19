# Quiz: Module 09 - Cryptography in Constrained Devices
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Question 1
Why is symmetric cryptography (like AES) preferred over asymmetric cryptography (like RSA) for securing sensor data transmissions directly on microcontrollers?

*   A) Symmetric crypto does not require keys
*   B) Asymmetric math is highly resource-intensive and computationally expensive for low-power CPUs
*   C) Symmetric crypto is not secure
*   D) Asymmetric is only allowed on servers

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
AES utilizes lightweight bitwise operations that execute quickly on small chips with minimal RAM and power.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Both use keys, and asymmetric can run on small devices but consumes significant battery.
