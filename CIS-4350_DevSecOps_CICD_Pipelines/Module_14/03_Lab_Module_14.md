# Lab Activity: Module 14 — Threat Modeling with STRIDE and OWASP Threat Dragon

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 90–120 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Overview

In this lab you will produce a complete threat model for a cloud-native CI/CD pipeline using the STRIDE framework and OWASP Threat Dragon. You will draw a data flow diagram with trust boundaries, apply STRIDE analysis to identify threats, document each threat with a severity and mitigation, and produce a traceability matrix mapping identified threats to CI/CD security controls. You will then export the threat model as JSON and author a written threat model summary document.

---

### Learning Objectives

By completing this lab you will be able to:

- Draw a data flow diagram with the four standard DFD element types and trust boundaries
- Apply the STRIDE framework to identify at least one threat per category in a cloud-native system
- Document threats in OWASP Threat Dragon with severity, status, and mitigation descriptions
- Export a Threat Dragon model as a JSON file suitable for version control
- Produce a threat model traceability matrix linking identified threats to CI/CD controls

---

### Prerequisites

- A web browser (Chrome or Firefox recommended)
- Access to `https://www.threatdragon.com` (free, no account required for basic use) or the OWASP Threat Dragon desktop app
- A text editor for the written deliverables

---

### Lab Structure

This lab has three parts:

- Part 1: Draw the data flow diagram in Threat Dragon
- Part 2: Apply STRIDE and document threats
- Part 3: Export and produce traceability matrix

---

### System to Model

You will threat model the following system. Read this description carefully — your DFD must accurately represent all components, data flows, and trust boundaries.

The system is a cloud-native SaaS application with a CI/CD pipeline:

- Developers push code to a GitHub repository
- GitHub Actions runs a build pipeline including SAST scanning, container image building, container scanning, and deployment
- The built container image is pushed to a container registry (Amazon ECR)
- The GitHub Actions workflow deploys the image to a Kubernetes cluster in AWS EKS
- The application consists of three services: a frontend pod, an API pod, and a database pod (PostgreSQL)
- The API pod reads application secrets (database credentials, API keys) from Kubernetes Secrets
- The frontend pod communicates with the API pod over HTTPS on port 443
- The API pod communicates with the database pod on port 5432
- End users access the frontend via a public load balancer
- All pods are in the `production` namespace; the CI/CD service account is in the `cicd` namespace

---

### Part 1 — Draw the Data Flow Diagram

#### Step 1.1 — Open OWASP Threat Dragon

Navigate to `https://www.threatdragon.com` and select "Start New Model." Enter:

- Title: `CIS-4350 Lab 14 — CI/CD Pipeline Threat Model`
- Owner: your name
- Description: `STRIDE threat model for a cloud-native CI/CD pipeline with GitHub Actions, ECR, EKS, and a three-tier application`

#### Step 1.2 — Add DFD elements

Add the following elements to your diagram. Use the correct DFD element type for each:

External entities (rectangles):

- `Developer (GitHub Push)`
- `End User (Browser)`
- `GitHub Actions Service`

Processes (circles/ovals):

- `GitHub Actions Runner`
- `Kubernetes API Server`
- `Frontend Pod`
- `API Pod`

Data stores (parallel lines):

- `GitHub Repository`
- `Amazon ECR (Container Registry)`
- `PostgreSQL Database Pod`
- `Kubernetes Secrets`

#### Step 1.3 — Add data flows with labels

Add directed arrows between elements, labeled with the data they carry:

- Developer → GitHub Repository: `Code push (HTTPS)`
- GitHub Repository → GitHub Actions Runner: `Webhook trigger (CI event)`
- GitHub Actions Runner → Amazon ECR: `Container image push (authenticated)`
- GitHub Actions Runner → Kubernetes API Server: `Deployment manifest apply (OIDC token)`
- End User → Frontend Pod: `HTTPS request (via load balancer)`
- Frontend Pod → API Pod: `HTTPS API call (port 443)`
- API Pod → Kubernetes Secrets: `Secret read (service account token)`
- API Pod → PostgreSQL Database Pod: `SQL query (port 5432, TLS)`
- Kubernetes API Server → Frontend Pod: `Pod scheduling`
- Kubernetes API Server → API Pod: `Pod scheduling`

#### Step 1.4 — Add trust boundaries

Add trust boundary lines to separate these zones:

- Internet boundary: separates `End User` from `Frontend Pod`
- Pipeline boundary: separates `GitHub Actions Service` / `GitHub Actions Runner` from the Kubernetes cluster
- Namespace boundary: separates the `cicd` namespace (Kubernetes API Server / pipeline service account) from the `production` namespace (Frontend, API, Database pods)
- Application boundary: separates `Frontend Pod` from `API Pod`
- Data boundary: separates `API Pod` from `PostgreSQL Database Pod` and `Kubernetes Secrets`

