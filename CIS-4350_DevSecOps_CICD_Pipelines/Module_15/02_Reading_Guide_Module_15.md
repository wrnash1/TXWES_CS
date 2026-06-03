# Reading Guide: Module 15 — Security Champions and DevSecOps Culture

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 15 addresses the organizational and cultural foundation that makes every technical DevSecOps control sustainable. A pipeline with SAST, SCA, container scanning, and OPA policies is only effective if engineers understand why the controls exist, respond to findings quickly, and have the authority to act on security concerns. This module covers Security Champion programs, developer security training (SANS and OWASP), gamification and engagement strategies, DORA metrics extended with security KPIs, DevSecOps maturity models (OWASP SAMM and DSOMM), and the organizational transformation patterns that distinguish sustainable DevSecOps programs from short-lived tool adoption projects.

---

## Section 1: High-Yield Glossary

**Security Champion** — An engineer embedded in a development team who serves as a security liaison between the team and the central security organization. Champions are not security professionals — they are developers with security interest and training who conduct first-level security reviews, triage pipeline findings, and represent security concerns in sprint planning. OWASP recommends one champion per eight to ten engineers.

**Security Champion program** — A formal organizational initiative that identifies, trains, and empowers Security Champions across development teams. A mature program includes a defined selection process, structured training curriculum, formal authority (Champions as required reviewers on security-sensitive PRs), a champion community (weekly sync, shared threat intelligence), and career recognition.

**OWASP Top 10** — The Open Web Application Security Project's ranked list of the ten most critical web application security risks (current version: 2021). Categories include Broken Access Control (A01), Cryptographic Failures (A02), Injection (A03), Insecure Design (A04), Security Misconfiguration (A05), Vulnerable and Outdated Components (A06), Identification and Authentication Failures (A07), Software and Data Integrity Failures (A08), Security Logging and Monitoring Failures (A09), and Server-Side Request Forgery (A10).

**OWASP ASVS (Application Security Verification Standard)** — A framework of security requirements for web applications organized into three verification levels. Level 1 is minimum security for all applications. Level 2 is for applications handling sensitive data. Level 3 is for high-assurance applications. ASVS requirements map directly to specific security controls in a CI/CD pipeline.

**SANS Secure Development training** — SANS Institute courses covering application security, cloud security, and DevSecOps for practitioners. Exam-relevant courses: DEV541 (Secure DevOps and Cloud Application Security), SEC522 (Application Security: Securing Web Apps, APIs, and Microservices), SEC542 (Web Application Penetration Testing).

**Just-in-time security training** — Security education delivered contextually within the developer workflow — for example, a SAST tool that annotates a finding with an explanation of the vulnerability class and a link to the relevant OWASP cheat sheet. More effective than scheduled training because it is directly tied to a real finding in the engineer's own code.

**Gamification** — The application of game design elements (points, leaderboards, challenges, achievements, rewards) to non-game activities to increase engagement and motivation. In DevSecOps, gamification is applied to security training, vulnerability remediation, and champion program participation.

**Capture the Flag (CTF)** — A security challenge format where participants find and exploit vulnerabilities in deliberately vulnerable systems to capture hidden flags. CTFs are effective for hands-on security skills development. Platforms include HackTheBox, TryHackMe, and OWASP WebGoat.

**DORA metrics** — The four software delivery performance metrics defined by the DevOps Research and Assessment organization: Deployment Frequency, Lead Time for Changes, Change Failure Rate, and Mean Time to Recovery. These metrics measure delivery throughput and stability and are the industry standard for benchmarking DevOps programs.

**Deployment Frequency** — How often an organization deploys code to production. Elite performers: multiple times per day. High performers: once per day to once per week.

**Lead Time for Changes** — The time from a code commit being merged to that commit running in production. Elite performers: less than one hour. High performers: one day to one week.

**Change Failure Rate** — The percentage of deployments to production that result in degraded service requiring remediation. Elite performers: under 5%. High performers: 5–10%.

**Mean Time to Recovery (MTTR)** — The time to restore service after a production failure. Elite performers: under one hour. High performers: under one day.

**Mean Time to Detect (MTTD)** — A security-specific metric measuring the average time between a vulnerability being introduced into the codebase and its detection by a security control. Reduced by earlier pipeline placement of security scans (shift left).

