# Reading Guide: Module 04 - S3 – Storage Classes, Lifecycle Policies, and Security
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 04 - S3 – Storage Classes, Lifecycle Policies, and Security**! Amazon Simple Storage Service (S3) is AWS's foundational object storage service and one of the most heavily tested topics on the SAA-C03 exam. This module covers how to select the appropriate storage class for different access patterns, how to automate cost reduction through Lifecycle policies, and how to secure bucket data using Block Public Access, bucket policies, ACLs, and encryption. S3 knowledge is tested both directly and as a dependency of services like CloudFront, Lambda, and Athena.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **S3 Storage Classes**: Tiered pricing tiers that trade retrieval speed and frequency for cost. S3 Standard is for frequently accessed data (millisecond latency, 99.99% availability). S3 Standard-IA (Infrequent Access) costs less per GB stored but charges a per-retrieval fee, suitable for data accessed monthly. S3 One Zone-IA stores data in a single AZ for 20% less than Standard-IA but with lower durability. S3 Glacier Instant Retrieval and S3 Glacier Flexible Retrieval are for archival data. S3 Glacier Deep Archive is the lowest-cost tier with retrieval times of 12–48 hours. S3 Intelligent-Tiering automatically moves objects between tiers based on access patterns.

*   **S3 Lifecycle Policies**: Rules attached to a bucket or prefix that automatically transition objects between storage classes or expire (delete) objects after a defined number of days. For example, transition objects to Standard-IA after 30 days, to Glacier Flexible Retrieval after 90 days, and delete after 365 days. Lifecycle policies eliminate manual cost management and are a key cost optimization pattern on the exam.

*   **S3 Versioning**: A bucket-level setting that retains all versions of every object, including deleted objects (via delete markers). Versioning is a prerequisite for S3 Replication, MFA Delete, and S3 Object Lock. Once enabled, versioning cannot be fully disabled — it can only be suspended, leaving existing versions intact.

*   **S3 Block Public Access**: A set of four account-level and bucket-level settings that prevent objects from becoming publicly accessible regardless of individual object ACLs or bucket policy statements. AWS enables Block Public Access at the account level by default for new accounts. It is the primary safeguard against accidental data exposure.

*   **S3 Encryption**: S3 supports server-side encryption (SSE) with three key management options: SSE-S3 (AWS-managed keys, enabled by default), SSE-KMS (AWS Key Management Service — provides audit logs via CloudTrail and customer-managed key rotation), and SSE-C (customer-provided keys managed entirely by the customer). Client-side encryption is also supported for data encrypted before upload. SSE-KMS is the exam answer whenever key management auditing or compliance is required.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** S3 questions appear in all four domains. Cost questions involve storage class selection and Lifecycle policies. Security questions involve Block Public Access, bucket policies, ACLs, and encryption. Resilience questions involve versioning, replication, and Cross-Region Replication.

*   **Storage Class Selection Trap:** The exam will describe an access frequency and ask which storage class is cheapest. The key rule: if data is accessed less than once a month, Standard-IA or One Zone-IA saves money. If data is accessed less than once a year, Glacier. If the access pattern is unknown, Intelligent-Tiering avoids retrieval charges and optimizes automatically.

*   **S3 vs. EBS vs. EFS:** S3 is object storage — ideal for static files, backups, data lakes, and media. EBS is block storage attached to a single EC2 instance for databases and boot volumes. EFS is network file storage mountable by multiple EC2 instances. Choosing the wrong storage type is the most common distractor in S3 questions.

*   **Bucket Policy vs. ACL:** Bucket policies are JSON-based resource policies that grant cross-account access and are the preferred access control mechanism. ACLs are legacy object-level access controls that AWS recommends disabling in favor of policies. The exam answer is almost always to use a bucket policy or IAM policy, not ACLs.

*   **Presigned URLs for Temporary Access:** When a question asks how to give an external user temporary access to a private S3 object without making it public, the answer is a presigned URL — a time-limited URL generated with the uploader's credentials that grants access for a specific duration.

*   **Study Resource:** The S3 documentation covers all storage classes, Lifecycle rules, and security features: [Amazon S3 User Guide](https://docs.aws.amazon.com/s3/index.html). The "Amazon S3 Security Best Practices" section is directly exam-relevant.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the S3 chapters in the AWS Solutions Architect study materials, focusing on storage class comparison and the security model. The [Amazon S3 FAQs page](https://aws.amazon.com/s3/faqs/) is a concise exam preparation resource. Also review the [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) for the "AWS Storage Services Overview" whitepaper.

*   **Required Video:** Watch the S3 module in the official course playlist, paying particular attention to the storage class transition waterfall, Lifecycle policy configuration, and the interaction between Block Public Access and bucket policies: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Create an S3 bucket with versioning and Block Public Access enabled:** Use the AWS CLI: `aws s3api create-bucket --bucket my-lab-bucket --region us-east-1` followed by `aws s3api put-bucket-versioning --bucket my-lab-bucket --versioning-configuration Status=Enabled`.

*   **Configure a Lifecycle policy:** Create a Lifecycle rule that transitions objects to Standard-IA after 30 days and to Glacier Flexible Retrieval after 90 days using the S3 console Lifecycle management tab or the `aws s3api put-bucket-lifecycle-configuration` CLI command.

*   **Generate and test a presigned URL:** Upload a private object and generate a presigned URL with a 1-hour expiration: `aws s3 presign s3://my-lab-bucket/myfile.txt --expires-in 3600`. Test access in a browser and verify expiration.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Compare all S3 storage classes and their use cases at [https://aws.amazon.com/s3/storage-classes/](https://aws.amazon.com/s3/storage-classes/).
- [ ] Review S3 security best practices at [https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html).
- [ ] Watch the S3 video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab creating buckets, Lifecycle policies, and presigned URLs.
- [ ] Proceed to the weekly quiz.
