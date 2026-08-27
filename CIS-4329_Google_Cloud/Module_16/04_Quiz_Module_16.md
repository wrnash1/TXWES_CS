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

---

### Question 11 (5 points)

A GCP project uses a custom VPC. An engineer creates a new Compute Engine VM but the VM cannot reach the internet or other VMs in the same VPC. No firewall rules have been configured yet. What is the most likely cause?

- A) The VM does not have a public IP address — external IP is required for VMs to communicate within a VPC
- B) Custom VPCs do not have default firewall rules; without explicit allow rules, all ingress and egress traffic is implicitly denied by the VPC's implied deny rule
- C) The VM is in the wrong zone — VMs can only communicate with other VMs in the same zone
- D) Custom VPCs require VPC peering to be enabled before any VM-to-VM communication is allowed

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) External IP addresses are for communication outside GCP's network (to the public internet). VMs in the same VPC communicate via internal IP regardless of whether they have external IPs. The absence of an external IP affects internet reachability but not intra-VPC communication.
  - C) VMs in the same VPC subnet can communicate regardless of zone. VPC networks span all zones in a region; zone isolation applies to infrastructure availability, not networking.
  - D) VPC peering connects two separate VPC networks. VMs within the same VPC do not require peering — they share the same network by definition.

---

### Question 12 (5 points)

An organization's GKE cluster runs workloads that require reading from Cloud Spanner. Currently the node pool's default service account is `[project-number]-compute@developer.gserviceaccount.com` and the pods are failing with `PERMISSION_DENIED` errors. The simplest secure fix that follows GCP best practices is:

- A) Grant `roles/spanner.databaseReader` to the Compute Engine default service account at the project level
- B) Enable Workload Identity on the cluster; create a dedicated GCP service account with `roles/spanner.databaseReader`; bind it to the Kubernetes service account used by the pods; remove any Spanner permissions from the default Compute Engine service account
- C) Add the Spanner API scope (`https://www.googleapis.com/auth/spanner.data`) to the GKE node pool and restart the pool
- D) Generate a service account JSON key with `roles/spanner.databaseReader` and mount it as a Kubernetes Secret in the pod

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Granting permissions to the Compute Engine default service account grants those permissions to every VM and pod in the project that uses the default service account — a violation of least privilege. If any other pod is compromised, it could also access Spanner.
  - C) Adding an OAuth scope to the node pool expands what all pods on those nodes can access and still requires the service account to have the IAM role. More importantly, this approach grants Spanner scope to all pods on the node — not just the intended workload. Workload Identity is the more granular and secure solution.
  - D) JSON key files are long-lived credentials that can be leaked from Kubernetes Secrets (which are only base64-encoded by default). Workload Identity eliminates the need for key files entirely and is the GCP-recommended approach.

---

### Question 13 (5 points)

A team runs a Cloud Composer (Apache Airflow) DAG on a nightly schedule that queries BigQuery and writes results to Cloud Storage. The DAG is failing with a quota exceeded error specifically for BigQuery concurrent interactive query slots. What is the most appropriate resolution?

- A) Switch the BigQuery queries from interactive to batch priority — batch queries are queued and do not consume interactive slot quota
- B) Increase the number of Cloud Composer worker nodes so more queries can run in parallel
- C) Move the BigQuery dataset to a different region with higher default quota
- D) Purchase BigQuery flat-rate slots and assign them to a reservation for the Cloud Composer project

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud Composer worker nodes process Airflow task scheduling and execution. Adding more workers increases DAG task parallelism but does not change the BigQuery query slot quota. The quota error is in BigQuery, not in Composer's capacity to execute tasks.
  - C) BigQuery interactive query quotas are per-project and are not region-dependent in a way that moving a dataset would resolve. Regional quotas apply to specific operations but the concurrent interactive query limit is project-wide.
  - D) Purchasing flat-rate slots resolves slot capacity for high-volume predictable workloads. However, switching to batch priority (Option A) is simpler, free, and directly addresses the "concurrent interactive query" quota issue by moving queries out of the interactive quota pool.

---

### Question 14 (5 points)

A GCP organization administrator wants to ensure that all new GCP projects created in the organization automatically inherit a specific set of firewall rules that block outbound connections to known malicious IP ranges. What is the correct architectural approach?

