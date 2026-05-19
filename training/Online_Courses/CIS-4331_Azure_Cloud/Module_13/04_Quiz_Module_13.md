# Quiz: Module 13 - Azure Monitoring and Diagnostics
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure service provides personalized recommendations to optimize resource performance, security, and cost?
*   A) Azure Monitor
*   B) Azure Log Analytics
*   C) Azure Advisor
*   D) Microsoft Sentinel
*   **Correct Answer:** C) Azure Advisor scans your deployment configuration and recommends improvements across five pillars: Cost, Security, Reliability, Performance, and Operational Excellence.
*   **Distractor Analysis:**
    *   *Why correct:* Azure Advisor scans your deployment configuration and recommends improvements across five pillars: Cost, Security, Reliability, Performance, and Operational Excellence.
    *   Azure Monitor collects telemetry metrics.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Advisor recommendations.**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
C) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
D) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Advisor recommendations.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Advisor recommendations.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Advisor recommendations.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Advisor recommendations.**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
A) gcloud compute instances list
C) kubectl get pods -n production
B) aws s3 sync local_dir s3://my-bucket
D) terraform apply
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure Monitoring and Diagnostics** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.


---

**Question 5**
When designing a system for **Azure Monitoring and Diagnostics**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..

