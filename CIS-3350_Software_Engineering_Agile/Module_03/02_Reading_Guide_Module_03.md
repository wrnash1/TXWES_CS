# Reading Guide: Module 03 – Scrum Framework: Roles, Events, Artifacts

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

This module covers the complete Scrum framework as defined in the 2020 Scrum Guide. The Scrum framework is the primary subject matter of the PSM I certification exam — every question on the exam tests your understanding of how Scrum works and why it is designed the way it is. This reading guide is your reference document for the framework's structure, language, and rationale.

The 2020 Scrum Guide is the authoritative source. It is free at scrum.org and is approximately 13 pages. You should read it in full before taking the PSM I exam. This guide supplements — but does not replace — that reading.

---

## 1. What Scrum Is (and Is Not)

The Scrum Guide defines Scrum as a lightweight framework that helps people, teams, and organizations generate value through adaptive solutions for complex problems. Key terms:

- Lightweight: Scrum is intentionally minimal. It prescribes exactly three accountabilities, five events, three artifacts, and a small number of rules. Everything else is left to the team.
- Framework: Scrum is not a methodology (a complete, prescriptive process). It is a framework within which teams use various techniques and practices. The Scrum Guide does not tell you how to write code, how to test, or how to design architecture.
- Adaptive: Scrum is built for environments where the work cannot be fully planned upfront. It assumes the future is uncertain and creates mechanisms for continuous adjustment.
- Complex problems: Scrum is designed for the complex domain — where cause and effect are only understood in retrospect and empirical process control is required.

What Scrum is not: Scrum is not a project management methodology, not a software development methodology, and not a set of engineering practices. It is a team operating framework.

---

## 2. The Scrum Team

The Scrum Team consists of one Product Owner, one Scrum Master, and Developers.

Key characteristics:

- No sub-teams or hierarchies within a Scrum Team
- Cross-functional: collectively possesses all skills needed to create value each Sprint
- Self-managing: the team decides internally who does what, when, and how
- Optimal size: typically 10 or fewer people
- Accountable to stakeholders and the organization for creating a valuable, useful Increment each Sprint

---

## 3. The Three Accountabilities — Reference Table

| Accountability | Primary Responsibility | Owns | Does NOT Do |
|---|---|---|---|
| Product Owner | Maximize product value | Product Backlog, Product Goal | Assign tasks to Developers, manage day-to-day work |
| Scrum Master | Team effectiveness, Scrum adoption | Process coaching, impediment removal | Assign work, report to management on individual performance, make product decisions |
| Developers | Create the Increment | Sprint Backlog, Definition of Done adherence | Receive work assignments from Scrum Master or managers |

### Product Owner Deep Dive

The Product Owner is one person, not a committee. Key accountabilities:

- Developing and explicitly communicating the Product Goal
- Creating and clearly communicating Product Backlog items
- Ordering Product Backlog items
- Ensuring the Product Backlog is transparent, visible, and understood

The Product Owner may delegate these activities to others, but they remain accountable for the results. If a stakeholder wants to change the Product Backlog, they must convince the Product Owner.

### Scrum Master Deep Dive

The Scrum Master serves the Scrum Team by coaching team members in self-management and cross-functionality, helping focus on creating high-value Increments, removing impediments to progress, and ensuring all Scrum events take place and are positive, productive, and kept within the timebox.

The Scrum Master serves the Product Owner by helping find techniques for effective Product Goal definition and Product Backlog management, helping establish empirical product planning, and facilitating stakeholder collaboration.

The Scrum Master serves the organization by leading, training, and coaching in Scrum adoption, planning and advising Scrum implementations, and helping employees and stakeholders understand and enact Scrum.

### Developers Deep Dive

The Developers create a plan for the Sprint (Sprint Backlog), instill quality by adhering to a Definition of Done, adapt the plan each day toward the Sprint Goal, and hold each other accountable as professionals.

---

## 4. The Five Scrum Events — Sprint Timebox Table

