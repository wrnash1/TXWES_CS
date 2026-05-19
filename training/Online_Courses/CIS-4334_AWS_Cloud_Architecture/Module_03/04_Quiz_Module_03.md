# Quiz: Module 03 - Amazon VPC Virtual Networks
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
What VPC component is required to route traffic from a public subnet out to the public internet?
*   A) NAT Gateway
*   B) Internet Gateway (IGW)
*   C) Customer Gateway
*   D) Direct Connect
*   **Correct Answer:** B) An Internet Gateway links the VPC to the public internet, enabling bidirectional communication.
*   **Distractor Analysis:**
    *   *Why correct:* An Internet Gateway links the VPC to the public internet, enabling bidirectional communication.
    *   NAT Gateway provides outbound-only internet access for private subnets.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Internet Gateways (IGWs)**?
D) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) The cloud framework of policies and technologies ensuring that the right entities have appropriate access to resources.
C) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Internet Gateways (IGWs)**.
    * *Why A is correct:* This describes the exact role and function of **Internet Gateways (IGWs)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Internet Gateways (IGWs)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Internet Gateways (IGWs)**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
B) kubectl get pods -n production
A) terraform apply
C) aws s3 sync local_dir s3://my-bucket
D) gcloud compute instances list
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Amazon VPC Virtual Networks** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Amazon VPC Virtual Networks**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
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

