# Quiz: Module 02 - Rules of Engagement and Legal Considerations

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash
**Instructions:** Select the single best answer for each question.

---

## Question 1

What must a penetration tester secure before executing any port scanning or exploitation tools against a client network?

- A) A public IP certificate from the client's domain registrar
- B) Written authorization from a client representative with legal authority over the systems
- C) Professional liability insurance for the engagement
- D) A server license for each tool used during testing

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Without written, signed authorization from a client representative with authority over the target systems, any scanning or exploitation is potentially a federal crime under the CFAA. Written authorization is the legal basis for all penetration testing activity.
- Why A is incorrect: A public IP certificate does not exist as a recognized pre-engagement authorization document. Domain certificates authenticate websites, not testing permissions.
- Why C is incorrect: Professional liability insurance is a best practice for testing firms but does not substitute for client authorization. Insurance does not make unauthorized access legal.
- Why D is incorrect: Server licenses govern software use rights, not the legal authorization to conduct security testing against systems.

---

## Question 2

Which of the following best defines a regulatory compliance framework such as PCI DSS in the context of penetration testing?

- A) A set of industry-specific security standards that mandate regular security assessments including penetration testing as a condition of compliance
- B) A cryptographic protocol that encrypts data in transit between client and server using asymmetric key pairs
- C) A software development methodology that uses iterative sprints and daily standups to coordinate team tasks
- D) A network architecture model where each layer is isolated from others to prevent lateral movement

**Correct Answer:** A

**Distractor Analysis:**

- Why A is correct: PCI DSS, HIPAA, GDPR, and similar frameworks define mandatory security controls and assessment requirements. PCI DSS Requirement 11.3 specifically mandates annual penetration testing for cardholder data environments.
- Why B is incorrect: This describes TLS or SSL encryption — a technical control, not a compliance framework requiring security assessments.
- Why C is incorrect: This describes Agile methodology, which is unrelated to security compliance requirements.
- Why D is incorrect: This describes defense-in-depth or DMZ network architecture, not a compliance standard.

---

## Question 3

A penetration tester's client has their web application hosted on a major cloud provider. The client's Rules of Engagement has been signed. What additional step is required before testing begins?

- A) No additional steps are needed — the signed RoE from the client covers all infrastructure including the cloud hosting environment
- B) Notify the client's IT department so they can monitor security alerts during testing
- C) Review the cloud provider's penetration testing policy and obtain any required prior notification or approval from that provider
- D) Restrict all testing to passive reconnaissance only, since active testing of cloud-hosted systems is never permitted

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Cloud providers own the underlying infrastructure and have their own acceptable use and penetration testing policies. Testing cloud-hosted systems without provider awareness may violate their terms of service and potentially trigger their incident response processes.
- Why A is incorrect: A client's authorization covers their application and data but does not extend to infrastructure owned and operated by the cloud provider.
- Why B is incorrect: Notifying the IT department is a good coordination practice but does not constitute required authorization from the cloud provider.
- Why D is incorrect: Active testing of cloud-hosted applications is permitted under the correct circumstances, but it requires proper authorization from both the client and the cloud provider.

---

## Question 4

During a penetration test, a tester accidentally takes down a production web server that is within the authorized scope. What is the correct immediate action?

- A) Attempt to restore the server using the exploited access and document the recovery steps in the report
- B) Continue testing other in-scope systems and include the outage in the final report as a finding
- C) Immediately stop testing, notify the client's designated emergency contact per the RoE, and document the incident thoroughly
- D) Move on quietly — unintended outages are expected and covered by the liability clause in the MSA

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The RoE defines an emergency contact and escalation procedure for unintended outages. Immediate notification is a professional and contractual obligation. Failing to notify promptly compounds damages and violates the engagement agreement.
- Why A is incorrect: Attempting self-recovery using exploited access may cause additional unauthorized changes and worsen the situation. The client's operations team is better positioned to restore their own systems.
- Why B is incorrect: Continuing to test after causing a service disruption without notifying the client is a serious breach of professional conduct and the RoE.
- Why D is incorrect: Liability clauses typically protect the tester only when they acted within scope and with due care. Concealing an incident would likely void those protections and increase legal exposure.

