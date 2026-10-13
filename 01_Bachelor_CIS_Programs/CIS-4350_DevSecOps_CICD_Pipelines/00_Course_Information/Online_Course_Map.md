# Online Course Map

## CIS-4350 – DevSecOps & CI/CD Pipelines

**16-Week Course | Target Certification: CDP (Practical DevSecOps)**

---

## Course Theme Overview

This course is organized into five thematic blocks that build progressively from culture and foundations through specialized security testing, infrastructure security, and advanced topics culminating in certification preparation.

| Block | Weeks | Theme |
|-------|-------|-------|
| Block 1 | 1–3 | Foundations — Culture, Version Control, and CI/CD Platforms |
| Block 2 | 4–5 | Container Security — Docker and Kubernetes |
| Block 3 | 6–9 | Security Testing — SAST, DAST, SCA, and Secrets |
| Block 4 | 10–13 | Infrastructure and Policy — IaC, Image Scanning, Kubernetes Security, Compliance as Code |
| Block 5 | 14–16 | Advanced Topics — Threat Modeling, Security Metrics, and CDP Exam Prep |

---

## Week-by-Week Breakdown

---

### Block 1 — Foundations: Culture, Version Control, and CI/CD Platforms (Weeks 1–3)

**Week 1 | Module 01: DevOps Fundamentals and the DevSecOps Mindset**

* Topics: DevOps evolution, DevSecOps culture, shift-left security, pipeline automation, feedback loops, SDLC security placement
* Tools introduced: None (conceptual week)
* Key concept: Security as shared responsibility across developer, operations, and security roles
* Assessment: Quiz 01, Discussion 01

**Week 2 | Module 02: Version Control with Git and GitHub**

* Topics: Git branching, pre-commit hooks, automation runners, lint steps, branch protection rules, required status checks
* Tools introduced: Git, GitHub, Gitleaks (pre-commit secret scanning), ESLint/Flake8 (linting)
* Key concept: Local pre-commit hooks as the earliest shift-left security gate
* Assessment: Quiz 02, Lab 02 (pre-commit hook configuration), Discussion 02

**Week 3 | Module 03: CI/CD Concepts – Jenkins, GitHub Actions, GitLab CI**

* Topics: GitHub Actions YAML workflow syntax, jobs and steps, trigger events (push, pull_request), runner environments, pipeline stage ordering
* Tools introduced: GitHub Actions, YAML linting (yamllint)
* Key concept: Pipeline trigger scoping — pull_request gates vs. push triggers
* Assessment: Quiz 03, Lab 03 (GitHub Actions workflow creation), Discussion 03

---

### Block 2 — Container Security: Docker and Kubernetes (Weeks 4–5)

**Week 4 | Module 04: Containerization – Docker Security**

* Topics: Dockerfile security instructions (FROM, USER, COPY, RUN), container layer security, multi-stage builds, image layer secrets exposure, build-time vs. runtime secrets
* Tools introduced: Docker, Docker Buildx, GitHub Container Registry (ghcr.io)
* Key concept: Secrets must never be written to Dockerfile instructions or image layers
* Assessment: Quiz 04, Lab 04 (multi-stage Dockerfile, pipeline image build), Discussion 04

**Week 5 | Module 05: Container Orchestration Security – Kubernetes**

* Topics: Kubernetes Pod Security Standards (Privileged/Baseline/Restricted), multi-stage builds for Kubernetes deployments, image pull policies, pipeline-to-registry-to-cluster delivery chain
* Tools introduced: Kubernetes (minikube or kind for labs), kubectl
* Key concept: Every deployed image must be pipeline-built, scanned, and signed — no manual pushes
* Assessment: Quiz 05, Lab 05 (multi-stage build + K8s pod security context), Discussion 05

---

### Block 3 — Security Testing: SAST, DAST, SCA, and Secrets (Weeks 6–9)

**Week 6 | Module 06: SAST – Static Application Security Testing**