Save your diagram before proceeding.

---

### Part 2 — Apply STRIDE and Document Threats

For each of the following threat entries, add a threat in Threat Dragon on the relevant DFD element. Complete all fields: STRIDE category, title, description, severity, status, and mitigation.

#### Step 2.1 — Spoofing threats

Add to the `GitHub Actions Runner` process:

- Category: Spoofing
- Title: `Malicious GitHub Action impersonates trusted action`
- Description: A supply chain attacker publishes a malicious GitHub Action with a name similar to a trusted action (e.g., `actions/checkoutt`). A developer copies a workflow that references the malicious action. The malicious action executes in the runner context with access to repository secrets and OIDC tokens.
- Severity: High
- Status: Mitigated
- Mitigation: Pin all GitHub Actions to a specific commit SHA rather than a mutable tag (e.g., `actions/checkout@a81bbbf` instead of `actions/checkout@v4`). Implement a CI lint rule that fails if unpinned action references are detected.

Add to the `Kubernetes API Server` process:

- Category: Spoofing
- Title: `Stolen OIDC token used to authenticate to Kubernetes API`
- Description: An attacker who compromises the GitHub Actions runner (via malicious action or repository secret exposure) can steal the OIDC token used to authenticate the CI/CD service account to the Kubernetes API, then make API calls as the CI/CD service account from outside the pipeline.
- Severity: High
- Status: Mitigated
- Mitigation: Scope the OIDC trust policy to require specific repository and branch conditions. Use a least-privilege CI/CD Role scoped to the production namespace with only the verbs required for deployment.

#### Step 2.2 — Tampering threats

Add to the `Amazon ECR (Container Registry)` data store:

- Category: Tampering
- Title: `Container image replaced in registry after scanning`
- Description: An attacker with write access to ECR replaces a scanned and approved container image with a backdoored version between the time the image is scanned and the time it is deployed. The Kubernetes cluster pulls the modified image.
- Severity: High
- Status: Mitigated
- Mitigation: Implement container image signing with AWS Signer or Cosign. Configure the Kubernetes cluster to verify image signatures at admission using Gatekeeper or Kyverno. Deploy images by digest (`@sha256:...`) rather than mutable tags.

Add to the `GitHub Repository` data store:

- Category: Tampering
- Title: `Malicious code injected via unreviewed pull request`
- Description: An external contributor or compromised developer account submits a pull request that introduces malicious code. Without mandatory review requirements, the code is merged and deployed.
- Severity: Medium
- Status: Mitigated
- Mitigation: Enforce branch protection rules: require at least two reviewers, require passing SAST and SCA gates, disallow self-approval, require signed commits.

#### Step 2.3 — Repudiation threats

Add to the `Kubernetes API Server` process:

- Category: Repudiation
- Title: `Privileged API action performed with no audit evidence`
- Description: An engineer with cluster-admin access deletes a namespace or modifies RBAC bindings during an incident. Without Kubernetes audit logging sent to an immutable log store, there is no evidence of who performed the action.
- Severity: Medium
- Status: Mitigated
- Mitigation: Enable Kubernetes audit logging at the `RequestResponse` level for sensitive API groups. Ship audit logs to an immutable store (CloudWatch Logs with retention policy, or Elasticsearch with S3 backup). Route audit logs to SIEM for correlation.

#### Step 2.4 — Information Disclosure threats

Add to the `Kubernetes Secrets` data store:

- Category: Information Disclosure
- Title: `Database credentials exposed via unencrypted Kubernetes Secret`
- Description: Kubernetes Secrets are base64-encoded, not encrypted, by default. An attacker with `get secrets` permission in the production namespace can read and decode all application secrets including database credentials and API keys.
- Severity: High
- Status: Mitigated
- Mitigation: Enable Kubernetes Secrets encryption at rest using AWS KMS envelope encryption. Apply RBAC to restrict `get secrets` to only the specific service accounts that need each secret. Consider an external secrets manager (AWS Secrets Manager + External Secrets Operator) for additional isolation.

Add to the `GitHub Repository` data store:

- Category: Information Disclosure
- Title: `Database credentials hardcoded in source code`
- Description: A developer hardcodes a database password, API key, or other secret directly in source code and commits it. The secret is now in Git history permanently — even if the commit is amended, it may exist in forks or local clones.
- Severity: Critical
- Status: Mitigated
- Mitigation: Add secret scanning gate to CI pipeline (GitHub Advanced Security secret scanning or TruffleHog). Enforce pre-commit hook with `gitleaks` to catch secrets before push. Rotate any secrets discovered in historical commits.

