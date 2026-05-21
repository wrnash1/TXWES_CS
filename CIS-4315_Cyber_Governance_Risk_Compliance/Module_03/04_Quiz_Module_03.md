# Quiz: Module 03 - Risk Management Frameworks (NIST RMF, ISO 27005)
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
What is the first step of the NIST Risk Management Framework (RMF) as defined in SP 800-37 Rev. 2?
*   A) Categorize System
*   B) Select Controls
*   C) Prepare
*   D) Implement Controls
*   **Correct Answer:** C) The updated RMF introduced the Prepare step to establish the organizational context, assign roles, and align risk management strategy before system-level work begins.
*   **Distractor Analysis:**
    *   *Why C is correct:* SP 800-37 Rev. 2 added Prepare as a preliminary step to improve efficiency and ensure risk management activities are organizationally anchored.
    *   *Why A is incorrect:* Categorize is the second step; it follows Prepare and focuses on determining the system's impact level.
    *   *Why B is incorrect:* Select Controls is the third step, occurring after categorization.
    *   *Why D is incorrect:* Implement Controls is the fourth step in the RMF sequence.

---

**Question 2**
Which of the following most accurately describes a **risk management framework**?
*   A) A software platform used to automate vulnerability scanning and patch management across enterprise endpoints
*   B) A structured methodology providing organizations with a repeatable, documented process for identifying, assessing, treating, and monitoring information security risks
*   C) A set of cryptographic algorithms approved for use in protecting classified government communications
*   D) A project management approach that schedules security activities in two-week development sprints
*   **Correct Answer:** B) Risk management frameworks provide the organizational structure and process consistency needed to make risk decisions in a repeatable, auditable way.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Vulnerability scanners are technical tools, not risk management frameworks.
    *   *Why B is correct:* This definition captures the essential purpose of frameworks like NIST RMF and ISO 27005 — structured, repeatable risk management processes.
    *   *Why C is incorrect:* Cryptographic algorithm suites (e.g., CNSS-approved algorithms) are a standards concern, not a risk management framework.
    *   *Why D is incorrect:* Agile sprint methodology is a software development approach unrelated to information security risk management.

---

**Question 3**
An organization is implementing NIST RMF for a new payroll processing system. The security team has completed system categorization and control selection. Which step should they perform next?
*   A) Authorize the system for operation
*   B) Monitor the system for ongoing compliance
*   C) Implement the selected security controls
*   D) Prepare the organizational risk management strategy
*   **Correct Answer:** C) After selecting controls (Step 3), the next RMF step is Implement (Step 4), where selected controls are put in place and documented.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Authorize (Step 6) occurs after controls are implemented and assessed — it cannot precede implementation.
    *   *Why B is incorrect:* Monitor (Step 7) is the final ongoing step; it follows authorization.
    *   *Why C is correct:* The RMF sequence after Select is Implement — controls must be deployed before they can be assessed.
    *   *Why D is incorrect:* Prepare is Step 1; it precedes all subsequent steps and cannot be revisited mid-process as a next step here.

---

**Question 4**
What is the primary purpose of system categorization in the NIST RMF (using FIPS 199)?
*   A) To assign a dollar value to each information system for insurance and asset management purposes
*   B) To determine the potential impact (Low, Moderate, High) of a security breach on organizational operations, assets, and individuals, which drives control selection
*   C) To rank the priority of software development projects in the IT project portfolio
*   D) To classify data by sensitivity level for storage location decisions
*   **Correct Answer:** B) Categorization sets the impact level of the system, which directly determines the appropriate baseline of security controls from NIST SP 800-53.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Financial asset valuation is an accounting function separate from FIPS 199 impact categorization.
    *   *Why B is correct:* FIPS 199 evaluates the potential impact on Confidentiality, Integrity, and Availability — the result drives control baseline selection in SP 800-53.
    *   *Why C is incorrect:* Project portfolio prioritization is an IT governance function, not an RMF categorization activity.
    *   *Why D is incorrect:* Data classification is a related but separate process; FIPS 199 categorizes systems based on potential impact, not data sensitivity labels.

---

**Question 5**
A federal agency has deployed a Moderate-impact system, completed all RMF steps through Assessment, and received a favorable assessment report. What is the appropriate next action?
*   A) Begin continuous monitoring immediately without additional review
*   B) Submit the security authorization package to the Authorizing Official for an Authorization to Operate (ATO) decision
*   C) Restart the RMF process from the Categorize step to confirm the impact level
*   D) Implement additional High-baseline controls to ensure comprehensive coverage
*   **Correct Answer:** B) After a favorable assessment, the authorization package (System Security Plan, SAR, POA&M) goes to the Authorizing Official, who makes the ATO decision based on residual risk.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Continuous monitoring (Step 7) requires a formal authorization decision first; systems cannot enter production without an ATO.
    *   *Why B is correct:* RMF Step 6 (Authorize) requires the Authorizing Official to review the package and formally accept residual risk before the system operates.
    *   *Why C is incorrect:* Re-categorization is only triggered by significant system changes, not as a routine post-assessment step.
    *   *Why D is incorrect:* Applying High-baseline controls to a Moderate system is disproportionate and not called for by the RMF process unless the categorization is revised upward.
