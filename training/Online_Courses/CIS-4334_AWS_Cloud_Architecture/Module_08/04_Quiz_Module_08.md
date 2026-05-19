# Quiz: Module 08 - Amazon RDS and DynamoDB
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which AWS database service is a fully managed NoSQL key-value database designed for single-digit millisecond latency at scale?
*   A) Amazon RDS
*   B) Amazon Aurora
*   C) Amazon DynamoDB
*   D) Amazon Redshift
*   **Correct Answer:** C) DynamoDB is fully managed key-value NoSQL database engine designed for scale.
*   **Distractor Analysis:**
    *   *Why correct:* DynamoDB is fully managed key-value NoSQL database engine designed for scale.
    *   RDS and Aurora are relational. Redshift is data warehouse.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Relational Database Service (RDS)**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
C) A logically isolated virtual network dedicated to a cloud account, giving control over subnets, IP ranges, and route tables.
D) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Relational Database Service (RDS)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Relational Database Service (RDS)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Relational Database Service (RDS)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Relational Database Service (RDS)**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
C) kubectl get pods -n production
D) aws s3 sync local_dir s3://my-bucket
B) gcloud compute instances list
A) terraform apply
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.


---

**Question 4**
While working on **Amazon RDS and DynamoDB** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.


---

**Question 5**
When designing a system for **Amazon RDS and DynamoDB**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

