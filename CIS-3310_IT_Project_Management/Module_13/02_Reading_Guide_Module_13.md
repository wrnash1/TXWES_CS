# Reading Guide: Module 13 — Quality Management

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


## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Introduction

Quality Management governs how a project defines, builds, and verifies quality in its deliverables and processes. The Project+ exam tests quality in three distinct ways: process identification (which quality process does this activity belong to?), tool identification (which quality tool is being used?), and concept application (QA vs. QC, prevention vs. appraisal costs, root cause vs. prioritization). This reading guide covers all three.

---

## Section 1 — High-Yield Glossary

### Quality

In project management, quality means conformance to requirements and fitness for use. A deliverable that meets all written specifications but fails to satisfy the customer's real need does not meet the quality standard.

### Quality Management Plan

A subsidiary plan defining quality standards, metrics, QA and QC activities, roles and responsibilities, and the tools and techniques to be applied. Created during Plan Quality Management.

### Quality Baseline

The documented target performance levels for quality metrics that will be used to compare actual quality results during monitoring and controlling.

### Quality Metric

A specific, measurable criterion used to determine whether a deliverable or process meets quality standards. Examples: defect rate, test coverage percentage, uptime percentage, mean time between failures.

### Quality Assurance (QA)

The process of auditing quality requirements and results from quality control measurements to ensure appropriate quality standards and operational definitions are used. QA is process-focused, proactive, and belongs to the Executing process group.

### Quality Control (QC)

The process of monitoring and recording results of executing quality activities to assess performance and recommend changes. QC is product-focused, reactive, and belongs to the Monitoring and Controlling process group.

### Cost of Quality (COQ)

The total cost of all quality-related activities including prevention, appraisal, and both categories of failure costs. Analyzing COQ helps organizations optimize quality investment allocation.

### Prevention Costs

Money spent to prevent defects from occurring. Includes training, process design, quality planning, and code reviews. Prevention is the cheapest quality investment.

### Appraisal Costs

Money spent evaluating whether quality standards are being met. Includes testing, inspections, audits, and peer reviews.

### Internal Failure Costs

Costs incurred when defects are found before delivery to the customer. Includes rework, scrap, debugging, and re-testing.

### External Failure Costs

Costs incurred when defects are found after delivery to the customer. Includes warranty repairs, support costs, rollbacks, and reputational damage. The most expensive quality cost category.

### Rule of Ten

The principle that the cost to fix a defect increases by approximately 10x for each phase it passes through undetected. Fixing a requirements defect is roughly 1/1,000th the cost of fixing it after customer delivery.

### Ishikawa Diagram

Also called a fishbone diagram or cause-and-effect diagram. A visual tool that maps potential root causes of a problem into categories to support structured root cause analysis.

### Pareto Chart

A combined bar chart and cumulative line graph that ranks defect types by frequency. Based on the Pareto principle: 80% of problems typically come from 20% of causes.

### Pareto Principle

The observation that a small number of causes account for the majority of effects. In quality management: approximately 80% of defects come from 20% of causes. The vital few vs. the trivial many.

### Control Chart

A time-series graph that tracks a quality metric against upper and lower control limits to determine whether a process is in statistical control. Points outside limits or seven consecutive points on one side of the center line indicate the process is out of control.

### Rule of Seven

A control chart interpretation rule: seven consecutive data points on one side of the center line (even within control limits) indicate a non-random pattern and signal that the process has shifted out of control.

### PDCA Cycle

Plan-Do-Check-Act. A continuous improvement framework in which changes are planned, implemented on a small scale, evaluated, and then standardized (if successful) or revised (if not). Also called the Deming Cycle or Shewhart Cycle.

### Kaizen

A Japanese philosophy meaning "change for the better." Describes small, continuous, incremental improvements made by all members of an organization over time.

### Six Sigma

A data-driven quality improvement methodology targeting fewer than 3.4 defects per million opportunities. Uses the DMAIC process: Define, Measure, Analyze, Improve, Control.

### Gold Plating

Adding features or functionality beyond the agreed-upon scope without a change request, often in the belief that the customer will appreciate it. Gold plating is a quality management violation — it consumes resources, may introduce defects, and bypasses the change control process.

---

## Section 2 — Quality Management Process Reference

| Process | Process Group | Key Inputs | Key Outputs |
|---------|--------------|------------|-------------|
| Plan Quality Management | Planning | Scope baseline, requirements, risk register, stakeholder register | Quality Management Plan, quality metrics, quality checklists |
| Manage Quality (QA) | Executing | Quality Management Plan, quality metrics, process performance data | Quality reports, process change recommendations, audit findings |
| Control Quality (QC) | Monitoring and Controlling | Deliverables, quality metrics, quality checklists | Verified deliverables, defect findings, change requests |

