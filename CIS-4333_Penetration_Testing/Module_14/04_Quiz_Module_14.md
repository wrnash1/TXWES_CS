# Quiz: Module 14 — Penetration Testing Reports

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002) — Domain 5: Reporting and Communication

---

**Question 1**

What section of a penetration testing report is written specifically for non-technical
stakeholders such as executives and board members, summarizing security risks in business terms?

- A) Technical Findings List
- B) Executive Summary
- C) Appendix — Scan Output
- D) Methodology Section

**Correct Answer:** B) Executive Summary

**Distractor Analysis:**

- *Why B is correct:* The Executive Summary translates technical findings into business
  language — describing overall risk posture, most critical issues, potential business impact
  (financial, regulatory, reputational), and high-level remediation priorities. Executives use
  it to make resource allocation and risk management decisions without needing to understand
  the technical details of each exploit.
- *Why A is incorrect:* The Technical Findings List contains detailed vulnerability
  descriptions, exploit steps, affected systems, evidence screenshots, and specific
  remediation guidance — written for IT and security teams who will remediate. It is not
  appropriate for a non-technical executive audience.
- *Why C is incorrect:* The Appendix typically contains raw tool output, full scan results,
  or supporting evidence. It is highly technical reference material — the opposite of an
  executive summary.
- *Why D is incorrect:* The Methodology section describes the testing approach, phases
  followed, and tools used. While less technical than findings, it is written for technical
  readers who need to understand how the assessment was conducted — not for executive
  business decision-making.

---

**Question 2**

A penetration tester confirms a vulnerability with the following CVSS 3.1 Base metrics:
AV:N, AC:L, PR:N, UI:N, S:U, C:H, I:H, A:H. What severity rating does this score produce?

- A) High (7.0–8.9)
- B) Medium (4.0–6.9)
- C) Critical (9.0–10.0)
- D) Low (0.1–3.9)

**Correct Answer:** C) Critical (9.0–10.0)

**Distractor Analysis:**

- *Why C is correct:* This vector — Network-accessible, Low complexity, No privileges
  required, No user interaction, Unchanged scope, High impact on all three CIA dimensions —
  is the signature of a maximally severe vulnerability. It corresponds to approximately 9.8
  on the CVSS 3.1 scale, placing it firmly in the Critical range. This is the exact CVSS
  profile of MS17-010 (EternalBlue) and CVE-2021-44228 (Log4Shell).
- *Why A is incorrect:* High requires either some friction in exploitability (AC:H, PR:L, or
  UI:R) or a less-than-High impact on at least one dimension. A fully Network-accessible,
  zero-authentication, full-impact vulnerability exceeds the High threshold.
- *Why B is incorrect:* Medium scores (4.0–6.9) reflect local or adjacent attack vectors,
  required privileges, or limited impact. None of those conditions apply here.
- *Why D is incorrect:* Low scores require very constrained attack vectors (Local or
  Physical), high complexity, and/or minimal impact. This vector has the opposite
  characteristics.

---

**Question 3**

Which CVSS 3.1 metric is rated "Changed" when a vulnerability in a guest virtual machine
allows an attacker to escape and execute code on the underlying hypervisor?

- A) Attack Complexity (AC)
- B) Privileges Required (PR)
- C) Scope (S)
- D) User Interaction (UI)

**Correct Answer:** C) Scope (S)

**Distractor Analysis:**

- *Why C is correct:* CVSS defines Scope as Changed when successful exploitation of a
  vulnerability in one component (the vulnerable VM guest) can impact resources managed by
  a different security authority (the hypervisor). A VM escape is the canonical Scope Changed
  scenario. A Changed scope increases the CVSS Base Score because the blast radius of
  exploitation extends beyond the originally vulnerable component.
- *Why A is incorrect:* Attack Complexity measures the conditions the attacker must meet to
  exploit the vulnerability — such as race conditions or specific configuration states. A VM
  escape may or may not be high complexity, but the relevant metric for cross-boundary impact
  is Scope, not Complexity.
- *Why B is incorrect:* Privileges Required describes what access the attacker needs before
  exploiting, such as requiring a guest user account. It does not describe whether
  exploitation crosses authorization boundaries.
- *Why D is incorrect:* User Interaction describes whether a victim must take an action (click
  a link, open a file) for exploitation to succeed. Container/VM escapes typically do not
  require victim interaction.

