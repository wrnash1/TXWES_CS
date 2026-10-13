# Video Script: Module 15 — Agile Project Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## SEGMENT 1: Introduction — Why Agile? (0:00–2:30)

[SHOW SLIDE: Module 15 Title Card — Agile Project Management]

Welcome back to CIS-3310. I'm Professor Nash, and today we are covering one of the
most important and most misunderstood topics in modern project management: Agile.

[PAUSE]

Here is the honest truth about Agile: it has become a buzzword. You will walk into
organizations that say they "do Agile" but still have waterfall project plans with
Gantt charts that nobody looks at and status reports that nobody reads. Real Agile
is a fundamentally different mindset, not just a different set of meeting names.

[SHOW SLIDE: The Agile Manifesto — Four Values]

Agile was formalized in 2001 when seventeen software developers gathered in Snowbird,
Utah and produced the Agile Manifesto. It contains four core values:

Individuals and interactions over processes and tools.
Working software over comprehensive documentation.
Customer collaboration over contract negotiation.
Responding to change over following a plan.

[PAUSE]

Notice the manifesto does not say processes and tools are worthless. It does not say
documentation is worthless. It says we value the left side of each statement MORE than
the right side. That distinction matters enormously. Agile is not anti-documentation —
it is pro-working-product.

[SHOW SLIDE: When Agile Works Best]

By the end of this module, you will understand the Scrum framework, Kanban, hybrid
approaches, key differences between Agile and waterfall, sprint planning, and velocity.
These topics are covered on Project+ and are increasingly tested in job interviews for
any IT role.

---

## SEGMENT 2: Agile vs. Waterfall (2:30–6:00)

[SHOW SLIDE: Waterfall vs. Agile — Side by Side]

Let's start with a direct comparison, because understanding the contrast between
waterfall and Agile is essential before we dig into Agile frameworks.

[PAUSE]

Waterfall, which we covered in the first weeks of this course, follows a sequential
lifecycle: requirements, design, build, test, deploy. Each phase must be fully complete
before the next begins. The plan is made upfront. Scope is defined early and controlled
strictly. The customer sees a working product at the end.

The strengths of waterfall are predictability, clear documentation, and defined roles.
The weaknesses are rigidity and late feedback. If requirements change — and they always
change in IT — waterfall projects absorb those changes badly. Change requests pile up.
Budgets inflate. Timelines slip.

[SHOW SLIDE: Agile Lifecycle — Iterative and Incremental]

Agile, by contrast, is iterative and incremental. Instead of delivering everything at
the end, Agile delivers working increments of the product at the end of each short
development cycle called an iteration or sprint. Requirements are not locked upfront —
they are expected to evolve based on feedback from each iteration.

[PAUSE]

The strengths of Agile are adaptability, early value delivery, and continuous feedback.
The weaknesses are that it requires active customer involvement, scope can drift without
discipline, and it can be harder to give fixed-price estimates.

A key concept here is that neither approach is universally superior. The right choice
depends on the nature of the project. Stable, well-defined requirements? Waterfall may
be fine. Evolving requirements and frequent stakeholder feedback? Agile is likely better.

[SHOW SLIDE: Project+ Comparison Table — Waterfall vs. Agile]

For Project+ exam purposes, know these contrasts cold. The exam will present scenarios
and ask you to identify whether waterfall or Agile is more appropriate.

---

## SEGMENT 3: The Scrum Framework (6:00–12:00)

[SHOW SLIDE: Scrum Overview — Roles, Events, Artifacts]

Scrum is the most widely used Agile framework in IT project management. It organizes
work into short fixed-length iterations called sprints, with a clear set of roles,
events, and artifacts.

[PAUSE]

Let's cover the three Scrum roles first.

The **Product Owner** is responsible for the product vision and the product backlog.
The Product Owner represents the customer and stakeholders. They define what needs to
be built and in what priority order. They are the single authority on scope decisions.

The **Scrum Master** is the servant-leader of the Scrum team. The Scrum Master does
not manage the team in the traditional sense — they facilitate Scrum ceremonies, remove
impediments that block the team's progress, and coach the team on Agile practices.
The Scrum Master is not a project manager, even though the roles share some DNA.

