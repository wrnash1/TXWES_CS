# Reading Guide: Module 16 — ACE Exam Preparation

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Introduction

Module 16 is the capstone and ACE exam preparation module for CIS-4329. This reading guide consolidates the highest-priority concepts from all five ACE exam domains, provides twenty practice questions with full distractor analysis, and supplies a study checklist for exam-day readiness. The ACE exam is scenario-based — it rewards understanding of when and why to use each GCP service, not isolated fact recall. Use this guide to identify your gaps, practice the two-constraint elimination method, and verify that you can trace every service choice back to a specific requirement.

---

## Section 1: ACE Exam Domain Map

### Domain 1 — Setting Up a Cloud Environment

| Topic | Key Concepts | Prior Module |
|---|---|---|
| Resource hierarchy | Organization, Folders, Projects, Resources; IAM inheritance | 2 |
| IAM role types | Primitive (Owner/Editor/Viewer); predefined; custom | 2 |
| Service accounts | Non-human identity; least privilege; avoid default SA | 2 |
| Organization Policies | vmExternalIpAddress; allowedPolicyMemberDomains; resource constraints | 2 |
| Billing hierarchy | Billing account → projects; IAM billing roles | 15 |
| Budget alerts | Pub/Sub notification; Cloud Function cost cap pattern | 15 |

### Domain 2 — Planning and Configuring a Cloud Solution

| Topic | Key Concepts | Prior Module |
|---|---|---|
| Compute Engine | Machine types; persistent disks; startup scripts; MIGs | 3, 4 |
| GKE | Cluster creation; node pools; autoscaling; Workload Identity | 7, 8 |
| Cloud Run | Serverless containers; scales to zero; billed per request | 9 |
| App Engine | Standard vs. Flexible; language runtimes; traffic splitting | 9 |
| Cloud Storage | Storage classes; lifecycle management; access control | 5 |
| Cloud SQL | Managed relational DB; PostgreSQL/MySQL/SQL Server; HA replicas | 6 |
| Cloud Spanner | Global relational DB; ACID at scale; horizontally scalable | 6 |
| Bigtable | NoSQL wide-column; time-series; high throughput | 6 |
| Firestore | NoSQL document; real-time sync; mobile/web | 6 |
| Networking | VPC, subnets, firewall rules; load balancers; VPN; Interconnect | 10, 11 |

### Domain 3 — Deploying and Implementing a Cloud Solution

| Topic | Key Concepts | Prior Module |
|---|---|---|
| gcloud compute | instances create, stop, start, delete, ssh | 3, 4 |
| gcloud container | clusters create/get-credentials; kubectl apply | 7, 8 |
| gcloud run | deploy; update-traffic; services list | 9 |
| gcloud sql | instances create; databases create; connect | 6 |
| gsutil | mb, cp, mv, rm, iam, lifecycle set | 5 |
| Cloud Deployment Manager | Infrastructure as Code on GCP; YAML templates | 13 |
| Terraform on GCP | provider configuration; resource blocks; plan/apply | 13 |

### Domain 4 — Ensuring Successful Operation

| Topic | Key Concepts | Prior Module |
|---|---|---|
| Cloud Monitoring | Metrics, alerting policies, uptime checks, dashboards | 12 |
| Cloud Logging | Log Router, log sinks (GCS/BQ/Pub/Sub), audit logs | 12 |
| Cloud Trace | Distributed request tracing; latency analysis | 12 |
| Log-based metrics | Derive monitoring metrics from log filters | 12 |
| Troubleshooting | VM network, load balancer health checks, Cloud SQL auth | All |

### Domain 5 — Configuring Access and Security

| Topic | Key Concepts | Prior Module |
|---|---|---|
| IAM best practices | Least privilege; resource-level grants; Workload Identity | 2 |
| VPC firewall rules | Allow/deny; priority; network tags vs. service accounts | 10 |
| VPC Service Controls | API service perimeter; data exfiltration prevention | 10 |
| Private Google Access | Internal IPs accessing Google APIs; subnet-level enable | 10 |
| Cloud Armor | DDoS, WAF; security policies on Cloud Load Balancing | 10 |
| Secret Manager | Versioned secrets; IAM access control; GKE/Cloud Run integration | 8 |

