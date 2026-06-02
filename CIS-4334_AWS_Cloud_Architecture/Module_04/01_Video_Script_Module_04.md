# Video Script: Module 04 - S3: Storage Classes, Lifecycle Policies, and Security

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Duration:** 20-24 minutes
**Instructor:** Professor Nash

---

## [00:00 - 01:30] Opening and Module Objectives

Welcome back. I am Professor Nash and this is Module 04: S3 — Storage Classes, Lifecycle Policies, and Security.

Amazon S3 is the most-used storage service in AWS and one of the most tested services on the SAA-C03 exam. S3 stores virtually everything — application assets, backups, data lake files, static websites, CloudTrail logs, CloudFormation templates. Understanding S3's storage classes, lifecycle management, and security model is not optional.

By the end of this module you will be able to:

- Select the correct S3 storage class for a given access pattern and cost requirement
- Design S3 lifecycle policies that automate cost optimization
- Implement S3 security controls including bucket policies, ACLs, encryption, and Block Public Access
- Explain S3 versioning, replication, and object lock
- Describe S3 access patterns including presigned URLs and S3 Transfer Acceleration

---

## [01:30 - 07:00] S3 Storage Classes

[SHOW DIAGRAM]

S3 offers multiple storage classes optimized for different access frequencies and cost profiles. The SAA-C03 exam regularly presents scenarios requiring you to select the right class. Let me walk through each one.

**S3 Standard** is the default storage class. It provides 11 nines of durability (99.999999999%) and 99.99% availability. Objects are stored across at least three Availability Zones within the Region. There is no minimum storage duration charge. Use S3 Standard for frequently accessed data — web application assets, recently generated reports, active dataset files.

**S3 Intelligent-Tiering** automatically moves objects between access tiers based on changing access patterns. It has three built-in tiers: Frequent Access (like Standard), Infrequent Access (40% savings), and Archive Instant Access (68% savings). For objects not accessed in 30 days, S3 automatically moves them to Infrequent Access. After 90 days without access, they move to Archive Instant Access. You can also activate deeper archive tiers. There is a small per-object monitoring fee. Use Intelligent-Tiering when access patterns are unknown or unpredictable.

**S3 Standard-Infrequent Access (Standard-IA)** is for data that is accessed less frequently but requires rapid access when needed. It has the same durability and multi-AZ availability as Standard but costs less for storage with a per-GB retrieval fee. There is a 30-day minimum storage charge. Use Standard-IA for backups, disaster recovery data, and files accessed monthly rather than daily.

**S3 One Zone-Infrequent Access (One Zone-IA)** stores data in only one Availability Zone, making it 20% cheaper than Standard-IA but with lower availability (99.5%) and no AZ redundancy. If the AZ fails, the data is lost until restored from a replica. Use One Zone-IA only for data that can be reproduced from another source — secondary backup copies, processed thumbnails, re-creatable intermediate data.

**S3 Glacier Instant Retrieval** is for archive data that needs millisecond retrieval. It costs much less than Standard-IA but has a 90-day minimum duration and a higher retrieval cost. Use Glacier Instant Retrieval for quarterly accessed medical images, news archives, user-generated content accessed rarely but immediately when needed.

**S3 Glacier Flexible Retrieval** (formerly S3 Glacier) is for archive data where you can wait minutes to hours for retrieval. Three retrieval options: Expedited (1-5 minutes), Standard (3-5 hours), Bulk (5-12 hours). Minimum storage duration: 90 days. Use Glacier Flexible Retrieval for compliance archives, long-term backups, yearly tax records.

**S3 Glacier Deep Archive** is the lowest-cost S3 storage class. Retrieval takes 12-48 hours. Minimum storage duration is 180 days. Use Deep Archive for data retained for regulatory compliance that is rarely or never accessed — 7-year financial records, medical records archives, long-term research data.

[SHOW DIAGRAM]

The retrieval trade-off pattern for the SAA-C03 exam:

- Instant access needed, low cost: Standard or Standard-IA
- Can wait 30-90 days for access, lowest cost: Glacier or Deep Archive
- Unknown access patterns: Intelligent-Tiering
- Only one AZ needed, cost is priority: One Zone-IA

---

## [07:00 - 11:30] S3 Lifecycle Policies

[SHOW DIAGRAM]

Lifecycle policies automate the transition of objects between storage classes or the expiration (deletion) of objects based on age or other criteria. This is how you implement systematic cost optimization without manual intervention.

A lifecycle policy consists of one or more rules. Each rule has a filter (which objects the rule applies to) and actions (what happens to matching objects).

Filter options include:

- Apply to all objects in the bucket
- Apply only to objects with a specific prefix (for example, `logs/` or `archive/2023/`)
- Apply only to objects with specific tags

Action types are transitions and expirations. Transitions move objects to a different storage class after a specified number of days since creation. Expirations delete objects or delete previous versions after a specified age.

[SHOW CONSOLE]

Here is a lifecycle policy example in JSON. This is the format you will see in the AWS console and CLI:

```json
{
  "Rules": [
    {
      "ID": "TransitionAndExpireAppLogs",
      "Filter": {
        "Prefix": "applogs/"
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
        }
      ],
      "Expiration": {
        "Days": 365
      }
    }
  ]
}
```

This policy applies to all objects with the `applogs/` prefix. After 30 days, they transition to Standard-IA. After 90 days, they transition to Glacier. After 365 days, they expire (are deleted).

Important transition order constraints: you can only transition down the cost hierarchy — Standard → Standard-IA → Glacier → Deep Archive. You cannot transition from Glacier back to Standard-IA using a lifecycle policy. Also, minimum storage durations matter — transitioning to Standard-IA before 30 days incurs the full 30-day minimum charge.

