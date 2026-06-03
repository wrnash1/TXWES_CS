# Quiz: Module 13 — Penetration Test Report Writing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

A penetration test finds an unpatched Apache Struts server (CVE-2017-5638, CVSS 10.0) in the company's DMZ. The system hosts a static marketing website with no sensitive data. The tester believes the appropriate report severity is High, not Critical. Which CVSS metric group should be used to document this contextual adjustment?

A. Base Metrics — adjust Confidentiality Impact to None.

B. Temporal Metrics — adjust Exploit Code Maturity to Unproven.

C. Environmental Metrics — adjust the Confidentiality, Integrity, and Availability Requirements.

D. There is no valid mechanism to adjust a 10.0 score downward in the report.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. Base Metrics reflect the intrinsic vulnerability characteristics, which do not change based on the specific deployment context. Adjusting Base Metrics to reflect context is a misuse of the framework.
- B is incorrect. Temporal Metrics reflect exploit availability and remediation status — characteristics that exist independent of this deployment. CVE-2017-5638 has public exploit code, so lowering Exploit Code Maturity would be inaccurate.
- C is correct. Environmental Metrics, specifically the Modified Impact Subscore and the CIA Requirements (CR, IR, AR), allow the tester to reflect the specific deployment context. A static marketing site with no sensitive data would have Confidentiality Requirement: Low, reducing the environmental score.
- D is incorrect. The CVSS framework explicitly includes Environmental Metrics for this purpose. A 10.0 Base Score can legitimately produce a lower Environmental Score when CIA Requirements are reduced.

---

**Question 2**

Which section of a penetration test report would a CISO turn to first when they have 10 minutes before a board meeting and need to understand the overall security posture?

A. Technical Findings section

B. Executive Summary

C. Assessment Scope and Methodology

D. Appendix — Vulnerability Index

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The Technical Findings section is written for technical staff with detailed vulnerability descriptions and remediation guidance. A CISO preparing for a board meeting needs high-level business-impact information.
- B is correct. The Executive Summary is explicitly designed for non-technical and time-limited stakeholders. It provides scope, overall posture, key findings in plain language, and priority actions — exactly what is needed for a board briefing.
- C is incorrect. The Scope and Methodology section documents what was tested and how. It does not communicate risk level or findings.
- D is incorrect. The Vulnerability Index is a reference appendix for tracking remediation progress. It lists findings but without the business context and overall narrative needed for a board briefing.

---

**Question 3**

A penetration tester calculates the following CVSS 3.1 vector: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N. What qualitative severity rating does this produce?

A. Critical

B. High

C. Medium

D. Low

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Critical requires a score of 9.0 or above. This vector produces a score of approximately 7.5 because Scope is Unchanged and only Confidentiality is High with no Integrity or Availability impact.
- B is correct. AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N calculates to approximately 7.5 (High). The key factors limiting the score: Scope Unchanged (preventing the score boost from a Changed scope), no Integrity impact, and no Availability impact.
- C is incorrect. Medium scores range from 4.0 to 6.9. Network-exploitable, no authentication, High Confidentiality impact produces a score above the Medium ceiling.
- D is incorrect. Low scores range from 0.1 to 3.9. This vector has multiple high-severity characteristics that place it well above this range.

---

**Question 4**

An executive summary states: "The penetration test revealed critical vulnerabilities that will inevitably be exploited by nation-state actors within weeks, potentially destroying the company's ability to operate." What is wrong with this statement?

A. It is too long for an executive summary.

B. It uses speculation and alarmist language instead of evidence-based risk statements.

C. It refers to threat actors, which should only appear in the technical findings section.

D. It does not include a CVSS score to support the claim.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Length is not the primary issue with this statement. The problem is the content and tone.
- B is correct. "Will inevitably be exploited" and "within weeks" are speculative claims not supported by evidence. "Nation-state actors" requires threat intelligence context. "Potentially destroying the company" is alarmist. Professional reports state risk based on evidence: "These vulnerabilities are easily exploitable using publicly available tools and create significant risk of unauthorized access to customer data."
- C is incorrect. Threat actor references can appear in executive summaries to provide context. The problem here is not the reference to threat actors but the unsupported specificity ("nation-state," "within weeks").
- D is incorrect. Executive summaries do not include CVSS scores — those are in the technical findings section. The problem is language quality, not missing metrics.

