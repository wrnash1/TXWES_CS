# Lab Activity: Module 14 — Scaled Agile: SAFe and LeSS Overview

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Points:** 100

---

## Overview

This lab is a scaling framework analysis and application exercise. You will evaluate organizational scenarios, recommend scaling approaches, and analyze how scaling choices affect Scrum's empirical process. No running code is required — this is a written analysis lab.

Estimated time: 90–120 minutes

---

## Part 1 — Framework Identification (30 points)

### Part 1 Instructions

Read each of the following four organizational descriptions. For each description:

- Identify which scaling framework (SAFe, LeSS, or neither — basic multi-team Scrum) best matches the described structure
- State the single most identifying structural element that led to your identification
- Write two to three sentences explaining how the described structure addresses the scaling challenge present in the scenario

Scenario 1: GlobalTech has forty-two development teams building an enterprise software platform. Each team is a feature team that selects work from its Requirement Area's backlog. All forty-two teams run Sprints on the same two-week cadence and deliver to a single Sprint Review. The product's overall direction is held by one person who coordinates twelve Area Product Owners.

Scenario 2: The FinanceFirst ART consists of nine teams building a corporate banking platform. Every twelve weeks, all nine teams and their leadership gather for a two-day planning event. During these two days, teams plan their next six Iterations, identify cross-team dependencies on a shared board, and commit to PI Objectives. At the end of the twelve weeks, all teams demonstrate their integrated work in a System Demo.

Scenario 3: MediApp has four teams building a healthcare application. Each team has its own Product Owner, its own backlog, and runs Sprints independently. When one team needs something from another team, they add it to that team's backlog and the receiving team's Product Owner prioritizes it whenever they choose. Teams demonstrate their work at four separate Sprint Reviews.

Scenario 4: StartupLogic has three teams building a SaaS analytics platform. One Product Owner owns a single shared backlog. All three teams start and end Sprints on the same date, attend a shared Sprint Planning Part 1 together with the Product Owner, hold separate Sprint Planning Part 2 sessions, and combine their work into one shared Sprint Review.

---

### Part 1 Grading (30 points)

- Each scenario: 7.5 pts (correct framework identified 4, identifying structural element stated 1.5, scaling explanation 2)

---

## Part 2 — Scenario Analysis: Choosing a Scaling Framework (35 points)

### Part 2 Instructions

Read the following organization description and complete the three tasks below.

### The CampusTech Platform Organization

CampusTech is a software company building a large-scale campus management platform used by 200 universities. The platform has five major product areas: Student Registration, Financial Aid, Housing, Academic Records, and Campus Events. The platform has been built by five independent teams, each owning one product area. Each team has its own Product Owner and its own backlog. The teams rarely communicate. Dependencies between teams are handled via email and informal conversations.

Current problems:

- Student Registration frequently blocks on Housing because enrollment and room assignments share a database schema that neither team fully controls
- Financial Aid features require Academic Records data that is not available in the right format until weeks after Financial Aid needs it
- Campus Events integrates with Student Registration for event capacity management — this integration breaks at least once per Sprint because neither team knows the other's release schedule
- The organization's CPO wants to add a new Mobile App product area. If current team patterns hold, the Mobile App team will immediately create dependencies on all five existing teams.

The company's CEO has asked an Agile consultant to recommend a scaling approach. The organization has 45 developers in total across the five teams.

Task A — Framework recommendation (15 points): Recommend either SAFe or LeSS for CampusTech and justify your recommendation. Your justification must:

- Address the specific dependency and coordination problems described
- Explain how your recommended framework's structure would reduce these problems
- Acknowledge the most significant trade-off of your recommendation
- Be 150–200 words

Task B — Team restructuring (10 points): Under your recommended framework, describe how you would restructure the existing five component teams. Would you keep component teams, convert to feature teams, or use a hybrid? Explain the rationale for your choice and how it addresses the Mobile App dependency risk.

Task C — Product Ownership (10 points): Under your recommended framework, describe how Product Ownership should be structured at CampusTech. Who owns what? How does priority get set across product areas? What problem does your proposed structure solve that the current model does not? Your response should be 100–150 words.

---

### Part 2 Grading (35 points)

- Task A — Framework recommendation: 15 pts (framework named 2, dependency connection 6, trade-off acknowledged 4, word count met 3)
- Task B — Team restructuring: 10 pts (restructuring approach described 5, Mobile App risk addressed 5)
- Task C — Product Ownership: 10 pts (ownership structure described 4, priority mechanism described 3, current-model problem solved 3)

---

## Part 3 — Scrum Values at Scale (35 points)

### Part 3 Instructions

Read the following scenario and complete the three tasks below.

### The Meridian ART After Six PIs

The Meridian ART has been running SAFe for six Program Increments. The organization adopted SAFe with high hopes eighteen months ago, but the Scrum Master community is reporting concerns:

- PI Planning takes two full days and produces a plan that most teams say is "out of date by Iteration 2"
- Teams are completing their Iteration work but the System Demo at PI end consistently reveals integration failures between Team 4 and Team 7
- The Release Train Engineer reports that 30 percent of PI Objectives are not met — teams commit to objectives at PI Planning and then cannot deliver them
- Team Retrospectives are happening but surfaced issues are rarely addressed at the ART level
- Developers say they spend more time in cross-team coordination meetings than in the previous non-SAFe structure

Task A — Empiricism diagnosis (10 points): Identify which of Scrum's three pillars of empiricism (Transparency, Inspection, Adaptation) is most significantly failing in the Meridian ART. Explain how the described symptoms show evidence of that failure. Reference at least two specific symptoms from the scenario.

