# Quiz: Module 09 - Elastic Load Balancing & Auto Scaling
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which type of load balancer is best suited for routing millions of ultra-low latency TCP requests at Layer 4?
*   A) Application Load Balancer (ALB)
*   B) Network Load Balancer (NLB)
*   C) Classic Load Balancer
*   D) Gateway Load Balancer
*   **Correct Answer:** B) NLB operates at Layer 4 (Transport) and handles volatile network spikes and TCP/UDP traffic at extreme speeds.
*   **Distractor Analysis:**
    *   *Why correct:* NLB operates at Layer 4 (Transport) and handles volatile network spikes and TCP/UDP traffic at extreme speeds.
    *   ALB operates at Layer 7 and evaluates HTTP headers and paths.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Auto Scaling Groups (ASG).**?
B) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
D) A two-dimensional CSS layout system that allows developers to design complex grid-based user interfaces with rows and columns, offering precise control over alignment.
C) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Auto Scaling Groups (ASG).**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Auto Scaling Groups (ASG).**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Auto Scaling Groups (ASG).**.
    * *Why A is correct:* This describes the exact role and function of **Auto Scaling Groups (ASG).**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
B) kubectl get pods -n production
D) gcloud compute instances list
A) terraform apply
C) aws s3 sync local_dir s3://my-bucket
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Elastic Load Balancing & Auto Scaling** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Elastic Load Balancing & Auto Scaling**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

