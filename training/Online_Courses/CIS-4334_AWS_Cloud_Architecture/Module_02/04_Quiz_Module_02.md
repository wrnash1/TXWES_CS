# Quiz: Module 02 - Amazon EC2 Compute Instances
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which storage type is standard for acting as the boot volume for an Amazon EC2 virtual machine?
*   A) Amazon S3
*   B) Amazon EBS (Elastic Block Store)
*   C) Amazon EFS
*   D) AWS Storage Gateway
*   **Correct Answer:** B) EBS provides block-level storage volumes designed for persistent boot partitions and database disks.
*   **Distractor Analysis:**
    *   *Why correct:* EBS provides block-level storage volumes designed for persistent boot partitions and database disks.
    *   S3 is object storage and cannot mount directly as boot volumes.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Amazon Machine Images (AMIs)**?
D) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
C) The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disaster.
B) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon Machine Images (AMIs)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon Machine Images (AMIs)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon Machine Images (AMIs)**.
    * *Why A is correct:* This describes the exact role and function of **Amazon Machine Images (AMIs)**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
B) aws s3 sync local_dir s3://my-bucket
A) terraform apply
C) kubectl get pods -n production
D) gcloud compute instances list
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Amazon EC2 Compute Instances** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..


---

**Question 5**
When designing a system for **Amazon EC2 Compute Instances**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
C) Enable full disk encryption on all client endpoints.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

