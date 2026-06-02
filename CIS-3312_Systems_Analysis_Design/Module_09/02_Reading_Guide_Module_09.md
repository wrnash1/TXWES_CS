# Reading Guide: Module 09 - System Design: Logical vs. Physical Design

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 09 covers the design phase of the SDLC — specifically, the distinction between logical design (technology-independent) and physical design (technology-specific), the BA's role during design, and the make-versus-buy-versus-subscribe decision. These concepts appear in BABOK Guide v3 KA 5 (Requirements Analysis and Design Definition) and are tested on the IIBA ECBA exam. Understanding the logical-physical distinction is fundamental to understanding how requirements become a working system.

---

## 1. Core Vocabulary

### 1.1 Logical Design

Logical design describes what the system will do in technology-independent terms. Logical artifacts (conceptual ERDs, logical DFDs, wireframes, process specifications) describe business entities, processes, data, and interfaces without naming specific products, platforms, or programming languages. Logical design is the bridge between requirements and physical implementation.

### 1.2 Physical Design

Physical design specifies how the system will be built in technology-specific terms. Physical artifacts (SQL schemas, infrastructure diagrams, API specifications, deployment configurations) name specific products, platforms, and technologies. Physical design translates logical models into implementable technical instructions.

### 1.3 System Architecture

System architecture is the high-level structural design of a software system — its major components, how they interact, and the design principles that govern them. Common architectural patterns include three-tier architecture (presentation, business logic, data layers), microservices (independently deployable service components), and event-driven architecture (components communicate through events). Architecture is a physical design decision — it names specific structural approaches and (often) specific technology products.

### 1.4 Make-Buy-Subscribe Analysis

Make-buy-subscribe (also called build-vs.-buy) analysis is the evaluation of whether to build a custom system, purchase a packaged software product (COTS), or subscribe to a cloud-based service (SaaS). This analysis compares how well each option satisfies requirements against cost, risk, timeline, and long-term maintainability.

### 1.5 COTS (Commercial Off-the-Shelf)

COTS refers to packaged, commercially available software products that are purchased and configured — not custom-built. COTS solutions are typically faster to deploy than custom builds and come with vendor support and regular updates. The risk is that they may not precisely match all requirements and create vendor dependency.

### 1.6 SaaS (Software as a Service)

SaaS is a software delivery model in which the application is hosted by a vendor and accessed via the internet, typically through a subscription. SaaS offers the lowest upfront cost and fastest deployment but provides the least customization flexibility. Data governance and vendor reliability are the primary risk factors.

### 1.7 Design Options

Design options are the alternative solution approaches evaluated by the BA during the design phase. BABOK KA 5 requires BAs to define design options, analyze their potential value (benefits, costs, risks), and recommend the option that best satisfies requirements. Design options may include variations in build approach (make/buy/subscribe), architectural patterns, and integration strategies.

### 1.8 Solution Recommendation

A solution recommendation is the BA's formal recommendation of which design option best satisfies requirements given constraints. The recommendation includes supporting analysis: requirements coverage, cost-benefit comparison, risk assessment, and alignment with organizational standards. It is a key deliverable from the BABOK KA 5 "Recommend Solution" task.

### 1.9 Non-Functional Requirements in Design

Non-functional requirements (performance, security, scalability, availability) directly constrain physical design decisions. A requirement for 99.9% uptime constrains infrastructure design. A requirement for sub-second response time constrains database and caching design. BAs ensure non-functional requirements are carried into physical design review — they are as binding as functional requirements.

---

## 2. Logical vs. Physical Design Comparison

| Dimension | Logical Design | Physical Design |
|---|---|---|
| Technology independence | Yes — no product names | No — specific products named |
| Produced by | Business analyst, data modeler | Software architect, DBA, DevOps engineer |
| Examples of artifacts | Conceptual ERD, logical DFD, wireframe, data dictionary | SQL schema, infrastructure diagram, API spec, deployment config |
| Purpose | Communicate what the system does | Specify how the system will be built |
| Audience | Business stakeholders, developers (for translation) | Development team, architects, operations |
| BABOK phase | KA 5: Requirements Analysis and Design Definition | KA 5 / Development handoff |

---

## 3. Make-Buy-Subscribe Decision Matrix

| Option | Best for | Advantages | Risks |
|---|---|---|---|
| Build Custom | Unique, proprietary requirements; competitive differentiators | Exact requirements fit; full control | Higher cost; longer timeline; ongoing maintenance |
| Buy COTS | Standard requirements; vendor support needed | Proven product; vendor support; regular updates | Configuration gaps; vendor dependency; licensing cost |
| Subscribe SaaS | Standard requirements; fast deployment; limited budget | Lowest upfront cost; fastest deployment; no infrastructure | Limited customization; data governance; vendor roadmap risk |

---

## 4. System Architecture Patterns

