# Reading Guide: Module 06 – Quality Management

**Course:** CIS-3310 IT Project Management
**Certification Alignment:** CompTIA Project+ (PK0-005) | PMBOK 6th and 7th Editions
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Quality Management ensures that project deliverables meet the standards and requirements that stakeholders need. It is not about perfection — it is about fitness for use. This module introduces the three quality management processes, the distinction between Quality Assurance and Quality Control, the Cost of Quality framework, and the Seven Basic Quality Tools. All of these appear regularly on the CompTIA Project+ exam.

---

## 1. High-Yield Glossary

### Quality

The degree to which a set of inherent characteristics fulfills requirements. In project management, quality means the deliverable does what it is supposed to do, at the standard required by the stakeholder.

### Grade

A category or ranking assigned to products or services that have the same functional purpose but different technical characteristics. Low grade is not automatically a defect. A budget laptop is low grade but high quality if it does exactly what was promised. A premium laptop that crashes constantly is high grade but low quality.

### Quality Management Plan

A component of the Project Management Plan that describes how the project will implement the organization's quality policies. Includes quality standards, metrics, QA approach, QC approach, and tools to be used.

### Quality Assurance (QA)

The proactive, process-oriented quality activity of auditing processes and standards to ensure they are being followed correctly and will prevent defects. QA occurs during the Executing Process Group. Output: quality reports, change requests for process improvement.

### Quality Control (QC)

The reactive, product-oriented quality activity of inspecting and testing completed deliverables to find defects before delivery. QC occurs during the Monitoring and Controlling Process Group. Output: quality control measurements, verified deliverables, defect reports.

### Cost of Quality (COQ)

All costs incurred to achieve quality or deal with the lack of it. Broken into conformance costs (prevention and appraisal) and non-conformance costs (internal and external failure).

### Control Chart

A statistical process control chart with upper and lower control limits. Points outside control limits signal an out-of-control process. The Rule of Seven states that seven consecutive data points on one side of the mean indicate a non-random pattern requiring investigation.

### Pareto Chart

A bar chart ranking defect types from most to least frequent, based on the 80/20 rule (roughly 80% of defects come from 20% of causes). Used to prioritize corrective actions.

### Ishikawa Diagram

Also called a Fishbone or Cause-and-Effect diagram. A visual tool for identifying the root causes of a quality problem, organized by category (People, Process, Equipment, Materials, Environment, Measurement).

### Checksheet

A simple data collection form used during real-time QC activities to record the frequency of defects or events.

### Histogram

A bar chart showing the frequency distribution of defect data over a range of values. Reveals patterns and central tendencies in quality data.

### Scatter Diagram

A graph plotting two variables to test for correlation. Used to validate hypotheses about cause-and-effect relationships in quality data.

### Benchmarking

Comparing the project's quality practices or metrics against industry standards or similar projects to identify improvement opportunities.

### Statistical Sampling

Testing a representative subset of the total population of items rather than inspecting every item. Used when 100% inspection is too costly or time-consuming.

### Fitness for Use

The concept that quality is defined by whether the deliverable meets the stakeholder's intended purpose, not by whether it meets an abstract standard of perfection.

---

## 2. Quality Management Process Reference

| Process | Process Group | Primary Purpose | Key Output |
|---|---|---|---|
| Plan Quality Management | Planning | Define quality standards and how they will be met | Quality Management Plan, Quality Metrics |
| Manage Quality (QA) | Executing | Audit processes; ensure quality standards are being followed | Quality Reports, Change Requests |
| Control Quality (QC) | Monitoring and Controlling | Inspect deliverables for defects; verify quality | Verified Deliverables, QC Measurements |

---

## 3. QA vs. QC Comparison

| Attribute | Quality Assurance (QA) | Quality Control (QC) |
|---|---|---|
| Orientation | Process-focused | Product-focused |
| Timing | Proactive (prevent defects) | Reactive (detect defects) |
| Process Group | Executing | Monitoring and Controlling |
| Question answered | "Are we doing the work correctly?" | "Does this deliverable meet the standard?" |
| Example activity | Process audit against coding standards | Running test cases on completed software modules |
| PMI process name | Manage Quality | Control Quality |
| Output | Quality reports, process change requests | Verified deliverables, defect reports |

---

## 4. Cost of Quality Categories

| Category | Type | Examples |
|---|---|---|
| Prevention | Conformance | Training, process design, quality planning, requirements reviews |
| Appraisal | Conformance | Testing, inspections, audits, peer reviews |
| Internal Failure | Non-conformance | Rework, scrap, re-testing, defect repair before delivery |
| External Failure | Non-conformance | Customer complaints, warranty work, recalls, legal liability |

The goal is to invest in Prevention and Appraisal costs to reduce Internal and External Failure costs. External failures are always more expensive than internal failures, which are always more expensive than prevention.

---

## 5. Seven Basic Quality Tools Reference

| Tool | Purpose | When to Use |
|---|---|---|
| Cause-and-Effect (Fishbone/Ishikawa) | Identify root causes of a defect, organized by category | When investigating why a defect is occurring |
| Flowchart (Process Map) | Visualize process steps and decision points | When analyzing a process for inefficiencies |
| Checksheet | Collect real-time tally data on defect frequency | During live QC activities |
| Pareto Chart | Rank defect categories by frequency to prioritize | When deciding which problem to fix first |
| Histogram | Show frequency distribution of defect data | When analyzing patterns in quality data |
| Control Chart | Monitor process stability over time against control limits | For ongoing process monitoring |
| Scatter Diagram | Test correlation between two variables | When testing a cause-and-effect hypothesis |

