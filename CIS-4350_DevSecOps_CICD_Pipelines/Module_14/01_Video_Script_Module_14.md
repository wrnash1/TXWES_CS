# Video Script: Module 14 — Threat Modeling in DevSecOps

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–2:00)

Welcome back to CIS-4350. I'm Professor Nash. In previous modules we covered detection and enforcement — Falco for runtime security, Gatekeeper for admission control, SIEM for event correlation. All of those operate after code is written and deployed. In this module we move to the earliest possible security intervention: threat modeling before you write a line of code.

Threat modeling is the practice of systematically identifying threats to a system, evaluating their potential impact, and deciding what controls to apply. Done well, it surfaces security requirements at design time when they are cheapest to address. A security control designed into an architecture costs a fraction of one retrofitted after a production breach.

The DSOE exam tests threat modeling through the STRIDE framework and the use of tooling like OWASP Threat Dragon to produce data flow diagrams with threat annotations. By the end of this module you will understand STRIDE and how to apply each category, how to draw a data flow diagram and annotate it with threats, how to use OWASP Threat Dragon to produce a threat model document, how to integrate threat modeling into a DevSecOps sprint workflow, and how to use threat model outputs to drive CI/CD security gate requirements.

---

### SEGMENT 2 — What Is Threat Modeling and Why Does It Matter (2:00–5:00)

Threat modeling answers four questions:

1. What are we building?
2. What can go wrong?
3. What are we going to do about it?
4. Did we do a good enough job?

These four questions correspond to the four phases of a threat model: decompose the system, identify threats, determine countermeasures, and validate.

The value of threat modeling in a DevSecOps context is that it moves security to the left of everything else. Before you commit the first line of code, you have a documented list of the threats your system faces and the controls you plan to implement. This documentation then drives your CI/CD pipeline: SAST gates close Spoofing and Tampering threats, container scanning closes known vulnerability threats, OPA policies close privilege escalation threats. The threat model is the security requirements document that all downstream controls trace back to.

Without threat modeling, security controls are added reactively — after a CVE, after a pentest finding, after a breach. Reactive security debt is expensive. The 2021 Log4Shell response cost organizations an estimated $10 billion in remediation work on a vulnerability class — remote code execution via untrusted deserialization — that threat modeling would have flagged as a design concern for any service that logs user-controlled input.

The three most widely used threat modeling methodologies are:

- STRIDE — Microsoft's threat category framework
- PASTA — Process for Attack Simulation and Threat Analysis — a risk-centric approach
- LINDDUN — a privacy-focused threat modeling framework

For the DSOE exam and this module, STRIDE is the primary focus.

---

### SEGMENT 3 — The STRIDE Framework (5:00–10:00)

STRIDE is a mnemonic that organizes threats into six categories. Each category maps to a violated security property.

**Spoofing** — An attacker claims to be someone or something they are not. Violated property: Authentication. Example in a cloud-native system: an attacker who compromises a Kubernetes pod steals its service account token and uses it to authenticate to the Kubernetes API as that service account, making API calls the legitimate service account was authorized to make.

**Tampering** — An attacker modifies data or code they should not be able to modify. Violated property: Integrity. Example: An attacker with write access to an S3 bucket that stores deployment artifacts replaces a legitimate binary with a backdoored version. Without artifact signing and hash verification, the pipeline deploys the modified artifact.

**Repudiation** — An actor denies performing an action, and there is no evidence to refute the claim. Violated property: Non-repudiation. Example: A privileged engineer deletes audit logs from CloudTrail before an investigation. Without CloudTrail log file validation and S3 object lock, the deletion cannot be proven.

**Information Disclosure** — Sensitive data is exposed to unauthorized parties. Violated property: Confidentiality. Example: A Kubernetes Secret is stored as a base64-encoded value in a Git repository. Base64 is encoding, not encryption. Anyone with repository read access can decode the secret.

**Denial of Service** — An attacker degrades or destroys availability. Violated property: Availability. Example: A container without resource limits can consume all available CPU and memory on a node, starving other containers. A threat actor who controls one container can deny service to the entire node.

**Elevation of Privilege** — An attacker gains capabilities beyond what they are authorized to have. Violated property: Authorization. Example: A container running as root with `allowPrivilegeEscalation: true` can exploit a kernel vulnerability to escape the container and gain root access to the underlying node.

STRIDE is applied during the threat identification phase of threat modeling. For each component in a data flow diagram, you ask: what STRIDE threats apply here? This systematic approach ensures you consider all threat categories for every component, rather than focusing only on the threat types your team has encountered before.

---

### SEGMENT 4 — Data Flow Diagrams (10:00–14:00)

A data flow diagram — DFD — is the primary artifact of threat modeling. It shows the components of a system, the data flows between them, and the trust boundaries between different security zones. Threats are annotated on the DFD.

A DFD has four element types:

**Process** — A component that transforms data. Represented as a circle or oval. Example: the API server, the authentication service, the CI/CD runner.

**Data store** — A component that stores data at rest. Represented as two parallel horizontal lines. Example: a database, an S3 bucket, a Kubernetes Secret, a configuration file.

**External entity** — An actor outside the system boundary that interacts with the system. Represented as a rectangle. Example: an end user, a third-party API, a CI/CD service like GitHub Actions.

**Data flow** — The movement of data between components. Represented as a directed arrow. Each data flow arrow is labeled with what data it carries.

**Trust boundary** — A line that separates zones with different security trust levels. Data crossing a trust boundary requires validation. Trust boundaries are where STRIDE threats most commonly apply.

