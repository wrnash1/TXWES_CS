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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **CloudFormation templates**?
C) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
B) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **CloudFormation templates**.
    * *Why A is correct:* This describes the exact role and function of **CloudFormation templates**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **CloudFormation templates**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **CloudFormation templates**.


---

**Question 3**
A systems administrator or developer needs to **synchronize local files directly to a cloud object storage bucket**. Which of the following commands is the most appropriate to execute?
A) aws s3 sync local_dir s3://my-bucket
B) kubectl get pods -n production
D) gcloud compute instances list
C) terraform apply
*   **Correct Answer:** A) aws s3 sync local_dir s3://my-bucket
*   **Distractor Analysis:**
    * *Why A is correct:* The `aws s3 sync local_dir s3://my-bucket` command is directly designed to synchronize local files directly to a cloud object storage bucket.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **AWS CloudFormation (IaC)** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **AWS CloudFormation (IaC)**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