| Event | Purpose | Timebox (1-month Sprint) | Who Attends |
|---|---|---|---|
| Sprint | Container for all other events; produces Increment | 1 week to 1 month | Entire Scrum Team |
| Sprint Planning | Define Sprint Goal, select backlog items, create plan | 8 hours maximum | Entire Scrum Team |
| Daily Scrum | Inspect progress toward Sprint Goal, adapt Sprint Backlog | 15 minutes | Developers (others may observe) |
| Sprint Review | Inspect Increment, gather feedback, update Product Backlog | 4 hours maximum | Scrum Team and stakeholders |
| Sprint Retrospective | Inspect team process, create improvement plan | 3 hours maximum | Entire Scrum Team |

### Sprint

The Sprint is the heartbeat of Scrum. Key rules:

- Fixed length: 1 week to 1 month; consistent throughout product development
- No changes are made that would endanger the Sprint Goal
- Quality does not decrease
- The Product Backlog is refined as needed
- Scope may be clarified and renegotiated with the Product Owner as more is learned
- Only the Product Owner can cancel a Sprint, and only if the Sprint Goal becomes obsolete

### Sprint Planning

Sprint Planning creates the Sprint Backlog and Sprint Goal by answering three questions:

1. Why is this Sprint valuable? (Product Owner proposes, team collaborates to define Sprint Goal)
2. What can be Done this Sprint? (Developers select items from Product Backlog)
3. How will the chosen work get done? (Developers plan the work, decomposing items into tasks of one day or less)

### Daily Scrum

The Daily Scrum is 15 minutes for Developers. It is held at the same time and place each working day. Its purpose is to inspect progress toward the Sprint Goal and adapt the Sprint Backlog. The Scrum Guide no longer mandates the three-question format — the structure is up to the team, as long as it focuses on the Sprint Goal.

### Sprint Review

The Sprint Review is a working session — not a presentation or status report. The Scrum Team demonstrates the Increment and gathers stakeholder feedback. The Product Backlog may be adjusted. The output is an updated Product Backlog.

### Sprint Retrospective

The Sprint Retrospective inspects: individuals, interactions, processes, tools, and the Definition of Done. It produces a plan of at least one high-priority process improvement for the next Sprint. The Scrum Guide says the most impactful improvements may be added to the Sprint Backlog for the next Sprint.

---

## 5. The Three Artifacts and Their Commitments

| Artifact | Definition | Commitment |
|---|---|---|
| Product Backlog | Emergent, ordered list of everything needed in the product | Product Goal |
| Sprint Backlog | Sprint Goal + selected PBIs + plan for the Sprint | Sprint Goal |
| Increment | Concrete stepping stone toward Product Goal; must be Done | Definition of Done |

### Product Backlog

The Product Backlog is never complete. It is dynamic — as the product and market evolve, the Product Backlog evolves. Product Backlog items have the following attributes: description, order, size (estimate), and value. The Product Owner is responsible for the Product Backlog, but Developers add size estimates.

Product Backlog Refinement is the act of breaking down and further defining Product Backlog items into smaller, more precise items. This is an ongoing activity and typically consumes no more than 10% of the Developers' capacity.

### Sprint Backlog

The Sprint Backlog belongs to the Developers. It is a real-time picture of the work planned for the Sprint. It is updated throughout the Sprint as the Developers learn more. The Sprint Goal is the single objective for the Sprint — it creates coherence and allows flexibility in exactly what work is done.

### Increment

An Increment is a concrete stepping stone toward the Product Goal. Each Increment is additive to all prior Increments. Multiple Increments may be created within a Sprint. An Increment must be usable before it can be released — the Product Owner decides whether to release it.

### Definition of Done

The Definition of Done (DoD) is a formal description of the quality state an Increment must reach. If a Product Backlog item does not meet the DoD, it cannot be included in the Sprint Review as a Done Increment. The DoD creates transparency and shared understanding of what "done" means.

If the organization has a standard DoD, the Scrum Team must comply with it as a minimum. The team may adopt a stricter DoD.