---

## [11:30 - 16:30] S3 Security

[SHOW DIAGRAM]

S3 security has multiple layers and the SAA-C03 exam tests them all. Let me cover each control.

**Bucket policies** are resource-based IAM policies attached directly to an S3 bucket. They define who can access the bucket and what they can do. Bucket policies can grant access to other AWS accounts, to IAM principals in your account, or even to the public (which you generally want to prevent). Bucket policies are evaluated by IAM alongside identity-based policies.

**Block Public Access** is a set of account-level and bucket-level settings that override bucket policies and ACLs that would otherwise make objects or buckets publicly accessible. AWS recommends enabling all four Block Public Access settings by default. On the SAA-C03 exam: if a scenario asks how to prevent S3 objects from ever being made public regardless of future bucket policy changes, the answer is Block Public Access.

**S3 Object Ownership** controls whether ACLs are enabled or disabled for a bucket. AWS now recommends disabling ACLs (setting Object Ownership to Bucket Owner Enforced). When ACLs are disabled, all objects in the bucket are owned by the bucket owner regardless of who uploaded them. Use bucket policies instead of ACLs for access control.

**Server-side encryption** encrypts objects at rest as they are written to disk. Three options:

- SSE-S3: AWS manages keys using AES-256. No cost. Default for new buckets.
- SSE-KMS: AWS KMS manages keys. Audit trail for key usage via CloudTrail. Additional cost per request. Enables key rotation and access control via KMS key policy. Required by many compliance standards.
- SSE-C: Customer provides and manages the encryption keys. AWS performs encryption/decryption but never stores the key.

For the exam: if a question requires an audit trail of who accessed which encryption key, SSE-KMS is the answer. If the question requires the customer to retain full key control with no key stored in AWS, SSE-C is the answer. SSE-S3 is sufficient for general encryption without compliance requirements.

**Encryption in transit** — S3 endpoints support HTTPS. You can enforce HTTPS-only access with a bucket policy condition:

[SHOW CONSOLE]

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
        "arn:aws:s3:::my-secure-bucket",
        "arn:aws:s3:::my-secure-bucket/*"
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

**VPC Endpoint for S3** lets EC2 instances access S3 without going through the public internet. A Gateway VPC Endpoint routes S3 traffic through the AWS private network. Traffic never leaves the AWS network and there is no data transfer charge.

---

## [16:30 - 20:00] Versioning, Replication, and Object Lock

**S3 Versioning** keeps every version of an object. When you enable versioning on a bucket, every PUT creates a new version and every DELETE creates a delete marker without removing the previous version. Versioning protects against accidental deletion and overwrites. Once enabled, versioning can be suspended but never fully disabled on a bucket that has had it enabled.

[SHOW DIAGRAM]

**S3 Cross-Region Replication (CRR)** automatically replicates objects from a source bucket in one Region to a destination bucket in a different Region. Use cases: compliance (data must exist in two countries), latency reduction for global users, disaster recovery for a second Region. Versioning must be enabled on both the source and destination buckets. CRR replicates only new objects created after replication is configured — it does not retroactively replicate existing objects.

**S3 Same-Region Replication (SRR)** replicates within the same Region — typically to a different account for log aggregation or to maintain a live copy for a different team.

**S3 Object Lock** prevents objects from being deleted or overwritten for a fixed amount of time or indefinitely. Two modes:

- Governance mode: most users cannot overwrite or delete; accounts with special permissions can
- Compliance mode: no one — including the root user — can overwrite or delete during the retention period

Object Lock is used for regulatory compliance requiring WORM (Write Once Read Many) storage — SEC 17a-4, HIPAA, financial records retention.

---

## [20:00 - 22:00] Presigned URLs and Transfer Acceleration

**Presigned URLs** allow you to grant temporary, time-limited access to a specific S3 object without making the bucket public and without requiring the requester to have AWS credentials. You generate a presigned URL using your IAM credentials — the URL embeds a time-limited signature. Anyone with the URL can access the object until the URL expires.

Use case: your application generates a download link for a user's report file stored in a private S3 bucket. Instead of making the bucket public, your application generates a presigned URL valid for 1 hour.

**S3 Transfer Acceleration** speeds up uploads to S3 from geographically distant clients by routing uploads through the nearest CloudFront Edge Location and then through AWS's optimized network backbone to the S3 bucket. It is most effective when objects are being uploaded from clients far from the bucket's Region. There is an additional per-GB charge.

---

## [22:00 - 24:00] Module Summary

S3 storage classes — know the hierarchy: Standard → Intelligent-Tiering → Standard-IA → One Zone-IA → Glacier Instant → Glacier Flexible → Deep Archive. Match the access pattern to the class.

Lifecycle policies automate transitions and expirations. Transitions can only go down the hierarchy. Minimum storage durations apply.

S3 security layers: Block Public Access to prevent public exposure; bucket policies for access control; SSE-S3 for basic encryption; SSE-KMS for auditable key management; enforce HTTPS with aws:SecureTransport condition; VPC Endpoints to keep traffic off the public internet.

Versioning protects against accidental deletion. CRR replicates across Regions for DR and compliance. Object Lock enforces WORM retention.

In the lab this week you will apply lifecycle policies, configure bucket policies, and analyze S3 security configurations. In the Reading Guide you will find a complete storage class comparison table, lifecycle policy examples, and security configuration checklists.

For your certification study: aws.amazon.com/certification.

---

End of Module 04 Video Script
