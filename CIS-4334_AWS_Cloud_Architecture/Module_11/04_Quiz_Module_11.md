# Quiz: Module 11 — AWS IAM and Security Architecture

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A Lambda function needs to read secret values from AWS Secrets Manager. A developer suggests embedding an IAM user's access key in the Lambda function's environment variables. A solutions architect objects. What is the CORRECT approach?

A. Store the access key in an encrypted S3 bucket and have Lambda retrieve it at runtime

B. Assign an IAM execution role to the Lambda function with permissions to access Secrets Manager

C. Use a hardcoded access key in the Lambda code but rotate it every 90 days

D. Use Secrets Manager to store the IAM access key and have Lambda retrieve it (circular)

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Retrieving an access key from S3 still involves long-term credentials — now stored in S3 rather than environment variables. It adds complexity without solving the fundamental problem.
- B is correct. Lambda supports IAM execution roles, which provide temporary credentials via AWS STS automatically. The Lambda service injects temporary credentials for the role into the execution environment. The function calls Secrets Manager using these temporary credentials without any hardcoded keys.
- C is incorrect. Hardcoded long-term access keys are a security risk regardless of rotation frequency. Rotation creates a manual process, and if the code repository is leaked, the key is exposed. Temporary credentials from IAM roles are the AWS-endorsed pattern.
- D is incorrect. Using Secrets Manager to store the IAM key creates a circular dependency — the Lambda needs credentials to access Secrets Manager, which stores the credentials it needs to access Secrets Manager. The solution is to eliminate the long-term credential entirely using an execution role.

---

### Question 2

A company uses AWS Organizations with an SCP attached to the Production OU that denies `ec2:RunInstances` for any instance type other than t3.micro, t3.small, and m6i.large. An IAM admin in a Production OU member account has an IAM policy with `ec2:RunInstances` on all resources with no conditions. They attempt to launch a c6g.xlarge instance and it fails. Why?

A. The IAM admin's policy does not include the correct ARN for c6g.xlarge instances

B. The SCP restricts the effective permissions in the member account even though the IAM policy allows it

C. c6g.xlarge is not available in the Production OU's region

D. The IAM admin needs a Permission Boundary that explicitly allows c6g.xlarge

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. EC2 RunInstances is specified by resource ARN in the policy — there is no instance-type-specific ARN condition in the IAM policy. The IAM policy grants the action on all resources.
- B is correct. SCPs define the maximum permissions available to all principals in a member account. Even if an IAM policy grants a permission, the SCP restricts what permissions can be exercised. The effective permissions are the intersection of SCP-allowed and IAM-allowed. The SCP's implicit deny on c6g.xlarge overrides the IAM allow.
- C is incorrect. The scenario doesn't mention region availability, and instance availability is not determined by OU membership.
- D is incorrect. Permission Boundaries are IAM constructs, not SCP constructs. They define maximum permissions for an IAM user or role. The issue here is the SCP, not a missing permission boundary.

---

### Question 3

A security engineer discovers that an S3 bucket policy has a statement with `"Principal": "*"` and `"Action": "s3:GetObject"`. The IAM policies for all IAM users in the account explicitly deny `s3:GetObject` on this bucket. Can unauthenticated public requests access objects in this bucket?

A. No — the IAM explicit deny overrides the bucket policy allow for all requests

B. Yes — for public (unauthenticated) requests, resource-based policies are evaluated alone and the bucket policy allow takes effect

C. No — `"Principal": "*"` does not include unauthenticated requests

