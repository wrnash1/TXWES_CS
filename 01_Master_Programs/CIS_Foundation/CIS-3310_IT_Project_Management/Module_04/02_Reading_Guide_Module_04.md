# Reading Guide: Module 04 – Schedule Management: Gantt Charts and CPM

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

Schedule Management is one of the most calculation-intensive topics on the CompTIA Project+ exam. You must be able to read a Gantt chart, calculate critical path duration, perform forward and backward pass arithmetic, compute float, and select the correct schedule compression technique. This reading guide provides the reference tables, formulas, and exam tips you need to master these skills.

---

## 1. High-Yield Glossary

### Schedule Baseline

The approved version of the project schedule, established at the end of Planning. The Schedule Baseline is used in Earned Value Management to calculate Planned Value (PV) and Schedule Variance (SV). Changes require a formal change request and approval.

### Activity

A specific, schedulable unit of work derived from a WBS work package. Activities are the verbs of the schedule — "Configure server," "Write test cases," "Conduct training." Activities have durations, resources, and dependencies.

### Milestone

A significant event with zero duration. Milestones mark important points in the project (phase completions, approvals, go-live). Represented as a diamond on a Gantt chart.

### Gantt Chart

A bar chart that displays the project schedule with activities shown as horizontal bars on a timeline. Easy to communicate to stakeholders, but does not directly show which activities are critical.

### Network Diagram (Precedence Diagramming Method)

A visual representation of the logical sequence of project activities and their dependencies. The foundation for Critical Path Method calculations. Also called PDM (Precedence Diagramming Method) or AON (Activity-on-Node) diagram.

### Critical Path

The longest continuous path of dependent activities from project start to finish. Determines the shortest possible project duration. Critical path activities have zero total float — any delay to a critical path task delays the project end date.

### Total Float (Slack)

The amount of time an activity can be delayed without delaying the project's planned completion date. Formula: Total Float = LS - ES or LF - EF. Critical path activities have zero total float.

### Free Float

The amount of time an activity can be delayed without delaying the Early Start of any of its immediate successors. Free Float is always less than or equal to Total Float.

### Lag Time

A deliberate waiting period inserted between the end of a predecessor activity and the start of its successor. Lag extends the schedule. Represented as a positive value. Example: +3 days after pouring concrete before tiling can begin.

### Lead Time

The amount of time a successor activity is allowed to start before its predecessor finishes. Lead compresses the schedule. Represented as a negative lag value. Example: -2 days means the successor starts 2 days before the predecessor finishes.

### Crashing

A schedule compression technique that adds resources (people, equipment, overtime) to critical path activities to shorten their duration. Effect: shorter schedule, higher cost.

### Fast-Tracking

A schedule compression technique that overlaps activities that were originally planned to be done sequentially. Effect: shorter schedule, higher risk of rework.

### Resource Leveling

Adjusting the schedule to resolve resource over-allocation by delaying activities until the overloaded resource has capacity. Effect: typically extends the schedule; resolves resource conflicts.

### Three-Point Estimating (PERT)

An estimating technique that calculates a weighted average using three estimates: Optimistic (O), Most Likely (M), and Pessimistic (P).

PERT Expected Duration = (O + 4M + P) / 6

PERT Standard Deviation = (P - O) / 6

---

## 2. Dependency Types Reference Table

| Type | Code | Definition | Exam Example |
|---|---|---|---|
| Finish-to-Start | FS | Successor cannot START until predecessor FINISHES | Testing cannot start until Development finishes |
| Start-to-Start | SS | Successor cannot START until predecessor STARTS | Documentation cannot start until Design starts |
| Finish-to-Finish | FF | Successor cannot FINISH until predecessor FINISHES | UAT cannot finish until all defect fixes finish |
| Start-to-Finish | SF | Successor cannot FINISH until predecessor STARTS | Rarely used in practice |

---

## 3. Critical Path Method — Forward and Backward Pass Formulas

### Forward Pass (Left to Right) — Calculates Early Dates

- Early Start (ES) of first activity = 1 (or 0, depending on convention)
- Early Finish (EF) = ES + Duration - 1
- ES of a successor = EF of predecessor + 1
- If multiple predecessors, use the LARGEST EF + 1

### Backward Pass (Right to Left) — Calculates Late Dates

- Late Finish (LF) of last activity = EF of last activity
- Late Start (LS) = LF - Duration + 1
- LF of a predecessor = LS of successor - 1
- If multiple successors, use the SMALLEST LS - 1

### Float Calculations

- Total Float = LS - ES (or LF - EF)
- Free Float = ES of successor - EF of current activity - 1
- Critical path activities: Total Float = 0

---

## 4. Worked CPM Example

Given the following activities:

| Activity | Duration | Predecessors |
|---|---|---|
| A | 4 days | None |
| B | 3 days | A |
| C | 5 days | A |
| D | 2 days | B |
| E | 4 days | C, D |

Paths through the network:

- Path A → B → D → E: 4 + 3 + 2 + 4 = 13 days
- Path A → C → E: 4 + 5 + 4 = 13 days

Both paths are 13 days — both are critical paths. Project duration = 13 days.

Float for Activity B: Total float = 13 - (4+3+2) = 13 - 9 = 4 days? No — let's use the formula.

Forward pass for B: ES = 5, EF = 7. Backward pass for B: LF = 7 (constrained by D→E path going through C). Wait — since both paths are equal at 13 days, all activities have zero float and all are critical.

If instead Activity C had a duration of 3 days (not 5), then:

