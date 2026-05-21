# Quiz: Module 15 – Migration to GCP: Transfer Service and Migrate for Compute Engine
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your company needs to migrate 800 TB of archive data from an on-premises data center to Cloud Storage. Your internet uplink is 500 Mbps shared with production traffic. Transferring 800 TB over a 500 Mbps connection would take approximately 13 days of continuous transfer at full bandwidth — which is not feasible given production traffic constraints. Which migration tool is most appropriate?

A) Storage Transfer Service with the on-premises agent installed on a local server to upload files directly over the internet.
B) `gsutil -m cp -r /data gs://destination-bucket` run in parallel across multiple on-premises servers to maximize throughput.
C) Transfer Appliance — request one or more physical appliances from Google, load the 800 TB of data onto the appliance locally, and ship it to Google for ingestion into Cloud Storage.
D) Cloud VPN with a dedicated tunnel reserved exclusively for data transfer at full 500 Mbps throughput.

*   **Correct Answer:** C) Transfer Appliance — request one or more physical appliances from Google, load the 800 TB of data onto the appliance locally, and ship it to Google for ingestion into Cloud Storage.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Storage Transfer Service with the on-premises agent uploads data over your internet connection — the same constrained 500 Mbps link. This does not solve the 13-day transfer time problem and competes with production traffic. Transfer Appliance bypasses the network entirely for the bulk data load.
    *   *Why B is incorrect:* `gsutil -m cp` also uses your internet connection. Distributing the upload across multiple servers increases parallelism but is still bounded by the total available internet bandwidth. It does not reduce the fundamental transfer time limitation of 500 Mbps shared bandwidth.
    *   *Why D is incorrect:* Cloud VPN tunnels operate over the internet and are bounded by the same internet uplink capacity — a VPN tunnel does not provision additional bandwidth. Even with a dedicated VPN tunnel at full 500 Mbps, the 13-day transfer time remains unchanged.

---

**Question 2**
Your organization runs a fleet of VMware vSphere VMs in an on-premises data center. You need to migrate these VMs to Compute Engine with minimal downtime during cutover. The VMs run production workloads that must remain online until the final cutover window. Which GCP migration tool is designed for this use case?

A) Storage Transfer Service — use it to copy the VM disk images from on-premises to Cloud Storage, then import them as Compute Engine custom images.
B) Migrate for Compute Engine — it continuously replicates VM disk data to GCP in the background, allowing you to test the migrated VM in GCP before cutting over with only minutes of downtime.
C) Database Migration Service — migrate the VM's application data to Cloud SQL and then redeploy the application on a new Compute Engine instance.
D) `gcloud compute images import` — run this command against each VM's exported OVA file to convert it to a Compute Engine image.

*   **Correct Answer:** B) Migrate for Compute Engine — it continuously replicates VM disk data to GCP in the background, allowing you to test the migrated VM in GCP before cutting over with only minutes of downtime.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Copying VM disk images to Cloud Storage and importing them as custom images is a valid approach for offline migration, but it requires the VM to be shut down during the image export to ensure consistency — causing significant downtime. Migrate for Compute Engine uses live replication so the source VM stays running until the cutover moment.
    *   *Why C is incorrect:* Database Migration Service migrates relational database data — it does not migrate entire VM workloads. This approach also requires re-architecting the application to use Cloud SQL, which is a re-platform strategy, not the lift-and-shift approach described in the scenario.
    *   *Why D is incorrect:* `gcloud compute images import` is a one-time import from a static disk image file. It requires the source VM to be shut down to export a consistent image, results in a long import process, and provides no mechanism for continuous replication or low-downtime cutover.

---

**Question 3**
Your team needs to keep a Cloud Storage bucket continuously synchronized with data produced by a partner organization's Amazon S3 bucket. New objects are added to the S3 bucket daily. You want the synchronization to happen automatically every 24 hours without manual intervention. Which Storage Transfer Service configuration achieves this?

A) Create a one-time transfer job from the S3 bucket to the Cloud Storage bucket and run it manually each morning.
B) Create a recurring transfer job in Storage Transfer Service with the S3 bucket as the source, the Cloud Storage bucket as the destination, and a daily schedule.
C) Write a Cloud Function triggered by a Cloud Scheduler job that calls `gsutil rsync s3://partner-bucket gs://gcp-bucket` daily.
D) Configure an S3 bucket event notification that publishes to Pub/Sub, which triggers a Cloud Function to copy each new object to Cloud Storage as it arrives.

