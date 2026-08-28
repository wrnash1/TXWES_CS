# Reading Guide: Module 16 — ITIL 4 Foundation Exam Preparation and Capstone

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4335 &BULL; IT SERVICE MANAGEMENT & ITIL FRAMEWORKS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

This reading guide is your comprehensive review document for the ITIL 4 Foundation certification exam. It consolidates the key terms, frameworks, and concepts from the entire course. Use it as a study reference in the days before your exam. Focus on areas where you feel less confident — do not simply re-read content you already know well.

**Recommended approach:** Read through once, then use the self-check questions at the end of each section to test recall. For any question you cannot answer confidently, return to the relevant module's reading guide.

**Estimated study time:** 3–4 hours (spread across multiple sessions)

---

## Section 1: ITIL 4 Foundation — What You Must Know

### 1.1 The ITIL 4 Certification Landscape

ITIL 4 has a structured certification scheme:

- **ITIL 4 Foundation** — entry level. Covers the key concepts of ITIL 4 and service management. This is the certification this course prepares you for.
- **ITIL 4 Managing Professional (MP)** — advanced. Four modules: High Velocity IT, Specialist Direct, Plan & Improve, Create Deliver & Support.
- **ITIL 4 Strategic Leader (SL)** — senior level. Two modules: Digital and IT Strategy, Directing, Planning, and Improving.
- **ITIL Master** — requires demonstrated application across multiple real-world ITIL assignments.

The Foundation exam is the gateway to all higher-level certifications.

### 1.2 Core ITIL 4 Vocabulary

**Service:** A means of enabling value co-creation by facilitating outcomes that customers want to achieve, without the customer having to manage specific costs and risks.

**IT service management (ITSM):** The implementation and management of quality IT services that meet the needs of the business.

**Value:** The perceived benefits, usefulness, and importance of something. Value is always co-created by the provider and the consumer — neither alone determines value.

**Outcome:** A result for a stakeholder enabled by one or more outputs. Outcomes are what customers ultimately want; outputs are what providers deliver.

**Output:** A tangible or intangible deliverable from an activity.

**Cost:** The amount of money spent on a specific activity or resource.

**Risk:** A possible event that could cause harm or loss.

**Utility:** The functionality offered by a product or service to meet a particular need. "Fit for purpose."

**Warranty:** Assurance that a product or service will meet agreed requirements. "Fit for use." Warranty covers availability, capacity, security, and continuity.

**Value = Utility + Warranty.** Both are required. A service that works but is always unavailable provides no warranty and therefore no value. A service that is always available but does not meet the need provides no utility.

---

## Section 2: The Four Dimensions of Service Management

All services must be designed, managed, and improved considering all four dimensions. External factors (PESTLE) affect all dimensions.

### 2.1 Dimension 1: Organizations and People

Covers: organizational structures, roles and responsibilities, culture, staffing and skills.

**Key concepts:**

- Clear responsibilities and accountability are prerequisites for effective service management.
- Organizational culture must support the values, attitudes, and behaviors required.
- Capability gaps must be identified and addressed through training, hiring, or partnering.

### 2.2 Dimension 2: Information and Technology

Covers: information required to manage services, technologies used to deliver services.

**Key concepts:**

- Information architecture must be designed alongside service design.
- Technology choices (cloud, AI, automation, analytics) affect service capabilities.
- Information must be managed with appropriate security and compliance controls.

### 2.3 Dimension 3: Partners and Suppliers

Covers: relationships with external organizations providing services or components.

**Key concepts:**

- Supplier strategy varies from commodity (transactional) to strategic partnership.
- Third-party dependencies are risks that must be managed.
- Contracts, SLAs, and performance management are ITAM and Supplier Management responsibilities.

### 2.4 Dimension 4: Value Streams and Processes

Covers: the activities and workflows through which the organization creates value.

**Key concepts:**

