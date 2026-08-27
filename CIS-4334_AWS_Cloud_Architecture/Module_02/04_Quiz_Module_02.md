# Quiz: Module 02 - IAM: Users, Roles, Policies, and Best Practices

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Questions:** 10

---

## Question 1

A company is deploying a web application on Amazon EC2 that needs to read objects from an S3 bucket. A developer proposes creating an IAM user and embedding the access keys in the application's configuration file on the instance. What is the most significant security risk with this approach, and what is the correct alternative?

- A) IAM user access keys cannot be used with S3; only IAM roles can access S3
- B) The access keys stored in the configuration file could be exposed if the instance is compromised or if the file is committed to source control; an IAM instance role should be used instead
- C) Access keys embedded in configuration files are rotated automatically by AWS, but this creates excessive API calls
- D) IAM users do not support S3 permissions; you must use a resource-based bucket policy instead

### Answer 1

Correct Answer: B

### Explanation 1

- A is incorrect: IAM user access keys can technically be used with S3, but using them for application access is an anti-pattern.
- B is correct: Static credentials in configuration files are a major security risk — they can be extracted from a compromised instance, accidentally committed to source control, or exposed in logs. An IAM instance role provides temporary credentials automatically via the instance metadata service with no static keys to manage or expose.
- C is incorrect: Access keys embedded in configuration files are never automatically rotated by AWS. They remain static until manually rotated.
- D is incorrect: IAM users can have S3 permissions. The issue is not capability but security practice.

---

## Question 2

A solutions architect needs to allow an IAM role in Account A (ID: 111122223333) to access an S3 bucket in Account B (ID: 444455556666). Which combination of policies is required to enable this cross-account access via role assumption?

- A) A resource-based bucket policy in Account B granting access to Account A's root, and an SCP in Account A allowing sts:AssumeRole
- B) A trust policy on a role in Account B allowing Account A's role to assume it, and an identity-based policy on Account A's role allowing sts:AssumeRole for the Account B role ARN
- C) An IAM group in Account B containing the Account A role as a member, with S3 permissions attached to the group
- D) An AWS Direct Connect connection between Account A and Account B to enable cross-account S3 access

### Answer 2

Correct Answer: B

### Explanation 2

- A is incorrect: While a resource-based bucket policy can grant cross-account access directly (without role assumption), this scenario involves role assumption. SCPs do not enable cross-account access — they restrict permissions.
- B is correct: Cross-account role assumption requires two policies: a trust policy on the role in the trusting account (Account B) listing the principal from the trusted account (Account A), and an identity-based policy on the principal in Account A allowing sts:AssumeRole for the Account B role ARN.
- C is incorrect: IAM groups cannot contain roles and cannot span accounts. Groups are for organizing IAM users within a single account.
- D is incorrect: AWS Direct Connect is a network connectivity service for connecting on-premises infrastructure to AWS. It does not grant IAM permissions for cross-account S3 access.

---

## Question 3

An IAM policy attached to a developer's user account includes an Allow statement for `s3:DeleteBucket` on all resources. A Service Control Policy applied to the organizational unit containing the developer's account includes a Deny statement for `s3:DeleteBucket`. What is the result when the developer attempts to delete an S3 bucket?

- A) The request is allowed because identity-based policies take precedence over SCPs
- B) The request is denied because explicit Deny in an SCP always overrides any Allow
- C) The request is allowed because the developer's policy is evaluated before the SCP
- D) The result depends on whether the bucket has a resource-based policy that allows or denies the action

### Answer 3

Correct Answer: B

### Explanation 3

- A is incorrect: SCPs are not overridden by identity-based policies. SCPs set the maximum permissions boundary for all identities in the account.
- B is correct: In IAM policy evaluation, an explicit Deny in any applicable policy — including an SCP at any Organizations level — always overrides any Allow. The developer cannot delete the bucket regardless of what their identity policy says.
- C is incorrect: Evaluation order does not determine precedence. A Deny at any level in the evaluation chain stops the request regardless of when it is evaluated.
- D is incorrect: Resource-based policies can affect same-account or cross-account access decisions, but they cannot override an explicit Deny from an SCP.

