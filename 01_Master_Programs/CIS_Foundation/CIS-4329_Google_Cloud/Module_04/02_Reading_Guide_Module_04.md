# Reading Guide: Module 04 — Cloud Storage

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4329 &BULL; GOOGLE CLOUD PLATFORM (GCP) CLOUD ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This reading guide covers Google Cloud Storage — GCP's object storage service.
Cloud Storage appears on the ACE exam in topics ranging from data management
and access control to cost optimization and event-driven architecture.

**Estimated Reading Time:** 45–55 minutes

---

## Section 1 — Object Storage Fundamentals

### 1.1 Buckets

A bucket is the top-level container in Cloud Storage. Bucket properties:

- **Name**: Globally unique across all of GCP; used in URLs
  (`gs://bucket-name` and `storage.googleapis.com/bucket-name`)
- **Location**: Regional, dual-region, or multi-region
- **Default storage class**: Applied to new objects unless overridden
- **Access control mode**: Uniform (IAM only) or fine-grained (IAM + ACLs)
- **Versioning**: Enabled or disabled
- **Retention policy**: Minimum retention period (for compliance)
- **Encryption**: Google-managed keys (GMEK) or customer-managed (CMEK)

### 1.2 Location Types

| Location type | Description | Use Case |
|---|---|---|
| Regional | Single region (e.g., us-central1) | Lowest latency, lowest cost |
| Dual-region | Two paired regions (e.g., NAM4 = Iowa + Virginia) | HA within a geo |
| Multi-region | Continental area (us, eu, asia) | Global availability, highest cost |

### 1.3 Objects

An object is an immutable unit of data in Cloud Storage. Objects consist of:

- **Object data**: The actual file bytes
- **Object metadata**: Key-value attributes (content-type, size, custom headers)
- **Object name**: The "path" within the bucket (slashes create logical folders)
- **Generation number**: Unique per version when versioning is enabled

Objects can be up to 5 TB in size. Objects cannot be partially updated —
any modification replaces the entire object.

---

## Section 2 — Storage Classes

### 2.1 Class Comparison

| Class | Min Duration | Retrieval Fee | Typical Use |
|---|---|---|---|
| Standard | None | None | Frequently accessed data |
| Nearline | 30 days | Per GB | Monthly backups |
| Coldline | 90 days | Per GB (higher) | Quarterly archives |
| Archive | 365 days | Per GB (highest) | Annual or compliance data |

### 2.2 Minimum Storage Duration

Minimum duration is a billing concept, not a restriction. You can delete a
Coldline object before 90 days — but you are charged for the full 90 days.

Example: You store 1 TB in Coldline for 45 days then delete it. You are billed
for 90 days of storage.

### 2.3 Dual-Region and Multi-Region Replication

- **Regional buckets**: Data stored in one region. Lower cost. Use for workloads
  requiring data residency in a specific location.
- **Dual-region**: Replicates data across two paired regions. Provides
  redundancy without global distribution.
- **Multi-region** (`us`, `eu`, `asia`): Replicates data across multiple
  regions in a continent. Highest availability; higher cost; data stays within
  the continental boundary.

---

## Section 3 — Object Lifecycle Management

### 3.1 Lifecycle Rule Structure

A lifecycle configuration is a JSON document containing an array of rules.
Each rule has a condition and an action.

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {
          "type": "SetStorageClass",
          "storageClass": "NEARLINE"
        },
        "condition": {
          "age": 30,
          "matchesStorageClass": ["STANDARD"]
        }
      },
      {
        "action": {
          "type": "Delete"
        },
        "condition": {
          "age": 365,
          "isLive": true
        }
      },
      {
        "action": {
          "type": "Delete"
        },
        "condition": {
          "numNewerVersions": 3,
          "isLive": false
        }
      }
    ]
  }
}
```

### 3.2 Condition Reference

| Condition | Type | Description |
|---|---|---|
| `age` | Integer | Days since object creation |
| `createdBefore` | Date string | Object created before this date |
| `isLive` | Boolean | True = live version; false = noncurrent |
| `matchesStorageClass` | Array | Object is in one of these classes |
| `numNewerVersions` | Integer | Noncurrent versions with N newer versions |
| `matchesPrefix` | Array | Object name starts with one of these prefixes |
| `matchesSuffix` | Array | Object name ends with one of these suffixes |

### 3.3 Applying Lifecycle Configuration

```bash
# Write lifecycle config to a file
cat > lifecycle.json << 'EOF'
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {"age": 30}
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365}
      }
    ]
  }
}
EOF

