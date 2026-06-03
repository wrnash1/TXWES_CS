# Reading Guide: Module 15 — DevOps, Agile, and ITIL 4 Integration

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

ITIL 4 was designed with a specific intent: to remain relevant in a world where Agile delivery, DevOps automation, and Lean thinking have fundamentally changed how IT organizations work. Earlier ITIL versions were sometimes perceived as obstacles to fast delivery — the change advisory board, the heavyweight processes, the separation between development and operations. ITIL 4 addresses these perceptions by explicitly aligning its principles and practices with the values of Agile, DevOps, and Lean.

This is not just a marketing claim. The ITIL 4 Service Value System is structurally designed to accommodate high-frequency, automated, iterative delivery alongside more structured governance practices. Understanding this integration is essential for applying ITIL 4 in modern organizations.

---

## ITIL 4 and Agile

### Agile Foundations

Agile is a software development philosophy based on the Agile Manifesto (2001). The four values of the Agile Manifesto are:

- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan

The Manifesto's 12 principles expand on these values — emphasizing frequent delivery, sustainable pace, technical excellence, continuous attention to changing requirements, and regular reflection on how to become more effective.

Common Agile frameworks include Scrum (sprint-based iterative delivery), Kanban (flow-based continuous delivery), and SAFe (Scaled Agile Framework for large organizations).

### ITIL 4 Guiding Principles and Agile Alignment

ITIL 4's seven guiding principles map closely to Agile values:

| ITIL 4 Guiding Principle | Agile Alignment |
|---|---|
| Focus on Value | Deliver what customers need, not what is internally convenient |
| Start Where You Are | Build on existing work rather than rebuilding from scratch |
| Progress Iteratively with Feedback | Sprint-based delivery; inspect and adapt after each iteration |
| Collaborate and Promote Visibility | Shared boards, daily standups, cross-functional teams |
| Think and Work Holistically | End-to-end service thinking beyond individual team boundaries |
| Keep It Simple and Practical | Minimize process overhead; favor working outcomes |
| Optimize and Automate | Automate repetitive work; free humans for judgment-intensive tasks |

The alignment is not accidental. ITIL 4's authors explicitly incorporated Agile thinking into the framework's design. Organizations that practice Agile do not need to abandon ITIL 4 — they need to apply it in a way that supports rather than constrains their delivery cadence.

### Where ITIL 4 Complements Agile

Agile methods are primarily focused on software development — the creation of new features and capabilities. ITIL 4 addresses the full operational lifecycle of IT services: support, monitoring, asset management, risk, compliance, and governance. Agile teams that operate within an ITIL 4 governance framework have the benefit of:

- Defined change authorization models that allow standard changes to be automated
- Incident management processes that respond when Agile-delivered features fail in production
- Configuration management that tracks what was deployed and where
- Risk management practices that evaluate the operational risk of new features before release

---

## ITIL 4 and DevOps

### DevOps Foundations

DevOps is a cultural and technical movement that integrates software development (Dev) and IT operations (Ops) into shared teams with shared accountability for the full lifecycle of services — from code commit to production monitoring.

Core DevOps principles include:

- **Culture of collaboration** — development and operations teams share goals, metrics, and accountability
- **Automation** — repetitive tasks (build, test, deploy, monitor) are automated to enable speed and consistency
- **Measurement** — data-driven decision making using operational and delivery metrics
- **Sharing** — knowledge, tools, and practices are shared across team boundaries
- **Lean thinking** — waste is identified and eliminated; flow is optimized

### The DORA Four Keys

The DevOps Research and Assessment (DORA) program has identified four metrics that reliably distinguish high-performing software delivery organizations from lower performers:

| Metric | Description | Elite Performance |
|---|---|---|
| Deployment Frequency | How often successful deployments to production occur | Multiple times per day |
| Lead Time for Changes | Time from code commit to production deployment | Less than one hour |
| Change Failure Rate | Percentage of deployments causing production failures | Below 5% |
| Time to Restore Service | Time to recover from a production failure | Less than one hour |

