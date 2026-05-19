# Quiz: Module 05 - AWS IAM (Identity Access Management)
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Question 1
Which IAM identity should be assigned to an EC2 instance to allow it to securely query an S3 bucket without hardcoded keys?

*   A) IAM User
*   B) IAM Group
*   C) IAM Role
*   D) Root User

---

### Answer Key
*   **Correct Option:** **C**

---

### Explanation
IAM Roles issue temporary security credentials to trusted services like EC2 instances.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Users are for human credentials. Groups hold users.
