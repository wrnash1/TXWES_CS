# Reading Guide: Module 04 - S3: Storage Classes, Lifecycle Policies, and Security

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Introduction

Amazon S3 is the primary object storage service in AWS and one of the most frequently tested services on the SAA-C03 exam. S3 questions appear in every exam domain: cost optimization (storage class selection), resilience (replication and versioning), security (bucket policies, encryption, Block Public Access), and performance (Transfer Acceleration, multipart upload). This reading guide provides the complete reference tables, policy examples, and configuration patterns needed to answer those questions accurately.

---

## Section 1: S3 Storage Classes Reference

### 1.1 Complete Storage Class Comparison Table

| Storage Class | Min Duration | Availability Zones | Availability SLA | Retrieval Fee | Best Use Case |
|---|---|---|---|---|---|
| S3 Standard | None | 3+ | 99.99% | None | Frequently accessed data, web assets |
| S3 Intelligent-Tiering | None | 3+ | 99.9% | None (auto-tiered) | Unknown or changing access patterns |
| S3 Standard-IA | 30 days | 3+ | 99.9% | Per-GB | Infrequent access, backups, DR data |
| S3 One Zone-IA | 30 days | 1 | 99.5% | Per-GB | Reproducible data, secondary backups |
| S3 Glacier Instant Retrieval | 90 days | 3+ | 99.9% | Per-GB | Quarterly access, medical images, news archives |
| S3 Glacier Flexible Retrieval | 90 days | 3+ | 99.99% | Per-GB + retrieval tier | Annual archives, compliance backups |
| S3 Glacier Deep Archive | 180 days | 3+ | 99.99% | Per-GB (highest) | 7+ year retention, regulatory compliance |

All storage classes share the same 11 nines (99.999999999%) durability — this is because durability is about data not being lost, while availability is about data being accessible. AWS achieves 11 nines by storing objects redundantly across multiple devices within a single AZ and, for multi-AZ classes, across multiple AZs.

### 1.2 Retrieval Time Comparison for Glacier Classes

| Storage Class | Expedited | Standard | Bulk |
|---|---|---|---|
| Glacier Instant Retrieval | Milliseconds | Milliseconds | N/A |
| Glacier Flexible Retrieval | 1-5 minutes | 3-5 hours | 5-12 hours |
| Glacier Deep Archive | N/A | 12 hours | 48 hours |

### 1.3 S3 Intelligent-Tiering Access Tiers

Intelligent-Tiering automatically moves objects between tiers based on access history:

| Tier | Activation | Cost Relative to Standard |
|---|---|---|
| Frequent Access | Default | Same as Standard |
| Infrequent Access | 30 days without access | ~40% less than Standard |
| Archive Instant Access | 90 days without access | ~68% less than Standard |
| Archive Access (optional) | 90-180 days (configurable) | Similar to Glacier Flexible |
| Deep Archive Access (optional) | 180+ days (configurable) | Similar to Glacier Deep Archive |

Objects returned to frequent access automatically when accessed in lower tiers. No retrieval fee between tiers, but a per-object monitoring fee applies.

---

## Section 2: S3 Lifecycle Policy Design

### 2.1 Lifecycle Policy Transition Rules

Valid transition order (can only go down the hierarchy):

```text
Standard
  -> Standard-IA (minimum 30 days in Standard)
  -> Intelligent-Tiering
  -> Glacier Instant Retrieval
  -> Glacier Flexible Retrieval
  -> Glacier Deep Archive
```

Minimum days between transitions: Standard → Standard-IA requires at least 30 days. Standard-IA → Glacier requires at least 30 more days (60 days total from creation).

### 2.2 Lifecycle Policy for a Three-Stage Data Retention Strategy

This policy applies a common three-stage retention model to application logs:

```json
{
  "Rules": [
    {
      "ID": "AppLogsRetentionPolicy",
      "Filter": {
        "Prefix": "app-logs/"
      },
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "STANDARD_IA"
        },
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        },
        {
          "Days": 365,
          "StorageClass": "DEEP_ARCHIVE"
        }
      ],
      "Expiration": {
        "Days": 2555
      }
    }
  ]
}
```

