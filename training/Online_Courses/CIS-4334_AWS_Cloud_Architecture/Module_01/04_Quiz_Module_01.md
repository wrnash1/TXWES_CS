# Quiz: Module 01 - AWS Infrastructure & Core Architecture
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which AWS infrastructure component consists of one or more discrete datacenters with redundant power and networking?
*   A) Region
*   B) Edge Location
*   C) Availability Zone
*   D) Local Zone
*   **Correct Answer:** C) An Availability Zone (AZ) is a group of datacenters inside a Region, designed for fault isolation.
*   **Distractor Analysis:**
    *   *Why correct:* An Availability Zone (AZ) is a group of datacenters inside a Region, designed for fault isolation.
    *   Regions contain multiple AZs. Edge locations cache content.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **AWS Global Infrastructure**?
D) The practice of managing and provisioning cloud infrastructure through machine-readable definition files (e.g. Terraform).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) A logically isolated virtual network dedicated to a cloud account, giving control over subnets, IP ranges, and route tables.
C) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **AWS Global Infrastructure**.
    * *Why A is correct:* This describes the exact role and function of **AWS Global Infrastructure**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **AWS Global Infrastructure**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **AWS Global Infrastructure**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
C) aws s3 sync local_dir s3://my-bucket
B) kubectl get pods -n production
D) gcloud compute instances list
A) terraform apply
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.


---

**Question 4**
While working on **AWS Infrastructure & Core Architecture** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **AWS Infrastructure & Core Architecture**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