# Apply to a bucket
gcloud storage buckets update gs://BUCKET_NAME \
  --lifecycle-file=lifecycle.json

# View current lifecycle config
gcloud storage buckets describe gs://BUCKET_NAME \
  --format='value(lifecycle)'
```

---

## Section 4 — Access Control

### 4.1 Uniform vs. Fine-Grained Access

#### Uniform bucket-level access (recommended)

- All access controlled through IAM policies on the bucket
- ACLs cannot be set on individual objects
- Consistent, auditable, simpler to manage
- Enforces uniform access to all objects in the bucket
- Can be enabled and, for 90 days after enablement, disabled (then permanent)

```bash
# Enable uniform bucket-level access
gcloud storage buckets update gs://BUCKET_NAME \
  --uniform-bucket-level-access
```

#### Fine-grained access (legacy)

- Allows per-object ACLs in addition to bucket-level IAM
- Required for some legacy applications and interoperability scenarios
- Harder to audit; two overlapping systems to manage

### 4.2 Making Buckets or Objects Public

```bash
# Make all current and future objects public
gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
  --member=allUsers \
  --role=roles/storage.objectViewer

# Make a single object public (fine-grained mode only)
gcloud storage objects add-iam-policy-binding gs://BUCKET_NAME/OBJECT \
  --member=allUsers \
  --role=roles/storage.objectViewer
```

### 4.3 Retention Policies

A retention policy sets a minimum duration that objects must be retained before
they can be deleted. Used for compliance requirements.

```bash
# Set a 7-year retention policy
gcloud storage buckets update gs://BUCKET_NAME \
  --retention-period=7y

# Lock the retention policy (irreversible — cannot reduce or remove)
gcloud storage buckets update gs://BUCKET_NAME \
  --lock-retention-policy
```

---

## Section 5 — Signed URLs

### 5.1 Overview

Signed URLs grant time-limited access to an object without requiring a Google
account. The URL contains:

- The object path
- An expiration timestamp
- A cryptographic signature from a service account

### 5.2 Generating Signed URLs

```bash
# Using gcloud with the attached service account
gcloud storage sign-url gs://BUCKET_NAME/OBJECT \
  --duration=1h \
  --region=us-central1

# For upload (PUT) operation
gcloud storage sign-url gs://BUCKET_NAME/upload-target.txt \
  --duration=30m \
  --method=PUT \
  --content-type=text/plain \
  --region=us-central1
```

Signed URLs support HTTP methods: GET (download), PUT (upload), DELETE.

### 5.3 V4 Signing

Use V4 signed URLs (the current standard):

- Maximum expiration: 7 days
- More secure than the deprecated V2 format
- Required for requests signed without a service account key
  (using the IAM signing API)

---

## Section 6 — Object Versioning

### 6.1 How Versioning Works

When versioning is enabled:

- Each object has a **generation number** (assigned at creation or overwrite)
- Overwriting an object creates a new generation; the old generation becomes
  a noncurrent version
- Deleting an object inserts a **delete marker** (noncurrent), making the
  object invisible; it is not permanently deleted
- Permanently deleting requires specifying the generation number

### 6.2 Versioning Commands

```bash
# Enable versioning
gcloud storage buckets update gs://BUCKET_NAME --versioning

# List all versions
gcloud storage ls -a gs://BUCKET_NAME/

