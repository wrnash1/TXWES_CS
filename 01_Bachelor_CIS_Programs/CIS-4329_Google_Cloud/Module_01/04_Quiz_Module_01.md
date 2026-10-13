# Quiz: Module 01 — Cloud Computing Fundamentals and GCP Overview

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
This quiz covers cloud computing fundamentals, GCP global infrastructure,
the resource hierarchy, billing, and the Cloud Console and gcloud CLI.

---

## Question 1

Which of the following is NOT one of the five NIST essential characteristics
of cloud computing?

- A) On-demand self-service
- B) Rapid elasticity
- C) Dedicated hardware
- D) Measured service

**Correct Answer:** C

**Explanation:** The five NIST characteristics are: on-demand self-service,
broad network access, resource pooling, rapid elasticity, and measured service.
Dedicated hardware describes private infrastructure, which is the opposite of
the shared resource pooling model that defines cloud computing.

---

## Question 2

Your company wants to deploy a web application where your team writes and
manages application code but does not want to manage servers, operating systems,
or runtime environments. Which GCP service model best fits this requirement?

- A) IaaS — using Compute Engine
- B) PaaS — using App Engine
- C) SaaS — using Google Workspace
- D) IaaS — using Cloud Storage

**Correct Answer:** B

**Explanation:** Platform as a Service (PaaS) abstracts the infrastructure and
runtime, allowing developers to focus on application code. App Engine is GCP's
managed PaaS offering. IaaS (Compute Engine) would still require OS and runtime
management.

---

## Question 3

A GCP project has three identifiers: Project Name, Project ID, and Project
Number. Which statement is correct?

- A) Project Name is globally unique and immutable
- B) Project ID is globally unique and immutable after creation
- C) Project Number is chosen by the user during creation
- D) All three identifiers are mutable after project creation

**Correct Answer:** B

**Explanation:** The Project ID is globally unique across all of GCP and cannot
be changed after the project is created. Project Number is also immutable but is
assigned by Google, not the user. Project Name is the only identifier that can
be changed after creation, and it is not required to be globally unique.

---

## Question 4

You have granted `roles/editor` to a user at the Organization level. A project
owner attempts to restrict that user to `roles/viewer` within a specific project
by adding a `roles/viewer` binding on that project. What is the result?

- A) The user now has viewer-only access in that project
- B) The user retains editor access in that project due to additive IAM inheritance
- C) The conflicting bindings cancel out and the user has no access
- D) The project-level binding overrides the organization-level binding

**Correct Answer:** B

**Explanation:** GCP IAM inheritance is additive only. Permissions granted at a
higher level in the hierarchy flow down and cannot be reduced by bindings at a
lower level. Adding `roles/viewer` at the project level does not reduce the
`roles/editor` inherited from the Organization level.

---

## Question 5

Your monthly GCP spending reaches 90% of your configured budget alert threshold.
Which of the following will happen automatically?

- A) All compute instances in the project will be stopped
- B) The billing account will be suspended
- C) An email notification will be sent to billing administrators
- D) New resource creation will be blocked until the budget resets

**Correct Answer:** C

**Explanation:** Budget alerts in GCP are notifications only. Crossing any budget
threshold sends an email (and optionally a Pub/Sub message) but takes no
automatic action on resources. Resources continue running and charges continue
to accrue. Automatic remediation requires custom automation via Cloud Functions.

---

## Question 6

Which statement best describes the difference between a GCP region and a zone?

- A) A region is a single data center; a zone is a collection of regions
- B) A region is a geographic location containing multiple isolated zones
- C) Zones span multiple regions for global availability
- D) Regions and zones are interchangeable terms for data center locations

**Correct Answer:** B

**Explanation:** A region is a specific geographic location (such as Iowa or
Belgium) that contains multiple zones. A zone is an isolated deployment area
within a region — typically one or more physical data centers with independent
power and cooling. Zones within a region are connected by low-latency networking.

---

## Question 7

An architect wants to ensure that no one in the organization can create GCP
resources outside of `us-central1` and `us-east1`, regardless of their IAM
role. What is the correct approach?

- A) Create IAM deny policies restricting resource creation in other regions
- B) Configure a VPC firewall rule limiting traffic to those regions
- C) Apply an Organization Policy constraint using `constraints/gcp.resourceLocations`
- D) Set a billing budget alert filtered to the approved regions

**Correct Answer:** C

