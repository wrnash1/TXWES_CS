# Video Script: Module 08 — Vulnerability Management

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## SEGMENT 1 — Introduction: The Vulnerability Management Imperative (0:00–2:30)

Welcome back to CIS-4332. I'm Professor Nash. Today's module is Vulnerability Management — one of the most operationally critical disciplines in information security and a major domain on the CySA+ exam.

Here is the core challenge: attackers exploit vulnerabilities. Organizations have thousands of systems running thousands of software versions, each with its own vulnerability surface. New vulnerabilities are discovered and publicly disclosed every day. Without a systematic process for finding, prioritizing, and remediating vulnerabilities, organizations are perpetually behind.

Vulnerability management is not just running a scanner and generating reports. Done well, it is a continuous program: scan, analyze, prioritize based on real-world risk, remediate, verify, and repeat. The analyst who understands this program end-to-end — including how CVSS scores work, how to use the NVD and KEV catalog, and how to communicate prioritization to IT teams — is an asset to any security program.

By the end of this module you will understand how vulnerability scanners work, how to interpret CVSS v3.1 scores, how to prioritize vulnerabilities for remediation beyond just CVSS scores, how patch management integrates with vulnerability management, and how to use the key vulnerability databases that every analyst references daily.

Let's get into it.

---

## SEGMENT 2 — Vulnerability Scanning Fundamentals (2:30–7:00)

[SHOW TOOL: Nessus Essentials scan configuration interface — policy selection and target entry]

### What a Vulnerability Scanner Does

A vulnerability scanner probes systems in your environment and identifies known vulnerabilities, misconfigurations, and compliance gaps. It compares what it finds against a database of known vulnerability signatures and configuration benchmarks, then generates a report of findings with severity ratings.

Two primary approaches define how scanners operate:

### Unauthenticated Scanning

The scanner probes targets from a network perspective — port scanning, service fingerprinting, banner grabbing, version detection — without any credentials. It determines what services are running and what versions they report, then maps those versions against known vulnerability databases.

Unauthenticated scanning gives you the attacker's view: what does this target look like from outside? However, it misses significant categories of vulnerabilities:

- Local privilege escalation vulnerabilities that require access to the file system
- Patch level discrepancies where the version string has not changed but a patch was applied
- Application-layer vulnerabilities inside authenticated sessions
- Configuration issues invisible from the network

### Authenticated Scanning

The scanner is given credentials — a service account with local admin or SSH access. It logs into each target, directly reads installed software versions, patch levels, registry settings, and system configurations. Authenticated scanning is dramatically more accurate and complete.

The tradeoff: authenticated scanning requires credential management, a dedicated service account with appropriate permissions on every target, and careful handling of those credentials in the scanner's configuration.

[SHOW TOOL: Nessus scan results — vulnerability list with severity colors and CVSS scores displayed]

### Nessus

Tenable Nessus is the most widely deployed vulnerability scanner in enterprise environments. Key features:

- Pre-built scan policies for common use cases (basic network scan, credential patch audit, web application scan, compliance scan)
- Nessus Plugin system — detection signatures for individual vulnerabilities, updated daily
- Output formats: HTML reports, CSV exports, XML for integration with other tools
- Nessus Essentials — free version supporting up to 16 IPs for home lab and learning

### OpenVAS / Greenbone

OpenVAS (Open Vulnerability Assessment Scanner) is the leading open-source vulnerability scanner, maintained by Greenbone Networks. It uses the same underlying Network Vulnerability Tests (NVTs) format as the original Nessus. The Greenbone Community Edition is fully free. OpenVAS is commonly used in CTF environments and security training labs.

---

## SEGMENT 3 — CVSS Scoring (7:00–12:00)

[SHOW TOOL: NVD CVE detail page for a recent critical vulnerability — CVSS v3.1 vector and score displayed]

### What CVSS Is

The Common Vulnerability Scoring System, CVSS, is an open framework for communicating the characteristics and severity of software vulnerabilities. CySA+ tests CVSS extensively — you need to understand the scoring components, not just the final number.

CVSS v3.1 is the current version. It produces a score from 0.0 to 10.0 and a qualitative severity rating:

- 0.0 — None
- 0.1–3.9 — Low
- 4.0–6.9 — Medium
- 7.0–8.9 — High
- 9.0–10.0 — Critical

### CVSS v3.1 Metric Groups

CVSS v3.1 has three metric groups: Base, Temporal, and Environmental.

