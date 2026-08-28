# Reading Guide: Module 14 — Threat Modeling in DevSecOps

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4350 &BULL; DEVSECOPS & CI/CD SECURITY AUTOMATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 14 covers threat modeling — the design-phase security activity that systematically identifies what can go wrong in a system before code is written. In a DevSecOps program, threat modeling is the upstream input that determines which pipeline controls to build, which security tests to write, and which parts of the system require the most attention during code review. This module covers the STRIDE framework, data flow diagrams, trust boundaries, OWASP Threat Dragon, and sprint-cadence threat modeling integration.

---

## Section 1: High-Yield Glossary

**Threat modeling** — A structured process for identifying security threats to a system at the design phase, before code is written. The outputs are a prioritized threat list and a set of mitigations that inform security requirements, pipeline gates, and test cases.

**STRIDE** — Microsoft's threat classification framework: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege. Each category represents a class of attack with a corresponding mitigation strategy.

**Spoofing** — Impersonating a legitimate user, service, or component. Mitigation: strong authentication, token signature verification, mutual TLS.

**Tampering** — Unauthorized modification of data in transit or at rest. Mitigation: TLS for data in transit, HMAC message signing, input validation, database integrity checks.

**Repudiation** — Denying that an action was performed. Mitigation: immutable audit logging, signed audit events, centralized log storage.

**Information Disclosure** — Exposing data to unauthorized parties. Mitigation: structured error responses, secrets management, data classification, TLS.

**Denial of Service** — Disrupting system availability. Mitigation: rate limiting, authentication at the edge, container resource limits, circuit breakers.

**Elevation of Privilege** — Gaining capabilities beyond what was authorized. Mitigation: `runAsNonRoot: true`, `allowPrivilegeEscalation: false`, principle of least privilege, RBAC.

**Data Flow Diagram (DFD)** — A structured diagram showing external entities, processes, data stores, data flows, and trust boundaries in a system. The primary artifact used in threat modeling.

**External entity** — An actor or system outside the trust boundary (user, third-party API, partner service). Drawn as a rectangle in a DFD.

**Process** — A component that transforms, stores, or transmits data (application, API gateway, worker service). Drawn as a circle in a DFD.

**Data store** — Persistent storage (database, cache, message queue, object storage). Drawn as parallel lines in a DFD.

**Data flow** — An arrow in a DFD showing how data moves between components, labeled with the data type and protocol.

**Trust boundary** — A line in a DFD delineating where data crosses from a trusted context to a less trusted one. Most attacks happen at trust boundary crossings. STRIDE threats are evaluated at each crossing.

**OWASP Threat Dragon** — A free, open-source threat modeling tool that provides a DFD diagramming interface and auto-suggests STRIDE threats based on component types and trust boundary crossings. Outputs a JSON threat model file that can be version-controlled.

**Threat actor** — An entity with motivation and capability to attack a system. Common categories: external adversary, malicious insider, automated scanner.

**Attack surface** — The set of all possible attack entry points into a system. Threat modeling systematically identifies and documents the attack surface.

**Mitigation** — A control that reduces the likelihood or impact of a threat. Mitigations map to specific DevSecOps pipeline controls (SAST, SCA, container scanning, secrets management, Kubernetes security).

**Sprint-cadence threat modeling** — A lightweight threat modeling process triggered by specific conditions (new trust boundary, new data type, new external integration) at feature design time, not on an annual schedule.

---

## Section 2: STRIDE Framework Reference

| Category | Threat | Example | Mitigation |
|---|---|---|---|
| Spoofing | False identity | Forged JWT token for admin access | Authentication, JWT signature verification, short token expiry |
| Tampering | Unauthorized data modification | MITM attack on microservice API call | TLS, HMAC signing, input validation |
| Repudiation | Denying actions | User deletes audit logs | Immutable logging, signed events, write-only log access |
| Information Disclosure | Data leakage | API returns stack traces with DB credentials | Structured errors, secrets management, data classification |
| Denial of Service | Availability attack | Unauthenticated endpoint flooded with requests | Rate limiting, auth at edge, container resource limits |
| Elevation of Privilege | Unauthorized capability gain | Container escape via root process | `runAsNonRoot`, `allowPrivilegeEscalation: false`, RBAC |

---

## Section 3: Data Flow Diagram Symbol Reference

| Symbol | Shape | Represents |
|---|---|---|
| External entity | Rectangle | Actor outside trust boundary |
| Process | Circle | Application component |
| Data store | Parallel lines | Persistent storage |
| Data flow | Arrow | Data movement (labeled with data type) |
| Trust boundary | Dashed line | Where trust level changes |

---

## Section 4: STRIDE-to-Pipeline-Control Mapping

| STRIDE Category | DevSecOps Pipeline Control | Module Reference |
|---|---|---|
| Spoofing | Secrets management (Vault/AWS Secrets Manager), OIDC federation | Module 9 |
| Tampering | SAST (code review for validation logic), TLS enforcement tests | Module 7 |
| Repudiation | Immutable audit logging, SIEM event retention | Module 12 |
| Information Disclosure | Secrets scanning (Gitleaks), SCA (dependency CVEs) | Modules 8, 9 |
| Denial of Service | Container resource limits (Checkov CKV_K8S_11-14), rate limit tests | Module 12 |
| Elevation of Privilege | Security Context checks (Checkov CKV_K8S_15, 20), container scanning | Modules 11, 12 |

---

## Section 5: Threat Modeling Sprint Cadence Trigger Conditions

