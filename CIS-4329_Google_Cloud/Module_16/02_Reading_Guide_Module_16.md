# Reading Guide: Module 16 – Final Exam Prep and Google Cloud ACE Certification Review
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 16 – Final Exam Prep and Google Cloud ACE Certification Review**! This is the capstone module for CIS-4329. Rather than introducing new GCP services, this module consolidates the high-priority concepts from all prior modules, reviews the ACE exam structure and question strategy, and provides a final study checklist. The Google Cloud Associate Cloud Engineer exam tests your ability to apply GCP knowledge to real-world scenarios — not recall isolated facts. This guide focuses on the highest-frequency exam topics and cross-domain integration scenarios.

---

### 1. ACE Exam Structure and Strategy

*   **Exam format**: 50–60 scenario-based multiple-choice questions. 2-hour time limit. Passing score approximately 70%. Questions describe a business or technical scenario and ask you to select the best GCP service, configuration, or command.

*   **Question strategy**: Read the full scenario before looking at the answers. Identify the key constraints — availability requirements, cost sensitivity, managed vs. unmanaged, global vs. regional, HTTP vs. non-HTTP. These constraints narrow the answer space significantly. Eliminate clearly wrong answers first, then choose between the remaining options based on GCP-specific knowledge.

*   **Most heavily tested domains** (based on Google's published exam guide):
    *   Setting up cloud environments (resource hierarchy, IAM, billing)
    *   Planning and configuring compute resources (Compute Engine, GKE, Cloud Run, App Engine)
    *   Planning and configuring data storage (Cloud Storage, Cloud SQL, Spanner, Bigtable)
    *   Managing and configuring networks (VPC, firewall rules, load balancers, hybrid connectivity)
    *   Deploying and implementing cloud solutions (`gcloud` commands, Deployment Manager, Terraform)
    *   Monitoring and logging (Cloud Monitoring, Cloud Logging, alerting policies)

---

### 2. High-Priority Cross-Domain Review

**Compute selection decision tree:**
- Need full OS control, custom kernel, or GPU: Compute Engine
- Containerized app, no node management, HTTP traffic, scale to zero: Cloud Run
- Existing web framework, supported runtime, minimal config: App Engine Standard
- Container orchestration with node pools, DaemonSets, stateful workloads: GKE
- Single event-driven function, short execution: Cloud Functions

**Storage selection decision tree:**
- Object/blob storage, static website, backups: Cloud Storage
- Relational, MySQL/PostgreSQL/SQL Server, regional: Cloud SQL
- Relational, global, horizontally scalable, strong consistency: Cloud Spanner
- NoSQL, high-throughput, time-series, row-key access: Cloud Bigtable
- NoSQL, document model, mobile/web SDK, real-time sync: Firestore

**Networking decision tree:**
- HTTP(S) + global traffic + URL routing + HTTPS termination: Global HTTP(S) Load Balancer
- TCP/UDP + regional + preserve source IP: Regional Network Load Balancer
- Internal VPC-to-VPC HTTP(S) traffic: Internal HTTP(S) Load Balancer
- On-premises hybrid connectivity, encrypted, up to several Gbps: Cloud VPN (HA VPN)
- On-premises hybrid connectivity, dedicated physical circuit, 10+ Gbps: Dedicated Interconnect

**IAM and security decision tree:**
- Minimum permissions, not primitive roles: Predefined or Custom roles
- Pod needs GCP API access: Workload Identity (not SA key files)
- Block specific IP ranges or SQL injection from HTTP traffic: Cloud Armor
- Detect misconfigurations across org: Security Command Center
- Customer control of encryption keys: Cloud KMS with CMEK
- Prevent data exfiltration to external projects: VPC Service Controls

---

### 3. Essential `gcloud` and `kubectl` Command Reference

These commands appear frequently on the ACE exam. Know what each does and when to use it.

**Identity and resource management:**
- `gcloud config set project PROJECT_ID` — sets the active project for subsequent commands
- `gcloud iam roles list --project=PROJECT_ID` — lists custom IAM roles in a project
- `gcloud projects add-iam-policy-binding PROJECT --member=user:EMAIL --role=roles/viewer` — grants an IAM role

**Compute Engine:**
- `gcloud compute instances create NAME --machine-type=e2-standard-4 --zone=us-central1-a` — creates a VM
- `gcloud compute instances stop/start NAME --zone=ZONE` — stops or starts a VM
- `gcloud compute ssh NAME --zone=ZONE` — SSH into a VM using IAP or external IP

**GKE:**
- `gcloud container clusters create NAME --region=REGION --num-nodes=3` — creates a regional GKE cluster
- `gcloud container clusters get-credentials NAME --region=REGION` — configures kubectl to connect to the cluster
- `kubectl apply -f deployment.yaml` — deploys a workload from a manifest
- `kubectl rollout undo deployment/NAME` — rolls back a Deployment to the previous revision

**Cloud Storage:**
- `gsutil mb -l us-central1 gs://my-bucket` — creates a bucket in a specific region
- `gsutil cp file.txt gs://my-bucket/` — uploads a file to a bucket
- `gsutil lifecycle set lifecycle.json gs://my-bucket` — applies a lifecycle policy

**Logging and monitoring:**
- `gcloud logging read 'severity>=ERROR' --limit=50` — reads recent error log entries
- `gcloud logging sinks create NAME DESTINATION --log-filter=FILTER` — creates a log export sink

---

### 4. Certification Exam Tips

*   **"Least privilege" is almost always the right IAM answer**: When the exam asks about granting access, the answer that grants the minimum role needed to accomplish the task is almost always correct. Primitive roles (`roles/owner`, `roles/editor`) on individual users or Service Accounts are almost always wrong in production scenarios.

*   **Managed services beat self-managed**: When the scenario emphasizes reducing operational overhead, the managed service (Cloud SQL over MySQL on a VM, Cloud Run over a GKE cluster, Cloud Bigtable over HBase on Compute Engine) is the correct answer.

*   **The ACE exam is scenario-based, not memorization-based**: You will not be asked to recite the exact throughput of Dedicated Interconnect. You will be asked: "A company needs 8 Gbps of encrypted connectivity from their data center to GCP — which product?" The scenario constraints lead you to the answer.

*   **Practice with the official sample questions**: Google publishes official ACE exam sample questions at [cloud.google.com/certification/cloud-engineer](https://cloud.google.com/certification/cloud-engineer). Work through these after completing the course to calibrate your readiness. The question style and difficulty closely match the actual exam.

*   **Study Resource**: The complete freeCodeCamp ACE certification course covers all exam domains: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Use the video index to revisit specific topics where you feel less confident.

---

### Required Readings & Videos
To prepare for the final exam, complete the following:

*   **Required Reading**: Review the official ACE exam guide to understand the exam domains and the percentage of questions from each area: [Associate Cloud Engineer Certification Exam Guide](https://cloud.google.com/certification/guides/cloud-engineer). Focus your remaining study time on the highest-weighted domains.
*   **Required Reading**: Review Google's official practice questions and sample exam to calibrate your readiness before scheduling the exam: [ACE Sample Questions](https://cloud.google.com/certification/cloud-engineer).
*   **Required Video**: Watch the full ACE certification course summary and final review segment: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Use the chapter index to revisit modules where you scored below 80% on the weekly quizzes.

---

### 5. Final Study Checklist
- [ ] Review all 15 module reading guides and confirm you can explain every glossary term without looking.
- [ ] Retake any module quiz where you scored below 80% and review the distractor analysis for every question you missed.
- [ ] Read the [ACE Exam Guide](https://cloud.google.com/certification/guides/cloud-engineer) and note which domains have the most questions.
- [ ] Work through the [ACE Sample Questions](https://cloud.google.com/certification/cloud-engineer) on Google's certification page.
- [ ] Watch the final review segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the Module 16 final quiz.
- [ ] Schedule your Google Cloud ACE exam at [webassessor.com/google](https://www.webassessor.com/google) when you are consistently scoring above 80% on practice questions.