---

## Section 2: High-Priority ACE Exam Distinctions

### Compute Engine vs. GKE vs. Cloud Run vs. App Engine

| Requirement | Correct Answer |
|---|---|
| Full OS control, GPU, specific kernel | Compute Engine |
| Containerized microservices, auto-scaling, rolling updates | GKE |
| HTTP/HTTPS API, zero idle cost, no cluster management | Cloud Run |
| Simple web app with language runtime, minimal infra management | App Engine Standard |
| Web app with custom runtime or Docker image | App Engine Flexible |
| Event-driven short-lived functions | Cloud Functions |

### Cloud SQL vs. Cloud Spanner vs. Bigtable vs. Firestore

| Requirement | Correct Answer |
|---|---|
| Relational, transactional, PostgreSQL/MySQL/SQL Server | Cloud SQL |
| Relational, global consistency, horizontal scale, ACID | Cloud Spanner |
| IoT, time-series, high-throughput writes, NoSQL | Bigtable |
| Document model, mobile/web app, real-time sync | Firestore |
| In-memory cache, session state, low latency | Memorystore |

### Cloud VPN vs. Cloud Interconnect

| Feature | Cloud VPN | Cloud Interconnect |
|---|---|---|
| Connection type | Encrypted over public internet | Dedicated private circuit |
| Bandwidth | Up to 3 Gbps per tunnel | 10–100 Gbps |
| Latency | Higher (public internet) | Lower (private, dedicated) |
| Cost | Lower | Higher |
| Use case | Small/medium bandwidth; lower cost | High bandwidth; low latency; private |
| HA option | HA VPN (two tunnels) | Dedicated + partner options |

### Cloud Storage Storage Classes

| Class | Min Duration | Access Pattern |
|---|---|---|
| Standard | None | Frequently accessed; active production data |
| Nearline | 30 days | < 1 access per month; monthly backups |
| Coldline | 90 days | < 1 access per quarter; quarterly DR |
| Archive | 365 days | < 1 access per year; compliance archives |

### Global vs. Regional Load Balancers

| Load Balancer | Scope | Protocol | Use Case |
|---|---|---|---|
| External HTTP(S) | Global | HTTP/HTTPS | Web apps, APIs with global users |
| Internal HTTP(S) | Regional | HTTP/HTTPS | Internal microservices |
| External Network TCP/UDP | Regional | TCP/UDP | Non-HTTP protocols |
| Internal TCP/UDP | Regional | TCP/UDP | Internal TCP/UDP traffic |
| External TCP Proxy | Global | TCP | Non-HTTP global TCP |

---

## Section 3: High-Frequency gcloud Command Reference

### Compute Engine

```bash
# Create VM
gcloud compute instances create NAME --zone=ZONE --machine-type=TYPE --image-family=FAMILY --image-project=PROJECT

# List VMs
gcloud compute instances list

# SSH into VM
gcloud compute ssh NAME --zone=ZONE

# Stop/Start VM
gcloud compute instances stop NAME --zone=ZONE
gcloud compute instances start NAME --zone=ZONE

# Create instance template
gcloud compute instance-templates create TEMPLATE --machine-type=TYPE --image-family=FAMILY --image-project=PROJECT

# Create Managed Instance Group
gcloud compute instance-groups managed create MIG_NAME --template=TEMPLATE --size=N --zone=ZONE

# Set autoscaling
gcloud compute instance-groups managed set-autoscaling MIG_NAME --zone=ZONE --max-num-replicas=10 --target-cpu-utilization=0.6
```

### GKE

```bash
# Create cluster
gcloud container clusters create CLUSTER --zone=ZONE --num-nodes=N --machine-type=TYPE

# Get credentials (configure kubectl)
gcloud container clusters get-credentials CLUSTER --zone=ZONE

# Delete cluster
gcloud container clusters delete CLUSTER --zone=ZONE

# Resize node pool
gcloud container clusters resize CLUSTER --node-pool=POOL_NAME --num-nodes=N --zone=ZONE
```

### Cloud Run

