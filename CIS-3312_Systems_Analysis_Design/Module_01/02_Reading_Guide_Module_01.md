# Reading Guide: Module 01 - Introduction to Systems Analysis and the SDLC

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


**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Welcome to Module 01. This module establishes the vocabulary and conceptual framework for the entire course. You will learn what a system is, why organizations invest in systems analysis, and how the Software Development Life Cycle (SDLC) structures the process of building or improving information systems. Every topic in this module maps directly to BABOK Guide v3 Chapter 1 and Chapter 2, which are tested on the IIBA ECBA certification exam.

Before diving into specific elicitation or modeling techniques in later modules, you need a firm understanding of where those techniques fit in the overall process. This module is your foundation.

---

## 1. Core Vocabulary

### 1.1 System

A system is a set of interrelated components that work together to achieve a defined purpose. Every information system has five elements:

- Inputs — data or resources entering the system
- Processing — transformation of inputs into outputs
- Outputs — results, reports, or actions produced
- Boundary — the line separating the system from its environment
- Feedback — output information that flows back to control future inputs

Understanding system boundaries is critical for scoping requirements. Anything outside the boundary is an external entity — a source or destination of data — not something the system itself manages.

### 1.2 Systems Analysis

Systems analysis is the process of studying a business problem domain to identify improvement opportunities and define the requirements a new or modified system must satisfy. It bridges the gap between business stakeholders (who understand the problem) and technical teams (who build the solution). The output of systems analysis is a clear, complete, and agreed-upon set of requirements — not code, not a design, and not a technology recommendation.

### 1.3 Business Analyst

According to BABOK Guide v3, a business analyst (BA) is the professional who "identifies business needs, recommends solutions that deliver value, and facilitates stakeholder communication throughout the change." The BA serves as the central communication hub between stakeholders with different vocabularies, goals, and constraints.

### 1.4 Stakeholder

A stakeholder is any individual, group, or organization that has an interest in, or is affected by, the outcome of a project or system change. Stakeholders include:

- End users — people who operate the system daily
- Sponsors — executives who fund and authorize the project
- Subject matter experts (SMEs) — people with specialized domain knowledge
- Regulators — government or industry bodies with compliance authority
- The development team — architects, developers, testers

Missing a stakeholder early almost always produces a missing requirement discovered late — which is far more expensive to fix.

### 1.5 Feasibility Study

A feasibility study is a preliminary assessment conducted early in the SDLC to determine whether a proposed system is worth pursuing. The four dimensions of feasibility are:

- Technical feasibility — can the organization build it with available or acquirable technology and skills?
- Economic feasibility — do the projected benefits justify the costs?
- Operational feasibility — will users adopt it and does it fit current workflows?
- Legal feasibility — are there regulatory or compliance constraints?

The output of the feasibility study is a recommendation to proceed, modify, or cancel the project.

### 1.6 Requirements

Requirements are documented statements of what a system must do (functional requirements) or how well it must perform (non-functional requirements). They represent the agreed-upon understanding between stakeholders and the development team and serve as the baseline for design, testing, and acceptance.

---

## 2. SDLC Phase Comparison Table

| Phase | Primary Question | Key Deliverables | BA Activity Level |
|---|---|---|---|
| Planning | Should we do this? | Project Charter, Feasibility Study | Moderate |
| Systems Analysis | What must the system do? | Requirements Spec, Use Cases, Process Models | High |
| Systems Design | How will the system do it? | Logical and Physical Design Documents, ERDs | Moderate |
| Implementation | Build and deploy | Working system, test results, training materials | Moderate |
| Maintenance | What needs to change? | Change requests, updated requirements | Ongoing |

The SDLC is not always strictly sequential. Iterative and Agile methodologies cycle through analysis, design, and implementation repeatedly in short sprints. However, regardless of methodology, the analysis activities always precede the design activities for any given feature.

---

## 3. BABOK Knowledge Area Overview

BABOK Guide v3 organizes all business analysis work into seven Knowledge Areas. These are not phases — they are groupings of related tasks that a BA may perform at any point in a project.

| Knowledge Area | Number | Core Focus |
|---|---|---|
| Business Analysis Planning and Monitoring | KA 2 | Plan how BA work will be conducted |
| Elicitation and Collaboration | KA 4 | Gather information from stakeholders |
| Requirements Life Cycle Management | KA 6 | Trace, maintain, and approve requirements |
| Strategy Analysis | KA 3 | Understand current state, define future state |
| Requirements Analysis and Design Definition | KA 5 | Specify, model, and validate requirements |
| Solution Evaluation | KA 7 | Assess whether deployed solutions deliver value |

Note: KA 1 in BABOK is the Introduction chapter. The numbered KAs for exam purposes are KA 2 through KA 7, plus a Perspectives chapter covering Agile, BI, IT, Business Architecture, and Business Process Management.

---

## 4. The Business Analysis Core Concept Model (BACCM)

The BACCM is BABOK's foundational framework. It defines six interrelated concepts that describe the context of all BA work:

- Change — the act of transformation in response to a need
- Need — a problem or opportunity to be addressed
- Solution — a specific way to satisfy a need
- Stakeholder — a group or individual with a relationship to the change
- Value — the worth, importance, or usefulness of a solution to stakeholders
- Context — the circumstances, environment, and constraints within which the change occurs

