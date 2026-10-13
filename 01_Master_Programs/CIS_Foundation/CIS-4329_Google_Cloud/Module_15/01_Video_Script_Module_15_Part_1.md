# Video Script: Module 15 — GCP Cost Management and Billing (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 15. I am Professor Nash. This module covers GCP Cost Management and Billing — how GCP charges for services, how to control and forecast costs, and how to prevent billing surprises in a production environment.

Cost management is tested on the ACE exam in scenario questions about billing accounts, budget alerts, discount types, and billing data analysis. It is also a real operational skill — cloud costs can grow unexpectedly if not actively managed, and a GCP administrator is expected to implement billing controls from day one.

By the end of this two-part video series you will understand the GCP billing hierarchy, budget alerts and programmatic cost caps, committed use discounts versus sustained use discounts, Spot VMs versus standard preemptible VMs, billing export to BigQuery, the Recommender service for cost optimization, and strategies for common GCP service cost reduction.

Part 1 covers the billing hierarchy, budget alerts, and discount types. Part 2 covers billing export, Recommender, cost optimization strategies, and the GCP free tier.

---

### Section 1: GCP Billing Hierarchy

GCP billing is organized in a three-level hierarchy: Organization, Billing Account, and Projects.

At the top level, an **Organization** is the root node of the GCP resource hierarchy. It corresponds to a Google Workspace or Cloud Identity domain. The Organization is where billing policies, IAM policies, and Organization Policies are defined at the broadest scope.

A **Cloud Billing Account** is a resource within the organization that defines who pays for a set of GCP projects. A billing account is linked to one or more projects. Billing accounts are connected to a payment method — either a Google payments profile (credit card) or invoiced billing for larger enterprise customers. Each project must be linked to exactly one billing account for any paid resources to function.

**Projects** are linked to a billing account. All resource costs incurred in a project are charged to the linked billing account. A single billing account can be linked to multiple projects — useful for consolidated billing across teams or environments.

**IAM roles for billing:**

- `roles/billing.viewer` — can view costs and invoices; cannot modify billing settings
- `roles/billing.admin` — full control over the billing account; can link/unlink projects and modify payment methods
- `roles/billing.projectManager` — can link and unlink projects to/from a billing account; useful for project administrators without full billing account access
- `roles/billing.budgetAdmin` — can create and manage budgets without full billing admin access

The ACE exam tests the distinction between these roles. A common scenario: a project manager needs to move a project from one billing account to another. They need `roles/billing.projectManager` on the billing account, not `roles/billing.admin`.

---

### Section 2: Budget Alerts

A **Cloud Billing Budget** defines a spending threshold and sends notifications when spending approaches or exceeds that threshold.

**Budget scope.** A budget can be scoped to: an entire billing account; one or more specific projects; one or more specific services (e.g., only Compute Engine costs); or a combination with label filters.

**Alert thresholds.** A budget can have up to five alert thresholds, each specified as a percentage of the budget amount. Common configuration: 50%, 90%, 100%, and 110% (to alert on overages). Each threshold can trigger email notifications to billing account admins and/or a Pub/Sub topic.

**Important exam distinction:** Budgets and alerts are **informational by default** — they do NOT stop resource usage or billing when a threshold is exceeded. GCP does not automatically shut down resources when a budget is exceeded. The budget only sends notifications.

**Programmatic cost control.** To take automated action when a budget threshold is hit — for example, disabling billing on a project to stop all resource usage — you must configure a Pub/Sub notification on the budget and connect a Cloud Function (or Cloud Run job) that calls the Cloud Billing API to disable billing. This is a common exam scenario: "How do you automatically stop all resource usage when a budget is exceeded?" — Answer: Budget → Pub/Sub → Cloud Function → disable billing.

**Disabling billing on a project** removes the billing account link, which causes paid resources to stop functioning. VMs shut down, Cloud SQL becomes inaccessible, etc. Free tier resources continue to operate.

---

### Section 3: Committed Use Discounts

**Committed Use Discounts (CUDs)** provide discounts on Compute Engine resources in exchange for a 1-year or 3-year usage commitment.

**Types of CUDs:**

- **Resource-based CUDs** — Commit to a specific amount of vCPU and memory in a specific region. Discounts up to 57% off on-demand prices for 3-year commitments, approximately 37% for 1-year. Applied at the project level. Do not require choosing a specific VM instance type — apply to any VM using the committed resources in the committed region.
- **Spend-based CUDs** — Commit to spending a minimum dollar amount per month on specific services (Cloud SQL, VMware Engine). Applied at the billing account level. Available for services where resource-based commitments are not offered.

