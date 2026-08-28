# Reading Guide: Module 09 – Kanban and Lean Principles

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

Kanban and Lean are foundational frameworks in the Agile ecosystem. Lean thinking — originating from the Toyota Production System — provides the philosophical basis for waste elimination, flow optimization, and pull-based systems. Kanban operationalizes these ideas for knowledge work through visualization, WIP limits, and flow management. Understanding both prepares you for PSM I exam questions about how Scrum compares to other approaches and for professional contexts where Kanban is used alongside or instead of Scrum.

---

## 1. The Toyota Production System and Lean Origins

Lean manufacturing was developed at Toyota in the 1950s and 1960s by Taiichi Ohno, Eiji Toyoda, and Shigeo Shingo as the Toyota Production System (TPS). Its core insight was that manufacturing quality and efficiency improve when waste is systematically eliminated and work is pulled through the system based on actual demand rather than pushed by a production schedule.

Lean was translated into software development terms by Mary and Tom Poppendieck in their 2003 book Lean Software Development. They mapped Toyota's manufacturing concepts to software work, arguing that the same principles of flow, pull, and waste elimination apply to building software as to building cars.

---

## 2. Lean's Five Principles

### Principle 1 — Identify Value

Value is defined from the customer's perspective: what are they willing to pay for? In software, a working feature that solves a real user problem is value. A feature that was built but nobody uses is waste. The first step in Lean thinking is to be ruthlessly clear about what constitutes genuine value in your context.

### Principle 2 — Map the Value Stream

A value stream is the complete sequence of activities required to deliver value to the customer — from initial idea to working software in production. Value stream mapping visualizes every step, classifying each as value-adding or non-value-adding. Non-value-adding steps (handoffs, approvals, waiting) are targets for elimination or reduction.

### Principle 3 — Create Flow

Once waste is identified, the goal is to make value-creating activities flow smoothly and continuously. Flow is disrupted by batch processing (accumulating many items before moving them forward), handoffs between teams, and multitasking. Creating flow means organizing work so items move from start to finish without unnecessary stopping.

### Principle 4 — Establish Pull

In a pull system, work is pulled into the next stage only when there is capacity to handle it. This contrasts with push systems where work is assigned according to a schedule regardless of whether the recipient is ready. Pull prevents overloading, reduces queue sizes, and enables faster delivery.

### Principle 5 — Seek Perfection

Lean improvement is continuous and never finished. Each improvement cycle reveals new opportunities for waste elimination and flow improvement. The pursuit of perfection is an ongoing commitment, not a destination.

---

## 3. The Seven Wastes of Lean Software Development

The Poppendiecks identified seven categories of waste in software development, adapted from Toyota's seven manufacturing wastes:

| Lean Waste | Software Manifestation |
|---|---|
| Partially done work | Code written but not integrated, tested, or deployed |
| Extra features | Building functionality users did not request (YAGNI violations) |
| Relearning | Solving the same problem multiple times due to poor knowledge transfer |
| Handoffs | Passing work between teams (e.g., dev → QA → ops) with coordination overhead |
| Delays | Waiting for approvals, reviews, environment access, or dependencies |
| Task switching | Working on multiple items simultaneously; context switching reduces all |
| Defects | Bugs requiring rework; also specification errors discovered late |

The connection to Agile: Agile Manifesto Principle 10 — "Simplicity — the art of maximizing the amount of work not done — is essential" — is a direct expression of Lean waste elimination. Short Sprints reduce partially done work. Continuous delivery reduces handoffs. Automated testing reduces defect waste.

---

## 4. Kanban: Definition and Core Practices

Kanban is a method for managing knowledge work that originated in Toyota's manufacturing floor. David Anderson adapted it for software at Microsoft in the early 2000s and formalized it in his 2010 book Kanban: Successful Evolutionary Change for Your Technology Business.

Kanban does not prescribe roles, events, or planning cadences. It is a method for improving an existing process incrementally, not a replacement for the process.

### Core Practice 1 — Visualize the Workflow

Create a board that represents the team's process as columns. Each work item is a card that moves left to right through the columns. Common column configurations:

- Simple: To Do | In Progress | Done
- Detailed: Backlog | Analysis | Development | Testing | Deployment | Done
- With sub-states: Development: In Progress | Waiting for Review | In Review

Visualization makes invisible problems visible. A card that has been in "In Testing" for five days is immediately apparent on a Kanban board; it would be invisible in a spreadsheet.

### Core Practice 2 — Limit Work in Progress (WIP)

WIP limits are maximum counts assigned to each column (or to the team overall) that restrict how many items can be in that stage simultaneously. WIP limits are the defining practice of Kanban.

Why WIP limits work: Little's Law, a mathematical principle from queueing theory, states:

Average Cycle Time = WIP / Throughput

Holding throughput constant, if you reduce WIP, cycle time decreases. Teams that maintain lower WIP move items through the system faster on average, even if they are working at the same rate.

WIP limits also force teams to resolve blockers before starting new work: "Stop starting, start finishing."

### Core Practice 3 — Manage Flow

Track how items move through the board and use flow metrics to identify improvement opportunities:

- Cycle time: How long from when work begins on an item to when it is done
- Lead time: How long from when a request is made to when work is done (includes wait time before work begins)
- Throughput: How many items are completed per unit of time (e.g., items per week)
- WIP: The current number of items in progress

Cumulative flow diagrams (CFDs) visualize all four metrics simultaneously, showing how items accumulate in various stages over time. Widening bands in a specific column indicate a bottleneck.

