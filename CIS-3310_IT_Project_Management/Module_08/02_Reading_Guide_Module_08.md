# Reading Guide: Module 08 – Communications Management

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

Communications Management addresses how project information is planned, created, distributed, stored, and monitored throughout the project lifecycle. The Project+ exam tests the communication channels formula, push/pull/interactive communication types, Communications Management Plan components, and formal vs. informal communication requirements. This reading guide provides the reference tables and exam tips you need.

---

## 1. High-Yield Glossary

### Communications Management Plan

A component of the Project Management Plan that documents who needs what information, when they need it, in what format, through what channel, and who is responsible for sending it. Also describes communication escalation paths and constraints.

### Communication Channels Formula

The formula used to calculate the total number of communication pathways in a project: n(n-1)/2, where n is the total number of communicating parties. Used to illustrate that adding stakeholders increases communication complexity exponentially.

### Interactive Communication

A two-way, real-time exchange between two or more parties. Both parties simultaneously send and receive information. Examples: meetings, phone calls, video conferences.

### Push Communication

Information sent from the sender to specific recipients without expectation of an immediate response. One-way distribution. Examples: status reports, emails, memos, newsletters.

### Pull Communication

Information made available in a central location for recipients to retrieve at their own discretion. Examples: intranet sites, shared document repositories, knowledge bases.

### Formal Communication

Written or structured communication required for contractual matters, scope changes, legal agreements, and official project records. Examples: change requests, contract modifications, status reports.

### Informal Communication

Unstructured communication used for day-to-day coordination, relationship building, and quick clarifications. Examples: hallway conversations, casual emails, instant messages.

### Noise

Any interference in the communication channel that degrades message quality or accuracy. Can be physical (poor audio on a call), semantic (jargon misunderstood by the receiver), or psychological (stress reducing comprehension).

### Manage Communications

The Executing process in which project information is created, collected, distributed, stored, retrieved, and disposed of in accordance with the Communications Management Plan.

### Monitor Communications

The Monitoring and Controlling process that assesses whether the communications approach is effective and takes corrective action when stakeholder communication needs are not being met.

---

## 2. Communications Management Process Reference

| Process | Process Group | Key Output | Purpose |
|---|---|---|---|
| Plan Communications Management | Planning | Communications Management Plan | Define who gets what, when, how |
| Manage Communications | Executing | Project communications, updated logs | Create and distribute information |
| Monitor Communications | Monitoring and Controlling | Change requests, updated plan | Verify communications are effective |

---

## 3. Communication Channels Formula

Formula: channels = n(n-1) / 2

Where n = total number of communicating parties (include the PM, all team members, sponsors, and relevant vendors).

| Stakeholder Count (n) | Channels |
|---|---|
| 2 | 1 |
| 3 | 3 |
| 5 | 10 |
| 8 | 28 |
| 10 | 45 |
| 12 | 66 |
| 15 | 105 |

Worked example — "adding stakeholders" question type:

A project starts with 6 stakeholders (15 channels). Four new stakeholders are added. New total is 10 stakeholders (45 channels). New channels added = 45 - 15 = 30.

---

## 4. Communication Methods Comparison

| Method | Direction | Timing | Best Used When | Examples |
|---|---|---|---|---|
| Interactive | Two-way | Real-time | Complex messages; immediate feedback needed | Meetings, video calls, phone calls |
| Push | One-way (outbound) | Asynchronous | Routine updates; stakeholder does not need to respond | Status reports, emails, memos |
| Pull | One-way (available) | On-demand | Large audiences; optional or reference content | Intranet, SharePoint, knowledge base |

---

## 5. Formal vs. Informal Communication Reference

| Communication Type | When Required | Examples |
|---|---|---|
| Formal Written | Scope changes, contract modifications, legal records, official decisions | Change requests, contracts, project charter |
| Formal Verbal | Presentations, structured briefings | Steering committee updates, kickoff meetings |
| Informal Written | Day-to-day coordination | Casual emails, instant messages, text messages |
| Informal Verbal | Quick questions, relationship building | Hallway conversations, water-cooler discussions |

Key rule: scope changes and contractual matters always require formal written communication.

---

## 6. Communications Management Plan Components

A complete Communications Management Plan addresses:

- Stakeholder communication requirements (who needs what)
- Information format and level of detail
- Frequency and timing of communications
- Responsible party for each communication
- Communication channel or medium
- Escalation procedures
- Glossary of terms and acronyms
- Communication constraints (availability, access, language, technology)

