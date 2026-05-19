# Quiz: Module 15 - Well-Architected Framework
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which pillar of the Well-Architected Framework focuses on running and monitoring systems to deliver business value?
*   A) Reliability
*   B) Performance Efficiency
*   C) Operational Excellence
*   D) Cost Optimization
*   **Correct Answer:** C) Operational Excellence is the pillar centered on managing and continuously improving system processes.
*   **Distractor Analysis:**
    *   *Why correct:* Operational Excellence is the pillar centered on managing and continuously improving system processes.
    *   Reliability deals with recoverability. Performance deals with compute scaling.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Security**?
C) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
B) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Security**.
    * *Why A is correct:* This describes the exact role and function of **Security**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Security**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Security**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
B) kubectl get pods -n production
C) terraform apply
D) aws s3 sync local_dir s3://my-bucket
A) gcloud compute instances list
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.


---

**Question 4**
While working on **Well-Architected Framework** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Well-Architected Framework**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
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

