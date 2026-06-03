# Reading Guide: Module 13 — Solution Design and Prototyping

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Overview

This reading guide supports Module 13's video lecture on solution design and prototyping. Prototyping is a core technique in the BABOK Guide, appearing under both Elicitation and Collaboration and Requirements Analysis and Design Definition. Understanding how to select, create, and validate prototypes is an essential ECBA competency.

**Estimated reading and study time:** 90–120 minutes

---

## Learning Objectives

By the end of this module you will be able to:

1. Distinguish between sketches, wireframes, mockups, and interactive prototypes.
2. Compare throwaway and evolutionary prototyping strategies and select the appropriate approach for a given context.
3. Apply Nielsen's usability heuristics to evaluate a proposed interface design.
4. Plan and conduct a design validation session.
5. Document design validation findings using severity classifications.
6. Connect prototyping and design validation to the ECBA knowledge areas.

---

## Section 1 — The Purpose of Prototypes in Business Analysis

### 1.1 Why Prototypes Matter

Requirements documents describe what a system must do. Prototypes show what a system will look and feel like. These are fundamentally different communication channels, and both are necessary.

Research in cognitive psychology consistently shows that people are better at evaluating concrete examples than abstract descriptions. A stakeholder who struggles to articulate exactly what reporting format they need will often recognize immediately — when shown a prototype — whether a proposed layout meets their needs.

Prototypes serve several specific BA purposes:

- Eliciting latent requirements that stakeholders could not articulate without a visual stimulus
- Resolving conflicting interpretations of requirements documents
- Communicating design intent to developers and UX specialists
- Gaining stakeholder sign-off with a shared visual baseline
- Reducing rework by catching design problems before development begins

### 1.2 BABOK Alignment

The BABOK Guide lists Prototyping as a technique under two knowledge areas:

- Elicitation and Collaboration (using prototypes to gather requirements)
- Requirements Analysis and Design Definition (using prototypes to define and validate the solution design)

ECBA candidates should understand prototyping both as an elicitation tool and as a design validation tool.

---

## Section 2 — The Design Fidelity Spectrum

### 2.1 Fidelity Defined

Fidelity refers to how closely a design artifact resembles the final product. Low-fidelity artifacts are fast, rough, and abstract. High-fidelity artifacts are detailed, polished, and closely resemble the final product.

### 2.2 Sketches

Sketches are hand-drawn or informally drawn layouts. They are appropriate for:

- Initial brainstorming with the project team
- Quick exploration of layout alternatives
- Communicating rough ideas before any formal design commitment

Sketches are deliberately imprecise. Their value is speed and openness — they invite modification and do not signal that decisions have been made.

### 2.3 Wireframes

Wireframes are structured, low-to-medium fidelity layouts that specify the placement and hierarchy of interface elements without applying visual design. Key characteristics:

- Elements shown as labeled boxes, not styled components
- No color, imagery, or typography — typically grayscale
- Navigation flows indicated with arrows
- Behavior documented via annotations

Wireframes communicate the information architecture and interaction model. They are appropriate during early design phases when structure and workflow are being defined.

Common wireframing tools include Balsamiq, Figma (in low-fidelity mode), Axure RP, and Microsoft Visio.

### 2.4 Mockups

Mockups are high-fidelity static representations of the finished interface. They include:

- Color schemes and branding elements
- Typography and iconography
- Realistic content placeholders
- Spacing and layout exactly matching design specifications

Mockups are appropriate when visual design decisions need stakeholder approval, when handing off to development teams, or when conformance to a style guide must be demonstrated. They remain static — users view them but cannot interact with them.

### 2.5 Interactive Prototypes

Interactive prototypes are clickable simulations that allow users to navigate between screens and experience workflow sequences. They may range from simple click-through prototypes (clicking a button shows the next screen) to sophisticated simulations with conditional logic.

Interactive prototypes are the highest-cost artifact to create but provide the most realistic validation environment. They are appropriate when:

- Complex workflows need to be tested end-to-end
- Usability testing with actual end users is planned
- Stakeholder approval requires a realistic demonstration

---

## Section 3 — Prototyping Strategies

