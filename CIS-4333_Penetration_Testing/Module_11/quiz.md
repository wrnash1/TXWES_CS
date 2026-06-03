# Quiz: Module 11 — Social Engineering Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

A penetration tester is authorized to conduct a phishing campaign against a healthcare organization. The tester plans to use a pretext claiming that an employee's health insurance is expiring unless they verify their benefits online. Which ethical concern MOST directly applies?

A. The pretext will not achieve a high enough click rate to be statistically significant.

B. The pretext exploits personal health anxieties and may cause undue distress to vulnerable employees.

C. The pretext requires spoofing the insurance provider's domain, which is unauthorized.

D. Healthcare organizations are exempt from social engineering testing under HIPAA.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Statistical significance is a methodology concern, not an ethical concern. Many effective pretexts achieve high click rates while remaining within ethical bounds.
- B is correct. Pretexts that target health anxieties can cause genuine distress to employees managing health conditions, create lasting mistrust of HR/benefits communication, and disproportionately impact vulnerable individuals. This crosses an ethical line even when technically authorized.
- C is incorrect. Domain spoofing decisions are a separate operational concern. The pretext's content is the primary ethical issue here.
- D is incorrect. HIPAA does not prohibit social engineering testing. Security testing is not only permitted but encouraged for HIPAA-covered entities. The constraint comes from professional ethics, not HIPAA regulation.

---

**Question 2**

Which GoPhish template variable inserts a unique, individually trackable URL for each recipient?

A. `{{.Email}}`

B. `{{.TrackingURL}}`

C. `{{.URL}}`

D. `{{.CampaignID}}`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. `{{.Email}}` inserts the recipient's email address into the template text.
- B is incorrect. `{{.TrackingURL}}` is not a GoPhish template variable. This option tests knowledge of the actual GoPhish API.
- C is correct. `{{.URL}}` generates a unique per-recipient phishing URL that GoPhish uses to track individual click events.
- D is incorrect. `{{.CampaignID}}` is not a GoPhish template variable. Campaign identifiers are handled internally.

---

**Question 3**

During an authorized vishing engagement, an employee says: "I don't give out my password over the phone. Let me submit a helpdesk ticket instead." What is the BEST response that maintains the pretext while respecting ethical boundaries?

A. Tell the employee their account will be permanently locked if they do not comply immediately.

B. Acknowledge their security awareness, explain the urgency of the issue requires immediate action, and offer an alternative verification method.

C. Hang up and mark the call as failed since the target is too security-aware to test further.

D. Threaten to escalate to their manager for non-compliance with a security directive.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. While urgency is a legitimate social engineering technique, threats of permanent consequences that are entirely false cross into coercive manipulation that may harm the employee and is unlikely to be authorized.
- B is correct. Acknowledging the concern (genuine positive security behavior) while maintaining reasonable urgency pressure is ethical and realistic. Offering an alternative mirrors real attacker behavior and continues the test without coercion.
- C is incorrect. A target questioning the call and refusing to provide passwords is actually a positive security finding — good security behavior. Documenting this as a "resistant" response is valuable. Abandoning the call is appropriate, but marking it as merely "failed" misrepresents what happened.
- D is incorrect. Threatening escalation to management is a coercive technique that creates disproportionate workplace stress and is likely not within the authorized scope of a security test.

---

**Question 4**

A tester launches a phishing campaign at 9:00 AM and finds that 70% of all clicks occurred within the first 8 minutes. What does this finding indicate about the phishing email's effectiveness?

A. The campaign achieved a low click rate — effective security awareness training is evident.

B. The urgency element in the pretext was highly effective at driving immediate action without rational deliberation.

C. The email filtering system failed to quarantine high-volume spam, causing rapid delivery.

D. The GoPhish server was misconfigured and sent multiple copies of the email to each recipient.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Rapid clicks indicate effective social engineering, not effective security awareness. A high click rate combined with rapid response indicates the pretext created strong urgency.
- B is correct. Clicks within minutes of receipt indicate the recipient did not pause to scrutinize the email. Urgency-driven pretexts ("your account will be locked") are specifically designed to prevent deliberation. Rapid clicks are a key indicator of pretext effectiveness.
- C is incorrect. Email filtering behavior affects delivery but not click timing after delivery. Bypassing spam filters explains delivery, not why recipients clicked within 8 minutes.
- D is incorrect. Multiple email copies would show in the GoPhish campaign as multiple "email sent" events per recipient. This would be a configuration error, not a normal campaign result.

---

**Question 5**

An attacker leaves USB drives labeled "Q3 Salary Adjustments — Confidential" in a company parking lot. Employees who plug in the drives install malware. Which social engineering technique is this?

A. Pretexting

B. Shoulder surfing

C. Quid pro quo

D. Baiting

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect. Pretexting involves creating a fictional scenario through direct communication. The USB attack does not involve communication — it relies on physical objects.
- B is incorrect. Shoulder surfing involves observing sensitive information by watching over someone's shoulder. It requires physical proximity and is passive.
- C is incorrect. Quid pro quo involves offering something in exchange for information or access (e.g., "I'll help fix your computer if you give me your login"). The USB attack does not involve an exchange.
- D is correct. Baiting places physical or digital lures that exploit curiosity or greed. The "Salary Adjustments" label is designed to trigger curiosity compelling enough to override security judgment.

---

**Question 6**

