# Video Script: Module 15 — DevOps, Agile, and ITIL 4 Integration

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation
**Estimated Duration:** 22–25 minutes
**Recorded by:** Professor Nash

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.
- [PAUSE] cues indicate natural break points for student note-taking.

---

## Section 1: Welcome and Module Overview [00:00 - 02:30]

Welcome to Module 15. I am Professor Nash. This module covers one of the most important conceptual shifts in ITIL 4 compared to earlier versions — the explicit integration of DevOps, Agile, and Lean thinking into the ITIL framework. If you have heard that ITIL is rigid and bureaucratic while DevOps is fast and collaborative, this module addresses that tension directly.

[SHOW DIAGRAM: Title slide — "Module 15: DevOps, Agile, and ITIL 4 Integration" with ITIL 4 SVS label and ITIL 4 Foundation certification badge]

ITIL 4 was redesigned with the explicit goal of working alongside DevOps and Agile rather than conflicting with them. The ITIL 4 Service Value System is designed to be flexible enough to encompass both structured, governance-heavy practices and fast, iterative delivery approaches. Understanding how these frameworks coexist is essential — both for the Foundation exam and for working in modern IT organizations where all three approaches are often present simultaneously.

By the end of this module you will be able to: explain how ITIL 4 aligns with Agile and DevOps, apply Value Stream Mapping concepts, describe CI/CD in the ITSM context, explain why breaking silos matters, define Site Reliability Engineering, and identify the metrics used to measure flow.

---

## Section 2: ITIL 4 and Agile [02:30 - 06:30]

