# Quiz: Module 06 - State Locking & Backends
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Question 1
Why is state locking critical in enterprise team environments?

*   A) To encrypt variables
*   B) To prevent concurrent runs from corrupting the state file
*   C) To speed up provisioning
*   D) None of the above

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
State locking ensures that if two users run `apply` at the same time, one is queued to avoid overwriting or corruption.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Locks do not accelerate deployments or encrypt variables.