- A) Create a firewall rule in each project after it is created using a manual checklist
- B) Use a Terraform module in a CI/CD pipeline that is triggered whenever a new project is detected via Cloud Asset Inventory change events
- C) Use a Shared VPC — attach all projects to a host project that contains the organization-wide firewall rules; Shared VPC firewall rules in the host project apply to all service projects
- D) Set a Cloud Billing budget alert that notifies the security team when a new project is created so they can manually apply rules

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Manual checklists are error-prone and do not ensure automatic inheritance. A new project could be used for days before the security team applies the firewall rules.
  - B) Terraform in a CI/CD pipeline is a valid IaC approach but is more complex to implement and maintain than Shared VPC. It also introduces a window between project creation and Terraform run during which the project has no firewall rules.
  - D) Cloud Billing budgets track spending, not resource creation events. Budget alerts cannot be configured to fire on new project creation.

---

### Question 15 (5 points)

An engineer runs `gcloud container clusters create my-cluster --zone=us-central1-a --num-nodes=3` and the command returns an error: `Insufficient regional quota to satisfy request: resource "CPUS" ... needed 6, available 4`. What is the cause and resolution?

- A) The GKE cluster node machine type requires more than 4 vCPUs per node; switch to a smaller machine type
- B) The GCP project has a CPU quota limit of 4 vCPUs in us-central1; the requested 3 nodes × default 2 vCPU machine type (e2-medium) = 6 vCPUs exceeds the regional quota; request a quota increase via the Cloud Console Quotas page
- C) The `--num-nodes=3` flag requires a minimum of 9 vCPUs; reduce to `--num-nodes=2`
- D) The zone us-central1-a has reached capacity; retry in us-central1-b

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The error specifically says the project needs 6 CPUs but only 4 are available in the quota. This is a project-level CPU quota limit, not a machine-type sizing issue. The default machine type for GKE clusters is e2-medium (2 vCPUs), so 3 nodes × 2 vCPUs = 6 vCPUs.
  - C) The vCPU count is determined by the number of nodes × vCPUs per node machine type, not by a per-node fixed requirement. There is no 9-vCPU minimum for `--num-nodes=3`.
  - D) Zone capacity exhaustion produces a different error message (ZONE_RESOURCE_POOL_EXHAUSTED or similar). A quota error explicitly names the quota resource and shows needed vs. available counts — this is a project quota issue, not zone capacity.

---

### Question 16 (5 points)

A company is planning to move their application from AWS to GCP. In AWS, they use Auto Scaling Groups with Launch Templates. What is the equivalent GCP construct for managing a group of identical VMs that automatically scales based on load?

- A) GKE node pools with Cluster Autoscaler
- B) Managed Instance Groups (MIGs) with autoscaling configured via an instance template — the instance template defines the VM configuration and the MIG manages scaling based on CPU utilization, load balancing metrics, or Cloud Monitoring metrics
- C) Cloud Run services with concurrency-based scaling
- D) App Engine Standard with `automatic_scaling` configuration in `app.yaml`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) GKE node pools with Cluster Autoscaler manage the VMs that run GKE worker nodes, but the application runs in containers on top of those nodes. This adds a Kubernetes orchestration layer that is not equivalent to the simpler VM-level Auto Scaling Group pattern.
  - C) Cloud Run is a serverless container platform, not a VM management service. It does not use instance templates or manage Compute Engine VMs — it manages container instances on Google's managed infrastructure.
  - D) App Engine Standard is a platform-as-a-service for web applications with specific language runtimes. It does not provide control over individual VM instances, machine types, or the level of configuration flexibility offered by instance templates.

---

### Question 17 (5 points)

A team needs to store application configuration data that changes infrequently and must be accessible to Cloud Run services with sub-millisecond latency reads. The data is key-value pairs (approximately 500 KB total). What GCP service is most appropriate?

- A) Cloud Storage — store configuration as a JSON file and read it on each request
- B) Cloud Spanner — use Spanner's globally consistent relational model for configuration data
- C) Memorystore for Redis — store configuration as Redis hash or string values; Cloud Run services read from Memorystore via Serverless VPC Access with microsecond-level latency
- D) Firestore — store configuration as a Firestore document and use the Firestore client SDK for real-time updates

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Cloud Storage reads involve HTTP API calls with typical latency in the range of tens to hundreds of milliseconds — far above sub-millisecond. Reading configuration from Cloud Storage on every request would add significant latency to each application request.
  - B) Cloud Spanner is a globally distributed relational database optimized for large-scale transactional workloads. Its query latency is typically single-digit milliseconds for simple lookups — fast, but not sub-millisecond. It is also significantly over-engineered for 500 KB of infrequently changing configuration data.
  - D) Firestore provides single-digit millisecond read latency for document reads, which is close to the requirement. However, Memorystore (Redis) specifically provides sub-millisecond in-memory access and is the canonical GCP service for low-latency key-value lookups. Firestore is better suited for real-time sync to mobile/web clients than for application configuration caching.

