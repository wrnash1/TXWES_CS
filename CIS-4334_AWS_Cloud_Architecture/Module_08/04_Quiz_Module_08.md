# Quiz: Module 08 — Amazon S3 and Storage Services

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A media company stores archived video files that are accessed once per quarter for licensing reviews. When accessed, retrieval must complete within 5 minutes. Multi-AZ durability is required because the files are irreplaceable. Which S3 storage class is MOST appropriate?

A. S3 Standard-Infrequent Access

B. S3 Glacier Flexible Retrieval with Expedited retrieval

C. S3 Glacier Instant Retrieval

D. S3 One Zone-Infrequent Access

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Standard-IA provides immediate retrieval but charges a per-GB retrieval fee at a storage cost higher than necessary for quarterly access. Glacier Instant Retrieval provides the same millisecond retrieval at a significantly lower storage cost for quarterly or less frequent access.
- B is incorrect. Glacier Flexible Retrieval Expedited retrieval takes 1–5 minutes — it would technically meet the 5-minute window — but it is more expensive than Glacier Instant Retrieval for data that needs instant access, and Expedited retrieval is not guaranteed during high demand periods.
- C is correct. Glacier Instant Retrieval delivers millisecond retrieval like Standard-IA but at a lower storage cost designed for quarterly access. It stores data across multiple AZs for durability and meets both the retrieval time and redundancy requirements.
- D is incorrect. One Zone-IA stores data in a single AZ. The requirement states the files are irreplaceable, making single-AZ storage unacceptable. One Zone-IA is only appropriate for reproducible data.

---

### Question 2

A company enables Cross-Region Replication (CRR) on an existing S3 bucket that already contains 50,000 objects. After enabling CRR, the company notices that only new objects appear in the destination bucket. What must be done to replicate the existing objects?

A. Disable and re-enable versioning on the source bucket

B. Use S3 Batch Operations to replicate the existing objects

C. Delete and re-upload the existing objects

D. CRR does not support existing objects under any circumstances

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Disabling and re-enabling versioning does not trigger replication of existing objects. Versioning is already a requirement for CRR to function.
- B is correct. S3 replication only applies to objects uploaded after the replication rule is configured. To replicate pre-existing objects, you must use S3 Batch Operations with a replication operation, which processes existing objects in batch.
- C is incorrect. Deleting and re-uploading objects would replicate the new uploads but would delete the originals (and their version history if applicable), which is destructive and unnecessary.
- D is incorrect. S3 Batch Operations specifically addresses this gap — existing objects can be replicated using Batch Operations. The statement that it is impossible is factually incorrect.

---

### Question 3

A company wants to reduce storage costs for application logs that are frequently accessed in the first 30 days and then never accessed again. The logs must be retained for exactly 7 years for compliance. Which S3 lifecycle configuration BEST meets these requirements?

A. Transition to Glacier Flexible Retrieval after 7 days; expire after 7 years

B. Transition to Standard-IA after 30 days; transition to Glacier Deep Archive after 90 days; expire after 2555 days

C. Use S3 Intelligent-Tiering with no expiration rule

D. Store in S3 One Zone-IA from creation; expire after 2555 days

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Transitioning after 7 days triggers the 30-day minimum storage duration charge for Standard-IA and incurs the charge for the remaining 23 days even though the object was only in that class briefly. Additionally, Glacier Flexible Retrieval has a 90-day minimum duration that would be violated with an early transition.
- B is correct. Standard holds frequently accessed logs for the first 30 days. Standard-IA accommodates the infrequent access period after 30 days (meeting the 30-day minimum). Glacier Deep Archive minimizes storage cost for the multi-year retention period. Expiration at 2555 days (7 years) meets the compliance requirement and prevents indefinite storage charges.
- C is incorrect. Intelligent-Tiering handles unpredictable access patterns efficiently but without an expiration rule, objects accumulate indefinitely after the 7-year retention period ends, incurring unnecessary storage costs.
- D is incorrect. One Zone-IA stores data in a single AZ. Compliance data that must be retained for 7 years requires multi-AZ durability.

