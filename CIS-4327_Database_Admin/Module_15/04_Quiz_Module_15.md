# Quiz: Module 15 - Database Cost Optimization on GCP
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A data analytics team runs approximately 500 TB of BigQuery queries per month. The queries are distributed evenly throughout the month with no significant peaks. Comparing on-demand pricing ($5/TB) and flat-rate pricing (a 100-slot reservation costs approximately $2,000/month), which pricing model is more cost-effective?
A) On-demand pricing, because 500 TB × $5 = $2,500/month, which is more than a 100-slot flat-rate at $2,000/month.
B) Flat-rate pricing, because it provides unlimited query slots regardless of how many TB are processed.
C) On-demand pricing, because flat-rate reservations are only available for BigQuery Enterprise editions.
D) Both pricing models cost the same, so the team should choose flat-rate for more predictable billing.
*   **Correct Answer:** A) On-demand pricing, because 500 TB × $5 = $2,500/month, which is more than a 100-slot flat-rate at $2,000/month.
*   **Distractor Analysis:**
    *   *Why A is correct:* At $5/TB on-demand, 500 TB = $2,500/month. A flat-rate reservation at $2,000/month costs $500 less. For consistent monthly volumes exceeding approximately 400 TB, flat-rate reservations are more economical. The team should purchase slot reservations.
    *   *Why B is incorrect:* Flat-rate reservations do not provide unlimited slots; you reserve a fixed number of slots (compute capacity). Queries that require more capacity than reserved slots will queue. The cost benefit is predictability and savings on consistent high-volume workloads.
    *   *Why C is incorrect:* BigQuery flat-rate slot reservations are available through BigQuery Reservations and do not require a specific "Enterprise edition." They are a billing model available to any BigQuery project.
    *   *Why D is incorrect:* The two pricing models produce different costs for this workload ($2,500 on-demand vs. $2,000 flat-rate). They are not equal.

---

---

**Question 2**
A Cloud SQL for PostgreSQL instance has been running in production for 6 months. Cloud Monitoring shows that average CPU utilization is consistently 8% and memory utilization is 15%. The instance is currently configured as a `db-custom-8-32768` (8 vCPUs, 32 GB RAM). Which cost optimization action should be taken?
A) Right-size the instance by downgrading to a smaller machine type such as `db-custom-2-7680` (2 vCPUs, 7.5 GB RAM) during a maintenance window, after verifying the application can handle the reduced capacity.
B) Enable Cloud SQL HA to allow load balancing between the primary and standby to improve utilization.
C) Add read replicas to distribute the low utilization across multiple instances.
D) Enable Committed Use Discounts on the current instance without changing the machine type.
*   **Correct Answer:** A) Right-size the instance by downgrading to a smaller machine type during a maintenance window, after verifying the application can handle the reduced capacity.
*   **Distractor Analysis:**
    *   *Why A is correct:* Consistently 8% CPU and 15% memory utilization on an 8-vCPU, 32 GB instance means the workload is significantly over-provisioned. Downgrading to a smaller machine type reduces the per-hour compute cost substantially (potentially 60–75% reduction). Right-sizing is the most impactful cost optimization action when metrics show chronic under-utilization.
    *   *Why B is incorrect:* HA adds a standby instance in a second zone, which doubles the compute cost — the opposite of cost optimization. HA standby instances do not serve read traffic and cannot balance load.
    *   *Why C is incorrect:* Adding read replicas when the primary is at 8% utilization increases cost by adding additional instance hours without solving any capacity problem.
    *   *Why D is incorrect:* Committed Use Discounts reduce the per-hour rate of the current machine type but do not reduce the over-provisioning problem. CUDs are most valuable when the machine type is already correctly sized; applying them to an oversized instance still wastes money, just at a discounted rate.

---

---

**Question 3**
A database cost analyst needs to **estimate the cost of a BigQuery query before running it, to ensure it will not exceed the project's monthly budget**. Which tool or command provides the estimated bytes scanned before query execution?
A) Use the `--dry_run` flag with the `bq query` command or click "Validate" in the BigQuery console to get the bytes estimate without executing the query.
B) Run `EXPLAIN ANALYZE` on the BigQuery query to view the estimated cost in the execution plan.
C) Check the `cloudbilling.googleapis.com/billing_export` metric in Cloud Monitoring before running the query.
D) Create a Cloud Monitoring budget alert set to $0, which will notify immediately when the query begins processing.
*   **Correct Answer:** A) Use the `--dry_run` flag with the `bq query` command or click "Validate" in the BigQuery console to get the bytes estimate without executing the query.
*   **Distractor Analysis:**
    *   *Why A is correct:* The `bq query --dry_run` command submits the query to the BigQuery planner without executing it and returns the estimated bytes that would be processed. The BigQuery console's "Validate" button provides the same estimate. This allows cost-checking queries before they incur charges.
    *   *Why B is incorrect:* `EXPLAIN ANALYZE` is a PostgreSQL/MySQL command that executes a query and shows its execution plan. BigQuery does not have an `EXPLAIN ANALYZE` command; it uses `bq query --dry_run` for pre-execution cost estimation.
    *   *Why C is incorrect:* The Cloud Billing export metric in Cloud Monitoring shows historical billed costs after queries have already been executed; it does not provide pre-execution estimates for individual queries.
    *   *Why D is incorrect:* A budget alert at $0 would trigger every time any billable BigQuery usage occurs, generating constant alerts that are not actionable. It does not provide a per-query cost estimate before execution.

