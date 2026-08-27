# Reading Guide: Module 05 — Service Value Chain Activities

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** ITIL 4 Foundation

---

## Purpose of This Guide

This reading guide supports Module 05 of CIS-4335. The six Service Value Chain activities are core exam content. You must know the purpose, key inputs, and key outputs of each activity, and you must be able to map scenarios and practices to activities.

---

## 1. SVC Architecture Overview

The Service Value Chain is the operational core of the ITIL 4 Service Value System. It converts demand and opportunity into delivered value through six interconnected activities. These activities do not execute in a fixed linear sequence — they are combined in flexible patterns called value streams, appropriate to the type of work being done.

All six activities have a bidirectional relationship with the Improve activity. Every activity contributes improvement data to Improve, and every activity receives improvement guidance from Improve.

---

## 2. The Six SVC Activities — Complete Reference

### Plan

Purpose: Ensure a shared understanding of the vision, current status, and improvement direction for all four dimensions and all products and services across the organization.

Plan is the alignment mechanism of the SVC. It produces the strategic direction that all other activities rely on.

| Inputs | Outputs |
|---|---|
| Stakeholder demand and opportunities | Strategic plans and portfolios |
| Policies from governance | Architectural decisions |
| Performance reports from Deliver and Support | Policies for other SVC activities |
| Improvement status from Improve | Product and service portfolio updates |

---

### Improve

Purpose: Ensure continual improvement of products, services, and practices across all value chain activities and the four dimensions of service management.

Improve is the only activity that connects bidirectionally to all other activities simultaneously. It is both an activity and a practice (covered in Module 06).

| Inputs | Outputs |
|---|---|
| Performance data from all SVC activities | Improvement initiatives and plans |
| Customer and stakeholder feedback | Performance evaluation reports |
| Audit results and assessments | Updates to all other SVC activities |
| Continual Improvement Register entries | Improvement status reports |

---

### Engage

Purpose: Provide a good understanding of stakeholder needs, set the direction for service delivery and continuous engagement, and establish good relationships with all stakeholders.

Engage is the voice of the consumer inside the SVC. It translates external demand into actionable requirements.

| Inputs | Outputs |
|---|---|
| Demand and opportunities from consumers | Stakeholder requirements and expectations |
| Service performance data | Change and service requests |
| Market intelligence | Customer feedback and satisfaction data |
| Third-party service information | Contracts and agreements |

---

### Design and Transition

Purpose: Ensure that products and services continually meet stakeholder expectations for quality, costs, and time to market.

Design and Transition covers the full arc of designing, testing, and transitioning new or changed services into live operation.

| Inputs | Outputs |
|---|---|
| Requirements from Engage | Service designs and architectures |
| Architectural decisions from Plan | Tested service components |
| Service components from Obtain/Build | Transition plans and documentation |
| Improvement initiatives from Improve | New and changed service documentation |

---

### Obtain/Build

Purpose: Ensure that service components are available when and where they are needed and meet agreed specifications.

Obtain/Build is where service components are acquired from external sources or built internally.

| Inputs | Outputs |
|---|---|
| Architectures from Design and Transition | Service components (acquired or built) |
| Specifications from Plan | Evaluation reports |
| Contracts and agreements from Engage | Updated asset and configuration records |
| Improvement initiatives from Improve | Knowledge articles and documentation |

---

### Deliver and Support

Purpose: Ensure that services are delivered and supported according to agreed specifications and stakeholders' expectations.

Deliver and Support is where day-to-day service operation occurs — service desk, incident resolution, request fulfillment, monitoring, and ongoing support.

| Inputs | Outputs |
|---|---|
| New and changed services from Design and Transition | Delivered services |
| Service components from Obtain/Build | Resolved incidents and fulfilled requests |
| User and stakeholder requests via Engage | Service performance data |
| Policies and plans from Plan | Improvement opportunities for Improve |

---

## 3. SVC Activities Quick Reference

| Activity | Core Purpose | Key Output | Primary Practices Enabled |
|---|---|---|---|
| Plan | Strategic alignment and direction | Plans, portfolios, policies | Strategy Management, Portfolio Management |
| Improve | Continual improvement across all activities | Improvement plans and initiatives | Continual Improvement |
| Engage | Stakeholder understanding and relationship management | Requirements, contracts, feedback | Relationship Management, Service Level Management |
| Design and Transition | Quality services ready for deployment | Tested components, transition plans | Change Enablement, Service Design, Service Validation |
| Obtain/Build | Available, specification-compliant service components | Built or acquired components | Deployment Management, Software Development |
| Deliver and Support | Live service delivery and user support | Delivered services, resolved incidents | Incident Management, Service Desk, Service Request Management |

---

## 4. The Improve Activity — Special Role

The Improve activity is unique among the six because it connects bidirectionally to all others. This means:

* Every other activity produces outputs that feed into Improve (performance data, incidents, user feedback, lessons learned).
* Improve produces outputs that feed back into every other activity (improvement plans, updated policies, performance evaluations).

No activity is exempt from contributing to improvement, and no activity is exempt from being improved. This is how ITIL 4 embeds continual improvement throughout the entire operating model rather than treating it as a separate phase.

---

## 5. Value Streams — How Activities Combine

A value stream is a series of steps (SVC activities) combined to create and deliver a specific product or service to a consumer. Organizations have multiple value streams serving different purposes.

### Common Value Stream Patterns