- Path A → B → D → E: 4 + 3 + 2 + 4 = 13 days (critical)
- Path A → C → E: 4 + 3 + 4 = 11 days

Float on path A → C → E = 13 - 11 = 2 days. Activities C has 2 days of float; Activity A and E are on both paths and have zero float.

---

## 5. Schedule Compression Comparison

| Technique | Method | Cost Impact | Risk Impact | When to Use |
|---|---|---|---|---|
| Crashing | Add resources to critical path tasks | Increases cost | Low to moderate | When budget allows; deadline is firm |
| Fast-tracking | Overlap sequential critical path activities | Minimal direct increase | Increases rework risk | When rework risk is acceptable |
| Resource leveling | Shift activities to reduce over-allocation | Minimal | Low | When resource conflicts exist (extends schedule) |

---

## 6. Estimation Techniques Comparison

| Technique | Data Required | Accuracy | When Used |
|---|---|---|---|
| Analogous (Top-down) | Historical data from similar projects | Low to moderate | Early phases; limited detail available |
| Parametric | Statistical unit rates (cost per server, hours per module) | Moderate | When reliable unit rates exist |
| Bottom-up | Complete WBS with detailed work packages | High | When WBS is complete and accuracy is critical |
| Three-point (PERT) | O, M, P estimates per activity | Moderate to high | When activity durations are uncertain |

---

## 7. Certification Exam Tips

**Tip 1 — Lag vs. lead on the exam:**
Lag = delay (positive number, extends schedule). Lead = head start (negative lag, compresses schedule). The exam will describe a scenario and ask which one is being used. Lead means overlap; lag means wait.

**Tip 2 — Critical path = longest path, not shortest:**
Students sometimes confuse "critical" with "fastest." The critical path is the LONGEST path — it determines the minimum project duration. There is no float on the critical path.

**Tip 3 — Multiple critical paths:**
A project can have more than one critical path. When two paths have equal duration, both are critical. Adding a day to any activity on either path extends the project.

**Tip 4 — Float belongs to the path:**
When non-critical activities share a path, the float is shared across all of them. If one activity uses two days of float, only the remaining float is available for the others on that path.

**Tip 5 — Crashing only works on critical path:**
Adding resources to a non-critical path activity will not shorten the project. Crashing must target critical path activities. The exam tests this with questions asking which activity to crash.

**Tip 6 — Fast-tracking increases risk:**
Fast-tracking increases the probability of rework because later tasks begin before earlier tasks are fully complete. It does not increase cost directly, but rework will if assumptions prove wrong.

**Tip 7 — Gantt charts do not show float:**
A Gantt chart is a communication tool that displays timing and dependencies but does not directly reveal which activities have float and which are on the critical path. For float information, you need the CPM network diagram calculations.

**Tip 8 — PERT formula on the exam:**
Expected Duration = (O + 4M + P) / 6. The factor of 4 weights the most likely estimate more heavily. This formula appears in both schedule and cost estimation contexts.

---

## 8. Required Reading and Study Resources

Complete the following before the lab and quiz:

- Read the schedule management chapter in the course OER textbook (linked in Canvas), focusing on CPM and network diagrams.
- Review the CompTIA Project+ PK0-005 exam objectives at comptia.org for the schedule management domain.
- For supplemental study, visit professormesser.com for Project+ schedule management coverage.

---

## 9. Study Checklist

- [ ] List all six Schedule Management processes in correct order
- [ ] Explain the difference between an activity and a milestone
- [ ] Describe all four dependency types with an original IT example for each
- [ ] Explain lag vs. lead time and give an example of each
- [ ] Define critical path and explain why critical path activities have zero float
- [ ] Perform a forward and backward pass for a 5-activity network (use Section 4 example to practice)
- [ ] Calculate total float using the LS - ES formula
- [ ] Distinguish crashing from fast-tracking using cost and risk impacts
- [ ] State the PERT three-point estimating formula from memory
- [ ] Complete the Module 04 Lab CPM calculation exercises
- [ ] Take the Module 04 Quiz
- [ ] Post Module 04 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 6: Schedule Management**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 6](https://opentextbc.ca/projectmanagement/chapter/chapter-6-project-time-management/)
   Covers activity sequencing, network diagrams, critical path method, and schedule compression. Includes step-by-step CPM examples.

2. **YouTube — "Critical Path Method Explained" (Practical PM)**
   [youtube.com/watch?v=4oDLMs11Exs](https://www.youtube.com/watch?v=4oDLMs11Exs)
   Clear visual walkthrough of the forward pass, backward pass, and float calculation — essential preparation for the Module 04 lab calculations.

3. **PMI — Practice Standard for Scheduling (Overview)**
   *Project Management Institute* — [pmi.org/pmbok-guide-standards/practice-guides/scheduling](https://www.pmi.org/pmbok-guide-standards/practice-guides/scheduling)
   Official PMI scheduling guidance covering PDM dependencies, float types, and schedule baseline development.

4. **Gantt Chart Tutorial — ProjectManager.com (Free)**
   [projectmanager.com/blog/gantt-chart-a-complete-guide](https://www.projectmanager.com/blog/gantt-chart-a-complete-guide)
   Comprehensive free guide to Gantt chart construction, reading milestone markers, and communicating schedule information to stakeholders.

5. **PERT/CPM Calculator — PM Study Circle**
   [pmstudycircle.com/pert-cpm](https://pmstudycircle.com/pert-and-cpm/)
   Interactive examples and formula drills for PERT three-point estimating and CPM float calculations — excellent practice before the quiz.