*   **Correct Answer:** B) Create a recurring transfer job in Storage Transfer Service with the S3 bucket as the source, the Cloud Storage bucket as the destination, and a daily schedule.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A one-time transfer job requires manual execution each morning. This introduces human error risk (forgetting to run it) and does not meet the "automatic without manual intervention" requirement. Storage Transfer Service's scheduling feature is designed specifically to eliminate this manual step.
    *   *Why C is incorrect:* `gsutil rsync` with S3 as the source requires AWS credentials to be available in the Cloud Function's environment, adds custom code to maintain, and runs from a Cloud Function instance that may have lower throughput than Storage Transfer Service's managed infrastructure. The native STS solution is simpler and more reliable.
    *   *Why D is incorrect:* An event-driven architecture that copies each object individually as it is created is more complex to implement and maintain than a scheduled batch sync. It also requires the partner to configure S3 notifications to your Pub/Sub topic, which depends on partner cooperation and adds cross-account IAM configuration. STS's scheduled transfer is the simpler and recommended approach.

---

**Question 4**
Your company is migrating a production MySQL database from an on-premises server to Cloud SQL for MySQL. The database is 2 TB and receives continuous write traffic. The migration must keep the source database online and serving traffic until the final cutover. Downtime must be less than 5 minutes. Which tool and approach is correct?

A) Use `mysqldump` to export the database, transfer the dump file to Cloud Storage, and import it into Cloud SQL — then update the application connection string during a maintenance window.
B) Use Database Migration Service with a continuous migration type (change data capture), validate that the Cloud SQL replica is consistent, then cut over by updating the application connection string.
C) Use Storage Transfer Service to copy the MySQL data files from on-premises storage to a Cloud Storage bucket, then attach the bucket as a Cloud SQL external data source.
D) Create a Cloud SQL read replica pointing to the on-premises database and promote it when ready to cut over.

*   **Correct Answer:** B) Use Database Migration Service with a continuous migration type (change data capture), validate that the Cloud SQL replica is consistent, then cut over by updating the application connection string.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `mysqldump` requires stopping writes or accepting inconsistency during the export, which for a 2 TB continuously written database could take hours. During the import window, the source database must be frozen or the dump will be stale. Total downtime would far exceed 5 minutes, violating the requirement.
    *   *Why C is incorrect:* Storage Transfer Service moves files between object storage systems — it does not understand MySQL data file formats and cannot create a consistent, importable Cloud SQL database from raw MySQL data directory files. MySQL data files require specific recovery procedures and cannot be directly attached as a Cloud SQL data source.
    *   *Why D is incorrect:* Cloud SQL read replicas replicate from other Cloud SQL instances — they cannot replicate directly from an on-premises MySQL server. Database Migration Service is specifically designed to bridge on-premises MySQL to Cloud SQL using standard MySQL replication protocols.

---

**Question 5**
A startup has its entire application running on AWS EC2 instances. They want to migrate to GCP Compute Engine using a lift-and-shift approach that minimizes application changes. The application uses a custom Linux kernel module that is compiled into the running OS. Which migration approach preserves the existing OS and kernel configuration most completely?

A) Export the EC2 instances as AMI snapshots, convert them to VMDK format using an open-source tool, then import them using `gcloud compute images import`.
B) Use Migrate for Compute Engine, which supports AWS EC2 as a source and performs continuous block-level disk replication — preserving the exact OS, kernel, and application configuration of each instance.
C) Provision new Compute Engine VMs from the nearest equivalent GCP-provided OS image and reinstall all applications and kernel modules from scratch.
D) Use the Cloud Build service to containerize the application and deploy it to Cloud Run, which abstracts away the underlying OS entirely.

*   **Correct Answer:** B) Use Migrate for Compute Engine, which supports AWS EC2 as a source and performs continuous block-level disk replication — preserving the exact OS, kernel, and application configuration of each instance.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While converting AMI snapshots to VMDK and importing them is technically feasible, it requires the source instance to be stopped during snapshot export (causing downtime), involves manual format conversion steps, and has no mechanism for ongoing replication or low-downtime cutover. Migrate for Compute Engine supports EC2 directly as a source with live replication.
    *   *Why C is incorrect:* Provisioning new VMs from GCP OS images and reinstalling applications is a re-platform approach, not lift-and-shift. Reinstalling a custom kernel module requires rebuilding it for the new kernel version, which may involve code changes and significant testing effort — exactly what the startup wants to avoid.
    *   *Why D is incorrect:* Containerizing the application with Cloud Build and deploying to Cloud Run is a re-architecture approach that requires significant code changes, cannot use a custom kernel module (containers share the host kernel), and fundamentally changes how the application is packaged and run. This is the opposite of lift-and-shift.
