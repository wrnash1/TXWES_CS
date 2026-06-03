# Quiz: Module 16 — ACE Exam Preparation

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

Instructions: Select the single best answer for each question. These questions consolidate all five ACE exam domains and mirror the scenario-based format of the Associate Cloud Engineer certification exam.

---

### Question 1

A startup is building a mobile app with a backend API that experiences highly variable traffic — thousands of requests per second at peak and near-zero traffic overnight. The API is stateless. The team wants zero idle-time cost and no infrastructure management. Which GCP service is the best fit?

- A) Compute Engine with a Managed Instance Group and autoscaling set to minimum 0 instances
- B) Cloud Run — fully managed, serverless containers that scale to zero automatically; the team manages no infrastructure and pays only for actual request processing
- C) GKE Autopilot with HPA scaling down to 0 pods during off-peak hours
- D) App Engine Flexible environment with `min_instances: 0` configured in `app.yaml`

Correct Answer: B — Cloud Run is purpose-built for this scenario: stateless containers, serverless management, automatic scale-to-zero, and per-request billing. MIGs cannot scale to zero (minimum 1 VM). GKE Autopilot charges for the cluster control plane even with zero pods. App Engine Flexible requires at least one container instance running at all times and does not support `min_instances: 0`.

Distractor Analysis:

- Why A is incorrect: Managed Instance Groups support minimum size of 0 only in specific configurations (zonal MIGs with autoscaling enabled and minimum replicas explicitly set to 0), but VMs take minutes to start — not suitable for serverless-style instant scaling. Additionally, the VM-based model still requires OS management.
- Why C is incorrect: GKE Autopilot scales pods to zero but does not eliminate control plane costs. The cluster itself remains running and billable even with no workloads. The team also manages Kubernetes manifests, which constitutes significant infrastructure management.
- Why D is incorrect: App Engine Flexible environment does not support scaling to zero. The Flexible environment uses Compute Engine VMs as the underlying runtime and requires at least one instance to be running at all times. App Engine Standard (not Flexible) supports scale-to-zero.

---

### Question 2

A security engineer needs to prevent all GCP projects in an organization from creating VM instances with external IP addresses, regardless of individual project-level IAM configurations. What is the correct control to use?

- A) Create a VPC firewall rule in each project's default VPC that blocks all ingress traffic from external IPs
- B) Set the `compute.vmExternalIpAddress` Organization Policy constraint at the Organization node to deny all values; this applies to all projects in the organization and cannot be overridden by project-level IAM policies
- C) Grant only `roles/compute.instanceAdmin.v1` (not `roles/compute.networkAdmin`) to all engineers, preventing them from assigning external IPs
- D) Use VPC Service Controls to create a service perimeter that blocks Compute Engine API access from external IPs

Correct Answer: B — Organization Policies are the correct mechanism for enforcing restrictions across an entire GCP organization regardless of IAM. `compute.vmExternalIpAddress` set to deny at the Organization node applies to every project in the organization. Project owners and IAM admins cannot override an Organization Policy set at a higher level. Firewall rules control traffic but not IP assignment. IAM roles can be modified by IAM admins with sufficient permissions. VPC Service Controls protect API access patterns, not resource IP configuration.

Distractor Analysis:

- Why A is incorrect: VPC firewall rules block network traffic flows, not the assignment of external IP addresses. A VM can have an external IP assigned even if firewall rules block all traffic to that IP. Additionally, project admins can modify their project's firewall rules.
- Why C is incorrect: `roles/compute.instanceAdmin.v1` does include the ability to assign external IPs when creating instances. The ACL for IP assignment is part of the compute instance creation permissions, not a separate network admin permission. Additionally, users with project Owner or Editor roles could still assign external IPs.
- Why D is incorrect: VPC Service Controls create perimeters around GCP API services to prevent data exfiltration between service perimeters. They do not control whether VMs are configured with external IPs during resource creation.

---

### Question 3

