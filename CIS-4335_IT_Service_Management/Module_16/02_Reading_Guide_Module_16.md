# Reading Guide: Module 16 — ITIL 4 Foundation Exam Preparation

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

This guide is your comprehensive exam preparation reference. It consolidates the key concepts, terminology, and practice knowledge from all sixteen modules into a single organized review document. Use it alongside the Module 16 video lecture, the practice quiz, and the official Axelos ITIL 4 Foundation study resources.

The ITIL 4 Foundation exam consists of 40 multiple-choice questions, requires 26 correct answers (65%) to pass, and must be completed in 60 minutes. There is no negative marking.

---

## Exam Format Summary

| Attribute | Detail |
|---|---|
| Number of questions | 40 |
| Pass mark | 26 correct (65%) |
| Time limit | 60 minutes |
| Question format | Multiple choice, one correct answer per question |
| Closed book | Yes — no materials permitted |
| Negative marking | No — always answer every question |
| Delivery | Online proctored (PeopleCert) or test center |
| Certification body | Axelos / PeopleCert |

---

## Part 1: The Service Value System

### Five Components of the SVS

The ITIL 4 Service Value System (SVS) describes how all components and activities of an organization work together to enable value creation. The five components are:

1. **Guiding Principles** — seven principles that guide decisions and actions in any circumstances
2. **Governance** — how the organization is directed and controlled
3. **Service Value Chain** — six interconnected activities that combine to create value
4. **Practices** — 34 sets of organizational resources for performing work
5. **Continual Improvement** — ongoing effort to improve all aspects of products, services, and practices

### The Seven Guiding Principles

Memorize all seven — they are tested directly and in scenario questions.

| Principle | Core Message |
|---|---|
| Focus on Value | Everything the organization does should link, directly or indirectly, to value for stakeholders |
| Start Where You Are | Do not start from scratch; assess and build on what exists |
| Progress Iteratively with Feedback | Work in iterations; use feedback to adapt |
| Collaborate and Promote Visibility | Work together; make information accessible |
| Think and Work Holistically | No service or practice operates in isolation |
| Keep It Simple and Practical | Eliminate what adds no value; use minimum necessary steps |
| Optimize and Automate | First optimize, then automate what remains |

### The Service Value Chain

Six activities that combine in flexible sequences (value streams) to deliver value:

- **Plan** — ensure shared understanding of vision, status, and improvement directions
- **Improve** — ensure continual improvement across products, services, and practices
- **Engage** — provide good understanding of stakeholder needs and facilitate transparency
- **Design and Transition** — ensure products and services continually meet stakeholder expectations
- **Obtain/Build** — ensure service components are available when needed
- **Deliver and Support** — ensure services are delivered and supported to meet agreed specifications

### The Four Dimensions of Service Management

The four dimensions must be considered for every service and practice. PESTLE factors form the external environment surrounding all four dimensions.

1. **Organizations and People** — roles, responsibilities, culture, and skills
2. **Information and Technology** — data, knowledge, and technology tools
3. **Partners and Suppliers** — relationships with other organizations supporting service delivery
4. **Value Streams and Processes** — how work flows from demand to value

---

## Part 2: Key Value Terminology

These definitions are among the most tested items on the Foundation exam.

| Term | Definition |
|---|---|
| Service | Means of enabling value co-creation by facilitating outcomes customers want to achieve without managing specific costs and risks |
| Value | Perceived benefits, usefulness, and importance of something — co-created by provider and customer |
| Product | Configuration of resources designed to offer value to a consumer |
| Utility | Functionality offered to meet a particular need — "fit for purpose" |
| Warranty | Assurance that a product or service will meet agreed requirements — "fit for use" |
| Output | Tangible or intangible deliverable of an activity |
| Outcome | Result for a stakeholder enabled by outputs |
| Cost | Amount of money spent on a specific activity or resource |
| Risk | Possible event that could cause harm or loss or affect the ability to achieve objectives |
| Customer | Person who defines service requirements and takes responsibility for outcomes |
| User | Person who uses services |
| Sponsor | Person who authorizes budget for service consumption |

### Utility vs. Warranty

This distinction is directly tested. A service has utility if it does what the customer needs (fit for purpose). A service has warranty if it is available when needed, with sufficient capacity, in a secure manner, and continuously (fit for use). Both are required for a service to deliver value.

