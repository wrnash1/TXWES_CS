# Reading Guide: Module 02 - IAM: Users, Roles, Policies, and Best Practices

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Introduction

IAM is the authorization and authentication backbone of AWS. Every request to every AWS service is evaluated by IAM before it is permitted. This module builds the skills to design, read, and evaluate IAM configurations with precision — skills the SAA-C03 exam tests in nearly every domain through scenario-based questions involving permissions, access control, and cross-account architecture.

---

## Section 1: IAM Identity Types Compared

### 1.1 Identity Comparison Table

| Identity Type | Has Long-Term Credentials | Can Be Assumed | Best Used For |
|---|---|---|---|
| IAM User | Yes (password, access keys) | No | Individual humans, legacy automation |
| IAM Group | No | No | Organizing users for bulk policy assignment |
| IAM Role | No (temporary credentials via STS) | Yes | Applications on AWS, cross-account access, federation |
| Federated Identity | No (uses external IdP tokens) | Via role | SSO from Active Directory, Cognito, Google, etc. |

### 1.2 When to Use Each Identity Type

IAM users are appropriate when a human needs console access or when automation outside of AWS (such as a CI/CD pipeline running on-premises) needs programmatic access and a role is not available. For any workload running on AWS compute — EC2, Lambda, ECS, EKS — use an IAM role. Embedding access keys in code or configuration files is an anti-pattern that creates credential exposure risk.

IAM groups simplify permission management. Instead of attaching policies to each user individually, attach policies to a group (for example, Developers, Operators, ReadOnly) and manage group membership. Users inherit permissions from all groups they belong to plus any policies attached directly to their user account.

IAM roles use the AWS Security Token Service (STS) to issue temporary credentials when the role is assumed. Key role use cases:

- EC2 instance profile: application on EC2 retrieves temporary creds from instance metadata
- Lambda execution role: Lambda assumes this role to call other AWS services
- ECS task role: individual container tasks assume this role at runtime
- Cross-account role: trusted account assumes a role in the trusting account
- Service-linked role: automatically created and managed by specific AWS services

---

## Section 2: IAM Policy Anatomy

### 2.1 Policy Document Structure

Every IAM policy is a JSON document with this top-level structure:

```json
{
  "Version": "2012-10-17",
  "Statement": [ ]
}
```

The Version field must be `"2012-10-17"` for all new policies. An older version string `"2008-10-17"` still exists but lacks several policy language features. Always use 2012-10-17.

The Statement array contains one or more statement objects. Each statement has these fields:

| Field | Required | Description |
|---|---|---|
| Sid | No | Statement ID — optional human-readable label |
| Effect | Yes | Allow or Deny |
| Principal | Conditional | Who the policy applies to (required in resource-based policies) |
| Action | Yes | List of AWS API operations (e.g., s3:GetObject) |
| Resource | Yes | ARN(s) of the target resource(s) |
| Condition | No | Conditions under which the statement applies |

### 2.2 Least-Privilege Policy Example

The following policy grants an application role permission to read objects from a specific S3 bucket and write to a specific DynamoDB table. Nothing else is permitted.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadS3AppData",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::app-data-bucket",
        "arn:aws:s3:::app-data-bucket/*"
      ]
    },
    {
      "Sid": "WriteDynamoOrderTable",
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:GetItem"
      ],
      "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Orders"
    }
  ]
}
```

Note the specificity: only two services, only the required actions within each service, only the specific resources needed. This is least-privilege design.

### 2.3 Deny Override Example with Condition

This policy denies all actions unless MFA is active. It is used to enforce MFA before any privileged action:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyWithoutMFA",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "BoolIfExists": {
          "aws:MultiFactorAuthPresent": "false"
        }
      }
    }
  ]
}
```

The `BoolIfExists` operator applies the condition only when the key is present in the request context. This prevents the condition from accidentally blocking API calls made by roles (which do not have MFA context).

### 2.4 Cross-Account Trust Policy Example

This role trust policy allows an IAM user in account 111122223333 to assume the role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
```

The Condition requiring MFA means the assuming user must have authenticated with MFA before assuming this role. This is a best-practice pattern for privileged cross-account operations.

### 2.5 Resource-Based Policy Example (S3 Bucket Policy)

This bucket policy allows a specific IAM role from account 999988887777 to read from the bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CrossAccountReadAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::999988887777:role/DataAnalyticsRole"
      },
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::shared-analytics-data",
        "arn:aws:s3:::shared-analytics-data/*"
      ]
    }
  ]
}
```

Resource-based policies (like this bucket policy) allow cross-account access without requiring the trusting account to create an IAM role. The identity in account 999988887777 does not need to call sts:AssumeRole — the bucket policy grants access directly.

---

## Section 3: IAM Policy Evaluation Logic

### 3.1 Full Evaluation Order

