# Quiz: Module 14 — Legal, Compliance, and Contractual Considerations

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

Which federal statute most directly creates criminal liability for accessing a computer system beyond the scope of written authorization during a penetration test?

A. 18 U.S.C. § 2511 — Electronic Communications Privacy Act

B. 18 U.S.C. § 1030 — Computer Fraud and Abuse Act

C. 15 U.S.C. § 6821 — Gramm-Leach-Bliley Act

D. 18 U.S.C. § 1343 — Wire Fraud

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The ECPA (18 U.S.C. § 2511) governs the interception of electronic communications. While relevant to packet capture without authorization, it does not directly address unauthorized computer access or "exceeding authorization."
- B is correct. The CFAA (18 U.S.C. § 1030) specifically prohibits both unauthorized access and access that "exceeds authorized access" to protected computers. Testing beyond the authorized scope constitutes exceeding authorization.
- C is incorrect. The GLBA pretexting provisions address obtaining customer financial information through false pretenses. They do not directly govern unauthorized computer system access.
- D is incorrect. Wire Fraud (18 U.S.C. § 1343) could theoretically apply if fraud was used to obtain access, but it is not the most direct statute. The CFAA specifically addresses unauthorized computer access.

---

**Question 2**

A penetration tester has written authorization to test `shop.example.com`. During testing, the tester discovers that `shop.example.com` makes API calls to `api.payments.thirdparty.com`, a payment processor not owned by the client. The tester believes the API is vulnerable to injection. What is the correct action?

A. Test the API since it was reached through the authorized application's normal functionality.

B. Do not test the API. Document the discovery, note it as a potential risk in the report, and recommend the client contact the third-party vendor for a separate assessment.

C. Test the API but limit testing to read-only operations that do not modify data.

D. Contact the payment processor directly and request emergency authorization to complete the test.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The client's authorization covers client-operated systems. `api.payments.thirdparty.com` is operated by a third party. The client cannot authorize testing of a system they do not own or operate. Testing it without the third party's authorization violates the CFAA regardless of how access was reached.
- B is correct. The tester documents the finding as an informational risk (third-party dependency vulnerability) and recommends the client engage the vendor through a formal assessment or bug disclosure. Testing the third-party system is out of scope and potentially illegal.
- C is incorrect. The restriction to "read-only operations" does not change the authorization problem. There is no authorized-read-only exception to the CFAA.
- D is incorrect. Contacting the payment processor during an active engagement to request authorization is impractical and would require the processor's formal testing authorization process, not a phone call during testing.

---

**Question 3**

A scope of work defines testing scope as "all systems at 10.10.0.0/16." During testing, the tester discovers that 10.10.15.100 belongs to a third-party vendor that provides outsourced HR services, operating within the client's IP range. What is the correct action?

A. Test the system since it is within the documented IP scope.

B. Stop testing the system, document its vendor ownership, notify the client, and obtain separate authorization from the vendor before including it in scope.

C. Test the system passively (port scan only) and include the results as informational.

D. Exclude the system and do not mention it in the report.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. IP scope does not override authorization requirements. The client cannot authorize testing of a third-party vendor's systems. An IP range scope that inadvertently includes third-party systems must be resolved before testing those systems.
- B is correct. Third-party systems require third-party authorization. The correct action is to pause testing on that specific host, document the ownership discovery, notify the client, and determine whether the vendor can and will authorize testing.
- C is incorrect. Passive testing (port scanning) still constitutes unauthorized access under the CFAA if the system is not within the authorized scope. The authorization deficiency is not resolved by limiting the testing intensity.
- D is incorrect. Discovering a third-party system within the client's IP range is a reportable finding — it indicates the client may not have accurate inventory of systems in their IP space. Omitting it entirely fails the client.

---

**Question 4**

Which document provides legal protection to a penetration tester who is stopped by law enforcement while conducting an authorized physical security assessment?

A. The non-disclosure agreement signed by both parties

B. The get-out-of-jail letter (authorization letter) carrying client letterhead and emergency contact

C. The tester's CompTIA PenTest+ certification card

