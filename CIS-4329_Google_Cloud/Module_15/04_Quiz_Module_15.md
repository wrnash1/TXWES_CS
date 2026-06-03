# Quiz: Module 15 — GCP Cost Management and Billing

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

Instructions: Select the single best answer for each question. Review the distractor analysis after completing the quiz.

---

### Question 1

A company wants to ensure that spending on a development GCP project never exceeds $500 in a single month. When the $500 limit is reached, all resource usage in the project must stop automatically. What is the correct implementation?

- A) Set the project quota to $500 in the Cloud Console — quotas automatically stop resources when reached
- B) Create a Cloud Billing Budget for $500 with a 100% threshold Pub/Sub notification; create a Cloud Function triggered by that Pub/Sub topic that calls the Cloud Billing API to disable billing on the project
- C) Create a Cloud Billing Budget for $500 — when the budget threshold is crossed, GCP automatically stops all resources in the project
- D) Create a Cloud Monitoring alert that terminates all VMs in the project when the billing metric exceeds $500

Correct Answer: B — Budgets are informational by default; they do not stop resources automatically. The only GCP-native programmatic cost enforcement mechanism is Budget → Pub/Sub → Cloud Function → disable billing via the Cloud Billing API. Disabling billing removes the billing account link from the project, causing all paid resources to stop functioning.

Distractor Analysis:

- Why A is incorrect: GCP quotas limit resource usage counts (number of CPUs, number of API requests per minute) — they are not spending controls. There is no quota that stops resources when a dollar amount is reached.
- Why C is incorrect: This is the most common misconception about GCP Budgets. Budgets send notifications only; they do not enforce spending by stopping resources. Engineers must explicitly implement the Cloud Function pattern to take automated action.
- Why D is incorrect: Cloud Monitoring billing metrics can alert on spending, but Cloud Monitoring does not have native support for calling the billing disable API. Even if a Cloud Monitoring alert triggered a Cloud Function, this would be a custom pattern — not simpler than the standard Budget → Pub/Sub → Cloud Function approach.

---

### Question 2

An organization runs 30 Compute Engine n2-standard-8 VMs in us-central1 continuously for production workloads. They have been running for 8 months and plan to continue for at least 3 more years. Currently they receive only Sustained Use Discounts. What action provides the greatest additional cost reduction?

- A) Migrate all VMs to Spot VM instances to take advantage of the 91% discount
- B) Purchase 3-year resource-based Committed Use Discounts for the sustained baseline vCPU and memory in us-central1
- C) Enable preemptible mode on the VMs to receive the preemptible discount on top of the existing SUD
- D) Migrate the VMs from n2-standard-8 to e2-standard-8 to receive the cheaper E2 pricing and SUD combined

Correct Answer: B — For stable, long-running production workloads with a multi-year horizon, 3-year resource-based CUDs provide up to 57% discount — significantly more than the ~30% SUD maximum. The CUD applies in addition to any applicable credits, and the organization's usage pattern (continuous, predictable) is exactly the scenario CUDs are designed for. CUDs and SUDs do not stack on the same usage — the CUD replaces the SUD for committed resources — but the CUD discount is substantially larger.

Distractor Analysis:

- Why A is incorrect: Spot VMs can be preempted at any time with 30 seconds notice. Production workloads requiring continuous availability cannot tolerate preemption. The 91% discount is not applicable when availability is required.
- Why C is incorrect: Preemptible mode cannot be enabled on running VMs — it is set at creation time. More importantly, enabling preemptible mode on production workloads would make them subject to interruption, which is operationally inappropriate. Also, preemptible and SUD discounts do not combine — preemptible VMs have their own pricing and do not receive SUDs.
- Why D is incorrect: E2 machine types do not receive Sustained Use Discounts — this is explicitly excluded. While E2 pricing may be lower per vCPU than N2 for some configurations, the combination of N2 + 3-year CUD typically provides greater savings than E2 without a commitment. Additionally, migrating machine families requires VM recreation, which is disruptive.

---

### Question 3

A GCP administrator wants to analyze which engineering teams are incurring the most GCP costs over the past quarter. All resources have been tagged with a `team` label. What is the most effective approach?

- A) Use Cloud Monitoring to create a dashboard that groups billing metrics by `team` label
- B) Export billing data to BigQuery using Cloud Billing export, then query the BigQuery billing dataset using SQL to aggregate cost by the `team` label value
- C) Navigate to Cloud Billing → Reports in the Cloud Console and filter by the `team` label
- D) Ask each team to submit their own GCP project billing reports and aggregate them manually

