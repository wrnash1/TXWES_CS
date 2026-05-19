# Quiz: Module 10 - Automated Cloud Deployment
## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Question 1
Which deployment strategy maintains two identical environments, routing traffic to one while updating and testing the other?

*   A) Direct Cutover
*   B) Blue-Green Deployment
*   C) Rolling Update
*   D) Shadow Deployment

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Blue-green deployment minimizes downtime and risk; if the new environment (green) fails, routing redirects to the old (blue).

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Canary releases slowly roll out updates to a small subset of users.
