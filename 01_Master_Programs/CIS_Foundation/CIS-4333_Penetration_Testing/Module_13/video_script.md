# Video Script: Module 13 — Penetration Test Report Writing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Production Notes

- **Runtime Target:** 28–32 minutes
- **Segments:** 6
- **Visual Aids:** Report structure diagram, CVSS calculator screenshot, sample findings (redacted), executive summary example
- **Lab Environment:** Report writing exercise using documented fictional findings

---

## Segment 1: Why Reporting Is the Deliverable (Lines 1–35)

[SLIDE: Module 13 Title Card]

Welcome to Module 13. Today we are talking about something that many technically-oriented students underestimate: the penetration test report.

Here is the reality: your technical findings are not the deliverable. The report is the deliverable. A brilliant technical assessment that produces an incomprehensible, poorly organized, or incomplete report has delivered almost nothing of value to the client. The client cannot act on what they cannot understand.

[SLIDE: The Report as Business Document]

A penetration test report is a professional business document. It serves multiple audiences simultaneously: executives who need to understand risk in business terms, technical staff who need specific remediation guidance, auditors who need evidence of due diligence, and potentially regulators and legal counsel who may review it.

Every section of the report has a different primary audience, and skilled report writers adjust their language and detail level accordingly.

[SLIDE: Professional and Legal Weight]

The penetration test report also carries legal and professional weight. It documents what was tested, what was found, and what the client should do. Clients may use it to justify security investments, demonstrate compliance, or respond to regulatory inquiries. A poorly written report can damage the client, expose the testing firm to liability, and undermine trust in the entire engagement.

[SLIDE: PT0-002 Alignment]

The PT0-002 exam dedicates an entire domain — Domain 4, Reporting and Communication — to this topic. You will be tested on report structure, CVSS scoring, finding components, and communication with stakeholders. Everything in this module has direct exam relevance.

[PAUSE for transition]

---

## Segment 2: Report Structure and Executive Summary (Lines 36–75)

[SLIDE: Standard Report Structure]

A professional penetration test report follows a recognized structure. Let me walk through each section.

The cover page includes the client name, report title, assessment date, testing firm name, and classification marking (typically "Confidential" or "Proprietary"). The report's classification is serious — this document contains sensitive vulnerability information.

The document control page tracks version history, distribution list (who received this report and when), and revision notes.

The table of contents ensures the report is navigable for different audiences who may want to jump directly to executive summary, specific findings, or appendices.

[SLIDE: The Executive Summary]

The executive summary is the most important section in the report because it is the section most people will actually read. Executives, board members, and non-technical stakeholders rely entirely on this section for their understanding of the engagement.

The executive summary should include:

A scope and objective statement — what was tested and why.

An overall security posture assessment — a brief qualitative judgment: strong, moderate, weak. Some firms use a letter grade or color rating.

Key findings summary — the top 3 to 5 findings in plain language, without technical detail.

Risk summary — a statement of the overall risk to the organization.

Priority action items — 3 to 5 recommended actions stated in business terms.

[SLIDE: Writing for Executives]

Writing an executive summary requires translating technical findings into business language. Consider the difference:

Technical: "The web application at 192.168.1.45 is vulnerable to SQL injection via the username parameter (CVE-2021-27850), enabling unauthenticated read access to the user credentials table."

Executive: "The customer portal's login page has a flaw that allows an attacker to access the entire customer database without requiring a password. This could expose 45,000 customer records including payment information."

Both describe the same finding. The executive version communicates the business impact. Lead with the consequence, not the mechanism.

[PAUSE for transition]

---

## Segment 3: Technical Findings Section (Lines 76–115)

[SLIDE: Finding Structure]

Each technical finding follows a standard structure. This structure is important for both clarity and for comparing findings across the report.

Finding Title: Brief, descriptive, and consistent. "SQL Injection in Customer Portal Login" is better than "SQLi" or "Web App Vulnerability #3."

Risk Rating: Critical, High, Medium, Low, or Informational. The basis for this rating should be documented (CVSS score, business impact).

CVSS Score: The quantitative severity score, with the full vector string documented.

Description: What is the vulnerability, where was it found, and how was it confirmed?

Evidence: Screenshots, command output, proof of concept. Evidence makes the finding irrefutable and enables the client's technical team to reproduce and verify.

Impact: What can an attacker accomplish using this vulnerability?

Affected Systems/Assets: Specific hostnames, IP addresses, or asset identifiers.

Remediation (Short-term): Immediate mitigation — configuration change, patch, disable feature.

Remediation (Long-term): Permanent fix — code remediation, architecture change, vendor upgrade.

