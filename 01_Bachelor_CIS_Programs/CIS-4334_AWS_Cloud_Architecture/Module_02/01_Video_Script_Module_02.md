# Video Script: Module 02 - IAM: Users, Roles, Policies, and Best Practices

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Duration:** 20-24 minutes
**Instructor:** Professor Nash

---

## Opening and Module Objectives

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp &bull; AWS Certified Cloud Practitioner CLF-C02 Full Course &bull; Module 02</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=7HKot-brXFE" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/7HKot-brXFE" title="freeCodeCamp &bull; AWS Certified Cloud Practitioner CLF-C02 Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp &bull; AWS Certified Cloud Practitioner CLF-C02 Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

Welcome back to CIS-4334. I am Professor Nash, and this is Module 02: IAM — Identity and Access Management.

If there is one service that underpins every other service in AWS, it is IAM. Every API call made to AWS — whether from the console, the CLI, or an application — is authenticated and authorized through IAM. Get IAM wrong and your architecture is insecure regardless of how well-designed everything else is. Get IAM right and you have a solid security foundation for everything we build in this course.

By the end of this module you will be able to:

- Differentiate between IAM users, groups, roles, and identity providers
- Construct IAM policy JSON documents that implement least-privilege access
- Explain how IAM policy evaluation logic determines allow or deny
- Apply IAM best practices including MFA enforcement and role-based access
- Analyze an existing IAM policy for over-permissions

---

## IAM Core Identity Types

IAM has four core identity types. Understanding each one and when to use it is fundamental to both the exam and real-world AWS security.

**IAM Users** are individual identities with long-term credentials — a username and password for console access, and access keys (access key ID plus secret access key) for programmatic access. IAM users represent a specific person or application that needs persistent access. The SAA-C03 exam will test you on when NOT to use IAM users — specifically, you should never create IAM users for applications running on AWS. Use roles for that. And you should never embed access keys in application code.

**IAM Groups** are collections of IAM users. You attach policies to a group and every user in that group inherits those permissions. Groups exist purely for administrative convenience — they are not identities themselves and cannot be used in policy conditions. A user can belong to multiple groups. Groups cannot contain other groups.

**IAM Roles** are the most important IAM identity type for the SAA-C03 exam. A role is an IAM identity that can be assumed by a trusted entity — an EC2 instance, a Lambda function, another AWS account, a federated identity provider, or a specific IAM user. Roles have no long-term credentials. When an entity assumes a role, it receives temporary security credentials — an access key, a secret key, and a session token — that expire after a configurable period from 15 minutes to 12 hours.

Why does this matter? Because roles solve the credential management problem. If you hardcode an IAM user's access keys in your EC2 application code, those keys can be extracted from the instance, committed to source control by mistake, or exposed in a breach. With an instance role, the EC2 instance assumes the role and gets temporary credentials automatically rotated by the AWS SDK. There are no static keys to manage or expose.

**Identity Providers** allow federation — the ability to use an external identity system to authenticate to AWS. AWS supports SAML 2.0 for enterprise federation (think Active Directory via ADFS) and OpenID Connect for web identity federation (think a Cognito user pool). With federation, users authenticate to their existing identity provider and receive temporary AWS credentials through the Security Token Service. This eliminates the need to create IAM users for every employee in a large organization.

---

## IAM Policies and Evaluation Logic

IAM policies are JSON documents that define what actions are allowed or denied on which resources under what conditions. There are several types of policies you must understand for the exam.

**Identity-based policies** are attached to an IAM user, group, or role. They define what that identity can do.

**Resource-based policies** are attached directly to an AWS resource — most commonly an S3 bucket policy, a KMS key policy, or an SQS queue policy. They define who can perform actions on that specific resource. Resource-based policies allow cross-account access without requiring the trusting account to create IAM roles.

**AWS Managed Policies** are pre-built policies maintained by AWS. Examples: AdministratorAccess, ReadOnlyAccess, AmazonS3FullAccess. They are convenient but often grant broader permissions than needed.

**Customer Managed Policies** are policies you create and maintain. They give you precise control over permissions and are the preferred approach for production environments.

**Inline Policies** are embedded directly within a single user, group, or role. They are not reusable and are deleted when the identity is deleted. Use inline policies sparingly — they make auditing harder.

Now let me show you a policy document.

