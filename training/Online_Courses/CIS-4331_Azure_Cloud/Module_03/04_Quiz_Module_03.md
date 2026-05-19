# Quiz: Module 03 - Azure Virtual Machines & Scale Sets
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure compute service allows you to automatically deploy and manage a set of identical, auto-scaling VMs?
*   A) Azure App Service
*   B) Azure Functions
*   C) Virtual Machine Scale Sets
*   D) Azure Container Instances
*   **Correct Answer:** C) VMSS enables automatic scaling of identical VMs based on CPU load or schedules.
*   **Distractor Analysis:**
    *   *Why correct:* VMSS enables automatic scaling of identical VMs based on CPU load or schedules.
    *   App Service is for web apps. Functions is serverless.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Virtual Machine Scale Sets (VMSS)**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
D) HTML tags that convey the meaning and structure of the enclosed content to both the browser and search engines (e.g., <header>, <article>, <footer>) instead of generic containers.
B) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
C) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Virtual Machine Scale Sets (VMSS)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Virtual Machine Scale Sets (VMSS)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Virtual Machine Scale Sets (VMSS)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Virtual Machine Scale Sets (VMSS)**.


---

**Question 3**
A systems administrator or developer needs to **list all active container pods running in the production namespace of the Kubernetes cluster**. Which of the following commands is the most appropriate to execute?
D) aws s3 sync local_dir s3://my-bucket
B) terraform apply
A) kubectl get pods -n production
C) gcloud compute instances list
*   **Correct Answer:** A) kubectl get pods -n production
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `kubectl get pods -n production` command is directly designed to list all active container pods running in the production namespace of the Kubernetes cluster.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure Virtual Machines & Scale Sets** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.


---

**Question 5**
When designing a system for **Azure Virtual Machines & Scale Sets**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

