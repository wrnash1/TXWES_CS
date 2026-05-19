# Quiz: Module 07 - Amazon EBS & EFS Storage Systems
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which storage service allows you to mount a shared file system on multiple EC2 instances concurrently?
*   A) Amazon EBS
*   B) Amazon S3
*   C) Amazon EFS (Elastic File System)
*   D) Amazon Instance Store
*   **Correct Answer:** C) EFS supports the NFS protocol, allowing thousands of EC2 instances to share access to the same storage space.
*   **Distractor Analysis:**
    *   *Why correct:* EFS supports the NFS protocol, allowing thousands of EC2 instances to share access to the same storage space.
    *   EBS can only mount to a single instance at a time (except special Multi-Attach volumes in same AZ).

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **HDD)**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
D) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
B) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **HDD)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **HDD)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **HDD)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **HDD)**.


---

**Question 3**
A systems administrator or developer needs to **list all active container pods running in the production namespace of the Kubernetes cluster**. Which of the following commands is the most appropriate to execute?
D) terraform apply
A) kubectl get pods -n production
C) aws s3 sync local_dir s3://my-bucket
B) gcloud compute instances list
*   **Correct Answer:** A) kubectl get pods -n production
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `kubectl get pods -n production` command is directly designed to list all active container pods running in the production namespace of the Kubernetes cluster.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Amazon EBS & EFS Storage Systems** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
D) Reboot the physical machine and wait for services to reload.
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **Amazon EBS & EFS Storage Systems**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
C) Enable full disk encryption on all client endpoints.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

