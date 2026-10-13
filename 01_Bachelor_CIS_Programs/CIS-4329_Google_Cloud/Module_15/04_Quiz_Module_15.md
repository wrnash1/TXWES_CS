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

---

### Question 11 (5 points)

A GCP administrator wants to identify which Compute Engine VMs in a project have been idle for the past two weeks — defined as consuming less than 5% CPU for the entire period. What is the most direct GCP-native method to identify these VMs?

- A) Write a Cloud Monitoring SQL query that joins VM instance metrics with billing data to find VMs with zero cost
- B) Use the Idle VM Recommender (`google.compute.instance.IdleResourceRecommender`) via `gcloud recommender recommendations list` to retrieve VMs that GCP has flagged as idle based on observed utilization
- C) Export billing data to BigQuery and group charges by instance name; any instance with low cost is idle
- D) Enable Cloud Profiler on all VMs and review CPU profiling output to find instances with low activity

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud Monitoring does not support a JOIN between metrics and billing data in a single query. Even if it did, identifying "idle VMs" would require writing custom aggregation logic — unnecessary when a dedicated recommender handles this automatically.
  - C) Low cost in billing data does not directly indicate idleness. A small e2-micro VM running at 100% CPU appears as low cost because the machine type is inexpensive. Billing cost is not a reliable proxy for CPU idleness.
  - D) Cloud Profiler is a code-level CPU profiling tool that samples execution call stacks within running applications. It is not an infrastructure utilization monitor and does not flag idle VMs.

---

### Question 12 (5 points)

A company runs 20 n2-standard-4 Compute Engine VMs in us-east1 that process financial transactions 24/7. They committed to a 1-year CUD for `n2-standard-4` VMs in `us-central1` three months ago. The team now wants to migrate these VMs to us-east1. Can the existing CUD discount be applied to the us-east1 VMs?

- A) Yes — CUDs are billing-account-level and apply across all regions automatically
- B) No — resource-based CUDs are region-specific; the existing commitment applies only to the region it was purchased for (`us-central1`); a separate CUD would need to be purchased for `us-east1`
- C) Yes — CUDs are project-level and automatically follow VMs when they are migrated to a new region
- D) No — CUDs cannot be purchased for n2-standard-4 machine types; only N1 machine types support resource-based CUDs

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Resource-based CUDs are region-specific, not billing-account-wide. Spend-based CUDs (for Cloud SQL or VMware Engine) are applied at the billing account level, but compute resource-based CUDs are tied to a specific region.
  - C) CUDs are not tied to specific VM instances — they apply to any VM matching the committed resource type in the committed region. But the region constraint is fixed at purchase time. Migrating a VM to a different region does not transfer the CUD.
  - D) Both N1 and N2 machine types support resource-based CUDs. E2 machine types do not receive CUD or SUD discounts, but N2 is fully eligible.

---

### Question 13 (5 points)

An organization has configured a $200/month Cloud Billing budget for their production project. Actual spend for the current month has already reached $210. The administrator checks the project and all VMs are still running. Why have the VMs not stopped?

- A) The budget alert threshold was set to 100% but no Pub/Sub topic was connected to the budget notification; email-only budget alerts do not stop VMs
- B) Cloud Billing budgets are informational by default; crossing a budget threshold triggers email notifications (and Pub/Sub if configured) but does not automatically stop resources or disable billing
- C) The VMs are covered by Committed Use Discounts and CUDs override billing budget enforcement
- D) The budget is still in a pending state because billing data is delayed by 24 hours and has not been applied yet

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Even with a Pub/Sub topic connected, the Pub/Sub notification alone does not stop VMs. The Pub/Sub notification only triggers enforcement when a Cloud Function explicitly calls the Cloud Billing API to disable billing. The absence of a Pub/Sub topic is a secondary detail — the core answer is that budgets are always informational unless a Cloud Function acts on the notification.
  - C) CUDs and budget enforcement are completely separate. CUDs provide pricing discounts; they have no effect on budget alert behavior or billing enforcement.
  - D) Billing data is delayed, but a project that has already been billed $210 has already had that data processed. The billing export latency does not explain why the budget did not stop resources — the fundamental reason is that budgets never stop resources automatically.

---

### Question 14 (5 points)

A Cloud Storage bucket contains 50 TB of production data. An analyst accidentally runs `gsutil rm -r gs://production-bucket/**` and begins deleting objects. What GCP-native mechanism would have prevented permanent deletion of this data?