Task B — Root cause analysis (15 points): The 30 percent PI Objective miss rate and the persistent integration failures between Team 4 and Team 7 are the most serious symptoms. For each, identify one probable root cause (not just the symptom) and propose one specific structural or behavioral change that would address it. Your analysis should draw on concepts from both the SAFe framework and core Scrum principles.

Task C — Scrum Master communication (10 points): Write a 100–150 word message from the Release Train Engineer to the organization's CPO explaining why the ART's current PI Planning and coordination model is not producing the expected results, and what specific change should be made. The message should:

- Reference empiricism or continuous improvement without using jargon-heavy language
- Frame the change in terms of business outcome (delivery reliability, integration quality)
- Avoid blaming teams or individual roles

---

### Part 3 Grading (35 points)

- Task A — Empiricism diagnosis: 10 pts (correct pillar identified 3, two symptoms cited 4, connection explained 3)
- Task B — Root cause analysis: 15 pts (root cause for PI Objective miss rate 5, root cause for integration failures 5, proposed changes appropriate 5)
- Task C — Communication message: 10 pts (empiricism referenced accessibly 3, business outcome framed 4, tone professional 3)

---

## Deliverables

Submit a single document (PDF or Word) containing:

1. Part 1: Four framework identifications with reasoning
2. Part 2: CampusTech framework recommendation, team restructuring, and Product Ownership design
3. Part 3: Empiricism diagnosis, root cause analysis, and Release Train Engineer communication

Submit to the Canvas assignment portal by the module due date.

---

## Part 9 — Challenge Exercise

### Challenge 1: PI Planning Simulation

Your team is preparing for PI Planning for the CampusTech platform from Part 2, assuming the organization has adopted SAFe with five teams on a single ART. The upcoming PI is 10 weeks long (five 2-week Iterations plus one IP Iteration).

1. The Program Backlog has been prioritized by the Product Manager. Design a PI Planning agenda for Day 1 (8 hours). For each agenda block: name the activity, specify the duration, describe who participates, and state the output produced. Your agenda must include at minimum: business context presentation, team breakout planning, and dependency identification.
2. Team 3 (Academic Records) and Team 5 (Campus Events) have identified a dependency: Team 5 needs Team 3 to expose a new API by Iteration 3. On your team board, draw this dependency using text notation (e.g., "Team 5 → Team 3: Academic Calendar API, needed by Iteration 3, at risk if Team 3 misses Iteration 2 target"). Then write the ROAM entry for this dependency: state whether it is Resolved, Owned, Accepted, or Mitigated, and explain the rationale.
3. Write three PI Objectives for Team 3 (Academic Records) for this PI. Each objective must be: business-facing (not a technical task), measurable (the team can say yes or no at PI end), and connected to the overall CampusTech platform's value delivery.
4. At Iteration 3 of the PI, Team 3 reports they cannot deliver the Academic Calendar API because a developer has left the team. Write a two-paragraph communication from the Release Train Engineer to the CPO explaining: what has happened, what the ART-level consequence is for Team 5's PI Objectives, and what options are available (team capacity reallocation, scope negotiation, risk acceptance).

### Challenge 2: Framework Transition Analysis

A healthcare software company, MedRecord Corp, currently has eight component teams using basic multi-team Scrum without a scaling framework. Their architecture splits across: Patient Data, Billing, Clinical Workflows, Lab Results, Scheduling, Reporting, Integration/APIs, and Mobile. The company wants to adopt a scaling framework within the next six months.

1. Write a two-column comparison analyzing MedRecord Corp's situation from both a SAFe perspective and a LeSS perspective. For each framework, address: what structural changes are required to the team organization, what the first three months of adoption look like, what the primary risk of adoption is, and what the anticipated benefit is after 12 months.
2. The LeSS adoption requires converting eight component teams into feature teams. The Billing team lead objects: "Our billing engineers specialize in financial compliance — they cannot become generalists." Write a 100-word response that acknowledges this concern while explaining what LeSS means by feature team and why specialization is preserved within a feature team structure.
3. A stakeholder asks: "Could we use SAFe for some teams and LeSS for others in the same organization?" Write a 75-100 word response explaining why this would be problematic from a shared Sprint cadence, Product Ownership, and empiricism perspective.
4. After 12 months of SAFe adoption, the MedRecord Corp engineering VP reports: "Our velocity per team is the same but we are spending 4 hours per week per developer in ART-level coordination meetings that produce no visible deliverables." Using the concept of value stream efficiency, calculate the cost of this coordination overhead for a 64-developer organization at 4 hours per developer per week. Express the result in person-hours per week and full-time-equivalent developers consumed by coordination. Then write a two-sentence recommendation.

### Reflection Questions

1. The Scrum Guide says that Scrum is intentionally incomplete — it defines the minimum structure needed for empiricism to function. SAFe adds substantial prescriptive structure on top of this minimum. From a Scrum purist perspective, what aspects of SAFe's prescription are most likely to undermine empiricism, and what evidence would you look for in a SAFe organization to determine whether empiricism is functioning?
2. Both SAFe and LeSS claim to scale Scrum while preserving its values. Yet practitioners in both camps argue the other framework is "not really Scrum." Based on your reading, which framework stays closer to Scrum's foundational principles (empiricism, self-organization, cross-functionality, transparency), and why does the other framework deviate? Support your argument with at least two specific structural differences.

---

## Rubric Summary

| Component | Points |
|---|---|
| Part 1 — Framework Identification (4 scenarios) | 30 |
| Part 2 — Scenario Analysis: Framework Selection (Tasks A, B, C) | 35 |
| Part 3 — Scrum Values at Scale (Tasks A, B, C) | 35 |
| Total | 100 |

---
