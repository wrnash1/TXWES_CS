# Video Script: Module 04 — Cloud Storage (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Introduction (1 minute)

Welcome to Module 04. This module covers Google Cloud Storage — GCP's object
storage service and one of the most versatile services in the entire platform.

Cloud Storage is used for everything from serving website assets to archiving
compliance records to staging data for analytics pipelines. It integrates with
nearly every other GCP service.

In Part 1 we cover the storage classes, bucket configuration, object lifecycle
management, and access control. In Part 2 we go hands-on with the console and
gcloud CLI and cover signed URLs and data transfer options.

---

## Segment 2 — Cloud Storage Fundamentals (3 minutes)

### Object Storage vs. Block Storage

Cloud Storage is object storage, not block storage. This is a fundamental
distinction:

- **Block storage** (Compute Engine Persistent Disk): Low-level, mounts as a
  filesystem, read/write at the byte level. Used as VM disks.
- **Object storage** (Cloud Storage): Files stored as discrete objects with
  metadata. Accessed via HTTP API or CLI. Not mountable as a filesystem without
  a special adapter.

Object storage is ideal for:

- Large, unstructured data (images, videos, log files)
- Data that is written once and read many times
- Long-term archival
- Serving static website content
- Input/output data for batch processing

### Buckets and Objects

Every piece of data in Cloud Storage is an **object**. Objects are stored in
**buckets**.

- A **bucket** is a container for objects. Buckets have globally unique names —
  no two buckets in all of GCP (across all projects and customers) can share
  the same name.
- An **object** consists of data (the file contents) plus metadata (name, size,
  content type, custom attributes, etc.).
- Object names can include slashes, which creates the appearance of a directory
  hierarchy. However, there are no actual directories — it is all a flat
  namespace.

### Key Bucket Properties

When creating a bucket you configure:

- **Name** — Globally unique; used in the bucket URL
- **Location type** — Regional, dual-region, or multi-region
- **Storage class** — Default class for new objects
- **Access control** — Uniform (IAM only) or fine-grained (IAM + ACLs)
- **Versioning** — Keep multiple versions of objects
- **Encryption** — Google-managed or customer-managed (CMEK)

---

## Segment 3 — Storage Classes (4 minutes)

Cloud Storage has four storage classes designed for different access frequency
and retention patterns. All classes offer the same latency and durability
(eleven nines — 99.999999999%).

### Standard Storage

- **Best for**: Frequently accessed data, short-term storage
- **Monthly storage cost**: Highest of the four classes
- **Retrieval cost**: None
- **Minimum storage duration**: None

Use Standard for data accessed regularly — active application data, frequently
read files, hot data for analytics.

### Nearline Storage

- **Best for**: Data accessed less than once per month
- **Monthly storage cost**: Lower than Standard
- **Retrieval cost**: Per-GB retrieval fee applies
- **Minimum storage duration**: 30 days

Use Nearline for backups, disaster recovery data, or content you might access
monthly. If you delete an object before 30 days, you are still charged for
30 days.

### Coldline Storage

- **Best for**: Data accessed less than once per quarter (90 days)
- **Monthly storage cost**: Lower than Nearline
- **Retrieval cost**: Higher per-GB retrieval fee than Nearline
- **Minimum storage duration**: 90 days

Use Coldline for compliance archives, long-term backups accessed rarely.

### Archive Storage

- **Best for**: Data accessed less than once per year
- **Monthly storage cost**: Lowest of all classes
- **Retrieval cost**: Highest retrieval fee; retrieval latency in milliseconds
  (still not tape — objects are available immediately)
- **Minimum storage duration**: 365 days

Use Archive for regulatory compliance data, legal holds, and true cold archives.
Note: Archive class still provides millisecond access — it is not tape storage.
The cost model penalizes frequent access, not access speed.

### Comparison Table

| Class | Min Duration | Best Access Pattern | Storage Cost | Retrieval Cost |
|---|---|---|---|---|
| Standard | None | Daily/hourly | Highest | None |
| Nearline | 30 days | Monthly | Medium | Low |
| Coldline | 90 days | Quarterly | Low | Medium |
| Archive | 365 days | Yearly | Lowest | Highest |

**ACE Exam Tip:** The ACE exam frequently presents cost-optimization scenarios.
Know which class to recommend based on stated access frequency. Minimum
storage duration charges are a common exam trap.

---

## Segment 4 — Object Lifecycle Management (3 minutes)

Lifecycle policies let you automatically transition objects between storage
classes or delete objects based on age or other conditions — without writing
any code.

### Lifecycle Rules

A lifecycle rule has two components:

- **Condition** — When the rule applies
- **Action** — What to do when the condition is met

#### Conditions

- `age` — Object is older than N days
- `createdBefore` — Object was created before a specific date
- `isLive` — Applies only to live or noncurrent (versioned) objects
- `matchesStorageClass` — Object is in a specific storage class
- `numNewerVersions` — Number of newer versions of this object that exist

#### Actions

- `SetStorageClass` — Transition to a different storage class
- `Delete` — Delete the object (or noncurrent version)

### Example Lifecycle Policy

A common pattern for log archival:

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {"age": 30, "matchesStorageClass": ["STANDARD"]}
      },
      {
        "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
        "condition": {"age": 90, "matchesStorageClass": ["NEARLINE"]}
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365}
      }
    ]
  }
}
```

This policy transitions objects from Standard to Nearline at 30 days, to
Coldline at 90 days, and deletes them at 1 year.

**ACE Exam Tip:** Lifecycle policies apply to existing and future objects.
When you set a policy, it is evaluated against all current objects.

---

## Segment 5 — Access Control (2 minutes)

### IAM vs. ACLs

Cloud Storage supports two access control systems that can coexist, but GCP
recommends uniform bucket-level access (IAM only) for new buckets.

- **Uniform bucket-level access (IAM)**: All access is controlled via IAM
  policies on the bucket. Applies to all objects. Consistent, auditable.
  Recommended.
- **Fine-grained access (IAM + ACLs)**: Each object can have its own ACL
  in addition to bucket-level IAM. More granular but harder to audit.
  Legacy mode for interoperability with older applications.

### Key IAM Roles for Cloud Storage

- `roles/storage.admin` — Full control of buckets and objects
- `roles/storage.objectAdmin` — Full control of objects; no bucket management
- `roles/storage.objectCreator` — Upload objects; cannot read or delete
- `roles/storage.objectViewer` — Read objects; no modification
- `roles/storage.legacyBucketReader` — Read bucket metadata and list objects

### Making a Bucket or Object Public

To make all objects in a bucket publicly readable:

```bash
gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
  --member=allUsers \
  --role=roles/storage.objectViewer
```

**ACE Exam Tip:** Using uniform bucket-level access prevents ACLs from being
used on individual objects, which makes the security model simpler and more
auditable. The exam often tests whether you know to use uniform access for
new architectures.

---

## Summary — Part 1

In Part 1 we covered:

- Cloud Storage fundamentals: objects, buckets, and global namespace
- The four storage classes: Standard, Nearline, Coldline, Archive
- When to use each class and the minimum storage duration charges
- Object lifecycle policies: conditions and actions for automated tiering
- Access control: IAM uniform access vs. fine-grained ACLs

In Part 2 we cover signed URLs, Pub/Sub notifications, data transfer
options, and the gcloud CLI for Cloud Storage.

See you in Part 2.

---

End of Part 1 — Module 04

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/storage/docs
