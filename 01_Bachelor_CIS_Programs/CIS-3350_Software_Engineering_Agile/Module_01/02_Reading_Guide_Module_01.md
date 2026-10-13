# Reading Guide: Module 01 – Software Engineering Overview and SDLC Models

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3350 &BULL; SOFTWARE ENGINEERING & AGILE METHODOLOGIES</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 01 establishes the conceptual foundation for the entire course. Before mastering Scrum, you must understand the landscape from which it emerged. This guide walks you through the history of software engineering, the anatomy of the Software Development Life Cycle (SDLC), and the four primary SDLC models you are expected to compare and evaluate — both for this course and for the PSM I certification exam.

The Scrum Guide situates Scrum as an empirical framework built in response to the failures of predictive, plan-driven development. To understand that argument, you need to understand what plan-driven development looks like, why it fails in complex environments, and what empiricism offers instead.

---

## 1. The Origins of Software Engineering

Software engineering as a formal discipline was born at the 1968 NATO Software Engineering Conference in Garmisch, Germany. The conference was convened because the software industry was experiencing a "software crisis" — projects routinely ran over budget, missed schedules, delivered unreliable products, and were nearly impossible to maintain.

The conference produced a key insight: building large software systems requires the same kind of engineering discipline applied to bridges, aircraft, and chemical plants. That insight led to the establishment of software engineering as a field distinct from computer science.

Key figures in the early history:

- **Winston Royce (1970):** Documented what became known as the Waterfall model in his paper "Managing the Development of Large Software Systems." Ironically, Royce himself warned that the model was risky without iterative prototyping — a warning that was largely ignored for decades.
- **Barry Boehm (1986):** Introduced the Spiral model as a risk-driven alternative to Waterfall in "A Spiral Model of Software Development and Enhancement."
- **Kent Beck, Ward Cunningham, and others (1990s):** Pioneered Extreme Programming (XP) and other lightweight methods that prioritized working software and customer collaboration.
- **Ken Schwaber and Jeff Sutherland (1995):** Presented Scrum at OOPSLA 1995 and later codified it in the Scrum Guide.
- **Agile Manifesto authors (2001):** Seventeen practitioners gathered in Snowbird, Utah, and signed the Agile Manifesto, creating a unified philosophical statement for lightweight development methods.

---

## 2. The Software Development Life Cycle — Six Phases

Every SDLC model covers these six activities. Models differ in how they sequence and repeat them.

| Phase | Key Question Answered | Primary Output |
|---|---|---|
| Requirements | What should the software do? | Requirements specification |
| Design | How will we build it? | Architecture and detailed design documents |
| Implementation | Build it | Source code and executables |
| Testing | Does it work correctly? | Test reports, defect logs |
| Deployment | Release it to users | Running production system |
| Maintenance | Keep it working and evolving | Patches, enhancements, documentation updates |

**Non-functional requirements** are quality attributes the system must exhibit — performance, security, reliability, usability, scalability, and maintainability. They are as important as functional requirements and are frequently overlooked in early phases.

**The cost of change** is a fundamental concept in SDLC model selection. Research by Barry Boehm showed that errors discovered in later phases cost exponentially more to fix than errors discovered in earlier phases. Waterfall's linear structure means late-discovered requirement errors can require revisiting months of prior work. Agile's short iterations keep the cost of change relatively flat by discovering errors early and continuously.

---

## 3. SDLC Model Comparison Table

| Model | Structure | Flexibility | Risk Handling | Best Fit |
|---|---|---|---|---|
| Waterfall | Linear, sequential | Very low | Risks assessed once at start | Fixed requirements, regulated industries |
| Spiral | Iterative loops with risk analysis | Medium | Formal risk analysis each loop | Large, high-risk projects |
| Iterative | Repeated build-and-refine cycles | Medium-high | Risks addressed through iteration | Evolving requirements, medium complexity |
| Agile/Scrum | Short Sprints, continuous delivery | Very high | Risks surfaced and addressed each Sprint | Complex, uncertain, customer-driven products |

---

## 4. Waterfall Model — Deep Dive

The Waterfall model arranges phases in a strict linear gate sequence: Requirements → Design → Implementation → Testing → Deployment → Maintenance.

Characteristics:

- Each phase must be fully completed and formally approved before the next begins
- Extensive documentation is produced at each phase gate
- Changes to requirements after approval require formal change control
- Customer involvement is high at the start (requirements) and end (acceptance testing), but minimal in the middle

Strengths:

- Clear milestones and deliverables make project tracking straightforward
- Comprehensive documentation supports regulatory compliance and auditability
- Works well when requirements are truly fixed and well-understood

Weaknesses:

- The assumption of stable requirements is rarely valid for software
- Integration problems are discovered late (in the testing phase) when they are expensive to fix
- Customer does not see working software until near the end of the project, giving them no early opportunity to validate direction

---

## 5. Spiral Model — Deep Dive

The Spiral model, created by Barry Boehm, treats risk management as the central driving force of development. Each cycle (spiral loop) passes through four quadrants:

1. Determine objectives, alternatives, and constraints
2. Evaluate alternatives, identify and resolve risks (including building prototypes to resolve unknowns)
3. Develop and test the current cycle's deliverable
4. Plan the next cycle

The Spiral model is particularly well-suited to large government and defense contracts where requirements are complex and technical risks are high. Its formal risk resolution steps make it more heavyweight than Agile but more adaptive than pure Waterfall.

---

## 6. Iterative Model — Deep Dive

The Iterative model builds software in cycles (iterations), each producing a working, testable version of the product. Unlike Waterfall, you do not complete all requirements before beginning design. Unlike Scrum, there is no prescribed cadence, team structure, or set of events.