---

## Section 3 — QA vs. QC Comparison

| Dimension | Quality Assurance (QA) | Quality Control (QC) |
|-----------|----------------------|---------------------|
| Focus | Process | Product / Deliverable |
| Orientation | Proactive | Reactive |
| Process Group | Executing | Monitoring and Controlling |
| Core Question | Are we following the right process? | Does this deliverable meet standards? |
| Primary Activities | Process audits, process improvement, quality management reviews | Inspections, testing, measurement, defect logging |
| Primary Tools | Process checklists, audit frameworks, flowcharts | Pareto charts, control charts, inspection checklists, Ishikawa |
| Output | Process improvement recommendations | Verified deliverables, defect reports |

---

## Section 4 — Cost of Quality Framework

| Category | Definition | IT Examples | Cost Level |
|----------|-----------|------------|------------|
| Prevention | Costs to prevent defects before they occur | Code review standards, developer training, quality planning | Lowest |
| Appraisal | Costs to evaluate quality of deliverables | Automated testing, peer reviews, code scanning, QA audits | Moderate |
| Internal Failure | Costs of defects found before customer delivery | Rework, bug fixing, re-testing, sprint rollbacks | High |
| External Failure | Costs of defects found after customer delivery | Hotfixes, support calls, SLA penalties, reputational damage | Highest |

The optimal quality investment strategy allocates the most resources to prevention and appraisal, which eliminates or reduces internal and external failure costs.

---

## Section 5 — Ishikawa Diagram Reference

### Structure

- Effect (problem): placed in a box at the right end of the main arrow
- Spine: horizontal arrow pointing to the effect
- Major bones: diagonal branches from the spine representing cause categories
- Minor bones: specific causes branching from each category

### Standard IT Cause Categories (6M)

| Category | Covers |
|----------|--------|
| Methods | Processes, procedures, work instructions |
| Machines | Systems, hardware, software tools, infrastructure |
| Materials | Data, documentation, inputs, third-party content |
| Measurement | Metrics, monitoring, reporting accuracy |
| Manpower | Skills, training, staffing, team capability |
| Mother Nature / Environment | Infrastructure environment, regulatory context, external conditions |

### When to Use

Use an Ishikawa diagram when a team needs to systematically identify the root causes of a recurring defect, incident, or quality failure before selecting a solution. It prevents jumping to solutions before understanding causes.

---

## Section 6 — Pareto Chart Reference

### Structure

- Left Y-axis: frequency (count of defects per category)
- Right Y-axis: cumulative percentage (0–100%)
- X-axis: defect categories ordered from most frequent to least frequent
- Bars: frequency of each category
- Line: cumulative percentage rising from left to right

### Reading a Pareto Chart

1. Identify the categories to the left of the 80% cumulative line
2. These are the "vital few" — the causes responsible for 80% of defects
3. Focus improvement efforts on these categories first

### Pareto Chart Sample Interpretation

If five defect categories total 200 defects and the top two categories account for 160 defects (80%), then fixing those two categories eliminates 80% of all defects. The remaining three categories are the "trivial many."

### When to Use

Use a Pareto chart when a team has defect frequency data and needs to prioritize which defect types to address to achieve the greatest improvement with limited resources.

---

## Section 7 — Control Chart Reference

| Element | Description |
|---------|-------------|
| Center Line (CL) | The process mean — expected average performance |
| Upper Control Limit (UCL) | Upper boundary of acceptable variation (typically mean + 3 sigma) |
| Lower Control Limit (LCL) | Lower boundary of acceptable variation (typically mean - 3 sigma) |
| In Control | All points within UCL and LCL; no non-random patterns |
| Out of Control (Special Cause) | One or more points outside UCL or LCL |
| Rule of Seven | Seven consecutive points on one side of CL — process has shifted |

---

## Section 8 — PDCA and Improvement Frameworks

### PDCA Cycle Steps

| Step | Action |
|------|--------|
| Plan | Define the problem; identify root cause; design the change |
| Do | Implement the change on a small scale (pilot) |
| Check | Measure results; compare to expected improvement |
| Act | Standardize if successful; revise and re-plan if not |

### Comparison of Improvement Philosophies

| Framework | Philosophy | Approach | Scale |
|-----------|-----------|---------|-------|
| Kaizen | Small, continuous, incremental improvement | Everyone participates; daily small changes | Organization-wide |
| Six Sigma | Defect reduction to 3.4 per million opportunities | Data-driven DMAIC methodology | Project-specific |
| PDCA | Structured improvement cycle | Plan small change; test; evaluate; standardize | Process-level |
| TQM | Total Quality Management — culture of quality | Broad organizational commitment to quality | Enterprise-wide |