```bash
# Deploy
gcloud run deploy SERVICE --image=IMAGE --region=REGION --platform=managed

# List services
gcloud run services list --region=REGION

# Update traffic split
gcloud run services update-traffic SERVICE --to-revisions=REV1=50,REV2=50 --region=REGION

# Delete service
gcloud run services delete SERVICE --region=REGION
```

### Cloud SQL

```bash
# Create instance
gcloud sql instances create NAME --database-version=POSTGRES_14 --tier=TIER --region=REGION

# Create database
gcloud sql databases create DB_NAME --instance=INSTANCE

# Create user
gcloud sql users create USER --instance=INSTANCE --password=PW

# List instances
gcloud sql instances list

# Export data to Cloud Storage
gcloud sql export sql INSTANCE gs://BUCKET/export.sql --database=DB_NAME
```

### Cloud Storage (gsutil)

```bash
# Create bucket
gsutil mb -l REGION gs://BUCKET_NAME

# Copy object
gsutil cp LOCAL_FILE gs://BUCKET/

# Recursive copy
gsutil cp -r LOCAL_DIR gs://BUCKET/

# Set lifecycle policy
gsutil lifecycle set lifecycle.json gs://BUCKET

# Set IAM on bucket
gsutil iam ch user:EMAIL:roles/storage.objectViewer gs://BUCKET

# Make bucket public (read)
gsutil iam ch allUsers:roles/storage.objectViewer gs://BUCKET

# Signed URL (time-limited access)
gsutil signurl -d 1h KEY_FILE gs://BUCKET/OBJECT
```

---

## Section 4: Twenty Practice Questions

---

### Question 1

A company needs to run a web application that handles variable traffic — millions of requests during business hours, near zero overnight. The application is stateless and containerized. Cost during idle periods must be minimized. What is the best compute option?

- A) Compute Engine with a Managed Instance Group autoscaling to zero nodes when traffic drops
- B) Cloud Run — serverless managed containers that scale to zero when there are no requests, incurring no cost during idle periods
- C) GKE Autopilot cluster with HPA scaling to zero pods
- D) App Engine Flexible environment with min-instances set to zero

Correct Answer: B — Cloud Run is the canonical GCP service for stateless HTTP containerized workloads with variable traffic. It scales to zero automatically and charges per request. MIGs cannot scale to zero (minimum 1 VM for availability). GKE Autopilot scales pods but the cluster control plane incurs charges even with zero pods. App Engine Flexible has a minimum of one instance running at all times.

---

### Question 2

An engineer runs `gcloud compute instances create web-server --zone=us-central1-a --machine-type=e2-medium --image-family=debian-11 --image-project=debian-cloud`. The VM starts but cannot be reached via SSH from the engineer's laptop. Which is the most likely cause?

- A) The VM has no boot disk — `--boot-disk-size` was not specified
- B) The VPC does not have a firewall rule allowing ingress on TCP port 22 from the engineer's IP address
- C) The VM's machine type (e2-medium) does not support SSH connections
- D) The engineer must use `gcloud compute ssh` — direct SSH is not supported on GCP VMs

Correct Answer: B — gcloud compute instances create creates a VM without an external IP unless on the default network with default firewall rules. On a custom VPC, there is no default allow-ssh rule. Even on the default VPC, the default-allow-ssh rule may have been removed. The most likely cause of SSH being unreachable is a missing firewall rule for TCP 22. Boot disk defaults to 10 GB if not specified. e2-medium supports SSH. Direct SSH is supported (not just gcloud compute ssh).

---

### Question 3

A team stores 50 TB of customer data in Cloud Storage. Regulatory requirements mandate that no object can be deleted for 7 years after creation. How do you enforce this requirement on the bucket?

- A) Set Object Lifecycle Management to delete objects after 7 years
- B) Configure a Retention Policy on the bucket with a retention period of 7 years; lock the retention policy with `gsutil retention lock` to make it immutable
- C) Set IAM to remove `storage.objects.delete` permission from all users except the bucket owner
- D) Enable versioning on the bucket — versioned objects cannot be permanently deleted

