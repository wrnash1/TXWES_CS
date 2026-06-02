# Video Script — Module 02, Part 1

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: IAM — Principals, Roles, and the Policy Model

### Estimated Duration: 13–15 minutes

---

## Introduction

Welcome to Module 02. I'm Professor Nash, and today we are going deep into Identity and Access Management — IAM. If Module 01 was about where things live in GCP, Module 02 is about who can touch them. IAM is arguably the most important topic in this entire course, and it is the most heavily tested domain on the Google Cloud Associate Cloud Engineer exam. Get this module right and you will carry that advantage through every other module.

By the end of Part 1 you will understand the principal model — who can be granted access — and the complete role system — what access they can have. In Part 2 we will cover service accounts in depth, IAM conditions, audit logging, and best-practice patterns.

---

## Section 1: The IAM Model

**[SHOW SLIDE: Three-column diagram labeled "Who (Principal)", "What (Role)", "Where (Resource)"]**

IAM answers one question: who can do what on which resource? Every IAM policy binding has three components:

- A principal — the identity being granted access
- A role — the collection of permissions being granted
- A resource — the GCP resource the policy is attached to

Let's work through each component.

---

## Section 2: Principals

**[SHOW SLIDE: List of principal types with their identifier prefixes]**

A principal is any identity that can be granted access in GCP. There are five principal types you must know for the ACE exam.

The first is a Google Account — a specific individual identified by their email address. Example: `william.nash@txwes.edu`. This represents a human user. In IAM policy JSON, a Google Account is prefixed with `user:`.

The second is a Service Account — a special account used by applications and workloads, not by humans. Service accounts have email-format identifiers like `my-app@my-project.iam.gserviceaccount.com`. In IAM policy JSON, service accounts are prefixed with `serviceAccount:`. We will cover service accounts in detail in Part 2.

The third is a Google Group — a named collection of Google Accounts and Service Accounts. When you grant a role to a group, all current and future members of that group inherit that role automatically. This is the recommended way to manage access for teams because you add and remove individuals from the group rather than modifying IAM policies directly.

The fourth is a Google Workspace or Cloud Identity domain — all users in a specific domain such as `txwes.edu`. In IAM policy JSON this is prefixed with `domain:`. Granting a role to a domain grants it to every user in that domain. Use this carefully.

The fifth special identifiers are `allAuthenticatedUsers` and `allUsers`. The `allAuthenticatedUsers` identifier means any Google account that is authenticated — essentially any signed-in Google user on the internet. The `allUsers` identifier means completely unauthenticated public access — any request, from anyone, with no sign-in required.

**[PAUSE — Professor on camera]**

The distinction between `allAuthenticatedUsers` and `allUsers` is a classic ACE exam trap. `allUsers` means the entire public internet with no login required. `allAuthenticatedUsers` means anyone who signs in with any Google account. Neither is appropriate for sensitive or internal data. The ACE exam will present scenarios asking which of these identifiers makes a Cloud Storage bucket or an API endpoint publicly accessible — and the answer is `allUsers` for truly public, `allAuthenticatedUsers` for "any Google account."

---

## Section 3: The Three Categories of Roles

**[SHOW SLIDE: Three-tier role hierarchy — Basic, Predefined, Custom]**

Roles are bundles of permissions. A permission is a single atomic action, like `compute.instances.create` or `storage.objects.get`. You never grant individual permissions directly to principals — you grant roles, which contain permissions.

GCP has three categories of roles.

### Basic Roles

**[SHOW SLIDE: Basic roles table — Viewer, Editor, Owner with a one-line summary of each]**

Basic roles — also called primitive roles — are the original, coarse-grained roles that predate the modern IAM system. There are three:

`roles/viewer` grants read-only access to all resources in the project. The holder can view configuration, list resources, and read data, but cannot create, modify, or delete anything.

`roles/editor` grants read and write access to most resources. The holder can create, modify, and delete most resources but cannot manage IAM policies themselves.

`roles/owner` grants full control including IAM policy management and billing. The holder can add and remove IAM bindings, link billing accounts, and delete the project itself.

Basic roles are convenient but dangerous. Granting `roles/editor` to someone gives them write access to every service in the project — Compute Engine, Cloud Storage, Cloud SQL, BigQuery, Pub/Sub — whether they need that access or not. For production environments, basic roles violate the principle of least privilege. The ACE exam will frequently present scenarios where basic roles are the wrong answer precisely because they are too broad.

### Predefined Roles

**[SHOW SLIDE: Table of predefined roles organized by service]**

