# Reading Guide: Module 10 – Requirements Engineering and Use Cases

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

**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

Requirements engineering is the process of discovering, analyzing, documenting, and managing what a software system must do and how well it must do it. This module examines the full requirements engineering discipline — from classical techniques (use cases, functional/non-functional specification) to the Scrum approach (Product Backlog as living requirements repository). Understanding both prepares you for PSM I exam questions about how Scrum handles requirements differently from traditional methods, and for professional environments where both approaches coexist.

---

## 1. Requirements Engineering Core Concepts

### What Requirements Engineering Does

Requirements engineering encompasses five activities that apply whether a team is using Waterfall or Agile:

| Activity | Description | Waterfall Application | Scrum Application |
|---|---|---|---|
| Elicitation | Discovering stakeholder needs | Workshops, interviews, observation before design | Ongoing — Sprint Reviews, refinement, user research |
| Analysis | Examining for conflicts, ambiguity, feasibility | Before specification document is written | Part of Product Backlog refinement |
| Specification | Documenting requirements in usable form | Formal SRS document | Product Backlog Items (user stories, use cases) |
| Validation | Confirming requirements match actual needs | Stakeholder sign-off on specification | Sprint Review feedback loop |
| Management | Tracking changes to requirements over time | Change control board | Product Owner maintains and reorders Product Backlog |

### Functional vs. Non-Functional Requirements

| Type | Definition | Examples | Scrum Home |
|---|---|---|---|
| Functional | What the system must do — specific behaviors triggered by inputs or conditions | User login, password reset, data export, report generation | Product Backlog Items (user stories) |
| Non-Functional (NFR) | How well the system must operate — quality attributes | Page load time < 2 seconds; 99.9% uptime; AES-256 encryption; WCAG 2.1 accessibility | Definition of Done (system-wide) or Product Backlog Items (significant development work) |

The key diagnostic question: can I describe the requirement as "the system shall do X when Y" (functional) or "the system shall operate with quality attribute Z" (non-functional)?

---

## 2. Use Cases

### Use Case Structure

A use case describes how a specific actor (human user or external system) interacts with the system to achieve a specific goal. Use cases are more formal than user stories and are common in regulated industries and enterprise environments.

| Component | Description | Example |
|---|---|---|
| Use case name | Brief goal statement | "Reset Password" |
| Actor | Who initiates the interaction | Registered User |
| Preconditions | What must be true before the use case begins | User has a registered account; user is on login page |
| Main success scenario | Numbered steps when everything goes right | 1. User clicks Forgot Password 2. System shows email form... |
| Alternative flows | Valid deviations from the main path | If email not recognized, show generic message |
| Exception flows | Error conditions the system must handle | If reset link expired, prompt user to request a new one |
| Postconditions | What is true after success | User password updated; user redirected to login |

### Use Case vs. User Story

| Dimension | Use Case | User Story |
|---|---|---|
| Format | Structured table with numbered steps | One sentence: As a / I can / so that |
| Detail level | High — all paths documented | Low — conversation starter |
| Primary purpose | Specification and testing | Dialogue and shared understanding |
| Acceptance criteria | Embedded in alternative/exception flows | Written separately (Given/When/Then) |
| Best fit | Regulated industries, detailed upfront spec needed | Agile teams, iterative discovery |
| Scrum compatibility | Both are valid PBI formats | Preferred Scrum format |

Both formats document the same underlying system behavior. Neither is prohibited in Scrum. Teams often use user stories for everyday features and use cases for complex, regulated, or safety-critical behaviors.

---

## 3. Requirements in Scrum

### The Product Backlog as Requirements Repository

The Scrum Guide does not use the phrase "requirements document." The Product Backlog is the Scrum team's complete, living, ordered list of what needs to be done on the product. It replaces the traditional requirements specification by distributing requirements discovery across the project rather than front-loading it.

Product Backlog characteristics that mirror good requirements practices:

- Emergent: new requirements are discovered and added as the team learns
- Ordered: the most valuable and best-understood items are at the top
- Transparent: visible to all stakeholders at all times
- Refined: items are analyzed and detailed before they enter a Sprint (equivalent to requirements analysis)

### Non-Functional Requirements in Scrum

| NFR Type | Where It Lives in Scrum | Rationale |
|---|---|---|
| System-wide quality standard (e.g., all pages < 2 seconds) | Definition of Done | Applies to every Increment — must be verified on every item |
| Specific infrastructure work (e.g., add TLS to legacy API) | Product Backlog Item | Requires dedicated development effort; should be planned and estimated |
| Regulatory compliance (e.g., HIPAA audit logging) | Definition of Done + possibly Product Backlog Items | Compliance applies to everything; remediation is specific work |

