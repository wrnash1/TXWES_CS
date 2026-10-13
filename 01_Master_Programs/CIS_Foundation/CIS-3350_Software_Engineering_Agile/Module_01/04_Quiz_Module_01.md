# Quiz: Module 01 – Software Engineering Overview and SDLC Models

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Instructor:** Professor Nash | Texas Wesleyan University
**Total Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

Which SDLC model is characterized by linear, sequential phases where each phase must complete before the next begins?

- A) Scrum
- B) Waterfall
- C) Spiral
- D) Kanban

Correct Answer: B — Waterfall defines strict phase gates (requirements, design, implementation, testing, deployment) and no phase begins until the previous is signed off and documented.

Distractor Analysis:

- Why A is incorrect: Scrum is an iterative Agile framework delivering working software in short Sprints; it is the opposite of a linear sequential model.
- Why C is incorrect: Spiral is a risk-driven model that loops through planning, risk analysis, engineering, and evaluation repeatedly — not linear.
- Why D is incorrect: Kanban is a flow-based method focused on limiting work in progress, not a sequential phase model.

---

## Question 2

Which of the following is the most accurate definition of Software Development Life Cycle (SDLC)?

- A) A structured sequence of phases — requirements, design, implementation, testing, and deployment — that guides software production from initial concept to retirement
- B) The core security model consisting of Confidentiality, Integrity, and Availability that governs data protection
- C) A web accessibility standard defining minimum contrast ratios for public-facing applications
- D) A queue data structure in which the first element added is always the first removed

Correct Answer: A — The SDLC describes the full lifecycle of software from requirements through maintenance and retirement, with phase orderings that vary by model.

Distractor Analysis:

- Why B is incorrect: This defines the CIA Triad, a cybersecurity framework — unrelated to SDLC.
- Why C is incorrect: This describes WCAG, a web accessibility standard — unrelated to SDLC.
- Why D is incorrect: This defines a FIFO queue data structure — unrelated to SDLC.

---

## Question 3

A project team is building mission-critical medical device firmware with fully fixed, regulatory-approved requirements. Which SDLC model is most appropriate?

- A) Scrum with two-week Sprints
- B) Kanban with continuous flow
- C) Waterfall with formal phase-gate reviews
- D) Extreme Programming with pair programming

Correct Answer: C — When requirements are fixed and regulatory compliance requires documented sign-off at each stage, Waterfall's phase-gate structure ensures traceability and auditability.

Distractor Analysis:

- Why A is incorrect: Scrum is designed for evolving requirements; iterative adaptation conflicts with a locked regulatory specification.
- Why B is incorrect: Kanban suits ongoing operational flow, not fixed-scope, sequentially approved projects.
- Why D is incorrect: XP assumes frequent requirement changes — misaligned with a locked regulatory spec.

---

## Question 4

Which of the following best describes the Agile Manifesto's stance on documentation?

- A) Documentation is forbidden in Agile teams
- B) Agile teams must produce a complete design document before writing any code
- C) Working software is valued over comprehensive documentation, but documentation still has value
- D) All Agile decisions must be made verbally with no written records kept

Correct Answer: C — The Manifesto states "Working software over comprehensive documentation." The word "over" signals a priority when trade-offs arise, not an elimination of documentation.

Distractor Analysis:

- Why A is incorrect: The Manifesto explicitly says items on the right "have value"; it simply prioritizes the left-side items.
- Why B is incorrect: This describes "big design up front," a Waterfall characteristic that Agile explicitly reacts against.
- Why D is incorrect: No Agile framework prohibits written records; Scrum requires written artifacts such as the Product Backlog.

---

## Question 5

A software project encounters significant technical risk around a new cloud infrastructure platform. Which SDLC model is best suited to address this risk proactively at the start of each development cycle?

- A) Waterfall, because all phases are fully planned upfront
- B) Scrum, because Sprint Reviews invite stakeholder feedback on the increment
- C) Spiral, because it embeds a formal risk analysis step at the start of every loop
- D) Kanban, because work items flow continuously without phase constraints

Correct Answer: C — The Spiral model's defining characteristic is that each cycle begins with explicit risk identification and mitigation, making it ideal for projects with significant technical unknowns.

