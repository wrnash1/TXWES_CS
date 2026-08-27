# Reading Guide: Module 16 — DevSecOps Professional Exam Preparation

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 16 is the capstone and exam preparation module for CIS-4350. Rather than introducing new material, this guide consolidates high-priority concepts from all fifteen prior modules into the four DSOE exam domains, provides twenty practice questions with full distractor analysis, and supplies a study checklist for exam-day readiness. The DSOE exam tests scenario-based application of concepts — not recall of isolated facts. Use this guide to identify gaps, practice the two-step elimination method, and verify that you can trace every pipeline control back to a threat model requirement.

---

## Section 1: Exam Domain Map

### Domain 1 — Culture and Organizational Transformation

| Topic | Key Concepts | Module |
|---|---|---|
| Security Champion program | Selection, training, authority, community, career recognition | 15 |
| Developer security training | OWASP Top 10, ASVS, SANS DEV541, just-in-time training | 15 |
| Gamification | CTF, bug bounty, team scorecards, recognition | 15 |
| DORA metrics | Deployment Frequency, Lead Time, Change Failure Rate, MTTR | 15 |
| Security KPIs | MTTD, MTTR-Security, Escape Rate, Gate Pass Rate | 15 |
| OWASP SAMM | Five functions, three practices each, three levels | 15 |
| DSOMM | Four levels, five dimensions | 15 |
| Transformation failure modes | Bottleneck, Tool Accumulation, Theater | 15 |

### Domain 2 — CI/CD Pipeline Security

| Topic | Key Concepts | Module |
|---|---|---|
| SAST | Semgrep, Bandit, SpotBugs; commit/PR stage; what it catches | 4 |
| SCA | Dependency-Check, Snyk, Grype; build stage; NVD/OSV | 5 |
| Container image scanning | Trivy, Grype; post-build; OS vs. app CVEs | 6 |
| Secrets scanning | git-secrets, TruffleHog; pre-commit + pipeline | 7 |
| DAST | OWASP ZAP; staging environment; runtime behavior | 9 |
| IaC scanning | Checkov, tfsec; Terraform/K8s manifests; misconfigurations | 10 |
| Artifact signing | Cosign, KMS; supply chain integrity; admission verification | 11 |
| Secrets management | HashiCorp Vault; dynamic secrets; K8s auth; injector | 8 |

### Domain 3 — Container and Kubernetes Security

| Topic | Key Concepts | Module |
|---|---|---|
| Security Contexts | runAsNonRoot, allowPrivilegeEscalation, capabilities.drop | 11 |
| Pod Security Standards | Privileged / Baseline / Restricted profiles; Audit/Warn/Enforce | 11 |
| Network Policies | Default-deny-all; explicit allow; lateral movement prevention | 12 |
| RBAC | Role, ClusterRole, RoleBinding; least-privilege service accounts | 12 |
| OPA/Gatekeeper | ConstraintTemplate, Constraint; Rego; admission webhook | 13 |
| Falco | eBPF syscall rules; default rules; Falcosidekick; SIEM | 12 |

### Domain 4 — Compliance as Code and Monitoring

| Topic | Key Concepts | Module |
|---|---|---|
| Compliance as Code | OPA, Conftest, Checkov, InSpec; continuous vs. periodic | 13 |
| Audit trail components | Signed commit, PR approval, scan results, image digest, pipeline run ID | 13 |
| SOC 2 mapping | CC6.1, CC7.2, CC8.1, CC9.2 | 13 |
| PCI-DSS mapping | Req 6.3, 6.4, 10.2 | 13 |
| SIEM | Log aggregation; correlation rules; multi-source detection | 12 |
| Kubernetes audit logging | API server audit; audit policy; sensitive verbs and resources | 12 |

---

## Section 2: High-Priority Exam Distinctions

The following pairs of concepts are frequently confused on scenario-based exams. Know the precise difference.

**SAST vs. SCA**

- SAST analyzes custom source code for vulnerabilities written by your developers (injection, XSS, hardcoded credentials, insecure API usage). It does not analyze third-party libraries.
- SCA analyzes third-party dependency manifests for known CVEs in libraries your code imports. It does not analyze your custom code logic.
- Container image scanning analyzes installed OS packages and system libraries in the built image. It catches CVEs that SCA misses because SCA only reads manifest files, not the image layer contents.