### 3.1 Throwaway Prototyping

Throwaway prototyping (also called rapid or exploratory prototyping) creates a prototype for the sole purpose of learning, then discards it. The prototype is never intended to become part of the delivered system.

Characteristics:

- Speed is the priority over quality or robustness
- Code and design are deliberately "rough"
- Typically used for high-uncertainty requirements
- Result feeds back into requirements, not directly into development

Advantages:

- Low cost relative to the insights gained
- No technical debt carried into production
- Encourages stakeholder engagement by making options tangible
- Surfaces hidden requirements early

Disadvantages:

- Time investment is "lost" if the prototype is truly discarded
- Stakeholders may resist discarding a prototype they find functional
- Requires clear communication that the prototype is not the final product

### 3.2 Evolutionary Prototyping

Evolutionary prototyping (also called breadboard or incremental prototyping) builds a prototype that grows and improves over successive iterations until it becomes the final delivered system.

Characteristics:

- Quality standards must be maintained from the beginning
- Each version is a working, tested increment
- Feedback loops with stakeholders are continuous
- Common in agile and iterative development environments

Advantages:

- No wasted effort — every iteration contributes to the final system
- Users interact with real, functioning software early
- Requirements are refined through actual use rather than abstract discussion

Disadvantages:

- Technical debt risk if early iterations cut corners
- Difficult to estimate final cost and schedule
- Scope creep risk if iteration cycles are not bounded

### 3.3 Choosing a Strategy

Use this decision framework when selecting a prototyping strategy:

| Condition | Recommended Strategy |
|---|---|
| Requirements are highly uncertain | Throwaway |
| Agile development methodology in use | Evolutionary |
| High-risk design decisions need validation | Throwaway |
| Stakeholders are available for frequent reviews | Evolutionary |
| Development timeline is fixed and short | Throwaway |
| Technology stack is mature and well-understood | Evolutionary |

---

## Section 4 — UI/UX Principles for Business Analysts

### 4.1 Nielsen's Usability Heuristics

Jakob Nielsen's ten usability heuristics are the foundational framework for evaluating interface design. A BA does not need to be a UX designer, but understanding these heuristics enables meaningful critique of proposed designs.

The ten heuristics are:

1. Visibility of system status
2. Match between system and the real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

### 4.2 BA-Relevant Heuristics in Detail

The following four heuristics are most relevant to requirements work.

**Visibility of system status** means the interface always keeps users informed about what is happening. From a BA perspective, this means requirements must specify feedback behaviors: confirmation messages after saves, loading indicators during processing, progress percentages during long operations.

**Match between system and the real world** means using language that reflects users' domain, not technical implementation language. A BA enforces this by reviewing screen labels, error messages, and field names against the business vocabulary established during elicitation.

**Error prevention** means the design prevents errors before they occur — not just recovers from them. Examples include disabling irrelevant fields, providing input format hints, requiring confirmation before destructive actions, and validating input in real time. BAs capture these as functional requirements.

**Consistency and standards** means the same action, term, or element behaves the same way throughout the system. BAs enforce this by maintaining a UI standards section in the requirements specification and reviewing all screens against it.

### 4.3 Accessibility Considerations

WCAG (Web Content Accessibility Guidelines) define accessibility standards that are increasingly required by law and organizational policy. BAs should document accessibility requirements explicitly:

- Color contrast ratios for text
- Keyboard navigation support
- Screen reader compatibility
- Form field labeling standards

Accessibility is a requirements concern, not just a design preference. If accessibility requirements are not documented by the BA, they are typically not implemented.

---

## Section 5 — Design Validation

### 5.1 Purpose of Design Validation

Design validation confirms that a proposed solution design meets stakeholder needs before development commits resources. It is distinct from requirements validation (which confirms requirements are correct and complete) and testing (which confirms the built system meets requirements).

### 5.2 Planning a Validation Session

Effective design validation sessions require planning on four dimensions.

**Participants:** Include representative end users — not just managers. The people who will use the system daily are the right validators. Aim for five to eight participants; beyond that, incremental insights diminish.

