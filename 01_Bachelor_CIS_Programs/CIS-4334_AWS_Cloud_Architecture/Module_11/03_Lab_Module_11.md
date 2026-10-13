# Lab: Module 11 — AWS IAM and Security Architecture

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Total Points:** 100

---

## Lab Overview

This lab builds hands-on IAM and security skills through three exercises: creating IAM policies, roles, and testing policy evaluation using the AWS CLI and IAM Policy Simulator; configuring a Customer Managed KMS Key and using it to encrypt and decrypt data; and analyzing a security architecture to identify IAM, KMS, and organizational policy gaps.

---

## Prerequisites

- AWS Academy Learner Lab account or AWS free-tier account
- AWS CLI v2 installed and configured
- Completed Module 11 video and reading guide
- A text editor for composing JSON policy documents

---

## Part 1: IAM Policies and Roles (40 points)

### Task 1.1 — Create an IAM Policy

Create a least-privilege IAM policy named `cis4334-s3-readonly` that allows:

- Reading objects from a specific S3 bucket named `cis4334-lab-data`
- Listing the objects in that bucket
- No other S3 permissions

Create the file `s3-readonly-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ListBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::cis4334-lab-data"
    },
    {
      "Sid": "AllowS3GetObject",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::cis4334-lab-data/*"
    }
  ]
}
```

Create the managed policy:

```bash
aws iam create-policy \
  --policy-name cis4334-s3-readonly \
  --policy-document file://s3-readonly-policy.json \
  --description "CIS4334 Lab - S3 read-only access to cis4334-lab-data bucket"
```

**Deliverable 1.1:** Paste the output showing the PolicyArn. Then answer: why are two separate `Resource` ARN formats needed — `arn:aws:s3:::cis4334-lab-data` and `arn:aws:s3:::cis4334-lab-data/*`? What does each one target?

### Task 1.2 — Create an IAM Role with a Trust Policy

Create an IAM role that EC2 instances can assume. This role simulates an instance profile for an application server.

Create the trust policy file `ec2-trust-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Create the role:

```bash
aws iam create-role \
  --role-name cis4334-app-server-role \
  --assume-role-policy-document file://ec2-trust-policy.json \
  --description "CIS4334 Lab - EC2 application server role"
```

Attach the policy created in Task 1.1:

```bash
# Replace ACCOUNT_ID with your 12-digit AWS account ID
aws iam attach-role-policy \
  --role-name cis4334-app-server-role \
  --policy-arn arn:aws:iam::ACCOUNT_ID:policy/cis4334-s3-readonly
```

**Deliverable 1.2:** Paste the output of:

```bash
aws iam get-role \
  --role-name cis4334-app-server-role \
  --query "Role.{Name:RoleName,ARN:Arn,AssumedBy:AssumeRolePolicyDocument.Statement[0].Principal}"
