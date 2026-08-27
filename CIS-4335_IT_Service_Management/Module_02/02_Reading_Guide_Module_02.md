# Reading Guide: Module 02 — The ITIL Service Value System (SVS)

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** ITIL 4 Foundation

---

## Purpose of This Guide

This reading guide supports Module 02 of CIS-4335. The Service Value System is the highest-priority structural concept on the ITIL 4 Foundation exam. Master every component, every activity, and every relationship described here before attempting the quiz or lab.

---

## 1. The SVS at a Glance

The Service Value System is ITIL 4's top-level operating model. It describes how all the components of an organization work together to enable value creation.

The SVS has two inputs and one output:

* Inputs: Opportunity and Demand
* Output: Value

Opportunity represents possibilities for adding value or improving performance. Demand represents the need or desire for products and services from internal or external consumers. All SVS components exist to convert these inputs into the output of value.

The five SVS components are:

* Guiding Principles
* Governance
* Service Value Chain
* Practices
* Continual Improvement

---

## 2. Component 1 — Guiding Principles

The Guiding Principles are seven universal recommendations that guide all organizational decisions and actions regardless of goals, strategies, or management structure. They apply universally — to every level of the organization, every team, every practice.

### The Seven Guiding Principles

| Principle | Core Meaning | Practical Application |
|---|---|---|
| Focus on Value | Every action traces back to stakeholder value | Before starting any work, ask: how does this contribute to value? |
| Start Where You Are | Assess and reuse existing capabilities | Do not discard working tools or processes without first evaluating them |
| Progress Iteratively with Feedback | Work in small increments; learn before expanding | Pilot new practices in one team before rolling out org-wide |
| Collaborate and Promote Visibility | Include all relevant parties; share information openly | Break down silos; involve suppliers and users early |
| Think and Work Holistically | Consider the whole system, not just one component | A change to one practice may affect three others — assess the full impact |
| Keep It Simple and Practical | Eliminate steps that do not add value | Challenge every procedure: does this genuinely help? |
| Optimize and Automate | Apply human judgment where it matters; automate the rest | Use AI and scripting for repetitive ticket routing; keep humans for escalation judgment |

The exam frequently presents a scenario and asks which Guiding Principle applies. Practice pairing each principle with concrete examples.

---

## 3. Component 2 — Governance

Governance is the means by which an organization is directed and controlled. It operates at the highest organizational level, establishing policies, objectives, and accountability structures within which service management activities take place.

### Governance vs. Management

| Aspect | Governance | Management |
|---|---|---|
| Level | Board / executive leadership | Operational management |
| Function | Direct and control | Plan, execute, monitor, improve |
| Example | Setting data security policy | Implementing firewall configurations |
| ITIL 4 Location | SVS component | Enabled by SVC activities and practices |

Governance does not manage services — it creates the framework within which the Service Value Chain and practices operate.

---

## 4. Component 3 — The Service Value Chain

The Service Value Chain is the operational heart of the SVS. It is a flexible operating model that describes how an organization creates, delivers, and continuously improves services. The SVC consists of six activities.

### The Six SVC Activities

| Activity | Purpose | Key Outputs |
|---|---|---|
| Plan | Shared understanding of direction for all dimensions and services | Strategies, portfolios, policies |
| Improve | Continual improvement across all activities and dimensions | Improvement plans, performance evaluations |
| Engage | Understand stakeholder needs; maintain ongoing communication | Stakeholder requirements, feedback, relationships |
| Design and Transition | Ensure new/changed services meet quality, cost, and time expectations | Designs, tested service components, transition plans |
| Obtain/Build | Ensure service components are available and meet specifications | Service components (built or procured) |
| Deliver and Support | Deliver services and support users per agreed specifications | Delivered services, resolved incidents, fulfilled requests |

### Important Distinctions

* The six SVC activities are not a linear sequence. They can be combined in any order relevant to the work being done.
* Multiple SVC activities may be active simultaneously within a single value stream.
* Every SVC activity contributes to the Improve activity, and Improve feeds back into all other activities.

---

## 5. Value Streams

A value stream is a series of steps an organization takes to create and deliver products and services to a service consumer. Value streams represent specific combinations of SVC activities applied to a particular type of work.

