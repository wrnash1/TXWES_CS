# Video Script: Module 02 - Rules of Engagement and Legal Considerations

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Estimated Duration:** 20-24 minutes
**Professor:** Nash

---

## Pre-Recording Checklist

- [ ] Title slide loaded: "Module 02 - Rules of Engagement and Legal Considerations"
- [ ] Terminal window ready for document examples
- [ ] CFAA statutory language excerpt prepared
- [ ] PT0-002 domain map highlighting Planning and Scoping at 14%

---

## [00:00 - 01:30] Opening

**[SLIDE: Module 02 — Rules of Engagement and Legal Considerations]**

Welcome back to CIS-4333. I'm Professor Nash. In Module 01 we built the foundation — you learned the five phases of penetration testing, the document hierarchy, and what scoping looks like in practice.

Module 02 goes deeper into two areas that are essential for professional practice and for the PT0-002 exam: how to construct a complete Rules of Engagement document, and the legal landscape that governs every authorized penetration test.

By the end of this module you will be able to:

- Construct a complete Rules of Engagement document for a real engagement
- Explain the CFAA and its implications for penetration testers
- Identify the key compliance standards that drive penetration testing requirements
- Describe the ethical obligations of a professional penetration tester
- Apply the concept of responsible disclosure to vulnerability findings

---

## [01:30 - 05:00] The Rules of Engagement in Depth

**[SLIDE: RoE — The Operational Contract]**

The Rules of Engagement document is the single most important technical document in a penetration test. In Module 01 we identified its components. Now let's walk through each component in depth.

### Component 1 — Scope of Authorized Systems

The scope section must be unambiguous. Every system the tester is authorized to interact with must be listed by IP address, CIDR range, domain name, or application URL. If a system is not listed, it is out of scope — no exceptions. There is no implied authorization from network proximity.

The scope section must also explicitly state exclusions. A scope that lists inclusions and explicitly names exclusions is clearer and safer than one that only lists what is included.

### Component 2 — Authorized Techniques

The RoE specifies which testing techniques are permitted. This matters because some techniques — denial-of-service testing, destructive exploits, data exfiltration — could harm production systems or violate laws beyond what the engagement warrants. If the RoE does not explicitly authorize a technique, that technique is prohibited. This protects both the client and the tester.

Common authorized technique categories: port scanning, service enumeration, vulnerability scanning, exploitation of confirmed vulnerabilities, credential testing, web application testing, wireless testing, and social engineering. Each must be explicitly authorized or excluded.

### Component 3 — Testing Window

The testing window specifies exactly when testing is authorized. It might be "Tuesdays and Thursdays, 11:00 PM to 5:00 AM Eastern Time" or "any time during the two-week engagement." Testing outside the authorized window is unauthorized testing even if every other element of the RoE is satisfied. The PT0-002 exam tests this concept.

### Component 4 — Communication and Escalation

The RoE defines how the tester communicates with the client. This includes:

- Who is the primary point of contact by name, not just title
- How often status updates are provided and in what format
- The emergency contact's 24/7 phone number during the active testing period
- The specific conditions that require immediate notification rather than a scheduled update

Immediate notification triggers include: disruption of a production service, discovery of active malicious activity by a third party, discovery of personally identifiable information in unexpected locations, and any situation where the tester believes they have exceeded authorized boundaries.

### Component 5 — Emergency Stop Conditions

The RoE must define conditions under which all testing halts immediately. These are non-negotiable. Common stop conditions include: the client's emergency contact instructs testing to stop, the tester disrupts a production service, the tester discovers evidence of an active breach by an unauthorized third party, the tester discovers evidence of criminal activity on target systems, and any system behaves unexpectedly in a way suggesting real-world harm could result.

### Component 6 — Data Handling

Any sensitive data discovered during testing — credentials, PII, financial data, PHI — must be handled according to defined rules. The RoE should specify storage method (encrypted at rest), transmission method (encrypted in transit only), retention period (typically 30 to 90 days after report delivery), and who may receive the report.

---

## [05:00 - 09:30] The Legal Framework

**[SLIDE: Computer Fraud and Abuse Act — 18 U.S.C. § 1030]**

As a penetration tester, you must understand the laws that govern what you do — not at an attorney's level, but well enough to recognize when you are at risk and when you need to stop and seek legal guidance.

### The Computer Fraud and Abuse Act

The CFAA, 18 U.S.C. § 1030, is the primary US federal law criminalizing unauthorized computer access. It was originally enacted in 1986 and has been amended multiple times. The key provisions relevant to penetration testing are:

