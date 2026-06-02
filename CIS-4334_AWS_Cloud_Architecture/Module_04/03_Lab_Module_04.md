# Lab: Module 04 - S3: Storage Classes, Lifecycle Policies, and Security

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Points:** 100

---

## Lab Overview

This lab builds hands-on S3 skills through three exercises: analyzing and selecting storage classes for real-world scenarios, writing and validating lifecycle policies using the AWS CLI, and evaluating S3 security configurations for compliance gaps. These tasks map directly to SAA-C03 cost optimization and security scenario questions.

---

## Prerequisites

- AWS account with S3 read and write permissions (AmazonS3FullAccess for testing, or a scoped policy)
- AWS CLI v2 installed and configured
- A test S3 bucket for this lab (you will create it in Part 1)
- Completed Module 04 video and reading guide

---

## Part 1: Storage Class Selection and Bucket Setup (25 points)

### Task 1.1 — Create a Lab Bucket

Create an S3 bucket for this lab. Replace `YOUR-ACCOUNT-ID` with your actual AWS account ID to ensure a globally unique bucket name:

```bash
aws s3api create-bucket \
  --bucket cis4334-lab04-YOUR-ACCOUNT-ID \
  --region us-east-1
```

Enable versioning on the bucket:

```bash
aws s3api put-bucket-versioning \
  --bucket cis4334-lab04-YOUR-ACCOUNT-ID \
  --versioning-configuration Status=Enabled
```

**Deliverable 1.1:** Paste the CLI output for both commands confirming successful creation and versioning enablement.

### Task 1.2 — Storage Class Selection Scenarios

For each of the following five data scenarios, identify the most cost-effective S3 storage class, explain your reasoning in two to three sentences, and identify any minimum storage duration charges the customer should be aware of.

**Scenario A:** A media company stores HD video source files that are accessed by editors daily for the first 30 days after a project, rarely accessed for the next 6 months, then archived permanently. The company needs to retrieve archived files within minutes when needed.

**Scenario B:** A financial services firm must retain trade confirmation records for 7 years per SEC regulations. Records are never accessed after the first 30 days but must be producible within 12 hours if subpoenaed.

**Scenario C:** A machine learning team stores 50 TB of training dataset images. The images were collected over two years and are accessed once per quarter during model retraining cycles. Retrieval must be immediate when needed.

**Scenario D:** A company stores application access logs that are actively monitored for security incidents for the first 30 days. After 30 days, logs are almost never reviewed. After 1 year, logs should be automatically deleted. Budget is the primary concern, and the logs can be reproduced from the source systems if necessary.

**Scenario E:** A startup uploads user profile photos to S3. Access patterns are unpredictable — some photos are viewed thousands of times per day, others are never viewed after upload. The team does not want to analyze access patterns manually.

**Deliverable 1.2:** For each scenario: storage class selected, reasoning (2-3 sentences), and minimum duration charge impact.

---

## Part 2: Lifecycle Policy Configuration (40 points)

### Task 2.1 — Write and Apply a Lifecycle Policy

Write a lifecycle policy JSON for the following requirements:

- Objects in the `raw-data/` prefix should transition to Standard-IA after 30 days
- After 90 days they should transition to Glacier Flexible Retrieval
- After 2 years (730 days) they should expire (be deleted)
- Previous (noncurrent) versions should be deleted after 60 days
- Incomplete multipart uploads should be aborted after 3 days

Save your policy as `lifecycle-policy.json` and apply it:

```bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket cis4334-lab04-YOUR-ACCOUNT-ID \
  --lifecycle-configuration file://lifecycle-policy.json
```

Verify the policy was applied:

```bash
aws s3api get-bucket-lifecycle-configuration \
  --bucket cis4334-lab04-YOUR-ACCOUNT-ID
```

**Deliverable 2.1:** Your complete lifecycle-policy.json content and the output of the get-bucket-lifecycle-configuration command confirming the policy is in effect.

### Task 2.2 — Analyze a Lifecycle Policy for Errors

The following lifecycle policy was submitted by a junior developer. Review it carefully and identify all errors, invalid configurations, or missing elements:

```json
{
  "Rules": [
    {
      "ID": "LogsPolicy",
      "Filter": {
        "Prefix": "logs/"
      },
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 15,
          "StorageClass": "STANDARD_IA"
        },
        {
          "Days": 10,
          "StorageClass": "GLACIER"
        }
      ],
      "Expiration": {
        "Days": 5
      }
    },
    {
      "ID": "LogsPolicy",
      "Filter": {
        "Prefix": "archive/"
      },
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 1,
          "StorageClass": "DEEP_ARCHIVE"
        }
      ]
    }
  ]
}
```

