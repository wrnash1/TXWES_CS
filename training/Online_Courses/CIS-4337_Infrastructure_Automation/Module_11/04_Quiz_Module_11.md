# Quiz: Module 11 - Workspaces & Multi-Env
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Question 1
Which environment variable/parameter references the name of the current active Terraform workspace?

*   A) var.workspace
*   B) terraform.workspace
*   C) local.workspace
*   D) active.workspace

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
The `terraform.workspace` path returns the current active workspace name (e.g. 'prod' or 'dev').

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    It is a built-in object, not a variable prefix.