Correct Answer: B — The Cloud Billing BigQuery export is the definitive tool for detailed cost analysis with label-based allocation. It provides line-item billing data that can be queried with SQL to aggregate costs by any label value, across any time period, with filtering by service, region, or SKU. Cloud Console Reports (Option C) also supports label filtering but has limited SQL flexibility and historical range.

Distractor Analysis:

- Why A is incorrect: Cloud Monitoring tracks operational metrics (CPU, memory, request rates) and can display some billing metrics via the Billing API. However, it does not provide the granular label-level cost breakdown available in the BigQuery billing export, and its SQL querying capability for billing analysis is limited.
- Why C is incorrect: Cloud Billing → Reports does support label filtering and is useful for quick visual analysis. However, for detailed programmatic analysis across a full quarter with multi-team breakdowns, BigQuery SQL is substantially more powerful and flexible. The ACE exam typically favors BigQuery export for "analyze" and "allocate" scenarios.
- Why D is incorrect: Manual aggregation from team-submitted reports is error-prone, non-scalable, and not a GCP-native solution. The label-based BigQuery export approach is the industry-standard pattern.

---

### Question 4

A Cloud Storage bucket stores application logs. Logs are accessed frequently during the first 30 days (debugging and monitoring), rarely between 30 and 90 days, and never after 90 days — but logs must be retained for 2 years for compliance. What Object Lifecycle Management policy minimizes storage cost while meeting the retention requirement?

- A) Delete all objects after 30 days and store a backup in a separate Archive bucket
- B) Transition objects to Nearline storage at 30 days, transition to Archive storage at 90 days, and delete at 730 days (2 years)
- C) Transition all objects to Archive storage immediately on creation to minimize cost from day one
- D) Keep all objects in Standard storage for 2 years to avoid the per-read charges associated with lower-tier storage classes

Correct Answer: B — This policy matches the access pattern to storage class. Standard (days 0–30) handles frequent access with no retrieval fee and no minimum duration. Nearline (days 30–90) handles rare monthly access — the 30-day minimum is satisfied. Archive (days 90–730) handles zero access with the lowest per-GB price — the 365-day minimum is satisfied. Deletion at 730 days fulfills the 2-year retention requirement. This is the standard ACE exam lifecycle policy design pattern.

Distractor Analysis:

- Why A is incorrect: Deleting logs at 30 days violates the 2-year retention requirement. Copying to a separate Archive bucket is operationally complex and unnecessary — lifecycle management handles class transitions within the same bucket.
- Why C is incorrect: Archive storage has a 365-day minimum storage duration. Objects deleted, moved, or accessed before 365 days incur an early deletion fee. For logs accessed frequently in the first 30 days, Archive would be the wrong class (high per-read charges) and would violate the minimum duration requirement if any log was deleted before a year.
- Why D is incorrect: Standard storage at $0.02/GB/month for 2 years of accumulating log data would be significantly more expensive than transitioning to Nearline ($0.01/GB) and Archive ($0.0012/GB). The per-read charges on Nearline and Archive are only relevant when data is actually accessed — since the logs are not accessed after 90 days, read charges are not a concern.

---

### Question 5

A GCP administrator runs the following command and sees several recommendations returned: `gcloud recommender recommendations list --recommender=google.compute.instance.MachineTypeRecommender --location=us-central1 --project=my-project`. What do these recommendations indicate and what is the appropriate response?

- A) These recommendations indicate that the listed VMs are at risk of running out of CPU capacity; the response is to upgrade to larger machine types before the VMs experience performance degradation
- B) These recommendations indicate that the listed VMs are consistently over-provisioned — using significantly less CPU and memory than their current machine type provides; the response is to review each recommendation, validate the projected savings, and resize appropriate VMs to the smaller recommended machine type during a maintenance window
- C) These recommendations indicate that the listed VMs have been idle for more than 14 days and should be deleted; resizing them will not help because they are not being used
- D) These recommendations are generated automatically on all VMs and do not reflect actual usage patterns; they should be dismissed unless a VM has been manually flagged by the team as over-provisioned

Correct Answer: B — The VM Rightsizing Recommender (MachineTypeRecommender) analyzes CPU and memory utilization metrics over 14 days and identifies VMs where actual usage is consistently much lower than the provisioned machine type. It recommends a smaller machine type and projects the monthly savings. The recommended response is to review each recommendation (validate the usage data is correct and the smaller machine type will handle peak loads), then downsize during a maintenance window.

