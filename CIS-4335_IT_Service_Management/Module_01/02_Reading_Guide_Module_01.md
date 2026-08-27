# Reading Guide: Module 01 — Introduction to ITIL 4 and Service Management

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** ITIL 4 Foundation

---

## Purpose of This Guide

This reading guide supports Module 01 of CIS-4335. Use it alongside the video lecture to build the conceptual vocabulary required for the ITIL 4 Foundation exam and for all subsequent modules. Work through every section before attempting the quiz or lab.

---

## 1. Core Definitions: Services and Value

ITIL 4 defines a **service** as a means of enabling value co-creation by facilitating outcomes that customers want to achieve, without the customer having to manage specific costs and risks.

Every word in that definition carries weight:

* "Value co-creation" — value is not delivered by the provider alone; it emerges from the interaction between provider and consumer.
* "Outcomes that customers want to achieve" — ITIL 4 focuses on business results, not just technical deliverables.
* "Without managing specific costs and risks" — services transfer complexity to specialists, freeing consumers to focus on their own objectives.

A **product** is a configuration of an organization's resources designed to offer value to a consumer. Services are frequently delivered through products. The distinction matters on the exam: products are the tangible or intangible configurations; services are the value-enabling relationships built around those products.

**Value** in ITIL 4 is defined as the perceived benefits, usefulness, and importance of something. It is always subjective — different consumers in different contexts will perceive value differently. This is why co-creation and active consumer engagement matter.

---

## 2. Utility and Warranty

ITIL 4 splits the requirements for value into two complementary properties.

**Utility** is the functionality offered by a product or service to meet a particular need. The shorthand is "fit for purpose." A service has utility if it either supports the performance of the consumer or removes constraints the consumer would otherwise face.

**Warranty** is the assurance that a product or service will meet agreed requirements. The shorthand is "fit for use." Warranty typically covers availability, capacity, security, and continuity.

### Utility vs. Warranty Comparison Table

| Property | Definition | Key Question | Example |
|---|---|---|---|
| Utility | Fit for purpose; what the service does | Does it do what the customer needs? | A ticketing system that creates, routes, and resolves tickets |
| Warranty | Fit for use; how reliably the service performs | Does it perform to agreed standards? | That same system available 99.9% of business hours |

Both utility and warranty are required for value. A service that does the right things but does them inconsistently fails consumers. A service that is always available but does nothing useful also fails. The exam tests this distinction in scenario form.

---

## 3. Organizations, People, and Stakeholder Roles

ITIL 4 defines distinct roles within service relationships.

### Service Relationship Roles

| Role | Definition | Primary Interaction Point |
|---|---|---|
| Service Provider | Organization delivering services | Designs, delivers, and improves services |
| Service Consumer | Organization receiving services | Customer, user, and sponsor roles |
| Customer | Defines requirements and owns outcomes | Service Level Management, contracts |
| User | Uses services daily | Service Desk, self-service portal |
| Sponsor | Authorizes budget for service consumption | Financial management, governance |

A single person may hold multiple roles. A small-business owner may be customer, user, and sponsor simultaneously. In large enterprises, these roles are typically held by different people or teams. The exam frequently tests whether students can correctly classify a stakeholder based on their described activity.

---

## 4. The History and Evolution of ITIL

Understanding ITIL's history provides context for why ITIL 4 is structured as it is.

### ITIL Version History

| Version | Era | Key Characteristic |
|---|---|---|
| ITIL v1 | 1980s | 40+ books; UK government guidance; broad but difficult to implement |
| ITIL v2 | Early 2000s | Consolidated; focused on Service Support and Service Delivery |
| ITIL v3 / 2011 | 2007 / 2011 | Service lifecycle (5 phases); "processes" terminology |
| ITIL 4 | 2019 | Service Value System; "practices" terminology; integrates Agile, DevOps, Lean |

The shift from ITIL v3 to ITIL 4 is conceptually significant:

* ITIL v3 organized guidance around a **service lifecycle** — a linear sequence of phases from strategy through continual improvement.
* ITIL 4 replaced the lifecycle with the **Service Value System** — a holistic, flexible model where components interact non-linearly.
* ITIL v3 used the term **processes**; ITIL 4 uses **practices**, reflecting a broader view of organizational capability.
* ITIL 4 explicitly integrates with Agile, DevOps, Lean, and organizational change frameworks.

---

## 5. The ITIL 4 Service Value System — Component Overview

