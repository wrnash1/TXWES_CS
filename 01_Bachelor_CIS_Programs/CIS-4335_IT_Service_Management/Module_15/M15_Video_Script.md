# Video Script: Module 15 — DevOps, Agile, and ITIL Integration

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Slide 1: Introduction (0:00–0:45)

Welcome to Module 15 of CIS-4335. I'm Professor Nash. This module addresses one of the most important evolutions in IT service management: how ITIL 4 embraces and integrates with DevOps, Agile, and modern software delivery practices.

For years, ITSM and DevOps were portrayed as adversaries. ITSM was seen as heavyweight and bureaucratic; DevOps as fast and ungoverned. ITIL 4 changed the conversation by recognizing that these approaches are complementary. By the end of this video you will understand where they align, where they differ, and how to build organizations that combine the best of all three.

---

## Slide 2: The Historical Tension (0:45–2:30)

The perception of ITIL vs. DevOps as opposing philosophies emerged from real friction in organizations.

**ITIL's traditional reputation:** Detailed processes, extensive documentation, change advisory boards that met weekly, change windows measured in months. Engineers complained that ITSM slowed everything down.

**DevOps' reputation:** "Move fast and break things." Deploy dozens of times a day. Automate everything. No gatekeepers.

The tension was real — but it was largely a conflict between poorly implemented ITIL (excessive bureaucracy without value) and early-stage DevOps (speed without accountability).

**ITIL 4 resolved this by:**

- Acknowledging that the guiding principles — particularly "optimize and automate" and "progress iteratively with feedback" — are the philosophical foundations of DevOps.
- Replacing rigid process prescriptions with flexible practices.
- Explicitly encouraging organizations to integrate ITIL with Agile and DevOps rather than treating them as mutually exclusive.

The ITIL 4 Foundation exam does NOT expect you to know DevOps or Agile in depth. But it expects you to understand that ITIL 4 is designed to work alongside these approaches.

---

## Slide 3: ITIL 4 Guiding Principles and Agile/DevOps Alignment (2:30–5:00)

The seven ITIL 4 Guiding Principles map surprisingly well to Agile and DevOps values.

### Principle 1: Focus on Value

- **ITIL 4:** Every activity must contribute to value creation for stakeholders.
- **Agile:** The Manifesto's first principle — "Our highest priority is to satisfy the customer through early and continuous delivery of valuable software."
- **Alignment:** Perfect. Both frameworks reject work that does not directly serve the customer.

### Principle 2: Start Where You Are

- **ITIL 4:** Assess the current state before changing it; reuse existing capabilities.
- **DevOps:** "You can't buy DevOps" — transformation must start with understanding your current processes and culture.
- **Alignment:** Both warn against greenfield idealism that ignores organizational reality.

### Principle 3: Progress Iteratively with Feedback

- **ITIL 4:** Deliver improvements in increments; use feedback to guide next steps.
- **Agile:** Sprints, retrospectives, daily standups — iterative delivery with embedded feedback loops.
- **DevOps:** Continuous integration, monitoring, and alerting — automated feedback at every stage.
- **Alignment:** This principle is essentially a statement of Agile and DevOps philosophy in ITIL language.

### Principle 4: Collaborate and Promote Visibility

- **ITIL 4:** Break silos; share information transparently across the value stream.
- **DevOps:** "You build it, you run it" — developers own operational responsibility; silos are the enemy.
- **Agile:** Cross-functional teams; working in the open; shared backlogs.
- **Alignment:** The anti-silo philosophy is shared across all three.

### Principle 5: Think and Work Holistically

- **ITIL 4:** Understand how all components and practices interact; avoid local optimization.
- **DevOps:** Systems thinking — the first Way of DevOps (from "The Phoenix Project"); optimize the whole system, not individual functions.
- **Alignment:** Both reject the "throw it over the wall" mentality between development and operations.

### Principle 6: Keep It Simple and Practical

- **ITIL 4:** Eliminate steps that add no value.
- **Agile:** Simplicity — "the art of maximizing the amount of work not done" (Agile Manifesto).
- **Alignment:** Both resist bureaucratic accretion and favor lean processes.

### Principle 7: Optimize and Automate

- **ITIL 4:** Automate repetitive tasks to free humans for complex work.
- **DevOps:** CI/CD pipelines, infrastructure as code, automated testing — automation is a core practice.
- **Alignment:** This principle is a direct statement of DevOps automation philosophy.

