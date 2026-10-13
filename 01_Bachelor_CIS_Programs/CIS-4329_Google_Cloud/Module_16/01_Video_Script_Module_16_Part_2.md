# Video Script: Module 16 — ACE Exam Preparation (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome back. This is Part 2 of the Module 16 ACE exam preparation series. In Part 1 we reviewed Domains 1 and 2. In this part we cover Domains 3, 4, and 5, plus the exam question strategy framework and key cross-domain integration scenarios.

---

### Domain 3 Review: Deploying and Implementing a Cloud Solution

Domain 3 covers the hands-on implementation tasks that constitute the largest share of ACE exam questions.

**Deploying Compute Engine VMs.** Know the gcloud command structure for VM creation:

```bash
gcloud compute instances create INSTANCE_NAME \
  --zone=us-central1-a \
  --machine-type=n2-standard-4 \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --boot-disk-size=50GB \
  --service-account=SA_EMAIL \
  --scopes=cloud-platform
```

Key flags to know: `--preemptible` for preemptible VMs; `--spot` for Spot VMs; `--metadata=startup-script=` for startup scripts; `--tags` for network tag-based firewall rules; `--no-address` to prevent external IP assignment.

**Managed Instance Groups (MIGs).** A MIG is a group of identical VMs managed by an instance template. Supports autoscaling (based on CPU utilization, custom metrics, or HTTP load), auto-healing (restart unhealthy VMs), rolling updates, and multi-zone distribution. Create a MIG:

```bash
# First create an instance template
gcloud compute instance-templates create WEB-TEMPLATE \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud

# Then create the MIG
gcloud compute instance-groups managed create web-mig \
  --template=WEB-TEMPLATE \
  --size=3 \
  --zone=us-central1-a
```

**GKE cluster operations.** Key gcloud commands:

```bash
# Create a GKE cluster
gcloud container clusters create CLUSTER_NAME \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=e2-standard-4

# Get credentials to configure kubectl
gcloud container clusters get-credentials CLUSTER_NAME --zone=us-central1-a

# Deploy a workload
kubectl create deployment nginx --image=nginx --replicas=3

# Expose with a LoadBalancer service
kubectl expose deployment nginx --type=LoadBalancer --port=80
```

**Cloud Run deployment.**

```bash
# Deploy a container image to Cloud Run
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE_NAME \
  --region=us-central1 \
  --platform=managed \
  --allow-unauthenticated
```

`--allow-unauthenticated` makes the service publicly accessible. Remove this flag to require authentication (IAM-based invoke permissions).

**Cloud Storage operations.**

```bash
# Create a bucket
gsutil mb -l us-central1 gs://BUCKET_NAME

# Copy files to a bucket
gsutil cp LOCAL_FILE gs://BUCKET_NAME/

# Set bucket-level IAM policy
gsutil iam ch user:USER_EMAIL:roles/storage.objectViewer gs://BUCKET_NAME

# Apply lifecycle configuration
gsutil lifecycle set lifecycle.json gs://BUCKET_NAME

# Make a bucket publicly readable
gsutil iam ch allUsers:roles/storage.objectViewer gs://BUCKET_NAME
```

**Cloud SQL operations.**

```bash
# Create a Cloud SQL PostgreSQL instance
gcloud sql instances create INSTANCE_NAME \
  --database-version=POSTGRES_14 \
  --tier=db-n1-standard-2 \
  --region=us-central1

# Create a database
gcloud sql databases create DB_NAME --instance=INSTANCE_NAME

# Create a user
gcloud sql users create USER_NAME --instance=INSTANCE_NAME --password=PASSWORD

# Connect via Cloud SQL Auth Proxy
cloud_sql_proxy --instances=PROJECT:REGION:INSTANCE=tcp:5432
```

---

### Domain 4 Review: Ensuring Successful Operation

Domain 4 covers monitoring, logging, troubleshooting, and maintaining running systems.

