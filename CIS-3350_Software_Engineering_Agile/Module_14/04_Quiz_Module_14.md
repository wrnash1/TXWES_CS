# Quiz: Module 14 — Scaled Agile: SAFe and LeSS Overview

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Total Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

In SAFe, what is an Agile Release Train (ART)?

- A) A tool for tracking Sprint velocity across a single Scrum Team
- B) A group of five to twelve Scrum Teams that plan, develop, and deliver together on a synchronized cadence
- C) A SAFe term for the Product Backlog at the enterprise level
- D) A deployment pipeline that automatically releases software to production after each Iteration

Correct Answer: B — An Agile Release Train is the primary value delivery unit in SAFe. Five to twelve teams work together on synchronized Iteration cadences, plan together during PI Planning, and deliver a System Demo at the end of each Program Increment.

Distractor Analysis:

- Why A is incorrect: Velocity tracking is a team-level metric unrelated to the ART structure. ARTs are not a reporting or measurement tool.
- Why C is incorrect: The SAFe term for the enterprise-level backlog is the Portfolio Backlog. The Program Backlog sits at the ART level, not the enterprise level.
- Why D is incorrect: A deployment pipeline is a CI/CD concept — the technical infrastructure for automated delivery. An ART is an organizational structure.

---

## Question 2

What is the primary purpose of PI Planning in SAFe?

- A) To review the work completed in the previous Program Increment and identify defects
- B) To allow all ART teams to plan their Iterations together, surface cross-team dependencies, and commit to PI Objectives
- C) To create the Program Backlog by prioritizing features for the next quarter
- D) To train team members in SAFe roles and responsibilities before a new Program Increment begins

Correct Answer: B — PI Planning is a two-day event at the start of every Program Increment where all ART teams plan together. Teams identify dependencies, negotiate scope, and commit to PI Objectives — the business outcomes they will deliver during the PI. It is SAFe's primary answer to the multi-team coordination challenge.

Distractor Analysis:

- Why A is incorrect: Reviewing completed work from the previous PI is the purpose of the System Demo and the Inspect and Adapt event — not PI Planning. PI Planning is forward-looking.
- Why C is incorrect: The Program Backlog is prepared by the Product Manager before PI Planning. PI Planning does not create the backlog — it plans the work from an existing backlog.
- Why D is incorrect: PI Planning is a planning event for the ART's work, not a training session. SAFe training happens separately through role-based education programs.

---

## Question 3

Which of the following best describes the LeSS approach to Product Ownership at scale?

- A) Each team has its own Product Owner who independently manages their team's backlog
- B) One Product Owner owns a single Product Backlog shared by all teams
- C) A Product Manager owns a Program Backlog and delegates to Team Product Owners
- D) Product Ownership rotates among team members to distribute the accountability

Correct Answer: B — LeSS's defining principle at the product ownership level is one Product Owner and one Product Backlog for all teams. All teams select work from the same shared backlog, and one person is accountable for its prioritization.

Distractor Analysis:

- Why A is incorrect: Multiple independent Product Owners with separate backlogs describes the fragmented product ownership model that LeSS explicitly avoids. It is a common anti-pattern in multi-team organizations.
- Why C is incorrect: That describes SAFe's two-level product ownership structure — Product Manager at the program level, Team Product Owners at the team level. LeSS deliberately avoids this layering.
- Why D is incorrect: Rotating Product Ownership is not a recognized practice in either SAFe or LeSS. The Product Owner role requires sustained product knowledge that cannot rotate without significant context loss.

---

## Question 4

In LeSS, what is a feature team, and why does LeSS require them?

- A) A team that specializes in UI features, as opposed to a backend team that specializes in data processing
- B) A cross-functional team capable of delivering end-to-end customer-facing features independently, without requiring handoffs to other component teams
- C) A team dedicated to testing and quality assurance for features delivered by development teams
- D) A temporary team assembled specifically to deliver a high-priority feature before returning to their regular teams

Correct Answer: B — Feature teams in LeSS are cross-functional and capable of taking a feature from the Product Backlog through development and testing without requiring work from other teams. LeSS requires feature teams because component teams create structural dependencies — handoffs between components that generate the coordination overhead LeSS is designed to eliminate.

