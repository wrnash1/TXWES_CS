# Video Script: Module 14 — Legal, Compliance, and Contractual Considerations

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Production Notes

- **Runtime Target:** 28–32 minutes
- **Segments:** 6
- **Visual Aids:** Scope of work template, rules of engagement example, bug bounty policy comparison
- **Lab Environment:** Contract review and SOW writing exercise — no live systems

---

## Segment 1: Why Legal Knowledge Is Not Optional (Lines 1–35)

[SLIDE: Module 14 Title Card]

Welcome to Module 14. This module covers the legal and contractual framework that governs penetration testing. I want to start with a direct statement: ignorance of the law is not a defense in federal court.

Penetration testers operate at the intersection of authorized security assessment and activities that, without proper authorization and documentation, constitute federal crimes. The Computer Fraud and Abuse Act, the Electronic Communications Privacy Act, state computer crime statutes, and industry-specific regulations create a complex legal environment that every practitioner must understand.

[SLIDE: The Authorization Chain]

The foundation of all legal protection for penetration testers is the authorization chain. At the top is the organization's legal authority to authorize testing — the entity that has the right to permit access to a system. Below that are the specific individuals with authority to grant this permission (typically the CISO, CTO, or executive with responsibility for the systems). Below that are the contractual documents — the SOW, ROE, NDA — that document the authorization. And at the bottom is the tester, acting within the documented scope.

Any break in this chain creates legal exposure. An employee saying "it's okay to test" is not the same as a board-authorized CISO signing a scope of work.

[SLIDE: Course Roadmap]

This module covers:

- The Computer Fraud and Abuse Act (CFAA) and Electronic Communications Privacy Act (ECPA) as they apply to testing
- Scope of work structure and requirements
- Rules of engagement
- Get-out-of-jail documentation
- Non-disclosure agreements
- Liability clauses and indemnification
- Bug bounty programs and responsible disclosure

[PAUSE for transition]

---

## Segment 2: Key Federal Laws (Lines 36–75)

[SLIDE: Computer Fraud and Abuse Act]

18 U.S.C. § 1030 — the Computer Fraud and Abuse Act — is the primary federal law governing unauthorized computer access. It was enacted in 1986 and amended multiple times to address the evolving nature of computer crime.

Key provisions relevant to penetration testing:

Section 1030(a)(1): Unauthorized access to classified government computer systems.

Section 1030(a)(2): Unauthorized access to obtain information from financial institutions, government systems, or protected computers.

Section 1030(a)(5): Intentional unauthorized damage to protected computers.

The word "unauthorized" is critical. Authorized penetration testing is not a CFAA violation. But the authorization must be clear, documented, and from the legitimate owner or authorized operator of the system.

[SLIDE: What "Unauthorized" Means]

CFAA cases have established that "unauthorized" access means accessing a system in a way the owner has not permitted. This includes:

- Accessing systems beyond the scope of your authorization (scope creep)
- Using authorization obtained through deception
- Continuing access after authorization has been revoked
- Accessing systems through pivot that were not explicitly included in scope

A penetration tester who discovers a vulnerability in a production system during a test of a development environment and exploits the production system may be violating the CFAA even though they are otherwise conducting an authorized test.

[SLIDE: Electronic Communications Privacy Act]

18 U.S.C. § 2511 — the Electronic Communications Privacy Act — prohibits the interception of electronic communications without authorization. This is relevant to:

- Packet capture during authorized network assessments
- Wireless traffic capture
- Email content interception during phishing tests

The key protection: authorization from the system owner (typically the employer for corporate networks) provides ECPA safe harbor for network monitoring within the authorized scope.

[SLIDE: State Laws]

Federal law is not the only concern. All 50 states have computer crime statutes, and many are broader or stricter than the CFAA. For multi-state engagements, the applicable state laws for each physical location must be considered.

Additionally, industry-specific regulations impose additional legal frameworks:

HIPAA — protected health information (healthcare)

GLBA — customer financial information (financial services)

FERPA — student educational records (educational institutions)

PCI DSS — cardholder data (any organization accepting payment cards)

SOX — financial reporting controls (publicly traded companies)

[PAUSE for transition]

---

## Segment 3: Scope of Work and Rules of Engagement (Lines 76–115)

[SLIDE: Scope of Work Structure]

The scope of work (SOW) is the primary contract document governing a penetration test engagement. A professional SOW must include:

Parties: The testing firm and the client organization, with full legal names.

Engagement description: What type of testing is being performed (external, internal, web application, physical, social engineering).

Scope definition: Specifically what systems, networks, IP ranges, domains, and applications are in scope. Also explicitly what is out of scope.

Testing period: Specific dates and times. After-hours testing versus business hours testing may require different authorization language.

Authorization statement: Explicit language that the client authorizes the testing firm to conduct security assessment activities against the specified systems.

Deliverables: What the client will receive — report format, timeline, presentation.

Payment terms: Fee structure, invoicing schedule, payment terms.

[SLIDE: Defining Scope Precisely]

