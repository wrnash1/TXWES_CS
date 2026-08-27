# Quiz: Module 04 - S3: Storage Classes, Lifecycle Policies, and Security

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Questions:** 10

---

## Question 1

A company stores financial transaction logs in S3. The logs are accessed frequently in the first 30 days, then accessed approximately once per month for the next 6 months, then are almost never accessed but must be retained for 7 years for regulatory compliance. What S3 lifecycle configuration best minimizes cost while meeting these requirements?

- A) Store in S3 Standard for the full 7 years
- B) Store in S3 Standard initially, transition to S3 Standard-IA after 30 days, transition to S3 Glacier Flexible Retrieval after 180 days, delete after 7 years
- C) Store in S3 Glacier Flexible Retrieval immediately to minimize cost from day one
- D) Store in S3 Intelligent-Tiering for the full 7 years

### Answer 1

Correct Answer: B

### Explanation 1

- A is incorrect: Storing all data in Standard for 7 years is the highest-cost option. Standard storage pricing is appropriate for frequent access but is significantly more expensive than archival tiers for data that is rarely accessed.
- B is correct: This tiered lifecycle matches the access pattern precisely: Standard for the initial 30 days of frequent access, Standard-IA for the monthly-access period (days 30-180), Glacier Flexible for the long-tail compliance retention period (months 6-84), and automatic deletion at 7 years.
- C is incorrect: Glacier Flexible Retrieval has retrieval delays of 3-5 hours for standard retrieval. Storing logs there from day one means the team cannot access them quickly for the first 30 days when operational access is needed.
- D is incorrect: Intelligent-Tiering is appropriate for unknown access patterns. This scenario has a well-understood pattern that is better served by explicit lifecycle transitions, which avoid the per-object monitoring fee that Intelligent-Tiering charges.

---

## Question 2

A solutions architect needs to ensure that objects in an S3 bucket can never be deleted or overwritten for a 7-year period to comply with SEC Rule 17a-4. Not even the account root user should be able to delete the records during the retention period. Which S3 feature provides this guarantee?

- A) S3 Versioning with MFA Delete
- B) S3 Object Lock in Governance mode
- C) S3 Object Lock in Compliance mode
- D) S3 Bucket Policy with a Deny statement for s3:DeleteObject

### Answer 2

Correct Answer: C

### Explanation 2

- A is incorrect: S3 Versioning with MFA Delete requires MFA to delete specific versions, but it does not prevent the root user from disabling MFA Delete or deleting versions. It does not provide the immutable retention guarantee required by SEC 17a-4.
- B is incorrect: Object Lock Governance mode allows users with the s3:BypassGovernanceRetention permission to override the retention. This does not satisfy the SEC 17a-4 requirement that no one — including root — can delete records during the retention period.
- C is correct: Object Lock Compliance mode is a true WORM control. Once set, the retention period cannot be shortened or overridden by any user, including the AWS account root user. This satisfies SEC 17a-4 and similar financial compliance requirements.
- D is incorrect: A bucket policy Deny statement can be removed or modified by an IAM administrator or the root user. It does not provide immutable retention.

---

## Question 3

A company runs an application on EC2 instances in a private subnet with no internet gateway. The application must read and write objects to an S3 bucket. How can you enable this access while ensuring S3 traffic never traverses the public internet?

- A) Create a NAT Gateway in a public subnet and route the private subnet's S3 traffic through it
- B) Configure a Gateway VPC Endpoint for S3 and add a route table entry for S3 traffic
- C) Enable S3 Transfer Acceleration on the bucket to route traffic through the private network
- D) Move the S3 bucket to the same Availability Zone as the EC2 instances

### Answer 3

Correct Answer: B

### Explanation 3

- A is incorrect: A NAT Gateway routes traffic to the public internet — it does not keep traffic on the private AWS network. Using a NAT Gateway means S3 traffic traverses the internet, which violates the requirement. Additionally, NAT Gateway costs per GB of data processed.
- B is correct: An S3 Gateway VPC Endpoint routes all S3 traffic through the AWS private network. It is added to the VPC route table and requires no NAT gateway or internet gateway. There is no additional charge for the endpoint or the data transferred through it.
- C is incorrect: S3 Transfer Acceleration speeds up uploads from distant geographic locations by routing through CloudFront Edge Locations — it routes traffic through the internet (via Edge Locations), not through a private network.
- D is incorrect: S3 buckets are regional services, not AZ-scoped. You cannot move an S3 bucket to a specific AZ, and AZ colocation does not affect whether traffic uses the public internet.