| Trigger | Example |
|---|---|
| New external-facing endpoint | Adding a public REST API for a new partner |
| New trust boundary | Microservice added that crosses namespace boundary |
| New elevated-sensitivity data type | Feature stores credit card numbers or SSNs |
| Authentication or authorization logic changed | Adding a new OAuth scope or RBAC role |
| New infrastructure component | New message queue, cache, or object storage bucket added |
| Integration with third-party API | Using a new payment processor or identity provider |

---

## Section 6: Threat Modeling Process Steps

1. **Scope** — Define what is in scope (the feature or system being modeled) and the threat actors to consider.
2. **Diagram** — Create a DFD showing all components, data flows, and trust boundaries.
3. **Identify threats** — For each data flow that crosses a trust boundary, enumerate applicable STRIDE threats.
4. **Prioritize** — Rank threats by likelihood and impact. Use the DREAD model or CVSS scores as a framework.
5. **Mitigate** — For each high-priority threat, identify the control that mitigates it.
6. **Verify** — Map each mitigation to a specific test case, pipeline gate, or acceptance criterion.
7. **Document** — Record the threat model in a versioned artifact (Threat Dragon JSON, ADR, or structured doc).

---

## Section 7: OWASP Threat Dragon Workflow

1. Create a new threat model project.
2. Add DFD components (processes, data stores, external entities) using the library.
3. Draw data flows between components.
4. Draw trust boundaries around components with different trust levels.
5. Threat Dragon auto-populates suggested threats for each component and data flow.
6. Review each threat: mark as mitigated, accepted, or not applicable.
7. For mitigated threats: record the mitigation control.
8. Export the JSON threat model file and commit it to the repository.

---

## Section 8: DevSecOps Professional Exam Tips

1. **STRIDE categories** — Know all six by memory. The exam tests both the threat type and the corresponding mitigation category. A common question pattern: given a scenario, identify which STRIDE category it represents.

2. **Trust boundaries are the focal point** — STRIDE threats are evaluated at trust boundary crossings, not at every component. The key skill is identifying trust boundaries in a system description and applying STRIDE analysis at each.

3. **Threat modeling placement in SDLC** — Threat modeling belongs at the design phase, before code is written. It is the first security activity in the pipeline. The order is: threat modeling, then SAST, then SCA, then container scanning, then IaC scanning, then runtime security.

4. **STRIDE mitigations map to pipeline controls** — Know the mapping table in Section 4. The exam tests whether you can connect a STRIDE threat to the DevSecOps tool that mitigates it.

5. **Repudiation mitigation** — The unique STRIDE category. Repudiation is mitigated by immutable audit logging, not by authentication or encryption. Know this distinction.

6. **OWASP Threat Dragon** — Know that it is a free tool that produces DFDs with STRIDE threat annotations. It outputs a JSON file that can be version-controlled. It does not scan code or run in a CI pipeline.

7. **Sprint cadence vs. annual review** — The DevSecOps approach is to threat model at feature design time (triggered by new trust boundaries), not on an annual compliance schedule. Annual threat model reviews supplement but do not replace sprint-cadence modeling.

8. **Defense in depth relationship** — Threat modeling identifies which security controls are needed. The subsequent modules' tools (SAST, SCA, etc.) implement those controls. A threat model that identifies an elevation of privilege risk should result in Checkov CKV_K8S_20 being required in the pipeline.

---

## Section 9: Required Reading

- Review the OWASP Threat Dragon documentation at [https://owasp.org/www-project-threat-dragon/](https://owasp.org/www-project-threat-dragon/).

---

## Section 10: Study Checklist

- [ ] Name all six STRIDE threat categories and the primary mitigation for each.
- [ ] Explain the four DFD symbol types (external entity, process, data store, data flow) and trust boundary.
- [ ] Explain why trust boundaries are the focal point for STRIDE threat analysis.
- [ ] Map each STRIDE category to at least one DevSecOps pipeline control.
- [ ] Describe the sprint-cadence threat modeling process and five trigger conditions.
- [ ] Describe the OWASP Threat Dragon workflow and what artifact it produces.
- [ ] Explain where threat modeling belongs in the SDLC relative to SAST and SCA.
- [ ] Complete the Module 14 lab activity.
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.

---

## 9. Supplemental Resources

**1. [OWASP Threat Dragon documentation](https://owasp.org/www-project-threat-dragon/)**
The official OWASP Threat Dragon project page and documentation, covering installation (desktop app and web application modes), DFD symbol types, STRIDE threat annotation, JSON export format, and integration with DevSecOps workflows. Includes tutorial walkthroughs and example threat models.

**2. [Microsoft STRIDE threat modeling framework — Security Development Lifecycle](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)**
Microsoft's authoritative documentation of the STRIDE framework and the Microsoft Threat Modeling Tool. Covers each STRIDE category with examples, the relationship between STRIDE categories and violated security properties, and how to apply STRIDE systematically to data flow diagrams. The foundational reference for STRIDE as used in the DSOE certification.

**3. [OWASP Application Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)**
The OWASP cheat sheet covering threat modeling process steps, DFD construction guidelines, trust boundary identification, STRIDE and PASTA framework comparison, risk rating methodologies (DREAD, CVSS), and integration of threat modeling into Agile sprints. Includes decision trees for when to threat model and how to scope a threat modeling session.

---

Reading Guide — Module 14 | CIS-4350 | Texas Wesleyan University | Professor Nash