Section 1030(a)(2) prohibits intentionally accessing a computer without authorization and obtaining information. Section 1030(a)(5) prohibits knowingly causing damage to a protected computer.

The phrase "without authorization" is the critical element. Written authorization from the system owner transforms penetration testing from a criminal act into a lawful professional activity. Your authorization documents are not bureaucratic overhead — they are your legal protection.

**[SLIDE: CFAA Key Points for the Exam]**

For the PT0-002 exam, remember these points:

The CFAA applies to any computer used in interstate or foreign commerce — in practice, virtually any internet-connected system. Both civil and criminal penalties exist under the CFAA. State computer crime laws may add additional requirements. Authorization must come from someone with legal authority to grant it — a low-level employee cannot authorize a penetration test of the entire enterprise network.

### State Computer Crime Laws

Many states have their own computer crime statutes. California's Comprehensive Computer Data Access and Fraud Act is stricter than the CFAA in some respects. Texas has the Harmful Access by Computer Act. If a test crosses state lines or involves systems in multiple states, both federal and applicable state laws must be considered.

### The Electronic Communications Privacy Act

The ECPA governs interception of electronic communications and access to stored communications. If you perform man-in-the-middle testing or traffic interception during an engagement, ECPA considerations apply. Your RoE authorization for traffic interception should specifically address this.

---

## [09:30 - 13:00] Compliance Standards That Drive Penetration Testing

**[SLIDE: Why Compliance Matters to Penetration Testers]**

Many organizations conduct penetration tests not only because it is good security practice but because their industry regulations require it. Understanding these requirements helps you scope engagements appropriately.

### PCI DSS

PCI DSS Requirement 11.3 mandates annual penetration testing for organizations that store, process, or transmit cardholder data. It requires both external and internal testing covering the cardholder data environment. If the client needs PCI DSS compliance, the test must follow PCI DSS penetration testing guidance, which includes specific methodology requirements including use of industry-accepted approaches and coverage of the full cardholder data environment perimeter.

### HIPAA

HIPAA does not mandate penetration testing by name, but requires a security risk analysis and appropriate technical safeguards. In practice, most HIPAA compliance programs include penetration testing as evidence for that risk analysis. When testing healthcare systems, you must address Protected Health Information — how you will avoid accessing it when unnecessary, and how you will handle it if you do encounter it.

### GDPR

If the client handles personal data of EU residents, GDPR applies. Article 32 requires organizations to implement appropriate technical security measures and regularly test them. A penetration tester working for a GDPR-regulated client must understand data residency requirements and the 72-hour breach notification obligation. If your testing activity causes a data incident, that notification obligation may apply.

### SOC 2

SOC 2 is an auditing framework for service organizations. The security trust service criteria require organizations to monitor for vulnerabilities and assess their controls. Penetration testing is commonly used as audit evidence for SOC 2 engagements. If your client is seeking SOC 2 certification, your pentest report may be reviewed by their auditor.

---

## [13:00 - 16:30] Ethics and Professional Obligations

**[SLIDE: The Ethics of Offensive Security]**

Penetration testing puts you in a privileged position. You have written authorization to do things that would otherwise be illegal. With that privilege comes significant ethical responsibility.

### Minimal Footprint

During a penetration test, do no more than necessary to demonstrate a vulnerability. If you can show a system is exploitable without exfiltrating real data, you do exactly that — demonstrate impact without maximizing it. Destroying data, disrupting services unnecessarily, and harvesting sensitive data beyond what is needed for the report are violations of professional ethics and potentially violations of your RoE.

### Responsible Disclosure

Responsible disclosure is the practice of notifying a vendor or organization about a vulnerability before making it public, giving them time to develop and release a fix. For penetration testers: vulnerabilities found during an engagement are disclosed to the client, not the public. If you discover a vulnerability in a third-party product (an unpatched CVE in a popular software library), you follow the established disclosure process for that vendor. You never weaponize findings or sell them to third parties.

### Conflicts of Interest

A penetration tester must not test a system where they have a conflict of interest. If you previously worked for the client and have inside knowledge of their architecture, disclose that conflict before accepting the engagement. If you own stock in the client company, that too is a conflict requiring disclosure.

### Protecting Client Confidentiality

Everything you discover during a penetration test is confidential. The NDA protects this legally. But ethically, you treat client information with care beyond what the NDA requires. You do not discuss findings with colleagues outside the engagement team. You do not post screenshots of interesting findings online. You protect the client's sensitive information as if it were your own.

---

## [16:30 - 19:30] Handling Difficult Situations

