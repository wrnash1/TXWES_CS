# Reading Guide: Module 14 — Legal, Compliance, and Contractual Considerations

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

This module examines the legal, contractual, and compliance framework governing authorized penetration testing. Understanding this framework is not optional — it is a prerequisite for professional practice. All activities described in this course require proper authorization documented in appropriate legal agreements.

---

## Learning Objectives

After completing this module, students will be able to:

1. Explain the Computer Fraud and Abuse Act's application to authorized and unauthorized testing.
2. Identify the required components of a penetration testing scope of work.
3. Distinguish between the SOW and rules of engagement documents.
4. Explain the provisions of a typical NDA in the testing context.
5. Describe liability, indemnification, and professional insurance requirements.
6. Explain bug bounty programs and responsible disclosure processes.
7. Map legal and contractual knowledge to PT0-002 Domain 1 exam objectives.

---

## Section 1: Federal Legal Framework

### 1.1 Computer Fraud and Abuse Act (18 U.S.C. § 1030)

The CFAA is the primary federal statute governing computer crimes. It applies to any computer connected to the internet (a "protected computer" as defined in 18 U.S.C. § 1030(e)(2)(B)).

Key provisions:

**§ 1030(a)(2):** Prohibits intentional unauthorized access to obtain information from financial institutions, U.S. government computers, or any protected computer. Penalties: up to 5 years imprisonment (10 years for repeat offenses).

**§ 1030(a)(3):** Prohibits intentional unauthorized access to non-public U.S. government computers.

**§ 1030(a)(5):** Prohibits knowingly causing damage through unauthorized access or transmission. Covers ransomware, denial of service, and destructive malware.

**§ 1030(a)(7):** Prohibits threatening to damage a protected computer to extort something of value. Covers ransomware extortion.

**Authorization as a defense:** The CFAA specifically exempts authorized access. The defense requires evidence of authorization at the time of access — not after the fact. This is why written authorization obtained before testing is critical.

### 1.2 Defining "Authorization" Under the CFAA

CFAA cases have interpreted "authorization" narrowly. Relevant precedent:

**Van Buren v. United States (2021):** The Supreme Court held that the CFAA's "exceeds authorized access" provision applies only to accessing information one is not permitted to access, not to accessing information for an impermissible purpose. This narrowed the CFAA's reach. However, accessing systems not included in scope remains unauthorized.

**United States v. Nosal (9th Cir., 2016):** Using someone else's credentials to access a system you would not otherwise be permitted to access constitutes unauthorized access even if that person authorized you to use their credentials.

**Practical implications:** A penetration tester must have authorization from the legal operator of the systems being tested. An employee authorizing testing of their employer's systems is insufficient unless they have authority to grant that permission (CISO, CTO, etc.).

### 1.3 Electronic Communications Privacy Act (18 U.S.C. § 2510–2523)

The ECPA prohibits the interception of wire, oral, or electronic communications. Relevant provisions for testing:

**Title I (Wiretap Act):** Prohibits real-time interception of communications content. Exceptions: system operator consent for their own system, party to the communication consent.

**Title II (Stored Communications Act, 18 U.S.C. § 2701):** Prohibits unauthorized access to stored communications.

**Safe harbor:** When testing a corporate network, the organization's authorization provides consent for monitoring within the scope of the engagement.

**Wireless communications:** Intercepting wireless communications without authorization violates both the ECPA and the Pen Register Act. Authorized wireless testing on authorized networks is protected.

### 1.4 State Computer Crime Laws

All 50 states have computer crime statutes. Selected examples:

**California Penal Code § 502:** Prohibits unauthorized access to computer systems, data, or networks. California's law is broader than the CFAA in some respects and has been applied in civil cases.

**Texas Penal Code § 33.02:** Unauthorized access to computer systems. Class B misdemeanor to second-degree felony depending on the value of data compromised.

**New York Penal Law § 156.10:** Computer trespass. Class A misdemeanor to Class C felony.

Multi-state engagements require attention to the laws of each state where systems are physically located.

---

## Section 2: Engagement Documentation

### 2.1 Master Services Agreement

The Master Services Agreement (MSA) is an umbrella agreement governing the overall relationship between a security firm and a client. It includes:

- Standard terms and conditions
- Indemnification clauses
- Limitation of liability
- Dispute resolution
- Governing law and jurisdiction
- Intellectual property ownership

The MSA covers all engagements under the relationship. Individual engagements are governed by Statements of Work that reference the MSA.

### 2.2 Statement of Work / Scope of Work

The SOW (sometimes called Statement of Work or Scope of Work — terms are used interchangeably) defines a specific engagement. Required elements:

**Parties and signatures:** Full legal names of both parties, authorized signatories, dates. The authorizing individual must have actual authority to bind the organization.

**Engagement description:** What type of assessment is being performed. Be specific: "External network penetration test, web application assessment, and wireless security assessment" rather than "security test."

