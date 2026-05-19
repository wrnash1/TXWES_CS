# Quiz: Module 05 - Azure Virtual Networking
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure service allows secure, dedicated, private fiber-optic connection from an on-premises datacenter directly to Azure?
*   A) Azure VPN Gateway
*   B) Azure ExpressRoute
*   C) Azure Bastion
*   D) VNet Peering
*   **Correct Answer:** B) ExpressRoute bypasses the public internet completely to provide high-speed, private connections to Azure.
*   **Distractor Analysis:**
    *   *Why correct:* ExpressRoute bypasses the public internet completely to provide high-speed, private connections to Azure.
    *   VPN Gateway travels over the public internet using encryption.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **VPN Gateways.**?
B) The core CSS layout block consisting of margins, borders, padding, and the actual content area, defining the sizing and spacing of every page element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
D) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **VPN Gateways.**.
    * *Why A is correct:* This describes the exact role and function of **VPN Gateways.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **VPN Gateways.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **VPN Gateways.**.


---

**Question 3**
A systems administrator or developer needs to **synchronize local files directly to a cloud object storage bucket**. Which of the following commands is the most appropriate to execute?
D) terraform apply
B) gcloud compute instances list
A) aws s3 sync local_dir s3://my-bucket
C) kubectl get pods -n production
*   **Correct Answer:** A) aws s3 sync local_dir s3://my-bucket
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `aws s3 sync local_dir s3://my-bucket` command is directly designed to synchronize local files directly to a cloud object storage bucket.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure Virtual Networking** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
D) Reboot the physical machine and wait for services to reload.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..


---

**Question 5**
When designing a system for **Azure Virtual Networking**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..