---

## Question 4

Which IAM policy type would a central security team use to ensure that no IAM principal in a specific AWS account can create IAM users, even if that account's administrator tries to grant that permission?

- A) A permission boundary attached to all IAM roles in the account
- B) A customer managed policy with a Deny statement for iam:CreateUser attached to all users
- C) A Service Control Policy with a Deny statement for iam:CreateUser applied to the account or its parent OU
- D) An inline policy with a Deny statement for iam:CreateUser attached to the account's root user

### Answer 4

Correct Answer: C

### Explanation 4

- A is incorrect: Permission boundaries apply to individual IAM entities, not account-wide. A new IAM role created without the boundary attached would not be restricted. Additionally, permission boundaries cannot be enforced without being explicitly attached to each entity.
- B is incorrect: A customer managed policy must be attached to every identity in the account to be effective. A new user or role created after the policy assignment would not have it attached, leaving a gap.
- C is correct: An SCP applied to an account or OU affects all IAM principals in that scope including the account's own administrators. Even if an administrator grants iam:CreateUser to a role, the SCP Deny overrides it universally.
- D is incorrect: The root user cannot have IAM policies attached to it. The root user's access cannot be restricted by IAM policies, only by MFA requirements and account-level controls. SCPs do restrict the root user within member accounts in an organization.

---

## Question 5

A Lambda function needs to write items to a DynamoDB table and publish messages to an SNS topic. What is the correct way to grant these permissions?

- A) Create an IAM user for the Lambda function, generate access keys, and pass them as environment variables in the Lambda function configuration
- B) Create an IAM role with an execution role trust policy for Lambda, attach a policy granting dynamodb:PutItem and sns:Publish, and assign the role to the Lambda function
- C) Add the Lambda function's ARN to the DynamoDB table's resource-based policy and the SNS topic's resource-based policy
- D) Enable the Lambda function's VPC configuration so it can access DynamoDB and SNS within the private network

### Answer 5

Correct Answer: B

### Explanation 5

- A is incorrect: Creating an IAM user for an AWS service is an anti-pattern. Environment variables in Lambda are not encrypted by default and could be exposed. Lambda functions must use execution roles for AWS service access.
- B is correct: Lambda functions use an IAM execution role. The role has a trust policy allowing Lambda to assume it. The permissions policy grants only the specific actions needed (dynamodb:PutItem and sns:Publish) on the specific resource ARNs. Lambda's SDK retrieves temporary credentials from STS automatically.
- C is incorrect: While resource-based policies on DynamoDB and SNS can grant access, DynamoDB does not support resource-based policies. This approach also does not follow the standard Lambda execution role pattern.
- D is incorrect: VPC configuration controls which VPC subnets and security groups the Lambda function runs in. It enables network access to private resources but does not grant IAM permissions to call AWS service APIs.

---

## Question 6

An auditor reviewing an IAM policy finds the following statement. What security risk does this statement introduce?

```json
{
  "Effect": "Allow",
  "Action": "s3:*",
  "Resource": "*"
}
```

- A) The statement does not include a Version field, so it will be ignored by AWS
- B) The statement grants full S3 access to all S3 buckets and objects in the account, including the ability to delete buckets, modify bucket policies, and disable encryption
- C) The statement will only allow read actions because write actions require an explicit second statement
- D) The wildcard in Resource applies only to the account's own buckets and cannot access other accounts' buckets

### Answer 6

Correct Answer: B

### Explanation 6

- A is incorrect: The Version field is at the policy document level, not the statement level. A missing Version in the statement does not cause the statement to be ignored. The policy document must have the Version field.
- B is correct: `s3:*` grants every S3 API action, including s3:DeleteBucket, s3:PutBucketPolicy, s3:PutBucketAcl, s3:DeleteObject, and s3:PutEncryptionConfiguration. Combined with `Resource: "*"`, this applies to all S3 buckets and objects in the account. This is a critical over-permission.
- C is incorrect: IAM does not split action categories automatically. `s3:*` is a wildcard that matches every S3 action including all write and destructive operations.
- D is incorrect: IAM policies by default apply within the account. However, this policy grants full S3 API access and could be combined with a bucket policy or cross-account role to grant access to other accounts' buckets. The risk within the account is itself severe.