The **Development Team** — now called Developers in the 2020 Scrum Guide — is the
cross-functional, self-organizing group that does the actual work. Typically three to
nine people. They pull work from the sprint backlog and are collectively responsible
for the sprint goal.

[SHOW SLIDE: Scrum Events — The Five Ceremonies]

[PAUSE]

Scrum has five events.

**Sprint** — The container event. A fixed time box of one to four weeks, most commonly
two weeks. Every sprint produces a potentially shippable product increment. The sprint
goal does not change mid-sprint.

**Sprint Planning** — Held at the start of each sprint. The team selects items from
the product backlog and commits to a sprint goal. They decompose selected items into
tasks and estimate the work. Output: the sprint backlog.

**Daily Scrum** — A 15-minute time-boxed standup held every day during the sprint.
Each team member answers: What did I complete yesterday? What will I complete today?
Are there any impediments? This is not a status report — it is a coordination meeting.

**Sprint Review** — Held at the end of the sprint. The team demonstrates the working
increment to stakeholders and the Product Owner. Feedback is gathered and the product
backlog is updated. This is the primary customer feedback loop.

**Sprint Retrospective** — Held after the sprint review. The team reflects on their
process, not the product. What went well? What could improve? What will we commit to
changing in the next sprint? Output: improvement actions.

[SHOW SLIDE: Scrum Artifacts — Backlog and Increment]

[PAUSE]

Scrum has three primary artifacts.

The **Product Backlog** is the ordered list of everything needed in the product. It is
managed by the Product Owner and is never fully complete — it evolves throughout the
project. Items in the backlog are called Product Backlog Items or PBIs.

The **Sprint Backlog** is the subset of product backlog items selected for the current
sprint, plus the plan for delivering them. Owned by the development team.

The **Product Increment** is the sum of all completed PBIs from the current sprint plus
all previous sprints. It must meet the team's Definition of Done to count as an increment.

[PAUSE]

The **Definition of Done** — often abbreviated DoD — is a shared understanding of what
"complete" means. Every increment must meet the DoD before it is accepted. Without a
clear DoD, teams ship half-finished work and accumulate technical debt.

---

## SEGMENT 4: Sprint Planning and Velocity (12:00–15:30)

[SHOW SLIDE: Sprint Planning in Depth]

Sprint planning is worth a deeper look because it is where Agile discipline either
takes hold or breaks down.

[PAUSE]

During sprint planning, the team and Product Owner collaborate to answer two questions.
First: what can we deliver this sprint? Second: how will we do it?

The team's answer to the first question is constrained by their capacity and velocity.
Velocity is the average number of story points completed per sprint, measured over
several recent sprints. Story points are a relative effort estimate — not hours, not
days, but a relative unit comparing complexity and risk.

[SHOW SLIDE: Story Points and Velocity Example]

For example, if a team completed 32, 28, 35, and 31 story points over the last four
sprints, their average velocity is approximately 31.5 story points. During sprint
planning, the team should not commit to more than roughly 31–32 story points.

[PAUSE]

Velocity is a planning tool, not a performance metric. Using velocity to pressure teams
to "go faster" destroys the accuracy of the metric because teams will inflate estimates
to make velocity look higher. Use velocity for forecasting, not scorekeeping.

User stories are the most common format for product backlog items in Scrum. A user
story follows this template: "As a [user type], I want [capability] so that [benefit]."
For example: "As a patient, I want to view my lab results online so that I do not need
to call the clinic."

Acceptance criteria are attached to each user story to define when it is done.

---

## SEGMENT 5: Kanban (15:30–18:00)

[SHOW SLIDE: Kanban — Visualize, Limit, Flow]

Kanban is a different flavor of Agile. Where Scrum uses time-boxed sprints, Kanban
uses a continuous flow model. Work items move through columns on a Kanban board —
typically To Do, In Progress, and Done — as capacity allows.

[PAUSE]

The defining feature of Kanban is Work In Progress limits, or WIP limits. Each column
on the board has a maximum number of items allowed at once. If the In Progress column
has a WIP limit of three, no new item can enter until one exits. This forces the team
to finish work before starting new work — a discipline that dramatically reduces
multitasking waste and exposes bottlenecks.

[SHOW SLIDE: Kanban Board Example]

Kanban's metrics include cycle time — how long it takes one item to move from start
to done — and throughput — how many items are completed per time period.

[PAUSE]