---

## Question 4

A company needs to store processed thumbnail images in S3. The thumbnails are generated from original images that are always available in a separate primary S3 bucket. The thumbnails are accessed about once per month. Cost reduction is the top priority. If the storage for these thumbnails is lost, they can be regenerated. Which storage class is most appropriate?

- A) S3 Standard
- B) S3 Standard-IA
- C) S3 One Zone-IA
- D) S3 Glacier Flexible Retrieval

### Answer 4

Correct Answer: C

### Explanation 4

- A is incorrect: S3 Standard is optimized for frequent access. It is more expensive than alternatives for monthly-access data.
- B is incorrect: S3 Standard-IA provides infrequent access pricing but still stores data across multiple AZs. Since the thumbnails can be regenerated, multi-AZ redundancy is unnecessary — paying for it wastes money.
- C is correct: S3 One Zone-IA stores data in a single AZ at 20% less cost than Standard-IA. The only downside is that if the AZ fails, data is lost — but since the thumbnails can be regenerated from the always-available originals, this risk is acceptable. This is the exact use case One Zone-IA is designed for.
- D is incorrect: Glacier Flexible Retrieval has retrieval delays of hours. Monthly access with immediate retrieval is not compatible with Glacier retrieval times.

---

## Question 5

A security team discovers that a developer accidentally made an S3 bucket publicly accessible by adding a public bucket policy. The security team wants to prevent any S3 bucket in the AWS account from ever being made publicly accessible, regardless of what bucket policies are created in the future. What is the most effective control?

- A) Remove the IAM s3:PutBucketPolicy permission from all developers
- B) Enable S3 Block Public Access at the account level with all four settings enabled
- C) Create an SCP in AWS Organizations that denies s3:PutBucketPolicy for all accounts
- D) Enable AWS Config to alert when public bucket policies are created

### Answer 5

Correct Answer: B

### Explanation 5

- A is incorrect: Removing s3:PutBucketPolicy prevents creating bucket policies but also prevents legitimate security configurations. It is overly restrictive and does not allow any bucket policy to be created.
- B is correct: Block Public Access settings at the account level override all bucket policies and ACLs that would grant public access. Even if a developer creates a bucket policy that grants s3:GetObject to `Principal: "*"`, Block Public Access prevents that policy from granting public access. This is the correct and intended tool for this use case.
- C is incorrect: An SCP that denies s3:PutBucketPolicy would block all bucket policies — including legitimate security controls like HTTPS enforcement or VPC endpoint restrictions. This is too broad.
- D is incorrect: AWS Config detection is reactive — it alerts after the public exposure has already occurred. Block Public Access is a preventive control that stops the exposure before it happens.

---

## Question 6

A developer needs to allow an external partner to download a specific file from a private S3 bucket for the next 24 hours. The partner does not have an AWS account. Creating a permanent IAM user for the partner is not acceptable. What is the correct solution?

- A) Temporarily enable public read access on the S3 bucket and share the object URL
- B) Create an IAM role for the partner and give them temporary console access
- C) Generate an S3 presigned URL for the specific object with a 24-hour expiration and share it with the partner
- D) Enable S3 Transfer Acceleration and share the bucket URL with the partner

### Answer 6

Correct Answer: C

### Explanation 6

- A is incorrect: Making the bucket publicly readable exposes all objects in the bucket, not just the one the partner needs. Public access should never be enabled for a private bucket.
- B is incorrect: An IAM role requires the partner to have an AWS account to assume the role. The scenario states the partner does not have an AWS account.
- C is correct: A presigned URL embeds temporary, time-limited access credentials that allow anyone with the URL to download the specific object. No AWS account is needed. The URL expires after 24 hours. The bucket remains private throughout.
- D is incorrect: Transfer Acceleration speeds up uploads/downloads but does not grant access to a private bucket. The bucket still requires authentication.

---

## Question 7

A company is designing an S3 security configuration for a bucket storing healthcare records under HIPAA. The security team requires an audit trail showing which encryption keys were used to access which objects, and who made each key access request. Which encryption option satisfies this requirement?

