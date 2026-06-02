# Reading Guide: Module 02 - Business Analysis Planning and Monitoring

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 02 covers BABOK Guide v3 Knowledge Area 2: Business Analysis Planning and Monitoring. This Knowledge Area defines what a BA must plan before elicitation begins — who to engage, how to work, how requirements will be governed, and how BA performance will be measured. KA 2 is among the most heavily tested areas on the ECBA exam because it defines the professional discipline of business analysis rather than just the techniques.

---

## 1. Core Vocabulary

### 1.1 Business Analysis Approach

The business analysis approach is the overall strategy the BA selects for conducting BA activities on a specific project. It includes decisions about methodology (predictive vs. adaptive), documentation level, formality of reviews, and collaboration frequency. The approach is tailored to the project context — its size, complexity, stability of requirements, and organizational culture.

### 1.2 Stakeholder Engagement Approach

The stakeholder engagement approach documents who the stakeholders are, their roles and authority, their attitudes toward the proposed change, how the BA will collaborate with each stakeholder or group, and the frequency and format of communications. It is the BA's plan for managing every human relationship that affects requirements quality.

### 1.3 Governance

In the BA context, governance defines who has the authority to approve, reject, or change requirements, and what process is followed when a requirement change is proposed after baseline approval. A governance plan prevents requirements from being changed informally — a major source of scope creep and project failure.

### 1.4 Predictive Approach

A predictive approach (often called Waterfall) defines all requirements before design begins, uses formal documentation and change control, and works best when scope is stable, requirements are well-understood, or regulatory compliance demands complete specification before construction.

### 1.5 Adaptive Approach

An adaptive approach (Agile, Scrum, Kanban) elaborates requirements incrementally through iterations or sprints. Requirements evolve through frequent stakeholder feedback. This works best when scope is expected to change, when delivering incremental value is prioritized, and when key stakeholders are highly available.

### 1.6 Business Analysis Performance Metrics

These are measures the BA uses to evaluate whether BA activities are producing high-quality results on schedule. Common metrics include: number of requirement defects discovered per review cycle, stakeholder satisfaction ratings, percentage of planned elicitation sessions completed on schedule, and the ratio of post-baseline change requests to original requirements.

---

## 2. The Five Tasks of BABOK KA 2

| Task | Purpose | Key Output |
|---|---|---|
| Plan Business Analysis Approach | Select methodology, formality, and collaboration model | BA Approach document |
| Plan Stakeholder Engagement | Identify and analyze all stakeholders | Stakeholder Register, Engagement Approach |
| Plan Business Analysis Governance | Define decision-making authority and change control | Governance Approach |
| Plan Business Analysis Information Management | Decide how requirements are stored, versioned, and shared | Information Management Approach |
| Identify Business Analysis Performance Improvements | Monitor BA work quality and take corrective action | Updated BA plan, performance improvements |

These five tasks are not a rigid sequence — they interact and feed each other. The chosen approach influences how information is managed, and the stakeholder analysis shapes governance structure.

---

## 3. The Power-Interest Grid

The Power-Interest Grid (also called the Stakeholder Analysis Matrix) classifies stakeholders on two dimensions: organizational power and level of interest in the project outcome.

| Quadrant | Power | Interest | Engagement Strategy |
|---|---|---|---|
| Manage Closely | High | High | Frequent involvement, real-time updates, direct access for decisions |
| Keep Satisfied | High | Low | Executive summaries at milestones, escalate only key decisions |
| Keep Informed | Low | High | Regular updates, involve in reviews and UAT |
| Monitor | Low | Low | Periodic briefings only; avoid over-communicating |

Stakeholder attitudes toward the change also matter. A resistant high-power stakeholder requires a different strategy than an enthusiastic one. Document attitudes as "Champion," "Neutral," or "Resistant" in the Stakeholder Register.

---

## 4. Stakeholder Register Columns

The Stakeholder Register is the BA's living document. It should capture at minimum:

- Full name and job title
- Organizational unit
- Stakeholder type (user, sponsor, SME, regulator, etc.)
- Power level: High, Medium, Low
- Interest level: High, Medium, Low
- Grid quadrant classification
- Attitude toward change: Champion, Neutral, Resistant
- Preferred communication channel and frequency
- Known concerns or constraints

The register is updated throughout the project whenever stakeholders join, leave, or change posture.

---

## 5. Predictive vs. Adaptive Approach Comparison