---

## Question 5

Which document in a penetration testing engagement specifically restricts the tester from sharing proprietary business information, network diagrams, and vulnerability findings with unauthorized parties?

- A) Rules of Engagement (RoE)
- B) Statement of Work (SOW)
- C) Non-Disclosure Agreement (NDA)
- D) System Security Plan (SSP)

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The NDA is a legally binding confidentiality contract that restricts the tester from disclosing sensitive information obtained during the engagement — including network architecture, discovered vulnerabilities, and business data — to unauthorized parties.
- Why A is incorrect: The RoE defines testing boundaries, permitted methods, and authorized targets. It governs what the tester may do, not what information may be shared externally.
- Why B is incorrect: The SOW defines project scope, deliverables, timeline, and pricing. It is a commercial agreement, not a confidentiality instrument.
- Why D is incorrect: A System Security Plan documents an organization's security controls, typically in FISMA or FedRAMP contexts. It is produced by the system owner, not the penetration tester.

---

## Question 6

A penetration tester discovers that the client's internal web server is running software with a known critical vulnerability. The RoE authorizes exploitation of confirmed vulnerabilities. The tester gains a shell and could easily read the entire customer database. According to the minimal footprint principle, what should the tester do?

- A) Read the database to confirm the full extent of data exposure and document all contents in the report as evidence
- B) Gain the shell, capture a screenshot proving access, and stop — do not read customer data beyond what is necessary to demonstrate impact
- C) Skip exploitation entirely since reading the database would violate customer privacy
- D) Exfiltrate a sample of the database to a secure testing server to preserve evidence for the report

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: The minimal footprint principle requires doing only what is necessary to demonstrate a vulnerability. Proving a shell was obtained and access was possible is sufficient. Reading an entire customer database goes beyond what is required to document the finding.
- Why A is incorrect: Reading the entire database is unnecessary to document the vulnerability and constitutes a far greater exposure of customer data than demonstrating the exploit requires.
- Why C is incorrect: The RoE authorizes exploitation, so gaining the shell is appropriate. The issue is how far exploitation extends — not whether exploitation occurs at all.
- Why D is incorrect: Exfiltrating actual customer data to a testing server creates serious privacy and legal exposure regardless of the secure storage. The RoE almost certainly prohibits actual data exfiltration.

---

## Question 7

Which US federal law governs the interception of electronic communications and may be relevant when a penetration tester performs man-in-the-middle traffic capture during an authorized engagement?

- A) Computer Fraud and Abuse Act (CFAA)
- B) Health Insurance Portability and Accountability Act (HIPAA)
- C) Electronic Communications Privacy Act (ECPA)
- D) Sarbanes-Oxley Act (SOX)

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The ECPA governs interception of wire, oral, and electronic communications. Man-in-the-middle testing that captures network traffic falls within the scope of the ECPA. The RoE authorization for traffic interception should specifically address ECPA compliance.
- Why A is incorrect: The CFAA governs unauthorized computer access. While also relevant to penetration testing broadly, it is not specifically the law addressing communications interception.
- Why B is incorrect: HIPAA governs protected health information in healthcare contexts. It is not the law governing interception of electronic communications during network testing.
- Why D is incorrect: SOX governs financial reporting controls for publicly traded companies. It has no direct application to traffic interception during security testing.

---

## Question 8

A penetration tester discovers what appears to be child sexual abuse material stored on a file server during an authorized engagement. What is the correct procedure?

- A) Continue the penetration test and include the discovery as a compliance finding in the final report
- B) Delete the material to protect the client from additional liability
- C) Stop the current testing activity, document what was observed without disturbing evidence, immediately notify the client through the escalation path in the RoE, and consult legal counsel about reporting obligations
- D) Anonymously report the finding to law enforcement without notifying the client, to avoid client interference

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Discovery of criminal activity requires stopping the test, preserving the scene without disturbing evidence, immediate client notification through established channels, and consultation with legal counsel. The tester should not attempt to investigate, delete, or act on the discovery independently.
- Why A is incorrect: Including criminal material discovery in a routine pentest report without immediate escalation is a serious failure of professional and likely legal obligation.
- Why B is incorrect: Deleting potential criminal evidence could constitute obstruction of justice and destroys forensic value for law enforcement.
- Why D is incorrect: Anonymous reporting without client notification bypasses the established escalation chain and may create legal complications. Legal counsel should determine the appropriate reporting path.

