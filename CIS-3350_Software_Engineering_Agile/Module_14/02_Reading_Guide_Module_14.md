# Reading Guide: Module 14 — Scaled Agile: SAFe and LeSS Overview

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

Single-team Scrum scales naturally to small products. When a product requires multiple teams working in parallel, coordination challenges emerge that the Scrum Guide does not directly address. Scaling frameworks provide structures and practices to extend Scrum's values across many teams. This module covers the two most prominent scaling frameworks — SAFe (Scaled Agile Framework) and LeSS (Large-Scale Scrum) — with enough depth to compare them intelligently and apply their concepts on the PSM I exam.

---

## 1. The Scaling Problem

Before studying the frameworks, understand the challenges they solve.

### Why Single-Team Scrum Doesn't Scale Directly

| Challenge | Description | Consequence |
|-----------|-------------|-------------|
| Integration | Multiple teams' Increments must combine into a single shippable product | Risk of integration failures at Sprint end if teams haven't coordinated |
| Dependencies | Team A's Sprint goal may require work that only Team B can deliver | Blocked teams, missed Sprint goals, cascading delays |
| Product Ownership | One Product Owner cannot maintain deep backlog understanding across 8 teams | Prioritization gaps, conflicting team directions |
| Architecture alignment | Parallel development without architectural coordination creates technical debt and incompatibility | Rework, increased coupling, slowed delivery |
| Strategy alignment | Independent Sprint teams may optimize locally while missing shared organizational objectives | Teams deliver value that doesn't combine into business outcomes |

### What Scaling Frameworks Provide

All scaling frameworks address these challenges through some combination of:

- Synchronized planning events that coordinate multiple teams
- Shared backlog structures with layers for team-level and program-level work
- Role definitions for coordination above the team level
- Coordination mechanisms during the execution period (Sprints/Iterations)
- Shared cadences so teams can integrate regularly

---

## 2. SAFe — The Scaled Agile Framework

### Core Concept

SAFe organizes multiple teams into an Agile Release Train (ART) — a group of five to twelve teams that plan, commit, develop, and release together on a synchronized cadence. The ART is the primary value delivery unit in SAFe.

### Program Increment

The Program Increment (PI) is SAFe's most important concept. A PI is a timebox — typically ten to twelve weeks — consisting of five to six two-week Iterations (Sprints) plus an Innovation and Planning (IP) Iteration at the end.

| PI Component | Description |
|-------------|-------------|
| PI Planning | Two-day event at PI start; all ART teams plan Iterations, identify dependencies, commit to PI Objectives |
| Iterations 1–5 | Two-week Sprints; teams execute against their PI Objectives |
| System Demo | End-of-PI demo of the integrated work from all teams |
| Inspect and Adapt | PI Retrospective and problem-solving workshop for the ART |
| IP Iteration | Final iteration reserved for testing, tech debt, exploration, and next PI Planning prep |

### PI Planning

PI Planning is SAFe's primary coordination event. All teams attend — either in person or via video conference. During PI Planning:

- Business context is presented (Product Management explains strategic themes)
- Teams review the Program Backlog and plan their Iterations
- Teams identify cross-team dependencies and negotiate handoffs
- Teams draft PI Objectives — the business outcomes they commit to deliver in the PI
- Risks are identified and assigned to the ART's risk board (ROAM: Resolved, Owned, Accepted, Mitigated)

### SAFe Roles

| SAFe Role | Equivalent To | Responsibility |
|-----------|--------------|----------------|
| Product Manager | Program-level Product Owner | Owns the Program Backlog; defines features and PI Objectives |
| Release Train Engineer (RTE) | Scrum Master for the ART | Facilitates PI Planning, Inspect and Adapt; removes ART-level impediments |
| System Architect / Engineer | Technical leadership | Guides technical architecture across all ART teams |
| Team Product Owner | Scrum Team Product Owner | Owns the Team Backlog; breaks features into stories for their team |
| Scrum Master | Scrum Team Scrum Master | Serves their individual team as defined in the Scrum Guide |

### SAFe Key Terms

- Agile Release Train (ART): the multi-team delivery unit
- Feature: a unit of work at the program level (above stories, below epics)
- PI Objective: a business outcome a team or ART commits to in a PI
- Innovation and Planning Iteration: the non-feature Iteration at PI end
- ROAM: a risk management tool used during PI Planning

---

## 3. LeSS — Large-Scale Scrum

### LeSS Core Concept

LeSS extends Scrum to multiple teams by keeping Scrum's structure as intact as possible. The fundamental LeSS design principle is: one Product Owner, one Product Backlog, multiple teams, one Sprint.

### LeSS Structure

| Scrum Element | LeSS Treatment |
|--------------|----------------|
| Product Owner | One PO for all teams; owns the single Product Backlog |
| Product Backlog | One shared Backlog; all teams select items from the same source |
| Sprint | One Sprint for all teams, starting and ending simultaneously |
| Sprint Planning | Part 1: all teams together with PO to clarify items; Part 2: each team individually plans how |
| Sprint Review | One review, all teams demonstrate integrated work to PO and stakeholders |
| Sprint Retrospective | Each team holds their own; plus an optional overall Retrospective |
| Daily Scrum | Each team runs their own Daily Scrum |

### LeSS Feature Teams

