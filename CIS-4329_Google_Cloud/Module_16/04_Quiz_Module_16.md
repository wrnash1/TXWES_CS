# Quiz: Module 16 – Final Exam Prep and Google Cloud ACE Certification Review
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
A retail company runs a global e-commerce platform. The application tier consists of stateless web servers deployed as a Managed Instance Group. The database tier is a 500 GB MySQL database. The company needs: (a) automatic VM replacement if a web server crashes, (b) the ability to scale the web tier up and down based on HTTP request load, and (c) automatic failover for the database if the primary zone goes offline. Which combination of GCP features satisfies all three requirements?

A) A Managed Instance Group with autohealing and autoscaling for the web tier; Cloud SQL for MySQL with a high availability (regional) configuration for the database tier.
B) A Managed Instance Group with autohealing for the web tier; a Cloud SQL read replica in a second zone for the database failover.
C) GKE Autopilot with a Horizontal Pod Autoscaler for the web tier; Cloud Spanner for the database tier.
D) A single large Compute Engine VM with a startup script that restarts crashed processes; Cloud SQL for MySQL with automated backups for the database tier.

*   **Correct Answer:** A) A Managed Instance Group with autohealing and autoscaling for the web tier; Cloud SQL for MySQL with a high availability (regional) configuration for the database tier.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* A Cloud SQL read replica uses asynchronous replication and does not provide automatic failover. If the primary instance fails, the read replica does not automatically promote to primary — high availability (regional) configuration is required for automatic failover.
    *   *Why C is incorrect:* GKE Autopilot with HPA would work for the web tier, but Cloud Spanner is a globally distributed database designed for horizontal scale at high cost. A 500 GB MySQL workload does not need Spanner — Cloud SQL is the appropriate and far more cost-effective choice.
    *   *Why D is incorrect:* A startup script restarting crashed processes is not autohealing — if the VM itself becomes unresponsive, the startup script cannot run. MIG autohealing uses a health check to detect and replace unhealthy VMs. Automated backups restore data after a failure but do not provide automatic failover — they require manual intervention to restore.

---

**Question 2**
Your organization has three GCP projects: `proj-dev`, `proj-staging`, and `proj-production`. You need to enforce an Organization Policy that prevents any Compute Engine VM in any of these projects from being assigned an external IP address. The policy must apply automatically to any new projects created in the future. At which level should you apply the Organization Policy?

A) Apply the policy to each of the three projects individually using `gcloud resource-manager org-policies set-policy`.
B) Apply the policy at the Organization level — it will automatically inherit to all current and future folders and projects within the organization.
C) Apply the policy at the billing account level so that it covers all projects linked to the same billing account.
D) Apply the policy to each project's default VPC network using a VPC-level access control configuration.

*   **Correct Answer:** B) Apply the policy at the Organization level — it will automatically inherit to all current and future folders and projects within the organization.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Applying the policy to each project individually means new projects created in the future will not have the policy until someone manually applies it. The organization level is the correct scope for a policy that must apply universally and automatically.
    *   *Why C is incorrect:* Organization Policies are applied to resources in the GCP resource hierarchy (Organization → Folders → Projects → Resources). Billing accounts are not part of the resource hierarchy for policy inheritance — they are financial constructs. You cannot apply an Organization Policy at the billing account level.
    *   *Why D is incorrect:* VPC network configurations control network traffic routing and firewall rules — they cannot enforce restrictions on VM configuration properties like external IP assignment. Organization Policies are the correct mechanism for restricting resource configuration across projects.

---

**Question 3**
You are designing a data processing pipeline. Raw event data arrives via HTTP from external sources at an unpredictable rate — sometimes 100 events per second, sometimes 10,000 events per second. A downstream processing service needs to consume events at a steady rate it can handle. You need a component between the ingest layer and the processing layer that can absorb traffic spikes and decouple the two services. Which GCP service fills this role?

A) A Global HTTP(S) Load Balancer between the ingest endpoints and the processing service.
B) Cloud Pub/Sub — ingest events publish to a topic, and the processing service subscribes with a pull subscription to consume at its own rate.
C) Cloud Storage — write each event as an object, and the processing service polls the bucket on a schedule.
D) Cloud Spanner — write incoming events to a globally distributed table and have the processing service query for new rows.

