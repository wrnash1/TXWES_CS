# Quiz: Module 15 - Reporting – Writing Professional Pentest Reports
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Why is post-engagement cleanup a required phase of every professional penetration test?
*   A) To improve the target network's performance by removing scanning traffic and temporary connections.
*   B) To ensure all backdoors, shells, persistence mechanisms, created accounts, and uploaded tools are removed — leaving the client's environment in its pre-test state so real attackers cannot leverage artifacts left by the tester.
*   C) To give the penetration tester time to compile screenshots and organize notes before writing the report.
*   D) To reset the engagement scope documentation so the client can request a follow-up test at no additional cost.
*   **Correct Answer:** B) To ensure all backdoors, shells, persistence mechanisms, created accounts, and uploaded tools are removed — leaving the client's environment in its pre-test state so real attackers cannot leverage artifacts left by the tester.
*   **Distractor Analysis:**
    *   *Why B is correct:* Cleanup is a professional and ethical obligation. Backdoors, shells, and persistence mechanisms installed during testing are fully functional attack tools. If left in place, real attackers could discover and use them — potentially causing more harm than the original vulnerabilities the tester was hired to find. Testers provide written attestation confirming all artifacts have been removed, which protects both the tester and the client legally.
    *   *Why A is incorrect:* While testing activities do generate network traffic, performance improvement is not the reason for cleanup. Cleanup focuses on removing persistent access artifacts — not optimizing bandwidth or clearing connection state.
    *   *Why C is incorrect:* Note organization and screenshot compilation are documentation tasks that occur throughout the engagement — not post-engagement cleanup activities. Cleanup is specifically about removing attack tools and access mechanisms from client systems.
    *   *Why D is incorrect:* Cleanup has no relationship to scope documentation or follow-up engagement pricing. It is a security-focused activity that restores the target environment to its original state, independent of any commercial considerations.

---

**Question 2**
In the context of professional pentest reporting, which of the following best defines the **Executive Summary**?
*   A) A detailed technical section listing each vulnerability with its CVE number, CVSS score, affected IP addresses, exploitation steps, and specific patch or configuration remediation guidance.
*   B) A non-technical section written for senior leadership and executives that describes the overall security risk posture, most critical findings in business terms, and high-level remediation priorities without requiring security expertise to understand.
*   C) A section documenting the testing methodology, phases executed, tools used, and dates of testing activity — written for quality assurance review and audit purposes.
*   D) An appendix containing raw tool output, full scan logs, and supporting evidence screenshots referenced by the technical findings section.
*   **Correct Answer:** B) A non-technical section written for senior leadership and executives that describes the overall security risk posture, most critical findings in business terms, and high-level remediation priorities without requiring security expertise to understand.
*   **Distractor Analysis:**
    *   *Why B is correct:* The Executive Summary bridges the gap between technical security testing and business decision-making. Executives need to understand the risk in terms of potential financial loss, regulatory penalties, operational disruption, and reputational damage — not CVE numbers or exploit commands. A well-written executive summary answers: "How exposed are we? What are the biggest risks? What should we prioritize fixing?" PT0-002 tests the distinction between this section and the technical findings.
    *   *Why A is incorrect:* This describes the Technical Findings section — the detailed, remediation-focused content written for IT and security engineers. It is the opposite of non-technical audience writing.
    *   *Why C is incorrect:* This describes the Methodology section, which documents the engagement process for quality assurance purposes. It is written for peer review and audit, not for executive decision-making.
    *   *Why D is incorrect:* This describes the Appendix — supplementary technical reference material. It is the most technical section of the report and entirely inappropriate for a non-technical executive audience.

---

**Question 3**
A penetration tester discovers a remotely exploitable vulnerability in a public-facing web server. It requires no authentication, allows full OS command execution, and has been confirmed exploitable. Using CVSS v3.1 scoring criteria, what severity range should this finding be rated?
*   A) Medium (4.0–6.9) — web application vulnerabilities are typically medium severity by default.
*   B) Low (0.1–3.9) — the vulnerability only affects the web server tier and not the entire network.
*   C) High (7.0–8.9) — remote exploitation without authentication qualifies as High but not Critical.
*   D) Critical (9.0–10.0) — remotely exploitable, no authentication required, full system impact across Confidentiality, Integrity, and Availability.
*   **Correct Answer:** D) Critical (9.0–10.0) — remotely exploitable, no authentication required, full system impact across Confidentiality, Integrity, and Availability.
*   **Distractor Analysis:**
    *   *Why D is correct:* CVSS v3.1 Base Scores reaching 9.0–10.0 require maximum scores across the Exploitability metrics: Attack Vector = Network (remotely accessible), Attack Complexity = Low (no special conditions), Privileges Required = None (no authentication), User Interaction = None, with High impact on Confidentiality, Integrity, and Availability. A confirmed remote command execution vulnerability with no authentication required and full system control satisfies all of these conditions and warrants a Critical rating.
    *   *Why A is incorrect:* Vulnerability tier (web, network, OS) does not determine CVSS severity by itself. A remotely exploitable, unauthenticated OS command execution on any tier scores Critical based on its Exploitability and Impact metrics, not its application layer.
    *   *Why B is incorrect:* CVSS scores are not discounted because a vulnerability affects a single component. Scope and blast radius are assessed separately. Full OS command execution is a maximum-impact finding regardless of network segmentation.
    *   *Why C is incorrect:* A High rating (7.0–8.9) typically applies when one or more factors reduce the score — for example, Privileges Required = Low, or Attack Complexity = High. With all factors at their maximum exploitability and full impact, the score reaches Critical. No authentication + network access + full impact = Critical.

