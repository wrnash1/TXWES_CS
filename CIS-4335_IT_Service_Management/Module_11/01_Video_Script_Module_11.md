# Video Script: Module 11 — Continual Improvement

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: ITIL 4 Foundation

---

## Introduction (0:00–1:30)

Welcome to Module 11. I'm Professor Nash, and today's topic is the one that ties
everything else together: **Continual Improvement**.

Think about everything we have covered so far. The Service Value Chain. Service Level
Management. Incident, Problem, and Change Management. Each of those practices generates
data, lessons learned, and opportunities. Continual Improvement is the practice that
captures those opportunities and turns them into structured, prioritized action.

ITIL 4 treats continual improvement not as an occasional audit or annual review — it
treats it as a permanent organizational capability. It is woven into the Service Value
Chain itself through the Improve activity. It is embedded in every practice. And it is
supported by a seven-step model that gives organizations a repeatable approach for making
things better.

[SHOW DIAGRAM: Continual improvement embedded in all SVC activities — Improve activity highlighted]

By the end of this module you will be able to describe all seven steps of the ITIL
Continual Improvement Model, explain improvement registers, define CSFs and KPIs, describe
benchmarking as a driver for improvement, and articulate how Lean and Agile thinking aligns
with ITIL's improvement approach.

[PAUSE]

---

## Section 1: The ITIL Continual Improvement Model (1:30–7:00)

The ITIL Continual Improvement Model is a seven-step cycle that organizations use to
structure and manage improvement efforts. It is iterative — you go through the cycle
repeatedly as the organization evolves.

[SHOW DIAGRAM: The seven-step continual improvement model as a circular cycle]

### Step 1: What Is the Vision?

Every improvement effort must start with the question: what are we trying to achieve?
The vision connects the improvement to the organization's strategic goals.

Without a vision, improvement efforts become disconnected technical upgrades that may
optimize a component while having no effect on what the business actually values. Before
starting any improvement, the team must be able to answer: "How does this contribute to
the organization's overall goals?"

[PAUSE]

### Step 2: Where Are We Now?

Before you can improve, you need an honest baseline. This step involves assessing the
current state — measuring current performance, documenting current processes, identifying
current pain points.

The key word is "honest." Organizations that only measure what looks good create false
baselines and unachievable targets. A credible current-state assessment may include:

- Service performance data from SLA reports
- Incident trend analysis
- Customer satisfaction scores
- Process maturity assessments
- Benchmarking against industry peers

[SHOW DIAGRAM: Baseline assessment — current state snapshot]

### Step 3: Where Do We Want to Be?

Define the specific, measurable target state. This is not the vision — the vision is
directional. Step 3 defines the concrete, measurable destination.

A well-formed Step 3 target is SMART: Specific, Measurable, Achievable, Relevant, and
Time-bound.

Example: "Reduce P2 incident resolution time from an average of 3.8 hours to 3.0 hours
within six months" — this is SMART. "Improve our incident response" — this is not.

[PAUSE]

### Step 4: How Do We Get There?

Design the improvement initiative. What specific changes need to be made? Who will
implement them? What resources are needed? What is the timeline? What risks must be
managed?

This step is where Lean and Agile thinking becomes valuable. Rather than designing one
massive change, break the improvement into small, iterative steps. Deliver value early
and often. Learn as you go.

### Step 5: Take Action

Implement the improvement initiative. This step often involves Change Management — the
changes to processes, tools, or services that deliver the improvement must be managed
through Change Enablement.

Key principle: measure as you go. Do not wait until the end to assess whether the
improvement is working.

[SHOW DIAGRAM: Iterative improvement cycles within Step 5]

[PAUSE]

### Step 6: Did We Get There?

Evaluate whether the target from Step 3 was achieved. Compare current performance against
the baseline from Step 2 and the target from Step 3. Be honest about the results.

If the target was achieved — document the success, capture lessons learned, and move to
Step 7.

If the target was partially achieved — understand why, capture lessons, and decide
whether to continue the initiative, adjust the approach, or revise the target.

If the target was not achieved — do not hide the result. Analyze what went wrong. Was
the target unrealistic? Was the approach flawed? Were there unforeseen obstacles? The
answer informs the next cycle.

### Step 7: How Do We Keep the Momentum Going?

