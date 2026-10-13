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

---

### Question 11 (5 points)

Which of the following engagement types is specifically designed to simulate an Advanced Persistent Threat (APT) and may include physical access, social engineering, and custom tooling — all within authorized boundaries?

- A) Gray box penetration test
- B) Vulnerability assessment
- C) Red team engagement
- D) Bug bounty program

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: A red team engagement is a long-duration, full-scope adversarial simulation that replicates the tactics, techniques, and procedures of an APT actor. It is explicitly authorized and may include physical access, social engineering, and custom malware within defined scope — far beyond a standard penetration test.
  - Why A is incorrect: A gray box test provides partial knowledge and follows a defined methodology, but it is scoped to technical testing and does not typically include physical access or social engineering unless explicitly authorized as separate scope items.
  - Why B is incorrect: A vulnerability assessment identifies and classifies weaknesses without actively exploiting them. It does not simulate attacker behavior and involves no exploitation or social engineering.
  - Why D is incorrect: A bug bounty program invites independent researchers to find and report vulnerabilities in specific scoped assets. It is not an adversarial simulation and is not designed to replicate APT behavior end-to-end.

---

### Question 12 (5 points)

A penetration tester is reviewing a signed Rules of Engagement document. The document lists authorized testing hours as "Monday through Friday, 8:00 AM to 5:00 PM EST." The tester finishes an authorized scan at 4:55 PM and notices that a service on a target host is responding unusually. What is the correct action?

- A) Continue investigating the unusual response because the root cause may be within scope and the window has not technically closed
- B) Stop all active testing at the end of the authorized window and document the observation for investigation the following authorized day
- C) Notify the client immediately that the test must be extended into after-hours to complete the investigation
- D) Switch to passive reconnaissance only after hours since passive techniques do not interact with systems

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The RoE testing window is an absolute boundary. When the authorized window closes, all active testing must stop regardless of what was being investigated. Observations should be documented and resumed during the next authorized period.
  - Why A is incorrect: The unusual response, while interesting, does not extend the authorized testing window. Any activity after 5:00 PM would be outside the agreed RoE boundaries and constitutes unauthorized access.
  - Why C is incorrect: Extending hours requires a written amendment to the RoE signed by the client. A unilateral decision to extend testing, even with verbal notification, is not authorized.
  - Why D is incorrect: Passive reconnaissance still directs investigation toward a specific target system and is an authorized testing technique. Conducting it outside the authorized window violates the time boundaries in the RoE.

---

### Question 13 (5 points)

A client requests a penetration test of their healthcare patient portal. The tester discovers during reconnaissance that the portal uses an authentication module provided by a third-party identity provider. The identity provider is NOT listed in the RoE. Which action is correct?

- A) Test the authentication module thoroughly — it is part of the web application and therefore implicitly in scope
- B) Skip the authentication module entirely and test only the portal's other functions
- C) Raise the third-party authentication module with the client and pause testing of that component until third-party authorization is obtained
- D) Perform only read-only input validation tests against the authentication module since these do not constitute exploitation

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The authentication module is operated by a third party whose infrastructure is not owned by the client. Third-party authorization is required before testing any component they operate, regardless of where it appears in the application flow.
  - Why A is incorrect: Being part of the web application flow does not grant implicit authorization to test third-party components. The infrastructure must be explicitly listed or separately authorized.
  - Why B is incorrect: Skipping the module without raising the issue with the client leaves a potential coverage gap undocumented and prevents the client from obtaining the necessary authorization to include it.
  - Why D is incorrect: Any active interaction with a third-party system — including input validation probing — constitutes testing activity that requires the third party's authorization.

---

### Question 14 (5 points)

Which of the following accurately describes the difference between a vulnerability assessment and a penetration test?

