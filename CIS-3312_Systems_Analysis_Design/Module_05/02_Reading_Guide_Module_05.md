# Reading Guide: Module 05 - Use Case Modeling and User Stories
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

### Introduction
Welcome to **Module 05 – Use Case Modeling and User Stories**! This module covers two of the most widely used techniques for modeling functional requirements from the user's perspective: use cases (common in predictive/UML-based approaches) and user stories (standard in Agile/Scrum environments). Both techniques shift the focus of requirements from system features to user goals, making requirements far more understandable to both business stakeholders and developers.

This module bridges traditional systems analysis (UML use case diagrams) with modern Agile practices (user story format, acceptance criteria, and backlog management), equipping you with tools relevant across all project methodologies.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Use Case**: A use case describes a sequence of interactions between an actor (a person or external system) and the system under development to achieve a specific business goal. Use cases focus on the *value delivered to the actor* rather than internal system mechanisms. A use case specification typically includes a name, primary actor, preconditions, main success scenario (step-by-step), alternative flows, and postconditions.

*   **Actor**: In use case modeling, an actor is any entity — human user, external system, or automated process — that interacts with the system from outside its boundary to achieve a goal. Actors are not part of the system; they initiate or participate in use cases. The same person can play multiple actor roles depending on the context (e.g., a librarian may act as both "Librarian" and "System Administrator" in different use cases).

*   **Use Case Diagram**: A use case diagram is a UML behavioral diagram that provides a high-level visual overview of a system's functional scope by showing the actors, the use cases they participate in, and the system boundary. It does not show the sequence of steps within a use case; it shows only what the system does and who interacts with it. Use case diagrams are excellent for stakeholder communication and scope definition.

*   **User Story**: A user story is a short, informal description of a software feature written from the perspective of an end user, following the format: "As a [role], I want [goal] so that [business value]." User stories are the primary unit of work in Agile/Scrum backlog management. They are deliberately brief to encourage conversation rather than serve as comprehensive documentation; the details emerge through discussion with the product owner and team.

*   **Acceptance Criteria**: Acceptance criteria are the specific conditions that a user story must satisfy for the product owner to accept it as done. They make the user story testable and define the boundary of the feature implementation. Well-written acceptance criteria use clear, verifiable language (e.g., "Given that a user is logged in, when they click Logout, then their session is terminated and they are redirected to the login page").

*   **Product Backlog**: A product backlog is a prioritized list of all work items — primarily user stories, but also bugs, technical tasks, and improvements — that the development team may be asked to implement. The product owner owns and maintains the backlog, continuously refining priorities based on business value, stakeholder feedback, and strategic direction. In Scrum, the sprint backlog is a subset of the product backlog selected for a specific sprint.

---

### 2. Certification Exam Tips
*   **Use Case vs. User Story**: The ECBA exam may test whether you can distinguish these two techniques. Use cases are more formal, document complete interaction flows, and are associated with traditional/UML methodologies. User stories are brief, focused on user value, and used in Agile contexts. Neither is "better" — the right choice depends on the project approach.
*   **Include vs. Extend Relationships**: In UML use case diagrams, `<<include>>` indicates a use case that is always invoked as part of another use case (mandatory sub-flow), while `<<extend>>` indicates an optional flow that may occur under specific conditions. A common ECBA question will describe a scenario and ask which relationship type is appropriate.
*   **INVEST Criteria for User Stories**: User stories should be Independent, Negotiable, Valuable, Estimable, Small, and Testable (INVEST). The ECBA exam may present a user story and ask you to evaluate its quality using the INVEST criteria — watch for stories that are too large (epic, not a story), not testable, or have no clear business value.
*   **Study Resource**: The Agile Alliance maintains a free glossary and resource library covering user stories, acceptance criteria, and backlog management at [https://www.agilealliance.org/glossary/](https://www.agilealliance.org/glossary/) — the "User Story" and "Acceptance Criteria" entries directly support ECBA exam preparation.

---

### Required Readings & Videos
*   **Required Reading**: Review the OMG UML Specification summary for behavioral diagrams (use case diagram notation) at [https://www.omg.org/spec/UML/](https://www.omg.org/spec/UML/). Also read the Agile Alliance's articles on User Stories and Acceptance Criteria at [https://www.agilealliance.org/glossary/](https://www.agilealliance.org/glossary/).
*   **Supplemental Reading**: BABOK® Guide v3 Techniques section — "Use Cases and Scenarios" and "User Stories." These entries describe both techniques from the IIBA perspective, which is the lens the ECBA exam uses.

---

### Lab & Activity Integration
In this week's lab, you will:
*   Draw a use case diagram for a provided scenario (a library management system), identifying at least three actors and five use cases, and using at least one `<<include>>` or `<<extend>>` relationship.
*   Write three user stories using the "As a / I want / So that" format, each with two to three acceptance criteria in Given/When/Then format.
*   Identify which items in a provided list of work items belong in a product backlog vs. which are too large (epics) and need splitting.

---

### 3. Study Checklist
- [ ] Read the glossary terms and write your own one-sentence version of each definition.
- [ ] Review OMG UML use case diagram notation at [https://www.omg.org/spec/UML/](https://www.omg.org/spec/UML/).
- [ ] Read the Agile Alliance User Story and Acceptance Criteria glossary entries at [https://www.agilealliance.org/glossary/](https://www.agilealliance.org/glossary/).
- [ ] Watch the Module 05 video lecture.
- [ ] Complete the use case diagram and user story lab before taking the quiz.
