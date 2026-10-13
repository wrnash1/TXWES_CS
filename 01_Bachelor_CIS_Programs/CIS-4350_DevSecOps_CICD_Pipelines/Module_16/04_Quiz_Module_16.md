# Quiz: Module 16 — DevSecOps Professional Exam Preparation

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

Instructions: Select the single best answer for each question. These questions consolidate material across all sixteen modules and mirror the scenario-based format of the DSOE certification exam.

---

### Question 1

A DevSecOps pipeline runs SAST, SCA, and container image scanning — all passing with no CRITICAL findings. After deployment to staging, a DAST scan finds a CRITICAL authentication bypass vulnerability. Which statement best explains why the earlier scans did not catch this finding?

- A) The SAST, SCA, and container scans are misconfigured — all three should have caught an authentication bypass
- B) Authentication bypass vulnerabilities often only manifest when the full application runs — with session management, configuration, and middleware integrated — which DAST tests by interacting with the live application, while SAST, SCA, and image scans analyze static artifacts without executing the application
- C) DAST always produces more findings than SAST and SCA combined; the earlier tools should be replaced with a DAST-only approach to eliminate redundancy
- D) The staging environment differs from production, so the finding is likely a false positive that will not exist in production

Correct Answer: B — Authentication bypass is a runtime vulnerability that depends on how session handling, middleware, and configuration interact when the application executes. DAST sends HTTP requests to the running application and observes responses — detecting vulnerabilities that only appear in the integrated running system. SAST analyzes source code logic (cannot execute it), SCA analyzes dependency versions (not authentication logic), and container scanning analyzes installed packages (not application behavior). Each tool covers a distinct scope; none is redundant.

Distractor Analysis:

- Why A is incorrect: SAST can detect some authentication implementation bugs (missing authentication checks in code paths), but it cannot detect authentication bypass vulnerabilities that depend on runtime session state, middleware ordering, or framework configuration. This is a fundamental scope limitation, not a misconfiguration.
- Why C is incorrect: DAST requires a running application and cannot scan source code or dependencies. Replacing SAST and SCA with DAST would eliminate shift-left detection of code vulnerabilities and known CVEs. Defense in depth requires all three layers.
- Why D is incorrect: Staging should replicate production configuration for security testing to be meaningful. Dismissing a CRITICAL finding as a staging false positive without investigation is the kind of reasoning that leads to production security incidents.

---

### Question 2

A security team deploys Falco to all production Kubernetes nodes with default rules. Two weeks later, Falco fires the following alert: `Sensitive file opened for reading by non-trusted program (user=www-data command=cat file=/etc/shadow)`. The application pod that generated this alert is a web server. What is the correct incident response sequence?

- A) Restart the pod — the alert was likely caused by a health check script reading system files; no investigation is required
- B) Isolate the affected pod (remove it from service), capture forensic state (logs, process list, open file descriptors, network connections), analyze how `/etc/shadow` was accessed from a web server process, and escalate to the security team for root cause analysis
- C) Tune the Falco rule to exclude `www-data` from the sensitive file alert since web servers legitimately read system files
- D) Delete the `/etc/shadow` file from the container to prevent further access — the container's shadow file is not needed for application operation

Correct Answer: B — `/etc/shadow` contains hashed system passwords and should never be read by a web server process. This alert indicates either a malicious actor who has compromised the web application and is attempting credential harvesting, or a severe application misconfiguration that enables file disclosure. The correct response follows the incident response principle: preserve evidence before remediation. Isolate the pod to prevent further damage, capture forensic state while the pod is still running, then conduct root cause analysis. Deleting files or restarting the pod destroys forensic evidence.

Distractor Analysis:

- Why A is incorrect: Health check scripts do not read `/etc/shadow`. This alert has no legitimate operational explanation for a web server. Dismissing it as noise from a health check is incorrect and would suppress a genuine security alert.
- Why C is incorrect: Excluding `www-data` from the sensitive file alert would create a blind spot for exactly this attack pattern — a compromised web application process harvesting credentials. Falco rules should be tuned for false positives, not for alert patterns that represent real attacks.
- Why D is incorrect: Deleting `/etc/shadow` from the container does not address the root cause (how did the web server process gain access to read it?) and destroys forensic evidence needed to understand the attack vector. The file is part of the container image; deletion from a running container would also not persist across pod restarts.

---

### Question 3

An engineer is designing a GitHub Actions workflow for a Node.js application. The workflow needs to: check out code, install npm dependencies, run SAST (Semgrep), build a container image, push to Amazon ECR, and deploy to EKS. The engineer wants to follow the principle of least privilege for the GitHub Actions GITHUB_TOKEN. Which permissions configuration is correct?

- A) Set `permissions: write-all` at the workflow level to ensure no job fails due to insufficient permissions
- B) Set `permissions: {}` at the workflow level to deny all default permissions, then grant per-job permissions: `contents: read` for checkout, `packages: write` for ECR push, and `id-token: write` for OIDC authentication to AWS
- C) Omit the permissions block entirely — GitHub Actions defaults to read-only which is sufficiently secure
- D) Set `permissions: read-all` at the workflow level — this provides read access to all resources while preventing write operations

