# Reading Guide: Module 09 - System Design: Logical vs. Physical Design
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

### Introduction
Welcome to **Module 09 – System Design: Logical vs. Physical Design**! Once requirements are fully analyzed and validated, the project transitions from the analysis phase to the design phase. This module explores the critical distinction between logical design (what the system must do, technology-independent) and physical design (how it will be built on specific technology), and the key design decisions that shape system architecture.

For business analysts, understanding design concepts is essential for two reasons: (1) BAs must be able to review design artifacts for requirements alignment, and (2) BABOK® Guide v3 KA 5 requires BAs to define design options and assess their tradeoffs. The ECBA exam tests whether candidates understand where BA responsibilities end and where developer/architect responsibilities begin.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Logical Design**: Logical design describes *what* the system will do and how it will function, expressed in technology-independent terms. It includes logical process models (DFDs), logical data models (conceptual ERDs), interface specifications, and business rule definitions. Logical design answers questions about system behavior and data structure without specifying which programming language, database product, or hardware platform will be used. It is the bridge between requirements and physical design.

*   **Physical Design**: Physical design specifies *how* the system will be implemented on a specific technology stack. It translates logical designs into concrete specifications: specific tables and SQL schemas derived from the ERD, actual screen layouts and navigation, server configurations, network topology, and API contracts. Physical design decisions are constrained by the technology choices made during the design phase and must satisfy all non-functional requirements (performance, security, scalability).

*   **System Architecture**: System architecture is the high-level structure of a software system — the major components (modules, services, databases, interfaces), how they interact, and the principles governing their design. Common architectural patterns include layered (presentation, business logic, data), client-server, microservices, event-driven, and service-oriented architecture (SOA). Architecture decisions have long-lasting implications and are expensive to change after implementation begins.

*   **Design Options**: In BABOK® KA 5, a design option is an alternative approach to building the solution — for example, build vs. buy, on-premises vs. cloud, a monolithic application vs. a microservices architecture. BAs are responsible for defining design options, evaluating their tradeoffs against requirements and constraints, and presenting recommendations to stakeholders. The selected option becomes the basis for physical design.

*   **Interface Design**: Interface design specifies how a system component communicates with external systems, users, or hardware. For user interfaces, this includes screen layouts, navigation flows, and interaction patterns. For system-to-system interfaces, it includes data exchange formats (JSON, XML), protocols (REST, SOAP), and API contracts. Good interface design ensures that components can integrate correctly without tight coupling.

*   **Make vs. Buy vs. Subscribe Analysis**: A make-vs.-buy analysis is a design-phase decision framework that compares the costs and risks of custom development (make) against acquiring a commercial-off-the-shelf (COTS) product (buy) or subscribing to a cloud-based SaaS platform (subscribe). BAs evaluate this tradeoff based on requirements fit, total cost of ownership, vendor viability, and strategic alignment. Most modern enterprise systems involve a combination of all three.

---

### 2. Certification Exam Tips
*   **Logical vs. Physical Boundary**: The ECBA exam tests whether you can classify design artifacts as logical or physical. Rule of thumb: if the artifact uses technology-specific names (Oracle, React, AWS, Python) → physical. If it describes behavior or data structure in technology-neutral terms → logical. A conceptual ERD is logical; a SQL CREATE TABLE script is physical.
*   **BA Role in Design**: BAs do not do physical design — that is the architect's and developer's responsibility. The BA's role in the design phase (BABOK KA 5) is to define and evaluate design options and ensure the selected design addresses the requirements. Expect ECBA questions asking whether a BA or a developer/architect is responsible for a specific design activity.
*   **COTS vs. Custom**: For "make vs. buy" questions on the ECBA exam, COTS is preferred when requirements are standard (commodity process), a proven product exists, and customization costs are low. Custom development is preferred when requirements are highly unique, competitive differentiation is at stake, or no viable commercial product exists.
*   **Study Resource**: The Software Engineering Institute (SEI) at Carnegie Mellon publishes free architecture guidance at [https://www.sei.cmu.edu/](https://www.sei.cmu.edu/) — the "Architecture Tradeoff Analysis Method (ATAM)" article provides real-world context for how design options are evaluated against quality attribute requirements.

---

### Required Readings & Videos
*   **Required Reading**: BABOK® Guide v3 Chapter 6 tasks — "Define Design Options" and "Analyze Potential Value and Recommend Solution." These describe the BA's specific role in the design phase. Also review BABOK® techniques: "Decision Analysis," "Benchmarking and Market Analysis" (for make/buy), and "Vendor Assessment."
*   **Supplemental Reading**: The IBM Architecture Center overview of common software architectural patterns is available at [https://www.ibm.com/architectures/](https://www.ibm.com/architectures/) — it provides concise descriptions of layered, microservices, event-driven, and SOA patterns that appear in ECBA scenario questions.

---

### Lab & Activity Integration
In this week's lab, you will:
*   Given a requirements document, identify three design options for the solution (e.g., custom build, COTS, SaaS) and create a simple tradeoff matrix comparing them on cost, fit, and risk.
*   Classify a provided list of ten design artifacts as either logical or physical design, with justification for each classification.
*   Sketch a one-page system architecture diagram showing the major layers (presentation, business logic, data) for a provided web application scenario.

---

### 3. Study Checklist
- [ ] Read the glossary terms and write your own one-sentence version of each definition.
- [ ] Read BABOK® Guide v3 Chapter 6 — "Define Design Options" and "Analyze Potential Value and Recommend Solution."
- [ ] Watch the Module 09 video lecture.
- [ ] Skim the IBM Architecture Center overview at [https://www.ibm.com/architectures/](https://www.ibm.com/architectures/).
- [ ] Complete the design options tradeoff matrix and artifact classification lab before taking the quiz.
