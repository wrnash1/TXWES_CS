# Quiz: Module 12 - Serverless Implementations
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which service provides decoupled, asynchronously stored message queues to help design resilient architectures?
*   A) Amazon SNS
*   B) Amazon SQS
*   C) AWS Lambda
*   D) AWS Step Functions
*   **Correct Answer:** B) Simple Queue Service (SQS) buffers messages between components, allowing systems to run decoupled.
*   **Distractor Analysis:**
    *   *Why correct:* Simple Queue Service (SQS) buffers messages between components, allowing systems to run decoupled.
    *   SNS is push notifications (pub/sub). Lambda is execution.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Amazon SQS (message queues).**?
D) The practice of managing and provisioning cloud infrastructure through machine-readable definition files (e.g. Terraform).
C) A logically isolated virtual network dedicated to a cloud account, giving control over subnets, IP ranges, and route tables.
B) A cloud feature that dynamically adjusts resource capacity (number of VMs) based on active demand or performance metrics.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon SQS (message queues).**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon SQS (message queues).**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon SQS (message queues).**.
    * *Why A is correct:* This describes the exact role and function of **Amazon SQS (message queues).**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
B) kubectl get pods -n production
D) aws s3 sync local_dir s3://my-bucket
C) terraform apply
A) gcloud compute instances list
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.


---

**Question 4**
While working on **Serverless Implementations** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **Serverless Implementations**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..