- A value stream is a series of steps to create and deliver a service outcome.
- Processes define how activities are performed — inputs, outputs, triggers, controls.
- Lean thinking (eliminate waste, optimize flow) applies to process design.

### 2.5 PESTLE External Factors

The four dimensions exist within an external environment shaped by:

- **Political** — government policy, regulations, political stability.
- **Economic** — market conditions, inflation, funding availability.
- **Social** — demographics, customer expectations, workforce culture.
- **Technological** — innovation, automation, cybersecurity landscape.
- **Legal** — laws, regulations, compliance requirements.
- **Environmental** — sustainability requirements, climate risk.

---

## Section 3: The Service Value System

### 3.1 SVS Overview

The Service Value System (SVS) represents how all the components and activities of an organization work together to facilitate value creation. It has five components:

1. Guiding Principles
2. Governance
3. Service Value Chain
4. Practices
5. Continual Improvement

**Input:** Opportunity and Demand.

**Output:** Value.

### 3.2 The Seven Guiding Principles

All seven guiding principles apply in all contexts. They are not sequential or exclusive — multiple principles often apply simultaneously.

| Principle | Core idea |
|---|---|
| Focus on Value | Every activity must link to value for stakeholders |
| Start Where You Are | Assess the current state; reuse what works |
| Progress Iteratively with Feedback | Small steps with feedback loops; avoid big-bang changes |
| Collaborate and Promote Visibility | Break silos; share information widely |
| Think and Work Holistically | No practice works in isolation; consider the whole system |
| Keep It Simple and Practical | Eliminate steps that add no value; only enough process |
| Optimize and Automate | Use automation to reduce manual effort and error |

### 3.3 Governance

Governance is the means by which an organization is directed and controlled. It ensures the organization achieves its objectives and manages risks.

**Three components of governance:**

- **Direct:** Set direction and strategy.
- **Monitor:** Track performance against objectives.
- **Evaluate:** Assess results and learn.

### 3.4 The Six Service Value Chain Activities

The SVC is the core operating model. Each activity transforms inputs into outputs. Multiple value streams are possible — different combinations of activities for different service types.

| Activity | Primary contribution |
|---|---|
| Plan | Shared understanding, strategy, policy |
| Improve | Continual improvement of all components |
| Engage | Stakeholder needs, transparency, feedback |
| Design and Transition | New/changed services ready for operation |
| Obtain/Build | Components acquired or developed |
| Deliver and Support | Services available and supported |

---

## Section 4: The 34 ITIL 4 Practices

### 4.1 Practice Groups

**General Management (14 practices):** Architecture Management, Continual Improvement, Information Security Management, Knowledge Management, Measurement and Reporting, Organizational Change Management, Portfolio Management, Project Management, Relationship Management, Risk Management, Service Financial Management, Strategy Management, Supplier Management, Workforce and Talent Management.

**Service Management (17 practices):** Availability Management, Business Analysis, Capacity and Performance Management, Change Enablement, Incident Management, IT Asset Management, Monitoring and Event Management, Problem Management, Release Management, Service Catalogue Management, Service Configuration Management, Service Continuity Management, Service Design, Service Desk, Service Level Management, Service Request Management, Service Validation and Testing.

**Technical Management (3 practices):** Deployment Management, Infrastructure and Platform Management, Software Development and Management.

### 4.2 Foundation-Scope Practice Reference

**Continual Improvement (General Management)**

- Purpose: Align practices with changing organizational needs through ongoing improvement of products, services, and practices.
- The Continual Improvement Model: 7-step loop from "what is the vision?" to "how do we keep the momentum going?"
- Continual Improvement Register (CIR): records all improvement ideas with status and priority.

**Change Enablement (Service Management)**

- Purpose: Maximize successful service and product changes by ensuring risks are properly assessed, authorizing changes to proceed, and managing a change schedule.
- Change types: Standard (pre-authorized), Normal (needs authorization), Emergency (expedited for urgency).
- Change Authority: Person or group authorizing changes. Varies by type and risk level.
- Change Advisory Board (CAB): Advisory body for Normal changes.

