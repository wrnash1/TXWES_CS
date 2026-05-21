# Quiz: Module 08 – Cloud Run and App Engine: Serverless Compute
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your team wants to deploy a containerized web API that handles unpredictable burst traffic. During off-hours the service receives zero requests, and you want to pay only for actual request processing time. The team does not want to manage any infrastructure. Which GCP service is the best fit?

A) GKE Autopilot with a Horizontal Pod Autoscaler that scales to zero replicas
B) Cloud Run on the fully managed platform
C) App Engine Flexible Environment with automatic scaling
D) Compute Engine Managed Instance Group with a minimum instance count of 0

*   **Correct Answer:** B) Cloud Run on the fully managed platform
*   **Distractor Analysis:**
    *   *Why A is incorrect:* GKE Autopilot does not truly scale to zero — it always maintains control plane overhead, and HPA cannot scale a Deployment below 1 replica without additional configuration. Cloud Run is the purpose-built zero-scale container platform.
    *   *Why C is incorrect:* App Engine Flexible Environment runs containers on Compute Engine VMs and always keeps at least one instance running, meaning you continue to pay even when there is zero traffic. It does not offer true scale-to-zero.
    *   *Why D is incorrect:* A Managed Instance Group's minimum instance count can be set to 0 via autoscaling, but this still requires managing instance templates, health checks, and startup latency — significantly more infrastructure overhead than Cloud Run.

---

**Question 2**
You are deploying a new version of your Cloud Run service and want to test it with a small subset of real traffic before shifting all users to it. You want 10% of requests to go to the new revision and 90% to remain on the current stable revision. Which approach achieves this?

A) Deploy the new revision and use `gcloud run services update-traffic my-service --to-revisions=NEW_REVISION=10,STABLE_REVISION=90`
B) Create two separate Cloud Run services and use a Cloud Load Balancer to split traffic between them by weight.
C) Deploy the new revision with a different service name and use Cloud DNS to route 10% of DNS queries to it.
D) Enable Cloud CDN on the Cloud Run service and configure a cache rule to serve the new revision for 10% of requests.

*   **Correct Answer:** A) Deploy the new revision and use `gcloud run services update-traffic my-service --to-revisions=NEW_REVISION=10,STABLE_REVISION=90`
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Cloud Run's built-in traffic splitting is designed exactly for this use case and operates within a single service. Creating two separate services and managing an external load balancer adds unnecessary complexity and is not the recommended pattern.
    *   *Why C is incorrect:* DNS-based traffic splitting using weighted routing records is a valid technique in some architectures, but DNS TTL caching makes the 10/90 split imprecise and unpredictable. Cloud Run's native traffic splitting is more accurate and immediate.
    *   *Why D is incorrect:* Cloud CDN is a content caching layer — it caches responses at edge nodes to reduce latency and origin load. It has no concept of routing traffic to different application revisions and cannot perform weighted traffic splitting.

---

**Question 3**
You have a Python Flask web application that uses only standard library packages and requires no background threads or custom system libraries. You want the simplest possible deployment with automatic scaling and no server management. The application can tolerate a short cold-start delay on the first request after a period of inactivity. Which App Engine environment should you use?

A) App Engine Flexible Environment with a custom Python runtime
B) App Engine Standard Environment with the Python runtime
C) Cloud Run with a Python container image built from a Dockerfile
D) GKE Standard with a Python deployment and a LoadBalancer Service

*   **Correct Answer:** B) App Engine Standard Environment with the Python runtime
*   **Distractor Analysis:**
    *   *Why A is incorrect:* App Engine Flexible runs on VMs and does not scale to zero, meaning you pay for at least one running instance at all times. For a standard Flask app with no custom system dependencies, the Standard Environment is simpler and more cost-effective.
    *   *Why C is incorrect:* Cloud Run is an excellent choice for containers, but the scenario describes a pure Flask app with no custom dependencies — App Engine Standard can deploy this directly from source code without requiring a Dockerfile or container build pipeline.
    *   *Why D is incorrect:* GKE Standard requires the most infrastructure management of any option: node pools, Kubernetes manifests, cluster upgrades, and networking configuration. It is significantly over-engineered for a simple Flask application with no special requirements.

---

**Question 4**
You deployed an update to your App Engine application, but the new version has a critical bug. You need to immediately send all traffic back to the previous stable version. Which command accomplishes this with the least disruption?

A) `gcloud app versions delete NEW_VERSION --service=default`
B) `gcloud app services set-traffic default --splits=STABLE_VERSION=1 --migrate`
C) `gcloud app deploy app.yaml --version=STABLE_VERSION --no-promote`
D) Delete the new version from the Cloud Console and wait for App Engine to automatically failover.

*   **Correct Answer:** B) `gcloud app services set-traffic default --splits=STABLE_VERSION=1 --migrate`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Deleting the new version removes it permanently but does not automatically redirect traffic back to the stable version — you must still shift traffic explicitly. Deletion also means you cannot roll forward to that version later without redeploying.
    *   *Why C is incorrect:* Deploying with `--no-promote` deploys the stable version again but keeps traffic on the buggy new version because `--no-promote` explicitly prevents traffic migration. This adds a new version entry without fixing the traffic routing.
    *   *Why D is incorrect:* App Engine does not perform automatic failover when a version is deleted via the Console. Traffic remains on the last version that was promoted until you explicitly change the traffic split — there is no automatic rollback mechanism.

---

**Question 5**
You need to run a lightweight function that triggers whenever a new file is uploaded to a Cloud Storage bucket. The function reads the file, transforms the data, and writes a result to Firestore. The entire operation takes under 30 seconds. No HTTP endpoint is needed. Which GCP service is most appropriate for this use case?

A) Cloud Run service configured with a Pub/Sub push subscription as the trigger
B) App Engine Standard with a background task queue that polls Cloud Storage
C) Cloud Functions triggered by a Cloud Storage finalize event
D) GKE Autopilot with a CronJob that scans the bucket every minute for new files

*   **Correct Answer:** C) Cloud Functions triggered by a Cloud Storage finalize event
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud Run with Pub/Sub push is a valid event-driven pattern but requires more setup: a Pub/Sub topic, a GCS notification that publishes to the topic, and a Cloud Run service with an HTTP handler. Cloud Functions provides a direct GCS trigger with no intermediate infrastructure.
    *   *Why B is incorrect:* Polling a Cloud Storage bucket with a task queue is inefficient — it introduces latency between upload and processing, consumes quota on every poll cycle, and is architecturally more complex than an event-driven trigger.
    *   *Why D is incorrect:* A CronJob scanning the bucket every minute is both inefficient (polling instead of event-driven) and imprecise — files uploaded between scan intervals are delayed. Cloud Functions responds immediately when a file finalizes, with zero polling overhead.
