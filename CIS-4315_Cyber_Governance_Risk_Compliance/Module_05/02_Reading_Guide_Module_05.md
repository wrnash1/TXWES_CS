# Reading Guide: Module 05 - Compliance – HIPAA, PCI DSS, SOX, GDPR
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

### Introduction
Welcome to **Module 05 - Compliance: HIPAA, PCI DSS, SOX, GDPR**! This module covers the major regulatory and industry compliance frameworks that information security managers must navigate. Understanding compliance obligations is central to CISM Domain 1 (Security Governance) and Domain 2 (Risk Management).

CISM candidates must understand compliance not as a checklist exercise, but as a risk management discipline — organizations are compliant when their security controls sufficiently address the risks that regulations are designed to prevent.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Qualitative vs. quantitative risk assessment**: Qualitative assessment uses descriptive scales (High/Medium/Low) to rate the likelihood and impact of risks, making it faster to perform and easier to communicate to non-technical stakeholders. Quantitative assessment uses numerical values (dollar amounts, probabilities) to calculate financial exposure, producing more precise results that require more data and expertise.
*   **Threats**: Any potential event or actor capable of exploiting a vulnerability to cause harm to an information asset. Threats can be natural (floods, earthquakes), accidental (employee errors), or adversarial (hackers, insider threats). Threat identification is the first step in risk assessment.
*   **Vulnerabilities**: Weaknesses or gaps in an information system, process, or control that could be exploited by a threat to cause harm. Vulnerabilities do not represent risk by themselves — risk materializes only when a credible threat can exploit a vulnerability and cause meaningful impact.
*   **Likelihood**: The probability or frequency with which a threat will successfully exploit a vulnerability within a defined period. Likelihood assessments consider historical data, threat intelligence, and the effectiveness of existing controls. In quantitative analysis, likelihood is expressed as Annualized Rate of Occurrence (ARO).
*   **Impact**: The magnitude of harm that would result from a successful threat exploitation, considering effects on organizational operations, assets, individuals, and mission. Impact assessments consider direct costs (recovery, notification), indirect costs (reputation, lost business), and regulatory penalties.
*   **Single Loss Expectancy (SLE)**: The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV × EF), where the Exposure Factor represents the percentage of asset value lost in the event.
*   **Annualized Loss Expectancy (ALE)**: The expected annual financial loss from a specific risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE × ARO). ALE is used to justify security investments by comparing the cost of a control against the risk it reduces.

---

### 2. Certification Exam Tips
*   **ALE Calculation Is Testable:** Memorize the ALE formula chain: SLE = AV × EF; ALE = SLE × ARO. The CISM exam may present a scenario with numbers and ask you to calculate ALE or determine whether a control investment is cost-justified (invest if control cost < ALE reduction).
*   **Qualitative vs. Quantitative Choice:** The exam tests when to use each method. Qualitative is appropriate for quick, broad assessments or when financial data is unavailable. Quantitative is appropriate when financial justification is needed for control investment decisions.
*   **Threat vs. Vulnerability vs. Risk:** These are frequently confused on the exam. Remember: Threat exploits Vulnerability to cause Impact = Risk. All three components must be present for risk to exist.
*   **Study Resource:** [NIST SP 800-30 Rev. 1: Guide for Conducting Risk Assessments](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final) is a free publication that covers both qualitative and quantitative risk assessment methodologies in detail.

---

### Required Readings & Videos
*   **Required Reading:** [NIST SP 800-30 Rev. 1: Guide for Conducting Risk Assessments](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final) — This free NIST publication covers the risk assessment process including threat identification, vulnerability analysis, likelihood and impact determination, and risk level calculation. Focus on Chapter 3 (Core Risk Assessment Activities) and Appendix D (Threat Sources).
*   **Required Video:** Watch the video lecture on **Compliance Frameworks** in the official course playlist: [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply risk assessment concepts through the following activities:
*   **Calculate SLE and ALE for a given scenario**: Using provided asset values, exposure factors, and ARO values, compute SLE and ALE for three risk scenarios and determine which poses the highest annualized financial risk.
*   **Perform a qualitative risk mapping exercise**: Using a 5×5 risk matrix (Likelihood × Impact), plot 10 identified risks on the matrix and classify each as High, Medium, or Low priority for treatment.
*   **Compare qualitative and quantitative results**: For one selected risk, perform both a qualitative assessment (H/M/L rating) and a quantitative assessment (ALE calculation) and explain the trade-offs of each approach.


---

### 3. Study Checklist
- [ ] Memorize the ALE formula: SLE = AV × EF; ALE = SLE × ARO.
- [ ] Read [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final), Chapter 3.
- [ ] Watch the video lecture on **Compliance Frameworks** in [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).
- [ ] Complete the lab activity on SLE/ALE calculation and risk matrix mapping.
- [ ] Proceed to the Module 05 quiz.