**Cloud Monitoring.** Collects metrics from all GCP services and custom applications. Key concepts:

- **Metrics** — time-series numerical data (CPU utilization, request count, error rate)
- **Alerting policies** — conditions that trigger notifications when a metric crosses a threshold
- **Uptime checks** — synthetic monitoring that verifies an endpoint is reachable from multiple global locations
- **Dashboards** — custom visualizations combining metrics from multiple services
- **Workspace (formerly Stackdriver workspace)** — a Cloud Monitoring project that can monitor resources across multiple GCP projects

**Cloud Logging.** Centralized log management for all GCP services and application logs.

- **Log Router** — routes logs to different sinks based on filter conditions. A sink can route logs to Cloud Storage (long-term storage), BigQuery (analysis), Pub/Sub (streaming), or another GCP project.
- **Log-based metrics** — Cloud Monitoring metrics derived from log entries matching a filter. Example: count of log entries with severity ERROR per minute.
- **Audit logs** — Admin Activity (always on, free), Data Access (must enable, may incur charges), System Event (always on, free). Audit logs record who did what on which GCP resource.
- `gcloud logging read` — query log entries from the CLI

**Cloud Trace and Cloud Profiler.** Cloud Trace analyzes distributed request latency across microservices. Cloud Profiler continuously profiles CPU and memory usage in production with minimal overhead.

**ACE troubleshooting patterns:**

- VM cannot reach the internet: check firewall rules (egress allow for port 443/80), check if VM has an external IP or a Cloud NAT configuration
- Application returning 502 Bad Gateway via Load Balancer: the backend instances are failing health checks; check that the application is running on the correct port and the health check path returns HTTP 200
- Cloud SQL connection refused: check if the connecting IP is in the authorized networks list or if the Cloud SQL Auth Proxy is being used

---

### Domain 5 Review: Configuring Access and Security

Domain 5 covers IAM at depth, VPC security, and compliance controls.

**IAM best practices:**

- **Least privilege**: Grant the minimum permissions required for the task
- **Predefined over primitive**: Use `roles/storage.objectViewer` instead of `roles/editor`
- **Resource-level grants**: Grant at the resource level (bucket, topic) when possible, not always at the project level
- **Workload Identity**: For GKE workloads accessing GCP APIs — bind a Kubernetes service account to a GCP service account via Workload Identity. Preferred over mounting service account keys.
- **Service account key management**: Avoid downloading service account keys when possible. Use Workload Identity (GKE), attached service accounts (Compute Engine), or Application Default Credentials instead.

**VPC security.** Key components:

- **Firewall rules** — allow or deny traffic to/from VMs based on IP ranges, protocols, ports, and network tags. Default network has default-allow-internal and default-allow-ssh rules. For security, create custom VPC with no default rules and add explicit allow rules.
- **VPC Service Controls** — create security perimeters around GCP API services (BigQuery, Cloud Storage) to prevent data exfiltration. Resources inside the perimeter can access each other; access from outside is blocked.
- **Private Google Access** — allows VMs with only internal IPs to access Google APIs and services without requiring external IPs. Enable at the subnet level.
- **Cloud Armor** — DDoS protection and Web Application Firewall (WAF) for Cloud Load Balancing. Create security policies with allow/deny rules based on IP ranges, geographic origin, or custom expressions.

**Secret Manager.** Stores API keys, passwords, certificates, and other secrets as versioned secret objects. Access controlled by IAM (`roles/secretmanager.secretAccessor`). Integrates with Cloud Run, GKE (via Workload Identity), Cloud Functions, and Compute Engine.

```bash
# Create a secret
gcloud secrets create SECRET_NAME --replication-policy=automatic

# Add a secret version
echo -n "SECRET_VALUE" | gcloud secrets versions add SECRET_NAME --data-file=-

# Access a secret value
gcloud secrets versions access latest --secret=SECRET_NAME
```

