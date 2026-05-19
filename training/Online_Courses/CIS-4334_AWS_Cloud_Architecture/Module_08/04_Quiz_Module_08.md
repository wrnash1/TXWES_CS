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
C) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
D) A logically isolated virtual network dedicated to a cloud account, giving control over subnets, IP ranges, and route tables.
B) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Relational Database Service (RDS)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Relational Database Service (RDS)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Relational Database Service (RDS)**.
    * *Why A is correct:* This describes the exact role and function of **Relational Database Service (RDS)**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
C) gcloud compute instances list
B) kubectl get pods -n production
A) terraform apply
D) aws s3 sync local_dir s3://my-bucket
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Amazon RDS and DynamoDB** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Amazon RDS and DynamoDB**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

