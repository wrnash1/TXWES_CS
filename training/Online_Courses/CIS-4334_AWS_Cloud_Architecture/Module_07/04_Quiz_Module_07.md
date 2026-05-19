# Quiz: Module 07 - Amazon EBS & EFS Storage Systems
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Question 1
Which storage service allows you to mount a shared file system on multiple EC2 instances concurrently?

*   A) Amazon EBS
*   B) Amazon S3
*   C) Amazon EFS (Elastic File System)
*   D) Amazon Instance Store

---

### Answer Key
*   **Correct Option:** **C**

---

### Explanation
EFS supports the NFS protocol, allowing thousands of EC2 instances to share access to the same storage space.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    EBS can only mount to a single instance at a time (except special Multi-Attach volumes in same AZ).
