# Quiz: Module 15 – Software Project Metrics and Velocity Tracking

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Question 1

Management asks a Scrum Master to compare the velocities of three development teams and identify which team is most productive. What should the Scrum Master do?

* A) Calculate each team's average velocity and rank them from highest to lowest as requested.
* B) Ask each team's Product Owner to provide velocity data to ensure accuracy.
* C) Explain that velocity is a team-specific planning tool and is not valid for cross-team productivity comparisons.
* D) Recommend extending all Sprints to one month so velocities are calculated on the same time basis.

Correct Answer: C) Velocity is calibrated per team, per context, and per story point scale — comparing velocities across teams is meaningless and creates pressure to inflate estimates rather than estimate honestly.

Distractor Analysis:

* *Why C is correct:* Different teams size story points differently, work on different problem domains, and have different team compositions. Velocity comparison across teams produces no useful information and incentivizes gaming.
* *Why A is incorrect:* Complying with the request would misuse velocity and damage team trust. The Scrum Master's coaching responsibility requires pushing back on this anti-pattern.
* *Why B is incorrect:* Routing the same invalid request through Product Owners does not fix the underlying misuse — it just adds indirection to a harmful practice.
* *Why D is incorrect:* Standardizing Sprint length does not make cross-team velocity comparison valid. The problem is not timebox length — it is that point scales are not comparable across teams.

---

### Question 2

Which of the following is the most accurate definition of a Sprint Burndown chart?

* A) A chart showing the cumulative number of features released to production over the life of the product.
* B) A chart tracking remaining Sprint Backlog work over the course of the Sprint, ideally trending toward zero by Sprint end.
* C) A quarterly management report showing team velocity trends across multiple Program Increments.
* D) A risk register visualizing technical debt items that threaten the team's ability to complete future Sprints.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* A Sprint Burndown chart shows how much work (in story points or tasks) remains in the Sprint Backlog each day, allowing Developers to inspect whether they are on track to complete their Sprint commitment.
* *Why A is incorrect:* This describes a release or cumulative flow chart, not a Sprint Burndown. Sprint Burndowns track within-Sprint remaining work, not cumulative production releases.
* *Why C is incorrect:* A quarterly management report is not a burndown chart. This description blends velocity reporting with PI-level planning artifacts from SAFe.
* *Why D is incorrect:* A risk register is a project management tool for tracking identified risks — unrelated to Sprint Burndown charts, which track remaining Sprint work.

---

### Question 3

After four Sprints, a team's velocity readings are 15, 40, 16, and 17 story points. What is the most likely explanation for Sprint 2's velocity of 40?

* A) The team permanently improved their engineering practices, and velocity will remain at 40 from now on.
* B) The team worked unsustainable overtime during Sprint 2 or the stories were estimated unusually low, making Sprint 2 an outlier that should not be used as the baseline forecast.
* C) The Product Owner selected easier stories for Sprint 2, which is the appropriate planning approach for raising velocity.
* D) Velocity of 40 means the team should commit to 40 story points every Sprint to maximize stakeholder value.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* A single Sprint that is 2–3× the team's typical velocity is almost always an anomaly — caused by overtime, underestimated stories, or unusual conditions. Using it as a planning baseline would lead to chronic over-commitment and missed Sprint Goals.
* *Why A is incorrect:* A one-Sprint spike does not represent a permanent capability improvement. Sustainable velocity improvement happens gradually through process and technical improvements, not as a sudden doubling.
* *Why C is incorrect:* Deliberately selecting underestimated stories to inflate velocity is "velocity gaming" — it makes the number look bigger without delivering more actual value.
* *Why D is incorrect:* Committing to an outlier velocity rather than average velocity sets the team up for failure. Sprint commitments should be based on stable average velocity, not a single exceptional Sprint.

---

### Question 4

The Scrum Guide prescribes which of the following as a required artifact for tracking Sprint progress?

* A) Sprint Burndown chart — required to be updated daily by the Scrum Master
* B) Release Burndown chart — required to be maintained by the Product Owner
* C) Neither — the Scrum Guide does not prescribe specific progress tracking artifacts; the team chooses their own tools
* D) Cumulative Flow Diagram — required for teams with more than five Developers

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* The Scrum Guide does not prescribe burndown charts or any other specific progress visualization. Teams are free to use whatever tracking tools support their transparency and inspection needs.
* *Why A is incorrect:* The Scrum Guide does not require Sprint Burndown charts or assign their maintenance to the Scrum Master. Using one is a team choice, not a Scrum rule.
* *Why B is incorrect:* The Scrum Guide does not require Release Burndown charts. The Product Owner manages the Product Backlog and can use any visualization that helps track progress toward the Product Goal.
* *Why D is incorrect:* Cumulative Flow Diagrams are a Kanban tool. The Scrum Guide does not require them and does not condition their use on team size.

---

### Question 5

A team's velocity has been consistently 20 story points per Sprint for six Sprints. The Product Backlog contains 100 story points of remaining work. The Product Owner needs to know when the product will be ready for release. What is the most accurate forecast?

* A) The product cannot be released until all 100 story points are complete, which will take exactly 5 Sprints with no variance.
* B) At 20 points per Sprint, approximately 5 Sprints are needed, but actual completion may vary because velocity fluctuates and the backlog evolves.
* C) The team needs to increase velocity to 25 points per Sprint to meet a 4-Sprint release target.
* D) Velocity cannot be used for release forecasting; the Product Owner should ask the Scrum Master to create a Gantt chart instead.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* 100 ÷ 20 = 5 Sprints is the forecast, but it is probabilistic, not deterministic. Velocity fluctuates, the Product Owner may add or remove backlog items, and the Definition of Done may change — all affecting actual completion.
* *Why A is incorrect:* Saying "exactly 5 Sprints with no variance" overstates the precision of a velocity-based forecast. Forecasts are probabilistic estimates, not guarantees.
* *Why C is incorrect:* The Product Owner cannot mandate that the team increase velocity. Developers set their own capacity; the Product Owner responds to actual velocity when making release decisions.
* *Why D is incorrect:* Velocity is a standard and valid Agile forecasting tool. A Gantt chart is a Waterfall project management artifact that imposes false precision on evolving Agile delivery timelines.
