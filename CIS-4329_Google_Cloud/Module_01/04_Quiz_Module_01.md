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