**Scope:**

In-scope systems: IP ranges, specific hosts, domain names, application URLs, physical locations, employee populations (for social engineering).

Out-of-scope systems: Explicitly list what cannot be tested — third-party shared infrastructure, emergency systems (911, hospital patient monitoring), systems under maintenance windows.

**Testing constraints:**

Business hours restrictions: Systems where downtime would cause business impact may only be tested during low-traffic windows.

Production vs. development: Destructive testing (certain DoS tests, database manipulation) typically restricted to non-production environments.

**Deliverables:** Detailed report, executive summary, re-test availability.

**Timeline:** Testing start and end dates, draft report due date, final report due date.

**Authorization statement:** "The Client authorizes [Firm] to conduct security assessment activities as described herein against the systems specified in Appendix A."

### 2.3 Rules of Engagement

The ROE is a technical companion document to the SOW. It provides operational guidance for the testing team.

**Standard ROE components:**

Testing hours: Specific windows — "8 AM to 6 PM Eastern, Monday through Friday unless prior approval obtained for after-hours testing."

Permitted techniques: Enumerated list of authorized attack categories.

Prohibited techniques: What cannot be done — specific tool categories, destructive actions, data exfiltration.

Notification thresholds: Conditions requiring immediate client notification — finding a pre-existing breach, discovery of critical vulnerabilities in systems with live customer data.

Emergency contacts: Client security team contacts, escalation contacts for critical situations.

Abort conditions: "Testing stops immediately if: the client experiences a production outage, a third-party system is inadvertently affected, or an active threat actor is identified."

Test status communication: How often the tester updates the client — daily status emails, weekly calls.

### 2.4 Authorization Letter / Get-Out-of-Jail Letter

Carried by testers during active testing. Must include:

- Client organization name and letterhead
- Authorizing executive's name, title, and signature
- Testing firm name
- Description of authorized activities ("This firm is authorized to conduct security assessment activities at this location")
- Testing dates
- Emergency contact name and phone number (must be accessible during testing hours)

---

## Section 3: Confidentiality and Data Protection

### 3.1 Non-Disclosure Agreement Structure

A bilateral NDA in the testing context protects both parties:

**Client's protected information:** Security posture, vulnerability details, system configurations, test results, employee information encountered during social engineering testing.

**Firm's protected information:** Testing methodologies, tool capabilities, proprietary techniques.

**Standard NDA provisions:**

Definition of confidential information: What is covered (typically all information exchanged in connection with the engagement).

Exclusions: Information already in the public domain, information independently developed, disclosures required by law or court order.

Obligations: Keep confidential, use only for the stated purpose, limit internal distribution to need-to-know.

Duration: 3–5 years is standard. Perpetual NDAs are sometimes used for especially sensitive information.

Return/destruction: At engagement end, return or destroy all confidential materials on request.

### 3.2 Report Data Handling

The penetration test report is among the most sensitive documents the client will handle — it is a detailed map of exploitable vulnerabilities. Data handling requirements include:

- Secure transmission to the client (encrypted email or secure portal)
- Client distribution limited to need-to-know personnel
- No storage in cloud services without explicit agreement
- Defined retention period and destruction protocol
- Client agreement to protect the report from unauthorized disclosure

### 3.3 Incident Data and Credential Handling

During social engineering and credential testing, actual passwords may be captured. Requirements:

- Immediately encrypt captured credentials
- Access limited to testing team leads
- Notify client of specific captured credentials for forced password reset
- Delete at engagement end (after client confirms reset)
- Document in engagement record

---

## Section 4: Liability Framework

### 4.1 Indemnification

Indemnification defines which party bears liability for specific categories of harm:

**Testing firm indemnifies client for:** Harm caused by the firm's negligence, gross negligence, or willful misconduct during testing.

**Client indemnifies testing firm for:** Third-party claims arising from the client's decision to authorize testing; harm caused by undisclosed system criticality (client authorized testing a system they represented as non-production that was actually production).

### 4.2 Limitation of Liability

Standard limitation of liability clauses cap total exposure at the engagement fee amount. Rationale: the testing fee is a modest sum relative to the potential liability of compromising enterprise systems.

Carve-outs from the limitation typically include:

- Gross negligence
- Willful misconduct
- Fraud
- Intellectual property infringement
- Breach of NDA

### 4.3 Professional Insurance

**Errors and Omissions (E&O) / Professional Liability:** Covers claims that professional services caused financial harm. For testing: testing caused system damage, a finding was reported incorrectly, or a critical vulnerability was missed.

**Cyber Liability:** Covers costs from data breaches involving the firm's own systems. If client data in the firm's possession is compromised, cyber liability covers notification, credit monitoring, and legal defense costs.

**General Liability:** Covers bodily injury and property damage. Relevant for physical security testing.

