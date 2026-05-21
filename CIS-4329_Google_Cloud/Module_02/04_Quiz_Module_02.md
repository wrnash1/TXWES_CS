# Quiz: Module 02 - Compute/Storage
## Course: CIS-4329_Google_Cloud (4329_Google_Cloud - Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your company has 500 terabytes of historical financial records that must be retained for 7 years to comply with government regulations. You expect to access this data at most once a year during an audit. Which Google Cloud Storage class is the most cost-effective choice for this requirement?
A) Standard Storage
B) Nearline Storage
C) Coldline Storage
D) Archive Storage
*   **Correct Answer:** D) Archive Storage
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Standard is for frequently accessed, "hot" data and has the most expensive storage-at-rest costs.
    *   *Why B is incorrect:* Nearline is optimized for data accessed roughly once a month (like recent backups).
    *   *Why C is incorrect:* Coldline is optimized for data accessed roughly once a quarter (every 90 days). Archive is the absolute cheapest storage for data accessed less than once a year.

---

---

**Question 2**
You need to perform a massive batch-processing job that involves rendering 1,000 video files. The rendering software is designed to automatically retry a video if a server crashes. Which Compute Engine option will allow you to complete this task with the lowest possible compute costs?
A) E2 standard instances
B) Compute Engine instances with sustained use discounts
C) Spot (Preemptible) instances
D) App Engine standard environment
*   **Correct Answer:** C) Spot (Preemptible) instances
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Standard on-demand instances charge full price.
    *   *Why B is incorrect:* Sustained use discounts automatically apply when a VM runs for most of the month, but they are significantly less of a discount than Spot pricing.
    *   *Why D is incorrect:* App Engine is a Platform-as-a-Service for hosting web applications, not a raw compute instance for heavy video rendering batch jobs. Spot instances offer up to 90% off standard pricing, with the caveat that Google can terminate them at any time—perfect for fault-tolerant batch jobs.

---

---

**Question 3**
A systems administrator or developer needs to **query the cloud API to retrieve a list of all active virtual machines in the project**. Which of the following commands is the most appropriate to execute?
D) aws s3 sync local_dir s3://my-bucket
B) kubectl get pods -n production
A) gcloud compute instances list
C) terraform apply
*   **Correct Answer:** A) gcloud compute instances list
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `gcloud compute instances list` command is directly designed to query the cloud API to retrieve a list of all active virtual machines in the project.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Compute/Storage** in a production environment, you encounter a system alert indicating a **Cloud Billing Spike** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Correct Answer:** A) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Billing Spike.
    * *Why A is correct:* Because Idle or over-provisioned virtual machine instances and orphan storage volumes are running continuously. The appropriate fix is to Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies..


---

**Question 5**
When designing a system for **Compute/Storage**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..

