# Reading Guide: Module 07 — The Service Value Chain

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

## Certification Alignment: ITIL 4 Foundation

---

## Overview

This reading guide supports Module 07 of CIS-4335. Use it alongside the video lecture,
the ITIL 4 Foundation study resources, and the Axelos ITIL 4 Foundation publication.

The Service Value Chain (SVC) is one of the highest-weight topic areas on the ITIL 4
Foundation exam. Expect 4–7 questions on SVC activities, value streams, and the flow
of demand to value.

---

## Core Concept: The Service Value Chain in Context

The Service Value Chain is the central element of the **Service Value System (SVS)**. The
SVS has five components:

1. Guiding Principles
2. Governance
3. Service Value Chain
4. Practices
5. Continual Improvement

The SVC sits between the inputs (Opportunity/Demand) on one side and the outputs (Value)
on the other. It is the transformation engine.

---

## ITIL 4 Terminology Table — Service Value Chain

| Term | Definition |
|---|---|
| Service Value Chain (SVC) | An operating model comprising six interconnected activities that create, deliver, and continually improve services |
| Value Stream | A specific combination of activities and practices designed to produce a defined outcome for a given stakeholder scenario |
| Activity | A step within the SVC that transforms inputs to outputs; not a process, but a category of work |
| Demand | Signals of need from customers, users, or internal sources that trigger value chain activity |
| Value | The perceived benefits, usefulness, and importance of a service to stakeholders |
| Co-creation of Value | The principle that value is jointly produced by the service provider and consumer — not unilaterally |
| Input | Resources, information, or requirements consumed by an SVC activity |
| Output | Products of an SVC activity passed to other activities or external stakeholders |

---

## The Six SVC Activities — Detailed Reference

### Activity 1: Plan

**Purpose:** Ensures a shared understanding of the vision, current status, and improvement
direction for all four dimensions and all products and services across the organization.

**Key inputs:**

- Policies and requirements from Governance
- Demand signals from Engage
- Improvement initiatives from Improve
- Performance information from all other activities

**Key outputs:**

- Strategic, tactical, and operational plans
- Portfolio decisions
- Policies and standards
- Architectural decisions

**Exam tip:** Plan is a **continuous** activity, not a one-time event. It applies at
strategic, tactical, and operational levels simultaneously.

---

### Activity 2: Improve

**Purpose:** Ensures continual improvement of products, services, and all SVC activities
across the entire value chain and the four dimensions.

**Key inputs:**

- Performance information and improvement opportunities from all activities
- Stakeholder feedback from Engage
- Lessons learned from incidents, problems, and reviews

**Key outputs:**

- Improvement initiatives
- Value chain performance information
- Improvement plans and status reports

**Exam tip:** Improve is the only activity with a **bidirectional relationship with all
other activities**. It is never absent from a value stream.

---

### Activity 3: Engage

**Purpose:** Provides a good understanding of stakeholder needs, ensures transparency,
and maintains continual engagement and good relationships with all stakeholders.

**Key inputs:**

- Customer and user requests
- Stakeholder requirements
- Market opportunities
- Partner and supplier information

**Key outputs:**

- Consolidated requirements passed to Design and Transition
- Service requests routed to Deliver and Support
- Change or project initiation requests
- Contract requirements sent to Obtain/Build
- Feedback loops back to Plan and Improve

**Exam tip:** Engage is the **gateway** for all external demand. All customer-facing
interactions flow through Engage, including service desk contact initiation.

---

### Activity 4: Design and Transition

**Purpose:** Ensures that products and services continually meet stakeholder expectations
for quality, costs, and time-to-market.

**Key inputs:**

- Requirements and feedback from Engage
- Strategic direction from Plan
- Components and knowledge from Obtain/Build
- Improvement initiatives from Improve

**Key outputs:**

- New or changed products and services passed to Deliver and Support
- Components and knowledge artifacts passed to Obtain/Build
- Service transition information and documentation

**Exam tip:** This activity covers **both design AND transition** — designing the solution
AND managing the change into production. Change Management and Release Management practices
plug in here.

---

### Activity 5: Obtain/Build

**Purpose:** Ensures that service components are available when and where they are needed
and that they meet agreed specifications.

**Key inputs:**

- Architectural and technical specifications from Design and Transition
- Strategic direction from Plan
- Contract and supplier requirements from Engage
- Third-party components and services from Partners/Suppliers

**Key outputs:**

- Service components passed to Design and Transition (for testing/integration)
- Service components passed to Deliver and Support (for operations)
- Knowledge and information artifacts

**Exam tip:** Obtain/Build covers **both build (internal) and obtain (external procurement)**.
The decision of whether to build or buy is a key activity output decision.

---

### Activity 6: Deliver and Support

**Purpose:** Ensures that services are delivered and supported according to agreed
specifications and stakeholders' expectations.

**Key inputs:**

- New or changed services from Design and Transition
- Service components from Obtain/Build
- Service requests from Engage
- User and customer feedback

**Key outputs:**

- Services delivered to customers and users
- Fulfilled service requests
- Resolved incidents and operational issues
- Performance information flowing to Improve

**Exam tip:** This is the **operational activity** — the day-to-day running of IT services.
Service Desk, Incident Management, and Monitoring practices operate primarily here.

---

## Practice Maturity Comparison: SVC Activity Involvement

| Practice | Primary SVC Activity | Secondary SVC Activity |
|---|---|---|
| Service Desk | Deliver and Support | Engage |
| Incident Management | Deliver and Support | Improve |
| Change Enablement | Design and Transition | Plan |
| Problem Management | Improve | Deliver and Support |
| Service Level Management | Engage | Plan |
| Continual Improvement | Improve | All activities |
| Release Management | Design and Transition | Obtain/Build |
| Supplier Management | Obtain/Build | Engage |

