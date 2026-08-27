# Reading Guide: Module 02 - Rules of Engagement and Legal Considerations

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash

---

## Introduction

Module 02 covers the legal and ethical framework that governs professional penetration testing. Before any technical work begins, a tester must ensure written authorization is in place, relevant laws are understood, and contractual protections for both parties are established.

These topics fall primarily under the **Planning and Scoping** domain of the PT0-002 exam at **14 percent of the exam weight**, with overlap into the **Reporting and Communication** domain. The same techniques used by authorized penetration testers are identical to those used by criminal hackers. Documentation and professional conduct within agreed boundaries are the only things that separate the two.

---

## Section 1: Core Vocabulary

### Definitions You Must Know

**Authorization Letter (Permission Letter):** A written document signed by a client executive granting a named tester or team permission to conduct testing against specified systems within a defined time window. Carried during the engagement and presented if internal security or law enforcement challenges the testing activity. Commonly called the "get-out-of-jail card."

**Computer Fraud and Abuse Act (CFAA):** 18 U.S.C. § 1030, the primary US federal law criminalizing unauthorized computer access. Establishes both civil and criminal liability. Written authorization from the system owner is the legal mechanism that makes penetration testing lawful under this statute.

**Electronic Communications Privacy Act (ECPA):** A US federal law governing interception of wire, oral, and electronic communications and access to stored communications. Relevant when penetration testing includes traffic interception or man-in-the-middle techniques.

**PCI DSS (Payment Card Industry Data Security Standard):** A set of security requirements for organizations that store, process, or transmit cardholder data. Requirement 11.3 mandates annual external and internal penetration testing. Failure to comply can result in fines and loss of the ability to process credit card payments.

**HIPAA (Health Insurance Portability and Accountability Act):** US law governing the privacy and security of Protected Health Information (PHI). Requires covered entities and business associates to conduct security risk analyses and implement appropriate safeguards. Penetration testing is a common component of HIPAA risk analysis programs.

**GDPR (General Data Protection Regulation):** EU regulation governing the collection, storage, and processing of personal data of EU residents. Article 32 requires organizations to regularly test and evaluate technical security measures. Breach notification to regulatory authorities within 72 hours is required.

**SOC 2 (Service Organization Control 2):** An auditing framework for service organizations based on the AICPA Trust Services Criteria. The security trust service criteria require organizations to monitor systems for vulnerabilities. Penetration testing results are commonly used as audit evidence.

**Sarbanes-Oxley Act (SOX):** US federal law requiring internal controls over financial reporting for publicly traded companies. IT security controls supporting financial systems are subject to SOX compliance review, which may include penetration testing of financial system infrastructure.

**Responsible Disclosure:** The practice of privately notifying a vendor or system owner about a discovered vulnerability before public disclosure, giving them time to develop and release a patch. Contrasted with "full disclosure" (immediate public release) and "bug bounty" programs (structured commercial disclosure).

**Liability and Indemnification:** Contractual clauses in the MSA or SOW that limit the penetration tester's liability for unintended service disruptions during authorized testing, provided the tester operated within the agreed scope with due care. These clauses also define client responsibilities such as maintaining backups and notifying third parties before testing begins.

**Minimal Footprint Principle:** The ethical practice of doing no more than is necessary during a penetration test to demonstrate a vulnerability. Testing must not cause unnecessary disruption, data destruction, or unauthorized data collection beyond what is required to document the finding.

**Scope Creep:** An unauthorized expansion of testing activity beyond the boundaries defined in the RoE. Scope creep — even well-intentioned exploration of interesting systems — constitutes unauthorized access under the CFAA. All scope changes must be documented in writing before the expanded activity begins.

---

## Section 2: RoE Components in Detail

### The Six Required Components

A complete, professionally drafted Rules of Engagement document must contain all six of the following components. Omitting any one of them creates ambiguity that can lead to legal and professional consequences.

| Component | What It Defines | Why It Matters |
|---|---|---|
| Authorized Systems | IP ranges, FQDNs, and application URLs in scope | Defines the legal boundary of testing |
| Authorized Techniques | Specific testing methods permitted per phase | Prevents unauthorized or destructive activity |
| Testing Window | Authorized dates, hours, and time zone | Testing outside the window is unauthorized |
| Communication Protocol | Contacts, update frequency, notification triggers | Ensures client is informed; triggers incident response when needed |
| Emergency Stop Conditions | Conditions that require immediate halt | Limits liability and operational damage |
| Data Handling Rules | Storage, transmission, retention, disclosure | Protects client data and tester from liability |

### Writing Unambiguous Scope

Ambiguous scope language creates legal and professional risk. Compare these two scope definitions:

