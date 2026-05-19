# Quiz: Module 13 - Terraform Cloud & Registry
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Question 1
Where does state storage and HCL compilation execute when using a VCS-connected Terraform Cloud workspace?

*   A) On the developer's laptop
*   B) In the Terraform Cloud remote runtime environment
*   C) In the target virtual machine
*   D) On the GitHub server

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Terraform Cloud acts as a remote agent, running `plan` and `apply` actions on its own containers, storing state securely.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    It handles operations remotely, freeing developers from local execution requirements.
