# Quiz: Module 01 - Resource Hierarchy
## Course: CIS-4329_Google_Cloud (4329_Google_Cloud - Google Cloud Associate Cloud Engineer)

---

**Question 1**
You want to receive an email notification if your Google Cloud spending exceeds $500 for the current month. You set up a budget and an alert threshold. What happens to your resources if the spending reaches $501?
A) All resources are immediately suspended to prevent further charges.
B) Compute instances are shut down, but storage remains active.
C) The resources continue to run normally, and you receive an email alert.
D) The project is automatically deleted.
*   **Correct Answer:** C) The resources continue to run normally, and you receive an email alert.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Budgets in GCP only trigger notifications (emails or Pub/Sub messages). They do not cap spending or suspend resources natively without custom automation.
    *   *Why B is incorrect:* GCP does not selectively shut down compute resources based on simple budget alerts.
    *   *Why D is incorrect:* GCP will never delete a project simply for crossing a billing threshold.

---

---

**Question 2**
At which level of the Google Cloud resource hierarchy are billing accounts attached to pay for consumed resources?
A) Organization level
B) Folder level
C) Project level
D) Resource level
*   **Correct Answer:** C) Project level
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While Organizations *own* Billing Accounts, the actual linkage that pays for a running VM happens by associating the Billing Account with the specific Project.
    *   *Why B is incorrect:* Folders are used to group projects for IAM and policy inheritance, not for direct billing linkages.
    *   *Why D is incorrect:* Individual resources (like a single VM) do not have their own billing accounts attached; they inherit the billing link from their parent Project.

---

---

**Question 3**
A systems administrator or developer needs to **execute the infrastructure plan to provision or modify resources defined in the configuration files**. Which of the following commands is the most appropriate to execute?
A) terraform apply
C) aws s3 sync local_dir s3://my-bucket
B) kubectl get pods -n production
D) gcloud compute instances list
*   **Correct Answer:** A) terraform apply
*   **Distractor Analysis:**
    * *Why A is correct:* The `terraform apply` command is directly designed to execute the infrastructure plan to provision or modify resources defined in the configuration files.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Resource Hierarchy** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.


---

**Question 5**
When designing a system for **Resource Hierarchy**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
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

