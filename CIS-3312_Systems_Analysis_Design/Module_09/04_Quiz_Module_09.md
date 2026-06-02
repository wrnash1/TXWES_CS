# Quiz: Module 09 - System Design: Logical vs. Physical Design

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

A BA produces a conceptual Entity-Relationship Diagram showing Customer, Order, and Product entities with their relationships, using no technology-specific names. Which type of design artifact is this?

A) Physical design — because it specifies the structure of data the system will store

B) Logical design — because it describes the data model in technology-independent terms

C) Implementation design — because it will be directly converted into database tables during development

D) Operational design — because it models the runtime behavior of entities in the production system

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Physical design artifacts specify technology-specific implementations (e.g., SQL CREATE TABLE with data types and constraints). A conceptual ERD uses technology-neutral notation.
- Why C is incorrect: "Implementation design" is not a standard systems analysis category; the distinguishing feature of the artifact is its technology independence, making it logical.
- Why D is incorrect: "Operational design" is not a standard design classification; the artifact models data structure, not runtime system behavior.
- Why B is correct: A conceptual ERD expresses what data the system will manage and how entities relate, without specifying any database product, table structure, or SQL syntax — the hallmark of logical design.

---

## Question 2

In the context of system design, which of the following is the most accurate definition of system architecture?

A) The visual wireframe sketches of all screens and navigation flows that users will interact with in the final system

B) The high-level structure of a software system — its major components, how they interact, and the principles governing their design

C) The detailed SQL schema defining all database tables, indexes, primary keys, and foreign key constraints

D) The project plan that specifies which development team members are responsible for building each software module

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Wireframes and screen flows are UI/UX design artifacts, not system architecture.
- Why C is incorrect: A SQL schema is a physical data design artifact — it is one output of physical design, not the definition of architecture.
- Why D is incorrect: A team assignment plan is a project management artifact; it is not system architecture.
- Why B is correct: System architecture describes the structural decisions about major components (layers, services, databases, interfaces) and their relationships — the blueprint that constrains all subsequent physical design decisions.

---

## Question 3

According to BABOK Guide v3 KA 5, which of the following design-phase activities is specifically the business analyst's responsibility?

A) Writing the source code for the user authentication module

B) Configuring the production database server and applying security patches

C) Defining and evaluating design options and recommending the solution approach that best satisfies the requirements

D) Conducting code reviews and approving pull requests before merging to the main branch

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Writing source code is a developer responsibility; BAs are not expected to code the solution.
- Why B is incorrect: Database server configuration and patching are IT operations responsibilities; they are outside the BA's scope.
- Why D is incorrect: Code reviews are a software engineering quality practice performed by technical team members; the BA does not review code.
- Why C is correct: BABOK KA 5 explicitly assigns the BA responsibility for defining design options (make/buy/subscribe, architecture alternatives), evaluating their tradeoffs, and recommending the option that best addresses requirements — bridging requirements and the development team's technical decisions.

---

## Question 4

A company is evaluating whether to custom-build a new expense reporting system or subscribe to a commercial SaaS expense management platform. The requirements analysis shows that the company's expense policies closely match the standard features of three competing SaaS products, and the budget is limited. Which design option is most appropriate?

A) Custom build — to ensure the system exactly matches the organization's unique branding requirements

B) SaaS subscription — because the standard requirements match available products and the cost is lower than custom development

C) Custom build — because SaaS products can never meet enterprise security requirements

D) Delay the decision until all requirements are re-analyzed to check for any non-standard needs

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Branding is a relatively minor concern; when requirements are standard and budget is constrained, building a custom system to satisfy only branding needs is not cost-justified.
- Why C is incorrect: Modern SaaS platforms routinely meet enterprise security requirements; this is a false generalization.
- Why D is incorrect: Requirements analysis has already been completed; delaying a straightforward make-buy decision to re-analyze is not justified by the scenario.
- Why B is correct: Make-versus-buy analysis recommends COTS or SaaS when requirements are standard and commercial products provide a strong fit at lower cost and risk than custom development — exactly the conditions described.

---

## Question 5

A physical design document specifies that the application will use PostgreSQL 16 for the relational database, React 18 for the front end, and Node.js 20 for the API layer, running on AWS EC2 instances behind an Application Load Balancer. What distinguishes this from a logical design document?

A) Physical design documents are shorter and less detailed than logical design documents

B) Physical design specifies concrete technology choices and configurations, while logical design is technology-independent

C) Physical design is produced by the business analyst, while logical design is produced by the developer

D) Physical design only covers the user interface, while logical design covers the data and process models

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Physical design documents are often more detailed than logical design documents; document length is not the distinguishing characteristic.
- Why C is incorrect: BAs contribute to logical design; physical design is primarily the responsibility of architects and developers — but this is about roles, not the definition of what makes a design "physical."
- Why D is incorrect: Physical design covers all components; it is not limited to user interface.
- Why B is correct: The defining characteristic of physical design is the presence of specific, named technology choices (PostgreSQL, React, Node.js, AWS). Logical design would describe the same system as "a relational database," "a web-based user interface," and "a RESTful API layer" without naming specific products.

---

## Question 6

A BA is reviewing a physical design document for a new patient records system. The document specifies that all patient records will be stored in a relational database with no encryption at rest. The approved non-functional requirements include: "All patient data shall be encrypted at rest using AES-256 encryption." What is the BA's correct response?

