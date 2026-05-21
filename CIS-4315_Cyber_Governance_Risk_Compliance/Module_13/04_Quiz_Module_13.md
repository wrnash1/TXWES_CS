# Quiz: Module 13 - Data Classification and Privacy Management
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
What is the key difference between a SOC 2 Type I and a SOC 2 Type II report?
*   A) Type I covers only the Security trust criterion; Type II covers all five Trust Services Criteria
*   B) Type I assesses whether controls are suitably designed at a specific point in time; Type II evaluates whether controls operated effectively over a defined review period
*   C) Type I reports are publicly available; Type II reports are confidential and restricted to contracting parties
*   D) Type I is required for software companies; Type II is required for hardware vendors
*   **Correct Answer:** B) Type II provides stronger assurance by validating that controls actually worked over time, not just that they were designed correctly on a single date.
*   **Distractor Analysis:**
    *   *Why B is correct:* This is the AICPA-defined distinction — Type I is a design assessment snapshot; Type II demonstrates sustained operational effectiveness over the review period (6–12 months typically).
    *   *Why A is incorrect:* Both Type I and Type II can cover any combination of the five Trust Services Criteria; the Type I/II distinction is about assessment period, not criteria scope.
    *   *Why C is incorrect:* Both Type I and Type II reports are restricted-use documents shared only with relevant parties; neither is publicly available by default.
    *   *Why D is incorrect:* SOC 2 applies to service organizations broadly; the type is not determined by whether the vendor provides software or hardware.

---

**Question 2**
Which of the following most accurately describes a **security questionnaire** as a vendor risk management tool?
*   A) A formal contract document that defines penalties for vendor security breaches and data loss events
*   B) A penetration testing methodology that vendors must complete before accessing organizational systems
*   C) A standardized set of questions used to assess a vendor's security controls, policies, and practices during onboarding and periodic review
*   D) A regulatory filing submitted to government agencies to declare a vendor's compliance status
*   **Correct Answer:** C) Security questionnaires are the most common initial vendor assessment tool — they provide structured insight into a vendor's security program without requiring an onsite audit.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes a contract or SLA provision, not a security questionnaire.
    *   *Why B is incorrect:* Penetration testing is a technical assessment activity, not a questionnaire-based process.
    *   *Why C is correct:* Security questionnaires (SIG, CAIQ, VSA) are standard risk assessment instruments used to evaluate vendor security posture.
    *   *Why D is incorrect:* Security questionnaires are internal risk management tools; they are not regulatory filings submitted to government agencies.

---

**Question 3**
A company outsources its customer data processing to a cloud vendor. The vendor later suffers a data breach exposing customer records. Which statement best describes the company's accountability?
*   A) The company bears no accountability because it contracted the processing to a qualified vendor
*   B) The company is solely responsible for the breach since it chose to share data with the vendor
*   C) The company retains accountability to its customers and regulators for the security of their data, even when processing is delegated to a vendor
*   D) Accountability transfers to the cloud vendor's cyber insurance provider upon breach notification
*   **Correct Answer:** C) Organizations cannot outsource regulatory and customer accountability for data security — they remain responsible for selecting appropriate vendors and ensuring adequate contractual protections are in place.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Outsourcing processing does not transfer the originating organization's compliance obligations or customer responsibilities.
    *   *Why B is incorrect:* The vendor also bears responsibility; this is a shared accountability situation, not sole organizational blame.
    *   *Why C is correct:* CISM Domain 2 and virtually all privacy regulations (GDPR, HIPAA, CCPA) establish that data controllers/covered entities remain accountable for processor/vendor breaches.
    *   *Why D is incorrect:* Insurance is a risk transfer mechanism; it does not transfer legal or regulatory accountability to the insurer.

---

**Question 4**
An organization is onboarding a new payroll processing vendor who will have access to sensitive employee data. The vendor provides only a SOC 2 Type I report dated 18 months ago. What is the most appropriate security response?
*   A) Accept the Type I report as sufficient evidence of the vendor's ongoing security effectiveness
*   B) Request a current SOC 2 Type II report or an updated assessment, since an 18-month-old Type I report does not demonstrate current operating effectiveness
*   C) Waive the vendor assessment requirement because payroll vendors are low-risk
*   D) Conduct a full onsite penetration test of the vendor's infrastructure before proceeding
*   **Correct Answer:** B) An 18-month-old Type I report provides minimal current assurance; a Type II report covering recent operations, or a current assessment, is required for a high-access vendor handling sensitive data.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A Type I report assesses design at a single point in time; an 18-month-old Type I provides no evidence that controls are currently functioning.
    *   *Why B is correct:* For a vendor handling sensitive employee data, a current Type II report (or equivalent current assessment) is the appropriate standard.
    *   *Why C is incorrect:* Payroll vendors with access to sensitive employee financial data are high-risk, not low-risk; full assessment is appropriate.
    *   *Why D is incorrect:* While penetration testing has value, demanding a full offensive test as the initial onboarding step is disproportionate and not standard vendor risk management practice.

---

**Question 5**
An organization is developing its vendor risk management program and needs to determine how much scrutiny to apply to each vendor. Which approach best aligns with risk-based vendor management principles?
*   A) Apply the maximum level of security assessment to all vendors regardless of the data they access or their system connectivity
*   B) Tier vendors by their data access level and system connectivity, applying proportionate assessment depth — critical vendors receive full assessment; lower-risk vendors receive questionnaires and SLA requirements only
*   C) Require all vendors to obtain ISO 27001 certification as a condition of doing business
*   D) Conduct security assessments only for vendors that have experienced a known data breach in the past
*   **Correct Answer:** B) Risk-based vendor tiering applies proportionate scrutiny — high-risk vendors with sensitive data access receive rigorous assessment while lower-risk vendors receive lighter-touch review.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Applying maximum scrutiny to every vendor is impractical and wastes resources that should be focused on the highest-risk relationships.
    *   *Why B is correct:* Risk-based tiering (Tier 1/2/3 or equivalent) is the CISM-aligned approach to vendor management — proportionate effort matches proportionate risk.
    *   *Why C is incorrect:* Requiring ISO 27001 certification excludes many qualified vendors unnecessarily; not all vendors can or should pursue third-party certification.
    *   *Why D is incorrect:* Limiting assessments to vendors with known breach history misses the vast majority of vendor risk — a vendor without a known breach history may still have significant security deficiencies.
