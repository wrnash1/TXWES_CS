# Reading Guide: Module 08 — Amazon S3 and Storage Services

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

---

## Introduction

AWS provides three distinct storage paradigms: object storage (S3), block storage (EBS), and file storage (EFS, FSx). Each paradigm serves different access patterns, concurrency models, and performance requirements. Understanding when to use each — and which configuration options within each service — is essential for both the SAA-C03 exam and real-world architecture. This guide provides the reference tables, decision frameworks, and exam patterns needed to answer storage scenario questions accurately.

---

## Section 1: S3 Storage Classes

### 1.1 Storage Class Comparison Table

| Storage Class | AZ Count | Min Duration | Retrieval Time | Retrieval Fee | Best Use Case |
|---------------|----------|--------------|----------------|---------------|---------------|
| S3 Standard | >= 3 | None | Milliseconds | None | Frequently accessed data |
| S3 Intelligent-Tiering | >= 3 | None (frequent tier) | Milliseconds | None | Unknown or changing access patterns |
| S3 Standard-IA | >= 3 | 30 days | Milliseconds | Per GB | Infrequent access, multi-AZ needed |
| S3 One Zone-IA | 1 | 30 days | Milliseconds | Per GB | Infrequent, reproducible data |
| S3 Glacier Instant Retrieval | >= 3 | 90 days | Milliseconds | Per GB | Quarterly access, instant retrieval |
| S3 Glacier Flexible Retrieval | >= 3 | 90 days | 1 min–12 hours | Per GB | Infrequent bulk archive |
| S3 Glacier Deep Archive | >= 3 | 180 days | 12–48 hours | Per GB | Long-term compliance archives |

### 1.2 S3 Intelligent-Tiering Access Tiers

| Tier | Triggered After | Retrieval | Monitoring Fee |
|------|----------------|-----------|----------------|
| Frequent Access | Default (new objects) | Immediate | Yes (per object) |
| Infrequent Access | 30 days without access | Immediate | Yes |
| Archive Instant Access | 90 days without access | Immediate | Yes |
| Archive Access (optional) | 90–180 days (configurable) | 3–5 hours | Yes |
| Deep Archive Access (optional) | 180+ days (configurable) | 12 hours | Yes |

The optional Archive and Deep Archive tiers must be explicitly activated. There are no retrieval fees for the Frequent and Infrequent Access tiers.

### 1.3 Storage Class Decision Framework

```
Is the data accessed frequently (multiple times per week)?
  Yes → S3 Standard

Is the access pattern unpredictable?
  Yes → S3 Intelligent-Tiering

Is the data accessed less than monthly but needs immediate retrieval?
  Is multi-AZ redundancy required?
    Yes → S3 Standard-IA
    No (reproducible data) → S3 One Zone-IA

Is the data accessed only quarterly with instant retrieval required?
  Yes → S3 Glacier Instant Retrieval

Is the data archived with bulk retrieval acceptable in 3–12 hours?
  Yes → S3 Glacier Flexible Retrieval

Is the data a regulatory archive retained 7+ years, almost never accessed?
  Yes → S3 Glacier Deep Archive
```

---

## Section 2: S3 Lifecycle Policies

### 2.1 Lifecycle Rule Action Types

| Action Type | Description | Example |
|-------------|-------------|---------|
| Transition | Move object to a different storage class after N days | Move to Standard-IA after 30 days |
| Expiration | Delete current object version after N days | Delete after 2555 days |
| Noncurrent version expiration | Delete old versions after N days (versioning enabled) | Delete versions older than 90 days |
| Abort incomplete multipart uploads | Clean up abandoned uploads after N days | Delete incomplete uploads after 7 days |

### 2.2 Lifecycle Transition Order

Transitions must follow the waterfall — you cannot transition from a lower-tier class back to a higher-tier class:

```
Standard → Standard-IA → One Zone-IA → Glacier Instant → Glacier Flexible → Glacier Deep Archive
```

Constraints:

- Objects must remain in Standard for at least 30 days before transitioning to Standard-IA or One Zone-IA
- Objects must remain in Standard-IA for at least 30 days before transitioning to Glacier Instant Retrieval

### 2.3 Example Lifecycle Policy — Log Retention