**Critical Finding Escape Rate** — The percentage of critical-severity security findings that reach production without being caught by the pipeline or by manual review. A non-zero escape rate indicates a gap in the pipeline or in override governance.

**Security Gate Pass Rate** — The percentage of CI/CD pipeline runs that pass all mandatory security gates without a human override decision. Low pass rates indicate either noisy gates (high false positive rate) or genuine security debt in the codebase.

**OWASP SAMM (Software Assurance Maturity Model)** — An open-source framework for assessing and improving a software security program. SAMM defines five business functions (Governance, Design, Implementation, Verification, Operations) with three practices each and three maturity levels per practice. Provides assessment tools that produce a scored maturity profile.

**DSOMM (DevSecOps Maturity Model)** — An OWASP project defining maturity levels specifically for DevSecOps pipeline practices. Four levels across dimensions including Build, Deploy, Test, Monitor, and Culture. Level 1 is basic awareness; Level 4 is continuous improvement with automated measurement.

**Security theater** — The appearance of security controls without substantive security benefit. Examples: warn-only security gates that never block deployments; override approvals rubber-stamped without review; compliance checklists completed without validating underlying controls. Security theater provides false assurance and increases organizational risk.

**DevSecOps transformation** — The organizational change process of integrating security practices, responsibilities, and culture into an existing software delivery organization. Distinguished from tool adoption by its focus on process change, cultural change, and structural changes to team responsibilities.

---

## Section 2: Security Champion Program Design Reference

### Champion Selection Criteria

| Criteria | Description |
|---|---|
| Security interest | Voluntarily raises security concerns in code review |
| Technical credibility | Respected by peers as a competent engineer |
| Communication skills | Able to explain security concepts to non-security engineers |
| Time availability | Can dedicate 20–25% of sprint capacity to champion activities |
| Management support | Team lead supports the role and protects champion time |

### Champion Responsibilities by Sprint Phase

| Phase | Champion Activity |
|---|---|
| Sprint planning | Review planned features for security requirements; flag new trust boundaries or data types |
| Development | Available for security questions; review security-sensitive PRs |
| Pipeline findings | Triage SAST/SCA/container scan findings; assign remediation tickets |
| Sprint review | Report security metrics for the sprint; escalate unresolved findings |
| Champion sync | Share team findings and threat intelligence with the champion network |

---

## Section 3: DORA Metrics and Security KPI Reference

### DORA Performance Bands

| Metric | Elite | High | Medium | Low |
|---|---|---|---|---|
| Deployment Frequency | Multiple/day | Daily–weekly | Weekly–monthly | Monthly+ |
| Lead Time for Changes | < 1 hour | 1 day–1 week | 1 week–1 month | > 1 month |
| Change Failure Rate | < 5% | 5–10% | 10–15% | > 15% |
| MTTR | < 1 hour | < 1 day | 1 day–1 week | > 1 week |

### Security KPIs Layered on DORA

| KPI | Definition | Target |
|---|---|---|
| MTTD | Time from vulnerability introduction to detection | < 24 hours (pipeline) |
| MTTR-Security | Time from detection to validated fix in production | Critical: < 24h; High: < 7d |
| Critical Escape Rate | Critical findings reaching production | 0% |
| Gate Pass Rate | Pipeline runs passing all security gates without override | > 95% |
| Override Approval Rate | Overrides with documented approval | 100% |
| Champion Training Currency | Champions with current certification | 100% |

---

## Section 4: OWASP SAMM Practice Areas for DevSecOps

### Implementation Function — Secure Build Practice

| Level | Requirements |
|---|---|
| Level 1 | SAST and SCA tools exist; findings are visible to teams |
| Level 2 | Mandatory gates block critical findings; remediation tracked with SLAs |
| Level 3 | All findings tracked to closure; security debt managed as engineering metric |

### Implementation Function — Secure Deployment Practice

| Level | Requirements |
|---|---|
| Level 1 | Deployment process documented; some manual security checks |
| Level 2 | Pipeline-enforced deployment controls; image signing; secrets in vault |
| Level 3 | Fully automated deployment security; deployment verification gates |

### Verification Function — Security Testing Practice