| Factor | Predictive Approach | Adaptive Approach |
|---|---|---|
| Requirements stability | Stable, well-understood | Evolving, emerging |
| Documentation level | High formality, full SRS | Just-enough; user stories and acceptance criteria |
| Change management | Formal change control board | Product backlog reprioritization |
| Stakeholder availability | Limited or batched review cycles | Continuous collaboration |
| Best suited for | Regulatory, fixed-scope, long-horizon projects | Innovation, fast-moving, high-feedback environments |
| BA role | Requirements gatekeeper, specification author | Backlog partner, sprint collaborator |

---

## 6. SDLC Phase Positioning of KA 2

KA 2 activities are most intense at the beginning of a project, before elicitation begins, because their outputs are prerequisites for all subsequent BA work. However, KA 2 activities recur throughout:

- Planning phase: Initial stakeholder identification, feasibility input, approach selection
- Analysis phase: Full stakeholder engagement, governance in operation, continuous monitoring
- Design phase: Governance manages post-baseline change requests
- Implementation phase: Monitoring BA performance on requirements traceability and defect rates

---

## 7. BABOK Knowledge Area Reference

| Knowledge Area | Number | Core Question |
|---|---|---|
| Business Analysis Planning and Monitoring | KA 2 | How will BA work be conducted? |
| Strategy Analysis | KA 3 | What is the need and what future state do we want? |
| Elicitation and Collaboration | KA 4 | How do we gather information from stakeholders? |
| Requirements Analysis and Design Definition | KA 5 | How do we specify, model, and validate requirements? |
| Requirements Life Cycle Management | KA 6 | How do we maintain, trace, and approve requirements? |
| Solution Evaluation | KA 7 | Is the deployed solution delivering expected value? |

---

## 8. Certification Exam Tips

1. The five tasks of KA 2 are frequently tested as a group. Be able to name them all and describe what each one produces. "Plan Stakeholder Engagement" produces the Stakeholder Register — do not confuse it with the elicitation activities in KA 4 that actually interview those stakeholders.

2. The Power-Interest Grid quadrant names are tested directly. Know all four: Manage Closely (high/high), Keep Satisfied (high/low), Keep Informed (low/high), Monitor (low/low). The exam will describe a stakeholder and ask which strategy applies.

3. A common trap question places a high-power, low-interest stakeholder (senior VP) and asks how the BA should engage them. "Meet frequently and involve in all decisions" is wrong. The correct answer is "Keep Satisfied" — high-level summaries at milestones, escalate only key decisions.

4. "BA performance monitoring" is KA 2's final task. When a scenario describes a BA noticing that elicitation is falling behind, the correct response is: analyze the variance, identify root cause, update the BA plan. Immediately escalating to the sponsor or skipping remaining sessions are both wrong.

5. When a scenario describes stable, regulatory-driven scope with a fixed deadline, select the predictive approach. When it describes innovative products with evolving stakeholder feedback, select the adaptive approach.

6. Governance in BA planning means defining who approves requirements changes — not who writes requirements or who builds the system. Governance prevents scope creep by requiring formal approval for any post-baseline change.

7. The BA approach is always tailored to the project. BABOK does not prescribe one methodology — it describes factors the BA should consider. This "it depends" philosophy is characteristic of BABOK and appears throughout the ECBA exam.

8. Stakeholder identification is the first step in stakeholder planning. You cannot plan engagement for stakeholders you have not yet identified. A scenario where a stakeholder is discovered late and raises a new requirement is a KA 2 failure — insufficient early identification.

---

## 9. Required and Supplemental Reading

Required reading:

- BABOK Guide v3, Knowledge Area 2 — all five tasks, inputs, outputs, and techniques
- BABOK Guide v3, Chapter 9 (Techniques) — review: Stakeholder List/Map/Personas, Interviews, Organizational Modeling, Lessons Learned

Supplemental reading:

- PMI PMBOK Guide section on Stakeholder Management — compare PM and BA perspectives on stakeholder analysis
- iiba.org — ECBA Certification Handbook for experience and exam eligibility requirements

---

## 10. Study Checklist

- [ ] Name and describe all five KA 2 tasks from memory.
- [ ] Draw the Power-Interest Grid and write the engagement strategy for each quadrant.
- [ ] List the standard columns of a Stakeholder Register.
- [ ] Explain the difference between predictive and adaptive BA approaches with one example context each.
- [ ] Define governance in the BA context and explain why it prevents scope creep.
- [ ] Read BABOK Guide v3 KA 2 (all five tasks).
- [ ] Watch the Module 02 video lecture.
- [ ] Complete the Module 02 lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.
