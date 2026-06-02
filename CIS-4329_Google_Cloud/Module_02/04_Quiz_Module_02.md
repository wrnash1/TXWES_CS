# Quiz — Module 02

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: IAM — Roles, Policies, and Service Accounts

### 10 Questions | 10 Points Each | Total: 100 Points

---

## Question 1

Your company has 500 terabytes of historical financial records that must be retained for seven years to comply with government regulations. The data is expected to be accessed at most once per year during an audit. Which Google Cloud Storage class is most cost-effective for this requirement?

A. Standard Storage

B. Nearline Storage

C. Coldline Storage

D. Archive Storage

Correct Answer: D

Distractor Analysis:

- Why A is incorrect: Standard storage is designed for frequently accessed hot data and carries the highest per-GB storage cost. It is far too expensive for data that is accessed less than once per year and stored for seven years.
- Why B is incorrect: Nearline is optimized for data accessed approximately once per month. Its 30-day minimum storage duration and retrieval fees make it inappropriate for annual-access retention archives.
- Why C is incorrect: Coldline is designed for data accessed approximately once per quarter with a 90-day minimum storage duration. Archive has a 365-day minimum duration and the lowest storage cost per GB, making it the correct choice for data accessed less than once per year.

---

## Question 2

A developer on your team needs to read objects from a specific Cloud Storage bucket as part of an automated data pipeline running on a Compute Engine VM. Following the principle of least privilege, which IAM configuration is most appropriate?

A. Grant the developer the `roles/editor` primitive role at the project level.

B. Create a service account, grant it `roles/storage.objectViewer` on the bucket, and attach the service account to the pipeline's Compute Engine VM.

C. Grant the developer `roles/storage.admin` on the bucket so they can also troubleshoot permission issues.

D. Share the developer's personal Google account credentials with the VM's application configuration.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: The `roles/editor` primitive role grants broad write access across every service in the project. This vastly exceeds the read-only requirement for a single bucket and violates least privilege.
- Why C is incorrect: `roles/storage.admin` grants full control including bucket creation and deletion. A pipeline that only needs to read objects requires far less access. Granting storage.admin violates least privilege and increases blast radius if the VM is compromised.
- Why D is incorrect: Sharing personal credentials between a human user account and a machine workload is a critical security violation. Machines should authenticate via service accounts. Personal credentials cannot be safely revoked from a VM without affecting the human user's other access.

---

## Question 3

You need to grant a new junior administrator the ability to view IAM policies on your GCP project, but they must not be able to modify any policies or resources. Which predefined role grants exactly this access?

A. `roles/iam.securityAdmin`

B. `roles/iam.roleAdmin`

C. `roles/iam.securityReviewer`

D. `roles/owner`

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: `roles/iam.securityAdmin` grants the ability to view AND modify IAM policies, which exceeds the read-only requirement stated in the scenario.
- Why B is incorrect: `roles/iam.roleAdmin` allows creating and managing custom IAM roles across the project. It is not scoped to viewing project-level IAM policy bindings.
- Why D is incorrect: `roles/owner` is a primitive role granting full administrative control over all project resources including billing and IAM management. It is the opposite of the least-privilege requirement.

---

## Question 4

While reviewing your project's IAM policy, you notice that a Compute Engine VM's service account has been granted `roles/owner` at the project level. Why is this a security concern, and what is the recommended remediation?

A. Service accounts cannot hold primitive roles; the policy binding is invalid and will have no effect.

B. The `roles/owner` grant gives any workload running on that VM full administrative control over all project resources. Replace it with the minimum predefined role the workload actually needs.

C. This is acceptable because service accounts operate within Google's internal network and cannot be accessed by external attackers.

D. Revoke the service account and re-create the VM using the default Compute Engine service account, which has no roles assigned by default.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Service accounts are fully valid IAM principals and can hold any role including primitive roles. The `roles/owner` binding is completely effective and is a real security risk.
- Why C is incorrect: Service account access tokens can be stolen through compromised application code, server-side request forgery (SSRF) attacks against the metadata server, or leaked key files. An attacker with these tokens has the same access as the service account.
- Why D is incorrect: The default Compute Engine service account is automatically granted `roles/editor` on the project — this is still overly broad. The correct fix is to create a purpose-built service account with only the permissions the workload requires.

---

## Question 5

Your organization needs to ensure that a specific contractor can only perform actions on GCP resources during weekday business hours (Monday through Friday, 9 AM to 5 PM local time). Which IAM feature enables this time-based access restriction?

A. Organization Policy constraints applied at the folder level

B. IAM Deny policies applied to every project the contractor can access

C. IAM Conditions added to the contractor's role binding

D. VPC Service Controls perimeter configured for the contractor's network

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Organization Policy constraints control what types of resources can be created or what configurations are allowed, such as restricting geographic regions. They cannot restrict the time window during which a specific principal can act.
- Why B is incorrect: IAM Deny policies explicitly block specific permissions regardless of what grants exist, but they do not support scheduling of access windows based on time of day or day of week.
- Why D is incorrect: VPC Service Controls create security perimeters around GCP service APIs to prevent data exfiltration between projects. They are not designed to restrict a specific user's access based on time of day.

---

## Question 6

Which statement correctly describes the difference between `allUsers` and `allAuthenticatedUsers` as IAM principals?

