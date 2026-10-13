# Video Script: Module 16 — DevSecOps Professional Exam Preparation

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 28–32 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–2:00)

Welcome to Module 16 — the final module of CIS-4350. I am Professor Nash. This module is your exam preparation session for the DevSecOps Professional — DSOE — certification. We are going to do three things: consolidate all domains covered across fifteen modules into a single review framework, work through exam strategy for scenario-based questions, and close with a pipeline capstone that connects every major tool and concept we have covered into one end-to-end system.

By the end of this module you should be able to describe every major domain of the DSOE exam, apply a systematic approach to scenario-based questions, identify which tool or control addresses a given threat, and configure a complete DevSecOps pipeline from a design document.

Let us get started.

---

### SEGMENT 2 — Domain 1 Review: Culture and Organizational Transformation (2:00–6:00)

The first exam domain covers the cultural and organizational foundations of DevSecOps — everything from Module 15.

**Security Champion programs.** Champions are embedded engineers who bridge the security team and development teams. One per eight to ten engineers is the recommended ratio. Champions triage findings, attend sprint planning to flag security requirements, are required reviewers on security-sensitive pull requests, and represent their team in the champion community sync. The DSOE exam tests champion program design: selection criteria, training approach, and how champions interact with the central security team.

**Developer training.** OWASP Top 10 is the baseline — every engineer should understand injection, broken access control, and cryptographic failures. SANS DEV541 is the exam-referenced course for DevSecOps practitioners. Just-in-time training — security education embedded in tool findings — has the highest retention because it is contextual and immediate.

**DORA metrics.** Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR. These four metrics measure delivery throughput and stability. The DSOE exam connects DORA to security: Change Failure Rate includes security incidents; Lead Time measures how fast security patches reach production; MTTR measures how quickly security incidents are resolved. Elite performers achieve all four metrics simultaneously — high throughput and high stability are not in tension.

**Security KPIs.** MTTD (time from introduction to detection), MTTR-Security (detection to fix in production), Critical Escape Rate (critical findings reaching production), Security Gate Pass Rate (pipeline runs passing without override). Know which KPI each pipeline control most directly improves.

**Maturity models.** OWASP SAMM — five business functions (Governance, Design, Implementation, Verification, Operations), three practices each, three levels each. DSOMM — four levels (Basic Understanding, Basic Adoption, High Adoption, Continuous Improvement) across Build, Deploy, Test, Monitor, Culture dimensions. DSOMM Level 2 is the minimum viable DevSecOps program; Level 3 requires a full gate suite and formal champion program.

**Transformation failure modes.** Security as Bottleneck — centralized ownership that does not scale; fix by distributing to champions. Tool Accumulation Without Process — tools with no defined ownership or SLAs; fix by defining process before adding tools. Security Theater — gates bypassed without governance; fix by adding override approval requirements and tracking.

---

### SEGMENT 3 — Domain 2 Review: CI/CD Pipeline Security (6:00–11:00)

The second domain covers the technical pipeline security controls from Modules 2 through 10.

**SAST — Static Application Security Testing.** Analyzes source code without execution. Tools: Semgrep, Bandit (Python), SpotBugs (Java), ESLint security plugins. Stage: on every commit to a feature branch or on pull request. Gate action: fail build on CRITICAL or HIGH findings above threshold. SAST catches injection, SQL injection, XSS, hardcoded credentials, and insecure API usage. Does not catch runtime issues or dependency vulnerabilities.

**SCA — Software Composition Analysis.** Scans dependency manifests (package.json, requirements.txt, pom.xml) against CVE databases (NVD, OSV). Tools: OWASP Dependency-Check, Snyk, Grype. Stage: at build time after dependencies are installed. Gate action: fail build on CRITICAL CVEs. SCA catches known vulnerable third-party dependencies. Does not catch custom code vulnerabilities.

**Container image scanning.** Scans built container images for OS-level and application-level CVEs in installed packages. Tools: Trivy, Grype. Stage: after docker build, before push to registry. Gate action: fail build on CRITICAL findings above threshold. Container scanning catches vulnerabilities in base images and installed system packages that SCA — which scans manifests — cannot see. Key exam point: SCA catches application dependency CVEs; container scanning catches OS and system library CVEs.

**Secrets scanning.** Detects secrets committed to source code. Tools: git-secrets, TruffleHog, detect-secrets. Stage: at pre-commit hook and as a pipeline gate. Gate action: fail immediately on any secret detection. Prevents credentials, API keys, and certificates from entering version control. Key exam point: pre-commit is the first gate; pipeline secret scanning is the catch-all for secrets that bypass pre-commit.

