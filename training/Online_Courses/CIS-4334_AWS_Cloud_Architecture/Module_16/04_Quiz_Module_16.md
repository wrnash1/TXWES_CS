# Quiz: Module 16 - Course Module
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Core Operations**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
C) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
B) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Core Operations**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Core Operations**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Core Operations**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Core Operations**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **System Configuration**?
B) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
D) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **System Configuration**.
    * *Why A is correct:* This describes the exact role and function of **System Configuration**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **System Configuration**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **System Configuration**.


---

**Question 3**
A systems administrator or developer needs to **synchronize local files directly to a cloud object storage bucket**. Which of the following commands is the most appropriate to execute?
A) aws s3 sync local_dir s3://my-bucket
D) terraform apply
B) kubectl get pods -n production
C) gcloud compute instances list
*   **Correct Answer:** A) aws s3 sync local_dir s3://my-bucket
*   **Distractor Analysis:**
    * *Why A is correct:* The `aws s3 sync local_dir s3://my-bucket` command is directly designed to synchronize local files directly to a cloud object storage bucket.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Course Module** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.


---

**Question 5**
When designing a system for **Course Module**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