Weak: "Test the client's web infrastructure."

Strong: "Test the web application at `app.example.com`, the API at `api.example.com`, and the server at 203.0.113.15. All other systems are explicitly out of scope including the payment processor at `pay.example.com` and all systems in the 10.100.0.0/16 range."

The strong version leaves no room for interpretation. Every tester on the team, every client stakeholder, and any legal reviewer would reach the same conclusion about what is and is not authorized.

---

## Section 3: The Legal Framework

### CFAA in Practice

The CFAA defines "protected computer" broadly — any computer used in interstate or foreign commerce. This encompasses virtually every internet-connected device. Under the CFAA:

- Accessing a computer without authorization is a crime
- Exceeding authorized access is a crime (this is why going beyond scope is a legal issue, not just an ethical one)
- Causing damage to a protected computer is a crime
- Civil suits under the CFAA are possible in addition to criminal prosecution

For penetration testers, the practical implications are:

1. Written authorization from someone with legal authority is required before any activity
2. Testing must stay strictly within the authorized scope
3. Accidental out-of-scope activity must be immediately documented and reported
4. Any activity that causes damage — even unintentionally — could have legal consequences

### State Laws

| State | Relevant Law |
|---|---|
| California | Comprehensive Computer Data Access and Fraud Act (CDAFA) |
| Texas | Harmful Access by Computer Act |
| New York | Computer Tampering laws (Penal Law § 156) |
| Florida | Florida Computer Crimes Act |

Penetration testers working across state lines or for clients in multiple states should be aware that multiple state laws may apply simultaneously.

### International Considerations

| Jurisdiction | Relevant Law |
|---|---|
| European Union | GDPR plus member state cybercrime laws |
| United Kingdom | Computer Misuse Act 1990 |
| Canada | Criminal Code sections on unauthorized use of computer |
| Australia | Criminal Code Act — Part 10.7 Computer offences |

If a penetration test touches systems in another country — even indirectly — foreign law may apply. Always consult legal counsel for international engagements.

---

## Section 4: Compliance Standards Compared

### Standards Requiring or Driving Penetration Testing

| Standard | Industry | Testing Requirement |
|---|---|---|
| PCI DSS | Payment card | Requirement 11.3: annual external and internal pentest of cardholder data environment |
| HIPAA | Healthcare | No explicit mandate but required as part of security risk analysis |
| GDPR | EU data handlers | Article 32: regularly test and evaluate technical security measures |
| SOC 2 | Service organizations | CC7.1: monitor for vulnerabilities; pentest commonly used as evidence |
| SOX | Publicly traded companies | IT controls over financial systems; may include pentest of financial infrastructure |
| FISMA / FedRAMP | US federal systems | Annual security assessments including penetration testing |

### PCI DSS Penetration Testing Requirements in Detail

PCI DSS Requirement 11.3 specifies:

- Testing must occur at least annually and after significant changes
- Both external and internal network penetration testing is required
- Application layer testing is required in addition to network layer testing
- Testing must use industry-accepted methodology (PTES, OWASP, NIST SP 800-115)
- Findings must be remediated and retesting performed to verify fixes
- Results must be retained for at least 12 months

---

## Section 5: Ethics in Professional Penetration Testing

### Core Ethical Principles

The minimal footprint principle means doing only what is necessary to demonstrate a vulnerability. If you can prove a system is exploitable by gaining a shell and capturing a flag, you do not need to also read through employee email or exfiltrate a database. Demonstrate impact — do not maximize it.

Responsible disclosure protects both the client and the broader security community. When you find a vulnerability in a third-party product during a client engagement, you notify the client and follow the vendor's coordinated disclosure program. The CERT/CC, vendor-specific bug bounty programs, and the CVE program are the established channels.

Professional integrity requires that you decline engagements where you have conflicts of interest and disclose any that arise. It requires that you are honest about the limitations of your testing — a penetration test is a point-in-time assessment, not a guarantee of security.

### Handling Discovered Criminal Activity

If during a penetration test you discover evidence of criminal activity — such as child sexual abuse material (CSAM), evidence of financial fraud, or ongoing criminal intrusion — you have both ethical and potentially legal obligations. The correct steps are:

1. Stop the current testing activity
2. Document exactly what was observed without disturbing any evidence
3. Immediately notify the client through the escalation path defined in the RoE
4. Consult your firm's legal counsel about any reporting obligations

Do not attempt to investigate the criminal activity yourself. Do not delete evidence. Do not continue your penetration test until the situation is resolved.

---

## Section 6: Responsible Disclosure Frameworks

### Disclosure Models Compared

