# Quiz: Module 09 - System Design: Logical vs. Physical Design
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

**Question 1**
A BA produces a conceptual Entity-Relationship Diagram showing Customer, Order, and Product entities with their relationships, using no technology-specific names. Which type of design artifact is this?
*   A) Physical design — because it specifies the structure of data the system will store
*   B) Logical design — because it describes the data model in technology-independent terms
*   C) Implementation design — because it will be directly converted into database tables during development
*   D) Operational design — because it models the runtime behavior of entities in the production system
*   **Correct Answer:** B) Logical design — because it describes the data model in technology-independent terms
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Physical design artifacts specify technology-specific implementations (e.g., SQL CREATE TABLE with data types and constraints). A conceptual ERD uses technology-neutral notation.
    *   *Why C is incorrect:* "Implementation design" is not a standard systems analysis category; the distinguishing feature of the artifact is its technology independence, making it logical.
    *   *Why D is incorrect:* "Operational design" is not a standard design classification; the artifact models data structure, not runtime system behavior.
    *   *Why B is correct:* A conceptual ERD expresses what data the system will manage and how entities relate, without specifying any database product, table structure, or SQL syntax — the hallmark of logical design.

---

**Question 2**
In the context of system design, which of the following is the most accurate definition of **system architecture**?
*   A) The visual wireframe sketches of all screens and navigation flows that users will interact with in the final system
*   B) The high-level structure of a software system — its major components, how they interact, and the principles governing their design
*   C) The detailed SQL schema defining all database tables, indexes, primary keys, and foreign key constraints
*   D) The project plan that specifies which development team members are responsible for building each software module
*   **Correct Answer:** B) The high-level structure of a software system — its major components, how they interact, and the principles governing their design
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Wireframes and screen flows are UI/UX design artifacts (covered in Module 10), not system architecture.
    *   *Why C is incorrect:* A SQL schema is a physical data design artifact — it is one output of physical design, not the definition of architecture.
    *   *Why D is incorrect:* A team assignment plan is a project management artifact; it is not system architecture.
    *   *Why B is correct:* System architecture describes the structural decisions about major components (layers, services, databases, interfaces) and their relationships — the blueprint that constrains all subsequent physical design decisions.

---

**Question 3**
According to BABOK® Guide v3 KA 5, which of the following design-phase activities is specifically the business analyst's responsibility?
*   A) Writing the source code for the user authentication module
*   B) Configuring the production database server and applying security patches
*   C) Defining and evaluating design options and recommending the solution approach that best satisfies the requirements
*   D) Conducting code reviews and approving pull requests before merging to the main branch
*   **Correct Answer:** C) Defining and evaluating design options and recommending the solution approach that best satisfies the requirements
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Writing source code is a developer responsibility; BAs are not expected to code the solution.
    *   *Why B is incorrect:* Database server configuration and patching are IT operations responsibilities; they are outside the BA's scope.
    *   *Why D is incorrect:* Code reviews are a software engineering quality practice performed by technical team members; the BA does not review code.
    *   *Why C is correct:* BABOK® KA 5 explicitly assigns the BA responsibility for defining design options (make/buy/subscribe, architecture alternatives), evaluating their tradeoffs, and recommending the option that best addresses requirements — bridging requirements and the development team's technical decisions.

---

**Question 4**
A company is evaluating whether to custom-build a new expense reporting system or subscribe to a commercial SaaS expense management platform. The requirements analysis shows that the company's expense policies closely match the standard features of three competing SaaS products, and the budget is limited. Which design option is most appropriate?
*   A) Custom build — to ensure the system exactly matches the organization's unique branding requirements
*   B) SaaS subscription — because the standard requirements match available products and the cost is lower than custom development
*   C) Custom build — because SaaS products can never meet enterprise security requirements
*   D) Delay the decision until all requirements are re-analyzed to check for any non-standard needs
*   **Correct Answer:** B) SaaS subscription — because the standard requirements match available products and the cost is lower than custom development
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Branding is a relatively minor concern; when requirements are standard and budget is constrained, building a custom system to satisfy only branding needs is not cost-justified.
    *   *Why C is incorrect:* Modern SaaS platforms routinely meet enterprise security requirements (SOC 2, ISO 27001, HIPAA-compliant options exist); this is a false generalization.
    *   *Why D is incorrect:* Requirements analysis has already been completed; delaying a straightforward make/buy decision to re-analyze is not justified by the scenario.
    *   *Why B is correct:* Make-vs.-buy analysis recommends COTS or SaaS when requirements are standard and commercial products provide a strong fit at lower cost and risk than custom development — exactly the conditions described.

---

**Question 5**
A physical design document specifies that the application will use PostgreSQL 16 for the relational database, React 18 for the front end, and Node.js 20 for the API layer, running on AWS EC2 instances behind an Application Load Balancer. What distinguishes this from a logical design document?
*   A) Physical design documents are shorter and less detailed than logical design documents
*   B) Physical design specifies concrete technology choices and configurations, while logical design is technology-independent
*   C) Physical design is produced by the business analyst, while logical design is produced by the developer
*   D) Physical design only covers the user interface, while logical design covers the data and process models
*   **Correct Answer:** B) Physical design specifies concrete technology choices and configurations, while logical design is technology-independent
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Physical design documents are often more detailed than logical design documents; document length is not the distinguishing characteristic.
    *   *Why C is incorrect:* BAs contribute to logical design (requirements, data models, process models); physical design is primarily the responsibility of architects and developers — but this is about roles, not the definition of what makes a design "physical."
    *   *Why D is incorrect:* Physical design covers all components (UI, data, API, infrastructure); it is not limited to user interface.
    *   *Why B is correct:* The defining characteristic of physical design is the presence of specific, named technology choices (PostgreSQL, React, Node.js, AWS). Logical design would describe the same system as "a relational database," "a web-based user interface," and "a RESTful API layer" without naming specific products.