### Value Stream Examples

| Scenario | SVC Activities Typically Involved |
|---|---|
| Onboarding a new employee with IT access | Engage → Obtain/Build → Deliver and Support |
| Resolving a user-reported incident | Engage → Deliver and Support → Improve |
| Deploying a new software feature | Plan → Design and Transition → Obtain/Build → Deliver and Support |
| Processing a service request | Engage → Obtain/Build → Deliver and Support |

Organizations should map and analyze their value streams to identify waste — steps that consume resources without contributing to value. This is a Lean thinking concept that ITIL 4 explicitly incorporates.

---

## 6. Component 4 — Practices

Practices are sets of organizational resources designed to perform work or accomplish an objective. ITIL 4 defines 34 practices in three categories.

### Practice Categories

| Category | Count | Scope |
|---|---|---|
| General Management Practices | 14 | Broad organizational capabilities applicable across all services |
| Service Management Practices | 17 | Specific to designing, delivering, and managing services |
| Technical Management Practices | 3 | Technical capabilities for infrastructure, software, and deployment |

### How Practices Relate to the SVC

Practices do not replace SVC activities. They enable them. An incident management practice, for example, enables the Deliver and Support activity. A continual improvement practice enables the Improve activity across the entire SVC. Each practice contributes to one or more SVC activities.

### The 14 General Management Practices

* Architecture Management
* Continual Improvement
* Information Security Management
* Knowledge Management
* Measurement and Reporting
* Organizational Change Management
* Portfolio Management
* Project Management
* Relationship Management
* Risk Management
* Service Financial Management
* Strategy Management
* Supplier Management
* Workforce and Talent Management

### Selected High-Priority Service Management Practices (exam focus)

* Availability Management
* Business Analysis
* Capacity and Performance Management
* Change Enablement
* Incident Management
* IT Asset Management
* Monitoring and Event Management
* Problem Management
* Release Management
* Service Catalogue Management
* Service Configuration Management
* Service Continuity Management
* Service Design
* Service Desk
* Service Level Management
* Service Request Management
* Service Validation and Testing

### The 3 Technical Management Practices

* Deployment Management
* Infrastructure and Platform Management
* Software Development and Management

---

## 7. Component 5 — Continual Improvement

Continual Improvement has a dual role in ITIL 4: it is both an SVS component and a standalone practice.

As an SVS component, Continual Improvement represents the organization's overarching commitment to improving all aspects of its services and service management at all levels. No SVS component is exempt — the Guiding Principles, governance structures, SVC activities, and all 34 practices are all subject to continual improvement.

As a practice, Continual Improvement uses a structured seven-step model (covered in detail in Module 06):

1. What is the vision?
2. Where are we now?
3. Where do we want to be?
4. How do we get there?
5. Take action.
6. Did we get there?
7. How do we keep the momentum going?

The Continual Improvement Register (CIR) is the tool organizations use to document, prioritize, and track improvement initiatives.

---

## 8. SVS Integration: How the Components Work Together

The five SVS components are not independent — they interact continuously.

Governance sets the direction and policies that the Service Value Chain must operate within. The Guiding Principles inform how all SVC activities and practices are executed. The Service Value Chain combines practices in value streams to convert demand into delivered services. Continual Improvement evaluates the outputs of all SVC activities and feeds improvement back into every component.

A useful mental model: Governance tells the organization what to do and sets boundaries. Guiding Principles tell people how to think and decide. The SVC shows what activities to perform. Practices provide the capability to perform those activities. Continual Improvement ensures the whole system keeps getting better.

---

## 9. SVS and Organizational Agility

ITIL 4 was designed to support organizations operating in rapidly changing environments. The SVS promotes agility in several specific ways:

* The SVC is non-prescriptive about sequencing — organizations choose how to combine activities.
* Value streams allow the same framework to support both traditional waterfall projects and Agile sprints.
* The Guiding Principles can be applied without rigid procedures, supporting fast decision-making.
* Continual Improvement is built in rather than periodic, so the framework evolves with the organization.

ITIL 4 is explicitly compatible with Agile, DevOps, Lean, and organizational change management approaches. This is a design choice, not an accident. The Foundation exam may include questions about this compatibility.

