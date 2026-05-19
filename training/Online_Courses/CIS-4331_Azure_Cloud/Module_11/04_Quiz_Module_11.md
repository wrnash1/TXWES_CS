# Quiz: Module 11 - Azure Security Tools
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure service is designed to securely store and control access to tokens, passwords, certificates, and API keys?
*   A) Azure Bastion
*   B) Azure Key Vault
*   C) Microsoft Entra ID
*   D) Azure Security Center
*   **Correct Answer:** B) Key Vault provides centralized secrets, keys, and certificate storage with strict access controls.
*   **Distractor Analysis:**
    *   *Why correct:* Key Vault provides centralized secrets, keys, and certificate storage with strict access controls.
    *   Bastion provides secure RDP/SSH. Entra ID is for identities.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Azure Sentinel (SIEM).**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) CSS rules (like width, height, max-width, box-sizing) that dictate how the dimensions of elements are calculated and rendered.
B) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
C) The practice of managing and provisioning cloud infrastructure through machine-readable definition files (e.g. Terraform).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Azure Sentinel (SIEM).**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Sentinel (SIEM).**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Sentinel (SIEM).**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Sentinel (SIEM).**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
C) aws s3 sync local_dir s3://my-bucket
D) gcloud compute instances list
B) kubectl get pods -n production
A) terraform apply
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.


---

**Question 4**
While working on **Azure Security Tools** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
D) Reboot the physical machine and wait for services to reload.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Azure Security Tools**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