**DAST — Dynamic Application Security Testing.** Tests the running application by sending attack payloads to HTTP endpoints. Tools: OWASP ZAP, Nikto. Stage: in the staging environment after deployment, before promotion to production. DAST catches runtime vulnerabilities — XSS, CSRF, open redirects, authentication bypasses — that SAST cannot detect because they require execution.

**IaC scanning.** Scans Terraform, CloudFormation, Kubernetes manifests, and Helm charts for misconfigurations before apply. Tools: Checkov, tfsec, kube-score. Stage: in CI pipeline when IaC files are modified. Catches open security groups, unencrypted storage, missing logging, and overly permissive IAM policies before they are provisioned.

**Artifact signing.** Container images signed with Cosign and a key stored in a KMS. Signature verified at deployment time by an OPA policy or Kubernetes admission webhook. Ensures the deployed image is the exact artifact that was built and scanned by the pipeline. Prevents supply chain attacks where a malicious image is substituted for the legitimate one.

**Secrets management.** HashiCorp Vault provides dynamic secrets (short-lived credentials generated on demand), static secrets with ACL policies, and Kubernetes authentication via the Vault Agent Injector or CSI Provider. Never store secrets in environment variables, ConfigMaps, or source code. Secrets in CI/CD pipelines are stored as encrypted GitHub Secrets or equivalent and injected into the build environment at runtime, never persisted.

---

### SEGMENT 4 — Domain 3 Review: Container and Kubernetes Security (11:00–15:30)

The third domain covers container and Kubernetes security from Modules 11 and 12.

**Security Contexts.** Applied at pod or container level in the Kubernetes manifest. Critical fields: `runAsNonRoot: true` prevents containers running as UID 0; `runAsUser: 1000` sets a specific non-root UID; `allowPrivilegeEscalation: false` prevents privilege escalation via setuid binaries; `capabilities.drop: [ALL]` removes all Linux capabilities; `readOnlyRootFilesystem: true` prevents filesystem writes.

**Pod Security Standards.** Three profiles: Privileged (no restrictions — only for system components), Baseline (prevents known privilege escalation), Restricted (requires non-root, no privilege escalation, dropped capabilities — the production standard). Enforced via Pod Security Admission at the namespace level with three modes: Audit (log violations), Warn (warn on apply), Enforce (reject non-compliant pods). Use `enforce: restricted` for production namespaces.

**Network Policies.** Kubernetes NetworkPolicy resources control pod-to-pod communication at the network layer. Default-deny-all ingress and egress is the security baseline. Explicit allow rules then open only the required communication paths. Without NetworkPolicies, all pods in a cluster can communicate with all other pods — a flat network that allows lateral movement after a container compromise.

**RBAC.** Kubernetes Role-Based Access Control uses Roles (namespace-scoped), ClusterRoles (cluster-scoped), RoleBindings, and ClusterRoleBindings. Service accounts are the identity for pods. Least-privilege service accounts — each pod gets a dedicated service account with only the permissions it needs. Avoid cluster-admin bindings for application workloads. Exam pattern: when a pod needs to read ConfigMaps in its own namespace only, bind a Role with `get`, `list` on ConfigMaps — not a ClusterRole.

**Falco.** Runtime security monitoring tool that uses eBPF to observe system calls and generates alerts when container behavior matches a threat rule. Default rules detect: terminal spawning in a container, privilege escalation attempts, sensitive file access (/etc/shadow, /etc/passwd), container escape syscalls. Alerts sent to Slack, Falcosidekick, or SIEM via webhook. Key exam point: Falco detects threats at runtime that admission control cannot prevent (runtime exploitation of legitimate container processes).

**OPA/Gatekeeper.** Open Policy Agent with Gatekeeper implements policy as code in Kubernetes as a Validating Admission Webhook. ConstraintTemplates define policy logic in Rego; Constraints instantiate policies with parameters. Common policies: block privileged containers; require resource limits; enforce image signing; block latest tag; require specific label sets. Key exam point: OPA blocks non-compliant resources at admission time — before the pod is scheduled. It does not monitor running containers; Falco does.

---

### SEGMENT 5 — Domain 4 Review: Compliance as Code and Monitoring (15:30–19:30)

The fourth domain covers compliance, monitoring, and SIEM from Modules 12 and 13.

