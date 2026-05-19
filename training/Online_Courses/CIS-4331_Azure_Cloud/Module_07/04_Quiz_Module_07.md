# Quiz: Module 07 - Azure Database Services
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure database service is a globally distributed, multi-model database engine supporting SQL, MongoDB, and Cassandra APIs?
*   A) Azure SQL Database
*   B) Azure Database for PostgreSQL
*   C) Azure Cosmos DB
*   D) Azure SQL Managed Instance
*   **Correct Answer:** C) Cosmos DB is Microsoft's NoSQL engine built for global distribution and multi-API access.
*   **Distractor Analysis:**
    *   *Why correct:* Cosmos DB is Microsoft's NoSQL engine built for global distribution and multi-API access.
    *   Azure SQL is strictly relational SQL.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **global distribution)**?
B) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
D) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
C) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **global distribution)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **global distribution)**.
    * *Why A is correct:* This describes the exact role and function of **global distribution)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **global distribution)**.


---

**Question 3**
A systems administrator or developer needs to **list all active container pods running in the production namespace of the Kubernetes cluster**. Which of the following commands is the most appropriate to execute?
C) terraform apply
A) kubectl get pods -n production
B) gcloud compute instances list
D) aws s3 sync local_dir s3://my-bucket
*   **Correct Answer:** A) kubectl get pods -n production
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `kubectl get pods -n production` command is directly designed to list all active container pods running in the production namespace of the Kubernetes cluster.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure Database Services** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
C) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **Azure Database Services**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