| Day Range | Storage Class | Rationale |
|-----------|---------------|-----------|
| 0–30 | S3 Standard | Frequent debug access |
| 30–365 | S3 Standard-IA | Occasional compliance review |
| 365–2555 | S3 Glacier Deep Archive | Long-term retention |
| Day 2555 | Expire (delete) | 7-year retention completed |

---

## Section 3: S3 Versioning and Replication

### 3.1 Versioning States

| State | PUT Behavior | DELETE Behavior |
|-------|-------------|-----------------|
| Unversioned (default) | Overwrites existing object | Permanently deletes |
| Versioning-enabled | Creates new version (old version retained) | Creates delete marker (recoverable) |
| Versioning-suspended | New objects receive null version ID | Null version is overwritten |

Versioning cannot be disabled once enabled — only suspended. This is permanent by design to protect data integrity.

### 3.2 Replication Comparison

| Feature | Cross-Region Replication (CRR) | Same-Region Replication (SRR) |
|---------|-------------------------------|-------------------------------|
| Scope | Different AWS Regions | Same AWS Region |
| Versioning required | Yes (both buckets) | Yes (both buckets) |
| Existing objects replicated | No (S3 Batch Operations required) | No (S3 Batch Operations required) |
| Storage class override | Configurable | Configurable |
| Primary use cases | Geo-redundancy, DR, latency | Log aggregation, account isolation |
| Replication Time Control (RTC) | Available (15-min SLA) | Not available |

### 3.3 S3 Object Lock

S3 Object Lock prevents object versions from being deleted or overwritten for a fixed amount of time or indefinitely. Two retention modes:

- **Governance Mode**: Most users cannot delete; designated administrators with special permissions can
- **Compliance Mode**: No user, including root, can delete or shorten the retention period

Object Lock is used for regulatory compliance requiring WORM (Write Once Read Many) storage.

---

## Section 4: S3 Event Notifications

### 4.1 Event Notification Target Comparison

| Target | Pattern | Fan-out | Best For |
|--------|---------|---------|----------|
| Amazon SNS | Publish-subscribe | Yes | Notify multiple consumers |
| Amazon SQS | Queue | No | Decoupled, ordered processing |
| AWS Lambda | Direct invocation | No | Immediate serverless processing |
| Amazon EventBridge | Event routing | Yes (multiple rules) | Complex routing and filtering |

### 4.2 S3 Select

S3 Select executes SQL-compatible SELECT statements against individual S3 objects server-side, returning only the matching data subset. Supported formats: CSV, JSON, Parquet, and GZIP or BZIP2-compressed CSV/JSON.

| Feature | S3 Select | Amazon Athena |
|---------|-----------|---------------|
| Scope | Single object | Multiple objects across a bucket |
| Query language | SQL subset (SELECT only) | Full ANSI SQL |
| Setup required | None | Table definitions in Glue Data Catalog |
| Cost | Per GB scanned and returned | Per TB scanned |
| Best for | Filter a large single file before processing | Analytics across many S3 objects |

---

## Section 5: EBS Volume Types

### 5.1 EBS Volume Type Reference

| Type | Category | Max IOPS | Max Throughput | Durability | Boot | Primary Use |
|------|----------|----------|----------------|------------|------|-------------|
| gp3 | General Purpose SSD | 16,000 | 1,000 MB/s | 99.8–99.9% | Yes | Default for most workloads |
| gp2 | General Purpose SSD (legacy) | 16,000 | 250 MB/s | 99.8–99.9% | Yes | Legacy — migrate to gp3 |
| io2 Block Express | Provisioned IOPS SSD | 256,000 | 4,000 MB/s | 99.999% | Yes | Mission-critical databases |
| io1 | Provisioned IOPS SSD | 64,000 | 1,000 MB/s | 99.8–99.9% | Yes | High-IOPS (older gen) |
| st1 | Throughput Optimized HDD | 500 IOPS | 500 MB/s | 99.8–99.9% | No | Big data, log processing |
| sc1 | Cold HDD | 250 IOPS | 250 MB/s | 99.8–99.9% | No | Infrequent cold sequential |

### 5.2 EBS Decision Framework

```
Boot volume required?
  Yes → gp3 (default), io2 if high-IOPS DB

Needs > 16,000 IOPS or 99.999% durability?
  Yes → io2 Block Express

Mission-critical DB with sustained high IOPS?
  Yes → io2 or io1

Large sequential workload (Hadoop, log pipeline)?
  Throughput priority → st1
  Cost priority → sc1

Default workload (app server, dev, general)?
  → gp3
```

