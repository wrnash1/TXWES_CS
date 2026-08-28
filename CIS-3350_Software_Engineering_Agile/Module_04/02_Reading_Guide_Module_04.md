# Reading Guide: Module 04 – Scrum in Practice: Sprint Planning and Daily Scrum

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

Module 04 moves from framework overview to event-level practice. Sprint Planning and the Daily Scrum are the two events that directly shape how a team works during a Sprint. Sprint Planning determines direction and commitment; the Daily Scrum maintains alignment and adaptation. Together they implement the empirical pillars of inspection and adaptation at the Sprint level. This guide provides deep coverage of both events, including the most common failure modes you will encounter in both practice and PSM I exam questions.

---

## 1. Sprint Planning — Full Coverage

### Sprint Planning Purpose

Sprint Planning initiates the Sprint by creating the Sprint Goal and Sprint Backlog through collaborative conversation among the entire Scrum Team. It is the first and foundational event of each Sprint.

### Participants

The entire Scrum Team attends Sprint Planning:

- Product Owner: presents the ordered Product Backlog, explains business context, proposes the Sprint's value proposition, and collaborates on the Sprint Goal
- Scrum Master: facilitates the event, ensures it stays within the timebox, and coaches the team on Sprint Planning practices
- Developers: ask clarifying questions, select work, decompose it into tasks, and commit to the Sprint Goal

The Scrum Guide notes that the Scrum Team may invite other people to attend Sprint Planning to provide advice, but they do not make commitments for the team.

### Timebox Reference

| Sprint Length | Sprint Planning Timebox |
|---|---|
| 1 week | 2 hours |
| 2 weeks | 4 hours |
| 3 weeks | 6 hours |
| 4 weeks (1 month) | 8 hours |

### Three Topics of Sprint Planning

Topic 1 — Why is this Sprint valuable?

The Product Owner proposes how the product could increase its value and utility in the current Sprint. The Scrum Team collaborates to define the Sprint Goal. The Sprint Goal must be finalized by the end of Sprint Planning.

Topic 2 — What can be Done this Sprint?

The Developers select items from the Product Backlog to include in the Sprint. Selection is informed by:

- The Sprint Goal
- Team capacity (accounting for vacations, meetings, and known commitments)
- Past Sprint velocity (a leading indicator, not a hard rule)
- The team's understanding of the work

The Developers have the final word on what they can accomplish. No one — not the Product Owner, not a manager — can force the Developers to commit to more than they believe they can deliver.

Topic 3 — How will the chosen work get done?

The Developers decompose selected Product Backlog items into tasks of one day or less. This detailed planning belongs entirely to the Developers. The Product Owner participates to clarify requirements but does not plan the technical work.

---

## 2. The Sprint Goal — Deep Reference

The Sprint Goal is the single objective for the Sprint. It is the commitment associated with the Sprint Backlog. Key properties:

- Created collaboratively during Sprint Planning
- Owned by the entire Scrum Team (not just the Product Owner)
- Fixed during the Sprint — it does not change unless a Sprint cancellation occurs
- Provides flexibility — Developers can negotiate Sprint Backlog scope with the Product Owner while protecting the Sprint Goal
- Evaluated at the Sprint Review — the team assesses whether the Sprint Goal was achieved

### Sprint Goal vs. Sprint Backlog Scope

A critical distinction tested on PSM I: the Sprint Goal is fixed, but the Sprint Backlog scope is flexible. If Developers discover a selected item is technically different than expected, they can negotiate a scope adjustment with the Product Owner — swapping one item for another — as long as the Sprint Goal remains achievable. The Sprint Goal anchors the Sprint's purpose; the Sprint Backlog is the current best plan for achieving it.

### What Makes a Good Sprint Goal

A good Sprint Goal:

- States a user-facing outcome, not a task list
- Is achievable within the Sprint's timebox
- Allows the Developers some flexibility about implementation
- Is testable — at the Sprint Review you can answer yes or no to "Did we achieve the Sprint Goal?"

Poor Sprint Goal example: "Complete stories 12, 14, and 17." (This is a task list, not a goal.)

Better Sprint Goal example: "Enable customers to browse and filter the product catalog by category and price so that the holiday marketing campaign can launch."

---

## 3. Daily Scrum — Full Coverage

### Daily Scrum Purpose

The Daily Scrum inspects progress toward the Sprint Goal and adapts the Sprint Backlog as necessary. It creates a shared picture of where the Sprint stands every day and allows the team to course-correct while there is still time.

### Key Attributes

| Attribute | Value |
|---|---|
| Timebox | 15 minutes |
| Frequency | Every working day of the Sprint |
| When | Same time each day |
| Where | Same location each day |
| Participants | Developers (mandatory); Scrum Master and Product Owner may attend |

### Format

The 2020 Scrum Guide removed the mandatory three-question format. The Developers choose their own structure as long as it creates focus on the Sprint Goal. Common formats include:

Format A — Three Questions (still widely used): What did I do yesterday toward the Sprint Goal? What will I do today toward the Sprint Goal? Do I see any impediments preventing me or the team from meeting the Sprint Goal?

Format B — Backlog Walkthrough: Team reviews the Sprint Backlog from the "Done" column backward, identifying what is complete, what is in progress, and what is at risk.

Format C — Sprint Goal Focus: Team addresses: Are we still on track to achieve the Sprint Goal? What changed since yesterday? What needs to change today?

### What the Daily Scrum Is Not

The Daily Scrum is not a status meeting for management. Developers do not report to the Scrum Master or to managers. They synchronize with each other.

The Daily Scrum is not a problem-solving session. Deep technical discussions happen after the Daily Scrum ends, with only the people who need to participate. The full 15 minutes should not be consumed by one person's technical problem.