---

## Section 9 — Project+ Exam Tips

**Tip 1 — QA is process, QC is product:**
This is the single most tested quality distinction. When the exam describes an audit of a process, a review of whether procedures are being followed, or an evaluation of how work is being done, that is QA. When the exam describes testing a deliverable, inspecting output, or measuring actual results against specifications, that is QC.

**Tip 2 — QA is Executing; QC is Monitoring and Controlling:**
Process group placement is tested directly. QA (Manage Quality) belongs to Executing. QC (Control Quality) belongs to Monitoring and Controlling.

**Tip 3 — Ishikawa for root cause; Pareto for prioritization:**
When the exam describes identifying why a problem occurs — analyzing categories of causes — the tool is Ishikawa. When the exam describes ranking defect types by frequency to focus resources — "which problems should we fix first" — the tool is Pareto.

**Tip 4 — Prevention costs less than failure:**
Any exam question about Cost of Quality economics points to the same answer: investing in prevention (training, process design, quality planning) produces lower total quality costs than discovering defects late. External failure is always the most expensive category.

**Tip 5 — Rule of Seven applies even when points are within limits:**
A control chart can show a process out of control even when no individual data point exceeds the UCL or LCL. Seven consecutive points on one side of the center line indicates a non-random process shift that must be investigated.

**Tip 6 — Gold plating violates quality and scope management:**
Adding features without a change request — even well-intentioned additions — violates both the change control process and quality management principles. The exam will present gold plating scenarios as wrong-answer behavior.

**Tip 7 — PDCA is cyclical, not linear:**
After the Act step, the cycle returns to Plan. Quality improvement never ends. If the exam asks what happens after a change is successfully implemented and standardized, the answer is returning to Plan for the next improvement cycle.

**Tip 8 — Six Sigma uses DMAIC, not PDCA:**
Six Sigma's five-step process is Define, Measure, Analyze, Improve, Control. This is different from PDCA's four steps. The exam may test which framework uses which process.

---

## Section 10 — Study Checklist

- [ ] Define quality in project management terms (conformance to requirements and fitness for use)
- [ ] Name and describe all four Cost of Quality categories with an IT example for each
- [ ] Explain the difference between QA and QC using process group, focus, and orientation
- [ ] Describe the structure of an Ishikawa diagram and name four cause categories
- [ ] Explain the Pareto principle and describe how to read a Pareto chart
- [ ] Define the Rule of Seven in control chart interpretation
- [ ] Name the four steps of the PDCA cycle and explain what each means
- [ ] Distinguish Kaizen from Six Sigma with one sentence each
- [ ] Define gold plating and explain why it is considered a quality violation
- [ ] Complete the Module 13 Lab quality tools activity
- [ ] Take the Module 13 Quiz (10 questions)
- [ ] Post Module 13 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 8: Quality Management Tools**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 8](https://opentextbc.ca/projectmanagement/chapter/chapter-8-project-quality-management/)
   Covers the seven basic quality tools including the Pareto chart, Fishbone diagram, and Control Chart with worked examples relevant to IT projects.

2. **ASQ — PDCA Cycle Overview (Free)**
   *American Society for Quality* — [asq.org/quality-resources/pdca-cycle](https://asq.org/quality-resources/pdca-cycle)
   Official ASQ explanation of the Plan-Do-Check-Act cycle with application examples. Directly tested on the Project+ exam in the quality management domain.

3. **iSixSigma — DMAIC vs. PDCA Comparison (Free)**
   [isixsigma.com/dmaic-vs-pdca](https://www.isixsigma.com/methodology/dmaic/pdca-vs-dmaic-which-one-should-you-use/)
   Side-by-side comparison of DMAIC and PDCA — addresses one of the most commonly tested quality framework distinctions on the Project+ exam.

4. **YouTube — "Fishbone Diagram Tutorial" (ASQ)**
   [youtube.com/watch?v=7aqXyNaQMVE](https://www.youtube.com/watch?v=7aqXyNaQMVE)
   Step-by-step demonstration of building an Ishikawa diagram using a real defect scenario. Directly supports the Module 13 lab root cause analysis exercise.

5. **Control Chart Tutorial — StatisticsHowTo (Free)**
   [statisticshowto.com/control-chart](https://www.statisticshowto.com/control-chart/)
   Clear explanation of UCL/LCL calculation, the Rule of Seven, and how to interpret out-of-control signals. Includes visual examples for all common control chart patterns.
