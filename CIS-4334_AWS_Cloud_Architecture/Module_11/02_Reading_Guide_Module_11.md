# Reading Guide: Module 11 — AWS IAM and Security Architecture

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

---

## Introduction

Security is the most cross-cutting topic on the SAA-C03 exam. IAM permissions errors are cited as the most common cause of cloud security incidents, and every architecture scenario has a security dimension. This guide provides the reference tables, policy evaluation logic, and decision frameworks needed to design secure AWS architectures and answer IAM and security scenario questions accurately.

---

## Section 1: IAM Policy Types and Structure

### 1.1 Policy Types

| Policy Type | Attached To | Includes Principal? | Scope |
|-------------|-------------|---------------------|-------|
| Identity-based (AWS Managed) | IAM user, group, or role | No | Actions the principal can take |
| Identity-based (Customer Managed) | IAM user, group, or role | No | Actions the principal can take |
| Identity-based (Inline) | Single user, group, or role (embedded) | No | Actions the principal can take |
| Resource-based | AWS resource (S3, SQS, KMS, Lambda) | Yes | Who can take actions on this resource |
| Permission Boundary | IAM user or role | No | Maximum permissions (cannot grant beyond boundary) |
| Session Policy | STS temporary session | No | Maximum permissions for a session |
| Service Control Policy (SCP) | AWS Organizations OU or account | No | Maximum permissions for all principals in scope |
| ACL | S3 bucket or object (legacy) | Yes | Access from other accounts (largely superseded by bucket policies) |

### 1.2 IAM Policy JSON Structure

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadSpecificBucket",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        }
      }
    }
  ]
}
```

Key elements:

- `Version`: always use `"2012-10-17"` (the current policy language version)
- `Effect`: `"Allow"` or `"Deny"`
- `Principal`: who this applies to (resource-based policies only)
- `Action`: list of AWS API actions (e.g., `s3:GetObject`, `ec2:DescribeInstances`, `*`)
- `Resource`: ARN(s) of the resources this statement applies to
- `Condition`: optional — further restricts when the statement applies

### 1.3 Policy Evaluation Logic

```
Request arrives → Is there an explicit DENY in any policy? → YES → DENY (final)
                                                         → NO ↓
                     Is there a Service Control Policy? → Does SCP allow this action?
                                                       → NO → DENY (final)
                                                       → YES ↓
                     Is there a Permission Boundary? → Does boundary allow this action?
                                                    → NO → DENY (final)
                                                    → YES ↓
                     Is there an explicit ALLOW in an identity-based policy? → YES → ALLOW
                     AND/OR resource-based policy grants cross-account access? → YES → ALLOW
                     Neither? → IMPLICIT DENY (final)
```

**Critical rule:** An explicit Deny in ANY attached policy always overrides any Allow, regardless of where the Allow comes from.

---

## Section 2: IAM Roles and AWS STS

### 2.1 IAM Role Components

| Component | Description |
|-----------|-------------|
| Trust Policy | Defines WHO can assume this role (the principal) |
| Permissions Policy | Defines WHAT this role can do (actions and resources) |
| Role ARN | The identifier used in AssumeRole API calls |
| Maximum Session Duration | How long temporary credentials are valid (15 min to 12 hours) |

### 2.2 STS API Operations

| API Call | Used By | Purpose |
|----------|---------|---------|
| AssumeRole | AWS accounts, IAM users | Cross-account or same-account role assumption |
| AssumeRoleWithWebIdentity | Applications using OIDC providers | Federation with Cognito, Google, Facebook |
| AssumeRoleWithSAML | Enterprise applications | Federation with SAML 2.0 IdP (Active Directory) |
| GetSessionToken | IAM users with MFA | Obtain temporary credentials with MFA enforcement |

### 2.3 Common Role Use Cases

| Use Case | Trust Principal | Example |
|----------|----------------|---------|
| EC2 instance accessing S3 | ec2.amazonaws.com | Instance needs to read config from S3 |
| Lambda function accessing DynamoDB | lambda.amazonaws.com | Function writes to DynamoDB table |
| ECS task accessing Secrets Manager | ecs-tasks.amazonaws.com | Container reads database password |
| Cross-account access | arn:aws:iam::ACCOUNT_ID:root | Account A assumes role in Account B |
| CI/CD pipeline deploying to AWS | oidc provider | GitHub Actions assumes a deployment role |

### 2.4 Instance Profile vs. IAM Role

An **instance profile** is a container that passes an IAM role to an EC2 instance. When you create an IAM role for EC2, an instance profile of the same name is automatically created. You associate the instance profile (not the role directly) with an EC2 instance at launch. Applications running on the instance retrieve temporary credentials via the EC2 metadata service at `http://169.254.169.254/latest/meta-data/iam/security-credentials/`.

