# Quiz: Module 11 - AWS Monitoring & Governance
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which service should you check to audit who made an API call to terminate an EC2 instance?
*   A) Amazon CloudWatch
*   B) AWS CloudTrail
*   C) AWS Systems Manager
*   D) Amazon Inspector
*   **Correct Answer:** B) CloudTrail records all API activity, user logins, and console actions across AWS accounts.
*   **Distractor Analysis:**
    *   *Why correct:* CloudTrail records all API activity, user logins, and console actions across AWS accounts.
    *   CloudWatch collects metrics and performance logs.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Amazon CloudWatch (metrics**?
C) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
D) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon CloudWatch (metrics**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon CloudWatch (metrics**.
    * *Why A is correct:* This describes the exact role and function of **Amazon CloudWatch (metrics**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon CloudWatch (metrics**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
A) gcloud compute instances list
D) kubectl get pods -n production
C) terraform apply
B) aws s3 sync local_dir s3://my-bucket
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **AWS Monitoring & Governance** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
D) Reboot the physical machine and wait for services to reload.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.


---

**Question 5**
When designing a system for **AWS Monitoring & Governance**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

