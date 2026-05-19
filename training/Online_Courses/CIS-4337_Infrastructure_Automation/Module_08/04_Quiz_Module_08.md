# Quiz: Module 08 - Data Sources & Dynamic Blocks
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Question 1
Which block type allows you to query API data from a provider without creating a new resource?

*   A) resource
*   B) data
*   C) variable
*   D) locals

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Data sources (`data` blocks) read configurations directly from target APIs (e.g. searching for AMI lists).

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    resource blocks declare objects that Terraform should manage/create.