The Daily Scrum is not optional. It occurs every working day. Skipping it creates information gaps that compound over the Sprint.

### Scrum Master and Product Owner Roles at the Daily Scrum

The Scrum Master ensures the Daily Scrum happens and helps the team understand its purpose. The Scrum Master does not run the Daily Scrum; the Developers run it.

The Product Owner may attend the Daily Scrum as an observer or as a participant if they are also a Developer. They do not use the Daily Scrum to add requirements or steer the team's daily choices.

---

## 4. Sprint Backlog as a Living Document

The Sprint Backlog is created during Sprint Planning and updated continuously throughout the Sprint. Key points:

- The Sprint Backlog belongs to the Developers — it is their plan
- It is updated at least daily (typically at or after the Daily Scrum)
- New tasks are added as the team discovers them; completed tasks are moved to Done
- Scope may be renegotiated with the Product Owner when work turns out to be significantly different than planned, as long as the Sprint Goal is protected
- No one outside the Developers can add items to the Sprint Backlog during the Sprint

---

## 5. Common Failure Modes

### Sprint Planning Failure Modes

Failure Mode 1: Sprint Planning is just a task assignment meeting. The Scrum Master or manager assigns work items to individual Developers. This violates the self-managing principle and typically produces poor estimates and low team ownership.

Failure Mode 2: No Sprint Goal is created. The team treats Sprint Planning as a backlog grooming session and commits to a list of items without articulating a meaningful objective. Without a Sprint Goal, there is no coherent direction for the Sprint and no meaningful metric for Sprint success.

Failure Mode 3: Overcommitment under pressure. A manager or Product Owner pressures the Developers to commit to more than they believe they can achieve. This leads to partially done work at Sprint end, Definition of Done shortcuts, and eroded trust.

Failure Mode 4: Sprint Planning goes over timebox. If Sprint Planning regularly exceeds its timebox, the team likely lacks enough refined Product Backlog items (this is a backlog refinement problem) or is trying to solve technical problems that should be deferred to the Sprint itself.

### Daily Scrum Failure Modes

Failure Mode 1: Status meeting for management. Developers report upward to a manager or Scrum Master rather than synchronizing with each other.

Failure Mode 2: Runs long. A 15-minute event that consistently runs 30–45 minutes is failing at its primary purpose. The fix is to enforce the timebox and move detailed discussions to post-standup breakouts.

Failure Mode 3: Dominated by one person. If one Developer consistently uses most of the 15 minutes, others disengage and the team loses the inspection benefit.

Failure Mode 4: Reporting to the Sprint Backlog, not the Sprint Goal. Teams that focus on task completion ("I finished task 7 and will start task 8") rather than Sprint Goal progress can lose sight of whether the Sprint is actually on track.

---

## 6. PSM I Exam Tips

Tip 1: The Sprint Goal is the most important output of Sprint Planning. Know that it is created collaboratively, belongs to the entire Scrum Team, and is fixed during the Sprint.

Tip 2: Developers, not the Product Owner, select how much work to take into a Sprint. The Product Owner orders the backlog; the Developers decide what they can accomplish.

Tip 3: The Daily Scrum is for Developers. It is not facilitated by the Scrum Master. The Scrum Master ensures it happens but does not run it.

Tip 4: The three-question format for the Daily Scrum is not required by the 2020 Scrum Guide. It is a common practice but not a rule.

Tip 5: The Sprint Backlog can be renegotiated (scope adjusted) during the Sprint — but the Sprint Goal cannot be changed during the Sprint.

Tip 6: Sprint Planning produces the Sprint Goal AND the Sprint Backlog. If a question asks for the output of Sprint Planning and only lists one, look for an answer that includes both.

Tip 7: No one outside the Developers can force scope into the Sprint Backlog during a Sprint. Work that arrives mid-Sprint goes to the Product Backlog for future Sprint consideration.

Tip 8: PSM I questions about "what the Scrum Master should do" at the Daily Scrum almost always involve coaching, facilitating, or removing impediments — not running the meeting or reporting results.

---

## 8. Supplemental Resources

The following free, open-access resources go deeper on Module 04 topics:

**1. "Sprint Planning" — Scrum.org Resources**
<https://www.scrum.org/resources/what-is-sprint-planning>
A concise, authoritative overview of Sprint Planning directly from Scrum.org. Covers the three topics, attendees, and outputs. Useful as a quick-reference companion to the Scrum Guide section on Sprint Planning.

**2. "The Daily Scrum" — Scrum.org Resources**
<https://www.scrum.org/resources/what-is-a-daily-scrum>
Scrum.org's official resource page for the Daily Scrum event. Addresses the 2020 format changes, common misconceptions, and the distinction between the Daily Scrum and a status meeting. Includes a short video overview.

**3. "Sprint Goals: Why, What, How" — Roman Pichler**
<https://www.romanpichler.com/blog/sprint-goals/>
A practitioner-focused blog post by a leading Scrum trainer on how to write effective Sprint Goals. Pichler covers the characteristics of a good Sprint Goal, common mistakes, and worked examples. Free access on romanpichler.com.

---

## 7. Study Checklist

- [ ] State the three topics of Sprint Planning and what each produces
- [ ] Explain what makes a Sprint Goal good versus poor — write one example of each
- [ ] State the timebox for the Daily Scrum and who the required participants are
- [ ] Explain three formats a team can use for the Daily Scrum
- [ ] Describe four failure modes in Sprint Planning and how to correct each
- [ ] Describe four failure modes in the Daily Scrum and how to correct each
- [ ] Explain the distinction between the Sprint Goal (fixed) and the Sprint Backlog scope (flexible)
- [ ] State who owns the Sprint Backlog and who can modify it during the Sprint
- [ ] Complete this module's Lab and Quiz

---