**Incident Management (Service Management)**

- Purpose: Minimize the negative impact of incidents by restoring normal service operation as quickly as possible.
- Incident: Unplanned interruption or reduction in quality of an IT service.
- Major incident: Highest impact/urgency; requires special procedure and post-incident review.
- Workaround: Temporary solution reducing or eliminating impact while awaiting full resolution.
- Escalation types: Functional (expertise), Hierarchical (authority/urgency).

**Problem Management (Service Management)**

- Purpose: Reduce likelihood and impact of incidents by identifying actual and potential causes and managing workarounds and known errors.
- Problem: Unknown cause of one or more incidents.
- Known error: A problem with documented root cause, whether or not a workaround exists.
- Problem lifecycle phases: Problem identification → Problem control → Error control.

**Service Request Management (Service Management)**

- Purpose: Support agreed quality of a service by handling service requests in an effective and user-friendly manner.
- Service request: Formal request for information, advice, standard change, or something the user is entitled to as part of normal service.
- Must be distinguished from incidents (something is broken) and changes (unauthorized modification needed).

**Service Desk (Service Management)**

- Purpose: Capture demand for incident resolution and service requests; provide a single point of contact for users.
- Must have empathy, communication skills, and understanding of user needs.
- Formats: Local, centralized, virtual, follow-the-sun.

**Service Level Management (Service Management)**

- Purpose: Set clear, business-based targets for service levels and ensure services are monitored, measured, and reported.
- SLA: Service Level Agreement (provider-customer).
- OLA: Operational Level Agreement (internal teams).
- UC: Underpinning Contract (provider-external supplier).
- Watermelon SLA: Appears green (metrics pass) but customers experience red (poor service). Caused by measuring the wrong metrics.

---

## Section 5: Key Frameworks and Tools

### 5.1 The Continual Improvement Model

The seven-step CI model asks:

1. What is the vision? (Strategic goal)
2. Where are we now? (Baseline assessment)
3. Where do we want to be? (Target state)
4. How do we get there? (Improvement plan)
5. Take action. (Implement)
6. Did we get there? (Measure and evaluate)
7. How do we keep the momentum going? (Embed and sustain)

### 5.2 Risk Response Strategies

The four strategies for responding to identified risks:

- **Avoid:** Eliminate the activity creating the risk.
- **Transfer:** Shift financial impact to a third party (insurance, contracts).
- **Mitigate (Reduce):** Take actions to reduce likelihood or impact.
- **Accept:** Acknowledge and document; take no further action (requires management sign-off).

### 5.3 Asset Lifecycle Stages

1. Request and Acquisition
2. Deployment
3. Operation and Maintenance
4. Refresh or Replace decision
5. Retirement
6. Disposal

### 5.4 Deployment Strategies

- **Big bang:** All users at once.
- **Phased:** Incremental by group or region.
- **Canary:** Small percentage of traffic to new version; expand if successful.
- **Blue/green:** Two parallel environments; traffic switched at cutover.

### 5.5 DORA Metrics

The four DevOps Research and Assessment metrics:

- Deployment frequency.
- Lead time for changes.
- Change failure rate.
- Mean time to restore (MTTR).

---

## Section 6: Common Exam Traps and Tips

### Trap 1: Confusing Incident, Problem, and Change

- Something is broken and needs immediate restoration → **Incident Management.**
- Something keeps breaking and you need to find out why → **Problem Management.**
- You want to make a planned modification to the environment → **Change Enablement.**
- A user wants something they are entitled to → **Service Request Management.**

### Trap 2: SLA vs. OLA vs. UC

- **SLA:** Between IT and the external customer (or business unit).
- **OLA:** Between IT teams internally (e.g., network team supports the service desk).
- **UC:** Between IT and an external vendor who supports delivery (e.g., hosting provider).

### Trap 3: Value Requires Both Utility AND Warranty