- A) A vulnerability assessment uses automated tools while a penetration test uses only manual techniques
- B) A vulnerability assessment identifies and classifies weaknesses without exploiting them; a penetration test actively attempts to exploit identified weaknesses to demonstrate real impact
- C) A vulnerability assessment is performed externally while a penetration test is always performed from inside the network
- D) A vulnerability assessment produces a report while a penetration test does not require formal documentation

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The key distinction is exploitation. A vulnerability assessment stops at identification and classification. A penetration test continues to exploitation in order to demonstrate the real-world impact of identified vulnerabilities — providing concrete evidence of risk.
  - Why A is incorrect: Both assessments can use automated tools. Penetration tests also routinely use automated tools such as Metasploit alongside manual techniques. Tool type is not the distinguishing factor.
  - Why C is incorrect: Both types of assessments can be performed externally, internally, or both. The perspective does not distinguish the two assessment types.
  - Why D is incorrect: Both types produce formal reports. Reporting is required for any professional security assessment regardless of whether exploitation occurred.

---

### Question 15 (5 points)

During engagement planning, the client requests that the penetration tester not disclose findings to the client's own IT staff until after the report is delivered to the CISO. What pre-engagement document should capture this confidentiality and disclosure restriction?

- A) Authorization letter
- B) Rules of Engagement communication protocol section
- C) Non-Disclosure Agreement
- D) Statement of Work deliverables section

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The RoE communication protocol section specifies who receives findings, when they are disclosed, and in what format. Restricting disclosure to the CISO until the final report is an operational communication rule that belongs in the RoE.
  - Why A is incorrect: The authorization letter establishes that testing is authorized and is carried on-site to prove legitimacy. It does not govern internal disclosure protocols.
  - Why C is incorrect: The NDA governs confidentiality between the testing firm and the client organization. It does not specify internal disclosure rules within the client's own organization.
  - Why D is incorrect: The SOW deliverables section describes what documents will be produced and when, not the internal disclosure chain or communication restrictions during the engagement.

---

### Question 16 (5 points)

A penetration tester is assigned to a white box engagement. On the first day the client provides full network diagrams, Active Directory structure, application source code, and administrative credentials. Which of the following is the primary advantage of white box testing over black box testing?

- A) White box testing is less expensive because it requires no reconnaissance phase
- B) White box testing provides higher assurance of thorough coverage because the tester can target all known components and logic paths without spending time discovering them
- C) White box testing is more realistic because it perfectly simulates how an external attacker approaches the organization
- D) White box testing results in fewer findings because the tester avoids wasting time on systems that are already documented as secure

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: White box testing's primary advantage is depth and coverage. By eliminating the time spent on discovery and reconnaissance, the tester can allocate all effort to thorough analysis of every known component, including code-level logic flaws that would be invisible to a black box tester.
  - Why A is incorrect: White box engagements are often more expensive than black box tests due to the depth of analysis required, particularly when source code review is included. Cost reduction is not the defining advantage.
  - Why C is incorrect: Realism of an external attacker simulation is the advantage of black box testing, not white box. White box simulates a knowledgeable insider or auditor, not an uninformed external threat.
  - Why D is incorrect: White box testing typically reveals more findings, not fewer, because complete system knowledge allows testers to identify subtle logic flaws and configuration issues that external testing would miss.

---

### Question 17 (5 points)

Which of the following best describes the purpose of the Penetration Testing Execution Standard (PTES)?

- A) A US federal law that criminalizes the use of penetration testing tools without a license
- B) A proprietary certification framework developed exclusively for CompTIA PenTest+ candidates
- C) An industry-standard framework that defines the phases of a professional penetration test from pre-engagement through reporting
- D) A government-mandated testing checklist required for all organizations subject to PCI DSS

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: PTES is an open industry framework defining six phases of a professional penetration test: pre-engagement interactions, intelligence gathering, threat modeling, vulnerability analysis, exploitation, and post-exploitation/reporting. It provides a consistent methodology reference for the profession.
  - Why A is incorrect: PTES is not a law. No US federal law specifically criminalizes penetration testing tools — the CFAA governs unauthorized access, not tool ownership or use.
  - Why B is incorrect: PTES is an open-source industry initiative, not a proprietary CompTIA product. The PT0-002 exam aligns to PTES but PTES was developed independently by security practitioners.
  - Why D is incorrect: PTES is not mandated by any compliance standard including PCI DSS. PCI DSS Requirement 11.3 mandates testing but does not specify a particular methodology framework.

