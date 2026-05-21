# Quiz: Module 13 - Compliance as Code – OPA and Policy Enforcement

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the purpose of centralized logging in a DevSecOps pipeline and production environment?

* A) To store compiled application binaries in a searchable format for faster deployment
* B) To aggregate system and application logs from all services into a single queryable platform, enabling rapid incident investigation, compliance audit trails, and security event correlation
* C) To host DNS domain records for the organization's production services and APIs
* D) To execute automated unit tests against deployed application endpoints
* **Correct Answer:** B) Centralized logs permit rapid query searches across microservices during security incidents and provide the immutable audit trail required to demonstrate compliance during regulatory reviews.
* **Distractor Analysis:**
  * *Why B is correct:* Centralized logging (via ELK Stack, Splunk, or similar) consolidates logs from every service, pipeline run, and infrastructure component into a searchable store. This enables security operations teams to correlate events across systems and provides auditors with timestamped evidence that security controls operated as required.
  * *Why A is incorrect:* Binary artifacts are stored in artifact registries (Docker registries, package repositories), not in logging systems. Logging systems store structured text and event data, not executable files.
  * *Why C is incorrect:* DNS hosting is provided by dedicated DNS services (Route53, Cloudflare). Logging platforms store and query log events, not DNS records.
  * *Why D is incorrect:* Unit test execution is a CI/CD pipeline job function. Logging platforms store and query log output from tests and services; they do not execute tests.

---

**Question 2**
Which of the following most accurately describes application telemetry in a DevSecOps context?

* A) The automated process of running SAST scans against application source code on a scheduled basis to detect newly introduced vulnerabilities
* B) The continuous collection and transmission of metrics, traces, and structured logs from running applications and infrastructure — providing real-time visibility into system health, performance, and security-relevant events
* C) The practice of manually sampling production traffic once per day and analyzing HTTP response codes for anomalies
* D) The Git commit history that records who made changes to the application's source code and configuration files
* **Correct Answer:** B) Application telemetry encompasses the three pillars of observability — metrics (Prometheus), distributed traces (Jaeger, Zipkin), and structured logs (ELK, Loki) — providing continuous visibility into the application's security posture and operational state.
* **Distractor Analysis:**
  * *Why B is correct:* Telemetry systems instrument the application to emit data automatically — CPU/memory metrics, request latency, error rates, and security events like authentication failures. This data feeds both operational monitoring and security alerting systems in real time.
  * *Why A is incorrect:* Scheduled SAST scanning is a static code analysis activity. Telemetry is about runtime data collection from a running application, not source code analysis.
  * *Why C is incorrect:* Daily manual traffic sampling is a periodic, low-coverage approach. Telemetry provides continuous, automated data collection that covers every request without sampling.
  * *Why D is incorrect:* Git commit history is version control metadata. Telemetry refers to runtime operational and security data emitted by live systems, not source code change history.

---

**Question 3**
An Open Policy Agent (OPA) Gatekeeper policy is deployed to a Kubernetes cluster. A developer submits a pod manifest with `securityContext.runAsRoot: true`. What action does OPA Gatekeeper take?

* A) OPA Gatekeeper logs the event but allows the pod to be created, flagging it for review in the next security audit
* B) OPA Gatekeeper, acting as a Kubernetes admission controller, rejects the pod creation request and returns a policy violation message — the pod is never created in the cluster
* C) OPA Gatekeeper modifies the pod manifest to automatically set `runAsRoot: false` before passing it to the API server for storage
* D) OPA Gatekeeper schedules the pod creation for manual review by a cluster administrator before it is permitted to run
* **Correct Answer:** B) OPA Gatekeeper operates as a Kubernetes validating admission webhook — when a pod manifest violates a policy (e.g., root execution prohibited), Gatekeeper rejects the API request and the pod is never created.
* **Distractor Analysis:**
  * *Why B is correct:* Kubernetes admission webhooks intercept API requests before resources are stored in etcd. A validating webhook (which OPA Gatekeeper implements) can reject the request entirely with a descriptive error message, enforcing Compliance as Code at the cluster API level.
  * *Why A is incorrect:* A validating admission webhook that logs and allows violations provides no preventive enforcement — it is advisory only. OPA Gatekeeper in enforcement mode rejects, not logs-and-allows.
  * *Why C is incorrect:* Automatically modifying resource manifests is the function of a mutating admission webhook (OPA Gatekeeper also supports mutation, but that is a separate policy type). The scenario describes a validation policy that prohibits root execution — the appropriate response is rejection, not auto-remediation.
  * *Why D is incorrect:* Kubernetes admission control is a synchronous, automated process — there is no built-in mechanism for manual administrator approval queuing. Policies either allow or deny the request immediately.

