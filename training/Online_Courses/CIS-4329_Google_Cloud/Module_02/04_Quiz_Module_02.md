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

**Question 3**
A systems administrator or developer needs to **synchronize local files directly to a cloud object storage bucket**. Which of the following commands is the most appropriate to execute?
D) kubectl get pods -n production
A) aws s3 sync local_dir s3://my-bucket
C) terraform apply
B) gcloud compute instances list
*   **Correct Answer:** A) aws s3 sync local_dir s3://my-bucket
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `aws s3 sync local_dir s3://my-bucket` command is directly designed to synchronize local files directly to a cloud object storage bucket.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Compute/Storage** in a production environment, you encounter a system alert indicating a **Cloud Instance Unreachable** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
B) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
D) Reboot the physical machine and wait for services to reload.
A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why B is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why D is incorrect:* This action does not resolve the root cause of Cloud Instance Unreachable.
    * *Why A is correct:* Because The virtual machine is inside a private subnet without routing to the internet, or the security group blocks the connection. The appropriate fix is to Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic..


---

**Question 5**
When designing a system for **Compute/Storage**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..