Correct Answer: B — Least privilege for GitHub Actions GITHUB_TOKEN requires setting the minimum permissions needed per job. `permissions: {}` at the workflow level denies all defaults; per-job grants open only what that specific job requires. `contents: read` covers checkout; `packages: write` covers container registry push; `id-token: write` enables OIDC federation to AWS (so no static AWS credentials are needed). This is the DSOE-recommended pattern for CI/CD token permissions.

Distractor Analysis:

- Why A is incorrect: `write-all` grants maximum permissions to every job — the broadest possible scope. If any job is compromised (via a malicious dependency or a pull-request-triggered workflow running untrusted code), the token can be used to push to the repository, modify releases, or write to package registries.
- Why C is incorrect: The default token permissions are repository-setting-dependent and often broader than read-only in older or misconfigured repositories. Relying on defaults is not a least-privilege practice; explicit permission grants are required.
- Why D is incorrect: `read-all` is more restrictive than `write-all` but still grants read access to all scopes — including secrets references, deployment configurations, and private packages. The correct pattern is to deny all defaults and grant only what each job explicitly needs.

---

### Question 4

A HashiCorp Vault administrator wants to provide database credentials to a Flask application running in Kubernetes. Two options are considered: (Option A) store the PostgreSQL username and password in Vault's KV secrets engine with a 90-day rotation policy; (Option B) configure Vault's database secrets engine to generate a unique PostgreSQL username and password for each application request, with a 1-hour TTL. Which option is more secure and why?

- A) Option A — 90-day rotation is industry standard and provides sufficient security for production database credentials
- B) Option B — dynamic secrets with a 1-hour TTL ensure that any stolen credential expires before it can be extensively exploited; a different credential is issued to each requesting pod, limiting blast radius; and no long-lived static credential exists in Vault that can be stolen
- C) Both options are equivalent in security — the important factor is that credentials are stored in Vault rather than in source code, not the TTL length
- D) Option A — Vault's KV engine uses AES-256 encryption which makes credential theft mathematically infeasible regardless of TTL

Correct Answer: B — Dynamic secrets eliminate the primary risk of static credentials: long-lived credentials that can be stolen and reused indefinitely. With a 1-hour TTL, a stolen credential expires quickly and automatically. Each pod receives unique credentials, so a credential from one compromised pod cannot be used to access the database from another context. With Option A, a 90-day credential that is compromised on day 1 remains valid for 89 more days. TTL length directly determines the exploit window for any compromised credential.

Distractor Analysis:

- Why A is incorrect: 90-day rotation is better than never rotating, but it represents a 90-day exploit window. Industry best practice for high-sensitivity credentials (production database access) has moved toward dynamic, short-TTL credentials precisely because static long-lived credentials are the most common class of stolen credential exploited in breaches.
- Why C is incorrect: Storing credentials in Vault rather than source code is a significant improvement, but the TTL fundamentally changes the risk profile. A static secret in Vault that is leaked via a misconfigured Vault policy or a compromised Vault token remains exploitable for the full rotation period. TTL is a critical security parameter.
- Why D is incorrect: Encryption of the stored secret prevents unauthorized reading from Vault's storage backend. It does not prevent authorized-but-compromised access paths (a leaked Vault token, an over-privileged Vault policy). The TTL addresses the time-to-exploit window for any credential that escapes through any path, including legitimate ones.

---

### Question 5

A DSOE exam question describes: "An organization runs mandatory SAST, SCA, and Trivy container scanning gates. The pipeline logs show that all three gates passed on every production deployment in the past quarter. However, the CISO reports three critical security incidents involving exploited vulnerabilities in production during the same period." Which explanation is most consistent with all facts presented?

- A) The scanning tools are defective — a correctly configured pipeline would have caught all three vulnerabilities
- B) The three vulnerabilities were either zero-days (CVEs published after the deployments were scanned), exploited via runtime behavior that static and image scanning cannot detect (requiring DAST or Falco), or introduced via configuration changes that bypassed the code pipeline — such as direct kubectl apply commands that skipped CI/CD
- C) The Security Champions failed to triage the scan results — the findings were present but ignored
- D) The change failure rate is too low — organizations with elite DevOps performance do not experience security incidents

Correct Answer: B — When all pipeline gates pass but production incidents still occur, the three most common explanations are: (1) zero-day vulnerabilities that were not in the NVD/CVE database at scan time; (2) runtime vulnerabilities that require execution to exploit (authentication bypass, SSRF, business logic flaws) that SAST and container scanning cannot detect; (3) changes deployed outside the CI/CD pipeline (direct kubectl apply, manual production patches) that bypass all gates. The scenario specifically states the pipeline logs show gates passed — not that findings were ignored.

Distractor Analysis:

- Why A is incorrect: A correctly configured pipeline with SAST, SCA, and container scanning does not catch all possible vulnerabilities. These tools have defined scopes and cannot detect zero-days, runtime vulnerabilities, or out-of-band configuration changes. "Defective" implies the tools failed at their defined purpose; the scenario is more likely a scope gap.
- Why C is incorrect: The scenario states "pipeline logs show all three gates passed" — not that findings were found and ignored. If gates passed, no findings were generated for champions to triage. Champion triage is relevant when findings exist but are not remediated, not when gates pass cleanly.
- Why D is incorrect: Change Failure Rate measures the percentage of deployments that cause failures. High change failure rate (frequent incidents) indicates stability problems, but elite DORA performance does not eliminate security incidents — it means the organization can recover from them quickly (low MTTR). Elite performers still experience security incidents.

---

### Question 6

A Kubernetes namespace has the Pod Security Admission label `pod-security.kubernetes.io/enforce: restricted`. A developer deploys a pod with `securityContext.runAsNonRoot: true` and `securityContext.allowPrivilegeEscalation: false` but omits `capabilities.drop: [ALL]`. What is the expected behavior?

- A) The pod deploys successfully — runAsNonRoot and allowPrivilegeEscalation are the two most important security context fields; capabilities.drop is optional
- B) The pod is rejected by the Pod Security Admission controller because the `restricted` profile requires containers to drop all capabilities; `capabilities.drop: [ALL]` is a mandatory field under the restricted profile
- C) The pod deploys with a warning, and Falco generates an alert that the pod has excessive capabilities at runtime
- D) The pod deploys successfully but OPA/Gatekeeper generates a policy violation report that is reviewed in the next security audit

Correct Answer: B — The Kubernetes `restricted` Pod Security Standard requires all of the following: `runAsNonRoot: true`, `allowPrivilegeEscalation: false`, `capabilities.drop: [ALL]`, `seccompProfile.type: RuntimeDefault` or `Localhost`, and `volumes` restricted to safe types. All criteria must be met; the `restricted` profile does not allow partial compliance. A pod missing `capabilities.drop: [ALL]` is rejected at admission with a descriptive error message. Pod Security Admission with `enforce` mode is a hard block, not a warning.

Distractor Analysis:

- Why A is incorrect: The `restricted` profile is explicitly defined as requiring all listed criteria. `capabilities.drop: [ALL]` is not optional under `restricted` — it is a required criterion. Partial Security Context compliance does not satisfy the restricted profile.
- Why C is incorrect: Pod Security Admission in `enforce` mode rejects non-compliant pods at the API server — they are never scheduled. Falco only monitors running containers, so it cannot generate an alert for a pod that was never scheduled. The `warn` mode (not `enforce`) would allow the pod to deploy with a warning.
- Why D is incorrect: Pod Security Admission and OPA/Gatekeeper are separate systems. PSA enforcement happens independently of Gatekeeper. With `enforce: restricted`, PSA rejects the pod immediately at admission — it does not defer to a policy report review cycle.

---

### Question 7

A compliance officer asks: "What is the difference between a SOC 2 audit and Compliance as Code?" Which answer correctly describes the relationship?

- A) SOC 2 is a technical standard for cloud applications; Compliance as Code is the organizational process for tracking SOC 2 findings
- B) SOC 2 is a third-party audit framework that assesses whether an organization's controls meet Trust Services Criteria at a point in time; Compliance as Code is the technical approach of expressing those control requirements as executable, version-controlled policy code that automatically enforces compliance on every deployment — providing continuous evidence rather than periodic snapshots
- C) They are synonymous — Compliance as Code is the modern term for the SOC 2 audit process
- D) SOC 2 applies to on-premises systems; Compliance as Code applies to cloud-native systems

Correct Answer: B — SOC 2 is an external audit standard produced by the AICPA; it defines Trust Services Criteria (Security, Availability, Confidentiality, Processing Integrity, Privacy) and auditors assess whether an organization's controls meet those criteria, typically through an annual Type II audit. Compliance as Code is an implementation approach: encoding compliance requirements as OPA Rego policies, Conftest tests, Checkov rules, and pipeline gates that run automatically on every deployment. The two are complementary: Compliance as Code provides the continuous machine-verifiable evidence that satisfies the SOC 2 auditor's evidence requirements for continuous control operation.

Distractor Analysis:

- Why A is incorrect: SOC 2 is not a technical standard for cloud applications — it is an audit framework that can apply to any service organization. Compliance as Code is not an organizational tracking process; it is a technical implementation pattern.
- Why C is incorrect: They are not synonymous. SOC 2 predates the DevSecOps movement and is an external audit framework. Compliance as Code is an engineering practice. One is a compliance standard; the other is a technical implementation approach that generates evidence for compliance standards.
- Why D is incorrect: SOC 2 applies to any service organization that handles customer data, whether on-premises or cloud-native. Compliance as Code is most commonly implemented in cloud-native pipelines but is not limited to cloud environments.

---

### Question 8