The Service Value System is the top-level model in ITIL 4. It describes how all the components and activities of an organization work together to enable value creation.

### SVS Inputs and Output

* **Inputs:** Opportunity (possibilities for adding value) and Demand (need or desire for products and services)
* **Output:** Value (outcomes, benefits, and perceptions of those who receive and experience services)

### SVS Components

| Component | Role in the SVS |
|---|---|
| Guiding Principles | Universal recommendations for all decisions and actions |
| Governance | Direction and control of the organization |
| Service Value Chain | The operating model for creating, delivering, and improving services |
| Practices | Sets of organizational resources for accomplishing objectives (34 total) |
| Continual Improvement | Ongoing effort to improve products, services, and practices |

All five components interact with and support one another. No component operates in isolation.

---

## 6. The Seven Guiding Principles

The Guiding Principles are among the most testable elements in the Foundation exam. Learn all seven and understand what each means in practice.

### ITIL 4 Guiding Principles

| Principle | Core Meaning |
|---|---|
| Focus on Value | Every action should directly or indirectly contribute to value for stakeholders |
| Start Where You Are | Do not start from scratch; assess current state and build on what works |
| Progress Iteratively with Feedback | Work in smaller increments, gather feedback, and adjust before committing fully |
| Collaborate and Promote Visibility | Work across boundaries, share information, and avoid silos |
| Think and Work Holistically | No service or practice operates in isolation; consider the whole system |
| Keep It Simple and Practical | Eliminate steps or elements that do not contribute to value |
| Optimize and Automate | Use human judgment where it adds value; automate repetitive tasks |

The Guiding Principles apply across the entire SVS. The exam sometimes presents a scenario and asks which principle is most relevant. Practice pairing principles with specific situations.

---

## 7. The Four Dimensions of Service Management

ITIL 4 requires every service and practice to be considered across four dimensions. Neglecting any dimension creates gaps and risk.

### Four Dimensions Summary

| Dimension | Focus Area | Common Exam Scenario |
|---|---|---|
| Organizations and People | Roles, culture, skills, accountability | Siloed teams, unclear ownership, resistance to change |
| Information and Technology | Data, tools, AI, automation, security | Platform selection, data governance, tool integration |
| Partners and Suppliers | External vendors, contracts, relationships | Cloud providers, outsourcing decisions, vendor risk |
| Value Streams and Processes | Workflows, procedures, activities | Process redesign, workflow automation, bottlenecks |

Surrounding the four dimensions are **external factors** (PESTLE: Political, Economic, Social, Technological, Legal, Environmental) that organizations cannot control but must account for.

---

## 8. ITIL 4 Practice Categories

ITIL 4 defines 34 management practices grouped into three categories.

### Practice Categories

| Category | Count | Examples |
|---|---|---|
| General Management Practices | 14 | Continual Improvement, Risk Management, Knowledge Management |
| Service Management Practices | 17 | Incident Management, Problem Management, Service Desk, Service Level Management |
| Technical Management Practices | 3 | Deployment Management, Infrastructure and Platform Management, Software Development and Management |

The Foundation exam focuses most heavily on Service Management Practices and a subset of General Management Practices. You will study each high-priority practice in Modules 6–15.

---

## 9. ITIL v3 vs. ITIL 4 — Side-by-Side Comparison

| Element | ITIL v3 | ITIL 4 |
|---|---|---|
| Core Model | Service Lifecycle (5 phases) | Service Value System |
| Operational Model | Processes | Value Chain Activities + Practices |
| Terminology | Processes | Practices |
| Agile/DevOps Integration | Limited | Explicit and central |
| Continual Improvement | Separate lifecycle phase (CSI) | Embedded throughout SVS |
| Number of Practices/Processes | 26 processes | 34 practices |

---

## 10. ITIL 4 Foundation Exam Tips

1. **"Practices" not "processes."** If an exam question uses ITIL v3 terminology as the correct answer in an ITIL 4 context, it is almost always a distractor. ITIL 4 uses "practices."

2. **Value is co-created.** Exam scenarios that describe the provider "delivering value to" a customer are using outdated framing. Value is co-created between provider and consumer.

3. **Utility AND warranty are both required.** Do not select utility alone or warranty alone as sufficient for value. Both are necessary.

4. **Know all seven Guiding Principles by name.** The exam will present scenarios and ask which principle applies. You must recognize each principle from a description.

5. **Know all four dimensions by name.** Scenario questions will describe a service failure and ask which dimension was neglected. Match the failure to its dimension.