---

## Value Streams — Key Concepts

A value stream is a **specific sequence** of SVC activities and practices used to create
a defined outcome. Value streams differ from the SVC itself:

| Concept | Description |
|---|---|
| Service Value Chain | The full model — all six activities available to be used |
| Value Stream | A specific pathway through selected activities for a given purpose |
| Practice | A set of resources and procedures supporting a goal — used within value streams |

**Characteristics of a good value stream:**

- Designed for a specific outcome (e.g., "resolve a P2 incident," "deploy a new application")
- Uses only the SVC activities needed for that outcome
- Eliminates waste (Lean principle) — no unnecessary steps
- Is documented and can be measured

**Common value stream examples:**

- Incident resolution
- Service request fulfillment
- New service introduction
- Change deployment
- Problem investigation and RCA

---

## Demand and Value — Flow Mechanics

**Demand** enters the SVC from two sources:

1. **External** — customers, users, and partners via Engage
2. **Internal** — strategic needs via Plan; improvement needs via Improve

**Value** exits the SVC in multiple forms:

- **Customer outcomes** — the results customers hired IT to achieve
- **Products and services** — the tangible deliverables
- **Customer experience** — how it felt to receive the service
- **Organizational benefits** — cost reduction, risk reduction, compliance

**The co-creation principle:** ITIL 4 states that value is not delivered **to** customers;
it is co-created **with** customers. The provider enables value. The customer realizes value
by using the service. Both parties must participate.

---

## Interconnection Patterns — How Activities Work Together

The diagram below represents common interaction flows (not exhaustive):

```text
Demand → Engage → Plan (requirements feed strategy)
Demand → Engage → Deliver and Support (service requests fulfilled)
Demand → Engage → Design and Transition (new service requirements)
Plan → Design and Transition (direction for new services)
Plan → Obtain/Build (strategic sourcing decisions)
Obtain/Build → Design and Transition (components for testing)
Design and Transition → Deliver and Support (new services go live)
Deliver and Support → Improve (performance data)
Improve → All activities (improvement initiatives)
All activities → Engage (status and output communicated to stakeholders)
```

---

## ITIL 4 Foundation Exam Tips — Module 07

The Foundation exam tests conceptual understanding, not deep technical knowledge.
For Module 07, focus on the following exam-relevant points:

**High-frequency exam topics:**

- Be able to identify which SVC activity is involved in a given scenario
- Know that the SVC is flexible and non-linear — activities can combine in any order
- Know that Improve touches all activities
- Know that Engage is the primary interface with external stakeholders
- Know that Design and Transition covers both design AND the change to production
- Understand the difference between the SVC and a value stream
- Understand co-creation of value

**Common distractor traps:**

- Confusing the SVC (a model with six activities) with the SVS (the full five-component system)
- Assuming SVC activities are sequential like a pipeline
- Forgetting that Improve interacts with every other activity
- Assuming "Deliver and Support" is the only activity that touches customers — Engage does too

**Practice scenario:** "A customer calls IT to request a new laptop. The request is logged,
approved, the laptop is procured, configured, and delivered." — Identify each SVC activity
involved. Answer: Engage (request received), Plan (budget/approval), Obtain/Build
(procurement), Design and Transition (configuration/testing), Deliver and Support
(delivery), Improve (tracking fulfillment performance).

---

## Glossary — Module 07 Terms

| Term | ITIL 4 Definition |
|---|---|
| Service Value System (SVS) | The model describing how all components and activities work together to facilitate value creation |
| Service Value Chain (SVC) | The set of six interconnected activities at the core of the SVS |
| Value Stream | A specific combination of activities designed for a given outcome |
| Demand | Input to the SVS — expressions of need from internal or external customers |
| Value | The perceived benefits, usefulness, and importance of something to stakeholder |
| Co-creation | The joint production of value by provider and consumer |
| Plan (activity) | SVC activity ensuring shared direction across all dimensions and services |
| Improve (activity) | SVC activity ensuring continual improvement across all activities |
| Engage (activity) | SVC activity managing stakeholder relationships and demand intake |
| Design and Transition | SVC activity ensuring services meet quality, cost, and time expectations |
| Obtain/Build | SVC activity ensuring service components are available per specifications |
| Deliver and Support | SVC activity ensuring ongoing service delivery per agreed expectations |

---

## Further Study Resources

- Axelos ITIL 4 Foundation publication — Chapter 4 (The ITIL Service Value System) and
  Chapter 5 (The ITIL Service Value Chain)
- ITIL 4 Foundation sample exam papers (Axelos official) — filter for SVC scenario questions
- Axelos MyITIL online resources — SVC interactive diagrams

---

---

## Supplemental Resources

**1. AXELOS — ITIL 4 Service Value Chain Activities**
<https://www.axelos.com/resource-hub/blog/itil-4-service-value-chain>
Official AXELOS explanation of all six SVC activities with descriptions, input/output tables, and examples of how they combine in value streams. Primary reference for Foundation exam SVC questions.

**2. Atlassian — Value Stream Mapping for Software Teams**
<https://www.atlassian.com/continuous-delivery/principles/value-stream-mapping>
A practitioner guide on applying value stream mapping to IT delivery workflows. Provides examples that translate directly into ITIL 4 SVC activity sequences and help visualize how value flows from demand to delivered outcome.

**3. ServiceNow — ITSM Value Stream Overview**
<https://www.servicenow.com/products/it-service-management/what-is-value-stream-management.html>
An industry practitioner overview of value stream management as applied in ITSM platforms. Shows how ServiceNow maps real workflows to SVC-aligned value streams, bridging ITIL 4 theory to enterprise tool implementation.

---

Module 07 Reading Guide | CIS-4335 IT Service Management | Texas Wesleyan University