References: CVE numbers, NVD entries, vendor advisories, standards references.

[SLIDE: Finding Quality Standards]

The standard for a well-written finding:

Reproducibility: A technical person reading the finding should be able to reproduce the vulnerability and verify the fix.

Specificity: Findings reference specific systems, versions, and parameters — not "a web server" but "the Apache 2.4.48 instance at webprod01.internal:443."

Evidence integrity: Screenshots must show the testing machine's IP and timestamp. Command output must be unedited. Manipulated evidence is career-ending.

Objectivity: Findings state what was found and what it means. They do not overstate severity to appear impressive or understate severity to appear client-friendly.

[SLIDE: Evidence Best Practices]

Evidence documentation requires care:

For screenshots: Use a consistent tool (Flameshot, Greenshot). Include timestamps. Show the URL or system identifier in the screenshot. Do not crop out context.

For command output: Copy directly from the terminal. Include the command issued, the full output, and the system you ran it from.

For network traffic: Wireshark captures with relevant packets highlighted. Include the source/destination IPs and timestamps.

Every piece of evidence should have a caption explaining what it shows. Do not assume the reader will understand an unexplained screenshot.

[PAUSE for transition]

---

## Segment 4: CVSS Scoring in Practice (Lines 116–155)

[SLIDE: CVSS 3.1 Architecture]

CVSS (Common Vulnerability Scoring System) version 3.1 is the current standard for vulnerability severity quantification. It produces a numerical score from 0.0 to 10.0 and a qualitative rating:

- 0.0: None
- 0.1–3.9: Low
- 4.0–6.9: Medium
- 7.0–8.9: High
- 9.0–10.0: Critical

The CVSS score is not a complete risk assessment — it measures the technical severity of the vulnerability in isolation. Business context, data classification, and system criticality modify the effective risk and are captured in the temporal and environmental metric groups.

[SLIDE: Base Metrics]

The Base Score reflects the intrinsic characteristics of the vulnerability:

Attack Vector (AV): Network (N), Adjacent (A), Local (L), Physical (P). Network-exploitable vulnerabilities score highest.

Attack Complexity (AC): Low (L) or High (H). No special conditions required = Low.

Privileges Required (PR): None (N), Low (L), High (H). No authentication required = None.

User Interaction (UI): None (N) or Required (R). Exploitation requires no user action = None.

Scope (S): Unchanged (U) or Changed (C). If exploitation affects resources beyond the vulnerable component's authorization scope, Scope is Changed.

Confidentiality Impact (C), Integrity Impact (I), Availability Impact (A): None (N), Low (L), High (H).

[SLIDE: Worked CVSS Example]

Let us score SQL injection in a web application that enables unauthenticated database read access:

Attack Vector: Network (N) — exploitable remotely.

Attack Complexity: Low (L) — basic SQL injection, no special conditions.

Privileges Required: None (N) — the login form is the attack surface.

User Interaction: None (N) — no victim action required.

Scope: Changed (C) — SQL injection crosses the web application boundary into the database.

Confidentiality: High (H) — full database read access.

Integrity: High (H) — SQL injection can also write to the database.

Availability: High (H) — database deletion is possible.

Vector string: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H

Score: 10.0 — Critical.

[SLIDE: Temporal and Environmental Metrics]

Temporal metrics adjust the score based on current conditions:

Exploit Code Maturity: Is there public exploit code? Published proof-of-concept code increases the effective risk.

Remediation Level: Is a vendor patch available? Unavailability of a patch increases effective risk.

Report Confidence: How confirmed is the vulnerability? Confirmed exploitation vs. theoretical vulnerability affects temporal scoring.

Environmental metrics adjust for the specific deployment context:

Modified Attack Vector, Modified Attack Complexity, etc. — reflect how the organization's environment affects the exploitability.

Confidentiality, Integrity, Availability Requirements — reflect the organization's specific data classification and system criticality.

A Critical CVSS base score vulnerability on a non-critical test system with no sensitive data may rate as High or Medium in environmental context.

[PAUSE for transition]

---

## Segment 5: Remediation Recommendations and Risk Ratings (Lines 156–195)

[SLIDE: Remediation Quality Standards]

Remediation recommendations are where the report delivers practical value. A good remediation recommendation is:

Specific: Not "improve authentication" but "enforce MFA on all privileged account logins using FIDO2 hardware tokens."

Actionable: The client's technical team can implement this recommendation without further research.

Tiered: Short-term (immediate mitigation) and long-term (permanent fix) are distinct. Disabling a vulnerable feature (short-term) is different from patching the root cause (long-term).