---

## Part 3: Most Tested Practices

### Incident Management

**Purpose:** Minimize the negative impact of incidents by restoring normal service operation as quickly as possible.

**Incident:** An unplanned interruption to or reduction in the quality of a service.

**Major incident:** Incident requiring a dedicated team with a separate response procedure due to highest-category impact.

**Priority:** Determined by combining impact (breadth of effect) and urgency (speed required). Priority determines response and resolution targets.

**Exam distinctions:**

- Incident Management restores service; Problem Management finds root causes — do not confuse these.
- Incidents are reactive; problems are proactive and reactive.

### Problem Management

**Purpose:** Reduce the likelihood and impact of incidents by identifying actual and potential causes and managing workarounds and known errors.

**Problem:** Cause, or potential cause, of one or more incidents. Root cause is not yet known when a problem is identified.

**Known error:** Problem where the root cause has been identified and a workaround exists. The known error is managed until a permanent fix is implemented.

**Workaround:** Temporary solution that reduces or eliminates the impact of a problem without resolving it.

**Three phases:** Problem identification → Problem control → Error control.

### Change Enablement

**Purpose:** Maximize the number of successful IT changes by ensuring risks are properly assessed, authorized changes are prioritized, and the change schedule is managed.

| Change Type | Description | Authorization |
|---|---|---|
| Standard | Pre-authorized, low-risk, follows documented procedure | Pre-authorized as a class — no individual CAB review |
| Normal | Requires individual risk assessment before authorization | Assessed and authorized through defined process; CAB may be consulted |
| Emergency | Requires immediate action; expedited authorization | Expedited process; may be reviewed by ECAB or post-hoc |

**Change Advisory Board (CAB):** Body that advises the change authority on the assessment, prioritization, and scheduling of changes. Not every change goes to the CAB — only those that warrant advisory input.

### Service Request Management

**Purpose:** Support agreed quality by handling all pre-defined, user-initiated service requests effectively and in a user-friendly manner.

**Service request:** A formal request from a user for something to be provided. Examples: password reset, access request, request for information, hardware request.

**Exam trap:** Service requests are NOT incidents. A password reset is a service request; an account locked due to a system error is an incident.

### Service Level Management

**Purpose:** Set clear, business-based targets for service levels and ensure delivery is assessed, monitored, and managed against those targets.

| Agreement | Parties | Nature |
|---|---|---|
| SLA | Service provider and customer | Documented service targets |
| OLA | Service provider and internal support team | Internal commitments underpinning SLA |
| UC (Underpinning Contract) | Service provider and external supplier | Legally binding contract |

**Watermelon SLA:** All metrics green but customer satisfaction is low — the measured metrics do not reflect what customers actually care about.

### Service Desk

**Purpose:** Capture demand for incident resolution and service requests.

**Shift-left:** Moving resolution capability closer to users — self-service, knowledge articles, automated resolution. Reduces cost and improves speed.

**Omnichannel:** Multiple contact channels (phone, chat, email, portal, walk-in) that provide a seamless, integrated user experience.

### IT Asset Management

**Purpose:** Plan and manage the full lifecycle of all IT assets to maximize value, control costs, manage risks, support decision-making, and meet regulatory requirements.

**Asset lifecycle:** Planning → Procurement → Deployment → Maintenance/Operation → Retirement → Disposal.

**SAM risks:** Under-licensing (compliance risk) and over-licensing (financial waste).

**Secure disposal:** Hardware containing data requires sanitization (physical destruction, cryptographic erasure, or software overwrite) before disposal.

### Release and Deployment Management

**Purpose:** Make new and changed services and features available for use.

**Deployment approaches:** Big bang (all at once), Phased (staged by group/region), Canary (small percentage first), Blue-green (two environments, instant traffic switch).

**Rollback planning** is required for every deployment. Database schema rollbacks are most complex.

**Post-implementation review (PIR):** Evaluates whether the release achieved its intended outcomes; feeds Continual Improvement.

### Continual Improvement

**Purpose:** Align practices and services with changing business needs through ongoing improvement.

**Continual Improvement Model (7 steps):** What is the vision? → Where are we now? → Where do we want to be? → How do we get there? → Take action → Did we get there? → How do we keep the momentum going?

**Continual Improvement Register:** Document tracking all improvement opportunities across the organization.

