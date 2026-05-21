# Quiz: Module 04 - Risk Assessment and Treatment
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
Why is asset classification critical to an effective risk management program?
*   A) It speeds up network packet routing by tagging frames with priority labels
*   B) It ensures that appropriate security controls are applied based on the value and sensitivity of information assets
*   C) It reduces local hard drive storage consumption by compressing low-priority files
*   D) It enables database administrators to write more efficient SQL schema definitions
*   **Correct Answer:** B) Classification allows organizations to apply cost-proportionate, high-tier security controls to sensitive assets while avoiding over-investment in low-risk areas.
*   **Distractor Analysis:**
    *   *Why B is correct:* Classification is a resource prioritization mechanism that connects asset sensitivity to control requirements — a core CISM Domain 2 concept.
    *   *Why A is incorrect:* Network QoS tagging is a networking function unrelated to information classification.
    *   *Why C is incorrect:* Storage management is an IT operations concern; classification is about risk-based access and protection decisions.
    *   *Why D is incorrect:* Database schema design is a development activity with no relationship to information security classification.

---

**Question 2**
Which of the following most accurately describes **asset valuation metrics**?
*   A) The cryptographic key length and algorithm type used to encrypt stored data
*   B) Performance benchmarks that measure how quickly a system processes database queries under peak load
*   C) Quantitative or qualitative measures used to determine the business value of an information asset, informing risk prioritization and security investment decisions
*   D) The number of user accounts with administrative privileges on a given system
*   **Correct Answer:** C) Asset valuation metrics assess what an asset is worth to the organization — combining financial, operational, regulatory, and reputational dimensions to prioritize risk treatment.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cryptographic parameters are a control implementation choice, not an asset valuation metric.
    *   *Why B is incorrect:* System performance benchmarks are operational metrics, not security asset valuations.
    *   *Why C is correct:* Valuation metrics (replacement cost, revenue dependency, regulatory exposure, reputational impact) are the inputs CISM-aligned risk managers use to justify security investment.
    *   *Why D is incorrect:* Privileged account counts are an access control metric, not an asset valuation measure.

---

**Question 3**
In an organization's information security program, who should be designated as the **owner** of a customer records database?
*   A) The database administrator who manages the server configurations
*   B) The network security engineer responsible for firewall rules protecting the database segment
*   C) The business unit manager whose department relies on the data to fulfill its function
*   D) The CISO, because all information assets fall under the security organization's ownership
*   **Correct Answer:** C) Asset ownership belongs to the business unit that has operational accountability for the data — not the IT team that maintains the infrastructure.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The DBA is the custodian (technical steward), not the owner; custodians implement controls on behalf of the owner.
    *   *Why B is incorrect:* Network engineers manage infrastructure protection but do not own the data assets themselves.
    *   *Why C is correct:* CISM and ISO 27001 define asset owners as the individuals or organizational units accountable for the asset's appropriate use and protection.
    *   *Why D is incorrect:* The CISO provides governance oversight and policy direction; assigning asset ownership to the CISO creates an organizational conflict of interest and overloads the security function.

---

**Question 4**
An organization discovers it has hundreds of untracked servers in a data center. Which risk management capability is most directly undermined by this situation?
*   A) Incident response — because security analysts cannot contain threats they are unaware of
*   B) Asset inventory management — because risk assessments cannot be performed on undiscovered assets
*   C) Change management — because untracked servers may have unauthorized software installed
*   D) Vulnerability management — because patch agents cannot be deployed to unknown systems
*   **Correct Answer:** B) An incomplete asset inventory is the most foundational failure — you cannot assess, protect, or manage risk for assets you do not know exist.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While incident response is impacted, the primary failure is inventory management — the root cause of all downstream problems.
    *   *Why B is correct:* CISM and virtually all GRC frameworks establish asset identification as the prerequisite to all risk management activities.
    *   *Why C is incorrect:* Change management is affected, but it is a secondary consequence of the inventory gap.
    *   *Why D is incorrect:* Vulnerability management is also impacted, but it is a downstream consequence of missing inventory data, not the primary capability undermined.

---

**Question 5**
An organization is classifying its information assets. Which asset would most appropriately be assigned the highest classification tier (Restricted/Confidential)?
*   A) The company's public-facing careers page content
*   B) The IT department's internal help desk ticketing system procedures
*   C) Customer credit card numbers and authentication credentials
*   D) The corporate holiday schedule published on the intranet
*   **Correct Answer:** C) Credit card numbers and authentication credentials carry the highest regulatory exposure (PCI DSS, breach notification laws) and potential for direct financial and reputational harm.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Public-facing web content is by definition public; it requires no confidentiality protection.
    *   *Why B is incorrect:* Internal procedures are Internal or Confidential at most, but do not approach the sensitivity of regulated personal financial data.
    *   *Why C is correct:* Payment card data and credentials are regulated data types subject to PCI DSS and privacy laws, requiring the strongest protection tier.
    *   *Why D is incorrect:* A published holiday schedule is low-sensitivity internal information with no regulatory requirements.