**OPA/Gatekeeper vs. Falco**

- OPA/Gatekeeper operates at admission time — it validates resources when they are created or modified via the Kubernetes API. It can prevent a non-compliant pod from being scheduled.
- Falco operates at runtime — it monitors system calls made by running containers. It cannot prevent a pod from starting; it detects malicious behavior after the pod is running.
- Use both: OPA prevents misconfiguration; Falco detects exploitation of correctly configured containers.

**Pod Security Standards vs. Network Policies**

- Pod Security Standards control the security configuration of pods (root user, privilege escalation, Linux capabilities). They prevent privilege escalation attacks.
- Network Policies control network communication between pods. They prevent lateral movement after a container is compromised.
- Both are required for a defense-in-depth Kubernetes security posture.

**DORA Change Failure Rate vs. MTTD**

- Change Failure Rate measures the business impact of failed deployments — the percentage that require remediation. Security incidents caused by escaped vulnerabilities increase Change Failure Rate.
- MTTD measures pipeline detection effectiveness — the time from vulnerability introduction to detection. MTTD is an early-warning metric; Change Failure Rate measures what happened when detection failed.

**Secrets management: Vault dynamic secrets vs. static secrets**

- Static secrets are long-lived credentials stored in Vault with ACL-based access control. They are better than environment variables but still represent a long-lived credential risk.
- Dynamic secrets are generated on-demand by Vault for each request, with a short TTL. They expire automatically, eliminating the risk of long-lived credential theft.
- For database credentials and cloud provider credentials, dynamic secrets are the recommended pattern.

**Security Theater vs. Tool Accumulation Without Process**

- Security Theater occurs when gates exist but are bypassed without oversight — the appearance of security without the substance. The gates run; findings appear; nothing is blocked or remediated.
- Tool Accumulation Without Process occurs when tools are added without defining ownership, SLAs, or escalation paths. Findings accumulate in a backlog with no clear owner or response requirement.
- Both can coexist: theater (gates set to warn-only) combined with accumulation (backlog with no process).

---

## Section 3: Pipeline Control to Threat Mapping

| STRIDE Category | Pipeline Control | Stage |
|---|---|---|
| Spoofing | Image signing (Cosign); OIDC-based CI/CD auth | Build; CI platform config |
| Tampering | SAST gates; SCA gates; Git commit signing; artifact signing | Commit/PR; Build |
| Repudiation | Pipeline audit logs; Kubernetes audit log; CloudTrail with Object Lock | Pipeline; Runtime |
| Information Disclosure | Secrets scanning; container scanning; TLS enforcement; secret vault | Pre-commit; Build; Deploy |
| Denial of Service | OPA resource limits policy; LimitRange; ResourceQuota | Admission; Namespace config |
| Elevation of Privilege | Security Contexts; Pod Security Standards; RBAC; OPA/Gatekeeper | Manifest; Admission |

---

## Section 4: Twenty Practice Questions

---

### Question 1

A CI/CD pipeline runs SAST and SCA on every pull request. A critical SQL injection vulnerability is discovered in production two weeks after a PR was merged. The SAST scan passed on that PR. What is the most likely explanation?

- A) The SAST tool does not scan SQL queries — SQL injection is a runtime behavior that only DAST can detect
- B) The vulnerability was introduced by a developer who committed directly to main, bypassing the PR branch protection rule that triggers SAST
- C) SCA should have caught the SQL injection — SAST is not designed for injection vulnerabilities
- D) The NVD database did not contain an entry for this SQL injection pattern, so the SAST tool had no signature to match against

Correct Answer: B — SAST scans source code and can detect SQL injection patterns (string concatenation in queries, unsanitized user input passed to query methods). If the scan passed, the most likely explanation is that the vulnerable code was not scanned — either committed directly to main bypassing the PR trigger, or introduced in a branch that merged after the last scan. NVD is used by SCA for library CVEs, not by SAST for custom code patterns. DAST detects runtime SQL injection but is not the primary shift-left control.

---

### Question 2

An OPA/Gatekeeper ConstraintTemplate is deployed to a Kubernetes cluster that blocks containers that do not set `runAsNonRoot: true`. A developer deploys a pod without the Security Context field. What is the expected behavior?

