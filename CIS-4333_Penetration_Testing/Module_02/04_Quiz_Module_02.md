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