A development team has implemented a full DevSecOps pipeline: SAST, SCA, container scanning, secrets scanning, IaC scanning, artifact signing, OPA/Gatekeeper, and Falco. A DSOE exam question asks: which control specifically provides evidence for the non-repudiation security property — ensuring that a specific developer cannot deny that they introduced a specific change to the codebase?

- A) SAST — because it identifies which developer introduced a vulnerable code pattern by analyzing commit history
- B) OPA/Gatekeeper — because it logs which admission controller policy was violated and the identity of the service account that made the API call
- C) Signed commits with Git GPG or SSH commit signing, enforced via branch protection rules — because each commit is cryptographically signed with the developer's private key, creating an unforgeable binding between the developer's verified identity and the specific code change
- D) Falco — because Falco logs the user identity associated with every container system call

Correct Answer: C — Non-repudiation requires that an action can be definitively attributed to a specific actor in a way that cannot be denied. Git commit signing uses asymmetric cryptography: the developer signs each commit with their private key; anyone can verify the signature with the developer's public key. Because only the developer holds the private key, a valid signature on a commit proves the developer authored it. Branch protection rules that require signed commits enforce this at the repository level, ensuring every commit in the protected branch has a verified developer identity.

Distractor Analysis:

- Why A is incorrect: SAST identifies vulnerability patterns in code but does not provide cryptographic attribution of authorship. Git blame provides commit author metadata, but that metadata can be forged. Signed commits provide cryptographic proof that cannot be forged without the private key.
- Why B is incorrect: OPA/Gatekeeper logs the service account identity for Kubernetes API calls — relevant for operational accountability in cluster operations but not for code authorship attribution. It does not address who wrote the application code.
- Why D is incorrect: Falco logs the Linux user identity associated with system calls in running containers — relevant for runtime incident attribution, not code change attribution. A Falco alert can tell you which container process performed a suspicious action; it cannot tell you which developer committed the code that contains the vulnerability.

---

### Question 9

An organization has completed DSOE Modules 1–15. The security architect wants to verify the pipeline provides complete defense in depth. Which gap analysis statement correctly identifies the one missing control if the current pipeline has SAST, SCA, Trivy, detect-secrets, Checkov, Cosign image signing, and OPA/Gatekeeper?

- A) There is no runtime monitoring — without Falco or equivalent eBPF-based syscall monitoring, the pipeline has no visibility into container behavior after deployment, leaving exploitation of running containers undetected
- B) There is no SCA tool — Trivy and Checkov do not scan application dependency manifests for known CVEs in third-party libraries
- C) There is no IaC scanning — Cosign and OPA do not evaluate Kubernetes manifests for security misconfigurations before apply
- D) There is no admission control — detect-secrets and Checkov do not enforce Kubernetes security policies at deployment time

Correct Answer: A — The listed controls cover: code vulnerabilities (SAST), dependency CVEs (SCA/Trivy), image CVEs (Trivy), secrets in code (detect-secrets), IaC misconfigurations (Checkov), supply chain integrity (Cosign), and admission control (OPA/Gatekeeper). The one missing layer is runtime monitoring — what happens after the pod is running. Falco provides continuous visibility into container behavior at the syscall level, detecting exploitation of running containers, container escape attempts, and sensitive file access. Without runtime monitoring, an attacker who gains code execution inside a container operates undetected.

Distractor Analysis:

- Why B is incorrect: Trivy scans both container images (OS packages) and application dependency files. With SCA tools like OWASP Dependency-Check, Snyk, or Grype also listed, the dependency CVE layer is covered. SCA is present.
- Why C is incorrect: Checkov explicitly provides IaC scanning for Kubernetes manifests, Terraform, Helm charts, and other infrastructure files. IaC scanning is present.
- Why D is incorrect: OPA/Gatekeeper explicitly provides admission control — it is a Validating Admission Webhook that enforces Kubernetes security policies at admission time. Admission control is present.

---

### Question 10

A DSOE candidate reviews a scenario: "An organization's SAMM Secure Build practice is at Level 2. Their security team recommends enabling DAST in the staging pipeline to advance their maturity." Which SAMM function and practice does DAST integration advance, and what level does it advance to?

- A) Implementation: Secure Build — Level 3; DAST is a build-time tool that strengthens the Secure Build practice
- B) Verification: Security Testing — Level 2; DAST integration in the staging pipeline advances the Security Testing practice from Level 1 (periodic manual testing) to Level 2 (automated security testing integrated in the pipeline)
- C) Operations: Incident Management — Level 2; DAST alerts feed the incident management process
- D) Design: Threat Assessment — Level 3; DAST findings inform threat model updates

Correct Answer: B — In OWASP SAMM, the Verification function contains the Security Testing practice. Level 1 is periodic manual penetration testing or ad hoc security testing. Level 2 is automated security testing integrated into the software delivery pipeline — including DAST at the staging stage. DAST integration is the Level 1 to Level 2 advancement for Security Testing because it converts periodic manual testing into automated pipeline-integrated testing that runs on every deployment to staging. SAST at the build stage is part of Implementation: Secure Build. DAST, which tests the running application, belongs to Verification: Security Testing.

