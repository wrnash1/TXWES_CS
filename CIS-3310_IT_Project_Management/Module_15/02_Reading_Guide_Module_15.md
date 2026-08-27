# Reading Guide: Module 15 — Agile Project Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Overview

This reading guide supports Module 15 of CIS-3310. Agile project management is a
growing portion of the CompTIA Project+ exam and an essential competency for any IT
professional entering the workforce today. This guide covers the Agile Manifesto and
principles, the Scrum framework in depth, Kanban, hybrid approaches, sprint planning,
velocity, and the PM's role in Agile environments.

---

## Section 1: The Agile Manifesto and Twelve Principles

### 1.1 The Four Values

The Agile Manifesto, published in 2001, establishes four core values that distinguish
Agile from traditional project management approaches.

| Agile Values — Preferred Left Over Right |
|---|
| Individuals and interactions over processes and tools |
| Working software over comprehensive documentation |
| Customer collaboration over contract negotiation |
| Responding to change over following a plan |

The manifesto explicitly states: "That is, while there is value in the items on the
right, we value the items on the left more." Agile is not anti-process or
anti-documentation; it is a prioritization statement about what matters most.

### 1.2 The Twelve Principles

The Agile Manifesto is supported by twelve principles. The following are the most
commonly tested on Project+.

| Principle | Summary |
|---|---|
| 1 | Highest priority is satisfying the customer through early and continuous delivery of valuable software |
| 2 | Welcome changing requirements, even late in development |
| 3 | Deliver working software frequently, from a couple of weeks to a couple of months |
| 4 | Business people and developers must work together daily throughout the project |
| 5 | Build projects around motivated individuals; give them the environment and support they need |
| 6 | Face-to-face conversation is the most efficient and effective method of conveying information |
| 7 | Working software is the primary measure of progress |
| 8 | Agile processes promote sustainable development — the team should maintain a constant pace indefinitely |
| 9 | Continuous attention to technical excellence and good design enhances agility |
| 10 | Simplicity — the art of maximizing the amount of work not done — is essential |
| 11 | The best architectures, requirements, and designs emerge from self-organizing teams |
| 12 | At regular intervals, the team reflects on how to become more effective and adjusts accordingly |

---

## Section 2: Agile vs. Waterfall Comparison

### 2.1 Core Differences

| Dimension | Waterfall | Agile |
|---|---|---|
| Requirements | Defined upfront; controlled change | Evolve continuously throughout |
| Planning horizon | Full project planned before execution | Rolling wave; sprint-by-sprint |
| Delivery | Single delivery at project end | Working increments every sprint |
| Customer involvement | Primarily at start and end | Continuous throughout |
| Change management | Formal change control process | Change welcomed; handled in backlog |
| Risk timing | Risk discovered late (at testing/UAT) | Risk surfaced early (end of each sprint) |
| Documentation | Comprehensive; required at each phase | Lightweight; just enough |
| Best for | Stable requirements; compliance-heavy | Evolving requirements; fast feedback |

### 2.2 Choosing the Right Approach

The Cynefin framework offers a useful lens for approach selection.

- Simple/Obvious problems with known solutions and stable requirements favor waterfall.
- Complicated problems where expertise matters but requirements can be defined favor waterfall or hybrid.
- Complex problems where requirements emerge through experimentation favor Agile.
- Chaotic problems requiring immediate action may need a stabilization phase before any framework applies.

---

## Section 3: The Scrum Framework

Scrum is the most widely adopted Agile framework globally. It is structured around
three roles, five events, and three artifacts, all governed by five values.

### 3.1 Scrum Values

The five Scrum values are commitment, focus, openness, respect, and courage. These
values underpin every Scrum practice. When teams lose these values, Scrum ceremonies
become hollow rituals rather than productive collaboration.

### 3.2 Scrum Roles

| Role | Responsibilities | What They Are NOT |
|---|---|---|
| Product Owner | Owns product backlog; prioritizes work; accepts/rejects increments; represents stakeholder interests | Not a committee; single decision authority |
| Scrum Master | Facilitates events; removes impediments; coaches team on Scrum; protects team from external interference | Not a project manager; not a team lead |
| Developers | Design, build, and test the product increment; self-organize to deliver sprint goal | Not interchangeable resources; cross-functional team |