| Model | Description | Risk Level |
|---|---|---|
| Coordinated (Responsible) Disclosure | Notify vendor privately; agree on a fix deadline; public disclosure after patch | Low |
| Full Disclosure | Immediate public release of all vulnerability details | High (vendor has no time to patch) |
| Bug Bounty | Structured program with defined scope, rewards, and disclosure rules | Managed |
| Zero-Day Market | Sale of undisclosed vulnerabilities to third parties | Ethically prohibited for professional testers |

For pentest engagements, all findings are disclosed to the client. If the client chooses to responsibly disclose a finding to a vendor, that is their decision to make — not the tester's. The tester's obligation is to the client.

---

## Section 7: Third-Party Authorization

### Cloud Provider Policies

When a client's systems are hosted on a cloud provider, the tester must comply with that provider's penetration testing policies in addition to the client's authorization. Key policies as of the course writing date:

AWS: Allows customers to perform security testing on their own instances and services within defined categories. Certain services require prior notification. Their policy is published and should be reviewed at the start of any AWS-hosted engagement.

Microsoft Azure: Permits penetration testing against customer resources under their defined rules of engagement. Prior notification is not required for most testing but coordinated testing has specific rules.

Google Cloud: Allows security testing of customer environments within acceptable use policy boundaries.

These policies evolve. Always check the current policy for the specific provider before testing begins.

---

## Section 8: PenTest+ PT0-002 Exam Tips

### Tip 1 — Exam Weight

Legal and ethical considerations fall under Planning and Scoping at 14 percent of the exam. Expect scenario-based questions testing your judgment, not just recall of definitions.

### Tip 2 — Scope Creep Is Unauthorized Access

When the exam presents a scenario where a tester discovers an interesting system outside the agreed scope, the correct answer is always to document the discovery and report it to the client rather than exploit it. Unauthorized scope expansion is a CFAA violation.

### Tip 3 — Cloud Provider Authorization

If a client's systems are hosted in a cloud environment, the tester must obtain the cloud provider's authorization in addition to the client's. The exam tests this nuance in scenario questions.

### Tip 4 — CFAA Is the Baseline

For US-law questions, the CFAA is the answer. Authorization is what separates legal testing from criminal hacking.

### Tip 5 — PCI DSS Requirement 11.3

This is the most tested compliance mandate related to penetration testing. Know that it requires annual testing, both external and internal, and covers the cardholder data environment.

### Tip 6 — Immediate Notification for Incidents

When the exam presents a scenario where the tester causes or discovers an incident, the correct answer always involves immediate client notification, not continuing the test or self-remediation.

### Tip 7 — Minimal Footprint

Ethics questions on the exam expect the most conservative response. Demonstrate impact without maximizing damage. Stop and notify when in doubt.

### Tip 8 — Responsible Disclosure Is Client-First

Findings from a penetration engagement go to the client. The tester does not independently disclose findings to the public or to vendors without client direction.

---

## Study Checklist

- [ ] Define all twelve vocabulary terms without referring to notes
- [ ] List the six required components of a Rules of Engagement document and explain each
- [ ] Explain the CFAA and why written authorization is the legal basis for penetration testing
- [ ] Identify PCI DSS Requirement 11.3 and describe its specific testing requirements
- [ ] Distinguish coordinated disclosure from full disclosure and explain which applies to pentest engagements
- [ ] Describe the correct procedure when a tester discovers criminal activity on a target system
- [ ] Explain why a client's authorization does not automatically authorize testing of cloud provider infrastructure
- [ ] List three state computer crime laws and their home states
- [ ] Complete the Module 02 lab exercises
- [ ] Attempt all ten Module 02 quiz questions before checking answers

---

## 9. Supplemental Resources

**1. OWASP Testing Guide — Legal Issues in Penetration Testing**
[https://owasp.org/www-project-web-security-testing-guide/](https://owasp.org/www-project-web-security-testing-guide/)
The OWASP Web Security Testing Guide includes a section on legal considerations, pre-engagement agreements, and scope definition practices that directly support Module 02 concepts on the RoE and compliance frameworks.

**2. SANS Reading Room — Legal Issues in Penetration Testing**
[https://www.sans.org/white-papers/](https://www.sans.org/white-papers/)
SANS publishes free white papers on legal and ethical considerations in penetration testing. Search for papers on CFAA compliance, responsible disclosure, and RoE best practices to supplement the reading guide content.

**3. OffSec — PWK / PEN-200 Ethics and Legal Module**
[https://www.offsec.com/courses/pen-200/](https://www.offsec.com/courses/pen-200/)
The Offensive Security PEN-200 course (OSCP preparation) includes a dedicated module on legal and ethical responsibilities, authorization documentation, and professional conduct that aligns with PT0-002 planning and scoping objectives.
