# Reading Guide: Module 01 — Cloud Computing Fundamentals and GCP Overview

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This reading guide accompanies Module 01 of CIS-4329. It is designed to
reinforce the video lecture content, provide additional depth on key concepts,
and prepare you for the module quiz and lab. All topics in this guide are
testable on the Google Cloud Associate Cloud Engineer exam.

**Estimated Reading Time:** 45–60 minutes

---

## Section 1 — Cloud Computing Fundamentals

### 1.1 The NIST Definition

The National Institute of Standards and Technology (NIST) Special Publication
800-145 defines cloud computing through five essential characteristics, three
service models, and four deployment models. This definition is the industry
standard and appears on cloud certification exams across all providers.

**Five Essential Characteristics:**

1. **On-demand self-service** — Consumers provision resources without requiring
   human interaction with the service provider.
2. **Broad network access** — Resources are available over the network and
   accessed through standard mechanisms (web browser, mobile app, CLI).
3. **Resource pooling** — Provider resources serve multiple consumers using a
   multi-tenant model, with resources dynamically assigned and reassigned.
4. **Rapid elasticity** — Resources can be provisioned and released elastically,
   appearing unlimited to the consumer.
5. **Measured service** — Resource usage is monitored, controlled, and reported,
   providing transparency for both provider and consumer.

### 1.2 Service Models

#### Infrastructure as a Service (IaaS)

IaaS delivers fundamental computing resources — virtual machines, storage, and
networking — over the internet. The cloud provider manages the physical
infrastructure; the customer manages the operating system, middleware, runtime,
data, and applications.

GCP IaaS examples: Compute Engine, Cloud Storage, Persistent Disk, VPC

#### Platform as a Service (PaaS)

PaaS delivers a computing platform and development stack. The cloud provider
manages infrastructure and the runtime; the customer deploys and manages
applications and data.

GCP PaaS examples: App Engine, Cloud Run, Cloud Functions, Cloud SQL

#### Software as a Service (SaaS)

SaaS delivers a complete software application over the internet. The cloud
provider manages everything, including the application.

GCP SaaS examples: Google Workspace (Gmail, Docs, Drive)

### 1.3 Deployment Models

- **Public cloud**: Infrastructure owned and operated by a third party, shared
  among multiple customers. Cost-efficient, no capital expense.
- **Private cloud**: Infrastructure operated solely for one organization.
  Greater control and compliance capability; higher cost.
- **Hybrid cloud**: Combination of on-premises or private cloud with public
  cloud. Workloads move between environments as needed.
- **Multi-cloud**: Use of services from two or more public cloud providers.
  Avoids vendor lock-in; increases operational complexity.

---

## Section 2 — GCP Global Infrastructure

### 2.1 Regions

A region is a specific geographic location containing at least two (usually
three or more) zones. Region names follow a standardized format:

```text
{area}-{direction}{number}
```

Examples:

- `us-central1` — Iowa, United States
- `europe-west1` — Belgium
- `asia-east1` — Taiwan
- `southamerica-east1` — São Paulo, Brazil
- `australia-southeast1` — Sydney, Australia

Region selection criteria:

- **Latency**: Deploy close to your end users.
- **Regulatory compliance**: Certain data must remain within specific
  jurisdictions (GDPR in Europe, data residency laws in India, etc.).
- **Service availability**: Not all GCP services are available in every region.
- **Cost**: Pricing varies by region; `us-central1` is typically the lowest-cost
  North American region.

### 2.2 Zones

A zone is a deployment area within a region, corresponding to one or more
physical data centers with independent power, cooling, and network. Zone names
append a letter to the region name:

```text
us-central1-a
us-central1-b
us-central1-c
us-central1-f
```

**Availability implications:**

| Deployment type | Protects against | Does not protect against |
|---|---|---|
| Single-zone | Hardware failure within a rack | Zone failure |
| Multi-zone (same region) | Zone failure | Regional failure |
| Multi-region | Regional failure | Global outages |

Most enterprise production workloads use multi-zone deployments within a single
region. Multi-region deployments are reserved for globally distributed
applications or disaster recovery requirements.

### 2.3 Network Infrastructure

