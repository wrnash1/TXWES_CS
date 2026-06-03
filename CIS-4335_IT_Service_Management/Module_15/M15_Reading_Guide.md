# Reading Guide: Module 15 — DevOps, Agile, and ITIL Integration

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

This reading guide supports Module 15's exploration of how ITIL 4 integrates with DevOps, Agile, and modern delivery practices. Understanding this integration is critical for practitioners entering organizations that use all three frameworks simultaneously — which describes the majority of modern IT environments.

**Estimated reading and reflection time:** 90–120 minutes

---

## Learning Objectives

After completing this module, you will be able to:

1. Explain why ITIL 4 was designed to integrate with, not replace, DevOps and Agile.
2. Map ITIL 4 Guiding Principles to Agile Manifesto values and DevOps principles.
3. Apply Value Stream Mapping to identify waste in an IT delivery process.
4. Describe how Change Enablement integrates with CI/CD pipelines.
5. Explain the Three Ways of DevOps and their alignment with ITIL practices.
6. Describe SRE concepts — SLO, SLI, error budget, toil — and their ITIL equivalents.
7. Identify organizational patterns that break down silos between development and operations.

---

## Section 1: The Evolution of IT Service Management

### 1.1 Why ITIL Had a Problem

ITIL v3 (2007/2011) was comprehensive and influential, but it accumulated a reputation for bureaucracy. Organizations implementing ITIL v3 sometimes created elaborate process structures — change management processes with 30+ steps, service design packages running to hundreds of pages — that consumed enormous effort without proportional benefit.

Meanwhile, Agile software development (Manifesto published 2001) and DevOps (emerged ~2008) were demonstrating that teams could deliver software reliably at high velocity without heavy process overhead. The contrast was stark.

**The specific friction point:** Change management. ITIL v3's change management process, as many organizations implemented it, required Normal changes to pass through a Change Advisory Board that met weekly. For teams attempting to deploy multiple times per week or per day, this was an absolute constraint.

### 1.2 ITIL 4's Response

ITIL 4 (2019) was a deliberate redesign addressing these criticisms:

- The rigid process model was replaced with a **practices** model — 34 practices with guidance rather than prescribed procedures.
- The Service Value System and Value Chain explicitly acknowledge that value delivery requires flexibility and feedback, not sequential process compliance.
- The guiding principles were articulated in ways that resonate with Agile and DevOps practitioners.
- ITIL 4's guidance explicitly states that the framework should be integrated with other approaches including Lean, DevOps, and Agile.

**Key quote from ITIL 4:** "ITIL 4 provides the guidance needed to address the new service management challenges and make use of the potential offered by technology. It has been created to align with the ways of working in modern organizations and include perspectives that are relevant for businesses in the digital age, such as Lean, Agile, DevOps, and digital transformation."

---

## Section 2: Framework Comparisons

### 2.1 The Agile Manifesto

The Agile Manifesto (2001) states four value pairs:

- **Individuals and interactions** over processes and tools.
- **Working software** over comprehensive documentation.
- **Customer collaboration** over contract negotiation.
- **Responding to change** over following a plan.

The Manifesto is careful to say "while there is value in the items on the right, we value the items on the left more." It is not anti-process or anti-documentation — it is a statement of priority.

**ITIL 4 alignment:** ITIL 4's guiding principles reflect these values. "Focus on Value" echoes the primacy of working software. "Collaborate and Promote Visibility" echoes individuals and interactions. "Progress Iteratively with Feedback" echoes responding to change.

### 2.2 The DevOps Philosophy

DevOps is not a single standard or specification. It is a cultural and organizational movement with common principles:

- **CALMS:** Culture, Automation, Lean, Measurement, Sharing — a common DevOps maturity model.
- **The Three Ways (Gene Kim):** Flow (fast delivery), Feedback (rapid learning), Continual Learning (organizational improvement).
- **The Phoenix Project / The DevOps Handbook:** The canonical texts that shaped DevOps practice.
- **DORA Research:** Evidence-based research identifying practices associated with high-performing software delivery teams.

**ITIL 4 alignment:** The Continual Improvement practice is a direct expression of the Third Way. The Service Value Chain's Deliver and Support activity embodies the Second Way's feedback loops. Release and Deployment Management practice incorporates automation principles from the First Way.

### 2.3 Lean Manufacturing Origins

Both ITIL 4 and DevOps draw explicitly from **Lean manufacturing** (Toyota Production System, perfected in the 1950s–1980s):

- **Value:** Identify what the customer values; everything else is waste.
- **Value stream:** Map the sequence of steps delivering value.
- **Flow:** Make value flow through the stream continuously; eliminate stops and waits.
- **Pull:** Let customer demand pull work through the system; avoid overproduction.
- **Perfection:** Continuously improve toward ideal flow.

In ITIL 4 terms: the Service Value System is the organization's value stream; the SVC activities are the major flow steps; practices are how work is done at each step.

---

## Section 3: Value Stream Mapping in Depth

### 3.1 VSM Origins and Application