---

## Question 9

A penetration testing firm operates under an MSA with a client. During an engagement, a tester causes unintended damage to a production system. The MSA contains a liability limitation clause. Under what condition would that clause most likely NOT protect the tester?

- A) If the damage occurred on a system that was explicitly listed as in scope in the RoE
- B) If the tester was operating within the authorized testing window defined in the RoE
- C) If the tester concealed the incident from the client and did not notify the emergency contact as required by the RoE
- D) If the tester documented the incident thoroughly in the post-engagement report

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Liability limitation clauses typically apply only when the tester operates within the agreed scope and with due professional care. Concealing an incident and failing to follow the contractually required notification process is a breach of the agreement that would likely void the liability protection.
- Why A is incorrect: Damage to an in-scope system during authorized testing is precisely the scenario that liability clauses are designed to address. Being in scope supports the protection.
- Why B is incorrect: Operating within the authorized testing window is a condition that supports the liability protection, not one that undermines it.
- Why D is incorrect: Thorough documentation is good professional practice and would support — not undermine — the tester's position under a liability clause.

---

## Question 10

Which of the following describes responsible disclosure as it applies to a vulnerability found during a penetration test engagement?

- A) The tester publicly posts the vulnerability details to a security mailing list immediately after discovery to accelerate vendor patching
- B) The tester sells the vulnerability details to a third-party broker to maximize compensation
- C) The tester privately discloses all findings to the client in the penetration test report, and the client determines whether and how to report product vulnerabilities to the affected vendor
- D) The tester reports the vulnerability directly to the affected software vendor without informing the client first

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: In a penetration test engagement, all findings are disclosed to the client. If a vulnerability involves a third-party product, the client decides how to handle vendor disclosure. The tester's primary obligation is to the client, not to the vendor or the public.
- Why A is incorrect: Immediate public disclosure of vulnerabilities without notifying the client first violates the NDA and could cause serious harm. Responsible disclosure is private, not immediate and public.
- Why B is incorrect: Selling client vulnerability findings to third parties violates the NDA, the RoE, and basic professional ethics. It would constitute a serious breach of contract and potentially criminal behavior.
- Why D is incorrect: Reporting to a vendor without the client's knowledge and consent violates the confidentiality obligations established by the NDA and the trust relationship with the client.

---

### Question 11 (5 points)

A penetration tester is performing an authorized internal assessment and discovers a misconfigured file share containing payroll records with employee Social Security numbers. The RoE does not specifically address the discovery of personally identifiable information. What is the correct immediate action?

- A) Copy a sample of the records to the testing system as evidence to include in the final report
- B) Review all records to determine the full scope of the exposure before notifying the client
- C) Document the existence and location of the exposed data without reading or copying it, then notify the client through the RoE escalation path
- D) Continue testing and include the misconfiguration as a low-severity finding in the final report

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The minimal footprint principle requires documenting exposure without unnecessarily reading or copying sensitive data. The discovery of PII warrants immediate client notification regardless of whether the RoE specifically addresses it, because the client may have incident response or breach notification obligations triggered by the exposure.
  - Why A is incorrect: Copying payroll records containing SSNs to a testing system creates unauthorized data exfiltration and significant legal liability for the tester, even in an authorized engagement. The RoE almost certainly does not authorize exfiltration of actual employee data.
  - Why B is incorrect: Reviewing all records to assess scope goes far beyond what is needed to document the finding and constitutes unnecessary exposure of sensitive PII. The existence and location are sufficient to document the risk.
  - Why D is incorrect: A misconfigured file share exposing payroll records with SSNs is a high-severity finding, not low severity. Failing to immediately notify the client could delay their incident response obligations.

---

### Question 12 (5 points)

Which of the following best describes the difference between scope creep and an authorized scope expansion during a penetration test?

