### 5. Quiz 3: Deploying Solutions (Question Bank)
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