- A) The pod is scheduled and starts normally; OPA generates a warning log entry
- B) The pod is rejected by the Kubernetes API server before it is scheduled; the developer receives an error describing the violated policy
- C) Falco generates an alert when the pod attempts to execute as root at runtime
- D) The kubelet on the target node blocks the container from starting after the API server schedules it

Correct Answer: B — OPA/Gatekeeper operates as a Validating Admission Webhook — it intercepts API server requests before they are persisted to etcd. A non-compliant pod is rejected at the API server level with a descriptive error message. The pod is never scheduled. This is the distinction between admission control (OPA — prevents creation) and runtime monitoring (Falco — detects behavior of running containers).

---

### Question 3

A security team wants to prevent developers from storing AWS access keys in GitHub repositories. Which control most directly addresses this at the earliest possible pipeline stage?

- A) Configure CloudTrail to alert when access keys are used from IP addresses outside the corporate VPN
- B) Deploy a pre-commit hook using git-secrets or detect-secrets on all developer workstations that scans staged changes for credential patterns before each commit
- C) Enable GitHub Advanced Security secret scanning on the repository to alert the security team when a secret is detected in a merged commit
- D) Rotate all AWS access keys monthly as a preventive control so that any committed key expires before it can be exploited

Correct Answer: B — The shift-left principle requires catching secrets at the earliest possible stage. A pre-commit hook runs before the commit is created — before the secret touches version control at all. GitHub Advanced Security scans after the push (after version control), which is later. CloudTrail detects exploitation after the key is used, which is the latest possible detection point. Rotation reduces the exploit window but does not prevent the secret from being committed.

---

### Question 4

A Kubernetes cluster uses a default-deny-all NetworkPolicy for all namespaces. A new microservice needs to receive traffic from the API gateway pod and send requests to a PostgreSQL database pod, both in different namespaces. Which configuration is correct?

- A) Delete the default-deny NetworkPolicy for the namespaces involved, then test that the service works before re-applying a more permissive policy
- B) Add an egress rule in the API gateway namespace allowing traffic to the microservice, an ingress rule in the microservice namespace allowing traffic from the API gateway, an egress rule in the microservice namespace allowing traffic to the database, and an ingress rule in the database namespace allowing traffic from the microservice
- C) Add a single ClusterNetworkPolicy that allows all traffic between the three namespaces to simplify the configuration
- D) Annotate the pods with `networking.kubernetes.io/allow-all: "true"` to override the default-deny policy for these specific pods

Correct Answer: B — Kubernetes NetworkPolicies require explicit allow rules in both directions for each traffic flow. The default-deny-all policy must remain in place; traffic is opened with minimal-scope rules. Each traffic flow requires: an egress allow on the source side and an ingress allow on the destination side. Answer A violates the principle of least privilege by removing the default-deny. Answer C allows all traffic between all pods in three namespaces — far broader than required. Answer D is not a valid Kubernetes annotation.

---

### Question 5

A Trivy image scan passes for a container image that contains the `libssl1.0.0` package. Six months later, a critical CVE is published for `libssl1.0.0`. The image is still running in production without being rebuilt. What combination of controls would detect this situation?

- A) SAST scanning on the next code push — because SAST detects library vulnerabilities in production images
- B) Scheduled Trivy scans of the container registry on a daily or weekly basis, with alerts when a previously clean image matches a newly published CVE, combined with an alert that triggers a rebuild pipeline
- C) Falco runtime monitoring would detect the CVE and alert the security team when the vulnerable library is loaded
- D) SCA scanning on the next PR — because SCA scans all installed packages in the running container image

Correct Answer: B — Container image scanning tools like Trivy can be run against images in a registry on a schedule, not just at build time. When a new CVE is published for a library that is present in a previously clean image, a scheduled scan will detect the match and can trigger an alert or automated rebuild. SAST does not scan images or libraries. Falco detects syscall-level behavior — not the presence of CVEs in installed packages. SCA scans dependency manifests, not built image layers.

---

### Question 6

An organization's DSOE exam preparation checklist includes: "Understand the difference between HashiCorp Vault's KV secrets engine and the database secrets engine." What is the most important operational difference?

