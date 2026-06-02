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
