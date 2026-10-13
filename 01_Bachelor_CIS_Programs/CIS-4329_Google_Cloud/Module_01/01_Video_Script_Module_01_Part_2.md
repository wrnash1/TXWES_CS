# Video Script: Module 01 — Cloud Computing Fundamentals and GCP Overview (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Recap and Agenda (1 minute)

Welcome back. In Part 1 we covered cloud service models, GCP's global
infrastructure, and the billing fundamentals. In Part 2 we are going hands-on.

We will walk through:

- The GCP resource hierarchy in depth — organizations, folders, and projects
- The Google Cloud Console interface
- Cloud Shell and the gcloud CLI
- ACE exam tips on all of the above

Let's open the console.

---

## Segment 2 — GCP Resource Hierarchy (4 minutes)

The GCP resource hierarchy has four levels. From top to bottom:

1. **Organization**
2. **Folders**
3. **Projects**
4. **Resources**

### Organization Node

The Organization node is the root of your GCP environment. It is provisioned
automatically when you use a Google Workspace or Cloud Identity domain. If you
sign up with a personal Gmail account, you do not get an Organization node —
you only get projects.

At Texas Wesleyan we would have an Organization node tied to `txwes.edu`. An
enterprise like a corporation would have its own Organization node.

The Organization node is where you apply the broadest IAM policies and
Organization Policy constraints. Anything granted at this level flows down to
every folder, project, and resource beneath it.

### Folders

Folders sit below the Organization node. They are optional but extremely useful
for governance. Common patterns:

- **By environment**: Production, Staging, Development folders
- **By department**: Engineering, Finance, HR folders
- **By team**: TeamA, TeamB folders

Folders can be nested up to ten levels deep, though deep nesting is rarely
needed in practice.

### Projects

The **project** is the fundamental unit in GCP. Every resource belongs to
exactly one project. Projects have three identifiers:

- **Project ID** — Globally unique, chosen by you (or auto-generated), immutable
  after creation. Used in API calls and CLI commands.
- **Project Number** — Assigned by Google, immutable. Used internally.
- **Project Name** — Human-readable label, not unique, can be changed.

When you run gcloud commands, you almost always reference the Project ID.

### IAM Policy Inheritance

IAM policies are additive and flow downward through the hierarchy. A role
granted at the Organization level applies to everything below it. A role granted
at a Project level applies only to resources in that project.

**Critical ACE Exam Point:** You cannot deny or reduce permissions at a lower
level that were granted at a higher level. Permissions only add; they never
subtract as you go down the hierarchy.

### Organization Policies

Organization Policies are a separate governance layer from IAM. While IAM
controls who can act, Organization Policies control what actions are permitted
at all. Key constraints include:

- `constraints/gcp.resourceLocations` — Restricts resource creation to approved
  regions
- `constraints/compute.requireOsLogin` — Requires OS Login for VM SSH access
- `constraints/iam.disableServiceAccountKeyCreation` — Prevents creation of
  downloadable service account keys

**ACE Exam Tip:** If a question asks how to prevent a specific action across an
entire org, the answer is an Organization Policy constraint, not an IAM role.

---

## Segment 3 — Cloud Console Walkthrough (4 minutes)

Open a browser and navigate to console.cloud.google.com.

### Navigation Bar

At the top of the console you see:

- The **hamburger menu** (three horizontal lines) on the left — opens the
  service navigation panel
- The **project selector** — shows your current project; click to switch
- The **search bar** — search for any GCP service or resource by name
- The **Cloud Shell** icon — activates Cloud Shell in a browser panel
- The **Notifications bell** — shows recent activity
- The **Help icon** — documentation and support

### Navigation Panel

Clicking the hamburger menu reveals every GCP service category:

- Compute (Compute Engine, GKE, Cloud Run, App Engine)
- Storage (Cloud Storage, Filestore, Persistent Disk)
- Networking (VPC, Cloud DNS, Load Balancing)
- Databases (Cloud SQL, Firestore, Bigtable, Spanner)
- Operations (Cloud Monitoring, Cloud Logging, Error Reporting)
- IAM & Admin (IAM, Service Accounts, Org Policies)
- Billing

Pin your most-used services to the top of the navigation by clicking the pin
icon next to each service name.

### Dashboard

The default Dashboard shows:

