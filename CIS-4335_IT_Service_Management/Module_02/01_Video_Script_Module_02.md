# Video Script: Module 02 — The ITIL Service Value System (SVS)

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** ITIL 4 Foundation

---

## [00:00 – 01:30] Opening and Module Objectives

Welcome back, everyone. I am Professor Nash, and this is Module 02 of CIS-4335 IT Service Management. In Module 01 we laid the groundwork — we defined services, explained value co-creation, introduced the ITIL history, and got a bird's-eye view of the ITIL 4 framework.

Today we go deeper into the single most important structural concept in ITIL 4: the Service Value System. By the end of this module you will be able to describe all five components of the SVS and explain how they interact, explain the purpose and six activities of the Service Value Chain, describe what a value stream is and why it matters, and explain the relationship between the SVS and organizational agility.

This is a high-density module for the exam. Every component we discuss today will appear in Foundation exam questions. Let us get into it.

---

## [01:30 – 04:00] The SVS — Purpose and Structure

[SHOW DIAGRAM]

The Service Value System is ITIL 4's answer to a fundamental question: how does an organization take the demand for services and the opportunities available to it, and convert those inputs into genuine value for stakeholders?

The SVS is the complete operating model that answers that question. It is not a process. It is not a lifecycle. It is a system — a set of interacting components that work together as a whole.

At the left side of the SVS diagram are two inputs. The first is **Opportunity** — the possibilities available to the organization for adding value or improving performance. The second is **Demand** — the need or desire for products and services expressed by internal or external consumers.

At the right side of the diagram is the single output: **Value**. Every component inside the SVS exists to convert those left-side inputs into that right-side output.

Inside the SVS there are five components: Guiding Principles, Governance, the Service Value Chain, Practices, and Continual Improvement. Let us examine each one.

---

## [04:00 – 07:00] Component 1: Guiding Principles

The Guiding Principles are seven universal recommendations that guide an organization's decisions and actions in all circumstances, regardless of changes in goals, strategies, type of work, or management structure.

The word "universal" is important. The Guiding Principles do not apply only to IT operations or only to certain departments. They apply across the entire organization, at all levels, in all situations.

The seven principles are:

Focus on Value — every activity, every decision, every investment should trace back to value for stakeholders.

Start Where You Are — before designing or redesigning anything, assess what you already have and what is working. Do not discard functional capabilities simply because they are old.

Progress Iteratively with Feedback — do not try to solve everything at once. Break work into manageable increments, deliver, gather feedback, and adjust.

Collaborate and Promote Visibility — involve the right people across organizational boundaries. Hiding information or working in silos leads to poor decisions and failed implementations.

Think and Work Holistically — every service and practice exists within a system. Changes to one component affect others. Consider the whole picture.

Keep It Simple and Practical — resist the urge to over-engineer. If an activity does not contribute to value, question whether it should exist.

Optimize and Automate — identify where human judgment genuinely adds value, and automate what is repetitive and rule-based. Automation frees people to focus on higher-value work.

The exam often presents a scenario and asks which principle applies. We will drill this extensively throughout the course.

---

## [07:00 – 09:00] Component 2: Governance

Governance is the means by which an organization is directed and controlled. In ITIL 4, governance operates at the highest level of the organization — it is how the board, executive leadership, or governing body establishes direction, delegates authority, and monitors performance.

The governance component of the SVS ensures that policies and objectives are established and communicated throughout the organization, that accountability is clearly defined, and that performance is evaluated against established objectives.

Governance is not the same as management. Governance sets the framework within which management operates. The Service Value Chain operates under governance's direction.

For the exam: governance directs and controls. The Service Value Chain executes. Know that distinction.

---

## [09:00 – 14:00] Component 3: The Service Value Chain

[SHOW DIAGRAM]

The Service Value Chain is the operational core of the SVS. It is a flexible operating model for the creation, delivery, and continual improvement of services.

The SVC defines six activities. These activities do not form a fixed linear process — they can be combined in different sequences and patterns depending on what the organization is doing. ITIL 4 calls these patterns **value streams**.

The six activities are:

Plan — this activity ensures a shared understanding of the vision, current status, and improvement direction for all four dimensions and all products and services across the organization. Planning produces strategies, portfolios, and policies.

Improve — this activity ensures continual improvement of products, services, and practices across all value chain activities and the four dimensions of service management. Every other activity in the SVC both contributes to and benefits from this activity.

Engage — this activity provides a good understanding of stakeholder needs, transparently engages with them, and maintains continuous communication with consumers, users, and other stakeholders. Engagement is how the organization understands demand and builds relationships.