- A) Scope creep is testing additional systems with verbal approval; an authorized expansion requires written approval from the client's legal team only
- B) Scope creep is an unauthorized expansion of testing beyond the agreed RoE; an authorized expansion requires a written amendment to the RoE signed by an authorized client representative before additional testing begins
- C) Scope creep refers to testing more vulnerability types than originally planned within the same systems; authorized expansion means adding new tools not listed in the RoE
- D) There is no meaningful difference — both terms describe testing beyond the original plan, and both are acceptable as long as the client is aware

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Scope creep is unauthorized — it constitutes a CFAA violation regardless of the tester's intent. An authorized expansion must be formalized in writing before any activity on the new systems begins. Verbal approval, email approval, or after-the-fact documentation do not meet the written authorization standard.
  - Why A is incorrect: Verbal approval is insufficient for either scope creep correction or authorized expansion. Written authorization signed by an authorized client representative is required, not just legal team approval.
  - Why C is incorrect: Scope creep refers to expanding the systems or assets tested, not to using additional vulnerability types within authorized targets. Testing more techniques against an authorized system is within scope as long as the RoE authorizes those techniques.
  - Why D is incorrect: Scope creep is never acceptable. Unauthorized testing of systems outside the agreed scope is a CFAA violation regardless of awareness or intent.

---

### Question 13 (5 points)

Under the Electronic Communications Privacy Act (ECPA), which penetration testing activity would most likely require explicit authorization language in the RoE to ensure compliance?

- A) Running an Nmap port scan against an authorized web server
- B) Performing a man-in-the-middle attack to intercept and analyze unencrypted network traffic between authorized hosts
- C) Attempting SQL injection against an authorized web application
- D) Using Nessus to scan an authorized host for known CVE vulnerabilities

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The ECPA governs interception of wire and electronic communications. A man-in-the-middle attack that captures live network traffic is a form of communications interception. The RoE must specifically authorize this technique, and the authorization must come from an entity with legal authority over the communications being intercepted.
  - Why A is incorrect: An Nmap port scan sends probe packets to a host but does not intercept or capture the content of communications. It is not governed by ECPA.
  - Why C is incorrect: SQL injection targets a web application's input handling — it does not intercept communications between other parties. ECPA is not the relevant statute for this technique.
  - Why D is incorrect: Vulnerability scanning identifies service banners and open ports. It does not intercept the content of network communications between systems and is not an ECPA concern.

---

### Question 14 (5 points)

A penetration tester working on an engagement notices that a client employee is accessing systems in a way that suggests they may be committing insider fraud — moving money between accounts in small amounts just below reporting thresholds. This activity was not discovered through exploitation; it was visible in system logs the tester accessed through authorized means. What is the correct response?

- A) Ignore it — the engagement is a penetration test, not a fraud investigation, and this is outside the tester's role
- B) Collect as much evidence as possible about the suspected fraud and include it in the penetration test report
- C) Document what was observed, immediately notify the client through the RoE escalation path, and consult legal counsel about any reporting obligations
- D) Confront the employee directly and ask them to explain the activity

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: Discovery of suspected criminal activity requires stopping related activity, documenting observations, notifying the client through established escalation channels, and consulting legal counsel. The tester should not investigate independently, confront personnel, or include sensitive allegations in a routine pentest report without proper handling.
  - Why A is incorrect: Ignoring potential criminal activity discovered during an authorized engagement is not appropriate. The tester has professional and potentially legal obligations to report to the client through the RoE escalation path.
  - Why B is incorrect: Collecting extensive evidence about suspected fraud goes beyond the penetration tester's role and authorization. The tester is not a forensic investigator and collecting financial records beyond what was incidentally observed may exceed authorization.
  - Why D is incorrect: Confronting the employee is outside the penetration tester's role, potentially constitutes harassment, and could compromise a future fraud investigation by alerting the suspect.

---

### Question 15 (5 points)

Which of the following accurately describes the liability protection that an MSA indemnification clause provides to a penetration testing firm?