**Deliverable 2.2:** List every error in the policy with a specific explanation of what is wrong and what the corrected value should be. You should find at least four distinct errors.

### Task 2.3 — Cost Comparison Calculation

A company stores 10 TB of data in S3 Standard. The data is accessed in the first 30 days after upload, then never accessed again. The company retains all data for exactly 1 year.

Using the conceptual price points below (not actual AWS prices — used for learning):

- Standard: $0.023/GB/month
- Standard-IA: $0.0125/GB/month with $0.01/GB retrieval fee
- Glacier Flexible: $0.004/GB/month with $0.01/GB retrieval (standard tier)

**Deliverable 2.3:** Calculate the approximate 12-month storage cost for each of these three strategies: (a) Store everything in Standard for 12 months, (b) Start in Standard, move to Standard-IA after 30 days and keep until deletion, (c) Start in Standard, move to Standard-IA after 30 days, move to Glacier Flexible after 90 days and keep until deletion. Show your calculation steps. Assume no retrieval occurs after the initial 30-day period.

---

## Part 3: S3 Security Configuration (35 points)

### Task 3.1 — Enable Bucket Security Baseline

Apply the following security controls to your lab bucket:

Enable Block Public Access:

```bash
aws s3api put-public-access-block \
  --bucket cis4334-lab04-YOUR-ACCOUNT-ID \
  --public-access-block-configuration \
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
```

Enable default SSE-S3 encryption:

```bash
aws s3api put-bucket-encryption \
  --bucket cis4334-lab04-YOUR-ACCOUNT-ID \
  --server-side-encryption-configuration '{
    "Rules": [
      {
        "ApplyServerSideEncryptionByDefault": {
          "SSEAlgorithm": "AES256"
        },
        "BucketKeyEnabled": true
      }
    ]
  }'
```

Verify both settings:

```bash
aws s3api get-public-access-block \
  --bucket cis4334-lab04-YOUR-ACCOUNT-ID

aws s3api get-bucket-encryption \
  --bucket cis4334-lab04-YOUR-ACCOUNT-ID
```

**Deliverable 3.1:** Output of both verification commands confirming the settings are applied.

### Task 3.2 — Write a Security-Compliant Bucket Policy

Write a bucket policy for your lab bucket that enforces both of the following:

- All requests must use HTTPS (deny HTTP requests)
- Access is only permitted from a specific VPC endpoint (use the placeholder VPC endpoint ID `vpce-0123456789abcdef0`)

**Deliverable 3.2:** Complete bucket policy JSON that enforces both requirements simultaneously in a single policy document. Explain in one paragraph why both conditions are needed and what threat each one prevents.

### Task 3.3 — Security Gap Analysis

The following S3 configuration was found in a production AWS account. Identify all security gaps and risks, and for each one provide the specific remediation:

```text
Bucket name: prod-customer-data-bucket
Block Public Access: All four settings are DISABLED
Default encryption: Disabled
Bucket policy: No bucket policy configured
Versioning: Disabled
Object Lock: Not enabled
Replication: Not configured
CloudTrail data events: Not enabled
```

The bucket stores sensitive customer PII (names, email addresses, phone numbers) for a company processing payments under PCI DSS requirements.

**Deliverable 3.3:** Security gap analysis with at least six identified gaps, the specific risk each gap creates, and the concrete remediation action. For each gap, identify whether it is required for PCI DSS compliance or represents general best practice.

---

## Cleanup

Delete the lab bucket and all its contents after completing the lab:

```bash
aws s3 rb s3://cis4334-lab04-YOUR-ACCOUNT-ID --force
```

**Deliverable — Cleanup:** Paste the output confirming the bucket was deleted.

---

## Submission Instructions

Compile all deliverables into a single document labeled clearly by task number. Include all CLI output verbatim and all JSON exactly as written. Submit to the Canvas assignment portal before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|---|---|---|
| Part 1: Storage Class Selection | 25 | Correct class for each scenario with accurate reasoning; minimum duration implications correctly identified |
| Part 2: Lifecycle Policy | 40 | Valid lifecycle policy JSON applied successfully; minimum four errors identified in the flawed policy; cost calculation shows correct methodology |
| Part 3: S3 Security | 35 | All four Block Public Access settings enabled; HTTPS enforcement and VPC endpoint restriction correctly implemented in one policy; minimum six security gaps identified with accurate PCI DSS classification |
| **Total** | **100** | |
