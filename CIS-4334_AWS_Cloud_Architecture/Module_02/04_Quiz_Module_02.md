# Quiz: Module 02 - IAM – Users, Roles, Policies, and Best Practices
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which IAM identity should be assigned to an EC2 instance to allow it to securely access an S3 bucket without storing long-term access keys on the instance?
*   A) IAM User with an access key stored in `~/.aws/credentials`
*   B) IAM Group with an S3 policy attached
*   C) IAM Role with an EC2 trust policy and an S3 permission policy attached
*   D) AWS Root Account credentials passed as environment variables
*   **Correct Answer:** C) An IAM Role with an EC2 trust policy issues temporary STS credentials automatically to the instance, eliminating the need for stored long-term keys.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Storing access keys in a credentials file on an EC2 instance is a security anti-pattern — if the instance is compromised, the long-term keys are exposed and cannot self-rotate.
    *   *Why B is incorrect:* IAM Groups are collections of IAM users; they cannot be assigned to EC2 instances and do not issue credentials to services.
    *   *Why C is correct:* An IAM Role attached to an EC2 instance injects rotating temporary credentials via the Instance Metadata Service (IMDS). The AWS SDK automatically retrieves these credentials without any configuration on the instance.
    *   *Why D is incorrect:* Using root account credentials anywhere other than account-level administrative tasks is an IAM security violation. The SAA-C03 exam always treats root credential usage in application code as incorrect.

---

**Question 2**
Which of the following is the most accurate definition of an **IAM Role** in AWS?
*   A) A permanent set of long-term access keys assigned to a named IAM user for API authentication.
*   B) A collection of IAM users organized for centralized permission management via attached group policies.
*   C) An identity with defined permissions that can be assumed by trusted entities (AWS services, users, or federated identities) to receive temporary, automatically rotating credentials.
*   D) A JSON document that defines allowed and denied API actions on specific AWS resources for a given principal.
*   **Correct Answer:** C) An IAM Role is an identity with defined permissions that can be assumed by trusted entities to receive temporary, automatically rotating STS credentials.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes an IAM User with long-term access keys — the opposite of what a Role provides.
    *   *Why B is incorrect:* This describes an IAM Group, not a Role.
    *   *Why C is correct:* IAM Roles issue short-lived STS credentials, are assumed by trusted principals (defined in the trust policy), and are the preferred mechanism for granting AWS services and cross-account identities permissions.
    *   *Why D is incorrect:* This describes an IAM Policy document, not a Role itself.

---

**Question 3**
A security team discovers that a developer committed AWS access keys to a public GitHub repository. Which combination of actions should be taken immediately to mitigate the impact?
*   A) Rotate the access key in IAM and update the GitHub repository's README to warn users.
*   B) Deactivate and delete the compromised access key immediately, review CloudTrail logs for unauthorized activity, and replace key-based authentication with IAM Roles.
*   C) Enable AWS Config to record resource configuration changes going forward and set a CloudWatch alarm.
*   D) Move the application to a different AWS Region and create a new IAM user with the same permissions.
*   **Correct Answer:** B) Deactivate and delete the compromised key immediately, review CloudTrail logs for unauthorized activity, and replace key-based authentication with IAM Roles.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Rotating the key (generating a new one) without immediately deleting the compromised key leaves the exposed credentials active. A README warning does nothing to stop an attacker who already has the key.
    *   *Why B is correct:* Immediate deactivation stops the exposure. CloudTrail audit reveals what actions the key was used for. Switching to IAM Roles eliminates the root cause — long-term static credentials that can be accidentally exposed.
    *   *Why C is incorrect:* AWS Config tracks resource configuration changes but does not detect or revoke compromised credentials. This is a useful long-term control but not an immediate remediation.
    *   *Why D is incorrect:* Moving Regions does not invalidate the compromised key, which is a global IAM credential. The same user in the new Region is still exposed.

---

**Question 4**
A solutions architect is writing an IAM policy. One policy statement contains `"Effect": "Allow"` for `s3:DeleteObject`, and a separate policy attached to the same user contains `"Effect": "Deny"` for `s3:DeleteObject` on the same bucket. What is the result when the user attempts to delete an object?
*   A) The Allow takes precedence because it was attached first.
*   B) The user is prompted to choose which policy to apply.
*   C) The Deny takes precedence; the delete operation is blocked regardless of any Allow.
*   D) Both policies cancel each other out, resulting in an implicit Deny.
*   **Correct Answer:** C) An explicit Deny in any policy always overrides any Allow. The delete operation is blocked.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IAM policy evaluation does not consider the order in which policies were attached. Explicit Deny always wins regardless of attachment order.
    *   *Why B is incorrect:* There is no interactive prompt in IAM policy evaluation. The evaluation logic is deterministic: explicit Deny overrides explicit Allow.
    *   *Why C is correct:* This is the foundational IAM policy evaluation rule for the SAA-C03 exam: Explicit Deny > Explicit Allow > Implicit Deny (default). An explicit Deny can never be overridden by an Allow in the same or a different policy.
    *   *Why D is incorrect:* Conflicting Allow and Deny do not cancel each other; the Deny wins unconditionally.

---

**Question 5**
A company wants to allow users from a partner AWS account (Account B) to access a specific S3 bucket in their own account (Account A) without creating IAM users in Account A. Which IAM feature best supports this requirement?
*   A) Create IAM users in Account A with the same usernames as Account B users and share the passwords.
*   B) Create an IAM Role in Account A with a trust policy that allows Account B to assume it, and grant the Role S3 bucket permissions.
*   C) Enable S3 Cross-Region Replication to copy bucket contents into Account B.
*   D) Attach an AWS managed policy to Account B's root user granting S3 access in Account A.
*   **Correct Answer:** B) Create an IAM Role in Account A with a trust policy allowing Account B to assume it, granting the Role the required S3 permissions.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Creating duplicate IAM users violates the principle of least privilege, creates credential management overhead, and does not scale. Sharing passwords across accounts is an IAM anti-pattern.
    *   *Why B is correct:* Cross-account IAM Roles are the canonical AWS pattern for granting partner or external account access without creating persistent users in the trusting account. Account B users assume the Role via STS and receive temporary credentials scoped to the defined permissions.
    *   *Why C is incorrect:* Cross-Region Replication copies data between S3 buckets — it is a data movement feature, not an access control mechanism. It does not grant Account B the ability to read from Account A's bucket on demand.
    *   *Why D is incorrect:* Root account credentials should never be used for application or cross-account access. AWS managed policies cannot be directly attached to a root user in another account; this is not a supported IAM construct.