---

**Question 4**

A penetration tester writes this finding title: "SQL Injection Found on Web Server." A senior
reviewer marks this title as deficient. What is the primary deficiency?

- A) The title uses a CVE number instead of a CWE number, which is incorrect for web
  application findings
- B) The title is too vague — it does not specify the location, affected asset, or consequence,
  making the finding unsearchable and uninformative to the reader
- C) The title is too long — professional report titles must be under five words to fit
  report templates
- D) The title incorrectly names SQL injection; the correct term is "database query
  manipulation vulnerability"

**Correct Answer:** B) The title is too vague — it does not specify the location, affected
asset, or consequence, making the finding unsearchable and uninformative to the reader

**Distractor Analysis:**

- *Why B is correct:* A professional finding title must communicate what was found, where,
  and its consequence — before the reader opens the full finding. "SQL Injection Found on
  Web Server" omits the specific URL or endpoint, the affected application or host identifier,
  and the consequence (data extraction, authentication bypass, etc.). A better title:
  "Unauthenticated SQL Injection in /login Endpoint Allows Full Database Extraction (CWE-89)."
- *Why A is incorrect:* CVE numbers are appropriate in finding titles when a known CVE
  applies. CWE numbers describe vulnerability classes. Using either or both is acceptable and
  encouraged — there is no rule prohibiting CVE references in finding titles.
- *Why C is incorrect:* There is no five-word title length rule in professional reporting
  standards. Descriptive, specific titles are valued over brevity. Titles of 10–15 words are
  normal in quality pentest reports.
- *Why D is incorrect:* "SQL Injection" is the correct, industry-standard term for this
  vulnerability class. It is documented as CWE-89 (Improper Neutralization of Special
  Elements used in an SQL Command). Renaming it "database query manipulation" is non-standard
  and would be confusing to technical readers.

---

**Question 5**

During an engagement, a penetration tester extracts a file containing 50,000 customer Social
Security numbers from a target database server. How should this finding be documented in the
report?

- A) Paste all 50,000 records into the evidence appendix to fully prove the severity of the
  data exposure
- B) Include the filename, table name, and column headers in the evidence section, then
  substitute actual SSN values with `XXX-XX-XXXX` redaction markers, showing only one to
  two redacted sample rows
- C) Omit the finding from the report entirely because including PII in the report would
  itself create a data breach
- D) Include the full file but encrypt it with a separate password and distribute it only
  to the CISO

**Correct Answer:** B) Include the filename, table name, and column headers in the evidence
section, then substitute actual SSN values with `XXX-XX-XXXX` redaction markers, showing
only one to two redacted sample rows

**Distractor Analysis:**

- *Why B is correct:* The goal of evidence is to prove the finding, not to reproduce the
  client's sensitive data in full. Showing the filename, database table name, column headers,
  and a redacted sample row conclusively proves that PII was accessible. Including the full
  50,000-record dump in the report creates additional exposure: the report itself becomes a
  PII breach if it is leaked, forwarded, or stored insecurely. Redaction is the professional
  and legally prudent approach.
- *Why A is incorrect:* Pasting 50,000 SSNs into the report creates a far greater data
  exposure risk than the finding itself. Reports are shared with multiple stakeholders and
  stored on client systems. This approach would almost certainly violate the data handling
  provisions of the engagement contract.
- *Why C is incorrect:* Omitting the finding would be a fundamental professional failure.
  The client needs to know that their PII was accessible. The solution is to report the
  finding with appropriately redacted evidence, not to suppress it.
- *Why D is incorrect:* Distributing a separate encrypted file containing 50,000 real SSNs
  still creates unnecessary data exposure. Even with encryption, the data should not be
  retained or transmitted beyond what is needed to prove the finding. Redaction eliminates
  the need to transfer actual PII.

---

**Question 6**

An attestation statement in a penetration test report serves which primary purpose?

- A) It certifies that the tester holds an active CompTIA PenTest+ certification valid at
  the time of the engagement
- B) It formally declares that the engagement was conducted within the agreed scope and that
  findings accurately represent the state of the environment at the time of testing
- C) It grants the client permission to publicly disclose the pentest findings on their
  website as a transparency measure
- D) It transfers legal liability for any damage caused during testing from the tester to
  the client organization