These metrics connect directly to ITIL 4 practices. Lead time reflects Change Enablement efficiency. Change failure rate reflects Release and Deployment Management quality. Time to restore reflects Incident Management maturity. Deployment frequency reflects the effectiveness of automation and standard change authorization.

### ITIL 4 Change Enablement and DevOps

The most significant alignment between ITIL 4 and DevOps is in Change Enablement. ITIL 4 defines three change types:

**Standard changes** are pre-authorized, low-risk changes that follow a documented procedure. Because they are pre-authorized, they can be implemented without individual CAB review. DevOps pipelines execute standard changes — routine deployments that have been assessed and pre-approved as a class of change.

**Normal changes** require individual risk assessment and authorization before implementation. For DevOps teams, normal changes represent exceptions — deployments with unusual risk profiles that warrant specific review.

**Emergency changes** require expedited authorization for urgent situations. Emergency changes can bypass standard pipeline gates with appropriate logging and post-hoc review.

This three-tier model enables high-frequency deployment (standard changes can flow continuously through automated pipelines) while maintaining governance for changes that carry higher risk.

### Breaking Silos

One of the most persistent challenges in traditional IT organizations is organizational silos — development, testing, deployment, and operations each operating as separate teams with different tools, priorities, and accountability structures. The consequences include:

- Handoff delays as work waits for the next team to pick it up
- Knowledge gaps when the team that built something is unavailable when it fails
- Misaligned incentives (development optimizes for feature delivery speed; operations optimizes for stability)
- Blame culture when things go wrong

DevOps addresses silos through cross-functional teams that own the full lifecycle of the services they build. ITIL 4 supports this by emphasizing value stream thinking — designing processes around how value flows end-to-end rather than how work is divided by functional team.

---

## Value Stream Mapping

### What Is a Value Stream?

A value stream is the series of steps an organization takes to create and deliver value to a customer. In IT service management, value streams connect customer needs to service delivery. ITIL 4 explicitly introduces value stream thinking as a lens for understanding how the Service Value Chain activities combine to deliver outcomes.

Different types of work follow different value streams. An incident flowing from user report to resolution follows a different value stream than a feature request flowing from product backlog to production deployment.

### Value Stream Mapping as a Lean Technique

Value Stream Mapping (VSM) is a Lean technique that visualizes a value stream by mapping every step in the process, the time spent at each step, and the waiting time between steps. The map distinguishes between:

**Value-added time** — work that directly contributes to the customer outcome. Writing code, running tests, deploying software, resolving an incident are value-added activities.

**Non-value-added time** — waiting, rework, handoffs, approvals, and any other activity that delays delivery without contributing to value. A change request sitting in an approval queue for three days is pure waste.

**Value-added ratio** — the proportion of total lead time that is value-added. The formula is:

> Value-Added Ratio = Total Value-Added Time / Total Lead Time

In most IT organizations, the value-added ratio is surprisingly low — often below 20%. This means the majority of calendar time from request to delivery is waiting, not working.

### VSM Process

1. Define the scope — identify the start and end of the value stream being mapped
2. Map the current state — document every step, the time for each step, and the wait time between steps
3. Calculate the value-added ratio for the current state
4. Identify waste — the largest wait times and non-value-added steps are prioritization targets
5. Design the future state — redesign the value stream to eliminate identified waste
6. Implement and measure — execute the redesign and track improvements in lead time and value-added ratio

---

## CI/CD in the ITSM Context

Continuous Integration (CI) is the practice of frequently integrating code changes into a shared repository where automated builds and tests validate each change immediately. Continuous Delivery (CD) ensures that code is always in a deployable state by automating the pipeline from code commit through to a production-ready artifact.

### CI/CD as ITSM Automation

In the ITSM context, a CI/CD pipeline is the automation of several ITIL 4 practice activities:

- **Change record creation** — the pipeline automatically creates a change record for each production deployment
- **Release validation** — automated tests in the pipeline constitute the testing component of Release and Deployment Management
- **Deployment execution** — the pipeline deploys the release to production following approved procedures
- **Post-deployment verification** — automated smoke tests confirm that the deployment succeeded
- **Monitoring integration** — the pipeline triggers monitoring alerts if post-deployment health checks fail
- **Rollback automation** — if defined conditions are met, the pipeline executes the rollback procedure automatically

### Approval Gates

ITIL 4's change model maps directly to pipeline gate design:

| Change Type | Pipeline Gate Behavior |
|---|---|
| Standard change | Automated gate — passes automatically if automated tests pass |
| Normal change | Human approval gate — pipeline pauses, notifies approver, waits for manual authorization |
| Emergency change | Expedited gate — authorized out-of-band with logging; post-hoc CAB review |

This design enables DevOps-speed deployment for standard changes while preserving governance for changes requiring individual review.

---

## Site Reliability Engineering

### SRE Foundations

Site Reliability Engineering (SRE) is a discipline developed at Google that applies software engineering principles to IT operations. SRE treats reliability as an engineering problem — writing code to automate manual operations tasks, designing systems for self-healing, and using data to make reliability decisions.

SRE teams are responsible for the reliability, scalability, and performance of the services they support. They write software that eliminates repetitive manual operations tasks — if a task can be automated, it should be.

### Service Level Objectives

An SLO is an internal reliability target — the level of service the SRE team commits to maintaining. SLOs are more specific and operational than SLAs. They are typically expressed as:

- Availability percentage: 99.9% of requests succeed
- Latency target: 95th percentile response time below 200 ms
- Error rate ceiling: fewer than 0.1% of requests return a 5xx error

### Error Budgets

The error budget is the permitted amount of unreliability within an SLO. If the SLO is 99.9% monthly availability, the monthly error budget is 43.8 minutes of allowable downtime.

The error budget creates a quantified trade-off between velocity and reliability:

- When the error budget is healthy (mostly unspent), teams can deploy frequently and take calculated risks
- When the error budget is nearly consumed, deployments are paused until the budget recovers
- This creates an objective, data-driven conversation between development and operations that is not based on opinion or politics

### SRE and ITIL 4

SRE connects to ITIL 4 in several ways. SLOs map to ITIL 4's Service Level Management. Error budgets are a practical implementation of risk management within service operations. SRE's emphasis on automation directly implements ITIL 4's "Optimize and Automate" principle. SRE runbooks — documented procedures for operational responses — align with ITIL 4's emphasis on documented processes in Incident and Problem Management.

---

## Key Terms for the ITIL 4 Foundation Exam

| Term | Definition |
|---|---|
| Value stream | The series of steps an organization takes to create and deliver value to a customer |
| Value Stream Mapping | Lean technique visualizing flow, value-added time, and waste in a process |
| Value-added ratio | Proportion of total lead time that is actually value-added work |
| CI/CD | Continuous Integration and Continuous Delivery — automated pipeline from code to production |
| Standard change | Pre-authorized change that can be implemented without individual CAB review |
| DevOps | Cultural and technical movement integrating development and operations with shared accountability |
| DORA Four Keys | Deployment frequency, lead time for changes, change failure rate, time to restore service |
| SRE | Site Reliability Engineering — applying software engineering to operations reliability |
| SLO | Service Level Objective — an internal reliability target set by SRE teams |
| Error budget | The permitted amount of unreliability within an SLO period |

---

## Study Questions

1. What are the four values of the Agile Manifesto, and how do they align with ITIL 4's guiding principles?

2. What are the DORA Four Keys, and which ITIL 4 practices do they map to?

3. What is the difference between a standard change, a normal change, and an emergency change in the context of a DevOps CI/CD pipeline?

4. How does Value Stream Mapping identify waste in a delivery process?

5. What is an error budget in SRE, and how does it create a data-driven trade-off between velocity and reliability?

6. Why do organizational silos create delivery problems, and how do DevOps and ITIL 4 both address this?

7. What is the value-added ratio, and why is it typically much lower than organizations expect?
