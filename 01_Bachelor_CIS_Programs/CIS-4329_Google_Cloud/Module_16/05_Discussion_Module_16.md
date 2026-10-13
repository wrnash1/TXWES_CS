# Discussion Forum: Module 16 — ACE Exam Preparation

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Discussion Prompt

This final discussion asks you to synthesize across all five ACE exam domains by designing a GCP architecture for a realistic scenario. Rather than selecting a single service, you will justify a complete set of architectural decisions — compute, storage, networking, identity, and monitoring — and engage critically with your classmates' designs.

The ACE exam heavily tests architectural decision-making across domains. This discussion builds exactly that skill.

### Scenario

A healthcare startup is launching a patient appointment booking application on GCP. Requirements:

- The booking API is containerized, stateless, and must handle unpredictable traffic with zero idle-time cost
- Patient data (appointment records) must be stored in a relational database with full ACID compliance; data must stay in the US
- Medical images (JPEG, PNG) must be stored durably; images are accessed frequently for 30 days after upload, then rarely
- The API must not be publicly accessible — only the mobile app (via an API gateway) should invoke it
- All API access to patient data must be logged for HIPAA audit compliance
- Engineers should not be able to create VMs with external IPs in this project

---

### Your Tasks

**Initial Post (Due Wednesday at 11:59 PM)**

In 225–275 words, design the GCP architecture for this scenario. Your post must address all five requirement areas:

1. Compute — which GCP compute service handles the API, and why is it the correct choice given the traffic pattern and cost constraints?

2. Database — which GCP database service stores appointment records, and what specific configuration ensures US-only data residency?

3. Storage — which Cloud Storage class handles medical images for the first 30 days, and what feature transitions them cost-effectively after 30 days?

4. Access control — how do you restrict API invocation to the API gateway's service account only, and what IAM configuration prevents engineers from creating VMs with external IPs?

5. Audit logging — which specific GCP logging feature ensures that all API calls to patient data are captured for HIPAA audit requirements?

Use correct, specific GCP service and feature names throughout your post.

---

**Peer Responses (Due Sunday at 11:59 PM)**

Write substantive replies of at least 75 words each to at least two classmates. For each reply, evaluate one of the following:

- Is the compute choice correct given the scale-to-zero and zero-idle-cost requirements? If your peer chose a different service, does their justification account for all stated constraints?
- Is the database configuration correct for US-only data residency? Cloud SQL regions are specified at instance creation — did your peer identify the correct regional constraint?
- Did your peer correctly distinguish between `allUsers`, `allAuthenticatedUsers`, and a specific service account for the API gateway access control? Evaluate the IAM specificity.

---

## Instructor Notes for Grading

Strong initial posts will:

- Choose Cloud Run for compute (the only GCP option that is both stateless-container-native and scale-to-zero with zero idle cost)
- Specify a US region for Cloud SQL at instance creation (e.g., `--region=us-central1`) and confirm ACID compliance is built into Cloud SQL PostgreSQL
- Specify Cloud Storage Standard for the first 30 days and Object Lifecycle Management transitioning to Nearline at 30 days
- Specify removing `--allow-unauthenticated` from Cloud Run and granting `roles/run.invoker` to the API gateway's service account only
- Correctly identify Cloud Audit Logs (specifically Data Access audit logs, which must be enabled manually and capture read/write API calls to data) as the HIPAA audit logging mechanism
- Mention Organization Policy `compute.vmExternalIpAddress` for the external IP restriction

Common errors to watch for:

- Choosing GKE or Compute Engine for a scale-to-zero, zero-idle-cost requirement
- Using `allAuthenticatedUsers` instead of a specific service account for API invocation
- Omitting the explicit enablement of Data Access audit logs (Admin Activity logs are always on but do not capture data reads)
- Confusing `compute.vmExternalIpAddress` Organization Policy with a VPC firewall rule

---

## Discussion Rubric

| Component | Points | Criteria |
|---|---|---|
| Initial Post — Compute | 1.5 | Correct service with scale-to-zero justification; specific service name used |
| Initial Post — Database | 1.5 | Correct service; US region specified; ACID compliance addressed |
| Initial Post — Storage | 1.5 | Correct initial class; Object Lifecycle Management named; transition at 30 days |
| Initial Post — Access Control | 2 | Cloud Run IAM (no public access + specific invoker); Organization Policy named |
| Initial Post — Audit Logging | 1.5 | Data Access audit logs correctly identified (not just Admin Activity) |
| Peer Response 1 | 1 | Substantive evaluation of peer's compute, database, or access control choice |
| Peer Response 2 | 1 | Substantive evaluation of peer's compute, database, or access control choice |
| **Total** | **10** | |

---

## Course Closing Note

This is the final discussion for CIS-4329 Google Cloud Computing. Over sixteen modules, you have covered the full spectrum of GCP services and operational practices: the resource hierarchy, IAM, Compute Engine, Cloud Storage, Cloud SQL, GKE, Cloud Run, VPC networking, Cloud Monitoring, Cloud Logging, Cost Management, and ACE exam preparation.

The Associate Cloud Engineer exam validates your ability to apply this knowledge to real-world scenarios. More importantly, the skills from this course are directly applicable to GCP environments you will build and operate as cloud practitioners.

Good luck on the ACE exam.

— Professor Nash
