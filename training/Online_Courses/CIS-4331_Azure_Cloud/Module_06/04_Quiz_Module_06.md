# Quiz: Module 06 - Azure Storage Services
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which storage tier has the lowest storage cost but the highest data retrieval latency?
*   A) Hot Tier
*   B) Cool Tier
*   C) Cold Tier
*   D) Archive Tier
*   **Correct Answer:** D) Archive storage offers the cheapest capacity rates but requires hours to rehydrate/retrieve data.
*   **Distractor Analysis:**
    *   *Why correct:* Archive storage offers the cheapest capacity rates but requires hours to rehydrate/retrieve data.
    *   Hot, Cool, and Cold tiers keep data online for immediate access at higher costs.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Disk Storage**?
C) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
B) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
D) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Disk Storage**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Disk Storage**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Disk Storage**.
    * *Why A is correct:* This describes the exact role and function of **Disk Storage**.


---

**Question 3**
A systems administrator or developer needs to **synchronize local files directly to a cloud object storage bucket**. Which of the following commands is the most appropriate to execute?
A) aws s3 sync local_dir s3://my-bucket
C) terraform apply
B) gcloud compute instances list
D) kubectl get pods -n production
*   **Correct Answer:** A) aws s3 sync local_dir s3://my-bucket
*   **Distractor Analysis:**
    * *Why A is correct:* The `aws s3 sync local_dir s3://my-bucket` command is directly designed to synchronize local files directly to a cloud object storage bucket.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure Storage Services** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..


---

**Question 5**
When designing a system for **Azure Storage Services**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