Google operates one of the world's largest private fiber networks. GCP traffic
between regions travels over this private network rather than the public
internet, providing lower latency and higher bandwidth than most competitors.

**Points of Presence (PoPs)**: More than 180 locations worldwide used for edge
caching (Cloud CDN) and global load balancing. PoPs are not regions — you
cannot deploy VMs to a PoP.

**Premium vs Standard Network Tier:**

- **Premium Tier**: Traffic enters Google's network at the PoP closest to the
  user and stays on Google's network all the way to the destination VM. Lower
  latency, higher cost.
- **Standard Tier**: Traffic uses the public internet until it reaches a Google
  ingress point near the destination region. Lower cost, higher latency.

---

## Section 3 — GCP Resource Hierarchy

### 3.1 Four-Level Structure

```text
Organization
  └── Folder
        └── Project
              └── Resource
```

This hierarchy is not just organizational — it is the foundation of GCP's access
control and policy enforcement systems.

### 3.2 Organization Node

- Created automatically when a Google Workspace or Cloud Identity account is
  associated with a domain.
- Represents the root of the entire GCP environment for that domain.
- IAM policies and Organization Policy constraints applied here affect all
  resources in the organization.
- The `roles/resourcemanager.organizationAdmin` role is required to manage the
  Organization node.

### 3.3 Folders

- Optional but recommended for organizations with multiple teams or environments.
- Can be nested up to 10 levels deep.
- Useful for delegating administrative control: grant a team admin rights over
  their folder without giving them org-level access.
- Common patterns: by department, by environment (prod/staging/dev), by product.

### 3.4 Projects

The project is the core organizational unit in GCP.

**Project identifiers:**

| Identifier | Set by | Unique | Mutable |
|---|---|---|---|
| Project ID | User (or auto-generated) | Globally unique | No (immutable) |
| Project Number | Google | Globally unique | No (immutable) |
| Project Name | User | Not required to be unique | Yes |

**Key project facts:**

- Every resource must belong to exactly one project.
- A project must be linked to an active billing account to use paid services.
- Projects can be deleted, but deletion is soft for 30 days (recoverable).
- Deleting a project deletes all resources within it.

### 3.5 IAM Policy Inheritance

IAM policies in GCP are inherited from parent to child in the resource hierarchy.
A policy granted at the Organization level is effective at all folders, projects,
and resources within that organization.

**Key rule — additive only:**

Permissions can only be added as you move down the hierarchy. A more permissive
policy at a higher level cannot be restricted at a lower level. If a user has
`roles/editor` at the Organization level, a `roles/viewer` binding at the project
level does not reduce their access — they retain the higher privilege.

This is a critical distinction from some other cloud platforms that support
explicit deny rules. GCP IAM uses allow-only policies (as of the current ACE
exam scope).

---

## Section 4 — Billing and Cost Management

### 4.1 Billing Accounts

A billing account is a GCP resource that stores payment information and tracks
charges. It exists at the Organization level but is separate from the project
hierarchy — it is linked to projects, not contained within them.

**Types of billing accounts:**

- **Self-serve**: Credit card billing; charges apply immediately.
- **Invoiced**: Monthly invoice billing; available for large enterprises after
  approval.

### 4.2 Pricing Models

**On-demand / Pay-as-you-go:**

The default model. Resources are billed per second (minimum 1 minute for most
compute) with no upfront commitment.

**Sustained Use Discounts (SUDs):**

Automatically applied discounts for running a VM for a significant portion of
a billing month:

- 25–50% of the month: small discount begins
- 50–75%: discount increases
- 75–100%: maximum 30% discount

No action required; discounts apply automatically. SUDs apply to Compute Engine
and GKE (node VMs) but not to preemptible or Spot VMs, or to commitments.

**Committed Use Discounts (CUDs):**

Contract-based discounts for committing to a specific resource level for 1 or
3 years:

- 1-year commitment: up to 37% discount
- 3-year commitment: up to 55–57% discount

Unlike AWS Reserved Instances, GCP CUDs are flexible by default — you commit to
a vCPU/memory amount, not a specific VM type.

**Preemptible and Spot VMs:**

Short-lived VMs that can be reclaimed by Google with 30-second notice. Up to
91% cheaper than regular VMs. Suitable for batch jobs, fault-tolerant workloads,
and distributed processing. We cover these in depth in Module 03.