- A) SSE-S3 with customer-managed key rotation
- B) SSE-KMS using an AWS KMS customer-managed key
- C) SSE-C with customer-provided encryption keys
- D) Client-side encryption using the AWS Encryption SDK

### Answer 7

Correct Answer: B

### Explanation 7

- A is incorrect: SSE-S3 uses AWS-managed keys (AES-256) with no visibility into key operations. There is no CloudTrail audit trail for SSE-S3 key usage. Key rotation occurs automatically but is not configurable or auditable by the customer.
- B is correct: SSE-KMS logs every key usage event to AWS CloudTrail, including the principal that made the request, the timestamp, and the KMS key used. Customer-managed KMS keys support custom key policies, automatic rotation, and fine-grained access control — all required for HIPAA audit requirements.
- C is incorrect: SSE-C requires the customer to provide the encryption key with every request. AWS does not store the key and cannot log key usage since the key is managed entirely by the customer outside of AWS.
- D is incorrect: Client-side encryption means the data is encrypted before it reaches AWS. AWS sees only ciphertext. There is no AWS-level audit trail of encryption key usage because AWS does not participate in the encryption operations.

---

## Question 8

An S3 lifecycle policy includes a transition rule that moves objects from S3 Standard to S3 Standard-IA after 10 days. What is the result of this configuration?

- A) The transition occurs successfully after 10 days with no issues
- B) The transition is invalid because Standard-IA requires a minimum of 30 days in Standard before transitioning
- C) The objects are moved but the customer is not charged any additional fee
- D) S3 automatically delays the transition to 30 days without generating an error

### Answer 8

Correct Answer: B

### Explanation 8

- A is incorrect: AWS enforces a minimum of 30 days before objects can be transitioned from Standard to Standard-IA. A 10-day transition rule violates this constraint.
- B is correct: Standard-IA has a 30-day minimum storage charge. AWS requires that lifecycle rules respect this minimum by not transitioning objects to Standard-IA before they have been in Standard for at least 30 days. Creating a lifecycle rule with a value below 30 days will result in an error.
- C is incorrect: Even if the transition were allowed, Standard-IA has a minimum 30-day storage charge. Moving objects before 30 days would incur the full 30-day charge regardless.
- D is incorrect: AWS does not silently modify lifecycle rules. An invalid rule either results in an error when the policy is applied or the rule is marked as invalid.

---

## Question 9

A company uses S3 Cross-Region Replication to maintain a copy of their primary bucket in a disaster recovery Region. After enabling CRR, the operations team notices that objects uploaded to the primary bucket before CRR was enabled are not appearing in the DR bucket. What is the most likely cause?

- A) CRR only replicates objects larger than 5 MB by default
- B) Cross-Region Replication replicates only objects created after CRR was configured; existing objects must be replicated using S3 Batch Replication or manually
- C) Versioning is not enabled on the source bucket, so CRR cannot function
- D) CRR requires a Direct Connect connection between Regions to replicate objects

### Answer 9

Correct Answer: B

### Explanation 9

- A is incorrect: CRR does not have a size threshold. It replicates all new objects matching the replication filter regardless of size.
- B is correct: CRR is a forward-looking replication service — it replicates objects created or modified after replication is enabled. Pre-existing objects in the bucket are not automatically replicated. S3 Batch Replication is the AWS-provided tool to replicate existing objects to the destination bucket.
- C is incorrect: If versioning were not enabled on the source bucket, CRR would fail entirely — no replication would occur at all, not just for older objects. The question describes new objects being replicated but old ones missing.
- D is incorrect: CRR uses the AWS global backbone network to transfer objects between Regions. No Direct Connect connection is required.

---

## Question 10

A company stores millions of objects in an S3 bucket. The objects have highly unpredictable access patterns — some objects are accessed thousands of times per day, others are never accessed after initial upload. The company wants to minimize storage costs without manually analyzing access patterns or creating complex lifecycle policies. Which storage class is most appropriate?

- A) S3 Standard for all objects
- B) S3 Standard-IA for all objects
- C) S3 Intelligent-Tiering
- D) S3 Glacier Flexible Retrieval for all objects

### Answer 10

Correct Answer: C

### Explanation 10