| Pattern | Description | Typical Use |
|---|---|---|
| Three-tier | Presentation (UI), business logic (application), data (database) layers | Traditional web applications |
| Microservices | Small, independently deployable services communicating via APIs | Large-scale distributed systems |
| Monolithic | All components in a single deployable application | Small to medium applications with simple requirements |
| Event-driven | Components communicate by producing and consuming events | Real-time processing, loosely coupled integrations |
| Serverless | Functions deployed without managing servers; triggered by events | Variable workloads; cost-optimized deployments |

---

## 5. The BA's Role During Design

The BA's role during design is to bridge requirements and implementation — not to produce technical design documents but to ensure that design decisions remain aligned with requirements. Key BA activities during design include:

Facilitating design option evaluation: presenting requirements coverage analysis for each option.

Reviewing physical design documents: checking that no requirement is violated or overlooked in the physical design.

Managing requirements traceability: ensuring the RTM is updated as design decisions are made — each design component should trace back to a requirement.

Communicating with stakeholders: translating technical design decisions into business terms for non-technical stakeholders who need to understand the implications.

Identifying scope creep: recognizing when design decisions introduce functionality not covered by requirements (unplanned additions).

---

## 6. Logical-to-Physical Design Progression

| Artifact Type | Logical Version | Physical Version |
|---|---|---|
| Data model | Conceptual ERD with entity/attribute/relationship labels | SQL schema with table names, column names, data types, constraints |
| Process model | Logical DFD with process names and data flows | Application code modules, API endpoints, function names |
| Interface | Wireframe showing layout and content | HTML/CSS/framework-specific UI components |
| Infrastructure | Description: "web server, database, cache" | Named products: "Nginx on AWS EC2, PostgreSQL RDS, Redis ElastiCache" |

---

## 7. BABOK KA 5 Design Tasks

BABOK Guide v3 KA 5 includes specific tasks for the design phase:

- Define Design Options: identify alternative approaches to meeting requirements
- Analyze Potential Value and Recommend Solution: evaluate options against requirements, costs, and risks; produce a recommendation
- Specify and Model Requirements: create the logical models that will guide design
- Validate Requirements: confirm that requirements satisfy stakeholder needs before design commits resources

---

## 8. Certification Exam Tips

1. The logical vs. physical distinction is directly tested. If an artifact or decision names a specific technology (PostgreSQL, Python, AWS, React), it is physical. If it describes the system in platform-neutral terms, it is logical. This binary test applies to every design artifact the exam presents.

2. Make-buy-subscribe analysis appears as a scenario question. The exam will describe requirements and constraints and ask which option is most appropriate. Standard requirements + limited budget = SaaS or COTS. Unique requirements + competitive differentiation = custom build. Know the tradeoffs for each option.

3. The BA evaluates and recommends design options — the BA does not produce physical design artifacts. Architecture documents, SQL schemas, and deployment configs are produced by architects, DBAs, and engineers. BAs review them against requirements.

4. Non-functional requirements constrain physical design. Performance, security, scalability, and availability requirements must be traced into design decisions. An exam question may present a performance requirement and ask which design component must satisfy it.

5. System architecture describes the major components and their interactions — not the detailed implementation. If a question describes major structural decisions (layering, service decomposition, integration patterns), it is asking about architecture, not about logical design.

6. BABOK KA 5 is the primary knowledge area for design phase BA activities. The exam may ask which KA covers design option evaluation — the answer is KA 5.

7. Requirements traceability must continue into design. The RTM links requirements to design components just as it links requirements to test cases. BAs maintain this traceability throughout the SDLC.

8. The solution recommendation deliverable is produced by the BA. It summarizes design options, evaluates their tradeoffs, and recommends a specific approach. It is not the same as an architecture document — it is the BA's analysis of options presented to decision makers.

---

## 9. Required and Supplemental Reading

Required reading:

- BABOK Guide v3, KA 5: Requirements Analysis and Design Definition — Define Design Options and Recommend Solution tasks
- BABOK Guide v3, Chapter 10 (Techniques) — Decision Analysis; Functional Decomposition

Supplemental reading:

- Any systems analysis textbook section on logical vs. physical design (Hoffer, George and Valacich is a common reference)
- Software architecture patterns reference (Martin Fowler's Patterns of Enterprise Application Architecture is a standard industry text)

---

## 10. Study Checklist

- [ ] Explain the difference between logical and physical design using one concrete example of each.
- [ ] Classify five design artifacts as logical or physical and justify each classification.
- [ ] Describe the make-buy-subscribe tradeoffs and identify one scenario where each option is most appropriate.
- [ ] List the BA's responsibilities during design and identify two things the BA does NOT do during design.
- [ ] Explain how non-functional requirements affect physical design decisions.
- [ ] Identify which BABOK knowledge area covers design option evaluation.
- [ ] Watch the Module 09 video lecture.
- [ ] Complete the Module 09 lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.
