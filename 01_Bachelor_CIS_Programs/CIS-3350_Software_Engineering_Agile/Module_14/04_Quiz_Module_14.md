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

### Question 11 (5 points)

In LeSS, what is the purpose of the Overall Retrospective, and who participates?

- A) It is the Retrospective held by each individual team at the end of a Sprint to improve their own working practices
- B) It is a cross-team event held after all team Retrospectives, where representatives from all teams and the Product Owner discuss systemic impediments that cannot be resolved within a single team
- C) It is a SAFe-equivalent Inspect and Adapt event held at the end of each Program Increment
- D) It is an optional event where the Product Owner reviews all team backlogs to ensure alignment before the next Sprint

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Individual team Retrospectives are held by each team separately and are not called the Overall Retrospective; they address team-level improvement, not systemic cross-team issues.
  - Why C is incorrect: The Inspect and Adapt is a SAFe event; it is not part of the LeSS structure. LeSS uses an Overall Retrospective for cross-team systemic improvement.
  - Why D is incorrect: Backlog review is a refinement activity, not a Retrospective purpose. The Overall Retrospective is about process and organizational improvement, not backlog management.

---

### Question 12 (5 points)

A SAFe organization has a Program Backlog with 40 Features. The Product Manager asks: "Who breaks these Features into Stories for the teams?" Who is responsible?

- A) The Release Train Engineer breaks Features into Stories during ART Sync meetings
- B) Each Team Product Owner breaks Features into Stories for their team's Team Backlog
- C) The System Architect breaks Features into Stories during the IP Iteration
- D) The development teams collectively break Features into Stories during PI Planning

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Release Train Engineer facilitates ART-level events and removes impediments; story decomposition is not an RTE responsibility.
  - Why C is incorrect: The System Architect guides technical decisions and architectural alignment, not backlog decomposition.
  - Why D is incorrect: Development teams provide effort estimates and identify dependencies during PI Planning, but the formal responsibility for decomposing features into stories for a team's backlog belongs to the Team Product Owner.

---

### Question 13 (5 points)

An organization is choosing between SAFe and LeSS. Their primary concern is minimizing organizational disruption while adding multi-team coordination. Which framework is more appropriate and why?

- A) LeSS — because it adds fewer roles and ceremonies and preserves the existing organizational structure
- B) SAFe — because it provides a complete organizational blueprint that fits within existing hierarchies and adds coordination roles without eliminating component team structures
- C) LeSS — because it requires the fewest changes to Product Ownership and team structure
- D) SAFe — because it is the only framework that supports more than eight teams

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: LeSS actually causes higher organizational disruption because it requires converting component teams to feature teams and consolidating Product Ownership, which challenges existing structures significantly.
  - Why C is incorrect: LeSS requires substantial changes — specifically converting component teams and centralizing Product Ownership — which is organizationally disruptive.
  - Why D is incorrect: LeSS Huge supports organizations larger than eight teams through Requirement Areas; the framework's scale ceiling is not a reason to choose SAFe.

---

### Question 14 (5 points)

In a LeSS Sprint Planning Part 1, what is the Product Owner's role?

- A) To assign Stories to specific teams based on their technical specializations
- B) To clarify the highest-priority items on the shared Product Backlog so all teams can understand the work and self-select items
- C) To split the Product Backlog into team-specific segments before the meeting
- D) To approve each team's Sprint Goal after Part 1 and before Part 2 begins

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Assigning stories based on specialization implies component team thinking; in LeSS, teams are feature teams that self-select based on capacity and the whole-product perspective, not technical specialty.
  - Why C is incorrect: There is one shared Product Backlog in LeSS — it is not split into team-specific segments. All teams pull from the same backlog.
  - Why D is incorrect: Sprint Goals in LeSS are set by teams during Part 2; the Product Owner does not approve them in a formal gate between Part 1 and Part 2.

---

### Question 15 (5 points)

In SAFe, what does ROAM stand for and when is it used?

- A) Review, Order, Assign, Manage — a backlog prioritization technique used after PI Planning
- B) Resolved, Owned, Accepted, Mitigated — a risk management tool used during PI Planning to categorize and assign ART risks
- C) Release, Optimize, Align, Monitor — a deployment strategy for managing production releases after each PI
- D) Retrospect, Observe, Adapt, Measure — the Inspect and Adapt framework used at the end of each PI

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: ROAM is about risk management, not backlog prioritization; the letters do not stand for Review, Order, Assign, Manage.
  - Why C is incorrect: ROAM is a planning-time risk tool, not a deployment strategy. Production release decisions are made separately from PI Planning risk categorization.
  - Why D is incorrect: The Inspect and Adapt is a separate SAFe event; ROAM is specifically a risk categorization tool used during PI Planning.

---

### Question 16 (5 points)

A Scrum team within a SAFe ART discovers a blocker on Day 3 of Iteration 2 that requires a design decision from the System Architect. The next System Demo is six weeks away. What is the most appropriate immediate action?

