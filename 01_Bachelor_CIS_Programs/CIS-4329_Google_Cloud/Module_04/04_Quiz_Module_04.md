# Quiz: Module 04 — Cloud Storage

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
This quiz covers storage classes, lifecycle policies, access control, signed
URLs, object versioning, and data transfer.

---

## Question 1

A media company stores master video files that are used for production daily.
After 6 months of production, the files are moved to a secondary archive but
may need to be retrieved quickly if re-editing is requested (roughly once per
year). After 3 years, the files are no longer needed. Which storage class
assignment best optimizes cost while meeting these requirements?

- A) Standard for the first 6 months, then Archive after
- B) Standard for the first 6 months, then Nearline after, then delete at 3 years
- C) Standard for the first 6 months, then Coldline after, then delete at 3 years
- D) Nearline from day 1, Archive after 6 months

**Correct Answer:** C

**Explanation:** The files are accessed roughly once per year after 6 months,
which aligns with Coldline (access less than once per quarter). Archive's minimum
365-day duration and highest retrieval cost would make re-editing requests
expensive. Standard for the active 6-month period is appropriate. Nearline
(option B) requires 30-day minimum but is designed for monthly access — less
cost-efficient than Coldline for yearly access.

---

## Question 2

An object is stored in a Coldline bucket. After 45 days, the object is deleted.
How many days of Coldline storage is the customer billed for?

- A) 45 days
- B) 90 days
- C) 0 days (Coldline deletes are free)
- D) 180 days

**Correct Answer:** B

**Explanation:** Coldline storage has a 90-day minimum storage duration. If an
object is deleted before 90 days, you are still charged for the full 90 days.
This minimum duration is a cost model, not a restriction — you can delete the
object, but the billing continues to the minimum.

---

## Question 3

A developer needs to allow a third-party vendor to upload a report file to a
private Cloud Storage bucket. The vendor does not have a Google account and
the upload window should expire in 2 hours. What is the correct solution?

- A) Grant the vendor `roles/storage.objectCreator` on the bucket using their
     email address
- B) Make the bucket publicly writable by adding `allUsers` as objectCreator
- C) Generate a signed URL with PUT method and 2-hour duration and share it
     with the vendor
- D) Create a temporary Google account for the vendor and grant bucket access

**Correct Answer:** C

**Explanation:** Signed URLs allow unauthenticated access to a specific object
for a defined time period. A PUT-method signed URL allows uploading to that
specific object path without requiring GCP credentials. Making the bucket
publicly writable (option B) creates a major security risk. Creating temporary
accounts (option D) adds unnecessary management overhead.

---

## Question 4

You are designing a compliance archiving system for a financial institution.
Regulations require that audit logs be retained for exactly 7 years and cannot
be deleted or modified by any user, including administrators, before that
period ends. Which Cloud Storage features should you use?

- A) Standard storage with a lifecycle policy that deletes after 7 years
- B) Archive storage with a locked retention policy of 7 years
- C) Coldline storage with object versioning enabled
- D) Multi-region Standard storage with IAM deny policies

**Correct Answer:** B

**Explanation:** A locked retention policy prevents objects from being deleted
or modified before the retention period expires — even by administrators.
Locking the retention policy makes it permanent and tamper-proof. Archive
storage minimizes storage cost for rarely accessed compliance data. A lifecycle
policy (option A) can still be overridden by admins. Object versioning (option C)
does not prevent deletion after recovery.

---

## Question 5

A bucket is configured with uniform bucket-level access. A developer has
`roles/storage.objectViewer` on the bucket. Which operations can they perform?

- A) Read objects and delete objects, but not list the bucket contents
- B) Read objects and list bucket contents, but not upload or delete
- C) Full control of all objects in the bucket
- D) List bucket contents only; cannot read object data

**Correct Answer:** B

**Explanation:** `roles/storage.objectViewer` includes `storage.objects.get`
(download objects) and `storage.objects.list` (list objects in bucket). It does
not include `storage.objects.create`, `storage.objects.delete`, or any bucket
management permissions. The viewer cannot upload, overwrite, or delete objects.

---

## Question 6

You need to configure a lifecycle policy that transitions objects from Standard
to Nearline after 30 days and deletes noncurrent (versioned) object versions
after 7 days. Which conditions should the delete rule use?

