# Quiz: Module 05 - Compliance – HIPAA, PCI DSS, SOX, GDPR
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
An asset worth $100,000 has an exposure factor of 40% if a server room flood occurs. The flood risk occurs once every 5 years. What is the ALE?
*   A) $40,000
*   B) $200,000
*   C) $8,000
*   D) $20,000
*   **Correct Answer:** C) SLE = $100,000 × 0.40 = $40,000. ARO = 1/5 = 0.2. ALE = SLE × ARO = $40,000 × 0.2 = $8,000.
*   **Distractor Analysis:**
    *   *Why C is correct:* This applies the correct ALE formula chain: SLE first, then multiply by ARO.
    *   *Why A is incorrect:* $40,000 is the SLE — the single-event loss before annualizing. It does not account for how frequently the event occurs.
    *   *Why B is incorrect:* $200,000 results from multiplying asset value by ARO without applying the exposure factor — an incorrect calculation.
    *   *Why D is incorrect:* $20,000 results from applying only a 20% exposure factor or an incorrect ARO — neither matches the scenario.

---

**Question 2**
Which of the following most accurately describes **likelihood** in the context of risk assessment?
*   A) The dollar value of an information asset before considering any potential losses
*   B) The percentage of an asset's value that would be lost in a single occurrence of a risk event
*   C) The maximum amount of data an organization can afford to lose before a backup restore is required
*   D) The probability or frequency with which a threat will successfully exploit a vulnerability within a defined period, often expressed as an Annualized Rate of Occurrence
*   **Correct Answer:** D) Likelihood represents the probability dimension of risk; without assessing how often a threat event occurs, it is impossible to calculate meaningful risk exposure.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes asset value — a separate input to SLE calculation.
    *   *Why B is incorrect:* That describes the Exposure Factor (EF) component of the SLE formula.
    *   *Why C is incorrect:* That describes Recovery Point Objective (RPO) — a business continuity metric.
    *   *Why D is correct:* Likelihood (ARO in quantitative terms) is what transforms a potential harm into an expected annual cost in the ALE formula.

---

**Question 3**
A security manager needs to quickly assess risk across 50 business processes within a two-week budget cycle. The organization lacks sufficient financial data to assign dollar values to all assets. Which risk assessment method is most appropriate?
*   A) Quantitative assessment using ALE calculations for all 50 processes
*   B) Penetration testing of all systems to identify exploitable vulnerabilities
*   C) Qualitative assessment using a likelihood-impact matrix with High/Medium/Low ratings
*   D) A full audit against NIST SP 800-53 controls for each business process
*   **Correct Answer:** C) Qualitative assessment is appropriate when financial data is unavailable and a broad, rapid assessment is needed to prioritize further analysis.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Quantitative ALE calculation requires financial asset data that the scenario states is unavailable — it is also too resource-intensive for a two-week window covering 50 processes.
    *   *Why B is incorrect:* Penetration testing identifies technical vulnerabilities; it is not a risk assessment methodology for business processes.
    *   *Why C is correct:* Qualitative risk matrices (5×5 likelihood × impact grids) provide rapid, communicable risk rankings without requiring detailed financial data.
    *   *Why D is incorrect:* A full NIST SP 800-53 control audit is a compliance assessment activity, not a risk assessment, and would far exceed a two-week timeline.

---

**Question 4**
What is the key distinction between a **threat** and a **vulnerability** in risk assessment terminology?
*   A) Threats are internal to the organization; vulnerabilities come from external sources
*   B) Threats are potential harmful events or actors; vulnerabilities are weaknesses that threats can exploit
*   C) Threats are documented in audit reports; vulnerabilities are identified during penetration tests only
*   D) Threats apply to data in transit; vulnerabilities apply to data at rest
*   **Correct Answer:** B) Risk exists when a credible threat can exploit an existing vulnerability to cause impact — both elements must be present.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Threats can be internal (insider threats) or external; vulnerabilities can exist internally or externally in systems.
    *   *Why B is correct:* This is the standard CISM/NIST definition — threats exploit vulnerabilities to cause impact, forming the risk equation.
    *   *Why C is incorrect:* Both threats and vulnerabilities are identified through multiple methods including assessments, threat intelligence, and audits.
    *   *Why D is incorrect:* Threats and vulnerabilities apply to all data states and contexts, not segmented by data location.

---

**Question 5**
After conducting a risk assessment, an organization determines that a web application vulnerability has a High likelihood of exploitation and a High impact if exploited. According to risk matrix principles, what is the most appropriate next action?
*   A) Accept the risk and document it in the risk register with no further action
*   B) Transfer the risk by purchasing additional cyber insurance coverage
*   C) Prioritize the risk for immediate treatment — such as patching, additional controls, or remediation — given its High-High classification
*   D) Defer treatment until the next annual risk assessment cycle
*   **Correct Answer:** C) A High likelihood / High impact risk falls in the critical zone of a risk matrix and requires immediate, prioritized treatment action.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Risk acceptance is appropriate only for low or residual risks within the organization's risk appetite; a High-High risk exceeds acceptable levels.
    *   *Why B is incorrect:* Insurance (risk transfer) reduces financial impact but does not address the exploitation risk or protect the application itself.
    *   *Why C is correct:* CISM Domain 2 establishes that High-High risks must be prioritized for treatment — the appropriate response is remediation or compensating controls.
    *   *Why D is incorrect:* Deferring a critical risk until the next annual cycle is a governance failure; High-High risks require prompt management attention.