- A) Raise the blocker at the Inspect and Adapt event in six weeks
- B) Move the story to the next Iteration and continue working on other items without escalating
- C) Raise the blocker through the Scrum Master to the Release Train Engineer who can engage the System Architect before the next ART Sync
- D) The Product Owner should change the PI Objective to remove the blocked story from scope

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Waiting six weeks to surface a blocker violates CI principles and the Scrum value of transparency. Blockers should be escalated immediately.
  - Why B is incorrect: Moving a blocked story to the next Iteration without escalation may cascade into PI Objective failures and does not resolve the architectural question that will recur.
  - Why D is incorrect: Changing PI Objectives is possible but is a last resort, not an immediate response to a Day 3 blocker. The first action is to resolve the blocker, not to change the commitment.

---

### Question 17 (5 points)

Which of the following correctly describes the relationship between a LeSS Sprint and a SAFe Program Increment?

- A) They are the same concept; SAFe renamed the Sprint to Program Increment to signal organizational maturity
- B) A LeSS Sprint is a single two-week iteration across all teams; a SAFe Program Increment is a multi-iteration timebox of 10–12 weeks containing multiple Sprints
- C) A SAFe Program Increment contains one Sprint; a LeSS Sprint contains multiple Iterations
- D) Both are timeboxes of the same duration but with different numbers of teams

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Sprint and Program Increment are not synonymous. A PI spans multiple Sprints and includes planning, coordination, and IP Iteration events that a single Sprint does not.
  - Why C is incorrect: The relationship is reversed — a PI contains multiple Sprints (Iterations), not the other way around.
  - Why D is incorrect: Sprint and Program Increment have different durations by definition; this answer is factually incorrect.

---

### Question 18 (5 points)

An Agile coach observes that in a SAFe organization, teams complete their Team Backlog Items each Iteration but the System Demo consistently reveals that teams built pieces that do not fit together. What is the most likely structural cause?

- A) The teams are not following the Definition of Done
- B) The teams planned their Iterations independently without identifying cross-team dependencies during PI Planning
- C) The Release Train Engineer is not facilitating Daily Scrums for each team
- D) The Product Manager's Program Backlog contains too many Features for the PI

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Individual stories meeting the DoD does not guarantee that stories from different teams integrate correctly. The DoD addresses completeness at the story level, not integration at the ART level.
  - Why C is incorrect: Daily Scrum facilitation is the Scrum Master's role; the RTE facilitates ART-level events. Individual team Daily Scrums address team-level blockers, not cross-team integration alignment.
  - Why D is incorrect: A full Program Backlog may indicate scope management issues, but the integration failure symptom specifically indicates dependency identification failure during PI Planning, not overall backlog size.

---

### Question 19 (5 points)

The Scrum Guide states that Scrum is designed for single Scrum Teams. Which Scrum Guide principle does both SAFe and LeSS attempt to preserve when scaling to many teams?

- A) The Product Owner must have final authority over the Sprint Backlog
- B) Empiricism — inspection, adaptation, and transparency must remain the foundation for decision-making across all teams and organizational layers
- C) Sprints must be two weeks long regardless of team size or product complexity
- D) The Scrum Master must protect the team from all external interruptions

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Product Owner has authority over the Product Backlog ordering, not the Sprint Backlog. The Sprint Backlog is owned by the Developers. This is not the scaling principle at stake.
  - Why C is incorrect: The Scrum Guide allows Sprint lengths of one to four weeks; it does not mandate two weeks. Sprint length is also not the preservation principle tested by scaling frameworks.
  - Why D is incorrect: Protecting the team from external interference is a Scrum Master behavior; it is not the foundational Scrum principle that scaling frameworks are designed to preserve.

---

### Question 20 (5 points)

A company has 120 developers building a single enterprise product. They adopt LeSS Huge. How does LeSS Huge differ from standard LeSS in its Product Backlog structure?

- A) LeSS Huge creates a separate Product Backlog for each team, eliminating the shared backlog to manage complexity
- B) LeSS Huge divides the Product Backlog into Requirement Areas — large customer-domain slices — each managed by an Area Product Owner, while one overall Product Owner coordinates all areas
- C) LeSS Huge creates a Program Backlog above the Product Backlog, equivalent to SAFe's two-level ownership structure
- D) LeSS Huge eliminates the Product Backlog entirely and replaces it with PI Planning boards

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Separate team backlogs would fragment Product Ownership — the exact problem LeSS is designed to solve. LeSS Huge does not abandon the shared backlog; it organizes it into Requirement Areas.
  - Why C is incorrect: Adding a Program Backlog layer above the Product Backlog describes SAFe's structure, not LeSS. LeSS Huge uses Requirement Areas within the single Product Backlog framework.
  - Why D is incorrect: PI Planning boards are a SAFe tool. LeSS does not use PI Planning or replace the Product Backlog with planning boards.

---
