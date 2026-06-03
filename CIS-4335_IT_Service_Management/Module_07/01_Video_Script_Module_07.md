# Video Script: Module 07 — The Service Value Chain

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: ITIL 4 Foundation

---

## Introduction (0:00–1:30)

Welcome back to CIS-4335 IT Service Management. I'm Professor Nash, and today we are
diving into one of the most important structural models in the entire ITIL 4 framework:
the **Service Value Chain**.

If you have been following along, you know that ITIL 4 introduced the Service Value System,
or SVS. The Service Value Chain sits at the heart of that system. It is the operating model
that describes how demand from customers is converted into real, tangible value.

Think of it as the engine inside the car. The SVS is the car. The Service Value Chain is
the engine that makes it move.

[SHOW DIAGRAM: ITIL 4 Service Value System overview — highlight the Service Value Chain in the center]

By the end of this module, you will be able to name and describe all six activities of the
Service Value Chain, explain how they interconnect, trace how demand flows through the chain
to produce value, and understand the concept of value streams. These are all testable topics
on the ITIL 4 Foundation exam.

[PAUSE]

---

## Section 1: What Is the Service Value Chain? (1:30–4:00)

The Service Value Chain is a flexible operating model for creating, delivering, and
continually improving services. ITIL 4 defines it as a set of **six interconnected activities**
that together transform inputs — demand, resources, components — into outputs and ultimately
into value for customers and stakeholders.

The six activities are:

- **Plan**
- **Improve**
- **Engage**
- **Design and Transition**
- **Obtain/Build**
- **Deliver and Support**

[SHOW DIAGRAM: The six SVC activities arranged in the ITIL 4 oval chain diagram]

Here is the critical insight that separates ITIL 4 from ITIL v3: these activities are **not
a linear pipeline**. They are not Step 1, Step 2, Step 3 in order. Any activity can receive
inputs from or send outputs to any other activity, depending on the situation.

That flexibility is intentional. It allows the Service Value Chain to support many different
approaches — Agile, DevOps, Waterfall, or hybrid. You combine the activities in different
sequences to create what ITIL calls **value streams**.

[PAUSE]

Let me give you a practical anchor. Imagine a university IT department. Every day, students
submit help desk tickets, faculty request new software, and administrators need reports. The
Service Value Chain is the model that describes how IT processes all of those demands —
from intake to resolution to improvement — as a connected, value-producing system.

---

## Section 2: The Activity — Plan (4:00–6:00)

Let us walk through each activity in detail, starting with **Plan**.

Plan ensures a shared understanding of the vision, current status, and improvement
direction for all four dimensions of service management and all products and services.

[SHOW DIAGRAM: Plan activity — inputs and outputs]

Think of Plan as the steering wheel. Without it, the other five activities have no direction.
Plan produces:

- Portfolios and strategic decisions
- Architectural and policy decisions
- Improvement plans

Inputs to Plan come from all other activities and from the Governance component of the SVS.
Demand also flows in — demand is the starting trigger. Stakeholders signal what they need,
and Plan translates that signal into strategic direction.

A key point for the exam: Plan is not just a one-time project kickoff. It is a **continuous
activity**. As the environment changes, as technology evolves, as stakeholder needs shift,
the Plan activity recalibrates.

[PAUSE]

---

## Section 3: The Activity — Improve (6:00–8:00)

Next is **Improve**. Improve ensures continual improvement of products, services, and
practices across all value chain activities and the four dimensions of service management.

[SHOW DIAGRAM: Improve activity — positioned as touching all other activities with double-headed arrows]

Improve is the only activity that has a relationship with **every other activity**. It
literally spans the entire chain. This is ITIL 4's structural commitment to the guiding
principle "Always improve."

What does Improve produce?

- Improvement initiatives and plans
- Value chain performance information
- Improvement status reports

Improve receives inputs from monitoring data, stakeholder feedback, performance assessments,
and lessons learned from incidents and problems. It feeds improvement plans back into Plan,
Engage, Design and Transition, Obtain/Build, and Deliver and Support.

