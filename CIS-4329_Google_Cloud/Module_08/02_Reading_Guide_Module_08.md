# Reading Guide: Module 08 – Cloud Run and App Engine: Serverless Compute
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 08 – Cloud Run and App Engine: Serverless Compute**! GCP offers multiple serverless platforms that let you deploy code without provisioning or managing servers. This module covers Cloud Run (for containerized workloads) and App Engine (for web application frameworks), explains when to choose each, and contrasts them with Cloud Functions and GKE. The ACE exam tests your ability to select the right compute platform for a given scenario and understand how these services handle scaling, concurrency, and traffic.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Cloud Run**: A fully managed serverless platform that runs stateless containers. You provide a container image, Cloud Run handles provisioning, scaling (including scale-to-zero), and load balancing. Cloud Run bills per 100 milliseconds of CPU and memory consumed during request processing. Suitable for HTTP-driven services, APIs, and event-driven workloads.

*   **App Engine Standard Environment**: A PaaS runtime that supports specific language runtimes (Python, Java, Node.js, Go, PHP, Ruby) with automatic scaling and scale-to-zero. Code runs in a sandboxed environment; direct filesystem access and arbitrary background processes are restricted. Ideal for web apps using supported runtimes with minimal configuration overhead.

*   **App Engine Flexible Environment**: Runs application code inside Docker containers on Compute Engine VMs. Supports custom runtimes, long-running background processes, and direct filesystem access. Does not scale to zero — at least one instance is always running. Use Flexible when the standard sandbox is too restrictive.

*   **Service (Cloud Run)**: The primary deployment unit in Cloud Run. Each service has a stable HTTPS endpoint. You deploy new container images as Revisions. Traffic splitting allows you to route a percentage of requests to different revisions for canary or blue/green deployments.

*   **Concurrency**: The number of simultaneous requests a single Cloud Run container instance can handle. The default is 80. Setting concurrency to 1 forces one-request-per-instance behavior (matching Cloud Functions semantics). Adjusting concurrency affects how aggressively Cloud Run scales new instances.

*   **Cloud Functions**: An event-driven serverless compute service that runs a single function in response to a trigger (HTTP request, Pub/Sub message, Cloud Storage event, Firestore write). Cloud Functions are not container-based and have shorter maximum execution times than Cloud Run. Best for lightweight glue code or event handlers.

---

### 2. Certification Exam Tips

*   **Choosing between Cloud Run, App Engine, and GKE**: The ACE exam presents scenarios to test platform selection. Key signals: containers + no server management + HTTP traffic → Cloud Run. Existing web framework (Django, Flask, Spring) + supported runtime + minimal config → App Engine Standard. Need DaemonSets, node-level control, or stateful workloads → GKE. Need fine-grained OS access → GKE or Compute Engine.

*   **Scale-to-zero distinguishes Standard from Flexible**: App Engine Standard and Cloud Run both scale to zero (no instances when idle, no cost). App Engine Flexible keeps at least one instance running at all times, resulting in continuous billing even with no traffic.

*   **Cloud Run traffic splitting for safe deployments**: The exam tests knowledge of Cloud Run's revision traffic-splitting feature. When you deploy a new revision, you can route 5% of traffic to the new version while 95% goes to the stable version — enabling canary testing before full rollout. Use `gcloud run services update-traffic` to manage splits.

*   **App Engine versions and traffic migration**: App Engine also supports traffic splitting across versions with `gcloud app services set-traffic`. The exam may test whether you know the difference between `--splits` (gradual rollout) and `--migrate` (immediately shift all traffic to the new version).

*   **Study Resource**: The freeCodeCamp ACE course covers Cloud Run and App Engine deployment patterns with live console demonstrations: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Serverless Compute chapter using the video index.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the Cloud Run overview including how services, revisions, and traffic splitting work: [Cloud Run Overview](https://cloud.google.com/run/docs/overview/what-is-cloud-run). Pay attention to the comparison table between Cloud Run and App Engine.
*   **Required Reading**: Review App Engine environments, how Standard and Flexible differ, and how to deploy using `gcloud app deploy`: [App Engine Overview](https://cloud.google.com/appengine/docs/the-appengine-environments).
*   **Required Video**: Watch the Serverless Compute segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Cloud Run and App Engine chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will deploy a containerized application to Cloud Run and a web application to App Engine. Key commands to practice:

*   `gcloud run deploy my-service --image=gcr.io/PROJECT/IMAGE --region=us-central1 --platform=managed` — deploys a container image to Cloud Run
*   `gcloud run services update-traffic my-service --to-revisions=REVISION=10` — routes 10% of traffic to a specific revision
*   `gcloud app deploy app.yaml` — deploys an App Engine application from a configuration file
*   `gcloud app services set-traffic default --splits=v2=1 --migrate` — migrates all App Engine traffic to a new version

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Cloud Run Overview](https://cloud.google.com/run/docs/overview/what-is-cloud-run) documentation page.
- [ ] Read the [App Engine Overview](https://cloud.google.com/appengine/docs/the-appengine-environments) documentation page.
- [ ] Watch the Serverless Compute segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: deploy a container to Cloud Run and a web app to App Engine.
- [ ] Proceed to the weekly quiz.
