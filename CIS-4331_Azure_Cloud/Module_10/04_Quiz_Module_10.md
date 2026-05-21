# Quiz: Module 10 - Azure RBAC and Subscriptions
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What is the scope hierarchy in Azure from largest to smallest?
*   A) Subscription -> Resource Group -> Resource -> Management Group
*   B) Management Group -> Subscription -> Resource Group -> Resource
*   C) Resource -> Resource Group -> Subscription -> Management Group
*   D) Tenant -> Resource -> Resource Group -> Subscription
*   **Correct Answer:** B) Inheritance flows from Management Groups down to Subscriptions, Resource Groups, and individual Resources.
*   **Distractor Analysis:**
    *   *Why correct:* Inheritance flows from Management Groups down to Subscriptions, Resource Groups, and individual Resources.
    *   A and C represent incorrect orderings. D starts at resource.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **scopes**?
B) A computer data storage architecture that manages data as objects (e.g. AWS S3, Google Cloud Storage), offering high scalability.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) The core CSS layout block consisting of margins, borders, padding, and the actual content area, defining the sizing and spacing of every page element.
C) CSS rules (like width, height, max-width, box-sizing) that dictate how the dimensions of elements are calculated and rendered.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **scopes**.
    * *Why A is correct:* This describes the exact role and function of **scopes**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **scopes**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **scopes**.


---

**Question 3**
A systems administrator or developer needs to **synchronize local files directly to a cloud object storage bucket**. Which of the following commands is the most appropriate to execute?
C) terraform apply
B) kubectl get pods -n production
D) gcloud compute instances list
A) aws s3 sync local_dir s3://my-bucket
*   **Correct Answer:** A) aws s3 sync local_dir s3://my-bucket
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `aws s3 sync local_dir s3://my-bucket` command is directly designed to synchronize local files directly to a cloud object storage bucket.


---

**Question 4**
While working on **Azure RBAC and Subscriptions** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **Azure RBAC and Subscriptions**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
D) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

