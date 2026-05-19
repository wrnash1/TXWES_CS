# Quiz: Module 05 - AWS IAM (Identity Access Management)
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which IAM identity should be assigned to an EC2 instance to allow it to securely query an S3 bucket without hardcoded keys?
*   A) IAM User
*   B) IAM Group
*   C) IAM Role
*   D) Root User
*   **Correct Answer:** C) IAM Roles issue temporary security credentials to trusted services like EC2 instances.
*   **Distractor Analysis:**
    *   *Why correct:* IAM Roles issue temporary security credentials to trusted services like EC2 instances.
    *   Users are for human credentials. Groups hold users.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **IAM users**?
B) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
D) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) The core CSS layout block consisting of margins, borders, padding, and the actual content area, defining the sizing and spacing of every page element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **IAM users**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **IAM users**.
    * *Why A is correct:* This describes the exact role and function of **IAM users**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **IAM users**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
D) terraform apply
C) aws s3 sync local_dir s3://my-bucket
B) kubectl get pods -n production
A) gcloud compute instances list
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.


---

**Question 4**
While working on **AWS IAM (Identity Access Management)** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **AWS IAM (Identity Access Management)**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