### Base Score Metrics

The Base Score reflects the intrinsic characteristics of a vulnerability — what it can do and how an attacker can exploit it, independent of any context. It has two sub-groups:

Exploitability Metrics:

- Attack Vector (AV): Network (N), Adjacent (A), Local (L), Physical (P). Network-based vulnerabilities are scored highest because an attacker anywhere on the internet can attempt exploitation.
- Attack Complexity (AC): Low (L) or High (H). Low complexity means exploitation is straightforward and repeatable.
- Privileges Required (PR): None (N), Low (L), High (H). Vulnerabilities requiring no privileges score higher.
- User Interaction (UI): None (N) or Required (R). No user interaction required scores higher.

Impact Metrics:

- Confidentiality Impact (C): None, Low, High
- Integrity Impact (I): None, Low, High
- Availability Impact (A): None, Low, High
- Scope (S): Unchanged (U) or Changed (C). A Changed scope means exploitation can impact components beyond the vulnerable component.

A classic critical vulnerability — like a remote code execution that requires no authentication, no user interaction, is network-accessible, and gives full system control — gets a CVSS v3.1 Base Score near 10.0. The vector string looks like: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`.

### Temporal Score

The Temporal Score adjusts the Base Score based on the current state of exploitation:

- Exploit Code Maturity (E): Proof of concept, functional exploit, wild exploitation
- Remediation Level (RL): Official fix, workaround, temporary fix, unavailable
- Report Confidence (RC): Confirmed, reasonable, unknown

If a functional public exploit exists and no official patch is available, the Temporal Score rises toward the Base Score. If the vulnerability has an official patch and no known exploitation, the Temporal Score may be lower.

### Environmental Score

The Environmental Score allows organizations to customize the score based on their specific environment:

- Modified Base Metrics: Re-weight any base metric based on your environment. If your network architecture means this vulnerability can only be reached from a specific internal subnet (not from the internet), you would lower the Attack Vector to Adjacent, reducing the score.
- Confidentiality, Integrity, Availability Requirements: Weight the impact components based on the criticality of the affected system in your environment.

[SHOW TOOL: CVSS v3.1 calculator at nvd.nist.gov/vuln-metrics/cvss/v3-calculator]

This is why a CVSS 9.8 vulnerability affecting a legacy system with no external access and no sensitive data may realistically be lower priority than a CVSS 7.5 vulnerability on an internet-facing server processing customer financial data. CVSS Base Score alone is not a sufficient prioritization input.

---

## SEGMENT 4 — Vulnerability Databases (12:00–14:30)

[SHOW TOOL: NVD search results for a recent CVE — full description, references, CVSS score, CPE applicability]

### National Vulnerability Database (NVD)

The NVD, maintained by NIST, is the authoritative US government repository for CVE data. Every publicly disclosed vulnerability receives a CVE identifier — Common Vulnerabilities and Exposures — from MITRE, and the NVD enriches that CVE with CVSS scores, affected software configurations using Common Platform Enumeration (CPE), and links to vendor advisories and patch information.

The NVD is the first stop for researching any specific vulnerability. It is free, authoritative, and searchable at nvd.nist.gov.

### CISA Known Exploited Vulnerabilities (KEV) Catalog

The CISA KEV catalog lists vulnerabilities that CISA has confirmed are being actively exploited in the wild. This is the single most important prioritization input available for free. A vulnerability in the KEV catalog demands immediate attention regardless of its CVSS score — if attackers are exploiting it today, your organization is at risk today.

CISA also mandates that all US federal civilian agencies patch KEV vulnerabilities within specific timeframes (typically 2 weeks for critical, 6 months for others). Private organizations should treat KEV listings as high-priority signals.

### CVE Database

The CVE list at cve.org (MITRE) is the primary identifier registry. CVE IDs follow the format CVE-YYYY-NNNNN. The CVE description provides the basic what — what product is vulnerable and what the vulnerability allows. The NVD enriches CVE data with CVSS scores and detailed analysis.

---

## SEGMENT 5 — Vulnerability Prioritization (14:30–17:30)

[SHOW TOOL: Risk-based prioritization matrix — CVSS score vs. asset criticality vs. exploitability]

CVSS alone is an inadequate prioritization framework. Here is why: an organization with 10,000 vulnerabilities and 80% scored "High" or "Critical" cannot patch everything at once. Prioritization requires additional context.

### Risk-Based Prioritization Factors

Asset criticality: A High vulnerability on a server processing payment card data is higher priority than the same vulnerability on a development sandbox with no sensitive data and no network connectivity.

Exploitability in the wild: Is there a public exploit? Is it in the CISA KEV catalog? Is it being used by threat actors documented in your threat intelligence? A CVSS 6.5 vulnerability with a working exploit in active use by a known threat actor targeting your sector is higher priority than a CVSS 9.8 with no known exploitation.

Exposure: Is the vulnerable system internet-facing? Can the vulnerability be reached from an untrusted network? Externally exposed systems with exploitable vulnerabilities are highest priority.

Compensating controls: Does a WAF, network segmentation, or IPS rule already partially mitigate the vulnerability? If so, the residual risk is lower.

### Prioritization Frameworks

SSVC (Stakeholder-Specific Vulnerability Categorization) is a decision-tree framework developed by CISA and Carnegie Mellon that goes beyond CVSS to assess whether exploitation is actively occurring, whether the system is mission-critical, and what the impact of exploitation would be.

EPSS (Exploit Prediction Scoring System) is a machine-learning model that predicts the probability a given CVE will be exploited in the wild within 30 days, based on characteristics of the vulnerability, historical exploitation patterns, and threat intelligence signals. EPSS scores complement CVSS — a vulnerability with a CVSS of 6.0 but an EPSS of 0.85 (85% probability of exploitation) may be higher priority than a CVSS 9.0 with an EPSS of 0.01.

---

## SEGMENT 6 — Remediation Workflows and Patch Management (17:30–21:00)

[SHOW TOOL: Vulnerability management workflow diagram — scan, triage, ticket, patch, verify, rescan]

Identifying vulnerabilities is only half the job. The remediation workflow determines whether findings actually get fixed.

### Remediation Options

Patching is the primary remediation — applying the vendor-provided fix. The patch management process must integrate with vulnerability management to ensure that findings generate tickets, tickets get assigned to system owners, patches get tested in non-production, and production patches are verified.

Workaround or configuration change is appropriate when a patch is not yet available. Disabling a vulnerable service, restricting access via firewall rules, or changing a configuration setting can reduce risk while waiting for an official fix.

Acceptance is appropriate when the risk is low enough and the remediation cost is high enough that the organization formally accepts the residual risk. This should be documented with a risk acceptance record signed by an appropriate authority.

### Patch Management Integration

Patch management and vulnerability management must work in coordination:

1. Vulnerability scanner identifies CVE-XXXX-YYYY on 47 Windows servers
2. Finding is exported to the vulnerability management platform or ticketing system
3. System owner is assigned the ticket with the CVE reference, CVSS score, KEV status, and remediation deadline
4. Patch is tested in the patch testing environment
5. Patch is deployed in production during the next maintenance window
6. Vulnerability scanner re-scans the affected hosts to verify remediation
7. Ticket is closed upon confirmed remediation

### SLA Targets by Severity

| Severity | CVSS Range | Typical Remediation SLA |
|---|---|---|
| Critical | 9.0–10.0 | 15 days (or 7 days if in KEV) |
| High | 7.0–8.9 | 30 days |
| Medium | 4.0–6.9 | 60–90 days |
| Low | 0.1–3.9 | 180 days or acceptance |

---

## SEGMENT 7 — Wrap-Up and CySA+ Alignment (21:00–24:00)

For the CySA+ exam, focus on these key topics from today.

Scanning types: authenticated vs. unauthenticated. Know the tradeoffs — authenticated gives more complete results; unauthenticated gives the attacker's perspective.

CVSS v3.1: Understand all Base Score metrics — Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, and the three Impact metrics. Know the five qualitative severity levels and their score ranges.

Prioritization: CVSS alone is insufficient. Add asset criticality, exploitability in the wild (KEV catalog), EPSS scores, and exposure context.

NVD and CVE: The NVD is the authoritative source for CVE information including CVSS scores and patch references. The CISA KEV catalog lists actively exploited vulnerabilities — KEV status elevates priority.

Remediation options: patch, workaround, configuration change, acceptance. Know when each is appropriate.

Patch management integration: scan, ticket, patch, rescan, verify.

In the lab this week you will analyze a set of Nessus scan findings and apply risk-based prioritization to produce a prioritized remediation list. You will also research two CVEs using the NVD.

Next module: Application Security Analysis.

See you there.

---

End of Module 08 Video Script

Total estimated runtime: 22–24 minutes