Scope definition is where many engagements go wrong. Common scope failures:

Too broad: "Test all systems" without specifying which systems exposes the tester to scope creep and exposes the client to unexpected downtime.

Ambiguous: "Test the network" — which network? All IP ranges? Cloud infrastructure? Partner networks?

Missing exclusions: Failing to explicitly exclude third-party systems, shared hosting environments, and production systems creates risk.

Out-of-date: Scope defined at contract signing that does not reflect the actual environment at test time.

Best practice: Define scope as specific IP ranges, domain names, and application URLs. Attach a technical inventory as an appendix. Update at kickoff to reflect current state.

[SLIDE: Rules of Engagement]

The rules of engagement document is a technical companion to the SOW. Where the SOW defines what is tested, the ROE defines how it is tested.

ROE elements:

Testing hours: "Testing may be conducted during business hours (8 AM–6 PM local time) with critical system testing only after business hours by prior arrangement."

Permitted techniques: Specific attack categories permitted — port scanning, exploitation, social engineering, physical testing.

Prohibited techniques: Specific techniques explicitly banned — denial of service, destructive payloads, testing of production databases without prior approval.

Notification procedures: What happens when a critical vulnerability is found mid-engagement? Who is called? What is the protocol?

Emergency abort conditions: Under what circumstances does the test stop immediately? (System outage, discovery of active threat actor, client emergency)

Third-party systems: Explicit statement that systems belonging to third parties are not in scope.

[SLIDE: The Testing Authorization Form]

For large organizations with multiple stakeholders, a testing authorization form may be required. This is a single-page document signed by the authorizing executive that explicitly permits testing and lists the authorizing party's name, title, and contact information.

This is distinct from the full SOW — it is designed to be carried by testing staff as the get-out-of-jail letter equivalent for network testing.

[PAUSE for transition]

---

## Segment 4: NDA, Liability, and Indemnification (Lines 116–155)

[SLIDE: Non-Disclosure Agreements]

A mutual non-disclosure agreement (NDA) governs what each party can share with third parties. In penetration testing, the NDA protects:

Client: The test results, including vulnerability details, cannot be disclosed to third parties. The client's systems and security posture are confidential business information.

Testing firm: The testing methodologies, tools, and techniques that represent intellectual property cannot be disclosed.

NDAs typically include:

Definitions: What constitutes "confidential information" for each party.

Exclusions: Information already in the public domain, information independently developed, information required to be disclosed by law.

Duration: How long the NDA remains in effect. 3–5 years is common; perpetual NDAs are disfavored.

Remedies: Typically injunctive relief (stopping the disclosure) since damages from information disclosure are difficult to quantify.

[SLIDE: Liability and Limitation of Liability]

Penetration testing inherently carries risk of unintended damage. Liability clauses define who bears that risk.

Indemnification: The testing firm typically indemnifies the client against claims arising from the testing firm's negligence. The client indemnifies the testing firm for authorized actions within scope.

Limitation of liability: A cap on total liability, typically equal to the engagement fee or some multiple thereof. "Limitation of liability to the engagement fee" is standard; "unlimited liability" is uncommon and typically uninsurable.

Carve-outs: Most limitation clauses have carve-outs for gross negligence, willful misconduct, and fraud.

[SLIDE: Errors and Omissions Insurance]

Professional penetration testers carry Errors and Omissions (E&O) insurance, also called Professional Liability Insurance. This covers claims arising from professional services — testing that inadvertently causes system damage, false findings, or failure to identify critical vulnerabilities.

Some clients require specific minimum E&O coverage as a contract condition. Typical minimums for enterprise engagements: $1 million per occurrence, $2 million aggregate.

Cyber liability insurance is a separate policy covering data breaches that may arise from the tester's infrastructure being compromised. If the tester's systems holding client report data are breached, cyber liability covers resulting costs.

[SLIDE: Third-Party and Cloud Considerations]

Modern environments involve third-party systems and cloud providers. Testing these requires additional consideration:

AWS, Azure, GCP: All major cloud providers have specific penetration testing policies. AWS requires customers to request permission before testing certain service types. GCP and Azure have similar policies. Violating cloud provider policies can result in account termination and potential legal action by the provider.

ISPs and network providers: Traffic traversing a provider's infrastructure may be subject to provider terms of service. Testing scenarios that involve traffic injection or manipulation at the ISP level require additional authorization.

SaaS vendors: Testing a client's SaaS applications against the vendor's infrastructure requires the vendor's authorization, not just the client's.

[PAUSE for transition]

---

## Segment 5: Bug Bounty Programs and Responsible Disclosure (Lines 156–195)

[SLIDE: Bug Bounty Programs Overview]

Bug bounty programs are formal vulnerability disclosure programs operated by organizations to compensate security researchers for identifying and reporting vulnerabilities. They represent a formalized, contractual arrangement for limited authorized testing.

Major platforms: HackerOne, Bugcrowd, Intigriti, Synack, YesWeHack.

Key characteristics:

Defined scope: The bug bounty policy specifies exactly which domains, applications, and vulnerability types are in scope.