This keeps logs in Standard for the first 30 days (frequent operational access), moves to Standard-IA for days 30-90 (occasional reference), to Glacier for days 90-365 (rare access), to Deep Archive for years 1-7 (compliance retention), and deletes after 7 years (2,555 days).

### 2.3 Lifecycle Policy for Version Cleanup

When versioning is enabled, previous versions accumulate. This policy automatically expires noncurrent versions and removes incomplete multipart uploads:

```json
{
  "Rules": [
    {
      "ID": "CleanupOldVersions",
      "Filter": {},
      "Status": "Enabled",
      "NoncurrentVersionTransitions": [
        {
          "NoncurrentDays": 30,
          "StorageClass": "STANDARD_IA"
        }
      ],
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 90
      },
      "AbortIncompleteMultipartUpload": {
        "DaysAfterInitiation": 7
      }
    }
  ]
}
```

The empty Filter object `{}` applies the rule to all objects in the bucket.

---

## Section 3: S3 Security Controls

### 3.1 Security Control Hierarchy

When AWS evaluates an S3 request, controls are applied in this order:

1. Block Public Access settings — override any ACL or bucket policy that would grant public access
2. Bucket policy — resource-based policy evaluated alongside identity policies
3. IAM identity policy — the requesting principal's identity-based policy
4. Object ACL — legacy per-object access control (AWS recommends disabling ACLs)

### 3.2 Block Public Access Settings

| Setting | What It Blocks |
|---|---|
| BlockPublicAcls | Prevents adding ACLs that grant public access |
| IgnorePublicAcls | Ignores any existing public ACLs |
| BlockPublicPolicy | Prevents bucket policies that grant public access |
| RestrictPublicBuckets | Restricts access to only AWS service principals and authorized accounts when a public policy exists |

AWS recommends enabling all four settings at the account level unless you intentionally need public S3 content. This is set in the S3 console under Block Public Access settings for the account.

### 3.3 Encryption Options Compared

| Encryption Type | Key Management | Audit Trail | Compliance Use Case |
|---|---|---|---|
| SSE-S3 (AES-256) | AWS-managed, transparent | None | Basic encryption, no compliance requirement |
| SSE-KMS | AWS KMS, customer-controlled policy | CloudTrail logs key usage | PCI DSS, HIPAA, SOC 2 requiring key audit |
| SSE-C | Customer-managed, never stored in AWS | None (key not in AWS) | Strict key custody requirements |
| Client-side encryption | Customer-managed | None (done before upload) | Maximum control — AWS never sees plaintext |
| DSSE-KMS | Dual-layer SSE-KMS | CloudTrail (dual) | Highest regulatory compliance (SEC, GovCloud) |

### 3.4 Bucket Policy Examples

Enforce HTTPS-only access (deny all HTTP requests):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyNonHTTPS",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::example-bucket",
        "arn:aws:s3:::example-bucket/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