Correct Answer: B — Cloud Storage Retention Policies prevent objects from being deleted or overwritten before the retention period expires. Locking the retention policy with `gsutil retention lock` makes the retention period immutable — even the bucket owner cannot reduce or remove the retention period. This is the regulatory-compliant approach for data retention requirements. Lifecycle management deletes objects (the opposite requirement). IAM can be bypassed by a user with sufficient permissions. Versioning allows permanent deletion if delete markers are also deleted.

---

### Question 4

A GKE application pod needs to read secrets from Secret Manager without downloading a service account key file. What is the recommended approach?

- A) Mount a service account JSON key as a Kubernetes Secret and reference it in the pod's environment variables
- B) Enable Workload Identity on the GKE cluster; create a GCP service account with `roles/secretmanager.secretAccessor`; bind the GCP service account to the Kubernetes service account used by the pod via IAM; the pod automatically authenticates using the bound identity
- C) Grant `roles/secretmanager.secretAccessor` to the Compute Engine default service account, which GKE pods use by default
- D) Use the Secret Manager API client library and pass the GCP project credentials via environment variable

Correct Answer: B — Workload Identity is the GCP-recommended approach for GKE workloads accessing GCP APIs without service account key files. It binds a Kubernetes service account to a GCP service account via IAM, so pods using the Kubernetes service account automatically authenticate as the GCP service account. No key file is needed — authentication is automatic. This is more secure than key files because there is no long-lived credential that can be stolen.

---

### Question 5

An organization wants to prevent any VM in their GCP organization from having an external IP address. Individual project owners should not be able to override this restriction. What is the correct configuration?

- A) Create a firewall rule in each VPC that blocks egress traffic to 0.0.0.0/0
- B) Set an Organization Policy with the `compute.vmExternalIpAddress` constraint set to `deny` at the Organization node
- C) Grant IAM roles that do not include `compute.instances.addAccessConfig` to all engineers
- D) Use VPC Service Controls to prevent VMs from connecting to external IP addresses

Correct Answer: B — Organization Policies are constraints that restrict GCP resource configurations at the Organization, Folder, or Project level. Setting `compute.vmExternalIpAddress` to deny at the Organization node prevents any VM in any project in the organization from having an external IP — regardless of IAM permissions or individual project settings. Project owners cannot override an Organization Policy set at a higher level. Firewall rules can be modified by project admins and do not prevent IP assignment. IAM permission removal can be worked around by IAM admins. VPC Service Controls prevent API access, not IP assignment.

---

### Question 6

A Cloud SQL PostgreSQL instance is running in us-central1. A VM in a different project in the same region needs to connect to it securely without exposing the Cloud SQL instance to the public internet. What is the recommended approach?

- A) Add the VM's external IP address to the Cloud SQL instance's authorized networks list
- B) Use Private Service Access (PSA) to connect the Cloud SQL instance to the VM's VPC network via a private IP; the VM connects to Cloud SQL's private IP without traversal of the public internet
- C) Configure Cloud VPN between the two projects to create an encrypted tunnel for Cloud SQL traffic
- D) Download a service account key for the Cloud SQL admin service account and configure it on the VM

Correct Answer: B — Private Service Access (also known as VPC peering with Google Services) allows a Cloud SQL instance to have a private IP in a specific VPC network. VMs in peered VPCs (including cross-project VPCs) can connect to Cloud SQL via its private IP without the traffic leaving Google's internal network. The Cloud SQL Auth Proxy is also a supported secure connection method. Adding the VM's external IP to authorized networks uses the public internet. VPN between projects is unnecessary overhead when Private Service Access provides direct VPC connectivity.

---

### Question 7

An e-commerce application on GCP receives a DDoS attack that floods the load balancer with traffic from IP ranges in a specific country. The attack is causing degraded performance for legitimate users. What GCP service provides the fastest mitigation?

- A) Cloud CDN — configure a CDN rule to block traffic from the attacking country
- B) Cloud Armor — create a security policy on the external HTTP(S) Load Balancer that denies traffic from the attacking country's IP ranges using a geo-block rule
- C) VPC firewall rules — create deny rules for the attacking IP ranges at the VPC level
- D) Cloud Monitoring — create an alert that triggers a Cloud Function to add the attacking IPs to a blocklist

