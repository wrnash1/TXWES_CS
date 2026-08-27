# Reading Guide: Module 02 — IAM and Access Control in GCP

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This reading guide covers Google Cloud Identity and Access Management (IAM) in
depth. IAM is the security foundation of every GCP deployment and one of the
most heavily tested domains on the ACE exam.

**Estimated Reading Time:** 50–60 minutes

---

## Section 1 — IAM Concepts

### 1.1 The IAM Model

Cloud IAM implements the principle of least privilege through a three-part model:

- **Principal** — Who is requesting access
- **Role** — What actions are permitted
- **Resource** — Which GCP resource is being accessed

An IAM **policy** binds principals to roles on a resource. A policy on a project
applies to all resources within that project.

### 1.2 Principals

GCP recognizes several principal types, each identified by a prefix:

| Principal type | Prefix | Example |
|---|---|---|
| Google Account | `user:` | `user:alice@example.com` |
| Service Account | `serviceAccount:` | `serviceAccount:app@project.iam.gserviceaccount.com` |
| Google Group | `group:` | `group:devs@company.com` |
| Google Workspace domain | `domain:` | `domain:company.com` |
| All authenticated users | `allAuthenticatedUsers` | (no prefix) |
| All users (public) | `allUsers` | (no prefix) |

Using `allUsers` grants public, unauthenticated access. This is appropriate for
public websites or open data sets but is a security misconfiguration when applied
to sensitive resources. The ACE exam includes scenarios involving unintended
public access caused by `allUsers` bindings.

### 1.3 Permissions

Permissions are the atomic units of access in IAM. Each permission allows a
single action on a specific resource type.

Permission format:

```text
SERVICE.RESOURCE_TYPE.ACTION
```

Examples:

- `compute.instances.start` — Start a Compute Engine VM
- `storage.objects.create` — Upload an object to Cloud Storage
- `bigquery.tables.getData` — Read data from a BigQuery table
- `iam.serviceAccounts.actAs` — Impersonate a service account

Permissions cannot be assigned directly to principals. They must be bundled into
roles, which are then assigned to principals via policy bindings.

---

## Section 2 — IAM Role Types

### 2.1 Primitive (Basic) Roles

Primitive roles are coarse-grained roles that predate Cloud IAM:

| Role | Description |
|---|---|
| `roles/owner` | Full access to all resources; can manage billing and IAM |
| `roles/editor` | Create and modify all resources; cannot manage IAM or billing |
| `roles/viewer` | Read-only access to all resources |

Primitive roles violate the principle of least privilege. Assigning `roles/editor`
at the project level grants modification access to every service in that project.
Google and the ACE exam recommend against using primitive roles in production.

### 2.2 Predefined Roles

Predefined roles are curated by Google per service and job function. They follow
least privilege by granting only the permissions required for a specific task.

#### Key predefined roles for the ACE exam

Compute Engine:

- `roles/compute.admin` — Full control of all Compute Engine resources
- `roles/compute.instanceAdmin.v1` — Create, modify, and delete VM instances
- `roles/compute.networkAdmin` — Manage networks, subnets, and firewalls
- `roles/compute.securityAdmin` — Manage firewall rules and SSL certificates
- `roles/compute.viewer` — Read-only access to Compute Engine

Cloud Storage:

- `roles/storage.admin` — Full control of buckets and objects
- `roles/storage.objectAdmin` — Full control of objects; cannot manage buckets
- `roles/storage.objectCreator` — Upload objects; cannot read or delete
- `roles/storage.objectViewer` — Read objects and list buckets
- `roles/storage.legacyBucketReader` — Read bucket metadata and list objects

IAM:

- `roles/iam.securityAdmin` — Manage IAM policies; view all resources
- `roles/iam.securityReviewer` — View IAM policies; no modification
- `roles/iam.serviceAccountAdmin` — Create and manage service accounts
- `roles/iam.serviceAccountUser` — Attach service accounts to resources
  (equivalent to `iam.serviceAccounts.actAs`)

Kubernetes Engine:

- `roles/container.admin` — Full control of GKE clusters and workloads
- `roles/container.developer` — Deploy and manage Kubernetes workloads
- `roles/container.viewer` — Read-only access to GKE resources

### 2.3 Custom Roles

Custom roles allow you to define the exact set of permissions needed for a
specific use case.

#### Creating custom roles

