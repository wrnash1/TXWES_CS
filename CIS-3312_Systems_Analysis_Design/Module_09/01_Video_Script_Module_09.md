# Video Script: Module 09 - System Design: Logical vs. Physical Design

**Course:** CIS-3312 Systems Analysis and Design
**Estimated Duration:** 22 minutes
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.

---

## Section 1: Welcome and Module Overview [00:00 - 03:00]

Welcome to Module 09. I am Professor Nash. Today we are covering one of the most important transitions in the systems development lifecycle: the move from requirements and analysis into design. Specifically, we are going to talk about what logical design and physical design mean, how the BA's role shifts during design, and what the key design decisions are that BAs help facilitate.

[SHOW DIAGRAM: Title slide — "Module 09: System Design — Logical vs. Physical Design" with BABOK KA 5 label and IIBA ECBA badge]

The design phase answers a different question than the analysis phase. Analysis asks: what does the system need to do? Design asks: how will the system do it? BAs do not write code, configure servers, or select database products — but they do facilitate the design process by translating requirements into logical models, evaluating design alternatives, and ensuring that design decisions remain aligned with the requirements baseline.

---

## Section 2: Logical Design [03:00 - 09:00]

[SHOW DIAGRAM: Side-by-side comparison — left column "Logical Design" showing a conceptual ERD with entity boxes, relationship lines, and no data types; right column "Physical Design" showing the same model converted to a SQL table schema with column names, data types, primary keys, and foreign keys in a monospace font]

Logical design describes what the system will do without specifying how it will be implemented in a particular technology. The word to remember is: technology-independent.

A logical data model describes the entities, attributes, and relationships the system needs to manage — without specifying which database product will store them. A logical process model describes what processes the system will perform — without specifying which programming language will implement them. A logical interface description describes what information will be presented to users — without specifying which framework or platform will render it.

The logical design artifacts that BAs typically produce or contribute to include: conceptual and logical ERDs, data dictionaries, logical DFDs, process specifications, and interface mockups or wireframes.

The key quality of a logical design artifact is that it could be implemented by any qualified developer using any appropriate technology — it does not constrain the implementation beyond the business requirements. This technology independence is important because it separates the business decisions (what the system must do) from the technical decisions (how it will be built).

> IIBA ECBA Exam Tip: The exam tests the logical vs. physical distinction directly. If a design artifact names a specific technology (Oracle, Python, AWS, React), it is physical. If it describes the system in platform-neutral terms, it is logical. Memorize this rule: technology-independent = logical; technology-specific = physical.

---

## Section 3: Physical Design [09:00 - 14:00]

[SHOW DIAGRAM: Physical design document excerpt — database schema with SQL syntax showing CREATE TABLE statements with column names, VARCHAR and INT data types, PRIMARY KEY and FOREIGN KEY constraints; beside it, a server infrastructure diagram with named cloud services]

Physical design specifies the actual technology implementation. It translates the logical design into concrete technical decisions.

Physical data design takes the logical ERD and produces a specific database schema: the exact table names, column names, data types, constraints, indexes, and stored procedures for a named database product (PostgreSQL, Oracle, Microsoft SQL Server). This is the document a database administrator would use to create the actual database.

Physical application design specifies the programming languages, frameworks, API protocols, and architectural patterns (three-tier, microservices, serverless) that will be used to build the application logic. This is the document a software architect produces.

Physical infrastructure design specifies the hosting environment: cloud provider, compute resources, storage, networking, security configuration, and deployment strategy. This is the document a DevOps or infrastructure engineer uses.

The BA's role in physical design is primarily evaluative, not constructive. BAs do not produce physical design documents — architects and engineers do. But BAs review physical design decisions against requirements to ensure they remain aligned. A physical design decision that would prevent the system from meeting a functional requirement must be flagged and resolved.

---

## Section 4: Design Options — Make, Buy, Subscribe [14:00 - 18:00]

[SHOW DIAGRAM: Make-Buy-Subscribe decision matrix — three columns: Build Custom (advantages: exact fit, competitive differentiation; risks: higher cost, longer timeline, maintenance burden), Buy COTS (advantages: proven, supported, faster; risks: configuration gaps, vendor dependency), Subscribe SaaS (advantages: fastest deployment, lowest upfront cost; risks: customization limits, data governance)]

One of the most important design decisions BAs facilitate is the make-versus-buy-versus-subscribe evaluation. Before the development team begins building, the BA should assess whether a commercial solution already exists that satisfies the requirements adequately.

Build custom means the organization develops the system from scratch using its own development team or contracted developers. This option makes sense when requirements are highly unique, when competitive differentiation depends on the system's specific capabilities, or when no commercial solution meets the requirements adequately. The risks are higher cost, longer timelines, and ongoing maintenance responsibility.

Buy COTS — Commercial Off-the-Shelf — means purchasing a packaged software product that is installed and configured. COTS solutions come with vendor support and regular updates. The risks are configuration gaps where the product does not perfectly match requirements, and vendor dependency. Common examples: ERP systems, HR platforms.

Subscribe SaaS — Software as a Service — means accessing the software through a subscription, typically via a web browser, without installing anything. SaaS has the lowest upfront cost and fastest deployment. The risks are limited customization, data governance concerns, and dependency on the vendor's roadmap. Common examples: Salesforce, ServiceNow, Microsoft 365.

The BA's role is to evaluate how well each option satisfies the requirements and recommend the option with the best balance of fit, cost, risk, and timeline.

---

## Section 5: Lab Preview and Closing [18:00 - 22:00]

This week's lab asks you to take a set of requirements and produce both a logical and a physical design artifact for the same system feature. You will also complete a make-buy-subscribe analysis for a provided scenario and write a recommendation.

Three exam reminders. First: technology-independent = logical design; technology-specific = physical design. Second: the BA facilitates and evaluates design — the BA does not write code, configure infrastructure, or produce physical design documents. Third: make-buy-subscribe analysis is a BABOK KA 5 design option evaluation technique. Know the tradeoffs for each option.

---

## Module 09 Complete

Next: Module 10 - User Interface and UX Design Principles

### Additional Resources

- iiba.org — BABOK Guide v3 KA 5: Define Design Options and Analyze Potential Value tasks
- iiba.org — ECBA exam blueprint weighting information