**Explanation:** Organization Policy constraints control what actions are
permitted at all, independent of IAM. The `constraints/gcp.resourceLocations`
constraint restricts which regions resources can be created in. IAM controls
who can perform actions; Organization Policies control what actions are possible.

---

## Question 8

You are comparing GCP's Compute Engine pricing to AWS EC2. Your workload runs
continuously for an entire month with no interruption. Which GCP pricing
benefit applies automatically without any reservation or commitment?

- A) Committed Use Discount at 57% off
- B) Preemptible VM pricing
- C) Sustained Use Discount at up to 30% off
- D) Custom machine type discount

**Correct Answer:** C

**Explanation:** Sustained Use Discounts (SUDs) are applied automatically when
a VM runs for more than 25% of a billing month. A VM running for a full month
qualifies for the maximum SUD of approximately 30%. No reservation or commitment
is required — this is a key differentiator from AWS Reserved Instances.

---

## Question 9

A developer runs the following command in Cloud Shell:

```bash
gcloud config set compute/region europe-west1
```

Which of the following is true?

- A) All existing Compute Engine resources are migrated to europe-west1
- B) The default region for new resources created by this gcloud configuration
   is set to europe-west1
- C) A new VPC network is created in europe-west1
- D) The project's billing is now linked to europe-west1 pricing

**Correct Answer:** B

**Explanation:** `gcloud config set compute/region` sets the default region for
the active gcloud CLI configuration. It affects which region is used when a
region is not explicitly specified in subsequent gcloud commands. It does not
move, create, or affect any existing resources.

---

## Question 10

Your organization uses Google Workspace with the domain `university.edu`. A new
GCP environment is being set up. Which resource will be automatically created
at the top of the GCP resource hierarchy?

- A) A default project named `university-edu`
- B) An Organization node for `university.edu`
- C) A billing account linked to the Workspace subscription
- D) A Folder named after the Workspace domain

**Correct Answer:** B

**Explanation:** When GCP is associated with a Google Workspace or Cloud
Identity domain, an Organization node is automatically provisioned at the top of
the resource hierarchy. This Organization node is named after the domain
(e.g., `university.edu`) and serves as the root for all folders, projects, and
resources within that GCP environment.

---

End of Quiz — Module 01

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

---

### Question 11 (5 points)

Which GCP CLI tool is the current recommended way to interact with Cloud Storage
buckets and objects, and what is its legacy predecessor?

- A) `bq` is current; `gsutil` is legacy
- B) `gcloud storage` is current; `gsutil` is legacy
- C) `kubectl` is current; `gcloud storage` is legacy
- D) `gsutil` is current; `gcloud` is legacy

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `bq` is the BigQuery command-line tool, not a Cloud Storage tool at all.
  - C) `kubectl` manages Kubernetes workloads and has no role in Cloud Storage operations.
  - D) `gsutil` is the legacy tool; `gcloud storage` is the modern replacement with improved performance and scripting support.

---

### Question 12 (5 points)

Your organization wants to prevent any GCP project from disabling audit logs,
regardless of who administers the project. Which mechanism enforces this at
the organizational level?

- A) A billing budget alert targeting all projects
- B) An Organization Policy constraint that prevents disabling Cloud Audit Logs
- C) A VPC firewall rule that blocks outbound log export traffic
- D) Granting `roles/viewer` to all principals at the Organization level

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Budget alerts send notifications about spending; they cannot enforce resource configuration or prevent operational changes.
  - C) Firewall rules govern network traffic; they cannot prevent a user from toggling audit log settings in the IAM console.
  - D) `roles/viewer` is read-only IAM and does not stop other principals with higher permissions from changing audit configurations.

---

### Question 13 (5 points)

A GCP project is accidentally deleted. What is the default recovery window
before the project and all its resources are permanently destroyed?

- A) 24 hours
- B) 7 days
- C) 30 days
- D) Projects cannot be recovered once deleted

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) 24 hours is far too short; GCP intentionally provides a longer grace period to protect against mistakes.
  - B) 7 days is the recovery window for some individual resources (such as certain database backups) but not for projects.
  - D) During the 30-day soft-delete window an Organization Admin can use the Resource Manager API to undelete the project.

---

### Question 14 (5 points)

Before deploying a new multi-tier GCP architecture, an architect wants to
estimate the monthly cost. Which tool is specifically designed for this purpose?