---

### ACE Exam Strategy

**The two-constraint method.** Every ACE scenario question has a primary constraint that eliminates most wrong answers, and a secondary constraint that distinguishes the correct answer from the remaining options.

Step 1: Identify the primary constraint — the most restrictive requirement (e.g., "must not use the public internet," "must scale to zero," "must maintain global consistency for ACID transactions").

Step 2: Eliminate every answer that violates the primary constraint.

Step 3: Apply the secondary constraint to choose between remaining answers (e.g., "lowest cost," "managed service," "no server management").

**Common ACE exam distractor patterns:**

- **Close but wrong scope**: The correct service but at the wrong scope (granting `roles/storage.admin` at project level when the requirement is read-only access to one bucket).
- **Similar names, different behavior**: Cloud Armor vs. Cloud IAP; Cloud VPN vs. Cloud Interconnect; Cloud SQL vs. Cloud Spanner.
- **"Best" vs. "possible"**: Multiple answers may work technically, but the ACE exam asks for the best approach — usually the most managed, most scalable, or most cost-effective given the constraints.
- **gcloud command flags**: Knowing the difference between `--zone` and `--region`; `--allow-unauthenticated` on Cloud Run; `--scopes` vs. IAM roles for VM API access.

**Time management.** 50–60 questions in 120 minutes = 2 minutes per question maximum. Flag and skip questions you are uncertain about; return to flagged questions after completing others. Do not spend more than 90 seconds on a question on the first pass.

---

### Cross-Domain Integration Scenarios

These are the question types that test knowledge of how domains connect — the highest-difficulty ACE exam questions.

**Scenario type 1: "How do you securely give a GKE workload access to Cloud SQL?"**

Answer: Create a GCP service account with `roles/cloudsql.client`. Enable Workload Identity on the GKE cluster. Bind the GCP service account to a Kubernetes service account via IAM. Configure the pod to use the Kubernetes service account. Use the Cloud SQL Auth Proxy as a sidecar container. This avoids downloading a service account key.

**Scenario type 2: "A VM cannot connect to Cloud Storage despite having a service account with objectViewer."**

Answer: Check if the VM's `--scopes` flag includes `storage-ro` or `cloud-platform`. Even with an IAM role, access requires the correct access scope on the VM. Use `--scopes=cloud-platform` for full API access; specific scopes for individual services.

**Scenario type 3: "How do you prevent engineers from creating VMs with external IP addresses in any project in the organization?"**

Answer: Set an Organization Policy constraint `compute.vmExternalIpAddress` to restrict to an empty list at the Organization node. This applies to all projects regardless of IAM permissions.

---

### Module 16 Wrap-Up

You have now reviewed all five ACE exam domains:

- Domain 1: Setting up cloud environments — resource hierarchy, IAM, billing
- Domain 2: Planning and configuring — compute, storage, networking service selection
- Domain 3: Deploying and implementing — gcloud commands, GKE, Cloud Run, Cloud SQL, Cloud Storage
- Domain 4: Ensuring successful operation — monitoring, logging, troubleshooting
- Domain 5: Configuring access and security — IAM best practices, VPC security, Secret Manager

Use the Reading Guide practice questions and the twenty quiz questions to identify any gaps before your exam. The ACE exam is a practical exam — if you have completed all sixteen modules' lab activities, you have the hands-on experience to complement the conceptual knowledge.

Good luck on the ACE exam. It has been a fantastic semester.

---

### PRODUCTION NOTES

- Slide: Five ACE exam domains with approximate question weight per domain
- Slide: gcloud command structure cheat sheet (compute instances create, container clusters, run deploy, sql instances)
- Slide: IAM best practices summary (least privilege, predefined roles, Workload Identity)
- Slide: Two-constraint exam method steps with example
- Slide: Common distractor patterns with examples
- Screen share: GKE Workload Identity configuration walkthrough