---

## 6. Control Chart Rules

The Control Chart uses three key lines:

- Upper Control Limit (UCL): the upper boundary of acceptable variation (typically 3 standard deviations above the mean)
- Mean (centerline): the process average
- Lower Control Limit (LCL): the lower boundary (typically 3 standard deviations below the mean)

A data point outside the UCL or LCL indicates a special cause variation — the process is out of control and requires investigation.

The Rule of Seven: seven consecutive data points on the same side of the mean, even within control limits, indicate a non-random pattern and warrant investigation.

---

## 7. Certification Exam Tips

**Tip 1 — QA = process audit; QC = product inspection:**
This is the most tested quality distinction. If the scenario describes reviewing a process or auditing compliance, it is QA. If it describes testing a deliverable or finding a defect, it is QC.

**Tip 2 — Validate Scope vs. Control Quality:**
Validate Scope is about customer acceptance of deliverables (Executing). Control Quality is about the PM verifying deliverables meet quality standards before presenting them to the customer (M&C). Control Quality happens before Validate Scope.

**Tip 3 — Pareto = prioritize the vital few:**
The Pareto chart's 80/20 principle means you should focus your corrective actions on the top two or three defect categories, not spread effort across all categories equally.

**Tip 4 — Fishbone identifies causes, not solutions:**
The Ishikawa diagram is a brainstorming tool for root cause analysis. It identifies potential causes of a problem. The corrective action comes after the diagram is analyzed — the diagram itself does not solve the problem.

**Tip 5 — Control chart = out-of-control process:**
If an exam scenario describes data points outside the control limits, the answer involves a Control Chart and an investigation of special cause variation. Control charts are also the answer for "monitoring process stability over time."

**Tip 6 — Grade vs. quality:**
A product can be low grade (basic features) and high quality (works perfectly as promised). A product can be high grade (many features) and low quality (broken, unreliable). The exam tests this distinction with scenario questions about customer satisfaction.

**Tip 7 — COQ: Prevention is cheapest:**
Prevention costs are the least expensive category in COQ. Every dollar invested in preventing defects saves multiple dollars in rework and customer failure costs. The exam may ask which COQ investment has the greatest return — prevention.

**Tip 8 — Statistical sampling is acceptable:**
When 100% inspection is impractical, statistical sampling is a valid QC approach. The sample must be representative and the sampling method must be defined in the Quality Management Plan.

---

## 8. Required Reading and Study Resources

Complete the following before the lab and quiz:

- Read the quality management chapter in the course OER textbook (linked in Canvas).
- Review the CompTIA Project+ PK0-005 exam objectives at comptia.org for the quality management domain.
- For supplemental study, visit professormesser.com for Project+ quality management coverage.

---

## 9. Study Checklist

- [ ] Distinguish QA from QC using the process group, orientation, and example activity criteria
- [ ] List all four Cost of Quality categories with one IT example for each
- [ ] Name and describe all seven basic quality tools
- [ ] Explain the 80/20 rule as it applies to the Pareto chart
- [ ] Explain the Rule of Seven as it applies to the Control Chart
- [ ] Distinguish Validate Scope from Control Quality
- [ ] Explain the difference between quality and grade with an IT hardware example
- [ ] Complete the Module 06 Lab activity
- [ ] Take the Module 06 Quiz
- [ ] Post Module 06 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 8: Quality Management**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 8](https://opentextbc.ca/projectmanagement/chapter/chapter-8-project-quality-management/)
   Covers QA vs. QC, the seven basic quality tools, and Cost of Quality with IT-sector examples.

2. **ASQ — Seven Basic Quality Tools (Free Reference)**
   *American Society for Quality* — [asq.org/quality-resources/seven-basic-quality-tools](https://asq.org/quality-resources/seven-basic-quality-tools)
   The definitive free reference for all seven tools (flowchart, check sheet, Pareto, histogram, scatter diagram, control chart, fishbone). Includes visual examples for each.

3. **YouTube — "Quality Management for PMP/CAPM" (Ricardo Vargas)**
   [youtube.com/watch?v=SBKIoYiMCUo](https://www.youtube.com/watch?v=SBKIoYiMCUo)
   Clear 20-minute video covering QA/QC distinction, COQ categories, and quality tools with exam-focused explanations.

4. **PMI — Quality Management Overview**
   *Project Management Institute* — [pmi.org/learning/library/quality-management-overview](https://www.pmi.org/learning/library/quality-management-4289)
   PMI article outlining the Plan Quality Management, Manage Quality, and Control Quality processes as tested on PK0-005.

5. **Cost of Quality Calculator and Guide — iSixSigma (Free)**
   [isixsigma.com/methodology/cost-of-quality](https://www.isixsigma.com/methodology/cost-of-quality-coq/)
   Detailed breakdown of prevention, appraisal, internal failure, and external failure costs with calculation examples — directly supports the COQ classification activity in the Module 06 lab.
