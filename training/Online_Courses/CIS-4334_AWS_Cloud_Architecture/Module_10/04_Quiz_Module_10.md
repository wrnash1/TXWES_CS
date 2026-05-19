# Quiz: Module 10 - Route 53 & CloudFront CDN
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which routing policy in Route 53 directs client traffic to the AWS resource that offers the lowest round-trip network time?
*   A) Simple Routing
*   B) Latency-Based Routing
*   C) Geolocation Routing
*   D) Failover Routing
*   **Correct Answer:** B) Latency-based routing measures network latency to direct clients to the optimal region.
*   **Distractor Analysis:**
    *   *Why correct:* Latency-based routing measures network latency to direct clients to the optimal region.
    *   Geolocation routing routes based on user continent/country, not speed.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Amazon Route 53 DNS records**?
D) The security framework dividing operations between the cloud provider (security OF the cloud) and the customer (security IN the cloud).
C) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
B) CSS rules (like width, height, max-width, box-sizing) that dictate how the dimensions of elements are calculated and rendered.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon Route 53 DNS records**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon Route 53 DNS records**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Amazon Route 53 DNS records**.
    * *Why A is correct:* This describes the exact role and function of **Amazon Route 53 DNS records**.


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
While working on **Route 53 & CloudFront CDN** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..


---

**Question 5**
When designing a system for **Route 53 & CloudFront CDN**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
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