#### Step 2.5 — Denial of Service threats

Add to the `API Pod` process:

- Category: Denial of Service
- Title: `Unbounded container resource consumption starves other pods`
- Description: The API pod has no memory or CPU limits defined. Under high load or during a memory leak, the API pod consumes all available node resources, causing the operating system's OOM killer to terminate other pods on the same node.
- Severity: Medium
- Status: Mitigated
- Mitigation: Define explicit `resources.limits.memory` and `resources.limits.cpu` for all containers. Apply OPA/Gatekeeper Constraint to deny pods without resource limits. Set namespace-level ResourceQuota and LimitRange as a backstop.

#### Step 2.6 — Elevation of Privilege threats

Add to the `API Pod` process:

- Category: Elevation of Privilege
- Title: `Container escape via privileged container or host process access`
- Description: If the API pod container runs as root with `privileged: true` or without `allowPrivilegeEscalation: false`, an attacker who achieves remote code execution in the API service can exploit the privileged context to escape the container namespace and gain root access to the underlying EKS node.
- Severity: Critical
- Status: Mitigated
- Mitigation: Apply Security Context with `runAsNonRoot: true`, `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, and `capabilities.drop: ALL`. Apply the `restricted` PodSecurity profile to the production namespace. Use Falco to detect privilege escalation attempts at runtime.

---

### Part 3 — Export and Produce Traceability Matrix

#### Step 3.1 — Export the Threat Dragon model

In Threat Dragon, export the model as JSON. Save the file as `cis4350-lab14-threat-model.json`. This file should be treated as a source code artifact — in a real project it would be committed to the application's Git repository.

#### Step 3.2 — Produce the traceability matrix

Create a table (in your lab report document) mapping each identified threat to the CI/CD control that mitigates it:

| Threat ID | STRIDE Category | Threat Title | CI/CD Control | Control Type |
|---|---|---|---|---|
| TM-001 | Spoofing | Malicious Action impersonation | GitHub Actions: pinned action SHA | Pipeline gate |
| TM-002 | Spoofing | Stolen OIDC token | OIDC trust policy + least-privilege RBAC | IAM control |
| TM-003 | Tampering | Image replaced in registry | Image signing (Cosign) + admission verification | Runtime gate |
| TM-004 | Tampering | Malicious PR merge | Branch protection + SAST + SCA gates | Pipeline gate |
| TM-005 | Repudiation | API action without audit evidence | Kubernetes audit logging → SIEM | Detective control |
| TM-006 | Information Disclosure | Unencrypted Kubernetes Secret | KMS encryption at rest + RBAC | Infrastructure control |
| TM-007 | Information Disclosure | Hardcoded credentials | Secret scanning gate (TruffleHog/GitHub) | Pipeline gate |
| TM-008 | Denial of Service | Unbounded resource consumption | Resource limits policy (OPA/Gatekeeper) | Admission control |
| TM-009 | Elevation of Privilege | Container escape via privileged context | Security Context + PodSecurity restricted + Falco | Multi-layer control |

For each row, verify that the CI/CD control listed is either already implemented (per the system description) or has been identified as a gap requiring a ticket.

#### Step 3.3 — Identify gaps

Review your traceability matrix and identify any STRIDE threats for which no control currently exists in the system as described. In your lab report, list these gaps as remediation recommendations with a suggested implementation priority (Critical/High/Medium).

---

### Deliverables

Submit the following in your lab report document:

1. Screenshot of the completed Threat Dragon DFD showing all elements, data flows, and trust boundaries
2. The exported `cis4350-lab14-threat-model.json` file
3. The completed traceability matrix (Step 3.2) with all nine threats and controls
4. Gap analysis (Step 3.3) identifying any threats without implemented controls and remediation recommendations
5. Written reflection (150–200 words): In your own words, explain how performing this threat model exercise changed or reinforced your understanding of which CI/CD security controls are most important for this system. Reference at least two specific STRIDE threats from the lab.

---

### Grading Rubric

| Criterion | Points |
|---|---|
| Threat Dragon DFD includes all required elements, data flows, and trust boundaries | 25 |
| All nine STRIDE threat entries are documented with all required fields (category, severity, status, mitigation) | 35 |
| Traceability matrix correctly maps all threats to controls with correct control type classification | 20 |
| Gap analysis identifies at least one genuine gap with a specific remediation recommendation | 10 |
| Written reflection demonstrates understanding of threat modeling value with specific threat references | 10 |
| **Total** | **100** |

---

*CIS-4350 DevSecOps and CI/CD Pipelines | Texas Wesleyan University | Professor Nash*