[SHOW CONSOLE]

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadOnSpecificBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-company-data",
        "arn:aws:s3:::my-company-data/*"
      ]
    }
  ]
}
```

Let me walk through every element. Version 2012-10-17 is the current policy language version — always use this. The Statement array contains one or more permission statements. Each statement has an Effect — either Allow or Deny. Action lists the specific API operations. Resource specifies the ARN of the resource.

Notice the two Resource ARNs. The first is the bucket itself — needed for s3:ListBucket. The second with the wildcard is all objects in the bucket — needed for s3:GetObject. This is a common exam trap: if you only include the bucket ARN without the wildcard, s3:GetObject will be denied.

Now let me explain IAM evaluation logic.

The evaluation logic follows these steps in order. First, start with an implicit deny — by default everything is denied. Second, check for an explicit Deny anywhere in all applicable policies. An explicit Deny always wins and cannot be overridden by any Allow. Third, check for an explicit Allow. If an Allow exists and no Deny overrides it, the request is permitted.

The critical rule: an explicit Deny always overrides any Allow. If a Service Control Policy denies an action and an identity-based policy allows that same action, the Deny wins. This is the most tested IAM evaluation concept on SAA-C03.

---

## IAM Best Practices

The SAA-C03 exam tests IAM best practices extensively.

**Least privilege access** — grant only the minimum permissions required to perform the task. Start with no permissions and add only what is needed. Do not start with AdministratorAccess and remove permissions later — that approach is risky.

**Never use the root account for day-to-day operations.** The AWS root user has unrestricted access to everything. Create an IAM admin user for routine administration. Lock away the root credentials. Enable MFA on root immediately.

**Enforce MFA.** Multi-factor authentication adds a time-based one-time password to the authentication process. You can enforce MFA using a policy condition:

[SHOW CONSOLE]

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
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

This policy denies all actions if MFA is not present. Attach it to users who must authenticate with MFA before performing any action.

**Use roles for applications on AWS, never access keys.** EC2 instances, Lambda functions, and ECS tasks should use IAM roles, not embedded access keys. The AWS SDK automatically retrieves and rotates temporary credentials from the EC2 instance metadata service when a role is attached. No key management required.

**Rotate access keys regularly.** If you must use access keys for automation, rotate them regularly and delete unused keys. Use the IAM credential report to audit key age.

**Use permission boundaries for delegated administration.** A permission boundary sets the maximum permissions an IAM entity can have. Even if an identity-based policy grants more, the permission boundary limits the effective permissions. This is used when a central team delegates IAM administration to individual teams but needs to prevent privilege escalation.

---

## IAM Roles in Practice

Let me walk through the two most common role patterns you will see on the exam.

**EC2 Instance Profile.** When you launch an EC2 instance, you attach an IAM role via an instance profile. The AWS SDK running on the instance retrieves temporary credentials from the EC2 Instance Metadata Service. The credentials are rotated automatically. The application code never handles static credentials.

```text
EC2 Instance
  |-- requests creds from Instance Metadata Service (169.254.169.254)
  |-- STS issues temporary credentials for IAM Role: MyAppRole
  |-- MyAppRole policy allows s3:GetObject on target bucket
```

**Cross-Account Role Assumption.** A role in Account B defines a trust policy that allows a principal in Account A to assume it. The user in Account A calls sts:AssumeRole targeting the role ARN in Account B, receives temporary credentials, and performs actions in Account B.

This pattern is essential for multi-account Organizations architectures — a central security account can assume roles into member accounts for audit and remediation without storing credentials for each account.

---

## Service Control Policies

Service Control Policies are IAM policies attached at the AWS Organizations level — to the root, an organizational unit, or an individual member account. SCPs set the maximum permissions for all identities in the accounts they apply to. Even if an IAM policy in a member account grants s3:DeleteBucket, if the SCP at the OU level denies s3:DeleteBucket, the delete will be denied for all identities in that OU — including the account root user.

SCPs do not grant permissions — they restrict them. An SCP that allows s3:* does not mean any IAM identity can use S3. The IAM identity still needs its own allow policy. SCPs define the ceiling of what is possible.

For the SAA-C03 exam: if a scenario involves preventing all accounts in an organization from using a specific Region or service, the answer is an SCP applied at the organization or OU level.

---

## Module Summary and Exam Preview

Here are the key patterns the SAA-C03 exam tests from this module.

An explicit Deny always overrides any Allow. When evaluating multi-policy scenarios, check for Deny statements first.

Applications on AWS use roles, not IAM user access keys. Any scenario mentioning embedded credentials is describing an anti-pattern — the solution is an IAM role.

The root user should only be used for tasks that explicitly require it. All other operations use IAM identities.

SCPs in AWS Organizations limit maximum permissions for entire accounts or OUs. They cannot grant permissions — only restrict them.

Resource-based policies enable cross-account access without requiring role assumption. S3 bucket policies, SQS resource policies, and KMS key policies are the most common examples.

In the lab this week you will write an IAM policy for a least-privilege scenario and analyze an existing policy for over-permissions — skills tested directly on the SAA-C03 exam.

For your certification study: <aws.amazon.com/certification>

---

End of Module 02 Video Script
