# Quiz: Module 02 – IAM: Roles, Policies, and Service Accounts
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your company has 500 terabytes of historical financial records that must be retained for 7 years to comply with government regulations. You expect to access this data at most once a year during an audit. Which Google Cloud Storage class is the most cost-effective choice for this requirement?

A) Standard Storage
B) Nearline Storage
C) Coldline Storage
D) Archive Storage

*   **Correct Answer:** D) Archive Storage
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Standard is for frequently accessed ("hot") data and carries the highest storage-at-rest cost, making it far too expensive for rarely accessed 7-year retention.
    *   *Why B is incorrect:* Nearline is optimized for data accessed roughly once per month; its per-retrieval costs and minimum storage duration (30 days) make it inappropriate for annual-access compliance archives.
    *   *Why C is incorrect:* Coldline is optimized for data accessed roughly once per quarter (90-day minimum storage duration). Archive has a 365-day minimum duration and the lowest storage cost, making it the correct choice for data accessed less than once a year.

---

**Question 2**
A developer on your team needs to read objects from a specific Cloud Storage bucket as part of an automated pipeline. Following the principle of least privilege, which IAM configuration is most appropriate?

A) Grant the developer the primitive `roles/editor` role at the project level.
B) Create a Service Account, grant it `roles/storage.objectViewer` on the bucket, and attach it to the pipeline's Compute Engine VM.
C) Grant the developer `roles/storage.admin` on the bucket so they can troubleshoot any issues.
D) Share your own account credentials with the developer so the pipeline can authenticate.

*   **Correct Answer:** B) Create a Service Account, grant it `roles/storage.objectViewer` on the bucket, and attach it to the pipeline's Compute Engine VM.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The primitive `roles/editor` grants broad write access across all project resources — far more than read access to a single bucket, violating least privilege.
    *   *Why C is incorrect:* `roles/storage.admin` grants full control over the bucket including deletion, which is far more than the read-only access required.
    *   *Why D is incorrect:* Sharing personal account credentials is a severe security violation; credentials should never be shared, and machines should authenticate via Service Accounts, not human user accounts.

---

**Question 3**
You need to grant a new junior administrator the ability to view IAM policies on your GCP project, but they must not be able to modify any policies. Which predefined role grants exactly this access?

A) `roles/iam.securityAdmin`
B) `roles/iam.roleAdmin`
C) `roles/iam.securityReviewer`
D) `roles/owner`

*   **Correct Answer:** C) `roles/iam.securityReviewer`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `roles/iam.securityAdmin` allows viewing and modifying IAM policies, which exceeds the read-only requirement.
    *   *Why B is incorrect:* `roles/iam.roleAdmin` allows creating and managing custom IAM roles — it is not scoped to viewing project policies.
    *   *Why D is incorrect:* `roles/owner` is a primitive role that grants full administrative control over all project resources, which is the opposite of least privilege.

---

**Question 4**
While reviewing your project's IAM policy, you notice that a Compute Engine VM's Service Account has been granted `roles/owner` at the project level. Why is this a security concern, and what is the recommended remediation?

A) Service Accounts cannot hold primitive roles; the policy binding is invalid and will have no effect.
B) The `roles/owner` binding gives any workload running on that VM full administrative control over all project resources; replace it with the minimum predefined role the workload actually needs.
C) This is acceptable because Service Accounts are internal to GCP and cannot be compromised by external attackers.
D) Revoke the Service Account and recreate the VM using the default Compute Engine Service Account, which has no roles assigned.

*   **Correct Answer:** B) The `roles/owner` binding gives any workload running on that VM full administrative control over all project resources; replace it with the minimum predefined role the workload actually needs.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Service Accounts are valid IAM principals and can hold any role including primitive roles; the binding is fully effective.
    *   *Why C is incorrect:* Service Account keys and tokens can be stolen through compromised application code, SSRF attacks, or metadata server abuse — they are absolutely a target for attackers.
    *   *Why D is incorrect:* The default Compute Engine Service Account actually carries the `roles/editor` primitive role by default, which is still overly broad; the correct fix is to create a dedicated Service Account with only the required predefined roles.

---

**Question 5**
Your organization needs to ensure that a specific user can only perform actions on GCP resources during weekday business hours (Monday–Friday, 9 AM–5 PM). Which IAM feature enables this time-based access restriction?

A) Organization Policy constraints
B) IAM Deny policies applied at the folder level
C) IAM Conditions added to the role binding for that user
D) VPC Service Controls perimeter configuration

*   **Correct Answer:** C) IAM Conditions added to the role binding for that user
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Organization Policy constraints control what *types* of resources can be created (e.g., restricting allowed regions or VM types), not the time window during which a principal can act.
    *   *Why B is incorrect:* IAM Deny policies explicitly block specific permissions regardless of what grants exist, but they do not support time-based scheduling of access windows.
    *   *Why D is incorrect:* VPC Service Controls create security perimeters around GCP APIs to prevent data exfiltration between projects, not to restrict a user's access based on time of day.