A real-world analogy: think of Improve as the quality assurance team that observes every
department and continuously recommends enhancements. No process is exempt from improvement.

[PAUSE]

---

## Section 4: The Activity — Engage (8:00–10:00)

**Engage** provides a good understanding of stakeholder needs, transparency, and continual
engagement and good relationships with all stakeholders.

[SHOW DIAGRAM: Engage activity — two-way arrows to external stakeholders outside the SVC boundary]

Engage is the front door of the Service Value Chain. All external stakeholder input —
customer requirements, user feedback, partner communications, supplier contracts — enters
the chain through Engage.

Engage produces:

- Consolidated stakeholder requirements passed to Design and Transition
- Service requests routed to Deliver and Support
- Contract and agreement input sent to Obtain/Build
- Feedback and performance information sent to Improve

Key point: Engage handles **demand** from customers and users. When a user calls the service
desk, that is Engage in action. When a product manager interviews stakeholders to understand
what they need, that is Engage. When IT communicates service status back to the business,
that is also Engage.

[PAUSE]

Engage is two-directional. It is not just about receiving requests — it is about maintaining
ongoing, transparent relationships so that value expectations are aligned.

For the Foundation exam, remember: Engage is where **demand enters** and where **value is
communicated back** to stakeholders.

---

## Section 5: The Activity — Design and Transition (10:00–12:30)

**Design and Transition** ensures that products and services continually meet stakeholder
expectations for quality, costs, and time-to-market.

[SHOW DIAGRAM: Design and Transition — inputs from Engage and Plan, outputs to Obtain/Build and Deliver and Support]

This activity covers everything involved in designing new or changed services and moving
them into production. It includes:

- Service and solution design
- Testing and validation
- Release management
- Transition planning and documentation

Design and Transition receives requirements from Engage, strategic direction from Plan, and
components from Obtain/Build. It produces tested, validated, documented service components
that are ready to be operated and supported.

One thing that surprises students: Design and Transition is **not just IT architecture**.
It includes process design, workforce planning, supplier agreements, and user documentation.
All four dimensions must be addressed.

[PAUSE]

A key exam concept: Design and Transition is responsible for ensuring that changes are
properly assessed, tested, and authorized before moving to production. This is where
Change Management practices plug into the value chain.

---

## Section 6: The Activity — Obtain/Build (12:30–14:30)

**Obtain/Build** ensures that service components are available when and where they are
needed and that they meet agreed specifications.

[SHOW DIAGRAM: Obtain/Build — inputs from Design and Transition, outputs flowing back to Design and Transition and forward to Deliver and Support]

This activity is about acquiring or constructing the components that services require —
hardware, software, cloud services, trained staff, and documentation.

Obtain/Build asks: Should we make it or buy it? Should we build infrastructure in-house or
procure from a cloud vendor? Should we write custom software or purchase off-the-shelf?

Outputs flow to:

- Design and Transition — for testing and integration
- Deliver and Support — for operational deployment

Inputs come from:

- Plan — strategic direction and budget alignment
- Design and Transition — specifications and requirements
- Engage — contract and supplier requirements from partners

[PAUSE]

Notice that Obtain/Build does not exist in isolation. A component built here must meet
specifications established in Design and Transition and must serve operational needs in
Deliver and Support.

---

## Section 7: The Activity — Deliver and Support (14:30–16:30)

**Deliver and Support** ensures that services are delivered and supported according to
agreed specifications and stakeholders' expectations.

[SHOW DIAGRAM: Deliver and Support — the operational activity closest to the user, with outputs flowing to Engage]

This is the operational heartbeat of IT. Every day, services must run reliably. Incidents
must be resolved. Service requests must be fulfilled. Users must receive the value they
were promised.

Deliver and Support receives:

- Service components from Obtain/Build
- New or changed services from Design and Transition
- Service requests from Engage

It produces:

- Services delivered to customers and users
- Resolved incidents and fulfilled requests
- Operational performance data flowing back to Improve