- A) `age: 7` (deletes all objects older than 7 days)
- B) `age: 7, isLive: false` (deletes noncurrent versions older than 7 days)
- C) `numNewerVersions: 1` (deletes objects with one newer version)
- D) `age: 37` (deletes objects older than 37 days total)

**Correct Answer:** B

**Explanation:** Using `age: 7` with `isLive: false` targets only noncurrent
(versioned) objects that have been noncurrent for 7 or more days. Without
`isLive: false`, the rule would delete live objects at 7 days, which is not
the intent. `numNewerVersions` (option C) deletes based on version count, not
age.

---

## Question 7

A data engineering team needs to migrate 500 TB of data from AWS S3 to Cloud
Storage. The migration should be automated and scheduled to run nightly to keep
the destination in sync. Which GCP service is best suited for this?

- A) gcloud storage rsync run manually in Cloud Shell
- B) Storage Transfer Service with a scheduled recurring transfer job
- C) Transfer Appliance shipped to AWS
- D) Cloud Data Fusion pipeline with manual execution

**Correct Answer:** B

**Explanation:** Storage Transfer Service is purpose-built for large-scale,
automated transfers from AWS S3, Azure Blob Storage, and HTTP sources to Cloud
Storage. It supports scheduled, recurring transfers and handles petabyte-scale
data. Running gcloud manually (option A) is not automated and does not scale to
500 TB. Transfer Appliance (option C) is for physical, offline data, not online
S3 transfers.

---

## Question 8

Object versioning is enabled on a Cloud Storage bucket. An object named
`report.pdf` exists in the bucket. A user runs `gcloud storage rm
gs://bucket/report.pdf`. What is the result?

- A) The object and all its versions are permanently deleted
- B) A delete marker is created; the live version becomes noncurrent; no data
     is destroyed
- C) The command fails because versioning is enabled
- D) The oldest version of the object is deleted

**Correct Answer:** B

**Explanation:** When versioning is enabled, a standard delete operation creates
a delete marker, making the object invisible to normal listings. The previous
live version becomes a noncurrent version and is not destroyed. To permanently
delete all versions, you must specify the generation number of each version
explicitly.

---

## Question 9

Which Cloud Storage feature allows you to be notified when a new file is
uploaded to a bucket, enabling downstream processing such as triggering a
Cloud Function?

- A) Object Change Notification (polling API)
- B) Cloud Storage Pub/Sub notifications
- C) Cloud Monitoring alert on storage metrics
- D) Cloud Logging audit log export

**Correct Answer:** B

**Explanation:** Cloud Storage Pub/Sub notifications publish a message to a
Pub/Sub topic whenever specified events occur on a bucket (OBJECT_FINALIZE,
OBJECT_DELETE, etc.). A Cloud Function, Cloud Run service, or other subscriber
can consume these messages to trigger downstream processing. This is the
standard event-driven pattern for Cloud Storage.

---

## Question 10

A Cloud Storage bucket stores objects that are accessed frequently for the
first 90 days after creation, then almost never accessed again. The company
wants to minimize storage costs while retaining all objects indefinitely.
What lifecycle configuration achieves this?

- A) Delete all objects after 90 days
- B) Transition objects from Standard to Archive after 90 days
- C) Transition objects from Standard to Nearline after 30 days, then to
     Archive after 90 days
- D) No lifecycle policy is needed; Archive is the default storage class

**Correct Answer:** B

**Explanation:** Transitioning directly from Standard to Archive after 90 days
is the most cost-effective approach when objects are frequently accessed for
the first 90 days and then almost never accessed. Archive has the lowest storage
cost and a 365-day minimum duration, but since the objects are being retained
indefinitely, that minimum is not a concern. Option C adds an unnecessary
Nearline tier.

---

End of Quiz — Module 04

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

---

### Question 11 (5 points)

You enable uniform bucket-level access on an existing Cloud Storage bucket
that previously used fine-grained ACLs. What happens to existing object-level
ACLs?

- A) Existing ACLs are preserved and continue to function alongside IAM
- B) Existing object ACLs are locked and can no longer be read or modified;
   access is controlled exclusively by IAM bucket-level policies
