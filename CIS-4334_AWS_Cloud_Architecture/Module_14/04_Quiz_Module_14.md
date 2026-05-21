# Quiz: Module 14 - AWS High Availability Patterns
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
What term describes the maximum acceptable delay of data loss during an outage?
*   A) Recovery Time Objective (RTO)
*   B) Recovery Point Objective (RPO)
*   C) Mean Time to Repair
*   D) Service Level Agreement
*   **Correct Answer:** B) Recovery Point Objective (RPO) defines how much data (measured in time) can be lost during an outage.
*   **Distractor Analysis:**
    *   *Why correct:* Recovery Point Objective (RPO) defines how much data (measured in time) can be lost during an outage.
    *   RTO is the target recovery duration.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **RTO and RPO targets.**?
C) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
B) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
D) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **RTO and RPO targets.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **RTO and RPO targets.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **RTO and RPO targets.**.
    * *Why A is correct:* This describes the exact role and function of **RTO and RPO targets.**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
A) terraform apply
C) aws s3 sync local_dir s3://my-bucket
D) gcloud compute instances list
B) kubectl get pods -n production
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **AWS High Availability Patterns** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..


---

**Question 5**
When designing a system for **AWS High Availability Patterns**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