Predefined roles are purpose-built roles created and maintained by Google for specific services. They follow the naming pattern `roles/SERVICE.ROLENAME`. Here are the most important ones for the ACE exam:

For Compute Engine:

- `roles/compute.instanceAdmin.v1` — manage VM instances: start, stop, create, delete
- `roles/compute.viewer` — view Compute Engine resources with no write access
- `roles/compute.networkAdmin` — manage network resources: VPCs, subnets, firewalls

For Cloud Storage:

- `roles/storage.objectAdmin` — create, read, update, delete objects in any bucket in the project
- `roles/storage.objectViewer` — read objects and list bucket contents
- `roles/storage.admin` — full control including bucket creation and deletion

For IAM itself:

- `roles/iam.serviceAccountUser` — attach service accounts to resources (impersonate them)
- `roles/iam.serviceAccountAdmin` — create and manage service accounts
- `roles/iam.securityReviewer` — view IAM policies across the project (read-only)

For Cloud SQL:

- `roles/cloudsql.client` — connect to Cloud SQL instances but not administer them
- `roles/cloudsql.admin` — full Cloud SQL administration including instance creation

Predefined roles are automatically updated by Google when new GCP features introduce new permissions. If you hold `roles/compute.instanceAdmin.v1` and Google releases a new Compute Engine feature with new permissions, your role may be updated to include those permissions automatically.

### Custom Roles

**[SHOW CONSOLE: Navigate to IAM and Admin > Roles > Create Role]**

Custom roles let you create a role with exactly the permissions you specify — no more, no less. Custom roles can be created at the Organization level or at the Project level. They cannot be created at the Folder level — this is an ACE exam detail worth memorizing.

Custom roles are the gold standard for least-privilege access. If an application only needs to read Pub/Sub messages and write to BigQuery, you can create a custom role with exactly those two permissions.

The maintenance trade-off: predefined roles are updated automatically by Google. Custom roles are NOT automatically updated. When Google adds new permissions for new features, you must manually add them to your custom roles if your workloads need them.

---

## Section 4: IAM Policy Structure

**[SHOW SLIDE: IAM policy JSON with bindings array highlighted]**

An IAM policy is a JSON document attached to a resource. It contains a list of bindings, a version number, and an etag. Here is what a minimal IAM policy looks like:

```json
{
  "bindings": [
    {
      "role": "roles/storage.objectViewer",
      "members": [
        "user:student@txwes.edu",
        "group:analysts@txwes.edu"
      ]
    },
    {
      "role": "roles/storage.admin",
      "members": [
        "serviceAccount:backup@my-project.iam.gserviceaccount.com"
      ]
    }
  ],
  "etag": "BwX1fakeEtag==",
  "version": 1
}
```

The `etag` field is a concurrency control mechanism. When you read a policy and then write it back, GCP checks that the etag you submit matches the current server-side etag. If another administrator changed the policy between your read and your write, the etags will not match and GCP will reject your write — preventing accidental overwrites. This is especially important in automated scripts and Terraform configurations.

---

## Section 5: The Principle of Least Privilege

**[SHOW SLIDE: Venn diagram — "permissions needed" circle and "permissions granted" circle with small overlap labeled "correct" and large overlap labeled "overprivileged"]**

The principle of least privilege is the single most important IAM design principle. Every principal should be granted only the minimum permissions needed to perform their job — nothing more.

In practice this means:

- Prefer predefined roles over basic roles for any production use
- Create custom roles when no predefined role is a precise fit
- Grant roles at the most specific resource level possible — a storage bucket grant instead of a project grant when only one bucket is involved
- Avoid granting `roles/owner` to service accounts
- Avoid granting `roles/editor` to human users in production
- Prefer granting roles to Google Groups rather than individual users, so that offboarding a user means removing them from the group rather than auditing every IAM binding across every project

The ACE exam presents scenarios and asks which IAM configuration is most appropriate. The correct answer is almost always the option that grants the narrowest predefined role at the most specific level in the hierarchy that still accomplishes the task.

---

## Closing — Part 1

To summarize Part 1: IAM answers who can do what on which resource. Principals are the identities — Google Accounts, Service Accounts, Groups, domains, or public identifiers. Roles contain permissions — basic roles are coarse-grained, predefined roles are service-specific, and custom roles are tailored to exact needs. IAM policies are JSON documents with bindings that pair roles to members. The etag prevents concurrent write conflicts. Always apply least privilege.

In Part 2 we will cover service accounts, IAM conditions, workload identity federation, and the gcloud commands for managing IAM policies.

---

End of Part 1 — Module 02

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