- C) All objects in the bucket are immediately deleted for security
- D) The bucket reverts to fine-grained mode after 30 days if no IAM bindings
   are added

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) When uniform bucket-level access is enabled, object ACLs are disabled and cannot be read or modified; IAM is the sole access control mechanism.
  - C) Enabling uniform access has no effect on object data; no objects are deleted.
  - D) Uniform bucket-level access can be disabled within 90 days of enabling, but it does not automatically revert; it is a deliberate configuration change.

---

### Question 12 (5 points)

A Cloud Storage bucket has object versioning enabled. A lifecycle rule is
configured with `numNewerVersions: 3`. An object has 5 versions. How many
versions will be retained after the lifecycle rule runs?

- A) All 5 versions are retained — lifecycle rules only apply to non-versioned
   objects
- B) The 3 most recent versions are retained; the 2 older versions are deleted
- C) All versions older than 3 days are deleted
- D) Only 1 version (the current live version) is retained

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Lifecycle rules fully support versioned objects; `numNewerVersions` is specifically designed to manage version counts.
  - C) `numNewerVersions: 3` is a count-based condition, not a time-based condition; age-based deletion uses the `age` condition.
  - D) `numNewerVersions: 3` retains the 3 most recent versions (not just 1); versions beyond that count are eligible for deletion.

---

### Question 13 (5 points)

What is the minimum storage duration charge for an object stored in Nearline
storage that is deleted after only 10 days?

- A) 10 days — you only pay for what you use
- B) 30 days — Nearline has a 30-day minimum storage duration
- C) 90 days — Nearline uses the same minimum as Coldline
- D) 0 days — deletion is always free in Nearline

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Nearline imposes a 30-day minimum storage charge regardless of when the object is actually deleted; deleting at 10 days incurs 30 days of charges.
  - C) Coldline has a 90-day minimum, not Nearline; each storage class has its own minimum duration (Nearline: 30 days, Coldline: 90 days, Archive: 365 days).
  - D) While object deletion itself has no direct API fee, the minimum storage duration means the storage charge continues to the minimum even after deletion.

---

### Question 14 (5 points)

A developer uses `gcloud storage cp gs://source-bucket/file.txt
gs://dest-bucket/file.txt`. The two buckets are in different GCP projects but
the same region. What network charges apply?

- A) Egress charges apply because data leaves the source project
- B) No egress charges — transfers between buckets in the same region within
   GCP are free
- C) Standard internet egress rates apply because the transfer goes through
   Google's public API
- D) Charges apply only if the destination bucket is in a different zone

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Egress charges for Cloud Storage are based on destination geography, not project boundaries; same-region bucket-to-bucket transfers within GCP do not incur egress fees.
  - C) The transfer does use the Google API, but same-region GCP-to-GCP data movement is billed at $0 for network egress.
  - D) Cloud Storage buckets are regional resources and do not have zone affinity; zone is not a factor in Storage egress pricing.

---

### Question 15 (5 points)

You need to grant a mobile application the ability to directly upload user
profile photos to a specific path in a private Cloud Storage bucket. Users
do not have Google accounts. Each upload should be scoped to a unique
object path and expire after 15 minutes. What is the correct approach?

- A) Make the bucket publicly writable with `allUsers` as objectCreator
- B) Generate a Signed URL with PUT method, specific object path, and
   15-minute expiration for each upload
- C) Create a service account key, embed it in the mobile app, and use it
   to authenticate uploads
- D) Grant `roles/storage.objectCreator` to `allAuthenticatedUsers` on the
   bucket

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Granting `allUsers` as objectCreator allows any internet user to upload to any path in the bucket — a critical security vulnerability.
  - C) Embedding service account keys in mobile apps is a severe security risk; keys can be extracted from the app binary and used to make unlimited API calls.
  - D) `allAuthenticatedUsers` requires a Google account, which contradicts the requirement that users do not have Google accounts, and it grants bucket-wide upload access rather than per-object scoped access.

---

### Question 16 (5 points)

A team wants to replicate a Cloud Storage bucket from `us-central1` to
`europe-west1` for disaster recovery. Changes made in either region should
automatically sync to the other. Which Cloud Storage feature supports this?