Correct Answer: B — Cloud Armor is the GCP service specifically designed for DDoS protection and WAF on Cloud Load Balancing. It supports security policies with rules that can allow or deny based on IP ranges, geography (country-level geo-blocking), and custom expressions. A geo-block rule in Cloud Armor can block traffic from a country at the load balancer edge — before it reaches backend instances — providing the fastest and most effective mitigation.

---

### Question 8

A data engineering team runs BigQuery queries that scan 500 TB per day on a predictable schedule. They are currently on on-demand pricing and the query costs are significant. What pricing option reduces cost for this workload?

- A) Switch all queries to use the `--dry_run` flag to reduce bytes scanned
- B) Purchase BigQuery flat-rate slots (slot commitments) for the expected daily query volume — flat-rate pricing decouples cost from bytes scanned and is cost-effective for high-volume, predictable query workloads
- C) Partition all tables by day to reduce the bytes scanned per query — partitioning reduces on-demand costs
- D) Use BigQuery BI Engine to cache query results and reduce repeated query costs

Correct Answer: B — BigQuery flat-rate pricing (slot commitments) is designed for predictable, high-volume query workloads. Organizations purchase dedicated query processing slots at a fixed monthly cost; queries consume slots rather than being billed per byte scanned. For 500 TB/day, flat-rate is typically significantly cheaper than on-demand. Partitioning and clustering reduce bytes scanned (good optimization), but still incur on-demand per-byte charges. Dry-run doesn't execute queries. BI Engine caches results for specific queries but doesn't reduce general query costs.

---

### Question 9

A team needs to deploy a Cloud Run service that should only be accessible by other Cloud Run services and internal GCP services — never publicly. How do they configure this?

- A) Deploy the service with `--allow-unauthenticated` and then add a VPC firewall rule blocking external access
- B) Deploy the service without `--allow-unauthenticated`; grant `roles/run.invoker` only to the specific service accounts of the services that need to invoke it
- C) Deploy the service in a VPC and use a VPC firewall rule to restrict HTTP access to internal IP ranges only
- D) Enable Cloud Armor on the Cloud Run service and create a policy blocking all external IP addresses

Correct Answer: B — Cloud Run authentication is controlled by IAM. When `--allow-unauthenticated` is not set, Cloud Run requires a valid Google identity token in the request. Granting `roles/run.invoker` only to specific service accounts means only services using those service accounts can invoke the Cloud Run service. This is the correct IAM-based access control pattern for internal Cloud Run services. Cloud Armor is not directly applicable to Cloud Run; it applies to Cloud Load Balancing.

---

### Question 10

A GCP administrator needs to configure logs from a production project to be automatically exported to a BigQuery dataset in a separate data analysis project for long-term querying. What is the correct configuration?

- A) In the production project, create a Cloud Monitoring export rule targeting the BigQuery dataset in the analysis project
- B) In the production project, create a log sink in Cloud Logging with a filter matching production logs, targeting the BigQuery dataset in the analysis project as the sink destination; grant the log sink's writer service account `roles/bigquery.dataEditor` on the destination dataset
- C) Enable Cloud Trace in the production project and configure it to forward traces to BigQuery
- D) Use Cloud Pub/Sub to subscribe to the production project's log stream and publish messages to a BigQuery streaming insert pipeline

Correct Answer: B — Cloud Logging log sinks route logs to external destinations. A sink specifies a filter (which logs to route) and a destination (Cloud Storage, BigQuery, Pub/Sub, or another GCP project's log bucket). For cross-project BigQuery export, the sink's service account must be granted write access to the destination BigQuery dataset. This is the standard pattern for centralized log analysis.

---

### Question 11

A startup is building their first GCP environment. They want to ensure engineers can create and manage Compute Engine VMs in the `dev` project, but cannot modify IAM policies for the project. What IAM configuration achieves this?

- A) Grant `roles/owner` to all engineers — Owners can do everything including Compute Engine management
- B) Grant `roles/compute.instanceAdmin.v1` to the engineers at the `dev` project level — this grants full Compute Engine instance management without IAM policy modification permissions
- C) Grant `roles/editor` to the engineers — Editors can manage most resources but cannot modify IAM
- D) Grant `roles/compute.admin` to the engineers — this includes IAM management for Compute Engine resources