Every BA task in BABOK can be described using these six concepts. When an exam question describes a scenario and asks what the BA is doing, map the activity back to one or more of these six concepts.

---

## 5. DFD and ERD Notation Preview

These modeling tools are covered in depth in Module 06. However, you should begin recognizing the symbols now.

### Data Flow Diagram (DFD) Symbol Reference

| Symbol | Shape | Represents |
|---|---|---|
| External Entity | Rectangle | Source or destination outside the system boundary |
| Process | Circle or rounded rectangle | A transformation of data within the system |
| Data Store | Open-ended rectangle (parallel lines) | A repository where data is held |
| Data Flow | Labeled arrow | Data moving between elements |

### Entity-Relationship Diagram (ERD) Symbol Reference

| Symbol | Shape | Represents |
|---|---|---|
| Entity | Rectangle | A person, place, thing, or concept about which data is stored |
| Attribute | Oval | A property or characteristic of an entity |
| Relationship | Diamond | An association between two entities |
| Primary Key | Underlined attribute | Uniquely identifies each entity instance |

---

## 6. Certification Exam Tips

1. The ECBA exam definition of business analysis is: "the practice of enabling change in an enterprise by defining needs and recommending solutions that deliver value to stakeholders." Memorize this verbatim — it appears in scenario questions that ask you to distinguish the BA role from PM and developer roles.

2. The SDLC phase sequence on the exam is always: Planning → Analysis → Design → Implementation → Maintenance. Any answer choice that puts Design before Analysis, or Implementation before Design, is wrong.

3. The BACCM's six concepts (Change, Need, Solution, Stakeholder, Value, Context) appear in BABOK Chapter 2 and are frequently tested. Know what each one means and how they relate to each other.

4. Feasibility has four dimensions: Technical, Economic, Operational, and Legal. A scenario describing a "skills gap" or "technology unavailability" is always technical feasibility. A scenario describing "user resistance" is always operational feasibility.

5. Requirements are not the same as solutions. A requirement states what the system must do. A solution states how it will do it. The BA documents requirements; architects and developers propose solutions.

6. Stakeholder identification errors are the most common root cause in exam scenarios involving late-discovered requirements, scope creep, or stakeholder dissatisfaction after go-live. When a scenario asks "what went wrong," look for the missed stakeholder.

7. The ECBA does not require work experience — it requires 21 hours of professional development education. This course counts. Review the official exam blueprint at iiba.org to understand how questions are distributed across the seven Knowledge Areas.

8. The distinction between "verification" and "validation" is tested in Module 04 but introduced here: verification checks that requirements are well-written (correct); validation checks that requirements address the real business need (right).

---

## 7. Required and Supplemental Reading

Required reading for this module:

- BABOK Guide v3, Chapter 1 (Introduction) and Chapter 2 (Business Analysis Key Concepts) — focus on the BACCM and the definition of business analysis
- The IIBA ECBA Exam Blueprint (free download at iiba.org) — review before you begin studying to understand question distribution

Supplemental reading:

- IEEE Std 610.12 definition of systems analysis — provides the industry-standard vocabulary used on certification exams
- Any introductory Systems Analysis and Design textbook chapter covering SDLC phases — Valacich and George, Satzinger, or Dennis/Wixom/Tegarden are all excellent

---

## 8. Study Checklist

- [ ] Write your own one-sentence definition of each of the six vocabulary terms in Section 1.
- [ ] Draw the SDLC phase diagram from memory and label the BA activity level for each phase.
- [ ] Identify the six BACCM concepts without looking at your notes.
- [ ] Read BABOK Guide v3 Chapter 1 and Chapter 2.
- [ ] Download and skim the IIBA ECBA Exam Blueprint at iiba.org.
- [ ] Watch the Module 01 video lecture.
- [ ] Complete the Module 01 lab activity before attempting the quiz.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 9. Supplemental Resources

The following open educational resources provide additional depth on module topics. All resources are freely accessible without login or purchase.

1. **IIBA BABOK Guide v3 Summary — Business Analysis Body of Knowledge Overview**
   <https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/>
   Focus: Official IIBA landing page for BABOK Guide v3; use to verify KA definitions and BACCM concepts directly from the source. Review the overview materials and download the exam blueprint.

2. **Systems Analysis and Design — Open Textbook (University of Minnesota Libraries)**
   <https://open.umn.edu/opentextbooks/textbooks/systems-analysis-and-design>
   Focus: Chapters 1–2 cover SDLC phases, the role of the systems analyst, and stakeholder identification. This is the primary ZTC textbook for the course.

3. **SDLC Phases Explained — GeeksForGeeks**
   <https://www.geeksforgeeks.org/software-development-life-cycle-sdlc/>
   Focus: Concise walkthrough of all five SDLC phases with diagrams. Use as a quick-reference companion while reading the OER textbook.

4. **Introduction to Business Analysis — OpenLearn (The Open University)**
   <https://www.open.edu/openlearn/money-business/business-strategy-studies/introduction-business-analysis/content-section-0>
   Focus: Free university-level course covering the BA role, stakeholder analysis, and requirements fundamentals. Excellent for students new to the BA profession.

5. **IEEE Glossary of Software Engineering Terminology (IEEE Std 610.12)**
   <https://ieeexplore.ieee.org/document/159342>
   Focus: Authoritative definitions for "system," "requirements," "verification," and "validation" as used in technical certification exams. Access via any university library proxy or the IEEE Xplore free abstract pages.
