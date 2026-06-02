# Video Script — Module 04, Part 1

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Storage — Buckets, Storage Classes, and Object Management

### Estimated Duration: 13–14 minutes

---

## Introduction

Welcome to Module 04. I'm Professor Nash, and today we are covering Cloud Storage — Google's object storage service. Cloud Storage is one of the most fundamental services in GCP. It stores unstructured data: images, videos, log files, backups, static website assets, big data files, and more. It is also where many GCP services — like Dataflow, BigQuery, and Cloud Functions — read and write data.

Cloud Storage is heavily tested on the ACE exam. By the end of this module you will understand buckets, storage classes, the lifecycle policy system, object versioning, signed URLs, retention policies, and IAM for storage. Let's start with the fundamentals.

---

## Section 1: Object Storage Basics

**[SHOW SLIDE: Object storage vs. block storage vs. file storage comparison]**

Before we dig into Cloud Storage, let me clarify what object storage is and why it is different from the disk types we covered in Module 03.

Block storage (like Compute Engine persistent disks) stores data as raw blocks on a virtual drive. You format it with a filesystem, mount it, and interact with it like a local disk. It is good for operating systems and databases.

File storage (like Cloud Filestore) presents a network file system. Multiple VMs can mount the same file system and access it like a shared drive.

Object storage stores data as discrete objects, each identified by a unique key (the object name) within a bucket. Objects are not organized in a true directory hierarchy — the "folder" structure you see in the Console is just a display convention based on the `/` character in object names. Object storage is ideal for data that you write once and read many times: backups, media files, machine learning datasets, archives.

Cloud Storage buckets have no capacity limits. You can store petabytes in a single bucket and pay only for what you actually store.

---

## Section 2: Buckets

**[SHOW CONSOLE: Cloud Storage > Buckets page, then Create Bucket dialog]**

A bucket is the top-level container for your data in Cloud Storage. Every object must belong to a bucket. When you create a bucket, you configure:

**Bucket name** — globally unique across all of Google Cloud. Not just unique in your project or your organization — unique across every GCP customer in the world. Bucket names form part of the public URL for objects, so they must follow DNS naming rules.

**Location type** — where your data is stored:

- Region: stored in a single region (e.g., `us-central1`). Lowest storage cost. Data is replicated across zones within the region.
- Dual-region: stored in two specific regions. Higher durability, lower latency reads from both regions. Higher cost than single region.
- Multi-region: stored redundantly across a large geographic area (e.g., `us` covers multiple US regions). Highest availability. Useful for globally distributed apps.

**Storage class** — the access frequency tier. We will cover this in detail in the next section.

**Access control** — either uniform (all objects in the bucket share bucket-level IAM) or fine-grained (allows object-level ACLs in addition to bucket-level IAM). Google recommends uniform access control.

---

## Section 3: Storage Classes

**[SHOW SLIDE: Storage class comparison table with access frequency, minimum storage duration, cost comparison]**

The storage class determines the cost structure for your data. Cloud Storage has four classes:

### Standard

Use for: data that is accessed frequently — daily or multiple times per day. Examples: website images, user-uploaded content, active application data.

Cost: highest per-GB storage cost, no retrieval fee, no minimum storage duration.

### Nearline

Use for: data accessed approximately once per month. Examples: monthly reports, data backups that you test once a month.

Cost: lower per-GB storage than Standard. Retrieval fee per GB. 30-day minimum storage duration — if you store an object for less than 30 days and delete it, you are billed as if it was stored for 30 days.

### Coldline

Use for: data accessed approximately once per quarter. Examples: disaster recovery backups, quarterly compliance archives.

Cost: lower than Nearline. Higher retrieval fee per GB. 90-day minimum storage duration.

### Archive

Use for: data accessed less than once per year. Examples: 7-year financial records, regulatory archives, long-term audit logs.

Cost: lowest per-GB storage of all classes. Highest retrieval fee. 365-day minimum storage duration.

**[PAUSE — Professor on camera]**

The ACE exam will describe a scenario — "data accessed once a year for 7 years" — and ask you to pick the right storage class. Archive is almost always the answer for anything accessed less than once a year. The key is the access frequency, not the retention duration. And remember: the less frequently accessed classes have minimum storage durations and retrieval fees. If you store something in Archive for one month and then retrieve it, you pay the retrieval fee AND the 365-day minimum storage bill.

### Autoclass

Autoclass is a newer feature that automatically transitions objects between storage classes based on their actual access patterns. Objects that are not accessed move to cheaper classes over time. Objects that are accessed get promoted back to Standard. This is useful when you have a mix of data with unpredictable access patterns and you want GCP to optimize costs automatically without you writing lifecycle policies.

---

## Section 4: Lifecycle Policies

**[SHOW SLIDE: Lifecycle policy diagram — objects aging from Standard to Nearline to Coldline to Archive to Delete]**

**[SHOW CONSOLE: Cloud Storage > Bucket > Lifecycle tab, then rule creation dialog]**

Lifecycle policies automate the management of objects over time. A lifecycle policy is a set of rules attached to a bucket. Each rule has a condition and an action.

Conditions can be based on:

- `age` — number of days since the object was created
- `createdBefore` — objects created before a specific date
- `isLive` — whether the object is the live version or a noncurrent (older) version
- `numNewerVersions` — how many newer versions of the object exist
- `matchesStorageClass` — only apply to objects currently in a specific storage class

Actions:

- `SetStorageClass` — transition the object to a different (typically cheaper) storage class
- `Delete` — permanently delete the object

Example use cases:

- Automatically move log files from Standard to Coldline after 30 days and delete after 1 year
- Delete all noncurrent (old) versions of files after 7 days (object versioning cleanup)
- Move infrequently-accessed data to Archive after 90 days of no access

Here is a lifecycle rule in JSON format:

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
        "condition": {"age": 30}
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365}
      }
    ]
  }
}
```

This policy moves all objects to Coldline after 30 days and deletes them after 365 days.

---

## Closing — Part 1

To summarize Part 1: Cloud Storage is GCP's object storage service. Objects live in buckets. Buckets are globally named and can be regional, dual-region, or multi-regional. Storage classes (Standard, Nearline, Coldline, Archive) trade access cost for storage cost based on access frequency. Lifecycle policies automate object transitions and deletion based on age, versioning, or storage class conditions.

In Part 2 we will cover object versioning, IAM for Cloud Storage, signed URLs, retention policies, and the gsutil and gcloud storage CLI commands.

---

End of Part 1 — Module 04

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