### 3.3 Scrum Events Reference Table

| Event | Purpose | Time Box | Who Attends |
|---|---|---|---|
| Sprint | Container for all work; produces shippable increment | 1–4 weeks (commonly 2 weeks) | All Scrum team members |
| Sprint Planning | Define sprint goal; select backlog items; decompose into tasks | Max 8 hours for 4-week sprint; proportionally shorter | All Scrum team members |
| Daily Scrum | Synchronize work; identify impediments; 15-minute standup | 15 minutes | Developers (Scrum Master optional; PO optional) |
| Sprint Review | Demonstrate increment to stakeholders; gather feedback; update backlog | Max 4 hours for 4-week sprint | All Scrum team + invited stakeholders |
| Sprint Retrospective | Inspect team process; identify improvements; create action plan | Max 3 hours for 4-week sprint | All Scrum team members |

### 3.4 Scrum Artifacts Reference Table

| Artifact | Owner | Description | Commitment |
|---|---|---|---|
| Product Backlog | Product Owner | Ordered list of all desired product features and improvements | Product Goal |
| Sprint Backlog | Developers | Selected PBIs for current sprint plus the plan to deliver them | Sprint Goal |
| Product Increment | Developers | Sum of all completed PBIs meeting the Definition of Done | Definition of Done |

### 3.5 Definition of Done

The Definition of Done (DoD) is a formal list of criteria that every increment must
meet before it can be considered complete. A strong DoD includes criteria such as:

- Code reviewed and approved by at least one peer
- Unit tests written and passing at 80%+ coverage
- Integration tests passing in staging environment
- Security scan completed with no critical findings
- Documentation updated
- Product Owner acceptance received

Without a DoD, teams accumulate undone work — sometimes called technical debt —
that resurfaces later as expensive rework or production defects.

---

## Section 4: Sprint Planning and Estimation

### 4.1 User Stories

User stories are the most common format for product backlog items in Scrum. They
follow the template: "As a [user type], I want [capability] so that [business value]."

A well-written user story is INVEST:

| Letter | Meaning |
|---|---|
| I | Independent — can be developed without depending on another story |
| N | Negotiable — details are discussed; not a rigid contract |
| V | Valuable — delivers clear value to the user or business |
| E | Estimable — the team can estimate the effort |
| S | Small — fits within a single sprint |
| T | Testable — acceptance criteria can be verified |

### 4.2 Story Point Estimation

Story points are a relative effort estimate used in Agile planning. Unlike hours,
story points capture complexity, uncertainty, and effort together in a single number.
Teams commonly use the Fibonacci sequence (1, 2, 3, 5, 8, 13, 21) for story point
values, because larger numbers reflect increasing uncertainty.

Planning Poker is the most common estimation technique. Each team member privately
selects a card representing their estimate. Cards are revealed simultaneously to avoid
anchoring bias. Where estimates diverge significantly, the team discusses and
re-estimates until consensus is reached.

### 4.3 Velocity

Velocity is the average number of story points a team completes per sprint, calculated
over the last three to six sprints.

Example velocity calculation:

| Sprint | Story Points Completed |
|---|---|
| Sprint 1 | 28 |
| Sprint 2 | 32 |
| Sprint 3 | 30 |
| Sprint 4 | 34 |
| Sprint 5 | 31 |
| Average Velocity | 31 |

A team with a velocity of 31 should plan approximately 31 story points into each
future sprint. Velocity is a forecasting tool, not a performance target.

### 4.4 Release Burndown

If a product backlog contains 310 story points and the team's velocity is 31, the
team can forecast approximately 10 sprints (at 2 weeks each = 20 weeks) to complete
the work. This is a release burndown calculation — a high-level roadmap projection.

---

## Section 5: Kanban

### 5.1 Core Kanban Principles

Kanban is a lean-influenced Agile method built on four core principles:

- Start with what you do now
- Agree to pursue incremental, evolutionary change
- Respect the current process, roles, and responsibilities
- Encourage acts of leadership at all levels

### 5.2 Kanban Practices

