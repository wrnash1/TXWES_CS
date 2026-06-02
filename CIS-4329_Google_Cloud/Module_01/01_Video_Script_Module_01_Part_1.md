# Video Script — Module 01, Part 1

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: GCP Overview — Regions, Zones, and the Resource Hierarchy

### Estimated Duration: 12–14 minutes

---

**[INTRO — Instructor on camera, neutral background with TXWES branding]**

Hello, and welcome to CIS-4329, Google Cloud Platform, here at Texas Wesleyan University. I'm Professor Nash, and this is Module 01. Before you provision a single virtual machine or write a single line of Terraform, you need to understand how Google Cloud organizes its global infrastructure. Everything we do for the rest of this semester builds on the concepts we cover today.

By the end of this module you will be able to explain the difference between a region and a zone, describe GCP's four-level resource hierarchy, navigate the Google Cloud Console, and run your first gcloud CLI commands. These are not just introductory concepts — they appear on every Google Cloud Associate Cloud Engineer exam, so pay close attention.

Let's get started.

---

## Section 1: GCP's Global Infrastructure

**[SHOW SLIDE: World map with colored dots marking GCP regions]**

Google Cloud operates one of the largest private networks in the world. As of 2024, Google has data centers in more than 40 regions spread across six continents. Each region is a distinct geographic location — for example, `us-central1` is in Iowa, `europe-west1` is in Belgium, and `asia-east1` is in Taiwan.

**[SHOW SLIDE: Region diagram — one region containing three zones labeled -a, -b, -c]**

Inside each region are zones. A zone is an isolated deployment area within that region — think of it as a single data center or a cluster of data centers in close proximity. Zones within the same region are connected by high-bandwidth, low-latency internal networking, but they have independent power, cooling, and physical infrastructure. Zone names follow the pattern `REGION-LETTER`, so `us-central1-a`, `us-central1-b`, and `us-central1-c` are three separate zones within the `us-central1` region.

Here is the key distinction for the ACE exam: a single-zone deployment is vulnerable to zone failures — a hardware outage in that one data center will take your application down. A multi-zone deployment within one region gives you resilience against zone failures but does not protect you against a full regional outage. A multi-region deployment using a global load balancer protects against regional failures, but adds cost and architectural complexity. Know which level of resilience each scenario requires.

**[SHOW SLIDE: Table comparing single-zone, multi-zone, multi-region deployments with failure scope and cost columns]**

Let me give you a concrete example. If your university's registration system goes down because of a single-zone failure, that is a disaster. Deploying across three zones in `us-central1` at almost no extra cost would have prevented that outage. But if you are building a globally distributed application that must survive a hurricane wiping out an entire region, you need multi-region. Most production workloads for enterprises are multi-zone, single region.

---

## Section 2: The Resource Hierarchy

**[SHOW SLIDE: Four-level tree diagram — Organization at top, then Folders, then Projects, then Resources at bottom]**

Now let's talk about how Google organizes the resources inside its cloud. GCP uses a strict four-level hierarchy: Organization, Folders, Projects, and Resources.

At the very top is the **Organization** node. The Organization represents your entire company or institution. At Texas Wesleyan, this might be `txwes.edu`. The Organization node is the root of your GCP environment and is provisioned through Google Workspace or Cloud Identity. If you sign up for GCP with a personal Gmail account, you do not automatically get an Organization node — you only get one when your account is tied to a domain managed by Google Workspace or Cloud Identity.

Below the Organization are **Folders**. Folders let you group Projects logically — by department, by team, by environment, or however your organization chooses. For example, you might have a folder called `Engineering`, another called `Finance`, and another called `Shared-Services`. Folders are optional, but for any organization with more than a handful of projects, they are essential for governance.

Below Folders are **Projects**. The Project is the fundamental unit of organization in GCP. Every resource — every virtual machine, every storage bucket, every database — must belong to exactly one Project. Projects are how GCP tracks ownership, billing, and access control. Each Project has three identifiers: a globally unique Project ID (which you choose or let GCP generate), a Project Number (assigned by Google, immutable), and a Project Name (a human-readable label that is not unique).

