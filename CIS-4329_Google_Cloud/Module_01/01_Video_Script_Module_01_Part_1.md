# Video Script: Module 01 — Cloud Computing Fundamentals and GCP Overview (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Welcome and Course Context (2 minutes)

Welcome to CIS-4329, Google Cloud Computing, at Texas Wesleyan University.
My name is Professor Nash, and over the next sixteen modules we are going to
build the skills you need to pass the Google Cloud Associate Cloud Engineer
certification and to deploy real workloads on Google Cloud Platform.

This is Module 01. We are starting at the very beginning — what cloud computing
actually is, why Google Cloud exists, and how GCP is organized at a structural
level. Everything we build later depends on the mental model you form today.

Before we dive in, a quick note on the exam. The ACE certification is Google's
entry-level professional credential. It tests your ability to deploy, monitor,
and manage cloud solutions using GCP services. We will flag every ACE exam topic
as it appears throughout the course.

**ACE Exam Tip:** Cloud fundamentals and the GCP resource hierarchy appear on
every version of the ACE exam. Know them cold.

---

## Segment 2 — What is Cloud Computing? (3 minutes)

Cloud computing is the on-demand delivery of computing resources — servers,
storage, databases, networking, software — over the internet, with pay-as-you-go
pricing.

The National Institute of Standards and Technology, NIST, defines cloud
computing through five essential characteristics:

1. On-demand self-service
2. Broad network access
3. Resource pooling
4. Rapid elasticity
5. Measured service

These five characteristics are what separate cloud from traditional data centers.
You do not need to call someone and wait three weeks for a server. You provision
it yourself in seconds, pay for what you use, and release it when you are done.

### Service Models

The three foundational service models are IaaS, PaaS, and SaaS.

**IaaS — Infrastructure as a Service** gives you raw compute, storage, and
networking. You manage the operating system and everything above it. GCP's
Compute Engine is IaaS.

**PaaS — Platform as a Service** gives you a runtime environment. You deploy
code; Google manages the infrastructure. GCP's App Engine and Cloud Run are PaaS.

**SaaS — Software as a Service** gives you a fully managed application. You log
in and use it. Google Workspace is SaaS.

### Deployment Models

- **Public cloud** — Resources owned and operated by a third-party provider,
  shared across customers. GCP is a public cloud.
- **Private cloud** — Resources operated exclusively for a single organization,
  on-premises or hosted.
- **Hybrid cloud** — Mix of on-premises and public cloud.
- **Multi-cloud** — Using services from multiple public cloud providers simultaneously.

GCP's Anthos product specifically supports hybrid and multi-cloud deployments,
which we cover in Module 06.

---

## Segment 3 — GCP vs AWS vs Azure (3 minutes)

Google Cloud Platform, Amazon Web Services, and Microsoft Azure are the three
dominant public cloud providers. Understanding how they compare helps you
contextualize GCP services throughout this course.

### Market Position

AWS launched in 2006 and is the market leader by revenue. Azure is second,
dominant in enterprise Microsoft environments. GCP is third but growing rapidly,
particularly in data analytics, AI/ML, and Kubernetes — Google invented
Kubernetes.

### Service Equivalences

| Category | GCP | AWS | Azure |
|---|---|---|---|
| Virtual Machines | Compute Engine | EC2 | Virtual Machines |
| Object Storage | Cloud Storage | S3 | Blob Storage |
| Managed Kubernetes | GKE | EKS | AKS |
| Serverless Functions | Cloud Functions | Lambda | Azure Functions |
| Managed Database | Cloud SQL | RDS | Azure SQL |
| Big Data | BigQuery | Redshift | Synapse Analytics |
| IAM | Cloud IAM | IAM | Azure AD + RBAC |
| DNS | Cloud DNS | Route 53 | Azure DNS |

### GCP Differentiators

Google Cloud has genuine advantages in several areas:

- **Network**: GCP runs on Google's own private fiber backbone — the same
  network that runs Google Search and YouTube. Traffic between GCP regions
  travels on Google's network, not the public internet.
- **BigQuery**: Serverless, petabyte-scale analytics with no infrastructure to
  manage. No direct equivalent in AWS or Azure at the same simplicity level.