[SHOW DIAGRAM: Agile values alignment table — Agile Manifesto's four values on the left, corresponding ITIL 4 SVS principles on the right, with connecting arrows]

### Agile Principles in Context

Agile is a software development philosophy based on the Agile Manifesto — 12 principles and 4 values centered on delivering working software frequently, responding to change, collaborating with customers, and valuing people over processes. Agile methods include Scrum, Kanban, and SAFe.

ITIL 4 aligns with Agile in several specific ways.

**"Focus on Value"** — ITIL 4's first guiding principle is directly aligned with Agile's emphasis on delivering working software that customers find valuable. Both frameworks push back against activity for its own sake.

**"Progress Iteratively with Feedback"** — ITIL 4's fourth guiding principle mirrors Agile's sprint model. Rather than planning everything upfront and delivering once, both approaches favor small increments, feedback, and adaptation.

**"Collaborate and Promote Visibility"** — ITIL 4's fifth principle aligns with Agile's emphasis on team communication, daily standups, and shared visibility through tools like Kanban boards.

[PAUSE]

The difference between Agile and ITIL is scope, not philosophy. Agile primarily addresses how software is developed. ITIL addresses the full lifecycle of IT service management — including operations, support, asset management, risk, and governance. ITIL 4 provides the governance and operational framework that operates around the Agile delivery teams.

---

## Section 3: ITIL 4 and DevOps [06:30 - 11:00]

[SHOW DIAGRAM: DevOps infinity loop — Plan → Code → Build → Test → Release → Deploy → Operate → Monitor → back to Plan — with ITIL 4 practice names mapped to relevant stages]

### What Is DevOps?

DevOps is a cultural and technical movement that breaks down the traditional separation between software development (Dev) and IT operations (Ops). DevOps organizations use automation, shared tooling, shared metrics, and shared accountability to enable frequent, reliable deployments. The DevOps Research and Assessment (DORA) program has identified four key metrics for high-performing DevOps teams: deployment frequency, lead time for changes, change failure rate, and time to restore service.

### ITIL 4 and DevOps Alignment

ITIL 4 explicitly embraces DevOps. The ITIL 4 publication recognizes DevOps as one of the key practices that organizations are adopting alongside ITIL. Where earlier ITIL versions were perceived as conflicting with DevOps (particularly around change management bureaucracy), ITIL 4 reframes change management to support high-frequency, low-friction deployments through standard changes and automated pipelines.

Key alignments include:

**Standard changes** — ITIL 4 Change Enablement defines standard changes as pre-authorized changes that follow a documented procedure. Standard changes can be implemented without individual CAB review — enabling the high deployment frequency that DevOps teams require.

**Deployment automation** — ITIL 4 explicitly supports deployment automation as a realization of the "Optimize and Automate" guiding principle. DevOps CI/CD pipelines implement the deployment automation that ITIL 4 advocates.

**Shared metrics** — DORA's four metrics — deployment frequency, lead time, change failure rate, time to restore — map directly to ITIL 4 service value metrics. Both frameworks measure the same outcomes from different perspectives.

[PAUSE]

The silo problem is where DevOps and traditional ITIL implementations have most frequently clashed. Traditional ITSM created separate teams for development, testing, deployment, and operations — each with its own tools, priorities, and accountability. DevOps organizations collapse these silos, creating cross-functional teams that own the full lifecycle of the services they build and run. ITIL 4 supports this model through its emphasis on collaboration and value stream thinking.

---

## Section 4: Value Stream Mapping [11:00 - 14:30]

[SHOW DIAGRAM: Value stream map example — user story request flows through: Product Backlog → Sprint Planning → Development → Code Review → Automated Testing → Staging Deployment → Production Deployment → User Value. Each step shows value-added time and wait time. Total lead time and value-added ratio labeled.]

### What Is Value Stream Mapping?

Value Stream Mapping (VSM) is a Lean technique for visualizing and analyzing the flow of work from request to value delivery. It was developed in manufacturing and adapted for software and IT service delivery. A value stream map shows every step in a process, the time spent at each step, and the waiting time between steps.

In ITSM, value streams represent the path from a customer need or service request to the delivery of value. ITIL 4 introduces the concept of value streams explicitly — the SVS recognizes that different types of work (incident resolution, new feature development, change implementation) follow different value streams.

### Key VSM Concepts

**Value-added time** is time spent on work that directly contributes to the customer outcome. Code being written, a test being executed, a change being deployed are value-added activities.

**Non-value-added time** is waiting, handoffs, rework, and approvals that do not contribute to the customer outcome. A change request sitting in an approval queue for three days is pure waste.

**Value-added ratio** is the proportion of total lead time that is actually value-added. In most IT organizations, the value-added ratio is surprisingly low — often below 20%. This means more than 80% of the time from request to delivery is spent waiting rather than working.

VSM reveals where waste is concentrated, which allows organizations to target improvement efforts where they will have the greatest impact on flow.

---

## Section 5: CI/CD in the ITSM Context [14:30 - 17:30]

[SHOW DIAGRAM: CI/CD pipeline with ITSM gates labeled — Code Commit → Build → Unit Tests → Integration Tests → Staging Deploy → Automated Acceptance Tests → Change Record Creation → Approval Gate → Production Deploy → Post-Deploy Tests → Monitoring Alerts]

Continuous Integration (CI) is the practice of frequently merging code changes into a shared repository, where automated builds and tests run to validate each change immediately. Continuous Delivery (CD) extends CI to ensure that code is always in a deployable state — every passing change is potentially releasable to production.

In the ITSM context, CI/CD is the implementation of deployment automation at scale. The pipeline does not replace ITSM practices — it executes them automatically. A CI/CD pipeline:

- Generates a change record for every production deployment (Change Management)
- Runs automated tests that constitute deployment validation (Release and Deployment Management)
- Triggers rollback if post-deployment tests fail (Release and Deployment Management)
- Creates deployment records that feed into audit evidence (Compliance)
- Generates alerts if health checks fail after deployment (Monitoring and Event Management)

The ITIL 4 integration point is the approval gate in the pipeline. Standard changes — pre-authorized, low-risk deployments — can pass through the gate automatically. Normal changes — requiring individual assessment — pause at the gate until human authorization is obtained. Emergency changes can bypass standard gates with appropriate logging and post-hoc review.

---

## Section 6: Site Reliability Engineering [17:30 - 20:00]

[SHOW DIAGRAM: SRE error budget model — vertical bar showing 100% availability target (99.9% = 43.8 minutes/month), error budget allocation, actual consumption to date, remaining error budget for the month]

Site Reliability Engineering (SRE) is a discipline developed at Google that applies software engineering principles to IT operations problems. SRE teams treat operational stability as an engineering challenge — writing code to automate manual operations tasks, building self-healing systems, and using data to make reliability decisions.

### Service Level Objectives

The foundation of SRE is the Service Level Objective (SLO). An SLO is an internal reliability target — the level of service the team commits to maintaining. SLOs are more specific than SLAs: they are set by the engineering team for the engineering team, based on what is technically achievable and what customers actually need.

### Error Budgets

The error budget is the permitted amount of unreliability within an SLO. If the SLO is 99.9% availability, the monthly error budget is 43.8 minutes of allowable downtime. When the error budget is healthy — most of it still available — the team has room to take deployment risks and move fast. When the error budget is consumed — the team has been close to or exceeded the SLO limit — deployments are paused until the budget recovers.

This concept is revolutionary because it quantifies the relationship between velocity and reliability. Moving fast consumes error budget. Stability preserves it. The error budget creates an objective, data-driven conversation between development and operations about the appropriate pace of change.

---

## Section 7: Measuring Flow [20:00 - 22:00]

[SHOW DIAGRAM: Four DORA metrics — four dials/gauges showing Deployment Frequency, Lead Time for Changes, Change Failure Rate, Time to Restore Service — with Elite/High/Medium/Low band labels from DORA research]

The DORA Four Keys are the industry-standard metrics for measuring software delivery performance:

**Deployment Frequency** — How often does the organization successfully deploy to production? Elite performers deploy multiple times per day. Low performers deploy once per month or less.

**Lead Time for Changes** — How long does it take for a committed code change to reach production? Elite performers achieve this in less than one hour. Low performers take one to six months.

**Change Failure Rate** — What percentage of deployments cause a failure in production requiring remediation? Elite performers keep this below 5%. Low performers see 46–60% failure rates.

**Time to Restore Service** — When a service incident occurs, how long does it take to restore normal service? Elite performers restore within one hour. Low performers take one week to one month.

These metrics connect directly to ITIL 4. Lead time for changes maps to Change Enablement efficiency. Change failure rate maps to Release and Deployment Management quality. Time to restore service maps to Incident Management performance. Deployment frequency reflects the maturity of automation and the effectiveness of standard change authorization.

---

## Section 8: Exam Reminders and Lab Preview [22:00 - End]

Three exam reminders. First: ITIL 4 was designed to coexist with Agile and DevOps — it is not a competing framework. Second: Value stream mapping reveals waste by comparing value-added time to total lead time. Third: SRE error budgets quantify the trade-off between deployment velocity and service reliability.

This week's lab asks you to perform a value stream map analysis on a provided IT delivery scenario, identify the three greatest sources of waste, and design a CI/CD pipeline that integrates ITSM practice gates at appropriate points.

---

## Module 15 Complete

Next: Module 16 — ITIL 4 Foundation Exam Preparation

### Additional Resources

- axelos.com — ITIL 4 Foundation study materials
- dora.dev — DORA State of DevOps Report and Four Keys documentation
- sre.google — Google SRE Book (free online)
