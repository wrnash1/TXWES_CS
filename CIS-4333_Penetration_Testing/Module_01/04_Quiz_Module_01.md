# Quiz: Module 01 - Penetration Testing Methodology and Scoping

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash
**Instructions:** Select the single best answer for each question.

---

## Question 1

Which document explicitly defines the authorized IP ranges, permitted testing techniques, testing window, and emergency stop conditions for a penetration test?

- A) Non-Disclosure Agreement (NDA)
- B) Master Service Agreement (MSA)
- C) Rules of Engagement (RoE)
- D) Statement of Work (SOW)

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The Rules of Engagement is the operationally binding technical document that specifies exactly what systems are in scope, which techniques are authorized, when testing may occur, and under what circumstances testing must stop. It is the document that separates authorized testing from unauthorized access.
- Why A is incorrect: The NDA establishes confidentiality obligations for both parties. It does not authorize any testing activity or define technical boundaries.
- Why B is incorrect: The MSA is a general commercial contract governing the ongoing business relationship. It sets payment terms and liability but does not authorize specific testing activities.
- Why D is incorrect: The SOW describes what work will be performed and the associated deliverables and cost. While it contributes to the authorization framework, it does not specify technical rules like allowed techniques or testing hours.

---

## Question 2

In penetration testing, which of the following best defines target classification?

- A) The process of assigning CVSS severity scores to discovered vulnerabilities after exploitation
- B) The categorization of in-scope assets by type and sensitivity level to guide methodology and prioritization
- C) A legal agreement specifying which systems are excluded from testing to reduce liability
- D) A technique for identifying operating systems by analyzing TTL values and TCP window sizes

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Target classification organizes in-scope systems by type (web application, network infrastructure, wireless, physical) and sensitivity so testers apply the correct methodology and allocate time appropriately to higher-risk assets.
- Why A is incorrect: CVSS scoring occurs during the reporting phase after exploitation — it is a vulnerability severity measurement, not a pre-engagement classification of targets.
- Why C is incorrect: Exclusion lists appear in the scoping document. Target classification groups what is in scope by type, not what is excluded.
- Why D is incorrect: OS fingerprinting via TTL and TCP analysis is a passive reconnaissance technique performed during information gathering, not a pre-engagement planning activity.

---

## Question 3

A penetration tester discovers a server at 10.0.5.200 during active scanning of an authorized subnet. This address does not appear anywhere in the signed Rules of Engagement. What is the correct action?

- A) Continue testing — the server is on the same subnet as authorized systems, implying implicit authorization
- B) Run a service version scan to confirm whether the server is critical before deciding to proceed
- C) Stop testing the out-of-scope system immediately, document the discovery, and notify the client to discuss whether authorization can be extended
- D) Exploit the server and include the findings in the final report to demonstrate thoroughness

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The PT0-002 exam consistently tests that testers must halt all activity against any system not explicitly authorized in the RoE and contact the client before proceeding. Unauthorized access — even accidental — violates the CFAA regardless of the system's location.
- Why A is incorrect: Subnet proximity never implies authorization. Every in-scope target must be explicitly listed or described in the scoping document.
- Why B is incorrect: Running even a passive version scan against an unauthorized host constitutes unauthorized testing and creates legal exposure for the tester.
- Why D is incorrect: Including findings from an unauthorized system in the report would expose both the tester and the firm to legal liability under the CFAA.

---

## Question 4

A client asks a penetration tester to skip the formal scoping document to save time, saying a verbal agreement is sufficient. What is the appropriate professional response?

- A) Proceed with testing — verbal agreements are legally binding in most US jurisdictions
- B) Accept the verbal agreement but record the conversation as documentation
- C) Decline to proceed until a written scoping document and Rules of Engagement are signed by an authorized representative
- D) Begin passive reconnaissance only, since passive activity does not require formal authorization

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Written authorization is a non-negotiable requirement in professional penetration testing. Without it, the tester has no legal protection and the activity could be considered unauthorized access under the CFAA.
- Why A is incorrect: Verbal agreements are difficult to enforce and provide no concrete protection if a dispute arises or law enforcement becomes involved.
- Why B is incorrect: Recording a conversation does not carry the same legal weight as a signed authorization document and may not be admissible depending on jurisdiction.
- Why D is incorrect: Even passive reconnaissance targeted at a specific organization in the context of an engagement requires written consent. The engagement itself requires authorization before any phase begins.

---

## Question 5

A financial institution wants any testers caught by their internal security team to be able to prove the test is authorized in real time. Which document serves this purpose?

- A) The Non-Disclosure Agreement signed at the start of the engagement
- B) The penetration tester's professional certification credential
- C) The written authorization letter signed by an executive of the client organization
- D) The final penetration test report submitted after the engagement concludes

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The authorization letter is a carry-on document identifying the tester, the scope, and the dates of authorized testing. It is presented to internal security or law enforcement to confirm legitimacy — hence the nickname "get-out-of-jail card."
- Why A is incorrect: An NDA protects confidential information but does not authorize testing or serve as proof of permission during an active engagement.
- Why B is incorrect: A certification proves qualifications but carries no legal authority to conduct testing on a specific organization's systems.
- Why D is incorrect: The final report is produced after testing concludes and cannot be presented during active testing as real-time proof of authorization.

