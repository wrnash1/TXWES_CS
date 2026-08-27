# Reading Guide: Module 14 — Penetration Testing Reports

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002) — Domain 5: Reporting and Communication (18%)

---

## Introduction

Welcome to Module 14. The penetration testing report is the primary deliverable of any
engagement. Regardless of how thorough or sophisticated the technical work was, the client
receives value only through clear, well-structured, and actionable communication. This module
covers report types, CVSS scoring, finding quality standards, sensitive data handling,
attestation, and client debriefing techniques. All of this content maps directly to PenTest+
Domain 5: Reporting and Communication, which represents 18% of the PT0-002 exam.

---

## 1. High-Yield Glossary

Review these definitions carefully before the quiz and exam.

- **Executive Summary**: The report section written for non-technical business stakeholders
  (CISO, CIO, board). Contains overall risk posture, narrative of critical findings,
  remediation priorities, and attestation. Avoids technical jargon.

- **Technical Report**: The detailed report section written for security engineers and
  administrators. Contains finding descriptions, evidence, reproduction steps, CVSS scores,
  and specific remediation guidance.

- **CVSS (Common Vulnerability Scoring System)**: Industry-standard 0.0–10.0 scoring system
  for vulnerability severity. Version 3.1 uses Base, Temporal, and Environmental metric groups.
  The Base Score is computed from Attack Vector, Attack Complexity, Privileges Required,
  User Interaction, Scope, and three Impact dimensions.

- **Attack Vector (AV)**: CVSS Base metric describing how the vulnerability is reached.
  Network (N) scores highest risk because no physical proximity is needed.

- **Scope (S)**: CVSS Base metric. "Changed" means successful exploitation can affect
  resources beyond the vulnerable component's authorization scope — for example, a VM escaping
  to its hypervisor.

- **Risk Rating**: The reported severity assigned to a finding, which may differ from the raw
  CVSS Base Score when asset criticality, compensating controls, or threat context justify
  adjustment.

- **Finding**: The atomic report unit for each confirmed vulnerability. A complete finding
  contains six components: Title, Description, Evidence, Impact, CVSS Score/Risk Rating, and
  Remediation.

- **Attestation**: A formal signed statement affirming that the engagement was conducted within
  agreed scope and that findings accurately represent the state of the environment at time of
  testing. Protects both tester and client.

- **Non-Disclosure Agreement (NDA)**: A pre-engagement contract prohibiting unauthorized
  disclosure of client vulnerabilities, methodologies, and findings. NDA obligations survive
  after the engagement ends.

- **Chain of Custody**: Documentation tracking who collected, handled, stored, and transferred
  evidence. Establishes integrity and authenticity of findings. Covered in depth in Module 15.

- **Remediation Guidance Document**: A supplemental deliverable providing an action plan with
  owner assignments and timelines, derived from the technical findings.

- **Scope Verification Document**: Confirms that only authorized targets were tested during
  the engagement.

---

## 2. CVSS Severity Thresholds

Memorize these ranges for the exam:

| Score Range | Severity |
|-------------|----------|
| 9.0–10.0 | Critical |
| 7.0–8.9 | High |
| 4.0–6.9 | Medium |
| 0.1–3.9 | Low |
| 0.0 | None / Informational |

---

## 3. Six-Component Finding Structure

Every finding in the technical report must include all six components. Missing any component
is a deficiency that the exam may test directly.

1. **Title** — Specific, searchable, informative; includes the finding class, affected asset,
   and severity signal
2. **Description** — Technical explanation of the vulnerability class, manifestation, and
   root cause; references CVE and CWE identifiers where applicable
3. **Evidence** — Verifiable proof: screenshots with timestamps, tool output, file paths,
   version strings; your IP address visible to confirm authorized testing
4. **Impact** — Business consequence in plain language; quantified where possible;
   references applicable regulations (GDPR, PCI-DSS, HIPAA)
5. **CVSS Score and Risk Rating** — Full vector string and base score; justification if
   reported rating differs from raw CVSS
6. **Remediation** — Specific, actionable fix with short-term workaround and long-term
   solution; references vendor advisories, CIS benchmarks, or NIST controls

---

