# Quiz: Module 02 — IAM and Access Control in GCP

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
This quiz covers IAM roles, service accounts, policies, conditions, Workload
Identity Federation, and Cloud Audit Logs.

---

## Question 1

A developer needs to deploy new virtual machines on Compute Engine but should
not be able to modify networking or IAM settings. Which predefined role best
satisfies least privilege?

- A) `roles/owner`
- B) `roles/compute.admin`
- C) `roles/compute.instanceAdmin.v1`
- D) `roles/editor`

**Correct Answer:** C

**Explanation:** `roles/compute.instanceAdmin.v1` grants the ability to create,
modify, and delete VM instances without granting network administration or IAM
management capabilities. `roles/compute.admin` includes network and security
management. Both `roles/owner` and `roles/editor` are primitive roles that
grant far broader access than required.

---

## Question 2

Your organization has a CI/CD pipeline running on GitHub Actions that needs to
deploy containers to Google Kubernetes Engine. The security team has forbidden
the use of service account key files. What is the recommended solution?

- A) Store the service account key in GitHub Secrets and reference it in the
     workflow
- B) Use Workload Identity Federation to allow GitHub Actions to exchange its
     OIDC token for a Google access token
- C) Grant the `allUsers` principal the `roles/container.developer` role on
     the GKE cluster
- D) Create a new Google Account for the pipeline and store its password in
     GitHub Secrets

**Correct Answer:** B

**Explanation:** Workload Identity Federation allows external workloads (such as
GitHub Actions) to authenticate to GCP using their native identity tokens
without requiring a service account key file. This is the recommended approach
when key files are prohibited. Storing keys in GitHub Secrets (option A) still
uses a key file. Options C and D are security violations.

---

## Question 3

An IAM policy at the Organization level grants a user `roles/editor`. A project
admin adds a `roles/viewer` binding for the same user on a specific project,
intending to restrict their access. What is the actual effect?

- A) The user has viewer access in that project due to the more specific binding
- B) The user has editor access in that project; the project-level binding adds
     permissions but does not reduce inherited ones
- C) The bindings conflict and the user loses all access in that project
- D) The most recently created binding takes precedence

**Correct Answer:** B

**Explanation:** GCP IAM inheritance is strictly additive. Permissions inherited
from higher levels in the resource hierarchy cannot be reduced by bindings at
lower levels. The user retains `roles/editor` (inherited from the Organization)
plus `roles/viewer` (granted at the project). The net result is editor access.

---

## Question 4

Which of the following is the correct format for a GCP IAM permission?

- A) `ProjectID:ServiceName:Action`
- B) `service.resourceType.action`
- C) `ACTION_ON_RESOURCE_BY_SERVICE`
- D) `roles/service.action`

**Correct Answer:** B

**Explanation:** GCP IAM permissions follow the format `service.resourceType.action`,
for example `compute.instances.start` or `storage.objects.delete`. Roles (option D)
use the `roles/` prefix, but individual permissions do not.

---

## Question 5

A Cloud Run service needs to read secrets from Secret Manager at runtime. No
human user should be able to perform this action directly. What is the
recommended approach?

- A) Grant `roles/secretmanager.secretAccessor` to `allAuthenticatedUsers`
- B) Create a service account, grant it `roles/secretmanager.secretAccessor`,
     and attach the service account to the Cloud Run service
- C) Create a service account key file, store it in the container image, and
     read it at runtime
- D) Grant the developer's personal Google Account
     `roles/secretmanager.secretAccessor` and hardcode their credentials

**Correct Answer:** B

**Explanation:** The correct pattern is to create a dedicated service account
with the minimum required permissions, then attach it to the Cloud Run service.
Cloud Run will automatically use the attached service account's identity when
calling GCP APIs, with no key files required. Options A, C, and D all introduce
security risks through overly broad access, hardcoded credentials, or key files.

---

## Question 6

Which Cloud Audit Log type must be explicitly enabled and may generate
significant log volume and cost?

- A) Admin Activity logs
- B) System Event logs
- C) Data Access logs
- D) Policy Denied logs

**Correct Answer:** C

**Explanation:** Data Access logs record API calls that read resource
configuration or user data. They are disabled by default because they can
generate very high log volumes (every object read in Cloud Storage, for example).
They must be explicitly enabled per service. Admin Activity, System Event, and
Policy Denied logs are always enabled at no charge.

---

## Question 7

You need to grant a third-party vendor read access to a specific Cloud Storage
bucket for exactly 30 days, after which access should automatically become
ineffective. No manual intervention should be needed after the initial setup.
What should you use?

- A) Create a time-limited service account that expires in 30 days
- B) Add an IAM binding with an IAM Condition using `request.time` to set an
     expiration timestamp
- C) Set a bucket lifecycle rule that removes the IAM binding after 30 days
- D) Use a Signed URL with a 30-day expiration

**Correct Answer:** B