- A) Cloud Storage object versioning — enabling versioning means `gsutil rm` creates a delete marker but does not permanently remove the current live version immediately
- B) A Cloud Monitoring alert on storage object deletion events would have blocked the deletion before it completed
- C) Cloud Storage Retention Policies with bucket lock — objects subject to a locked retention policy cannot be deleted until the retention period expires, regardless of IAM permissions
- D) IAM Conditions set to deny delete operations during business hours

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Object versioning does protect against accidental deletion — `gsutil rm` on a versioned bucket creates a delete marker and moves the current version to a noncurrent state. However, noncurrent versions can still be permanently deleted with `gsutil rm -a`. Versioning is a valid protection but the locked retention policy (Option C) provides stronger, irrevocable protection that cannot be bypassed even by the bucket owner.
  - B) Cloud Monitoring detects events after they occur and can alert on them, but it cannot intercept and block in-progress API calls. Monitoring is reactive, not preventive.
  - D) IAM Conditions can restrict delete operations by time window, but a determined (or mistaken) user could delete outside business hours, or the condition could be modified by an IAM admin. Conditions are also evaluated per-request and can be misconfigured.

---

### Question 15 (5 points)

A development team's GCP project accumulates significant costs from Compute Engine VMs that are left running overnight and on weekends. The team does not want to write custom automation. What is the simplest GCP-native solution to automatically stop VMs outside business hours?

- A) Configure Cloud Monitoring to send an alert at 6 PM daily and have the on-call engineer manually stop the VMs
- B) Use VM Manager (OS Patch Management) scheduled tasks to shut down VMs at configured times
- C) Use Compute Engine instance schedules — attach a resource policy with a start and stop schedule (e.g., stop at 6 PM, start at 8 AM weekdays) to the VMs using `gcloud compute resource-policies create instance-schedule`
- D) Write a Cloud Function triggered by Cloud Scheduler that calls `gcloud compute instances stop` on all VMs in the project

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Manual intervention is not a GCP-native automated solution. It relies on human action and is error-prone (engineers forget or are unavailable).
  - B) VM Manager OS Patch Management schedules OS patching operations (applying security patches), not VM power state changes. It cannot start or stop instances.
  - D) Cloud Scheduler + Cloud Function is a valid technical solution and is used in practice. However, it requires writing, deploying, and maintaining a Cloud Function — it is not "the simplest" solution. Compute Engine instance schedules (Option C) require no custom code and are natively integrated into the Compute Engine API.

---

### Question 16 (5 points)

An organization wants to understand which GCP projects are generating the most egress costs (data transfer out of GCP). Billing export has been enabled for three months. What is the correct approach to identify top-egress projects?

- A) Navigate to Cloud Billing → Reports → filter by "Network" service and sort by project
- B) Query the BigQuery billing export table: filter on `service.description = 'Networking'` and SKUs related to egress; aggregate `SUM(cost)` grouped by `project.id` and order descending
- C) Use Cloud Monitoring network metrics to sum egress bytes per project and convert to cost using the public pricing sheet
- D) Use the GCP Pricing Calculator to estimate egress costs for each project based on estimated traffic volumes

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud Billing Reports provides a useful visual breakdown and does support filtering by service and project. However, it cannot perform cross-project aggregation with egress-specific SKU filtering in the same SQL-level precision available in BigQuery. For a definitive multi-project egress cost analysis, BigQuery SQL is the correct tool.
  - C) Cloud Monitoring tracks network bytes transferred but does not compute billing cost directly. Converting bytes to dollars requires knowing the per-GB egress pricing for each destination region and ISP tier — a complex calculation that the billing export handles automatically.
  - D) The Pricing Calculator estimates future costs for hypothetical configurations. It cannot analyze historical actual charges from three months of existing billing data.

---

### Question 17 (5 points)

A GCP organization has a billing account linked to 40 projects across 5 business units. The finance team needs each business unit to be charged back for their own GCP costs each month. No resource labels currently exist. What is the first step to enable cost allocation by business unit?

- A) Create a separate billing account for each business unit and migrate their projects to the respective billing account
- B) Apply consistent resource labels with a `business_unit` key to all GCP resources in each project, then query the BigQuery billing export grouping by the `business_unit` label value
- C) Create a Cloud Monitoring custom metric for each business unit that tracks their resource spend
- D) Export all project billing data to Cloud Storage and write a custom Python script to allocate costs by project owner

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Creating separate billing accounts per business unit is a valid governance structure, but it requires migrating 40 projects across billing accounts — a significant organizational change. Label-based cost allocation within a single billing account is simpler and does not require project migration. Separate billing accounts also lose the ability to apply billing account-level CUDs across all units.
  - C) Cloud Monitoring custom metrics track operational measurements (latency, error counts, etc.). They cannot track billing cost — billing data is in Cloud Billing and BigQuery, not Cloud Monitoring.
  - D) Custom Python scripts require ongoing maintenance and are error-prone. The BigQuery billing export + SQL approach is the GCP-native, supported pattern that does not require custom code for this use case.