- A) KV stores secrets as key-value pairs with configurable TTLs; the database secrets engine stores SQL schema definitions for Vault to query
- B) KV secrets are static values stored in Vault that must be manually rotated; the database secrets engine generates dynamic, short-lived database credentials on-demand that expire automatically after a configured TTL
- C) KV requires an HSM for encryption; the database secrets engine uses Vault's built-in AES-256 transit engine
- D) KV is only available in Vault Enterprise; the database secrets engine is available in the open-source version

Correct Answer: B — The key operational distinction is static vs. dynamic. KV (key-value) stores secrets that a human or automation writes to Vault — they persist until manually updated. The database secrets engine integrates with database backends (PostgreSQL, MySQL, etc.) and generates a unique set of credentials for each requesting application, with a TTL after which the credentials are automatically revoked. Dynamic credentials eliminate the risk of long-lived database credentials being stolen and reused — a critical security improvement over static credentials.

---

### Question 7

A pipeline runs the following stages in order: SAST, SCA, docker build, Trivy scan, deploy to staging, OWASP ZAP DAST, manual approval, deploy to production. At which stage would a stored cross-site scripting (XSS) vulnerability in a React component most likely first be detected?

- A) SAST — because SAST analyzes source code for XSS patterns in JavaScript files
- B) SCA — because stored XSS is typically introduced through vulnerable npm dependencies
- C) Trivy — because Trivy scans the container image for XSS vulnerability signatures
- D) OWASP ZAP DAST — because stored XSS requires the application to be running; ZAP sends test payloads and observes rendered responses to detect stored XSS

Correct Answer: A — SAST can detect XSS patterns in source code: improper sanitization of user input before rendering, use of `dangerouslySetInnerHTML` with unsanitized data, or direct DOM manipulation with untrusted input. SAST tools like Semgrep have rules for React-specific XSS patterns. While DAST can also detect XSS, SAST is earlier in the pipeline (commit/PR stage) and would detect the pattern before deployment. The question asks which stage would "first" detect — SAST is earlier.

Note for exam: If the SAST tool has no rules for the specific XSS pattern, DAST would be the first stage to catch it. The question implies a competently configured SAST ruleset.

---

### Question 8

An organization's Change Failure Rate has increased from 8% to 19% over the past two quarters. The DevSecOps team correlates the increase to three security incidents caused by CVEs in production that were present in the Trivy backlog. The Trivy gate is set to block on CRITICAL findings, but engineers are overriding the gate with a single-click approval. What is the root cause, and what two controls most directly address it?

- A) Root cause: the Trivy scan is producing false positives. Controls: tune the Trivy ruleset and increase the CRITICAL threshold to BLOCKER severity
- B) Root cause: Security Theater — the override mechanism eliminates the gate's security value. Controls: require documented justification and manager approval for overrides; report override frequency to engineering leadership as a KPI
- C) Root cause: the Trivy scan runs too infrequently. Controls: increase Trivy scan frequency to hourly and deploy Trivy as a pre-commit hook
- D) Root cause: the CRITICAL CVEs should have been caught by SCA, not Trivy. Controls: add an SCA gate and remove the Trivy gate to eliminate redundancy

Correct Answer: B — The root cause is Security Theater: a gate that nominally blocks but is bypassed without accountability. Engineers overriding without documented justification means three CVEs reached production despite the gate existing. The two most direct controls are: governance for the override process (documented justification + approval) and leadership visibility (override frequency as a KPI, visible in leadership reviews). These make overrides deliberate decisions rather than reflexive habit.

---

### Question 9

A Falco rule fires the alert: `A shell was spawned in a container with an attached terminal (user=root command=bash terminal=34816)`. What does this alert indicate, and what should the incident response first action be?

- A) This is a normal operational event — developers routinely attach to containers for debugging; no action is required
- B) This indicates that an interactive shell was spawned inside a running container, which is anomalous in a production environment where containers should run a single process without an attached terminal; the first response is to capture the container forensic state (logs, process list, network connections) before killing the pod
- C) This indicates a Kubernetes RBAC misconfiguration — the alert fires when a service account with excessive permissions creates a pod; revoke the service account ClusterRoleBinding
- D) This indicates that the container image contains a shell binary, which violates the distroless image policy; rebuild the image using a distroless base

