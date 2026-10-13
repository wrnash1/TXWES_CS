# Video Script: Module 02 - Business Process Management

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 21-23 minutes

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### [00:00 - 01:30] Opening

Professor Nash on camera. Title card: "Module 02 - Business Process Management."

"Welcome back to CIS-4320. Last module we established why enterprise systems exist — to break down functional silos and create integrated, consistent data across the organization. But here is the thing: ERP software doesn't just organize data. It organizes processes. And before you can configure a system, you have to understand the process the system is supposed to execute.

That is what Business Process Management is about. BPM is the discipline of documenting, analyzing, and improving how work flows through an organization. Every ERP implementation begins with BPM. Every Salesforce deployment begins with BPM. If you skip the process design work, you get a very expensive system that automates the wrong things.

Today we cover BPMN notation, process mapping, AS-IS and TO-BE analysis, and how these concepts connect to what the certification exams test."

---

### [01:30 - 05:00] What Is a Business Process?

Cut to slide: "Defining a Business Process."

"A business process is a repeatable sequence of activities that transforms an input into an output of value to a customer or stakeholder. Let me give you a concrete example.

Consider the Procure-to-Pay process — often abbreviated P2P. It starts when a department identifies a need: we are running low on warehouse supplies. It ends when the vendor has been paid and the goods are in use. In between, there are multiple steps: a purchase request is submitted, a manager approves it, a purchase order is sent to the vendor, the goods arrive and are inspected, the vendor invoice is matched against the purchase order, and payment is released.

Every one of those steps is an activity in the business process. Every one has an actor. Every one has an input and an output. And every one is a potential failure point if it is not clearly defined, assigned, and monitored.

[SHOW DIAGRAM: A left-to-right flow chart. Boxes in sequence: 'Purchase Request' → 'Manager Approval' → 'Purchase Order to Vendor' → 'Goods Receipt and Inspection' → 'Invoice and 3-Way Match' → 'Payment Released.' Below each box, show the responsible actor: Requester, Manager, Buyer, Warehouse Clerk, AP Clerk, AP Manager.]

ERP systems execute, enforce, and monitor exactly these kinds of processes. When you implement SAP Materials Management, you are configuring the system to carry out the P2P process. When you implement Salesforce, you are configuring the system to carry out the Lead-to-Cash process. The software is the engine; the business process is the road."

---

### [05:00 - 09:30] BPMN 2.0: The Language of Process Diagrams

Cut to slide: "BPMN 2.0 — Business Process Model and Notation."

"To document business processes consistently, we use a standard notation called BPMN — Business Process Model and Notation, version 2.0. BPMN is an internationally standardized visual language for how work flows through an organization. It is used by business analysts, ERP consultants, and software architects worldwide.

You need to know five core BPMN elements for the certification exams.

[SHOW DIAGRAM: A BPMN reference card. Five elements displayed side by side: a circle labeled 'Event,' a rounded rectangle labeled 'Task,' a diamond labeled 'Gateway,' a horizontal band labeled 'Swimlane,' and an arrow labeled 'Sequence Flow.']

First: Events. A circle. Events mark when something happens: a thin-border start event begins the flow, a thick-border end event closes it, and a double-border intermediate event marks things mid-process — like receiving a message or hitting a timer deadline.

Second: Tasks. A rounded rectangle. A unit of work performed by an actor. 'Review invoice,' 'Approve purchase request,' 'Ship order' — these are all tasks.

Third: Gateways. A diamond. Gateways control how the process flow splits and merges. Three types to memorize: Exclusive (XOR) — only one outgoing path fires based on a condition. Parallel (AND) — all outgoing paths fire simultaneously. Inclusive (OR) — one or more paths fire based on evaluated conditions.

Fourth: Swimlanes. Horizontal or vertical bands that assign each task to the actor or department responsible for it. If the Purchasing lane contains a task, Purchasing owns it. Swimlanes make ownership explicit and reveal where handoffs — and therefore delays and errors — occur.

Fifth: Sequence Flow. The arrows connecting tasks, events, and gateways. They show the order and direction of the process.

These five elements are the vocabulary of BPMN. Once you know them, you can read and draw any process diagram."

---

### [09:30 - 13:30] AS-IS and TO-BE Process Mapping

Cut to slide: "AS-IS vs. TO-BE: The Foundation of ERP Design."

"Every ERP implementation and every Salesforce deployment starts with two documents: the AS-IS process map and the TO-BE process map.

The AS-IS process map documents how the business currently operates. Not how management thinks it operates. Not how the policy manual says it should operate. How it actually operates — including the manual workarounds, the email threads, the spreadsheet hand-offs, and the approval delays. AS-IS mapping requires interviewing the people who do the actual work.

The TO-BE process map documents how the business will operate after the system is configured. The TO-BE map incorporates the capabilities and constraints of the target system. In an SAP implementation, the TO-BE processes should align as closely as possible with SAP's standard processes — because every deviation from standard increases cost and upgrade risk.

[SHOW DIAGRAM: Side-by-side BPMN diagrams. Left, AS-IS: purchase approval goes through manual email to manager, a 3-day wait symbol, manual entry into QuickBooks. Right, TO-BE: digital workflow submission, automated notification to manager, one-click approval, automatic posting to SAP. Red X marks over the eliminated manual steps in the AS-IS diagram.]