# Restore a noncurrent version (copy to a new object)
gcloud storage cp \
  "gs://BUCKET_NAME/OBJECT#GENERATION" \
  gs://BUCKET_NAME/OBJECT

# Permanently delete a specific version
gcloud storage rm "gs://BUCKET_NAME/OBJECT#GENERATION"
```

---

## Section 7 — Data Transfer Options

### 7.1 Transfer Method Comparison

| Method | Best For | Max Scale |
|---|---|---|
| gcloud storage / gsutil | Scripts, small-medium transfers | TBs |
| Storage Transfer Service | Online transfers from S3, Azure, HTTP | PBs |
| Transfer Appliance | Offline, on-premises large datasets | Up to 1 PB |
| BigQuery Data Transfer | Scheduled SaaS to BigQuery loads | Varies |

### 7.2 Storage Transfer Service

```bash
# Create a transfer job from AWS S3 to Cloud Storage
gcloud transfer jobs create \
  s3://source-bucket \
  gs://destination-bucket \
  --source-creds-file=aws-creds.json \
  --schedule-starts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
```

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| Bucket | Top-level container in Cloud Storage; globally unique name |
| Object | Unit of data stored in a bucket; includes data and metadata |
| Storage class | Billing tier based on access frequency |
| Standard | Highest-cost class; for frequently accessed data |
| Nearline | 30-day minimum; for monthly access patterns |
| Coldline | 90-day minimum; for quarterly access patterns |
| Archive | 365-day minimum; lowest cost; for annual or less access |
| Lifecycle policy | Rules for automatic storage class transitions or deletions |
| Signed URL | Time-limited URL granting access without requiring GCP credentials |
| Versioning | Feature retaining previous object versions on overwrite/delete |
| Uniform bucket-level access | IAM-only access control mode (no per-object ACLs) |
| Retention policy | Minimum hold duration for objects (compliance use) |
| Storage Transfer Service | Managed service for large-scale data transfers |
| Transfer Appliance | Physical device for offline petabyte-scale data uploads |

---

## ACE Exam Focus Areas — Module 04

- Select the correct storage class for a described access frequency.
- Identify minimum storage duration charges for Nearline, Coldline, Archive.
- Design a lifecycle policy to transition and delete objects automatically.
- Distinguish uniform bucket-level access from fine-grained ACLs.
- Describe signed URLs and when to use them vs. IAM.
- Explain how versioning interacts with lifecycle policies.
- Choose the appropriate data transfer method based on data volume and source.
- Know that Cloud Storage provides millisecond access on all storage classes
  (Archive is not tape).

---

## Further Reading

- Cloud Storage overview: cloud.google.com/storage/docs
- Storage classes: cloud.google.com/storage/docs/storage-classes
- Lifecycle management: cloud.google.com/storage/docs/lifecycle
- Signed URLs: cloud.google.com/storage/docs/access-control/signed-urls
- Storage Transfer Service: cloud.google.com/storage-transfer/docs

## 9. Supplemental Resources

**1. Google Cloud Documentation — Cloud Storage Storage Classes**
<https://cloud.google.com/storage/docs/storage-classes>
Detailed comparison of Standard, Nearline, Coldline, and Archive storage
classes including minimum storage durations, retrieval fees, and use case
guidance. Essential for ACE exam cost optimization questions.

**2. Google Cloud Skills Boost — Cloud Storage: Qwik Start**
<https://www.cloudskillsboost.google/focuses/1836>
Hands-on lab covering bucket creation, object upload, access control
configuration, and lifecycle policy setup using both the Console and
`gcloud storage` CLI commands.

**3. Google Cloud Documentation — Object Lifecycle Management**
<https://cloud.google.com/storage/docs/lifecycle>
Complete reference for lifecycle configuration rules including all supported
conditions (`age`, `createdBefore`, `isLive`, `matchesStorageClass`,
`numNewerVersions`) and action types with JSON and YAML examples.