---

### Question 18 (5 points)

A penetration tester completes an engagement for a retail client and produces the final report. Six months later the same client asks the tester to reference old notes to answer a question about a system vulnerability. According to professional data handling standards documented in the RoE, what should govern whether the tester can comply?

- A) The tester can always provide information from past engagements since the client is the same organization
- B) The tester should charge an additional consulting fee and then share the notes
- C) The data retention and destruction policy defined in the RoE governs how long engagement data is kept and under what conditions it may be shared
- D) The tester should post the old notes to a shared client portal for convenience

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The RoE data handling section specifies the retention period (for example, data destroyed 30 days after report delivery) and disclosure restrictions. If the notes were properly destroyed per the RoE, the tester cannot share them. If still within retention, disclosure must still follow the agreed channel and authorization.
  - Why A is incorrect: Client identity does not override data handling agreements. The RoE data handling terms define what can be retained and shared, not the client relationship.
  - Why B is incorrect: Billing is irrelevant to data handling obligations. Whether or not a fee is charged, the tester must comply with the data retention and destruction terms agreed in the RoE.
  - Why D is incorrect: Posting sensitive engagement findings to a shared portal without authorization would violate both the NDA and the RoE data handling provisions, creating confidentiality and security risks.

---

### Question 19 (5 points)

Which of the following scenarios most accurately describes an engagement that would be classified as a bug bounty program rather than a traditional penetration test?

- A) A company hires a single security firm to perform a two-week internal and external assessment under a signed RoE
- B) A company publishes a public or private program scope and invites independent researchers to find and responsibly disclose vulnerabilities in exchange for rewards
- C) A company's CISO requests an annual compliance test of the cardholder data environment under PCI DSS Requirement 11.3
- D) A company hires a red team to simulate an APT attack including physical intrusion over a three-month period

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: A bug bounty program defines a scope document and invites independent security researchers — not a single hired firm — to continuously find and responsibly disclose vulnerabilities, typically for monetary rewards. It is an ongoing program rather than a time-boxed engagement.
  - Why A is incorrect: A two-week engagement by a single hired firm under a signed RoE describes a traditional penetration test, not a bug bounty program.
  - Why C is incorrect: An annual compliance test under PCI DSS Requirement 11.3 is a structured, time-boxed penetration test driven by compliance requirements — not a bug bounty program.
  - Why D is incorrect: A three-month APT simulation with physical intrusion describes a red team engagement, which is distinct from a bug bounty program in scope, methodology, and authorization structure.

---

### Question 20 (5 points)

During pre-engagement scoping, a client proposes testing windows of 9:00 AM to 5:00 PM Monday through Friday for all systems, including production database servers. What risk should the penetration tester raise with the client about testing production systems during business hours?

- A) No risk exists — business-hours testing is standard industry practice and is preferred for reporting
- B) Business-hours testing of production systems increases the risk of service disruption affecting real users and business operations, and off-hours windows should be considered for critical production assets
- C) Business-hours testing creates additional legal liability because the CFAA applies differently during working hours
- D) Testing during business hours is always prohibited by PCI DSS Requirement 11.3

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Active penetration testing techniques against production systems carry a risk of service disruption or instability. Testing during peak business hours amplifies the impact of any disruption. Professional testers advise clients to schedule production system testing during off-hours or maintenance windows to minimize operational risk.
  - Why A is incorrect: Business-hours testing of production systems is not standard best practice — it is the higher-risk option. Best practice recommends low-traffic windows for production system testing.
  - Why C is incorrect: The CFAA does not distinguish between business hours and off-hours. The legal framework for authorized testing is the same regardless of time of day.
  - Why D is incorrect: PCI DSS Requirement 11.3 does not specify prohibited testing hours. It mandates annual testing but leaves scheduling decisions to the organization and its testing provider.
