# Video Script: Module 16 — GCP ACE Exam Preparation (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 16, the final module of CIS-4329. I am Professor Nash. This is your ACE exam preparation session. In this two-part video we consolidate all five ACE exam domains, work through the exam question strategy, and review the highest-frequency topic areas from across the course.

The Google Cloud Associate Cloud Engineer exam consists of 50 to 60 multiple-choice and multiple-select questions. You have two hours. The passing score is approximately 70 percent. Questions are scenario-based — they describe a real-world GCP situation and ask you to identify the correct service, command, configuration, or architectural decision.

The exam does not reward memorization of isolated facts. It rewards understanding how GCP services work together — which service to use for a given constraint, which gcloud command achieves a specific result, which storage class matches a given access pattern. Part 1 covers Domains 1 and 2: Setting Up a Cloud Environment and Planning and Configuring a Cloud Solution. Part 2 covers Domains 3, 4, and 5, plus exam strategy and twenty practice question guidance.

---

### Domain 1 Review: Setting Up a Cloud Environment

Domain 1 is tested throughout the ACE exam and underpins every other domain. It covers the GCP resource hierarchy, IAM, and billing.

**Resource hierarchy.** GCP has four levels: Organization → Folders → Projects → Resources. IAM policies and Organization Policies set at higher levels are inherited by lower levels. An Organization Policy set at the Organization node applies to all projects in the organization. This is the model for enforcing security controls at scale.

**Projects** are the primary unit of resource isolation. Resources in different projects are logically separated; cross-project access requires explicit IAM grants or VPC peering. Every project has a unique Project ID (immutable), a Project Number (auto-assigned, immutable), and a Project Name (mutable).

**IAM roles.** Know the three types:

- **Primitive roles**: Owner, Editor, Viewer — broad, legacy roles that apply to all services. Avoid in production; use predefined roles instead.
- **Predefined roles**: Fine-grained, service-specific roles. Example: `roles/compute.instanceAdmin.v1` grants full Compute Engine instance management; `roles/storage.objectViewer` grants read access to Cloud Storage objects. These are the roles you use in production.
- **Custom roles**: User-defined roles assembling specific permissions. Used when no predefined role provides exactly the right scope.

**Service accounts** are non-human identities used by applications, VMs, and services. A VM's service account defines what GCP APIs the VM's code can call. Best practice: create dedicated service accounts per workload with only the permissions that workload needs. Avoid using the Compute Engine default service account for production workloads — it has Editor-level access by default.

**ACE exam IAM patterns:**

- A VM needs to read from a specific Cloud Storage bucket only: grant `roles/storage.objectViewer` to the VM's service account on that specific bucket (not the project).
- An engineer needs to create VMs but not modify IAM policies: grant `roles/compute.instanceAdmin.v1` at the project level.
- An external application needs to write metrics to Cloud Monitoring: grant `roles/monitoring.metricWriter` to the application's service account.

**Organization Policies.** Constraints that restrict what can be done in a GCP organization, regardless of IAM permissions. Examples: `compute.vmExternalIpAddress` — restrict which VMs can have external IP addresses; `iam.allowedPolicyMemberDomains` — restrict which domains can be added to IAM policies (prevents adding personal Gmail accounts to organizational projects). Organization Policies are tested on the ACE exam in "how do you prevent X across the entire organization" scenarios.

**Billing hierarchy.** Billing accounts link to projects. IAM roles on billing accounts (viewer, admin, projectManager, budgetAdmin) have specific scope. Budgets are informational unless connected to a Pub/Sub → Cloud Function automation. CUDs, SUDs, and Spot VMs are the three main compute discount mechanisms.

---

### Domain 2 Review: Planning and Configuring a Cloud Solution

Domain 2 covers selecting the right compute, storage, and network services for a given set of requirements.

**Compute service selection.** The four main compute options and when to use each:

- **Compute Engine** — full control over OS, custom machine types, persistent storage, VM lifecycle. Use when you need specific OS configurations, persistent disks with specific IOPS, or migration of existing server workloads (lift and shift).
- **Google Kubernetes Engine (GKE)** — managed Kubernetes for containerized workloads requiring orchestration, auto-scaling, rolling updates, and multi-replica deployments. Use for microservices, stateful applications with persistent volumes, or workloads that need the Kubernetes ecosystem.
- **Cloud Run** — fully managed serverless containers. No cluster management. Scales to zero. Billed per request. Use for HTTP-driven workloads, APIs, webhooks, and applications with variable or unpredictable traffic.
- **App Engine** — fully managed platform for web applications and APIs. Standard environment (sandboxed, scales to zero, language-specific) vs. Flexible environment (Docker containers, more configuration). Use when you want platform management with minimal infrastructure knowledge.

