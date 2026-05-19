# Quiz: Module 02 - Azure Physical Architecture
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
How many separate physical datacenters must exist within a single Azure Availability Zone?
*   A) At least one
*   B) Exactly three
*   C) Ten
*   D) Availability Zones do not contain physical datacenters
*   **Correct Answer:** A) An Availability Zone is made up of one or more physical datacenters equipped with independent power, cooling, and networking.
*   **Distractor Analysis:**
    *   *Why correct:* An Availability Zone is made up of one or more physical datacenters equipped with independent power, cooling, and networking.
    *   Exactly three is a common misconception (an Azure region with AZ support has at least three zones, not datacenters per zone).

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Azure Resource Manager.**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) The cloud framework of policies and technologies ensuring that the right entities have appropriate access to resources.
B) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
D) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Azure Resource Manager.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Resource Manager.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Resource Manager.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Azure Resource Manager.**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
B) gcloud compute instances list
C) kubectl get pods -n production
D) aws s3 sync local_dir s3://my-bucket
A) terraform apply
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.


---

**Question 4**
While working on **Azure Physical Architecture** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **Azure Physical Architecture**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
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

