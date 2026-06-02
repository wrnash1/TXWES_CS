# Reading Guide — Module 02

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: IAM — Roles, Policies, and Service Accounts

### Certification Target: Google Cloud Associate Cloud Engineer

---

## Introduction

Identity and Access Management is the single most tested domain on the Google Cloud Associate Cloud Engineer exam. This reading guide covers the complete IAM model — principals, roles, policy bindings, service accounts, IAM conditions, and audit logging. Study every section carefully. The ACE exam tests these concepts through scenario-based questions that require you to identify the most secure and least-privileged solution, not just recall definitions.

---

## 1. IAM Core Concepts

### The Three-Part Model

Every IAM decision has three components:

- Who: the principal (the identity being granted access)
- Can do what: the role (a bundle of permissions)
- On which resource: where the policy binding is attached

### Principal Types

| Principal Type | IAM Prefix | Description | Use Case |
|---|---|---|---|
| Google Account | `user:` | Individual human user with a Google identity | Named employees or students |
| Service Account | `serviceAccount:` | Application or workload identity | VMs, pipelines, automation |
| Google Group | `group:` | Named collection of accounts | Team-level access management |
| Workspace Domain | `domain:` | All users in a Google Workspace domain | Organization-wide grants |
| allAuthenticatedUsers | (none) | Any signed-in Google account | Broadly public resources |
| allUsers | (none) | Unauthenticated public internet | Fully public assets |

### Choosing the Right Principal Type

Granting roles to Google Groups rather than individual users is the recommended enterprise pattern. When an employee joins a team, add them to the group — they inherit all group permissions instantly. When they leave, remove them from the group — all permissions revoke instantly. This approach scales far better than auditing individual IAM bindings across hundreds of projects.

---

## 2. Role Categories

### Basic Roles

Basic roles (also called primitive roles) predate the modern IAM system. They operate at the project scope and affect every service in the project.

| Role | Identifier | Permissions |
|---|---|---|
| Viewer | `roles/viewer` | Read-only on all project resources |
| Editor | `roles/editor` | Read/write on most project resources; cannot manage IAM |
| Owner | `roles/owner` | Full control including IAM, billing, and project deletion |

When to use basic roles: development or sandbox environments only. Never in production. The ACE exam treats basic roles as the wrong answer whenever a least-privilege solution is requested.

### Predefined Roles — Compute Engine

| Role | Identifier | Key Permissions |
|---|---|---|
| Compute Admin | `roles/compute.admin` | Full control of all Compute Engine resources |
| Instance Admin v1 | `roles/compute.instanceAdmin.v1` | Create, delete, start, stop VM instances |
| Network Admin | `roles/compute.networkAdmin` | Manage networks, subnets, firewalls, routes |
| Security Admin | `roles/compute.securityAdmin` | Manage SSL certs and firewall rules only |
| Viewer | `roles/compute.viewer` | Read-only view of all Compute Engine resources |
| OS Login | `roles/compute.osLogin` | SSH into VMs using OS Login (no sudo) |
| OS Admin Login | `roles/compute.osAdminLogin` | SSH into VMs with sudo via OS Login |

### Predefined Roles — Cloud Storage

| Role | Identifier | Key Permissions |
|---|---|---|
| Storage Admin | `roles/storage.admin` | Full control of buckets and objects |
| Storage Object Admin | `roles/storage.objectAdmin` | Full control of objects; cannot create/delete buckets |
| Storage Object Creator | `roles/storage.objectCreator` | Create objects only; cannot read or delete |
| Storage Object Viewer | `roles/storage.objectViewer` | Read objects; list bucket contents |
| Storage Viewer | `roles/storage.legacyBucketReader` | List buckets; does not include object read |

### Predefined Roles — IAM

| Role | Identifier | Key Permissions |
|---|---|---|
| Security Admin | `roles/iam.securityAdmin` | View and modify IAM policies |
| Security Reviewer | `roles/iam.securityReviewer` | View IAM policies; no modifications |
| Service Account Admin | `roles/iam.serviceAccountAdmin` | Create, update, delete service accounts |
| Service Account User | `roles/iam.serviceAccountUser` | Attach a service account to a resource |
| Service Account Token Creator | `roles/iam.serviceAccountTokenCreator` | Generate tokens for a service account |
| Role Admin | `roles/iam.roleAdmin` | Create and manage custom IAM roles |
| Organization Role Admin | `roles/iam.organizationRoleAdmin` | Manage custom roles at the organization level |

### Custom Roles

Custom roles contain exactly the permissions you specify. Key facts:

- Can be created at Organization level or Project level (not Folder level)
- NOT automatically updated when Google adds new permissions to predefined roles
- Identified by the prefix `roles/` at org level or `projects/PROJECT_ID/roles/` at project level
- Suitable when no predefined role is a precise fit for least-privilege requirements

