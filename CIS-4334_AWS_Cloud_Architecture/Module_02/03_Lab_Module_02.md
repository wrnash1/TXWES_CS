# Lab: Module 02 - IAM: Users, Roles, Policies, and Best Practices

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Points:** 100

---

## Lab Overview

This lab develops precision IAM skills through two core exercises that mirror real SAA-C03 exam scenarios: writing an IAM policy JSON document for a least-privilege access scenario, and analyzing an existing policy JSON for over-permissions. These are the most practically important IAM skills for both the certification exam and production cloud security work.

No billable resources are created in this lab. All work is policy analysis, policy authoring, and CLI inspection.

---

## Prerequisites

- AWS account with IAM user or role that has ReadOnlyAccess plus iam:SimulatePrincipalPolicy permission
- AWS CLI v2 installed and configured
- Text editor for JSON authoring
- Completed Module 02 video and reading guide

Verify CLI access before starting:

```bash
aws iam get-user
```

---

## Part 1: Write a Least-Privilege IAM Policy (40 points)

### Business Scenario

A software development team is building a web application on AWS with the following components:

- An EC2 instance (instance ID: i-0abc1234def567890) running the application server
- An S3 bucket named `webapp-user-uploads-prod` that stores user-uploaded files
- A DynamoDB table named `UserSessions` in us-east-1 (account ID: 123456789012) that stores session tokens
- A CloudWatch Logs log group named `/webapp/app-server` where the application writes logs

The application needs an IAM role (not a user) with a policy that allows exactly the following and nothing else:

- Read and write objects in the S3 bucket (not delete; not list all buckets)
- List objects in the S3 bucket
- Read and write items in the DynamoDB table (not delete; not scan the full table)
- Create log streams and put log events in the CloudWatch Logs log group

The policy must not use any wildcards in the Action field. Each action must be explicitly named.

### Task 1.1 — Draft the Policy JSON

Write the complete IAM policy JSON document that satisfies the requirements above. Your policy must:

- Use Version 2012-10-17
- Include a meaningful Sid for each statement
- Specify exact action names (no wildcards in Action)
- Specify exact resource ARNs (construct the DynamoDB and CloudWatch ARNs correctly)
- Use separate Statement blocks for each service

**Deliverable 1.1:** Submit your complete policy JSON. It will be evaluated for correctness of action names, ARN formatting, and absence of over-permissions.

### Task 1.2 — Validate the Policy Structure

Use the AWS CLI to validate your policy document syntax:

```bash
aws iam create-policy \
  --policy-name WebAppLeastPrivilegePolicy-Test \
  --policy-document file://my-policy.json \
  --description "Test policy for Module 02 lab" \
  --tags Key=Environment,Value=Lab
```

If the command succeeds, record the policy ARN from the output. Then clean up:

```bash
aws iam delete-policy \
  --policy-arn arn:aws:iam::123456789012:policy/WebAppLeastPrivilegePolicy-Test
```

**Deliverable 1.2:** Paste the CLI output confirming successful policy creation (showing the policy ARN). If the command returned an error, paste the error, identify the JSON problem, correct it, and re-run.

### Task 1.3 — Justify Each Permission

For each AWS service in your policy (S3, DynamoDB, CloudWatch Logs), write two to three sentences explaining why each specific action is required and why any potentially useful actions were intentionally excluded. For example: why is `s3:DeleteObject` excluded? Why is `dynamodb:Scan` excluded?

**Deliverable 1.3:** Three short justification paragraphs, one per service.

---

## Part 2: Analyze a Policy for Over-Permissions (35 points)

### Over-Permissioned Policy Under Review

The following IAM policy was found attached to an IAM role used by a billing report generator. The role's only job is to read cost and usage data from Cost Explorer and write a summary report as a CSV file to an S3 bucket named `billing-reports-archive`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CostExplorerAccess",
      "Effect": "Allow",
      "Action": "ce:*",
      "Resource": "*"
    },
    {
      "Sid": "S3ReportAccess",
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "*"
    },
    {
      "Sid": "GeneralReadAccess",
      "Effect": "Allow",
      "Action": [
        "iam:ListUsers",
        "iam:GetUser",
        "ec2:DescribeInstances",
        "ec2:DescribeRegions",
        "rds:DescribeDBInstances",
        "lambda:ListFunctions"
      ],
      "Resource": "*"
    }
  ]
}
```

### Task 2.1 — Identify All Over-Permission Problems

Review the policy and identify every over-permission problem. For each problem, state:

- The specific policy element that is overly permissive (Statement Sid, Action, or Resource field)
- Why it is a problem (what unintended actions does it permit?)
- What the corrected value should be

Present your findings as a structured list with one entry per identified problem.

**Deliverable 2.1:** Annotated list of over-permission findings (minimum five distinct problems).

### Task 2.2 — Rewrite the Policy

Write a corrected version of this policy that grants the billing report generator only the permissions it actually needs: read cost and usage data from Cost Explorer, and write objects to the specific S3 bucket.

**Deliverable 2.2:** Complete corrected policy JSON. It must have no wildcards in Action fields and must scope the S3 permissions to the specific bucket ARN only.

### Task 2.3 — Simulate the Original vs. Corrected Policy

Use the IAM Policy Simulator CLI to test one specific high-risk action against both the original and corrected policies.

First, create the original policy temporarily and simulate iam:CreateUser:

```bash
aws iam simulate-custom-policy \
  --policy-input-list file://original-policy.json \
  --action-names iam:CreateUser \
  --resource-arns "*"