---

## Part 4: Additional Practices — High-Level Purpose Statements

Know the purpose of every practice at the Foundation level.

| Practice | Purpose |
|---|---|
| Availability Management | Ensure services deliver agreed levels of availability |
| Capacity and Performance Management | Ensure services achieve agreed and expected performance |
| IT Asset Management | Plan and manage full IT asset lifecycle |
| Monitoring and Event Management | Observe services and CI states; record and report events |
| Service Configuration Management | Ensure accurate CI information is available |
| Service Continuity Management | Ensure service availability at required levels in major disruption events |
| Information Security Management | Protect organizational information assets |
| Supplier Management | Ensure supplier performance supports agreed service levels |
| Service Design | Design products and services fit for purpose, use, and continued improvement |
| Service Catalogue Management | Provide single source of consistent information about all services |

---

## Part 5: Relationships Between Practices

The exam frequently tests relationships between practices. Key relationships to know:

**Incident Management → Problem Management:** Major incidents and recurring incidents trigger problem investigations. Problem Management identifies root causes that Incident Management cannot address.

**Change Enablement → Release and Deployment Management:** Changes are authorized by Change Enablement; Release and Deployment Management executes the deployment of authorized releases.

**IT Asset Management → Service Configuration Management:** Assets are tracked in CMDB as configuration items. The two practices share data but have different purposes — Asset Management focuses on value/lifecycle; Configuration Management focuses on CI attributes and relationships.

**Service Level Management → Service Desk:** SLM sets the targets (response time, resolution time) that the Service Desk must meet in day-to-day operations.

**Continual Improvement → All Practices:** Continual Improvement draws inputs from PIRs, incident patterns, problem investigations, and service reviews across all practices.

---

## Part 6: Exam Strategy

### Before the Exam

- Complete all module quizzes and review any questions answered incorrectly
- Practice timed sessions with 40-question practice exams — simulate exam conditions
- Review purpose statements for all practices until you can state them from memory
- Know all seven guiding principles and be able to apply them to scenarios

### During the Exam

1. Read each question and scenario carefully before looking at the answer choices
2. Identify what the question is testing (purpose, definition, relationship, or application)
3. Eliminate the two obviously wrong answers first
4. If stuck between two answers, return to purpose statements — the correct answer aligns with the stated purpose of the practice
5. Answer every question — no negative marking means a guess is always better than a blank
6. Use remaining time to review flagged questions, not to second-guess confident answers

### Common Exam Traps

- Confusing Incident Management (restore service) with Problem Management (find root cause)
- Confusing service requests with incidents
- Reversing the SLA/OLA/UC relationships
- Selecting an answer that describes a reasonable-sounding practice that does not exist in ITIL 4
- Confusing utility (fit for purpose) with warranty (fit for use)

---

## Part 7: Career Pathways in ITSM

### ITIL 4 Certification Levels

| Level | Modules | Target Audience |
|---|---|---|
| Foundation | This course | Anyone entering ITSM |
| Managing Professional | CDS, DSV, HVIT, DPI | Practitioners in IT operations and delivery |
| Strategic Leader | DPI, DITS | Senior managers and executives |
| Master | Demonstrated application | Experienced ITSM leaders |

### ITSM Career Roles

Entry-level roles that benefit directly from ITIL 4 Foundation certification:

- Service Desk Analyst / Agent
- IT Support Specialist
- Change Management Coordinator
- Incident Manager (Associate)

Mid-level roles:

- Service Delivery Manager
- ITSM Process Owner
- IT Operations Manager
- Problem Manager

Senior roles:

- ITSM Director
- Chief Information Officer (CIO)
- Chief Information Security Officer (CISO)
- IT Governance Manager

---

## Exam Day Checklist

- [ ] Know all seven guiding principles and their core messages
- [ ] Know the five components of the SVS
- [ ] Know the six Service Value Chain activities
- [ ] Know the four dimensions of service management
- [ ] Know the purpose of every practice tested in this course
- [ ] Know the utility vs. warranty distinction
- [ ] Know all three change types and their authorization models
- [ ] Know the SLA/OLA/UC distinction
- [ ] Know the watermelon SLA concept
- [ ] Know the continual improvement model (7 steps)
- [ ] Have reviewed all module quizzes and practice questions
- [ ] Have completed at least one timed 40-question practice exam