---

## Slide 4: Value Stream Mapping (5:00–7:00)

**Value Stream Mapping (VSM)** is a technique borrowed from Lean manufacturing and widely used in both ITIL 4 and DevOps contexts.

A value stream is the sequence of steps that delivers value from initial demand to the customer. VSM visualizes this sequence to identify:

- **Value-adding activities:** Steps that directly contribute to what the customer wants.
- **Non-value-adding activities (waste):** Steps that consume time or resources without adding customer value. In Lean terminology, these are called "muda."

### VSM in ITIL 4

ITIL 4 uses the concept of value streams explicitly. Organizations are encouraged to map their service value streams — the combination of Service Value Chain activities, practices, and people that deliver a specific service outcome.

A typical IT value stream for deploying a new feature might show:

1. Customer request captured (minutes).
2. Product backlog grooming (days).
3. Sprint planning (hours).
4. Development (days–weeks).
5. Code review (hours–days).
6. Automated testing (minutes).
7. Manual testing (days).
8. Change approval (days — often the longest wait).
9. Deployment (hours).
10. Monitoring and validation (hours).

VSM reveals where time is lost. In many organizations, the change approval step alone accounts for 40–60% of total lead time. That is the bottleneck to address.

### VSM Output

A VSM exercise produces two maps:

- **Current state map:** How the value stream works today.
- **Future state map:** How it should work after improvements.

The gap between the two maps becomes the improvement roadmap.

---

## Slide 5: CI/CD in an ITSM Context (7:00–9:00)

We covered CI/CD technically in Module 12. Here we examine it from the governance and ITSM perspective.

### Change Enablement and CI/CD

One of the most productive integrations of ITIL and DevOps is embedding change governance into CI/CD pipelines.

In traditional ITIL, a Normal change required a change request, risk assessment, CAB review, and approval — a process measured in days. This was incompatible with teams deploying multiple times per day.

ITIL 4 addressed this with **Standard Changes** — pre-authorized, low-risk, well-documented changes that can be deployed without individual CAB approval. A CI/CD pipeline deployment that meets defined criteria (tests passed, code reviewed, within authorized window) can be treated as a standard change.

**Key principle:** The change process should be embedded in the pipeline — not a separate, manual, parallel process. Evidence of automated tests, security scans, and approvals lives in the pipeline log. The pipeline IS the change record.

### The Three Ways of DevOps

Gene Kim's "Three Ways" from "The Phoenix Project" provide a useful framework:

**First Way — Flow:** Optimize the flow of work from left (development) to right (operations to customer). Remove impediments, reduce batch sizes, eliminate handoff delays.

**Second Way — Feedback:** Create fast, amplified feedback loops at every stage. Make problems visible immediately. Monitoring in production feeds back to development in near real-time.

**Third Way — Continual Learning and Experimentation:** Create a culture of learning from failures, experimenting safely, and continuously improving. Directly parallels ITIL 4's Continual Improvement practice.

---

## Slide 6: Breaking Silos — The Wall of Confusion (9:00–10:45)

One of the defining achievements of the DevOps movement was naming the "Wall of Confusion" — the organizational divide between development and operations that creates dysfunction.

**Development incentives:** Deliver new features quickly. Frequent changes.

**Operations incentives:** Maintain stability. Minimize changes.

These opposing incentives create adversarial dynamics: developers blame operations for slow deployments; operations blames developers for unstable releases.

### Solutions

**Shared ownership:** "You build it, you run it" — developers take on-call responsibility for services they build. This creates a direct feedback loop between code quality and operational pain.

**Blameless post-mortems:** Instead of finding who caused an incident, analyze why the system allowed the incident to happen. Borrowed from aviation's safety culture, this practice is central to both DevOps and ITIL 4's continual improvement approach.

**Cross-functional teams:** Rather than siloed development and operations departments, organize teams around services or products. Each team has the skills to build, deploy, and operate their service.

**Platform engineering:** A dedicated platform team provides shared deployment infrastructure, tooling, and standards that all product teams use. This eliminates duplicate effort and creates consistent governance without siloed bureaucracy.

---

## Slide 7: Site Reliability Engineering (10:45–12:30)

**Site Reliability Engineering (SRE)** is Google's operationalized approach to reliability, described in the 2016 book "Site Reliability Engineering" by Beyer et al. SRE has been widely adopted across the industry and is deeply relevant to ITSM practitioners.

