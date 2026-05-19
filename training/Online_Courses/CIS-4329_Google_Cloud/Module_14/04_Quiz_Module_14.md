# Quiz: Module 14 - Security Command Center
## Course: CIS-4329_Google_Cloud (4329_Google_Cloud - Google Cloud Associate Cloud Engineer)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Documentation**?
B) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
C) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) The descendant node connected to the left branch of a parent node in a binary tree structure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why A is correct:* This describes the exact role and function of **Documentation**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Core Concept**?
D) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
C) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why A is correct:* This describes the exact role and function of **Core Concept**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
B) gcloud compute instances list
C) aws s3 sync local_dir s3://my-bucket
D) kubectl get pods -n production
A) terraform apply
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.


---

**Question 4**
While working on **Security Command Center** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.


---

**Question 5**
When designing a system for **Security Command Center**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