D. Yes — IAM policies only apply to authenticated requests from the same account; a public request bypasses IAM entirely

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. IAM policies apply to IAM principals (authenticated users, roles). Unauthenticated public requests do not have an IAM identity, so IAM deny policies cannot be applied to them. The S3 bucket policy is the only applicable policy for public requests.
- B is correct. When an unauthenticated (public) request is made, there is no IAM principal associated with it. AWS evaluates only the resource-based policy (bucket policy). The bucket policy allows `s3:GetObject` for `"Principal": "*"` (which includes unauthenticated requests). IAM identity-based deny policies do not apply to requests with no IAM identity. Note: for this to work, the bucket's Block Public Access settings must also be disabled.
- C is incorrect. `"Principal": "*"` in an S3 bucket policy does include unauthenticated (anonymous) requests in addition to authenticated ones.
- D is incorrect in its framing but points toward the correct concept. The reason public access works is because unauthenticated requests have no IAM principal, not because IAM is "bypassed."

---

### Question 4

A company needs to encrypt data stored in an S3 bucket. The security policy requires that they control who can use the encryption key, that all key usage is logged in CloudTrail, and that they can rotate the key material annually. Which KMS key type meets ALL these requirements?

A. AWS Owned Key

B. AWS Managed Key

C. Customer Managed Key (CMK)

D. S3-Managed Key (SSE-S3)

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. AWS Owned Keys are managed entirely by AWS. The customer has no visibility into key policies, key usage, or rotation schedules. CloudTrail does not log AWS Owned Key usage in the customer's account.
- B is incorrect. AWS Managed Keys are managed by AWS on behalf of the service. You cannot configure custom key policies (so you cannot control who uses the key), and you cannot configure rotation — AWS rotates them on a fixed 3-year schedule. Key usage is logged in CloudTrail but you cannot customize the key policy.
- C is correct. Customer Managed Keys allow you to: configure a custom key policy controlling which principals can use the key, view all key usage in CloudTrail (every Encrypt/Decrypt call), and enable annual key rotation. CMKs satisfy all three requirements.
- D is incorrect. SSE-S3 (AES-256) uses S3-managed keys. You have no control over the key, no custom key policy, and no CloudTrail visibility into individual key usage.

---

### Question 5

An analyst reports that a production EC2 instance has been making DNS requests to a known malware command-and-control domain. The security team needs to investigate whether the instance has been compromised. Which AWS service MOST LIKELY generated the finding that identified this activity?

A. AWS CloudTrail

B. Amazon Inspector

C. Amazon GuardDuty

D. AWS Config

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. CloudTrail records AWS API calls (management plane operations). It does not analyze DNS traffic or detect connections to C2 domains. CloudTrail would not generate this type of network-level finding.
- B is incorrect. Amazon Inspector scans EC2 instances and container images for software vulnerabilities (known CVEs) and unintended network exposure. It does not monitor runtime DNS traffic for C2 communication.
- C is correct. GuardDuty analyzes DNS logs (captured by the Route 53 Resolver DNS logs feature and VPC Flow Logs) and uses threat intelligence feeds to detect DNS lookups to known malicious domains. The specific finding `Backdoor:EC2/C&CActivity` or similar GuardDuty findings are generated for EC2 instances making DNS requests to known C2 infrastructure.
- D is incorrect. AWS Config tracks configuration changes to AWS resources (was this security group modified? was this S3 bucket made public?). It does not monitor DNS traffic or detect C2 communication.

---

### Question 6

A company wants a centralized dashboard that shows security findings from GuardDuty, Amazon Inspector, and Amazon Macie across all accounts in their AWS Organization. They also want the dashboard to score their overall security posture against the CIS AWS Foundations benchmark. Which service provides this?

A. Amazon GuardDuty (with multi-account delegation)

B. AWS Security Hub

C. AWS CloudTrail (with cross-account log aggregation)

D. Amazon CloudWatch (with a custom dashboard)

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. GuardDuty with multi-account delegation aggregates GuardDuty findings across accounts, but it does not consolidate findings from Inspector, Macie, or other services. It also does not evaluate compliance against security benchmarks like CIS AWS Foundations.
- B is correct. AWS Security Hub is specifically designed to aggregate security findings from GuardDuty, Inspector, Macie, IAM Access Analyzer, AWS Config, and third-party tools into a single view. It evaluates resources against security standards including CIS AWS Foundations, AWS FSBP, and PCI DSS, and generates a security score. Multi-account aggregation is supported via a delegated administrator account.
- C is incorrect. CloudTrail is an audit log service. It records API calls but does not aggregate security findings, evaluate compliance benchmarks, or provide a security posture score.
- D is incorrect. CloudWatch is a monitoring and observability service. You can build custom dashboards for operational metrics, but it has no native capability to aggregate security findings or evaluate against security frameworks.