### Core SRE Concepts

**Service Level Objectives (SLOs):** Internal reliability targets — more specific than the SLAs in customer agreements. Example: "99.9% of API requests complete in under 200ms." SLOs are engineering targets.

**Service Level Indicators (SLIs):** The actual metrics used to measure whether SLOs are being met. Example: the 99th percentile response time measured by the monitoring system.

**Error Budget:** The allowable amount of unreliability derived from the SLO. If the SLO is 99.9% availability, the error budget is 0.1% — about 43 minutes per month. When the error budget is consumed, the team must stop new feature development and focus on reliability. When it is healthy, the team can deploy new features aggressively.

The error budget creates a mathematical bridge between development speed and operational stability — replacing the adversarial dynamic with a shared goal.

**Toil:** In SRE terminology, toil is manual, repetitive operational work that scales with service growth and provides no lasting improvement. Reducing toil through automation is an SRE priority — and directly embodies ITIL's "optimize and automate" principle.

### SRE and ITIL Alignment

- SLOs align with ITIL's Service Level Management practice.
- Error budgets provide a quantitative mechanism for the ITIL risk management approach to service changes.
- Blameless postmortems are SRE's version of ITIL's Problem Management practice.
- Toil reduction parallels ITIL's Continual Improvement practice.

---

## Slide 8: Agile and ITIL in Practice (12:30–14:00)

Agile software development and ITIL service management have historically operated in separate organizational layers — Agile in development, ITIL in operations. Modern organizations recognize these must integrate.

### Agile Ceremonies and ITSM

Agile ceremonies can double as ITSM activities:

- **Sprint retrospectives** are informal continual improvement sessions — surfacing process waste, tool issues, and collaboration problems.
- **Sprint reviews** are opportunities to involve service owners and customers in feature validation before release.
- **Definition of Done** can include ITSM requirements: change record created, release notes drafted, monitoring configured, runbook updated.

### Scaled Agile (SAFe) and ITIL

The Scaled Agile Framework (SAFe) is widely used in enterprise environments for coordinating multiple Agile teams. SAFe's Program Increment (PI) planning — a quarterly synchronization event — maps naturally to ITIL's release calendar and strategic planning cycles.

### Kanban and ITSM

Kanban — the visual workflow management method — is used in both Agile product development and ITSM service operations. IT operations teams use Kanban boards to manage:

- Incident queues.
- Service request backlogs.
- Change pipeline visualization.
- Continual improvement ideas.

---

## Slide 9: Key Terms Summary (14:00–15:15)

Key vocabulary for this module:

- **DevOps** — cultural and technical movement unifying development and operations.
- **Agile** — iterative software development methodology prioritizing working software and collaboration.
- **Value Stream Mapping (VSM)** — technique to visualize and optimize the flow of work.
- **CI/CD** — Continuous Integration / Continuous Delivery or Deployment.
- **Three Ways** — Flow, Feedback, Continual Learning (DevOps framework).
- **Wall of Confusion** — organizational divide between development and operations.
- **Blameless postmortem** — incident review focused on systemic causes, not individual fault.
- **Site Reliability Engineering (SRE)** — Google's approach to reliability through software engineering.
- **SLO (Service Level Objective)** — internal reliability target.
- **SLI (Service Level Indicator)** — metric measuring SLO attainment.
- **Error budget** — allowable unreliability derived from SLO.
- **Toil** — manual, repetitive operational work that scales without automation.
- **Platform engineering** — shared deployment infrastructure for product teams.
- **SAFe** — Scaled Agile Framework for enterprise coordination.

---

## Slide 10: Closing and Preview (15:15–16:00)

This brings Module 15 to a close. You now understand why ITIL 4 is positioned as compatible with, not opposed to, DevOps and Agile. The guiding principles, the Service Value System, and the practice-based architecture of ITIL 4 were all designed to accommodate modern delivery methods.

Module 16 is our final module — and it is special. We consolidate everything from the course into a comprehensive exam preparation session for the ITIL 4 Foundation certification. We review all key terms, walk through exam strategy, and work through 20 practice questions together.

Complete the reading guide, lab, and quiz for Module 15, then bring your best preparation to Module 16. Good luck — I'll see you there.

---

*End of Module 15 Video Script — approximately 238 lines*
