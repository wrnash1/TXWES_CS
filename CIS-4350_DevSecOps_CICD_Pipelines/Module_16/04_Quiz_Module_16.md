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