The Rational Unified Process (RUP) is the most prominent iterative framework. It organizes development into four phases — Inception, Elaboration, Construction, and Transition — each containing multiple iterations.

Key distinction from Agile: Iterative models still tend toward "big design up front" for the overall architecture, even if features are delivered incrementally.

---

## 7. Agile Model and the Path to Scrum

Agile is not a single methodology — it is a philosophy described by four values and twelve principles in the 2001 Agile Manifesto. Specific Agile frameworks include Scrum, Extreme Programming (XP), Kanban, Feature-Driven Development (FDD), and Dynamic Systems Development Method (DSDM).

The four Agile Manifesto values:

- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan

The word "over" is critical: items on the right have value, but when there is a trade-off, Agile practitioners choose the left-side item.

Scrum operationalizes Agile values through a specific framework of roles, events, and artifacts. Module 03 covers the full Scrum framework. For now, understand Scrum as Agile put into practice with just enough structure to be useful without being bureaucratic.

---

## 8. Empiricism vs. Defined Process Control

The Scrum Guide grounds Scrum in empirical process control theory, which contrasts directly with the defined process control approach used by Waterfall.

**Defined process control** assumes that given a well-defined process with known inputs, the output is predictable. This works for manufacturing — if you follow the same steps to assemble a car engine, you get the same car engine every time.

**Empirical process control** assumes that knowledge comes from experience, not prediction. When the work is complex and the future is uncertain, you cannot design the perfect process upfront. Instead, you inspect and adapt continuously.

Scrum's three empirical pillars:

- **Transparency:** Significant aspects of the process must be visible to those responsible for outcomes. The Sprint Backlog, Product Backlog, and Definition of Done all serve transparency.
- **Inspection:** Scrum artifacts and progress must be inspected frequently to detect undesirable variances. The four Scrum events are all inspection points.
- **Adaptation:** If inspection reveals that aspects of the process deviate outside acceptable limits, the process must be adjusted as soon as possible.

---

## 9. PSM I Exam Tips

**Tip 1:** The PSM I exam frequently presents a scenario where a team wants to "finalize all requirements before starting development." The correct Scrum response is to start with the current best understanding, deliver incrementally, and refine the Product Backlog continuously. Never freeze requirements.

**Tip 2:** Know the three empirical pillars by name: Transparency, Inspection, Adaptation. Questions may ask which pillar is being violated when, for example, a team does not share its Sprint progress with stakeholders.

**Tip 3:** Waterfall is tested on PSM I primarily as a contrast. Questions will describe plan-driven behaviors (upfront planning, sequential phases, fixed scope) and ask why they conflict with Scrum. The answer always relates to empiricism and the inability to predict complex outcomes.

**Tip 4:** The Agile Manifesto values are tested directly. Memorize all four. Pay attention to the "over" language — many wrong-answer choices will present the right-side values (documentation, processes, contracts, plans) as the Agile priority.

**Tip 5:** The Scrum Guide (2020) is the authoritative source for PSM I. It is free at scrum.org. You should read it in full. It is approximately 13 pages. Every PSM I question is answered by the Scrum Guide, so deep familiarity with its exact language is essential.

**Tip 6:** "Complexity" is a recurring concept in the Scrum Guide. The Stacey Matrix (not named in the Guide but foundational to Scrum theory) distinguishes simple, complicated, complex, and chaotic problem spaces. Scrum is designed for complex domains where empirical control outperforms defined process control.

**Tip 7:** On PSM I scenario questions, watch for the phrase "What should the Scrum Master do?" The answer almost never involves the Scrum Master making the decision for the team. The Scrum Master serves the team through coaching, facilitation, and removing impediments — not directing.

**Tip 8:** The cost-of-change concept is implicitly tested whenever a PSM I question describes discovering a problem late in development. The correct answer will always involve practices that surface problems earlier — short Sprints, frequent inspection, continuous testing.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 01 topics:

**1. The 2020 Scrum Guide — Scrum.org**
<https://scrumguides.org/scrum-guide.html>
The authoritative, free, 13-page specification for the Scrum framework. Every PSM I question is answered by this document. Read the "Scrum Theory" and "Scrum Values" sections before attempting any exam practice.

**2. Agile Manifesto and Twelve Principles — agilemanifesto.org**
<https://agilemanifesto.org/principles.html>
The original 2001 manifesto text plus the twelve supporting principles. Essential reading for understanding what Agile means philosophically before applying any specific framework.

**3. Barry Boehm, "A Spiral Model of Software Development and Enhancement" (IEEE Computer, 1988)**
<https://ieeexplore.ieee.org/document/59>
The original peer-reviewed paper introducing the Spiral model and the cost-of-change concept. IEEE Xplore provides free access to this landmark article. Focus on Figure 1 (the spiral diagram) and the risk management quadrant descriptions.

---

## 10. Study Checklist

- [ ] Define software engineering in your own words and explain the 1968 NATO crisis that motivated it
- [ ] Name and describe the six phases of the SDLC
- [ ] Explain the difference between functional and non-functional requirements with one example of each
- [ ] Describe the Waterfall model, including its phase-gate structure, strengths, and weaknesses
- [ ] Describe the Spiral model and explain what makes it risk-driven
- [ ] Describe the Iterative model and explain how it differs from both Waterfall and Agile
- [ ] State the four Agile Manifesto values from memory, including the "over" language
- [ ] Explain the three pillars of empiricism and connect each to a specific Scrum event or artifact
- [ ] Explain why Scrum is designed for complex rather than complicated problems
- [ ] Read the "Purpose of the Scrum Guide" and "Scrum Theory" sections of the 2020 Scrum Guide at scrum.org

---
