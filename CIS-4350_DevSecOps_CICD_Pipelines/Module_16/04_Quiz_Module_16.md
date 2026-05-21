# Quiz: Module 16 - Final Exam Prep & DevSecOps Professional Certification

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
A DevSecOps pipeline runs SAST (Semgrep), SCA (Snyk), and container image scanning (Trivy) — all passing with no CRITICAL findings. After deployment to staging, a DAST scan (OWASP ZAP) finds a CRITICAL authentication bypass vulnerability. Which statement best explains why the earlier scans did not catch this finding?

* A) The SAST, SCA, and container scans are misconfigured; all three should have caught an authentication bypass
* B) Authentication bypass vulnerabilities often only manifest when the full application runs — with session management, configuration, and middleware integrated — which DAST tests by interacting with the live application, while SAST, SCA, and image scans analyze artifacts that do not include runtime behavior
* C) DAST always produces more findings than SAST and SCA combined; the earlier tools should be replaced with a DAST-only approach to eliminate redundancy
* D) The staging environment differs from production, so the finding is likely a false positive that will not exist in production
* **Correct Answer:** B) Authentication bypass is a runtime vulnerability that depends on how session handling, middleware, and configuration interact when the application runs — DAST tests exactly this, while SAST, SCA, and image scans operate on static artifacts without executing the application.
* **Distractor Analysis:**
  * *Why B is correct:* SAST finds insecure code patterns; SCA finds vulnerable packages; image scanning finds OS CVEs. None of these test runtime behavior. Authentication bypass often involves interaction between multiple system components (load balancer, session store, authentication middleware) that only presents as a vulnerability when tested end-to-end — precisely what DAST does.
  * *Why A is incorrect:* SAST, SCA, and image scanning are not designed to detect runtime authentication behavior. Their failure to catch the DAST finding is not misconfiguration — it reflects the fundamental difference in what each tool type can detect.
  * *Why C is incorrect:* DAST and SAST detect different, complementary vulnerability classes. Eliminating SAST, SCA, and image scanning would leave entire categories of vulnerabilities undetected (hardcoded secrets, vulnerable dependencies, OS CVEs). Both static and dynamic testing are required.
  * *Why D is incorrect:* While staging/production differences can cause false positives, an authentication bypass finding in staging is a significant finding that requires investigation before production deployment. Dismissing it as a false positive without analysis is a dangerous security assumption.

---

**Question 2**
A security engineer is reviewing a GitHub Actions workflow. The `on:` trigger is set to `schedule: cron: '0 2 * * 1'`. A secrets scanning step using Gitleaks runs in this workflow. What is the security limitation of this configuration compared to a `pull_request` triggered scan?

* A) Scheduled scans use more CI runner compute time than pull_request scans, making them less cost-effective
* B) A weekly scheduled scan means secrets committed to any branch during the week go undetected until the next Monday scan — creating a window of up to 7 days where a committed secret is in the repository but has not been flagged
* C) Scheduled workflows cannot access GitHub Actions Secrets, making Gitleaks unable to authenticate to external CVE databases
* D) The `cron` trigger cannot be combined with secrets scanning; a separate repository-dispatch event is required
* **Correct Answer:** B) A weekly scheduled scan creates a detection gap — secrets committed Monday through Sunday are not detected until the following Monday, potentially sitting in the repository for up to 7 days and being pulled into other developers' branches.
* **Distractor Analysis:**
  * *Why B is correct:* A `pull_request`-triggered secret scan catches exposed secrets the moment the PR is opened — before the commit is merged and before other systems can pull the secret. The weekly schedule leaves a significant detection window where secrets are live and potentially cloned or accessed by CI systems that consume the branch.
  * *Why A is incorrect:* Compute cost is an operational concern, not a security limitation. The security limitation is the detection delay, not the resource consumption.
  * *Why C is incorrect:* Scheduled workflows have full access to GitHub Actions Secrets just like other workflow trigger types. There is no authentication limitation specific to scheduled runs.
  * *Why D is incorrect:* The `schedule` trigger is a standard GitHub Actions trigger type that is fully compatible with any job configuration including secrets scanning steps.

---

**Question 3**
A Kubernetes cluster uses OPA Gatekeeper to enforce the policy: "All container images in the `production` namespace must be pulled from `registry.company.internal` only." A developer deploys a pod using `image: nginx:latest` (from Docker Hub). What happens, and why?

* A) The pod is created successfully because `nginx:latest` is a trusted, official Docker Hub image
* B) OPA Gatekeeper's validating admission webhook intercepts the pod creation request, evaluates it against the registry allowlist policy, determines the image source violates the policy, and rejects the request — the pod is never created
* C) The pod is created but immediately terminated by Kubernetes after the image is pulled, because post-creation image validation detects the policy violation
* D) OPA Gatekeeper modifies the image reference from `nginx:latest` to `registry.company.internal/nginx:latest` before creating the pod
* **Correct Answer:** B) OPA Gatekeeper operates as a Kubernetes validating admission webhook — it evaluates every resource creation request against defined policies before the resource is stored in etcd. A policy violation results in immediate rejection of the API request.
* **Distractor Analysis:**
  * *Why B is correct:* The validating webhook intercepts the API request at admission time. The Rego policy checks whether the image field matches the allowed registry prefix; `nginx:latest` from Docker Hub does not match `registry.company.internal`, so the policy evaluation returns `deny` and the API server rejects the request with a descriptive error.
  * *Why A is incorrect:* OPA Gatekeeper policies are agnostic to the trustworthiness of the image source — they enforce the organization's defined rules, not Docker Hub's image quality. "Official" images from Docker Hub still violate a policy that requires internal registry images.
  * *Why C is incorrect:* Kubernetes does not perform post-creation image policy evaluation. Admission control is pre-creation; once a pod object is stored in etcd and scheduled, there is no automatic policy-based termination for pre-existing image policy violations.
  * *Why D is incorrect:* Automatically rewriting the image reference is the behavior of a mutating admission webhook, not a validating webhook. OPA Gatekeeper can be configured as either type, but a registry allowlist policy is typically a validating policy (enforce or deny), not a mutating one.

