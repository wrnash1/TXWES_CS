# Lab Activity: Module 16 — Pipeline Capstone and Exam Readiness

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 120–150 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Overview

This capstone lab brings together every major domain from CIS-4350. You will configure a complete DevSecOps CI/CD pipeline for a Python Flask application deployed to Kubernetes, covering pre-commit security hooks, pipeline security gates (SAST, SCA, container scanning, secrets scanning, IaC scanning), artifact signing, Kubernetes admission policy, and runtime monitoring configuration. You will then complete a pipeline design exercise that mirrors the scenario-based questions on the DSOE certification exam.

Completing this lab in full constitutes a working demonstration of a production-grade DevSecOps pipeline and is the strongest possible exam preparation for the pipeline and tooling domains of the DSOE exam.

---

### Learning Objectives

By completing this lab you will be able to:

- Configure a pre-commit hook with secrets scanning on a local Git repository
- Write a GitHub Actions workflow implementing all four pipeline security stages
- Configure a Trivy image scan gate with a CRITICAL finding threshold
- Write an OPA Rego policy that blocks containers running as root
- Describe the complete pipeline sequence from commit to runtime monitoring
- Apply the two-step elimination method to three DSOE-style scenario questions

---

### Prerequisites

- Git installed on your workstation
- Docker installed and running
- A GitHub account with a test repository
- Python 3.x installed (for the Flask application)
- Access to a Kubernetes cluster (Minikube, Kind, or any managed cluster)
- `kubectl` configured and pointing to your cluster
- `cosign` installed (optional, for artifact signing exercises)

---

### Part 1: Pre-Commit Security Hooks (20 minutes)

Pre-commit hooks run before each git commit on the developer's workstation — the earliest possible security gate.

#### Task 1.1 — Install detect-secrets

```bash
pip install detect-secrets
detect-secrets scan > .secrets.baseline
```

Initialize the baseline file. This file records any existing secrets-like strings in the repository so they are not re-flagged on every commit.

#### Task 1.2 — Configure the pre-commit hook

Create `.pre-commit-config.yaml` in your repository root:

```yaml
repos:
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
```

Install the hook:

```bash
pip install pre-commit
pre-commit install
```

#### Task 1.3 — Verify the hook fires

Create a test file with a fake AWS key pattern:

```bash
echo 'AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY' > test_secret.py
git add test_secret.py
git commit -m "test secret detection"
```

Expected result: the commit is blocked with a detect-secrets warning listing the detected secret. Remove the file before proceeding.

#### Deliverable 1

Screenshot or terminal output showing the pre-commit hook blocking the commit with a detected secret.

---

### Part 2: GitHub Actions Pipeline — Four Security Stages (40 minutes)

#### Task 2.1 — Create the workflow file

Create `.github/workflows/devsecops-pipeline.yml` with the following structure. You will fill in each stage.

```yaml
name: DevSecOps Pipeline

on:
  pull_request:
    branches: [main]

permissions:
  contents: read
  security-events: write

jobs:
```

#### Task 2.2 — Stage 1: SAST with Semgrep

Add the SAST job to the workflow:

```yaml
  sast:
    name: SAST - Semgrep
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Semgrep
        uses: semgrep/semgrep-action@v1
        with:
          config: >-
            p/python
            p/owasp-top-ten
          generateSarif: "1"
      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: semgrep.sarif
```

#### Task 2.3 — Stage 2: SCA with OWASP Dependency-Check

```yaml
  sca:
    name: SCA - Dependency-Check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: OWASP Dependency-Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: 'flask-app'
          path: '.'
          format: 'JSON'
          args: '--failOnCVSS 9'
      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: dependency-check-report
          path: reports/
```

Note: `--failOnCVSS 9` fails the build on CRITICAL findings (CVSS >= 9.0).

#### Task 2.4 — Stage 3: Container Build and Trivy Scan

```yaml
  container-security:
    name: Container Build and Scan
    runs-on: ubuntu-latest
    needs: [sast, sca]
    steps:
      - uses: actions/checkout@v4
      - name: Build image
        run: docker build -t flask-app:${{ github.sha }} .
      - name: Trivy scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: flask-app:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL'
          exit-code: '1'
      - name: Upload Trivy SARIF
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: trivy-results.sarif
```