- A) It protects the testing firm from any legal consequence regardless of how the tester conducted themselves during the engagement
- B) It protects the testing firm from liability for unintended service disruptions that occur while the tester operated in good faith within the agreed scope and with due professional care
- C) It transfers all legal liability for system damage to the client, even if the tester acted outside the authorized scope
- D) It requires the client to pay for any systems that are damaged during testing, replacing the need for the tester to carry errors and omissions insurance

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Indemnification clauses in penetration testing contracts protect the tester from liability for unintended damage that occurs during authorized, in-scope testing conducted with reasonable professional care. They do not provide blanket protection for negligence, out-of-scope activity, or concealment of incidents.
  - Why A is incorrect: Indemnification is conditional, not absolute. Operating outside the agreed scope, exceeding authorization, or failing to follow notification requirements are typical conditions that void the protection.
  - Why C is incorrect: Indemnification does not shift liability for out-of-scope activity to the client. If the tester acted outside authorization, the tester retains liability regardless of the clause.
  - Why D is incorrect: An indemnification clause does not replace errors and omissions (E&O) insurance. Both serve complementary but distinct purposes in managing professional liability.

---

### Question 16 (5 points)

A penetration tester discovers a critical zero-day vulnerability in a widely used commercial software product while testing an authorized client environment. The vulnerability was not known to the vendor. According to responsible disclosure principles, what is the correct course of action?

- A) Publish a detailed proof-of-concept exploit to a public security mailing list immediately to maximize awareness and pressure the vendor to patch quickly
- B) Sell the vulnerability to a zero-day broker for maximum compensation since the tester discovered it through their own work
- C) Report the finding to the client in the penetration test report; the client and tester may then coordinate notification to the software vendor through the vendor's coordinated disclosure program
- D) Report the vulnerability directly and immediately to the vendor without telling the client, to prevent harm to other organizations

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The tester's primary duty is to the client. The finding is disclosed to the client in the engagement report. The client and tester can then determine how to responsibly notify the software vendor — typically through the vendor's coordinated disclosure or bug bounty program — while giving the vendor time to develop a patch before public disclosure.
  - Why A is incorrect: Immediate public disclosure without vendor notification is full disclosure, not responsible disclosure. It denies the vendor the opportunity to patch before exploitation, potentially harming users of the software globally.
  - Why B is incorrect: Selling vulnerability details discovered during a client engagement to a third-party broker violates the NDA and RoE, constitutes a serious breach of professional ethics, and may expose the tester to legal liability.
  - Why D is incorrect: Reporting directly to the vendor without the client's knowledge violates client confidentiality. The client has the right to be part of any disclosure decision involving vulnerabilities found during their engagement.

---

### Question 17 (5 points)

Which of the following statements about state computer crime laws is accurate in the context of penetration testing?

- A) Only federal law (CFAA) applies to penetration testing activities — state laws are preempted by federal statute
- B) State computer crime laws may apply simultaneously with the CFAA, and a tester operating across state lines may be subject to multiple state laws in addition to federal law
- C) State computer crime laws only apply to residents of that state, so out-of-state testers are not subject to them
- D) State computer crime laws exclusively govern social engineering activities; network testing is only regulated by the CFAA

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Federal and state computer crime laws can apply simultaneously. There is no complete federal preemption of state cybercrime laws. A penetration tester whose activities affect systems in multiple states may be subject to the computer crime laws of each state where a target system is located.
  - Why A is incorrect: The CFAA does not preempt state computer crime laws. States have their own statutes — such as California's CDAFA and Texas's Harmful Access by Computer Act — that apply independently of and concurrently with federal law.
  - Why C is incorrect: State computer crime laws apply based on the location of the affected system, not the residence of the actor. An out-of-state tester affecting systems in California can be subject to California's CDAFA.
  - Why D is incorrect: State computer crime laws broadly cover unauthorized computer access and are not limited to social engineering. Network testing activity that affects systems in a given state falls within the scope of that state's computer crime statutes.

---

### Question 18 (5 points)

During a penetration test, the tester gains access to a system and discovers a folder of files that appear to be client merger and acquisition documents that are not yet public. The RoE does not specifically mention M&A documents. What governs the tester's handling of these files?