- A is incorrect: S3 Standard is cost-effective only for frequently accessed objects. Storing objects that are never accessed again in Standard wastes money compared to cheaper storage tiers.
- B is incorrect: S3 Standard-IA charges a retrieval fee per GB. For objects accessed thousands of times per day, the retrieval costs would far exceed the storage savings, making Standard-IA more expensive than Standard for high-access objects.
- C is correct: S3 Intelligent-Tiering is designed precisely for unpredictable access patterns. It automatically moves objects between Frequent Access, Infrequent Access, and Archive tiers based on actual access history with no retrieval fees between tiers. Frequently accessed objects stay in the Frequent Access tier at Standard pricing; rarely accessed objects move to cheaper tiers automatically.
- D is incorrect: Glacier Flexible Retrieval is appropriate only when all objects have very infrequent access and retrieval delays of hours are acceptable. It is completely wrong for objects accessed thousands of times per day.

---

## Question 11

A developer wants to allow an external partner to upload a single file to a specific S3 object path without providing the partner with AWS credentials or changing the bucket policy. The upload link should expire after 2 hours. Which S3 feature satisfies this requirement?

- A) S3 Transfer Acceleration enabled on the bucket with a custom upload URL provided to the partner
- B) A presigned URL for s3:PutObject generated using the developer's IAM credentials with a 7200-second expiry
- C) A public S3 bucket with the partner's IP address allowed in the bucket policy
- D) An S3 Access Point with a policy allowing PutObject for the partner's AWS account ID

### Answer 11

Correct Answer: B

### Explanation 11

- A is incorrect: S3 Transfer Acceleration speeds up uploads over long distances by routing through CloudFront edge locations. It does not provide time-limited upload access without credentials. It is also not a mechanism for partner access control.
- B is correct: A presigned URL embeds temporary, time-limited authorization for a specific action on a specific S3 object. Generating a presigned URL for `s3:PutObject` on the exact object path and setting the expiry to 7200 seconds (2 hours) allows the partner to upload the file without AWS credentials. No bucket policy change is required.
- C is incorrect: Making the bucket public introduces significant security risk by exposing all objects to the internet. IP-based bucket policy restrictions require knowing the partner's exact IP range, which may change, and expose the bucket to the public internet.
- D is incorrect: S3 Access Points are useful for simplifying access management for shared datasets, but they require the partner to have their own AWS account and use AWS IAM credentials to access the access point. This is not a credential-free access solution.

---

## Question 12

A company needs to ensure that S3 objects stored in a compliance archive cannot be deleted or overwritten for 10 years, even by the AWS account root user. Which S3 configuration achieves this?

- A) Enable S3 Versioning and configure MFA Delete requiring root account MFA for permanent deletion
- B) Enable S3 Object Lock in Compliance mode with a retention period of 10 years on the bucket
- C) Enable S3 Object Lock in Governance mode with a retention period of 10 years and remove all s3:BypassGovernanceRetention IAM permissions
- D) Apply a bucket policy with a Deny for s3:DeleteObject and s3:PutObject for all principals including root

### Answer 12

Correct Answer: B

### Explanation 12

- A is incorrect: MFA Delete adds an authentication requirement for permanent deletions but can be disabled by a user with root account credentials. It does not provide true WORM immutability against the root user.
- B is correct: S3 Object Lock in Compliance mode creates a WORM (Write Once, Read Many) retention lock that no user — including the account root user — can remove or shorten during the retention period. This is the only mechanism that provides true immutability against all principals for the full retention duration. It is designed for regulatory compliance requirements like SEC Rule 17a-4(f) and FINRA.
- C is incorrect: Governance mode can be bypassed by users with the `s3:BypassGovernanceRetention` IAM permission. Even if this permission is removed from all current IAM identities, an administrator could create a new role with this permission. Governance mode does not provide the same level of protection as Compliance mode.
- D is incorrect: Bucket policies can be modified or deleted by any IAM principal with `s3:PutBucketPolicy` permission, including the account root user. Bucket policies do not provide immutable protection.

---

## Question 13

An application generates 1,000 S3 PUT requests per second to a single S3 bucket prefix. A developer notices increased latency and some request failures. What is the root cause, and what is the correct solution?