#### Task 2.5 — Stage 4: IaC Scanning with Checkov

```yaml
  iac-security:
    name: IaC Scan - Checkov
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: k8s/
          framework: kubernetes
          soft_fail: false
          output_format: sarif
          output_file_path: checkov.sarif
      - name: Upload Checkov SARIF
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: checkov.sarif
```

#### Task 2.6 — Review the complete workflow

Open a pull request to your test repository and observe all four jobs running. Capture the result of each job.

#### Deliverable 2

Screenshot of the GitHub Actions run showing all four security jobs with their pass/fail status. Write a one-paragraph explanation of which stage catches which category of vulnerability and why each stage is placed in its current position in the pipeline.

---

### Part 3: Kubernetes Security Configuration (30 minutes)

#### Task 3.1 — Security Context

Create `k8s/deployment.yaml` for the Flask application with a fully hardened Security Context:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
  namespace: production
spec:
  replicas: 2
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      serviceAccountName: flask-app-sa
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 2000
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: flask-app
          image: flask-app:latest
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
          resources:
            limits:
              cpu: "500m"
              memory: "256Mi"
            requests:
              cpu: "100m"
              memory: "128Mi"
```

Apply this manifest and verify the pod starts successfully:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl get pods -n production
kubectl describe pod -n production -l app=flask-app
```

#### Task 3.2 — Default-Deny NetworkPolicy

Create `k8s/network-policy.yaml`:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-flask-ingress
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: flask-app
  policyTypes:
    - Ingress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: ingress-nginx
      ports:
        - protocol: TCP
          port: 5000
```

Apply and verify:

```bash
kubectl apply -f k8s/network-policy.yaml
kubectl get networkpolicies -n production
```

#### Task 3.3 — OPA Gatekeeper Policy

If OPA Gatekeeper is installed in your cluster, apply the following ConstraintTemplate that blocks containers running as root:

```yaml
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequirenonroot
spec:
  crd:
    spec:
      names:
        kind: K8sRequireNonRoot
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequirenonroot

        violation[{"msg": msg}] {
          container := input.review.object.spec.containers[_]
          not container.securityContext.runAsNonRoot
          msg := sprintf("Container %v must set runAsNonRoot: true", [container.name])
        }
