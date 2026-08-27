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

### Question 11 (5 points)

A penetration tester writes a remediation recommendation that states: "Update the software to the latest version." A senior reviewer marks this as insufficient. What specific improvement is required?

- A) The recommendation must include the tester's personal opinion about whether the client should prioritize this finding over others
- B) The recommendation must specify the exact patch or version number, the vendor advisory reference, the configuration change required, and both a short-term workaround and a long-term fix
- C) The recommendation must include the CVSS Temporal score in addition to the Base score before remediation guidance can be written
- D) The recommendation must be removed from the technical report and placed only in the executive summary

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Professional remediation guidance must be actionable — the reader (a system administrator) must know exactly what to do. "Update the software" gives no version target, no patch reference, and no workaround for organizations that cannot patch immediately. A complete remediation entry includes the specific patch (e.g., KB5004945), the vendor advisory URL, a short-term mitigation (e.g., disable the affected service or restrict access), and a long-term fix (apply the patch within the organization's change management window).
  - Why A is incorrect: Personal opinions about relative priority belong in the executive summary as remediation priorities, not in the technical finding's remediation section. The remediation section is prescriptive, not advisory or comparative.
  - Why C is incorrect: CVSS Temporal scores are optional and do not gate the writing of remediation guidance. Remediation can be written from the Base Score alone, or even without a CVSS score, as long as the guidance is specific and actionable.
  - Why D is incorrect: Remediation guidance belongs in the technical finding entry where engineers will read it. Placing it only in the executive summary removes it from the context where it will be acted upon.

---

### Question 12 (5 points)

Which of the following is the correct approach when a penetration tester discovers a critical vulnerability during testing that poses immediate risk of data loss if exploited — before the formal report is complete?

- A) Document the finding in the report and wait until report delivery to notify the client — findings should not be shared piecemeal
- B) Immediately notify the designated client point of contact as specified in the Rules of Engagement communication plan, using the agreed escalation channel, without waiting for the final report
- C) Post the finding to a shared ticket system so the client's IT team can begin remediation on their own initiative
- D) Stop the engagement entirely until the critical finding is remediated before continuing any further testing

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The Rules of Engagement communication plan defines escalation procedures for urgent findings. Critical findings that represent immediate risk must be communicated immediately — waiting for the final report could allow the vulnerability to be exploited during the remaining test period. The RoE specifies who to call, what channel to use (secure phone, encrypted email), and what information to convey. This is the emergency finding notification procedure.
  - Why A is incorrect: Withholding critical findings until report delivery prioritizes the tester's reporting process over the client's security. The communication plan exists precisely to handle situations where immediate disclosure is warranted. Waiting is a professional failure in this scenario.
  - Why C is incorrect: Posting findings to shared ticketing systems without the client's explicit authorization may violate data handling provisions and expose finding details to unauthorized parties. The communication channel is defined by the RoE, not chosen by the tester.
  - Why D is incorrect: Stopping the engagement is not required or appropriate for a single critical finding. Testing should continue (unless the RoE specifies otherwise) while the notification is made. Stopping prematurely would leave the rest of the engagement incomplete and leave other vulnerabilities undiscovered.

---

### Question 13 (5 points)

A penetration test report includes a finding titled "Weak Password Policy." The description states that default credentials were accepted on the admin panel at `10.10.5.5`. Which additional component is most critically missing from this finding as described?