---

## Section 3: AWS Organizations and Service Control Policies

### 3.1 AWS Organizations Structure

| Level | Description |
|-------|-------------|
| Management Account | Root of the organization; cannot have SCPs applied |
| Organizational Root | Top-level container; all accounts descend from here |
| Organizational Unit (OU) | Logical grouping of accounts (Production, Development, Security) |
| Member Account | Individual AWS account within the organization |

### 3.2 SCP Behavior

| Behavior | Description |
|----------|-------------|
| SCPs restrict, not grant | An SCP alone never gives permissions; IAM policies must also allow |
| Deny overrides everything | An SCP explicit Deny cannot be overridden by any IAM policy |
| Effective permissions | Intersection of SCP-allowed permissions AND IAM-allowed permissions |
| Does not apply to | Management account (root account of the organization) |
| Cascades down | SCP on an OU applies to all accounts and sub-OUs beneath it |

### 3.3 Common SCP Examples

Prevent disabling CloudTrail (governance guardrail):

```json
{
  "Effect": "Deny",
  "Action": [
    "cloudtrail:DeleteTrail",
    "cloudtrail:StopLogging",
    "cloudtrail:UpdateTrail"
  ],
  "Resource": "*"
}
```

Restrict to specific regions only:

```json
{
  "Effect": "Deny",
  "Action": "*",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "aws:RequestedRegion": ["us-east-1", "us-west-2"]
    }
  }
}
```

---

## Section 4: AWS KMS

### 4.1 KMS Key Types

| Key Type | Created By | Rotation | Key Policy | Cost |
|----------|-----------|----------|------------|------|
| AWS Managed Key | AWS service (auto) | Every 3 years (automatic) | Managed by AWS | Free |
| Customer Managed Key (CMK) | You | Configurable (annually by default when enabled) | Fully configurable | $1/month + API |
| AWS Owned Key | AWS (internal) | AWS-managed | Not accessible | Free |

### 4.2 Envelope Encryption Flow

```
Encrypt:
  1. Call KMS GenerateDataKey → returns plaintext data key + encrypted data key
  2. Use plaintext data key to encrypt data locally (AES-256)
  3. Store encrypted data + encrypted data key together
  4. Delete plaintext data key from memory

Decrypt:
  1. Retrieve encrypted data key
  2. Call KMS Decrypt → returns plaintext data key
  3. Use plaintext data key to decrypt data locally
  4. Delete plaintext data key from memory
```

The CMK never leaves KMS. All encryption/decryption of the data key happens inside KMS's hardware security modules.

### 4.3 KMS Key Policy

Every KMS key has a resource-based policy called the key policy. The key policy must explicitly grant the AWS account permission to use the key via IAM — without this, IAM policies alone cannot grant KMS access. A key policy that includes `"Principal": {"AWS": "arn:aws:iam::ACCOUNT_ID:root"}` delegates key access to IAM policies in the account.

### 4.4 KMS Integration with AWS Services

KMS integrates natively with: S3 (SSE-KMS), EBS (volume encryption), RDS and Aurora, DynamoDB, Secrets Manager, SSM Parameter Store, Lambda environment variables, CloudWatch Logs, Kinesis, SQS, SNS, and dozens of others. When you select "encrypt with KMS key" on any of these services, they use envelope encryption transparently.

---

## Section 5: AWS CloudTrail

### 5.1 CloudTrail Event Types

| Event Type | What It Records | Enabled by Default | Cost |
|------------|----------------|-------------------|------|
| Management events | API calls on AWS resources (control plane) | Yes (90-day history in console) | Free for read/write; additional events cost |
| Data events | S3 GetObject/PutObject, Lambda invocations | No | Per event charge |
| Insights events | Unusual API activity detection | No | Per event charge |

### 5.2 CloudTrail Log Record Fields

| Field | Description |
|-------|-------------|
| eventTime | When the API call was made |
| eventName | The API action called (e.g., CreateBucket, DeleteInstance) |
| eventSource | The AWS service called (s3.amazonaws.com, ec2.amazonaws.com) |
| userIdentity | Who made the call (IAM user, role, AWS service) |
| sourceIPAddress | IP address of the requester |
| requestParameters | Parameters passed in the API call |
| responseElements | What was returned or created |
| errorCode / errorMessage | Present if the call failed |

