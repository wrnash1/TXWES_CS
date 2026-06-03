# Video Script: Module 11 — Risk Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Production Notes

- Slides: Risk register table shown as animated build; probability-impact matrix shown as color-coded grid
- Graphics: Risk response strategy decision tree; risk lifecycle diagram
- Tone: Practical and scenario-driven — connect every concept to a real IT project context
- Screen segment: Walk through a partial risk register live in a spreadsheet

---

## Segment 1 — Introduction: Why Risk Management Fails (0:00–2:30)

[SHOW SLIDE: Title — "Module 11: Risk Management"]

Welcome back to CIS-3310. I'm Professor Nash. Module 11 is Risk Management — and I want to start with a statistic that should get your attention.

[PAUSE — 2 seconds]

The Standish Group's Chaos Report consistently shows that over 60% of IT projects experience significant budget overruns, schedule slippage, or scope failures. The number one root cause cited by project managers is not technical complexity. It is poor risk management — specifically, risks that were either never identified, never analyzed, or identified but never acted upon.

[SHOW SLIDE: "Risk Management Is Not About Pessimism"]

Risk management is not about being negative or assuming the worst. It is about being honest about uncertainty. Every project has uncertainty. Risk management is the structured process of turning that uncertainty into something you can see, measure, and respond to. A project manager who never talks about risks is not optimistic — they are uninformed.

[PAUSE — 2 seconds]

There is one more thing I want you to understand before we dive in. In project management, "risk" includes both threats — negative events that could harm the project — and opportunities — positive events that could benefit the project. Both require a management response. The Project+ exam will test both.

[SHOW SLIDE: "Risk Management Process Overview"]

The risk management process in PMI's framework has six steps: Plan Risk Management, Identify Risks, Perform Qualitative Risk Analysis, Perform Quantitative Risk Analysis, Plan Risk Responses, and Implement and Monitor Risk Responses. Today we will work through all six.

---

## Segment 2 — Identifying Risks (2:30–6:30)

[SHOW SLIDE: "Step 1 — Plan Risk Management"]

Before you can manage risk, you need a plan for how you will manage risk. The Risk Management Plan documents the methodology, roles and responsibilities, budget for risk activities, timing of risk reviews, risk categories, probability and impact scales, and risk tolerance levels. The Risk Management Plan is a subsidiary plan within the overall Project Management Plan.

[PAUSE — 2 seconds]

One of the most important outputs of this step is the risk breakdown structure, or RBS — a hierarchical categorization of risk sources. For an IT project, typical top-level RBS categories might include technical risks, organizational risks, external risks, and project management risks.

[SHOW SLIDE: "Step 2 — Risk Identification Techniques"]

Risk identification is the process of finding, recognizing, and documenting potential project risks. The output is the Risk Register. Here are the key techniques you need to know for the Project+ exam.

[PAUSE — 2 seconds]

Brainstorming is the most common technique. The project team and subject matter experts generate a comprehensive list of potential risks in a facilitated session. No risk is dismissed during brainstorming — evaluation comes later.

The Delphi Technique uses anonymous expert opinion. A facilitator gathers risk assessments from experts separately, aggregates the results, and circulates them back to the experts for further refinement. Because responses are anonymous, senior voices do not dominate and groupthink is reduced.

[SHOW SLIDE: "More Identification Techniques"]

Interviews with stakeholders, subject matter experts, and project team members surface risks that brainstorming misses — particularly risks that individuals hold privately.

SWOT Analysis — Strengths, Weaknesses, Opportunities, Threats — expands risk identification by examining both internal factors (team capability, processes, tools) and external factors (market, regulations, dependencies).

Assumption analysis examines the assumptions documented in the project charter and scope statement. Every assumption is a potential risk if it turns out to be wrong.

Checklist analysis uses historical records from similar past projects to identify risks that commonly occur in the project's domain.

[SHOW SLIDE: "The Risk Register — Key Output of Identification"]

The Risk Register is the central risk management document. After identification, it contains at a minimum:

- Risk ID and description
- Risk category (from the RBS)
- Potential cause and potential effect
- Risk owner (person responsible for monitoring and responding)
- Probability and impact ratings (added in analysis)
- Response strategy and specific actions (added in response planning)
- Risk status (open, in progress, closed)

The Risk Register is a living document — it is updated throughout the entire project lifecycle.

---

## Segment 3 — Qualitative Risk Analysis (6:30–10:30)