A GCP administrator needs to connect their on-premises data center to GCP to transfer 8 Gbps of data between on-premises databases and Cloud SQL. The connection must be private (not over the public internet) and must have low latency. The company has budget for a premium solution. What connectivity option is best?

- A) Cloud VPN HA configuration with two 3 Gbps tunnels providing 6 Gbps combined bandwidth
- B) Dedicated Cloud Interconnect providing a 10 Gbps dedicated circuit between the on-premises data center and a Google peering location — private, low-latency, and meeting the 8 Gbps requirement
- C) Partner Cloud Interconnect with a 50 Mbps connection via a network service provider
- D) Cloud VPN Classic configuration with BGP routing and jumbo frames enabled for maximum throughput

Correct Answer: B — Dedicated Cloud Interconnect provides 10 or 100 Gbps dedicated private circuits directly to Google's network. It satisfies all three requirements: 8+ Gbps bandwidth (10 Gbps circuit), private connection (does not traverse the public internet), and low latency (dedicated circuit with no public internet hops). HA VPN maximum throughput is 3 Gbps per tunnel (the "two tunnels providing 6 Gbps" in Option A is incorrect — tunnels do not combine bandwidth this way). Partner Interconnect at 50 Mbps is far below the 8 Gbps requirement.

Distractor Analysis:

- Why A is incorrect: HA VPN provides 99.99% availability via two tunnels, but bandwidth does not aggregate across tunnels. Each tunnel provides up to 3 Gbps, and traffic does not load-balance across both simultaneously in a simple additive manner. Maximum sustained throughput for a single HA VPN tunnel is approximately 3 Gbps — insufficient for an 8 Gbps requirement.
- Why C is incorrect: Partner Interconnect at 50 Mbps is orders of magnitude below the 8 Gbps requirement. Partner Interconnect can support up to 50 Gbps via aggregated connections, but the scenario specifies 50 Mbps, which is inadequate.
- Why D is incorrect: Classic VPN does not support higher throughput than HA VPN (both max at approximately 3 Gbps per tunnel). Jumbo frames affect per-packet overhead but do not multiply tunnel bandwidth capacity. Classic VPN also provides only 99.9% SLA vs. HA VPN's 99.99%.

---

### Question 4

A Compute Engine VM running a Python application consistently receives `403 Forbidden` errors when calling the Cloud Storage API, despite the service account being granted `roles/storage.objectAdmin` on the bucket. The VM was created with the following command: `gcloud compute instances create app-vm --service-account=app-sa@project.iam.gserviceaccount.com --scopes=logging-write,monitoring`. What is the cause and fix?

- A) `roles/storage.objectAdmin` is not a valid Cloud Storage role — use `roles/storage.admin` instead
- B) The VM's access scopes (`--scopes=logging-write,monitoring`) do not include Cloud Storage access; even with the correct IAM role on the service account, API calls are blocked because Compute Engine access scopes are a second authorization layer; recreate the VM with `--scopes=cloud-platform` or `--scopes=storage-full`
- C) The service account needs to be added to the `storage-admins` group in Google Workspace before Cloud Storage API calls will succeed
- D) The Python application must use the service account JSON key file — the attached service account is not used for API calls made from application code

