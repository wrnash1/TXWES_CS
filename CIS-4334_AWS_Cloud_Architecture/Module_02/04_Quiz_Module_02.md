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