**Compliance as Code.** Compliance requirements expressed as executable, version-controlled code enforced automatically. Tools: OPA Rego (Kubernetes policies), Conftest (pipeline policy tests), Checkov (IaC), Chef InSpec (runtime). Key principle: every deployment is validated against compliance policy automatically, generating machine-verifiable evidence of compliance at deployment time rather than during periodic audits.

**Audit trails.** A compliant deployment audit trail includes: signed commit (developer identity), PR approval record (code review evidence), SAST/SCA/container scan pass results (security scanning evidence), image digest (exact artifact identity), pipeline run ID (automated process evidence), deployment timestamp and target environment (deployment record). Stored in tamper-evident centralized logging (CloudTrail S3 with Object Lock, or equivalent).

**SOC 2 mapping.** SOC 2 Trust Services Criteria: CC6.1 (logical access) → RBAC, least privilege, Vault; CC7.2 (monitoring) → SIEM, Falco alerts; CC8.1 (change management) → pipeline gates, PR approvals, deployment audit logs; CC9.2 (risk mitigation) → SAST, SCA, container scanning gates.

**PCI-DSS mapping.** PCI-DSS v4.0: Requirement 6.3 (security vulnerabilities addressed) → SAST, SCA, container scanning gates with SLAs; Requirement 6.4 (public-facing web applications protected) → DAST, WAF; Requirement 10.2 (audit log events) → pipeline audit logs, Kubernetes audit logs.

**SIEM integration.** Security Information and Event Management aggregates logs from multiple sources (Kubernetes audit logs, Falco alerts, application logs, CloudTrail) into a centralized platform (Elastic SIEM, Splunk, AWS Security Hub). Detection rules correlate events across sources to identify attack patterns. Example correlation: Falco alert (unexpected process in container) + Kubernetes audit log (service account token request) + CloudTrail (new IAM role assumption) = container escape to cloud credential theft detection rule.

**Kubernetes audit logging.** The Kubernetes API server logs every request to the API. Audit policy controls which requests are logged at which verbosity. Minimum audit policy for security: log all requests in the `RequestResponse` stage for sensitive verbs (create, update, delete, patch) on sensitive resources (Secrets, RoleBindings, ClusterRoleBindings, Pods). Audit logs ship to Falco or SIEM for real-time analysis.

---

### SEGMENT 6 — Exam Strategy (19:30–23:00)

The DSOE exam consists of scenario-based multiple choice questions. Understanding exam question structure is as important as knowing the content.

**The question anatomy.** Every DSOE scenario question has: a situation description (environment, current state, what went wrong or what is needed), a task statement (what you are asked to do, configure, or identify), and four answer choices (one correct, three plausible distractors). The distractors are designed to catch common misconceptions — correct tools at the wrong pipeline stage, correct concepts applied to the wrong threat, and technically true but incomplete answers.

**The four distractor patterns.** Learn to recognize them:

- **Right tool, wrong stage.** DAST placed at commit time instead of staging; Falco described as preventing container creation instead of detecting runtime behavior. Know precisely which stage each tool operates at.
- **Symptom vs. root cause.** The scenario describes a finding escaping to production — the distractor says "fix the finding faster"; the correct answer says "enforce the gate that should have caught it."
- **Administrative vs. technical control.** A scenario asks for a technical control that prevents hardcoded secrets in code. The distractor offers "security policy requiring no hardcoded secrets"; the correct answer is "pre-commit secrets scanning gate with git-secrets."
- **Correct in isolation, wrong in context.** `imagePullPolicy: IfNotPresent` is operationally valid for performance but does not pull updated signed images; `imagePullPolicy: Always` is required for image signing verification.

**The two-step elimination method:**

1. Identify the primary constraint in the scenario (pipeline stage, threat type, tool category, organizational context).
2. Eliminate answers that violate the primary constraint. Choose between remaining answers based on secondary constraints (least privilege principle, shift-left placement, policy as code over manual control).

**Common cross-domain questions.** The exam frequently tests integration across domains. Examples: "A Trivy scan passes but a runtime security alert fires — what is the most likely explanation?" (Answer: the CVE was not in the NVD database at scan time — zero-day or newly published; Falco detected the exploitation behavior.) "SAST passes, SCA passes, OPA blocks the deployment — what is the most likely cause?" (Answer: a Kubernetes configuration policy violation — not a code or dependency issue, but a manifest misconfiguration like a privileged container or missing resource limits.)

---