Correct Answer: B — Compute Engine VMs have two authorization layers: the IAM role on the service account (which controls what the identity is permitted to do) AND the access scopes on the VM (which control which GCP APIs the VM's code can call). Access scopes are set at VM creation and cannot be changed without stopping the VM and editing it (in some cases requiring VM recreation). `logging-write` and `monitoring` scopes do not include Cloud Storage. The fix is to use `--scopes=cloud-platform` (grants all APIs, relying on IAM for actual access control) or `--scopes=storage-full` for Cloud Storage specifically.

Distractor Analysis:

- Why A is incorrect: `roles/storage.objectAdmin` is a valid and commonly used Cloud Storage predefined role that grants full control over objects (read, write, delete) but not bucket-level administrative operations. The role is not the cause of the error.
- Why C is incorrect: Service accounts do not join Google Groups to gain permissions — they receive IAM bindings directly or inherit from groups they are added to. There is no `storage-admins` built-in group that grants Cloud Storage API access. This answer describes an incorrect mechanism.
- Why D is incorrect: When a VM has an attached service account, application code using GCP client libraries automatically uses Application Default Credentials (ADC), which detects and uses the attached service account. No JSON key file is needed for VMs with attached service accounts. The JSON key file pattern is for non-GCP environments.

---

### Question 5

A team manages a multi-project GCP organization. They want all application logs from three production projects consolidated into a single Cloud Logging project for centralized analysis. What configuration achieves this?

- A) Install Fluentd agents on all VMs in the three projects and configure them to forward logs to the central project
- B) In each of the three production projects, create a log sink with the destination set to a log bucket in the central logging project; grant the sink's writer service account `roles/logging.bucketWriter` on the destination log bucket
- C) Enable VPC peering between the three production projects and the logging project so Cloud Logging can share data across projects
- D) Configure Cloud Monitoring to forward all log-based metric data from the three projects to the central project's workspace

Correct Answer: B — Cloud Logging log sinks support cross-project log routing. Each production project creates a log sink targeting a log bucket in the central project. The sink's service account (auto-created per sink) must be granted `roles/logging.bucketWriter` on the destination log bucket. This is the GCP-native pattern for log centralization without installing custom agents or modifying application code.

Distractor Analysis:

- Why A is incorrect: Fluentd agents can forward logs, but this requires installation on every VM, custom configuration, and ongoing maintenance. GCP's native log sink mechanism is simpler, more reliable, and works for all log types (not just VM application logs) including service logs from serverless products.
- Why C is incorrect: VPC peering connects networks for traffic routing, not for log sharing between Cloud Logging instances. Cloud Logging log routing is an application-layer configuration, not a network configuration.
- Why D is incorrect: Cloud Monitoring workspaces can monitor metrics across multiple projects, but this is for metrics (numerical time-series data), not logs (structured event records). Cloud Monitoring does not forward raw log data between projects.

---

### Question 6

A Cloud SQL PostgreSQL instance is experiencing high read latency due to heavy analytical query load. The write workload is moderate. How can read latency be reduced without changing the primary instance configuration?

- A) Enable Cloud SQL automatic storage increase — more storage IOPS will reduce query latency
- B) Create a Cloud SQL read replica in the same region as the primary instance; route all analytical (read-only) queries to the replica's IP address
- C) Enable Cloud CDN on the Cloud SQL instance to cache frequently queried results at the edge
- D) Migrate the database to Cloud Spanner — Spanner provides lower read latency for relational workloads

Correct Answer: B — Cloud SQL read replicas are exact replicas of the primary instance that serve read-only queries. By routing analytical queries to the replica, read load is offloaded from the primary, reducing its latency for both reads and writes. Read replicas can be created in the same or different region. This is the standard pattern for read scaling in Cloud SQL without modifying the primary instance.

Distractor Analysis:

- Why A is incorrect: Automatic storage increase provisions additional storage capacity to prevent the disk from filling up — it does not increase IOPS per se. Storage tier determines IOPS in Cloud SQL, and automatically expanded storage does not change the storage type. More storage can increase IOPS on SSD storage, but this is not the straightforward solution to read latency from analytical queries.
- Why C is incorrect: Cloud CDN caches HTTP responses at Google edge locations. It is not applicable to database connections — Cloud SQL does not serve HTTP responses. CDN cannot cache SQL query results.
- Why D is incorrect: Migrating to Cloud Spanner is a significant, disruptive change that would require application refactoring. It is not proportionate to a read latency problem that can be solved with a read replica. Spanner also has a substantially different cost profile. The question asks how to reduce latency "without changing the primary instance configuration."

---

### Question 7

An organization's GKE application needs to access a Cloud Storage bucket. The cluster admin wants to avoid downloading or storing service account JSON key files. What is the recommended authentication approach?