- A) S3 cannot handle more than 100 requests per second; shard the workload across multiple buckets
- B) The application is hitting S3's per-prefix request rate limit of 3,500 PUT/COPY/POST/DELETE requests per second; distribute objects across multiple key prefixes using hash prefixes
- C) The bucket policy is blocking requests above a rate threshold; increase the throttle limit in the bucket policy
- D) The application should enable S3 Transfer Acceleration to increase the PUT request throughput limit

### Answer 13

Correct Answer: B

### Explanation 13

- A is incorrect: S3 can handle thousands of requests per second per prefix and scales automatically beyond those rates with key prefix diversification. The limit is per prefix, not per bucket, and the solution is prefix diversification, not multiple buckets.
- B is correct: S3 supports up to 3,500 PUT/COPY/POST/DELETE and 5,500 GET/HEAD requests per second per prefix. At 1,000 PUT requests per second, the application is approaching but may not have exceeded the limit. If the key names are sequential or use a common prefix pattern, S3's internal partitioning may not spread the load. The solution is to use random hash prefixes (first 4-8 characters of a hash of the object name) to distribute objects across multiple S3 internal partitions, increasing throughput.
- C is incorrect: S3 bucket policies do not have rate throttling settings. Rate limits are an S3 service-level control, not a policy configuration.
- D is incorrect: S3 Transfer Acceleration speeds up data transfer from client to S3 by routing through CloudFront edge locations. It does not increase the per-prefix request rate limit.

---

## Question 14

A company uses S3 Cross-Region Replication to copy objects from a source bucket in us-east-1 to a destination bucket in ap-southeast-1 for disaster recovery. The security team requires that replicated objects in the destination bucket use a customer-managed KMS key that is different from the key used in the source Region. Which configuration is required?

- A) Enable S3 Transfer Acceleration on the destination bucket and specify the destination KMS key
- B) Configure the CRR replication rule to re-encrypt objects with the destination Region's KMS key; grant the S3 replication role kms:GenerateDataKey and kms:Decrypt permissions on both keys
- C) Enable S3 Intelligent-Tiering on the destination bucket, which automatically re-encrypts objects during tier transitions
- D) Use AWS DataSync instead of S3 CRR to support cross-Region KMS key re-encryption

### Answer 14

Correct Answer: B

### Explanation 14

- A is incorrect: S3 Transfer Acceleration is a data transfer performance feature, not an encryption configuration. It has no interaction with CRR or KMS key selection.
- B is correct: S3 CRR supports encryption with a different KMS key in the destination Region. The replication configuration specifies the destination KMS key ARN for re-encryption. The IAM role used for replication must have `kms:Decrypt` permission on the source key (to decrypt objects before replication) and `kms:GenerateDataKey` permission on the destination key (to re-encrypt objects in the destination Region).
- C is incorrect: S3 Intelligent-Tiering automatically moves objects between storage cost tiers. It does not re-encrypt objects with a different KMS key. Encryption is a separate configuration from storage tiering.
- D is incorrect: AWS DataSync is a data transfer service for migrating data to AWS or between storage services. It does not have a feature advantage over CRR for cross-Region KMS key re-encryption. CRR natively supports this use case.

---

## Question 15

A static website is hosted on Amazon S3 with static website hosting enabled. The website owner wants to serve the site over HTTPS with a custom domain name (e.g., www.example.com). Which combination achieves this?

- A) Enable S3 Transfer Acceleration and configure the acceleration endpoint with the custom domain in Route 53
- B) Create a CloudFront distribution with the S3 bucket as the origin, configure an SSL/TLS certificate in ACM, and create a Route 53 alias record pointing to the CloudFront distribution
- C) Enable S3 static website hosting with HTTPS on the S3 bucket website endpoint and create a Route 53 CNAME to the website endpoint
- D) Attach an Application Load Balancer to the S3 bucket and configure ACM SSL on the ALB listener

### Answer 15

Correct Answer: B

### Explanation 15