---

### Question 18 (5 points)

A startup has been running on GCP for six months using only e2-micro VMs (1 in us-central1) and 4 GB of Cloud Storage in the US region. Their monthly bill has been $0 every month. They now add a Cloud SQL db-f1-micro instance in us-central1. What change do they expect on their next bill?

- A) The Cloud SQL instance will be free — it falls within the Always Free tier for Cloud SQL
- B) The bill will increase — Cloud SQL has no Always Free tier allocation; a db-f1-micro instance incurs per-hour charges from the moment it is created
- C) The Cloud SQL instance will be free for the first 30 days as a new service trial, then billed normally
- D) The bill will be $0 because db-f1-micro is included in the Always Free tier alongside the f1-micro VM

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud SQL is not included in the GCP Always Free tier. The Always Free tier covers specific Compute Engine, Cloud Storage, BigQuery, Cloud Functions, and Firestore quotas — but not Cloud SQL. Any Cloud SQL instance incurs charges.
  - C) GCP does not offer a 30-day free trial period for individual services on an existing billing account. The Google Cloud free trial ($300 credit) is available for new accounts, not individual new services added to an established account.
  - D) The Always Free tier f1-micro is a Compute Engine VM type; db-f1-micro is a Cloud SQL machine tier. Despite the similar naming, they are entirely different products. The Compute Engine f1-micro free tier does not extend to Cloud SQL db-f1-micro instances.

---

### Question 19 (5 points)

A team stores security audit logs in Cloud Storage Archive class. The compliance team requests that these logs be queryable by date range using SQL. The current Archive storage class makes access expensive due to per-read retrieval fees. What is the most cost-effective solution that adds SQL query capability?

- A) Transition all Archive objects to Standard class so retrieval is free, then query with gsutil
- B) Export the Cloud Storage billing export to BigQuery and query it for log metadata
- C) Configure a Cloud Logging log sink to route future audit logs directly to a BigQuery dataset; for historical data in Archive storage, use a one-time BigQuery load job (`bq load`) to ingest the data into BigQuery for SQL querying
- D) Use Cloud Dataflow to stream the Archive objects to Pub/Sub for real-time querying

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Transitioning from Archive to Standard would cost the early-deletion fee (Archive has a 365-day minimum storage duration) plus higher per-GB storage costs ongoing. This is expensive and unnecessary. Standard class does not provide SQL query capability by itself — gsutil does not support SQL.
  - B) The Cloud Storage billing export contains billing and cost data for the storage bucket, not the contents of the audit log files themselves. This does not enable SQL querying of the log records.
  - D) Cloud Dataflow is a managed data processing service for streaming and batch pipelines. Streaming Archive objects to Pub/Sub adds complexity and cost without a clear path to SQL query capability. BigQuery (Option C) is the direct, purpose-built SQL analytics solution.

---

### Question 20 (5 points)

A GCP project has been running for one year. The billing administrator notices that the `credits` column in the BigQuery billing export shows negative values for several line items. What do these negative credit values represent?

- A) Credits indicate billing errors where GCP overcharged the project; they are automatically refunded
- B) Credits represent discount amounts applied by GCP — such as Sustained Use Discounts, Committed Use Discount credits, promotional credits, or free tier credits — that reduce the net cost of a billing line item; a larger negative credit means more savings were applied
- C) Credits represent charges for support plans that appear as negative costs in the billing export
- D) Credits indicate that the resource was deleted during the billing period and a prorated refund was applied

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) While GCP does issue billing adjustments for errors, the `credits` column in the standard billing export is not specifically for billing error refunds. It primarily represents automatic discount mechanisms (SUDs, CUDs) and promotional credits applied as a normal part of GCP pricing.
  - C) Support plan charges appear as positive cost line items associated with the support SKU, not as negative credits. Negative values in the credits column are reductions in cost, not additional charges.
  - D) When a resource is deleted mid-month, billing is prorated but this appears as a shorter usage duration in the billing line item, not as a credit. Prorated charges are reflected in the `usage_amount` and `cost` fields, not the `credits` field.
