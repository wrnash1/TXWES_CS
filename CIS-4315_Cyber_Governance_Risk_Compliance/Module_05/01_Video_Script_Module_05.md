# Video Script: Module 05 — Risk Treatment and Control Selection

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 21–23 minutes

## CISM Domain Alignment: Domain 2 — Information Risk Management

---

## Production Notes

- Slides: 19 slides total
- Recording environment: lecture capture with slide overlay
- Use decision tree diagrams for risk treatment options; highlight cost-benefit formula

---

## Opening Segment (2 minutes)

[SHOW SLIDE 1 — Title: Risk Treatment and Control Selection]

Welcome back, everyone. I'm Professor Nash, and this is Module 5 of CIS-4315.

Over the last two modules, we built a solid foundation. In Module 3, we learned the frameworks that organize risk management programs. In Module 4, we learned the analytical techniques that measure risk — qualitative ratings, ALE calculations, Business Impact Analysis, and threat modeling.

[PAUSE — 2 seconds]

Now comes the moment where analysis turns into action. You have identified your risks. You have assessed their likelihood and impact. Now the most important question: what are you going to do about them?

[SHOW SLIDE 2 — The Risk Treatment Decision]

This is where many students — and even some practitioners — get tripped up. They assume the answer is always the same: implement a control, reduce the risk, done. But that is not how real risk management works. Organizations have limited budgets, limited staff, and unlimited risks competing for attention. Every risk treatment decision is a business decision, and it requires judgment.

By the end of this module, you will be able to describe the four risk treatment options — avoid, transfer, mitigate, and accept — and explain when each is appropriate. You will be able to categorize security controls as preventive, detective, corrective, or deterrent. You will understand how to conduct a cost-benefit analysis for control selection. And you will understand the concept of residual risk and why it always remains.

[PAUSE — 2 seconds]

Let's get started.

---

## Part 1 — The Four Risk Treatment Options (7 minutes)

[SHOW SLIDE 3 — Risk Treatment Overview]

Once an organization has assessed a risk, it must choose one of four treatment options. These four options are: Avoid, Transfer, Mitigate, and Accept. Every risk treatment decision falls into one of these categories, and on the CISM exam you will see scenario questions testing your ability to identify which option is most appropriate for a given situation.

[PAUSE — 2 seconds]

[SHOW SLIDE 4 — Risk Avoidance]

The first option is Risk Avoidance. Avoidance means eliminating the risk entirely by not engaging in the activity or condition that creates it. If a company is considering offering a new online service and the risk assessment reveals unacceptable exposure, the company might decide not to offer that service at all. The risk is avoided because the risky activity no longer occurs.

Avoidance is the most complete form of risk treatment — by eliminating the activity, you eliminate the associated risk. But it comes at a cost: the organization also loses any benefit the risky activity would have provided. A company that avoids all digital transformation to eliminate cyber risk also avoids all the competitive advantages of digital services.

[PAUSE — 2 seconds]

Avoidance is most appropriate when the risk is extremely high and cannot be reduced to an acceptable level through any feasible control, or when the potential benefit of the activity does not justify the risk exposure.

For the CISM exam, remember: avoidance is not the same as ignoring risk. Avoidance is a deliberate, active decision not to pursue an activity. Ignoring risk is negligence.

[SHOW SLIDE 5 — Risk Transfer]

The second option is Risk Transfer. Transfer means shifting the financial consequences of a risk to a third party. The most common mechanism is insurance — cyber liability insurance, errors and omissions insurance, or business interruption insurance. Contracts can also transfer risk: a vendor contract that holds the vendor financially liable for a data breach caused by their systems transfers risk from your organization to the vendor.

[PAUSE — 2 seconds]

It is critically important to understand what risk transfer does and does not do. Risk transfer shifts the financial impact — it does not eliminate the threat or reduce the likelihood of the risk event occurring. If your organization experiences a ransomware attack and has cyber insurance, the insurance may pay for the recovery and ransom. But the attack still happened. Your systems were still disrupted. Your reputation may still be damaged.

For this reason, transfer is most appropriate as a complement to mitigation — not as a replacement for it. You transfer the residual financial risk that remains after you have implemented controls.

For the CISM exam, a key distinction: insurance transfers risk, but operational impact — system downtime, reputational damage, regulatory scrutiny — cannot be transferred.

[SHOW SLIDE 6 — Risk Mitigation]

The third option is Risk Mitigation. Mitigation means reducing the likelihood or impact of a risk through the implementation of security controls. This is the most common risk treatment option in information security practice. Controls can reduce likelihood — preventing the risk event from occurring — or reduce impact — limiting the damage when the risk event does occur.