- A is incorrect: S3 Transfer Acceleration uses an acceleration endpoint that is not the same as a custom domain. Transfer Acceleration is for speeding up uploads from distant locations, not for HTTPS hosting with custom domains. S3 website endpoints do not support HTTPS.
- B is correct: S3 static website endpoints support HTTP only. To serve over HTTPS with a custom domain, place a CloudFront distribution in front of the S3 bucket. ACM provides a free SSL/TLS certificate for the custom domain attached to the CloudFront distribution. Route 53 alias record points the custom domain to the CloudFront distribution's domain name.
- C is incorrect: S3 static website hosting endpoints support HTTP only, not HTTPS. There is no built-in option to enable HTTPS directly on the S3 website endpoint. A CNAME to the HTTP endpoint would still serve HTTP, not HTTPS.
- D is incorrect: Application Load Balancers cannot be directly attached to S3 buckets. ALBs route traffic to EC2 instances, ECS tasks, Lambda functions, or IP addresses — not S3 objects.

---

## Question 16

A company stores audit log files in S3 that accumulate at 50 GB per day. After 30 days, logs are rarely accessed. After 1 year, they must be retained for 6 more years for legal compliance but will never be accessed. Which lifecycle policy minimizes cost while meeting the access and retention requirements?

- A) S3 Standard for 30 days → transition to S3 Glacier Deep Archive after 30 days → expire after 7 years
- B) S3 Standard for 30 days → transition to S3 Standard-IA after 30 days → transition to S3 Glacier Deep Archive after 365 days → expire after 2,555 days (7 years)
- C) S3 Standard for 30 days → transition to S3 Glacier Instant Retrieval after 30 days → expire after 7 years
- D) S3 Intelligent-Tiering for the full retention period with archiving activated

### Answer 16

Correct Answer: B

### Explanation 16

- A is incorrect: Transitioning directly to Glacier Deep Archive after only 30 days would place logs that are "rarely but still sometimes accessed" in a storage class with 12-48 hour retrieval times. The question states logs are rarely accessed after 30 days — not never accessed — so Standard-IA is more appropriate for the 30-365 day window before moving to Deep Archive.
- B is correct: Standard-IA is appropriate for infrequently accessed data that still needs occasional access (retrieval fees apply per access, acceptable for rare access). After 1 year, logs are never accessed and can move to Glacier Deep Archive (the lowest-cost S3 storage at $0.00099/GB/month) for the remaining 6 years. Expiration after 7 years satisfies the legal retention deadline.
- C is incorrect: Glacier Instant Retrieval is appropriate for data accessed a few times per year with instant retrieval needed. It is more expensive than Standard-IA for data accessed more than that, and more expensive than Glacier Deep Archive for long-term never-accessed compliance storage.
- D is incorrect: S3 Intelligent-Tiering is designed for unpredictable access patterns. For data with a known pattern (frequent for 30 days, rare for 11 months, never for 6 years), a lifecycle policy with explicit transitions is more cost-effective and predictable than Intelligent-Tiering's per-object monitoring fee.

---

## Question 17

A development team accidentally deleted a critical S3 object. The S3 bucket has versioning enabled. Which statement correctly describes the outcome and the recovery process?

- A) The object is permanently deleted because deletion operations bypass versioning
- B) A delete marker is placed on the current version; the previous version is still present and can be restored by deleting the delete marker
- C) The object is moved to the S3 Recycle Bin automatically and can be recovered within 30 days
- D) The deleted object can be recovered from the most recent S3 lifecycle policy backup

### Answer 17

Correct Answer: B

### Explanation 17

- A is incorrect: When S3 versioning is enabled, a simple DELETE request (without specifying a version ID) does not permanently delete any version. It only creates a delete marker, which hides all previous versions.
- B is correct: With versioning enabled, a DELETE request without a version ID creates a delete marker as the latest version. The previous object version is still stored in S3. To restore the object, a developer deletes the delete marker (by specifying the delete marker's version ID in a DELETE request), which makes the previous version the current version again.
- C is incorrect: S3 does not have a built-in "Recycle Bin" for versioned objects. AWS Backup and S3 Glacier are the archive and backup mechanisms. S3 Versioning itself is the accidental deletion protection mechanism.
- D is incorrect: S3 lifecycle policies manage object transitions between storage classes and object expiration. They do not create backups or provide a recovery mechanism. Versioning is the feature that enables recovery from accidental deletion.

---

## Question 18

A solutions architect needs to configure S3 event notifications to trigger a Lambda function whenever a new object is uploaded to a specific prefix in a bucket. Which combination is correct?

- A) Configure an S3 bucket policy with an SNS notification target and subscribe Lambda to the SNS topic
- B) Configure an S3 event notification on the bucket with event type s3:ObjectCreated:* filtered by the prefix, with Lambda as the destination
- C) Create an EventBridge rule with a schedule trigger and a Lambda target that polls S3 for new objects
- D) Enable S3 Transfer Acceleration and configure a callback URL to invoke Lambda on each upload