Correct Answer: B — `roles/compute.instanceAdmin.v1` grants full control over Compute Engine instances, disks, images, instance templates, and related resources — but does not include `resourcemanager.projects.setIamPolicy`. Engineers can create and manage VMs but cannot change project-level IAM. `roles/editor` is a primitive role and, while it technically does not include IAM policy modification, it grants broad access to all services — violating least privilege. `roles/compute.admin` includes IAM permissions for Compute Engine.

---

### Question 12

An application running on Compute Engine is failing to access Cloud Storage objects. The VM has a service account with `roles/storage.objectViewer` at the bucket level. The error is `403 Forbidden`. What is the most likely cause?

- A) The `roles/storage.objectViewer` role does not exist — the correct role is `roles/storage.objectReader`
- B) The VM was created with `--scopes=logging-write,monitoring-write` — the access scopes do not include Cloud Storage access, and even though the IAM role is set, API calls are blocked because access scopes are a second layer of authorization on Compute Engine VMs
- C) The service account needs `roles/storage.admin` rather than `roles/storage.objectViewer` to access objects
- D) The bucket is in a different region than the VM — cross-region storage access requires a different role

Correct Answer: B — Compute Engine VMs have two layers of authorization: the IAM role on the service account AND the access scopes set on the VM. If the VM's scopes do not include storage access (e.g., `storage-ro` or `cloud-platform`), API calls to Cloud Storage are blocked even if the service account has the correct IAM role. This is a common ACE exam trap. The fix is to recreate the VM with `--scopes=cloud-platform` (or `--scopes=storage-ro` for read-only access).

---

### Question 13

A company wants to set up a highly available VPN connection between their on-premises data center and GCP. The connection must survive the failure of any single VPN gateway or tunnel. What VPN configuration should they use?

- A) Classic VPN with a single tunnel and BGP routing
- B) HA VPN with two VPN tunnels, each connecting to different interfaces on the Cloud VPN gateway, with dynamic BGP routing
- C) Classic VPN with two tunnels and static routing configured for failover
- D) Cloud Interconnect with a single 10 Gbps circuit for maximum bandwidth

Correct Answer: B — HA VPN provides a 99.99% SLA by using two separate tunnels connecting to two different interfaces on the Cloud VPN gateway. If one tunnel fails, traffic automatically routes through the second tunnel. Dynamic BGP routing is required for HA VPN — static routing is not supported. Classic VPN provides 99.9% SLA with single tunnels and does not offer the redundancy of HA VPN. Cloud Interconnect is not VPN — it is a dedicated circuit, and a single circuit is not HA.

---

### Question 14

A development team wants to use Cloud Deployment Manager to deploy a Compute Engine VM and a Cloud Storage bucket together as a single deployable unit that can be created and deleted together. What artifact do they create?

- A) A Terraform module that references both resources
- B) A Cloud Deployment Manager configuration file (YAML or Python) that defines both the Compute Engine instance and Cloud Storage bucket as resources; deploy with `gcloud deployment-manager deployments create`
- C) A Cloud Build pipeline YAML that creates both resources using gcloud commands
- D) A Terraform workspace that groups the two resources under a single plan

Correct Answer: B — Cloud Deployment Manager is GCP's native infrastructure-as-code service. A Deployment Manager configuration defines GCP resources in YAML (or Python/Jinja2) that are created, managed, and deleted together as a deployment. The `gcloud deployment-manager deployments create NAME --config FILE.yaml` command creates all resources in the configuration. Terraform is also a correct IaC approach for GCP but is not Cloud Deployment Manager.

---

### Question 15

Cloud Monitoring shows that a load balancer backend is returning a high rate of 502 errors. The backend is a Managed Instance Group of web servers. What should the administrator check first?

