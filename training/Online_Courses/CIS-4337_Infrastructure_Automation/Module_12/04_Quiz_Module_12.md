# Quiz: Module 12 - Drift Management & Importing
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Question 1
Which command reads real-world resource details and registers them inside your local state file?

*   A) terraform apply
*   B) terraform import
*   C) terraform plan
*   D) terraform state push

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
`terraform import` reads the target ID and populates it inside your state. You must manually write the matching HCL code.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    import does not generate HCL code; it only writes state.