**Explanation:** IAM Conditions support time-based expressions using
`request.time`. Adding a condition like `request.time < timestamp('EXPIRY_DATE')`
to the role binding makes the binding ineffective after that date — no manual
cleanup needed. Service accounts do not have native expiration dates (option A).
Lifecycle rules control object storage, not IAM bindings (option C). Signed URLs
are per-object, not per-principal IAM bindings (option D).

---

## Question 8

A security auditor asks you to show all actions taken in your GCP project over
the last 7 days that modified IAM policies. Which resource contains this
information?

- A) Cloud Monitoring metrics
- B) VPC Flow Logs
- C) Cloud Audit Logs — Admin Activity
- D) Cloud Audit Logs — Data Access

**Correct Answer:** C

**Explanation:** IAM policy changes are administrative operations and are
recorded in Admin Activity audit logs under the `SetIamPolicy` method name.
Admin Activity logs are always enabled and record all configuration and metadata
changes. Data Access logs record data reads and writes, not admin operations.
VPC Flow Logs record network traffic.

---

## Question 9

Which statement correctly describes the difference between an IAM role and an
IAM permission?

- A) A role is granted to a resource; a permission is granted to a principal
- B) A permission is an atomic action allowed on a resource type; a role is a
     named collection of permissions granted to a principal
- C) Roles and permissions are interchangeable terms in Cloud IAM
- D) Permissions are granted directly to principals; roles are granted to
     resources

**Correct Answer:** B

**Explanation:** A permission is the atomic unit — one specific action on one
resource type (e.g., `storage.objects.get`). A role bundles multiple permissions
together and is what gets granted to a principal via a policy binding. Permissions
are never assigned directly to principals in GCP IAM.

---

## Question 10

A VM running a web application is using the Compute Engine default service
account with Project Editor permissions. A security review flags this as a risk.
What is the recommended remediation?

- A) Disable the Compute Engine default service account
- B) Create a dedicated service account with only the permissions the application
     requires, and attach it to the VM
- C) Remove all service accounts from the VM so it runs with no identity
- D) Upgrade the default service account to Project Owner to ensure it never
     lacks permissions

**Correct Answer:** B

**Explanation:** The principle of least privilege requires creating a dedicated
service account with only the specific permissions the application needs, rather
than relying on the broad default service account. Removing all identity (option C)
would break any API calls the application makes. Upgrading to Owner (option D)
makes the problem worse.

---

End of Quiz — Module 02

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

---

### Question 11 (5 points)

A new GCP project is created. No IAM bindings have been added yet. Which
principal automatically has Owner access to the project?

- A) The Google Cloud support team
- B) The user who created the project (the project creator)
- C) The billing account administrator
- D) No one — projects start with no permissions assigned

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Google Cloud support does not receive automatic Owner access to customer projects; they must be explicitly granted access.
  - C) Billing account administrators can link billing accounts to projects but do not automatically receive project-level IAM Owner permissions.
  - D) The project creator is automatically granted `roles/owner` at project creation; the project is not permission-less by default.

---

### Question 12 (5 points)

An organization wants to ensure that service account key files cannot be
created in any project, as a security policy. Which control enforces this
at the organizational level?

- A) Set the `constraints/iam.disableServiceAccountKeyCreation` Organization
   Policy at the Organization node
- B) Revoke `roles/iam.serviceAccountAdmin` from all principals
- C) Enable Data Access audit logs for IAM to monitor key creation events
- D) Create a custom role that omits the `iam.serviceAccountKeys.create`
   permission and assign it to all users

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Revoking `roles/iam.serviceAccountAdmin` would block service account management entirely, not just key creation, and would not affect principals with `roles/owner` or `roles/editor`.
  - C) Audit logs record events after the fact; they do not prevent key creation from occurring.
  - D) Custom roles can only be assigned alongside existing bindings; a user with `roles/owner` still retains key creation ability regardless of additional custom role assignments.

---

### Question 13 (5 points)

Which Cloud Audit Log type records events such as Google performing an
automatic live migration of a Compute Engine VM?

- A) Admin Activity log
- B) Data Access log
- C) System Event log
- D) Policy Denied log

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Admin Activity logs record user-initiated administrative actions, not Google-initiated maintenance events.
  - B) Data Access logs record reads and writes of resource data by users and service accounts, not system-level events.
  - D) Policy Denied logs record access attempts rejected by IAM or VPC Service Controls, not Google maintenance operations.

---

### Question 14 (5 points)

A principal is granted `roles/storage.objectCreator` on a Cloud Storage
bucket. Which operations can this principal perform?

- A) Read, create, and delete objects in the bucket
- B) Create (upload) new objects only — cannot read existing objects or delete
- C) Full administrative control over the bucket and all objects
- D) List objects and read their metadata, but not download content

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `roles/storage.objectCreator` includes `storage.objects.create` only; it does not include `storage.objects.get` (read) or `storage.objects.delete`.
  - C) Full admin control requires `roles/storage.admin`; objectCreator is a narrowly scoped write-only role.
  - D) Listing and reading metadata requires `storage.objects.list` and `storage.objects.getIamPolicy`; those are not included in objectCreator.

