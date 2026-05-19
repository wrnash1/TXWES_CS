# Quiz: Module 14 - AWS High Availability Patterns
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
What term describes the maximum acceptable delay of data loss during an outage?
*   A) Recovery Time Objective (RTO)
*   B) Recovery Point Objective (RPO)
*   C) Mean Time to Repair
*   D) Service Level Agreement
*   **Correct Answer:** B) Recovery Point Objective (RPO) defines how much data (measured in time) can be lost during an outage.
*   **Distractor Analysis:**
    *   *Why correct:* Recovery Point Objective (RPO) defines how much data (measured in time) can be lost during an outage.
    *   RTO is the target recovery duration.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **RTO and RPO targets.**?
B) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
D) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **RTO and RPO targets.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **RTO and RPO targets.**.
    * *Why A is correct:* This describes the exact role and function of **RTO and RPO targets.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **RTO and RPO targets.**.


---

**Question 3**
A systems administrator or developer needs to **list all active container pods running in the production namespace of the Kubernetes cluster**. Which of the following commands is the most appropriate to execute?
B) terraform apply
A) kubectl get pods -n production
C) aws s3 sync local_dir s3://my-bucket
D) gcloud compute instances list
*   **Correct Answer:** A) kubectl get pods -n production
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `kubectl get pods -n production` command is directly designed to list all active container pods running in the production namespace of the Kubernetes cluster.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **AWS High Availability Patterns** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.


---

**Question 5**
When designing a system for **AWS High Availability Patterns**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