---

## Question 7

A company wants to allow its employees to sign in to the AWS Management Console using their existing corporate Active Directory credentials without creating individual IAM users for each employee. Which AWS feature enables this?

- A) IAM groups with an Active Directory membership sync configured through IAM
- B) AWS Single Sign-On (IAM Identity Center) with a SAML 2.0 federation to the corporate Active Directory via ADFS
- C) Amazon Cognito user pools with an Active Directory synchronization plugin
- D) AWS Directory Service for Microsoft Active Directory with IAM user provisioning

### Answer 7

Correct Answer: B

### Explanation 7

- A is incorrect: IAM groups do not support federation or Active Directory synchronization. IAM groups are for organizing IAM users within an account only.
- B is correct: IAM Identity Center (formerly AWS SSO) integrates with external identity providers including Microsoft Active Directory via ADFS using SAML 2.0. Employees authenticate with their AD credentials and receive temporary AWS access. No IAM user creation per employee is needed.
- C is incorrect: Amazon Cognito is designed for web and mobile application user authentication, not for AWS Management Console federated access.
- D is incorrect: AWS Directory Service for Microsoft Active Directory extends AD into AWS and is often used in conjunction with identity federation, but it does not directly provision IAM users or enable console login by itself.

---

## Question 8

What is the purpose of an IAM permission boundary?

- A) To define the maximum permissions that AWS services can grant to other services on your behalf
- B) To set the maximum permissions an IAM user or role can have, such that the effective permissions are the intersection of the identity policy and the permission boundary
- C) To prevent root account users from performing destructive operations in production accounts
- D) To restrict which AWS Regions IAM identities can operate in

### Answer 8

Correct Answer: B

### Explanation 8

- A is incorrect: This describes service roles and service-linked roles, not permission boundaries.
- B is correct: A permission boundary is an advanced feature that sets a ceiling on what an IAM entity can do. If an identity policy grants s3:DeleteBucket but the permission boundary does not include s3:DeleteBucket, the action is denied. Effective permissions = intersection of identity policy AND permission boundary.
- C is incorrect: Permission boundaries are attached to IAM users and roles, not to root account users. Root users cannot have permission boundaries attached.
- D is incorrect: Region restriction is implemented through condition keys (aws:RequestedRegion) in SCP or IAM policies, not through permission boundaries as a distinct feature.

---

## Question 9

A security engineer discovers that an EC2 instance was recently compromised. During forensic analysis, they find that the attacker extracted temporary credentials from the EC2 instance metadata service and used them to call S3 and DynamoDB APIs. Which mitigation would have best reduced the impact of this attack?

- A) Encrypting the EC2 instance's EBS volumes with AWS KMS to prevent credential extraction
- B) Enabling IMDSv2 on the instance to require session-oriented metadata requests, reducing SSRF-based credential theft
- C) Disabling the IAM role attached to the instance and relying on embedded access keys in the application code instead
- D) Moving the instance to a private subnet with no internet gateway to block outbound API calls

### Answer 9

Correct Answer: B

### Explanation 9

- A is incorrect: EBS encryption protects data at rest on disk. It does not prevent credential extraction from the instance metadata service endpoint, which is accessible from within the running instance.
- B is correct: IMDSv2 requires applications to first make a PUT request to obtain a session token before reading metadata. This breaks common SSRF-based exploits that use simple GET requests to read metadata, making credential theft significantly harder. IMDSv2 enforcement is a recommended hardening step for all EC2 instances.
- C is incorrect: Switching to embedded access keys in code introduces static credential risks that are worse than the temporary credential risk from instance metadata. Static keys do not expire and can be extracted even more easily.
- D is incorrect: Moving to a private subnet restricts internet access but does not prevent use of the extracted credentials. AWS API calls from within a VPC can use VPC endpoints or NAT gateway, and the attacker who extracted the credentials could make API calls from outside the VPC using them.

---

## Question 10