---

### Question 7

A company's web application is experiencing HTTP request floods from multiple IP addresses that appear to be an automated attack. The requests are syntactically valid HTTP requests targeting the application's login endpoint at a rate of 10,000 requests per minute from a single IP. Which service provides the MOST direct protection?

A. AWS Shield Standard

B. Amazon GuardDuty

C. AWS WAF with a rate-based rule

D. Amazon Inspector

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Shield Standard protects against volumetric network and transport layer (Layer 3 and 4) DDoS attacks — SYN floods, UDP reflection, and similar attacks that target network bandwidth. An HTTP request flood using valid HTTP syntax is a Layer 7 application attack, which Shield Standard does not directly mitigate.
- B is incorrect. GuardDuty detects threats by analyzing logs. It would detect the attack in its findings, but it does not block traffic in real time. GuardDuty is a detection service, not a blocking service.
- C is correct. WAF operates at Layer 7 (application layer) and can be attached to an Application Load Balancer, CloudFront, or API Gateway. A rate-based rule in WAF counts requests from a single IP within a 5-minute window and blocks the IP when the count exceeds the configured threshold. This directly blocks the automated request flood.
- D is incorrect. Inspector scans for software vulnerabilities and network exposure. It does not inspect live HTTP traffic or block application-layer attacks.

---

### Question 8

A company wants to ensure that no member account in their AWS Organization can disable CloudTrail or GuardDuty, even if an account administrator has IAM AdministratorAccess. What is the CORRECT control to enforce this?

A. IAM Permission Boundaries attached to the AdministratorAccess role in each member account

B. A Service Control Policy attached to the organizational root that denies CloudTrail and GuardDuty disable actions

C. AWS Config rules that automatically re-enable CloudTrail if it is disabled

D. GuardDuty alerts that notify when CloudTrail is stopped

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Permission Boundaries limit the maximum permissions of an IAM entity. They must be applied to specific IAM users and roles and do not prevent root users from taking actions. They also must be manually maintained for each account. An SCP is a simpler, more comprehensive enforcement mechanism.
- B is correct. SCPs attached to the organizational root apply to all member accounts and all principals (except the management account). An SCP with explicit deny on `cloudtrail:StopLogging`, `cloudtrail:DeleteTrail`, `guardduty:DeleteDetector`, and `guardduty:DisassociateFromMasterAccount` prevents any principal in any member account from disabling these services, regardless of their IAM permissions.
- C is incorrect. AWS Config can detect and remediate misconfigurations automatically, but this is reactive — CloudTrail would be briefly disabled before Config detects and re-enables it. The SCP prevention is proactive — the disable action never succeeds.
- D is incorrect. GuardDuty alerts are detective, not preventive. You would be notified after CloudTrail was stopped, not prevented from stopping it.

---

### Question 9

A company stores customer financial records in an S3 bucket with Server-Side Encryption using a Customer Managed KMS Key (SSE-KMS). They need to ensure that even if a malicious AWS administrator in their account deletes the KMS key, the records cannot be permanently lost. Which KMS feature protects against accidental or malicious key deletion?

A. KMS key rotation, which creates a new key if the old one is deleted

B. KMS key deletion requires a minimum pending window (7–30 days) before permanent deletion

C. KMS key replication, which automatically copies the key to another region