### SEGMENT 7 — Pipeline Capstone (23:00–29:00)

Let us build the complete DevSecOps pipeline as a single end-to-end system. This capstone connects every domain.

**The complete pipeline sequence:**

```text
Developer workstation
  └── pre-commit hook
        ├── git-secrets (secrets scan)
        ├── detect-secrets (secrets scan)
        └── SAST lint (optional fast rules)

Pull Request opened to main
  └── CI pipeline triggers
        ├── STAGE 1: Code Security
        │   ├── Semgrep SAST (block on CRITICAL/HIGH)
        │   └── OWASP Dependency-Check SCA (block on CRITICAL)
        │
        ├── STAGE 2: Build and Artifact Security
        │   ├── docker build
        │   ├── Trivy image scan (block on CRITICAL)
        │   ├── cosign sign (KMS-backed key)
        │   └── push to registry
        │
        ├── STAGE 3: Infrastructure Security
        │   ├── Checkov IaC scan (block on HIGH)
        │   └── Conftest policy tests (OPA Rego)
        │
        └── STAGE 4: Deploy to Staging
              ├── kubectl apply (OPA Gatekeeper validates)
              ├── OWASP ZAP DAST scan
              └── promotion gate (human approval for production)

Merge to main → Deploy to Production
  └── OPA Gatekeeper admission control (enforce: restricted)
        ├── image signing verification (cosign)
        ├── Pod Security Standards (restricted profile)
        ├── Network Policy enforcement (default-deny)
        └── RBAC (least-privilege service accounts)

Runtime Monitoring
  ├── Falco (eBPF syscall rules → Falcosidekick → SIEM)
  ├── Kubernetes audit log → SIEM
  ├── Application logs → SIEM
  └── CloudTrail → SIEM

SIEM Correlation Rules
  ├── Container escape detection
  ├── Credential theft detection
  └── Lateral movement detection

Security Program Layer
  ├── Security Champions (one per team)
  ├── DORA + security KPI tracking
  ├── SAMM/DSOMM assessment (annual)
  └── Override governance (approval + tracking)
```

**How the domains connect:**

The Security Champion reviews the threat model at sprint planning. The threat model outputs identify which STRIDE threats require which pipeline gates. SAST, SCA, and secrets scanning address Tampering and Information Disclosure at commit and build time. Container scanning and image signing address Tampering at the artifact layer. OPA/Gatekeeper and Pod Security Standards address Elevation of Privilege and Denial of Service at admission time. Network Policies address Lateral Movement post-exploitation. Falco and SIEM address detection of Spoofing, Repudiation, and Elevation of Privilege at runtime. Compliance as Code (Conftest, OPA) generates the machine-verifiable evidence that satisfies SOC 2 CC8.1 and PCI-DSS Requirement 6.3 at each deployment. DORA and security KPIs measure whether the entire system is effective, and the maturity model tells you where to invest next.

---

### SEGMENT 8 — Final Wrap-Up (29:00–31:00)

You have now covered every domain of the DSOE certification:

- Culture and organizational transformation — Security Champions, DORA, maturity models, transformation failure modes
- CI/CD pipeline security — SAST, SCA, container scanning, secrets management, DAST, IaC scanning, artifact signing
- Container and Kubernetes security — Security Contexts, Pod Security Standards, Network Policies, RBAC, OPA/Gatekeeper, Falco
- Compliance as code and monitoring — Compliance as Code, audit trails, SOC 2 and PCI-DSS mapping, SIEM, Kubernetes audit logging

The pipeline capstone shows how these domains connect into a single end-to-end security architecture where every control traces back to a threat model requirement and every deployment generates machine-verifiable compliance evidence.

For your final exam preparation: complete the twenty practice questions in the reading guide, review any domain where you were uncertain during the quiz questions this week, and work through the capstone lab to configure the full pipeline from scratch.

It has been a great semester. Good luck on the DSOE exam. I will see you there.

---

### PRODUCTION NOTES

- Slide: Complete domain map — all four exam domains with key tools per domain
- Slide: Pipeline capstone diagram (full sequence from pre-commit to runtime monitoring)
- Slide: STRIDE to pipeline control traceability matrix (from Module 14 — revisit here)
- Slide: DORA + security KPI summary table with elite benchmarks
- Slide: Four distractor pattern types with examples
- Screen share: GitHub Actions workflow YAML showing all four pipeline stages
- Screen share: OPA Gatekeeper ConstraintTemplate for image signing verification