---

**Question 4**
A company runs a Cloud Spanner instance with 5 nodes for a global e-commerce workload. After a seasonal peak, Cloud Monitoring shows that Spanner CPU utilization has dropped to 15% for the past 30 days and is expected to remain low for the next 3 months. What is the most appropriate cost optimization action?
A) Reduce the Spanner instance's node count to 2 or 3 nodes to better match the current workload, saving approximately 40–60% on compute costs for the period.
B) Migrate the Spanner database to Cloud SQL to reduce costs permanently.
C) Purchase a 1-year Committed Use Discount for the current 5-node configuration to lock in a discounted rate.
D) Enable Spanner's autoscaling feature to scale down to 1 node and back up to 5 nodes within seconds when traffic increases.
*   **Correct Answer:** A) Reduce the Spanner instance's node count to 2 or 3 nodes to better match the current workload.
*   **Distractor Analysis:**
    *   *Why A is correct:* Cloud Spanner nodes can be added or removed through the Cloud Console or API without downtime. At 15% CPU utilization, the workload needs 2–3 nodes (leaving headroom for bursts). Reducing from 5 to 2 nodes saves 60% on compute costs. You can scale back up before the next peak.
    *   *Why B is incorrect:* Migrating from Spanner to Cloud SQL is a major architectural change that requires re-evaluating schema design, global distribution needs, and consistency requirements. This is not an appropriate response to a temporary post-peak utilization drop.
    *   *Why C is incorrect:* Purchasing a 1-year CUD for 5 nodes when the current workload only needs 2–3 nodes locks in payment for excess capacity. CUDs should be applied after right-sizing, not instead of it.
    *   *Why D is incorrect:* Cloud Spanner does have an autoscaler, but it does not scale down to 1 node instantaneously; scaling operations take several minutes and Spanner requires a minimum of 1 node (or 100 processing units). The autoscaler is a helpful tool but is not a substitute for manual right-sizing after a sustained utilization change.

---

**Question 5**
When reviewing the cost of a GCP database project, you discover that a Cloud SQL for PostgreSQL instance is storing 2 TB of unused historical data from 2 years ago that is never queried. The compliance team confirms the data must be retained but does not need to be queryable within 1 second. Which action reduces cost while maintaining compliance?
A) Export the historical data to a Cloud Storage nearline or coldline bucket, then delete it from Cloud SQL to reduce database storage costs; retrieve it from Cloud Storage when needed for compliance audits.
B) Enable Cloud SQL storage auto-increase to handle the current 2 TB and future data growth at no additional cost.
C) Create a BigQuery dataset and move the 2 TB to BigQuery, then immediately query it to verify completeness.
D) Apply a Committed Use Discount to the Cloud SQL storage to reduce the per-GB storage rate for the 2 TB.
*   **Correct Answer:** A) Export the historical data to a Cloud Storage nearline or coldline bucket, then delete it from Cloud SQL to reduce database storage costs; retrieve it from Cloud Storage when needed for compliance audits.
*   **Distractor Analysis:**
    *   *Why A is correct:* Cloud SQL storage costs approximately $0.17/GB/month for SSD. Cloud Storage Nearline costs $0.01/GB/month and Coldline costs $0.004/GB/month. Moving 2 TB (2,048 GB) from Cloud SQL to Coldline reduces storage cost from ~$348/month to ~$8/month — a 97% reduction. Since the data only needs to be accessible for compliance audits (not sub-second queries), the retrieval latency of Cloud Storage is acceptable.
    *   *Why B is incorrect:* Storage auto-increase means the Cloud SQL instance will pay for the full 2 TB of storage at Cloud SQL SSD rates indefinitely. Enabling auto-increase does not reduce cost; it adds cost as storage grows.
    *   *Why C is incorrect:* Moving data to BigQuery does reduce the storage to BigQuery's lower rate ($0.02/GB/month for active storage), which is better than Cloud SQL but more expensive than Cloud Storage Coldline. Additionally, if the data will never be queried operationally, BigQuery's query-optimized storage is unnecessary overhead.
    *   *Why D is incorrect:* Committed Use Discounts apply to Cloud SQL compute costs (vCPU and RAM), not to storage costs. Cloud SQL storage is charged separately and cannot be discounted with CUDs.