---

## Section 5: Bug Bounty Programs

### 5.1 Program Types

**Private bug bounty:** Invitation-only. Participants are vetted security researchers. Higher quality findings, lower volume.

**Public bug bounty:** Open to all researchers. Higher volume, more variation in quality.

**Vulnerability Disclosure Program (VDP):** Similar to bug bounty but without monetary rewards. Provides a legal channel for reporting vulnerabilities.

### 5.2 Legal Protections in Bug Bounty Programs

A well-written bug bounty policy provides:

**Safe harbor:** "We will not pursue legal action against researchers who follow these guidelines."

**Good faith standard:** Testing is within scope, does not extract data beyond confirmation, does not degrade service availability.

**CFAA implications:** The DOJ's Cybersecurity Unit recommends that organizations include a "good faith" safe harbor in their policies. However, bug bounty safe harbor does not override state laws or international laws.

### 5.3 Responsible Disclosure Timeline

The standard 90-day responsible disclosure policy (Google Project Zero):

- Day 0: Researcher reports vulnerability.
- Day 7: Vendor acknowledges receipt.
- Day 90: Researcher may publicly disclose, regardless of patch status.
- Day 90+7: If patch is released within 7 days before the 90-day deadline, researcher extends by 7 days.

CISA's coordinated vulnerability disclosure (CVD) framework allows flexible timelines based on complexity and impact. Critical infrastructure vulnerabilities may receive extended timelines.

---

## Section 6: PT0-002 Exam Alignment

### 6.1 Exam Objectives Mapping

| Topic | PT0-002 Objective |
|-------|------------------|
| CFAA, ECPA | 1.1 — Governance, risk, compliance |
| SOW, ROE | 1.2 — Scoping and organizational requirements |
| NDA, liability | 1.2 — Contractual considerations |
| Bug bounty | 1.2 — Target and scope considerations |
| Authorization letter | 1.2 — Environmental considerations |
| Responsible disclosure | 1.3 — Ethical hacking mindset |

### 6.2 Exam Scenario Patterns

Common exam scenario patterns:

"A tester is asked to test a web application and discovers the application is hosted by a third-party SaaS provider. What must the tester do before testing?" — Obtain authorization from the SaaS provider (not just the client).

"During a test, the tester discovers systems outside the authorized scope that appear vulnerable. What is the correct action?" — Stop testing those systems, document the discovery, and report to the client with a scope expansion recommendation.

"A penetration tester performs testing on a cloud provider's infrastructure without checking the provider's testing policy. Which law is most directly at risk?" — The Cloud Provider's Terms of Service violation could implicate CFAA (§ 1030 — exceeds authorized access).

---

## Key Terms

**CFAA:** Computer Fraud and Abuse Act — primary federal statute governing computer crimes.

**ECPA:** Electronic Communications Privacy Act — governs interception of communications.

**SOW:** Scope of work — the primary engagement contract defining what is tested.

**ROE:** Rules of engagement — technical document defining how testing is conducted.

**NDA:** Non-disclosure agreement — governs confidentiality of information exchanged.

**MSA:** Master services agreement — umbrella agreement governing an ongoing client relationship.

**Indemnification:** Contractual obligation to bear the cost of loss for one party arising from the other party's actions.

**E&O Insurance:** Errors and Omissions insurance — professional liability coverage for testing firms.

**Bug bounty:** Formal program rewarding external researchers for reporting vulnerabilities.

**Responsible disclosure:** Reporting vulnerabilities to the vendor before public disclosure.

---

## Review Questions

1. A penetration tester has written authorization from a company's IT Director to test their web application. During testing, the tester discovers the application also processes data for a subsidiary company. What must the tester do before testing the subsidiary's data?

2. Explain the difference between the SOW and ROE. Can the ROE exist independently of an SOW?

3. What is the standard safe harbor timeline in responsible disclosure, and what organization established it as an industry norm?

4. A bug bounty program's policy says "test only *.example.com domains." A researcher discovers a vulnerability in api.v2.example.com. Is this within scope? Explain your reasoning.

5. What is the difference between E&O insurance and cyber liability insurance? Give one scenario where each would be relevant in a penetration testing context.

---

## References

- CompTIA PenTest+ PT0-002 Exam Objectives, Domain 1.1, 1.2, 1.3
- 18 U.S.C. § 1030 — Computer Fraud and Abuse Act
- 18 U.S.C. § 2510–2523 — Electronic Communications Privacy Act
- Van Buren v. United States, 593 U.S. ___ (2021)
- DOJ Cybersecurity Unit, "A Framework for a Vulnerability Disclosure Program for Online Systems" (2017)
- CISA Coordinated Vulnerability Disclosure: https://www.cisa.gov/coordinated-vulnerability-disclosure
- AWS Penetration Testing Policy: https://aws.amazon.com/security/penetration-testing/