---
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequireNonRoot
metadata:
  name: require-non-root-containers
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    namespaces: ["production"]
```

Test the policy by attempting to deploy a pod without `runAsNonRoot: true`. Confirm that the deployment is rejected.

#### Deliverable 3

Screenshot of:

- The hardened pod running successfully in the production namespace
- The NetworkPolicy list showing default-deny and the ingress allow rule
- The OPA Gatekeeper policy rejection message when a non-compliant pod is attempted

---

### Part 4: Pipeline Design Exam Exercise (30 minutes)

This part mirrors the scenario-based format of DSOE exam questions. For each scenario, write your answer using the two-step elimination method from the video lecture: identify the primary constraint first, eliminate non-compliant options, then select the best answer with a one-paragraph justification.

#### Scenario A

An organization deploys a Python microservice to Kubernetes. The pipeline runs SAST and SCA on every PR. A security audit finds that the production pod is running as root with no resource limits. Which pipeline stage should be added to catch this class of misconfiguration before production deployment?

Options:

1. Add a DAST scan in the staging environment
2. Add Checkov IaC scanning on the Kubernetes manifests directory in the CI pipeline, configured to fail on HIGH severity Kubernetes misconfigurations
3. Add Trivy image scanning to catch OS-level vulnerabilities in the container image
4. Add Falco runtime rules that alert when a container runs as root

Write your primary constraint identification, elimination reasoning, and final answer with justification.

#### Scenario B

A Kubernetes cluster has OPA/Gatekeeper deployed with a policy that blocks containers without resource limits. A developer reports that a legitimate deployment was rejected. The Rego policy evaluates `container.resources.limits`. The developer's deployment has `resources.limits.cpu: "500m"` but no `resources.limits.memory`. Is the policy functioning correctly? What should the developer do?

Write your analysis. Include whether this is a policy false positive or a genuine policy violation, and what the correct fix is.

#### Scenario C

A security team wants to implement Compliance as Code for PCI-DSS Requirement 6.3 (security vulnerabilities identified and addressed). Three options are proposed:

1. Annual penetration test with findings tracked in a spreadsheet
2. Quarterly automated vulnerability scan of production with findings emailed to the team
3. Mandatory SAST, SCA, and container scanning gates in the CI/CD pipeline with CRITICAL findings blocking every deployment, scan results published to an immutable log store linked to each deployment's pipeline run ID

Which option satisfies Compliance as Code principles, and why do the other options not qualify?

Write your analysis using the Compliance as Code definition from the course.

---

### Deliverables Summary

| Deliverable | Description |
|---|---|
| Deliverable 1 | Pre-commit hook blocking screenshot |
| Deliverable 2 | GitHub Actions four-stage pipeline screenshot + one-paragraph explanation |
| Deliverable 3 | Kubernetes security configuration screenshots (three items) |
| Deliverable 4 | Written analysis for Scenarios A, B, and C using two-step elimination |

Submit all four deliverables as a single PDF or document via Canvas LMS before the module deadline.

---

### Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Pre-commit hook (Part 1) | 15 | Hook correctly installed; screenshot shows detection and block |
| Pipeline workflow (Part 2) | 30 | All four stages present; correct tools; correct exit codes; explanation accurate |
| Kubernetes security (Part 3) | 30 | Security Context fully hardened; NetworkPolicy correct; OPA policy rejects non-compliant pod |
| Pipeline design exam exercise (Part 4) | 25 | Two-step elimination applied; correct answers with justified analysis for all three scenarios |
| **Total** | **100** | |

---

## Part 9 — Challenge Exercise

### Challenge 1: End-to-End Pipeline Security Audit

Conduct a security audit of your completed capstone pipeline from Lab Parts 1–4 and produce a gap analysis report.

1. Review your full pipeline workflow YAML and list every security control present. For each control, record: the tool name, the pipeline stage, the STRIDE threat category it addresses, and whether it is a preventive gate (blocks merge/deploy) or a detective alert (reports but does not block).
2. Cross-reference your control list against the DSOE exam domain map from Module 16 Reading Guide Section 1. Identify any exam domains that have no corresponding control in your pipeline.
3. For each identified gap, write a remediation recommendation: the specific tool or configuration change needed, which pipeline stage it belongs in, and which compliance framework requirement it addresses (SOC 2, PCI-DSS, or HIPAA).
4. Produce a one-page executive summary that characterizes your pipeline's current DSOMM maturity level with evidence, identifies the top three gaps, and proposes a prioritized 30-day remediation roadmap.

### Challenge 2: Full-Stack Threat Model to Pipeline Traceability

Produce a complete threat model to pipeline control traceability document for the Flask application from Lab Parts 1–4.

1. Draw a DFD for the full system: developer workstation → GitHub → GitHub Actions CI → container registry → Kubernetes production cluster → end user browser. Include all external entities, processes, data stores, data flows, and trust boundaries.
2. Apply STRIDE to each trust boundary. Document at least 12 threats (minimum 2 per STRIDE category).
3. For each threat, map it to a specific control in your pipeline or cluster configuration. Use the format: Threat ID | STRIDE Category | Threat Title | Control | Control Stage | Control Type (preventive/detective/corrective).
4. Identify any threats for which no control exists in your current pipeline. Write a GitHub issue title and description for each gap that could be used to track the remediation as a backlog item.

### Reflection Questions

1. You have built and audited a complete DevSecOps pipeline across all sixteen modules of this course. Looking back at the full control suite — pre-commit hooks, SAST, SCA, container scanning, secrets scanning, IaC scanning, artifact signing, admission control, runtime monitoring — describe the single most important architectural principle that unifies all of these controls, and explain how each control layer would fail in the absence of that principle.
2. A colleague who has not taken this course asks: "We already have a firewall and run annual penetration tests. Why do we need all of these pipeline tools?" Write a 200-word response that explains the shift-left DevSecOps argument using concrete cost-of-defect data, and describe the specific class of attack that each module's primary tool is designed to prevent that a firewall and annual pen test cannot.

---

Lab 16 | CIS-4350 | Texas Wesleyan University | Professor Nash
