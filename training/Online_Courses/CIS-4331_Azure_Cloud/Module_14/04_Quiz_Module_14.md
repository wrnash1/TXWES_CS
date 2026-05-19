# Quiz: Module 14 - Azure Cost Management
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What purchase option allows you to reduce VM costs by up to 72% by committing to a 1-year or 3-year term?
*   A) Pay-as-you-go
*   B) Spot Instances
*   C) Azure Reservations
*   D) Hybrid Benefit
*   **Correct Answer:** C) Reservations provide significant discounts in exchange for a committed usage duration.
*   **Distractor Analysis:**
    *   *Why correct:* Reservations provide significant discounts in exchange for a committed usage duration.
    *   Spot instances can be evicted. Hybrid Benefit uses on-premises licensing.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **TCO calculator**?
D) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
B) The security framework dividing operations between the cloud provider (security OF the cloud) and the customer (security IN the cloud).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **TCO calculator**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **TCO calculator**.
    * *Why A is correct:* This describes the exact role and function of **TCO calculator**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **TCO calculator**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
A) gcloud compute instances list
D) aws s3 sync local_dir s3://my-bucket
B) terraform apply
C) kubectl get pods -n production
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure Cost Management** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
D) Reboot the physical machine and wait for services to reload.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..


---

**Question 5**
When designing a system for **Azure Cost Management**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
C) Enable full disk encryption on all client endpoints.
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..