Distractor Analysis:

- Why A is incorrect: Waterfall performs risk assessment only during initial planning; it does not revisit risks between phases.
- Why B is incorrect: Scrum's Sprint Review is a stakeholder inspection of the product increment, not a formal risk analysis mechanism.
- Why D is incorrect: Kanban focuses on visualizing and limiting work in progress; it has no built-in risk analysis loop.

---

## Question 6

According to the Scrum Guide, Scrum is founded on empirical process control theory. Which three pillars support empiricism in Scrum?

- A) Planning, Execution, Review
- B) Transparency, Inspection, Adaptation
- C) Vision, Roadmap, Delivery
- D) Requirements, Design, Testing

Correct Answer: B — The 2020 Scrum Guide explicitly names Transparency, Inspection, and Adaptation as the three pillars of empiricism on which Scrum is founded.

Distractor Analysis:

- Why A is incorrect: Planning, Execution, and Review are generic project management phases, not Scrum's empirical pillars.
- Why C is incorrect: Vision, Roadmap, and Delivery are product management concepts, not Scrum's empirical pillars.
- Why D is incorrect: Requirements, Design, and Testing are SDLC phases, not empirical pillars.

---

## Question 7

The 1968 NATO Software Engineering Conference is historically significant because it:

- A) Launched the Agile Manifesto and its 12 principles
- B) Introduced Scrum as a framework for complex product development
- C) Identified a "software crisis" and established software engineering as a formal discipline
- D) Mandated the use of Waterfall for all government software contracts

Correct Answer: C — The 1968 conference identified widespread project failures and established that software development needed engineering-level discipline and rigor.

Distractor Analysis:

- Why A is incorrect: The Agile Manifesto was written in 2001 in Snowbird, Utah — 33 years after the NATO conference.
- Why B is incorrect: Scrum was first presented by Schwaber and Sutherland at OOPSLA 1995.
- Why D is incorrect: The conference was a research and discussion event, not a regulatory body.

---

## Question 8

In the context of SDLC model selection, the "cost of change curve" refers to the observation that:

- A) Agile teams spend more money on change management than Waterfall teams
- B) Requirement errors discovered late in a project cost exponentially more to fix than errors discovered early
- C) The cost of software licenses increases as a project scales from prototype to production
- D) Teams that change their SDLC model mid-project always exceed their original budget

Correct Answer: B — Barry Boehm's research showed that fixing a requirement error in the maintenance phase can cost 100 times more than fixing the same error in the requirements phase.

Distractor Analysis:

- Why A is incorrect: The cost of change curve measures the relative cost of fixing errors at different lifecycle phases, not a comparison of methodology budgets.
- Why C is incorrect: Software licensing costs are unrelated to the cost of change concept.
- Why D is incorrect: Mid-project model changes may affect budget, but this is not the definition of the cost of change curve.

---

## Question 9

Which of the following best distinguishes the Iterative model from the Waterfall model?

- A) The Iterative model delivers working software in repeated cycles; Waterfall completes the full product in a single linear pass
- B) The Iterative model requires formal risk analysis at the start of each cycle; Waterfall does not
- C) The Iterative model is used only for small projects; Waterfall is used only for large projects
- D) The Iterative model eliminates the need for testing; Waterfall requires extensive testing

Correct Answer: A — The Iterative model produces working increments through repeated build-and-refine cycles, allowing feedback and course correction between iterations; Waterfall completes all phases once in sequence.

Distractor Analysis:

- Why B is incorrect: Formal risk analysis at the start of each cycle is the defining characteristic of the Spiral model, not the Iterative model.
- Why C is incorrect: Both models can be applied to projects of varying sizes; size is not the distinguishing factor.
- Why D is incorrect: No SDLC model eliminates testing; it is a fundamental phase in all models.

---

## Question 10

A Scrum team's Product Owner wants to add a new high-priority feature to the current Sprint after Sprint Planning has concluded. What is the most appropriate response according to Scrum?

- A) The entire Sprint is cancelled and a new Sprint Planning session is held to incorporate the feature
- B) The Scrum Master immediately adds the feature to the Sprint Backlog without consulting the team
- C) The Sprint continues as planned; the Product Owner adds the feature to the Product Backlog for consideration in a future Sprint
- D) The Developers add the feature to the Sprint and extend the Sprint duration to accommodate the extra work

