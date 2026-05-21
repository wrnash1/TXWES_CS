# Reading Guide: Module 15 - Database Cost Optimization on GCP
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 15 - Database Cost Optimization on GCP**! This week focuses on managing and reducing the cost of running database workloads on Google Cloud. Cost optimization is a core responsibility of a Cloud Database Engineer and appears on the GCP Professional Cloud Database Engineer exam as scenario questions where you must identify the most cost-effective configuration for a given workload.

You will learn how to right-size Cloud SQL instances, use committed use discounts, optimize BigQuery costs with partitioning and clustering, control Spanner Processing Unit consumption, and avoid common cost waste patterns across all GCP database services.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cloud SQL Storage Auto-Increase**: Cloud SQL can automatically increase disk storage when usage approaches the current limit. While convenient, auto-increase only grows storage — it never shrinks it. Enabling auto-increase on a database that has a temporary spike can permanently lock in a higher storage cost. Plan storage capacity carefully and use Cloud Monitoring storage alerts.
*   **BigQuery On-Demand vs. Flat-Rate Pricing**: BigQuery charges on-demand pricing at $5 per TB of bytes processed. For consistent, high-volume workloads, flat-rate (slot reservation) pricing provides a fixed monthly cost for a reserved number of query processing slots. The break-even point is typically around 1,000+ TB of queries per month. The exam tests which model is more cost-effective for a described usage pattern.
*   **Cloud SQL Instance Right-Sizing**: Running a Cloud SQL instance at 10% CPU utilization wastes 90% of the compute you are paying for. Use Cloud Monitoring to analyze CPU, memory, and connection metrics over time, then resize the instance to a smaller machine type during a maintenance window. Cloud SQL instances can be resized up or down.
*   **Committed Use Discounts (CUDs)**: GCP offers 1-year and 3-year committed use contracts for Cloud SQL, AlloyDB, and Spanner that provide discounts of 25–57% compared to on-demand pricing in exchange for a usage commitment. CUDs are appropriate for stable, predictable production workloads. They do not apply to storage costs, only to compute.
*   **Cloud Spanner Processing Unit Optimization**: Spanner charges per Processing Unit per hour. Monitor Spanner's CPU utilization and throughput metrics in Cloud Monitoring. If CPU utilization is consistently low (< 65% for multi-region), you may have over-provisioned and can reduce Processing Units to save cost.

---

### 2. Certification Exam Tips
*   **Service Selection for Cost**: The exam may present a workload and ask which GCP database service is the most cost-effective. Always consider: Cloud SQL (lowest cost for regional relational), Firestore (no charge for idle databases), BigQuery (pay per query byte scanned, not per instance), Spanner (expensive for low-concurrency workloads — use Cloud SQL instead).
*   **BigQuery Cost Reduction**: The exam frequently tests BigQuery cost optimization. Key techniques: partition tables by date column (partition pruning reduces bytes scanned), cluster tables to further reduce scan range, never use `SELECT *` (always specify columns — columnar storage charges by column scanned), cache query results (repeated identical queries are free within 24 hours).
*   **Cloud SQL Idle Instance Cost**: Development and test Cloud SQL instances that run 24/7 but are only used for a few hours per day waste significant cost. Recommend: use Cloud Scheduler + Cloud Functions to start/stop instances on a schedule, or switch to Cloud SQL's serverless export and BigQuery for ad-hoc dev queries.
*   **Spanner vs. Cloud SQL Cost Decision**: Cloud Spanner starts at $0.90/hour per node (or $0.09/hour per 100 Processing Units). For a workload that fits within Cloud SQL, Spanner can be 10–100x more expensive. Choose Spanner only when the workload genuinely requires its global distribution or >99.999% SLA.
*   **Study Resource:** The official Google Cloud pricing documentation and the Cloud Pricing Calculator are the primary references for cost optimization: [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator). The freeCodeCamp database course covers foundational concepts: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Use *Database Design* by Adrienne Watt to reinforce the capacity planning and architectural concepts that drive cost optimization decisions: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This comprehensive free lecture covers database administration concepts including capacity planning and resource management applicable to GCP cost optimization: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will use Cloud Monitoring to analyze Cloud SQL instance utilization and identify right-sizing opportunities, run BigQuery queries with and without partition filters to measure cost differences using the `--dry_run` flag, review Cloud Spanner CPU utilization to assess over-provisioning, and calculate the ROI of a 1-year CUD for a Cloud SQL production workload.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the capacity planning and architecture chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the database administration and capacity management segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the right-sizing and cost analysis steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