Restrict access to a specific VPC endpoint only (traffic must come through the VPC endpoint):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RestrictToVPCEndpoint",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::example-bucket",
        "arn:aws:s3:::example-bucket/*"
      ],
      "Condition": {
        "StringNotEquals": {
          "aws:sourceVpce": "vpce-1234567890abcdef0"
        }
      }
    }
  ]
}
```

### 3.5 VPC Endpoints for S3

S3 Gateway VPC Endpoints allow EC2 instances in a VPC to access S3 without traversing the public internet. Key characteristics:

- No additional charge for the endpoint or for data transfer through it
- Route table entry is added to direct S3 traffic through the endpoint
- Does not require an internet gateway, NAT gateway, or VPN
- Works with S3 and DynamoDB only (other services use Interface VPC Endpoints which have a cost)

For the exam: if a scenario requires EC2 instances in a private subnet to access S3 without internet access or NAT gateway, the answer is an S3 Gateway VPC Endpoint.

---

## Section 4: S3 Versioning, Replication, and Object Lock

### 4.1 Versioning Behavior

| Action | Versioning Disabled | Versioning Enabled | Versioning Suspended |
|---|---|---|---|
| PUT object | Replaces existing | Creates new version | Creates new version with null ID |
| DELETE object | Deletes the object | Creates delete marker (object preserved) | Creates delete marker |
| GET object | Returns current | Returns latest version | Returns null-version or latest |
| Recover from delete | Not possible | Delete the delete marker | Limited recovery |

Versioning cannot be disabled once enabled — it can only be suspended. Suspended versioning stops creating new versions but preserves existing versions.

### 4.2 Replication Comparison

| Feature | Cross-Region Replication | Same-Region Replication |
|---|---|---|
| Source and destination | Different Regions | Same Region, different bucket |
| Requirement | Versioning on both buckets | Versioning on both buckets |
| Replicates existing objects | No (only new objects by default) | No (only new objects by default) |
| Replicates delete markers | Optional (configurable) | Optional |
| Common use case | DR, compliance, global access | Log aggregation, cross-account copy, test/prod sync |
| Replication Time Control | Optional (15-minute SLA) | Optional |

### 4.3 Object Lock Retention Modes

| Mode | Who Can Delete | Override Possible | Use Case |
|---|---|---|---|
| Governance | Must have s3:BypassGovernanceRetention | Yes, with permission | Testing WORM, internal compliance |
| Compliance | Nobody (including root) | No | SEC 17a-4, financial records, legal hold |

Legal Hold is a separate Object Lock feature — it prevents deletion without a retention period expiry. It can be removed by any user with s3:PutObjectLegalHold permission.

---

## Section 5: S3 Access Patterns

### 5.1 Presigned URLs

A presigned URL embeds temporary, time-limited credentials that allow the bearer to perform a specific S3 action on a specific object without needing AWS credentials. Key characteristics:

- Generated using the IAM credentials of the creator
- Expires at a configurable time (up to 7 days for IAM user credentials; up to 1 hour for IAM role temporary credentials)
- Scope is limited to a single object and a single action (GET or PUT)
- No bucket policy change required

CLI generation example:

```bash
aws s3 presign s3://my-bucket/report.pdf \
  --expires-in 3600
```

This generates a URL valid for 3600 seconds (1 hour). Anyone with this URL can GET the object.

### 5.2 S3 Multipart Upload

For objects larger than 100 MB, AWS recommends using multipart upload. For objects larger than 5 GB, multipart upload is required. Multipart upload:

- Uploads object in parts (minimum 5 MB per part except the last)
- Allows parallel upload of parts for improved throughput
- Allows resuming failed uploads without restarting from zero
- Incomplete multipart uploads incur storage costs until completed or aborted — use lifecycle rules to abort after N days

### 5.3 S3 Transfer Acceleration

Transfer Acceleration uses CloudFront Edge Locations as upload entry points. The client uploads to the nearest Edge Location, and AWS routes the data across its optimized backbone network to the S3 bucket. Most effective for:

- Uploads from geographically distant clients
- Large file uploads where reduced round-trip time per TCP packet matters
- Distributed applications uploading to a central bucket from global locations

---

## Section 6: S3 Additional Features

### 6.1 S3 Event Notifications

S3 can publish event notifications when objects are created, deleted, or restored. Destinations:

- Amazon SQS queue
- Amazon SNS topic
- AWS Lambda function
- Amazon EventBridge (for all events)

Common exam pattern: trigger a Lambda function to process an uploaded image, file, or CSV when it arrives in an S3 bucket. This is a serverless event-driven architecture pattern.

### 6.2 S3 Static Website Hosting

S3 buckets can host static websites (HTML, CSS, JavaScript, images). Requirements:

- Bucket must be publicly accessible (Block Public Access must allow public bucket policies)
- Static website hosting must be enabled in bucket properties
- An index document (typically index.html) must be specified
- Custom error documents optional

The bucket website endpoint format is: `http://bucket-name.s3-website-region.amazonaws.com`

For HTTPS, use CloudFront with an SSL certificate in front of the S3 bucket. CloudFront can serve S3 website content over HTTPS even though S3 website endpoints are HTTP-only.

### 6.3 S3 Storage Lens

