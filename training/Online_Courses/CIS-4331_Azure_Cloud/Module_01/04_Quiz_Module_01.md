# Quiz: Module 01 - Cloud Computing Concepts
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which service model gives the consumer the greatest control over virtual machines and operating systems?
*   A) Software as a Service (SaaS)
*   B) Platform as a Service (PaaS)
*   C) Infrastructure as a Service (IaaS)
*   D) Database as a Service (DBaaS)
*   **Correct Answer:** C) IaaS provides raw infrastructure (VMs, networking, storage), leaving OS and software management to the customer.
*   **Distractor Analysis:**
    *   *Why correct:* IaaS provides raw infrastructure (VMs, networking, storage), leaving OS and software management to the customer.
    *   PaaS and SaaS manage the OS layer for you, reducing your control.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **CAPEX vs OPEX.**?
D) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
B) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **CAPEX vs OPEX.**.
    * *Why A is correct:* This describes the exact role and function of **CAPEX vs OPEX.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **CAPEX vs OPEX.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **CAPEX vs OPEX.**.


---

**Question 3**
A systems administrator or developer needs to **synchronize local files directly to a cloud object storage bucket**. Which of the following commands is the most appropriate to execute?
A) aws s3 sync local_dir s3://my-bucket
B) terraform apply
D) kubectl get pods -n production
C) gcloud compute instances list
*   **Correct Answer:** A) aws s3 sync local_dir s3://my-bucket
*   **Distractor Analysis:**
    * *Why A is correct:* The `aws s3 sync local_dir s3://my-bucket` command is directly designed to synchronize local files directly to a cloud object storage bucket.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Cloud Computing Concepts** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Cloud Computing Concepts**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