- A) Bucket replication via a Pub/Sub notification and Cloud Function
- B) Dual-region buckets using a specific paired-region designation
- C) Multi-region buckets using the `eu` multi-region location
- D) Cross-region replication using the Storage Transfer Service scheduled
   every 5 minutes

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) A custom Pub/Sub + Cloud Function replication pipeline is a valid DIY approach but requires significant maintenance; GCP's native dual-region feature provides built-in automatic replication.
  - C) The `eu` multi-region covers European regions collectively but does not specifically pair `us-central1` (which is in North America) with `europe-west1`; dual-region pairs are geographically specific.
  - D) Storage Transfer Service scheduled every 5 minutes would introduce replication lag and not be truly bidirectional; dual-region buckets replicate synchronously within the pair.

---

### Question 17 (5 points)

What happens to a Cloud Storage lifecycle rule transition from Standard to
Nearline if an object's `age` is set to 30 days and the object already has
`storageClass: NEARLINE` applied manually before the rule fires?

- A) The object is transitioned to Standard first, then back to Nearline by
   the lifecycle rule
- B) The lifecycle rule is a no-op for that object — lifecycle transitions can
   only move objects to a colder storage class, not back to the same class
- C) The lifecycle rule overwrites the manual storage class assignment and
   re-applies Nearline
- D) The lifecycle rule fails with an error because the object is already in
   Nearline

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Lifecycle rules cannot transition objects to a warmer (more expensive) storage class; there is no mechanism to move from Nearline back to Standard via lifecycle policy.
  - C) Cloud Storage lifecycle rules are evaluated against the current object state; a rule targeting Nearline is already satisfied if the object is in Nearline and does not re-apply the transition.
  - D) The lifecycle rule does not produce an error; it simply evaluates the condition and finds nothing to do when the object is already at the target class.

---

### Question 18 (5 points)

A Cloud Storage bucket stores sensitive medical records. The organization
requires that the encryption keys be managed by the customer and stored in
Cloud KMS, not by Google. Which Cloud Storage configuration provides this?

- A) Server-side encryption with Google-managed keys (GMEK) — this is the
   default
- B) Customer-supplied encryption keys (CSEK) stored in Cloud KMS
- C) Customer-managed encryption keys (CMEK) with a Cloud KMS key ring
   configured on the bucket
- D) Client-side encryption using application-layer AES-256 before upload

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) GMEK is the default and means Google controls the encryption keys; it does not satisfy the requirement for customer-managed keys.
  - B) CSEK means the customer supplies the actual raw key bytes with each API request; those keys are not stored in Cloud KMS — the customer must manage the key bytes directly, which is operationally complex.
  - D) Client-side encryption satisfies the requirement technically but is not a Cloud Storage configuration feature; it requires custom application logic and does not integrate with GCP's key management audit trail.

---

### Question 19 (5 points)

What is the effect of enabling `requesterPays` on a Cloud Storage bucket?

- A) Only the bucket owner is charged for all operations; requesters are never
   billed
- B) Requesters who access the bucket must specify a billing project; egress
   and operation charges are billed to the requester's project rather than
   the bucket owner's project
- C) The bucket becomes publicly accessible and all costs are paid by Google
- D) Read operations are charged to the requester; write operations are still
   charged to the bucket owner

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `requesterPays` is specifically designed to shift access costs from the bucket owner to the requester; without it, all costs fall on the bucket owner.
  - C) `requesterPays` does not change the bucket's access control; private buckets remain private and still require IAM authorization.
  - D) `requesterPays` applies to all access costs (reads, writes, and egress) associated with accessing the bucket, not just reads.

---

### Question 20 (5 points)

A team has a Cloud Storage bucket in the `us` multi-region. They want to
ensure that objects are never stored outside the United States for data
residency compliance. Which statement is correct?

- A) The `us` multi-region guarantees data is stored only in US regions
- B) Using the `us` multi-region with a CMEK key in a US region is required
   for full compliance
- C) The `us` multi-region may store data in Canada or Mexico; use
   `us-central1` regional storage for strict US-only residency
- D) Cloud Storage does not provide data residency guarantees under any
   configuration

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) While CMEK adds key management control, the `us` multi-region itself already constrains data to US locations; adding CMEK addresses key residency, not object data residency.
  - C) The `us` multi-region is specifically scoped to United States locations; GCP guarantees data remains within the US boundary for this multi-region designation.
  - D) Cloud Storage location configurations (regional, dual-region, multi-region) do provide data residency guarantees as part of GCP's contractual commitments.