Correct Answer: B — The Falco rule `Terminal shell in container` fires when a shell process is spawned with an attached terminal inside a running container. In production, legitimate containers run a single process (the application binary) with no interactive shell. A shell with an attached terminal strongly suggests either an attacker who has compromised the container and opened an interactive session, or unauthorized interactive debugging by a developer. The first response principle is to preserve forensic evidence before remediation — capture logs, process lists, and network connections, then terminate the compromised pod.

---

### Question 10

A developer asks: "Why do we need both OPA/Gatekeeper and Kubernetes Pod Security Standards? Aren't they redundant?" What is the most accurate explanation of why both are used?

- A) They are fully redundant; organizations should choose one to avoid policy conflicts
- B) Pod Security Standards enforce a defined set of pod security profiles (Privileged, Baseline, Restricted) with fixed criteria; OPA/Gatekeeper provides a programmable policy engine for custom requirements beyond what the three standard profiles cover — such as requiring image signing verification, enforcing naming conventions, or mandating resource limits. Both are needed because PSS covers the standard security baseline and OPA covers organization-specific requirements
- C) Pod Security Standards operate at the cluster level only; OPA/Gatekeeper operates at the namespace level, so both are needed for multi-namespace clusters
- D) OPA/Gatekeeper replaces Pod Security Standards in Kubernetes 1.25 and later; organizations using 1.25+ should use only OPA

Correct Answer: B — Pod Security Standards provide three predefined security profiles with a fixed set of criteria (runAsNonRoot, allowPrivilegeEscalation, capabilities, etc.). They cover the well-known privilege escalation controls. OPA/Gatekeeper provides a programmable policy layer for requirements that PSS does not cover: image signing verification (is this image signed by the approved key?), image registry allowlisting (is this image from an approved registry?), resource limits enforcement (does this pod have CPU and memory limits?), and custom label requirements. Both layers are complementary, not redundant.

---

### Question 11

A compliance audit finds that the organization cannot demonstrate that every production deployment in the past year was preceded by a passing container image scan. The pipeline does run Trivy on every build, but results are not persisted. What architectural change most directly resolves this audit finding?

- A) Instruct developers to take screenshots of Trivy scan results and submit them to the compliance team after each deployment
- B) Configure the pipeline to publish Trivy scan results as structured JSON to a tamper-evident, time-stamped log store (S3 with Object Lock, or an immutable SIEM index), linked to the pipeline run ID and deployed image digest, so that each deployment has a machine-verifiable, immutable scan record
- C) Add a manual sign-off step where a security engineer reviews the Trivy output and signs off on the deployment in a spreadsheet
- D) Run Trivy in the production environment post-deployment so that the live image is scanned rather than the pre-deployment build

Correct Answer: B — Compliance audit evidence must be system-generated, tamper-evident, and cover every deployment — not just a sample or manual attestation. Publishing structured Trivy results to an immutable log store with deployment metadata (pipeline run ID, image digest, timestamp) creates machine-verifiable per-deployment evidence that satisfies continuous compliance requirements. Screenshots and spreadsheets are easily fabricated and do not scale. Post-deployment scanning is shift-right and does not demonstrate pre-deployment control.

---

### Question 12

A SAMM assessment identifies that the organization's Education and Guidance practice is at Level 2 (security training exists for champions, no program for all developers). What initiative advances it to Level 3?

- A) Purchase a security scanning tool and deploy it to all CI pipelines to automatically enforce secure coding standards
- B) Implement a mandatory just-in-time security training program where every developer receives contextual secure coding guidance in their development environment, linked to real findings from the team's SAST and SCA tools, with completion tracking and quarterly training effectiveness metrics reviewed in leadership meetings
- C) Require all engineers to complete a 2-hour annual compliance video before accessing production systems
- D) Hire three additional Application Security engineers to provide one-on-one security consultations to development teams on demand

Correct Answer: B — SAMM Level 3 for Education and Guidance requires security training that is comprehensive, contextual, and measured. Level 3 criteria include: training is available to all developers (not just champions), training is contextual (tied to actual findings rather than generic compliance content), and effectiveness is measured and reviewed by leadership. Just-in-time training integrated with SAST/SCA findings is the canonical Level 3 implementation. Annual compliance videos address awareness but are not contextual or measured. Tool deployment and additional security headcount address different SAMM practices.