- A) Mount the service account JSON key as a Kubernetes Secret and reference it via the `GOOGLE_APPLICATION_CREDENTIALS` environment variable in the pod
- B) Enable Workload Identity on the GKE cluster; create a GCP IAM service account with the required Cloud Storage role; bind it to the Kubernetes service account used by the pod using `iam.workloadIdentityUser` binding; configure the pod to use the Kubernetes service account — the GKE metadata server automatically exchanges the Kubernetes service account token for a GCP access token
- C) Grant `roles/storage.objectViewer` to the Compute Engine default service account; GKE node pools use the default service account and pods inherit its permissions
- D) Use the Cloud Storage HMAC key authentication method — generate HMAC keys for the service account and provide them as environment variables to the pod

Correct Answer: B — Workload Identity is the GCP-recommended, key-free authentication method for GKE workloads. It eliminates the security risk of JSON key files (long-lived credentials that can be stolen from Kubernetes Secrets or container images). Workload Identity binds a Kubernetes service account (namespace-scoped identity) to a GCP IAM service account, allowing the GKE metadata server to issue short-lived GCP access tokens automatically to pods using the bound Kubernetes service account.

Distractor Analysis:

- Why A is incorrect: Storing JSON key files as Kubernetes Secrets is the legacy approach explicitly deprecated in favor of Workload Identity. Kubernetes Secrets are base64-encoded (not encrypted) by default in etcd, making them accessible to anyone who can read Secrets in the namespace. This approach introduces the exact key management risk the question asks to avoid.
- Why C is incorrect: Granting permissions to the Compute Engine default service account is an anti-pattern. The default service account often has broad Editor-level permissions. Granting it additional permissions and relying on all node pool VMs and pods to share a single identity violates the principle of least privilege and provides no per-workload isolation.
- Why D is incorrect: HMAC keys are used for Cloud Storage interoperability with S3-compatible tools and APIs. They are long-lived credentials that must be stored and managed — the same problem as JSON key files. HMAC key authentication is not the recommended approach for GKE-to-Cloud-Storage authentication.

---

### Question 8

A Cloud Run service returns HTTP 200 for most requests but occasionally returns HTTP 500 errors. The team wants to be alerted whenever the error rate exceeds 1% over a 5-minute window. What is the correct configuration?

- A) Enable Cloud Trace on the Cloud Run service — trace data includes error rates and can trigger alerts
- B) Create a log-based metric in Cloud Logging with a filter for Cloud Run request logs where `httpRequest.status >= 500`; create a Cloud Monitoring alerting policy that triggers when the metric count divided by total request count exceeds 1% for 5 minutes
- C) Create a Cloud Monitoring uptime check on the Cloud Run service URL — uptime checks detect 500 errors
- D) Use Cloud Profiler to monitor error rates — profiling data includes HTTP error distributions

Correct Answer: B — Log-based metrics convert Cloud Logging log entries into Cloud Monitoring time-series metrics. Cloud Run logs all HTTP requests including status codes. A filter for `httpRequest.status >= 500` counts error responses; dividing by total request count gives the error rate. A Cloud Monitoring alerting policy evaluates this metric over a 5-minute window and triggers when the threshold is exceeded. This is the standard GCP pattern for error rate alerting on serverless services.

Distractor Analysis:

- Why A is incorrect: Cloud Trace provides distributed tracing data — it records request latency across service calls. While traces include status codes, Cloud Trace is not designed for metric-based alerting on error rates. It is an analysis tool for investigating specific slow requests.
- Why C is incorrect: Cloud Monitoring uptime checks send synthetic requests (one check per minute) to verify the service is reachable. They detect sustained outages (the service is completely down) but are not designed to detect intermittent 500 errors at a 1% rate across real production traffic.
- Why D is incorrect: Cloud Profiler continuously samples CPU and memory usage for performance profiling. It does not track HTTP status codes or error rates. It is a performance optimization tool, not an error monitoring tool.

---

### Question 9