D. KMS key versioning, which retains previous key material indefinitely

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Key rotation creates a new version of the key material for future encryptions — it does not prevent deletion or recover a deleted key. Rotation and deletion are independent operations.
- B is correct. KMS enforces a mandatory pending deletion window of 7 to 30 days. During this window, the key is disabled but not yet deleted, and you can cancel the deletion. This provides a safety net to recover from accidental or unauthorized deletion requests. The company should also monitor CloudTrail for `ScheduleKeyDeletion` API calls and configure a CloudWatch alarm to alert immediately.
- C is incorrect. KMS does not have an automatic cross-region key replication feature. Multi-Region KMS keys exist but require explicit configuration and are a separate feature from deletion protection.
- D is incorrect. KMS does not have a "key versioning" feature that retains key material versions independently after deletion. Key rotation retains old key material to decrypt previously encrypted data, but this is within the same key — deleting the key deletes all versions.

---

### Question 10

An architect is reviewing an IAM policy. The policy has two statements: Statement 1 with `"Effect": "Allow"` on `s3:*` for all S3 resources, and Statement 2 with `"Effect": "Deny"` on `s3:DeleteObject` for all S3 resources. What can a user with only this policy attached do?

A. The user can perform all S3 actions including DeleteObject because Allow was listed before Deny

B. The user can perform all S3 actions except DeleteObject because the explicit Deny overrides the Allow for that action

C. The user cannot perform any S3 actions because a Deny statement exists in the policy

D. The user can DeleteObject only if they explicitly request it; otherwise the Deny applies

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Statement order in an IAM policy JSON document does not affect evaluation. AWS evaluates all statements simultaneously, not sequentially. An explicit Deny in any statement overrides any Allow for the same action, regardless of order.
- B is correct. The Allow on `s3:*` permits all S3 actions. However, the explicit Deny on `s3:DeleteObject` overrides the Allow specifically for that action. The net effect is: all S3 actions allowed EXCEPT `s3:DeleteObject`, which is explicitly denied. This is how you implement "allow all except one specific action" in IAM.
- C is incorrect. A Deny in one statement does not block all actions — only the specific actions matched by the Deny statement's `Action` element. All other S3 actions remain allowed by the Allow statement.
- D is incorrect. IAM policy evaluation is not interactive — there is no concept of "explicitly requesting" an action to bypass a Deny. An explicit Deny in an IAM policy is unconditional within the policy scope.

---

### Question 11 (5 points)

A company uses AWS Organizations. The security team applies an SCP to a member account that denies `ec2:TerminateInstances`. An IAM administrator in that member account grants a developer an IAM policy with `Allow` on `ec2:*`. What can the developer do?

A. Terminate instances because the IAM Allow overrides the SCP Deny

B. Terminate instances only if they have MFA enabled

C. Terminate instances only after the SCP is detached from the account

D. Terminate instances because SCPs do not apply to IAM users, only to IAM roles

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. SCPs act as guardrails that set the maximum permissions available in an account. An explicit SCP Deny cannot be overridden by any IAM policy within the member account, regardless of whether the policy is Allow. The IAM Allow has no effect against the SCP Deny.
- B is incorrect. MFA conditions in IAM policies create conditional access requirements but do not override SCPs. The SCP operates at the account boundary, above IAM policy evaluation.
- C is correct. The SCP Deny on `ec2:TerminateInstances` restricts the entire member account. To allow the developer to terminate instances, the SCP must first be modified or detached from the account — only then can the IAM Allow take effect. This demonstrates the SCP-first evaluation order in AWS authorization.
- D is incorrect. SCPs apply to all IAM principals in a member account — both IAM users and IAM roles. The management account is exempt from SCPs, but member accounts are fully subject to them regardless of principal type.

---

### Question 12 (5 points)

An application running on an EC2 instance needs to write objects to an S3 bucket. A developer proposes storing the IAM access keys in the application's configuration file on the instance. What is the correct AWS-recommended approach?

A. Store the access keys in AWS Secrets Manager and retrieve them at application startup

B. Attach an IAM instance profile with a role that grants S3 write permissions to the EC2 instance

C. Encrypt the access keys using KMS before storing them in the configuration file