6. **SVS inputs are Opportunity and Demand.** The output is Value. Know this for diagram-based questions.

7. **Customer vs. user distinction.** The customer defines requirements; the user consumes services day-to-day. These may be the same person or different people depending on context.

8. **ITIL 4 integrates with Agile and DevOps.** Questions about whether ITIL 4 is compatible with those approaches have a clear answer: yes, by design.

---

## 11. Key Terms Glossary

**Co-creation of value** — The concept that value results from the active collaboration of both the service provider and service consumer, not from one party alone.

**Continual Improvement** — A recurring organizational activity performed at all levels to ensure performance meets stakeholder expectations over time.

**Customer** — A person who defines service requirements and owns the outcomes of service consumption.

**Demand** — The need or desire for products and services.

**Four Dimensions** — Organizations and People; Information and Technology; Partners and Suppliers; Value Streams and Processes.

**Guiding Principles** — Seven universal recommendations that apply across all ITIL 4 decisions and activities.

**IT Service Management (ITSM)** — The policies, practices, and capabilities an organization uses to design, deliver, manage, and improve IT services aligned to business needs.

**ITIL** — IT Infrastructure Library; the world's most widely adopted IT service management framework, currently in version 4 (published 2019).

**Opportunity** — A possibility for adding value or improving performance.

**Outcome** — A result for a stakeholder enabled by one or more outputs.

**Output** — A tangible or intangible deliverable of an activity.

**Practice** — A set of organizational resources designed to perform work or accomplish an objective. ITIL 4 defines 34 practices.

**Product** — A configuration of an organization's resources designed to offer value to a consumer.

**Service** — A means of enabling value co-creation by facilitating outcomes that customers want to achieve, without the customer having to manage specific costs and risks.

**Service Consumer** — An organization that uses services.

**Service Provider** — An organization that delivers services to consumers.

**Service Value Chain (SVC)** — The operating model at the heart of the SVS; six interconnected activities that create, deliver, and improve services.

**Service Value System (SVS)** — The top-level ITIL 4 model showing how all components work together to enable value creation.

**Sponsor** — A person who authorizes the budget for service consumption.

**User** — A person who uses services on a daily basis.

**Utility** — Fit for purpose; the functionality a service offers to meet a particular need.

**Warranty** — Fit for use; assurance that a service meets agreed requirements for availability, capacity, security, and continuity.

---

## 12. Required Resources

* Official ITIL 4 Foundation certification information and glossary: axelos.com
* Module 01 video lecture (Professor Nash, approximately 20–24 minutes)

---

## 13. Study Checklist

* [ ] Watch the Module 01 video lecture in full and take notes on all bolded terms.
* [ ] Read Sections 1–3 of this guide and write definitions for all glossary terms without looking.
* [ ] Reproduce the Utility vs. Warranty comparison table from memory.
* [ ] List all five SVS components without referring to notes.
* [ ] List all seven Guiding Principles and write one-sentence explanations for each.
* [ ] List all four dimensions and describe what each covers.
* [ ] Explain the ITIL v3 vs. ITIL 4 distinction in your own words (at least three differences).
* [ ] Review the eight exam tips and identify which concepts feel least secure.
* [ ] Complete the Module 01 Lab Activity before taking the quiz.
* [ ] Take the Module 01 Quiz.
* [ ] Post your initial response in the Module 01 Discussion by Wednesday at 11:59 PM.
* [ ] Respond to at least two classmates by Sunday at 11:59 PM.

---

## 14. Supplemental Resources

**1. AXELOS — ITIL 4 Foundation Guidance**
<https://www.axelos.com/certifications/itil-service-management/itil-4-foundation>
The official AXELOS page for the ITIL 4 Foundation certification. Includes the official syllabus, exam format details, and links to the ITIL 4 glossary. Useful for verifying exact terminology before exams.

**2. ITIL 4 Official Glossary (PDF)**
<https://www.axelos.com/resource-hub/blog/itil-4-glossary>
A downloadable reference of all ITIL 4 terms and their official definitions. Use this alongside the module reading guide to check definitions and confirm the exact ITIL 4 wording for utility, warranty, outcome, output, and service.

**3. ServiceNow — What Is ITSM?**
<https://www.servicenow.com/products/itsm/what-is-itsm.html>
A practitioner-focused introduction to IT service management from the industry's leading ITSM platform vendor. Bridges the gap between framework theory (ITIL 4) and how ITSM concepts are implemented in real enterprise software tools.
