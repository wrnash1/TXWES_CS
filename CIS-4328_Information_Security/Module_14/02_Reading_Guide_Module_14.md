# Reading Guide: Module 14 - Risk Management and Business Continuity
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 14 – Risk Management and Business Continuity**! Risk management is the process of identifying, analyzing, and responding to threats to organizational assets. Business continuity planning ensures operations can survive and recover from disruptive events. SY0-701 tests both disciplines heavily in Domain 5 (Security Program Management and Oversight, 20%).

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Risk Terminology (Asset, Threat, Vulnerability, Risk)**: An asset is anything of value to the organization (data, systems, people). A threat is any potential cause of harm to an asset. A vulnerability is a weakness that a threat can exploit. Risk is the likelihood that a threat will exploit a vulnerability and the resulting impact. SY0-701 tests these definitions and the relationships between them — risk exists only when a vulnerability is exposed to a threat.
*   **Risk Response Strategies**: The four standard ways to handle identified risks: (1) Mitigation — implement controls to reduce the likelihood or impact (e.g., patch the vulnerability); (2) Avoidance — stop the activity that creates the risk (e.g., discontinue a vulnerable service); (3) Transference — shift the financial impact to a third party (e.g., purchase cyber insurance); (4) Acceptance — acknowledge the risk and take no action, typically documented for low-severity risks. SY0-701 scenarios test selecting the appropriate response for a given risk context.
*   **Risk Quantification (ALE, SLE, ARO)**: Key formulas for quantifying risk financially. Single Loss Expectancy (SLE) = Asset Value × Exposure Factor (the percentage of asset value lost per incident). Annualized Rate of Occurrence (ARO) = how many times the incident is expected per year. Annualized Loss Expectancy (ALE) = SLE × ARO. ALE is used to justify security control costs — a control costing less than the ALE reduction it provides is financially justified.
*   **Business Continuity Plan (BCP)**: A comprehensive plan that ensures critical business functions can continue during and after a disruptive event (natural disaster, cyberattack, power outage). A BCP addresses people, processes, and technology. It encompasses both the Disaster Recovery Plan (DRP) for IT systems and broader operational continuity. SY0-701 tests BCP as the overarching plan for organizational resilience.
*   **Recovery Time Objective (RTO) and Recovery Point Objective (RPO)**: RTO is the maximum acceptable duration of downtime — how quickly a system must be restored after a disruption. RPO is the maximum acceptable data loss measured in time — how old the restored data can be. Example: RTO of 4 hours means systems must be back online within 4 hours of a failure; RPO of 1 hour means no more than 1 hour of data can be lost. Lower RTO/RPO values require more investment in redundancy and frequent backups.
*   **Disaster Recovery Site Types**: Three tiers of alternate site readiness. Hot site — a fully equipped, continuously operational duplicate that can take over within minutes to hours; highest cost. Warm site — partially equipped with hardware and connectivity but requires configuration and data restoration; takes hours to days. Cold site — a physical space with power and connectivity but no pre-installed hardware; lowest cost, longest recovery time (days to weeks). SY0-701 tests matching the site type to the stated RTO requirement.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Risk management and business continuity fall under **Domain 5 – Security Program Management and Oversight (20%)** of SY0-701. ALE calculations and BCP/DR terminology questions are consistently present on the exam.
*   **ALE Calculation Trap:** SY0-701 may present a scenario with an asset value, exposure factor, and occurrence rate and ask you to calculate ALE or determine whether a control is cost-effective. Remember: SLE = Asset Value × Exposure Factor; ALE = SLE × ARO. A control is cost-effective if its annual cost is less than the ALE reduction it provides.
*   **RTO vs. RPO Trap:** RTO answers "how long can we be down?" RPO answers "how much data can we lose?" A very low RPO requires frequent backups or continuous replication. A very low RTO requires a hot site or active-active failover. If a question asks which recovery metric defines the backup frequency requirement, the answer is RPO.
*   **Risk Response Selection:** Transference does not eliminate risk — it transfers the financial consequence. Avoidance eliminates the risk entirely by stopping the activity. Mitigation reduces but does not eliminate risk. Acceptance is only appropriate when the cost of mitigation exceeds the risk impact. If a question asks which response best fits a low-value, low-likelihood risk, acceptance is usually correct.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include ALE calculation walkthroughs, BCP/DR tier comparison tables, and risk response scenario examples that map directly to SY0-701 exam questions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Risk Management" and "Business Continuity" sections in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on risk terminology, ALE calculations, and BCP/DR site types matched to RTO/RPO requirements.
*   **Required Video:** Watch the risk management and business continuity video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos include worked ALE examples and disaster recovery site comparison scenarios.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform a sample risk assessment, calculate ALE for two hypothetical threat scenarios, evaluate whether a proposed control is cost-justified, and match disaster recovery site types to stated RTO requirements.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to calculate SLE, ARO, and ALE for any given scenario.
- [ ] Read the "Risk Management" and "Business Continuity" sections in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the risk management video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Memorize: ALE = SLE × ARO; RTO = downtime limit; RPO = data loss limit; Hot site = fastest recovery; Cold site = cheapest but slowest.
- [ ] Proceed to the weekly hands-on lab activity.
