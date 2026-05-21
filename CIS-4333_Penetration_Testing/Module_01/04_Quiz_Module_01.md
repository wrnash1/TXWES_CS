# Quiz: Module 01 - Penetration Testing Methodology and Scoping
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which document explicitly defines the boundaries, methods, and authorized targets of a penetration test?
*   A) Non-Disclosure Agreement (NDA)
*   B) Rules of Engagement (RoE)
*   C) Service Level Agreement (SLA)
*   D) Master Service Agreement (MSA)
*   **Correct Answer:** B) The RoE sets rules, exclusions, IP targets, and schedule guidelines for the team.
*   **Distractor Analysis:**
    *   *Why correct:* The RoE sets rules, exclusions, IP targets, and schedule guidelines for the team.
    *   NDA protects confidential data. SLA is service uptime. MSA is general commercial agreements.

---

**Question 2**
In penetration testing, which of the following best defines **target classification**?
*   A) The process of assigning severity ratings to discovered vulnerabilities using CVSS scores after exploitation.
*   B) The categorization of in-scope assets by type and sensitivity level to guide testing methodology and prioritization.
*   C) A legal agreement that specifies which systems are excluded from testing to reduce liability for the testing firm.
*   D) A technique for fingerprinting operating systems by analyzing TTL values and TCP window sizes in network packets.
*   **Correct Answer:** B) The categorization of in-scope assets by type and sensitivity level to guide testing methodology and prioritization.
*   **Distractor Analysis:**
    *   *Why B is correct:* Target classification organizes in-scope systems by type (web app, network, wireless, physical) and sensitivity so testers apply the right methodology and prioritize higher-risk assets.
    *   *Why A is incorrect:* CVSS scoring occurs during the reporting phase, after testing — it is a vulnerability severity measurement, not a classification of targets.
    *   *Why C is incorrect:* Exclusion lists are part of the scoping document, not target classification. Classification groups what is in scope, not what is out.
    *   *Why D is incorrect:* OS fingerprinting via TTL/TCP analysis is a passive reconnaissance technique performed during the information-gathering phase, not a pre-engagement planning activity.

---

**Question 3**
A penetration tester has just completed active scanning of an in-scope subnet and discovers a server at an IP address that was not listed in the signed Rules of Engagement. What is the correct action?
*   A) Continue testing the server — it is on the same subnet as authorized systems, implying implicit authorization.
*   B) Run a service version scan to confirm whether it is a critical asset before deciding to proceed.
*   C) Stop testing the out-of-scope system immediately and notify the client to discuss whether authorization can be extended.
*   D) Document the server in the final report and include findings from any exploits run against it.
*   **Correct Answer:** C) Stop testing the out-of-scope system immediately and notify the client to discuss whether authorization can be extended.
*   **Distractor Analysis:**
    *   *Why C is correct:* The PT0-002 exam consistently tests that testers must halt activity on any system not explicitly authorized in the RoE and contact the client before proceeding. Unauthorized access — even accidental — violates authorization boundaries.
    *   *Why A is incorrect:* Subnet proximity does not imply authorization. Every in-scope target must be explicitly listed or described in the scoping document.
    *   *Why B is incorrect:* Running even a passive scan against an unauthorized host still constitutes unauthorized testing and creates legal exposure for the tester.
    *   *Why D is incorrect:* Including findings from an unauthorized system in the report would expose both the tester and the firm to legal liability.

---

**Question 4**
During the pre-engagement phase, a client asks a penetration tester to skip drafting a formal scoping document to save time, saying a verbal agreement is sufficient. What is the appropriate response from the tester?
*   A) Proceed with testing — verbal agreements are legally binding in most jurisdictions.
*   B) Accept the verbal agreement but record the conversation as documentation.
*   C) Decline to proceed until a written scoping document and Rules of Engagement are signed by an authorized representative.
*   D) Begin passive reconnaissance only, which does not require formal authorization.
*   **Correct Answer:** C) Decline to proceed until a written scoping document and Rules of Engagement are signed by an authorized representative.
*   **Distractor Analysis:**
    *   *Why C is correct:* Written authorization is a non-negotiable requirement in professional penetration testing. Without it, the tester has no legal protection and the activity could be considered unauthorized access under laws like the CFAA.
    *   *Why A is incorrect:* Verbal agreements are extremely difficult to enforce and provide no concrete protection if a dispute arises or if law enforcement becomes involved.
    *   *Why B is incorrect:* Recording a conversation does not carry the same legal weight as a signed authorization document and may not be admissible depending on jurisdiction.
    *   *Why D is incorrect:* Even passive reconnaissance against systems requires written consent — gathering publicly available information about a specific target in the context of a test is part of the authorized engagement.

---

**Question 5**
When designing a penetration test engagement for a financial institution, the client wants to ensure that any testers caught by internal security staff can prove the test is authorized. Which document serves this purpose and is sometimes called the "get-out-of-jail card"?
*   A) The Non-Disclosure Agreement (NDA) signed at the start of the engagement.
*   B) The penetration tester's professional certification (e.g., CompTIA PenTest+).
*   C) The written authorization letter or permission letter signed by an executive of the client organization.
*   D) The final penetration test report submitted after the engagement concludes.
*   **Correct Answer:** C) The written authorization letter or permission letter signed by an executive of the client organization.
*   **Distractor Analysis:**
    *   *Why C is correct:* The authorization/permission letter is a carry-on document that identifies the tester, the scope, and the dates of authorized testing. It is presented to internal security or law enforcement to confirm legitimacy — hence the nickname "get-out-of-jail card."
    *   *Why A is incorrect:* An NDA protects confidential information shared between parties but does not authorize testing or serve as proof of permission during an active engagement.
    *   *Why B is incorrect:* A certification proves the tester's qualifications but carries no legal authority to conduct a test on a specific organization's systems.
    *   *Why D is incorrect:* The final report is produced after testing concludes and is not a real-time authorization document that can be presented during active testing.
