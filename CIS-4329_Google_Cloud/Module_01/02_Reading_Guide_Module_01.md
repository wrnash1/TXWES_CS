# Reading Guide — Module 01

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: GCP Overview — Regions, Zones, and Console Navigation

### Certification Target: Google Cloud Associate Cloud Engineer

---

## Introduction

This reading guide accompanies the Module 01 video lectures and lab. Use it as your primary study reference before attempting the quiz. Module 01 establishes the foundational vocabulary and mental model for every topic that follows in this course. The Google Cloud Associate Cloud Engineer exam dedicates a significant portion of its questions to resource hierarchy, IAM inheritance, and infrastructure geography — all covered here.

Read every section carefully. The ACE exam tips are drawn from official exam guide objectives and from patterns observed across real certification exams.

---

## 1. GCP Global Infrastructure

### Regions

A region is a specific geographic location where Google operates clusters of data centers. Each region is identified by a short code. Examples:

- `us-central1` — Council Bluffs, Iowa, USA
- `us-east1` — Moncks Corner, South Carolina, USA
- `europe-west1` — St. Ghislain, Belgium
- `asia-east1` — Changhua County, Taiwan
- `australia-southeast1` — Sydney, Australia
- `southamerica-east1` — Osasco, São Paulo, Brazil

Regions are engineered to be fault-isolated from one another. A failure in one region does not affect services running in another region. When you choose a region, consider three factors:

1. Latency — choose the region geographically closest to your users
2. Compliance — some industries require data to remain within specific countries or jurisdictions
3. Service availability — not every GCP service is available in every region

### Zones

A zone is an isolated deployment area within a region. Zone names append a letter suffix to the region name: `us-central1-a`, `us-central1-b`, `us-central1-c`, `us-central1-f`. Zones within the same region share low-latency, high-bandwidth internal networking but have independent power feeds, cooling systems, and network paths. A hardware failure in zone `us-central1-a` does not affect zone `us-central1-b`.

### Deployment Resilience Comparison

| Deployment Type | Survives Zone Failure | Survives Region Failure | Relative Cost |
|---|---|---|---|
| Single Zone | No | No | Lowest |
| Multi-Zone, Single Region | Yes | No | Low |
| Multi-Region | Yes | Yes | Highest |

The ACE exam frequently presents scenarios and asks which deployment strategy meets the stated availability requirement at the lowest cost. Multi-zone, single region is the correct answer for most standard enterprise workloads. Multi-region is only warranted when the scenario explicitly requires surviving a full regional outage.

### Network Tier

GCP offers two network service tiers:

- **Premium Tier** — traffic travels over Google's private backbone as much as possible before entering the public internet. Lower latency, higher reliability. Default for most services.
- **Standard Tier** — traffic enters and exits the public internet sooner, similar to a typical ISP route. Lower cost, acceptable for non-latency-sensitive workloads.

---

## 2. Resource Hierarchy

### Four-Level Structure

GCP organizes all resources in a strict parent-child hierarchy with four levels:

```text
Organization
  └── Folder (optional, nestable up to 10 levels)
        └── Project
              └── Resource (VMs, buckets, databases, etc.)
```

Every resource must belong to exactly one Project. Every Project can optionally belong to one Folder. Every Folder ultimately rolls up to the Organization.

### Organization Node

The Organization node is the root of your GCP environment. It maps to a Google Workspace or Cloud Identity domain. Key facts:

- Created automatically when a Google Workspace or Cloud Identity account is established
- Acts as the root IAM boundary for all resources in your domain
- The `roles/resourcemanager.organizationAdmin` role grants full control over the Organization
- Personal Gmail accounts do not have an Organization node

### Folders

Folders are optional grouping containers that sit between the Organization and Projects. You can nest folders up to 10 levels deep. Common uses:

- Group by department: `Engineering`, `Finance`, `Operations`
- Group by environment: `Production`, `Development`, `Staging`
- Group by geographic subsidiary

Folders are especially useful for applying IAM policies and Organization Policy constraints to a subset of projects without affecting the rest of the organization.

### Projects

Projects are the core unit of organization. Every interaction with GCP resources happens within a project context. Key facts:

- Each Project has a **Project ID** (globally unique string, immutable after creation, chosen by you or auto-generated)
- Each Project has a **Project Number** (globally unique integer, assigned by Google, immutable)
- Each Project has a **Project Name** (display label, not unique, mutable)
- A Project must be linked to exactly one active Billing Account to use paid services
- Projects can be deleted but enter a 30-day pending deletion period before permanent removal

### Project Identifier Comparison

| Identifier | Example | Unique | Mutable | Assigned By |
|---|---|---|---|---|
| Project ID | `my-web-app-prod-2024` | Globally | No | User or auto-generated |
| Project Number | `123456789012` | Globally | No | Google |
| Project Name | `My Web App Production` | No | Yes | User |