**Correct Answer:** B) It formally declares that the engagement was conducted within the
agreed scope and that findings accurately represent the state of the environment at the time
of testing

**Distractor Analysis:**

- *Why B is correct:* An attestation is a sworn professional statement of accuracy and
  compliance with scope. It protects the client by giving auditors and regulators a documented
  assertion from a qualified professional. It protects the tester by establishing a clear
  record of what was and was not tested. Attestation language typically includes the testing
  dates, scope boundaries, and a declaration that findings reflect the environment's state
  at the time of assessment.
- *Why A is incorrect:* Attestation does not certify the tester's credentials. Credential
  verification is the client's responsibility during vendor selection and may be separately
  documented in the contract or proposal — not in the report attestation block.
- *Why C is incorrect:* Attestation says nothing about public disclosure rights. Public
  disclosure rights are governed by the NDA and engagement contract, not the report
  attestation. Most NDAs explicitly prohibit public disclosure.
- *Why D is incorrect:* Attestation is a statement of professional accuracy — it does not
  transfer legal liability. Liability provisions are defined in the master service agreement
  (MSA) and statement of work (SOW) executed before the engagement begins.

---

**Question 7**

A penetration tester completes an engagement and is scheduling the debrief. Which approach
best follows professional reporting standards?

- A) Hold a single combined debrief for all stakeholders simultaneously — executives,
  managers, and technical staff — to ensure consistent messaging
- B) Send the full technical report to all stakeholders via unencrypted email and cancel
  the live debrief to save time
- C) Hold separate debrief sessions: a brief executive session focused on business risk and
  remediation priorities, and a technical session with the security team covering finding
  reproduction and remediation details
- D) Present only the executive summary to all audiences and withhold the technical report
  until remediation is complete

**Correct Answer:** C) Hold separate debrief sessions: a brief executive session focused on
business risk and remediation priorities, and a technical session with the security team
covering finding reproduction and remediation details

**Distractor Analysis:**

- *Why C is correct:* Different stakeholders have different informational needs and different
  tolerances for technical depth. A combined session forces the presenter to either
  over-simplify for technical staff or overwhelm executives with technical detail. Separate
  sessions allow each audience to engage at the appropriate level. Executive sessions typically
  run 30–45 minutes and avoid tool names and CVE numbers. Technical sessions run 1–2 hours
  and include reproduction walkthroughs.
- *Why A is incorrect:* A combined session creates competing communication problems: executives
  disengage from technical detail, while technical staff grow frustrated with over-simplified
  summaries. It produces a worse outcome for both groups.
- *Why B is incorrect:* Reports containing vulnerability details and evidence must be delivered
  via encrypted channels — not unencrypted email. Canceling the debrief eliminates the
  opportunity to clarify findings, answer questions, and build the working relationship needed
  for remediation follow-through.
- *Why D is incorrect:* Withholding the technical report prevents the security team from
  beginning remediation. The technical team needs the full report immediately to prioritize
  and begin fixing vulnerabilities. Waiting until remediation is complete makes no logical
  sense — the report is the guide for remediation, not a reward after it.

---

**Question 8**

A penetration tester scores a finding with a CVSS 3.1 Base Score of 9.4 (Critical). However,
the affected host is a development server with no production data, isolated from the
internet, and accessible only from a single internal VLAN. The tester reports the finding as
High rather than Critical. What principle justifies this adjustment?

- A) CVSS scores are advisory only; pentesters may reduce severity ratings arbitrarily to
  satisfy client preferences
- B) The CVSS Base Score measures inherent vulnerability severity, but reported risk rating
  should account for compensating controls and asset criticality, which reduce the effective
  business risk below the raw score
- C) Any finding on an internal host must be rated one severity level lower than its CVSS
  score by standard penetration testing methodology
- D) A CVSS score above 9.0 can only be assigned to vulnerabilities with confirmed active
  exploitation in the wild; without a known threat actor, the score must be reduced

**Correct Answer:** B) The CVSS Base Score measures inherent vulnerability severity, but
reported risk rating should account for compensating controls and asset criticality, which
reduce the effective business risk below the raw score

**Distractor Analysis:**