---

## 7. Communication Barriers

Common barriers that degrade communication effectiveness:

- Language differences and jargon
- Cultural differences in directness, hierarchy, and formality norms
- Physical distance and time zone mismatches
- Information overload — too many messages dilutes attention
- Filtering — senders edit information before passing it on
- Noise in the channel — technical problems, interruptions, poor connections
- Lack of feedback — receiver never confirms receipt or understanding

---

## 8. Certification Exam Tips

**Tip 1 — Channels formula: always divide by 2:**
Students frequently compute n(n-1) and stop. The formula is n(n-1)/2. Every Project+ exam that tests this formula requires the division step.

**Tip 2 — n includes everyone:**
When counting n for the channels formula, include the project manager, all team members, the sponsor, and any relevant vendors explicitly mentioned in the question. Students often miss the PM or a named external party.

**Tip 3 — Interactive is not always best:**
Interactive communication is most efficient for complex, sensitive, or ambiguous messages. For routine status distribution, Push is more appropriate. Choose the method that fits the scenario.

**Tip 4 — Pull for large audiences:**
When a question describes posting information to a shared site or repository for team members to access, that is Pull communication — not Push. The distinguishing factor is that the recipient retrieves it rather than receiving it.

**Tip 5 — Formal written for scope changes:**
Any scenario where a stakeholder verbally requests a scope change requires a formal written response. The PM should not agree verbally to a scope change or begin work before a formal change request is processed.

**Tip 6 — Communications Plan is not the Stakeholder Engagement Plan:**
The Communications Management Plan documents information delivery logistics. The Stakeholder Engagement Plan documents strategies for managing stakeholder involvement and engagement levels. They are separate documents, though both reference stakeholder information.

**Tip 7 — Monitor Communications is Monitoring and Controlling:**
Students sometimes place Monitor Communications in Closing. It belongs in Monitoring and Controlling because communication effectiveness must be assessed throughout the project, not just at the end.

**Tip 8 — Adding stakeholders increases channels dramatically:**
The exam frequently tests the impact of adding stakeholders to an existing project. Be prepared to calculate channels before and after, then subtract to find new channels added. The exponential growth is the conceptual point being tested.

---

## 9. Study Checklist

- [ ] State the communication channels formula and apply it to a 5-person and 10-person scenario
- [ ] Describe the difference between push, pull, and interactive communication with one example each
- [ ] Name the three Communications Management processes and their process groups
- [ ] List five components of the Communications Management Plan
- [ ] Identify three communication barriers and one mitigation for each
- [ ] Explain when formal written communication is required
- [ ] Distinguish the Communications Management Plan from the Stakeholder Engagement Plan
- [ ] Complete the Module 08 Lab activity
- [ ] Take the Module 08 Quiz
- [ ] Post Module 08 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 10: Communications Management**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 10](https://opentextbc.ca/projectmanagement/chapter/chapter-10-project-communications-management/)
   Covers the communications model, push/pull/interactive methods, the Communications Management Plan, and stakeholder communication strategies.

2. **PMI — Effective Communication in Project Management (Free Article)**
   *Project Management Institute* — [pmi.org/learning/library/effective-communication-better-project-management](https://www.pmi.org/learning/library/effective-communication-better-project-management-8865)
   PMI research article on communication effectiveness factors, barriers, and best practices — directly aligned to PK0-005 Domain 3.

3. **Stakeholder Engagement Assessment Matrix Guide — PM Study Circle**
   [pmstudycircle.com/stakeholder-engagement-assessment-matrix](https://pmstudycircle.com/stakeholder-engagement-assessment-matrix/)
   Clear explanation of the five engagement levels (Unaware through Leading), how to read the matrix, and how to develop targeted engagement strategies.

4. **YouTube — "Project Communications Management Overview" (Coursera / Google PM Certificate)**
   [youtube.com/watch?v=3sJ8b0b7IH8](https://www.youtube.com/watch?v=3sJ8b0b7IH8)
   Free lecture segment covering communication planning, stakeholder register, and communications plan components with worked examples.

5. **Communication Channels Formula Drill — PM Exam SmartNotes (Free)**
   [pmexamsmartnotes.com/communication-channels-formula](https://www.pmexamsmartnotes.com/communication-channels-formula/)
   Interactive formula practice for N(N-1)/2 with examples at various team sizes — essential preparation for calculation questions on the Module 08 quiz.
