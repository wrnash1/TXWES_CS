# Quiz: Module 10 - Secure Boot & OTA updates
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Question 1
How does Secure Boot protect an embedded IoT device?

*   A) It boots the system faster
*   B) It cryptographically verifies the signature of the bootloader and firmware before executing, preventing unsigned code runs
*   C) It disables the power button
*   D) It deletes system database logs

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Secure Boot checks digital signatures against keys burned into the hardware's root-of-trust, blocking tampered firmware.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    It is a verification check, not a boot booster.
