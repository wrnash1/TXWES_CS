# Reading Guide: Module 07 — Requirements Elicitation Techniques

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3312 &BULL; SYSTEMS ANALYSIS & DESIGN</text>
    
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


## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Overview

Requirements elicitation is the process of discovering, drawing out, and capturing stakeholder needs. It is not a passive activity of simply asking people what they want — it is an active investigative discipline that uses structured techniques to surface stated needs, unstated assumptions, and tacit knowledge that stakeholders cannot always articulate directly.

BABOK Guide v3 covers elicitation and collaboration as Knowledge Area 4 (KA 4). The IIBA ECBA exam tests knowledge of elicitation techniques and judgment about which technique is appropriate in different contexts. This guide organizes all key content for both exam preparation and practical application.

---

## Why Elicitation Is Challenging

Requirements elicitation is difficult for several reasons that are important to understand before studying specific techniques.

### Tacit Knowledge

Much of what experienced workers know is tacit — embedded in practice, habit, and muscle memory rather than in written documentation. When you ask a claims adjustor "how do you process a claim?" they may describe the standard path but forget to mention the three informal exception-handling rules they developed over years of experience. Observational techniques are specifically designed to surface this tacit knowledge.

### Stakeholder Conflicts

Different stakeholders have different needs, priorities, and constraints. The needs of a department manager (comprehensive reporting), a frontline worker (simple data entry screens), and an IT administrator (minimal integration complexity) may all be legitimate but may conflict with each other. The BA's role is to surface these conflicts during elicitation — not leave them to emerge during development or testing.

### Requirements Uncertainty

Stakeholders often do not know what they need until they see what they do not want. Abstract requirements discussions frequently produce vague answers. Showing stakeholders a concrete prototype — even a rough paper mockup — generates far more specific and useful feedback than asking them to describe requirements in the abstract.

### Stated vs. Unstated Requirements

Stakeholders state some requirements explicitly: "The system must process orders within 30 seconds." But many requirements are unstated because stakeholders assume them as obvious: "The system will, of course, not show one customer another customer's data." Unstated requirements are as binding as stated ones — the BA must actively probe for them.

---

## Elicitation Techniques

### Interviews

Interviews are one-on-one or small-group conversations between the BA and a stakeholder. They are the most flexible and widely used elicitation technique.

**Interview types:**

**Structured interviews** use a fixed set of questions asked in the same sequence to every participant. They are useful when comparing responses across multiple stakeholders, ensuring consistent topic coverage, and producing analyzable results. The limitation is that the fixed structure may prevent exploration of important unexpected topics.

**Unstructured interviews** begin with an open-ended prompt and follow the conversation naturally. They are excellent for initial exploration when the BA does not yet know enough about the domain to ask specific questions. The limitation is that unstructured interviews are difficult to compare across participants.

**Semi-structured interviews** combine a prepared set of core questions with freedom to probe and follow interesting responses. This is the most common BA approach in practice — it ensures key topics are covered while allowing the depth and flexibility needed to surface important insights.

**Effective interview practices:**

- Prepare open-ended questions in advance, organized by topic area
- Begin with broad context-setting questions before narrowing to specifics
- Use probing follow-ups: "Can you give me an example?" "What happens when that fails?"
- Allow silence — stakeholders often provide important information when the interviewer pauses rather than rushing to the next question
- Take notes or record the session (with permission); do not rely on memory alone
- Send a summary to the stakeholder after the interview to confirm accuracy

### Workshops

Requirements workshops bring multiple stakeholders together in a facilitated session to elicit, discuss, and validate requirements collaboratively. Workshops are most effective when:

- Requirements involve multiple departments or stakeholder groups whose perspectives must be reconciled
- There is known conflict between stakeholder groups that needs structured resolution
- Time pressure makes sequential individual interviews impractical
- Group interaction is likely to generate ideas that no single stakeholder would produce alone

The BA's role in a workshop is facilitator — managing discussion, keeping the group focused, ensuring all voices are heard (not just the loudest), capturing agreements and disagreements, and synthesizing outputs into documented requirements.

**Workshop advantages:** Speed, group consensus, cross-functional visibility, immediate issue resolution.

**Workshop risks:** Dominant personalities suppressing quieter stakeholders; groupthink; logistics complexity for large, distributed groups.

### Joint Application Development (JAD)

JAD is a structured workshop methodology developed for requirements elicitation in software development contexts. A JAD session follows a formal agenda with defined roles: Sponsor (articulates business objectives), Facilitator (manages the session), Subject Matter Experts (contribute domain knowledge), IT representatives (contribute technical constraints), and Scribe (documents all outputs).

JAD sessions typically run one to three days and produce: a documented requirements specification, decision logs recording agreements reached, an issues log for items requiring further investigation, and participant sign-off on session outputs.

JAD sessions are investment-intensive but compress the elicitation timeline significantly by resolving requirements in real time rather than through extended back-and-forth correspondence.

### Observation