---

### Question 4

A company's EC2 instances need to share access to a common set of configuration files and HTML templates. The instances run Amazon Linux 2 and are spread across three Availability Zones. Which storage solution provides concurrent read/write access from all instances?

A. An EBS gp3 volume with Multi-Attach enabled

B. An S3 bucket accessed via the AWS SDK

C. Amazon EFS mounted on all instances

D. An EBS io2 volume with Multi-Attach enabled

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. EBS Multi-Attach allows up to 16 instances in the same AZ to mount the same volume. It does not work across AZs, and the file system must handle concurrent write coordination at the application layer — standard file systems are not safe with Multi-Attach.
- B is incorrect. S3 accessed via the SDK is object storage, not a mounted file system. Applications expecting a file system path (not HTTP API calls) cannot use S3 as a drop-in file system replacement without significant code changes.
- C is correct. EFS is a regional NFS file system that can be mounted concurrently by thousands of EC2 instances across all AZs in a region. It provides a standard POSIX file system interface accessible to all Linux instances simultaneously.
- D is incorrect. io2 Multi-Attach has the same AZ limitation as gp3 Multi-Attach — it does not span AZs, and the file system concurrency safety issues remain.

---

### Question 5

A company stores financial transaction records in S3. Regulatory requirements mandate that no record can be deleted or modified for 7 years. Even AWS administrators must not be able to delete the records during the retention period. Which combination of features enforces this requirement?

A. S3 versioning and S3 Replication

B. S3 Object Lock in Compliance Mode with a 7-year retention period

C. AWS Backup with a 7-year retention plan

D. S3 Object Lock in Governance Mode with a 7-year retention period

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Versioning preserves previous versions but does not prevent deletion. With sufficient permissions, any version can be permanently deleted using a version-specific delete operation.
- B is correct. S3 Object Lock in Compliance Mode prevents any user — including root and AWS — from deleting or shortening the retention period during the lock window. It enforces WORM compliance for the specified retention duration.
- C is incorrect. AWS Backup provides centralized backup management but does not prevent deletion of S3 objects directly. It would not prevent an administrator from deleting the S3 records through the S3 API.
- D is incorrect. Governance Mode allows designated users with specific IAM permissions to delete objects. The requirement states that no one can delete the records — this requires Compliance Mode, not Governance Mode.

---

### Question 6

A data engineering team uploads large CSV files (averaging 10 GB each) to S3 daily. Each morning they need to extract only the rows where the `country` column equals "US" before loading to a database. The files are not split across multiple objects. Which approach minimizes data transfer costs?

A. Download the full file and filter locally

B. Use Amazon Athena to query the CSV

C. Use S3 Select with a SQL expression to filter server-side

D. Convert the files to Parquet and then use Amazon Redshift Spectrum

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Downloading the full 10 GB file and filtering locally incurs the maximum data transfer cost and puts unnecessary load on the application.
- B is incorrect. Athena is designed for querying across many objects using a catalog. For filtering a single object, it is over-engineered. Athena also requires a Glue Data Catalog table definition and charges per TB scanned.
- C is correct. S3 Select executes the filter expression server-side and returns only the matching rows, dramatically reducing data transferred from S3. For a single large object filtered by a column value, this is the most cost-effective and operationally simple solution.
- D is incorrect. Converting to Parquet and using Redshift Spectrum introduces significant complexity and additional services. It is appropriate for ongoing analytical workloads, not a daily filter-and-load ETL pipeline operating on single objects.

---

### Question 7

A production PostgreSQL database requires an EBS volume with 50,000 IOPS, 1,000 MB/s throughput, and 99.999% durability. Which EBS volume type should be used?

A. gp3

B. io1

C. io2 Block Express