- A) A MITRE ATT&CK technique number cross-reference
- B) Evidence — a screenshot or tool output showing that the default credentials were actually accepted, with the tester's source IP and a timestamp
- C) A comparison to industry-average password policy statistics
- D) A reference to the penetration tester's professional certifications that qualify them to assess password policy

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Every finding requires verifiable evidence. A description alone — even a specific description — is an assertion without proof. The client's security team, auditors, and regulators need to see that the finding was actually confirmed: a screenshot showing the login succeeding with the default credentials, with the tester's IP address visible in browser developer tools or the URL bar, and a timestamp. Without evidence, the finding cannot be independently verified or used in a compliance audit.
  - Why A is incorrect: MITRE ATT&CK cross-references are valuable and recommended but are not one of the six required finding components. Their absence is a quality improvement opportunity, not a critical deficiency that invalidates the finding.
  - Why C is incorrect: Industry benchmark comparisons are informative context but are not a required finding component. The finding's severity is established by the CVSS score, the affected asset, and the demonstrated impact — not by comparison to industry averages.
  - Why D is incorrect: Tester credentials are documented in the report introduction or attestation block, not in individual findings. A finding's validity rests on its evidence, not the tester's credentials.

---

### Question 14 (5 points)

What is the purpose of the CVSS Environmental Score group, and when is it most appropriately used in a penetration test report?

- A) The Environmental Score adjusts the Base Score to reflect the importance of the affected asset and any security controls already in place in the specific deployment context — used when the tester knows details about the target environment's sensitivity and existing mitigations
- B) The Environmental Score is always required in PenTest+ compliant reports and replaces the Base Score entirely
- C) The Environmental Score measures how many threat actors are actively exploiting the vulnerability in the wild, expressed as a multiplier against the Base Score
- D) The Environmental Score is used only for physical security findings and does not apply to network or application vulnerabilities

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why A is correct: The CVSS Environmental metric group — Modified Base Metrics and Supplemental metrics — allows organizations to customize the score to reflect their specific deployment context. A vulnerability on a highly critical production server surrounded by no compensating controls warrants a higher effective risk than the same vulnerability on an isolated test server. Environmental scoring is optional but appropriate when the tester has sufficient context about asset criticality and existing controls to make the adjustment meaningful.
  - Why B is incorrect: The Environmental Score is optional, not mandatory. Many professional reports report only the Base Score, sometimes supplemented by a contextual risk rating narrative. The Base Score is never fully replaced by the Environmental Score — both can coexist.
  - Why C is incorrect: Active exploitation data is captured in the CVSS Temporal Score's Exploit Code Maturity (E) metric — not the Environmental Score. The Environmental Score adjusts for deployment context, not threat landscape activity.
  - Why D is incorrect: CVSS Environmental scoring applies to all vulnerability categories, not just physical security. It is most commonly used for network, application, and operating system vulnerabilities to reflect how the deployment environment affects exploitability and impact.

---

### Question 15 (5 points)

During report delivery, a client executive asks the penetration tester to remove a Critical finding from the report because "it will look bad during the upcoming audit." What is the correct professional response?

- A) Remove the finding from the technical report but note it verbally in the debrief session so there is no written record
- B) Offer to downgrade the finding from Critical to High as a compromise to satisfy the client's audit concern
- C) Decline to alter, suppress, or remove any confirmed finding — explain that the attestation statement certifies the accuracy and completeness of all findings, and that altering the report would compromise the integrity of the assessment
- D) Accept the request — the client owns the report and has the right to determine its final content

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The penetration test report is a professional attestation of the security state of the client's environment. Removing or altering confirmed findings under commercial pressure is a fundamental breach of professional ethics, potentially fraudulent, and could expose the tester to legal liability. The attestation statement specifically certifies that findings accurately represent the environment. A professional tester explains this obligation clearly and does not comply with requests to manipulate findings.
  - Why A is incorrect: Suppressing a written finding while noting it verbally is deceptive and creates a false record. If the finding is real, it must be in the written report. Verbal-only communication of critical security issues serves neither the client nor the tester professionally.
  - Why B is incorrect: Downgrading a confirmed Critical finding without technical justification is equally unprofessional. Severity ratings must reflect the actual technical characteristics of the vulnerability, not the client's political concerns about audits.
  - Why D is incorrect: While clients do receive the report as a deliverable, the content of the report reflects the tester's professional findings — not the client's desired narrative. Clients do not have editorial control over confirmed findings. If a client disputes a finding's accuracy, the appropriate process is a technical retest, not deletion.