Observation involves the BA watching how work is actually performed — in the actual work environment, during normal operations. The fundamental insight behind observation is that people describe their work as it is supposed to be performed; observation reveals how it is actually performed.

**Passive observation:** The BA observes without participating or asking questions during the session. The goal is to see the natural flow of work without interference. Questions are saved for a structured debrief afterward.

**Active observation (shadowing):** The BA accompanies the worker and asks questions during the session. This is useful for immediately clarifying what is being observed but may interrupt the natural flow of work.

Observation is the technique most effective at surfacing tacit knowledge — the informal rules, workarounds, exception paths, and undocumented steps that experienced workers follow automatically. It is particularly valuable for understanding complex operational processes where the gap between documentation and practice is likely to be significant.

**Observation is most effective when combined with interviews:** observe the process, then interview the worker about specific things you saw. This combination surfaces both what happens and why.

### Document Analysis

Document analysis involves reviewing existing artifacts to understand the current state, identify constraints, and extract requirements. Documents reviewed may include: current system documentation, process procedure manuals, regulatory requirements, sample reports and outputs, data dictionaries, organizational charts, audit reports, and prior project deliverables.

**Value of document analysis:**

- Identifies existing data structures that must be preserved, migrated, or replaced
- Surfaces regulatory constraints that the new system must comply with
- Provides baseline terminology and definitions used by the organization
- Reveals what was previously attempted and why it succeeded or failed

**Limitation:** Documents describe the intended state, not the actual state. A procedures manual that has not been updated in three years may not reflect how the process is actually executed. Document analysis must be validated through other techniques — particularly observation and interviews.

### Surveys and Questionnaires

Surveys enable the BA to collect requirements input from large numbers of stakeholders efficiently. They are most appropriate when:

- The stakeholder population is large or geographically distributed
- Quantitative data is needed to prioritize requirements or identify patterns across a population
- Questions are well-defined enough to be answered without facilitation

**Survey design principles:**

| Question Type | Use Case | Limitation |
|---|---|---|
| Closed questions (rating scale, yes/no, multiple choice) | Quantifiable, comparable data | May not capture nuance or unexpected answers |
| Open questions (short answer, free text) | Richer narrative and context | Requires qualitative analysis; harder to compare |
| Likert scale | Priority ranking, satisfaction measurement | Response set bias; depends on scale design |

**Survey limitations:** Cannot probe unexpected responses in real time. If a stakeholder provides an unusual answer, the BA cannot follow up immediately. Surveys work best when paired with follow-up interviews for stakeholders who provided particularly important or unexpected responses.

### Prototyping

A prototype is a partial, preliminary representation of a system used to elicit and validate requirements through stakeholder interaction and feedback. Prototyping is based on the insight that stakeholders often cannot articulate requirements abstractly but can quickly and specifically react to a concrete representation.

**Throwaway prototypes** (wireframes, paper mockups, low-fidelity screen mockups) are built quickly to generate feedback and then discarded. A wireframe showing proposed screen layout and navigation can be produced in hours and generates specific, actionable feedback about field placement, workflow, and missing functionality. Wireframes are not intended to be the actual system — they are conversation tools.

**Evolutionary prototypes** are iteratively refined into increasingly complete representations. In Agile environments, evolutionary prototyping is common — working software is built in small increments with continuous stakeholder review.

**When prototyping is most effective:**

- Stakeholders struggle to articulate requirements in the abstract
- The user interface is central to the requirements (screen layout, workflow, navigation)
- Multiple design options need to be compared through stakeholder feedback
- Requirements change frequently and iterative refinement is more efficient than upfront specification

---

## Requirements Documentation

### Why Documentation Matters

Verbal requirements agreements are insufficient. Documentation provides the shared reference that all project participants — business stakeholders, developers, testers, and management — can review, verify, and hold each other accountable to throughout the project lifecycle.

### Quality Characteristics of Requirements

BABOK Guide v3 defines the quality characteristics of well-formed requirements:

| Characteristic | Description |
|---|---|
| Clear | Unambiguous — only one interpretation is possible |
| Complete | All necessary information is included; no gaps |
| Consistent | No internal contradictions; aligned with other requirements |
| Verifiable | Can be tested or demonstrated to be met or not met |
| Traceable | Connected to the business need or stakeholder need that motivated it |
| Feasible | Achievable within known constraints |
| Prioritized | Relative importance is established |

### Requirements Levels

BABOK Guide v3 organizes requirements into four levels:

**Business requirements** — describe why the organization needs a change; the goals and objectives the project must achieve.

**Stakeholder requirements** — describe what stakeholders need from the solution to achieve the business requirements.

**Solution requirements** — describe what the solution must do and how it must perform. Solution requirements have two sub-types: functional requirements (what the system does) and non-functional requirements (quality attributes — performance, security, availability, usability).

**Transition requirements** — describe what must happen to move from the current state to the future state — data migration, training, change management.

### Documentation Formats

Common formats include:

- **Business Requirements Document (BRD)** — traditional document used in waterfall projects
- **Software Requirements Specification (SRS)** — detailed technical specification of system behavior
- **User stories** — Agile format: "As a [user role], I want [goal] so that [reason]"
- **Use cases** — structured descriptions of how actors interact with the system to achieve goals

---

## Stakeholder Management

### Stakeholder Identification

A stakeholder is anyone with an interest in the project outcome — those who are affected by the solution, those who influence decisions about it, and those who have knowledge or authority needed for its success. Stakeholders include: direct users, business owners, IT staff, regulators, customers of the organization, and anyone else the system will affect.

### Stakeholder Analysis

A stakeholder analysis maps stakeholders along dimensions of interest and influence:

- **High interest, high influence** — key partners requiring intensive, regular engagement
- **High interest, low influence** — keep informed; their concerns are legitimate even if they cannot direct decisions
- **Low interest, high influence** — keep satisfied; their support or opposition could determine project success
- **Low interest, low influence** — monitor; minimal engagement required

### Managing Stakeholder Conflicts

When stakeholder requirements conflict, the BA's role is not to arbitrate the conflict alone but to surface it clearly, document both positions, and escalate to an appropriate decision-maker. Options for resolving conflicts include: priority-based resolution (higher-priority stakeholder's need prevails), scope negotiation (both needs are met but in different ways or different phases), and compromise (both stakeholders accept a solution that partially meets each need).

---

## Key Terms for the IIBA ECBA Exam

| Term | Definition |
|---|---|
| Elicitation | Process of drawing out and discovering stakeholder needs and requirements |
| Tacit knowledge | Knowledge embedded in practice rather than explicit documentation |
| Structured interview | Interview with a fixed set of questions in a defined sequence |
| Semi-structured interview | Interview with core prepared questions plus adaptive follow-up |
| JAD | Joint Application Development — structured workshop for collaborative requirements elicitation |
| Passive observation | Watching work without participating or asking questions during the session |
| Document analysis | Reviewing existing artifacts to extract requirements and constraints |
| Survey | Questionnaire used to collect requirements input from large stakeholder populations |
| Prototype | Preliminary system representation used to elicit and validate requirements |
| Throwaway prototype | Low-fidelity mockup built for feedback, not intended as the final system |
| Business requirements | Why the organization needs the change — goals and objectives |
| Functional requirements | What the system must do |
| Non-functional requirements | How the system must perform — quality attributes |
| Traceable requirements | Requirements linked to the business need that motivated them |

---

## Study Questions

1. What is tacit knowledge, and which elicitation technique is most effective at surfacing it?

2. What distinguishes a structured interview from a semi-structured interview?

3. In what situation is a requirements workshop preferred over individual interviews?

4. What is the difference between passive and active observation?

5. A project involves collecting requirements from 400 frontline employees across 12 locations. Which elicitation technique is most appropriate for the initial data collection, and why?

6. What are the five quality characteristics of well-formed requirements in BABOK Guide v3?

7. What is the difference between a throwaway prototype and an evolutionary prototype?

8. A stakeholder has high influence but low interest in the project. What is the appropriate stakeholder management strategy?

---

## 9. Supplemental Resources

The following open educational resources extend module content on elicitation techniques, requirements documentation, and stakeholder management. All are freely accessible without login or purchase.

1. **BABOK Guide v3 — Elicitation and Collaboration (KA 4) and Requirements Life Cycle Management (KA 6)**
   <https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/>
   Focus: Official IIBA reference for all tasks in KA 4 and KA 6. KA 4 covers the five elicitation tasks tested in this module; KA 6 covers requirements maintenance and change control.

2. **Tacit Knowledge in Requirements Engineering — IEEE Software (open abstract)**
   <https://ieeexplore.ieee.org/document/6816468>
   Focus: Academic paper examining why tacit knowledge is the most common source of missing requirements and how observation and cognitive interview techniques surface it. Supports the observation and interview sections of this guide.

3. **Requirements Elicitation Techniques Comparison — Bridging the Gap**
   <https://www.bridging-the-gap.com/elicitation-techniques/>
   Focus: Practitioner-level comparison of elicitation technique strengths, weaknesses, and appropriate use contexts. Reinforces the technique selection framework discussed in the Elicitation Techniques section of this guide.

4. **Stakeholder Analysis Power-Interest Grid — MindTools**
   <https://www.mindtools.com/pages/article/newPPM_07.htm>
   Focus: Illustrated explanation of the Power-Interest Grid with engagement strategy examples for each quadrant. Directly supports the Stakeholder Analysis section and the Study Question 8 in this guide.

5. **Focus Group Research Methodology — Research Methods Knowledge Base**
   <https://conjointly.com/kb/focus-groups/>
   Focus: Academic-quality explanation of focus group strengths, limitations (dominance effects, groupthink), and best practices. Reinforces the focus group technique content and the limitation discussed in Question 12 of the quiz.