The gap between AS-IS and TO-BE is documented in a gap analysis. The gap analysis asks: what does the current process require that the standard system does not provide out of the box? Every gap is a decision point. You can change the business process to match the system — recommended. You can configure the system to accommodate the process — acceptable if justified. Or you can customize the system with new code — expensive and risky.

SAP's Activate methodology — covered in Module 04 — is built on Fit-to-Standard workshops that are structured gap analysis sessions. Exam tip: if a question asks which phase of SAP Activate involves Fit-to-Standard workshops, the answer is the Explore phase."

---

### [13:30 - 17:00] Process Bottlenecks and Improvement

Cut to slide: "Identifying and Eliminating Bottlenecks."

"One of the most valuable things BPM analysis reveals is process bottlenecks. A bottleneck is a step where work queues up faster than it can be processed, slowing everything downstream.

Bottlenecks have two common causes: resource constraints and handoff delays. A resource constraint is when the person or system responsible for a step cannot process requests fast enough — for example, a single manager who approves all expense reports for 200 employees. A handoff delay is when work sits waiting to be transferred from one actor to the next — for example, an invoice sitting in an inbox for 48 hours before anyone opens it.

[SHOW DIAGRAM: A process flow with a funnel shape inserted at the 'Manager Approval' step. A growing stack of request icons queues behind the funnel. Annotation below: 'Average wait: 3.2 business days. Root cause: single approver, reviews email once daily.']

Once you can measure a bottleneck, you can fix it. ERP systems provide three standard remedies. Workflow automation: the system notifies the approver automatically and tracks the deadline. Escalation rules: if not approved within 24 hours, the request automatically escalates to a backup approver. Delegation rules: the approver can assign authority to a deputy when out of office.

These capabilities are built into both SAP's workflow management engine and Salesforce Flows and Approval Processes. When you configure them, you are directly applying BPM improvement principles to system design."

---

### [17:00 - 19:30] BPM in Salesforce: Flows and Process Automation

Cut to slide: "Business Process Automation in Salesforce."

"Let me show you how BPM translates directly into Salesforce.

Salesforce has a declarative automation tool called Flow Builder. Flow Builder allows administrators — without writing a single line of code — to design automated business processes that execute when certain conditions are met.

For example: a TO-BE process might say that when an Opportunity is marked Closed Won, the system should simultaneously create an onboarding task for the customer success team, send a welcome email to the customer, and notify the finance team to generate an invoice. In BPMN terms, that is a parallel gateway — three things happening at the same time when one event occurs.

[SHOW DIAGRAM: Left side — a BPMN parallel gateway diagram. 'Opportunity Closed Won' event triggers a parallel split into three paths: 'Create CS Onboarding Task,' 'Send Customer Welcome Email,' 'Notify Finance.' Right side — a simplified Salesforce Flow screen showing the same three branches from a single trigger element. Arrow connecting left to right labeled 'BPMN becomes Flow.']

In Salesforce Flow Builder, you model that exact logic: the trigger, the parallel paths, and the actions at each path. The BPMN you draw becomes the blueprint for what you build in Flow Builder.

This is why learning BPMN is not just academic. Every time you design a Salesforce Flow or configure an SAP workflow, you are executing business process design. The exam tests whether you understand what kind of gateway to use, what swimlane ownership means, and how to distinguish a bottleneck from a routing decision."

---

### [19:30 - 21:30] Module Summary and Exam Tips

Cut to slide: "Module 02 Key Takeaways."

"Let's close Module 02 with the key takeaways.

First: a business process is a repeatable sequence of activities with a defined actor, input, output, and value. ERP systems execute business processes.

Second: BPMN 2.0 uses five core elements — events, tasks, gateways, swimlanes, and sequence flows. Know what each represents and when to use each gateway type: XOR for exclusive decisions, AND for parallel simultaneous paths, OR for conditional multi-path activation.

Third: AS-IS maps current state; TO-BE maps future state; gap analysis identifies what must be changed, configured, or customized to close the gap.

Fourth: bottlenecks are measurable points of delay. ERP systems resolve them through workflow automation, escalation rules, and delegation.

Three exam tips: On the SAP Associate exam, expect a scenario asking which BPMN gateway type to use — parallel, exclusive, or inclusive — read the scenario carefully for whether all paths always fire. On the Salesforce Associate exam, know that Flows automate business processes and replace manual steps. Both exams love AS-IS and TO-BE — know which phase each activity belongs to.

Complete the reading guide and lab before the quiz. Your lab this week asks you to draw an AS-IS diagram for a given scenario and design the TO-BE version with ERP automation. I'll see you in Module 03."

---

### [End Card]

Text on screen:

- Complete Reading Guide 02
- Complete Lab 02 (BPMN Process Mapping Exercise)
- Complete Quiz 02 (10 questions)
- Post to Discussion Forum 02 (due Wednesday)
- Peer responses due Sunday
- Trailhead: trailhead.salesforce.com — search "Business Process Automation with Flow"