---

### Question 13

A threat model for a new microservice identifies a Spoofing threat: another service in the cluster could impersonate the microservice's identity and receive requests intended for it. Which two controls most directly mitigate this threat?

- A) Enable `readOnlyRootFilesystem: true` in the pod's Security Context and configure Falco to alert on unexpected network connections
- B) Deploy mutual TLS (mTLS) between all microservices using a service mesh (Istio or Linkerd) so that each service cryptographically proves its identity, and configure Kubernetes Network Policies to restrict ingress to the microservice to only the specific source pod that should communicate with it
- C) Enable SAST scanning on the microservice's source code to detect authentication implementation bugs
- D) Configure the OPA/Gatekeeper policy to block privileged containers in the namespace

Correct Answer: B — Spoofing threats require authentication controls that verify identity. mTLS provides cryptographic service identity — each service presents a certificate and verifies the peer's certificate, making identity impersonation infeasible without the private key. Network Policies restrict which pods can initiate connections to the microservice at the network layer, reducing the attack surface for spoofing attempts. ReadOnlyRootFilesystem prevents filesystem writes but does not address identity spoofing. SAST finds code vulnerabilities but cannot implement network-layer identity verification. OPA privilege controls address Elevation of Privilege, not Spoofing.

---

### Question 14

An organization's Security Gate Pass Rate is 94%. The security team is satisfied with this value. A DSOE exam question asks: what is the most important secondary metric to track alongside Gate Pass Rate to ensure the 94% figure is meaningful?

- A) Deployment Frequency — to ensure the pass rate is not inflated by low deployment volume
- B) The override approval rate for the 6% of failed builds — to verify that every failed build that proceeded to deployment had a documented justification and an appropriate approver, and that no critical findings escaped to production via unapproved overrides
- C) The number of SAST rules configured in Semgrep — to ensure the high pass rate is not caused by having too few rules
- D) The percentage of developers who completed security training — because training completion drives pass rate improvement

Correct Answer: B — A 94% pass rate means 6% of builds failed a security gate. What happened to those 6%? If they were overridden without governance, the 94% metric is meaningless — critical findings may have reached production through the 6% failure path. The override approval rate and override documentation completeness are the critical secondary metrics that validate whether the 94% pass rate reflects genuine security effectiveness or whether the 6% represents an escape valve for security theater.

---

### Question 15

A Kubernetes deployment manifest includes: `securityContext.privileged: true` and `securityContext.hostPID: true`. An OPA/Gatekeeper policy blocks the deployment. Which STRIDE categories do these two Security Context settings enable as threats, and why does OPA correctly block them?

- A) Denial of Service and Information Disclosure — `privileged` containers can consume host resources; `hostPID` can read process environment variables
- B) Elevation of Privilege for both — `privileged: true` gives the container full root capabilities equivalent to the host root, enabling container escape via kernel vulnerabilities; `hostPID: true` allows the container to see and signal all host processes, enabling privilege escalation to other containers or the host
- C) Spoofing and Tampering — privileged containers can modify the host network namespace to intercept other pods' traffic
- D) Repudiation — these settings disable kernel audit logging for the container's syscalls

Correct Answer: B — Both settings are Elevation of Privilege threats. `privileged: true` grants the container all Linux capabilities and removes namespace isolation — a container with this setting can exploit kernel vulnerabilities to escape the container namespace and gain host root access. `hostPID: true` shares the host's PID namespace, allowing the container to see all processes on the host, send signals to them, and potentially read sensitive information from process memory or environment variables. OPA correctly blocks both because they violate the Pod Security Standards `restricted` profile and represent the most severe class of Kubernetes privilege escalation threats.

---

### Question 16

A developer configures a GitHub Actions workflow with `permissions: write-all` for the entire workflow file. A DSOE security review flags this. What is the security risk, and what is the correct remediation?

- A) `write-all` causes the workflow to run twice — once for read and once for write; split the workflow into two files
- B) `write-all` grants the GitHub Actions GITHUB_TOKEN maximum permissions across all workflow scopes (contents, packages, deployments, security-events, etc.); if the workflow is compromised via a malicious dependency or a pull-request-triggered workflow, the token can be used to push malicious code, delete branches, or modify releases. Remediation: set `permissions: {}` at the workflow level and grant only the specific permissions each job requires (e.g., `contents: read` for checkout, `packages: write` for registry push)
- C) `write-all` is not a valid permission value; the workflow will fail to parse and the pipeline will not run
- D) `write-all` only affects permissions within the repository; it cannot be used to access external services or cloud providers