---

## 3. IAM Policy Structure

### Policy JSON Format

An IAM policy is a JSON document containing:

- `version`: policy schema version (1, 2, or 3; version 3 is required for IAM Conditions)
- `bindings`: array of role-to-member mappings
- `etag`: server-assigned concurrency token

```json
{
  "version": 1,
  "bindings": [
    {
      "role": "roles/storage.objectViewer",
      "members": [
        "user:analyst@txwes.edu",
        "group:data-team@txwes.edu"
      ]
    }
  ],
  "etag": "BwX1AbcDef=="
}
```

### The etag Mechanism

The etag prevents concurrent policy write conflicts. When you read a policy with `get-iam-policy`, the response includes an etag. If you then modify and rewrite the policy using `set-iam-policy`, GCP compares the etag you submit with the current server-side etag. If another administrator modified the policy between your read and write, the etags will not match and GCP rejects your write. Always include the etag when updating policies programmatically.

### Additive Inheritance

IAM policies at parent hierarchy levels automatically apply to all children. The effective permissions on a resource equal the union of:

- Policies directly on the resource
- Policies on the parent project
- Policies on parent folders (all levels)
- Policies on the organization

You cannot reduce a permission at a lower level that was granted at a higher level through standard IAM. (IAM Deny Policies are a newer feature that can explicitly deny permissions at any level — this is advanced and only lightly tested on the current ACE exam.)

---

## 4. Service Accounts

### Service Account Types

| Type | Email Format | Created By | Default Role |
|---|---|---|---|
| User-managed | `NAME@PROJECT_ID.iam.gserviceaccount.com` | You | None (you assign roles) |
| Compute Engine default | `PROJECT_NUM-compute@developer.gserviceaccount.com` | Google when Compute API enabled | `roles/editor` (change this) |
| App Engine default | `PROJECT_ID@appspot.gserviceaccount.com` | Google when App Engine enabled | `roles/editor` (change this) |
| Google-managed | Various `@*.iam.gserviceaccount.com` | Google for internal services | Managed by Google |

The default service accounts carrying `roles/editor` is a well-known security concern. Best practice: disable the default service accounts and create purpose-built user-managed service accounts with only the permissions each workload needs.

### VM Authentication Pattern (Correct)

When code running on a Compute Engine VM needs to call a GCP API:

1. Create a user-managed service account with the minimum required roles
2. Attach the service account to the VM at creation time (`--service-account` flag)
3. Code running on the VM calls the GCP API — credentials are fetched automatically from the instance metadata server
4. No key files are created, stored, or transmitted

### Service Account Key Pattern (Avoid When Possible)

When code runs outside of GCP and cannot use workload identity federation:

1. Create a service account
2. Generate a JSON key file (`gcloud iam service-accounts keys create`)
3. Store the key securely (Secret Manager, CI/CD secret store)
4. Code loads the key to authenticate

Key file risks: long-lived credentials, no automatic rotation, accidental exposure in source code repositories. Use only when no alternative exists.

### Service Account Permissions Dual Role

A service account is both a principal (can be granted roles) and a resource (can have its own IAM policy). To control who can impersonate a service account:

- `roles/iam.serviceAccountUser` on the service account resource — allows attaching the SA to a VM or running jobs as the SA
- `roles/iam.serviceAccountTokenCreator` on the service account resource — allows generating tokens to authenticate as the SA

Common ACE exam question: "A developer with `roles/compute.instanceAdmin` cannot create a VM with a specific service account attached. Why?" Answer: they need `roles/iam.serviceAccountUser` on that service account.

---

## 5. IAM Conditions

IAM Conditions attach attribute-based logic to policy bindings. They require policy version 3.

### Common Condition Attributes

| Attribute | Example Use |
|---|---|
| `request.time` | Restrict access to specific hours or date ranges |
| `resource.name` | Grant access only to resources matching a name prefix |
| `resource.type` | Restrict grant to a specific GCP resource type |
| `resource.service` | Restrict grant to a specific GCP service |

### When to Use IAM Conditions (vs. Other Controls)

| Requirement | Correct Control |
|---|---|
| Time-based access window | IAM Condition on the policy binding |
| Resource-name-based restriction | IAM Condition on the policy binding |
| Prevent resource creation in unauthorized regions | Organization Policy constraint |
| Network-level API access restriction | VPC Service Controls |
| Temporary elevated access (break-glass) | IAM Condition with expiry date |

---

## 6. gcloud IAM Command Reference

### Role Commands

