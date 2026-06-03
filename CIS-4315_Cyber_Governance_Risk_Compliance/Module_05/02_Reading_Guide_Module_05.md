# Reading Guide: Module 05 — Risk Treatment and Control Selection

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

---

## Introduction

Module 05 completes the three-module arc of information risk management. Modules 03 and 04 addressed how to identify, organize, and measure risk. This module addresses what to do about it. Risk treatment is where analysis becomes decision — and where security professionals demonstrate business judgment by selecting responses that are proportionate, cost-effective, and aligned with organizational objectives.

The four risk treatment options (avoid, transfer, mitigate, accept) and control categories (preventive, detective, corrective, deterrent; administrative, technical, physical) are among the most heavily tested topics on the CISM exam.

---

## Section 1 — Risk Treatment Options Overview

After a risk has been identified and assessed, the organization must make an explicit treatment decision. ISACA CISM and virtually all major risk management frameworks recognize four primary treatment options.

The key principle underlying all four options is proportionality: the treatment should be proportionate to the level of risk and the cost of treatment. Over-investing in low-risk areas wastes resources that could protect against higher-priority threats. Under-investing in high-risk areas leaves the organization dangerously exposed.

A second key principle is formality: every risk treatment decision — including the decision to accept a risk — must be explicitly documented, assigned to an accountable owner, and approved by an appropriate decision-maker.

---

## Section 2 — Risk Avoidance

### 2.1 Definition

Risk avoidance eliminates a risk entirely by discontinuing or not initiating the activity that creates the risk. The organization removes itself from the risk scenario rather than attempting to manage it.

### 2.2 When to Use

Avoidance is appropriate when:

- The risk level is unacceptably high and cannot be reduced to an acceptable level through feasible controls
- The potential benefit of the risky activity does not justify the exposure
- Legal, regulatory, or ethical concerns make the activity inadvisable regardless of controls

### 2.3 Examples

An organization decides not to store payment card data at all — eliminating PCI DSS scope by using a third-party tokenization service. This avoids the risk of a cardholder data breach entirely.

A company evaluating a new mobile application decides not to collect user geolocation data after threat modeling reveals disproportionate privacy risk. The feature is eliminated from the product.

### 2.4 Limitations

Avoidance always has a cost: the opportunity cost of not pursuing the activity. Organizations that avoid all digital risk also forgo digital opportunity. Avoidance is rarely a complete enterprise strategy — it is a tactical option for specific high-risk activities.

> Exam Tip: Avoidance eliminates the risk by eliminating the activity. It is not the same as ignoring risk. On the CISM exam, a question about a company that "stops collecting" certain data or "discontinues" a risky service is describing avoidance.

---

## Section 3 — Risk Transfer

### 3.1 Definition

Risk transfer shifts the financial consequences of a risk to a third party while leaving operational risk management within the organization. The organization still experiences the risk event — but a third party bears some or all of the financial burden.

### 3.2 Transfer Mechanisms

The two primary transfer mechanisms are insurance and contracts.

**Insurance:** Cyber liability insurance, errors and omissions (E&O) insurance, business interruption insurance, and directors and officers (D&O) insurance all transfer specific categories of financial loss to insurers. Coverage typically includes breach notification costs, forensic investigation, legal fees, regulatory fines, and business interruption losses.

**Contracts:** Service level agreements, vendor contracts, and outsourcing agreements can include indemnification clauses, liability caps, and hold harmless provisions that transfer financial risk to vendors or service providers.

### 3.3 What Transfer Does Not Cover

Risk transfer is frequently misunderstood. Insurance and contracts transfer financial impact — they do not transfer:

- Operational disruption (systems are still down while a claim is processed)
- Reputational damage (customers and media do not care that the vendor is liable)
- Regulatory scrutiny (regulators hold the organization accountable regardless of contract terms)
- Loss of customer trust

### 3.4 Transfer as a Complement to Mitigation

Risk transfer is most effective when used as a complement to mitigation, not as a substitute for it. Organizations implement controls to reduce risk to an acceptable level, then use insurance to cover the residual financial exposure that remains. Relying on insurance instead of controls typically results in both inadequate coverage (insurers exclude claims from negligent security practices) and continued operational exposure.

> Exam Tip: CISM exam questions distinguishing transfer from avoidance typically focus on this key difference: avoidance eliminates the activity; transfer keeps the activity but shifts financial consequences. Both leave the organization with some level of operational risk.

---

## Section 4 — Risk Mitigation

### 4.1 Definition

Risk mitigation reduces the likelihood that a risk event will occur, the impact if it does occur, or both. It is accomplished through the implementation of security controls — safeguards and countermeasures applied to the threat, vulnerability, or potential impact.

### 4.2 Mitigation Targets

Controls can target different points in the risk equation.