**Tasks:** Prepare realistic task scenarios based on actual business workflows. Task scenarios should be goal-based ("Complete the quarterly reconciliation report") rather than action-based ("Click the Reports menu").

**Environment:** Conduct sessions in conditions that resemble actual work conditions as closely as possible. Remote validation via screen-sharing tools is acceptable for distributed teams.

**Observer roles:** At least two observers are ideal — one facilitating, one taking notes. The facilitator asks follow-up questions; the note-taker captures behavioral observations.

### 5.3 Running the Session

Facilitation principles for design validation:

- Begin with a brief explanation: participants are evaluating the design, not being evaluated themselves
- Ask participants to think aloud — narrate what they are trying to do and what they expect to happen
- Do not intervene when participants struggle unless they are completely stuck
- Ask probing questions after tasks: "What were you expecting to happen when you clicked that?" "Was there anything that confused you?"

### 5.4 Documenting Findings

Classify each finding by severity:

| Severity | Definition | Action Required |
|---|---|---|
| Critical | Prevents task completion | Must be resolved before development |
| Major | Causes significant difficulty or repeated errors | Should be resolved before development |
| Minor | Causes slight confusion but does not block task | Address in next design iteration |
| Cosmetic | Polish or preference issue | Address if time permits |

A findings log captures: session date, participant ID, task scenario, observation (behavioral, specific), severity classification, and recommended design change.

### 5.5 Iteration After Validation

Design validation is not a one-time event. When critical or major findings are discovered, the BA revises the prototype and conducts a follow-up validation with a subset of participants to confirm the design change resolved the issue.

This iterative loop — design, validate, refine, validate again — is the professional standard for solution design.

---

## Section 6 — Prototyping in Project Methodologies

### 6.1 Waterfall Context

In waterfall projects, prototyping typically occurs during the design phase, after requirements are baselined. Throwaway prototypes are common for resolving ambiguities. Results feed back into the requirements specification or design document before development begins.

### 6.2 Agile Context

In agile projects, evolutionary prototyping is embedded in the sprint structure. Sprint reviews function as ongoing validation sessions. The BA (often in the Product Owner role) ensures that the sprint backlog reflects validated design decisions.

### 6.3 Hybrid Context

Many organizations use a hybrid approach: initial throwaway prototyping to validate the high-level design concept, followed by evolutionary prototyping during agile delivery sprints. BAs in hybrid contexts must be explicit about which approach is being used at each stage.

---

## Section 7 — ECBA Exam Focus Points

ECBA candidates should know:

- The definition of prototyping as an elicitation and design technique per BABOK
- The difference between throwaway and evolutionary prototyping
- How prototypes fit into the Requirements Analysis and Design Definition knowledge area
- The core Nielsen heuristics and how they generate requirements
- How design validation findings are classified and acted upon

---

## Key Terms

| Term | Definition |
|---|---|
| Wireframe | Low-fidelity layout showing structure and element placement without visual design |
| Mockup | High-fidelity static visual representation of the final interface |
| Throwaway prototype | Disposable prototype built to answer a question, then discarded |
| Evolutionary prototype | Prototype refined over iterations to become the final delivered system |
| Usability heuristic | A general principle for evaluating interface design quality |
| Design validation | Process of confirming a design meets stakeholder needs before development |
| Fidelity | Degree to which a design artifact resembles the finished product |
| Think-aloud protocol | Validation technique where participants narrate their thoughts while using a prototype |
| Annotation | Note attached to a wireframe element explaining its intended behavior |
| WCAG | Web Content Accessibility Guidelines — accessibility standards for digital interfaces |

---

## Self-Check Questions

Answer these before attempting the quiz.

1. What is the key difference between a wireframe and a mockup?
2. Why are wireframes deliberately kept free of color and visual styling?
3. When is throwaway prototyping more appropriate than evolutionary prototyping?
4. Name three of Nielsen's ten usability heuristics.
5. What is the difference between a critical and a major finding in a design validation session?
6. Why should validation task scenarios be goal-based rather than action-based?
7. How does prototyping fit into the agile sprint structure?

---

*Module 13 Reading Guide | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