---

## 10. ITIL 4 Foundation Exam Tips

1. **Know the five SVS components by name and function.** The exam will ask you to identify which component serves a specific purpose within the SVS.

2. **Know the six SVC activities by name.** Questions will describe an activity and ask you to name it, or name an activity and ask what it does.

3. **The SVC is not linear.** If an exam answer says the SVC activities must be followed in a fixed sequence, that answer is wrong.

4. **Governance directs; management executes.** Do not confuse governance (board-level direction) with management (operational planning and execution).

5. **Practices enable SVC activities.** They are not separate from the SVC — they provide the capability that makes SVC activities possible.

6. **Continual Improvement applies to everything.** No SVS component, practice, or service is exempt from improvement.

7. **Value streams are flexible combinations of SVC activities.** A value stream for incident resolution uses different activities in a different sequence than a value stream for new service deployment.

8. **The SVS supports Agile and DevOps — by design.** This is a frequently tested exam point.

---

## 11. Key Terms Glossary

**Continual Improvement** — An SVS component and a practice representing the ongoing organizational commitment to improving all aspects of services and service management.

**Continual Improvement Register (CIR)** — A documented log used to record, prioritize, and track improvement initiatives.

**Demand** — The need or desire for products and services from internal or external consumers; an SVS input.

**Governance** — The means by which an organization is directed and controlled; an SVS component operating at the highest organizational level.

**Guiding Principles** — Seven universal recommendations that apply to all organizational decisions and actions across the SVS.

**Opportunity** — Possibilities for adding value or improving organization performance; an SVS input.

**Practice** — A set of organizational resources designed to perform work or accomplish an objective. ITIL 4 defines 34 practices.

**Service Value Chain (SVC)** — The operating model at the heart of the SVS; six activities (Plan, Improve, Engage, Design and Transition, Obtain/Build, Deliver and Support) combined in flexible value streams.

**Service Value System (SVS)** — ITIL 4's top-level operating model showing how all components work together to enable value creation.

**Value** — Perceived benefits, usefulness, and importance; the output of the SVS.

**Value Stream** — A series of steps an organization takes to create and deliver products and services to a service consumer; a specific combination of SVC activities.

---

## 12. Required Resources

* Official ITIL 4 SVS documentation and Foundation exam resources: axelos.com
* Module 02 video lecture (Professor Nash, approximately 20–24 minutes)

---

## 13. Study Checklist

* [ ] Watch the Module 02 video lecture and diagram walkthroughs in full.
* [ ] Draw the SVS diagram from memory, labeling all five components and both inputs and output.
* [ ] List all six SVC activities and write one sentence describing each.
* [ ] List all seven Guiding Principles and write one-sentence explanations for each.
* [ ] Explain the difference between governance and management in ITIL 4 terms.
* [ ] Describe three different value streams using different combinations of SVC activities.
* [ ] List the three practice categories and give two examples from each.
* [ ] Review the eight exam tips and note which concepts need more study.
* [ ] Complete the Module 02 Lab Activity.
* [ ] Take the Module 02 Quiz.
* [ ] Post your initial discussion response by Wednesday at 11:59 PM.
* [ ] Reply to at least two classmates by Sunday at 11:59 PM.

---

## 14. Supplemental Resources

**1. AXELOS — ITIL 4 Service Value System Overview**
<https://www.axelos.com/resource-hub/blog/itil-4-the-service-value-system>
An official AXELOS article explaining the SVS architecture, inputs, outputs, and the relationship between its five components. Recommended as a companion to the module reading guide for exam preparation.

**2. IT Process Wiki — ITIL 4 Value Chain Activities**
<https://wiki.en.it-processmaps.com/index.php/ITIL_4_Service_Value_Chain>
A detailed reference covering all six Service Value Chain activities with descriptions, inputs, and outputs. Includes diagrams showing how activities combine into value streams.

**3. Atlassian — DevOps and ITSM Integration**
<https://www.atlassian.com/itsm/itil>
A practitioner-oriented guide explaining how ITIL 4 and DevOps complement each other. Useful for understanding why the SVS was designed to support Agile and DevOps environments and how value streams apply in real software delivery organizations.