Here is a simple DFD for a CI/CD pipeline with a Kubernetes deployment:

```text
[GitHub (External Entity)]
        |
        | Code push (trigger)
        v
[GitHub Actions Runner (Process)]  ---trust boundary---
        |
        | Build artifact
        v
[Container Registry (Data Store)]
        |
        | Image pull
        v
[Kubernetes API Server (Process)]  ---trust boundary---
        |
        | Pod scheduling
        v
[Pod / Container (Process)]
        |
        | App data
        v
[Database (Data Store)]
```

Each arrow crossing a trust boundary is a threat annotation candidate. The push from GitHub to the runner crosses an external boundary — Spoofing threat (is this push from the legitimate repository?). The image pull from the registry to the cluster crosses a trust boundary — Tampering threat (is this image unmodified from what was built and scanned?). The pod to database connection crosses an internal service boundary — Information Disclosure threat (is the connection encrypted? does the pod have least-privilege database credentials?).

---

### SEGMENT 5 — OWASP Threat Dragon (14:00–17:30)

OWASP Threat Dragon is a free, open-source threat modeling tool that provides a diagramming interface for drawing DFDs and a structured form for documenting threats. It runs as a web application (app.threatdragon.com) and as a desktop Electron app.

Threat Dragon stores threat model data as JSON files, which can be committed to a Git repository alongside the code they model. This is the "threat model as code" practice — the threat model evolves with the codebase through pull requests, just like application source code.

In Threat Dragon, you draw your DFD using the four element types — processes, data stores, external entities, and data flows with trust boundaries. For each element, Threat Dragon provides a threat panel where you document:

- Threat type (STRIDE category)
- Threat title and description
- Threat severity (High/Medium/Low)
- Status (Open/Mitigated/Not Applicable)
- Mitigation description

A completed Threat Dragon model for a Kubernetes microservice might contain 15–30 individual threats across all components. The output can be exported as a PDF threat model document or as a JSON file for version control.

Integrating Threat Dragon into a DevSecOps workflow:

1. At sprint planning, identify features that introduce new components or data flows
2. During design, open Threat Dragon and update the DFD to include the new components
3. Run a threat identification session using STRIDE against each new element and data flow
4. Add threat entries in Threat Dragon with mitigations identified
5. Open tickets for mitigations that require code changes
6. Commit the updated `.threat-model.json` to the feature branch
7. As part of PR review, validate that the threat model reflects the implemented changes

---

### SEGMENT 6 — Threat Modeling Output to CI/CD Controls (17:30–20:30)

The threat model is not a compliance artifact that gets filed and forgotten. Its output directly drives what security gates you implement in your CI/CD pipeline. Here is how each STRIDE category maps to DevSecOps controls:

**Spoofing threats** drive: OIDC-based authentication for CI/CD (no static secrets), mTLS between microservices, Kubernetes RBAC with dedicated service accounts, container image signing with Cosign.

**Tampering threats** drive: SAST gates (prevent code injection), SCA gates (prevent dependency tampering), artifact signing and hash verification, Git commit signing, branch protection rules.

**Repudiation threats** drive: CloudTrail and Kubernetes audit logging, SIEM centralization, log integrity controls (S3 Object Lock, CloudTrail log file validation), immutable audit trails.

**Information Disclosure threats** drive: Secret scanning gates (prevent secrets in code), container image scanning (prevent known vulnerable libraries), encryption at rest for data stores, TLS requirements for all service connections, Kubernetes Secret encryption at rest.

**Denial of Service threats** drive: Resource limits policies (OPA/Gatekeeper), Kubernetes ResourceQuota and LimitRange, rate limiting at API gateways, autoscaler configuration.

**Elevation of Privilege threats** drive: PodSecurity admission controller (restricted profile), Security Contexts (no root, no privilege escalation, drop ALL capabilities), Network Policies (default-deny-all), Falco runtime rules for privilege escalation detection.

When a security engineer can trace a CI/CD gate requirement back to a specific STRIDE threat in the threat model, the gate has a defensible justification. When an engineer asks "why do we have this OPA policy blocking privileged containers?", the answer is "it mitigates STRIDE Elevation of Privilege threat TM-047 in our API service threat model, documented in threat-model.json in the repo."

---

### SEGMENT 7 — Wrap-Up (20:30–22:00)

Threat modeling is the practice that ties all other DevSecOps controls together. STRIDE gives you a systematic framework for identifying threats across six categories. Data flow diagrams give you a visual representation of your system and its trust boundaries. OWASP Threat Dragon gives you a tool to document threats and their mitigations in a version-controlled file alongside your code.

The output of a threat model is not a document — it is a list of security requirements and the CI/CD controls that enforce them. When your pipeline has SAST, SCA, container scanning, OPA policies, and SIEM correlation, threat modeling explains why each control exists and what specific threat it is designed to prevent.

In the next module we cover Security Champions and DevSecOps Culture — how to scale security across an engineering organization by embedding security-minded engineers in development teams, building incentive programs, and measuring cultural change with DORA metrics.

See you there.

---

### PRODUCTION NOTES

- Screen share: OWASP Threat Dragon web app — draw a simple DFD for a CI/CD pipeline live
- Demo: Adding STRIDE threats to each component in Threat Dragon
- Slide: STRIDE table — six categories, violated properties, and CI/CD control mapping
- Slide: DFD element type diagram (process, data store, external entity, data flow, trust boundary)
- Demo: Exporting Threat Dragon model as JSON and committing to a Git repository
- Slide: Threat model output → CI/CD control traceability matrix
