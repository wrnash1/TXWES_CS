# Quiz: Module 12 - Azure Governance & Compliance
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which resource lock type prevents users from deleting a resource but still allows them to read and modify it?
*   A) ReadOnly
*   B) CanNotDelete
*   C) WriteLock
*   D) DeleteLock
*   **Correct Answer:** B) The `CanNotDelete` lock allows read and write modifications but blocks deletion requests.
*   **Distractor Analysis:**
    *   *Why correct:* The `CanNotDelete` lock allows read and write modifications but blocks deletion requests.
    *   ReadOnly blocks both deletions and writes.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Azure Blueprints**?
C) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
D) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Blueprints**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Blueprints**.
    * *Why A is correct:* This describes the exact role and function of **Azure Blueprints**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Blueprints**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
C) aws s3 sync local_dir s3://my-bucket
D) terraform apply
A) gcloud compute instances list
B) kubectl get pods -n production
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure Governance & Compliance** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **Azure Governance & Compliance**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
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

