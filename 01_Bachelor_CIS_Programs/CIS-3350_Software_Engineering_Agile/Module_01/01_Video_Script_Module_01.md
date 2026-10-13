# Video Script: Module 01 – Software Engineering Overview and SDLC Models

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Estimated Duration:** 22 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Instructor on screen for introduction and transitions
- Slides: Title cards for each section heading
- [SHOW DIAGRAM] tags indicate moments to cut to prepared visual assets
- All diagrams should be high-contrast with accessible alt-text captions

---

## Section 1 — Welcome and Learning Objectives [00:00–04:00]

"Welcome to Module 1 of CIS-3350, Software Engineering and Agile. I am Professor Nash at Texas Wesleyan University, and I am glad you are here.

This module establishes the entire intellectual foundation of the course. Before we can understand Scrum — before we can talk about Sprints, Product Backlogs, or Daily Scrums — we need to understand the bigger picture: what software engineering actually is, and why the industry has developed so many different approaches to building software over the past six decades.

By the end of this module you will be able to:

- Define software engineering and explain why it emerged as a formal discipline
- Describe the six major phases of a Software Development Life Cycle
- Compare and contrast Waterfall, Spiral, Iterative, and Agile SDLC models
- Identify which model fits a given project context
- Explain why Scrum's empirical approach is a direct response to the failures of plan-driven models

That last point is directly testable on the PSM I certification exam. Everything we cover today sets up that argument.

Let's start at the beginning."

---

## Section 2 — What Is Software Engineering? [04:00–08:30]

"The term 'software engineering' was first used at a 1968 NATO conference in Germany. The industry had a crisis. Software projects were failing at massive rates — over budget, behind schedule, and full of defects. Researchers and practitioners gathered and asked: can we apply the rigor and discipline of traditional engineering to software? That conference gave birth to software engineering as a formal discipline.

[SHOW DIAGRAM: Timeline from 1968 NATO Conference to present, marking key milestones: Waterfall 1970, Spiral 1986, Agile Manifesto 2001, Scrum Guide 2010, Scrum Guide 2020]

The IEEE defines software engineering as: 'The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software.' Notice three key words: systematic, disciplined, and quantifiable. Those words tell you software engineering is not hacking — it is principled construction.

Software engineering addresses the fundamental challenges that make software hard to build:

First, software is invisible. You cannot look at software the way you look at a bridge or a building. Defects hide in logic, not in physical structure.

Second, requirements change. Stakeholders do not always know what they want until they see something working. This is not a failure of communication — it is a property of complex human needs.

Third, software teams are large and distributed. Coordinating twenty engineers working on the same codebase requires discipline that a single programmer working alone never needs.

The SDLC — the Software Development Life Cycle — is our answer to these challenges. It is the framework that says: here is a structured sequence of phases, here is how information flows between them, and here is how we know when we are done."

---

## Section 3 — The Six Phases of the SDLC [08:30–13:30]

"Every SDLC model, regardless of whether it is Waterfall or Agile, covers the same fundamental activities. The models differ in how they order and repeat these activities, not in whether they perform them.

[SHOW DIAGRAM: SDLC six-phase cycle — Requirements, Design, Implementation, Testing, Deployment, Maintenance — shown as a circular diagram with arrows]

Phase one is Requirements. This is where we answer the question: what should the software do? We gather input from stakeholders, users, and domain experts. We document functional requirements — the specific behaviors the system must exhibit — and non-functional requirements — qualities like performance, security, and scalability.

Phase two is Design. Given the requirements, how will we build the system? Design covers architecture — how the system is structured at a high level — and detailed design — how individual components are constructed internally.

Phase three is Implementation, which most people call coding. Developers translate design decisions into executable software using programming languages, frameworks, and tools.

Phase four is Testing. We verify that the software works correctly — that it meets the requirements — and we validate that it solves the right problem for the user. Testing includes unit tests, integration tests, system tests, and acceptance tests.

Phase five is Deployment. We release the software to the production environment where real users interact with it.

Phase six is Maintenance. Software is never truly finished. After deployment, teams fix defects, make enhancements, and adapt the software to changing environments. Studies suggest that maintenance consumes between 60 and 80 percent of a software system's total lifetime cost.

Now, the critical question is not what these phases are — every model agrees on the phases. The question is: how do you sequence them? And that is where the SDLC models diverge dramatically."

---

## Section 4 — Comparing the SDLC Models [13:30–19:00]

"Let's walk through the four major models and compare them honestly.