Correct Answer: B — GitHub Actions GITHUB_TOKEN permissions default to the repository's permission setting (often broad in older configurations). `permissions: write-all` grants the token maximum scope across all resource types. In a compromised workflow (via a malicious third-party Action, a poisoned dependency, or a pull-request trigger that runs untrusted code), an overly permissive token enables supply chain attacks: push to the main branch, modify release artifacts, or write to the container registry. Least-privilege token permissions are a DSOE pipeline security requirement. `permissions: {}` at the workflow level combined with per-job grant is the correct pattern.

---

### Question 17

An organization runs SAST (Semgrep), SCA (OWASP Dependency-Check), container scanning (Trivy), and secrets scanning (detect-secrets). A security architect proposes adding Conftest with OPA Rego policies to the pipeline. What gap does Conftest address that the existing four tools do not cover?

- A) Conftest provides a fifth layer of secret detection that is more accurate than detect-secrets
- B) Conftest validates Kubernetes manifests, Terraform, Helm charts, and other structured configuration files against custom OPA Rego policies before they are applied — catching security misconfigurations in infrastructure-as-code (open security groups, missing encryption, overly permissive RBAC) that SAST, SCA, Trivy, and secrets scanning cannot assess
- C) Conftest replaces Trivy by scanning container images against OPA policies rather than the NVD CVE database
- D) Conftest performs DAST-style API testing using OPA Rego test cases against a deployed application

Correct Answer: B — SAST analyzes application code logic. SCA analyzes dependency manifests for known CVEs. Trivy scans image layers for installed package CVEs. Detect-secrets finds credential patterns in code. None of these tools evaluate whether infrastructure configuration files conform to security policy. Conftest fills this gap: it evaluates Kubernetes YAML, Terraform HCL, Helm charts, and other structured files against Rego policies that encode your security requirements (no root containers, no privileged pods, no public storage buckets, encryption at rest required). This is the IaC security scanning layer.

---

### Question 18

A DSOMM assessment rates an organization's pipeline at Level 3 for all technical dimensions. The CISO asks how to demonstrate that the program reduces business risk, not just that tools are deployed. Which measurement framework most directly answers this question?

- A) Report the number of security tools deployed and the number of pipeline gates configured per repository
- B) Report DORA Change Failure Rate (showing reduction in security-caused production failures), Critical Finding Escape Rate (trending toward zero), and MTTR-Security (showing faster remediation cycles), correlated with the number of security incidents over the past four quarters — demonstrating that pipeline maturity improvements are producing measurable reductions in production risk
- C) Conduct an annual penetration test and report the number of findings compared to the previous year
- D) Report compliance certification status (SOC 2 Type II, ISO 27001) as evidence that business risk is being managed

Correct Answer: B — Tool count and gate configuration measure program inputs, not outcomes. Compliance certifications measure control existence, not risk reduction. Penetration tests are annual snapshots. The CISO's question is about business risk reduction — which requires outcome metrics that connect pipeline controls to production security outcomes. Change Failure Rate (reduction in security-caused failures), Escape Rate (fewer vulnerabilities reaching production), and MTTR-Security (faster response when they do), correlated with incident frequency trend, directly answer whether the program is reducing the business impact of security risk.

---

### Question 19

A developer reviews a Kubernetes manifest and notices a Security Context with `capabilities.add: [NET_RAW]`. A DSOE security review flags this. What threat does this capability introduce?

- A) NET_RAW allows the container to write to the host filesystem, enabling an attacker to modify the host OS
- B) NET_RAW allows the container to craft arbitrary network packets, enabling packet sniffing of other pods' unencrypted traffic, ARP poisoning for man-in-the-middle attacks, and ICMP-based reconnaissance within the cluster network
- C) NET_RAW increases container network throughput by bypassing the kernel network stack, which could cause denial-of-service conditions on shared nodes
- D) NET_RAW enables the container to call privileged system calls reserved for the host kernel, enabling container escape