---

**Question 5**

A penetration tester finds evidence of a Critical vulnerability during a test but the client's security manager asks the tester to omit it from the report because "it would cause panic in the executive team." What is the correct response?

A. Omit the finding but include it in a separate confidential addendum delivered only to the security manager.

B. Downgrade the finding to High so it remains in the report but with reduced alarm.

C. Decline to omit the finding. Document it accurately and offer to present it to the executive team with appropriate context.

D. Include the finding but categorize it as "Informational" to reduce its prominence.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. A separate addendum delivered only to the security manager is not a professional resolution — it creates an incomplete official report and raises liability questions. Omitting a Critical finding from the client's primary report deliverable is a professional integrity violation.
- B is incorrect. Downgrading a finding from Critical to High without evidence-based justification is dishonest reporting. Risk ratings must be based on technical and business evidence, not on stakeholder preferences.
- C is correct. The tester's obligation is to report findings accurately. A professional response offers to present the finding to executives with appropriate context — explaining risk in business terms, providing actionable remediation steps, and framing it constructively. The finding remains in the report.
- D is incorrect. Categorizing a confirmed Critical finding as Informational is a significant misrepresentation. Informational findings are observations without direct security impact. This would be deliberately misleading.

---

**Question 6**

Which of the following best demonstrates the correct executive-level translation of: "The IIS 7.5 server at 10.10.2.45 is vulnerable to CVE-2015-1635 (MS15-034), enabling remote kernel-level code execution via HTTP Range header overflow."?

A. "CVE-2015-1635 represents a kernel-level RCE vulnerability in Microsoft IIS 7.5 with a CVSS score of 10.0."

B. "The company's internal web server has an unpatched flaw that allows an attacker to take complete control of the server without a password. This server should be patched immediately."

C. "HTTP Range header processing in IIS 7.5 is subject to heap buffer overflow conditions in the kernelmode HTTP.sys driver."

D. "A web server vulnerability was identified. Please contact IT for remediation details."

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. This maintains technical language (CVE identifier, RCE, CVSS score) without translation. An executive reading this would not understand the business implication.
- B is correct. This translation uses plain language ("unpatched flaw," "complete control," "without a password"), communicates the business impact, and provides a clear action item. It requires no technical background to understand.
- C is incorrect. This is more technical than the original finding description. It uses kernel, heap buffer overflow, and driver — all technical terms requiring security knowledge.
- D is incorrect. While plain in language, this is too vague to be useful. An executive cannot evaluate urgency, business impact, or appropriate escalation from this description.

---

**Question 7**

A finding has the CVSS vector AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H. Which statement BEST describes what this vector represents?

A. A remotely exploitable vulnerability requiring no authentication that gives an attacker full system control.

B. A locally exploitable vulnerability requiring low-privilege authentication that gives an attacker full control of the affected system.

C. A physically-accessible vulnerability requiring high-privilege authentication that impacts confidentiality only.

D. A network vulnerability that requires user interaction and affects availability only.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. AV:L indicates Local attack vector, not Network (AV:N). The attack requires local access, not remote.
- B is correct. AV:L = Local access required, AC:L = no special conditions, PR:L = low-privilege account needed, UI:N = no user interaction, S:U = unchanged scope, C/I/A:H = complete impact on all three CIA dimensions. This matches a local privilege escalation vulnerability.
- C is incorrect. AV:P is Physical; this vector shows AV:L (Local). Physical requires hands-on access to the hardware. PR:H would be high privilege; this shows PR:L (low privilege). C:H alone contradicts I:H/A:H.
- D is incorrect. AV:N is Network; this vector shows AV:L. UI:R is Required; this shows UI:N. A:H means High availability impact, but C:H and I:H also apply.

