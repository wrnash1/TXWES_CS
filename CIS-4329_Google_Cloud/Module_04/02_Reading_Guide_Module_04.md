# Reading Guide — Module 04

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Storage — Buckets, Classes, and Lifecycle Policies

### Certification Target: Google Cloud Associate Cloud Engineer

---

## Introduction

Cloud Storage is GCP's fully managed object storage service and a major ACE exam topic. This reading guide covers bucket configuration, storage classes, lifecycle policies, object versioning, signed URLs, retention policies, and the CLI commands for storage management. The exam tests both conceptual knowledge (which storage class for which scenario) and CLI knowledge (correct gsutil and gcloud storage syntax).

---

## 1. Object Storage vs. Other Storage Types

| Storage Type | GCP Service | Best For | Key Characteristic |
|---|---|---|---|
| Object storage | Cloud Storage | Files, blobs, archives, media | Globally accessible, unlimited scale |
| Block storage | Compute Engine Persistent Disks | OS drives, databases | Mountable as filesystem |
| File storage | Cloud Filestore | Shared filesystem for VMs | NFS-compatible |
| In-memory | Cloud Memorystore | Caching, session data | Sub-millisecond latency |

---

## 2. Bucket Configuration

### Bucket Location Types

| Location Type | Example Value | Replication | Best For |
|---|---|---|---|
| Region | `us-central1` | Multiple zones in one region | Single-region workloads, lowest cost |
| Dual-region | `nam4` (Iowa + South Carolina) | Two specific regions | Higher durability with specific region control |
| Multi-region | `us`, `eu`, `asia` | Many regions in continent | Global apps, maximum availability |

### Bucket Name Rules

- Globally unique across all GCP customers
- 3 to 63 characters
- Lowercase letters, numbers, hyphens, and underscores only
- Must start and end with a letter or number
- Cannot contain "google" or misleading domain names
- Names that contain dots must be domain-verified

### Access Control Models

| Model | Description | Recommended |
|---|---|---|
| Uniform bucket-level access | All objects governed by bucket IAM policy only; object ACLs disabled | Yes |
| Fine-grained | Each object can have individual ACLs in addition to bucket IAM | Legacy only |

---

## 3. Storage Classes

### Standard

- Access frequency: Daily or more
- Minimum storage duration: None
- Retrieval fee: None
- Use cases: Active website assets, user-uploaded content, frequently read data, application data

### Nearline

- Access frequency: Approximately once per month
- Minimum storage duration: 30 days
- Retrieval fee: Per-GB fee applies
- Use cases: Monthly reports, monthly disaster recovery drills, data backups verified monthly

### Coldline

- Access frequency: Approximately once per quarter
- Minimum storage duration: 90 days
- Retrieval fee: Per-GB fee (higher than Nearline)
- Use cases: Quarterly compliance archives, disaster recovery backups

### Archive

- Access frequency: Less than once per year
- Minimum storage duration: 365 days
- Retrieval fee: Per-GB fee (highest)
- Use cases: 7-year financial records, regulatory long-term archives, rarely accessed historical data

### Storage Class Cost Comparison

| Class | Storage Cost | Retrieval Cost | Min Duration |
|---|---|---|---|
| Standard | Highest | None | None |
| Nearline | Lower than Standard | Low | 30 days |
| Coldline | Lower than Nearline | Medium | 90 days |
| Archive | Lowest | Highest | 365 days |

### Autoclass

Autoclass automatically transitions objects between Standard, Nearline, Coldline, and Archive based on their actual access patterns. Objects not accessed for 30 days move to Nearline; not accessed for 90 days move to Coldline; not accessed for 365 days move to Archive. When an object is accessed, it is immediately promoted back to Standard. Use Autoclass when access patterns are unpredictable and you want GCP to optimize costs automatically.

---

## 4. Lifecycle Policies

### Policy Structure

A lifecycle policy JSON document contains a `rule` array. Each rule has:

- `action` — what to do: `SetStorageClass` or `Delete`
- `condition` — when to do it

### Condition Types