In LeSS, all teams are feature teams — cross-functional teams capable of taking a customer-facing feature from the Product Backlog through development and testing end-to-end. Feature teams avoid component ownership (where Team A owns the database layer and Team B owns the UI) because component ownership creates dependencies and handoffs.

### LeSS Coordination Mechanisms

LeSS adds minimal coordination structure:

- Scrum of Scrums: optional; one representative per team discusses cross-team integration and dependency issues
- Multi-team Sprint Planning: the Part 1 Sprint Planning is held with all teams and the PO together
- Shared Sprint Review: all teams demonstrate to stakeholders in a shared event
- Communities of Practice: informal cross-team groups for specialists (architects, testers) to coordinate technical standards

### LeSS Huge

For organizations exceeding eight teams, LeSS Huge divides the Product Backlog into Requirement Areas — large customer-centric domain slices. Each Requirement Area has an Area Product Owner (APO). There is still one overall Product Owner who coordinates the APOs. The team structure does not change — teams remain feature teams selecting from their Requirement Area's backlog.

---

## 4. SAFe vs. LeSS Comparison

| Dimension | SAFe | LeSS |
|-----------|------|------|
| Philosophy | Prescriptive; provides complete organizational blueprint | Principled; minimal additions to Scrum |
| Product Ownership | Two levels: Product Manager (program) + Team PO | One Product Owner for all teams |
| Backlog structure | Program Backlog (features) + Team Backlog (stories) | One Product Backlog for all teams |
| Planning cadence | PI Planning every 10–12 weeks + Sprint-level planning | Sprint-level planning only (shared across all teams) |
| Team type | May include component teams | Feature teams only |
| Coordination overhead | High — PI Planning, ART Sync, System Demo | Low — Scrum of Scrums, shared Sprint events |
| Organizational disruption | Lower — fits existing hierarchy; adds coordination roles | Higher — challenges component team structure and middle management |
| PSM I emphasis | PI Planning, PI Objectives, ART structure | One PO/Backlog, feature teams, LeSS Huge Requirement Areas |

---

## 5. Scrum Values at Scale

Both SAFe and LeSS claim to preserve Scrum's values. The PSM I perspective on scaling is grounded in whether the framework supports or undermines empiricism.

Empiricism at scale requires:

- Transparency: the state of work across all teams must be visible. PI Planning boards (SAFe) and shared Product Backlogs (LeSS) both support this.
- Inspection: teams and the organization must regularly inspect the integrated Increment and their processes. System Demo (SAFe) and shared Sprint Review (LeSS) both provide this.
- Adaptation: teams and the ART/organization must be able to adjust based on what inspection reveals. Inspect and Adapt (SAFe) and multi-team Retrospectives (LeSS) provide this.

Where scaling frameworks fail, it is usually because coordination overhead consumes the capacity for inspection and adaptation — teams are too busy managing dependencies to inspect what they are actually producing.

---

## 6. PSM I Exam Tips

Tip 1: The PSM I does not test SAFe or LeSS in detail. It tests whether candidates understand why Scrum scales the way it does — the values, empiricism, and team structure principles that any scaling approach must preserve.

Tip 2: Know PI Planning by name and purpose. SAFe's PI Planning is frequently referenced in exam scenarios about multi-team coordination. It is a synchronous planning event where all ART teams plan together, surface dependencies, and commit to PI Objectives.

Tip 3: LeSS's defining characteristic is one Product Owner and one Product Backlog for all teams. When an exam scenario describes multiple teams with fragmented Product Ownership and multiple Backlogs, that is the antithesis of the LeSS philosophy.

Tip 4: The scaling problem is not primarily technical — it is organizational. Dependencies between teams often exist because the architecture forces them, not because scaling is inherently complex. Both SAFe and LeSS ultimately acknowledge this.

Tip 5: Feature teams (LeSS) versus component teams (common in SAFe and traditional organizations) is an important distinction. Feature teams reduce dependencies; component teams create handoffs that must be coordinated.

Tip 6: Neither SAFe nor LeSS is mentioned in the Scrum Guide. The Scrum Guide describes a single Scrum Team. SAFe and LeSS are external frameworks built on Scrum.

Tip 7: Sprint velocity at scale must be understood carefully. Multi-team velocity is the sum of team velocities only if all team Increments integrate without integration costs. Integration failures reduce effective velocity across the ART.

Tip 8: The Scrum Master's role expands in scaling contexts. In SAFe, the Release Train Engineer fulfills a Scrum Master function at the ART level. In LeSS, Scrum Masters may serve multiple teams and facilitate multi-team events.

---

## 7. Study Checklist

- [ ] Describe the five scaling challenges that single-team Scrum cannot address directly
- [ ] Explain what an Agile Release Train is and how many teams it typically contains
- [ ] Describe the Program Increment structure and the purpose of PI Planning
- [ ] Name the SAFe roles at the program level and their responsibilities
- [ ] Explain the LeSS principle of one Product Owner and one Product Backlog
- [ ] Describe what a feature team is and why LeSS requires them
- [ ] Compare SAFe and LeSS on product ownership, backlog structure, and coordination overhead
- [ ] Connect both frameworks to Scrum's three pillars of empiricism
- [ ] Complete this module's Lab and Quiz

---