Custom roles can be defined using:

- The Cloud Console (IAM & Admin > Roles > Create Role)
- A YAML definition file with gcloud

Example YAML definition:

```yaml
title: Custom Storage Read Write
description: Read and write objects; cannot delete or manage buckets
stage: GA
includedPermissions:
  - storage.objects.get
  - storage.objects.create
  - storage.objects.update
  - storage.buckets.list
```

Deploy using:

```bash
gcloud iam roles create customStorageRW \
  --project=PROJECT_ID \
  --file=role.yaml
```

#### Custom role restrictions

Not all permissions can be included in custom roles. Some permissions are
reserved for primitive roles or are otherwise non-bindable. The Console and
gcloud will indicate when a permission cannot be used in a custom role.

---

## Section 3 — IAM Policies

### 3.1 Policy Structure

An IAM policy is stored as a JSON document. It contains:

- `version` — Policy schema version (currently 1, 2, or 3; version 3 required
  for conditions)
- `bindings` — Array of role-principal bindings
- `etag` — Concurrency control token; used to prevent race conditions when
  updating policies
- `auditConfigs` — Optional; configures audit logging

Example policy:

```json
{
  "version": 3,
  "bindings": [
    {
      "role": "roles/storage.objectViewer",
      "members": [
        "user:bob@example.com"
      ],
      "condition": {
        "title": "Expires 2026-12-31",
        "expression": "request.time < timestamp('2026-12-31T00:00:00Z')"
      }
    }
  ],
  "etag": "BwXmhg2..."
}
```

### 3.2 IAM Conditions

IAM Conditions allow attribute-based conditions on role bindings. Version 3
policies are required when conditions are used.

Condition expression language: Common Expression Language (CEL)

Common condition attributes:

| Attribute | Example use |
|---|---|
| `request.time` | Grant access only before a deadline |
| `resource.type` | Grant role only on a specific resource type |
| `resource.name` | Grant role only on resources matching a name prefix |
| `request.auth.access_levels` | Require access levels from Access Context Manager |

### 3.3 Policy Etags and Concurrency

The `etag` in an IAM policy is a fingerprint of the current policy version.
When you update a policy, GCP checks that the etag in your request matches the
current stored etag. If they differ, the update is rejected, preventing you
from overwriting changes made by another concurrent process.

Best practice: Always fetch the current policy (including its etag) immediately
before modifying and re-applying it.

---

## Section 4 — Service Accounts

### 4.1 Service Account Identity

A service account is both a principal (can be granted roles) and a resource
(can be administered by humans with the right permissions).

Service account email format:

```text
NAME@PROJECT_ID.iam.gserviceaccount.com
```

### 4.2 Attaching Service Accounts to Resources

A VM or other GCP resource can be associated with a service account. When the
code running on that resource calls GCP APIs, it automatically uses the attached
service account's identity — no key file needed.

Example: Attaching a service account when creating a Compute Engine VM:

```bash
gcloud compute instances create my-vm \
  --service-account=my-sa@PROJECT_ID.iam.gserviceaccount.com \
  --scopes=cloud-platform \
  --zone=us-central1-a
```

### 4.3 Service Account Impersonation

A user or service account can impersonate another service account if they have
the `iam.serviceAccounts.actAs` permission on the target service account.

```bash
# Generate a short-lived token for a service account
gcloud auth print-access-token \
  --impersonate-service-account=target-sa@PROJECT_ID.iam.gserviceaccount.com
```

### 4.4 Service Account Key Best Practices

If a key file is absolutely required:

- Store keys in Secret Manager, not in source code or environment variables
- Rotate keys regularly (90-day maximum recommended)
- Set an Organization Policy constraint
  `constraints/iam.disableServiceAccountKeyCreation` to block key creation
  organization-wide
- Enable the Service Account Key Creation audit log

---

## Section 5 — Workload Identity Federation

### 5.1 Overview

Workload Identity Federation replaces service account keys for workloads running
outside GCP. It enables external identities (AWS, Azure, GitHub, etc.) to
exchange their native credentials for Google access tokens.

### 5.2 Components

- **Workload Identity Pool**: Container for external identity providers
- **Workload Identity Pool Provider**: Configuration linking to a specific IdP
  (AWS, OIDC, SAML)
- **Attribute mapping**: Maps external token claims to Google attributes
- **Attribute conditions**: Restrict which external identities can federate