### Requirements Traceability in Scrum

Traditional requirements traceability links each requirement to its source and forward to its implementation and tests. Agile teams achieve traceability through:

- Acceptance criteria: each user story's Given/When/Then criteria are directly testable
- Definition of Done: quality standards verified on every story
- Backlog management tools: linking stories to test cases and sprint outcomes
- Sprint Reviews: stakeholders validate that implemented items match their needs

Formal traceability matrices are not prescribed in Scrum but are not prohibited. Teams in regulated industries (healthcare, finance, aerospace) often maintain them as required artifacts alongside their Scrum workflow.

---

## 4. Traditional vs. Agile Requirements: Key Differences

| Dimension | Traditional (Waterfall) | Scrum |
|---|---|---|
| When requirements are captured | Before development begins | Progressively throughout the project |
| Format | Formal specification document | Product Backlog Items (user stories, use cases) |
| Completeness assumption | Requirements can be fully known upfront | Requirements emerge; full specification upfront is waste |
| Change management | Change control board; changes are expensive | Product Backlog is always open; changes welcome |
| Stakeholder involvement | Heavy at the beginning, light during development | Continuous — Sprint Reviews, refinement sessions |
| Validation | Document sign-off before build | Working software demonstrated at Sprint Review |
| Non-functional requirements | Separate NFR section in specification | Definition of Done + select backlog items |

---

## 5. PSM I Exam Tips

Tip 1: The Product Backlog is Scrum's requirements document. Any question that asks where requirements "live" in Scrum points to the Product Backlog (and its commitment, the Product Goal, for strategic direction).

Tip 2: Non-functional requirements that apply system-wide belong in the Definition of Done. This is one of the most tested NFR concepts on PSM I — "where should performance standards be captured?" → Definition of Done.

Tip 3: The Product Backlog is never frozen. A common exam scenario presents a stakeholder who wants to sign off on a complete requirements list before Sprint 1. The correct Scrum response: the Product Backlog supports progressive elaboration and is always open to change.

Tip 4: The Scrum Guide does not specify the format of Product Backlog Items. User stories are common practice, not a Scrum rule. Use cases, job stories, or plain descriptions are all valid PBI formats.

Tip 5: Agile Manifesto Principle 2 — "Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage." This principle directly contrasts with Waterfall requirements freezing.

Tip 6: Scrum does not define a requirements analyst role. The Product Owner is responsible for the Product Backlog, including eliciting and ordering requirements. Developers and stakeholders contribute knowledge during refinement.

Tip 7: Use cases and user stories document the same underlying behavior differently. Neither format is prohibited in Scrum. Teams choose the format that best serves their context.

Tip 8: Acceptance criteria (whether in Given/When/Then or use case format) serve as the bridge between requirements and testing — they make requirements testable and provide the basis for the Definition of Done verification.

---

## 7. Supplemental Resources

The following free, open-access resources go deeper on Module 10 topics:

**1. "Writing Good Use Cases" — Alistair Cockburn**
<http://alistair.cockburn.us/Writing+effective+use+cases>
Alistair Cockburn (an Agile Manifesto signatory) is the leading authority on use case writing. His free online resources cover use case structure, goal levels, and the relationship between use cases and user stories. The site contains multiple free articles and chapters.

**2. "Non-Functional Requirements" — IEEE Software Engineering Body of Knowledge (SWEBOK)**
<https://www.computer.org/education/bodies-of-knowledge/software-engineering>
The IEEE SWEBOK provides an authoritative, free reference for software engineering fundamentals including requirements classification. The Requirements chapter covers functional vs. non-functional requirements, quality attributes, and elicitation techniques. The full guide is available as a free PDF download.

**3. "Agile Requirements" — Agile Alliance**
<https://www.agilealliance.org/agile101/agile-glossary/requirements/>
The Agile Alliance's resources on requirements in Agile contexts. Covers how Agile teams handle requirements discovery, validation, and change management differently from traditional methods. Includes references to user stories, acceptance criteria, and backlog management practices.

---

## 6. Study Checklist

- [ ] Define requirements engineering and state its five core activities
- [ ] Distinguish functional from non-functional requirements and give two examples of each
- [ ] Write a complete use case with all required components for a common system behavior
- [ ] Explain how the Product Backlog replaces a traditional requirements specification in Scrum
- [ ] Describe two ways non-functional requirements are handled in Scrum
- [ ] Explain what requirements traceability is and how Agile teams achieve it without a formal matrix
- [ ] Complete this module's Lab and Quiz

---