| Practice | Description |
|---|---|
| Visualize work | All work items visible on the board; nothing hidden in email or spreadsheets |
| Limit WIP | Maximum number of items allowed in each column; forces finishing before starting |
| Manage flow | Monitor cycle time and throughput; identify and remove bottlenecks |
| Make policies explicit | Team agrees on how work moves between columns; DoD for each stage |
| Implement feedback loops | Regular cadence reviews; adjust WIP limits as needed |
| Improve collaboratively | Use data and models to guide improvement decisions |

### 5.3 Kanban vs. Scrum

| Dimension | Scrum | Kanban |
|---|---|---|
| Cadence | Fixed sprints (1–4 weeks) | Continuous flow; no sprints |
| Roles | Product Owner, Scrum Master, Developers | No prescribed roles |
| WIP limits | Implicit (sprint capacity) | Explicit per column |
| Change within cycle | No scope changes mid-sprint | New work can enter anytime |
| Estimation | Required (story points) | Optional |
| Primary metric | Velocity (points/sprint) | Cycle time; throughput |
| Best for | Product development; known team; regular cadence | Support work; unpredictable demand; ops |

---

## Section 6: Hybrid Project Management

### 6.1 Why Hybrid Exists

Pure Agile approaches assume fully empowered, co-located teams, active product owners,
and organizations tolerant of evolving scope. Most real enterprises have governance
requirements, regulatory compliance needs, and financial reporting structures that
require some level of upfront planning and formal documentation.

Hybrid approaches blend waterfall's structure with Agile's adaptability. Common hybrid
patterns include:

- Waterfall initiation and planning phases followed by Agile delivery sprints
- Agile development with waterfall infrastructure and procurement
- Scrum for software with stage-gate approvals at major milestones
- Waterfall program management with Agile team-level execution

### 6.2 PMI's Hybrid Stance

PMI's PMBOK Guide Seventh Edition and the Agile Practice Guide both recognize that
hybrid is the most common real-world approach. The Project+ exam tests candidates'
ability to identify when hybrid is appropriate and to describe how waterfall and Agile
elements coexist.

---

## Section 7: Agile PM Roles and Responsibilities

### 7.1 Traditional PM vs. Agile PM

| Dimension | Traditional PM | Agile PM |
|---|---|---|
| Planning | Detailed upfront plan; WBS driven | Rolling wave; sprint-by-sprint |
| Control | Variance analysis against baseline | Adaptation; remove impediments |
| Scope | Defined and controlled | Managed via backlog prioritization |
| Reporting | Status reports; milestone tracking | Velocity; burndown; sprint reviews |
| Team management | Assign tasks; track hours | Servant leadership; self-organizing teams |
| Risk | Risk register; formal mitigation | Surfaced in retrospectives; addressed in backlog |

### 7.2 Agile Governance

Governance does not disappear in Agile — it evolves. Key governance mechanisms in
Agile environments include:

- Sprint Reviews as formal stakeholder checkpoints
- Product Backlog as the living scope baseline
- Velocity and burndown charts as progress transparency
- Retrospectives as process improvement accountability
- Definition of Done as quality governance

---

## Section 8: Key Terms Glossary

| Term | Definition |
|---|---|
| Agile | Iterative, incremental approach to project management emphasizing adaptability and customer collaboration |
| Scrum | Most popular Agile framework; time-boxed sprints; three roles, five events, three artifacts |
| Sprint | Fixed-length iteration in Scrum (1–4 weeks) that produces a shippable product increment |
| Product Owner | Scrum role responsible for product backlog and stakeholder representation |
| Scrum Master | Scrum role responsible for facilitating events and removing impediments |
| Product Backlog | Ordered list of all desired product features; owned by Product Owner |
| Sprint Backlog | Items selected for the current sprint; owned by the development team |
| Definition of Done | Shared agreement on what criteria must be met for work to be considered complete |
| User Story | Backlog item format: "As a [user], I want [capability] so that [value]" |
| Story Points | Relative effort estimate unit; captures complexity, risk, and effort |
| Velocity | Average story points completed per sprint; used for forecasting |
| Planning Poker | Team estimation technique using simultaneous card reveal to avoid anchoring |
| Kanban | Agile method using continuous flow and WIP limits; no fixed sprints |
| WIP Limit | Maximum number of work items allowed in a Kanban column simultaneously |
| Cycle Time | Time from work item start to completion; primary Kanban metric |
| Hybrid | Project approach blending waterfall and Agile elements |
| Retrospective | Scrum event where the team inspects process and plans improvements |
| Sprint Review | Scrum event where the team demonstrates the increment to stakeholders |
| Increment | Working product output of a sprint; must meet Definition of Done |
| Burndown Chart | Visual showing remaining work over time; tracks sprint or release progress |