Design and Transition — this activity ensures that products and services continually meet stakeholder expectations for quality, costs, and time to market. This is where new or changed services are designed, tested, and prepared for deployment.

Obtain/Build — this activity ensures that service components are available when and where they are needed and meet agreed specifications. This covers both obtaining components from external sources and building them internally.

Deliver and Support — this activity ensures that services are delivered and supported according to agreed specifications and stakeholders' expectations. This is where day-to-day service operation happens — the help desk, incident response, and routine service delivery.

A critical exam point: these six activities do not correspond one-to-one with the old ITIL v3 lifecycle phases. They interact with each other and with the practices in flexible combinations. The SVC explicitly supports both waterfall-style and Agile/DevOps ways of working.

---

## [14:00 – 17:30] Value Streams

A **value stream** is a series of steps an organization takes to create and deliver products and services to a service consumer. Value streams are specific instances of the Service Value Chain activities being combined in a particular sequence to accomplish a particular objective.

Every organization has multiple value streams. Examples include the steps followed to onboard a new employee and provision their IT access, the steps followed when a user reports an incident until that incident is resolved, and the steps followed when a software development team deploys a new application feature.

Value streams are important because they give ITIL 4 its flexibility. Rather than prescribing a single fixed process for all situations, ITIL 4 gives organizations a set of activities and says: combine them in whatever sequence creates value for your specific context.

When organizations analyze their value streams, they often discover waste — steps that add cost or time without adding value. This is where Lean thinking, which ITIL 4 explicitly draws on, enters the picture. Identifying and eliminating waste in value streams is a core improvement activity.

---

## [17:30 – 20:00] Components 4 and 5: Practices and Continual Improvement

Practices are sets of organizational resources designed to perform work or accomplish an objective. ITIL 4 defines 34 practices in three categories: General Management Practices, Service Management Practices, and Technical Management Practices.

Practices are not the same as processes. A practice includes not just the defined activities, but also the people who perform them, the technology that supports them, the information they use, and the partners or suppliers involved. This is why ITIL 4 uses the term "practice" — it captures the full organizational capability, not just the documented flowchart.

Practices integrate into the Service Value Chain. When an incident management practice activates, it draws on the Deliver and Support activity and potentially on Engage and Improve as well. The practices do not live outside the SVC — they enable and execute the SVC activities.

Continual Improvement is the fifth SVS component and also a standalone ITIL 4 practice. As an SVS component, it represents the ongoing commitment embedded throughout the entire system to identify and implement improvements at every level and in every activity. No component of the SVS is exempt from improvement.

As a practice, Continual Improvement uses a seven-step model we will cover in depth in Module 06.

---

## [20:00 – 22:30] SVS Integration and Organizational Agility

One of the design goals of ITIL 4 was to create a framework that supports organizational agility — the ability to respond quickly and effectively to changing circumstances.

The SVS supports agility in several ways. The Service Value Chain is non-prescriptive about sequencing, so organizations can adapt quickly to new demand patterns. The Guiding Principles can be applied independently of specific procedures, so teams can make good decisions even in novel situations. The Continual Improvement component ensures that the organization is always adapting rather than waiting for a major revision cycle. And the integration with Agile and DevOps means organizations do not have to choose between ITIL and the ways of working their development teams already use.

The exam sometimes asks why ITIL 4 was redesigned. A key part of the answer is that the ITIL v3 lifecycle model was perceived as too rigid and sequential for modern IT environments — environments where cloud, automation, DevOps, and continuous delivery have transformed the pace of change. The SVS was designed to be flexible enough for those environments.

---

## [22:30 – 24:00] Module Summary and What Is Next

Let us recap Module 02.

The Service Value System is ITIL 4's top-level operating model. Its inputs are Opportunity and Demand; its output is Value.

The five components of the SVS are: Guiding Principles, Governance, the Service Value Chain, Practices, and Continual Improvement.

The Service Value Chain contains six activities — Plan, Improve, Engage, Design and Transition, Obtain/Build, and Deliver and Support — that combine in flexible patterns called value streams.

Practices are organizational capabilities that enable the SVC activities. All 34 practices serve the SVS. Continual Improvement is embedded throughout the entire system.

In Module 03 we examine the Four Dimensions of Service Management in depth. In Module 04 we go deep on the seven Guiding Principles.

Complete the Reading Guide, Lab, and Quiz before the module deadline. The discussion this week connects SVS concepts to a real organizational scenario — engage early and engage substantively.

For authoritative SVS documentation, see axelos.com.

---

End of Module 02 Video Script