Reducing likelihood: Multi-factor authentication reduces the likelihood that stolen credentials enable unauthorized access. Security awareness training reduces the likelihood of phishing success. Patch management reduces the likelihood that known vulnerabilities are exploited.

Reducing impact: Data backup and recovery capabilities reduce the impact of ransomware or data loss events. Segmented network architecture limits the blast radius of a breach. Incident response plans reduce the impact of any security incident by enabling faster, more effective response.

### 4.3 Residual Risk

Mitigation never reduces risk to zero. After implementing controls, residual risk — the risk that remains after treatment — always exists. The goal is to reduce risk to within the organization's defined risk appetite and tolerance, not to eliminate it.

Residual risk must be formally documented, communicated to decision-makers, and explicitly accepted.

### 4.4 Layers of Defense

Effective mitigation uses a defense-in-depth strategy — multiple layers of controls, each compensating for the limitations of others. If a preventive control fails (an attacker bypasses the firewall), detective controls provide the next layer of protection (SIEM alerts on anomalous traffic). If detection is delayed, corrective controls minimize impact (automated system isolation). No single control is a complete solution.

---

## Section 5 — Risk Acceptance

### 5.1 Definition

Risk acceptance is the deliberate decision to tolerate a known risk without implementing additional controls. Acceptance acknowledges that the risk exists and that the organization will bear the consequences if the risk materializes.

### 5.2 When to Use

Acceptance is appropriate when:

- The risk level falls within the organization's defined risk appetite
- The cost of available treatment options exceeds the benefit of reducing the risk
- No effective treatment option is feasible given current technology or budget constraints
- The risk is low-probability and low-impact relative to organizational priorities

### 5.3 Formal vs. Informal Acceptance

The distinction between formal acceptance and informal acceptance is one of the most important governance concepts in this module — and it is directly tested on the CISM exam.

**Formal acceptance:** The risk has been identified and assessed. The analysis and residual risk level have been documented. An accountable decision-maker (with appropriate authority) has reviewed the documentation and explicitly decided to accept the risk. The acceptance decision, rationale, and owner are recorded in the risk register.

**Informal acceptance (negligence):** The risk exists but has never been formally identified, assessed, or decided upon. No one has made a deliberate decision — the organization simply never addressed it.

Informal acceptance is not a risk treatment strategy. It is a governance failure. The CISM exam consistently tests this distinction.

### 5.4 Risk Acceptance Authority

Risk acceptance authority should be commensurate with the level of risk being accepted. Low-risk acceptances may be within the authority of a department manager. High-risk acceptances may require the CISO, CRO, or board-level approval. Acceptance authority levels should be defined in the organization's risk management policy.

---

## Section 6 — Control Categories

### 6.1 Functional Types

Controls are classified by the security function they perform.

| Control Type | Function | Examples |
|---|---|---|
| Preventive | Stops a risk event from occurring | Firewall, MFA, access controls, encryption, security training |
| Detective | Identifies that a risk event has occurred | SIEM, IDS, audit logs, anomaly detection, security cameras |
| Corrective | Restores normal operations after an event | Backup/recovery, patch management, incident response |
| Deterrent | Discourages harmful actions through perceived consequence | Warning banners, visible cameras, published policy, security guards |

A fifth category — compensating controls — appears in some frameworks (including PCI DSS). A compensating control is an alternative control that provides equivalent protection when the standard control cannot be implemented.

### 6.2 Implementation Methods

Controls are also categorized by how they are implemented.

**Administrative controls** govern human behavior through policy, procedure, and process. Examples: security policies, acceptable use policies, security awareness training, background checks, separation of duties, change management procedures.

**Technical controls** use technology to enforce security requirements. Examples: encryption, firewalls, intrusion detection systems, digital certificates, access control lists, data loss prevention tools.

**Physical controls** protect the physical environment. Examples: locked server rooms, badge readers, biometric access systems, security guards, cable locks, environmental sensors (smoke, temperature, flood).

### 6.3 Control Mapping Example

A single risk — unauthorized access to a server room — can be addressed by controls across all three implementation categories simultaneously.

Administrative: Access authorization policy requiring manager approval for all server room access.

Technical: Electronic badge reader logging every entry and exit, integrated with the SIEM.

Physical: Steel door, biometric lock, security camera with 90-day retention.

The combination is more robust than any single control, and the detective (camera, badge log) and preventive (steel door, biometric lock) controls complement each other.

---

## Section 7 — Cost-Benefit Analysis for Control Selection

### 7.1 The Investment Decision Framework

Control selection requires answering a business question: is the cost of this control justified by the risk reduction it provides? The ALE-based framework from Module 04 provides the quantitative foundation for this decision.

The calculation:

- Calculate current ALE (before control)
- Calculate projected ALE after control is implemented
- Calculate annual cost of control (acquisition, implementation, licensing, maintenance, staffing)
- Net benefit = (Current ALE - Projected ALE) - Annual Control Cost

If net benefit is positive: the control is cost-justified.

If net benefit is negative: the control costs more than it saves and requires additional business justification (regulatory mandate, risk tolerance policy, board directive).

### 7.2 Worked Example

Current situation: Web application with ALE of $350,000 for SQL injection risk.

Proposed control: Web application firewall (WAF) at $40,000 per year. WAF would reduce the ALE to $70,000.

Net benefit = ($350,000 - $70,000) - $40,000 = $280,000 - $40,000 = $240,000 per year.

The WAF produces a net benefit of $240,000 annually — clearly cost-justified.

### 7.3 Qualitative Factors in Control Selection

The ALE formula does not capture all relevant considerations.

Mandatory controls: Regulatory requirements (PCI DSS, HIPAA, SOX) may require controls regardless of cost-benefit. Non-compliance costs — fines, penalties, loss of operating license — may not be fully captured in the ALE calculation.

Risk tolerance: Some organizations will invest in controls whose cost exceeds ALE reduction because the potential impact of the residual risk is simply unacceptable, regardless of the math.

Operational trade-offs: Controls that significantly degrade productivity, user experience, or system performance carry hidden costs that the ALE formula does not account for.

Control synergies: A control that addresses multiple risks simultaneously may be undervalued if only one risk's ALE is used in the calculation.

### 7.4 Documenting Control Decisions

Every significant control selection decision should be documented in the risk register or a dedicated control decision record including: the risk being addressed, the treatment option selected, the controls chosen, the cost-benefit analysis, the residual risk after implementation, and the accountable owner.

---

## Section 8 — Residual Risk and Risk Acceptance

After all selected controls are implemented, residual risk remains. The final step in the risk treatment process is formal disposition of residual risk.

This disposition takes one of two forms: the residual risk level is within the organization's risk appetite, and it is formally accepted; or the residual risk level exceeds the appetite, and the organization must identify additional treatment options or formally document a policy exception approved by appropriate authority.

Residual risk should never be silently left unaddressed. Every assessed risk must have a documented treatment decision and, ultimately, a documented acceptance of the remaining exposure.

---

## Section 9 — Risk Treatment Summary Table

| Treatment Option | Risk Eliminated? | Activity Continues? | Financial Impact Transferred? | Best Used When |
|---|---|---|---|---|
| Avoid | Yes | No | N/A | Risk too high; activity not worth it |
| Transfer | No | Yes | Yes (partially) | Residual financial exposure after mitigation |
| Mitigate | Reduced | Yes | No | Cost-effective controls available |
| Accept | No | Yes | No | Risk within appetite; treatment disproportionate |

---

## Section 10 — Glossary

**Compensating control:** An alternative control providing equivalent protection when the standard control cannot be implemented.

**Control:** A safeguard or countermeasure that reduces the likelihood or impact of a risk.

**Defense in depth:** A security strategy using multiple overlapping layers of controls so that the failure of any single control does not leave the organization unprotected.

**Deterrent control:** A control that discourages harmful actions through perceived consequences.

**Formal risk acceptance:** A documented, authorized decision to tolerate a known risk without additional treatment.

**Residual risk:** The risk that remains after controls have been implemented and risk treatment actions completed.

**Risk appetite:** The amount and type of risk an organization is willing to accept in pursuit of its objectives.

**Risk tolerance:** The acceptable variation around the risk appetite level — the boundaries within which risk levels are managed.

**Risk transfer:** A treatment option that shifts the financial consequences of a risk to a third party through insurance or contract.

**Risk treatment:** The process of selecting and implementing options to modify risk — including avoidance, transfer, mitigation, and acceptance.

---

## Required Reading

- NIST SP 800-53 Rev. 5 — Introduction and control family overviews. Provides the authoritative catalog of security controls used in NIST RMF. Free at csrc.nist.gov.
- NIST SP 800-39 — Managing Information Security Risk: Organization, Mission, and Information System View. Chapter 3 covers the risk response step. Free at csrc.nist.gov.
- ISO 31000:2018 — Section 6.5 (Risk Treatment). Available through university library database access.

---

## Study Checklist

- [ ] List the four risk treatment options and state one scenario where each is appropriate
- [ ] Distinguish formal risk acceptance from informal risk acceptance
- [ ] Name the four functional control types and give one example of each
- [ ] Name the three control implementation categories and give one example of each
- [ ] Work through a cost-benefit analysis calculation: given ALE before and after, and annual control cost, determine net benefit
- [ ] Define residual risk and explain who must formally accept it
- [ ] Proceed to the Module 05 Lab Activity