Correct Answer: C — Scrum protects Sprint integrity. The Sprint Goal and scope are set during Sprint Planning. New items are added to the Product Backlog and prioritized for future Sprints, unless the Sprint Goal itself becomes obsolete.

Distractor Analysis:

- Why A is incorrect: Cancelling a Sprint is reserved for situations where the Sprint Goal becomes obsolete, not for adding individual features.
- Why B is incorrect: The Scrum Master does not add items to the Sprint Backlog unilaterally; the Developers own the Sprint Backlog.
- Why D is incorrect: Sprints have a fixed timebox — their duration is never extended to accommodate additional scope.

---

### Question 11 (5 points)

Which of the following best describes a "non-functional requirement"?

- A) A requirement that has not yet been formally approved by the product owner
- B) A quality attribute the system must exhibit, such as performance, security, or scalability
- C) A feature that will be deferred to a future release and is therefore not currently functional
- D) A requirement written by a stakeholder who is not a developer and therefore lacks technical precision

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Approval status is a workflow concept; non-functional refers to the type of requirement, not its approval state.
  - C) Incorrect — Deferred features are backlog items, not non-functional requirements.
  - D) Incorrect — Non-functional is a technical classification (performance, reliability, etc.), not a description of who wrote the requirement.

---

### Question 12 (5 points)

The Rational Unified Process (RUP) is best classified as which type of SDLC model?

- A) Waterfall, because it defines sequential phase gates
- B) Agile, because it uses short Sprints with defined roles
- C) Iterative, because it organizes development into repeated cycles within four lifecycle phases
- D) Spiral, because it performs formal risk analysis before each phase

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — RUP does not require each phase to be fully completed before the next; iterations can overlap across phases.
  - B) Incorrect — RUP does not use Sprints or Scrum roles; it predates the Scrum Guide and is more heavyweight than Agile.
  - D) Incorrect — Formal risk quadrant analysis is the distinguishing feature of the Spiral model, not RUP.

---

### Question 13 (5 points)

According to the 2020 Scrum Guide, who is responsible for ordering the Product Backlog?

- A) The Scrum Master, as the servant-leader of the Scrum Team
- B) The Developers, because they understand the technical complexity of each item
- C) The Product Owner, who is accountable for maximizing the value of the product
- D) The stakeholders, because they represent the business interests driving priority

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — The Scrum Master serves and coaches the team but does not own or order the Product Backlog.
  - B) Incorrect — Developers provide effort estimates and technical input but do not order the Product Backlog.
  - D) Incorrect — Stakeholders provide input to the Product Owner, but the Product Owner has sole accountability for backlog ordering.

---

### Question 14 (5 points)

A software team follows a process where they release a new version of their product every two weeks, gather user feedback, and use that feedback to adjust the next version's scope. Which SDLC principle does this most directly exemplify?

- A) Defined process control — because each two-week cycle follows a defined set of steps
- B) Empirical process control — because the team inspects outcomes and adapts based on real evidence
- C) Waterfall phase-gate management — because each two-week block ends with a formal review
- D) Spiral risk management — because releasing to users is a form of risk mitigation

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Defined process control assumes predictable outputs from repeatable inputs; gathering feedback to change direction is empirical, not defined.
  - C) Incorrect — Waterfall phase-gate reviews approve a phase before the next begins; they do not involve shipping to real users for feedback.
  - D) Incorrect — Although releasing early can reduce market risk, this scenario describes empirical inspection and adaptation, not Spiral's formal risk quadrant process.

---

### Question 15 (5 points)

Winston Royce's 1970 paper on managing large software development is historically ironic because:

- A) He argued that software engineering was impossible and should be abandoned
- B) He actually advocated iterative prototyping, but later readers ignored that recommendation and adopted only the sequential diagram
- C) He invented the Agile Manifesto values twenty years before they were formally published
- D) He proved that Waterfall always delivers on time and within budget when followed correctly

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Royce made no such argument; his paper was about improving management of large software projects.
  - C) Incorrect — Royce did not write the Agile Manifesto values; those were authored collectively in 2001.
  - D) Incorrect — Royce explicitly warned that the sequential model was risky; he did not claim it always succeeds.

