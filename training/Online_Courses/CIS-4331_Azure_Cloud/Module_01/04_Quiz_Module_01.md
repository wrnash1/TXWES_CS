# Quiz: Module 01 - Cloud Computing Concepts
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which service model gives the consumer the greatest control over virtual machines and operating systems?
*   A) Software as a Service (SaaS)
*   B) Platform as a Service (PaaS)
*   C) Infrastructure as a Service (IaaS)
*   D) Database as a Service (DBaaS)
*   **Correct Answer:** C) IaaS provides raw infrastructure (VMs, networking, storage), leaving OS and software management to the customer.
*   **Distractor Analysis:**
    *   *Why correct:* IaaS provides raw infrastructure (VMs, networking, storage), leaving OS and software management to the customer.
    *   PaaS and SaaS manage the OS layer for you, reducing your control.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Public/Private/Hybrid clouds**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) CSS properties (like block, inline, flex, grid) that determine how an element is rendered and how it behaves relative to surrounding elements.
C) A computer data storage architecture that manages data as objects (e.g. AWS S3, Google Cloud Storage), offering high scalability.
B) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Public/Private/Hybrid clouds**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Public/Private/Hybrid clouds**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Public/Private/Hybrid clouds**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Public/Private/Hybrid clouds**.


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
While working on **Cloud Computing Concepts** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **Cloud Computing Concepts**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