Distractor Analysis:

- Why A is incorrect: SAST and SCA gate enforcement are Secure Build practices under the Implementation function. DAST operates on a running application, not on source code or build artifacts — it belongs to the Verification function, not Implementation.
- Why C is incorrect: Incident Management is an Operations function practice that covers how the organization responds to confirmed security incidents. DAST findings are pre-production test results; they inform remediation before deployment, not incident response after exploitation.
- Why D is incorrect: Threat Assessment is a Design function practice that covers threat modeling at the design phase. DAST findings can inform future threat model updates, but integrating DAST into the pipeline is a Verification: Security Testing maturity advancement, not a Design function activity.

---

### Question 11

A pipeline has SAST, SCA, and container scanning all passing. A new dependency is added to `requirements.txt`. The SCA gate passes because the dependency has no known CVEs at the time of the commit. Six weeks later, a CVE is published for that dependency. Which control is designed to catch this post-commit vulnerability disclosure?

- A) The SAST gate — SAST re-analyzes dependencies continuously as CVE databases are updated
- B) A Snyk `monitor` or OWASP Dependency-Check scheduled pipeline job that re-scans the production artifact's dependency manifest against the current CVE database on a recurring schedule
- C) The container scan gate — Trivy re-scans images continuously after they are pushed to the registry
- D) The pre-commit secrets hook — it would detect the new dependency's credentials if exposed

Correct Answer: B — SCA gates run at CI time against the CVE database as of that moment. New CVEs published after the build are not retroactively detected by the CI gate. Continuous SCA monitoring tools (Snyk `monitor`, OWASP Dependency-Track, or a scheduled Dependency-Check job) re-evaluate the registered dependency manifest against a continuously updated CVE database and alert when new vulnerabilities are published against known-deployed versions. This is the post-deploy continuous SCA monitoring pattern.

Distractor Analysis:

- Why A is incorrect: SAST analyzes source code logic for code-level vulnerabilities — it does not monitor CVE databases for dependency vulnerabilities. SAST re-runs on code changes, not on CVE database updates.
- Why C is incorrect: Trivy scans when triggered (on push, on schedule, or by the Trivy operator in-cluster). The default container scan job runs at build time. The Trivy operator in Kubernetes provides continuous in-cluster scanning, but this is an additional deployment, not the default CI gate behavior.
- Why D is incorrect: Pre-commit secrets hooks scan for credential patterns in files. They do not analyze dependency CVE status and have no connection to CVE database updates.

---

### Question 12

An organization's pipeline requires that all HIGH and CRITICAL container findings are remediated before deployment. A developer argues that the base image `python:3.11-slim` has 14 HIGH findings that have no available fix versions, and the pipeline should not block on unfixable findings. Which CLI flag resolves this specific issue without permanently lowering the security bar?

- A) `--severity LOW,MEDIUM` — lower the threshold so HIGH findings no longer block the pipeline
- B) `trivy image --ignore-unfixed --severity HIGH,CRITICAL python:3.11-slim` — filter out CVEs without a fixed version, so the gate only fails on findings that the team can actually remediate
- C) `trivy image --skip-files /usr/lib/python3.11 python:3.11-slim` — skip scanning the Python library directory to avoid false positives
- D) Add all 14 CVE IDs to `.trivyignore` without expiry dates to permanently suppress them

Correct Answer: B — `--ignore-unfixed` is the correct tool for this scenario. It filters the output to findings that have a patched version available, making the gate actionable. The HIGH/CRITICAL severity threshold is preserved — the gate still blocks on HIGH and CRITICAL findings that have fixes. This is the standard pattern for reducing base image noise without permanently accepting unfixed CVEs.

Distractor Analysis:

- Why A is incorrect: Lowering the severity threshold to LOW/MEDIUM would allow all HIGH and CRITICAL findings through — a permanent, broad security regression. The problem is specifically about unfixable findings, not about the severity level.
- Why C is incorrect: `--skip-files` skips scanning specific paths regardless of whether findings have fixes. It would hide both fixable and unfixable findings in the Python library directory, including future fixable CVEs.
- Why D is incorrect: `.trivyignore` without expiry dates permanently suppresses specific CVEs. When a fix becomes available for one of those 14 CVEs, the suppression would continue hiding the now-fixable finding. The `--ignore-unfixed` flag dynamically includes a CVE in the output as soon as a fix version is published.

---

### Question 13

A GitHub Actions workflow uses `actions/checkout@v4` without `fetch-depth: 0`. The pipeline runs `gitleaks detect --source .` for secrets scanning. A developer committed an AWS access key in commit `abc123f` six months ago and removed it in commit `def456a` two commits later. The current HEAD commit contains no secrets. Does the pipeline detect the historical secret?