An IAM identity-based policy attached to a role includes `"Effect": "Allow"` for `s3:PutObject` on a specific bucket. A bucket policy on the same S3 bucket includes `"Effect": "Deny"` for `s3:PutObject` for all principals. What is the result when the role attempts to put an object in the bucket?

- A) The request is allowed because identity-based policies take precedence over resource-based policies
- B) The request is denied because the explicit Deny in the bucket policy overrides the Allow in the identity policy
- C) The result depends on which policy was created first; newer policies take precedence
- D) The request is allowed because the role's identity policy is evaluated before the bucket policy and the Allow is found first

### Answer 10

Correct Answer: B

### Explanation 10

- A is incorrect: Identity-based policies do not take precedence over resource-based policies. Both types of policies are evaluated together and an explicit Deny in either one takes effect.
- B is correct: An explicit Deny in any applicable policy — whether identity-based, resource-based, SCP, or permission boundary — always overrides any Allow. The bucket policy's Deny for all principals applies to the role and blocks the PutObject operation.
- C is incorrect: Policy evaluation is not based on creation order. All applicable policies are evaluated simultaneously and the explicit Deny rule applies regardless of when policies were created.
- D is incorrect: IAM does not evaluate policies in sequence and stop at the first Allow. All policies are evaluated and a Deny anywhere in the result set causes denial.

---

## Question 11

A company is using AWS Organizations and wants to prevent any IAM principal in their production account from disabling AWS CloudTrail logging, even account administrators. Which approach achieves this with the least operational overhead?

- A) Attach a permission boundary to every IAM role in the production account that excludes cloudtrail:StopLogging
- B) Apply a Service Control Policy to the production account's OU that denies cloudtrail:StopLogging and cloudtrail:DeleteTrail for all principals
- C) Create a customer managed IAM policy with a Deny for cloudtrail:StopLogging and attach it to every user and role in the account
- D) Enable AWS Config with a remediation rule that re-enables CloudTrail within 5 minutes of it being disabled

### Answer 11

Correct Answer: B

### Explanation 11

- A is incorrect: Permission boundaries must be attached to each individual IAM entity. New roles created later without the boundary would not be restricted. This approach also does not affect the account root user.
- B is correct: An SCP applied to the production OU denies the specified CloudTrail actions for ALL IAM principals in the account, including administrators and the account root user (within AWS Organizations member accounts). This is the lowest-overhead, most comprehensive control — set once at the org level and it applies universally.
- C is incorrect: A customer managed policy must be manually attached to every user and role. New identities created later would not have it attached, and the account administrator could simply detach it from their own role.
- D is incorrect: AWS Config with remediation is a detective and reactive control, not preventive. There is a window between when CloudTrail is disabled and when remediation fires during which audit logging is lost. This does not prevent the action from occurring.

---

## Question 12

An application running on Amazon EC2 uses the AWS SDK to call the S3 API. The developer wants to understand how the SDK obtains the AWS credentials it uses to sign API requests. Which credential source does the SDK use by default when running on an EC2 instance with an attached IAM instance profile?

- A) It reads the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables that must be set by the developer
- B) It retrieves temporary credentials from the EC2 Instance Metadata Service (IMDS) endpoint automatically, refreshing them before expiry
- C) It generates a new set of long-term credentials each time the SDK is initialized using the IAM API
- D) It reads credentials from the ~/.aws/credentials file that was created when the developer ran aws configure

### Answer 12

Correct Answer: B

### Explanation 12

- A is incorrect: Environment variable credentials are a valid SDK credential source, but when an instance profile is attached, the SDK's default credential provider chain finds the IMDS credentials before checking environment variables in most implementations. More importantly, relying on environment variables for application credentials running on EC2 is an anti-pattern.
- B is correct: The AWS SDK credential provider chain checks for instance profile credentials via the EC2 IMDS endpoint (169.254.169.254) automatically. When an IAM instance profile is attached to the EC2 instance, the SDK retrieves temporary STS credentials from IMDS without any developer configuration. The SDK also handles automatic credential refresh before expiry.
- C is incorrect: The SDK never generates new long-term credentials. Long-term credentials are created manually by an IAM administrator. The SDK only retrieves credentials that already exist.
- D is incorrect: The ~/.aws/credentials file is populated by aws configure for human users. On an EC2 instance with an instance profile, the SDK will find IMDS credentials higher in the credential provider chain before it reads the credentials file.

