# Quiz: Module 15 - Security Metrics and KPIs
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
Why is establishing pre-defined incident escalation pathways critical in security governance?
*   A) To prevent security analysts from needing to learn any technical skills during incident response
*   B) To ensure that security breaches of sufficient severity are reported to appropriate executive management and legal teams within regulatory timelines and before opportunities for mitigation are missed
*   C) To reduce the number of incidents classified as high-severity by routing them through additional review steps
*   D) To ensure that all security alerts are acknowledged by the help desk before reaching the security operations center
*   **Correct Answer:** B) Pre-defined escalation ensures critical incidents receive executive attention and regulatory notifications are met on time — delays caused by ad hoc decisions are a primary governance failure in incident management.
*   **Distractor Analysis:**
    *   *Why B is correct:* Escalation governance ensures the right people are informed at the right time — a core CISM Domain 4 principle. Pre-definition prevents delay caused by individual judgment under pressure.
    *   *Why A is incorrect:* Technical skills remain essential for incident responders; escalation pathways govern communications and authority, not analyst competency.
    *   *Why C is incorrect:* Escalation pathways should ensure high-severity incidents receive more attention, not less; down-classifying incidents is a governance failure.
    *   *Why D is incorrect:* Routing all alerts through the help desk before the SOC introduces unnecessary delay and is not a security governance best practice.

---

**Question 2**
Which of the following most accurately describes **communication logs** in the context of incident response governance?
*   A) System access logs that record all user authentication events during normal operations
*   B) Documented records of all notifications and communications made to internal stakeholders, regulators, affected individuals, and external parties during a security incident
*   C) The audit trail created by a SIEM platform that correlates security events from multiple log sources
*   D) Network traffic captures used by forensic analysts to reconstruct how an attacker moved through the environment
*   **Correct Answer:** B) Communication logs document who was notified, when, what information was shared, and who authorized each communication — they are evidence of governance compliance during incident management.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Authentication logs are system logs; communication logs record incident-related human communications, not authentication events.
    *   *Why B is correct:* During an incident, documented communications serve as evidence that regulatory notification obligations were met and that the response was properly coordinated.
    *   *Why C is incorrect:* SIEM correlation is a technical security monitoring function; it produces alerts and event records, not incident communication documentation.
    *   *Why D is incorrect:* Network traffic captures (PCAPs) are forensic technical evidence; they are distinct from incident communication records.

---

**Question 3**
An organization discovers a ransomware attack has encrypted employee PII and ePHI. The incident occurred on a Tuesday. By what day must the organization notify the relevant EU supervisory authority (GDPR) and when must affected HIPAA-covered patients be notified?
*   A) GDPR: within 7 days; HIPAA: within 30 days
*   B) GDPR: within 72 hours (Friday); HIPAA: within 60 days
*   C) GDPR: within 30 days; HIPAA: within 72 hours
*   D) Both regulations require notification within 72 hours
*   **Correct Answer:** B) GDPR requires supervisory authority notification within 72 hours of discovery; HIPAA requires notification to individuals within 60 days of discovery.
*   **Distractor Analysis:**
    *   *Why B is correct:* These are the legally specified timelines — GDPR's 72-hour clock (Article 33) is dramatically faster than HIPAA's 60-day individual notification window (45 CFR § 164.404).
    *   *Why A is incorrect:* GDPR's requirement is 72 hours, not 7 days; HIPAA's requirement is 60 days, not 30.
    *   *Why C is incorrect:* This reverses the two regulatory timelines; GDPR is the faster requirement.
    *   *Why D is incorrect:* HIPAA does not require notification within 72 hours; GDPR's 72-hour requirement applies to supervisory authorities, not necessarily affected individuals.

---

**Question 4**
A security incident has been contained and eradicated. The CISO proposes moving immediately to other priorities without conducting a formal post-incident review. What is the most significant risk of skipping this step?
*   A) The legal team will lack documentation to support any potential breach notification filings
*   B) The organization misses the primary opportunity to identify root causes, improve controls, and prevent recurrence — the post-incident review is the mechanism that drives security program improvement
*   C) The incident responders will not receive performance recognition without a formal review document
*   D) The organization will fail its next ISO 27001 surveillance audit due to missing paperwork
*   **Correct Answer:** B) Post-incident reviews identify root causes and generate actionable improvements — skipping them means the organization will likely face similar incidents again without having addressed the underlying failures.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Breach notification requirements are separate from post-incident reviews; notifications are made based on discovery, not completion of a review.
    *   *Why B is correct:* NIST SP 800-61 and CISM Domain 4 both establish post-incident activity as essential — it converts incidents from costs into learning opportunities that strengthen the security program.
    *   *Why C is incorrect:* Performance recognition is not the purpose of post-incident reviews; security improvement is.
    *   *Why D is incorrect:* While ISO 27001 does require continual improvement evidence, the more immediate and significant risk is the missed opportunity to prevent recurrence.

---

**Question 5**
During a post-incident review, the team discovers that a critical server was compromised due to an unpatched vulnerability that had been identified in a risk assessment 90 days earlier but was deprioritized due to resource constraints. What governance lesson does this finding illustrate?
*   A) Vulnerability assessments should be conducted less frequently to avoid generating more work than can be addressed
*   B) Risk acceptance decisions require formal documentation with management sign-off on residual risk; undocumented deprioritization represents an unmanaged risk, not a formal acceptance
*   C) Technical teams should be given full authority to independently decide which vulnerabilities require patching
*   D) The post-incident review finding should not be disclosed outside the security team to protect the organization from liability
*   **Correct Answer:** B) "Deprioritizing" a known risk without formal documentation and management acceptance is a governance failure — the organization incurred the harm of a risk it had identified but failed to formally decide how to manage.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Reducing assessment frequency would only create more blind spots; the problem is the governance of identified risks, not the identification rate.
    *   *Why B is correct:* CISM governance requires that identified risks be formally accepted (with sign-off) or treated; informal deprioritization without documentation is not risk acceptance — it is negligence.
    *   *Why C is incorrect:* Risk acceptance decisions require management authority; technical teams identify and recommend but do not independently accept business risk.
    *   *Why D is incorrect:* Concealing findings from leadership violates governance principles and potentially regulatory disclosure obligations; post-incident transparency is essential for organizational learning.