---

**Question 4**
A DevSecOps team wants to ensure that every Kubernetes deployment in their production cluster has resource limits (`resources.limits.cpu` and `resources.limits.memory`) defined. Which approach implements this as Compliance as Code?

* A) Add a comment in the deployment template YAML file reminding developers to set resource limits before deploying to production
* B) Write an OPA Gatekeeper ConstraintTemplate and Constraint that rejects any Deployment resource where `resources.limits` is not defined for all containers, enforced at admission time
* C) Run a monthly `kubectl get deployments --all-namespaces` review and manually add resource limits to any deployments found without them
* D) Configure a Prometheus alert that fires when a pod's CPU usage exceeds 90%, as a proxy signal for missing resource limits
* **Correct Answer:** B) An OPA Gatekeeper ConstraintTemplate encodes the resource limits requirement as a Rego policy; the Constraint applies it to Deployment resources cluster-wide; any non-compliant deployment is rejected at admission time, preventing the policy violation from ever reaching the cluster.
* **Distractor Analysis:**
  * *Why B is correct:* This is the definition of Compliance as Code — the requirement (resource limits must be defined) is expressed as executable policy code (Rego), enforced automatically at every resource creation event (admission control), not by periodic manual review or documentation reminders.
  * *Why A is incorrect:* Comments in YAML files are documentation, not enforcement. A developer can easily miss or ignore the comment. Compliance as Code requires technical enforcement, not advisory guidance.
  * *Why C is incorrect:* Monthly manual review is a periodic detective control — non-compliant deployments exist for up to a month before being corrected. Compliance as Code provides continuous, preventive enforcement at submission time.
  * *Why D is incorrect:* A CPU usage alert detects the symptom (resource exhaustion) after the pod is running, not the cause (missing resource limits) at submission time. This is a monitoring control, not a preventive compliance control.

---

**Question 5**
A regulated organization must demonstrate to auditors that all code deployed to production was scanned by a SAST tool, approved by a code reviewer, and built by the authorized CI/CD pipeline. Which set of artifacts provides this compliance evidence?

* A) Developer testimonials stating that they followed the security process, collected in a shared spreadsheet updated monthly
* B) Immutable CI/CD pipeline audit logs showing each pipeline run's trigger event, scan step results, reviewer approval, and deployment timestamp — stored in a centralized, tamper-evident logging system
* C) The organization's security policy document describing the required process, approved by the CISO and published on the intranet
* D) A one-time penetration test report showing no critical vulnerabilities in the current production application
* **Correct Answer:** B) Immutable pipeline audit logs provide timestamped, traceable evidence for each deployment — proving the scan ran, the reviewer approved, and the pipeline (not a manual process) performed the deployment.
* **Distractor Analysis:**
  * *Why B is correct:* Modern CI/CD platforms generate structured, time-stamped audit logs for every pipeline run — which commit triggered it, which steps ran and their outcomes, who approved the deployment. When stored in a tamper-evident centralized logging system, these logs satisfy the evidentiary requirements of compliance frameworks like SOC 2, PCI-DSS, and ISO 27001.
  * *Why A is incorrect:* Self-reported spreadsheets are easily falsified, incomplete, and provide no cryptographic or system-generated evidence. Auditors require system-generated, tamper-evident records, not self-attestations.
  * *Why C is incorrect:* A policy document describes what should happen; it does not provide evidence that the controls actually operated as described on any specific deployment. Auditors require operational evidence, not just policy documentation.
  * *Why D is incorrect:* A penetration test report is point-in-time evidence about the current state of the application; it does not prove that each historical deployment followed the required process. Continuous pipeline audit logs provide the per-deployment evidence chain.