---

## 6. Scrum Values

The 2020 Scrum Guide emphasizes five Scrum values that enable successful Scrum practice:

- Commitment: Scrum Team members personally commit to achieving their goals and supporting each other
- Focus: Their primary focus is the work of the Sprint to make the best possible progress toward these goals
- Openness: The Scrum Team and stakeholders are open about the work and challenges
- Respect: Scrum Team members respect each other as capable, independent people
- Courage: Scrum Team members have the courage to do the right thing and work on tough problems

These values provide the foundation of trust that makes empirical process control possible.

---

## 7. PSM I Exam Tips

Tip 1: The 2020 Scrum Guide uses "accountabilities" not "roles." Using "roles" in an exam answer is not wrong, but knowing the Guide's exact language demonstrates deeper familiarity.

Tip 2: Know the exact timeboxes: Sprint Planning 8h, Daily Scrum 15 min, Sprint Review 4h, Sprint Retrospective 3h — all for one-month Sprints. Shorter Sprints have proportionally shorter events.

Tip 3: The Daily Scrum is for Developers. The Scrum Master does not run it; they ensure it happens. The Product Owner does not attend unless they are also serving as a Developer (which the Scrum Guide permits in small teams).

Tip 4: Only the Product Owner can cancel a Sprint. Not the Scrum Master. Not the Developers. Not a manager. Only the Product Owner.

Tip 5: The Sprint Review is not a status meeting or a demo for approval. It is an inspection and adaptation event. The output is an updated Product Backlog, not approval to ship.

Tip 6: The Sprint Retrospective focuses on the team's process, not on the product. The Sprint Review focuses on the product Increment. These two events are often confused on the exam.

Tip 7: The Definition of Done is not the same as acceptance criteria. Acceptance criteria are specific to individual Product Backlog items. The Definition of Done applies to every Increment.

Tip 8: Scrum does not prescribe engineering practices (unit testing, CI/CD, pair programming). These may be included in the Definition of Done, but Scrum itself does not mandate them.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 03 topics:

**1. The 2020 Scrum Guide — Scrum.org (Full Text)**
<https://scrumguides.org/scrum-guide.html>
Every PSM I question is grounded in this document. For Module 03, focus on the "Scrum Team," "Scrum Events," "Scrum Artifacts," and "Scrum Values" sections. The guide is free and approximately 13 pages — there is no substitute for reading it directly.

**2. Scrum Open Assessment — Scrum.org**
<https://www.scrum.org/open-assessments/scrum-open>
A free, official 30-question practice assessment from Scrum.org that mirrors the PSM I exam format. Questions are drawn from the Scrum Guide. Aim for a score above 85% before sitting the actual PSM I exam. Unlimited free attempts.

**3. "Scrum: The Art of Doing Twice the Work in Half the Time" — Jeff Sutherland (Overview)**
<https://www.scruminc.com/scrum-the-art-of-doing-twice-the-work-in-half-the-time/>
The companion overview page for Sutherland's book, co-written by a Scrum co-creator. The page contains free excerpts and background on why Scrum was designed the way it was. Understanding the design rationale helps answer "why" questions on the PSM I exam that go beyond rules memorization.

---

## 8. Study Checklist

- [ ] Draw the complete Scrum framework diagram from memory (accountabilities, events, artifacts, timeboxes, commitments)
- [ ] State the responsibility of each accountability in two sentences
- [ ] Recite the timebox for all five events (for a one-month Sprint)
- [ ] Explain the commitment associated with each of the three artifacts
- [ ] Explain the difference between the Sprint Review and the Sprint Retrospective
- [ ] Explain what the Definition of Done is, and what happens to a PBI that does not meet it
- [ ] State the five Scrum values from memory
- [ ] Read the complete 2020 Scrum Guide at scrum.org before taking the Module 03 quiz
- [ ] Complete the Module 03 Lab (Scrum Framework Diagram fill-in exercise)

---