- A) Cloud Billing export to BigQuery
- B) Cloud Monitoring cost dashboards
- C) Google Cloud Pricing Calculator at cloud.google.com/products/calculator
- D) `gcloud billing accounts describe`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Billing export analyzes historical spending on existing resources, not hypothetical future architectures.
  - B) Cloud Monitoring cost metrics report on costs already incurred, not forward-looking estimates.
  - D) `gcloud billing accounts describe` returns billing account metadata such as name and currency; it does not model projected costs.

---

### Question 15 (5 points)

At which level of the GCP resource hierarchy is a billing account directly
linked in order to track resource charges?

- A) Organization
- B) Folder
- C) Project
- D) Individual resource (e.g., a single VM)

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) The Organization node governs policy and hierarchy but is not itself the unit that links to a billing account; projects are.
  - B) Folders are organizational containers; billing accounts are associated with projects inside folders, not the folders themselves.
  - D) Individual resources are billed through their parent project's linked billing account; you cannot attach a billing account to a single VM.

---

### Question 16 (5 points)

A Cloud Shell session is left idle for more than one hour. What happens?

- A) The 5 GB persistent home directory is deleted immediately
- B) The session is disconnected and the ephemeral VM is recycled, but the
   persistent home directory is preserved for the next session
- C) All gcloud CLI configurations are reset to factory defaults
- D) The user's Google account is permanently suspended

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The 5 GB home directory is persistent storage; it is only deleted after approximately 120 days of complete inactivity, not after an idle session.
  - C) gcloud configurations are stored in the persistent home directory (`~/.config/gcloud`) and survive session disconnections.
  - D) An idle Cloud Shell timeout has no effect on the Google account; it only terminates the terminal session.

---

### Question 17 (5 points)

An engineer frequently switches between a development project in `us-central1`
and a production project in `europe-west1`. Which gcloud feature allows them
to switch all defaults at once without re-entering each setting individually?

- A) `gcloud projects switch`
- B) Named gcloud configurations (`gcloud config configurations`)
- C) `gcloud auth switch-account`
- D) Setting `CLOUDSDK_CORE_PROJECT` environment variable only

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) There is no `gcloud projects switch` command; projects are changed via `gcloud config set project` or named configurations.
  - C) `gcloud auth switch-account` changes the authenticated user, not the project or region defaults.
  - D) Environment variables can override one setting but cannot bundle multiple defaults (project, region, zone, account) into a named, switchable profile.

---

### Question 18 (5 points)

Which of the following is a valid GCP multi-region storage location identifier?

- A) `us-central1`
- B) `us-east1-b`
- C) `us`
- D) `northamerica`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) `us-central1` identifies a single region (Iowa), not a multi-region location.
  - B) `us-east1-b` is a zone — one level below a region — and is not a multi-region designator.
  - D) `northamerica` is not a valid GCP location identifier; the three supported multi-region designators are `us`, `eu`, and `asia`.

---

### Question 19 (5 points)

You hold `roles/resourcemanager.organizationViewer` at the Organization level.
Which of the following actions are you permitted to perform?

- A) Create new folders within the organization
- B) Delete projects anywhere in the organization
- C) View the resource hierarchy and list folders and projects
- D) Modify IAM policies on projects within the organization

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Creating folders requires `roles/resourcemanager.folderCreator` or a higher role; the Viewer role is strictly read-only.
  - B) Deleting projects requires `roles/resourcemanager.projectDeleter` or `roles/owner` on the specific project.
  - D) Modifying IAM policies requires `roles/resourcemanager.projectIamAdmin` or `roles/owner`; Viewer grants no write permissions.

---

### Question 20 (5 points)

A startup runs variable workloads and wants no upfront commitment while
still benefiting from automatic discounts for VMs that run continuously
through the month. Which combination of GCP pricing features applies?

- A) Committed Use Discounts (1-year) applied automatically at month end
- B) Pay-as-you-go billing with automatic Sustained Use Discounts
- C) Spot VMs with manual discount request forms
- D) Flat-rate monthly prepaid billing

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Committed Use Discounts require signing a 1- or 3-year contract upfront, which contradicts the no-commitment requirement.
  - C) Spot VMs are interruptible; the scenario implies stable, continuously running workloads that need automatic discounts, not a separate low-cost VM class.
  - D) GCP does not offer flat-rate monthly prepaid billing for general compute; pricing is usage-based with automatic discounts applied.