[SHOW DIAGRAM: Four-quadrant comparison matrix — Waterfall, Spiral, Iterative, Agile — with axes for 'Flexibility to Change' (low to high) and 'Customer Involvement' (low to high)]

The Waterfall model, described by Winston Royce in 1970, arranges the six phases in a strict linear sequence. Requirements are fully defined and signed off. Then design begins. Then coding. Then testing. Then deployment. No phase begins until the previous one is complete.

The Waterfall model's strength is documentation clarity and traceability. If your requirements never change — as in regulated industries like medical device manufacturing — Waterfall's phase-gate structure provides the audit trail that regulators require.

Its weakness is catastrophic when requirements do change. If you discover in the testing phase that a fundamental requirement was misunderstood six months ago, you must re-do design and implementation. Studies of 1970s and 1980s government software projects found that requirements errors discovered late in Waterfall projects cost ten to one hundred times more to fix than errors discovered early. This is the 'cost of change curve' and it is the core argument against Waterfall for complex, uncertain projects.

[SHOW DIAGRAM: Cost-of-Change curve under Waterfall (exponential) vs. Agile (relatively flat)]

The Spiral model, proposed by Barry Boehm in 1986, addresses Waterfall's weakness by explicitly building risk analysis into the development cycle. Each loop of the spiral has four quadrants: determine objectives, identify and resolve risks, develop and test, and plan the next iteration. The spiral is excellent for large, high-risk projects — NASA uses spiral-derived approaches for mission-critical systems.

The Iterative model builds software in repeated cycles, each producing a working — though incomplete — version. Unlike Spiral, Iterative does not mandate formal risk analysis steps. It simply says: build a little, show it, get feedback, build more. The Rational Unified Process (RUP) is the most famous iterative framework.

The Agile model is not a single methodology — it is a family of approaches united by the values declared in the 2001 Agile Manifesto. Agile methods deliver working software in short cycles, welcome changing requirements even late in development, and build projects around motivated individuals with face-to-face communication.

[SHOW DIAGRAM: Sprint cycle — Plan, Build, Test, Review, Retrospect — shown as a tight loop with 'Potentially Shippable Increment' as output]

Scrum is the most widely-used Agile framework. And this is where the PSM I exam becomes directly relevant.

PSM I Exam Tip: The Scrum Guide describes Scrum as founded on three pillars of empiricism: transparency, inspection, and adaptation. These pillars are a direct philosophical response to Waterfall's assumptions. Waterfall assumes you can predict the future accurately enough to plan the entire project upfront. Empiricism says: you cannot predict accurately, so inspect frequently and adapt constantly. Know this distinction. It appears in multiple PSM I scenario questions."

---

## Section 5 — Why This Matters for the PSM I Exam [19:00–22:00]

"Let me close with the direct connection between this module and your PSM I certification.

The Scrum Guide opens with a statement about complexity. It says Scrum was developed in the early 1990s by Ken Schwaber and Jeff Sutherland for developing and sustaining complex products. The word 'complex' is doing serious work there. Complex environments are ones where cause and effect are only understood in retrospect — where you cannot plan your way to success, you must experiment your way there.

Waterfall was designed for complicated problems — problems where expertise and upfront analysis can produce a correct plan. Scrum was designed for complex problems — problems where the right answer emerges through iteration and feedback.

[SHOW DIAGRAM: Stacey Matrix — Simple / Complicated / Complex / Chaotic quadrants with Waterfall and Scrum positioned appropriately]

PSM I Exam Tip: When a PSM I question gives you a scenario where a team is facing uncertain requirements and asks which approach to use, the answer will always leverage Scrum's empirical pillars. Never choose 'finalize requirements before starting development' as a Scrum answer.

PSM I Exam Tip: Know the four Agile Manifesto values by heart:

- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan

The 'over' language is critical. The right side has value — the Manifesto says so explicitly. But when there is a trade-off, Agile chooses the left side. Exam questions frequently present a trade-off situation and ask what an Agile team should do.

As you move into Module 2 we will go deep on the Agile Manifesto and its 12 Principles. But today's foundation — understanding where Agile came from and why it exists — makes every subsequent module more coherent.

Thank you for your attention. Head to the Reading Guide, complete the Lab, take the Quiz, and participate in the Discussion Forum this week. I will see you in Module 2."

---

## End Card

- Next module: Module 02 – Agile Manifesto and the 12 Principles
- Additional Resources (Scrum.org only):
  - The Scrum Guide (free): scrum.org/resources/scrum-guide
  - Professional Scrum Master I (PSM I) exam details: scrum.org/professional-scrum-master-i-certification

---
