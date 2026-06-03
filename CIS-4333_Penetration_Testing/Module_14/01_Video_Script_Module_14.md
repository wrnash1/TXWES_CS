# Video Script: Module 14 — Penetration Testing Reports

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4333. I am Professor Nash, and today we are tackling one of the most
professionally consequential topics in the entire course: the penetration testing report.

Here is a truth that surprises many new pentesters: the report IS the deliverable. You can
compromise every system on the network, obtain domain administrator credentials, and exfiltrate
simulated sensitive data — but if you cannot communicate what you found, why it matters, and
what the client should do about it, the engagement has largely failed. The client hired you to
reduce risk, and risk reduction requires action, and action requires communication.

By the end of this module you will be able to distinguish report types and match them to the
right audience, score and rate findings using CVSS, write professional-quality findings with
all required components, structure a complete report, handle sensitive data appropriately, and
prepare for a client debriefing.

Let us begin.

---

## SEGMENT 2 — Report Types and Audiences (1:30–5:00)

A mature penetration test produces at least two distinct report documents aimed at two very
different audiences.

### The Executive Summary

The executive summary is written for business leadership: the CISO, the CIO, the board, legal
counsel, and in some cases risk officers and auditors. These readers are not reading to
understand how SQL injection works. They are reading to understand business risk and to make
resource decisions.

An executive summary typically runs two to four pages and includes:

- The engagement scope and dates in plain language
- A top-level risk rating for the organization (Critical / High / Medium / Low)
- A brief narrative of the most significant findings
- A prioritized remediation roadmap
- An attestation statement — a signed declaration that the findings are accurate and the
  engagement was conducted according to the agreed scope

The tone is professional, non-technical, and action-oriented. Avoid jargon. When you must
reference a technical concept, define it briefly in parentheses.

### The Technical Report

The technical report is written for the security team, system administrators, and developers
who will actually perform remediation. It is detailed, evidence-rich, and reproducible. A
skilled security engineer reading your technical report should be able to independently verify
your findings by following your steps.

The technical report contains:

- Methodology overview
- Detailed finding entries (covered in Segment 4)
- Tool outputs, screenshots, and raw evidence
- Appendices with full scan results, password crack statistics, and network diagrams

### Supplemental Deliverables

Many engagements also produce supplemental documents:

- **Remediation guidance document** — a standalone action plan referencing the technical
  findings with owner assignments and timelines
- **Scope verification document** — confirms that only authorized targets were tested
- **Rules of engagement summary** — documents what was and was not permitted

For the PenTest+ exam, remember that report types are matched to audiences. Executive audiences
receive high-level business-risk summaries. Technical audiences receive detailed findings with
reproduction steps.

---

## SEGMENT 3 — CVSS Scoring and Risk Rating (5:00–9:00)

Before we can write a finding, we need to understand how to score its severity. The industry
standard is the Common Vulnerability Scoring System, version 3.1, abbreviated CVSS.

### CVSS Base Score Components

CVSS uses three metric groups. For the PenTest+ exam, the Base Score is the most important.

The Base Score is calculated from eight metrics divided into two sub-groups.

**Exploitability Metrics:**

- **Attack Vector (AV)** — How is the vulnerability exploited? Network (N), Adjacent (A),
  Local (L), or Physical (P). Network is worst because anyone on the internet can attack it.
- **Attack Complexity (AC)** — How hard is exploitation? Low (L) or High (H).
- **Privileges Required (PR)** — What access does the attacker need before exploiting? None
  (N), Low (L), or High (H).
- **User Interaction (UI)** — Does a victim need to do something? None (N) or Required (R).

**Impact Metrics:**

- **Confidentiality Impact (C)** — None / Low / High
- **Integrity Impact (I)** — None / Low / High
- **Availability Impact (A)** — None / Low / High
- **Scope (S)** — Unchanged or Changed. Changed means the vulnerability can affect resources
  beyond its authorization scope — for example, a guest VM escaping to the hypervisor.

The resulting score is a decimal from 0.0 to 10.0, mapped to severity ratings:

| Score Range | Severity |
|-------------|----------|
| 9.0–10.0 | Critical |
| 7.0–8.9 | High |
| 4.0–6.9 | Medium |
| 0.1–3.9 | Low |
| 0.0 | None / Informational |

### Temporal and Environmental Scores

CVSS also supports Temporal metrics (exploit code maturity, remediation level, report
confidence) and Environmental metrics (modified base metrics and confidentiality/integrity/
availability requirements specific to the organization). For client reports, document the
Base Score at minimum. Including Environmental scores when you know the client's asset
criticality adds significant value.

### Practical Scoring Example

Consider MS17-010 (EternalBlue), the vulnerability exploited by WannaCry. Its CVSS 3.1 Base
Score is 9.8 — Critical. Why?

