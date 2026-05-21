# Reading Guide: Module 02 - Business Process Management

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 02 - Business Process Management**! This module examines how organizations analyze, model, and improve the workflows that drive business outcomes. Understanding Business Process Management (BPM) is foundational to ERP implementation: before you can configure a system, you must understand what the business actually does step by step.

You will learn how to read and create BPMN 2.0 process diagrams, identify bottlenecks in existing workflows, and apply process optimization concepts — all of which are tested in SAP implementation methodology questions and inform how Salesforce Flows automate multi-step business processes.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Business Process Management (BPM)**: A discipline that uses systematic methods to discover, model, analyze, measure, improve, and optimize business processes. In an ERP context, BPM determines how the system will be configured to match real organizational workflows before go-live.
* **BPMN 2.0 notation**: The Business Process Model and Notation standard (version 2.0), a globally recognized graphical language for drawing process diagrams. It defines specific symbols — rounded rectangles for tasks, diamonds for gateways, circles for events — that any trained analyst can read regardless of the software tool used.
* **Swimlanes**: Horizontal or vertical bands within a BPMN diagram that separate tasks by the role, department, or system responsible for performing them. Swimlanes make ownership and handoffs between departments immediately visible.
* **Events**: BPMN elements (drawn as circles) that represent something that happens during a process — a start trigger, an intermediate milestone, or an end state. Events drive process flow without performing work themselves.
* **Gateways**: BPMN decision points (drawn as diamonds) that split or merge process flow based on conditions. An exclusive gateway (X) routes to exactly one path; a parallel gateway (+) activates all outgoing paths simultaneously.
* **Process optimization**: The practice of analyzing a current-state process to eliminate waste, reduce cycle time, and improve quality — then redesigning and reconfiguring the system to reflect the improved future-state workflow.

---

### 2. Certification Exam Tips

* **SAP focus:** SAP uses its own methodology called SAP Activate, which includes a Discover phase for process mapping. Exam questions may ask you to identify which phase involves documenting AS-IS and TO-BE business processes. The answer is always the Explore or Fit-to-Standard phase.
* **Salesforce Certified Associate focus:** Salesforce Flows are the platform's primary automation tool and are directly modeled on process-flow logic. Understanding gateways (decision elements) and events (triggers) in BPMN directly maps to Flow's Decision elements and Record-Triggered entry conditions.
* **Diagram reading tip:** In BPMN exam questions, always identify the swimlane owner first, then trace the gateway conditions. Most wrong-answer traps use the correct task sequence but assign it to the wrong swimlane (wrong department).
* **Study Resource:** Explore the free Salesforce Trailhead module [Business Process Automation](https://trailhead.salesforce.com/content/learn/modules/business_process_automation) — it connects BPMN-style process thinking directly to how Salesforce automates workflows using Flows and Approvals.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the Salesforce Trailhead module [Business Process Automation](https://trailhead.salesforce.com/content/learn/modules/business_process_automation) — a free, no-cost unit that shows how enterprise process logic translates into automated Salesforce workflows.
* **Required Video:** Watch the video lecture on **Business Process Management** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Draft a procurement process map using BPMN 2.0 swimlanes**: Draw a three-lane diagram (Requestor, Procurement, Finance) showing a purchase requisition from submission through vendor payment, labeling all gateways and events correctly.
* **Analyze bottlenecks in a fulfillment pipeline**: Given a sample order-to-cash process diagram, identify the two steps with the longest average cycle time and propose one process change that would reduce each.
* **Define event gateways**: In your procurement diagram, replace an exclusive gateway with an event-based gateway and explain how waiting for a document receipt (event) differs from evaluating a fixed condition.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to draw each BPMN symbol from memory.
* [ ] Complete [Business Process Automation](https://trailhead.salesforce.com/content/learn/modules/business_process_automation) on Trailhead (earn the badge).
* [ ] Watch the video lecture on **Business Process Management** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab procurement BPMN diagram and bottleneck analysis.
* [ ] Proceed to the weekly quiz.