A) Accept the design since encryption can be added later as a maintenance task

B) Escalate the conflict to the project sponsor and request that the non-functional requirement be removed from scope

C) Flag the design as non-compliant with the approved requirement and require the design to be updated before approval

D) Defer to the database architect since physical design decisions are outside the BA's scope

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Deferring a security requirement to maintenance exposes the organization to risk between go-live and maintenance implementation; non-functional requirements are binding at deployment.
- Why B is incorrect: Removing an approved non-functional requirement requires stakeholder approval and business justification; the BA's first action is to flag the gap, not remove the requirement.
- Why D is incorrect: BAs review physical design against requirements — that is a core BA responsibility during design, not an activity outside scope.
- Why C is correct: Non-functional requirements are as binding as functional requirements. The BA's role during design review is to identify gaps between the design and the approved requirements baseline and require resolution before approval. Flagging a requirement violation is the correct BA action.

---

## Question 7

A nonprofit organization is selecting a donor management system. The requirements include standard donor tracking, event registration, email communications, and donation processing. These are common features found in several established donor management SaaS products. The organization has no IT staff and a very small budget. Which design option is most appropriate?

A) Custom build — to ensure the nonprofit retains full ownership of its donor data in its own infrastructure

B) Buy COTS — to avoid recurring subscription fees and maintain software independence

C) Subscribe SaaS — because requirements are standard, budget is limited, and no IT staff is available to maintain on-premise software

D) Custom build — because only custom software can integrate with nonprofit-specific fundraising platforms

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Custom build requires significant upfront development investment and ongoing maintenance by skilled staff — neither of which this organization has.
- Why B is incorrect: COTS still requires installation, configuration, and server maintenance; without IT staff, maintaining on-premise software is not realistic for this organization.
- Why D is incorrect: Many SaaS donor management platforms include integration capabilities with fundraising and payment platforms; the generalization is not accurate.
- Why C is correct: SaaS is the correct choice when requirements are standard, budget is constrained, and no IT maintenance staff is available. The vendor hosts, maintains, and updates the system — eliminating the need for internal technical capacity.

---

## Question 8

A BA has produced a data flow diagram, an ERD, and a set of process specifications for a new billing system. The development team is now asking for the specific database schema (table names, column names, data types, primary keys, foreign keys) so they can begin database creation. Who is responsible for producing this artifact?

A) The business analyst — because the BA produced the ERD and data dictionary that the schema is derived from

B) The product owner — because the schema reflects business data ownership decisions

C) The database administrator or data architect — because the schema is a physical design artifact requiring technical expertise

D) The project manager — because the schema is a project deliverable that falls under the project manager's accountability

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: The BA produces the logical ERD and data dictionary; translating these into a technology-specific physical schema is the responsibility of the DBA or data architect.
- Why B is incorrect: Product owners define business priorities; physical database design is a technical responsibility, not a product ownership responsibility.
- Why D is incorrect: Project managers oversee schedules and resources; they do not produce technical design artifacts.
- Why C is correct: A SQL schema is a physical design artifact that requires knowledge of the specific database product, data type specifications, constraint syntax, and performance considerations. This is the responsibility of the database administrator or data architect, who works from the BA's logical ERD as input.

---

## Question 9

A requirement states: "The system shall process payment transactions within 1.5 seconds under normal load." This is a non-functional requirement. How does this requirement influence physical design?

A) It determines the layout and navigation of the payment screen in the user interface

B) It specifies the database table structure for storing transaction records

C) It constrains infrastructure and application performance decisions — such as caching strategy, database indexing, and server capacity

D) It defines the business rule for when a payment is considered complete

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Screen layout and navigation are UI design concerns, not performance requirements.
- Why B is incorrect: Table structure is determined by the data model, not by a response time requirement.
- Why D is incorrect: Defining when a payment is considered complete is a functional or business rule requirement, not what a performance non-functional requirement specifies.
- Why C is correct: A performance requirement (1.5-second response time) directly constrains physical design decisions about infrastructure (server capacity), application architecture (caching, async processing), and database design (indexes, query optimization). The architect and DBA must design the physical system to meet this constraint.

---

## Question 10

In BABOK Guide v3, which knowledge area is primarily responsible for the activities of defining design options, analyzing their potential value, and recommending a solution to stakeholders?

A) KA 2: Business Analysis Planning and Monitoring

B) KA 3: Elicitation and Collaboration

C) KA 4: Requirements Life Cycle Management

D) KA 5: Requirements Analysis and Design Definition

Correct Answer: D

Distractor Analysis:

- Why A is incorrect: KA 2 covers planning the BA's own work — approach, stakeholder engagement, governance — not design option evaluation.
- Why B is incorrect: KA 3 covers elicitation techniques and stakeholder collaboration for gathering requirements, not design analysis.
- Why C is incorrect: KA 4 covers requirements tracing, prioritization, and change management — maintaining requirements after they are defined, not design option analysis.
- Why D is correct: BABOK KA 5 (Requirements Analysis and Design Definition) includes the tasks of defining design options, analyzing potential value, and recommending solutions. It is the knowledge area that bridges the gap between approved requirements and the design decisions that implement them.