* Topics: SAST tool operation (pattern matching, data flow analysis), Semgrep vs. CodeQL, false positive management, pipeline blocking gates, SAST result suppression best practices
* Tools introduced: Semgrep (free OSS), CodeQL (GitHub native)
* Key concept: SAST runs at the pull request stage without requiring a running application
* Assessment: Quiz 06, Lab 06 (SAST pipeline integration), Discussion 06

**Week 7 | Module 07: DAST – Dynamic Application Security Testing**

* Topics: DAST vs. SAST comparison, OWASP ZAP passive vs. active scanning, sandbox/staging environment requirements, DAST pipeline placement, severity threshold configuration
* Tools introduced: OWASP ZAP (free OSS), DVWA or Juice Shop (vulnerable test targets)
* Key concept: DAST requires a running application — it runs after staging deployment, not at commit time
* Assessment: Quiz 07, Lab 07 (ZAP DAST pipeline integration), Discussion 07

**Week 8 | Module 08: SCA – Software Composition Analysis and Dependency Scanning**

* Topics: SCA vs. SAST distinctions, dependency trees (direct and transitive), CVE databases (NVD, GitHub Advisory), license compliance, SBOM generation, Log4Shell as a case study
* Tools introduced: OWASP Dependency-Check (free OSS), Snyk (free tier), Grype
* Key concept: Transitive dependencies carry the same CVE risk as direct dependencies
* Assessment: Quiz 08, Lab 08 (SCA scan + CVE remediation), Discussion 08

**Week 9 | Module 09: Secrets Management – HashiCorp Vault and AWS Secrets Manager**

* Topics: Secret scanning (Gitleaks, TruffleHog), Git history permanence, GitHub Actions encrypted secrets, HashiCorp Vault dynamic secrets, OIDC-based keyless authentication patterns
* Tools introduced: Gitleaks, HashiCorp Vault (free OSS)
* Key concept: Dynamic secrets expire automatically; static secrets persist as long-lived risks
* Assessment: Quiz 09, Lab 09 (Gitleaks + GitHub Actions secrets), Discussion 09

---

### Block 4 — Infrastructure and Policy: IaC, Image Scanning, K8s Security, Compliance (Weeks 10–13)

**Week 10 | Module 10: Infrastructure as Code Security – Terraform Security Scanning**

* Topics: IaC security scanning (Checkov, tfsec), common Terraform misconfigurations (public S3 buckets, open security groups, unencrypted EBS), pipeline placement before `terraform apply`, CIS Benchmark mapping
* Tools introduced: Checkov (free OSS), tfsec (free OSS), Terraform (free CLI)
* Key concept: IaC scanning at the pull request stage prevents misconfigured infrastructure from ever being provisioned
* Assessment: Quiz 10, Lab 10 (Checkov + tfsec pipeline integration), Discussion 10

**Week 11 | Module 11: Container Image Scanning – Trivy and Grype**

* Topics: Container image scanning vs. SCA (distinct attack surface layers), Trivy scan targets (image, fs, repo, k8s), severity thresholds (`--exit-code 1 --severity CRITICAL`), SARIF output for GitHub Code Scanning, base image selection impact on CVE count
* Tools introduced: Trivy (free OSS), Grype (free OSS)
* Key concept: Container image scanning catches OS-level CVEs that SCA cannot see
* Assessment: Quiz 11, Lab 11 (Trivy image scan pipeline gate), Discussion 11

**Week 12 | Module 12: Kubernetes Security – RBAC, Network Policies, Pod Security**

* Topics: Kubernetes RBAC (Role vs. ClusterRole, least privilege, service account scoping), NetworkPolicy default-deny pattern, Pod Security Standards (Privileged/Baseline/Restricted profiles), security context configuration
* Tools introduced: kubectl, minikube/kind, kube-bench (CIS benchmark scanner)
* Key concept: Default-deny NetworkPolicy + explicit allow rules + Restricted PSS = defense-in-depth Kubernetes security
* Assessment: Quiz 12, Lab 12 (Alpine base image refactor + RBAC configuration), Discussion 12