When AWS receives an API request, it evaluates all applicable policies in this order:

1. Explicit Deny in any SCP — if an SCP at any Organizations level denies the action, the request is denied immediately. No further evaluation.
2. Explicit Deny in any identity-based or resource-based policy — if any policy attached to the calling identity or the target resource explicitly denies the action, the request is denied.
3. Explicit Allow in an identity-based policy and (for cross-account requests) a resource-based policy — both must allow for cross-account access without role assumption.
4. Implicit Deny — if no explicit Allow is found after exhausting all policies, the request is denied.

### 3.2 Policy Evaluation Scenarios

| Scenario | SCP | Identity Policy | Resource Policy | Result |
|---|---|---|---|---|
| Same-account, identity Allow | Allow s3:* | Allow s3:GetObject | None | Allow |
| Same-account, explicit Deny | Allow s3:* | Deny s3:DeleteObject | None | Deny |
| Cross-account, both Allow | Allow s3:* | Allow s3:GetObject | Allow from Account A | Allow |
| Cross-account, missing resource policy | Allow s3:* | Allow s3:GetObject | None | Deny |
| SCP Deny overrides identity Allow | Deny s3:DeleteBucket | Allow s3:DeleteBucket | None | Deny |

### 3.3 Permission Boundaries

A permission boundary is an advanced policy that sets the maximum permissions an IAM entity can have. The effective permissions are the intersection of the identity policy and the permission boundary — only actions allowed by both are permitted.

Example: An identity policy grants `s3:*`. The permission boundary allows only `s3:GetObject` and `s3:ListBucket`. The effective permissions are only `s3:GetObject` and `s3:ListBucket` — even though the identity policy grants full S3 access.

Permission boundaries are used in organizations that delegate IAM administration to application teams. The central security team sets a permission boundary that prevents teams from granting themselves permissions beyond a defined scope, even if they create their own IAM policies.

---

## Section 4: IAM Roles Deep Dive

### 4.1 Role Assumption Flow

When an entity assumes an IAM role:

1. The entity calls `sts:AssumeRole` with the target role ARN.
2. AWS STS validates that the entity's trust policy permits the assumption.
3. STS issues temporary credentials: access key ID, secret access key, session token.
4. The entity uses these temporary credentials to make API calls under the role's permissions.
5. Credentials expire (default 1 hour for role assumptions, configurable up to 12 hours).

### 4.2 EC2 Instance Metadata and Credentials

When an EC2 instance has an instance profile attached, the AWS SDK retrieves credentials automatically from the Instance Metadata Service:

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/MyRoleName
```

The response includes AccessKeyId, SecretAccessKey, Token, and Expiration. The SDK handles retrieval and refresh transparently. Application code never stores or rotates credentials.

IMDSv2 (Instance Metadata Service version 2) requires a session-oriented request that includes a PUT call to obtain a session token before reading metadata. Enable IMDSv2 enforcement on all instances to prevent SSRF attacks that could extract metadata:

```bash
aws ec2 modify-instance-metadata-options \
  --instance-id i-1234567890abcdef0 \
  --http-tokens required \
  --http-endpoint enabled