### 5.3 Setup with GitHub Actions

```bash
# Create a Workload Identity Pool
gcloud iam workload-identity-pools create github-pool \
  --location=global \
  --display-name="GitHub Actions Pool"

# Create a provider for GitHub OIDC
gcloud iam workload-identity-pools providers create-oidc github-provider \
  --location=global \
  --workload-identity-pool=github-pool \
  --issuer-uri="https://token.actions.githubusercontent.com" \
  --attribute-mapping="google.subject=assertion.sub,attribute.repository=assertion.repository"

# Allow the GitHub repo to impersonate a service account
gcloud iam service-accounts add-iam-policy-binding \
  my-sa@PROJECT_ID.iam.gserviceaccount.com \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/github-pool/attribute.repository/my-org/my-repo"
```

---

## Section 6 — Cloud Audit Logs

### 6.1 Log Types

| Log Type | Always Enabled | Charges Apply | Records |
|---|---|---|---|
| Admin Activity | Yes | No | Config and metadata changes |
| Data Access | No | Yes | Resource data reads/writes |
| System Event | Yes | No | Google-generated system events |
| Policy Denied | Yes | No | Access denied by policy |

### 6.2 Enabling Data Access Logs

```bash
# Get current audit config
gcloud projects get-iam-policy PROJECT_ID --format=json

# Enable Data Access logging for Cloud Storage via policy file
# Add auditConfigs section to the policy JSON, then apply:
gcloud projects set-iam-policy PROJECT_ID policy-with-audit.json
```

### 6.3 Querying Audit Logs

```bash
# View admin activity logs for a project
gcloud logging read \
  'logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"' \
  --limit=20

# Filter for IAM policy change events
gcloud logging read \
  'logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
   AND protoPayload.methodName="SetIamPolicy"' \
  --limit=10
```

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| Principal | An identity that can be granted access (user, group, SA, domain) |
| Role | A named collection of permissions |
| Permission | Atomic unit granting one action on one resource type |
| IAM Policy | JSON document binding principals to roles on a resource |
| Primitive role | Coarse-grained legacy role (owner/editor/viewer); avoid in production |
| Predefined role | Google-curated role for a specific service and function |
| Custom role | User-defined role with exactly specified permissions |
| Service account | Non-human GCP identity for applications and automated workloads |
| IAM Condition | CEL expression adding attribute-based constraints to a role binding |
| WIF | Workload Identity Federation — keyless auth for external workloads |
| Audit log | Record of who did what and when on GCP resources |
| etag | Concurrency token in IAM policies to prevent race conditions |

---

## ACE Exam Focus Areas — Module 02

- Identify the three IAM role types and when to use each.
- Recommend the minimum role for a described task (least privilege).
- Explain why primitive roles are discouraged.
- Describe how to authenticate an external workload without a service account key.
- Distinguish between Admin Activity logs (always on) and Data Access logs (opt-in).
- Explain that IAM policies are additive — permissions cannot be reduced at
  a lower hierarchy level.
- Describe the dual nature of service accounts (principal and resource).

---

## Further Reading

- Cloud IAM overview: cloud.google.com/iam/docs/overview
- Predefined roles reference: cloud.google.com/iam/docs/understanding-roles
- Workload Identity Federation: cloud.google.com/iam/docs/workload-identity-federation
- Cloud Audit Logs: cloud.google.com/logging/docs/audit
- IAM best practices: cloud.google.com/iam/docs/using-iam-securely

## 9. Supplemental Resources

**1. Google Cloud Documentation — Understanding IAM Roles**
<https://cloud.google.com/iam/docs/understanding-roles>
Comprehensive reference for all predefined roles across every GCP service,
including the exact permission lists for each role. Essential for ACE exam
preparation on least-privilege questions.

**2. Google Cloud Skills Boost — Cloud IAM: Qwik Start**
<https://www.cloudskillsboost.google/focuses/44159>
Hands-on lab walking through IAM policy creation, role assignment, and
service account configuration in a live GCP environment. Free with a Skills
Boost trial or subscription.

**3. Google Cloud Architecture Center — IAM Best Practices**
<https://cloud.google.com/architecture/framework/security/access-control>
Official best practice guidance covering service account security, Workload
Identity Federation, and organizational IAM governance patterns from Google's
architecture team.