D. The scope of work contract stored on the tester's laptop

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. An NDA governs confidentiality between the parties. It does not establish authorization to be on the premises or to conduct physical testing. Law enforcement has no obligation to accept an NDA as evidence of authorization.
- B is correct. The get-out-of-jail letter is a physical document on client letterhead, signed by a named client executive, explicitly authorizing the tester's activities. It includes a phone number for a contact who can verify authorization immediately. This is designed for exactly this situation.
- C is incorrect. A professional certification demonstrates competence but says nothing about authorization for a specific engagement. Law enforcement is not concerned with whether the tester is qualified — they are concerned with whether the tester is authorized.
- D is incorrect. An electronic document on a laptop is not suitable for presentation during a law enforcement encounter. The get-out-of-jail letter must be a physical document that can be presented without technology dependency.

---

**Question 5**

A bug bounty program's policy states "we will not pursue legal action against researchers who follow our guidelines." A researcher operating within the program's scope discovers a critical vulnerability but publishes full technical details publicly 48 hours after reporting, well before the vendor's 90-day remediation window. What is the legal status of the researcher?

A. Protected by the safe harbor since they discovered the vulnerability within the program scope.

B. Potentially liable since the safe harbor is conditioned on following the program guidelines, which include the disclosure timeline.

C. Protected by First Amendment rights to publish security research.

D. Protected since the vendor failed to respond within 24 hours of the report.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Safe harbor in bug bounty programs is conditional. The researcher must comply with all stated guidelines, including the disclosure timeline. Violating a material guideline condition forfeits the safe harbor protection.
- B is correct. The safe harbor provision is conditioned on following the guidelines. Early public disclosure before the remediation window violates the guidelines. The researcher may face civil claims for damages caused by the premature disclosure, and the safe harbor does not protect them.
- C is incorrect. First Amendment protections apply to government censorship of speech. They do not protect a private legal claim by a company that suffered damages from premature vulnerability disclosure. Constitutional rights do not override contractual obligations.
- D is incorrect. The guidelines specified a 90-day disclosure timeline, not a 24-hour vendor response requirement. Even if the vendor failed to respond quickly, the researcher's obligation to wait 90 days before public disclosure is separate from the vendor's acknowledgment timeline.

---

**Question 6**

Which of the following best describes the purpose of the Limitation of Liability clause in a penetration testing MSA?

A. It prevents clients from filing lawsuits against the testing firm for any reason.

B. It caps the testing firm's maximum financial exposure for claims arising from the engagement, typically at the engagement fee.

C. It limits the scope of testing to systems that the testing firm can test without causing harm.

D. It protects the client from liability if their systems harm the testing firm's infrastructure.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. A limitation of liability clause does not prevent lawsuits — it limits the financial exposure if a claim succeeds. Clients retain the right to sue; the clause limits recovery.
- B is correct. The limitation of liability sets a maximum on total damages recoverable. The standard approach: "Neither party's liability shall exceed the fees paid for the engagement." This protects the testing firm from catastrophic liability claims that could dwarf the engagement fee.
- C is incorrect. Limitations on testing scope are addressed in the SOW and ROE, not in the liability clause. The liability clause is purely about financial exposure.
- D is incorrect. This describes the reverse — client indemnification of the testing firm. The limitation of liability clause typically applies to the testing firm's liability to the client, though mutual caps are common.

---

**Question 7**

AWS requires customers to notify AWS before conducting penetration testing on certain service types. Which of the following is MOST accurate regarding this requirement?

A. AWS requires pre-approval for all penetration testing, including testing of EC2 instances.

B. AWS's Penetration Testing Policy permits testing of certain services (EC2, RDS, etc.) without pre-authorization but prohibits simulated DoS, DNS zone walking, and port flooding.

C. Testing any AWS service without prior written approval from AWS constitutes an ECPA violation.

D. AWS prohibits all third-party security testing of its infrastructure.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. AWS updated its policy to permit penetration testing of specific services (EC2, RDS, CloudFront, API Gateway, Lambda, Lightsail, Elastic Beanstalk, and Fargate) without pre-authorization, as long as the testing is of the customer's own resources.
- B is correct. AWS's current policy permits customer-authorized penetration testing of specific services without prior AWS notification. The policy explicitly prohibits simulated DDoS, DNS zone walking, and flooding attacks that could affect other AWS customers.
- C is incorrect. The ECPA governs communication interception. Testing AWS infrastructure, even without authorization, would implicate the CFAA and AWS's Terms of Service — not primarily the ECPA.
- D is incorrect. AWS explicitly permits penetration testing of its infrastructure for customer-operated resources under the Penetration Testing Policy. The prohibition is on specific attack types that could affect AWS's shared infrastructure.