| Scenario | Typical Activity Sequence |
|---|---|
| New service deployment | Plan → Engage → Design and Transition → Obtain/Build → Deliver and Support → Improve |
| Incident resolution | Engage → Deliver and Support → Improve |
| Service request fulfillment | Engage → Obtain/Build → Deliver and Support |
| Service improvement initiative | Improve → Plan → Design and Transition → Obtain/Build → Deliver and Support |
| Vendor contract renewal | Engage → Plan → Obtain/Build |

Note: These are typical patterns, not mandatory sequences. Organizations adapt value streams to their specific context.

---

## 6. Practices Connected to SVC Activities

Practices provide the organizational capability that enables SVC activities. Most practices contribute to multiple activities.

### Practice-to-Activity Connections

| Practice | Primary SVC Activity | Secondary Activities |
|---|---|---|
| Incident Management | Deliver and Support | Improve, Engage |
| Service Desk | Deliver and Support | Engage |
| Service Request Management | Deliver and Support | Obtain/Build |
| Change Enablement | Design and Transition | Plan, Obtain/Build |
| Deployment Management | Obtain/Build | Design and Transition, Deliver and Support |
| Service Level Management | Engage | Deliver and Support, Plan |
| Continual Improvement | Improve | All activities |
| Knowledge Management | Deliver and Support | Improve, Design and Transition |
| Problem Management | Improve | Deliver and Support |

---

## 7. ITIL v3 SVC vs. ITIL 4 SVC

Students with prior ITIL v3 knowledge should note the differences between the ITIL v3 lifecycle phases and the ITIL 4 SVC activities.

| ITIL v3 Phase | ITIL 4 Closest Equivalent | Key Difference |
|---|---|---|
| Service Strategy | Plan | Plan is ongoing, not a one-time phase |
| Service Design | Design and Transition | Combined with transition; not a separate phase |
| Service Transition | Design and Transition | Combined with design; not a separate phase |
| Service Operation | Deliver and Support | More focused; does not contain design activities |
| Continual Service Improvement | Improve | Embedded throughout the SVC, not a final phase |

The ITIL 4 SVC is explicitly non-linear and non-sequential. This is the single most important structural difference from the ITIL v3 lifecycle.

---

## 8. ITIL 4 Foundation Exam Tips

1. **Know the purpose of each activity in one sentence.** Exam questions will describe an activity's output or purpose and ask you to name the activity.

2. **Improve connects to everything.** Any question asking which activity applies to "ensuring improvement across all activities" has one answer: Improve.

3. **Engage captures demand.** Any question describing collecting stakeholder requirements, managing customer relationships, or responding to user feedback involves Engage.

4. **Deliver and Support is day-to-day operation.** Incident resolution, request fulfillment, and monitoring all happen in Deliver and Support.

5. **Design and Transition covers both design and testing.** In ITIL 4 these are a single activity, not separate phases.

6. **Value streams are not the same as the SVC.** The SVC defines the six activities; a value stream is a specific combination of those activities for a particular purpose.

7. **Practices enable activities — they do not replace them.** Incident Management enables Deliver and Support; it does not substitute for it.

8. **The SVC is non-linear.** No exam answer describing a required sequential order for SVC activities is correct.

---

## 9. Key Terms Glossary

**Deliver and Support** — The SVC activity ensuring services are delivered and supported according to agreed specifications.

**Design and Transition** — The SVC activity ensuring products and services meet stakeholder expectations for quality, cost, and time to market.

**Engage** — The SVC activity providing a good understanding of stakeholder needs and maintaining good relationships with all stakeholders.

**Improve** — The SVC activity ensuring continual improvement of products, services, and practices across all activities and dimensions.

**Obtain/Build** — The SVC activity ensuring service components are available and meet agreed specifications.

**Plan** — The SVC activity ensuring a shared understanding of vision, current status, and improvement direction across the organization.

**Service Value Chain (SVC)** — The operating model at the heart of the SVS; six interconnected activities combined in value streams to convert demand into value.

**Value stream** — A series of steps combining SVC activities to create and deliver a specific product or service to a consumer.

---

## 10. Required Resources

* Official ITIL 4 SVC documentation and Foundation exam resources: axelos.com
* Module 05 video lecture (Professor Nash, approximately 20–24 minutes)

---

## 11. Study Checklist

* [ ] Watch the Module 05 video lecture in full.
* [ ] Write the purpose of each of the six SVC activities from memory.
* [ ] For each activity, write two key inputs and two key outputs.
* [ ] Draw the SVC showing all six activities and their connections to Improve.
* [ ] Map three different scenarios to their value stream activity sequences.
* [ ] Match at least six practices to their primary SVC activity.
* [ ] Review the exam tips and identify which concepts need more reinforcement.
* [ ] Complete the Module 05 Lab Activity.
* [ ] Take the Module 05 Quiz.
* [ ] Post your initial discussion response by Wednesday at 11:59 PM.
* [ ] Reply to at least two classmates by Sunday at 11:59 PM.

---

## Supplemental Resources

**1. AXELOS — ITIL 4 Service Value Chain**
<https://www.axelos.com/resource-hub/blog/itil-4-service-value-chain>
Official AXELOS description of the six SVC activities, their purposes, and how they combine into value streams. Essential reference for the Foundation exam section on SVC activity identification.

**2. IT Process Wiki — Value Stream Mapping in ITSM**
<https://wiki.en.it-processmaps.com/index.php/Value_Stream_Mapping>
A practitioner guide to value stream mapping as applied to IT service management workflows. Includes examples of how SVC activities appear in real-world service delivery value streams.

**3. Atlassian — Incident Management Best Practices**
<https://www.atlassian.com/incident-management/incident-response>
A detailed practitioner resource covering the full incident management lifecycle from detection through post-incident review. Directly maps to the Deliver and Support and Improve SVC activities that are central to this module.