- A) Yes — Gitleaks scans the working directory and would find the deleted file's content in the `.git` object store
- B) No — `actions/checkout@v4` without `fetch-depth: 0` performs a shallow clone with depth 1 (current HEAD only); the historical commit `abc123f` is not present in the shallow clone, so Gitleaks cannot scan it
- C) Yes — GitHub's built-in push protection would have blocked the original commit, so the secret was never actually stored in the repository history
- D) No — Gitleaks only scans staged changes, not committed history; `gitleaks protect` would have caught it at commit time

Correct Answer: B — Without `fetch-depth: 0`, GitHub Actions `actions/checkout@v4` defaults to a shallow clone containing only the HEAD commit (or a limited recent history). The historical commit containing the secret is not present in the shallow clone's `.git` directory, so Gitleaks cannot find it. This is the critical `fetch-depth: 0` requirement for historical secrets scanning.

Distractor Analysis:

- Why A is incorrect: Gitleaks scans the Git history available in the `.git` directory, not a separate object store. A shallow clone's `.git` directory does not contain the full commit history — only the commits included in the shallow clone depth.
- Why C is incorrect: GitHub push protection (when enabled) blocks pushes of known secret patterns, but it was not enabled in all repositories by default for the timeframe described. Even with push protection enabled, it does not guarantee all secrets are blocked — only known patterns. Historical secrets in existing repositories are a separate concern from push protection.
- Why D is incorrect: `gitleaks detect` scans repository history; `gitleaks protect` scans staged changes. The scenario uses `detect` mode — the issue is shallow clone depth preventing history access, not Gitleaks' mode.

---

### Question 14

A Kubernetes cluster uses the `restricted` PodSecurity profile in `enforce` mode on the `production` namespace. A deployment manifest includes `securityContext.runAsNonRoot: true` and `securityContext.allowPrivilegeEscalation: false` but omits `capabilities.drop: [ALL]`. What is the admission outcome?

- A) The pod is admitted — `runAsNonRoot` and `allowPrivilegeEscalation: false` satisfy the `restricted` profile requirements
- B) The pod is rejected — the `restricted` profile requires all three: `runAsNonRoot: true`, `allowPrivilegeEscalation: false`, AND `capabilities.drop: [ALL]`; an incomplete Security Context fails admission
- C) The pod is admitted with a warning — missing `capabilities.drop` generates a warning but does not block admission in `enforce` mode
- D) The pod is admitted — capability drops are only required in the `baseline` profile, not `restricted`

Correct Answer: B — The Kubernetes Pod Security Standards `restricted` profile has a defined set of requirements that all must be satisfied. The required Security Context fields include: `runAsNonRoot: true`, `allowPrivilegeEscalation: false`, `seccompProfile.type: RuntimeDefault` (or Localhost), AND `capabilities.drop: [ALL]` with only a specific allowlist of capabilities permitted. An incomplete Security Context that omits any required field fails the `restricted` profile check in `enforce` mode.

Distractor Analysis:

- Why A is incorrect: Satisfying some but not all `restricted` profile requirements is not sufficient. The profile is a complete specification — all conditions must be met. Two out of four required fields is a failing configuration.
- Why C is incorrect: In `enforce` mode, violations result in rejection, not warnings. Warnings are the behavior of `warn` mode. `enforce` mode rejects the admission request.
- Why D is incorrect: `capabilities.drop: [ALL]` is a requirement of the `restricted` profile specifically. The `baseline` profile prohibits certain capabilities (like `SYS_ADMIN`) but does not require dropping all capabilities. `restricted` is the more stringent profile that requires dropping all capabilities.

---

### Question 15

A security engineer reviews a Checkov scan result that shows `FAILED for resource: aws_s3_bucket.data [CKV_AWS_18]`. The Terraform file shows the bucket has versioning enabled, server-side encryption enabled, and public access blocked. Why is the check still failing?

- A) Checkov CKV_AWS_18 checks for S3 server-side encryption — the scan result contradicts the description
- B) Checkov CKV_AWS_18 checks for S3 access logging — a separate configuration block enabling access logging is required even though versioning, encryption, and public access are correctly configured
- C) Checkov CKV_AWS_18 checks for S3 bucket versioning — the versioning configuration has a syntax error
- D) Checkov cannot evaluate S3 resources that have encryption enabled — the finding is a known false positive

Correct Answer: B — CKV_AWS_18 specifically checks that S3 bucket access logging is enabled (the `logging` block in the Terraform `aws_s3_bucket` resource). Versioning, encryption, and public access block are separate controls with their own check IDs. Multiple S3 security checks can fail independently: CKV_AWS_18 (access logging), CKV_AWS_19 (encryption), CKV_AWS_20 (public ACL), CKV_AWS_57 (public policy). A bucket can pass some checks and fail others.

Distractor Analysis:

- Why A is incorrect: CKV_AWS_18 is the access logging check, not the encryption check. CKV_AWS_19 covers server-side encryption. The scenario states encryption is enabled — CKV_AWS_19 would pass. CKV_AWS_18 failing independently of encryption status is consistent.
- Why C is incorrect: Versioning is covered by a different Checkov check ID. CKV_AWS_18 is access logging specifically. Versioning configuration syntax errors would also produce a different failure mode.
- Why D is incorrect: Checkov evaluates S3 resources regardless of their encryption status. Each check tests a specific attribute independently. Encryption being enabled does not cause false positives for unrelated checks.

---

### Question 16

In a GitHub Actions pipeline, a `secrets-scan` job uses `gitleaks/gitleaks-action@v2`. The job is defined with `if: github.event_name == 'push'`. A developer opens a PR from a feature branch. Does the secrets scan run?

- A) Yes — pull request events are included in `push` events in GitHub Actions
- B) No — `github.event_name == 'push'` only evaluates to true for direct push events (`git push`), not for pull request creation events (`pull_request`). The secrets scan is not triggered by a PR.
- C) Yes — the Gitleaks action overrides the `if` condition and always runs on all events
- D) No — the job requires `fetch-depth: 0` to run; without it, the `if` condition always evaluates to false

Correct Answer: B — In GitHub Actions, `github.event_name` is set to the name of the event that triggered the workflow. A `git push` sets `event_name` to `push`. Opening a pull request sets `event_name` to `pull_request`. These are distinct event types. The `if: github.event_name == 'push'` condition is false for pull request events, so the job is skipped. To also scan on PRs, the condition should be `if: github.event_name == 'push' || github.event_name == 'pull_request'`.

Distractor Analysis:

- Why A is incorrect: `push` and `pull_request` are distinct event types in GitHub Actions. A pull request creation does not trigger `push` event handlers. The trigger must explicitly include `pull_request` in the workflow's `on:` clause or the `if` condition.
- Why C is incorrect: GitHub Actions step and job conditions (`if:`) are evaluated by the GitHub Actions runner before executing any action. An action's internal logic cannot override a job-level `if` condition — if the condition is false, the job does not execute at all.
- Why D is incorrect: `fetch-depth: 0` controls whether the checkout step clones full Git history. It is a parameter of `actions/checkout@v4`, not a prerequisite for evaluating `if` conditions. These are unrelated mechanisms.

---

### Question 17

A team is building a complete DevSecOps pipeline and has enabled all of the following gates: Gitleaks secrets scan, Semgrep SAST, OWASP Dependency-Check SCA, Trivy container scan, and Checkov IaC scan. Which security domain is NOT covered by any of these five tools?

- A) Hardcoded credentials in source code
- B) Known CVEs in application dependencies
- C) Runtime behavioral anomalies in a running production container
- D) Misconfigured Terraform S3 bucket policies

Correct Answer: C — Runtime behavioral anomaly detection requires a tool that observes the running system — container process activity, syscalls, network connections, and file access patterns at runtime. None of the five CI pipeline tools (secrets scan, SAST, SCA, container scan, IaC scan) observe runtime behavior. This is the gap that Falco fills: it runs as a DaemonSet in Kubernetes and detects suspicious runtime behavior using syscall-level rules.

Distractor Analysis:

- Why A is incorrect: Hardcoded credentials in source code are detected by secrets scanning tools (Gitleaks). This domain is covered.
- Why B is incorrect: Known CVEs in application dependencies are detected by SCA tools (OWASP Dependency-Check, Snyk). This domain is covered.
- Why D is incorrect: Misconfigured Terraform resources are detected by IaC scanning tools (Checkov, tfsec). S3 bucket policy misconfigurations are specifically covered by Checkov CKV_AWS checks. This domain is covered.

---

### Question 18

A team wants to enforce that GitHub Actions workflows in their organization never use `pull_request_target` with a `checkout` step that checks out code from the PR head ref. Which risk does this combination create, and which control enforces the restriction?

- A) It creates a Denial of Service risk; enforce with a `--timeout` flag on all workflow jobs
- B) It creates a supply chain injection risk: `pull_request_target` runs with repository write permissions and access to secrets; if it checks out PR head code (from a fork), an attacker can submit a PR with a malicious `run:` step that exfiltrates secrets. A CODEOWNERS rule on `.github/workflows/` requiring security review of workflow changes enforces the restriction
- C) It creates an infinite loop risk when the workflow modifies the repository; enforce with `concurrency: cancel-in-progress: true`
- D) It creates a branch protection bypass; enforce by requiring status checks from all workflow jobs before merge