---

## Question 13

A security engineer needs to write an IAM policy that allows users to start and stop only EC2 instances that are tagged with `Environment: production` in the same AWS account. Which policy element correctly implements the tag-based condition?

- A) `"Condition": {"StringEquals": {"aws:ResourceTag/Environment": "production"}}`
- B) `"Condition": {"StringEquals": {"ec2:InstanceType": "production"}}`
- C) `"Condition": {"StringEquals": {"aws:RequestTag/Environment": "production"}}`
- D) `"Condition": {"ArnLike": {"aws:ResourceArn": "arn:aws:ec2:*:*:instance/production-*"}}`

### Answer 13

Correct Answer: A

### Explanation 13

- A is correct: `aws:ResourceTag/TagKey` is the condition key used to match tags that already exist on the resource being acted upon. For controlling access to EC2 instances based on their existing tags, `aws:ResourceTag/Environment` with value `production` is the correct condition.
- B is incorrect: `ec2:InstanceType` is a condition key for the instance type (e.g., t3.micro, m5.xlarge). It is not related to tags and `production` is not a valid instance type.
- C is incorrect: `aws:RequestTag/TagKey` applies to tags that are being set in a CreateResource or TagResource API call (the tags being applied in the request). It is not used to control access based on existing resource tags. This is the correct key for `ec2:CreateTags` or `ec2:RunInstances` tag-enforcement policies.
- D is incorrect: `aws:ResourceArn` is not a standard IAM condition key used for tag-based access control. ARN-based conditions use `ArnLike` with `aws:SourceArn`, not with resource ARNs in this context.

---

## Question 14

An IAM role named `DataProcessorRole` has a policy allowing `s3:GetObject` on `arn:aws:s3:::reports-bucket/*`. A permission boundary attached to the role allows `s3:*` on all resources. What S3 actions can the role effectively perform on the reports bucket?

- A) All S3 actions because the permission boundary allows s3:*
- B) Only s3:GetObject because the effective permissions are the intersection of the identity policy and the permission boundary
- C) No S3 actions because permission boundaries deny all actions not explicitly listed in the identity policy
- D) All S3 actions except s3:DeleteObject because deletion is blocked by permission boundaries by default

### Answer 14

Correct Answer: B

### Explanation 14

- A is incorrect: A permission boundary does not grant permissions on its own. The permission boundary allows `s3:*`, but the identity policy only allows `s3:GetObject`. The effective permissions are the intersection, so only `s3:GetObject` is allowed.
- B is correct: Effective permissions equal the intersection of the identity policy AND the permission boundary. The identity policy allows only `s3:GetObject`. Even though the permission boundary allows `s3:*`, the identity policy does not grant any other actions. Therefore, only `s3:GetObject` is effective.
- C is incorrect: Permission boundaries do not deny actions from the identity policy. They restrict the ceiling. If the identity policy allows `s3:GetObject` and the boundary also includes `s3:GetObject` in its allow set (which `s3:*` does), the action is permitted.
- D is incorrect: There is no default block on `s3:DeleteObject` from permission boundaries. The restriction comes from the identity policy's scope, not from any default permission boundary behavior.

---

## Question 15

A company uses AWS IAM Identity Center (SSO) to grant employees access to multiple AWS accounts. A developer in the company attempts to access the AWS Management Console but receives an "Access Denied" error on the IAM Identity Center portal. Which is the most likely cause?

- A) The developer's IAM user in the target account does not have the AdministratorAccess policy attached
- B) The developer has not been assigned to a permission set in IAM Identity Center that grants access to the target account
- C) The developer's MFA device is not registered with IAM Identity Center
- D) The target AWS account has not been linked to the company's Active Directory domain

### Answer 15

Correct Answer: B

### Explanation 15

