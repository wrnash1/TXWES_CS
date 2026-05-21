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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **EFS (multi-instance mount)**?
B) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
C) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
D) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **EFS (multi-instance mount)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **EFS (multi-instance mount)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **EFS (multi-instance mount)**.
    * *Why A is correct:* This describes the exact role and function of **EFS (multi-instance mount)**.


---

**Question 3**
A systems administrator or developer needs to **list all active container pods running in the production namespace of the Kubernetes cluster**. Which of the following commands is the most appropriate to execute?
D) gcloud compute instances list
A) kubectl get pods -n production
C) terraform apply
B) aws s3 sync local_dir s3://my-bucket
*   **Correct Answer:** A) kubectl get pods -n production
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `kubectl get pods -n production` command is directly designed to list all active container pods running in the production namespace of the Kubernetes cluster.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Amazon EBS & EFS Storage Systems** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
D) Reboot the physical machine and wait for services to reload.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..


---

**Question 5**
When designing a system for **Amazon EBS & EFS Storage Systems**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