D. Store the access keys as EC2 user data so they are available at launch

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. While Secrets Manager is appropriate for rotating database credentials, using it to store IAM access keys for EC2-to-S3 access adds unnecessary complexity and cost when the native instance profile mechanism exists specifically for this purpose.
- B is correct. Attaching an IAM instance profile assigns a role to the EC2 instance, allowing the EC2 metadata service (IMDS) to provide temporary credentials automatically. Applications using the AWS SDK or CLI automatically retrieve these credentials without any stored keys. This is the AWS-recommended approach — no long-term credentials are stored anywhere.
- C is incorrect. Encrypting access keys does not eliminate the risk — the encryption key itself must be stored somewhere, creating a second secret management problem. The underlying issue is storing long-term credentials on the instance at all.
- D is incorrect. EC2 user data is stored unencrypted and is accessible to anyone who can view instance metadata or the EC2 console. Storing credentials in user data is a significant security risk and explicitly against AWS best practices.

---

### Question 13 (5 points)

A company wants to enforce that all new IAM users created in their AWS account must have MFA enabled before they can perform any action. What is the correct implementation?

A. Enable MFA on the root account and MFA enforcement automatically propagates to all IAM users

B. Attach a permission boundary to each new IAM user that denies all actions unless MFA is present

C. Attach an IAM policy to all IAM users or a group that denies all actions except MFA-related actions when `aws:MultiFactorAuthPresent` is false

D. Configure an SCP in AWS Organizations that denies all actions unless MFA is present

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Root account MFA has no effect on IAM user MFA requirements. Root MFA protects only the root user session. IAM users have entirely separate authentication flows.
- B is incorrect. Permission boundaries define the maximum permissions a principal can have — they do not enforce conditions like MFA presence. Permission boundaries are used for delegation scenarios, not for MFA enforcement.
- C is correct. Attaching a policy with a Deny on all actions conditioned on `Condition: {"BoolIfExists": {"aws:MultiFactorAuthPresent": "false"}}` forces users to authenticate with MFA before performing any action. The policy must explicitly allow MFA self-service actions (like `iam:CreateVirtualMFADevice`) so users can enroll their own MFA devices.
- D is incorrect. SCPs can enforce MFA requirements but only when the account is in AWS Organizations. For a standalone account or when the requirement is specifically about IAM user policy enforcement, the IAM policy approach is the direct implementation.

---

### Question 14 (5 points)

A security team discovers that an S3 bucket has a bucket policy allowing public read access to all objects. The account also has an IAM policy attached to an IAM role that allows `s3:GetObject` only on a specific prefix. An external unauthenticated user attempts to read an object outside that prefix. What happens?

A. The request is denied because the IAM policy limits access to the specific prefix

B. The request is allowed because the bucket policy allows public access and no IAM policy applies to unauthenticated users

C. The request is allowed only if the account's S3 Block Public Access settings are disabled

D. The request is denied because resource-based policies require identity-based policies to also allow access for unauthenticated users

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. IAM identity-based policies do not apply to unauthenticated (anonymous) requests. The IAM role policy is irrelevant for a request with no identity — the evaluation applies only to the bucket policy for anonymous access.
- B is partially correct in logic but ignores the overriding control. A bucket policy allowing public access would grant access to anonymous users — unless account-level S3 Block Public Access settings override the bucket policy and block it.
- C is correct. Even if a bucket policy explicitly allows public access, the account-level S3 Block Public Access setting `BlockPublicPolicy` prevents the bucket policy from taking effect. If Block Public Access is enabled at the account level, the bucket policy's public Allow is ignored regardless of what the policy says.
- D is incorrect. Resource-based policies (like bucket policies) can independently grant access to anonymous users without any identity-based policy involvement. This is how public S3 websites work — no IAM identity required.

---

### Question 15 (5 points)

An organization uses AWS IAM Identity Center (formerly SSO) to manage access across 15 AWS accounts. A developer needs read-only access to EC2 in three specific accounts. What is the correct way to configure this?

A. Create an IAM user in each of the three accounts and attach the AmazonEC2ReadOnlyAccess managed policy

