# Quiz: Module 04 - S3 – Storage Classes, Lifecycle Policies, and Security
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A company stores compliance audit logs in S3. The logs are accessed frequently for the first 30 days, rarely accessed for the next 60 days, and must be retained for 7 years for regulatory purposes. Which S3 configuration minimizes storage cost while meeting these requirements?
*   A) Store all logs in S3 Standard for the full 7 years for simplest management.
*   B) Use an S3 Lifecycle policy to transition to S3 Standard-IA after 30 days, transition to S3 Glacier Flexible Retrieval after 90 days, and expire after 2,555 days (7 years).
*   C) Store logs in S3 One Zone-IA immediately to minimize cost, relying on external backups for durability.
*   D) Enable S3 Intelligent-Tiering and disable all Lifecycle rules, relying entirely on automated tiering.
*   **Correct Answer:** B) A Lifecycle policy automating transitions from Standard → Standard-IA → Glacier with a 7-year expiration directly matches the access pattern and minimizes total cost.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* S3 Standard for 7 years is significantly more expensive than transitioning to cheaper tiers after the active access period. The requirement does not justify paying Standard rates for archival data.
    *   *Why B is correct:* This is the canonical SAA-C03 Lifecycle policy pattern. Matching storage class to access frequency (frequent → Standard, infrequent → IA, archival → Glacier) and automating with a Lifecycle policy is both cost-optimal and operationally efficient.
    *   *Why C is incorrect:* S3 One Zone-IA stores data in a single AZ, risking data loss if that AZ fails. Compliance audit logs require the 99.999999999% durability of multi-AZ storage classes. Regulatory requirements typically prohibit single-AZ storage for compliance records.
    *   *Why D is incorrect:* Intelligent-Tiering is appropriate when access patterns are unknown or unpredictable. For a known pattern (frequent for 30 days, then rare for 60 days, then archival), explicit Lifecycle transitions to Glacier are cheaper because Intelligent-Tiering does not tier into Glacier by default without optional archive configurations.

---

**Question 2**
Which of the following is the most accurate definition of **S3 Server-Side Encryption with AWS KMS (SSE-KMS)**?
*   A) An encryption method where the customer encrypts data locally before uploading it to S3, with no AWS involvement in key management.
*   B) A server-side encryption option where AWS KMS manages and audits the encryption keys, providing CloudTrail key usage logs and support for customer-managed key rotation — required for many compliance frameworks.
*   C) An S3 feature that enforces HTTPS-only access to a bucket by rejecting HTTP PUT and GET requests at the network level.
*   D) An automatic replication feature that copies encrypted objects to a secondary S3 bucket in another Region for disaster recovery.
*   **Correct Answer:** B) SSE-KMS uses AWS KMS to manage encryption keys, providing key usage audit trails in CloudTrail and support for customer-managed key (CMK) rotation, making it the correct choice for compliance-regulated data.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes client-side encryption (CSE), where the customer handles all key management outside of AWS. SSE-KMS is server-side — AWS performs encryption on the server after receiving the object.
    *   *Why B is correct:* SSE-KMS is the exam answer whenever a question mentions compliance, auditing, key rotation, or the need to know "who used which key and when." KMS integrates with CloudTrail to log every Decrypt call, unlike SSE-S3.
    *   *Why C is incorrect:* Enforcing HTTPS-only access is accomplished via a bucket policy with a Condition denying requests where `aws:SecureTransport` is false — it is an access control mechanism, not an encryption configuration.
    *   *Why D is incorrect:* This describes S3 Cross-Region Replication (CRR), a separate feature used for disaster recovery. CRR can replicate encrypted objects but is not itself an encryption feature.

---