- *Why B is correct:* CVSS Base Scores are calculated from the vulnerability's inherent
  characteristics, independent of the deployment context. Business risk — the thing that
  drives remediation urgency — depends on additional factors: how critical is the asset?
  What compensating controls are in place? How likely is this specific path to be exploited
  given the network architecture? A Critical CVSS score on an isolated development server
  with no sensitive data presents materially lower business risk than the same vulnerability
  on an internet-facing production database. Documenting the adjustment with justification
  is required and transparent.
- *Why A is incorrect:* Arbitrary severity reductions to satisfy client preferences are
  unprofessional and potentially fraudulent. Any adjustment must be documented with specific
  technical justification — not client preference. A tester who softens ratings under
  commercial pressure is compromising the integrity of the assessment.
- *Why C is incorrect:* There is no automatic "internal host minus one level" rule in any
  standard pentest methodology (PTES, OWASP, NIST). The adjustment must be justified by
  specific contextual factors, not a blanket rule based on network location.
- *Why D is incorrect:* CVSS Base Scores are calculated from the vulnerability's technical
  characteristics, not from threat intelligence about active exploitation. Active exploitation
  data is captured in the Temporal Score's Exploit Code Maturity metric — it does not
  retroactively reduce the Base Score.

---

**Question 9**

Which of the following is the correct format for documenting a CVSS 3.1 vector string in
a penetration test report finding?

- A) `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`
- B) `CVSS v3.1 = Network/Low/None/None/Unchanged/High/High/High`
- C) `Base Score: 9.8 — all metrics at maximum risk`
- D) `Risk Level: Critical (per internal assessment rubric)`

**Correct Answer:** A) `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

**Distractor Analysis:**

- *Why A is correct:* The CVSS specification defines a standard vector string format using
  abbreviated metric value codes separated by forward slashes, prefixed with the version
  identifier `CVSS:3.1/`. This format is machine-readable, unambiguous, and universally
  understood by security professionals and vulnerability management tools. Including the
  full vector string in a report finding makes the score reproducible and auditable.
- *Why B is incorrect:* Spelling out full metric names and values in prose is non-standard,
  verbose, and does not conform to the CVSS specification format. It cannot be parsed by
  vulnerability management tools and is harder to read quickly than the standard vector.
- *Why C is incorrect:* "All metrics at maximum risk" is an informal description, not a
  vector string. It does not convey which specific metrics were assigned which values, making
  it impossible for a reader to verify or reproduce the score.
- *Why D is incorrect:* "Per internal assessment rubric" removes the finding from any
  standardized, externally verifiable scoring framework. The value of CVSS is that it is a
  common language — substituting a proprietary rubric without the standard vector makes the
  rating unverifiable.

---

**Question 10**

A penetration tester's NDA with a client prohibits disclosure of engagement findings without
written authorization. Two years after the engagement, the tester wants to present the
methodology and sanitized findings at a security conference. Which action is appropriate?

- A) Proceed with the conference presentation because the NDA only covers the 12 months
  following the engagement
- B) Post the report on a personal blog with all IP addresses changed — the altered details
  make disclosure permissible
- C) Obtain explicit written authorization from the client before including any details
  derived from the engagement in the presentation
- D) The tester may present generic methodology without referencing the client, because
  NDAs only restrict disclosure of the client's name and never the technical content

**Correct Answer:** C) Obtain explicit written authorization from the client before including
any details derived from the engagement in the presentation

**Distractor Analysis:**

- *Why C is correct:* NDA obligations are contractual and typically survive indefinitely
  unless the agreement specifies an expiration date. Even sanitized, paraphrased, or
  generalized versions of engagement details may be covered if they are derived from
  confidential information. The safest and professionally correct approach is to request
  written permission from the client before using any engagement-derived content publicly.
  Many clients will grant permission for sanitized case studies — but permission must be
  explicit and documented.
- *Why A is incorrect:* NDAs do not automatically expire after 12 months unless the contract
  explicitly states that term. Assuming expiration without reading the agreement is a serious
  professional and legal error.
- *Why B is incorrect:* Changing IP addresses does not remove confidentiality obligations.
  The protected information includes vulnerability details, methodology insights, architectural
  weaknesses, and findings — not just IP addresses. A client could still identify their own
  environment from sanitized technical details.
- *Why D is incorrect:* NDAs routinely cover technical content, not just the client's name.
  Standard NDA language covers "all confidential information disclosed during the engagement,"
  which typically includes vulnerability findings, system configurations, and assessment
  methodology applied to the client's environment.

---

*End of Module 14 Quiz*
