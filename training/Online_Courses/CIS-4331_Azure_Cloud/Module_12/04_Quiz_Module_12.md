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
D) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
C) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
B) CSS rules (like width, height, max-width, box-sizing) that dictate how the dimensions of elements are calculated and rendered.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Blueprints**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Blueprints**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Blueprints**.
    * *Why A is correct:* This describes the exact role and function of **Azure Blueprints**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
C) aws s3 sync local_dir s3://my-bucket
D) kubectl get pods -n production
B) gcloud compute instances list
A) terraform apply
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.


---

**Question 4**
While working on **Azure Governance & Compliance** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Azure Governance & Compliance**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