Correct Answer: B — The `NET_RAW` Linux capability grants a process the ability to use raw sockets and craft arbitrary network packets. In a Kubernetes context, a container with NET_RAW can: perform packet sniffing on the pod network using tools like tcpdump; craft ARP packets for man-in-the-middle attacks within the pod network; perform ICMP-based network reconnaissance. The Pod Security Standards `restricted` profile drops this capability (along with all others via `capabilities.drop: [ALL]`). The security review correctly flags NET_RAW as a network-layer Information Disclosure and Spoofing threat enabler.

---

### Question 20

A DevSecOps team completes Modules 1–15 of CIS-4350. They need to configure a complete GitHub Actions pipeline for a Python Flask application deployed to Kubernetes. Which sequence of pipeline stages correctly implements defense in depth from commit to runtime?

- A) Deploy to production → Trivy scan → OWASP ZAP DAST → SAST → SCA → approve
- B) Pre-commit secrets scan → SAST (Semgrep/Bandit) on PR → SCA (Dependency-Check) on PR → docker build → Trivy image scan → Checkov IaC scan → push to registry with Cosign signing → deploy to staging → OWASP ZAP DAST → manual approval → deploy to production with OPA/Gatekeeper admission → Falco runtime monitoring
- C) SAST → deploy to production → Trivy scan → Falco alert → rollback if Falco alerts fire
- D) SCA → SAST → DAST → deploy to production → enable Vault → configure Network Policies post-deployment

Correct Answer: B — This sequence implements the complete shift-left DevSecOps pipeline: secrets scanning at pre-commit (earliest possible detection), SAST and SCA at PR time (code security before merge), container scanning after build (artifact security before push), IaC scanning (infrastructure security), artifact signing (supply chain integrity), DAST at staging (runtime behavior testing), human approval gate (change control), OPA/Gatekeeper at production admission (policy enforcement), and Falco at runtime (continuous monitoring). Every other option violates shift-left ordering by running security controls after production deployment or skipping critical stages.

---

## Section 5: Exam-Day Checklist

Use this checklist in the 48 hours before your DSOE exam:

- [ ] Review the Domain Map table and verify you can describe each tool's purpose, stage, and scope
- [ ] Review the High-Priority Exam Distinctions — SAST vs. SCA vs. container scanning; OPA vs. Falco; PSS vs. Network Policies
- [ ] Review the Pipeline Control to Threat Mapping table — know which control addresses which STRIDE category
- [ ] Complete the twenty practice questions without looking at answers; then review all distractors
- [ ] Re-watch the pipeline capstone segment of the Module 16 video and trace the full pipeline sequence from memory
- [ ] Review the three transformation failure modes and be able to identify each from a scenario description
- [ ] Review the DORA performance bands — know Elite vs. High performer values for all four metrics
- [ ] Confirm you can describe DSOMM Levels 1–4 and identify the level from a described program state
- [ ] Confirm you can map a compliance requirement (SOC 2 CC8.1, PCI-DSS Req 6.3) to a specific pipeline control

---

## 9. Supplemental Resources

**1. [DevSecOps Professional (DSOE) certification — Security Knowledge Framework](https://www.practical-devsecops.com/devsecops-professional-certification/)**
The official Practical DevSecOps DSOE certification page covering exam domains, topic areas, and preparation guidance. Cross-references the tool and framework domains tested in the exam with the module content from this course.

**2. [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/)**
The OWASP DevSecOps Guideline covers the full DevSecOps lifecycle from pre-commit through production monitoring. Includes tool recommendations, integration patterns, and maturity model guidance that aligns with exam scenarios requiring end-to-end pipeline design decisions across all security domains.

**3. [CNCF Cloud Native Security Whitepaper](https://github.com/cncf/tag-security/blob/main/security-whitepaper/v2/CNCF_cloud-native-security-whitepaper-May2022-v2.pdf)**
The CNCF Security Technical Advisory Group's comprehensive whitepaper on cloud native security, covering supply chain security, runtime security, Kubernetes hardening, and compliance-as-code. Maps security controls across the software lifecycle and provides the architectural context for understanding how individual DevSecOps tools fit into a defense-in-depth strategy.

---

Reading Guide — Module 16 | CIS-4350 | Texas Wesleyan University | Professor Nash
