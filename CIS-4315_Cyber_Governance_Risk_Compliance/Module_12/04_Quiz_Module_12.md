# Quiz: Module 12 - Third-Party Risk and Vendor Management
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
What is the primary purpose of an IT security audit?
*   A) To write and refactor application source code to improve security
*   B) To evaluate whether security controls are adequately designed and operating effectively in alignment with policies, regulatory requirements, and organizational objectives
*   C) To execute penetration tests against production systems and document discovered vulnerabilities
*   D) To procure new security technologies recommended during the risk assessment process
*   **Correct Answer:** B) Auditors independently evaluate whether documented security controls actually operate as intended — both their design adequacy and operational effectiveness.
*   **Distractor Analysis:**
    *   *Why B is correct:* IT audits provide assurance (independent verification), not execution of security activities. The auditor assesses, not implements.
    *   *Why A is incorrect:* Code improvement is a development activity; auditors review code but do not write it.
    *   *Why C is incorrect:* Penetration testing is a technical assessment activity; while it may inform an audit, it is not what an IT security audit does.
    *   *Why D is incorrect:* Technology procurement is a security management function; auditors evaluate what exists, not recommend purchases.

---

**Question 2**
Which of the following most accurately describes **audit trail logs** in the context of information security assurance?
*   A) A formal report produced by an external auditor summarizing all security control findings and remediation recommendations
*   B) Configuration files that define the security settings applied to an information system at initial deployment
*   C) Chronological records of system events, user activities, and access transactions that enable reconstruction of what occurred and serve as tamper-evident audit evidence
*   D) The documented chain of custody for physical security equipment during a facility inspection
*   **Correct Answer:** C) Audit trail logs are the primary technical evidence of system activity — they must be comprehensive, accurate, and protected from tampering to serve as reliable audit evidence.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An audit report is a document produced by auditors; it is not itself an audit trail log.
    *   *Why B is incorrect:* Configuration files define settings but do not record events over time; audit trails are time-stamped event records.
    *   *Why C is correct:* Audit trails record who did what, when, and from where — they are essential for both security monitoring and forensic reconstruction.
    *   *Why D is incorrect:* Physical chain of custody documentation is specific to evidence handling; audit trail logs are digital event records from information systems.

---

**Question 3**
An internal audit reveals that the IT security team is responsible for both implementing security controls and auditing those same controls for effectiveness. What governance concern does this situation represent?
*   A) Excessive documentation burden on the security team due to overlapping responsibilities
*   B) A conflict of interest that compromises auditor independence — those who implement controls should not audit those same controls
*   C) A resource efficiency gain — combining implementation and audit reduces overhead
*   D) A violation of the principle of least privilege in access control design
*   **Correct Answer:** B) Auditor independence is a foundational principle — auditors cannot objectively assess controls they designed or implemented; the audit function must be organizationally separate.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The concern is independence and objectivity, not documentation burden.
    *   *Why B is correct:* Independence is required for audit assurance to be credible; self-assessment creates an inherent conflict of interest that undermines reliability.
    *   *Why C is incorrect:* Combining implementation and audit is not an efficiency gain — it is a governance failure that produces unreliable assurance.
    *   *Why D is incorrect:* Least privilege governs access rights to systems, not the organizational separation of duties in audit governance.

---

**Question 4**
During an IT audit, the auditor finds that a password policy requiring 90-day expiration is well-documented and approved but has not been technically enforced on any user accounts for two years. How should this finding be classified?
*   A) A design deficiency — the policy is not written clearly enough to be implemented
*   B) An operating effectiveness failure — the control exists on paper but is not functioning as designed
*   C) An informational observation — the policy gap poses no meaningful risk
*   D) A compensating control finding — other controls make up for the missing password expiration
*   **Correct Answer:** B) Operating effectiveness failures occur when a properly designed control is not actually being executed as required — the gap between policy intent and operational reality.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The policy is described as well-documented and approved; the design is adequate, but execution has failed.
    *   *Why B is correct:* This is a classic operating effectiveness failure — a control passes design review but fails in practice due to lack of enforcement.
    *   *Why C is incorrect:* An unenforced password policy creates real risk (unauthorized access, credential reuse) and is not merely informational.
    *   *Why D is incorrect:* The scenario does not describe any compensating controls; classifying it as compensating without evidence is incorrect.

---

**Question 5**
An external audit has produced a finding that a critical production system lacks multi-factor authentication for privileged access. As the security manager, what is the most appropriate immediate response?
*   A) Request that the auditor remove the finding from the report because MFA is on the roadmap for next year
*   B) Escalate the finding to the board and recommend replacing the entire authentication system immediately
*   C) Develop a formal corrective action plan with a defined timeline, responsible owner, and interim compensating controls, and submit it as the management response to the finding
*   D) Accept the finding as-is and wait for the next audit cycle to address it
*   **Correct Answer:** C) The appropriate governance response to an audit finding is a documented corrective action plan with ownership and timeline — not dispute, delay, or disproportionate response.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Attempting to suppress audit findings is a governance failure; findings must be acknowledged and addressed.
    *   *Why B is incorrect:* Escalating a control gap as a full system replacement recommendation is disproportionate; a targeted remediation plan is the appropriate response.
    *   *Why C is correct:* CISM governance practice requires formal management responses to audit findings that include remediation plans, owners, timelines, and interim controls.
    *   *Why D is incorrect:* Leaving a critical MFA gap unaddressed until the next audit cycle creates unacceptable risk and fails to demonstrate governance accountability.
