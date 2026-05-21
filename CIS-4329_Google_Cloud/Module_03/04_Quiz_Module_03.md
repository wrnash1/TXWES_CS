# Quiz: Module 03 - GKE
## Course: CIS-4329_Google_Cloud (4329_Google_Cloud - Google Cloud Associate Cloud Engineer)

---

**Question 1**
You are managing a fleet of Compute Engine instances. You need to capture the exact state of a data disk right before a major software upgrade, so you can quickly roll back if the upgrade fails. What is the most efficient Google Cloud feature to use?
A) Create a Custom Image of the disk.
B) Create a Snapshot of the disk.
C) Export the disk to a Cloud Storage bucket.
D) Use Database Migration Service.
*   **Correct Answer:** B) Create a Snapshot of the disk.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While an image *could* be used to create new identical VMs, snapshots are specifically designed for incremental backups and point-in-time state capture for existing disks.
    *   *Why C is incorrect:* Exporting takes significantly longer and is used for moving disks out of GCP or deep archiving, not for quick pre-upgrade backups.
    *   *Why D is incorrect:* DMS is for database migrations, not backing up raw Compute Engine persistent disks.

---

---

**Question 2**
When deploying a Kubernetes application on Google Cloud, you want to avoid managing the underlying Compute Engine nodes (VMs) entirely. You only want to focus on your containers and pay only for the CPU and memory your pods request. Which service should you choose?
A) GKE Standard Cluster
B) GKE Autopilot Cluster
C) Compute Engine Managed Instance Group (MIG)
D) App Engine Flexible Environment
*   **Correct Answer:** B) GKE Autopilot Cluster
*   **Distractor Analysis:**
    *   *Why A is incorrect:* In a GKE Standard cluster, you are responsible for managing the node pools and you pay for the underlying VMs regardless of whether your pods use all their capacity.
    *   *Why C is incorrect:* MIGs manage raw Virtual Machines, not Kubernetes pods/containers.
    *   *Why D is incorrect:* App Engine Flex runs containers, but it is a PaaS offering, not a Kubernetes environment. GKE Autopilot is the specific Kubernetes offering that abstracts node management.

---

---

**Question 3**
A systems administrator or developer needs to **list all active container pods running in the production namespace of the Kubernetes cluster**. Which of the following commands is the most appropriate to execute?
B) gcloud compute instances list
D) aws s3 sync local_dir s3://my-bucket
A) kubectl get pods -n production
C) terraform apply
*   **Correct Answer:** A) kubectl get pods -n production
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `kubectl get pods -n production` command is directly designed to list all active container pods running in the production namespace of the Kubernetes cluster.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **GKE** in a production environment, you encounter a system alert indicating a **IAM Access Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
B) Set up billing alerts, delete unused volumes, and configure auto-scaling scale-down policies.
D) Reboot the physical machine and wait for services to reload.
C) Check the VPC route table for an Internet Gateway path and verify that the security group allows incoming traffic.
*   **Correct Answer:** A) Review the user's IAM policies and attach the specific policy granting permissions for the resource action.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The user account or service role lacks the explicit IAM permissions required to execute the API call. The appropriate fix is to Review the user's IAM policies and attach the specific policy granting permissions for the resource action..
    * *Why B is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of IAM Access Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of IAM Access Denied.


---

**Question 5**
When designing a system for **GKE**, you must mitigate the risk of **Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Enable Block Public Access configurations and enforce access control via IAM or signed URLs.
*   **Correct Answer:** A) Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce temporary credentials (STS), rotate keys regularly, and never hardcode API keys in repositories. mitigates the risk of Developers committing plain-text cloud access keys to public source code repositories, allowing full account takeover..
    * *Why C is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why D is incorrect:* This does not address the security vulnerability of Compromised Access Keys.
    * *Why B is incorrect:* This does not address the security vulnerability of Compromised Access Keys.

