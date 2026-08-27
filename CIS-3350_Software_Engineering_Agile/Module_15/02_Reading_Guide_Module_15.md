# Reading Guide: Module 15 — Software Project Metrics and Velocity Tracking

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

Metrics in Scrum serve empiricism — they make the team's progress and the system's behavior transparent, support meaningful inspection, and enable informed adaptation. This module covers the primary metrics used by Scrum teams: velocity, Sprint and Release Burndown Charts, flow metrics (lead time, cycle time), and the Cumulative Flow Diagram. It also addresses metric anti-patterns that undermine team performance when metrics are used as management instruments rather than team tools.

---

## 1. Velocity

### Definition

Velocity is the sum of story points (or other estimation units) from Product Backlog Items that met the Definition of Done during a Sprint. Only items that are fully done count — a story that is 80 percent complete at Sprint end contributes zero to velocity.

### Calculation Example

| Story | Estimate (points) | Status at Sprint End | Contribution |
|-------|-------------------|---------------------|--------------|
| Login feature | 5 | Done | 5 |
| Password reset | 3 | Done | 3 |
| Profile edit | 8 | Done | 8 |
| Email notifications | 5 | In progress — not done | 0 |
| Dashboard redesign | 13 | Not started | 0 |
| **Sprint Velocity** | | | **16** |

### Legitimate Uses of Velocity

- Sprint planning: use the average of the last three Sprints' velocity to forecast how much to plan
- Release forecasting: divide remaining backlog points by average velocity to estimate Sprints remaining
- Team trend monitoring: inspect velocity trend in Retrospectives to identify systemic issues

### Velocity Limitations

- Velocity is team-specific: story point scales are relative to each team's calibration. Cross-team comparison is meaningless and harmful.
- Velocity fluctuates naturally: team composition changes, Sprint length variations, holidays, and bug influx all affect velocity. A single low-velocity Sprint is not a signal of team failure.
- Velocity does not measure value: a team can have high velocity while delivering stories that do not address the Sprint Goal or business priority.

---

## 2. Sprint Burndown Chart

### Sprint Burndown Definition

A Sprint Burndown Chart plots remaining Sprint Backlog work (in story points or hours) against the days of the Sprint. It answers: is the team on track to complete the Sprint Backlog?

### Reading a Sprint Burndown

| Element | Description |
|---------|-------------|
| X-axis | Sprint days (day 1 through Sprint end day) |
| Y-axis | Remaining work in story points |
| Ideal line | Diagonal line from total Sprint points to zero at Sprint end |
| Actual line | Real remaining work updated daily |

### Common Burndown Patterns and What They Indicate

| Pattern | Description | Likely Cause |
|---------|-------------|--------------|
| Flat then sharp drop | Actual line stays near original total, then drops steeply in last two days | Developers batch completion; stories not being broken into daily-completable units |
| Consistently above ideal | Actual line remains above ideal throughout Sprint | Overcommitment; team planned more than velocity supports |
| Steps rather than slope | Line drops in large jumps rather than steadily | Stories are too large; decomposition needed |
| Early completion | Actual line reaches zero before Sprint end | Undercommitment; team could take more work into Sprint |
| Line goes up mid-Sprint | Remaining work increases during Sprint | Scope was added to Sprint Backlog, or stories were re-estimated upward |

### The Burndown as an Empirical Tool

The Sprint Burndown is a team tool for self-management, not a management reporting tool. Teams inspect it during the Daily Scrum to assess whether they need to renegotiate scope with the Product Owner. When the actual line diverges significantly from the ideal line, the team adapts — either by removing lower-priority stories from the Sprint or by asking the Product Owner to clarify priority.

---

## 3. Release Burndown Chart

### Release Burndown Definition

The Release Burndown Chart plots remaining Product Backlog work across multiple Sprints. It communicates the product's release trajectory to stakeholders.

### Elements

- X-axis: Sprints in the release
- Y-axis: Remaining story points in the Product Backlog
- The line descends as Sprints are completed; it rises when new items are added to the backlog

### Scope Changes on the Release Burndown

Unlike the Sprint Burndown, the Release Burndown frequently shows the line rising as well as falling. This reflects the reality of Agile development: the Product Owner continuously adds, removes, and repriorizes the backlog. A rising line in the Release Burndown is not a failure — it is transparency about scope growth. When stakeholders ask "why isn't the line going down faster?" the Product Owner can show exactly which new items raised the line.

### Using Release Burndown for Forecasting

If the Release Burndown shows 240 remaining points and the team's average velocity is 30 points per Sprint, the forecast is 8 more Sprints. If the release target is 6 Sprints away, the Product Owner must make a decision: reduce scope, extend the release date, or add capacity. The Release Burndown makes this decision visible and evidence-based.

---

## 4. Flow Metrics

### Lead Time and Cycle Time

| Metric | Measured From | Measured To | What It Reveals |
|--------|--------------|-------------|-----------------|
| Lead time | Item added to backlog | Item delivered to production | Total customer wait time |
| Cycle time | Team begins work on item | Item delivered | Team execution efficiency |
| Queue time | Item added to backlog | Team begins work | How long items wait before being worked on |

The relationship: Lead Time = Cycle Time + Queue Time

### Little's Law

Little's Law: Average Cycle Time = Work in Progress ÷ Throughput

This formula reveals why WIP limits improve flow. Holding throughput constant, reducing WIP directly reduces average cycle time. Scrum teams apply this by not overloading Sprint Backlogs — too many stories in flight simultaneously extend every story's individual cycle time.

### Cumulative Flow Diagram (CFD)

The CFD shows the number of items in each workflow stage (Backlog, In Progress, Testing, Done) over time as stacked area bands.