Value Stream Mapping originated in Lean manufacturing — Toyota used it to visualize the flow of materials and information in vehicle production. Mary and Tom Poppendieck adapted it for software development in "Lean Software Development" (2003). ITIL 4 incorporates VSM as a tool for analyzing and improving IT value streams.

### 3.2 VSM Symbols and Conventions

A VSM uses standard symbols:

- **Process boxes:** Each step or activity in the value stream.
- **Push arrows:** Work pushed from one step to the next (scheduled, not demand-driven).
- **Pull arrows:** Work pulled by downstream demand.
- **Inventory triangles:** Work waiting between steps (the queues where waste accumulates).
- **Data boxes:** Beneath each process box — shows cycle time (how long work is in process) and wait time (how long work waits before the next step).
- **Timeline:** Running along the bottom, showing the cumulative value-adding vs. non-value-adding time.

### 3.3 Types of Waste

Lean identifies eight types of waste (expanded from the original seven in manufacturing), commonly remembered with the acronym DOWNTIME:

- **Defects:** Errors requiring rework — failed deployments, bug fixes, incorrect configurations.
- **Overproduction:** Building more than needed — features no user requests, premature capacity.
- **Waiting:** Idle time waiting for approvals, responses, environments.
- **Non-utilized talent:** People doing work below their capability; knowledge siloed.
- **Transportation:** Unnecessary handoffs or movement of work between teams.
- **Inventory:** Work in progress (WIP) piling up in queues.
- **Motion:** Unnecessary movement — physical or digital — to complete tasks.
- **Extra processing:** Doing more than the customer requires — gold-plating, over-engineering.

In IT environments, **waiting** is typically the largest source of waste. Change approval queues, testing environment availability, and access request processing are common waiting time generators.

### 3.4 VSM in Practice: An IT Example

Consider a value stream for deploying a security patch to production:

| Step | Cycle Time | Wait Time |
|---|---|---|
| Vulnerability detected and ticket created | 1 hour | 0 |
| Ticket triaged and assigned | 15 min | 4 hours |
| Developer applies patch in dev environment | 2 hours | 0 |
| Automated test run | 20 min | 0 |
| Code review | 1 hour | 8 hours (wait for reviewer availability) |
| Change request created | 30 min | 0 |
| CAB approval (next scheduled meeting) | 30 min | 72 hours (wait for CAB meeting) |
| Deployment to staging | 20 min | 4 hours (maintenance window) |
| UAT sign-off | 2 hours | 24 hours |
| Deployment to production | 20 min | 2 hours |
| **Total** | **8.25 hours active** | **~116 hours waiting** |

Total elapsed time: approximately 5–6 days.
Value-adding time: 8.25 hours.
Waste percentage: approximately 93%.

This map clearly identifies the CAB waiting time (72 hours) and UAT waiting (24 hours) as the primary improvement targets.

---

## Section 4: Integrating Change Enablement with CI/CD

### 4.1 Change Types in a DevOps Context

ITIL 4 defines three change types relevant to CI/CD integration:

**Standard changes:** Pre-authorized, low-risk, well-documented changes executed according to a defined procedure. In a CI/CD context, automated deployments that meet predefined criteria (tests passed, security scans clean, within authorized window, within defined scope) can be classified as standard changes. No individual CAB review is needed per deployment.

**Normal changes:** Require assessment, authorization, and scheduling. In a DevOps context, these should be reserved for genuinely novel or high-risk changes that lack a pre-approved procedure — not every routine feature deployment.

**Emergency changes:** Reserved for responses to major incidents. CI/CD pipelines should have an "emergency lane" — a fast path for critical security patches or incident recovery deployments.

### 4.2 Change Enablement Embedded in Pipelines

The maturity model for integrating change governance with CI/CD:

**Level 1 (Basic):** CI/CD pipeline exists; change requests created manually after each deployment. Governance is reactive.

**Level 2 (Integrated):** CI/CD pipeline automatically creates change records in the ITSM tool upon deployment. Pipeline log provides evidence. Still manual approval for normal changes.

**Level 3 (Standard change automation):** Deployments meeting predefined criteria auto-approve as standard changes. Pipeline log IS the change record. Human review only for exceptions.

**Level 4 (Policy-as-code):** Change governance policies encoded in the pipeline itself. Deployments are automatically classified, approved or escalated based on risk scoring. Compliance is enforced automatically, not audited after the fact.

---

## Section 5: Site Reliability Engineering

### 5.1 SRE Principles

SRE emerged from Google's engineering team and was described publicly in 2016. It is now practiced at thousands of organizations. The core insight: reliability is a software problem, and therefore reliability engineering should use software engineering practices.

**Key SRE practices:**

- Define reliability targets quantitatively (SLOs).
- Measure reliability accurately (SLIs).
- Create error budgets to enable rational risk decisions.
- Build automation to reduce toil.
- Conduct blameless postmortems after incidents.
- Practice chaos engineering — intentionally introduce failures to test resilience.

### 5.2 SLO, SLI, SLA Relationships

These three related terms are often confused:

**SLI (Service Level Indicator):** A quantitative measurement of a service dimension. Example: "request success rate" = percentage of HTTP requests that return a 2xx or 3xx response code.

**SLO (Service Level Objective):** A target value or range for an SLI. Example: "Request success rate SLO = 99.9% over a rolling 28-day window."

**SLA (Service Level Agreement):** A contractual commitment to a customer about service performance, with financial or other consequences for violation. Example: "We guarantee 99.5% monthly availability; failure results in service credits."

The relationship: SLIs are measured → compared against SLOs (internal targets, stricter) → SLAs are the customer-facing commitments (looser, with buffer).

**Why have stricter internal SLOs than external SLAs?** To catch degradation before customers are contractually affected. If the SLO is breached, engineering investigates before the SLA breach that triggers penalties.

### 5.3 Error Budgets as a Management Tool

The error budget transforms the development-vs-operations conflict into a shared mathematical framework.

**Calculation example:**

- SLO: 99.9% availability over 30 days.
- Total minutes in 30 days: 43,200.
- Error budget: 0.1% × 43,200 = 43.2 minutes of allowed downtime per month.

**Using the error budget:**

- If the error budget is healthy (most of the 43.2 minutes remains), the team can deploy new features aggressively.
- If the error budget is nearly consumed (close to 43.2 minutes of downtime), feature deployments pause and reliability work takes priority.
- If the error budget is gone (exceeded 43.2 minutes), a deployment freeze is enforced until the budget resets.

This replaces "development wants to move fast / operations wants stability" with "both teams want to maximize the error budget's utility."

### 5.4 Blameless Postmortems

The blameless postmortem is one of the most culturally significant SRE practices. Its rules:

- The goal is to understand what happened and why — not to assign blame.
- Focus on systems and processes, not individuals.
- All findings are learning opportunities.
- The output is a set of action items to prevent recurrence and improve system resilience.
- The document is shared broadly within the organization.

**ITIL alignment:** Blameless postmortems are SRE's operational version of ITIL's Problem Management practice. Both seek root cause analysis and systemic improvement from incidents.

---

## Section 6: Organizational Patterns

### 6.1 Team Topologies

Matthew Skelton and Manuel Pais's "Team Topologies" (2019) provides a framework for organizing teams to optimize software delivery:

**Stream-aligned teams:** Aligned to a flow of business value — a product, service, or user journey. These teams have all capabilities needed to deliver and operate their service.

**Platform teams:** Provide internal shared platforms that stream-aligned teams consume. Reduce cognitive load and enable self-service.

**Enabling teams:** Temporary specialist teams that help stream-aligned teams acquire new capabilities (adopt new technologies, improve practices).

**Complicated subsystem teams:** Handle technically complex components (e.g., cryptography, DSP algorithms) where deep specialization is required.

This organizational model replaces the traditional Dev/Ops/QA silo structure.

### 6.2 Platform Engineering

Platform engineering creates an Internal Developer Platform (IDP) — a set of self-service tools and workflows that developers use to build, test, deploy, and monitor their services.

From an ITIL perspective, the platform engineering team is essentially delivering a service to internal development customers. The ITIL practices of Service Design, Service Level Management, and Continual Improvement apply directly to how the platform team operates.

---

## Key Vocabulary

- **DevOps** — cultural and technical movement unifying development and operations.
- **Agile Manifesto** — 2001 document establishing values and principles for software development.
- **CALMS** — DevOps maturity model: Culture, Automation, Lean, Measurement, Sharing.
- **Three Ways** — Flow, Feedback, Continual Learning (Gene Kim's DevOps framework).
- **Value Stream Mapping (VSM)** — technique to visualize and optimize delivery flow.
- **Waste (DOWNTIME)** — Defects, Overproduction, Waiting, Non-utilized talent, Transportation, Inventory, Motion, Extra processing.
- **Standard change** — pre-authorized, low-risk change needing no individual CAB review.
- **Policy-as-code** — governance rules encoded in automated pipeline logic.
- **Site Reliability Engineering (SRE)** — Google's reliability engineering approach.
- **SLI** — quantitative measurement of a service dimension.
- **SLO** — internal reliability target value for an SLI.
- **Error budget** — allowable unreliability derived from SLO.
- **Toil** — manual, repetitive operational work that scales with service growth.
- **Blameless postmortem** — incident review focused on systemic improvement.
- **Platform engineering** — shared internal delivery platform for development teams.
- **Team Topologies** — framework organizing teams around flow rather than function.

---

## Self-Check Questions

1. Choose two ITIL 4 Guiding Principles and explain how each is expressed in Agile or DevOps practice.
2. Draw (or describe in text) a simple value stream map for a process you are familiar with. Identify the biggest source of wait time.
3. What is the difference between an SLI, an SLO, and an SLA? Give an example of each for the same service.
4. How does an error budget resolve the traditional conflict between development speed and operational stability?
5. What is the difference between a Standard change and a Normal change in a CI/CD deployment context?

---

*End of Module 15 Reading Guide — approximately 265 lines*