### 4.3 Budget Alerts

Budget alerts are configured under Cloud Billing. They send email notifications
(and optionally Pub/Sub messages) when spending crosses defined thresholds.

**Important facts for the ACE exam:**

- Budget alerts do not cap or stop spending.
- Crossing a budget threshold has no effect on running resources.
- To automatically respond to budget events, you must connect a Pub/Sub
  notification to a Cloud Function or other automation.
- Budgets can be set for a billing account, a project, or filtered by service
  or label.

### 4.4 GCP Pricing Calculator

The official pricing calculator at `cloud.google.com/products/calculator`
allows you to estimate monthly costs by selecting services and configuring
parameters. Use it to compare configurations before deploying.

---

## Section 5 — Cloud Console and CLI

### 5.1 Google Cloud Console

The Cloud Console is the web-based GUI for managing GCP resources. Key areas:

- **Project selector** (top bar): Switch between projects.
- **Navigation menu** (hamburger): Access all GCP services.
- **Search bar**: Find services, documentation, and resources.
- **Dashboard**: Overview of project health, billing, and recent activity.
- **IAM & Admin**: Manage users, service accounts, and policies.
- **APIs & Services**: Enable/disable APIs; manage credentials.
- **Billing**: View costs, set budgets, link billing accounts.

### 5.2 Cloud Shell

Cloud Shell is a free, browser-based development environment:

- Debian-based Linux VM, provisioned per user session
- 5 GB persistent home directory storage
- Pre-installed: gcloud CLI, gsutil, bq, kubectl, terraform, git, and more
- Pre-authenticated as your signed-in Google account
- Free to use; no additional charge

### 5.3 gcloud CLI Reference

Key command groups for the ACE exam:

```bash
# Configuration management
gcloud config set project PROJECT_ID
gcloud config set compute/region REGION
gcloud config set compute/zone ZONE
gcloud config list
gcloud config configurations create NAME

# Project management
gcloud projects list
gcloud projects create PROJECT_ID
gcloud projects describe PROJECT_ID
gcloud projects delete PROJECT_ID

# IAM
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:name@example.com" \
  --role="roles/viewer"

gcloud projects get-iam-policy PROJECT_ID

# Compute (preview — full coverage in Module 03)
gcloud compute instances list
gcloud compute zones list
gcloud compute regions list
```

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| Region | A specific geographic location containing GCP data centers |
| Zone | An isolated deployment area within a region |
| Organization | Root node of the GCP resource hierarchy; tied to a domain |
| Folder | Optional grouping layer between Organization and Projects |
| Project | Fundamental unit of resource ownership and billing in GCP |
| Project ID | Globally unique, immutable identifier chosen at project creation |
| Billing account | Payment profile linked to one or more GCP projects |
| SUD | Sustained Use Discount — automatic compute discount for long-running VMs |
| CUD | Committed Use Discount — discount for 1- or 3-year resource commitment |
| IAM | Identity and Access Management — controls who can do what in GCP |
| Organization Policy | Governance constraints controlling what actions are allowed at all |
| Cloud Shell | Free browser-based terminal with gcloud pre-installed |
| gcloud | Primary CLI tool for managing GCP resources |
| PoP | Point of Presence — edge location for CDN and global load balancing |

---

## ACE Exam Focus Areas — Module 01

- Identify the four levels of the GCP resource hierarchy in order.
- Explain IAM policy inheritance and why permissions cannot be reduced at lower
  levels.
- Distinguish between Organization Policies and IAM policies.
- State that budget alerts notify only; they do not stop resources.
- Differentiate sustained use discounts from committed use discounts.
- Define region and zone and describe their relationship.
- Identify the three project identifiers and their mutability.

---

## Further Reading

- Google Cloud Documentation — Resource Manager:
  cloud.google.com/resource-manager/docs
- GCP Regions and Zones reference:
  cloud.google.com/compute/docs/regions-zones
- Cloud Billing documentation:
  cloud.google.com/billing/docs
- gcloud CLI overview:
  cloud.google.com/sdk/gcloud
- NIST SP 800-145 (Cloud Computing Definition):
  nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
