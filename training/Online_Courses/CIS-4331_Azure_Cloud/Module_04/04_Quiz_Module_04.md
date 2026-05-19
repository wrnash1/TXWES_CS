# Quiz: Module 04 - Azure Container Services
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What is the fastest way to run a single Docker container in Azure without provisioning virtual machines?
*   A) Azure Kubernetes Service (AKS)
*   B) Azure Container Instances (ACI)
*   C) Azure Functions
*   D) Windows Server container host
*   **Correct Answer:** B) ACI is a serverless container solution designed to quickly run single containers without VM management overhead.
*   **Distractor Analysis:**
    *   *Why correct:* ACI is a serverless container solution designed to quickly run single containers without VM management overhead.
    *   AKS is for full container orchestrations and requires cluster provisioning.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **serverless computing.**?
B) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) A cloud feature that dynamically adjusts resource capacity (number of VMs) based on active demand or performance metrics.
D) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **serverless computing.**.
    * *Why A is correct:* This describes the exact role and function of **serverless computing.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **serverless computing.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **serverless computing.**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
B) kubectl get pods -n production
A) terraform apply
C) gcloud compute instances list
D) aws s3 sync local_dir s3://my-bucket
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure Container Services** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Azure Container Services**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
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