### Core Practice 4 — Make Policies Explicit

Document the rules that govern how work moves through the board:

- What does "ready for development" mean? (the equivalent of a Definition of Ready)
- When can a card move from Development to Testing? (similar to a Definition of Done for that stage)
- How are blocked items handled?
- What happens when a WIP limit is reached?

Explicit policies eliminate inconsistent behavior and reduce the need for constant management direction.

---

## 5. Scrum vs. Kanban — Side-by-Side Comparison

| Dimension | Scrum | Kanban |
|---|---|---|
| Cadence | Fixed Sprints (1–4 weeks) | Continuous flow; no required cadence |
| Prescribed roles | Yes: Product Owner, Scrum Master, Developers | No prescribed roles |
| Prescribed events | Yes: 5 events with timeboxes | No prescribed events |
| WIP management | Implicit (Sprint scope limits work) | Explicit WIP limits on board columns |
| Iteration commitment | Sprint Goal | No Sprint Goal; items pulled individually |
| Accepting new work | Protected Sprint scope; new items to Product Backlog | New items can be pulled anytime within WIP limits |
| Output metric | Velocity (story points per Sprint) | Throughput (items per week) and cycle time |
| Best fit | Product development with evolving features | Operations, support, continuous maintenance |
| Change management | Changes deferred to next Sprint | Changes accepted anytime within limits |

---

## 6. Scrumban

Scrumban is an informal term for teams that combine Scrum's structural elements with Kanban's flow-based practices. Common Scrumban configurations:

- Using a Kanban board within a Sprint to visualize and limit WIP at the task level
- Using Kanban's cycle time and throughput metrics alongside Scrum's velocity
- Applying Kanban WIP limits to specific workflow stages (e.g., no more than 2 items in code review at once)
- Retaining Scrum events (Daily Scrum, Retrospective) while using Kanban flow management

Scrumban is not an official framework and is not mentioned in the Scrum Guide. However, the Scrum Guide explicitly states that Scrum is a framework within which teams can employ various processes and techniques — Kanban practices are a natural complement.

---

## 7. PSM I Exam Tips

Tip 1: Scrum has prescribed roles, events, and artifacts. Kanban has none of these. PSM I questions that describe a "Scrum team" using a Kanban board are not violating Scrum; the Scrum Guide does not prohibit Kanban tools within a Sprint.

Tip 2: WIP limits are a Kanban concept, not a Scrum concept. The Scrum Guide does not mention WIP limits. If a PSM I question mentions WIP limits, it is in a Kanban or Scrumban context.

Tip 3: Lean's pull principle is foundational to understanding why Scrum's Sprint Planning is designed as it is — Developers pull work from the Product Backlog rather than having it pushed onto them.

Tip 4: Lean's seven wastes map directly to common software problems. "Partially done work" is particularly relevant to Scrum — items that do not meet the Definition of Done at Sprint end are partially done work waste.

Tip 5: Cycle time and throughput are Kanban metrics. Velocity is a Scrum-adjacent metric. Both are legitimate planning tools but measure different things and are not interchangeable.

Tip 6: The PSM I exam may present scenarios describing Kanban practices (continuous flow, no Sprints, WIP limits) and ask whether this is Scrum. The answer is no — these are Kanban practices. Scrum requires Sprints and Sprint events.

Tip 7: Agile Manifesto Principle 10 (maximize work not done) is the Manifesto's expression of Lean waste elimination. When exam questions connect Lean to Agile, this principle is the bridge.

Tip 8: Kanban does not require or prohibit any specific estimation technique. Some Kanban teams use story points; others use T-shirt sizes; some use no estimates at all (#NoEstimates). The absence of prescribed estimation is a key Kanban characteristic.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 09 topics:

**1. "Kanban Guide for Scrum Teams" — Scrum.org**
<https://www.scrum.org/resources/kanban-guide-scrum-teams>
An official Scrum.org guide describing how Kanban practices can be applied within a Scrum Team context. Covers flow metrics, WIP limits, and the relationship between the Sprint and Kanban's continuous flow. Free PDF download from Scrum.org.

**2. "Lean Software Development: An Agile Toolkit" — Chapter Summary (Mary Poppendieck)**
<https://www.informit.com/articles/article.aspx?p=169223>
A free excerpt and summary from the original Poppendieck Lean Software Development book on InformIT. Covers the seven wastes of software development with software-specific examples. Essential reading for Module 09's waste analysis lab.

**3. "Little's Law for Everyone" — Dr. Neil Gunther**
<https://www.agilealliance.org/resources/experience-reports/littles-law-applied-to-agile-development/>
An accessible Agile Alliance article applying Little's Law to software development teams. Explains the math behind WIP limits and cycle time improvement with worked numerical examples. Free access via the Agile Alliance resource library.

---

## 8. Study Checklist

- [ ] State the five Lean principles from memory and give one software example for each
- [ ] List the seven wastes of Lean software development and identify a specific example of each in a software team context
- [ ] Describe the four core Kanban practices and explain why each improves team performance
- [ ] Explain Little's Law and how it justifies WIP limits
- [ ] Complete the Scrum vs. Kanban comparison table from memory across all eight dimensions
- [ ] Explain what Scrumban is and give two examples of how a Scrum team might incorporate Kanban practices
- [ ] Explain the connection between Lean's pull principle and Scrum's Sprint Planning
- [ ] Complete this module's Lab and Quiz

---
