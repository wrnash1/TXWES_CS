# Reading Guide: Module 02 - IAM – Users, Roles, Policies, and Best Practices
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 02 - IAM – Users, Roles, Policies, and Best Practices**! AWS Identity and Access Management (IAM) is the security control plane for every AWS account. This module covers how identities are created, how permissions are expressed as JSON policies, and how IAM Roles enable secure, credential-free access between AWS services. IAM is the highest-weighted security topic on the SAA-C03 exam and appears in scenario questions across nearly every service domain.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **IAM Users**: Long-term identity objects within an AWS account that represent a human operator or an application. Users have static access credentials (username/password for console, access key/secret key for API). Best practice is to avoid long-lived user credentials in favor of IAM Roles and federated identity wherever possible.

*   **IAM Groups**: A collection of IAM users. Policies attached to a group apply to all users in that group, enabling centralized permission management. Groups cannot be nested (a group cannot contain another group), and users can belong to multiple groups. This is the preferred pattern for assigning permissions to human operators at scale.

*   **IAM Roles**: An identity with a set of permissions that can be assumed by trusted entities — including AWS services (e.g., EC2 assuming a Role to access S3), IAM users from other accounts (cross-account access), or federated users (SAML/OIDC). Roles issue short-lived, automatically rotated temporary credentials via AWS STS (Security Token Service), making them far more secure than long-term access keys.

*   **IAM Policies (JSON)**: Documents written in JSON that define what actions are allowed or denied on which AWS resources under which conditions. Policies consist of one or more statements, each containing Effect (Allow/Deny), Action (e.g., `s3:GetObject`), Resource (ARN), and optional Condition. Explicit Deny always overrides Allow. Policies can be managed (AWS-managed or customer-managed) or inline.

*   **Multi-Factor Authentication (MFA)**: An additional layer of authentication requiring a second factor — typically a time-based one-time password (TOTP) from a virtual or hardware device — beyond a username and password. MFA should be enforced on all IAM users with console access, and especially on the root account. IAM policies can require MFA as a condition for sensitive API calls.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** IAM falls primarily in Design Secure Architectures (30% of exam). Nearly every scenario question that involves security, access, or "least privilege" touches IAM. This is the most important service to master for the exam.

*   **Roles Over Users for Services:** The exam consistently rewards the answer "use an IAM Role" whenever a service (EC2, Lambda, ECS task) needs to access another AWS service. Using an IAM Role eliminates the need to store or rotate access keys and leverages STS temporary credentials automatically.

*   **Policy Evaluation Logic:** When multiple policies apply, AWS evaluates them in this order: (1) explicit Deny always wins; (2) explicit Allow grants access; (3) default implicit Deny. Exam questions frequently set up scenarios with conflicting policies — always look for the Deny first.

*   **Least Privilege Principle:** The exam favors answers that grant only the minimum permissions required. Watch for distractor answers that grant `*` (wildcard) actions or resource ARNs when a narrower scope is possible.

*   **Root Account Best Practice Trap:** Never use or share the root account credentials for day-to-day operations. The exam will test this — the correct answer always involves creating an IAM user or Role and locking away the root account with MFA.

*   **Study Resource:** The official AWS IAM documentation provides the definitive policy reference and best practices guide: [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/). Review the "Security best practices in IAM" section specifically, as it maps directly to SAA-C03 scenario questions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the IAM chapter in the AWS Solutions Architect study materials and the "AWS IAM Best Practices" section of the IAM User Guide, available through the AWS Whitepapers portal: [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/). The whitepaper "AWS Security Best Practices" covers IAM policy design in depth.

*   **Required Video:** Watch the IAM module in the AWS Certified Solutions Architect Associate course playlist, focusing on policy evaluation, Role trust relationships, and the difference between identity-based and resource-based policies: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Create an IAM user and assign it to a group with a managed policy:** In the AWS Console, create a group named `developers`, attach the `AmazonEC2ReadOnlyAccess` managed policy, and add a new IAM user to the group. Observe how group membership grants the policy permissions.

*   **Create and assume an IAM Role for EC2:** Create an IAM Role with EC2 as the trusted service, attach a policy allowing `s3:GetObject` on a specific bucket ARN, and attach the Role to an EC2 instance. Verify from within the instance that `aws s3 cp s3://your-bucket/file .` succeeds without any stored access keys.

*   **Enable MFA on an IAM user and test the MFA condition:** Enable a virtual MFA device on an IAM user, then write and test a policy with a `Condition` block requiring `aws:MultiFactorAuthPresent: true` for sensitive operations.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Review AWS IAM best practices at [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).
- [ ] Read the "AWS Security Best Practices" whitepaper at [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/).
- [ ] Watch the IAM video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab creating IAM users, groups, roles, and MFA.
- [ ] Proceed to the weekly quiz.
