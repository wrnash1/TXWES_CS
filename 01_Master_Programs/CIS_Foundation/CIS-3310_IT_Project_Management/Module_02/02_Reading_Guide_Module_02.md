# Reading Guide: Module 02 – Project Lifecycle and Process Groups

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3310 &BULL; IT PROJECT MANAGEMENT & AGILE METHODOLOGIES</text>
    
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


**Course:** CIS-3310 IT Project Management
**Certification Alignment:** CompTIA Project+ (PK0-005) | PMBOK 6th and 7th Editions
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 02 builds directly on Module 01 by showing how a project progresses from authorization to closure. The five PMI Process Groups are the backbone of the PMBOK framework and among the most frequently tested topics on the CompTIA Project+ exam. Pay close attention to which documents belong in which Process Group — this distinction drives a significant portion of exam questions.

---

## 1. High-Yield Glossary

### Project Lifecycle

The sequence of phases a specific project moves through from start to finish. Lifecycles are tailored to the project type, industry, and organization. A software project lifecycle might be: Requirements → Design → Development → Testing → Deployment. The lifecycle is project-specific; the Process Groups are universal.

### Process Group

A PMI-defined category of management activities applied to every project. The five Process Groups are Initiating, Planning, Executing, Monitoring and Controlling, and Closing. They are not sequential phases — they can overlap, and some (like Monitoring and Controlling) run continuously.

### Project Charter

The formal document that authorizes the project's existence, names the project manager, and grants the PM authority to apply organizational resources. Produced in the Initiating Process Group. Signed by the project sponsor, not the PM. The charter does not contain detailed schedules or WBS — those belong in Planning.

### Business Case

The document that justifies the investment in a project by analyzing the problem or opportunity, evaluating options, and recommending a course of action based on expected costs, benefits, and risks. Typically prepared before the project is formally authorized. The Business Case is the sponsor's tool for securing organizational funding.

### Project Objectives

Clear, measurable statements describing what the project must accomplish. Strong objectives follow SMART criteria: Specific, Measurable, Achievable, Relevant, and Time-bound. Objectives are documented in the Project Charter and serve as the primary measure of project success.

### Stakeholder Register

A project document that records all identified stakeholders with their roles, contact information, interests, influence levels, and initial engagement strategies. Created during Initiating, updated continuously. The Stakeholder Register is a living document — it should never be treated as final.

### Project Management Plan

The master planning document produced during the Planning Process Group. It integrates all subsidiary management plans (Scope, Schedule, Cost, Quality, Resource, Communications, Risk, Procurement, Stakeholder) into a single coherent guide for executing and controlling the project.

### Predictive Lifecycle

A lifecycle model in which all scope is defined upfront and the project proceeds through phases in sequence with minimal change. Also called Waterfall. Best suited for stable, well-understood requirements.

### Adaptive Lifecycle

A lifecycle model in which requirements and solutions evolve through iterative collaboration with customers. Work is done in short time-boxed cycles (sprints). Best suited for complex, fast-changing environments. Covered in depth in Module 12.

### Lessons Learned Register

A Closing Process Group output that captures knowledge gained during the project — what worked, what failed, and what should change on future projects. Stored as an Organizational Process Asset for future teams to consult.

---

## 2. The Five Process Groups — Inputs, Activities, and Key Outputs

| Process Group | Primary Purpose | Key Inputs | Key Outputs |
|---|---|---|---|
| Initiating | Authorize the project; identify stakeholders | Business Case, Agreements, EEFs, OPAs | Project Charter, Stakeholder Register |
| Planning | Develop the comprehensive project roadmap | Project Charter, EEFs, OPAs | Project Management Plan, Scope Baseline, Schedule Baseline, Cost Baseline, Risk Register |
| Executing | Perform the work defined in the plan | Project Management Plan, approved change requests | Deliverables, Work Performance Data, Change Requests |
| Monitoring and Controlling | Track performance; manage changes | Work Performance Data, Project Management Plan | Work Performance Reports, Change Requests, Updates to PM Plan |
| Closing | Formally end the project or phase | Project Management Plan, accepted deliverables | Final product/service/result transition, Lessons Learned Register |

---

## 3. Process Groups vs. Project Lifecycle Phases

| Attribute | Process Groups | Lifecycle Phases |
|---|---|---|
| Defined by | PMI (universal) | Project team (tailored) |
| How many | Always 5 | Varies by project type |
| Can repeat? | Yes — across phases | Generally sequential |
| Overlap? | Yes — M&C overlaps Executing | Generally sequential |
| Exam relevance | Heavily tested | Context for scenario questions |

---

## 4. Lifecycle Model Comparison

| Attribute | Predictive (Waterfall) | Iterative/Incremental | Adaptive (Agile) |
|---|---|---|---|
| Requirements | Defined upfront | Partially defined, refined per cycle | Emerge through collaboration |
| Change tolerance | Low (formal change control) | Moderate | High (welcomed) |
| Delivery | Single final delivery | Incremental deliveries | Continuous delivery each sprint |
| Best for | Stable, regulated, well-defined scope | Complex products with some unknowns | Rapidly changing, customer-driven scope |
| Example IT projects | Network migration, hardware rollout | ERP implementation in phases | Custom software, mobile apps |