[PAUSE — 2 seconds]

For example, implementing multi-factor authentication reduces the likelihood that stolen credentials will lead to unauthorized access. Implementing a data backup strategy does not reduce the likelihood of ransomware, but it significantly reduces the impact by enabling recovery without paying ransom.

Mitigation does not eliminate risk entirely. Even with the best controls, some residual risk always remains. The goal of mitigation is to reduce risk to a level within the organization's risk appetite — not to achieve zero risk, which is impossible.

[SHOW SLIDE 7 — Risk Acceptance]

The fourth option is Risk Acceptance. Acceptance means acknowledging that a risk exists and deciding to tolerate it without additional controls. Acceptance is appropriate when the cost of treating the risk exceeds the benefit of treatment, when the risk level is already within the organization's defined risk appetite, or when no effective treatment option is available.

[PAUSE — 2 seconds]

Here is an important distinction the CISM exam tests repeatedly: acceptance must be formal and documented. It is not acceptable to simply ignore a risk and never make a decision. A formal risk acceptance means: the risk has been identified, it has been assessed, a decision-maker with appropriate authority has reviewed the analysis, and the organization has explicitly decided to accept the risk with full awareness of its potential consequences.

Informal acceptance — where risks are never reviewed or decided upon — is a governance failure, not a risk treatment strategy.

[PAUSE — 2 seconds]

[SHOW SLIDE 8 — Risk Treatment Decision Framework]

Here is a decision framework that combines all four options. Ask: can the risk be eliminated by stopping the activity? If yes and if the benefit is not worth the risk, then avoid. Ask: is the risk within our risk appetite already, or is the cost of treatment disproportionate to the benefit? If yes, then formally accept. Ask: is there a cost-effective control that can reduce the risk to an acceptable level? If yes, then mitigate. Ask: does residual financial exposure remain after mitigation? If yes, then transfer the financial exposure through insurance or contract.

In most real-world situations, organizations use a combination — mitigate to reduce the risk, then transfer some residual financial exposure through insurance, and formally accept whatever residual risk remains.

[PAUSE — 3 seconds]

---

## Part 2 — Control Categories (5 minutes)

[SHOW SLIDE 9 — Control Category Overview]

Once an organization decides to mitigate a risk, it must select appropriate controls. Controls are the specific safeguards or countermeasures that reduce risk. Understanding control categories helps security professionals design comprehensive, layered defense strategies.

Controls can be categorized in two dimensions: by their functional type and by their implementation method.

[SHOW SLIDE 10 — Functional Control Types]

By functional type, controls fall into four categories.

**Preventive controls** stop a risk event from occurring in the first place. Examples include firewalls, access controls, multi-factor authentication, and security awareness training. The goal of a preventive control is to keep the threat from succeeding.

**Detective controls** identify that a risk event has occurred or is occurring. Examples include intrusion detection systems, security information and event management (SIEM) platforms, audit logging, and anomaly detection. Detective controls do not stop an attack — they alert the organization that something is happening.

[PAUSE — 2 seconds]

**Corrective controls** restore systems and operations to a normal state following an incident. Examples include backup and recovery systems, incident response procedures, and patch management. Corrective controls reduce the impact of a risk event that has already occurred.

**Deterrent controls** discourage potential attackers or policy violators from attempting a harmful action. Examples include security warning banners, visible CCTV cameras, and published acceptable use policies. Deterrents work by influencing behavior rather than technically preventing or detecting actions.

[SHOW SLIDE 11 — Implementation Method Categories]

By implementation method, controls are categorized as administrative, technical, or physical.

**Administrative controls** are policy and process-based safeguards. Security policies, acceptable use policies, security awareness training, background checks, and incident response plans are all administrative controls. They govern human behavior.

**Technical controls** are technology-based safeguards. Encryption, firewalls, antivirus software, access control lists, and digital signatures are technical controls. They are implemented in hardware or software.

**Physical controls** are environmental and physical safeguards. Locked doors, security guards, badge readers, biometric access systems, and cable locks are physical controls. They protect the physical environment where information systems reside.

[PAUSE — 2 seconds]

[SHOW SLIDE 12 — Defense in Depth]

These categories work together in a defense-in-depth strategy. No single control is perfect. An attacker who defeats a preventive control (bypasses a firewall) will then encounter a detective control (SIEM alerts on unusual traffic) and a corrective control (incident response team isolates the affected system). A comprehensive security program includes controls from all functional types and all implementation methods, creating multiple overlapping layers of protection.

[PAUSE — 3 seconds]