Key practices that operate within Deliver and Support include Incident Management, Service
Request Fulfillment, Service Desk, and Monitoring and Event Management. We will explore all
of these in Module 08.

[PAUSE]

---

## Section 8: Value Streams Explained (16:30–18:30)

Now that you understand each activity, let us talk about **value streams**.

A value stream is a specific combination of value chain activities and practices, carefully
sequenced to create a particular outcome for a specific stakeholder scenario. Think of it
as a recipe that uses ingredients from the six SVC activities.

[SHOW DIAGRAM: Two example value streams — one for incident resolution, one for new service deployment]

**Example Value Stream 1 — Incident Resolution:**

1. Engage — User reports an incident through the service desk
2. Deliver and Support — Service desk logs, diagnoses, and resolves the incident
3. Improve — Trend data from incidents feeds the improvement register

A simple three-activity stream producing one unit of value: the user's service is restored.

**Example Value Stream 2 — New Service Deployment:**

1. Engage — Stakeholder requirements are gathered
2. Plan — Strategic decision is made to fund the new service
3. Obtain/Build — Infrastructure and components are provisioned
4. Design and Transition — Service is designed, tested, and authorized
5. Deliver and Support — Service goes live and is operated
6. Improve — Post-launch performance is monitored and optimized

More complex, but every activity is purposeful.

[PAUSE]

The flexibility of value streams is one of ITIL 4's greatest strengths. Organizations can
define their own streams to match their unique context, culture, and tools. There is no
single prescribed sequence. That is a deliberate design choice.

---

## Section 9: Demand and Value Flows (18:30–20:30)

Let us close with the big picture: how **demand** enters the chain and how **value** exits it.

[SHOW DIAGRAM: SVS overview — Demand on the left, Value on the right, Service Value Chain in the center]

Demand flows in from external sources — customers, users, partners — through the Engage
activity. It also flows internally through the Plan and Improve activities, which generate
strategic and improvement demands that feed back into the chain.

Value flows out in multiple forms:

- **Outcomes** — the results stakeholders actually care about
- **Products and services** — the tangible deliverables
- **Cost reductions** — value delivered through efficiency
- **Risk reductions** — value delivered through reliability and compliance

Value is co-created. ITIL 4 is emphatic on this point. The service provider does not produce
value alone. The customer must consume and use the service for value to materialize. A
perfectly built service that nobody uses creates no value.

[PAUSE]

The entire Service Value Chain is designed around this co-creation principle. Every activity
contributes to enabling the customer to realize outcomes. Engage aligns expectations. Plan
provides direction. Obtain/Build and Design and Transition create capable components.
Improve makes the chain better over time. Deliver and Support keeps promises every day.

---

## Module Summary and Exam Tips (20:30–22:00)

Let us summarize the key points from Module 07.

The Service Value Chain has **six activities**: Plan, Improve, Engage, Design and Transition,
Obtain/Build, and Deliver and Support.

These activities are **not sequential** — they are interconnected and flexible, allowing
organizations to design value streams for specific outcomes.

**Demand enters through Engage** from external stakeholders, and through Plan and Improve
internally. **Value exits** as outcomes, products, services, cost reductions, and risk
reductions.

**Value streams** are specific sequences of activities and practices designed to produce
a particular outcome. Every organization designs its own streams for its unique context.

[SHOW DIAGRAM: Summary reference table — six activities, primary purpose, and key inputs/outputs]

For the ITIL 4 Foundation exam, know:

- The name and purpose of each of the six activities
- That Improve touches all other activities
- That Engage is the primary interface with external stakeholders
- The difference between a value stream and the Service Value Chain itself
- That value is co-created between provider and consumer

[PAUSE]

Next module, Module 08, we move into specific ITIL Management Practices: the Service Desk,
Incident Management, and Monitoring and Event Management. These practices plug directly
into the Deliver and Support activity we covered today.

Great work this module. I will see you in Module 08.

---

*End of Module 07 Video Script*

*Estimated delivery: 22 minutes at average instructional pace*
