# Quiz: Module 09 - Entra Authentication and MFA
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Entra ID feature allows you to enforce security policies based on signals like user location or device state?
*   A) Multi-Factor Authentication
*   B) Conditional Access
*   C) Role-Based Access Control
*   D) Privileged Identity Management
*   **Correct Answer:** B) Conditional Access implements 'if-then' policies (e.g. if logging in from outside corporate network, require MFA).
*   **Distractor Analysis:**
    *   *Why correct:* Conditional Access implements 'if-then' policies (e.g. if logging in from outside corporate network, require MFA).
    *   MFA is the authentication mechanism, but Conditional Access controls when it is triggered.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Multi-Factor Authentication (MFA)**?
C) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disaster.
D) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Multi-Factor Authentication (MFA)**.
    * *Why A is correct:* This describes the exact role and function of **Multi-Factor Authentication (MFA)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Multi-Factor Authentication (MFA)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Multi-Factor Authentication (MFA)**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
B) gcloud compute instances list
A) terraform apply
D) aws s3 sync local_dir s3://my-bucket
C) kubectl get pods -n production
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Entra Authentication and MFA** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **Entra Authentication and MFA**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