---

### Question 16 (5 points)

Which Agile Manifesto value most directly challenges the traditional Waterfall practice of requiring a fully signed-off requirements specification before design begins?

- A) Individuals and interactions over processes and tools
- B) Working software over comprehensive documentation
- C) Customer collaboration over contract negotiation
- D) Responding to change over following a plan

- **Correct Answer:** D
- **Distractor Analysis:**
  - A) Incorrect — This value addresses team dynamics and communication style, not the timing of requirements lock-in.
  - B) Incorrect — This value prioritizes a working product over documents, but does not directly address locking requirements before design.
  - C) Incorrect — This value concerns how agreements with customers are formed, not sequential phase structure.

---

### Question 17 (5 points)

In the Scrum framework, the Sprint is described as the "container for all other Scrum events." What does this mean?

- A) All Scrum events — Sprint Planning, Daily Scrum, Sprint Review, and Sprint Retrospective — occur within the fixed timebox of a single Sprint
- B) The Sprint is the longest Scrum event and all other events are nested inside it as sub-Sprints
- C) The Sprint Backlog contains all other Scrum artifacts as nested documents
- D) Sprints replace all other planning events, which are only held quarterly

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Incorrect — There are no sub-Sprints in Scrum; Sprint Planning, Daily Scrum, Review, and Retrospective are distinct events, not nested Sprints.
  - C) Incorrect — The Sprint Backlog is an artifact, not a container for other artifacts; and events are distinct from artifacts.
  - D) Incorrect — All four Scrum events occur every Sprint; none are quarterly.

---

### Question 18 (5 points)

Which of the following project characteristics makes the Spiral model a better choice than Agile/Scrum?

- A) The project has uncertain requirements and needs frequent customer feedback
- B) The project is a large government contract requiring formal, documented risk mitigation reports at each development milestone
- C) The project team is co-located and prefers daily stand-up meetings over formal documentation
- D) The project has a three-week deadline and must be completed with minimal process overhead

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Frequent customer feedback and uncertain requirements describe conditions where Agile/Scrum excels, not Spiral.
  - C) Incorrect — Co-located teams preferring daily stand-ups describe Scrum team dynamics, not Spiral's heavyweight risk-driven approach.
  - D) Incorrect — A three-week deadline with minimal overhead favors a lightweight Agile approach, not the heavyweight Spiral model.

---

### Question 19 (5 points)

The concept of "Definition of Done" in Scrum most directly supports which empirical pillar?

- A) Adaptation — because the team changes the definition after each Sprint
- B) Transparency — because it provides a shared, visible standard for what "complete" means
- C) Inspection — because the Definition of Done is reviewed at every Daily Scrum
- D) Planning — because it defines the scope for the next Sprint

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — The Definition of Done can be updated over time, but its primary purpose is to create a shared understanding, not to drive adaptation.
  - C) Incorrect — The Definition of Done is not reviewed at the Daily Scrum; it is applied when evaluating whether an increment is complete.
  - D) Incorrect — Sprint scope is set during Sprint Planning based on the Product Backlog; the Definition of Done defines quality criteria, not scope.

---

### Question 20 (5 points)

A team is debating whether to use a Kanban board or a Scrum Sprint to manage an ongoing customer support queue with no fixed end date and unpredictable incoming requests. Which is the better choice and why?

- A) Scrum, because two-week Sprints create accountability and regular review points
- B) Kanban, because it is designed for continuous flow work where items arrive unpredictably and there is no definable Sprint Goal
- C) Waterfall, because support work requires formal phase gates before each issue is closed
- D) Spiral, because each support ticket represents a risk that must be formally analyzed before resolution

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Scrum requires a Sprint Goal — a single objective the team commits to each Sprint; an unpredictable support queue rarely fits a coherent Sprint Goal.
  - C) Incorrect — Waterfall's sequential phase-gate structure is incompatible with a continuous stream of independent support tickets.
  - D) Incorrect — The Spiral model is used for large software development projects, not for managing operational support queues.