| Level | Requirements |
|---|---|
| Level 1 | Periodic manual penetration testing |
| Level 2 | DAST integrated in staging pipeline; automated security regression tests |
| Level 3 | Continuous security testing; fuzz testing; security test coverage metrics |

---

## Section 5: DSOMM Four-Level Reference

### Level 1 — Basic Understanding

- SAST tool deployed but findings not mandatory
- No formal Security Champion program
- Security training is optional or ad hoc
- No security-specific metrics tracked

### Level 2 — Basic Adoption

- Mandatory SAST and SCA gates for critical findings
- Security Champions identified per team; informal training
- Basic security KPIs tracked (MTTD, MTTR)
- Incident response process documented

### Level 3 — High Adoption

- Full pipeline security gate suite (SAST, SCA, container, secrets, IaC)
- Formal Security Champion program with training and community
- DORA and security KPIs reviewed in engineering leadership meetings
- SAMM/DSOMM assessment conducted annually; roadmap maintained

### Level 4 — Continuous Improvement

- Security pipeline coverage metrics automated and integrated into engineering dashboards
- Champion program includes certification track and career impact
- Maturity assessments drive quarterly OKRs
- Security improvement metrics (escape rate trending to zero, MTTD trending down) are leadership-level KPIs

---

## Section 6: Three Transformation Failure Modes

### Failure Mode 1 — Security as Bottleneck

**Symptom:** Security team owns all finding triage and remediation decisions; development teams wait for security approval.

**Root cause:** Centralized security responsibility model that does not scale.

**Fix:** Push first-level triage to Security Champions; establish team-owned remediation SLAs; security team owns policy and tooling, not individual findings.

### Failure Mode 2 — Tool Accumulation Without Process

**Symptom:** Multiple security tools deployed but finding backlogs growing; unclear ownership of findings; teams uncertain what response is required.

**Root cause:** Tool deployment without process design.

**Fix:** For each tool, define who reviews findings, what the remediation SLA is by severity, what the escalation path is for unresolved critical findings, and how overrides are approved and documented.

### Failure Mode 3 — Security Theater

**Symptom:** Security gates set to warn-only; override process is a rubber stamp; compliance reports show green while critical findings remain open.

**Root cause:** Leadership pressure for delivery velocity without accountability for security quality.

**Fix:** Define an override governance policy with required approval chain; track override usage as a metric; make gate bypass rate visible to engineering leadership.

---

## Section 7: Practice Questions

**1.** A DevSecOps program has deployed SAST, SCA, and container scanning across all pipelines, but the finding backlog has grown to 4,000 open items over six months. No critical findings have been remediated in the past 30 days. Which transformation failure mode does this best represent, and what is the highest-priority corrective action?

**2.** A DSOMM assessment places a team at Level 1 for Culture. Which two actions would most directly advance the team to Level 2? Options: deploy a SAST tool; identify Security Champions and provide structured training; set all security gates to block-on-critical; conduct an annual penetration test.

**3.** An organization wants to demonstrate DevSecOps program value to the CISO. Which combination of DORA and security KPI metrics provides the most complete picture of both delivery performance and security effectiveness?

**4.** A Security Champion reports that the SAST gate is generating 200 false positives per week, causing engineers to ignore all findings. What corrective action should the Champion take, and which security KPI will improve as a result?

**5.** During sprint planning, a developer proposes adding a new third-party OAuth integration. At what point should the Security Champion engage with this feature, and what artifact should the Champion produce before the feature is implemented?

---

## Exam-Focus Summary

- **DSOE exam topics from this module**: Security Champion program design and rationale, SANS and OWASP training resources, DORA four metrics and elite performer benchmarks, security KPIs (MTTD, MTTR, escape rate, gate pass rate), OWASP SAMM five business functions, DSOMM four levels, three transformation failure modes.
- **High-frequency question patterns**: Champion-to-engineer ratio, which DORA metric is most directly improved by security gate automation, SAMM practice area for CI/CD security, DSOMM level for a described program state.
- **Cross-module connections**: Security Champion authority connects to pipeline governance from Module 3; DORA metrics connect to change failure rate impacted by security incidents from Module 12; SAMM Verification practices connect to DAST from Module 9 and compliance from Module 13.