- A) The Cloud Load Balancer SSL certificate — 502 errors indicate SSL handshake failures
- B) The health check configuration — 502 errors from a load balancer typically mean the backend instances are failing the health check (wrong port, wrong path, or application not running), causing the load balancer to report failures rather than route traffic to healthy instances
- C) The billing account — 502 errors indicate the project has exceeded its billing quota
- D) The MIG autoscaler settings — the autoscaler may have scaled the group to zero instances

Correct Answer: B — HTTP 502 Bad Gateway from a Cloud Load Balancer means the load balancer received an invalid response (or no response) from the backend. The most common cause is backend instances failing health checks — either because the health check is configured to check a wrong port or path, or because the application is not running or not responding on the expected port. Check the health check configuration and the instance health status in the load balancer backend service details.

---

### Question 16

An organization uses Cloud Armor to protect their external HTTP(S) load balancer. A security team wants to allow traffic only from their corporate office IP range (203.0.113.0/24) and block all other traffic. What is the correct Cloud Armor configuration?

- A) Create two rules: priority 1000 — allow traffic from 203.0.113.0/24; priority 2147483647 (default rule) — deny all
- B) Create one rule: deny all traffic except 203.0.113.0/24 using a CIDR block inversion expression
- C) Create one rule: allow traffic from 203.0.113.0/24; the default Cloud Armor rule automatically denies all other traffic
- D) Set the Cloud Armor security policy to `preview` mode with an allow rule for 203.0.113.0/24

Correct Answer: A — Cloud Armor evaluates rules in priority order (lower number = higher priority). The default rule (priority 2147483647) defines the default action for traffic that matches no explicit rule. By setting the default rule to deny and adding a higher-priority allow rule for the corporate IP range, all traffic from 203.0.113.0/24 is allowed and all other traffic is denied. The default Cloud Armor action is allow-all unless explicitly changed (Option C is incorrect). Preview mode evaluates but does not enforce rules (Option D is incorrect).

---

### Question 17

A team deploys a new version of their Cloud Run service. They want to gradually shift traffic from the old version to the new version — starting with 10% to the new version and increasing over several hours — to validate the new version before full cutover. What feature supports this?

- A) Cloud Run versions cannot receive split traffic — each deploy replaces the current version
- B) Cloud Run traffic splitting — use `gcloud run services update-traffic SERVICE --to-revisions=OLD_REVISION=90,NEW_REVISION=10 --region=REGION` to split traffic between named revisions; adjust the split gradually until the new revision receives 100%
- C) Configure a Cloud Load Balancer with weighted backend routing to split traffic between the two Cloud Run service URLs
- D) Use Cloud Armor to route 10% of requests to a different Cloud Run service endpoint

Correct Answer: B — Cloud Run natively supports traffic splitting between revisions. Each deployment creates a new revision; traffic can be split between revisions using percentages that sum to 100%. This enables canary deployments and gradual rollouts. The `gcloud run services update-traffic` command adjusts the traffic split without redeploying. Cloud Load Balancer is not required for Cloud Run traffic splitting.

---

### Question 18

An App Engine Standard application is running in the `us-central` region. During peak load, the application needs to scale up quickly. What App Engine Standard feature controls the scaling behavior?

- A) Managed Instance Groups with autoscaling — App Engine Standard uses MIGs under the hood
- B) App Engine scaling configuration in `app.yaml` — the `automatic_scaling` section defines min/max instances, target CPU utilization, and target throughput utilization; App Engine Standard scales instantly (within seconds) by design
- C) GKE Horizontal Pod Autoscaler — App Engine shares infrastructure with GKE
- D) Cloud Run min-instances setting — App Engine Standard uses Cloud Run as its runtime

Correct Answer: B — App Engine Standard scaling is configured in `app.yaml`. The `automatic_scaling` section supports: `min_instances`, `max_instances`, `target_cpu_utilization`, and `target_throughput_utilization`. App Engine Standard can scale from zero to many instances within seconds due to its sandboxed runtime environment. It does not use MIGs, GKE HPA, or Cloud Run — these are separate compute services.

---

### Question 19

A company is migrating from AWS S3 to Cloud Storage. They need to transfer 200 TB of data from S3 to a Cloud Storage bucket. What is the most efficient transfer method?

