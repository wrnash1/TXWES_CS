# Reading Guide: Module 01 — Introduction to DevSecOps

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Learning Objectives

After completing this reading guide, you will be able to:

- Compare DevOps, DevSecOps, and traditional SDLC models
- Explain the shift-left security principle and its cost implications
- Map security activities to each phase of the DevSecOps lifecycle
- Identify the primary tools in each DevSecOps toolchain category
- Describe the CALMS framework for organizational adoption
- Calculate a basic ROI argument for DevSecOps investment

---

## Section 1 — From Waterfall to DevSecOps: A Historical Overview

### 1.1 The Waterfall Model

The waterfall model organizes software development into sequential phases: Requirements, Design, Implementation, Verification, and Maintenance. Each phase must complete before the next begins. Security review, if it existed at all, occurred during Verification — at the very end.

The core problem with waterfall security: defect cost grows exponentially the later it is found. Fixing a security flaw during Requirements costs roughly 1x. The same fix during Maintenance costs 30–100x.

### 1.2 The Agile Revolution

Agile methodologies, formalized in the 2001 Agile Manifesto, addressed the slow delivery problem through iterative sprints. However, Agile did not inherently address security or operational concerns. Security was still often bolt-on.

### 1.3 DevOps Emergence

DevOps, coined around 2008–2009, united development and operations through cultural change and automation. Key practices include:

- Continuous Integration (CI): developers integrate code frequently, triggering automated builds and tests
- Continuous Delivery (CD): every commit is potentially releasable
- Infrastructure as Code (IaC): infrastructure is managed through version-controlled configuration files
- Monitoring and observability: production systems emit metrics and logs for continuous feedback

### 1.4 DevSecOps: Security as a First-Class Citizen

DevSecOps adds Security to the Dev+Ops equation. The core premise: security is everyone's responsibility, and security controls should be automated and embedded in the pipeline, not added as a manual gate before release.

The term was popularized around 2012 by Gartner and gained widespread adoption with the publication of the DoD Enterprise DevSecOps Reference Design in 2019.

---

## Section 2 — Shift-Left Security in Detail

### 2.1 The Cost Curve

The shift-left argument rests on the defect cost curve. Industry data from IBM, NIST, and the Systems Sciences Institute consistently shows:

| SDLC Phase | Relative Cost to Fix |
|---|---|
| Requirements / Design | 1x |
| Coding | 5x |
| Unit Testing | 10x |
| Integration Testing | 20x |
| System Testing | 50x |
| Production / Post-Release | 100x+ |

Security defects follow the same curve. A SQL injection found by a developer in their IDE during coding takes 20 minutes to fix. The same vulnerability found by a penetration tester after deployment may require a hotfix release cycle, customer notification, and compliance reporting.

### 2.2 Practical Shift-Left Techniques

The following techniques implement shift-left security at each stage:

| Stage | Technique | Example Tool |
|---|---|---|
| Planning | Threat modeling | STRIDE, Microsoft Threat Modeling Tool |
| Coding | IDE security plugins | SonarLint, Snyk IDE extension |
| Code Review | Security-focused PR checklists | GitHub PR templates |
| Pre-commit | Git hooks to block secrets | pre-commit, git-secrets |
| Build | SAST scanning | SonarQube, Semgrep |
| Build | Dependency scanning | OWASP Dependency-Check, Snyk |
| Test | DAST against staging | OWASP ZAP |
| Deploy | IaC scanning | tfsec, checkov |
| Runtime | Container security | Falco, Trivy |

### 2.3 The Security Champion Model

A security champion is a developer or engineer with additional security training who serves as a liaison between their team and the central security function. Security champions:

- Review security findings from automated tools and prioritize remediation
- Conduct lightweight threat modeling for new features
- Mentor colleagues on secure coding practices
- Participate in security community of practice meetings

---

## Section 3 — The DevSecOps Lifecycle

### 3.1 Eight Phases with Security Activities

```text
PLAN → CODE → BUILD → TEST → RELEASE → DEPLOY → OPERATE → MONITOR
```

#### Plan

Activities: Threat modeling, security requirements definition, attack surface analysis.

Key artifact: Threat model document (STRIDE or PASTA methodology).

#### Code

Activities: Secure coding, IDE-based linting, pre-commit hooks, peer code review with security checklist.

Key artifact: Reviewed pull request with security approval.

#### Build

Activities: SAST scan, dependency vulnerability scan, license compliance check, secret detection in codebase.

Key artifact: CI pipeline security report.

#### Test

Activities: DAST scan against deployed staging environment, fuzzing, security regression tests.

Key artifact: DAST report with CVSS scores.

#### Release

Activities: Security gate validation, SBOM generation, compliance policy check, sign-off audit trail.

Key artifact: Signed release with associated SBOM.

#### Deploy

Activities: IaC security scan, container image scan, Kubernetes admission control, secret injection from vault.

Key artifact: Deployment manifest with security annotations.

#### Operate

Activities: Runtime threat detection, anomaly alerting, vulnerability management tracking.

Key artifact: Security incident timeline.

#### Monitor

Activities: Log aggregation to SIEM, compliance dashboard, vulnerability aging reports.

Key artifact: Monthly security posture report.

---

## Section 4 — Security as Code

### 4.1 Core Concepts

Security as Code (SaC) means encoding security policies, controls, and configurations into version-controlled files that can be tested, reviewed, and deployed automatically. The benefits:

- **Repeatability** — Automated policies run identically every time.
- **Auditability** — Git history records who changed what policy and when.
- **Velocity** — Automated checks run in seconds, not days.
- **Collaboration** — Policy changes go through pull request review.

### 4.2 OPA/Rego Example

Open Policy Agent (OPA) uses the Rego language to define policies. The following policy denies Kubernetes pods running as root:

```rego
package kubernetes.admission

deny[msg] {
    input.request.kind.kind == "Pod"
    container := input.request.object.spec.containers[_]
    not container.securityContext.runAsNonRoot
    msg := sprintf("Container %v must not run as root", [container.name])
}
```

### 4.3 Conftest for Policy Testing

Conftest uses OPA policies to test configuration files directly in CI:

```yaml
# .github/workflows/policy-check.yml
jobs:
  policy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Conftest
        run: |
          conftest test k8s/ --policy policies/
```

---

## Section 5 — DevSecOps Toolchain Reference

### 5.1 Tool Categories and Leading Options

| Category | Open Source / Free | Commercial |
|---|---|---|
| SAST | SonarQube CE, Semgrep OSS | Checkmarx, Veracode |
| DAST | OWASP ZAP | Burp Suite Enterprise |
| Dependency Scan | OWASP Dependency-Check | Snyk, Black Duck |
| Container Scan | Trivy, Grype | Snyk Container, Prisma Cloud |
| IaC Scan | tfsec, checkov, Terrascan | Bridgecrew, Prisma Cloud |
| Secrets Detection | gitleaks, truffleHog | GitGuardian, Nightfall |
| Secrets Management | HashiCorp Vault OSS | HashiCorp Vault Enterprise, AWS SM |
| SCA / SBOM | Syft, CycloneDX CLI | Snyk, FOSSA |
| Runtime Security | Falco | Aqua Security, Sysdig |
| Policy Engine | OPA, Conftest | HashiCorp Sentinel |

### 5.2 Tool Selection Criteria

When selecting DevSecOps tools, evaluate against these dimensions:

- **Integration**: Does it integrate natively with your CI platform?
- **False positive rate**: High FP rates cause alert fatigue.
- **CVSS scoring**: Does it map findings to standard severity scores?
- **SARIF output**: Static Analysis Results Interchange Format enables tool-agnostic result consumption.
- **Remediation guidance**: Does the tool explain how to fix findings?
- **License compliance**: Open source licenses have legal implications.

---

## Section 6 — Cultural and Organizational Change

### 6.1 The CALMS Framework

| Pillar | DevSecOps Meaning |
|---|---|
| Culture | Shared ownership of security; blameless post-mortems |
| Automation | Replace manual security gates with pipeline controls |
| Lean | Eliminate handoff delays; streamline security review |
| Measurement | Track MTTR, vulnerability density, gate pass rate |
| Sharing | Publish security findings; run security brown-bags |

### 6.2 Adoption Anti-Patterns to Avoid

#### Tool-First Adoption

Buying tools without changing processes. Tools amplify existing practices; bad processes become bad automated processes.

#### Security Team as Gatekeeper

Security team manually approves every release. This creates a bottleneck and does not scale. Automate the gate; humans review exceptions.

#### Ignoring Developer Experience

Security tools with poor developer UX get disabled or bypassed. Choose tools with clear, actionable output.

#### Treating All Findings as Equal

Prioritize by CVSS score, exploitability, and asset criticality. Trying to fix everything creates burnout.

---

## Section 7 — ROI and Business Case

### 7.1 Cost Reduction Model

| Cost Driver | Traditional Model | DevSecOps Model |
|---|---|---|
| Vulnerability discovery cost | High — late-stage pen test | Low — automated, early |
| Vulnerability remediation time | Weeks (sprint rework) | Hours (IDE feedback) |
| Compliance evidence generation | Manual — days before audit | Automated — always ready |
| Mean Time to Remediate (MTTR) | 60–90 days | 7–14 days |
| Average data breach cost | $4.45M (IBM 2023) | 28% lower with DevSecOps |

### 7.2 Key Metrics to Track

- **Vulnerability Density** — Vulnerabilities per 1,000 lines of code over time (goal: trending down)
- **Mean Time to Remediate (MTTR)** — Average days from finding to fix (goal: under 30 days for critical)
- **Pipeline Gate Pass Rate** — Percentage of builds that pass all security gates (goal: above 90%)
- **Escape Rate** — Percentage of vulnerabilities that reach production (goal: near zero for critical)
- **Security Debt** — Total open vulnerabilities weighted by severity (goal: trending down)

---

## Exam Tips for DSOE Certification

- Know the three ways of DevOps: Flow, Feedback, Continual Learning.
- Know CALMS: Culture, Automation, Lean, Measurement, Sharing.
- Know STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.
- Be able to map tools to lifecycle phases.
- Understand the difference between SAST (static, no running app needed) and DAST (dynamic, requires running app).
- The DoD Enterprise DevSecOps Reference Design (2019) is a frequently referenced policy document.
- Security as Code enables repeatability, auditability, velocity, and collaboration.
- Shift-left reduces fix cost by finding defects earlier in the SDLC.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| DevSecOps | Integration of security practices into DevOps processes |
| Shift-Left | Moving security activities earlier in the SDLC |
| SAST | Static Application Security Testing — analyzes source code |
| DAST | Dynamic Application Security Testing — tests running application |
| SBOM | Software Bill of Materials — inventory of software components |
| SCA | Software Composition Analysis — analyzes open-source dependencies |
| IaC | Infrastructure as Code — managing infrastructure via config files |
| OPA | Open Policy Agent — general-purpose policy engine |
| CALMS | DevOps maturity framework: Culture, Automation, Lean, Measurement, Sharing |
| STRIDE | Threat modeling framework covering 6 threat categories |
| Security Champion | Developer with security expertise embedded in a dev team |
| CVSS | Common Vulnerability Scoring System — industry-standard severity scoring |
| SARIF | Static Analysis Results Interchange Format — standard for tool output |

---

Reading Guide — Module 01 | CIS-4350 | Texas Wesleyan University