**Week 13 | Module 13: Compliance as Code – OPA and Policy Enforcement**

* Topics: Open Policy Agent (OPA) and Rego policy language, OPA Gatekeeper as Kubernetes admission controller, centralized logging (ELK Stack), application telemetry (Prometheus), compliance-as-code vs. periodic audit, SIEM integration
* Tools introduced: OPA/Gatekeeper, Prometheus (free OSS), Grafana (free OSS)
* Key concept: Compliance as Code enforces policy at every API call — not just at audit time
* Assessment: Quiz 13, Lab 13 (Prometheus alerting + OPA Gatekeeper policy), Discussion 13

---

### Block 5 — Advanced Topics: Threat Modeling, Metrics, and CDP Prep (Weeks 14–16)

**Week 14 | Module 14: Threat Modeling in DevSecOps**

* Topics: STRIDE framework, Data Flow Diagrams, trust boundary identification, chaos engineering, failure injection (Chaos Monkey, Gremlin), resilience testing of security controls, fallback path security analysis
* Tools introduced: Microsoft Threat Modeling Tool (free), draw.io for DFDs
* Key concept: Threat modeling is the design-phase security activity that precedes all automated pipeline security gates
* Assessment: Quiz 14, Lab 14 (STRIDE threat enumeration + resilience path analysis), Discussion 14

**Week 15 | Module 15: Security Metrics and Dashboards in CI/CD**

* Topics: DevSecOps KPIs (MTTR, vulnerability backlog, gate pass rates), DORA metrics with security integration, pipeline audit logs as compliance evidence, signed commits and build log validation, release approval workflows for regulatory compliance
* Tools introduced: GitHub Security tab (code scanning results), Git GPG signing
* Key concept: Immutable pipeline audit logs provide continuous compliance evidence — replacing periodic manual attestation
* Assessment: Quiz 15, Lab 15 (signed commit verification + compliance audit log review), Discussion 15

**Week 16 | Module 16: Final Exam Prep & DevSecOps Professional Certification**

* Topics: Complete pipeline security gate sequence review, cross-tool integration scenarios, CDP exam strategy (shift-left reasoning, tool-to-stage mapping, distractor pattern recognition), official CDP exam objectives review
* Tools: Review all tools from Modules 01–15
* Key concept: Each security gate covers a distinct, non-overlapping attack surface — SAST + SCA + image scanning + DAST + IaC scanning together provide defense in depth across the full pipeline
* Assessment: Quiz 16, Lab 16 (end-to-end pipeline documentation), **Final Exam**

---

## Pipeline Security Gate Quick Reference

The following table summarizes the complete DevSecOps pipeline sequence covered in this course:

| Pipeline Stage | Security Gate | Tool(s) | Trigger |
|----------------|--------------|---------|---------|
| Pre-commit | Secret scanning, linting | Gitleaks, ESLint/Flake8 | Local git hook |
| Pull Request | SAST | Semgrep, CodeQL | `on: pull_request` |
| Build | SCA | OWASP Dep-Check, Snyk | `on: pull_request` |
| Post-build | Container image scan | Trivy, Grype | After `docker build` |
| IaC change | IaC security scan | Checkov, tfsec | PR to IaC repo |
| Pre-apply | IaC linting | tflint | Before `terraform plan` |
| Staging deploy | DAST | OWASP ZAP | After staging deploy |
| K8s admission | Policy enforcement | OPA Gatekeeper | Every K8s API request |
| Production | Compliance gate | Pipeline audit + signatures | Before prod deploy |

---

## CDP Certification Exam Reference

* **Certification:** Certified DevSecOps Professional (CDP)
* **Provider:** Practical DevSecOps
* **Exam Information:** [https://www.practical-devsecops.com/certified-devsecops-professional/](https://www.practical-devsecops.com/certified-devsecops-professional/)
* **Format:** Scenario-based multiple choice questions
* **Exam fee:** Not included in course — students register independently
