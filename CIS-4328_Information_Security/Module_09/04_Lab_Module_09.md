# Lab: Module 09 — Cloud Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

**Title:** Auditing and Hardening Cloud Storage Security

**Duration:** Approximately 75 minutes

**Environment:** AWS Free Tier (no cost expected) and manual configuration audit worksheet

**Skill Level:** Intermediate — assumes basic familiarity with web-based AWS console navigation

---

## Objectives

Upon completing this lab, you will be able to:

1. Identify misconfigured cloud storage settings that expose data publicly
2. Apply Block Public Access controls to an S3 bucket
3. Enable server-side encryption with customer-managed keys (SSE-KMS)
4. Configure S3 bucket access logging for audit trail purposes
5. Evaluate an S3 bucket policy for over-permissive access
6. Complete a cloud security configuration checklist against CIS Benchmark standards

---

## Prerequisites

- AWS Free Tier account (create at [https://aws.amazon.com/free/](https://aws.amazon.com/free/) if needed)
- Web browser
- This lab worksheet (keep open alongside the AWS console)
- Completed Module 09 video lectures and Reading Guide

---

## Safety and Cost Notice

This lab uses only AWS S3 within Free Tier limits (5 GB storage, 20,000 GET requests, 2,000 PUT requests per month). Do not upload large files. Delete all resources you create at the end of the lab using the cleanup instructions in Section 7.

---

## Part 1 — Create a Test S3 Bucket with Intentional Misconfigurations (15 minutes)

You will deliberately create an insecure bucket, then audit and fix it. This simulates what a security engineer finds during a cloud audit.

### Step 1.1 — Create the Bucket

1. Log into the AWS Management Console at [https://console.aws.amazon.com](https://console.aws.amazon.com)
2. Navigate to **S3** via the Services menu
3. Click **Create bucket**
4. Set bucket name: `txwes-cis4328-lab09-[your-initials]` (bucket names must be globally unique)
5. Set region: **US East (N. Virginia) us-east-1**
6. Under **Block Public Access settings for this bucket**: uncheck **Block all public access** and acknowledge the warning
7. Under **Default encryption**: leave as **Disabled** for now
8. Leave all other settings at defaults
9. Click **Create bucket**

**What you just did:** You created a bucket with public access potentially enabled and no encryption. This is a misconfiguration pattern found frequently in real breach investigations.

### Step 1.2 — Upload a Test File

1. Click your new bucket name to open it
2. Click **Upload**
3. Click **Add files** and upload any small text file (create a file named `test-data.txt` with the content "TXWES Lab 09 Test File — Not Sensitive")
4. Click **Upload**

### Step 1.3 — Record Initial State

Complete the following audit fields for your lab report:

| Configuration Item | Current Value | Compliant? |
|---|---|---|
| Block Public Access — Block all public access | Disabled | No |
| Default encryption | Disabled | No |
| Bucket versioning | Disabled | No |
| Server access logging | Disabled | No |
| Object lock | Disabled | N/A (optional) |

---

## Part 2 — Audit Bucket Access (10 minutes)

### Step 2.1 — Review the Bucket Policy

1. Navigate to your bucket → **Permissions** tab
2. Look at the **Bucket policy** section
3. If empty, note "No bucket policy — defaults to private"

### Step 2.2 — Check the Access Control List

1. Still in **Permissions**, find the **Access control list (ACL)** section
2. Review what permissions are listed for "Everyone (public access)"
3. Record what you see in your lab report

### Step 2.3 — Attempt to Make Object Public (Demonstration)

Because you disabled Block Public Access during creation, you can now observe how easily a public ACL can be set:

1. Click the **Objects** tab
2. Click `test-data.txt`
3. Click **Permissions** for this object
4. Note the current ACL status (should be owner-only at this point)

Do NOT make the object public — this step is observation only. The point is to recognize that without Block Public Access, a developer could easily enable public access on any object.

**Lab Reflection Question 1:** In the context of the shared responsibility model, if a developer in your organization accidentally makes an S3 bucket public and customer data is exposed, who is responsible — your organization or AWS? Explain your answer in two to three sentences.

---

## Part 3 — Enable Block Public Access (10 minutes)

### Step 3.1 — Enable the Guardrail

1. Navigate to your bucket → **Permissions** tab
2. Click **Edit** in the Block Public Access section
3. Check **Block all public access**
4. Click **Save changes** and type "confirm" when prompted

### Step 3.2 — Verify the Setting

1. Confirm the Block Public Access status now shows all four options as **On**
2. Update your audit table:

| Configuration Item | Current Value | Compliant? |
|---|---|---|
| Block Public Access — Block all public access | Enabled | Yes |

**Lab Reflection Question 2:** Block Public Access prevents public access even if a bucket policy or ACL would otherwise allow it. In what scenario would you legitimately disable this setting? What compensating controls would you put in place?

---

## Part 4 — Enable Encryption (15 minutes)

### Step 4.1 — Enable SSE-KMS

1. Navigate to your bucket → **Properties** tab
2. Scroll to **Default encryption** → click **Edit**
3. Select **AWS Key Management Service key (SSE-KMS)**
4. Under KMS key, select **AWS managed key (aws/s3)** — this is the AWS-managed KMS key (SSE-KMS with AWS-managed key, equivalent to SSE-KMS at no additional KMS cost for this lab)
5. Click **Save changes**

### Step 4.2 — Review Key Policy Implications

Navigate to **AWS KMS** in the console (search "KMS" in the Services menu):

1. Click **AWS managed keys**
2. Find the `aws/s3` key
3. Review the Key policy tab — note which principals can use this key

**Lab Reflection Question 3:** What is the difference between SSE-S3, SSE-KMS with AWS-managed keys, and SSE-KMS with customer-managed keys? When would you choose each option? (Three to four sentences.)

### Step 4.3 — Update Audit Table

| Configuration Item | Current Value | Compliant? |
|---|---|---|
| Default encryption | SSE-KMS (aws/s3) | Yes |

---

## Part 5 — Enable Versioning and Access Logging (10 minutes)

### Step 5.1 — Enable Versioning

1. Navigate to your bucket → **Properties** tab
2. Find **Bucket Versioning** → click **Edit**
3. Select **Enable**
4. Click **Save changes**

### Step 5.2 — Enable Server Access Logging

1. Still in **Properties**, find **Server access logging** → click **Edit**
2. Select **Enable**
3. For the target bucket, you can log to the same bucket with a prefix, or create a separate logging bucket
4. Enter prefix: `access-logs/`
5. Click **Save changes**

**Lab Reflection Question 4:** Why is it better practice to store access logs in a separate bucket rather than the bucket being monitored? What security principle does this support?

### Step 5.3 — Final Audit State

Update your complete audit table:

| Configuration Item | Final Value | Compliant? |
|---|---|---|
| Block Public Access — Block all public access | Enabled | Yes |
| Default encryption | SSE-KMS | Yes |
| Bucket versioning | Enabled | Yes |
| Server access logging | Enabled | Yes |

---

## Part 6 — Write a Simulated Bucket Policy and Evaluate It (10 minutes)

### Step 6.1 — Review a Sample Over-Permissive Policy

Examine the following bucket policy. Do NOT apply it — this is a desk exercise.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::example-bucket",
        "arn:aws:s3:::example-bucket/*"
      ]
    }
  ]
}
```

**Lab Reflection Question 5:** Identify at least three specific security problems with this bucket policy. For each problem, write one sentence describing the risk and one sentence describing the fix.

### Step 6.2 — Write a Corrected Policy

On paper or in a text editor, rewrite the policy above to:

- Allow read access (`s3:GetObject`) only
- Restrict access to a specific IAM role ARN (you can invent a realistic ARN: `arn:aws:iam::123456789012:role/AppReadRole`)
- Apply to all objects in the bucket but not bucket-level operations

Include your corrected policy in your lab report.

---

## Part 7 — Cleanup (5 minutes)

To avoid any unexpected charges and to keep your AWS account clean:

1. Navigate to your bucket
2. Click **Empty** and confirm — this deletes all objects and versions
3. After emptying, click **Delete bucket** and confirm by typing the bucket name
4. Navigate to **KMS** and verify no customer-managed keys were created (only AWS-managed keys were used; no action needed)

---

## Lab Report Submission Requirements

Submit a single document containing:

1. Your completed audit table (initial state and final state)
2. Answers to all five Lab Reflection Questions (numbered, full paragraphs)
3. Your corrected bucket policy from Step 6.2
4. One paragraph (five to seven sentences) describing how the misconfigurations you fixed in this lab relate to the shared responsibility model — specifically, what your organization was responsible for and what AWS provides automatically

**Format:** PDF or Word document

**Length:** Minimum 500 words excluding the policy JSON and tables

---

## Grading Rubric

| Component | Points |
|---|---|
| Audit tables — initial and final states complete and accurate | 20 |
| Lab Reflection Question 1 — shared responsibility explanation | 15 |
| Lab Reflection Question 2 — justified scenario for disabling Block Public Access | 15 |
| Lab Reflection Question 3 — SSE comparison (three options) | 15 |
| Lab Reflection Question 4 — logging separation rationale | 10 |
| Lab Reflection Question 5 — policy analysis (three problems identified) | 15 |
| Corrected bucket policy — syntactically valid, least-privilege | 10 |
| **Total** | **100** |

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 09*