Distractor Analysis:

- Why A is incorrect: The MachineTypeRecommender recommends downsizing (smaller machine types), not upsizing. If a VM needed more capacity, Cloud Monitoring CPU utilization alerts would flag the high utilization, not the rightsizing recommender.
- Why C is incorrect: The Idle VM Recommender (IdleResourceRecommender) identifies idle VMs for stopping or deletion. The MachineTypeRecommender is specifically for over-provisioned VMs that are running but using less than their provisioned capacity. These are different recommenders.
- Why D is incorrect: Recommender recommendations are based on actual Cloud Monitoring utilization metrics — they are data-driven, not arbitrary. A recommendation for a specific VM means that VM's actual utilization data supports the smaller machine type. They should not be dismissed without review.

---

### Question 6

An organization has a sustained use discount applied to their n1-standard-16 Compute Engine VMs in us-east1. They are now planning a 3-year infrastructure contract. Their finance team asks: which discount type provides the highest savings for committed, long-running workloads? What is the correct answer?

- A) Sustained Use Discounts provide up to 57% off, making them the best option for 3-year committed workloads
- B) 3-year resource-based Committed Use Discounts provide up to 57% off for vCPU and memory in a specific region — higher than the maximum SUD discount of approximately 30% — making CUDs the better choice for committed 3-year workloads
- C) Preemptible VMs provide 91% off and are the best choice for any long-term workload
- D) Sustained Use Discounts and Committed Use Discounts stack — you receive both simultaneously for a combined discount exceeding 60%

Correct Answer: B — 3-year resource-based CUDs provide up to 57% discount off on-demand pricing, compared to SUDs which max out at approximately 30%. For a 3-year committed workload, CUDs are definitively the higher-discount option. Note that for committed resources, the CUD replaces the SUD — they do not stack. Uncommitted usage above the CUD commitment would still receive SUDs.

Distractor Analysis:

- Why A is incorrect: SUDs provide approximately 30% maximum discount, not 57%. The 57% discount belongs to 3-year CUDs. Confusing these two values is a common exam distractor.
- Why C is incorrect: Preemptible VMs and Spot VMs are not suitable for long-term committed production workloads that must remain continuously available. Preemption at any time makes them operationally inappropriate for workloads that cannot tolerate interruption.
- Why D is incorrect: CUDs and SUDs do not stack on the same vCPU/memory resources. CUD covers committed resources at the CUD price; SUD applies to usage above the committed amount. For the committed portion, you receive the CUD discount only (which is higher than SUD).

---

### Question 7

A team is setting up billing governance for a new GCP organization with 10 projects managed by 3 teams. A billing administrator needs to allow each team's project manager to link their team's projects to the appropriate billing account, but the project managers should not be able to see payment method information or modify billing account settings. Which IAM role should be granted to the project managers on the billing account?

- A) `roles/billing.admin` — project managers need admin access to link projects
- B) `roles/billing.viewer` — project managers can view the billing account and link projects with this role
- C) `roles/billing.projectManager` — this role allows linking and unlinking projects to billing accounts without granting access to payment methods or billing account configuration
- D) `roles/resourcemanager.projectOwner` — project owners can link projects to billing accounts using their project-level role

Correct Answer: C — `roles/billing.projectManager` is specifically designed for this use case. It grants the ability to link and unlink projects to billing accounts without providing access to payment method information, billing account settings, or the ability to manage other billing account properties. This follows the principle of least privilege.

Distractor Analysis:

- Why A is incorrect: `roles/billing.admin` grants full control over the billing account — including payment method modification, invoice management, and all billing settings. This is far more access than project managers need to link projects.
- Why B is incorrect: `roles/billing.viewer` grants read-only access to billing data (costs, invoices, reports). It does not grant the ability to link or unlink projects.
- Why D is incorrect: `roles/resourcemanager.projectOwner` grants Owner-level access at the project level. It does not grant billing account-level permissions. Linking a project to a billing account requires a billing account-level role, not just a project-level role.

---

### Question 8

A GCP administrator notices that the Cloud Billing export to BigQuery shows significant costs for reserved static IP addresses in several regions. No resources appear to be attached to these IP addresses. What is the most appropriate next step?

- A) Delete all reserved static IP addresses immediately — unused IPs are always safe to delete
- B) Use the Idle IP Address Recommender to identify unattached reserved IPs, verify that each IP is not needed (check with teams), and release IPs that are confirmed unneeded
- C) The cost is expected — reserved static IPs always appear as significant charges; no action is required
- D) Move the IP addresses to a different region where reserved IP pricing is lower

