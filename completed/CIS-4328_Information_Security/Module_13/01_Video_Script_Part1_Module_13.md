# Video Script: Module 13 — Risk Management for Security+ (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — Introduction: Why Risk Management Is Central to Security (2 minutes)

Welcome to Module 13, Risk Management. This module ties together everything we have studied in this course. Every security decision we make — every firewall rule, access control policy, encryption standard, and incident response procedure — is ultimately a risk management decision. We are trying to reduce risk to an acceptable level at a justifiable cost.

Risk management is explicitly tested throughout the Security+ exam, not just in a single domain. You will see risk concepts in questions about governance, compliance, vulnerability management, and security architecture. Understanding risk thinking is what separates a security professional who can make defensible decisions from someone who just runs checklists.

For this module we focus on Security+ Domain 5 (Governance, Risk, and Compliance) and related objectives in Domain 2.

---

## Segment 2 — Core Risk Concepts (5 minutes)

Risk management begins with a shared vocabulary. These terms have specific technical meanings that differ from everyday usage.

### The Risk Equation

**Risk = Threat × Vulnerability × Impact**

This is the fundamental formula and the lens through which every risk analysis is performed.

**Threat** is any circumstance or event with the potential to cause harm to a system. Threats are external to the organization and largely outside your control. Examples:

- A nation-state actor targeting your industry
- A ransomware criminal group
- A natural disaster (hurricane, flood)
- A disgruntled insider
- A vendor with access to your systems

You cannot eliminate most threats. You can reduce your exposure to them.

**Vulnerability** is a weakness in a system, process, or control that a threat can exploit. Vulnerabilities are internal to your environment and largely within your control. Examples:

- An unpatched operating system with a known CVE
- A firewall misconfiguration that allows unnecessary inbound traffic
- Weak password policy that permits short passwords
- Lack of MFA on privileged accounts
- An untrained employee susceptible to phishing

You cannot eliminate all vulnerabilities, but reducing vulnerabilities is the primary lever security teams control.

**Impact** is the magnitude of harm that would result if a threat successfully exploits a vulnerability. Impact is measured in terms of:

- **Confidentiality impact** — unauthorized disclosure of sensitive data
- **Integrity impact** — unauthorized modification of data or systems
- **Availability impact** — disruption of system or service availability
- **Financial impact** — direct costs (breach notification, forensics, remediation) and indirect costs (regulatory fines, litigation, reputational damage, lost business)

When threat is high, vulnerability is high, and impact is high — risk is high. Reducing any one of these three factors reduces overall risk.

### Key Risk Concepts

**Asset** — anything of value to the organization: hardware, software, data, intellectual property, reputation, personnel. Risk management begins with identifying and valuing assets.

**Risk Appetite** — the amount of risk an organization is willing to accept in pursuit of its objectives. An organization with low risk appetite (a nuclear power plant) accepts very little risk and invests heavily in controls. An organization with high risk appetite (a startup) accepts more risk to move faster. Risk appetite is a business decision made by executive leadership, not by the security team.

**Risk Tolerance** — the specific acceptable variation around the risk appetite. If the risk appetite is "low financial exposure from security incidents," the risk tolerance might be "no single incident will cost more than $500,000."

**Risk Threshold** — the point at which risk becomes unacceptable and requires mandatory treatment. Risks above the threshold must be addressed. Risks below the threshold are acceptable.

**Residual Risk** — the risk that remains after security controls have been applied. No control eliminates risk entirely. The goal is to reduce risk to a level within the organization's risk tolerance.

**Inherent Risk** — the risk that exists in the absence of any controls. Inherent risk is the baseline before you do anything about it.

### Risk Likelihood vs. Probability

**Likelihood** — a qualitative assessment of how often a threat event might occur. Typically rated: Low / Medium / High or using a numeric scale.

**Probability** — a quantitative expression of likelihood as a number between 0 and 1, or as a frequency (e.g., once every five years = annual probability of 0.2 = 20%).

In qualitative risk analysis, likelihood is a category. In quantitative analysis, likelihood is expressed numerically. We will cover this distinction in detail in the next segment.

---

## Segment 3 — Risk Response Strategies (4 minutes)

Once risks are identified and assessed, you must decide what to do about each one. There are four risk response strategies. Security+ tests all four, and you must know them by their correct names.

### Risk Avoidance

Risk avoidance means eliminating the activity or condition that creates the risk. You avoid the risk by not doing the thing that creates it.

Example: An organization evaluates launching a mobile banking application. The security team assesses the risk as too high given current development capabilities and the regulatory environment. The organization decides NOT to launch the mobile app — avoiding the risk entirely.

Avoidance is appropriate when the risk is unacceptably high and no other strategy reduces it to an acceptable level. It is not always practical — an organization cannot avoid all risk and still conduct business.

### Risk Transference (Risk Transfer)

Risk transference means shifting the financial impact of a risk to another party. The risk itself does not go away — the liability for its financial consequences moves.

The most common form of risk transference in security is **cyber insurance**. An organization purchases a policy that reimburses costs associated with a breach (forensic investigation, breach notification, legal defense, regulatory fines in some cases, business interruption losses). The insurer assumes the financial risk.

Third-party contracts are another transference mechanism: service level agreements (SLAs) with vendors that include financial penalties for security failures transfer some risk back to the vendor.

