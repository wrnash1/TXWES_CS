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