- A is incorrect: IAM Identity Center federation does not use IAM users with direct policy attachments. SSO creates temporary role sessions, not IAM user sessions. The developer does not need an IAM user in the target account.
- B is correct: In IAM Identity Center, access to an AWS account is granted by assigning a user (or group) to a permission set for that account. If the developer has not been assigned to any permission set for the target account, they will not see that account in the portal and will receive an access denied error if they try to access it directly.
- C is incorrect: MFA can be configured as a requirement in IAM Identity Center, but if MFA were the issue, the user would receive an MFA challenge prompt rather than an immediate access denied. Unregistered MFA would block authentication entirely, not just access to a specific account.
- D is incorrect: AWS accounts in IAM Identity Center do not need to be linked to Active Directory at the account level. The identity source (Active Directory) is configured centrally at the IAM Identity Center level, not per-account.

---

## Question 16

A security audit finds that an S3 bucket storing sensitive customer data has the following bucket policy. What is the security risk introduced by this policy?

```json
{
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::customer-data-bucket/*"
}
```

- A) The policy uses a wildcard resource, which allows GetObject on all S3 buckets in the account
- B) The Principal set to wildcard (`*`) allows any unauthenticated or authenticated user on the internet to read all objects in the bucket, making it publicly accessible
- C) The policy missing a Condition block means it will be evaluated as a Deny by default
- D) The policy applies only to IAM users in the same AWS account and poses no external risk

### Answer 16

Correct Answer: B

### Explanation 16

- A is incorrect: The `Resource` ARN `arn:aws:s3:::customer-data-bucket/*` scopes the policy to objects in the specific `customer-data-bucket`. It is not a global wildcard across all S3 buckets.
- B is correct: `"Principal": "*"` in an S3 bucket policy grants access to any principal — any AWS account, any IAM user, any unauthenticated (anonymous) internet user. Combined with `s3:GetObject`, this makes every object in the bucket publicly readable. This is a critical misconfiguration that exposes sensitive customer data to the open internet.
- C is incorrect: A missing Condition block does not cause a Deny. IAM policy evaluation defaults to implicit Deny only if no applicable Allow statement exists. An Allow with no conditions applies unconditionally.
- D is incorrect: `"Principal": "*"` explicitly includes entities outside the AWS account, including unauthenticated users. It is not scoped to the same account.

---

## Question 17

A DevOps team wants to allow developers to create IAM roles for their own applications, but only if those roles have a specific permission boundary attached that limits what the created roles can do. Which IAM feature enables this delegation pattern?

- A) Service Control Policies applied to the developer OU
- B) A policy on the developers that allows iam:CreateRole only when the iam:PermissionsBoundary condition key matches the approved boundary ARN
- C) AWS Config rules that detect newly created roles without the required boundary and send an SNS alert
- D) A resource-based policy on the IAM service restricting role creation to approved principals

### Answer 17

Correct Answer: B

### Explanation 17

- A is incorrect: SCPs restrict what actions can be performed in an account, but they do not enforce that a specific permission boundary is attached when creating roles. They can deny role creation entirely but not conditionally allow it with boundary enforcement.
- B is correct: An IAM policy on the developer role can allow `iam:CreateRole` with a condition: `"Condition": {"StringEquals": {"iam:PermissionsBoundary": "arn:aws:iam::ACCOUNT:policy/DevRoleBoundary"}}`. This forces any role created by the developer to have the specified permission boundary — any attempt to create a role without it is denied. This is the AWS-recommended "permission boundary delegation" pattern.
- C is incorrect: An AWS Config alert is a detective control that fires after the role is already created. It does not prevent the creation of over-privileged roles and requires a separate remediation process.
- D is incorrect: IAM is not a resource-based policy service. You cannot attach resource-based policies to the IAM service itself to restrict API calls the way you can with S3 bucket policies.

---

## Question 18

An IAM policy evaluation results in an implicit deny. What does this mean?

- A) An explicit Deny statement in one of the applicable policies matched the requested action
- B) No applicable policy contained an Allow statement for the requested action and resource combination, so access is denied by default
- C) The requesting principal exceeded their API rate limit and the request was automatically denied
- D) The requested action is not supported by IAM and was denied by the IAM service itself

### Answer 18