**Question 3**
A developer accidentally deleted an important S3 object that held production configuration data. Which S3 feature, if enabled before the deletion, would allow the operations team to recover the previous version of the object?
*   A) S3 Cross-Region Replication — automatically copies the deleted object to a secondary bucket.
*   B) S3 Versioning — retains all previous versions of objects, allowing recovery by deleting the delete marker.
*   C) S3 Transfer Acceleration — improves upload speed and maintains a write-ahead log for recovery.
*   D) S3 Intelligent-Tiering — stores redundant object copies across tiers, one of which retains the pre-deletion version.
*   **Correct Answer:** B) S3 Versioning retains all object versions including deleted objects as delete markers, allowing recovery by removing the delete marker to restore the previous version.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* S3 Cross-Region Replication copies objects to another bucket in real time, but if the source object is deleted, the delete operation is also replicated. CRR does not protect against accidental deletion unless combined with replication rules that exclude delete markers.
    *   *Why B is correct:* With versioning enabled, deleting an object inserts a delete marker rather than permanently removing the data. Removing the delete marker (via the console, CLI, or SDK) restores the latest previous version — the standard recovery procedure.
    *   *Why C is incorrect:* S3 Transfer Acceleration is a network optimization feature that routes uploads through CloudFront Edge Locations for faster performance. It has no role in data recovery or versioning.
    *   *Why D is incorrect:* S3 Intelligent-Tiering automatically moves objects between storage tiers based on access frequency. It does not maintain multiple copies of objects or provide any recovery from accidental deletion.

---

**Question 4**
A security auditor reports that an S3 bucket contains sensitive customer data and is publicly accessible. The bucket policy does not contain any public access statements, but individual objects were granted public read via Object ACLs during upload. Which single action most effectively closes this exposure immediately?
*   A) Delete and re-create all objects without the public ACL flag.
*   B) Enable S3 Block Public Access at the bucket level — specifically the "Block public access granted through ACLs" setting — to override all existing object ACLs.
*   C) Rotate the bucket's encryption keys in KMS and force all users to re-authenticate.
*   D) Attach an explicit Deny bucket policy for `s3:GetObject` to all principals and then re-grant access individually.
*   **Correct Answer:** B) Enabling Block Public Access (specifically the ACL-blocking settings) immediately overrides all existing public object ACLs without requiring objects to be deleted or re-uploaded.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Re-uploading every object without the public ACL is operationally expensive, time-consuming, and unnecessary. Block Public Access can override ACLs without touching the objects themselves.
    *   *Why B is correct:* S3 Block Public Access has settings that override both bucket ACLs and object ACLs. Enabling "BlockPublicAcls" and "IgnorePublicAcls" at the bucket level immediately removes public access granted by ACLs — no object modification needed. This is the fastest and safest remediation.
    *   *Why C is incorrect:* Rotating KMS encryption keys changes the cryptographic protection of objects at rest but does not affect who can access the objects over HTTP. A publicly accessible object remains accessible regardless of its encryption state.
    *   *Why D is incorrect:* Writing a broad Deny policy would also block legitimate IAM-authorized access, requiring individual re-grants that create significant operational complexity and risk of access outages during the transition.

---

**Question 5**
A media company needs to allow a third-party content delivery partner to download specific S3 objects for a limited time without creating an IAM user or making the objects permanently public. Which S3 feature solves this requirement?
*   A) S3 Static Website Hosting — enable public access on the bucket and host the objects as a website.
*   B) S3 Presigned URLs — generate a time-limited URL signed with AWS credentials that grants temporary GET access to the specific object.
*   C) S3 Access Points — create a dedicated access point with a policy granting the partner account permanent access.
*   D) S3 Cross-Origin Resource Sharing (CORS) — configure the bucket to accept requests from the partner's domain.
*   **Correct Answer:** B) S3 Presigned URLs grant temporary, credential-free access to a specific object for a defined time window without permanent IAM user creation or public exposure.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Enabling static website hosting makes objects permanently public to anyone on the internet — the opposite of "limited time" and "without making objects permanently public."
    *   *Why B is correct:* A presigned URL is a time-limited, object-specific URL signed with the credentials of the generating principal (IAM user or Role). It grants access for the configured expiration period (max 12 hours for IAM user credentials, up to 7 days for Role credentials via STS). This is the canonical answer for "temporary external access without IAM users."
    *   *Why C is incorrect:* S3 Access Points simplify bucket policy management for multiple applications sharing one bucket, but they still require IAM credentials for the partner account. They do not enable credential-free temporary access.
    *   *Why D is incorrect:* CORS (Cross-Origin Resource Sharing) controls which browser origins can make cross-origin HTTP requests to the bucket. It is a browser security control, not an access grant mechanism. It does not prevent or enable non-browser downloads by the partner.