---

## Section 9: Module 15 Study Checklist

Use this checklist to confirm your readiness before the quiz and Project+ exam.

- [ ] I can state the four Agile Manifesto values correctly
- [ ] I can explain the twelve Agile principles at a summary level
- [ ] I can describe the differences between Agile and waterfall approaches
- [ ] I know the three Scrum roles and their distinct responsibilities
- [ ] I can name and describe all five Scrum events with their time boxes
- [ ] I know the three Scrum artifacts and their commitments
- [ ] I can explain the Definition of Done and why it matters
- [ ] I know the INVEST criteria for user stories
- [ ] I can explain story points and how Planning Poker works
- [ ] I can calculate velocity from sprint data
- [ ] I know the core principles and practices of Kanban
- [ ] I can compare Scrum and Kanban across key dimensions
- [ ] I can describe at least two hybrid approach patterns
- [ ] I understand how traditional PM responsibilities shift in Agile environments
- [ ] I can identify whether Agile, waterfall, or hybrid is appropriate for a given scenario

---

## Section 10: Project+ Exam Alignment

| Exam Domain | Objective | Module Coverage |
|---|---|---|
| Domain 1: Project Management Concepts | 1.5 Compare and contrast project management methodologies | Sections 2, 6 |
| Domain 2: Project Planning | 2.5 Explain Agile project planning concepts | Sections 3, 4 |
| Domain 3: Project Execution | 3.5 Explain Agile execution activities | Sections 3.3, 4, 5 |
| Domain 4: Monitoring and Control | 4.6 Explain Agile monitoring techniques | Sections 4.3, 4.4, 7.2 |
| Domain 5: Project Closing | 5.3 Explain Agile closing activities | Section 7.2 |

---

*End of Reading Guide — Module 15*

*Texas Wesleyan University — CIS-3310 IT Project Management*

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Agile Manifesto — Original Text and Twelve Principles (Free)**
   *Agile Alliance* — [agilemanifesto.org](https://agilemanifesto.org)
   The primary source document for all Agile frameworks. Read the four values and twelve principles directly. Every Project+ Agile question traces back to this document.

2. **Scrum Guide 2020 — Official Free Reference**
   *Scrum.org* — [scrumguides.org/scrum-guide.html](https://scrumguides.org/scrum-guide.html)
   The definitive, freely downloadable Scrum framework reference. Covers all three roles, five events, three artifacts, and the commitments (Definition of Done, Sprint Goal, Product Goal) tested on Project+ and Scrum certifications.

3. **Kanban University — Kanban Method Overview (Free)**
   *Kanban University* — [kanban.university/kanban-development-method](https://kanban.university/kanban-development-method/)
   Official overview of the Kanban method including WIP limits, flow metrics, and cycle time principles. Directly supports the Kanban vs. Scrum comparison tested in Module 15.

4. **PMI Agile Practice Guide — Free Download (PMI Member or OpenEd version)**
   *Project Management Institute* — [pmi.org/pmbok-guide-standards/practice-guides/agile](https://www.pmi.org/pmbok-guide-standards/practice-guides/agile)
   PMI's official guide to Agile, hybrid, and iterative approaches aligned with PMBOK. Covers hybrid lifecycle patterns and the PM's evolving role in Agile environments — both tested on Project+.

5. **Mountain Goat Software — User Stories and Story Points Guide (Free)**
   *Mike Cohn* — [mountaingoatsoftware.com/agile/user-stories](https://www.mountaingoatsoftware.com/agile/user-stories)
   Comprehensive free guide to writing user stories, applying the INVEST criteria, sizing with story points, and running Planning Poker. Directly supports the Module 15 lab backlog construction and estimation exercises.