B. Create a Permission Set in IAM Identity Center with the AmazonEC2ReadOnlyAccess policy and assign it to the developer for each of the three accounts

C. Create cross-account IAM roles in each account and provide the developer with role ARNs to assume manually

D. Add the developer to an IAM group in the management account with cross-account access to all 15 accounts

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Creating separate IAM users in each account requires managing multiple sets of credentials, violating the principle of centralized identity management. This approach scales poorly and creates credential management burden.
- B is correct. IAM Identity Center Permission Sets are reusable policy containers assigned to users or groups for specific accounts. The developer authenticates once through the Identity Center portal and receives temporary credentials for each assigned account. This is the recommended multi-account access pattern.
- C is incorrect. Manual role assumption requires distributing role ARNs, is error-prone, and lacks the centralized visibility and session management that Identity Center provides. This is an older pattern that IAM Identity Center supersedes.
- D is incorrect. IAM groups exist within a single account — they cannot span multiple accounts. IAM itself has no native multi-account group construct; that is what IAM Identity Center provides.

---

### Question 16 (5 points)

A company needs to encrypt data at rest in an S3 bucket. The security team requires that they can rotate the encryption key annually, audit every decryption event, and revoke access to the key if a security incident occurs. Which encryption approach meets all three requirements?

A. SSE-S3 (Server-Side Encryption with Amazon S3-managed keys)

B. SSE-KMS with a Customer Managed Key (CMK)

C. SSE-KMS with an AWS Managed Key

D. Client-side encryption using the AWS Encryption SDK with a locally generated key

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. SSE-S3 uses S3-managed keys — the customer has no control over key rotation schedule and no ability to audit individual decryption events through KMS CloudTrail logs. Key revocation is also not possible.
- B is correct. A Customer Managed Key (CMK) gives the security team full control: they can configure automatic annual rotation, every API call using the key generates a CloudTrail entry (Decrypt, GenerateDataKey), and they can disable or schedule deletion of the key to revoke access immediately during a security incident.
- C is incorrect. AWS Managed Keys are rotated automatically by AWS every year, satisfying rotation, and do log to CloudTrail. However, the customer cannot manually rotate them on-demand, cannot disable them, and cannot delete them — failing the "revoke access" requirement.
- D is incorrect. Client-side encryption with locally managed keys would satisfy the security requirements but adds significant operational complexity: the application must manage keys, and if the key is lost locally, data is permanently unrecoverable. It is also outside AWS-managed services.

---

### Question 17 (5 points)

AWS GuardDuty generates a finding of type `UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B`. The finding indicates a successful console login from an IP address in a country where the organization has no employees. What is the MOST appropriate immediate response?

A. Disable GuardDuty temporarily and re-enable it after investigating

B. Revoke all active IAM sessions for the affected user and rotate their credentials immediately

C. Delete the IAM user immediately and create a new user with the same permissions

D. Change the IAM user's password and wait 24 hours to see if additional GuardDuty findings appear

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Disabling GuardDuty removes detection capability at exactly the moment it is most needed. GuardDuty should remain active and findings should be investigated with it running.
- B is correct. The immediate response to suspected account compromise is to contain the threat: revoke all active sessions using `aws iam delete-login-profile` (if console), `aws iam update-access-key` to deactivate programmatic keys, and use `aws iam create-login-profile` to reset with a new credential. Containing first prevents ongoing damage while investigation proceeds.
- C is incorrect. Deleting the IAM user and creating a new one may erase forensic evidence (access key metadata, last used timestamps) and disrupts legitimate workflows. Containment through session revocation is preferred over destruction.
- D is incorrect. Waiting 24 hours allows the attacker to continue operating in the environment. Security incidents require immediate containment, not a monitoring window.

---

### Question 18 (5 points)

A web application is experiencing HTTP flood attacks where bots are sending thousands of requests per second to a specific API endpoint. The attacks originate from hundreds of different IP addresses, making IP blocking ineffective. Which AWS service best addresses this threat?