**ACE compute decision framework:**

| Requirement | Service |
|---|---|
| Specific OS / custom kernel / GPU | Compute Engine |
| Container orchestration / multi-replica / stateful | GKE |
| HTTP API, scales to zero, no cluster management | Cloud Run |
| Simple web app, language runtime, minimal infra | App Engine Standard |
| Custom container runtime for web app | App Engine Flexible |

**Storage service selection.** Five primary storage types:

- **Cloud Storage** — object storage (blobs, files, images, backups). Not a filesystem. Access via HTTP API. Multi-regional, regional, or single-region. Storage classes: Standard, Nearline, Coldline, Archive.
- **Cloud SQL** — managed relational database (PostgreSQL, MySQL, SQL Server). Use for transactional applications that need SQL, foreign keys, and ACID transactions. Up to 96 vCPUs and 624 GB RAM. Regional (cross-region via read replicas).
- **Cloud Spanner** — globally distributed, horizontally scalable relational database with ACID transactions. Use when you need global consistency and scale beyond what Cloud SQL can provide. Much more expensive than Cloud SQL.
- **Bigtable** — managed NoSQL wide-column store for high-throughput, low-latency time-series, analytics, and IoT data. Petabyte-scale. Not for SQL queries or relational data.
- **Firestore** — managed NoSQL document database for mobile and web applications requiring real-time sync and offline support. Serverless, scales automatically.
- **Memorystore** — fully managed Redis or Memcached in-memory cache. Use for session state, query result caching, and pub/sub messaging that requires low latency.

**ACE storage decision framework:**

| Use Case | Service |
|---|---|
| File storage, backups, media, logs | Cloud Storage |
| Relational, transactional, < 10 TB | Cloud SQL |
| Relational, global consistency, > 10 TB | Cloud Spanner |
| High-throughput time-series, IoT, analytics | Bigtable |
| Document storage, mobile/web real-time | Firestore |
| Session cache, query cache | Memorystore |

**Networking service selection.** Key networking services for the ACE exam:

- **Cloud Load Balancing** — fully managed, global or regional load balancing. HTTP(S) Load Balancer is global; Network Load Balancer (TCP/UDP) is regional. Use cases: distribute traffic across VM instances or GKE pods, SSL termination, content-based routing.
- **Cloud CDN** — content delivery network integrated with Cloud Load Balancing. Caches static content at Google edge locations. Use for media, web assets, and public APIs with global users.
- **Cloud VPN** — encrypted site-to-site VPN over the public internet. Classic VPN (single tunnel, up to 3 Gbps) vs. HA VPN (two tunnels, higher availability, up to 3 Gbps per tunnel).
- **Cloud Interconnect** — dedicated, private connectivity to GCP data centers. Dedicated Interconnect: 10 or 100 Gbps circuits directly to Google's network. Partner Interconnect: lower-bandwidth connectivity via a partner provider. Use when you need high-bandwidth, low-latency, private connectivity without traversing the public internet.
- **VPC peering** — connect two VPC networks privately. No VPN or gateway required. Traffic stays within Google's network. Not transitive — if A peers with B and B peers with C, A cannot reach C through B.

---

### Segment Summary

In this first part we reviewed:

- Domain 1: Resource hierarchy, IAM role types, service accounts, Organization Policies, billing hierarchy
- Domain 2: Compute service selection (CE, GKE, Cloud Run, App Engine), storage service selection (Cloud Storage, SQL, Spanner, Bigtable, Firestore, Memorystore), and networking services (Load Balancing, CDN, VPN, Interconnect, VPC peering)

In Part 2 we cover Domains 3, 4, and 5 — deploying, ensuring success, and configuring access — plus exam strategy and twenty practice question review.

---

### PRODUCTION NOTES

- Slide: GCP resource hierarchy diagram (Organization → Folders → Projects → Resources)
- Slide: IAM role types comparison table (primitive, predefined, custom)
- Slide: Compute service decision table
- Slide: Storage service decision table
- Slide: Networking service comparison (VPN vs. Interconnect, global vs. regional load balancing)
- Screen share: Cloud Console IAM page showing role assignment at bucket level vs. project level
