# Video Script: Module 02 — IAM and Access Control in GCP (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Introduction (1 minute)

Welcome to Module 02. This module covers Identity and Access Management — IAM —
which is one of the most heavily tested topic areas on the Google Cloud Associate
Cloud Engineer exam.

In Part 1 we cover the IAM conceptual model: who can do what on which resource.
We look at the three types of IAM roles, how policies work, service accounts,
and the newer features like IAM Conditions and Workload Identity Federation.

Pay close attention. IAM questions make up a significant portion of the ACE exam.

---

## Segment 2 — IAM Fundamentals (4 minutes)

### The IAM Model

Google Cloud IAM answers one question: who can do what on which resource?

- **Who** — a principal (a person, a group, a service account, or a domain)
- **Can do what** — a role (a collection of permissions)
- **On which resource** — a GCP resource (project, bucket, VM, etc.)

An IAM policy is the binding that ties a principal to a role on a resource.

### Principals

GCP recognizes the following principal types:

- **Google Account** — An individual user's Google identity (`user:alice@example.com`)
- **Service Account** — A non-human identity used by applications and VMs
  (`serviceAccount:myapp@project.iam.gserviceaccount.com`)
- **Google Group** — A named collection of Google Accounts and service accounts
  (`group:team@example.com`)
- **Google Workspace Domain** — All users in a Google Workspace domain
  (`domain:example.com`)
- **allAuthenticatedUsers** — Any authenticated Google account
- **allUsers** — Anyone on the internet, including unauthenticated users

**ACE Exam Tip:** `allUsers` grants public access. Never use it on sensitive
resources. The ACE exam often includes questions about unintended public access.

### Permissions

A permission is the most granular unit in IAM. Permissions follow this format:

```text
service.resource.verb
```

Examples:

- `compute.instances.create` — permission to create Compute Engine VMs
- `storage.buckets.delete` — permission to delete Cloud Storage buckets
- `iam.serviceAccounts.actAs` — permission to act as a service account

Permissions are never granted directly to principals. They are grouped into roles,
and roles are granted to principals.

---

## Segment 3 — IAM Role Types (5 minutes)

GCP has three categories of IAM roles.

### Primitive Roles (Basic Roles)

Primitive roles predate IAM and were the original access control mechanism.
There are three primitive roles:

- `roles/owner` — Full control of all resources plus billing management
- `roles/editor` — Create and modify all resources (no billing management)
- `roles/viewer` — Read-only access to all resources

**Why to avoid primitive roles:** They are extremely broad. Granting someone
`roles/editor` on a project gives them the ability to modify every resource in
that project. The ACE exam and GCP best practices strongly recommend using
predefined or custom roles instead.

### Predefined Roles

Predefined roles are curated by Google for specific services and job functions.
They bundle the exact permissions needed for a particular task, following the
principle of least privilege.

Examples:

- `roles/compute.instanceAdmin.v1` — Full control of Compute Engine instances
- `roles/compute.viewer` — Read-only access to Compute Engine
- `roles/storage.admin` — Full control of Cloud Storage
- `roles/storage.objectViewer` — Read objects in Cloud Storage
- `roles/container.developer` — Deploy and manage workloads in GKE
- `roles/logging.viewer` — View log entries in Cloud Logging
- `roles/iam.securityReviewer` — View IAM policies across all resources

There are hundreds of predefined roles. For the ACE exam, focus on roles for
the services covered in this course: Compute Engine, Cloud Storage, GKE,
Cloud Run, and IAM itself.

### Custom Roles

Custom roles allow you to define exactly which permissions to bundle. They are
used when no predefined role fits the least-privilege requirement.

Custom roles can be created at two levels:

- **Project level** — Applicable only within that project
- **Organization level** — Applicable across the organization

**ACE Exam Tip:** Custom roles cannot include all permissions. Some permissions
are restricted to specific roles (e.g., primitive roles) and cannot be added to
custom roles. When a question asks how to grant exactly the permissions needed
with no extras, the answer is a custom role.

---

## Segment 4 — IAM Policies (3 minutes)

### Policy Structure

An IAM policy is a JSON document that binds principals to roles on a resource.
Each binding specifies one role and one or more principals.

```json
{
  "bindings": [
    {
      "role": "roles/storage.objectViewer",
      "members": [
        "user:alice@example.com",
        "group:devs@example.com"
      ]
    },
    {
      "role": "roles/compute.instanceAdmin.v1",
      "members": [
        "serviceAccount:myapp@project.iam.gserviceaccount.com"
      ]
    }
  ],
  "etag": "BwXmhg2..."
}
```

### Policy Inheritance

As covered in Module 01, IAM policies are inherited downward through the resource
hierarchy. A policy set at the Organization level is effective at all projects
and resources below it.

### IAM Conditions

IAM Conditions allow you to add attribute-based access control on top of role
bindings. Common condition attributes include:

- **Resource type** — Apply the role only to specific resource types
- **Resource name** — Apply the role only to resources matching a name pattern
- **Date/time** — Grant access only during a specific time window
- **IP address** — Restrict access to specific IP ranges

Example use case: Grant a contractor `roles/editor` only until a specific
project end date. After the date passes, the binding is automatically ineffective.

**ACE Exam Tip:** IAM Conditions are evaluated at policy enforcement time.
They do not delete or modify bindings after expiration — the binding persists
but its condition is no longer satisfied, so access is denied.

---

## Segment 5 — Service Accounts (2 minutes)

### What is a Service Account?

A service account is a special type of Google account intended to represent
a non-human user — typically an application, VM, or automated process.

Service accounts have two roles in IAM:

1. **As a principal** — You grant roles to a service account, giving it
   permissions to access GCP resources.
2. **As a resource** — You grant the `iam.serviceAccounts.actAs` permission
   to users or other service accounts, controlling who can use the service
   account.

### Types of Service Accounts

- **User-managed service accounts** — Created by you in your project.
  Format: `NAME@PROJECT_ID.iam.gserviceaccount.com`
- **Default service accounts** — Automatically created when you enable certain
  APIs (e.g., App Engine, Compute Engine). These have broad permissions by
  default — a security concern.
- **Google-managed service accounts** — Used internally by Google services.
  You generally do not interact with these.

### Service Account Keys

Service accounts can authenticate using two methods:

- **Short-lived credentials** (recommended) — Access tokens generated by the
  metadata server or Workload Identity Federation
- **Service account keys** (avoid when possible) — Long-lived JSON key files
  that can be downloaded

**ACE Exam Tip:** GCP best practice strongly discourages creating and
downloading service account keys. Keys are a security risk if mishandled.
Use Workload Identity Federation or attached service accounts instead.

---

## Summary — Part 1

In Part 1 we covered:

- The IAM model: who can do what on which resource
- Principal types: Google Accounts, service accounts, groups, domains
- The three role categories: primitive, predefined, and custom
- IAM policy structure and inheritance
- IAM Conditions for attribute-based access
- Service accounts: as principals and as resources

In Part 2 we will look at Workload Identity Federation, Cloud Audit Logs, and
walk through IAM configuration in the Cloud Console and with gcloud.

See you in Part 2.

---

End of Part 1 — Module 02

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/iam/docs
