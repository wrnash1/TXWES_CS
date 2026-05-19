# Quiz: Module 08 - Microsoft Entra ID (Azure AD) Basics
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What is the primary function of Microsoft Entra ID?
*   A) Network routing and DNS
*   B) Identity and Access Management
*   C) Database storage
*   D) Host virtualization
*   **Correct Answer:** B) Entra ID (formerly Azure Active Directory) handles authentication and access management for cloud identities.
*   **Distractor Analysis:**
    *   *Why correct:* Entra ID (formerly Azure Active Directory) handles authentication and access management for cloud identities.
    *   It is not a domain controller replacement for DNS or database storage.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **groups**?
B) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
D) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **groups**.
    * *Why A is correct:* This describes the exact role and function of **groups**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **groups**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **groups**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
A) terraform apply
C) aws s3 sync local_dir s3://my-bucket
B) kubectl get pods -n production
D) gcloud compute instances list
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Microsoft Entra ID (Azure AD) Basics** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
D) Reboot the physical machine and wait for services to reload.
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **Microsoft Entra ID (Azure AD) Basics**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