---

### Question 16 (5 points)

Which report component is specifically designed to help an organization track remediation progress after the penetration test is complete?

- A) The executive summary
- B) The attestation block
- C) The remediation tracking matrix or action plan, which lists each finding with its risk rating, assigned owner, and target remediation date
- D) The methodology section

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: A remediation tracking matrix (sometimes called a remediation action plan or finding tracker) is a supplemental deliverable that converts findings into trackable work items. It includes the finding ID, risk rating, responsible team or owner, target completion date, and a status field. It is the bridge between the penetration test report and the client's project management process — enabling the security team to demonstrate progress to management and auditors after the engagement.
  - Why A is incorrect: The executive summary provides context and priorities but is not designed as a tracking tool. It lacks the granularity and status-tracking fields needed to manage remediation work items over time.
  - Why B is incorrect: The attestation block is a certification statement affirming that the engagement was conducted within scope and findings are accurate. It is a quality and legal document, not a project tracking tool.
  - Why D is incorrect: The methodology section describes how the test was conducted. It does not reference specific findings and provides no tracking mechanism for remediation activities.

---

### Question 17 (5 points)

A penetration test report is classified CONFIDENTIAL. Which delivery method is most appropriate?

- A) Email the PDF report as an unencrypted attachment to the primary client contact's standard corporate email address
- B) Post the report to the penetration testing firm's public website in a client portal section
- C) Deliver the report as a password-protected or encrypted file over a secure channel (such as encrypted email or a secure file sharing portal), with the decryption password or key transmitted separately through a different channel
- D) Print the report and mail a physical copy via standard postal service — physical delivery avoids digital interception risks entirely

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: CONFIDENTIAL documents must be delivered over secure channels that protect the data in transit. Encrypting the report file and delivering the decryption key through a separate channel (for example, the report via encrypted email and the password via phone or SMS) ensures that interception of either channel alone does not expose the contents. Secure file transfer portals with authentication provide equivalent protection. This is the professional standard for sensitive engagement deliverables.
  - Why A is incorrect: Unencrypted email attachments traverse multiple servers and can be intercepted, stored, or forwarded without the sender's knowledge. Delivering a CONFIDENTIAL report with vulnerability details via unencrypted email is a significant data handling failure.
  - Why B is incorrect: Posting client reports to any web-accessible portal — even a private client section — without strong access controls and encryption creates unacceptable exposure. Client-specific reports must never be accessible via a predictable URL or shared portal where they could be accessed by unauthorized parties.
  - Why D is incorrect: Physical mail is not a secure delivery method. Mail can be delayed, lost, or intercepted. Additionally, for reports containing technical vulnerability details, physical copies create additional storage and disposal challenges that digital encrypted delivery avoids.

---

### Question 18 (5 points)

In CVSS 3.1, what does a Privileges Required (PR) value of "None" indicate about a vulnerability?

- A) The vulnerability can only be exploited by a user with administrator or root privileges
- B) The attacker does not need any prior authentication or account on the target system to exploit the vulnerability — the attack can be launched anonymously
- C) The vulnerability requires physical proximity to the target and no network account is needed
- D) No privileges are needed on the attacker's own system — but the victim must be a privileged user for the attack to succeed

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Privileges Required (PR) in CVSS 3.1 measures the level of privileges the attacker must possess before exploiting the vulnerability. PR:None means the attacker needs no authentication at all — the attack works without logging into the target system. This is the highest-risk PR value because it removes the authentication barrier entirely, making the vulnerability exploitable by any anonymous actor on the network. PR:Low requires a basic user account; PR:High requires elevated (administrator/root) access.
  - Why A is incorrect: That description corresponds to PR:High — requiring elevated privileges before exploitation. PR:None is the opposite: no privileges whatsoever are required.
  - Why C is incorrect: Physical proximity is captured in the Attack Vector (AV) metric, specifically AV:Physical. PR:None refers to authentication requirements, not physical access requirements.
  - Why D is incorrect: PR measures what the attacker needs, not what the victim must have. Whether the victim is privileged is captured in other metrics (User Interaction and Impact). PR:None means the attacker needs nothing to begin exploiting — not that the victim must have privileges.