- **Pricing**: Sustained use discounts apply automatically — no reserved instance
  commitments required.
- **Kubernetes**: GCP invented Kubernetes. GKE is widely considered the most
  mature managed Kubernetes service.

**ACE Exam Tip:** You do not need to memorize the AWS/Azure comparison for the
ACE exam, but understanding GCP's positioning helps you remember why certain
architectural choices exist.

---

## Segment 4 — GCP Global Infrastructure (4 minutes)

Google Cloud's infrastructure is organized into regions, zones, and a global
network.

### Regions and Zones

A **region** is a specific geographic location where Google operates data
centers. As of 2026, GCP has more than 40 regions worldwide, with more
announced regularly.

A **zone** is an isolated location within a region. Each region contains at
least three zones, named with a letter suffix. For example, `us-central1-a`,
`us-central1-b`, and `us-central1-c` are all zones within the `us-central1`
region in Iowa.

Zones provide fault isolation. If one zone goes down due to a power outage or
hardware failure, the other zones in the region are unaffected. High-availability
architectures distribute resources across multiple zones.

**ACE Exam Tip:** Know the difference between a region and a zone. Managed
instance groups can be zonal or regional. Regional MIGs span three zones for
higher availability.

### Network Edge Locations

Beyond regions and zones, Google has over 180 network edge locations called
Points of Presence, or PoPs. These are used by Cloud CDN and Google's global
load balancers to serve content close to users.

### Key Regions to Know

- **us-central1** — Iowa (most labs default here; lowest cost in North America)
- **us-east1** — South Carolina
- **us-west1** — Oregon
- **europe-west1** — Belgium
- **asia-east1** — Taiwan

For the ACE exam, you do not need to memorize every region, but you do need to
understand the naming convention and the region-zone relationship.

### Why Region Selection Matters

Choosing the right region affects:

- **Latency** — Deploy close to your users.
- **Compliance** — Data residency laws may require data to stay within certain
  geographic boundaries.
- **Cost** — Pricing varies by region.
- **Feature availability** — Not every GCP service is available in every region.

---

## Segment 5 — GCP Billing Fundamentals (3 minutes)

Understanding billing is both a practical skill and an ACE exam topic.

### Billing Accounts

A **billing account** is the payment instrument in GCP. It is linked to a
payment method — credit card, bank account, or invoice — and is associated with
one or more GCP projects.

Billing accounts live outside the project hierarchy. One billing account can pay
for many projects, and projects can be moved between billing accounts.

### Pricing Model

GCP uses several pricing mechanisms:

- **Pay-as-you-go**: Pay per second for most compute resources, per GB for storage.
- **Sustained use discounts (SUDs)**: Automatically applied when you use a VM for
  more than 25% of a month. No action required. Maximum discount is 30% off.
- **Committed use discounts (CUDs)**: 1-year or 3-year commitments for predictable
  workloads. Up to 57% off for compute.
- **Free tier**: 1 e2-micro VM per month in select regions, 5 GB Cloud Storage,
  and other always-free resources — great for labs.

### Budgets and Alerts

GCP allows you to set budget alerts. When spending reaches a threshold — say 50%,
90%, or 100% of your budget — you receive an email notification. Budget alerts
do not automatically stop resources; they only notify. To stop resources
automatically, you would connect a Pub/Sub notification to a Cloud Function.

### Pricing Calculator

The GCP Pricing Calculator at cloud.google.com/products/calculator lets you
estimate costs before deploying. The ACE exam may ask you to identify
cost-optimization strategies.

**ACE Exam Tip:** Know the difference between sustained use discounts (automatic)
and committed use discounts (contract-based). Know that budget alerts notify but
do not enforce spending limits automatically.

---

## Summary — Part 1

In Part 1 we covered:

- The five NIST characteristics of cloud computing
- IaaS, PaaS, and SaaS service models
- How GCP compares to AWS and Azure
- GCP's global infrastructure: regions, zones, and network PoPs
- GCP billing: billing accounts, pricing models, and budget alerts

In Part 2 we will explore the GCP resource hierarchy — organizations, folders,
and projects — and then walk through the Cloud Console and Cloud Shell hands-on.

See you in Part 2.

---

End of Part 1 — Module 01

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