S3 Storage Lens provides account-wide visibility into object storage usage and activity trends. It generates metrics across buckets and Regions including total storage, object count, cost efficiency metrics, and activity metrics. Use Storage Lens to identify underutilized buckets, buckets without versioning, and buckets without server-side encryption.

---

## Section 7: SAA-C03 Exam Tips for Module 04

**Exam Tip 1 — Storage class selection by access pattern:**
Frequently accessed = Standard. Unknown patterns = Intelligent-Tiering. Monthly access, data must be in multiple AZs = Standard-IA. Monthly access, single AZ acceptable = One Zone-IA. Quarterly access, instant retrieval = Glacier Instant. Annual access, can wait hours = Glacier Flexible. Multi-year compliance archive = Deep Archive.

**Exam Tip 2 — One Zone-IA risk:**
One Zone-IA stores data in only one AZ. If the AZ fails, data is lost. Only use One Zone-IA for data that can be recreated from another source or that is a secondary copy.

**Exam Tip 3 — Block Public Access is the strongest public prevention control:**
If a question asks how to ensure no object in a bucket can ever be made public regardless of future policy changes, Block Public Access is the answer. Bucket policies can be changed; Block Public Access prevents those changes from granting public access.

**Exam Tip 4 — SSE-KMS for compliance and audit:**
When a question mentions auditing, compliance, key rotation, or the need to see which principals accessed which encryption keys, SSE-KMS is correct. SSE-S3 provides encryption but no audit capability.

**Exam Tip 5 — VPC Endpoint for private S3 access:**
When a scenario has EC2 instances in a private subnet that need S3 access without internet connectivity, the answer is an S3 Gateway VPC Endpoint. It is free and does not require a NAT gateway.

**Exam Tip 6 — CRR requires versioning:**
Cross-Region Replication requires versioning to be enabled on both the source and destination buckets. If a question mentions CRR and does not mention versioning, enabling versioning is a prerequisite step.

**Exam Tip 7 — Compliance WORM = Object Lock Compliance mode:**
If the scenario mentions SEC 17a-4, HIPAA immutable records, or "no one including root can delete," the answer is S3 Object Lock in Compliance mode. Governance mode allows privileged users to bypass retention.

**Exam Tip 8 — Presigned URLs for temporary private object access:**
When a scenario asks how to give an external user temporary access to a private object without making the bucket public or creating IAM credentials, presigned URLs are the answer.

---

## Section 8: Key CLI Commands for Module 04

List S3 buckets in your account:

```bash
aws s3 ls
```

Get bucket encryption configuration:

```bash
aws s3api get-bucket-encryption \
  --bucket my-bucket-name
```

Get bucket versioning status:

```bash
aws s3api get-bucket-versioning \
  --bucket my-bucket-name
```

Get bucket lifecycle configuration:

```bash
aws s3api get-bucket-lifecycle-configuration \
  --bucket my-bucket-name
```

Get Block Public Access settings for a bucket:

```bash
aws s3api get-public-access-block \
  --bucket my-bucket-name
```

Generate a presigned URL (valid for 1 hour):

```bash
aws s3 presign s3://my-bucket/myfile.pdf \
  --expires-in 3600
```

---

## Section 9: Study Checklist

- [ ] Name all seven S3 storage classes, their minimum storage durations, and their primary use cases without referencing notes
- [ ] Explain the 11-nines durability guarantee and the difference between durability and availability
- [ ] Write a lifecycle policy JSON that transitions objects through three classes over 12 months and deletes them after 7 years
- [ ] Describe all four Block Public Access settings and explain why AWS recommends enabling all of them by default
- [ ] Compare SSE-S3, SSE-KMS, and SSE-C on key management, audit capability, and compliance use case
- [ ] Write a bucket policy that enforces HTTPS-only access
- [ ] Explain the difference between S3 Object Lock Governance mode and Compliance mode
- [ ] Describe the prerequisite for enabling Cross-Region Replication
- [ ] Run the CLI commands in Section 8 and record the output
- [ ] Complete the Module 04 quiz with a score of at least 80 percent
- [ ] Post your initial response in the Module 04 discussion forum by the Wednesday deadline

---

## References

All certification study materials and exam registration: aws.amazon.com/certification