---

## 3. IAM Policy Inheritance

### How Inheritance Works

IAM policies set at any level in the hierarchy automatically apply to all child levels. A role granted at the Organization level grants that role on every Folder, Project, and Resource in the organization. A role granted at a Folder level grants that role on every Project and Resource inside that folder.

This inheritance is additive only. You cannot deny or remove a permission at a lower level that was granted at a higher level. The effective policy for any resource is the union of all policies on that resource plus all policies on every ancestor in the hierarchy.

### Inheritance Direction

```text
Organization policy  -->  applies to all Folders, Projects, Resources below
Folder policy        -->  applies to all child Folders, Projects, Resources below
Project policy       -->  applies to all Resources in the project
Resource policy      -->  applies to that resource only
```

### Common Exam Scenario

A question states: "A user has `roles/editor` granted at the Organization level. An administrator wants to restrict this user to `roles/viewer` on a specific project. What should the administrator do?" The answer is: remove the `roles/editor` grant at the Organization level, because a project-level restriction cannot override an organization-level grant. IAM does not support deny rules at the resource/project level for inherited organization permissions (note: IAM Deny policies, introduced later, are a separate advanced feature).

---

## 4. Billing Architecture

### Billing Account Structure

A Billing Account is a GCP resource that stores a payment method and receives charges for GCP usage. Key structural facts:

- A Billing Account belongs to an Organization (in enterprise setups) or to an individual Google account
- A Billing Account can be linked to one or more Projects
- Each Project can be linked to exactly one Billing Account at a time
- Billing Accounts are not directly linked to Folders or Resources — only to Projects

### Billing Roles

| Role | What It Allows |
|---|---|
| `roles/billing.admin` | Full control of billing account: link/unlink projects, manage payment methods |
| `roles/billing.user` | Link projects to a billing account (does not see payment methods) |
| `roles/billing.viewer` | View billing account data and usage reports |
| `roles/billing.projectManager` | Link/unlink billing accounts on projects you own |

### Budget Alerts

Budget alerts are configured under Cloud Billing > Budgets and Alerts. You define:

- Scope: the entire billing account, or specific projects
- Budget amount: a fixed dollar amount per month
- Alert thresholds: percentage triggers (50%, 90%, 100%, or custom)
- Notification channels: email to billing admins, or a Pub/Sub topic

Critical ACE exam fact: budget alerts are notifications only. They do not cap, suspend, limit, or delete any resource. This distinction is tested on virtually every ACE exam.

---

## 5. Organization Policies

Organization Policies are constraints that control which GCP actions are permitted, independent of IAM permissions. While IAM answers "who can do X", Organization Policies answer "is X allowed at all".

### Constraint Types

| Type | Description |
|---|---|
| Boolean constraint | On/off toggle (e.g., disable serial port access) |
| List constraint | Allow or deny a list of values (e.g., allowed resource regions) |

### Frequently Tested Constraints

| Constraint | Effect |
|---|---|
| `constraints/compute.disableSerialPortAccess` | Blocks interactive serial console on VMs |
| `constraints/compute.requireOsLogin` | Enforces OS Login for VM SSH access |
| `constraints/iam.disableServiceAccountKeyCreation` | Prevents downloadable service account keys |
| `constraints/gcp.resourceLocations` | Restricts resource creation to approved regions |
| `constraints/compute.vmExternalIpAccess` | Controls which VMs can have external IP addresses |
| `constraints/iam.allowedPolicyMemberDomains` | Restricts IAM grants to specific domains |

Policies are set using the gcloud resource-manager CLI or in the Console under IAM and Admin > Organization Policies.

---

## 6. Google Cloud Console Navigation

### Key Console Sections

| Section | Path | Purpose |
|---|---|---|
| Home Dashboard | console.cloud.google.com | Overview widgets, recent resources, billing summary |
| Navigation Menu | Hamburger icon (top-left) | Browse all GCP services by category |
| Project Selector | Top center dropdown | Switch between projects |
| Cloud Shell | Terminal icon (top-right) | Browser-based CLI environment |
| IAM and Admin | Navigation > IAM & Admin | Manage roles, service accounts, audit logs |
| Billing | Navigation > Billing | Manage billing accounts, budgets, reports |
| APIs and Services | Navigation > APIs & Services | Enable/disable GCP APIs, manage credentials |

### Cloud Shell Key Facts

| Property | Value |
|---|---|
| VM type | Small Debian Linux VM (e2-micro class) |
| Cost | Free |
| Persistent storage | 5 GB home directory in Cloud Storage |
| VM lifespan | Ephemeral — recycled after 20 min inactivity |
| Pre-installed tools | gcloud, kubectl, Docker, Terraform, Python, Node.js, Java, Go |
| Authentication | Auto-authenticated to your Google account |
| Web preview | Available on port 8080 (and others) |

