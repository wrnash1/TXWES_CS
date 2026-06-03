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