---

**Question 8**

A client's security team disputes a High-rated finding, arguing that they have a compensating control (a web application firewall rule blocking the attack payload). They want to lower the finding's risk rating. What is the MOST appropriate response in the report?

A. Downgrade the finding to Medium and note the WAF in the remediation section.

B. Remove the finding since the compensating control eliminates the exploitability.

C. Keep the High rating in the finding body. Add a "Compensating Controls" note documenting the WAF rule, and recommend verifying WAF rule effectiveness and ensuring the rule is maintained.

D. Keep the High rating and do not acknowledge the client's compensating control, since CVSS does not account for mitigations.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. The CVSS base score reflects the vulnerability's inherent severity, which does not change because the client has deployed a compensating control. A compensating control is temporary mitigation, not remediation. The underlying vulnerability remains.
- B is incorrect. A compensating control does not eliminate a vulnerability — it reduces the attack surface. WAF rules can be bypassed, disabled, or circumvented. The finding remains valid until the underlying vulnerability is remediated.
- C is correct. The finding's base risk rating reflects the vulnerability's severity. The compensating control is documented as a mitigating factor — acknowledging that the client has reduced immediate exploitability while noting that the underlying vulnerability persists and the compensating control requires maintenance.
- D is incorrect. Acknowledging compensating controls is appropriate professional practice. Ignoring relevant client context would be dismissive and would undermine the report's credibility. The base score is not lowered, but the compensating control is documented.

---

**Question 9**

When transmitting a completed penetration test report to a client, which method is MOST appropriate?

A. Unencrypted email attachment since the report is already password-protected.

B. Encrypted email using PGP/GPG or an encrypted file transfer portal with delivery confirmation.

C. Personal Google Drive link shared with the client's email address.

D. Printed physical copies only, hand-delivered to the client's CISO.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. A password on a PDF provides basic protection but transmitting it via unencrypted email means the file travels through multiple mail servers in potentially unencrypted form. Standard professional practice requires secure transmission.
- B is correct. PGP-encrypted email or a dedicated encrypted file transfer portal ensures the report is protected in transit, provides delivery confirmation, and creates an audit trail. This is the industry standard for delivering sensitive assessment reports.
- C is incorrect. Personal Google Drive is a consumer service with terms of service that may permit Google to scan content, lacks professional audit trails, and is not appropriate for confidential client security data.
- D is incorrect. Physical delivery is impractical and does not create a digital record. Most clients need a digital report for distribution to their technical team and for tracking remediation. Physical-only delivery is not standard practice.

---

**Question 10**

A tester documents a finding with the following remediation recommendation: "Fix the SQL injection vulnerability." This remediation recommendation is inadequate. Which revised version meets professional standards?

A. "SQL injection is a well-known vulnerability class. The development team should research OWASP guidance."

B. "Apply parameterized queries or prepared statements to all database interactions in the application. Specifically, remediate the `username` parameter in the `/login.php` endpoint. Deploy input validation as a defense-in-depth measure. Consider deploying a WAF as an interim compensating control."

C. "The development team must immediately patch all SQL injection vulnerabilities within 24 hours or risk regulatory penalties."

D. "Update the application framework to the latest version, which may include SQL injection protections."

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Directing the client to research a standard is not actionable remediation guidance. The client should not have to research how to fix their own system based on the assessment report.
- B is correct. This recommendation is specific (parameterized queries, the specific affected parameter and file), actionable (a technical team can implement this immediately), tiered (includes an interim compensating control), and complete.
- C is incorrect. Threatening regulatory penalties is speculative and unprofessional. The 24-hour timeline may not be realistic. The tone is coercive rather than helpful.
- D is incorrect. "Updating the framework" is vague and may not address the specific SQL injection vulnerability. If an update is relevant, the specific framework, current version, and target version must be cited.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | C |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | C |
| 6 | B |
| 7 | B |
| 8 | C |
| 9 | B |
| 10 | B |