D. st1

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. gp3 supports a maximum of 16,000 IOPS and 1,000 MB/s throughput. It cannot meet the 50,000 IOPS requirement. gp3 also has 99.8–99.9% durability, not 99.999%.
- B is incorrect. io1 supports a maximum of 64,000 IOPS (which would technically meet the requirement) but provides only 99.8–99.9% durability. It cannot meet the 99.999% durability requirement.
- C is correct. io2 Block Express supports up to 256,000 IOPS, 4,000 MB/s throughput, and provides 99.999% (five nines) durability. It is the only EBS type that meets all three requirements simultaneously.
- D is incorrect. st1 is a throughput-optimized HDD with a maximum of 500 IOPS. It cannot meet the 50,000 IOPS requirement and is designed for sequential throughput, not random database I/O. It also cannot be used as a boot volume.

---

### Question 8

A company currently uses gp2 EBS volumes for all EC2 instances. A solutions architect recommends migrating to gp3. Which TWO advantages does gp3 provide compared to gp2? (Select TWO)

A. gp3 allows IOPS and throughput to be configured independently of volume size

B. gp3 supports higher maximum IOPS than gp2

C. gp3 provides 99.999% durability compared to gp2's 99.9%

D. gp3 is approximately 20% less expensive than gp2 for the same storage capacity

**Correct Answer: A and D**

**Distractor Analysis:**

- A is correct. gp3 allows you to provision IOPS (up to 16,000) and throughput (up to 1,000 MB/s) independently of the volume size. gp2 ties IOPS to volume size (3 IOPS/GB), meaning you must over-provision storage to get more IOPS.
- B is incorrect. Both gp3 and gp2 have the same maximum IOPS of 16,000. The advantage of gp3 is the baseline and independent configuration, not a higher maximum.
- C is incorrect. Both gp3 and gp2 provide 99.8–99.9% durability. 99.999% durability is exclusive to io2 Block Express.
- D is correct. gp3 is approximately 20% less expensive per GB-month than gp2, making it both more capable and cheaper.

---

### Question 9

A company uses S3 to store user-uploaded images. They want to automatically resize uploaded images using a Lambda function. The Lambda function should only be triggered for `.png` files uploaded to the `images/raw/` prefix. Which S3 feature enables this targeted trigger?

A. S3 Batch Operations

B. S3 Replication with a Lambda destination

C. S3 event notification with prefix and suffix filters targeting a Lambda function

D. S3 Inventory with a Lambda trigger

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. S3 Batch Operations processes existing objects in bulk — it is not an event-driven trigger for new uploads.
- B is incorrect. S3 Replication copies objects to a destination bucket. Lambda is not a replication destination. Replication does not trigger serverless image processing.
- C is correct. S3 event notifications support prefix and suffix filters. Configuring an event notification for `s3:ObjectCreated:*` with prefix `images/raw/` and suffix `.png` will trigger the Lambda function only for PNG files uploaded to that prefix.
- D is incorrect. S3 Inventory generates a daily or weekly report of all objects in a bucket. It is not an event-driven trigger for real-time processing of new uploads.

---

### Question 10

A company needs to centrally manage backups for EC2 instances, RDS databases, and DynamoDB tables across multiple AWS accounts and regions. They need to enforce a policy that backup recovery points cannot be deleted for 90 days, even by account administrators. Which service and configuration meets this requirement?

A. AWS Backup with a 90-day retention plan

B. AWS Backup with vault lock in Compliance Mode and a 90-day minimum retention period

C. AWS Backup with vault lock in Governance Mode and a 90-day minimum retention period

D. Individual service-level snapshot policies with IAM policies preventing deletion

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. A retention plan in AWS Backup defines when backups expire, but without vault lock, administrators with sufficient IAM permissions can still delete recovery points before the retention period expires.
- B is correct. AWS Backup provides centralized backup management across services, accounts, and regions. Vault lock in Compliance Mode makes recovery points immutable — no account, including root and AWS, can delete them during the lock period. This enforces the 90-day requirement absolutely.
- C is incorrect. Governance Mode allows designated users with specific IAM permissions to delete recovery points. The requirement states that even account administrators cannot delete backups, which requires Compliance Mode.
- D is incorrect. Individual service snapshots with IAM policies are difficult to manage across accounts and services, and IAM policies can be modified by administrators. This approach is operationally complex and does not provide the immutability guarantee that vault lock provides.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