Distractor Analysis:

- Why A is incorrect: That describes a component team model where teams specialize by technology layer. LeSS specifically recommends against this model.
- Why C is incorrect: Dedicated QA teams are separate specialist teams, not feature teams. In LeSS, testing is a skill within each feature team, not a separate team.
- Why D is incorrect: Temporary teams assembled for specific features are project-based structures. LeSS feature teams are permanent teams with stable membership.

---

## Question 5

An organization has seven teams building a single product. Each team selects items from one shared Product Backlog. All teams run Sprints on the same cadence and hold a combined Sprint Review. One person is accountable for the Product Backlog's prioritization. Which scaling structure does this describe?

- A) SAFe with seven teams on a single ART
- B) LeSS with one Product Owner and one shared Product Backlog
- C) Scrum of Scrums — seven teams coordinating via daily representative meetings
- D) Portfolio SAFe — seven teams aligned to a shared portfolio vision

Correct Answer: B — This describes the core LeSS structure exactly: one Product Owner, one Product Backlog, all teams on the same Sprint cadence, and a shared Sprint Review. SAFe would add a Program Backlog layer and a Product Manager role above the teams.

Distractor Analysis:

- Why A is incorrect: An SAFe ART would have a Program Backlog managed by a Product Manager, separate from Team Backlogs. The scenario describes one shared backlog with no program-level layer.
- Why C is incorrect: Scrum of Scrums is a coordination practice (daily representative meetings) — it is not a complete scaling structure that includes shared backlogs or synchronized Sprint events.
- Why D is incorrect: Portfolio SAFe is an organizational layer above the ART level, not a structure for describing how teams relate to a single Product Backlog.

---

## Question 6

A SAFe team's PI Objective states: "Enable customer self-service password reset in the mobile application." At the PI System Demo, this feature is not complete. What does the incomplete PI Objective most likely indicate about the PI Planning process for this team?

- A) The team did not understand how to write a good PI Objective
- B) The team's Sprint Reviews during the PI were not transparent enough
- C) The team committed to an objective without adequately identifying the dependencies, effort, or risks involved
- D) The Release Train Engineer failed to allocate enough Iterations to the mobile team

Correct Answer: C — Incomplete PI Objectives most commonly result from overcommitment during PI Planning. Teams may underestimate complexity, fail to surface a dependency on another team, or accept optimistic capacity assumptions. PI Planning's dependency mapping and risk identification (ROAM) process is specifically designed to prevent this — when it fails, the root cause is usually incomplete dependency identification or unrealistic capacity planning.

Distractor Analysis:

- Why A is incorrect: Writing PI Objectives is a skill, but poorly worded objectives lead to ambiguity — not necessarily incompleteness. The question describes a feature not delivered, not a poorly defined target.
- Why B is incorrect: Sprint Reviews during the PI reveal incremental progress but do not cause the PI Objective miss. A transparent Sprint Review might reveal the objective is at risk earlier — but the root cause is the planning commitment, not the review process.
- Why D is incorrect: The Release Train Engineer facilitates PI Planning but does not allocate Iterations to teams. Teams self-organize their Iteration plans during PI Planning.

---

## Question 7

Which of Scrum's three pillars of empiricism does multi-team dependency management most directly threaten?

- A) Transparency — because teams cannot see each other's work
- B) Inspection — because integrated Increments cannot be reviewed if teams deliver separately
- C) Adaptation — because teams cannot adjust when dependencies on other teams delay their work
- D) All three equally — because empiricism requires all three pillars simultaneously

Correct Answer: A — When teams have unmanaged dependencies, they cannot see the full state of the integrated product. A team might complete their stories but not know whether their work integrates correctly with another team's work until late — often at Sprint Review. This opacity is a Transparency failure. Without transparency, meaningful inspection and adaptation cannot follow.

Distractor Analysis:

- Why B is incorrect: Inspection may be compromised as a consequence of failed transparency, but the root pillar failure is transparency. You cannot inspect what you cannot see.
- Why C is incorrect: Adaptation is the response to inspection failures — it is downstream of the transparency problem. Delayed adaptation results from the inability to see the dependency problem early.
- Why D is incorrect: While all three pillars interact, the primary failure is in transparency. The exam tests the ability to identify the root pillar failure, not just note that the system is impaired.