| CFD Pattern | Interpretation |
|-------------|---------------|
| Widening band in one stage | Bottleneck: items are accumulating in that stage faster than they are leaving |
| All bands stable width | Smooth flow: items move through stages at balanced rates |
| Large gap between In Progress and Done bands | Long cycle time: items started but not finishing |
| Narrow In Progress band with wide Done band | High throughput and good flow efficiency |

---

## 5. Metric Anti-Patterns

Anti-patterns are metric uses that appear reasonable but actively harm team performance or organizational trust.

| Anti-Pattern | Description | Consequence |
|-------------|-------------|-------------|
| Comparing velocity across teams | Using team A's velocity of 40 to judge team B's velocity of 25 | Teams inflate estimates to appear competitive; velocity numbers become meaningless |
| Velocity as management target | Manager sets "velocity must reach 50 by Q3" | Teams inflate estimates to hit the number; actual output does not increase |
| Individual velocity tracking | Measuring each developer's story point contribution | Destroys collaboration; developers guard work instead of helping others |
| 100% utilization management | Expecting every developer to be fully productive every hour | Eliminates slack needed for quality, learning, and interruption absorption |
| Lines of code as productivity | Measuring output in lines written or committed | Incentivizes verbose code over simple code; refactoring appears as negative productivity |
| Burndown as status report | Using burndown charts as management performance reports | Teams optimize the chart (batch work to end of Sprint) rather than the work |

---

## 6. Metrics and Scrum

### Which Scrum Artifact Contains Metrics?

The Scrum Guide does not prescribe specific metrics. The artifacts — Product Backlog, Sprint Backlog, and Increment — each have commitments (Product Goal, Sprint Goal, Definition of Done) but no required metrics. Teams choose metrics that serve their empirical process.

### Connecting Metrics to Scrum Events

| Metric | Most Relevant Scrum Event | How It Supports the Event |
|--------|--------------------------|---------------------------|
| Velocity | Sprint Planning | Team uses recent velocity to forecast how much to plan |
| Sprint Burndown | Daily Scrum | Team inspects daily to identify if adaptation is needed |
| Release Burndown | Sprint Review | Product Owner and stakeholders inspect release trajectory |
| Lead time / Cycle time | Sprint Retrospective | Team identifies process improvements to reduce cycle time |
| CFD | Sprint Retrospective | Team identifies bottlenecks in workflow stages |

---

## 7. PSM I Exam Tips

Tip 1: The Scrum Guide does not define velocity or prescribe any specific metric. When exam questions describe metrics, evaluate them against whether they support or undermine empiricism and self-management.

Tip 2: Velocity is a forecasting tool, not a productivity measure. When an exam scenario describes using velocity to evaluate developer performance, compare teams, or set organizational targets, the correct response is that this misuses velocity.

Tip 3: A Sprint Burndown that shows the actual line consistently above the ideal line indicates overcommitment — the team planned more than their velocity supports. The adaptation is to improve Sprint Planning calibration.

Tip 4: Little's Law (Cycle Time = WIP / Throughput) explains why reducing WIP improves flow. This connects Kanban (Module 9) to Scrum metrics — the same insight applies at the story level in Sprint Backlogs.

Tip 5: The Release Burndown line rising does not indicate failure — it indicates that the Product Owner is continuously managing scope. This is expected and healthy in Agile development.

Tip 6: Metrics that measure individual developer output (commits, lines of code, story points assigned) are inconsistent with Scrum's team model. Scrum Teams are self-organizing collective units; individual attribution metrics undermine collaboration.

Tip 7: The Cumulative Flow Diagram is the primary visualization for identifying bottlenecks. A widening band in one stage is the signal. This connects to Lean's value stream mapping from Module 9.

Tip 8: Metrics serve the team's self-management. When metrics serve management control instead, they create the perverse incentives that destroy what they are supposed to measure.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 15 topics:

**1. "Velocity" — Mountain Goat Software (Mike Cohn)**
<https://www.mountaingoatsoftware.com/blog/know-exactly-what-velocity-means-to-your-scrum-team>
A free blog post from Mike Cohn clarifying what velocity is, what it is not, and the most common misuses. Directly addresses the anti-patterns of cross-team comparison and velocity as a management target. Relevant to the lab's metric anti-pattern analysis tasks.

**2. "Little's Law Applied to Agile Development" — Agile Alliance**
<https://www.agilealliance.org/resources/experience-reports/littles-law-applied-to-agile-development/>
A free Agile Alliance article that applies Little's Law to software development teams with worked numerical examples. Explains how WIP limits reduce cycle time using the same math covered in this module. Particularly useful for the flow metrics and CFD analysis tasks in Part 3 of the lab.

**3. "Cumulative Flow Diagrams" — Agile Alliance Glossary**
<https://www.agilealliance.org/glossary/cfd/>
A free reference entry explaining Cumulative Flow Diagrams — how to read them, what widening bands indicate, and how to use CFDs to identify bottlenecks. Includes example diagrams showing healthy flow versus bottleneck patterns, directly supporting the visual interpretation skills required for this module.

---

## 8. Study Checklist

- [ ] Define velocity and calculate it from a sample Sprint scenario
- [ ] Describe the three legitimate uses of velocity
- [ ] Read a Sprint Burndown chart and explain what deviation patterns indicate
- [ ] Describe the Release Burndown and explain why the line sometimes rises
- [ ] Define lead time, cycle time, and queue time and explain the relationship between them
- [ ] State Little's Law and explain its implication for Sprint Backlog size
- [ ] Identify at least four metric anti-patterns and explain the consequence of each
- [ ] Connect Sprint Burndown, velocity, and lead time to specific Scrum events
- [ ] Complete this module's Lab and Quiz

---