Improvement is not a project with a start and end date. Sustainable improvement requires
embedding the new state into standard practice, updating procedures, training staff, and
using the outcome as the new baseline for the next improvement cycle.

[SHOW DIAGRAM: Step 7 feeding back into Step 1 for the next cycle]

This step prevents the most common improvement failure: the organization invests in
improvement, achieves a target, and then drifts back to the old way of working within
six months because nothing was embedded or institutionalized.

---

## Section 2: The Improvement Register (7:00–10:00)

The improvement register is the central repository for all improvement opportunities,
initiatives, and their status.

[SHOW DIAGRAM: Improvement register structure — columns labeled]

Every improvement idea — whether it comes from an incident review, an SLA breach, a
customer complaint, a staff suggestion, or a proactive assessment — gets recorded in
the improvement register. It is the backlog of improvement work for the IT organization.

### Key Fields in an Improvement Register

- **Improvement ID** — unique reference
- **Description** — what improvement is proposed
- **Source** — where the idea came from (incident, problem, customer feedback, etc.)
- **Priority** — how important is this improvement relative to others?
- **Owner** — who is responsible for driving this improvement?
- **Status** — proposed, approved, in progress, completed, deferred
- **Target completion** — when should this be done?
- **Expected benefit** — what outcome is expected?
- **Actual benefit** — what was actually achieved? (completed after implementation)

[PAUSE]

### Prioritizing the Improvement Register

Not everything in the register can be done at once. Prioritization considers:

- Alignment with the organizational vision (Step 1)
- Impact on customer outcomes and SLA performance
- Risk of not acting (compliance, safety, stability)
- Effort and cost required
- Dependencies on other improvements

The improvement register is reviewed regularly — typically in the service review meeting
and in the IT governance cycle.

---

## Section 3: CSFs and KPIs (10:00–13:00)

To know whether you are improving, you need to measure the right things. ITIL 4 uses
two complementary concepts: **Critical Success Factors** and **Key Performance Indicators**.

[SHOW DIAGRAM: CSF → KPI hierarchy]

### Critical Success Factors (CSFs)

A CSF is a necessary condition for achieving a strategic objective. It answers the question:
"What must be true for us to succeed?"

Example: "Our ability to restore P1 incidents within one hour is critical to maintaining
the trust of our banking customers."

CSFs are qualitative and strategic. They describe what matters most. They cannot be
directly measured, but they can be monitored through KPIs.

### Key Performance Indicators (KPIs)

A KPI is a metric used to evaluate the factors that are critical to the success of an
organization. KPIs operationalize CSFs — they turn the qualitative success condition into
measurable data points.

Example CSF: "We must maintain high availability of our trading platform."

Corresponding KPIs:

- Monthly availability percentage (target: 99.9%)
- Number of P1 incidents per month
- Mean time to restore for P1 incidents (target: under 45 minutes)
- Percentage of monitoring alerts actioned within 15 minutes

[PAUSE]

### The CSF-KPI Relationship — Common Mistakes

- **Too many KPIs:** When everything is measured, nothing is prioritized. Best practice:
  three to five KPIs per CSF.
- **Measuring what is easy, not what matters:** Organizations often gravitate toward metrics
  that look good rather than metrics that reveal problems. Good KPIs must be honest.
- **KPIs without CSFs:** Metrics without strategic context become data without insight.
  Always tie KPIs to CSFs.
- **Vanity metrics:** High numbers that look impressive but don't connect to outcomes —
  for example, ticket closure rate can be gamed by closing tickets without resolving issues.

---

## Section 4: Benchmarking (13:00–15:30)

Benchmarking is the process of comparing your organization's performance against internal
historical data, industry peers, or recognized best-practice standards.

[SHOW DIAGRAM: Three types of benchmarking — internal, competitive, functional]

### Why Benchmarking Matters for Continual Improvement

Without an external reference point, it is difficult to know whether "where we are now"
is actually good or bad. An organization that reduced its P2 resolution time from 6 hours
to 4.5 hours might feel they have improved — but if the industry median is 3.2 hours,
they are still below average.

Benchmarking provides:

- An honest external perspective on current performance
- Targets informed by what is actually achievable (not just internally negotiated)
- Credibility for improvement proposals — "industry peers achieve X" is a compelling argument
- Identification of capability gaps that internal assessments might miss