| Condition | Type | Description |
|---|---|---|
| `age` | Integer (days) | Object is older than N days |
| `createdBefore` | Date string | Object was created before a specific date |
| `isLive` | Boolean | True = live version; False = noncurrent version |
| `numNewerVersions` | Integer | Only apply when N or more newer versions exist |
| `matchesStorageClass` | Array of strings | Only apply to objects with specific current storage class |

### Example: Log Retention Policy

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

### Common Lifecycle Patterns

| Business Requirement | Lifecycle Rule |
|---|---|
| Delete objects after 90 days | `Delete` action, `age: 90` |
| Move to Archive after 1 year | `SetStorageClass: ARCHIVE`, `age: 365` |
| Clean up old object versions | `Delete` action, `isLive: false`, `numNewerVersions: 2` |
| Transition log files to cheapest class over time | Chain of SetStorageClass rules with increasing age |

---

## 5. Object Versioning

When versioning is enabled on a bucket:

- Each upload of an object with an existing name creates a new version, assigned a unique generation number
- The newest upload is the "live" version
- Previous uploads become "noncurrent" versions
- Noncurrent versions are billed at the bucket's storage class rate
- Noncurrent versions can be listed, downloaded, or permanently deleted

### Versioning and Deletion

With versioning disabled: `gcloud storage rm gs://bucket/file.txt` permanently deletes the object.

With versioning enabled: `gcloud storage rm gs://bucket/file.txt` creates a delete marker, making the object appear deleted. The object data is still stored as a noncurrent version. To permanently delete all versions, use the `-a` flag:

```bash
gcloud storage rm -a gs://bucket/file.txt
```

### Managing Version Cost

Enable versioning, then add a lifecycle rule to delete noncurrent versions after N days:

```json
{
  "action": {"type": "Delete"},
  "condition": {"isLive": false, "numNewerVersions": 1, "age": 30}
}
```

This deletes noncurrent versions that are older than 30 days and have at least one newer version.

---

## 6. Signed URLs

| Property | Value |
|---|---|
| Purpose | Temporary access to a specific object without requiring Google credentials |
| Authentication | Cryptographic signature using a service account's private key |
| Supported methods | GET (download), PUT (upload), DELETE |
| Duration | Configurable, maximum 7 days (604800 seconds) |
| Scope | Single specific object path |

### When to Use Signed URLs

- Share a private file with an external partner who has no Google Account
- Allow a user to upload a file directly to Cloud Storage from a browser (avoiding upload through your backend server)
- Provide a download link that expires automatically

### Generating a Signed URL

```bash
gcloud storage sign-url gs://my-bucket/file.txt \
  --duration=24h \
  --private-key-file=service-account-key.json
```

Or using a service account's impersonation (no key file needed):

```bash
gcloud storage sign-url gs://my-bucket/file.txt \
  --duration=1h \
  --impersonate-service-account=sa@project.iam.gserviceaccount.com
```

---

## 7. Retention Policies

### How Retention Policies Work

A retention policy sets a minimum duration objects in a bucket must be retained. Until the retention period expires:

- Objects cannot be deleted
- Objects cannot be overwritten (cannot be replaced with a newer version)
- This restriction applies to ALL users including project owners and Storage Admins

### Locking a Retention Policy

Once you lock a retention policy on a bucket, you cannot:

- Shorten the retention period
- Remove the retention policy
- Delete the bucket unless all objects have met their retention period

Even Google cannot override a locked retention policy. This makes it suitable for legal hold and compliance requirements where evidence of non-tampering is required.

### Retention vs. Versioning vs. Lifecycle

| Feature | Protects Against | Can Admin Override | Use Case |
|---|---|---|---|
| Object versioning | Accidental deletion/overwrite | Yes (admin can delete all versions) | Recovery window |
| Lifecycle policy | N/A — it deletes objects | Yes (admin controls policy) | Cost management |
| Retention policy | All deletions until period expires | No (hard lock, even with locked policy) | Regulatory compliance |

---

## 8. gcloud Storage and gsutil Command Reference

### Bucket Management