[SHOW SLIDE: "Step 3 — Qualitative Risk Analysis"]

After you have identified your risks, you analyze them. Qualitative risk analysis is the process of prioritizing risks based on their probability of occurring and the impact they would have if they did occur. This step uses subjective judgment — expert opinion, scales, and scoring — rather than statistical data.

[PAUSE — 2 seconds]

The primary tool is the Probability and Impact Matrix, sometimes called the P-I matrix or heat map. You assign each risk a probability score — typically on a scale like 0.1 (very low) to 0.9 (very high) — and an impact score on the same scale. You then multiply them together to get a risk score, also called a risk priority number.

[SHOW SLIDE: "Probability-Impact Matrix — Color Zones"]

The P-I matrix divides risks into zones based on their combined score.

High probability and high impact risks fall in the red zone — these require immediate attention and active response planning.

Medium probability or medium impact risks fall in the yellow zone — these require monitoring and contingency planning.

Low probability and low impact risks fall in the green zone — these may be accepted with minimal response.

[PAUSE — 3 seconds]

For example, a risk scored at probability 0.7 and impact 0.8 produces a risk score of 0.56 — that is a red zone risk. A risk scored at probability 0.3 and impact 0.2 produces a risk score of 0.06 — that is a green zone risk.

[SHOW SLIDE: "Qualitative Analysis Updates the Risk Register"]

After qualitative analysis, the Risk Register is updated with probability ratings, impact ratings, risk scores, and a priority ranking. High-priority risks get the most attention in response planning.

Two additional qualitative concepts you need for the exam: risk urgency (risks that require a rapid response regardless of their P-I score) and risk proximity (how soon the risk might materialize — near-term risks need faster attention).

---

## Segment 4 — Quantitative Risk Analysis (10:30–13:00)

[SHOW SLIDE: "Step 4 — Quantitative Risk Analysis"]

Quantitative risk analysis applies numerical techniques to estimate the probability and cost or schedule impact of risks more precisely. Not all projects use quantitative analysis — it requires historical data, statistical expertise, and significant effort. It is most common on large, high-stakes projects.

[PAUSE — 2 seconds]

The two techniques you need to know for the Project+ exam are Expected Monetary Value and Monte Carlo simulation.

[SHOW SLIDE: "Expected Monetary Value — EMV"]

Expected Monetary Value, or EMV, calculates the statistical average outcome of a risk event. The formula is `EMV = Probability × Impact`. For threats, the impact is expressed as a negative dollar value. For opportunities, as a positive dollar value.

[PAUSE — 2 seconds]

Example: A risk has a 40% probability of occurring and would cost $50,000 if it does. Its EMV is `0.40 × (-$50,000) = -$20,000`. This means the risk contributes negative $20,000 to the project's expected value. If you summed the EMV of all identified risks, you would get a quantified risk reserve estimate.

[SHOW SLIDE: "Monte Carlo Simulation"]

Monte Carlo simulation runs the project schedule or cost model thousands of times with randomly varied inputs to produce a probability distribution of outcomes. Rather than a single point estimate, it produces a range — for example, "there is an 80% probability the project will complete within $2.3 million."

Monte Carlo is a powerful technique, but it requires specialized software and significant data preparation. For the Project+ exam, understand what it does conceptually — you will not be asked to run a simulation.

---

## Segment 5 — Risk Response Strategies (13:00–18:00)

[SHOW SLIDE: "Step 5 — Plan Risk Responses"]

Risk response planning is where you decide what to do about each risk. There are different response strategy categories for threats and opportunities. The Project+ exam tests these extensively.

[SHOW SLIDE: "Response Strategies for Threats (Negative Risks)"]

There are five response strategies for threats.

Avoid: Change the project plan to eliminate the risk entirely. This might mean removing a risky scope element, changing a supplier, or extending the schedule to avoid a constrained resource window. Avoidance is the most aggressive response — it eliminates the risk but often has cost or scope implications.

[PAUSE — 2 seconds]

Transfer: Shift the financial impact of the risk to a third party. Insurance is the classic example. Fixed-price contracts transfer cost risk to the vendor. Transferring a risk does not make it disappear — someone still manages the consequence; you are just paying someone else to absorb it.

[PAUSE — 2 seconds]

Mitigate: Take action to reduce the probability or impact of the risk before it occurs. Adding extra testing time reduces the probability of a defect escaping to production. Building in buffer time mitigates schedule risk. Mitigation does not eliminate the risk — it makes it less likely or less damaging.