---

## 7. gcloud CLI Reference

### Configuration Commands

| Command | Description |
|---|---|
| `gcloud init` | Interactive setup: authenticate, choose project and region |
| `gcloud config list` | Show current active configuration (project, account, region, zone) |
| `gcloud config set project PROJECT_ID` | Set active project |
| `gcloud config set compute/region REGION` | Set default compute region |
| `gcloud config set compute/zone ZONE` | Set default compute zone |
| `gcloud config get-value project` | Print only the active project ID |
| `gcloud config configurations create NAME` | Create a new named configuration |
| `gcloud config configurations activate NAME` | Switch to a named configuration |
| `gcloud config configurations list` | List all named configurations |

### Project and Infrastructure Commands

| Command | Description |
|---|---|
| `gcloud projects list` | List all projects your account can access |
| `gcloud projects describe PROJECT_ID` | Show project metadata (number, labels, state) |
| `gcloud projects create PROJECT_ID` | Create a new project |
| `gcloud compute regions list` | List all GCP regions and their status |
| `gcloud compute zones list` | List all GCP zones |
| `gcloud compute zones list --filter="region:(REGION)"` | Filter zones by region |

### Output Formatting

The `--format` flag controls output format. Common values:

- `--format=table(field1,field2)` — custom table with selected columns
- `--format=json` — full JSON output, useful for scripting
- `--format=yaml` — YAML output
- `--format=value(field)` — print a single field value, useful in shell scripts

Example: print only project IDs:

```bash
gcloud projects list --format="value(projectId)"
```

---

## 8. ACE Exam Tips

1. Budget alerts never stop resources. This is one of the most frequently tested facts in Module 01. If a question offers "resources are suspended" as an answer choice when a budget is exceeded, that choice is always wrong.

2. IAM inheritance is additive only. A permission granted higher in the hierarchy cannot be blocked at a lower level through standard IAM. If a question asks how to prevent an org-level permission from applying to a project, the answer is to remove the grant at the org/folder level, not to set something at the project level.

3. Billing Accounts attach at the Project level. Answers stating "billing account is linked to the Organization" or "billing account is linked to individual resources" are incorrect.

4. Organization Policies vs IAM. When a question asks how to prevent a specific action across all projects in an organization regardless of user permissions, the answer is an Organization Policy constraint, not an IAM role removal.

5. Project ID vs Project Number. The Project ID is user-chosen or auto-generated and is globally unique. The Project Number is Google-assigned and immutable. Both uniquely identify a project. The Project Name is mutable and not unique.

6. Cloud Shell is ephemeral but has persistent home storage. The VM itself does not persist, but files in your 5 GB home directory do. Files written outside the home directory are lost when the Cloud Shell VM is recycled.

7. Multi-zone for zone resilience, multi-region for regional resilience. The ACE exam always pairs a resilience requirement with the appropriate architecture. Match zone-failure protection to multi-zone, and regional-failure protection to multi-region.

8. Named configurations in gcloud allow you to manage multiple project contexts safely. The command `gcloud config configurations activate NAME` switches all subsequent commands to use that configuration's project and settings.

---

## 9. Key GCP Documentation References

All links go to cloud.google.com/learn or official Google Cloud documentation:

- Resource Hierarchy overview: cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy
- Regions and Zones reference: cloud.google.com/compute/docs/regions-zones
- Organization Policies: cloud.google.com/resource-manager/docs/organization-policy/overview
- Cloud Billing overview: cloud.google.com/billing/docs/overview
- gcloud CLI reference: cloud.google.com/sdk/gcloud/reference
- Cloud Shell documentation: cloud.google.com/shell/docs

---

## 10. Study Checklist

Work through every item before taking the Module 01 quiz.

- [ ] Explain the difference between a region and a zone without looking at notes
- [ ] Draw the four-level GCP resource hierarchy from memory
- [ ] State the three identifiers of a GCP Project and the uniqueness rules for each
- [ ] Explain why IAM policy inheritance is additive only with a concrete example
- [ ] Explain why a budget alert does not stop resources
- [ ] Name the hierarchy level at which a Billing Account attaches
- [ ] List four common Organization Policy constraints and what each prevents
- [ ] Navigate to IAM, Billing, Compute Engine, and Cloud Storage in the Console
- [ ] Open Cloud Shell and successfully run `gcloud config list`
- [ ] Run `gcloud projects list` and identify your active project
- [ ] Run `gcloud compute regions list` and identify the region closest to you
- [ ] Create a named gcloud configuration with `gcloud config configurations create`
- [ ] Review the gcloud CLI command reference table in Section 7 above
- [ ] Complete the Module 01 lab
- [ ] Take the Module 01 quiz
- [ ] Post your Module 01 discussion response

---

End of Reading Guide — Module 01

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