Which email authentication record, when set to enforcement mode (`p=reject`), causes receiving servers to reject emails that fail SPF and DKIM checks?

A. SPF (Sender Policy Framework)

B. DKIM (DomainKeys Identified Mail)

C. DMARC (Domain-based Message Authentication, Reporting and Conformance)

D. DNSSEC (Domain Name System Security Extensions)

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. SPF specifies which IP addresses are authorized to send for a domain, but SPF alone does not define what action to take on failures. The action policy is defined in DMARC.
- B is incorrect. DKIM provides cryptographic signature verification of email content but does not define enforcement actions. DMARC uses DKIM pass/fail as an input to its enforcement decision.
- C is correct. DMARC's `p=` tag defines the policy: `none` (monitor), `quarantine` (spam folder), or `reject` (refuse delivery). Setting `p=reject` tells receiving servers to reject messages that fail DMARC evaluation.
- D is incorrect. DNSSEC secures DNS lookups against tampering. While important for overall DNS integrity, it is not the mechanism that enforces email authentication policy.

---

**Question 7**

A phishing campaign targeting 200 employees results in: 140 opens, 55 clicks, 28 credential submissions, and 12 reports to the IT helpdesk. What is the credential submission rate (as a percentage of emails sent)?

A. 50.9%

B. 20.0%

C. 14.0%

D. 8.6%

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. 50.9% would be 28 ÷ 55 (submissions ÷ clicks). This is the submission-to-click conversion rate, not the submission rate relative to emails sent.
- B is incorrect. 20% would represent 40 ÷ 200. This does not correspond to any of the campaign values.
- C is correct. Submission rate = submissions ÷ emails sent = 28 ÷ 200 = 14.0%.
- D is incorrect. 8.6% would be approximately 12 ÷ 140 (reports ÷ opens). This is not a standard phishing metric.

---

**Question 8**

During a spear phishing campaign, a tester discovers through LinkedIn that a target company recently completed a major Salesforce implementation. Which pretext would MOST effectively leverage this intelligence?

A. A generic "Your Microsoft account requires immediate verification" email.

B. An email from "Salesforce Support" regarding new security requirements following the recent deployment, with a link to verify admin credentials.

C. A phishing email claiming the target won a prize in a company raffle.

D. A vishing call about an expiring parking pass.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. A generic Microsoft account email is not spear phishing — it is mass phishing. It does not use any of the specific intelligence gathered about the organization.
- B is correct. Referencing the actual, recent Salesforce implementation makes the email credible and timely. Employees who just lived through an implementation expect follow-up communications. The "security requirements" pretext is plausible for a fresh deployment.
- C is incorrect. A prize raffle email does not leverage the Salesforce intelligence and is a generic lure rather than targeted spear phishing.
- D is incorrect. A parking pass vishing call is unrelated to the Salesforce intelligence and would not benefit from the specific organizational knowledge gathered.

---

**Question 9**

Which federal law creates civil and criminal liability for making false statements to obtain financial information from a financial institution, regardless of security testing authorization?

A. Computer Fraud and Abuse Act (18 U.S.C. § 1030)

B. Electronic Communications Privacy Act (18 U.S.C. § 2511)

C. Gramm-Leach-Bliley Act pretexting provisions (15 U.S.C. § 6821)

D. CAN-SPAM Act (15 U.S.C. § 7701)

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. The CFAA addresses unauthorized computer access. While relevant to social engineering testing, it does not specifically address pretexting to obtain financial information from institutions.
- B is incorrect. The ECPA addresses interception of electronic communications. It is relevant to wiretapping and email monitoring, not specifically to pretexting financial institutions.
- C is correct. The GLBA's pretexting provisions (15 U.S.C. § 6821) specifically prohibit using false, fictitious, or fraudulent statements to obtain customer financial information from financial institutions. This applies even in authorized testing if the pretext involves impersonating customers or employees of financial institutions.
- D is incorrect. The CAN-SPAM Act governs commercial email practices. It does not address pretexting or obtaining financial information.

---

**Question 10**

After completing a phishing campaign, a tester's report identifies 12 employees who submitted credentials, listed by name and department. The client's CISO asks the tester to share this list with HR so managers can be informed. What is the BEST course of action?

A. Immediately share the full list with HR as the CISO has the authority to direct this.

B. Refuse to share any individual data since it violates the employees' privacy rights.

C. Confirm whether the scope of work pre-authorized individual-level disclosure to HR and follow the documented protocol.

D. Share the list only if all 12 employees receive security awareness training first.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. The CISO's authority is real, but the penetration test report should follow the data handling and disclosure protocols agreed upon in the scope of work. Sharing individual data not covered by the scope creates liability and trust issues.
- B is incorrect. Employees working for an organization that authorized testing do not have an absolute privacy right to non-disclosure of test results to authorized stakeholders. The constraint is contractual (scope of work), not absolute privacy law.
- C is correct. The scope of work should define exactly what individual-level data is shared, with whom, and under what conditions. This is a standard social engineering engagement consideration. Confirm the protocol; follow it.
- D is incorrect. Conditioning data sharing on training completion is not a security testing principle. Training is a remediation action, not a prerequisite for reporting.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | C |
| 3 | B |
| 4 | B |
| 5 | D |
| 6 | C |
| 7 | C |
| 8 | B |
| 9 | C |
| 10 | C |