**Limitation:** Cyber insurance does not transfer the reputational damage, regulatory scrutiny, or customer loss that follows a breach. It only addresses financial impact.

### Risk Mitigation

Risk mitigation means implementing controls to reduce the likelihood, the vulnerability, or the impact of a risk. This is the most common risk response in security.

Examples:

- Patching a vulnerability — reduces vulnerability (makes it harder to exploit)
- Implementing MFA — reduces likelihood of credential-based attack succeeding
- Encrypting data at rest — reduces impact (exfiltrated encrypted data is less valuable)
- Network segmentation — limits lateral movement (reduces impact of initial compromise)

Mitigation does not eliminate risk — it reduces it to a level within the risk tolerance. The residual risk after mitigation must be acceptable.

### Risk Acceptance

Risk acceptance means acknowledging a risk and deliberately choosing not to address it further. This is appropriate when:

- The cost of mitigation exceeds the expected cost of the risk occurring
- The risk is below the organization's risk threshold
- The organization has limited resources and the risk does not merit priority treatment

**Documented risk acceptance** is critical. A risk that is not mitigated must have explicit documentation that it was reviewed, assessed, and consciously accepted — not just forgotten. This documentation protects the organization and individuals from liability.

Risk acceptance is NOT the same as ignoring risk. If leadership accepts a risk, they must understand what they are accepting and sign off on it formally.

### A Fifth Response: Risk Exemption vs. Acknowledgment

Some frameworks distinguish between formal acceptance (leadership reviewed and consciously accepted) and exemption (a specific exception to a security policy is granted for a defined period with specific conditions and an expiration date). Security+ primarily tests the four core strategies.

---

## Segment 4 — Quantitative vs. Qualitative Risk Analysis (4 minutes)

There are two broad approaches to risk analysis: quantitative and qualitative. Both are valid. The choice depends on the availability of data, the audience, and the purpose of the analysis.

### Quantitative Risk Analysis

Quantitative analysis expresses risk in financial terms. It requires numerical inputs and produces a dollar-value output — making risk directly comparable to security investment costs.

**Key quantitative terms:**

**AV (Asset Value)** — the monetary value of the asset being protected. A database containing 1 million customer credit card records has a different AV than a laptop.

**EF (Exposure Factor)** — the percentage of asset value lost if a specific threat occurs. If the threat is ransomware and it would encrypt 60% of your data, EF = 0.60.

**SLE (Single Loss Expectancy)** = AV × EF

This is the expected financial loss from a single occurrence of the threat. Example: AV = $1,000,000, EF = 0.60, therefore SLE = $600,000.

**ARO (Annual Rate of Occurrence)** — how often you expect the threat to occur per year. If ransomware attacks happen once every two years, ARO = 0.5.

**ALE (Annual Loss Expectancy)** = SLE × ARO

This is the expected annual financial loss from this threat. Example: SLE = $600,000, ARO = 0.5, therefore ALE = $300,000.

**Cost-Benefit Analysis for Security Controls:**

If a security control costs $50,000 per year and reduces the ALE from $300,000 to $100,000, the control saves $200,000/year — a clear positive return on investment. If the control costs $350,000/year, it costs more than the risk it mitigates and the economics favor acceptance.

**Value of the Safeguard** = ALE before control − ALE after control − Annual cost of control

**Limitations of quantitative analysis:**

- Requires reliable historical data on occurrence rates and loss values — often difficult to obtain
- The false precision of exact numbers can provide unwarranted confidence
- Takes significant time and resources to perform rigorously

### Qualitative Risk Analysis

Qualitative analysis uses descriptive scales rather than financial numbers. It is faster, requires less data, and is more accessible to non-financial stakeholders.

**Risk Matrix** — the primary tool of qualitative analysis. A matrix plots likelihood (Low/Medium/High) against impact (Low/Medium/High) to produce a risk rating:

| | Low Impact | Medium Impact | High Impact |
|---|---|---|---|
| High Likelihood | Medium | High | Critical |
| Medium Likelihood | Low | Medium | High |
| Low Likelihood | Low | Low | Medium |

Risks in the Critical and High zones require priority treatment. Risks in the Low zone may be accepted.

**Limitations of qualitative analysis:**

- Subjective — different analysts may rate the same risk differently
- Cannot directly compare risk cost to control cost
- May mask differences between risks in the same category (two "High" risks may differ enormously in actual dollar impact)

### Using Both Together

In practice, mature organizations use qualitative analysis for initial risk screening (to identify which risks deserve deeper attention) and quantitative analysis for high-priority risks where the investment in rigorous analysis is justified.

---

## Module 13 Part 1 Summary

The foundation of risk management:

- Risk = Threat × Vulnerability × Impact — understanding which factor to reduce is the key to efficient security investment
- Risk appetite, tolerance, threshold, inherent risk, and residual risk are distinct concepts with specific meanings
- Four risk response strategies: avoidance (don't do the risky thing), transference (cyber insurance, contracts), mitigation (apply controls), acceptance (document and consciously accept)
- Quantitative analysis: AV → EF → SLE → ARO → ALE → cost-benefit analysis of controls
- Qualitative analysis: risk matrix mapping likelihood vs. impact to risk rating
- Both approaches have strengths and limitations; mature programs combine them

In Part 2 we cover the risk register, Business Impact Analysis (BIA), and security controls classification. See you there.

---

*End of Part 1 Script*