```

### 4.3 Service-Linked Roles

Service-linked roles are IAM roles automatically created by specific AWS services with a predefined trust policy and permissions policy. You cannot manually edit their trust policy or permissions. Examples: AWSServiceRoleForECS (created by ECS), AWSServiceRoleForElasticLoadBalancing (created by ELB). These roles allow the service to perform actions on your behalf — creating ENIs, registering targets, writing logs — without requiring you to configure IAM manually for each service integration.

---

## Section 5: IAM Best Practices Reference

### 5.1 Account-Level Best Practices

| Practice | Action |
|---|---|
| Lock root account | Enable MFA, delete root access keys, store root password in secure vault |
| Use IAM admin user | Create an IAM user with AdministratorAccess for day-to-day admin tasks |
| Enable IAM Access Analyzer | Identifies unintended external access to your resources |
| Enable CloudTrail | Logs all IAM API calls for auditing |
| Review IAM credential report | Audit all users, last-used dates, MFA status, key age |
| Use AWS Organizations SCPs | Set guardrails at the organization level |

### 5.2 User-Level Best Practices

| Practice | Action |
|---|---|
| Enable MFA for all users | Require virtual or hardware MFA for console login |
| Apply least-privilege policies | Use Customer Managed Policies with specific actions and resources |
| Rotate access keys every 90 days | Automate rotation with IAM and Secrets Manager |
| Delete unused credentials | Deactivate then delete keys and passwords not used in 90 days |
| Use groups for permissions | Never attach policies directly to individual users |

### 5.3 Application-Level Best Practices

| Practice | Action |
|---|---|
| Use IAM roles for EC2, Lambda, ECS | Attach instance profiles and task roles, never hardcode keys |
| Use Secrets Manager for DB credentials | Rotate database passwords automatically |
| Enable IMDSv2 | Prevent SSRF-based metadata credential theft |
| Scope roles to minimum actions | Create one role per application function, not one per account |
| Use condition keys in policies | Restrict by source IP, MFA presence, request time as appropriate |

---

## Section 6: Over-Permission Analysis

When auditing a policy for over-permissions, check for these anti-patterns:

- Wildcard actions: `"Action": "*"` or `"Action": "s3:*"` — grants more than needed
- Wildcard resources: `"Resource": "*"` — applies to all resources of the type, not just the intended one
- Missing conditions: no MFA requirement on privileged actions, no IP restriction on sensitive data
- Unnecessary services: policy grants EC2 actions to an application role that only needs S3
- Admin policies on non-admin users: AdministratorAccess or PowerUserAccess on regular application roles

---

## Section 7: SAA-C03 Exam Tips for Module 02

**Exam Tip 1 — Explicit Deny always wins:**
In any multi-policy evaluation scenario, if any applicable policy contains an explicit Deny for the requested action, the request is denied. There are no exceptions. SCPs, identity policies, permission boundaries, and resource policies can all contribute Deny statements.

**Exam Tip 2 — Roles over users for AWS workloads:**
Any exam scenario where an application on AWS (EC2, Lambda, ECS) needs to access another AWS service should use an IAM role, not IAM user access keys. The phrase "least effort" or "most secure" in the question stem is a signal to choose roles.

**Exam Tip 3 — Cross-account access patterns:**
Cross-account access via role assumption requires: (1) a trust policy on the role in the trusting account that lists the principal from the trusted account, and (2) an identity policy on the principal in the trusted account that allows sts:AssumeRole for the target role ARN. Both must be in place.

**Exam Tip 4 — Resource-based policies for same-account shortcut:**
When a resource-based policy (like an S3 bucket policy) grants access to a principal in the same account, that principal does not also need an identity-based policy to access the resource. The resource-based policy is sufficient for same-account access.

**Exam Tip 5 — SCPs do not grant permissions:**
An SCP that allows `s3:*` does not grant any S3 permissions. SCPs set the maximum ceiling. The IAM identity in the account still needs an Allow in its own identity-based policy. If an SCP denies a service entirely, no identity in the account can use that service regardless of their IAM policies.

**Exam Tip 6 — Permission boundary vs. SCP:**
Both are guardrails, but they operate at different levels. SCPs are applied at the AWS Organizations level and affect all identities in an account. Permission boundaries are applied to individual IAM users or roles. You can use both simultaneously — the effective permissions are the intersection of all three: SCP, permission boundary, and identity policy.

**Exam Tip 7 — IAM is global:**
IAM is a global service. IAM users, groups, roles, and policies exist at the account level and are not scoped to a Region. When you create an IAM role, it is available in all Regions. This is different from EC2 key pairs, which are regional.

**Exam Tip 8 — Policy condition operators:**
The exam tests common condition operators. `StringEquals` for exact string match. `StringLike` for wildcard string match. `ArnLike` for ARN pattern match. `Bool` for boolean checks. `IpAddress` for CIDR-based source IP restriction. `DateLessThan` for time-based restrictions. Know when to use each.

---

## Section 8: Key CLI Commands for Module 02

List all IAM users in the account:

```bash
aws iam list-users --output table
```

Get a specific user's attached policies:

```bash
aws iam list-attached-user-policies --user-name developer01
```

Generate an IAM credential report:

```bash
aws iam generate-credential-report
aws iam get-credential-report --query Content --output text | base64 -d
```

List all roles:

```bash
aws iam list-roles --output table
```

Get a role's trust policy:

```bash
aws iam get-role --role-name MyAppRole \
  --query "Role.AssumeRolePolicyDocument"
```

Simulate a policy evaluation:

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/MyAppRole \
  --action-names s3:GetObject \
  --resource-arns arn:aws:s3:::my-bucket/*
```

---

## Section 9: Study Checklist

- [ ] Define IAM user, group, role, and identity provider without referencing notes
- [ ] Explain the four-step IAM policy evaluation order from memory
- [ ] Write a least-privilege IAM policy JSON for a given application scenario
- [ ] Identify at least five over-permission anti-patterns in a sample policy
- [ ] Explain the difference between a permission boundary and a Service Control Policy
- [ ] Describe the EC2 instance metadata credential retrieval flow and explain why IMDSv2 is more secure
- [ ] Explain cross-account role assumption and identify both policies that must exist
- [ ] Run the CLI commands in Section 8 against your AWS account and record the output
- [ ] Complete the Module 02 quiz with a score of at least 80 percent
- [ ] Post your initial response in the Module 02 discussion forum by the Wednesday deadline

---

## References

All certification study materials and exam registration: aws.amazon.com/certification