---

**Question 8**

A security researcher discovers a critical vulnerability in a product from a small software company that has no bug bounty program and no published security contact. The researcher has responsibly attempted to contact the company but received no response after 14 days. What is the MOST appropriate next step?

A. Publish full technical details immediately since the company has failed to respond.

B. Attempt to contact the company once more, then consider engaging CISA's vulnerability coordination program for assistance if the vulnerability affects critical infrastructure.

C. Sell the vulnerability to a government buyer for maximum financial return.

D. Disclose to a mailing list such as Full Disclosure immediately to pressure the company to respond.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Immediate full disclosure after 14 days of non-response is premature. The standard responsible disclosure period is 90 days. Non-response at 14 days is common, especially for smaller companies without dedicated security staff. Responsible practice requires continued good-faith effort.
- B is correct. Making one additional contact attempt, then engaging CISA's vulnerability coordination capabilities for critical infrastructure vulnerabilities, follows the spirit of coordinated disclosure. CISA can engage vendors on the researcher's behalf and help facilitate remediation.
- C is incorrect. Selling discovered vulnerabilities to third-party buyers (including government agencies) without the affected vendor's involvement raises significant legal and ethical concerns. Vulnerability markets involving non-consensual discovery and sale create legal risk under the CFAA and have broader security implications.
- D is incorrect. Disclosing to Full Disclosure after only 14 days of non-response is contrary to coordinated disclosure norms. The 90-day window reflects the real-world time needed for patch development, testing, and distribution. Premature disclosure harms users who cannot yet patch.

---

**Question 9**

A penetration testing firm is engaged to assess a healthcare organization. During the assessment, the tester's own testing laptop is stolen from a rental car. The laptop contains the client's penetration test report in an unencrypted folder. Which insurance product is MOST directly relevant to the resulting liability?

A. General Liability insurance

B. Errors and Omissions (Professional Liability) insurance

C. Cyber Liability insurance

D. Property and Casualty insurance

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. General Liability covers bodily injury and property damage. The harm here is data exposure — a cyber liability issue, not a general liability issue.
- B is incorrect. E&O covers claims that professional services (the assessment itself) caused harm. A laptop theft is not a failure of professional services — it is a data security incident on the firm's own infrastructure.
- C is correct. Cyber Liability insurance covers data breaches involving the firm's own systems, including costs of notification, credit monitoring for affected individuals, forensic investigation, and legal defense. The theft of a laptop containing client PHI is exactly the scenario cyber liability insurance covers.
- D is incorrect. Property and Casualty insurance covers the physical loss of the laptop itself. It does not cover the liability arising from the data breach that results from the theft.

---

**Question 10**

A penetration tester completes an engagement and the report documents a Critical vulnerability. The client's CTO asks the tester to sign a document acknowledging that the vulnerability was "satisfactorily remediated" before the tester has verified the fix. What is the correct response?

A. Sign the document since the CTO has authority over the organization's security posture.

B. Refuse to sign. Offer to conduct a re-test of the specific finding and sign a remediation verification statement only after confirming the fix.

C. Sign the document with a handwritten notation that the statement is unverified.

D. Sign the document and note in the internal file that the signature was obtained under pressure.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The CTO's authority over the organization does not obligate the tester to make false professional representations. Signing a document falsely certifying remediation that has not been verified is professional misrepresentation.
- B is correct. The tester's professional integrity requires that remediation verification be based on actual testing. Offering to conduct a re-test — which is standard practice — allows the tester to issue an honest verification statement based on evidence.
- C is incorrect. Adding a notation acknowledges the misrepresentation but does not resolve it. A document certifying remediation should not be signed unless remediation has been confirmed.
- D is incorrect. This is the same misrepresentation as option A, with documentation of the coercion. The professional obligation is to refuse to sign without verification, not to document the circumstances under which a false statement was made.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | B |
| 6 | B |
| 7 | B |
| 8 | B |
| 9 | C |
| 10 | B |