**[SHOW SLIDE: Project identifiers table — ID vs. Number vs. Name, with uniqueness and mutability columns]**

Below Projects are **Resources** — the actual cloud services: Compute Engine VMs, Cloud Storage buckets, BigQuery datasets, Cloud SQL instances, and so on.

Why does this hierarchy matter? Because of policy inheritance. IAM policies — the rules that control who can do what — flow downward through the hierarchy. If you grant someone the `roles/viewer` role at the Organization level, that person has viewer access to every Folder, every Project, and every Resource in your entire organization. If you grant a role at the Folder level, it applies to all Projects inside that folder. This additive inheritance is a core security concept, and it is tested heavily on the ACE exam.

**[PAUSE — Professor on camera]**

Let me emphasize something that trips up many students. IAM inheritance in GCP is additive only. You can grant permissions at a higher level, and those permissions cascade down. But you cannot revoke or reduce a permission at a lower level that was granted at a higher level. If an executive at your company has `roles/owner` at the Organization level, there is no Project-level setting that will strip that access. The only way to restrict them is to remove the role at the Organization level itself.

---

## Section 3: Billing Accounts and Budget Alerts

**[SHOW SLIDE: Billing hierarchy diagram — Billing Account linked to one or more Projects]**

Billing in GCP is managed through Billing Accounts. A Billing Account is a payment profile — it stores a payment method and tracks charges. Critically, billing accounts attach at the **Project** level, not at the Organization level and not at the individual resource level. Each Project must be linked to exactly one active Billing Account in order to use paid GCP services.

One Billing Account can be linked to many Projects. This is the typical enterprise pattern — a central IT team owns one or a few Billing Accounts, and multiple project teams have their projects linked to those accounts.

**[SHOW CONSOLE: Navigate to Billing > Budgets and Alerts in the GCP Console]**

GCP lets you create budget alerts inside Cloud Billing. You set a budget amount — say, $1,000 per month — and you set threshold percentages, like 50%, 90%, and 100%. When your spending crosses those thresholds, GCP sends you an email notification, or it can publish a message to a Pub/Sub topic for programmatic handling.

Here is the ACE exam trap that catches almost every new student: budget alerts do not stop or suspend your resources. Crossing a budget threshold does absolutely nothing to your running VMs, your databases, or your storage. Your spending continues, and you continue getting charged. The alert is just a notification. To actually cap spending, you would need to build custom automation — for example, a Cloud Function triggered by a Pub/Sub budget notification that shuts down non-critical instances. But that automation is something you build yourself. GCP does not do it for you by default.

---

## Section 4: Organization Policies

**[SHOW SLIDE: Organization Policy console showing constraint list]**

Beyond IAM, GCP provides a separate governance layer called Organization Policies. While IAM controls who can perform actions, Organization Policies control what actions are allowed at all, regardless of who is asking. For example, you can use an Organization Policy constraint to prevent anyone from creating resources outside of approved regions — even if they have Owner-level access.

Organization Policies are applied at the Organization, Folder, or Project level, and they also inherit downward. The most common constraints tested on the ACE exam include:

- `constraints/compute.disableSerialPortAccess` — prevents interactive serial port connections to VMs
- `constraints/compute.requireOsLogin` — requires OS Login for SSH access to VMs
- `constraints/iam.disableServiceAccountKeyCreation` — prevents creation of service account keys
- `constraints/gcp.resourceLocations` — restricts which regions resources can be created in

For the ACE exam, if a question asks how to prevent a specific action across an entire organization or folder, the answer is almost certainly an Organization Policy constraint, not an IAM role.

---

## Closing — Part 1

Let's recap what we covered. GCP's global infrastructure is organized into Regions and Zones. Regions are geographic locations; zones are isolated data centers within a region. The resource hierarchy has four levels: Organization, Folders, Projects, and Resources. IAM policies inherit downward additively. Billing Accounts attach at the Project level. Budget alerts are notifications only — they do not stop resources. And Organization Policies control what actions are permitted organization-wide.

In Part 2, we will open the Google Cloud Console, tour its navigation, activate Cloud Shell, and run our first gcloud CLI commands. See you there.

---

End of Part 1 — Module 01

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
