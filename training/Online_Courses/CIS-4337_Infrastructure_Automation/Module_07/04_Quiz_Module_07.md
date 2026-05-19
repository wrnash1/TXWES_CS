# Quiz: Module 07 - Provisioners & Local Exec
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Question 1
Which provisioner executes a command on the machine running the Terraform CLI?

*   A) remote-exec
*   B) local-exec
*   C) host-exec
*   D) system-exec

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
The `local-exec` provisioner runs commands locally on the operator's shell system.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    remote-exec runs command inside the deployed target virtual machine.