---

## Question 6

Which of the following best describes a gray box penetration test?

- A) The tester has no prior knowledge of the target environment, simulating an external attacker
- B) The tester has complete knowledge including network diagrams, source code, and credentials
- C) The tester has partial knowledge such as a user-level account and basic network documentation
- D) The tester uses only passive reconnaissance and never interacts directly with target systems

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: A gray box test gives the tester some knowledge of the environment — typically a user-level account or partial network documentation — simulating a compromised credential or insider-threat scenario.
- Why A is incorrect: No prior knowledge describes a black box test, which simulates an uninformed external attacker.
- Why B is incorrect: Full knowledge including source code and credentials describes a white box test, which allows the most thorough coverage in the shortest time.
- Why D is incorrect: Testing using only passive reconnaissance is a description of a specific reconnaissance phase technique, not a test type classification.

---

## Question 7

Which US federal law is the primary statute that makes unauthorized computer access a crime, and therefore makes written authorization the legal basis for penetration testing?

- A) Electronic Communications Privacy Act (ECPA)
- B) Computer Fraud and Abuse Act (CFAA)
- C) Gramm-Leach-Bliley Act (GLBA)
- D) Health Insurance Portability and Accountability Act (HIPAA)

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: The CFAA, 18 U.S.C. § 1030, makes it a federal crime to access a computer without authorization or to exceed authorized access. Written authorization from the system owner is what makes penetration testing lawful under this statute.
- Why A is incorrect: The ECPA governs the interception of electronic communications and stored communications. While relevant to some surveillance scenarios, it is not the primary law governing computer access authorization for penetration testing.
- Why C is incorrect: GLBA governs financial data privacy. It may influence the compliance requirements for a financial sector pentest but does not define what makes computer access authorized or unauthorized.
- Why D is incorrect: HIPAA governs protected health information in the healthcare sector. It affects data handling rules during a healthcare pentest but does not define authorization for computer access.

---

## Question 8

A penetration testing firm is about to begin an engagement for a client whose web servers are hosted on a major cloud provider. The client has signed the RoE. What additional step is required before testing begins?

- A) No additional steps are needed — the client's signed RoE covers all testing against their systems regardless of hosting location
- B) The testing firm must obtain their own cloud provider account on the same platform
- C) The tester must review the cloud provider's penetration testing policy and obtain any required prior notification or approval from that provider
- D) The tester must notify the Internet Service Provider that assigned the client's IP addresses

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Cloud providers have their own acceptable use and penetration testing policies. Even if a client authorizes testing of their cloud-hosted infrastructure, the cloud provider's policies govern what testing is permitted against their platform. Failure to comply can violate the provider's terms of service.
- Why A is incorrect: A client's authorization does not override a third-party cloud provider's policies. The provider's infrastructure is not the client's property to authorize testing against without restriction.
- Why B is incorrect: The tester does not need their own account on the same platform. The requirement is to review the provider's testing policies, not to establish a customer relationship.
- Why D is incorrect: ISP notification is not a standard requirement for cloud-hosted systems. The relevant third party is the cloud provider who hosts the target infrastructure.

---

## Question 9

Which compliance standard explicitly requires external and internal penetration testing to be conducted at least annually, and what is the relevant requirement number?

- A) HIPAA, Security Rule §164.312
- B) GDPR, Article 32
- C) PCI DSS, Requirement 11.3
- D) SOC 2, CC6.1

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: PCI DSS Requirement 11.3 mandates that organizations perform penetration testing of their cardholder data environment at least annually and after any significant infrastructure or application changes.
- Why A is incorrect: HIPAA's Security Rule requires a risk analysis and implementation of appropriate safeguards but does not mandate penetration testing by name or set a specific annual requirement.
- Why B is incorrect: GDPR Article 32 requires organizations to implement appropriate technical security measures and regularly test them, but does not specify penetration testing or an annual cadence explicitly.
- Why D is incorrect: SOC 2 CC6.1 addresses logical access controls. While penetration testing can support SOC 2 audit evidence, it is not mandated by a specific SOC 2 control requirement the way PCI DSS mandates it.

---

## Question 10

During the pre-engagement phase, the penetration tester and client discuss testing the organization's internal network and its externally hosted marketing website. The marketing website is managed by a third-party web development firm. What must happen before the external website can be included in the scope?

- A) The website only needs to be listed in the RoE — no additional steps are required since the client owns the domain
- B) The tester must independently assess whether the third-party firm's systems are hardened before including them
- C) The client must obtain authorization from the third-party web development firm whose infrastructure hosts the site
- D) The tester must verify the site's SSL certificate to confirm the client's ownership before testing begins

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: When in-scope assets are hosted or managed by a third party, that third party must authorize testing of their infrastructure. Domain ownership does not grant the right to penetration test systems operated by another organization without that organization's consent.
- Why A is incorrect: Listing a system in the RoE only establishes the client's intent to include it. The RoE cannot grant authorization over infrastructure the client does not control.
- Why B is incorrect: Assessing the third party's security posture before including them in scope is not the correct procedure. The correct step is obtaining authorization, not evaluating their security.
- Why D is incorrect: SSL certificate verification confirms domain identity but has no bearing on penetration testing authorization. Authorization requires consent from the infrastructure operator.