---

### Question 19 (5 points)

A penetration tester calculates a CVSS 3.1 Base Score of 7.5 (High) for a finding, but notes that the vulnerability exists only on a system with multiple network-layer compensating controls that would require an attacker to first compromise two other systems. The tester reports the finding as Medium risk and documents the justification. Which of the following best describes this practice?

- A) Improper — CVSS Base Scores are absolute and may never be adjusted in a professional report
- B) Appropriate — contextual risk rating allows the tester to reflect the effective business risk after accounting for compensating controls and exploitation complexity beyond what CVSS Base metrics capture, provided the adjustment is documented with specific justification
- C) Appropriate only if the client's legal team approves the rating adjustment in writing before the report is finalized
- D) Improper — risk ratings may only be increased above the CVSS Base Score, never decreased

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: CVSS Base Scores measure the inherent severity of a vulnerability independent of deployment context. They do not account for compensating controls, network segmentation, or multi-step exploitation chains that significantly reduce real-world exploitability. Professional reporting standards recognize that effective business risk can differ from the raw Base Score. Adjusting the reported risk rating (up or down) is accepted practice when the adjustment is clearly documented with technical justification — the tester must explain what compensating controls exist and why they reduce the effective risk. Without documentation, the adjustment is inappropriate.
  - Why A is incorrect: CVSS Base Scores are a starting point, not an absolute final answer. The CVSS specification itself acknowledges that organizations should use Environmental and Temporal metrics to adjust scores for context. Contextual risk adjustments in professional reports are a recognized and encouraged practice.
  - Why C is incorrect: Risk rating adjustments are the tester's professional judgment, not a legal negotiation requiring client legal team approval. Requiring legal approval for technical findings would compromise the tester's independence. The justification must be technical, not political.
  - Why D is incorrect: Risk ratings can be adjusted in either direction — upward when the deployment context makes exploitation more likely or impactful than the Base Score suggests, or downward when compensating controls materially reduce the effective risk. The CVSS Environmental Score supports both types of adjustment.

---

### Question 20 (5 points)

Which section of a penetration test report would a compliance auditor reviewing the organization's PCI DSS Requirement 11.3 controls primarily reference to verify that a qualified penetration test was conducted?

- A) The findings summary table listing all discovered vulnerabilities
- B) The executive summary describing the overall risk posture
- C) The scope verification and methodology section, combined with the attestation statement, which confirms what was tested, how it was tested, the tester's qualifications, and that the engagement was conducted within the authorized scope
- D) The appendix containing raw tool output and scan logs

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: A PCI DSS auditor reviewing Requirement 11.3 compliance needs to verify that a qualified penetration tester conducted a test meeting specific criteria: scope covered the cardholder data environment, both internal and external testing was performed, segmentation controls were validated, and the methodology included application-layer testing. These elements are documented in the scope verification section, methodology section, and attestation statement — not primarily in the findings list or the executive summary. The attestation confirms that the engagement was conducted by a qualified tester as described.
  - Why A is incorrect: The findings list shows what was discovered but does not demonstrate the scope, methodology, or tester qualifications that an auditor needs to confirm PCI DSS compliance with Requirement 11.3. A test with no findings does not mean no test was conducted — but the compliance evidence lies in the methodology and attestation.
  - Why B is incorrect: The executive summary provides business context and risk narrative. It is not the audit evidence section. It does not typically contain the scope boundary details, tester qualifications, or compliance attestation that an auditor requires.
  - Why D is incorrect: Raw tool output in the appendix is supporting evidence for specific findings. It does not document the overall scope, methodology, or professional attestation that PCI DSS auditors require to confirm Requirement 11.3 compliance.

---

*End of Module 14 Quiz*