---

**Question 4**
A team member asks: "We already run SAST and SCA on every pull request. Do we really need container image scanning (Trivy) as well?" Which response correctly explains why all three are necessary?

* A) No — SAST and SCA together cover all possible vulnerability classes; Trivy adds no additional security value and slows down the pipeline unnecessarily
* B) Yes — SAST detects insecure code patterns in the application's own code; SCA detects CVEs in application-level dependencies listed in manifest files; Trivy detects CVEs in OS packages, system libraries, and language runtimes installed in the container image that SCA does not scan. Each tool covers a distinct attack surface layer
* C) Yes — but only if the organization is subject to PCI-DSS compliance; non-regulated organizations do not need container image scanning
* D) No — if the base image is official and from Docker Hub, it has already been scanned by Docker and no additional scanning is required
* **Correct Answer:** B) SAST, SCA, and container image scanning have complementary, non-overlapping coverage. Removing any one of them leaves an entire category of vulnerability undetected.
* **Distractor Analysis:**
  * *Why B is correct:* A concrete example: an application using a patched version of all its pip/npm dependencies (SCA passes) running on Ubuntu 20.04 base image (Trivy finds 15 CRITICAL OS CVEs in `glibc`, `openssl`, `libcurl`). SCA cannot see OS packages — Trivy is required to detect them. Similarly, SAST cannot see CVEs in dependencies (SCA's job).
  * *Why A is incorrect:* SAST and SCA do not scan OS-level packages installed in container images. This is a materially distinct attack surface — OS CVEs are among the most commonly exploited in containerized environments.
  * *Why C is incorrect:* Container image scanning provides security value regardless of regulatory framework. The presence of CRITICAL OS CVEs in unscanned images creates real exploitable risk for any organization, regulated or not.
  * *Why D is incorrect:* Docker Hub's official images are scanned by Docker's security tooling, but those scans may lag behind the latest CVE disclosures, and the scanning criteria may differ from the organization's policy. Additionally, "official" images may still contain packages with known CVEs — organizations are responsible for their own risk posture, not Docker Hub's scanning cadence.

---

**Question 5**
A CDP exam question presents the following scenario: "An organization wants to prevent any Terraform infrastructure change from being applied unless: (a) the change passed a Checkov security scan, (b) the pull request was approved by two reviewers, and (c) the pipeline run that produced the `terraform plan` is the same run that executes `terraform apply`." Which combination of controls implements all three requirements?

* A) Add a comment template to the Terraform PR description reminding reviewers to check Checkov results before approving, and use `terraform apply -auto-approve` in the pipeline for consistency
* B) Configure a GitHub Actions workflow with: a Checkov step that fails the pipeline on CRITICAL findings (requirement a); branch protection requiring two reviewer approvals as a required status check (requirement b); and a pipeline design where `apply` is a dependent job that only runs after `plan` and Checkov pass within the same workflow run, using the plan artifact from that run (requirement c)
* C) Run Checkov, approval collection, and `terraform apply` as three separate independent workflows triggered on different schedules to avoid pipeline complexity
* D) Store the Checkov scan results in a shared wiki page that the two reviewers must read and acknowledge in the PR comment before the pipeline proceeds to apply
* **Correct Answer:** B) A GitHub Actions workflow combining a Checkov blocking step, branch protection with two required reviewer approvals, and a `needs:` dependency chain from plan to apply within the same workflow run satisfies all three requirements technically and enforces them automatically.
* **Distractor Analysis:**
  * *Why B is correct:* (a) The Checkov step with `--exit-code 1` fails the pipeline on critical findings, blocking the `plan` and `apply` jobs. (b) Branch protection with `required_pull_request_reviews: required_approving_review_count: 2` enforces two approvals before merge. (c) The `needs: [checkov, plan]` dependency in the `apply` job ensures apply uses the plan artifact from the exact same pipeline run that passed the scan — preventing plan-substitution attacks.
  * *Why A is incorrect:* Comment templates are advisory, not enforced. `-auto-approve` removes the human checkpoint and does not guarantee the apply uses the same run's plan. Neither control is technical enforcement.
  * *Why C is incorrect:* Separate, independently scheduled workflows cannot enforce that all three conditions are satisfied for the same change. An apply workflow could run independently of the Checkov scan workflow, defeating the security intent.
  * *Why D is incorrect:* Wiki acknowledgement in PR comments is a manual, honor-system control. It does not technically enforce that the Checkov scan actually passed for this specific plan, nor does it prevent a reviewer from approving without reading the results.