Correct Answer: B — Reserved static IP addresses that are not attached to a resource incur a per-hour holding charge. The Idle IP Address Recommender identifies these unattached IPs. However, before releasing IPs, an administrator should confirm with the owning teams that the IPs are genuinely unused — some teams reserve IPs in advance for planned resources or maintain IPs for DNS entries that are actively in use but not currently attached to a live resource.

Distractor Analysis:

- Why A is incorrect: Deleting IPs without checking with teams could release IPs that are tied to DNS records or firewall rules that teams depend on. The correct process is to verify before releasing.
- Why C is incorrect: Reserved but unattached IP addresses do incur charges — this is a known cost optimization opportunity. The billing export identifying this cost is evidence that action may be warranted, not that the charges are expected and acceptable.
- Why D is incorrect: Reserved static IP pricing is consistent across GCP regions — there is no "cheaper region" for reserved IPs. Moving IPs to a different region also changes the IP address value, which would break any DNS records or firewall rules referencing the specific IP.

---

### Question 9

An organization wants to estimate the monthly cost of a planned GCP architecture before provisioning any resources. The architecture includes 20 Compute Engine VMs, a Cloud SQL PostgreSQL instance, 50 TB of Cloud Storage, and a GKE cluster with 5 nodes. What tool should they use?

- A) Cloud Monitoring — create a cost dashboard for the planned resources
- B) gcloud cost estimate command — the gcloud CLI provides cost projections for resource configurations
- C) GCP Pricing Calculator — input the planned resource specifications to generate a monthly cost estimate with options to compare on-demand vs. CUD pricing
- D) Cloud Billing → Reports — navigate to the planned project and view projected costs

Correct Answer: C — The GCP Pricing Calculator is the dedicated pre-provisioning cost estimation tool. It supports detailed configuration of all major GCP services and provides monthly cost estimates with and without committed use discounts. It can export estimates as PDFs and is the tool explicitly referenced in the ACE exam guide for cost forecasting.

Distractor Analysis:

- Why A is incorrect: Cloud Monitoring tracks actual utilization metrics of running resources. It cannot project costs for resources that do not yet exist.
- Why B is incorrect: There is no `gcloud cost estimate` command. gcloud CLI manages GCP resources and configurations but does not provide a cost estimation capability.
- Why D is incorrect: Cloud Billing → Reports shows historical actual costs for existing projects. A planned project with no resources has no billing data to report. Reports cannot project future costs.

---

### Question 10

A startup running on GCP's Always Free tier has been using one f1-micro VM in us-west1, 4 GB of Cloud Storage, and 800 GB of BigQuery queries per month for the past three months. They are considering adding a second f1-micro VM in us-east1. Will this incur charges? What is the always-free limit for Compute Engine?

- A) No — the Always Free tier provides one free f1-micro per region, so adding a VM in us-east1 is free in addition to the us-west1 VM
- B) Yes — the Always Free tier provides only 1 f1-micro VM instance per month across all three eligible US regions combined (us-west1, us-central1, us-east1); a second VM in any region would be billed at on-demand rates
- C) No — Always Free instances are unlimited in the three eligible US regions; only non-US regions incur charges for f1-micro instances
- D) Yes — the Always Free tier only covers f1-micro VMs in us-central1; a VM in us-west1 or us-east1 would already be billed

Correct Answer: B — The Compute Engine Always Free tier provides exactly 1 f1-micro VM instance per month total, shared across us-west1, us-central1, and us-east1. It is not 1 per region — it is 1 across all three regions combined. Adding a second f1-micro in any region (including us-east1) would exceed the free tier allocation and incur charges. This is a frequently tested exam detail.

Distractor Analysis:

- Why A is incorrect: The Always Free limit is 1 f1-micro per billing month across the three eligible regions combined, not 1 per region. Running one in us-west1 and one in us-east1 simultaneously uses 2 instance-months, which exceeds the single free-tier allocation.
- Why C is incorrect: The free f1-micro is limited to the three specific US regions (us-west1, us-central1, us-east1). It is not unlimited in those regions — it is limited to 1 per month total. Instances in any region beyond the first free instance are billed.
- Why D is incorrect: The Always Free tier explicitly includes us-west1 and us-east1 in addition to us-central1. The current startup is correctly using a free VM in us-west1. The question is whether a second VM is free — and the answer is no, because the limit is 1 combined across all three eligible regions.