Correct Answer: B

### Explanation 18

- A is incorrect: This describes an explicit deny, not an implicit deny. An explicit deny occurs when a Deny statement in an applicable policy directly matches the action and resource.
- B is correct: AWS IAM uses a default-deny model. If no applicable policy (identity policy, resource policy, SCP, permission boundary) contains an Allow statement for the specific action and resource, access is implicitly denied. The request is rejected not because anything said "no," but because nothing said "yes."
- C is incorrect: API rate limiting results in throttling errors (HTTP 429 / ThrottlingException), not IAM authorization denials. Throttling is a service-level control, not an IAM evaluation outcome.
- D is incorrect: IAM evaluates whether the principal is authorized to perform the action. If the service action is valid but no Allow exists, the result is implicit deny — not a rejection of the action's validity.

---

## Question 19

A company uses AWS CloudTrail to log all IAM API activity. A security engineer wants to be alerted immediately when any IAM policy is created or modified. Which combination of services accomplishes this with the least custom code?

- A) Enable AWS Config with a managed rule for IAM policy changes and set up an SNS notification
- B) Create a CloudWatch Metric Filter on the CloudTrail log group matching IAM policy change events, then create a CloudWatch Alarm with an SNS action
- C) Poll the CloudTrail API every 5 minutes with a Lambda function and compare results to the previous snapshot
- D) Enable AWS Security Hub and subscribe to the IAM findings category

### Answer 19

Correct Answer: B

### Explanation 19

- A is incorrect: AWS Config managed rules evaluate resource configuration compliance but are not designed to trigger real-time alerts on API calls like policy creation. Config evaluates on configuration change and may have delays.
- B is correct: CloudTrail logs all IAM API calls to CloudWatch Logs. A CloudWatch Metric Filter matching `eventSource = iam.amazonaws.com` and specific `eventNames` (CreatePolicy, PutUserPolicy, AttachRolePolicy, etc.) creates a custom metric. A CloudWatch Alarm fires when the metric count exceeds zero, triggering an SNS notification to the security team in near-real-time with no custom code beyond the metric filter pattern.
- C is incorrect: Polling the CloudTrail API every 5 minutes adds custom Lambda code, introduces up to a 5-minute alert delay, and requires storing and comparing state between invocations. This is high operational overhead compared to option B.
- D is incorrect: AWS Security Hub aggregates findings from integrated services (GuardDuty, Inspector, Macie, etc.) but does not directly alert on specific IAM API activity events. GuardDuty detects unusual IAM activity patterns but not routine policy changes.

---

## Question 20

Which IAM best practice should a solutions architect recommend when a new employee joins the company and needs access to the AWS Management Console to manage EC2 resources?

- A) Create an IAM user for the employee with a password, attach the AmazonEC2FullAccess managed policy directly to the user, and provide the console login URL
- B) Create an IAM user for the employee, add them to an existing IAM group that has the appropriate EC2 permissions policy attached, and enable MFA on the account
- C) Share the AWS root account credentials with the employee so they can access all services without needing individual permissions configured
- D) Create a new IAM role for the employee and have them assume it using their personal Google account credentials

### Answer 20

Correct Answer: B

### Explanation 20

- A is incorrect: Attaching policies directly to individual users is an anti-pattern. As the organization grows, managing per-user policy attachments becomes unmanageable. The AWS best practice is to use groups for permission management. Additionally, MFA should always be required for console access.
- B is correct: This follows IAM best practices: (1) use IAM groups to manage permissions at scale — add users to groups rather than attaching policies to individual users; (2) the group has the appropriate scoped policy, not AdministratorAccess; (3) MFA is required for console access, adding a second authentication factor against credential theft.
- C is incorrect: Sharing root credentials is a critical security violation. The root account has unrestricted access to all AWS services and cannot be restricted by IAM policies. Root credentials must never be shared and should only be used for the specific tasks that require root access (such as changing the account email address).
- D is incorrect: Personal Google accounts cannot directly assume IAM roles without proper federation configuration (such as SAML 2.0 or OIDC federation through IAM Identity Center or Cognito). This is not the standard approach for employee access provisioning.
