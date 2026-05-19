# Quiz: Module 15 - Terraform Security & Secrets
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Question 1
Which HCL variable attribute prevents its value from being printed to the console stdout during apply runs?

*   A) write = false
*   B) sensitive = true
*   C) hidden = true
*   D) secret = true

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Declaring `sensitive = true` instructs Terraform to mask the values in logs and console outputs.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    The value is still written to the state file in plain text, making backend security critical.