---

**Question 4**
A penetration tester documents a finding in the technical findings section of a report. Which of the following components is essential for a complete, professional technical finding?
*   A) The tester's personal opinion about whether the finding is realistic for a real-world attacker to exploit.
*   B) A severity rating with CVSS score, description of the vulnerability, evidence of exploitation (screenshots/output), affected systems, business impact, and specific remediation recommendations.
*   C) A list of all other organizations that have been affected by the same vulnerability, to demonstrate industry prevalence.
*   D) The full source code of the exploit used during testing, so the client's developers can understand the underlying vulnerability mechanism.
*   **Correct Answer:** B) A severity rating with CVSS score, description of the vulnerability, evidence of exploitation (screenshots/output), affected systems, business impact, and specific remediation recommendations.
*   **Distractor Analysis:**
    *   *Why B is correct:* A professional technical finding must be complete, actionable, and evidence-based. The severity rating (with CVSS justification) sets remediation priority. The description explains what the vulnerability is and why it exists. Evidence (screenshots, command output) proves the finding is real and reproducible, not a false positive. Affected systems scope the remediation effort. Business impact explains why it matters. Specific remediation recommendations tell the client exactly what to do — vague guidance like "patch the server" is insufficient.
    *   *Why A is incorrect:* Professional reports present confirmed, evidence-based findings — not subjective opinions about exploitability likelihood. If a vulnerability was confirmed exploitable during testing, it is documented as such based on evidence.
    *   *Why C is incorrect:* Industry prevalence data may appear in supplementary context but is not a required component of an individual technical finding. The finding documents what was found in this specific engagement, not what has been found elsewhere.
    *   *Why D is incorrect:* Including full exploit source code in a client report creates unnecessary risk — the report itself becomes a ready-to-use attack toolkit if it falls into the wrong hands. Reports reference the vulnerability and exploitation method conceptually, not as executable code.

---

**Question 5**
After delivering a pentest report, the client's CISO reviews a High-severity finding and informs the tester that the organization has evaluated the risk and decided not to remediate it due to the cost and operational complexity of the fix. What is the appropriate professional response from the tester?
*   A) Remove the finding from the final report — undocumented risks that the client has acknowledged are not the tester's responsibility.
*   B) Escalate the finding to Critical severity in the report to compel the client to remediate it.
*   C) Document the finding as "Risk Accepted by Client" in the report with the date and name of the authorizing stakeholder, preserving the finding and the client's decision as an audit trail.
*   D) Refuse to submit the final report until the client agrees to remediate all High and Critical findings.
*   **Correct Answer:** C) Document the finding as "Risk Accepted by Client" in the report with the date and name of the authorizing stakeholder, preserving the finding and the client's decision as an audit trail.
*   **Distractor Analysis:**
    *   *Why C is correct:* Risk acceptance is a legitimate and common business decision — organizations regularly accept residual risks that are too costly or disruptive to fully remediate. The tester's role is to identify and document risks, not to mandate remediation. When a client formally accepts a risk, the tester documents this in the report — noting who accepted it, when, and under what conditions. This creates an audit trail that protects both parties and ensures the finding is not simply forgotten or lost.
    *   *Why A is incorrect:* Removing a finding because the client chose not to remediate it falsifies the report and exposes the tester to professional and legal liability. A pentest report must accurately reflect all findings regardless of remediation decisions. Removing confirmed findings is unethical and violates professional standards.
    *   *Why B is incorrect:* Severity ratings must reflect the actual technical risk of a vulnerability based on CVSS criteria — they cannot be manipulated to pressure clients into remediation decisions. Artificially inflating severity damages the tester's credibility and misrepresents the technical reality.
    *   *Why D is incorrect:* The tester's contractual obligation is to conduct the assessment and deliver findings — not to enforce remediation. Refusing to submit the report would breach the engagement contract. The client retains the right to make risk management decisions about their own environment.
