# Quiz: Module 13 - Hybrid Cloud
## Course: CIS-4329_Google_Cloud (4329_Google_Cloud - Google Cloud Associate Cloud Engineer)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Exam Tip**?
D) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
B) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Exam Tip**.
    * *Why A is correct:* This describes the exact role and function of **Exam Tip**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Exam Tip**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Exam Tip**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Documentation**?
D) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
B) A cloud feature that dynamically adjusts resource capacity (number of VMs) based on active demand or performance metrics.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why A is correct:* This describes the exact role and function of **Documentation**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.


---

**Question 3**
A systems administrator or developer needs to **list all active container pods running in the production namespace of the Kubernetes cluster**. Which of the following commands is the most appropriate to execute?
C) gcloud compute instances list
B) aws s3 sync local_dir s3://my-bucket
A) kubectl get pods -n production
D) terraform apply
*   **Correct Answer:** A) kubectl get pods -n production
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `kubectl get pods -n production` command is directly designed to list all active container pods running in the production namespace of the Kubernetes cluster.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Hybrid Cloud** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.


---

**Question 5**
When designing a system for **Hybrid Cloud**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..

