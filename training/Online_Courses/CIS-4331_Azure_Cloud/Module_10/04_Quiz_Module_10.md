# Quiz: Module 10 - Azure RBAC and Subscriptions
## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What is the scope hierarchy in Azure from largest to smallest?
*   A) Subscription -> Resource Group -> Resource -> Management Group
*   B) Management Group -> Subscription -> Resource Group -> Resource
*   C) Resource -> Resource Group -> Subscription -> Management Group
*   D) Tenant -> Resource -> Resource Group -> Subscription
*   **Correct Answer:** B) Inheritance flows from Management Groups down to Subscriptions, Resource Groups, and individual Resources.
*   **Distractor Analysis:**
    *   *Why correct:* Inheritance flows from Management Groups down to Subscriptions, Resource Groups, and individual Resources.
    *   A and C represent incorrect orderings. D starts at resource.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **subscriptions.**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
B) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
C) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
D) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within cloud operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **subscriptions.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **subscriptions.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **subscriptions.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **subscriptions.**.


---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
A) terraform apply
C) gcloud compute instances list
D) kubectl get pods -n production
B) aws s3 sync local_dir s3://my-bucket
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Azure RBAC and Subscriptions** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **Azure RBAC and Subscriptions**, you must mitigate the risk of **Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
B) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Block Public Access configurations and enforce access control via IAM or signed URLs. mitigates the risk of Storing sensitive corporate documents in publicly readable cloud buckets, leading to data breaches..
    * *Why B is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why D is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.
    * *Why C is incorrect:* This does not address the security vulnerability of Publicly Exposed Storage Buckets.