---

## 5. Project Charter Components Reference

A complete Project Charter should contain the following elements:

- Project title and description
- Business need or problem being addressed (Business Case summary)
- Project objectives (SMART format)
- High-level scope (in-scope and out-of-scope items)
- High-level milestones and target dates
- Approved budget summary
- Key stakeholders and their roles
- Known risks and constraints
- Project manager name and authority level
- Sponsor signature and date

The charter does NOT include detailed WBS breakdowns, detailed risk registers, or full project schedules — those are Planning outputs.

---

## 6. Certification Exam Tips

**Tip 1 — Charter vs. Management Plan:**
The Project Charter is an Initiating output. The Project Management Plan is a Planning output. On scenario questions asking what to produce "first" or "during initiation," the answer is the charter or the Stakeholder Register — never the management plan.

**Tip 2 — M&C runs in parallel:**
Monitoring and Controlling does not happen after Executing. It runs throughout the project alongside Executing. Questions describing a PM "checking performance and adjusting the plan" during execution describe M&C activities — not a separate phase.

**Tip 3 — Closing is NOT optional:**
Even if deliverables are accepted and the work is done, the project is not complete until contracts are closed, documents are archived, and the team is formally released. Exam questions about skipping formal closure always test whether students know this.

**Tip 4 — Who signs the charter:**
The project sponsor signs the Project Charter. The PM does not sign it — the PM is named in it. This distinction appears on exam questions about charter authorization.

**Tip 5 — Multi-phase project Process Groups:**
In a multi-phase project, Process Groups repeat in each phase. Phase 1 has its own Initiating, Planning, Executing, M&C, and Closing. Phase 2 starts again with Initiating. Students who think Initiating only happens once will miss scenario questions about phased projects.

**Tip 6 — Business Case vs. Project Charter:**
The Business Case justifies whether to invest. The Project Charter formally authorizes the investment. The Business Case is an input to the charter — it comes first. Do not confuse them.

**Tip 7 — Stakeholder Register vs. Stakeholder Engagement Plan:**
The Stakeholder Register (Initiating) records who the stakeholders are. The Stakeholder Engagement Plan (Planning) defines how the PM will engage them. Both documents are frequently confused on exam questions.

**Tip 8 — Lessons learned timing:**
Lessons Learned should be captured throughout the project, not only at closure. However, the formal Lessons Learned Register is a Closing output. If a question asks "when are lessons learned documented?" the correct answer is "throughout the project but formalized during Closing."

---

## 7. Required Reading and Study Resources

Complete the following before the lab and quiz:

- Read the project initiation and lifecycle chapters in the course OER textbook (linked in Canvas).
- Review the CompTIA Project+ PK0-005 exam objectives at comptia.org, focusing on the Process Groups domain.
- For supplemental video study, visit professormesser.com for Project+ coverage of the project lifecycle.

---

## 8. Study Checklist

- [ ] Define each of the five Process Groups and state its primary purpose
- [ ] List the two key outputs of the Initiating Process Group
- [ ] List at least five outputs of the Planning Process Group
- [ ] Explain why Monitoring and Controlling runs in parallel with Executing
- [ ] Identify the three SMART components most commonly omitted from poorly written objectives
- [ ] Explain the difference between a project lifecycle phase and a Process Group using an original example
- [ ] Compare predictive and adaptive lifecycle models using at least two distinguishing attributes
- [ ] State who signs the Project Charter and what authority it grants
- [ ] Explain the difference between the Business Case and the Project Charter
- [ ] Complete the Module 02 Lab activity
- [ ] Take the Module 02 Quiz
- [ ] Post Module 02 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 3: The Project Management Process Groups**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 3](https://opentextbc.ca/projectmanagement/chapter/chapter-3-the-project-management-process-groups-a-case-study/)
   Walks through all five Process Groups using a case study format. Excellent preparation for scenario-based Project+ exam questions.

2. **PMI — Project Lifecycle and Phases**
   *Project Management Institute* — [pmi.org/learning/library/project-life-cycle](https://www.pmi.org/learning/library/project-life-cycle-phases-processes-8950)
   Official PMI article distinguishing lifecycle phases from Process Groups — the most commonly confused pair of concepts in Module 02.

3. **PMBOK 7th Edition Overview — PM PrepCast (Free Excerpt)**
   *OSP International* — [project-management-prepcast.com/pmbok-7](https://www.project-management-prepcast.com/free/pmbok-guide)
   Free chapter summary comparing PMBOK 6 (process-based) and PMBOK 7 (principle-based) perspectives — directly tested on PK0-005.

4. **YouTube — "Project Lifecycle vs Process Groups" (Mike Clayton / OnlinePMCourses)**
   [youtube.com/watch?v=fPNqT_5vVk4](https://www.youtube.com/watch?v=fPNqT_5vVk4)
   A clear visual explanation of how lifecycle phases and Process Groups interact. Highly recommended before the quiz.

5. **Stakeholder Analysis Tutorial — MindTools (Free)**
   [mindtools.com/stakeholder-analysis](https://www.mindtools.com/aol0rms/stakeholder-analysis)
   Step-by-step guide to building a Power/Interest Grid and planning stakeholder engagement strategies — directly supports the Module 02 lab.