### 5.3 CloudTrail Log Integrity

CloudTrail supports log file integrity validation. When enabled, CloudTrail creates a hash of each log file and a digest file every hour. You can use the AWS CLI to validate that log files have not been tampered with. This is required for compliance scenarios that demand tamper-evident audit logs.

---

## Section 6: Amazon GuardDuty

### 6.1 GuardDuty Data Sources

| Data Source | What GuardDuty Analyzes |
|-------------|------------------------|
| VPC Flow Logs | Network traffic patterns, port scanning, unusual destinations |
| CloudTrail Management Events | API anomalies, credential theft patterns |
| CloudTrail S3 Data Events | Unusual S3 data access patterns, exfiltration |
| DNS Logs | Domain lookups to known malicious domains (C2 detection) |
| EKS Audit Logs | Suspicious activity in Kubernetes clusters |
| RDS Login Events | Brute force and unusual DB login patterns |

### 6.2 GuardDuty Finding Categories

| Category | Example Finding |
|----------|----------------|
| Unauthorized access | `UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B` — login from unusual location |
| Instance compromise | `Backdoor:EC2/C&CActivity.B` — EC2 instance communicating with known C2 server |
| Data exfiltration | `Exfiltration:S3/AnomalousBehavior` — unusual S3 data transfer |
| Credential threat | `CredentialAccess:IAMUser/AnomalousBehavior` — unusual API calls for a user |
| Cryptocurrency mining | `CryptoCurrency:EC2/BitcoinTool.B!DNS` — EC2 DNS lookups for crypto mining domains |

---

## Section 7: Security Hub, WAF, and Shield

### 7.1 Security Hub

| Feature | Description |
|---------|-------------|
| Purpose | Unified security posture and findings aggregation |
| Input sources | GuardDuty, Inspector, Macie, IAM Access Analyzer, Config, third-party tools |
| Standards supported | AWS FSBP, CIS Benchmarks, PCI DSS, NIST |
| Multi-account support | Designate an administrator account to aggregate findings across org |
| Automated response | EventBridge integration for automated remediation |

### 7.2 WAF vs. Shield

| Feature | AWS WAF | AWS Shield Standard | AWS Shield Advanced |
|---------|---------|---------------------|---------------------|
| Layer | Application (Layer 7) | Network/Transport (L3/L4) | L3/L4 and L7 (with WAF) |
| Protection type | HTTP filter rules | DDoS volumetric attacks | Enhanced DDoS + L7 |
| Cost | Per rule/per request | Free (automatic) | $3,000/month + data transfer |
| Managed rules | Yes (AWS and marketplace) | N/A | N/A |
| Integration | CloudFront, ALB, API GW | All AWS resources | CloudFront, ALB, ELB, EC2 |
| 24/7 DRT support | No | No | Yes |

### 7.3 WAF Rule Types

| Rule Type | Description | Example |
|-----------|-------------|---------|
| IP set | Allow or block specific IPs or CIDRs | Block known malicious IP ranges |
| Rate-based | Limit requests from a single IP per 5 minutes | Block if > 2000 requests from one IP |
| Managed rule group | AWS or marketplace rules for common threats | AWS-ManagedRulesCommonRuleSet (OWASP Top 10) |
| SQL injection | Detect and block SQL injection patterns | Block requests with SQL in query params |
| XSS | Detect and block cross-site scripting | Block requests with script tags in headers |
| Geo match | Allow or block by country | Block requests from specific countries |

---

## Section 8: Additional Security Services

### 8.1 Amazon Macie

Amazon Macie uses machine learning to automatically discover, classify, and protect sensitive data in S3. It identifies personally identifiable information (PII), financial data, credentials, and other sensitive data types. Macie findings appear in Security Hub.

### 8.2 AWS Inspector

AWS Inspector automatically scans EC2 instances and container images for software vulnerabilities and unintended network exposure. Inspector integrates with ECR to scan images as they are pushed. Findings appear in Security Hub.

### 8.3 IAM Access Analyzer

IAM Access Analyzer identifies resources in your account that are shared with external accounts or the public — S3 buckets, IAM roles, KMS keys, Lambda functions, SQS queues, Secrets Manager secrets. It helps identify unintended public access and cross-account sharing.

---