Correct Answer: B — `pull_request_target` runs in the context of the target branch (with full write permissions and access to secrets), but if the workflow also checks out code from the PR head ref (the contributor's fork), an attacker can craft a malicious workflow step in their fork that runs with the target branch's elevated permissions — a classic CI/CD injection attack. CODEOWNERS review of workflow files is the primary preventive control, ensuring that any change to `pull_request_target` workflows is reviewed by a security engineer.

Distractor Analysis:

- Why A is incorrect: The risk is secret exfiltration and supply chain injection, not DoS. Timeout flags address runaway processes, not credential theft.
- Why C is incorrect: `concurrency` settings control whether multiple workflow runs execute simultaneously. They have no connection to the security risk of running untrusted code with elevated permissions.
- Why D is incorrect: Branch protection status checks ensure that required CI jobs pass before merge. They do not prevent a malicious PR from running elevated-permission steps in a `pull_request_target` workflow before the merge decision.

---

### Question 19

A full DSOE exam preparation scenario: A team has the following security posture — Gitleaks pre-commit, Semgrep SAST on PR, Snyk SCA on PR, Trivy container scan at build, Cosign signing at push, Checkov IaC on PR, OWASP ZAP DAST at staging, OPA Gatekeeper on production cluster, Falco DaemonSet. An attacker compromises an engineer's workstation and modifies a legitimate application library in the engineer's local `node_modules/` folder before the build step runs, injecting malicious code that exfiltrates environment variables at runtime. Which control gap does this attack exploit?

- A) There is no gap — Semgrep SAST would detect the injected code in the library file before build
- B) The attack exploits the gap between local build environments and the CI build environment: CI should build from a clean dependency install (`npm ci` from `package-lock.json`) rather than using developer-supplied artifacts; additionally, Cosign signs the final built image but cannot detect code injected into a local `node_modules/` cache before CI fetch
- C) Falco would detect the environment variable exfiltration at runtime and prevent data loss
- D) Snyk SCA would detect the modification because it scans installed packages against known-good signatures

Correct Answer: B — This is a CI build environment integrity threat. If the CI pipeline uses developer-supplied artifacts (a locally modified `node_modules/`) rather than building from a clean fetch, malicious modifications to local dependencies bypass all pre-commit and PR scanning controls. The mitigation is build integrity: the CI pipeline should always run `npm ci` (or `pip install -r requirements.txt`) from the lockfile — downloading dependencies fresh from the registry, not copying from a developer's local environment. This ensures CI scans the same artifacts that will be in the final image.

Distractor Analysis:

- Why A is incorrect: Semgrep SAST scans the application's source code in the repository, not installed `node_modules/` files. Injected library code in `node_modules/` is not in the repository and is not scanned by SAST unless the `node_modules/` directory is committed (an anti-pattern).
- Why C is incorrect: Falco detects runtime anomalies — it might detect suspicious outbound connections or unusual process behavior, but it would not prevent the initial data exfiltration if the malicious code disguises its behavior. Falco is a detective, not a preventive control for this attack.
- Why D is incorrect: Snyk SCA scans declared dependencies in `package.json`/`package-lock.json` against the CVE database. It does not verify the integrity of installed package files against their expected content. A locally modified `node_modules/` package would not be flagged by CVE-based SCA.

---

### Question 20

A DSOE candidate must design a DevSecOps pipeline for a healthcare application that processes Protected Health Information (PHI). The pipeline must satisfy HIPAA Technical Safeguard requirements for access controls and audit logging. Which combination of pipeline and runtime controls maps most directly to HIPAA Technical Safeguard requirements?

- A) Run OWASP Dependency-Check and ship the SCA report to the auditors annually
- B) Configure SAST with HIPAA-specific rules; deploy OPA Gatekeeper policies enforcing `runAsNonRoot` and `readOnlyRootFilesystem` (access control safeguards); configure Kubernetes audit logging to an immutable log store and enable Falco runtime alerts for anomalous data access (audit logging safeguards); encrypt all data at rest (storage encryption KMS) and in transit (TLS 1.2+); gate deployment on all CRITICAL findings resolved
- C) Deploy a Web Application Firewall in front of the application and configure rate limiting
- D) Conduct an annual third-party penetration test and obtain HIPAA BAA agreements from all cloud providers

Correct Answer: B — HIPAA Technical Safeguards require: access controls (who can access PHI — `runAsNonRoot`, RBAC, least-privilege service accounts, network policies), audit controls (records of access — Kubernetes audit log, Falco alerts, immutable log storage), integrity controls (PHI is not altered improperly — read-only filesystems, signed artifacts), and transmission security (PHI in transit is protected — TLS 1.2+). The combination described maps each Technical Safeguard category to a specific pipeline or runtime control.

Distractor Analysis:

- Why A is incorrect: SCA reports provide dependency vulnerability status but do not address HIPAA Technical Safeguard categories of access control, audit logging, integrity, or transmission security. Annual reporting is a compliance documentation activity, not a safeguard implementation.
- Why C is incorrect: WAF and rate limiting address network-layer availability and some injection risks. They are useful perimeter controls but do not address HIPAA's access control requirements (who is authorized to access PHI within the system) or audit logging requirements.
- Why D is incorrect: Annual penetration testing and BAA agreements are administrative and legal controls. HIPAA Technical Safeguards require implemented technical controls — encryption, access enforcement, audit trails — not just agreements with vendors or point-in-time assessments.

---

Quiz — Module 16 | CIS-4350 | Texas Wesleyan University | Professor Nash