Realistic: Consider the client's environment. Recommending a vendor patch is reasonable; recommending a complete application rewrite is not a short-term remediation.

[SLIDE: Prioritization Framework]

The report should present findings in priority order and provide a remediation roadmap:

Immediate (0–30 days): Critical and High findings. These represent active exploitable risk. Patch critical vulnerabilities, disable exposed services, implement emergency access controls.

Short-term (30–90 days): Medium findings. Address with targeted configuration changes, patches, and policy updates.

Long-term (90 days+): Low and Informational findings, architectural changes, and comprehensive program improvements.

[SLIDE: Risk Rating vs. CVSS Score]

A critical distinction: the CVSS score is a severity measure. The finding's risk rating to the specific client may differ based on:

Business impact: A Critical severity vulnerability in a non-production system with no sensitive data may be rated High or Medium in context.

Compensating controls: An existing WAF may reduce the effective exploitability of a web vulnerability, lowering the effective risk.

Likelihood: A vulnerability requiring physical access to exploit is less likely to be used against a well-protected facility.

Regulatory context: Some medium-severity findings may be rated High because they implicate regulatory compliance requirements.

Document the basis for any deviation from CVSS-based ratings.

[SLIDE: Communicating Risk Without Alarm]

Report language should inform without creating panic. Specific guidance:

Do not use fear-based language: "This vulnerability will certainly be exploited" is speculation. "This vulnerability is easily exploitable and represents significant risk" is accurate.

Quantify where possible: "Exploitation takes less than 5 minutes with freely available tools" is more informative than "this is trivial to exploit."

Focus on remediation: Frame findings with the solution in mind. "This vulnerability can be eliminated by applying the available patch" is more actionable than dwelling on the impact.

Do not embarrass individuals: If an employee made a security error, findings reference the system or process, not the person.

[PAUSE for transition]

---

## Segment 6: Final Report Assembly and Client Communication (Lines 196–240)

[SLIDE: Appendices and Supporting Material]

Appendices capture material that supports findings but would interrupt the report narrative if included in the body:

Appendix A — Scope and Methodology: The formal description of tested systems, testing dates, methodologies used, and tools employed.

Appendix B — Testing Limitations: What was out of scope, what testing was not performed, and how limitations may affect completeness.

Appendix C — Vulnerability Index: A complete list of all findings with title, severity, and page reference. Useful for tracking remediation progress.

Appendix D — Tool Output: Raw tool output, full Nmap scans, full Nikto output, and other unprocessed data that supports technical findings.

Appendix E — Confidentiality Notice: Legal language defining the classification and handling requirements for the report.

[SLIDE: Report Quality Review]

Before delivery, all reports undergo quality review:

Technical accuracy review: A second tester validates findings are accurately described and reproducible.

Clarity review: A non-technical reader (or the writer after a day away from the document) reviews for unclear language.

Evidence review: All screenshots and command output are verified against original capture files.

Consistency review: Risk ratings, CVSS scores, and remediation timelines are internally consistent. A Critical finding should not be assigned a 90-day remediation timeline without explanation.

Completeness review: Every finding follows the complete structure. Every finding has evidence. Every finding has remediation.

[SLIDE: Delivering the Report]

Report delivery includes both document delivery and a readout meeting.

The document should be transmitted securely. Email is generally insufficient for a document containing sensitive vulnerability information. Use an encrypted transfer: password-protected PDF, encrypted email (PGP), or a secure file sharing portal.

The readout meeting walks the client through findings. Have two versions ready: an executive briefing (30–45 minutes, top findings and business risk) and a technical walkthrough (60–90 minutes, detailed findings for the security team). These are often separate meetings with different audiences.

[SLIDE: Handling Client Pushback]

Clients sometimes dispute findings, especially severity ratings. Guidelines:

Engage professionally: Listen to the client's perspective. If they have technical context that changes the finding's exploitability, it may legitimately affect the rating.

Stand on evidence: If your rating is supported by evidence and sound methodology, explain your basis clearly.

Document disagreements: If the client wishes to accept a risk you have rated as High, document their acceptance decision in the report as a "Risk Acceptance" note — do not remove the finding.

Do not negotiate severity for relationship reasons: Downgrading a critical finding to avoid a difficult conversation is a professional and potentially legal violation.

[SLIDE: Module Summary]

Module 13 covered the complete penetration test report: structure from cover page to appendices, executive summary writing for non-technical audiences, technical finding structure, CVSS 3.1 scoring methodology, remediation recommendation quality standards, risk rating considerations, and professional delivery practices.

The report is your most visible professional product. Invest in making it excellent.

[END RECORDING]