---

## Part 3 — Cost-Benefit Analysis for Control Selection (5 minutes)

[SHOW SLIDE 13 — The Control Selection Challenge]

Selecting which controls to implement is a business decision, not just a technical one. Organizations cannot implement every possible control — budget and staff are finite. The question is always: which controls provide the most risk reduction per dollar spent?

[PAUSE — 2 seconds]

In Module 4, we introduced the ALE-based control justification formula. Let me build on that here and extend it to a full cost-benefit analysis framework for control selection.

[SHOW SLIDE 14 — Cost-Benefit Analysis Framework]

The basic structure of a control cost-benefit analysis has four inputs.

First, the current Annualized Loss Expectancy — the expected annual financial loss before the control is implemented.

Second, the projected ALE after the control is implemented — reflecting the reduced likelihood or impact that the control provides.

Third, the annual cost of the control — including acquisition, implementation, licensing, maintenance, and staffing.

Fourth, the benefit of the control — calculated as the reduction in ALE minus the annual cost of the control.

If the benefit is positive — meaning the ALE reduction exceeds the annual control cost — the investment is financially justified. If the benefit is negative, the control costs more than it saves and requires additional justification.

[PAUSE — 2 seconds]

[SHOW SLIDE 15 — Beyond the Formula]

However, the ALE formula is not the only consideration in control selection. Several qualitative factors must also be evaluated.

Regulatory requirements may mandate certain controls regardless of their cost-benefit ratio. A healthcare organization must implement HIPAA-required controls even if the cost exceeds the calculated ALE reduction. Compliance is non-negotiable.

Risk appetite and tolerance set boundaries. An organization with a very low risk tolerance may accept negative-return controls for high-consequence risks because the board is unwilling to accept the residual exposure regardless of the math.

Operational impact matters. A control that is technically effective but severely degrades user productivity may cost more in lost efficiency than it saves in risk reduction — a cost the ALE formula does not capture.

Control coverage is also relevant. A single control that partially addresses multiple risks may be more valuable than its single-risk ALE calculation suggests.

[PAUSE — 2 seconds]

[SHOW SLIDE 16 — Residual Risk]

After implementing all selected controls, some risk always remains. This remaining exposure is called residual risk. Residual risk cannot be eliminated — it can only be reduced to a level within the organization's defined risk appetite.

The formal disposition of residual risk is the authorization or acceptance decision. In NIST RMF terms, this is the ATO decision. In ISO 31000 terms, this is documented risk acceptance. In all cases, a senior decision-maker must formally review and acknowledge the residual risk.

Residual risk must be communicated clearly to decision-makers. A risk register entry should not just document what controls were implemented — it should document what risk remains after those controls are in place, and confirm that the remaining risk has been formally accepted by an accountable owner.

[PAUSE — 3 seconds]

---

## Summary and Closing (2 minutes)

[SHOW SLIDE 17 — Module 05 Integration]

Let me bring the last three modules together before we close.

Module 3 gave us the frameworks — the organized processes for managing risk at the enterprise and system level.

Module 4 gave us the analytical techniques — how to measure risk, calculate financial exposure, assess business impact, and model threats.

Module 5 completes the picture — once we know what our risks are and how serious they are, we choose how to treat them: avoid, transfer, mitigate, or accept. We select controls based on their functional type and implementation method. We evaluate their cost-benefit. And we formally document the residual risk that remains.

[SHOW SLIDE 18 — CISM Exam Focus Areas]

For your CISM exam preparation, the following topics from Module 5 are most heavily tested.

Know the four risk treatment options and the criteria for choosing each one. Know that acceptance must be formal and documented — this is tested frequently.

Know the four functional control types: preventive, detective, corrective, deterrent.

Know the three implementation categories: administrative, technical, physical.

Know the cost-benefit analysis formula and the principle that a control is cost-justified if annual control cost is less than the ALE reduction.

Know that residual risk always remains and must be formally accepted by an accountable decision-maker.

[SHOW SLIDE 19 — Looking Ahead]

In Module 6, we begin the Information Security Program domain. We will move from individual risk decisions to building the organizational structures, policies, and programs that make risk management systematic and sustainable at scale.

[PAUSE — 2 seconds]

Your lab this week is one of the most practically relevant in the course — you will conduct a full risk treatment analysis for a real-world scenario, selecting treatment options and controls for a set of assessed risks. I think you will find the synthesis satisfying after the analytical groundwork of the last two modules.

I will see you in Module 6. Keep up the great work.

---

*End of Module 05 Video Script*

*Total estimated runtime: 22 minutes*