- AV: Network (remote, no adjacency required)
- AC: Low (no special conditions)
- PR: None (unauthenticated)
- UI: None (victim does not interact)
- S: Unchanged
- C/I/A: High / High / High

That combination produces a near-maximum score. An unpatched SMB host exposed to the internet
is genuinely catastrophic.

### Risk Rating Beyond CVSS

CVSS measures severity, not business risk. You adjust risk rating based on:

- **Asset criticality** — A critical finding on a development sandbox is lower business risk
  than the same finding on a production payment server
- **Threat context** — Is this vulnerability actively exploited in the wild?
- **Compensating controls** — Is the host protected by a WAF, network segmentation, or EDR
  that reduces effective exploitability?

Document these factors explicitly in your finding when they cause your reported risk to differ
from the raw CVSS score.

---

## SEGMENT 4 — Writing Quality Findings (9:00–14:00)

The finding is the atomic unit of a penetration test report. Each vulnerability you confirm
and decide to report gets its own finding entry. A professional finding has six required
components.

### Component 1: Title

The title should be specific, informative, and searchable. Poor titles include "SQL Injection
Found" or "Weak Authentication." Strong titles include:

- "Unauthenticated SQL Injection in Login Form Allows Database Extraction (CVE-2023-XXXX)"
- "Default Credentials on VMware ESXi 7.0 Host (10.10.1.50) Grant Full Hypervisor Control"

The title tells the reader what was found, where, and how serious it is — before they read
a single body word.

### Component 2: Description

The description explains the vulnerability in technical terms. A good description answers:

- What is the vulnerability class?
- How does it manifest in this specific system?
- What is the root cause?

Keep descriptions to three to five sentences for most findings. Reference CVE numbers and CWE
identifiers where applicable. For example: "The application fails to parameterize SQL queries
in the authentication endpoint (CWE-89). User-supplied input in the `username` field is
concatenated directly into a database query, allowing an attacker to manipulate query logic."

### Component 3: Evidence

Evidence is proof. It makes your finding verifiable and protects you legally. Evidence should
include:

- Screenshots with timestamps
- Tool output snippets (sqlmap output, nmap scan results, Burp Suite requests/responses)
- Specific file paths, registry keys, version strings, or configuration excerpts that
  confirm the vulnerability
- Your IP address visible in screenshots to confirm you performed the test from an authorized
  host

Never fabricate or manipulate evidence. Chain of custody for evidence is addressed in Module 15.

### Component 4: Impact

The impact section answers "so what?" in business terms. Connect the technical vulnerability
to its business consequence. Examples:

- "An unauthenticated attacker could extract the full customer database, resulting in
  regulatory exposure under GDPR and PCI-DSS and potential financial penalties."
- "Full hypervisor control allows an attacker to shut down all virtual machines, resulting
  in a complete service outage for all hosted applications."

Quantify where possible. Vague impact statements like "could lead to data exposure" add no
value to a decision-maker.

### Component 5: CVSS Score and Risk Rating

Include the CVSS vector string and base score, plus your reported risk rating. If you adjusted
the rating from the raw CVSS score, explain why. For example:

```
CVSS 3.1 Base Score: 9.8 (Critical)
Vector: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
Reported Risk: High (adjusted from Critical — host is isolated from internet by perimeter
firewall; not externally reachable at time of testing)
```

### Component 6: Remediation

The remediation section tells the client exactly how to fix the vulnerability. It should be:

- **Specific**: "Apply Microsoft patch KB5014692" not "Update your software"
- **Actionable**: Provide configuration steps or code changes where practical
- **Prioritized**: Distinguish immediate mitigations from permanent fixes
- **Referenced**: Link to vendor advisories, CIS benchmarks, OWASP guidance, or NIST SP 800
  controls

For complex fixes, provide a short-term workaround and a long-term solution.

---

## SEGMENT 5 — Report Structure and Professional Formatting (14:00–17:00)

A complete penetration test report follows a consistent structure that allows clients,
auditors, and future security teams to navigate it efficiently.

### Standard Report Structure

1. **Cover Page** — Client name, engagement name, date, classification (CONFIDENTIAL), and
   your firm's name
2. **Table of Contents** — With page numbers; essential for reports exceeding 20 pages
3. **Executive Summary** — Risk overview, narrative, top findings summary, remediation roadmap
4. **Methodology** — Testing phases followed, standards referenced (PTES, OWASP, NIST)
5. **Scope and Limitations** — Exact IP ranges, domains, applications in scope; exclusions
6. **Findings Summary Table** — All findings with title, affected asset, risk rating
7. **Detailed Findings** — One section per finding, all six components present
8. **Appendices** — Full scan outputs, password analysis statistics, network diagrams

### Formatting Standards

Use consistent heading hierarchy. Number findings sequentially (FIND-001, FIND-002) for easy
reference. Use syntax-highlighted code blocks for commands and tool output. Redact portions
of sensitive data in screenshots — show enough to prove the finding, not enough to enable
independent exploitation of the client's live systems after the report is shared.

