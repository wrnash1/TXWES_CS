# Reading Guide: Module 15 - Reporting – Writing Professional Pentest Reports
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 15 - Reporting – Writing Professional Pentest Reports**! A penetration test that is not clearly communicated in a professional report has limited value to the client. The report is the primary deliverable of an engagement — it must accurately document what was found, how it was found, what it means for the business, and how to fix it. Reporting and communication maps to the **Reporting & Communication** domain of PT0-002 (**18% of exam weight**), making it the third-largest domain and one that is frequently underestimated by candidates who focus exclusively on technical attack skills.

Professional report writing separates competent penetration testers from excellent ones. The ability to translate technical findings into clear, actionable business guidance directly determines the impact an engagement has on improving the client's security posture.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Executive Summary**: The non-technical section of a pentest report written for senior leadership, executives, and board members who make business decisions. It describes the overall security posture, the most critical findings in business terms (financial risk, regulatory exposure, reputational impact), the engagement scope, and high-level remediation priorities. The executive summary should be understandable without any technical security knowledge — it answers "How bad is it and what should we do about it?" PT0-002 tests the distinction between the executive summary and the technical findings section.

*   **Technical Findings Section**: The detailed, technical portion of the report written for IT and security teams who will remediate identified vulnerabilities. Each finding should include: a descriptive title, severity rating (Critical/High/Medium/Low), CVSS score, affected systems, a description of the vulnerability, step-by-step evidence of exploitation (screenshots, command output), business impact, and specific remediation recommendations. PT0-002 tests the required components of a well-formed technical finding.

*   **CVSS (Common Vulnerability Scoring System) v3.1**: The industry-standard framework for rating vulnerability severity. The Base Score considers Exploitability metrics (Attack Vector, Attack Complexity, Privileges Required, User Interaction) and Impact metrics (Confidentiality, Integrity, Availability impact). Score ranges: Critical 9.0–10.0, High 7.0–8.9, Medium 4.0–6.9, Low 0.1–3.9. PT0-002 expects testers to know these ranges and how base score factors affect ratings — for example, a remotely exploitable vulnerability with no authentication required and full system impact scores Critical.

*   **Remediation Recommendations**: Specific, actionable guidance for each finding that tells the client exactly what to do to fix the vulnerability. Recommendations should be prioritized by severity and feasibility, include both immediate mitigations (short-term workarounds) and permanent fixes (long-term solutions), and reference industry standards or patches where applicable. Vague recommendations ("improve security") are not acceptable in a professional pentest report.

*   **Post-Engagement Cleanup and Attestation**: After testing concludes, the tester must remove all artifacts placed on client systems — backdoors, persistence mechanisms, uploaded tools, created accounts, and modified configurations. The tester provides written attestation confirming cleanup completion. Failure to clean up leaves the client's environment in a more vulnerable state than before the engagement. PT0-002 tests that cleanup is an explicit engagement phase, not an afterthought.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Reporting & Communication is **18% of PT0-002** — the third-largest domain. Do not neglect this domain while preparing. Report structure, CVSS scoring, and communication skills are directly tested.
*   **Report Audiences:** PT0-002 tests that different report sections serve different audiences. The Executive Summary targets non-technical leadership. The Technical Findings target IT/security teams. The Methodology section documents process for quality assurance. Understand which section answers which stakeholder's questions.
*   **CVSS Base Score Components:** The six base metrics are: Attack Vector (Network/Adjacent/Local/Physical), Attack Complexity (Low/High), Privileges Required (None/Low/High), User Interaction (None/Required), Scope (Unchanged/Changed), and the three Impact metrics (Confidentiality/Integrity/Availability each: None/Low/High). PT0-002 scenario questions may describe a vulnerability and ask which CVSS severity range it falls into.
*   **Recommended vs. Accepted Risk:** When a client acknowledges a finding but chooses not to remediate it (risk acceptance), the tester documents this as "Risk Accepted by Client" in the report. This protects the tester legally and creates an audit trail. PT0-002 tests awareness of risk acceptance as a formal documentation step.
*   **Report Handling and Confidentiality:** Pentest reports contain sensitive information — attack paths, credential hashes, system vulnerabilities. Reports must be delivered securely (encrypted, password-protected) and handled according to the data handling provisions in the NDA and MSA. PT0-002 tests awareness of report confidentiality obligations.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Pentest Reports" and "Reporting" rooms provide guided practice with report structure, finding documentation, CVSS scoring, and writing effective remediation recommendations in the context of real engagement scenarios.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Reporting & Communication section for content covering report structure, CVSS scoring, executive vs. technical audience writing, and post-engagement cleanup mapped to PT0-002 domain 4.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Reporting and Communication rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). TryHackMe is a browser-based cybersecurity training platform covering all phases of penetration testing. The reporting rooms cover professional finding documentation, CVSS scoring practice, executive summary writing techniques, and post-engagement cleanup procedures.
*   **Required Video:** Watch the Reporting & Communication segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This is a free, full-length PT0-002 prep course on YouTube. Use chapter markers to navigate to the domain 4 content covering report structure, CVSS scoring, audience-appropriate writing, and engagement closure procedures.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Draft a complete technical finding**: Using a vulnerability discovered in a previous lab, you will write a fully formed technical finding — including title, CVSS score with justification, affected system, description, evidence, business impact, and specific remediation recommendations. You will evaluate whether each component meets the standard expected in a professional pentest report.
*   **Write an Executive Summary for a simulated engagement**: Given a set of findings from a hypothetical engagement (2 Critical, 3 High, 5 Medium), you will write a 1–2 paragraph executive summary appropriate for a non-technical VP audience — translating the technical severity into business risk language and prioritizing the most impactful findings.
*   **Complete a post-engagement cleanup checklist**: You will document all artifacts that would need to be removed after a real engagement (shells, accounts, registry keys, uploaded files, firewall rules) and draft a written cleanup attestation statement — demonstrating understanding of the tester's obligation to restore the client's environment to its pre-test state.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Reporting rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Reporting & Communication section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