**[SLIDE: When Things Get Complicated]**

Even with a well-written RoE, penetration testers encounter situations requiring careful judgment. The PT0-002 exam tests these scenarios.

### Discovering an Active Breach

During a penetration test you find evidence that a real attacker has already compromised one of the target systems — active reverse shells, exfiltrated data in staging directories, logs of activity from an external IP you did not control.

Correct action: stop your testing immediately. Notify the client emergency contact right now — not at the end of the day. Preserve your own logs documenting what you found, but do not disturb the evidence. The client may need to engage incident response, and your notes may be important. Do not continue your penetration test — continuing could contaminate the incident response investigation.

### Accidentally Exceeding Scope

You are running an automated scanner and realize you misconfigured the target range — it scanned a /16 instead of a /24, touching hundreds of systems outside your authorized scope.

Correct action: stop the scan immediately. Document exactly what happened — timestamps, tool output, IP addresses contacted. Notify the client immediately and be transparent. This is a serious mistake, but handling it professionally and honestly is far better than concealing it. Your documentation of the accidental activity protects both parties.

### Client Requests Illegal Activity

A client asks you to test a competitor's network to "see how they compare." This is not a penetration test. Testing systems you are not authorized to test is unauthorized computer access under the CFAA regardless of who asked you. Decline immediately, document the request, and consult legal counsel about your obligations.

---

## [19:30 - 22:30] Constructing a Complete RoE — Walkthrough

**[SHOW TERMINAL]**

Let me show you what a professionally formatted Rules of Engagement document looks like at the structural level. This is the format you will produce in professional practice.

```text
RULES OF ENGAGEMENT
Engagement: External and Internal Network Penetration Test
Client: Lone Star Financial Services, LLC
Testing Firm: ClearPath Security Consulting
Reference: CSC-2026-0042  |  Version: 1.0

SECTION 1 — AUTHORIZED TARGETS
  See Appendix A (attached IP ranges and hostnames).

SECTION 2 — TESTING WINDOW
  Mon–Fri, 22:00–06:00 CT, weeks of [start]–[end].
  Weekend testing requires 48-hour advance written approval.

SECTION 3 — AUTHORIZED TECHNIQUES
  Recon: OSINT, Nmap TCP/UDP, banner grabbing, service enum
  Analysis: Nessus authenticated scan, manual CVE research
  Exploit: Confirmed vulns only; no destructive payloads
  Post-Exploit: Pivot within auth'd ranges; no data exfil

SECTION 4 — PROHIBITED TECHNIQUES
  Social engineering, physical access, DoS/DDoS,
  out-of-scope systems, actual data exfiltration,
  payment processor systems, third-party cloud infra.

SECTION 5 — COMMUNICATIONS
  Daily status email by 08:00 CT to [named contact].
  Emergency: [name], [phone], available 24/7 during engagement.

SECTION 6 — STOP CONDITIONS
  (a) Client orders halt  (b) Production disruption
  (c) Active third-party intrusion detected
  (d) PHI or PII accessed unexpectedly

SECTION 7 — DATA HANDLING
  Findings encrypted at rest (AES-256) and in transit (TLS).
  Report delivered to named recipients only.
  All data purged 30 days after report delivery.

SIGNATURES
  Client Representative: _________________ Date: _______
  Testing Firm Lead:    _________________ Date: _______
```

Notice how every section is specific and actionable. There is no ambiguity about what is authorized and what is not.

---

## [22:30 - 23:30] Exam Tips and Summary

**[SLIDE: PT0-002 Exam Tips — Module 02]**

Key exam tips for this module:

First: the RoE is the operationally binding document that authorizes testing. Know its six components.

Second: the CFAA is the primary US federal law. Authorization equals legality under this statute.

Third: PCI DSS Requirement 11.3 is the most commonly tested compliance mandate for penetration testing.

Fourth: ethics questions expect the most conservative, client-protective response. When in doubt about whether something is ethical, stop and consult the client.

Fifth: responsible disclosure means the client gets your findings first, not the public.

For additional study, visit **professormesser.com** and **comptia.org** for PT0-002 aligned resources.

---

## [23:30 - 24:00] Closing

In Module 03 we move into the reconnaissance phase — specifically passive OSINT techniques. You will learn how much information about a target can be gathered without ever touching their systems, using only publicly available sources.

Review your quiz, complete your lab, and contribute to the discussion. See you in Module 03.

---

*All demonstrations in this course are performed in authorized, isolated lab environments. No techniques should be applied to systems without explicit written authorization.*