- A) Since M&A documents are business records, not personal data, they have no special handling requirements during a pentest
- B) The minimal footprint principle and the NDA both govern handling — the tester documents the access to prove impact without reading the documents, and maintains strict confidentiality about their contents
- C) The tester should read the documents to assess whether they contain personally identifiable information that would trigger compliance obligations
- D) The tester should copy the documents to a secure server as evidence that sensitive data was accessible

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The minimal footprint principle requires documenting access (a screenshot proving the folder was accessible) without reading documents beyond what is necessary to identify their nature. The NDA requires strict confidentiality about all sensitive information encountered, including M&A materials. The tester documents the finding as a data exposure risk without consuming the confidential content.
  - Why A is incorrect: M&A documents are among the most sensitive business records that exist — their premature disclosure can violate securities laws and cause enormous business harm. They require careful handling regardless of whether they contain personal data.
  - Why C is incorrect: Reading the documents to search for PII goes far beyond what is needed to document that sensitive business records were accessible. The nature of the documents is evident without reading their full content.
  - Why D is incorrect: Copying confidential M&A documents to an external testing system constitutes unauthorized exfiltration of highly sensitive business materials and would violate the NDA and RoE data handling provisions.

---

### Question 19 (5 points)

A penetration tester is asked to sign an NDA before beginning an engagement. The NDA contains a clause requiring the tester to maintain confidentiality of the client's information indefinitely — with no expiration date. Why might this be a concern, and what is the standard professional response?

- A) NDAs should never be signed before an engagement because they prevent the tester from discussing the work publicly, which limits professional development
- B) An indefinite NDA is standard practice and poses no professional concerns — it is always appropriate to sign without modification
- C) Indefinite NDAs may be overly broad; the tester may negotiate a reasonable time-limited confidentiality period (such as two to three years) while accepting that some categories of information — such as specific vulnerability details — may warrant longer or permanent confidentiality
- D) The NDA's duration does not matter because the CFAA automatically voids any NDA clause more than one year old

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: Indefinite NDAs can create unreasonable ongoing obligations. Professional practice involves reviewing NDA terms carefully and negotiating appropriate time limits where reasonable, while recognizing that specific highly sensitive categories such as unpublished vulnerability details may warrant longer confidentiality. Legal review of NDA terms before signing is a standard practice for professional testing firms.
  - Why A is incorrect: NDAs are a standard and essential part of professional engagements — they protect the client and the tester. Refusing to sign NDAs would be highly unprofessional and would prevent legitimate engagement.
  - Why B is incorrect: Not all NDA terms are standard or appropriate. Indefinite confidentiality obligations may create legal and professional burdens that should be reviewed and, if necessary, negotiated before signing.
  - Why D is incorrect: The CFAA governs unauthorized computer access, not contract law. It has no provision that voids NDA clauses based on duration.

---

### Question 20 (5 points)

A penetration testing engagement has concluded and the tester has delivered the final report. The RoE stated that all testing data must be destroyed 30 days after report delivery. The client calls on day 45 asking if the tester still has the raw notes and exploitation logs from the engagement. What is the correct response?

- A) Provide the notes and logs immediately — client requests always supersede contractual data destruction timelines
- B) Charge an additional fee for late retrieval and then provide the stored data
- C) Explain that per the data handling agreement in the RoE, all engagement data was destroyed on day 30 and is no longer available
- D) Provide whatever data is still available and update the RoE retroactively to extend the retention period

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The data destruction timeline in the RoE is a contractual obligation. If the tester properly destroyed engagement data on day 30 as agreed, that is the correct professional response to report to the client. The tester cannot and should not retroactively extend a retention period that has already passed.
  - Why A is incorrect: Client requests after agreed data destruction timelines have passed cannot override contractual data handling obligations. The tester is not required to retain data beyond the agreed period and may have destroyed it to comply with the contract.
  - Why B is incorrect: Billing for late retrieval is irrelevant if the data no longer exists due to proper contractual destruction. If the data was retained beyond the agreed period, that would itself be a violation of the data handling agreement.
  - Why D is incorrect: Retroactively modifying an RoE after the engagement has concluded is not appropriate. Contract amendments must occur before or during the engagement, not after. Providing data that should have been destroyed is also a violation of the agreed data handling terms.