### Classification and Handling

Mark every page header and footer with the classification level. Most pentest reports are
classified CONFIDENTIAL or RESTRICTED. Include a handling statement on the cover page:

> This document contains sensitive security information. Distribution is restricted to
> authorized personnel only. Unauthorized disclosure may violate contractual and legal
> obligations.

---

## SEGMENT 6 — Sensitive Data Handling and Attestation (17:00–19:30)

### Handling Sensitive Data in Reports

During the engagement you may obtain: plaintext credentials, PII from exfiltrated files,
financial records, protected health information, or proprietary source code. How you handle
this data matters legally and ethically.

Rules for sensitive data in reports:

- **Do not reproduce full credential dumps** — show five to ten representative hashes or
  partial passwords to prove the finding; do not paste thousands of credentials
- **Redact PII** — if you exfiltrated a file containing Social Security numbers, show
  the filename and column headers, then redact actual values with `XXX-XX-XXXX` substitution
- **Do not retain client data post-engagement** — your agreement should specify a data
  retention and destruction policy; follow it exactly
- **Encrypt the report in transit** — deliver via encrypted email (PGP/GPG) or a secure
  portal, never unencrypted email or unprotected cloud storage

### Attestation

An attestation is a formal statement affirming the accuracy and completeness of the report
and the scope of the engagement. It is typically signed by the lead tester and a company
officer. The attestation protects both parties: the client can show auditors that a qualified
professional conducted the assessment, and you document that your work was authorized.

A standard attestation includes:

- Statement that testing was conducted according to agreed scope and rules of engagement
- Dates of active testing
- A declaration that findings represent the state of the environment at time of testing
- Signature lines for the lead tester and, where required, a client representative

### Non-Disclosure Requirements

Most engagements are governed by a non-disclosure agreement signed before work begins. Your
NDA obligations survive the engagement — you cannot discuss client vulnerabilities,
methodologies, or results publicly without explicit written authorization. This applies to
conference talks, blog posts, and academic papers.

---

## SEGMENT 7 — Debriefing the Client (19:30–22:00)

The debrief meeting is where you present findings to the client in person or via video
conference. This is a critical communication event.

### Audience Segmentation

Schedule separate debrief sessions if possible: a brief executive session (30–45 minutes)
for leadership, and a technical debrief (1–2 hours) for the security and IT team.

### Executive Debrief Techniques

- Open with the overall risk posture in one sentence: "Based on our assessment, your
  organization is at High risk, with three critical findings that require immediate attention."
- Use visual risk matrices and charts — a heat map of findings by likelihood vs. impact
  is immediately intuitive to business stakeholders
- Avoid tool names and CVE numbers in this session — use business language
- Be direct about severity; do not soften findings under pressure
- End with a prioritized action list

### Technical Debrief Techniques

- Walk through each finding using your report as the guide
- Reproduce the finding live if the client requests it and your rules of engagement permit
- Anticipate "why wasn't this detected" questions about SIEM rules and EDR gaps
- Discuss remediation timelines and offer to schedule a retest

### Managing Difficult Conversations

Sometimes clients are surprised, defensive, or argumentative about findings. Techniques:

- Lead with data, not opinion: "The CVSS score of 9.8 reflects these specific characteristics
  of the vulnerability — network-accessible, no authentication required."
- Acknowledge compensating controls when present
- Avoid blame language — findings are system and process issues, not personal failures

---

## SEGMENT 8 — Summary and PenTest+ Exam Points (22:00–24:00)

Let us recap the key points from Module 14.

Report types match audiences: executive summaries for business leadership, technical reports
for security and IT teams.

CVSS 3.1 produces scores from 0.0 to 10.0. The Base Score components cover Attack Vector,
Attack Complexity, Privileges Required, User Interaction, Scope, and three impact dimensions.
Know the severity thresholds: Critical 9.0+, High 7.0–8.9, Medium 4.0–6.9, Low 0.1–3.9.

Every finding has six components: Title, Description, Evidence, Impact, CVSS Score/Risk
Rating, and Remediation. Missing any component is a deficient finding.

Sensitive data must be redacted, encrypted in transit, and destroyed per contract terms.

Attestation documents that the engagement was authorized and conducted as agreed.

Debriefs are audience-segmented: executives hear business risk, technical teams hear
reproduction steps and remediation detail.

For the exam: Domain 5 (Reporting and Communication) comprises 18% of PT0-002. Questions
in this domain test your knowledge of report components, CVSS scoring, communication
techniques, and post-engagement documentation. Expect scenario-based questions where you
must identify a missing report component or choose the correct risk rating.

Lab and quiz for this module are on Canvas. See you in Module 15, where we cover post-engagement
cleanup and debriefing follow-through.

---

*End of Module 14 Video Script*