---

## Question 8

What is the Innovation and Planning (IP) Iteration in SAFe, and when does it occur?

- A) The first Iteration of each PI, used for planning the remaining Iterations before development begins
- B) The final Iteration of each PI, reserved for testing, technical debt reduction, exploration, and preparation for the next PI Planning event
- C) A special Sprint scheduled quarterly, separate from the normal PI cadence, for innovation hackathons
- D) An optional Iteration that teams can skip if their PI Objectives are fully met ahead of schedule

Correct Answer: B — The IP Iteration is the last Iteration of each Program Increment. It is intentionally not a feature development Iteration. Teams use it for integration testing, technical debt work, exploration of new ideas, and preparation for the upcoming PI Planning event. It provides a buffer between the end of development and the next PI's planning activities.

Distractor Analysis:

- Why A is incorrect: The first Iteration is a development Iteration. PI Planning occurs before any Iteration begins — it is a separate event, not an Iteration.
- Why C is incorrect: The IP Iteration is a standard SAFe structure, not an optional add-on. It occurs in every PI, not quarterly, and is not a hackathon — it is structured work time.
- Why D is incorrect: The IP Iteration is not conditional on PI Objective completion. It is a fixed part of the PI cadence regardless of delivery status.

---

## Question 9

A software organization has eight teams building separate components of the same platform. Each team has its own Product Owner and deploys independently. Teams frequently block each other because their APIs are incompatible. Management has decided to adopt LeSS. What is the most significant organizational change LeSS would require?

- A) Adding a Release Train Engineer to coordinate the eight teams
- B) Converting the eight component teams into feature teams and consolidating to one Product Owner with one shared Product Backlog
- C) Implementing PI Planning every twelve weeks so all eight teams plan together
- D) Creating a Program Backlog above the eight team backlogs to manage cross-component dependencies

Correct Answer: B — LeSS's most significant organizational change is the elimination of component teams in favor of feature teams, and the consolidation of eight Product Owners into one. This directly addresses the API incompatibility problem — feature teams capable of working across the full stack can own a feature end-to-end without creating handoffs that generate incompatibilities.

Distractor Analysis:

- Why A is incorrect: The Release Train Engineer is a SAFe role. LeSS does not introduce this role.
- Why C is incorrect: PI Planning is a SAFe practice. LeSS does not add a PI Planning event — it relies on Sprint-level planning shared across all teams.
- Why D is incorrect: A Program Backlog above team backlogs is a SAFe structure. LeSS uses one shared Product Backlog for all teams with no program-level layer.

---

## Question 10

A Scrum Master at an organization that recently adopted SAFe says: "Our team spends more time in cross-team coordination meetings than we did before SAFe. We're less productive, not more." What does this observation most likely indicate?

- A) SAFe is inappropriate for this organization — it should switch to LeSS immediately
- B) The coordination overhead may indicate that the underlying cause of dependencies — component team structure, architectural coupling, or fragmented ownership — was not addressed before adding SAFe's coordination machinery
- C) The team's Scrum Master is not facilitating Daily Scrums effectively
- D) SAFe requires a longer adoption period — the coordination cost will reduce after three to four PI cycles

Correct Answer: B — Coordination overhead in SAFe is a symptom of unresolved structural problems. SAFe's ceremonies — Scrum of Scrums, System Demo, ART Sync — are designed to coordinate teams that have inherent dependencies. If those dependencies stem from component team structures or architectural coupling that SAFe did not address, the coordination machinery adds overhead without reducing the root cause. The observation is a signal to examine whether the team structure itself needs to change.

Distractor Analysis:

- Why A is incorrect: The observation is insufficient to conclude that SAFe is wrong for the organization. It indicates implementation problems, not a framework mismatch. Switching frameworks without diagnosing root causes would likely reproduce the same problems.
- Why C is incorrect: Daily Scrum facilitation affects team-level communication, not cross-team coordination overhead. The problem described is inter-team, not intra-team.
- Why D is incorrect: While SAFe adoption does have a learning curve, coordination overhead that exceeds pre-SAFe levels after multiple PIs is a structural signal, not a temporary adoption cost.

---