### Types of Benchmarking

- **Internal benchmarking** — comparing performance across teams, regions, or time periods
  within the same organization
- **Competitive benchmarking** — comparing against direct industry competitors
- **Functional benchmarking** — comparing a specific practice (e.g., service desk metrics)
  against recognized standards regardless of industry

Sources for IT benchmarking: HDI (service desk), ITIL maturity models, industry analyst
reports (Gartner, Forrester), vendor benchmarks, and peer networks.

[PAUSE]

---

## Section 5: Lean and Agile Alignment (15:30–18:30)

ITIL 4 explicitly embraces Lean and Agile thinking as complementary to the continual
improvement model. Understanding these connections strengthens both exam performance and
real-world practice.

[SHOW DIAGRAM: Lean waste categories and Agile improvement sprint mapped to ITIL steps]

### Lean and Continual Improvement

Lean originated in manufacturing and focuses on maximizing value by eliminating waste.
The seven categories of Lean waste — often remembered as TIMWOOD — translate directly
to IT service management:

- **Transportation** — unnecessary movement of information or work items
- **Inventory** — unresolved tickets, backlogged improvement items, unused knowledge articles
- **Motion** — unnecessary steps in a process (e.g., routing tickets through teams
  that cannot resolve them)
- **Waiting** — tickets waiting for approval, vendor response, or customer confirmation
- **Overproduction** — generating reports nobody reads; automating processes not worth automating
- **Over-processing** — requiring excessive approvals for low-risk standard changes
- **Defects** — resolved incidents that recur because the fix was incomplete

[PAUSE]

In the continual improvement context, a Lean lens helps teams identify which activities
in a value stream are wasteful and prioritize eliminations over additions.

### Agile and Continual Improvement

Agile principles align naturally with the iterative nature of the ITIL Continual
Improvement Model:

- **Short iterations:** Rather than designing one large improvement program, run
  two-week sprints targeting specific, measurable improvements
- **Early value delivery:** Deliver small improvements quickly rather than waiting for
  a perfect comprehensive solution
- **Feedback loops:** Continuously measure the impact of each improvement and adjust
- **Team empowerment:** The people doing the work are best positioned to identify
  improvement opportunities

The Agile principle "inspect and adapt" is essentially the ITIL continual improvement
cycle stated differently.

### Improvement Culture

Neither Lean nor Agile nor ITIL can succeed without an organizational culture that
values improvement. Key cultural attributes:

- **Psychological safety** — staff feel safe to report problems and propose changes
  without fear of blame
- **Blameless post-mortems** — incidents are analyzed to improve systems, not to
  assign fault to individuals
- **Management support** — leaders must visibly prioritize and fund improvement work
- **Recognition** — improvement contributions are acknowledged and celebrated

---

## Module Summary and Exam Tips (18:30–20:30)

Module 11 covered Continual Improvement.

The **ITIL Continual Improvement Model** has seven steps: What is the vision? Where are
we now? Where do we want to be? How do we get there? Take action. Did we get there? How
do we keep the momentum going?

The **improvement register** is the central backlog of all improvement opportunities,
prioritized and tracked through to completion.

**CSFs** (Critical Success Factors) define what must be true for success. **KPIs**
operationalize CSFs with measurable metrics — three to five KPIs per CSF is best practice.

**Benchmarking** provides external reference points that prevent organizations from
setting targets in a vacuum.

**Lean** eliminates waste from value streams. **Agile** delivers improvement iteratively.
Both are fully compatible with ITIL 4's approach.

[SHOW DIAGRAM: Module 11 summary — seven steps, register, CSF/KPI hierarchy]

For the ITIL 4 Foundation exam:

- Know all seven steps of the Continual Improvement Model in order
- Know the purpose and key fields of the improvement register
- Know the relationship between CSFs and KPIs
- Know that continual improvement is embedded in all SVC activities through the Improve
  activity
- Know that Step 7 prevents regression — it embeds improvements into standard practice

[PAUSE]

Congratulations on completing Module 11. You now have the full ITIL 4 Foundation conceptual
framework. The remaining modules apply these concepts to specialized contexts and help you
prepare for the certification exam. I will see you in Module 12.

---

End of Module 11 Video Script

Estimated delivery: 22 minutes at average instructional pace