### Answer 18

Correct Answer: B

### Explanation 18

- A is incorrect: While SNS can be an S3 event notification destination (and Lambda can subscribe to SNS), the question asks for a direct S3-to-Lambda integration. S3 supports Lambda as a direct event notification destination without the need for an SNS intermediary. The bucket policy is not the mechanism for configuring event notifications.
- B is correct: S3 event notifications can be configured directly to invoke Lambda functions. The event type `s3:ObjectCreated:*` triggers on all create events (Put, Post, Copy, CompleteMultipartUpload). A prefix filter limits the notification to objects uploaded to the specific path. Lambda must have a resource-based policy allowing S3 to invoke it.
- C is incorrect: EventBridge can receive S3 events via EventBridge notifications (a separate configuration from S3 event notifications), but a scheduled poll pattern is inefficient and adds latency. For real-time S3 event processing, direct S3 event notifications to Lambda are the standard approach.
- D is incorrect: S3 Transfer Acceleration is a data transfer performance feature. It has no callback URL or Lambda invocation mechanism.

---

## Question 19

A company's S3 bucket contains objects encrypted with SSE-KMS using a customer-managed key. The security team wants to ensure that all API calls that use the KMS key are logged for compliance purposes. Which AWS service automatically captures these key usage events?

- A) Amazon Macie
- B) AWS CloudTrail
- C) S3 Server Access Logging
- D) AWS Config

### Answer 19

Correct Answer: B

### Explanation 19

- A is incorrect: Amazon Macie analyzes S3 object content using machine learning to discover sensitive data such as PII and financial information. It does not log KMS key usage events.
- B is correct: AWS CloudTrail automatically records API calls to AWS KMS, including every Decrypt, GenerateDataKey, and Encrypt operation. When S3 uses SSE-KMS to encrypt or decrypt an object, KMS records the event in CloudTrail with details including the principal that initiated the operation, the key ARN, the timestamp, and the request context. This audit trail satisfies compliance logging requirements.
- C is incorrect: S3 Server Access Logging records requests made to the S3 bucket (such as GET, PUT, DELETE operations on S3 objects). It does not record KMS key usage events because KMS is a separate service with its own API call logging.
- D is incorrect: AWS Config records the configuration of AWS resources over time and evaluates them against compliance rules. It does not log real-time API call activity or KMS key usage events.

---

## Question 20

An architect is designing an S3-based data lake. Raw data is uploaded in Parquet format to a prefix `s3://datalake/raw/`. After processing by an ETL pipeline, curated data is written to `s3://datalake/curated/`. The architect wants to ensure that only the ETL pipeline role can write to the `raw/` prefix, and only data scientists can read from the `curated/` prefix. Which S3 feature simplifies managing these distinct access patterns for different prefixes within the same bucket?

- A) S3 Versioning with separate access policies applied to each version ID
- B) S3 Access Points — create one access point for the ETL role with write permissions on the raw prefix, and one for data scientists with read permissions on the curated prefix
- C) S3 Lifecycle policies that automatically enforce access control transitions when objects age
- D) S3 Requester Pays, which shifts authentication responsibility to the requesting party

### Answer 20

Correct Answer: B

### Explanation 20

- A is incorrect: S3 Versioning tracks object history by maintaining multiple versions of the same key. It does not provide access control differentiation by prefix and version ID is not an access control mechanism.
- B is correct: S3 Access Points allow architects to create named endpoints for an S3 bucket, each with its own IAM access policy. An access point policy for the ETL role can allow PutObject only on the `raw/` prefix; a separate access point policy for data scientists can allow GetObject only on the `curated/` prefix. This simplifies permission management by separating access policies per use case rather than combining all rules into one complex bucket policy.
- C is incorrect: S3 Lifecycle policies manage object transitions between storage classes and object expiration based on age or date. They do not enforce or modify access control permissions.
- D is incorrect: S3 Requester Pays is a billing feature that charges the requester rather than the bucket owner for data transfer and API request costs. It has no effect on access control or who can read or write to specific prefixes.
