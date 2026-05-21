# Reading Guide: Module 01 – GCP Overview: Regions, Zones, and Console Navigation
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 01 – GCP Overview: Regions, Zones, and Console Navigation**! This module establishes the foundational concepts every Google Cloud administrator needs before deploying any resource. You will learn how GCP organizes its global infrastructure, how the resource hierarchy governs access and billing, and how to navigate both the Google Cloud Console and the `gcloud` CLI. These topics appear on every ACE exam and underpin every other module in this course.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Region**: A specific geographic location (e.g., `us-central1`, `europe-west1`) that contains multiple zones. Regions are isolated from each other for fault tolerance, and choosing the right region reduces user latency. Most GCP services require you to specify a region at creation time.

*   **Zone**: An isolated deployment area within a region (e.g., `us-central1-a`, `us-central1-b`). Zones are Google's equivalent of availability zones. Deploying across multiple zones within the same region provides resilience against single-zone hardware failures.

*   **Resource Hierarchy**: GCP organizes resources in a four-level tree — **Organization → Folders → Projects → Resources**. IAM policies set at a higher level automatically inherit downward to all child resources. Billing accounts attach at the Project level, not at the Organization or individual resource level.

*   **Billing Account**: A GCP construct that is linked to one or more Projects to pay for consumed cloud resources. A Project must be associated with exactly one active Billing Account to use paid services; the Billing Account itself belongs to an Organization.

*   **Budget and Alerts**: In Cloud Billing you can create a budget and set alert thresholds (e.g., 50%, 90%, 100% of your expected spend). **Budgets do NOT automatically stop or delete resources** — they only trigger email or Pub/Sub notifications. This is a classic ACE exam trap.

*   **`gcloud` CLI Essentials**: `gcloud init` sets up your local SDK with your account, project, and default region/zone. `gcloud config list` shows your current active configuration. `gcloud config set project PROJECT_ID` switches the active project without reinitializing the entire SDK.

---

### 2. Certification Exam Tips

*   **Region vs. Zone failure scope**: The ACE exam distinguishes between zone-level failures (single data center outage) and region-level failures (entire geographic area). A multi-zone deployment within one region survives zone failures; a multi-region deployment survives full regional outages.

*   **IAM inheritance is additive only**: Policies granted at the Organization or Folder level flow down to all child Projects and resources. You cannot use a Project-level setting to *remove* a permission granted higher up — GCP IAM only adds permissions, never subtracts inherited ones.

*   **Billing attaches at the Project level**: The ACE exam offers "Organization level" and "Resource level" as distractors. Individual resources (VMs, buckets) inherit billing from their parent Project, not from any other hierarchy level.

*   **Console vs. gcloud parity**: Nearly all tasks can be performed through either the Cloud Console or the `gcloud` CLI. The ACE exam tests both interfaces — know common `gcloud compute`, `gcloud iam`, and `gcloud projects` command patterns in addition to Console navigation flows.

*   **Study Resource**: The freeCodeCamp ACE certification video covers GCP fundamentals, regions, zones, and the Console in its opening chapters: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). This is the primary OER video supplement for the entire course.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the GCP resource hierarchy documentation, which explains Organization, Folder, Project, and Resource levels with architecture diagrams: [Google Cloud Resource Hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).
*   **Required Reading**: Review region and zone concepts, including which GCP services are zonal, regional, or global: [Google Cloud Regions and Zones](https://cloud.google.com/compute/docs/regions-zones).
*   **Required Video**: Watch the GCP overview and fundamentals segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Use the video chapters to navigate directly to the GCP Fundamentals section.

---

### Lab & Command Integration
In this module's lab, you will navigate the Google Cloud Console, create a Project, and run your first `gcloud` commands. Key commands to practice:

*   `gcloud init` — configures your SDK with account, project, and default region
*   `gcloud config list` — displays your current active SDK configuration
*   `gcloud projects list` — lists all Projects your account can access
*   `gcloud compute regions list` — lists all available GCP regions and their status

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Google Cloud Resource Hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) documentation page.
- [ ] Read the [Regions and Zones](https://cloud.google.com/compute/docs/regions-zones) documentation page.
- [ ] Watch the GCP Overview segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a project, configure gcloud, list regions and zones.
- [ ] Proceed to the weekly quiz.