## 4. Certification Exam Tips

- **Domain weight**: Domain 5 (Reporting and Communication) = 18% of PT0-002. Expect 9–12
  questions on this material.

- **Report type matching**: Exam questions frequently present a scenario and ask which report
  type or section is appropriate. Executive stakeholders → executive summary. Technical
  remediation → technical report.

- **CVSS vectors on the exam**: You do not need to calculate exact decimal scores, but you
  must understand what each metric measures and how high-risk values differ from low-risk
  values. Know that AV:N is worse than AV:L, and PR:N is worse than PR:H.

- **Scope Changed vs. Unchanged**: A common exam scenario involves a vulnerability that
  allows escaping a container or VM. That is a Scope Changed scenario and increases the
  CVSS score significantly.

- **Evidence handling**: The exam tests that evidence must not be fabricated, must be
  timestamped, and must be encrypted before delivery to the client.

- **Attestation vs. NDA**: These are distinct concepts. Attestation is in the report and
  affirms accuracy. An NDA is a pre-engagement legal agreement governing confidentiality.

- **Debrief audience**: Exam questions may test that executive debriefs avoid tool names and
  CVE numbers, while technical debriefs include reproduction steps.

---

## 5. Required Readings and Videos

- **Required Reading**: CompTIA PenTest+ Study Guide (PT0-002), Chapter on Reporting and
  Communication. Focus on report component definitions, CVSS scoring methodology, and
  sensitive data handling requirements.

- **Required Video**: Watch the Reporting and Communication segment of the
  [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
  Use chapter markers to navigate to Domain 5 content.

- **Supplemental Resource**: The [FIRST CVSS v3.1 Specification](https://www.first.org/cvss/v3.1/specification-document)
  provides the authoritative definition of all Base, Temporal, and Environmental metrics.
  Review the metric definitions table.

- **Supplemental Resource**: NIST National Vulnerability Database (NVD) at nvd.nist.gov —
  look up three CVEs of your choice and examine how CVSS scores and vector strings are
  documented in real vulnerability records.

---

## 6. Lab and Quiz Integration

This week's lab has you draft a two-finding report section using a provided vulnerability
scenario. You will write a compliant Title, Description, Evidence summary, Impact, CVSS
vector with score, and Remediation for each finding. Pay close attention to the CVSS
calculator exercise — you will be asked to justify each metric selection.

The quiz covers CVSS scoring, report component identification, sensitive data handling rules,
and debrief audience segmentation.

---

## 7. Study Checklist

- [ ] Memorize the six finding components and be able to describe each in your own words
- [ ] Memorize the four CVSS severity thresholds and their score ranges
- [ ] Be able to explain each CVSS Base metric and identify which value indicates higher risk
- [ ] Distinguish executive summary from technical report by audience and content
- [ ] Understand attestation, NDA, and sensitive data handling requirements
- [ ] Complete the required reading and video segments
- [ ] Review the lab instructions before starting the hands-on exercise
- [ ] Proceed to the weekly quiz on Canvas

---

## 9. Supplemental Resources

**1. FIRST — CVSS v3.1 Specification Document**
https://www.first.org/cvss/v3.1/specification-document
The authoritative specification for CVSS 3.1 published by the Forum of Incident Response and Security Teams (FIRST). Covers the definition of every Base, Temporal, and Environmental metric with decision trees and worked examples. Essential reference for understanding why specific metric values are selected and how scores are calculated.

**2. OWASP Testing Guide — Reporting Chapter**
https://owasp.org/www-project-web-security-testing-guide/
The OWASP Web Security Testing Guide includes a dedicated reporting chapter covering finding structure, evidence requirements, and risk rating methodology. As an open standard widely referenced in professional penetration testing, it provides a vendor-neutral benchmark for report quality that complements the CompTIA PenTest+ exam objectives.

**3. TCM Security — Writing a Pentest Report (Free Course Sample)**
https://tcm-sec.com/practical-ethical-hacking-course/
TCM Security's Practical Ethical Hacking course includes a well-regarded module on professional report writing, covering executive summary tone, finding format, and client communication. The course is frequently recommended by working penetration testers as a practical supplement to certification study materials.