*   **Correct Answer:** B) Cloud Pub/Sub — ingest events publish to a topic, and the processing service subscribes with a pull subscription to consume at its own rate.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A load balancer distributes traffic across multiple backend instances — it does not buffer or queue messages. If the processing service cannot keep up with 10,000 requests per second, the load balancer will still forward all requests to the backends, which may become overwhelmed. Pub/Sub holds messages until the subscriber is ready to consume them.
    *   *Why C is incorrect:* Writing each event as a Cloud Storage object at high ingest rates creates millions of small objects, generates excessive Class A operation costs, and introduces significant latency. Polling on a schedule also means the processing service cannot react in near-real-time. Pub/Sub is purpose-built for high-throughput event streaming.
    *   *Why D is incorrect:* Cloud Spanner is a globally distributed relational database optimized for transactional workloads with strong consistency. Using it as a message queue by polling for new rows is an anti-pattern — it is expensive, requires careful row-key design to avoid hotspots, and does not have native acknowledgment semantics that prevent double-processing.

---

**Question 4**
A cloud operations engineer receives a page at 2:00 AM: users cannot access the web application. The application runs on Compute Engine VMs behind a Global HTTP(S) Load Balancer. The engineer checks Cloud Monitoring and sees that the load balancer's backend health check is failing for all VMs. The VMs were running normally 30 minutes ago. Which troubleshooting step should the engineer take first to diagnose why the health checks are failing?

A) Delete and recreate all VMs in the Managed Instance Group from the latest snapshot.
B) Use the Cloud Console's VM Serial Console or SSH to connect to one of the VMs, check if the web server process is running (`systemctl status nginx` or equivalent), and review the application logs for errors.
C) Change the health check protocol from HTTP to TCP to bypass application-layer checks while the investigation continues.
D) Increase the health check failure threshold from 2 to 10 consecutive failures so the VMs are not marked unhealthy during the investigation.

*   **Correct Answer:** B) Use the Cloud Console's VM Serial Console or SSH to connect to one of the VMs, check if the web server process is running and review the application logs for errors.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Deleting and recreating VMs is a destructive action that destroys any diagnostic information (logs, core dumps, memory state) that could help identify the root cause of the failure. Always diagnose before taking destructive remediation steps.
    *   *Why C is incorrect:* Changing the health check protocol to TCP would cause the load balancer to mark VMs as healthy if the TCP port is open — even if the application is returning errors. This restores traffic to broken backends and hides the problem from users in the opposite way: users get errors instead of seeing an outage. It does not diagnose the root cause.
    *   *Why D is incorrect:* Increasing the failure threshold delays how quickly unhealthy VMs are removed from rotation but does not diagnose or fix the underlying problem. It also means users continue receiving errors from unhealthy backends for longer. Diagnosing the root cause is always the first step.

---

**Question 5**
You are preparing to take the Google Cloud Associate Cloud Engineer exam. You have completed all 16 modules of this course and scored above 80% on most quizzes. Which final preparation steps are most likely to improve your exam performance?

A) Memorize every `gcloud` command flag and option listed in the official documentation — the exam tests exact syntax.
B) Review the official ACE exam guide to understand domain weights, retake quizzes from modules where you scored below 80%, work through Google's official sample questions, and practice hands-on in the Cloud Console to build familiarity with the actual interface.
C) Focus exclusively on Compute Engine and IAM — these are the only two domains that matter for the ACE exam.
D) Schedule the exam immediately without additional preparation — the course content is sufficient and additional study has diminishing returns.

*   **Correct Answer:** B) Review the official ACE exam guide to understand domain weights, retake quizzes from modules where you scored below 80%, work through Google's official sample questions, and practice hands-on in the Cloud Console to build familiarity with the actual interface.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The ACE exam is scenario-based and does not test exact command flag memorization. You will never be asked "what is the exact flag to set the number of nodes?" — you will be asked which command accomplishes a described task. Understanding what commands do and when to use them is far more important than memorizing exact syntax.
    *   *Why C is incorrect:* The ACE exam covers six major domain areas with roughly equal weighting: setting up environments, planning compute, planning storage, managing networks, deploying solutions, and monitoring. Focusing exclusively on two domains leaves you underprepared for the majority of exam questions covering networking, storage, serverless, databases, security, and cost management.
    *   *Why D is incorrect:* While this course provides comprehensive preparation, hands-on practice in the Cloud Console and working through official Google sample questions are consistently the most effective final preparation steps cited by candidates who pass the ACE exam. These activities build pattern recognition for the scenario-based question style and reveal any remaining knowledge gaps before exam day.