```

Then explain in 2–3 sentences: what does the trust policy accomplish, and why is a trust policy distinct from the permissions policy?

### Task 1.3 — Add a Condition to Restrict the Policy

Modify the policy to add a condition that only allows `s3:GetObject` when the request includes a specific tag on the object — objects must have the tag `Environment=production`. Create a new policy version with this condition.

Create `s3-readonly-v2-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ListBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::cis4334-lab-data"
    },
    {
      "Sid": "AllowS3GetObjectProductionOnly",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::cis4334-lab-data/*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/Environment": "production"
        }
      }
    }
  ]
}
```

Create a new policy version:

```bash
aws iam create-policy-version \
  --policy-arn arn:aws:iam::ACCOUNT_ID:policy/cis4334-s3-readonly \
  --policy-document file://s3-readonly-v2-policy.json \
  --set-as-default
```

**Deliverable 1.3:** Paste the output. Then answer: with this policy version active, what happens when the application server role tries to call `s3:GetObject` on an object that has the tag `Environment=staging`? What happens if the object has no Environment tag at all?

### Task 1.4 — Write a Resource-Based Policy

Write a bucket policy for the S3 bucket `cis4334-lab-data` that allows the application server role created in Task 1.2 to list and get objects, but explicitly denies all access if the request is not using HTTPS (SSL).

Create `bucket-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyNonSSL",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::cis4334-lab-data",
        "arn:aws:s3:::cis4334-lab-data/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    },
    {
      "Sid": "AllowAppServerRole",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT_ID:role/cis4334-app-server-role"
      },
      "Action": [
        "s3:ListBucket",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::cis4334-lab-data",
        "arn:aws:s3:::cis4334-lab-data/*"
      ]
    }
  ]
}
```

**Deliverable 1.4:** Write (but do not run unless you have the bucket) the CLI command that would apply this bucket policy. Explain in 3–4 sentences: if the application server role makes an HTTP (not HTTPS) request, which statement in the bucket policy applies first and what is the result? Does the order of the statements in the JSON matter for this determination?

### Task 1.5 — Clean Up IAM Resources

```bash
aws iam detach-role-policy \
  --role-name cis4334-app-server-role \
  --policy-arn arn:aws:iam::ACCOUNT_ID:policy/cis4334-s3-readonly

aws iam delete-role \
  --role-name cis4334-app-server-role

aws iam delete-policy \
  --policy-arn arn:aws:iam::ACCOUNT_ID:policy/cis4334-s3-readonly
```

**Deliverable 1.5:** Confirm all IAM resources were deleted.

---

## Part 2: AWS KMS — Customer Managed Key (35 points)

### Task 2.1 — Create a Customer Managed Key

```bash
# Create the KMS CMK
KEY_ID=$(aws kms create-key \
  --description "CIS4334 Lab CMK" \
  --key-usage ENCRYPT_DECRYPT \
  --query "KeyMetadata.KeyId" \
  --output text)
echo "Key ID: $KEY_ID"

# Create a human-readable alias
aws kms create-alias \
  --alias-name alias/cis4334-lab-key \
  --target-key-id $KEY_ID
```

**Deliverable 2.1:** Paste the output of:

```bash
aws kms describe-key \
  --key-id alias/cis4334-lab-key \
  --query "KeyMetadata.{KeyId:KeyId,Description:Description,KeyState:KeyState,KeyManager:KeyManager,CreationDate:CreationDate}"
```

Confirm `KeyManager` is `CUSTOMER` (not `AWS`). Explain in 1–2 sentences why this distinction matters.

### Task 2.2 — Encrypt and Decrypt Data

Encrypt a plaintext value with your CMK:

```bash
# Encrypt a secret value
ENCRYPTED=$(aws kms encrypt \
  --key-id alias/cis4334-lab-key \
  --plaintext "SuperSecretPassword123" \
  --query "CiphertextBlob" \
  --output text)
echo "Encrypted (base64): $ENCRYPTED"

# Write the encrypted value to a file
echo $ENCRYPTED | base64 --decode > encrypted_secret.bin
echo "Encrypted blob written to encrypted_secret.bin"
```

Decrypt the encrypted value:

```bash
DECRYPTED=$(aws kms decrypt \
  --ciphertext-blob fileb://encrypted_secret.bin \
  --query "Plaintext" \
  --output text | base64 --decode)
echo "Decrypted value: $DECRYPTED"
```

**Deliverable 2.2:** Paste both commands and their outputs. Confirm the decrypted value matches the original plaintext. Then answer in 2–3 sentences: if an attacker gains access to the `encrypted_secret.bin` file but not to the AWS account, can they recover the plaintext? Why or why not?

### Task 2.3 — Enable Key Rotation

```bash
aws kms enable-key-rotation \
  --key-id alias/cis4334-lab-key

aws kms get-key-rotation-status \
  --key-id alias/cis4334-lab-key
```

**Deliverable 2.3:** Paste the rotation status output confirming rotation is enabled. Then answer: when key rotation occurs, what happens to data encrypted with the previous key material? Do you need to re-encrypt existing data after rotation? Explain in 3–4 sentences.

### Task 2.4 — Review CloudTrail for KMS API Calls

```bash
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventSource,AttributeValue=kms.amazonaws.com \
  --start-time $(date -d '30 minutes ago' '+%Y-%m-%dT%H:%M:%SZ') \
  --query "Events[*].{Time:EventTime,Action:EventName,User:Username}" \
  --output table
```

**Deliverable 2.4:** Paste the CloudTrail output showing your KMS API calls (CreateKey, Encrypt, Decrypt, EnableKeyRotation). Explain in 2–3 sentences why having CloudTrail records of Decrypt API calls is valuable from a security and compliance perspective.

### Task 2.5 — Clean Up KMS Resources

```bash
# Schedule key deletion (minimum 7 days; this prevents immediate accidental deletion)
aws kms schedule-key-deletion \
  --key-id alias/cis4334-lab-key \
  --pending-window-in-days 7

# Delete the alias
aws kms delete-alias \
  --alias-name alias/cis4334-lab-key
```

**Deliverable 2.5:** Paste the schedule-key-deletion output. Explain why KMS requires a minimum 7-day pending deletion window rather than allowing immediate deletion.

---

## Part 3: Security Architecture Analysis (25 points)

### Architecture Description

A startup has the following AWS security architecture:

- All workloads run in a single AWS account
- EC2 instances have IAM roles with `AdministratorAccess` policies for "convenience"
- S3 buckets containing customer PII have no bucket policies; access is controlled only by IAM user policies
- CloudTrail is enabled but logs are stored in the same account that is being audited
- No GuardDuty, WAF, or Security Hub is configured
- RDS databases are encrypted with AWS Managed Keys (not Customer Managed Keys)
- Application developers have direct console access to the production environment

### Task 3.1 — Security Risk Identification

Identify and explain at least six specific security risks in this architecture. For each risk, describe:

- The specific configuration or gap that creates the risk
- The potential impact if the risk is exploited
- The AWS feature or configuration change that would mitigate it

**Deliverable 3.1:** Six security risks in a structured table or numbered list format.

### Task 3.2 — IAM Least Privilege Redesign

The startup wants to implement IAM least privilege. They have three application roles: Web Server (reads from S3, writes to SQS), Worker (reads from SQS, writes to DynamoDB), and Reporting (reads from RDS and S3).

For each of the three roles, list the specific IAM actions that should be granted (be specific — e.g., `s3:GetObject`, not `s3:*`). Explain in 2–3 sentences what the principle of least privilege means and why `AdministratorAccess` violates it even for trusted applications.

**Deliverable 3.2:** Three role permission specifications with principle of least privilege explanation.

### Task 3.3 — Defense-in-Depth Recommendations

The CTO asks you to design a defense-in-depth security strategy for a customer PII data platform on AWS. Without writing actual IAM policies or KMS commands, describe the security architecture across five layers:

1. Account-level governance (AWS Organizations and SCPs)
2. Identity and access (IAM principles)
3. Data protection (encryption at rest and in transit)
4. Threat detection (which services and what they monitor)
5. Application-layer protection (for the customer-facing web interface)

**Deliverable 3.3:** Five-layer security architecture description. Each layer should be 4–6 sentences describing specific AWS services and configurations.

---

## Submission Instructions

Compile all deliverables into a single document labeled clearly by task number. Include all CLI commands and outputs, all written responses, and the security architecture description. Submit through Canvas before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|------|--------|----------|
| Part 1: Policy Creation Tasks 1.1–1.3 | 20 | Policy ARN confirmed; two Resource ARNs explained; conditional access effect described correctly |
| Part 1: Resource-based Policy Task 1.4 | 15 | Bucket policy written correctly; DenyNonSSL explains explicit deny; order of statements in JSON explained |
| Part 1: Cleanup Task 1.5 | 5 | All IAM resources confirmed deleted |
| Part 2: KMS Tasks 2.1–2.3 | 20 | CMK created and CUSTOMER manager confirmed; encrypt/decrypt successful; rotation status confirmed; rotation explanation accurate |
| Part 2: CloudTrail Task 2.4 | 10 | CloudTrail output shows KMS calls; compliance value of Decrypt audit trail explained |
| Part 2: Cleanup Task 2.5 | 5 | Key deletion scheduled; minimum window explained |
| Part 3: Risk Identification Task 3.1 | 10 | Six risks identified with specific configuration, impact, and mitigation for each |
| Part 3: Least Privilege Task 3.2 | 5 | Specific actions named (not wildcards); principle of least privilege explained |
| Part 3: Defense-in-Depth Task 3.3 | 10 | All five layers addressed; specific AWS services named per layer |
| **Total** | **100** | |

---

## Part 9 — Challenge Exercise

### Challenge 1: IAM Access Analyzer Finding Investigation
Use IAM Access Analyzer to detect and review externally accessible resources, then practice remediating the findings.
1. Enable IAM Access Analyzer for your account: `aws accessanalyzer create-analyzer --analyzer-name lab11-analyzer --type ACCOUNT`. Wait for the status to become `ACTIVE`: `aws accessanalyzer get-analyzer --analyzer-name lab11-analyzer --query "analyzer.status"`.
2. List any findings generated: `aws accessanalyzer list-findings --analyzer-arn <analyzer-arn> --output table`. If no findings exist, create a test condition by temporarily setting an S3 bucket policy that grants access to a second AWS account (use a test/non-production bucket): `aws s3api put-bucket-policy --bucket <your-bucket> --policy '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:root"},"Action":"s3:GetObject","Resource":"arn:aws:s3:::<your-bucket>/*"}]}'`. Re-list findings to observe the cross-account access finding.
3. Archive the finding to acknowledge it: `aws accessanalyzer update-findings --analyzer-arn <arn> --status ARCHIVED --ids <finding-id>`. Then remove the cross-account bucket policy and verify the finding moves to RESOLVED status within a few minutes.
4. Document the difference between an ACTIVE, ARCHIVED, and RESOLVED Access Analyzer finding. Explain what action each status implies the security team should take.

### Challenge 2: CloudTrail Log Querying for Security Events
Practice querying CloudTrail event history to reconstruct a security timeline — a core skill for incident response.
1. Query CloudTrail for all IAM-related API calls from the last hour: `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=iam.amazonaws.com --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%SZ) --output table`. Record the event names observed.
2. Query for all `ConsoleLogin` events in the last 24 hours: `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%SZ)`. For each login event, note the `sourceIPAddress` and `userAgent` fields in the event JSON.
3. Query for any `DeleteBucket` or `DeleteObject` events: `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=DeleteBucket`. If none exist, query for `PutBucketPolicy` to find a policy change event and examine the full event JSON: `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=PutBucketPolicy --query "Events[0].CloudTrailEvent" --output text | python -m json.tool`.
4. Identify which fields in a CloudTrail event record are most useful for answering each of these incident response questions: (a) Who performed the action? (b) From where? (c) Was it authenticated with MFA? (d) Did the action succeed or fail?

### Reflection Questions
1. After completing Challenge 1, explain how IAM Access Analyzer differs from a manual IAM policy review. What specific class of misconfiguration — affecting cross-account or public access — can Access Analyzer detect that a policy review of individual IAM policies alone would miss? How does this relate to the AWS Well-Architected Framework Security pillar principle of "apply security at all layers"?
2. Based on Challenge 2, explain why CloudTrail event history (90-day lookup) is sufficient for routine auditing but insufficient for long-term compliance requirements. What configuration change converts CloudTrail from a short-term lookup service into a permanent, tamper-evident audit log, and which AWS service would you use to alert on specific API patterns (such as `DeleteTrail` or `StopLogging`) in near-real time?

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
