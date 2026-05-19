# Quiz: Module 15 - Azure Resource Manager (ARM) & CLI
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What file format is used to write Azure Resource Manager (ARM) templates?
*   A) XML
*   B) JSON
*   C) YAML
*   D) CSV
*   **Correct Answer:** B) ARM templates are written in JSON (JavaScript Object Notation), representing resources declaratively.
*   **Distractor Analysis:**
    *   *Why correct:* ARM templates are written in JSON (JavaScript Object Notation), representing resources declaratively.
    *   YAML is used for Bicep or Kubernetes configurations but not native ARM templates.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Azure CLI**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
C) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
D) The descendant node connected to the left branch of a parent node in a binary tree structure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Azure CLI**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Azure CLI**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Azure CLI**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Azure CLI**.


---

**Question 3**
A systems administrator or developer needs to **synchronize local files directly to a cloud object storage bucket**. Which of the following commands is the most appropriate to execute?
B) terraform apply
D) gcloud compute instances list
A) aws s3 sync local_dir s3://my-bucket
C) kubectl get pods -n production
*   **Correct Answer:** A) aws s3 sync local_dir s3://my-bucket
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `aws s3 sync local_dir s3://my-bucket` command is directly designed to synchronize local files directly to a cloud object storage bucket.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure Resource Manager (ARM) & CLI** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **Azure Resource Manager (ARM) & CLI**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
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