Never say a service has value if utility OR warranty is missing. The exam will test scenarios where one is present but not the other.

### Trap 4: Guiding Principles Are Not Sequential

Do not apply them in order 1–7. In any scenario, multiple principles may be relevant. Choose the most relevant one for the specific context described.

### Trap 5: The Service Value Chain Is Not Linear

Demand enters and value exits. In between, activities combine in many ways depending on the value stream. The SVC is not a waterfall from Plan through Deliver.

### Trap 6: Practices vs. Processes

ITIL 4 uses "practices" — not "processes." Practices are broader; they include people, tools, partners, and information in addition to processes. Never describe ITIL 4 as a process framework — it is a practice-based framework.

---

## Section 7: All Key Terms Quick Reference

This section provides a consolidated glossary. Review all terms before the exam.

**Availability** — proportion of time a service is functional.

**CMDB** — Configuration Management Database; repository of CI records and relationships.

**Configuration item (CI)** — component managed in the CMDB.

**Demand** — need or desire for services from internal and external customers.

**Error budget** — allowable unreliability derived from SLO.

**Event** — change of state significant to CI or service management.

**Four Dimensions** — Organizations & People, Information & Technology, Partners & Suppliers, Value Streams & Processes.

**Governance** — means by which organization is directed and controlled.

**Guiding Principles** — seven recommendations guiding decisions across ITIL 4.

**Incident** — unplanned interruption or reduction in quality of a service.

**Known error** — problem with documented root cause and/or workaround.

**Lifecycle (asset)** — acquire, deploy, operate, refresh, retire, dispose.

**Major incident** — highest-impact incident requiring special procedure.

**Outcome** — result for a stakeholder enabled by one or more outputs.

**PESTLE** — Political, Economic, Social, Technological, Legal, Environmental.

**Problem** — unknown cause of one or more incidents.

**Release** — version of service or component available for deployment.

**Residual risk** — risk remaining after controls applied.

**Risk** — possible event causing harm or difficulty achieving objectives.

**Service** — means of enabling value co-creation without customer managing costs/risks.

**Service consumer** — organization using services (includes customer, user, sponsor).

**Service offering** — description of services available to a consumer.

**Service provider** — organization delivering services.

**Service relationship** — cooperation between provider and consumer.

**Service request** — request from user for something they are entitled to.

**Service Value Chain** — six activities transforming demand into value.

**Service Value System (SVS)** — how all components work together to create value.

**SLA** — Service Level Agreement (customer-facing).

**SLI** — Service Level Indicator (measurement metric).

**SLO** — Service Level Objective (internal reliability target).

**Standard change** — pre-authorized, low-risk change.

**SVS inputs** — Opportunity, Demand.

**SVS output** — Value.

**Toil** — manual, repetitive work that scales without automation.

**Utility** — functionality of a service; fit for purpose.

**Value** — perceived benefits relative to cost.

**Value stream** — series of steps creating and delivering a service outcome.

**Warranty** — assurance of availability, capacity, security, continuity; fit for use.

**Watermelon SLA** — green metrics, red customer experience.

**Workaround** — temporary solution reducing incident impact.

---

## Self-Check Questions

Answer these before consulting notes:

1. What are the seven Guiding Principles of ITIL 4?
2. What are the six Service Value Chain activities?
3. What is the difference between utility and warranty?
4. What are the four dimensions of service management?
5. What are the three change types in Change Enablement?
6. Define incident, problem, known error, and workaround.
7. What is the purpose of the Service Desk practice?
8. What does the acronym PESTLE stand for?
9. What are the inputs and output of the Service Value System?
10. What are the four risk response strategies?
11. What is a service request? Give two examples.
12. What is the Watermelon SLA effect?
13. What are the DORA four key metrics?
14. Define residual risk.
15. What is the difference between an SLA, OLA, and underpinning contract?

---

*End of Module 16 Reading Guide — approximately 265 lines*
