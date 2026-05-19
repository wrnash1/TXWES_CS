# Quiz: Module 06 - Amazon S3 Object Storage
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which S3 storage class offers the lowest retrieval times and cost for archival data accessed once a year?
*   A) S3 Standard
*   B) S3 Standard-IA
*   C) Amazon S3 Glacier Deep Archive
*   D) S3 One Zone-IA
*   **Correct Answer:** C) Glacier Deep Archive is AWS's lowest-cost archival tier, designed for multi-hour retrieval targets.
*   **Distractor Analysis:**
    *   *Why correct:* Glacier Deep Archive is AWS's lowest-cost archival tier, designed for multi-hour retrieval targets.
    *   Standard is for active data. IA is for monthly access.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **storage classes (Standard**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
C) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
D) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **storage classes (Standard**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **storage classes (Standard**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **storage classes (Standard**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **storage classes (Standard**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
B) kubectl get pods -n production
C) aws s3 sync local_dir s3://my-bucket
A) terraform apply
D) gcloud compute instances list
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Amazon S3 Object Storage** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Amazon S3 Object Storage**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..