## Section 9: SAA-C03 Exam Tips for Module 11

**Exam Tip 1 — Explicit Deny always wins:**
No matter where an Allow comes from — an IAM policy, a resource-based policy, a session policy — an explicit Deny in ANY attached policy overrides it. SCPs can effectively "deny" by not including an Allow.

**Exam Tip 2 — Roles for AWS services, not long-term access keys:**
Any scenario where an EC2 instance, Lambda function, or ECS task needs AWS permissions should use an IAM role (via instance profile, execution role, or task role). Long-term access keys in application code or on EC2 instances are an anti-pattern and a security risk.

**Exam Tip 3 — SCPs are restrictive guardrails, not grants:**
SCPs never directly grant permissions. They define the ceiling of what IAM policies can authorize. A member account principal needs both an SCP-allowed permission AND an IAM policy that allows it. The SCP must not deny it, and the IAM policy must allow it.

**Exam Tip 4 — Customer Managed Keys for custom key policies:**
If a scenario requires audit of key usage in CloudTrail, custom access controls on who can use the key, or key rotation control, the answer is a Customer Managed KMS Key. AWS Managed Keys do not provide this control.

**Exam Tip 5 — CloudTrail for audit, GuardDuty for threat detection:**
CloudTrail records API calls (who did what, when). GuardDuty analyzes those logs (and others) to detect threats. They are complementary, not alternatives. "Audit trail for compliance" → CloudTrail. "Detect compromised credentials or unusual activity" → GuardDuty.

**Exam Tip 6 — WAF for Layer 7, Shield for DDoS:**
WAF filters HTTP/HTTPS requests based on rules (SQL injection, XSS, rate limits, IP blocks). Shield protects against DDoS volumetric attacks. A scenario mentioning "SQL injection" or "HTTP flooding" → WAF. "DDoS attack" or "volumetric attack" → Shield. Both can be used together.

**Exam Tip 7 — Security Hub aggregates findings:**
If a scenario says "central view of security findings across multiple AWS accounts and services" → Security Hub. It aggregates from GuardDuty, Inspector, Macie, and others.

**Exam Tip 8 — IAM Access Analyzer for unintended public access:**
If a scenario mentions "identifying S3 buckets or IAM roles that are accessible from outside the account" → IAM Access Analyzer.

---

## Section 10: Key CLI Commands

Create a Customer Managed KMS Key:

```bash
aws kms create-key \
  --description "CIS4334 Lab CMK" \
  --key-usage ENCRYPT_DECRYPT \
  --origin AWS_KMS

aws kms create-alias \
  --alias-name alias/cis4334-lab-key \
  --target-key-id KEY_ID_FROM_ABOVE
```

Encrypt a value with KMS:

```bash
aws kms encrypt \
  --key-id alias/cis4334-lab-key \
  --plaintext "mysecretpassword" \
  --query "CiphertextBlob" \
  --output text | base64 --decode > encrypted.bin
```

Look up recent CloudTrail events:

```bash
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=CreateBucket \
  --start-time $(date -d '24 hours ago' '+%Y-%m-%dT%H:%M:%SZ') \
  --query "Events[*].{Time:EventTime,User:Username,Event:EventName}"
```

Enable GuardDuty:

```bash
aws guardduty create-detector \
  --enable \
  --finding-publishing-frequency FIFTEEN_MINUTES
```

---

## Section 11: Study Checklist

- [ ] Write an IAM policy from memory with Effect, Action, Resource, and Condition elements
- [ ] Explain the policy evaluation order: SCP → Permission Boundary → Identity-based → Resource-based
- [ ] Describe the three STS API operations and when each is used
- [ ] Explain the difference between an IAM role trust policy and a permissions policy
- [ ] Describe how SCPs work and why they do not apply to the management account
- [ ] Explain envelope encryption: what a data key is, where the CMK fits, and why data doesn't go through KMS directly
- [ ] Name the three KMS key types and when a Customer Managed Key is required
- [ ] Describe what CloudTrail records, the three event types, and what the key fields in a log record contain
- [ ] Explain GuardDuty's data sources and name four finding categories
- [ ] Distinguish WAF from Shield — what each protects against and at which OSI layer
- [ ] Describe Security Hub's role: what it aggregates and what standards it evaluates against
- [ ] Run the CLI commands in Section 10 and record the output
- [ ] Complete the Module 11 quiz with a score of at least 80 percent

---

## References

All AWS certification study materials and exam registration: aws.amazon.com/certification

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