| Command | Description |
|---|---|
| `gcloud storage buckets create gs://NAME --location=REGION --storage-class=CLASS` | Create a bucket |
| `gcloud storage buckets describe gs://NAME` | View bucket configuration |
| `gcloud storage buckets update gs://NAME --default-storage-class=NEARLINE` | Change default storage class |
| `gcloud storage buckets update gs://NAME --versioning` | Enable versioning |
| `gcloud storage buckets update gs://NAME --lifecycle-file=policy.json` | Apply lifecycle policy |
| `gcloud storage buckets delete gs://NAME` | Delete an empty bucket |

### Object Operations

| Command | Description |
|---|---|
| `gcloud storage cp FILE gs://BUCKET/` | Upload a file |
| `gcloud storage cp -r FOLDER/ gs://BUCKET/folder/` | Upload a folder recursively |
| `gcloud storage cp gs://BUCKET/file.txt ./` | Download a file |
| `gcloud storage ls gs://BUCKET/` | List objects |
| `gcloud storage ls -a gs://BUCKET/` | List all versions including noncurrent |
| `gcloud storage rm gs://BUCKET/file.txt` | Delete an object |
| `gcloud storage mv gs://BUCKET/old.txt gs://BUCKET/new.txt` | Rename/move an object |

### Access Management

| Command | Description |
|---|---|
| `gcloud storage buckets add-iam-policy-binding gs://BUCKET --member=TYPE:ID --role=ROLE` | Grant a role on a bucket |
| `gcloud storage buckets remove-iam-policy-binding gs://BUCKET --member=TYPE:ID --role=ROLE` | Remove a role from a bucket |
| `gcloud storage buckets get-iam-policy gs://BUCKET` | View bucket IAM policy |

---

## 9. ACE Exam Tips

1. Storage class selection follows access frequency. Monthly access = Nearline. Quarterly access = Coldline. Less than yearly = Archive. Frequently accessed = Standard. Minimum storage durations (30/90/365 days) and retrieval fees apply to Nearline, Coldline, and Archive — important for cost calculations.

2. Lifecycle policies are the automatic solution. When a question asks how to automatically manage storage costs or automatically delete objects after N days, the answer is a lifecycle policy with the appropriate action and condition.

3. Signed URLs are for external access without Google credentials. If a question says the recipient has no Google Account or asks about time-limited access, Signed URLs are the answer. Making a bucket public (`allUsers`) is never the correct answer for sharing with a specific external user.

4. Retention policies enforce hard immutability. Object versioning allows recovery but admins can still permanently delete all versions. Only a retention policy (especially a locked one) prevents deletion by anyone.

5. Uniform bucket-level access is recommended. Fine-grained ACLs are legacy. When a question asks how to simplify access management for a Cloud Storage bucket, enabling uniform access is the correct answer.

6. Multi-region buckets cost slightly more than regional but provide higher availability for globally distributed reads. The `US` multi-region automatically replicates across multiple US regions — not just two.

7. Autoclass is the automatic storage class optimizer. When a question describes unpredictable access patterns and asks how to optimize storage costs without manual intervention, Autoclass is the feature to suggest.

8. Object versioning + lifecycle rules is the cost-safe combination. Enable versioning for recovery capability, then use lifecycle rules to delete noncurrent versions after a reasonable recovery window to prevent unbounded cost growth.

---

## 10. Study Checklist

- [ ] State the four storage classes and their access frequency thresholds, minimum durations, and retrieval fee status
- [ ] Explain the difference between regional, dual-region, and multi-region bucket locations
- [ ] Describe the two access control models for Cloud Storage buckets and state which is recommended
- [ ] Write a lifecycle policy JSON that transitions objects to Nearline at 30 days and deletes at 365 days
- [ ] Explain how object versioning interacts with `gcloud storage rm`
- [ ] Describe the use case for signed URLs and explain why making a bucket public is not equivalent
- [ ] Explain the difference between object versioning and a retention policy for compliance purposes
- [ ] Create a bucket using gcloud storage with a specific storage class and location
- [ ] Upload and list objects in a bucket
- [ ] Apply a lifecycle policy JSON to a bucket
- [ ] Complete the Module 04 lab
- [ ] Take the Module 04 quiz
- [ ] Post your Module 04 discussion response

---

End of Reading Guide — Module 04

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
