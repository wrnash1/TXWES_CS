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
C) A cloud feature that dynamically adjusts resource capacity (number of VMs) based on active demand or performance metrics.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) Electrostatic Discharge protection; tools (like wrist straps, grounding mats) used to prevent static electricity from destroying sensitive microchips when handling hardware.
B) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Advisor recommendations.**.
    * *Why A is correct:* This describes the exact role and function of **Advisor recommendations.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Advisor recommendations.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Advisor recommendations.**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
C) aws s3 sync local_dir s3://my-bucket
D) terraform apply
B) kubectl get pods -n production
A) gcloud compute instances list
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.


---

**Question 4**
While working on **Azure Monitoring and Diagnostics** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
D) Reboot the physical machine and wait for services to reload.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Azure Monitoring and Diagnostics**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..