```

Then simulate the same action against your corrected policy:

```bash
aws iam simulate-custom-policy \
  --policy-input-list file://corrected-policy.json \
  --action-names iam:CreateUser \
  --resource-arns "*"
```

**Deliverable 2.3:** Paste the output of both simulations. The original should show `allowed`; the corrected should show `implicitDeny`. Explain in one paragraph why an implicit deny is the expected result in the corrected policy.

---

## Part 3: IAM Trust Policy and Cross-Account Scenario (25 points)

### Cross-Account Architecture Scenario

Your organization has two AWS accounts:

- Account A (Production): 111122223333
- Account B (Security): 444455556666

The security team in Account B needs to read CloudTrail logs stored in an S3 bucket in Account A named `prod-cloudtrail-logs`. The security team uses an IAM role in Account B named `SecurityAuditRole`.

### Task 3.1 — Write the Trust Policy

Write the trust policy document for a new IAM role in Account A named `CrossAccountCloudTrailReadRole`. This trust policy must allow `SecurityAuditRole` from Account B (444455556666) to assume it, and must require MFA.

**Deliverable 3.1:** Complete trust policy JSON for `CrossAccountCloudTrailReadRole`.

### Task 3.2 — Write the Permissions Policy

Write the permissions policy that will be attached to `CrossAccountCloudTrailReadRole` in Account A. It must allow only the minimum S3 actions needed to list and read objects in `prod-cloudtrail-logs`.

**Deliverable 3.2:** Complete permissions policy JSON.

### Task 3.3 — Explain the Full Flow

In 100-150 words, describe the complete authentication and authorization flow that occurs when a member of the security team in Account B needs to read a CloudTrail log file from Account A. Include: who calls what API, what both policies check, and what credential type is used to access the bucket.

**Deliverable 3.3:** Written flow explanation.

---

## Submission Instructions

Compile all deliverables into a single document. Label each deliverable clearly (1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3). Include all policy JSON exactly as you would deploy it. Submit to the Canvas assignment portal before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|---|---|---|
| Part 1: Least-Privilege Policy | 40 | Correct action names (no wildcards); correct ARN format for all three services; separate statements per service; CLI validation successful |
| Part 2: Over-Permission Analysis | 35 | Minimum five problems identified with specific explanations; corrected policy eliminates all over-permissions; simulation output shows allow then implicitDeny with correct explanation |
| Part 3: Cross-Account Trust | 25 | Trust policy correctly references Account B role ARN with MFA condition; permissions policy scoped to specific bucket; flow explanation accurate and complete |
| **Total** | **100** | |

---

## Part 9 — Challenge Exercise

### Challenge 1: IAM Policy Simulator Validation
Use the AWS IAM Policy Simulator to test a policy you have written in this lab against specific API actions.
1. In the AWS Management Console, navigate to IAM → Policy Simulator (https://policysim.aws.amazon.com/).
2. Select the IAM role or user you created in Part 1 as the simulation principal.
3. Select Amazon S3 as the service and test at least four actions: `GetObject`, `PutObject`, `DeleteObject`, and `ListBucket`. For each action, specify the exact resource ARN you used in your policy.
4. Record the simulation result (allowed / denied) for each action and compare it to your expected results. If any result is unexpected, diagnose the cause and fix the policy.

### Challenge 2: IAM Credential Report Analysis
Generate an IAM credential report and analyze the security posture of all IAM users in your account.
1. Run `aws iam generate-credential-report` and then `aws iam get-credential-report --query Content --output text | base64 -d > credential_report.csv` to download the report.
2. Open the CSV and identify: (a) any IAM users with access keys older than 90 days, (b) any IAM users with console password access but no MFA enabled, and (c) any IAM users who have never used their access key.
3. For each finding, document the specific IAM best practice being violated and the recommended remediation step (rotate the key, enable MFA, or deactivate the unused key).

### Reflection Questions
1. After using the IAM Policy Simulator, explain one scenario where the simulation result differed from what you initially expected. What did this reveal about how IAM policy evaluation logic works in practice?
2. How does the AWS Well-Architected Framework Security pillar's principle of "apply security at all layers" apply to the combination of SCPs, permission boundaries, and identity policies you worked with in this lab? Which layer provides the strongest protection and why?
