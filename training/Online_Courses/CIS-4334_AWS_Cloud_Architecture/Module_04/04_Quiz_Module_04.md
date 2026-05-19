# Quiz: Module 04 - AWS Network Security
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
What is the key operational difference between Security Groups and Network ACLs?
*   A) Security Groups are stateless, NACLs are stateful
*   B) Security Groups are stateful, NACLs are stateless
*   C) Security Groups filter Layer 7, NACLs filter Layer 2
*   D) None of the above
*   **Correct Answer:** B) Security Groups are stateful (allowing inbound traffic automatically allows return traffic). NACLs are stateless (requires explicit inbound/outbound rules).
*   **Distractor Analysis:**
    *   *Why correct:* Security Groups are stateful (allowing inbound traffic automatically allows return traffic). NACLs are stateless (requires explicit inbound/outbound rules).
    *   A is reversed.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Security Groups (stateful) vs Network ACLs (stateless)**?
D) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
C) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Security Groups (stateful) vs Network ACLs (stateless)**.
    * *Why A is correct:* This describes the exact role and function of **Security Groups (stateful) vs Network ACLs (stateless)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Security Groups (stateful) vs Network ACLs (stateless)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Security Groups (stateful) vs Network ACLs (stateless)**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
A) terraform apply
D) kubectl get pods -n production
C) aws s3 sync local_dir s3://my-bucket
B) gcloud compute instances list
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **AWS Network Security** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **AWS Network Security**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