### 5.3 gp3 vs. gp2

| Feature | gp3 | gp2 |
|---------|-----|-----|
| Baseline IOPS | 3,000 (independent of size) | 3 IOPS/GB (min 100) |
| Max throughput | 1,000 MB/s | 250 MB/s |
| IOPS independent of size | Yes | No |
| Cost | ~20% cheaper than gp2 | Baseline |

gp3 is strictly superior in almost all cases. AWS recommends migrating all gp2 volumes to gp3.

### 5.4 EBS Characteristics

- EBS volumes exist within a single Availability Zone and can only be attached to instances in the same AZ
- EBS volumes can be modified (resized, type changed) while attached and in use — no downtime required
- EBS snapshots are stored in S3 and are regional; they can be copied to other regions
- EBS Multi-Attach (io1/io2 only): one volume attached to up to 16 Nitro instances in the same AZ; applications must handle concurrent write coordination

---

## Section 6: Amazon EFS

### 6.1 EFS vs. EBS vs. S3

| Feature | EFS | EBS | S3 |
|---------|-----|-----|-----|
| Storage paradigm | File (NFS) | Block | Object |
| Concurrent access | Thousands of instances | 1 (except Multi-Attach) | Unlimited |
| AZ scope | Regional (mount targets per AZ) | Single AZ | Regional |
| OS | Linux only | Linux and Windows | All (HTTP) |
| Elasticity | Auto-scales with usage | Fixed size (modifiable) | Unlimited |
| Use case | Shared home dirs, content, ML | OS volumes, databases | Backups, data lakes, static files |

### 6.2 EFS Performance and Throughput Modes

| Setting | Options | When to Use |
|---------|---------|-------------|
| Performance Mode | General Purpose (default) | Most workloads; lowest latency |
| Performance Mode | Max I/O | Highly parallelized (10,000+ clients); higher latency acceptable |
| Throughput Mode | Elastic (default, recommended) | Auto-scales based on workload |
| Throughput Mode | Provisioned | Specify fixed throughput independent of file system size |

### 6.3 EFS Storage Classes

| Class | Access | Automatic Lifecycle |
|-------|--------|---------------------|
| EFS Standard | Frequent access | N/A |
| EFS Standard-IA | Infrequent access | Files not accessed in 7/14/30/60/90 days |
| EFS One Zone | Frequent (single AZ) | N/A |
| EFS One Zone-IA | Infrequent (single AZ) | Same lifecycle options |

EFS One Zone provides ~47% cost reduction vs. EFS Standard. Use for dev/test or reproducible data.

---

## Section 7: AWS Backup

### 7.1 Supported Resources

AWS Backup centralizes backup for: EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, S3, Storage Gateway, and VMware virtual machines.

### 7.2 Key Concepts

| Concept | Description |
|---------|-------------|
| Backup Plan | Policy defining frequency, retention window, and copy rules |
| Backup Vault | Encrypted container for recovery points |
| Recovery Point | A backup of a specific resource at a point in time |
| Vault Lock (Governance) | Prevents deletion except by designated administrators |
| Vault Lock (Compliance) | Permanently immutable; no account can delete during lock period |
| Cross-Account Backup | Copy to a separate account for isolation from account-level events |
| Cross-Region Backup | Copy to a different region for disaster recovery |

### 7.3 Vault Lock Compliance Use Case

Compliance mode vault lock is used when regulatory requirements mandate immutable backups. During the compliance lock period, no account — including root — can delete recovery points or shorten the retention period. This satisfies HIPAA, SEC 17a-4, and other regulations requiring WORM-compliant storage.

---

## Section 8: SAA-C03 Exam Tips for Module 08

**Exam Tip 1 — Minimum duration charges:**
Standard-IA and One Zone-IA have a 30-day minimum. Glacier Instant and Flexible have 90-day minimums. Glacier Deep Archive has a 180-day minimum. Deleting before minimum still incurs the minimum charge.

**Exam Tip 2 — One Zone-IA for reproducible data only:**
One Zone-IA is never appropriate for compliance data, unique data, or disaster recovery purposes. It is appropriate for thumbnails, derived files, and on-premises backup replicas.

**Exam Tip 3 — CRR vs. SRR by scope:**
"Different region" always means CRR. "Same region, different account" or "same region log aggregation" means SRR.