A. AWS Shield Standard (automatically enabled)

B. AWS Network Firewall with a stateful rule blocking high-rate connections

C. AWS WAF with a rate-based rule configured on the specific API endpoint

D. Amazon GuardDuty with automated remediation via EventBridge and Lambda

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. AWS Shield Standard protects against network-layer (Layer 3/4) DDoS attacks such as SYN floods and UDP reflection. HTTP flood attacks are application-layer (Layer 7) attacks that Shield Standard does not mitigate.
- B is incorrect. AWS Network Firewall operates at the network layer and can inspect Layer 7 content through protocol detection, but it is not purpose-built for per-URI rate limiting or HTTP-specific rule logic. It also requires deployment in a VPC and adds architectural complexity.
- C is correct. AWS WAF rate-based rules count requests per IP address (or other aggregation keys) within a rolling 5-minute window. When the threshold is crossed, WAF automatically blocks further requests from that IP. This directly addresses HTTP floods even when spread across many IPs by setting a per-IP rate limit on the target endpoint.
- D is incorrect. GuardDuty detects threats from CloudTrail, VPC Flow Logs, and DNS logs — it does not inspect HTTP request rates at the application layer. It is a detection service, not a traffic rate-limiting tool.

---

### Question 19 (5 points)

A company wants to centralize security findings from GuardDuty, AWS Config, Inspector, and IAM Access Analyzer across all accounts in their AWS Organization into a single view. Which service provides this aggregation?

A. Amazon CloudWatch

B. AWS CloudTrail Lake

C. AWS Security Hub

D. AWS Trusted Advisor

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. CloudWatch collects metrics and logs for operational monitoring. While it can trigger alarms and display dashboards, it does not aggregate security findings from GuardDuty, Config, or Inspector in a normalized finding format.
- B is incorrect. CloudTrail Lake aggregates and queries API audit logs across accounts, but it does not aggregate security findings from GuardDuty, Config Rules compliance results, or Inspector vulnerability findings.
- C is correct. AWS Security Hub is specifically designed to aggregate, normalize, and prioritize security findings from multiple AWS services (GuardDuty, Config, Inspector, IAM Access Analyzer, Macie, and third-party tools) across all accounts in an Organization. It evaluates findings against security standards such as CIS AWS Foundations and AWS Foundational Security Best Practices.
- D is incorrect. Trusted Advisor provides cost optimization, performance, security, and fault tolerance recommendations, but it does not aggregate findings from GuardDuty, Inspector, or Config in a unified security posture view.

---

### Question 20 (5 points)

A company is using AWS KMS with automatic key rotation enabled on a Customer Managed Key. An S3 object was encrypted with the CMK two years ago. After three years of annual rotation, an application attempts to decrypt the object. What happens?

A. The decryption fails because the key material used to encrypt the object has been rotated away

B. The decryption succeeds because KMS retains all previous key material versions and automatically selects the correct version to decrypt

C. The decryption fails unless the application specifies the original key version ARN

D. The decryption succeeds only if the application re-encrypts the object with the new key material first

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. KMS key rotation does not delete old key material. Old versions are retained indefinitely within the same CMK. The CMK logical ID (key ARN) remains unchanged — only new data is encrypted with the new key material going forward.
- B is correct. When KMS automatic rotation occurs, the new key material is used for all new encryption operations. However, KMS retains all previous key material versions under the same key ARN. When a Decrypt request is made for data encrypted with older key material, KMS identifies the correct version from the ciphertext metadata and uses that version to decrypt transparently. No application changes are required.
- C is incorrect. Applications do not specify key material versions in KMS API calls — this is handled transparently by the KMS service. There is no version ARN syntax for KMS key material versions.
- D is incorrect. Re-encryption (using `aws kms re-encrypt`) is optionally recommended to migrate ciphertext to new key material for performance or security reasons, but it is not required for decryption. Existing ciphertext remains decryptable with the retained old key material indefinitely.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
