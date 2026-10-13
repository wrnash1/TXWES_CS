# Video Script: Module 13 — Solution Design and Prototyping

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Production Notes

- **Runtime Target:** 20–24 minutes
- **Format:** Lecture with annotated screen examples and sketch diagrams
- **Slides:** Approximately 26 slides

---

## SEGMENT 1 — Introduction (0:00–2:30)

[OPEN on slide: "Module 13 — Solution Design and Prototyping"]

Welcome back. I'm Professor Nash, and Module 13 is one of my favorite topics in this course — solution design and prototyping.

Here is why this matters. You have spent weeks gathering requirements, modeling processes, building data diagrams. At some point, stakeholders need to see something they can react to. Words and diagrams are valuable, but most people understand a system far better when they can interact with even a rough visual representation of it.

That is where prototyping comes in.

In this module we cover the spectrum from rough sketches to interactive mockups. We discuss two fundamentally different prototyping strategies — throwaway and evolutionary — and we examine when each one is appropriate. We also look at UI/UX principles that a BA needs to know and how prototypes get formally validated with stakeholders.

By the end of this module you will be able to create and distinguish between wireframes and mockups, explain the difference between throwaway and evolutionary prototyping, apply basic UI/UX principles to solution design, and lead a design validation session.

Let's start with the big picture.

---

## SEGMENT 2 — The Design Spectrum (2:30–5:00)

[SLIDE: "From Sketch to Prototype — The Design Spectrum"]

There is a spectrum of fidelity in design artifacts. Low fidelity on the left, high fidelity on the right. Understanding where each artifact sits on this spectrum tells you when to use it.

At the lowest fidelity end, we have **sketches** — hand-drawn boxes on paper or a whiteboard. Sketches are fast, disposable, and perfect for early-stage brainstorming. No one feels attached to a sketch.

One step up: **wireframes**. Wireframes are structured layouts that show the placement of interface elements — buttons, navigation menus, input fields, content blocks — without color, imagery, or final styling. They communicate structure, not appearance.

Above wireframes: **mockups**. Mockups add visual design — colors, fonts, spacing, images. They look like the finished product but are typically static images with no interactive behavior.

At the highest fidelity end: **interactive prototypes**. These are clickable, navigable simulations of the real system. Users can perform workflows and experience transitions, even though no real back-end logic exists.

As a BA, you will work across this entire spectrum depending on the project phase, stakeholder needs, and the complexity of what you are designing.

---

## SEGMENT 3 — Wireframes in Depth (5:00–8:00)

[SLIDE: "Wireframes — Structure Without Distraction"]

Wireframes are your primary tool for communicating layout and flow before any visual design decisions are made.

A wireframe answers these questions: What elements appear on this screen? Where are they positioned? What happens when a user interacts with them?

A wireframe does NOT answer: What color is the button? What font do we use? What image goes in the header?

That separation is intentional. When stakeholders see colors and fonts, they react to those choices — "I don't like that shade of blue" — instead of evaluating whether the workflow is correct. Wireframes keep the conversation focused on the right things during the analysis phase.

[SLIDE: Example wireframe — login screen layout]

A login page wireframe might show a rectangle for a logo placeholder at the top, two input field boxes labeled "Username" and "Password," a "Login" button, and a "Forgot Password" link below it. No colors. No images. Just layout.

Wireframing tools include Balsamiq, which deliberately uses a hand-drawn style to prevent stakeholders from treating wireframes as finished designs. Other tools include Figma, Axure, Microsoft Visio, and even PowerPoint or Google Slides.

When drawing wireframes, use annotations. An annotation is a note connected to an element that explains its behavior. "This field validates against the user directory on tab-out." That annotation captures a requirement that the wireframe shape alone cannot convey.

---

## SEGMENT 4 — Mockups and High-Fidelity Design (8:00–10:30)

[SLIDE: "Mockups — The Visual Layer"]

Mockups are wireframes with design applied. They answer the visual questions that wireframes deliberately avoided.

Mockups are valuable in several specific situations.

First: when gaining executive approval. Senior stakeholders often need to see something that looks real before they will commit to a direction. A polished mockup communicates professionalism and provides the visual context they need.

Second: when handing off to a UI design team. The mockup defines visual specifications so designers know the intent without having to interpret abstract boxes.

Third: when branding is a constraint. If the solution must conform to a corporate style guide, mockups show how that guide is applied to the specific screens in scope.

One caution: high-fidelity mockups can create false expectations. Stakeholders may assume that what they see is close to being "done." Establish explicit agreements upfront: this mockup represents the visual design direction, not a working system.

---

## SEGMENT 5 — Prototyping Strategies (10:30–14:00)

[SLIDE: "Two Prototyping Strategies — Throwaway vs. Evolutionary"]

Now we get to the strategic question: what is the prototype for?

There are two fundamentally different answers, and they lead to two completely different approaches.

### Throwaway Prototyping

In throwaway prototyping — also called rapid prototyping or exploratory prototyping — you build a prototype specifically to answer a question or resolve an uncertainty, and then you discard it.

The prototype is a learning tool. Once you have learned what you needed to learn, the prototype has served its purpose. The actual system will be built separately, using proper engineering practices.

Throwaway prototyping is appropriate when:

- Requirements are unclear and stakeholders need to see options before they can decide
- A specific interaction pattern needs to be tested before committing to it
- You need to surface hidden requirements that stakeholders cannot articulate without a concrete example
- Risk is high and assumptions need to be validated cheaply before development begins

The key characteristic: the code or design artifact produced is never intended to become part of the delivered system. This keeps quality standards for the prototype appropriately lower — speed matters more than robustness.

### Evolutionary Prototyping

In evolutionary prototyping — also called incremental or breadboard prototyping — you build a working prototype that is refined and extended over time to become the final system.

Each iteration adds functionality and polish. The prototype evolves continuously until it meets all requirements and quality standards.

Evolutionary prototyping is appropriate when:

- Requirements are reasonably well understood but benefit from iterative refinement
- The technology stack is familiar and can support early working builds
- Agile or iterative development practices are in use
- Stakeholders are available for frequent feedback cycles

The risk: if quality standards are not enforced from the beginning, a poorly built evolutionary prototype accumulates technical debt that becomes expensive to fix later.

---

## SEGMENT 6 — UI/UX Principles for Business Analysts (14:00–17:30)

[SLIDE: "UI/UX — What Every BA Needs to Know"]

Business analysts are not UX designers. You will typically collaborate with a UX specialist on larger projects. But you need to understand enough UI/UX to evaluate whether a proposed design actually supports user needs.

Here are the core principles every BA must know.

**Principle 1 — Visibility of system status.**
Users should always know what the system is doing. A page that goes blank after a button click with no feedback is a violation of this principle. The fix: loading indicators, confirmation messages, progress bars.

**Principle 2 — Match between system and the real world.**
Use language and concepts that match how users think, not how the database is organized. Users say "invoice," not "AR_TRANSACTION_RECORD."

**Principle 3 — User control and freedom.**
Users make mistakes. The system should support easy undo, back navigation, and confirmation dialogs before irreversible actions.

**Principle 4 — Consistency and standards.**
Use the same terminology, layout patterns, and interaction behaviors throughout. If "Save" means one thing on screen A, it should mean the same thing on screen B.

**Principle 5 — Error prevention and recovery.**
Design to prevent errors before they happen. When errors do occur, provide clear, actionable error messages — not "Error 404" or "Something went wrong."

**Principle 6 — Recognition over recall.**
Minimize what users must remember. Options should be visible or easily discoverable rather than requiring users to memorize commands or paths.

These principles come from Jakob Nielsen's usability heuristics — the foundational framework of the UX field. As a BA, you use these to critique proposed designs and generate design requirements.

---

## SEGMENT 7 — Design Validation (17:30–20:30)

[SLIDE: "Validating Your Design With Stakeholders"]

A prototype is only as valuable as the validation session that follows it. Design validation is the process of confirming that the proposed solution meets stakeholder needs before development commits resources.

Here is how a BA runs a design validation session effectively.

**Step 1 — Prepare scenarios, not scripts.**
Give participants realistic tasks to perform against the prototype. "Find the invoice for customer Acme Corp from last March and print it." Do not say "click the Invoices menu." You want to observe natural behavior, not guided behavior.

**Step 2 — Observe, do not lead.**
When participants struggle, resist the urge to help. Struggle reveals design problems. Silence is data.

**Step 3 — Document observations, not opinions.**
Record what you saw: "User clicked the wrong button twice before finding the correct one." Not: "Users found the interface confusing." The specific observation is actionable. The vague opinion is not.

**Step 4 — Debrief and prioritize.**
After the session, classify findings by severity: critical (blocks task completion), major (causes significant difficulty), minor (causes slight confusion). Critical and major findings require design changes before development.

**Step 5 — Iterate.**
Update the prototype and validate again if critical findings were found. Validation is not a one-time checkpoint.

---

## SEGMENT 8 — Prototyping in the BA Workflow (20:30–22:30)

[SLIDE: "Where Prototyping Fits in the BA Process"]

Let's place all of this in context. Where does prototyping fit in the overall BA workflow?

Prototyping typically occurs after initial elicitation and during requirements analysis, but before final requirements sign-off. It is a validation and refinement tool.

In waterfall projects: prototyping usually occurs during the design phase, and throwaway prototypes are common for resolving requirement ambiguities.

In agile projects: evolutionary prototyping is built into the sprint structure. Each sprint produces a working increment that stakeholders review and refine.

In either context, the BA's role is to ensure that prototypes are grounded in validated requirements — not wishful thinking — and that design validation findings are formally documented and feed back into the requirements baseline.

---

## SEGMENT 9 — Module Wrap-Up (22:30–24:00)

[SLIDE: "Module 13 Summary"]

Let's close with today's key takeaways.

The design spectrum runs from rough sketches through wireframes, mockups, and interactive prototypes. Each level of fidelity serves a different purpose.

Wireframes communicate structure and workflow without visual design distractions.

Mockups add visual design for approval and handoff purposes.

Throwaway prototyping creates disposable artifacts to resolve uncertainty and surface hidden requirements.

Evolutionary prototyping builds iteratively toward the final system, common in agile environments.

UI/UX heuristics — especially visibility, consistency, and error prevention — give BAs a framework to evaluate designs critically.

Design validation sessions produce specific, actionable findings that drive design improvements before development begins.

Complete your reading guide, lab, and quiz. Module 14 covers testing, validation, and quality assurance — which is where all this design work gets put to the test.

[END]

---

*Total runtime estimate: 22–24 minutes*
