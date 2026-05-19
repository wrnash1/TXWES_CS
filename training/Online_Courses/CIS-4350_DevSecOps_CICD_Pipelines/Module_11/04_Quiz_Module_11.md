# Quiz: Module 11 - Secret Management in Pipelines
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Question 1
Why should API keys and database passwords never be hardcoded in Git source files?

*   A) Git cannot compile files with secrets
*   B) Once pushed, keys are saved in history logs and can be exposed to unauthorized parties
*   C) Secrets slow down code execution
*   D) Secrets cause network routing loops

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Git histories are persistent; exposing keys allows attackers to scrape repositories and compromise systems.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    It is a severe security risk, not a compilation or speed constraint.