---

### Question 18 (5 points)

A Cloud Build pipeline fails at the step that deploys a container image to Cloud Run. The error in the build logs is: `ERROR: (gcloud.run.deploy) PERMISSION_DENIED: Permission 'run.services.create' denied on resource`. What is the correct fix?

- A) Add `--allow-unauthenticated` to the Cloud Run deploy command — the permission error is caused by authentication, not authorization
- B) Grant `roles/run.admin` (or `roles/run.developer`) to the Cloud Build service account (`[PROJECT_NUMBER]@cloudbuild.gserviceaccount.com`) at the project level
- C) Enable the Cloud Run API in the project — the permission denied error means the API is not enabled
- D) Grant `roles/owner` to the Cloud Build service account to ensure it has all permissions

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `--allow-unauthenticated` controls whether end-users can invoke the Cloud Run service without authentication. It does not affect Cloud Build's permission to create or update the service itself. The error is a Cloud Build IAM authorization error during deployment, not an invocation authentication issue.
  - C) If the Cloud Run API were not enabled, the error would be `SERVICE_DISABLED: The API is not enabled` or similar. A `PERMISSION_DENIED` on `run.services.create` specifically means the API is reachable but the calling identity lacks the IAM permission.
  - D) Granting `roles/owner` to the Cloud Build service account violates least privilege. The correct fix grants only the Cloud Run deployment permission needed (`roles/run.admin` or `roles/run.developer`). Granting Owner access to a CI/CD service account gives it full destructive control over all project resources.

---

### Question 19 (5 points)

A GCP organization has enabled VPC Service Controls and created a service perimeter around three projects containing sensitive BigQuery datasets. A data analyst in a project outside the perimeter needs read access to a specific BigQuery table inside the perimeter. What is the correct way to grant this access without moving the analyst's project into the perimeter?

- A) Grant `roles/bigquery.dataViewer` on the specific table to the analyst — IAM grants override VPC Service Controls
- B) Create an Access Level in VPC Service Controls that allows the analyst's identity; add an ingress rule to the service perimeter that allows the analyst's identity with the Access Level to call the BigQuery API on the protected resources
- C) Share the dataset publicly so external analysts can access it without needing perimeter membership
- D) Move the analyst's workstation IP to the same subnet as the perimeter projects using a VPN connection

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) VPC Service Controls check both IAM and perimeter membership. An IAM grant alone is insufficient to access resources inside a service perimeter from outside the perimeter. Both checks must pass. IAM does not override VPC Service Controls.
  - C) Making a sensitive dataset public defeats the purpose of protecting it with VPC Service Controls and creates a critical data exposure security incident.
  - D) VPC Service Controls evaluate the access context (identity, device, IP) of the requesting principal, not just network routing. Routing a workstation's traffic through a VPN does not satisfy a service perimeter's access requirements without an explicit Access Level or perimeter membership.

---

### Question 20 (5 points)

During an ACE exam review session, a student is given this scenario: "A company needs a managed database that stores JSON documents, scales automatically, requires no schema management, and supports real-time data synchronization to mobile clients." The student must select from Cloud SQL, Cloud Spanner, Bigtable, and Firestore. What is the correct answer and what two constraints from the scenario uniquely identify it?

- A) Cloud SQL — it supports JSON column types and real-time replication to read replicas
- B) Firestore — the two constraints are "JSON document model" (Firestore stores documents as JSON-like structures in collections) and "real-time synchronization to mobile clients" (Firestore's onSnapshot listener provides native real-time sync to iOS, Android, and web SDKs)
- C) Bigtable — it stores semi-structured data and supports low-latency reads for mobile clients
- D) Cloud Spanner — it provides automatic scaling and global consistency suitable for mobile backends

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud SQL stores relational data in tables with a fixed schema. It supports JSONB columns in PostgreSQL mode but requires schema definition and does not natively support real-time client synchronization. Cloud SQL read replicas are for read scaling, not client-push real-time sync.
  - C) Bigtable is a NoSQL wide-column store optimized for high-throughput time-series or IoT data with very low latency at scale. It does not use a document model and has no native mobile client SDK for real-time sync. It requires a custom application layer between Bigtable and mobile clients.
  - D) Cloud Spanner is a globally distributed relational database with ACID transactions at scale. It uses a relational (not document) model, requires schema definition, and has no native real-time sync capability to mobile clients. Its design target is global relational consistency, not mobile backend flexibility.