Rules of engagement: Specific actions are permitted (testing) and prohibited (DoS, data exfiltration, social engineering).

Reward structure: Different reward tiers for different severity levels. Critical findings may yield $10,000+ at major technology companies; Low findings may yield $100–$500.

Safe harbor language: The policy provides legal protection for researchers acting within scope. This is the bug bounty equivalent of the SOW authorization.

[SLIDE: Responsible Disclosure]

Responsible disclosure (also called coordinated disclosure) is the practice of reporting vulnerabilities to the affected organization before public disclosure, allowing time for remediation.

The standard responsible disclosure process:

1. Researcher discovers vulnerability.
2. Researcher contacts the organization's security team.
3. Organization acknowledges receipt and begins remediation.
4. Researcher waits a reasonable disclosure period (typically 90 days).
5. Organization releases a patch or mitigation.
6. Researcher may publish technical details.

Google Project Zero popularized the 90-day disclosure deadline. CISA advocates for coordinated disclosure with flexible timelines based on severity and remediation complexity.

[SLIDE: Disclosure Without a Bug Bounty]

Many organizations do not have formal bug bounty programs. When a vulnerability is discovered in a system that has no public bug bounty:

Check for a security contact: Look for security.txt files (RFC 9116), security@domain.com email, or PSIRT (Product Security Incident Response Team) contact information.

Document everything: Before reporting, document the vulnerability, the discovery date, and all testing activity.

Report through proper channels: Contact the security team directly, not the general support team or CEO.

Follow up: If there is no response within 14 days, follow up once. After 30 days with no response, consider contacting CISA's vulnerability coordination program (for critical infrastructure).

Do not sell to third parties: Selling discovered vulnerabilities to anyone other than the affected organization (or established vulnerability brokers with clear legal frameworks) creates legal risk.

[SLIDE: Vulnerability Disclosure Policy Best Practices]

For clients, recommending a vulnerability disclosure policy is a valuable advisory output. A good VDP includes:

Safe harbor statement: Legal protection for researchers acting in good faith within the policy scope.

Scope definition: What can researchers test.

Communication channel: Where to report findings (typically a security email with a PGP key).

Acknowledgment timeline: How quickly the organization will acknowledge receipt.

Disclosure timeline: The organization's timeline for remediation and the researcher's right to publish after.

[PAUSE for transition]

---

## Segment 6: PT0-002 Alignment and Summary (Lines 196–240)

[SLIDE: PT0-002 Domain 1 — Planning and Scoping]

The majority of Module 14's content maps directly to PT0-002 Domain 1:

Objective 1.1: Compare and contrast governance, risk, and compliance concepts. Covers industry standards and frameworks, compliance requirements by sector.

Objective 1.2: Explain the importance of scoping and organizational/customer requirements. Covers target, scope, and authorization discussion; technical constraints; environmental considerations.

Objective 1.3: Given a scenario, demonstrate an ethical hacking mindset by maintaining professionalism and integrity. Covers staying within scope, identifying risk to the client and tester, and communicating findings.

[SLIDE: Key Legal Knowledge for PT0-002]

The PT0-002 exam tests specific legal knowledge. Know these:

CFAA (18 U.S.C. § 1030): Unauthorized computer access. "Unauthorized" is the operative word.

ECPA (18 U.S.C. § 2511): Electronic communications interception.

PCI DSS: Payment card data. 12 requirements. Testing implications in Requirement 11.

HIPAA: PHI protection. Security Rule physical, technical, and administrative safeguards.

The exam may ask: Which law most directly prohibits unauthorized access to a protected computer? (CFAA) Which document defines the specific techniques permitted during a test? (ROE) What provides legal protection when law enforcement challenges a physical pen tester? (Get-out-of-jail letter / authorization letter)

[SLIDE: Exam Vocabulary]

Master this vocabulary for PT0-002:

SOW: Scope of work — the primary engagement contract.

ROE: Rules of engagement — the technical testing parameters.

NDA: Non-disclosure agreement — governs information confidentiality.

MSA: Master services agreement — overarching relationship agreement.

SLA: Service level agreement — defines performance standards.

Authorization letter: Written permission from the system owner — the foundational legal document.

Get-out-of-jail letter: Physical document carried during testing that confirms authorization to challenging parties.

Bug bounty: Formal vulnerability rewards program with defined scope and safe harbor.

Responsible disclosure: The practice of notifying organizations before publishing vulnerability details.

[SLIDE: Module Summary]

Module 14 covered the complete legal and contractual framework for authorized penetration testing: the CFAA and ECPA as they apply to testing activities, scope of work structure, rules of engagement, NDA provisions, liability and indemnification, insurance requirements, third-party authorization requirements, bug bounty programs, and responsible disclosure practices.

The legal framework is not bureaucratic overhead — it is what separates a professional security assessment from a federal crime. Every tester must understand this framework before touching a target system.

Your lab for this module involves reviewing and revising a deficient scope of work document to bring it to professional standards.

[END RECORDING]