Kanban is particularly well-suited for operations and support work where requests
arrive continuously and unpredictably. IT help desks, DevOps pipelines, and
maintenance teams often use Kanban because it does not require organizing work into
fixed sprints.

---

## SEGMENT 6: Hybrid Approaches (18:00–20:30)

[SHOW SLIDE: Hybrid Project Management]

In practice, most organizations do not run pure waterfall or pure Agile. They run
hybrid approaches that borrow elements from both.

[PAUSE]

A common hybrid pattern uses waterfall at the project level — initiation, planning,
and closure phases are formal and document-heavy — while the execution phase uses
Agile sprints. This satisfies governance and financial reporting requirements while
giving the delivery team the flexibility to adapt during execution.

Another hybrid pattern uses Agile for software development while maintaining waterfall
for infrastructure, procurement, and stakeholder reporting. This is common in
organizations that have adopted Agile for development teams but have not yet extended
it to other functions.

[SHOW SLIDE: When to Use Hybrid]

The PMI Agile Practice Guide recommends thinking of the choice between waterfall and
Agile as a spectrum rather than a binary. Most projects land somewhere in the middle.
The right position on the spectrum depends on the project's requirements stability,
team experience with Agile, organizational culture, and stakeholder needs.

[PAUSE]

For Project+ exam purposes, know that hybrid approaches are explicitly recognized and
that the exam may ask you to identify which elements of a described project are waterfall
versus Agile.

---

## SEGMENT 7: Agile PM Roles and Responsibilities (20:30–22:30)

[SHOW SLIDE: Where Does the PM Fit in Agile?]

One question students always ask is: where does the traditional project manager fit
in Agile? The honest answer is that it depends on the framework and the organization.

[PAUSE]

In pure Scrum, there is no role called "project manager." The Scrum Master handles
facilitation, the Product Owner handles scope, and the team is self-organizing. But
in most real organizations, a project manager still exists alongside Scrum teams to
handle budget management, stakeholder reporting, procurement, resource allocation,
and program-level coordination — the things Scrum does not address.

[SHOW SLIDE: Agile PM vs. Traditional PM]

The Agile PM's mindset is different from the traditional PM's mindset. The traditional
PM plans the work upfront and controls against the plan. The Agile PM creates conditions
for the team to succeed, removes impediments, and manages the organizational interface
while the team manages the work.

[PAUSE]

PMI's PMI-ACP certification and the Project+ exam both recognize this evolution. The
exam tests whether you understand Agile values and practices, not just whether you can
name Scrum ceremonies.

---

## SEGMENT 8: Wrap-Up and Exam Alignment (22:30–24:00)

[SHOW SLIDE: Module 15 Key Takeaways]

Let's summarize Module 15.

Agile is a value-based approach rooted in the 2001 Agile Manifesto. Its core values
prioritize working product, collaboration, and adaptability over plan adherence.

Scrum organizes work into sprints with three roles (Product Owner, Scrum Master,
Developers), five events (Sprint, Sprint Planning, Daily Scrum, Sprint Review,
Retrospective), and three artifacts (Product Backlog, Sprint Backlog, Increment).

Velocity is the average story points completed per sprint, used for forecasting.
The Definition of Done defines when work is truly complete.

Kanban uses continuous flow and WIP limits to manage work without sprints.

Hybrid approaches blend waterfall and Agile elements to fit organizational realities.

[PAUSE]

[SHOW SLIDE: Project+ Exam Focus Areas for Module 15]

For Project+ exam prep, focus on Scrum roles and their responsibilities, the purpose
of each Scrum event, the three Scrum artifacts, how velocity is calculated and used,
the difference between Kanban and Scrum, and the characteristics of hybrid approaches.

Your assignments this module include the Scrum Sprint Simulation Lab, a 10-question
quiz, and a discussion forum with three Agile scenarios.

See you in Module 16 — the final module — where we do our comprehensive Project+ exam
preparation and capstone. I'll see you there.

[SHOW SLIDE: End Card — Module 15 Complete]

---

*End of Script — Module 15*

*Total estimated duration: 22–24 minutes*

*Production notes: Scrum event diagram in Segment 3 should animate each ceremony in sprint order.*
*Kanban board in Segment 5 should show a live demo of moving cards with WIP limit enforcement.*