| Command | Description |
|---|---|
| `gcloud iam roles list` | List all available roles (predefined and custom) |
| `gcloud iam roles describe ROLE_ID` | Show a role's included permissions |
| `gcloud iam roles create ROLE_ID --project=P --permissions=p1,p2` | Create a custom role at project level |
| `gcloud iam roles copy --source=roles/storage.admin --dest=my.role --dest-project=P` | Copy a predefined role as a starting point for a custom role |

### Policy Binding Commands

| Command | Description |
|---|---|
| `gcloud projects get-iam-policy PROJECT_ID` | Retrieve the IAM policy for a project |
| `gcloud projects set-iam-policy PROJECT_ID policy.json` | Replace the IAM policy from a JSON file |
| `gcloud projects add-iam-policy-binding PROJECT_ID --member=TYPE:ID --role=ROLE` | Add a single binding |
| `gcloud projects remove-iam-policy-binding PROJECT_ID --member=TYPE:ID --role=ROLE` | Remove a single binding |

### Service Account Commands

| Command | Description |
|---|---|
| `gcloud iam service-accounts create NAME --display-name="LABEL"` | Create a user-managed service account |
| `gcloud iam service-accounts list` | List all service accounts in the active project |
| `gcloud iam service-accounts describe SA_EMAIL` | Show service account metadata |
| `gcloud iam service-accounts keys create KEY_FILE --iam-account=SA_EMAIL` | Generate and download a JSON key |
| `gcloud iam service-accounts keys list --iam-account=SA_EMAIL` | List keys for a service account |
| `gcloud iam service-accounts delete SA_EMAIL` | Delete a service account |

### Attaching a Service Account to a VM

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --service-account=my-sa@PROJECT_ID.iam.gserviceaccount.com \
  --scopes=cloud-platform
```

The `--scopes=cloud-platform` flag grants the VM access to all GCP APIs within the roles assigned to the service account. You can also specify individual API scopes for finer control.

---

## 7. Audit Logging

### Log Types

| Log Type | Always On | Covers | Default Enabled |
|---|---|---|---|
| Admin Activity | Yes | IAM changes, resource creation/deletion | Yes (cannot disable) |
| Data Access | No | Data reads, API calls | No (must enable per service) |
| System Event | Yes | GCP infrastructure events | Yes (cannot disable) |
| Policy Denied | Yes | Requests denied by VPC Service Controls | Yes (cannot disable) |

### Viewing Audit Logs

Navigate to Cloud Logging > Logs Explorer. Filter by log name:

```text
logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
```

Or use gcloud:

```bash
gcloud logging read 'logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com/activity"' \
  --limit=50 \
  --format=json
```

---

## 8. ACE Exam Tips

1. Basic roles fail least-privilege questions. Whenever a scenario asks for the minimum access required, eliminate `roles/viewer`, `roles/editor`, and `roles/owner` first and look for the predefined role that precisely fits the use case.

2. Service accounts are for machines, users are for humans. If a VM or automated job needs GCP API access, the answer is a service account attached to that resource — never embed a user's credentials.

3. The default Compute Engine service account has `roles/editor`. This is a security concern, not a feature. Best practice is to create purpose-built service accounts and disable defaults.

4. `serviceAccountUser` is required to attach a service account. A developer with `instanceAdmin` who cannot create a VM with a specific service account is missing `roles/iam.serviceAccountUser` on that service account.

5. Custom roles cannot be created at the Folder level. Only at Organization or Project level.

6. IAM Conditions require policy version 3. If you add a condition to a policy and the version is 1 or 2, the API will reject it.

7. IAM inheritance is additive. Effective permissions are the union of all policies from resource up to Organization. You cannot subtract a higher-level grant using a lower-level policy.

8. Admin Activity logs are always on and free. Data Access logs must be explicitly enabled and can generate large volumes that incur cost.

---

## 9. Study Checklist

Work through every item before taking the Module 02 quiz.

- [ ] State the five principal types and their IAM policy prefixes from memory
- [ ] Explain the difference between basic, predefined, and custom roles with a production example for each
- [ ] Describe the IAM policy JSON structure including the purpose of the etag field
- [ ] Explain why IAM inheritance is additive and give a scenario where this matters
- [ ] Describe the correct pattern for giving a Compute Engine VM access to Cloud Storage APIs
- [ ] List the two IAM roles related to service account usage and explain the difference
- [ ] Describe when you would use an IAM Condition versus an Organization Policy constraint
- [ ] Run `gcloud iam roles describe roles/storage.objectViewer` and review the permissions list
- [ ] Run `gcloud projects get-iam-policy` on your lab project and read the JSON output
- [ ] Create a service account using gcloud and grant it a predefined role
- [ ] Complete the Module 02 lab
- [ ] Take the Module 02 quiz
- [ ] Post your Module 02 discussion response

---

End of Reading Guide — Module 02

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
