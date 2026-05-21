# Quiz: Module 13 - AWS CloudFormation (IaC)
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
What is the purpose of AWS CloudFormation?
*   A) Auto-scaling servers
*   B) Provisioning resources declaratively using templates (IaC)
*   C) Encrypting files
*   D) Routing web traffic
*   **Correct Answer:** B) CloudFormation handles infrastructure provision automations via declarative YAML/JSON templates.
*   **Distractor Analysis:**
    *   *Why correct:* CloudFormation handles infrastructure provision automations via declarative YAML/JSON templates.
    *   It is an IaC tool, not auto-scaling or routing software.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **parameters**?
B) The descendant node connected to the left branch of a parent node in a binary tree structure.
C) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **parameters**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **parameters**.
    * *Why A is correct:* This describes the exact role and function of **parameters**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **parameters**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
C) terraform apply
D) kubectl get pods -n production
B) aws s3 sync local_dir s3://my-bucket
A) gcloud compute instances list
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.


---

**Question 4**
While working on **AWS CloudFormation (IaC)** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..


---

**Question 5**
When designing a system for **AWS CloudFormation (IaC)**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..