---

### Question 15 (5 points)

You have an IAM policy binding with `version: 1`. You need to add an
IAM Condition to one of the bindings. What must you do first?

- A) Delete the existing policy and recreate it with conditions
- B) Upgrade the policy version to 3 — IAM Conditions require policy version 3
- C) Add the condition directly; version 1 supports conditions
- D) Create a new project and apply conditions in that project

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Deleting and recreating the policy would work but is unnecessarily destructive; simply updating the policy version is correct.
  - C) Version 1 policies do not support IAM Conditions; the policy format must be version 3, which uses Common Expression Language (CEL) for condition expressions.
  - D) IAM Conditions can be applied to any project; there is no requirement to create a new project.

---

### Question 16 (5 points)

A team uses the `iam.serviceAccounts.actAs` permission frequently. What
does this permission allow?

- A) It allows the holder to view the list of service accounts in a project
- B) It allows the holder to impersonate a service account, running code as
   that service account's identity
- C) It allows creating new service accounts
- D) It allows disabling and deleting service accounts

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Viewing service accounts requires `iam.serviceAccounts.list`, which is separate from `actAs`.
  - C) Creating service accounts requires `iam.serviceAccounts.create`, which is included in `roles/iam.serviceAccountAdmin`.
  - D) Disabling and deleting service accounts requires `iam.serviceAccounts.disable` and `iam.serviceAccounts.delete` respectively; `actAs` is purely for impersonation.

---

### Question 17 (5 points)

A security engineer wants to verify that a specific user has NOT been
granted any IAM role on a project, either directly or through group membership.
Which tool in the Cloud Console provides this analysis?

- A) Cloud Audit Logs filtered by the user's email
- B) IAM Policy Analyzer (Policy Troubleshooter)
- C) Cloud Asset Inventory search
- D) VPC Service Controls access review

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Audit logs show historical actions performed, not the current effective permissions of a principal.
  - C) Cloud Asset Inventory tracks resource configuration and IAM policies in aggregate, but IAM Policy Analyzer is purpose-built for answering "does this principal have access to this resource and why?"
  - D) VPC Service Controls manages service perimeter policies; it does not analyze IAM role assignments.

---

### Question 18 (5 points)

What is the primary security advantage of using `allAuthenticatedUsers`
versus `allUsers` on a Cloud Storage bucket?

- A) `allAuthenticatedUsers` restricts access to users within the same GCP
   organization
- B) `allAuthenticatedUsers` requires a valid Google account for access, while
   `allUsers` allows completely unauthenticated public internet access
- C) `allAuthenticatedUsers` enforces MFA; `allUsers` does not
- D) There is no difference — both provide equivalent public access

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `allAuthenticatedUsers` is not scoped to an organization; it applies to any person with any valid Google account worldwide.
  - C) Neither principal type enforces MFA; authentication requirements are controlled by Google Account security settings, not IAM member types.
  - D) The difference is significant: `allUsers` requires zero authentication while `allAuthenticatedUsers` requires a Google account sign-in — however, both are considered overly permissive for sensitive data.

---

### Question 19 (5 points)

A GCP organization has three IAM role types available. For a new custom
application that needs only `bigquery.tables.getData` and
`bigquery.jobs.create`, which role type is most appropriate?

- A) Primitive role `roles/editor` — it includes all BigQuery permissions
- B) Predefined role `roles/bigquery.dataViewer` — it covers read operations
- C) Custom role with exactly `bigquery.tables.getData` and
   `bigquery.jobs.create` — follows least privilege precisely
- D) Primitive role `roles/viewer` — it provides read-only access to all
   services

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) `roles/editor` grants modification rights to every service in the project — far broader than the two BigQuery permissions needed.
  - B) `roles/bigquery.dataViewer` includes read access to datasets and tables but does not include `bigquery.jobs.create`, which is needed to actually execute queries. A predefined role that is close but missing a required permission makes it incorrect here.
  - D) `roles/viewer` grants read-only access across all GCP services, which is broader than necessary and does not follow least privilege.

---

### Question 20 (5 points)

When using `gcloud projects get-iam-policy`, the returned JSON includes an
`etag` field. A script reads the policy, modifies it, and then sets it using
`gcloud projects set-iam-policy`. Why is preserving the `etag` in the update
request important?

- A) The etag controls which IAM policy version (1, 2, or 3) is used
- B) The etag prevents race conditions — if another process changed the policy
   between your read and write, the set operation fails rather than silently
   overwriting the concurrent change
- C) The etag is a checksum that verifies the policy JSON is not corrupted
   during transit
- D) The etag is optional metadata and has no functional effect on the policy
   update

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The IAM policy version is controlled by the `version` field, not the etag.
  - C) GCP API transport is already TLS-encrypted; the etag is not a transport integrity check — it is a concurrency control token tied to the server-side policy state.
  - D) If you omit or modify the etag, GCP may reject the update if the policy has changed since you last read it, protecting against overwriting concurrent modifications.