- Project info (Project ID, Project Number)
- Current billing summary
- Recent API activity
- Resource health alerts

You can customize the dashboard by adding or removing cards.

### APIs and Services

Before using any GCP service programmatically, you must enable its API. Navigate
to **APIs & Services > Library** to search for and enable APIs. Navigate to
**APIs & Services > Credentials** to create API keys and service account keys.

---

## Segment 4 — Cloud Shell and gcloud CLI (5 minutes)

Cloud Shell is a browser-based Linux shell with the gcloud CLI pre-installed,
5 GB of persistent home directory storage, and a code editor. It is free and
requires no local installation.

### Activating Cloud Shell

Click the Cloud Shell icon in the top-right of the console. A terminal panel
opens at the bottom of the browser. The first activation takes about 30 seconds.

### gcloud CLI Basics

The gcloud command-line tool is the primary way to interact with GCP
programmatically. It follows this structure:

```bash
gcloud [GROUP] [SUBGROUP] [COMMAND] [FLAGS]
```

#### Authentication and Configuration

```bash
# Authenticate with your Google account
gcloud auth login

# Set your active project
gcloud config set project PROJECT_ID

# View current configuration
gcloud config list

# List all available configurations
gcloud config configurations list
```

#### Working with Projects

```bash
# List all projects you have access to
gcloud projects list

# Describe a specific project
gcloud projects describe PROJECT_ID

# Create a new project
gcloud projects create my-new-project --name="My New Project"
```

#### Regions and Zones

```bash
# List all available regions
gcloud compute regions list

# List all available zones
gcloud compute zones list

# Set a default region and zone for your config
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a
```

#### Getting Help

```bash
# Top-level help
gcloud help

# Help for a specific command group
gcloud compute instances --help

# Interactive help browser
gcloud help --format=text
```

### Cloud Shell Persistent Storage

Your Cloud Shell home directory (`/home/your-username`) persists across
sessions. Files you create there are saved even after you close the terminal.
However, anything outside your home directory is ephemeral.

**ACE Exam Tip:** Cloud Shell provides a pre-authenticated environment. When
you open Cloud Shell, you are already authenticated as the Google account you
are logged into. You do not need to run `gcloud auth login` inside Cloud Shell
unless you need to authenticate as a different account.

### gcloud vs gsutil vs bq

The GCP CLI ecosystem has three main tools:

- **gcloud** — General GCP management (Compute, IAM, GKE, etc.)
- **gsutil** — Cloud Storage operations (now largely replaced by `gcloud storage`)
- **bq** — BigQuery operations

All three are pre-installed in Cloud Shell.

```bash
# Modern Cloud Storage commands (preferred)
gcloud storage buckets list
gcloud storage cp local-file.txt gs://my-bucket/

# Legacy gsutil (still works, widely documented)
gsutil ls
gsutil cp local-file.txt gs://my-bucket/

# BigQuery
bq ls
bq query "SELECT COUNT(*) FROM mydataset.mytable"
```

---

## Segment 5 — ACE Exam Tips for Module 01 (1 minute)

Before we wrap up Module 01, here are the top ACE exam focus areas:

- **Resource hierarchy**: Know all four levels and which identifiers belong to
  a project (ID, Number, Name). Know which is immutable.
- **IAM inheritance**: Permissions are additive and flow downward. Cannot revoke
  at a lower level what was granted at a higher level.
- **Organization Policies vs IAM**: Org policies control what is possible; IAM
  controls who can do it.
- **Budget alerts**: Notify only. Do not stop resources.
- **Sustained vs committed use discounts**: SUDs are automatic; CUDs require a
  commitment contract.
- **Regions vs zones**: Regions are geographic; zones are isolated data centers
  within a region. Multi-zone = resilience against zone failure; multi-region =
  resilience against regional failure.

---

## Summary — Module 01

Across both parts of Module 01 we covered:

- NIST cloud computing characteristics and service models
- GCP vs AWS vs Azure positioning
- GCP regions, zones, and global network infrastructure
- The four-level resource hierarchy and IAM inheritance
- Billing accounts, pricing models, budget alerts
- Cloud Console navigation
- Cloud Shell and gcloud CLI fundamentals

The lab for this module will have you create your first GCP project, set up
billing alerts, and run gcloud commands in Cloud Shell. See you there.

---

End of Part 2 — Module 01

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/sdk/gcloud