A. `allUsers` means all users within your Google Workspace domain; `allAuthenticatedUsers` means all users in your GCP project.

B. `allUsers` means any request from any person on the public internet with no authentication required; `allAuthenticatedUsers` means any request from someone signed in with any Google account.

C. `allUsers` and `allAuthenticatedUsers` are interchangeable synonyms for public access in GCP IAM.

D. `allAuthenticatedUsers` is restricted to users with a Verizon-verified corporate identity; `allUsers` includes non-corporate Google accounts.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Neither identifier is scoped to a specific organization domain. `allUsers` is the entire unauthenticated public internet. `allAuthenticatedUsers` is any Google-authenticated user anywhere in the world, not just within your project.
- Why C is incorrect: The two identifiers are meaningfully different. `allUsers` requires no login and grants access to anyone. `allAuthenticatedUsers` requires a valid Google sign-in, which provides a layer of identity even if that identity is not from your organization.
- Why D is incorrect: GCP does not integrate with Verizon or any specific corporate directory for these built-in principal identifiers. Corporate-domain restriction is achieved with the `domain:` principal prefix combined with a specific Google Workspace domain.

---

## Question 7

A developer is attempting to create a Compute Engine VM using a specific service account, but the command fails with a permission error. The developer has already been granted `roles/compute.instanceAdmin.v1` on the project. What is the most likely missing permission?

A. The developer needs `roles/compute.admin` instead of `roles/compute.instanceAdmin.v1`.

B. The developer needs `roles/iam.serviceAccountUser` granted on the specific service account they are trying to attach.

C. The developer needs `roles/owner` because creating VMs with custom service accounts requires project ownership.

D. The service account must be in the same folder as the VM to be attached.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: `roles/compute.admin` is a broader role than `roles/compute.instanceAdmin.v1` but the issue is not about Compute Engine permissions — the developer can create VMs, they just cannot attach the specific service account. The missing permission is about service account usage, not Compute Engine administration.
- Why C is incorrect: `roles/owner` is not required to attach a service account to a VM. The `roles/iam.serviceAccountUser` role on the specific service account is the precise permission needed. Requiring ownership for this task would violate least privilege.
- Why D is incorrect: Service account attachment is governed by IAM permissions, not by resource hierarchy proximity. A service account in any project can be attached to a VM in any project, subject to cross-project IAM configuration. There is no folder-proximity requirement.

---

## Question 8

You want to create a custom IAM role that includes specific permissions tailored to your application's needs. At which levels of the GCP resource hierarchy can custom roles be created?

A. Organization and Folder levels only

B. Folder and Project levels only

C. Organization and Project levels only

D. Organization, Folder, and Project levels

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Custom roles cannot be created at the Folder level. This is a specific limitation in GCP IAM that is commonly tested on the ACE exam.
- Why B is incorrect: Custom roles cannot be created at the Folder level in GCP. While Project-level custom role creation is correct, the Folder level is excluded.
- Why D is incorrect: Folder-level custom role creation is not supported in GCP IAM. Custom roles can exist at the Organization level (available to all projects in the org) or at the Project level (available only within that project).

---

## Question 9

Your team decides to stop using a service account. You delete the service account from the project. A week later you need to restore it because a legacy system still depends on it. What happens when you try to recreate a service account with the same name?

A. GCP restores the original service account from a 30-day backup automatically.

B. A new service account is created with the same email address but a new unique ID; any previous IAM bindings referencing the old service account's ID are not automatically restored.

C. You cannot reuse a service account name for 60 days after deletion to prevent impersonation attacks.

D. The deletion is reversible within 7 days by clicking "Undelete" in the Console under IAM and Admin.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: GCP does not maintain a backup of deleted service accounts. Service account deletion is intended to be a permanent action, and there is no automatic restore mechanism.
- Why C is incorrect: GCP does allow reuse of a service account name after deletion. The name (email address) can be recreated, but the new service account has a different unique numeric ID. This means any IAM policies that referenced the old unique ID by number will not automatically apply to the new account.
- Why D is incorrect: Standard IAM service account deletion does not support undelete. (There is a workload identity pool service account undelete in specific scenarios, but standard user-managed service account deletion is not reversible in the way described.)

---

## Question 10

You are auditing a GCP project and want to find out who modified the project's IAM policy three days ago. Which GCP service and log type would you query?

A. Cloud Monitoring > Metrics Explorer, filtering for IAM change events

B. Cloud Logging > Logs Explorer, querying Admin Activity audit logs

C. Security Command Center > Findings, filtering for IAM misconfigurations

D. Cloud Trace > Trace List, searching for IAM policy write operations

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Cloud Monitoring metrics track numerical time-series data such as CPU utilization and request counts. It does not record who performed administrative actions like IAM policy changes. IAM changes are recorded as audit log entries, not metrics.
- Why C is incorrect: Security Command Center identifies security vulnerabilities and misconfigurations in your GCP environment. It can surface IAM-related findings but it does not provide a time-stamped audit trail of who made specific IAM changes on a specific date.
- Why D is incorrect: Cloud Trace records distributed tracing data for application performance analysis — request latency, call graphs, and spans. It does not capture administrative control-plane operations such as IAM policy modifications.

---

End of Quiz — Module 02

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
