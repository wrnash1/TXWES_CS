# Quiz: Module 06 - IAM
## Course: CIS-4329_Google_Cloud (4329_Google_Cloud - Google Cloud Associate Cloud Engineer)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Custom Roles**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
D) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
B) The descendant node connected to the right branch of a parent node in a binary tree structure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Custom Roles**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Custom Roles**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Custom Roles**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Custom Roles**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Primitive vs. Predefined Roles**?
B) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
D) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
C) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Primitive vs. Predefined Roles**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Primitive vs. Predefined Roles**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Primitive vs. Predefined Roles**.
    * *Why A is correct:* This describes the exact role and function of **Primitive vs. Predefined Roles**.


---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
A) gcloud compute instances list
B) kubectl get pods -n production
C) aws s3 sync local_dir s3://my-bucket
D) terraform apply
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **IAM** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.


---

**Question 5**
When designing a system for **IAM**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
C) Enable full disk encryption on all client endpoints.
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