A company is running a batch job that processes images stored in Cloud Storage. The job runs daily for 4 hours and can be restarted from a checkpoint if interrupted. Currently using standard on-demand Compute Engine VMs at significant monthly cost. What change reduces cost most significantly?

- A) Purchase 1-year Committed Use Discounts for the VMs — CUDs provide up to 37% off for 1-year commitments
- B) Switch the batch VMs to Spot VMs — the job's checkpointing capability means interruptions are recoverable; Spot VMs provide up to 91% discount over on-demand pricing for interruptible workloads
- C) Migrate the batch job to App Engine Standard with automatic scaling — App Engine Standard is cheaper than Compute Engine for batch processing
- D) Enable Sustained Use Discounts on the VMs — running for 4 hours daily qualifies for SUD discounts

Correct Answer: B — The batch job is an ideal Spot VM workload: it runs for a defined duration, it can be restarted from a checkpoint (tolerating preemption), and the 91% discount over on-demand pricing provides by far the greatest cost reduction. CUDs require a commitment for the VMs to run continuously — a 4-hour daily job does not have continuous usage to commit. SUDs require more than 25% of the month (approximately 180 hours); a 4-hour daily job runs about 120 hours/month — below the 25% threshold.

Distractor Analysis:

- Why A is incorrect: CUDs require committing to continuous resource usage for 1 or 3 years. A batch job that runs 4 hours/day (120 hours/month = ~16% of the month) is not a good CUD candidate — you would be paying for committed resources that sit idle 84% of the time. CUDs are designed for continuously running workloads.
- Why C is incorrect: App Engine Standard is designed for web applications and APIs, not batch image processing jobs. It does not provide a lower-cost alternative for compute-intensive image processing. App Engine Standard has strict sandbox limitations that would prevent many image processing operations.
- Why D is incorrect: Sustained Use Discounts apply automatically when a VM runs more than 25% of a calendar month (approximately 180 hours). A VM running 4 hours/day × 30 days = 120 hours/month is approximately 16% of the month — below the SUD threshold. No SUD discount would apply.

---

### Question 10

A GCP project has a Cloud Storage bucket containing sensitive customer data. An internal audit finds that `allUsers` has `roles/storage.objectViewer` on the bucket. What is the security impact, and what is the immediate remediation?

- A) `allUsers` means all authenticated GCP users — only Verizon employees can access the data; no remediation is required
- B) `allUsers` means all internet users without authentication — the bucket is publicly readable by anyone on the internet; immediately remove the `allUsers` IAM binding using `gsutil iam ch -d allUsers:roles/storage.objectViewer gs://BUCKET_NAME`
- C) `allUsers` in IAM means all users in the organization's Google Workspace domain — external access is blocked; no immediate risk
- D) `allUsers` means all users who have authenticated with any Google account; change the binding to `allAuthenticatedUsers` to limit access to logged-in users

Correct Answer: B — In GCP IAM, `allUsers` is a special identifier that means all internet users — including completely unauthenticated users with no Google account. Any object in the bucket is publicly readable by anyone who knows the object URL or can enumerate the bucket contents. This is a critical data exposure finding. Immediate remediation is to remove the `allUsers` binding to restore private access.

Distractor Analysis:

- Why A is incorrect: `allUsers` does not mean all authenticated GCP users. `allAuthenticatedUsers` means all users authenticated with a Google account. `allUsers` means literally all internet users — no authentication required.
- Why C is incorrect: `allUsers` is not scoped to an organization's Workspace domain. Domain-restricted sharing (limiting to specific domains) uses the `domain:DOMAIN` member type in IAM (e.g., `domain:example.com`), which requires authentication with that domain. `allUsers` has no domain restriction whatsoever.
- Why D is incorrect: This describes the difference between `allUsers` and `allAuthenticatedUsers`. The question's `allUsers` means unauthenticated public access. `allAuthenticatedUsers` would require at minimum a Google account — a partial improvement but still inappropriate for sensitive customer data. The correct answer is to remove public access entirely.