- A) Download all S3 data to an on-premises server and use gsutil to upload to Cloud Storage
- B) Use Storage Transfer Service — configure an S3 source with AWS credentials and a Cloud Storage destination bucket; the transfer runs server-to-server within Google's network without requiring data to pass through on-premises infrastructure
- C) Use `gsutil cp` with the `-m` flag to enable parallel multi-threaded transfers from S3 directly
- D) Use BigQuery Data Transfer Service to move S3 data to Cloud Storage

Correct Answer: B — Storage Transfer Service is GCP's managed service for large-scale data transfers to Cloud Storage. For S3-to-GCS transfers, it authenticates to AWS using AWS credentials and transfers data directly from S3 to GCS without the data traversing on-premises networks. It supports scheduling, incremental transfers, and filtering. Direct gsutil from S3 would require the data to route through the initiating machine. BigQuery Data Transfer Service is for loading data into BigQuery from specific sources, not for Cloud Storage transfers.

---

### Question 20

A company's Cloud Monitoring dashboard shows 99.5% uptime for their web application over the past 30 days. The SLA with their customers requires 99.9% uptime. An engineer asks: "What specific Cloud Monitoring feature can proactively detect outages from a user's perspective — not just when the backend metrics spike — so we can investigate before customers report issues?" What is the answer?

- A) Log-based metrics — set a metric based on HTTP 500 error log entries
- B) Uptime checks — Cloud Monitoring uptime checks send synthetic HTTP(S) requests to the application endpoint from multiple global locations every minute and alert when the check fails from a configurable number of locations
- C) Cloud Trace — distributed tracing detects latency increases before they become outages
- D) Cloud Profiler — CPU profiling detects resource bottlenecks that precede outages

Correct Answer: B — Cloud Monitoring Uptime Checks perform synthetic monitoring — they send real HTTP(S) requests to the application URL from multiple geographic locations at configurable intervals (minimum 1 minute). If the check fails from a specified number of locations, an alert triggers. This provides proactive detection of outages from the user's perspective (can they reach the service?) rather than just monitoring backend infrastructure metrics. Log-based metrics detect errors after they occur in logs; Trace and Profiler measure internal application behavior.

---

## Section 5: Exam-Day Checklist

- [ ] Review the Domain Map table — can you name the primary service for each topic area?
- [ ] Review the High-Priority Distinctions — Compute Engine vs. Cloud Run vs. GKE; SQL vs. Spanner vs. Bigtable; VPN vs. Interconnect
- [ ] Complete the twenty practice questions without looking at answers; then review all distractors
- [ ] Review the gcloud command reference — practice writing key commands from memory
- [ ] Review IAM best practices — Workload Identity, least privilege, predefined vs. primitive roles
- [ ] Review the Organization Policy and VPC Service Controls distinction
- [ ] Review the billing cost management patterns: Budget + Pub/Sub + Cloud Function; CUD vs. SUD; Spot VMs
- [ ] Confirm you can describe the two-constraint exam method and apply it to a novel scenario

---

## 9. Supplemental Resources

**1. Google Cloud Documentation — Associate Cloud Engineer Exam Guide**
<https://cloud.google.com/certification/guides/cloud-engineer>
Official exam guide listing all five ACE exam domains with specific topic areas and weightings — the authoritative source for understanding what the exam tests. Use this as the final checklist before sitting for the exam to confirm coverage of all domains.

**2. Google Cloud Skills Boost — ACE Learning Path**
<https://www.cloudskillsboost.google/paths/11>
Google's official hands-on ACE certification learning path including Qwiklabs for all major service areas: Compute Engine, GKE, Cloud Storage, Cloud SQL, IAM, networking, and operations. Completing the labs in this path provides exam-ready practical experience across all five ACE domains.

**3. Google Cloud Documentation — IAM Overview**
<https://cloud.google.com/iam/docs/overview>
Comprehensive reference for GCP IAM covering the resource hierarchy, role types (primitive, predefined, custom), service accounts, allow policies, deny policies, and IAM conditions — the most heavily tested ACE exam domain. Particular focus on the distinction between predefined and primitive roles and the Workload Identity pattern for key-free service authentication.