**Key CUD characteristics:**

- Commitments are billed monthly whether or not the resources are used. If you commit to 100 vCPUs and only use 50, you pay for 100.
- CUDs do not require choosing VM machine type in advance — they apply automatically to eligible usage in the committed region.
- CUDs can be shared across projects in the same billing account if commitment sharing is enabled.
- CUDs do not apply to preemptible/Spot VMs — those have their own discount mechanism.

**ACE exam scenario pattern:** "An organization runs 50 Compute Engine VMs continuously in us-central1 for 3 years. What is the best discount strategy?" — Answer: Purchase resource-based 3-year CUDs for the committed baseline usage. Any usage above the committed amount is billed at on-demand rates (or SUD rates if sustained use applies).

---

### Section 4: Sustained Use Discounts

**Sustained Use Discounts (SUDs)** are automatic discounts applied by GCP when a Compute Engine VM runs for more than 25% of a calendar month. No commitment or configuration is required — SUDs apply automatically.

**How SUDs work.** GCP tracks usage per VM per month. When a VM crosses the 25% monthly usage threshold, a discount is automatically applied retroactively to that VM's usage for the month. The discount increases incrementally as usage crosses 50% and 75% of the month. A VM running for the full month (100%) receives approximately 30% discount compared to per-second on-demand pricing.

**SUD eligibility:**

- Applies to: N1 and N2 machine types on Compute Engine
- Does not apply to: Spot VMs, preemptible VMs, E2 machine types, A2 (GPU) machine types, Cloud SQL instances, or Kubernetes Engine node pools

**SUD vs. CUD comparison:**

| Feature | SUD | CUD |
|---|---|---|
| Commitment required | No | Yes (1-year or 3-year) |
| Configuration required | No (automatic) | Yes (purchase commitment) |
| Maximum discount | ~30% | Up to 57% (3-year) |
| Eligible VM types | N1, N2 | Most Compute Engine types |
| Applies to Spot VMs | No | No |

**ACE exam pattern:** "An organization has unpredictable VM usage — sometimes high, sometimes low. What discount applies automatically?" — Answer: Sustained Use Discounts. CUDs require a commitment to a fixed resource amount, which is risky with unpredictable usage. SUDs require no commitment.

---

### Section 5: Spot VMs and Preemptible VMs

**Preemptible VMs** (the original product) and **Spot VMs** (the newer, recommended replacement) both provide deeply discounted compute at up to 91% off on-demand prices by using excess GCP capacity. The trade-off is that GCP can reclaim (preempt) these VMs at any time with 30 seconds notice.

**Key characteristics:**

- Preemptible VMs run for a maximum of 24 hours before being automatically terminated
- Spot VMs have no maximum runtime — they can run as long as capacity is available but can still be preempted at any time
- Both types are unsuitable for workloads that cannot tolerate interruption: databases, long-running batch jobs without checkpointing, services requiring high availability
- Best use cases: stateless web serving, batch processing with checkpointing, CI/CD workers, data analysis jobs that can restart

**ACE exam pattern:** "A company runs embarrassingly parallel data processing jobs that can be restarted from a checkpoint. They want to minimize compute cost. What VM type should they use?" — Answer: Spot VMs (or Preemptible VMs). The 60–91% discount is significant for batch workloads that tolerate interruption.

---

### Segment Summary

In this first part we covered:

- The GCP billing hierarchy: Organization → Billing Account → Project
- IAM roles for billing and their scope of access
- Budget alerts: threshold configuration, informational-only default behavior, and the Pub/Sub → Cloud Function pattern for programmatic cost control
- Committed Use Discounts: resource-based and spend-based, discount levels, and sharing
- Sustained Use Discounts: automatic, no commitment required, N1/N2 only
- Spot VMs and Preemptible VMs: deep discount for interruptible workloads

In Part 2 we cover billing export to BigQuery, the Recommender service, cost optimization strategies for Compute Engine, Cloud Storage, and managed services, and the GCP free tier.

---

### PRODUCTION NOTES

- Slide: GCP billing hierarchy diagram (Organization → Billing Account → Projects)
- Slide: IAM billing roles table with scope and use cases
- Slide: Budget alert configuration diagram showing Pub/Sub + Cloud Function pattern
- Slide: CUD vs. SUD comparison table
- Screen share: Cloud Console — Cloud Billing → Budgets and Alerts — creating a budget with multiple thresholds
- Screen share: Compute Engine → Committed Use Discounts dashboard