**Exam Tip 4 — Replication does not copy existing objects:**
S3 replication only applies to objects written after the rule is configured. S3 Batch Operations is required for pre-existing objects.

**Exam Tip 5 — gp3 default, io2 for highest IOPS:**
"High IOPS," "sub-millisecond," "mission-critical database" → io2. "Boot volume," "general workload" → gp3. "Sequential big data" → st1. "Lowest cost cold" → sc1.

**Exam Tip 6 — EFS for shared concurrent Linux access:**
Multiple EC2 instances needing simultaneous shared file access → EFS (Linux) or FSx for Windows File Server (Windows). EBS cannot be shared across instances without Multi-Attach limitations.

**Exam Tip 7 — AWS Backup vault lock for WORM compliance:**
Immutable backups that cannot be deleted even by root → AWS Backup with Vault Lock in Compliance Mode.

**Exam Tip 8 — S3 Select for single-object filtering:**
S3 Select filters within one object server-side. Amazon Athena queries across many objects. The distinction is object count: one → S3 Select, many → Athena.

---

## Section 9: Key CLI Commands

List all S3 buckets:

```bash
aws s3api list-buckets \
  --query "Buckets[*].{Name:Name,Created:CreationDate}" \
  --output table
```

Copy with specific storage class:

```bash
aws s3 cp myfile.csv s3://my-bucket/data/myfile.csv \
  --storage-class STANDARD_IA
```

Create a lifecycle configuration:

```bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-log-bucket \
  --lifecycle-configuration '{
    "Rules": [{
      "ID": "log-retention",
      "Status": "Enabled",
      "Filter": {"Prefix": "logs/"},
      "Transitions": [
        {"Days": 30, "StorageClass": "STANDARD_IA"},
        {"Days": 365, "StorageClass": "DEEP_ARCHIVE"}
      ],
      "Expiration": {"Days": 2555}
    }]
  }'
```

Enable versioning:

```bash
aws s3api put-bucket-versioning \
  --bucket my-bucket \
  --versioning-configuration Status=Enabled
```

Run S3 Select on a CSV object:

```bash
aws s3api select-object-content \
  --bucket my-bucket \
  --key data/records.csv \
  --expression "SELECT * FROM S3Object WHERE region = 'West'" \
  --expression-type SQL \
  --input-serialization '{"CSV": {"FileHeaderInfo": "USE"}}' \
  --output-serialization '{"CSV": {}}' \
  output.csv
```

---

## Section 10: Study Checklist

- [ ] Name all seven S3 storage classes, minimum storage duration, and retrieval time for each
- [ ] Draw the lifecycle transition order from Standard to Deep Archive
- [ ] Explain the difference between CRR and SRR with a use case for each
- [ ] Describe what happens to existing objects when replication is first configured
- [ ] Compare S3 Select and Amazon Athena on scope and use case
- [ ] List EBS volume types and identify the correct type for boot, mission-critical DB, big data, and cold storage
- [ ] Explain when EFS is required instead of EBS and what OS limitation applies
- [ ] Describe AWS Backup vault lock Compliance Mode and its regulatory use case
- [ ] Run the CLI commands in Section 9 and record the output
- [ ] Complete the Module 08 quiz with a score of at least 80 percent

---

## References

All AWS certification study materials and exam registration: aws.amazon.com/certification

---

## 11. Supplemental Resources

**1. AWS Documentation — Amazon S3 Multipart Upload Overview**
https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html
Complete guide to S3 multipart upload — when to use it, how to initiate, upload, and complete multipart uploads, and CLI/SDK examples — essential for understanding large object upload patterns tested on SAA-C03.

**2. AWS Skill Builder — Amazon EBS: Elastic Block Store Deep Dive**
https://skillbuilder.aws/learn/course/external/view/elearning/678/amazon-ebs-elastic-block-store-deep-dive
Free course covering EBS volume types (gp3, io2, st1, sc1), performance characteristics, snapshots, encryption, and Multi-Attach — directly supporting Module 08 EBS selection questions.

**3. AWS Documentation — AWS Storage Services Overview (Whitepaper)**
https://docs.aws.amazon.com/whitepapers/latest/aws-storage-services-overview/welcome.html
AWS whitepaper comparing all storage services (S3, EBS, EFS, FSx, Storage Gateway, Snowball) by use case, performance, durability, and access patterns — the definitive reference for storage service selection scenarios on SAA-C03.

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
