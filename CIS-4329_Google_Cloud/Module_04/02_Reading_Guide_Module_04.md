# Reading Guide: Module 04 – Cloud Storage: Buckets, Classes, and Lifecycle Policies
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 04 – Cloud Storage: Buckets, Classes, and Lifecycle Policies**! Cloud Storage is GCP's fully managed object storage service. This module covers bucket creation and configuration, choosing the right storage class for your access patterns, enforcing data retention with lifecycle policies, and controlling access with ACLs and IAM. These topics are heavily tested on the ACE exam, particularly the cost-optimization scenarios involving storage class selection.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Storage Classes**: Cloud Storage offers four classes optimized for different access frequencies. **Standard** is for hot, frequently accessed data (no minimum storage duration, highest cost per GB). **Nearline** is for data accessed roughly once per month (30-day minimum). **Coldline** is for data accessed roughly once per quarter (90-day minimum). **Archive** is for data accessed less than once per year (365-day minimum, lowest cost per GB, highest retrieval cost).

*   **Bucket**: The fundamental container in Cloud Storage. All objects (files) are stored in buckets. Buckets have a globally unique name, a geographic location (single region, dual-region, or multi-region), a default storage class, and an IAM policy. Bucket names are part of public URLs, so they must be unique across all GCP customers.

*   **Lifecycle Policy**: A set of rules that automatically transition objects to a cheaper storage class or delete them after a specified number of days or after a certain date. For example: move objects to Nearline after 30 days, move to Coldline after 90 days, delete after 365 days. Lifecycle policies reduce manual storage management.

*   **Object Versioning**: When enabled on a bucket, Cloud Storage preserves a copy of an object each time it is overwritten or deleted. Older versions become noncurrent and can be retrieved or permanently deleted. Versioning protects against accidental overwrites but increases storage costs.

*   **Signed URLs**: Time-limited URLs that grant temporary access to a specific Cloud Storage object without requiring the requester to have a Google Account or IAM role. Signed URLs are the correct way to share private objects with external users for a limited time.

*   **Managed Instance Group (MIG) with Autohealing**: A Compute Engine feature that monitors VM health via an HTTP health check and automatically replaces any instance that fails the check. MIGs also support autoscaling based on CPU utilization, HTTP load, or custom metrics from Cloud Monitoring.

---

### 2. Certification Exam Tips

*   **Storage class selection is a high-frequency exam topic**: Memorize the access frequency thresholds — monthly = Nearline, quarterly = Coldline, yearly or less = Archive. The exam presents cost-optimization scenarios where you must pick the cheapest class that meets the access requirement.

*   **Lifecycle policies automate cost management**: The ACE exam often asks how to automatically reduce storage costs over time. The answer is always a lifecycle policy with `SetStorageClass` actions, not manual management or scripts.

*   **Multi-region buckets vs. dual-region**: Multi-region buckets (like `US` or `EU`) provide the highest availability and lowest latency for globally distributed users but cost slightly more than single-region. Dual-region provides redundancy in two specific regions with a replication SLA.

*   **`gsutil` command family**: Know `gsutil mb gs://BUCKET_NAME` (make bucket), `gsutil cp FILE gs://BUCKET/` (copy), `gsutil ls gs://BUCKET/` (list), `gsutil lifecycle set POLICY.json gs://BUCKET/` (apply lifecycle). The `gcloud storage` command family is the newer equivalent.

*   **Study Resource**: The freeCodeCamp ACE course covers Cloud Storage storage classes, lifecycle rules, and access control with worked examples: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Supplement with the official Cloud Storage documentation for exact minimum storage duration values.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review Cloud Storage storage classes and their pricing characteristics: [Cloud Storage Storage Classes](https://cloud.google.com/storage/docs/storage-classes). Pay close attention to the minimum storage duration and retrieval cost for each class.
*   **Required Reading**: Review lifecycle configuration options including `SetStorageClass` and `Delete` actions: [Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle). Understand how conditions like `age` and `numNewerVersions` work.
*   **Required Video**: Watch the Cloud Storage segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Cloud Storage chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create buckets, upload objects, configure a lifecycle policy, and test access control. Key commands to practice:

*   `gsutil mb -l us-central1 gs://my-bucket-name` — creates a regional bucket
*   `gsutil cp localfile.txt gs://my-bucket-name/` — uploads a file
*   `gsutil lifecycle set lifecycle.json gs://my-bucket-name` — applies a lifecycle policy from a JSON file
*   `gsutil signurl -d 1h keyfile.json gs://my-bucket-name/object.txt` — generates a 1-hour signed URL

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Cloud Storage Storage Classes](https://cloud.google.com/storage/docs/storage-classes) documentation page.
- [ ] Read the [Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle) documentation page.
- [ ] Watch the Cloud Storage segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a bucket, upload objects, apply a lifecycle policy, test signed URLs.
- [ ] Proceed to the weekly quiz.