[PAUSE — 2 seconds]

Accept: Acknowledge the risk and choose not to take action unless it occurs. Active acceptance sets aside a contingency reserve. Passive acceptance simply records the risk and monitors it.

[PAUSE — 2 seconds]

Escalate: Pass the risk to a higher authority — a program manager, portfolio manager, or organizational leader — because it is outside the project manager's authority or influence to respond to. This is a new response strategy added to the PMI framework.

[SHOW SLIDE: "Response Strategies for Opportunities (Positive Risks)"]

There are four corresponding strategies for opportunities.

Exploit: Take action to ensure the opportunity definitely occurs. If there is a chance the team could deliver two weeks early, you allocate additional resources to guarantee it.

Share: Partner with another party to capture the opportunity jointly. A teaming agreement or joint venture is an example.

Enhance: Take action to increase the probability or impact of the opportunity. Adding a more experienced developer increases the probability of early completion.

Accept: Acknowledge the opportunity but take no specific action to pursue it. Let it occur if it does.

[SHOW SLIDE: "Residual Risks and Secondary Risks"]

Two more risk concepts that appear on the exam: residual risks and secondary risks.

A residual risk is the risk that remains after a response strategy has been applied. If you mitigate a risk, some portion of it usually remains — that remainder is the residual risk.

A secondary risk is a new risk created by a risk response. For example, adding a new vendor to transfer a technology risk creates a new risk of vendor coordination failures. Secondary risks must be added to the Risk Register and managed like any other risk.

[PAUSE — 2 seconds]

Contingency reserves are funds or time buffers set aside specifically for identified risks. Management reserves are for unknown unknowns — risks that were never identified. The project manager controls contingency reserves; management reserves require higher authorization.

---

## Segment 6 — Monitoring and Controlling Risk (18:00–20:30)

[SHOW SLIDE: "Step 6 — Monitor and Control Risks"]

Risk management does not end after planning. Risks must be monitored continuously throughout the project. The Monitor and Control Risk process has several key activities.

[PAUSE — 2 seconds]

Risk audits examine whether risk responses are being implemented effectively and whether the Risk Register remains accurate. A risk audit is typically conducted by someone outside the immediate project team for objectivity.

Risk reassessments revisit the Risk Register at regular intervals to update probability, impact, and status of identified risks, and to identify any new risks that have emerged.

Risk reviews are scheduled check-ins, often held at project status meetings, where the team reviews the top risks and their current status.

Triggers and watchlist: Risk triggers are the warning signs that a risk is about to materialize. The watchlist contains low-priority risks that are being monitored but do not yet require active response.

[SHOW SLIDE: "Workarounds — Unplanned Responses"]

A workaround is an unplanned response to a risk that has actually occurred — a risk that was not previously identified or was on the watchlist but escalated unexpectedly. Workarounds are reactive; response strategies are proactive. The exam distinguishes these: if the risk was identified and planned for, executing the response plan is not a workaround. If it was unidentified, the improvised response is a workaround.

---

## Segment 7 — Closing Summary (20:30–22:00)

[SHOW SLIDE: "Module 11 Key Takeaways"]

Risk management is a proactive, ongoing discipline. The process flows from planning through identification, qualitative analysis, quantitative analysis, response planning, and continuous monitoring.

The Risk Register is the central document — it records every risk, its analysis, its owner, its response, and its current status. Risks include both threats and opportunities. Response strategies for threats are Avoid, Transfer, Mitigate, Accept, and Escalate. Response strategies for opportunities are Exploit, Share, Enhance, and Accept.

[PAUSE — 2 seconds]

Remember: residual risks remain after responses are applied; secondary risks are created by the responses themselves. Contingency reserves cover identified risks; management reserves cover unidentified risks.

[SHOW SLIDE: "Coming Up — Module 12: Communication and Stakeholder Management"]

In Module 12, we turn to communication and stakeholder management — how to plan communications, analyze stakeholder interests, build a RACI matrix, and manage engagement throughout the project lifecycle. Strong communicators make strong project managers.

Complete the lab risk register exercise, take the quiz, and post your discussion response before Wednesday. I will see you in Module 12.

[SHOW SLIDE: End card — Texas Wesleyan University | CIS-3310 | Professor Nash]

---

*End of Module 11 Video Script*

*Total estimated runtime: 20–22 minutes*
