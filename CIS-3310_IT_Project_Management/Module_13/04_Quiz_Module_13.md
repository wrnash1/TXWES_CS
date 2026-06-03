# Quiz: Module 13 — Quality Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Question 1

A quality manager is conducting a review of the software development process to verify that developers are following the peer code review procedure defined in the Quality Management Plan. No actual code or deliverables are being examined — only whether the process is being followed. Which quality activity is this?

- A) Quality Control
- B) Quality Assurance
- C) Quality Planning
- D) Defect repair

**Correct Answer: B**

Quality Assurance (QA) is process-focused and proactive. It evaluates whether the correct processes and procedures are being followed during execution. Auditing adherence to the peer code review procedure — without inspecting the deliverable itself — is a QA activity.

Distractor Analysis:

- **Why B is correct:** QA asks "Are we doing it right?" by examining processes and procedures. The manager is verifying whether a defined process (peer review) is being followed, not measuring the quality of specific code output. This is a process audit — the defining QA activity.
- **Why A is incorrect:** Quality Control examines actual deliverables — code, documents, test results — to determine whether they meet quality standards. No deliverable is being inspected in this scenario. The focus is entirely on process compliance.
- **Why C is incorrect:** Quality Planning (Plan Quality Management) occurs during the Planning process group and produces the Quality Management Plan and quality metrics. The review described is happening during execution, not planning.
- **Why D is incorrect:** Defect repair is the corrective action taken after a defect is found during QC. The scenario describes a process audit, not a response to an identified defect.

---

## Question 2

A project manager adds a set of advanced analytics dashboards to a software deliverable without a change request because she believes the client will appreciate the extra value. The dashboards were not in the original scope. Which quality concept does this action violate?

- A) Fitness for use
- B) Gold plating
- C) Cost of quality
- D) Kaizen

**Correct Answer: B**

Gold plating is the practice of adding features, functionality, or work beyond the agreed-upon scope without a formal change request. Even well-intentioned additions violate change control, consume unplanned resources, and may introduce defects.

Distractor Analysis:

- **Why B is correct:** Gold plating is explicitly prohibited in project quality management because it bypasses the change control process, consumes budget and schedule resources not allocated for the addition, and may introduce unintended defects in a system not designed or tested for the new features.
- **Why A is incorrect:** Fitness for use refers to whether a deliverable meets the customer's actual need. Adding unrequested features may affect fitness for use, but the term that describes adding unauthorized scope is gold plating specifically.
- **Why C is incorrect:** Cost of quality is a framework for categorizing quality-related spending (prevention, appraisal, internal failure, external failure). Adding unauthorized features is a process violation, not a cost category error.
- **Why D is incorrect:** Kaizen describes a philosophy of small, continuous, incremental improvement made through proper channels. Adding unauthorized features outside the change control process is the opposite of a structured improvement approach.

---

## Question 3

An IT team has been tracking defects logged during testing for the past six months. They have data showing the frequency of each defect type. The quality manager wants to identify which defect types account for most of the problems so the team can concentrate improvement efforts on the highest-impact categories. Which quality tool is most appropriate?

- A) Control chart
- B) Ishikawa diagram
- C) Pareto chart
- D) Scatter diagram

**Correct Answer: C**

The Pareto chart ranks defect categories by frequency and shows the cumulative percentage of total defects. It directly answers the "which defect types account for most problems" question by identifying the vital few causes responsible for approximately 80% of all defects.

Distractor Analysis:

- **Why C is correct:** When the goal is prioritization — deciding where to concentrate limited improvement resources based on defect frequency data — the Pareto chart is the correct tool. It visually identifies the vital few by ranking categories from most to least frequent and overlaying a cumulative percentage line.
- **Why A is incorrect:** Control charts track a metric over time against upper and lower control limits to assess process stability. They answer "is the process in control?" not "which defect type is most common?" No time-series analysis is described here.
- **Why B is incorrect:** Ishikawa diagrams identify the root causes of a specific problem by mapping contributing factors into categories. The team already has defect frequency data — they need prioritization, not root cause mapping. Ishikawa would be used after Pareto to investigate the highest-priority defect categories.
- **Why D is incorrect:** Scatter diagrams show the relationship between two variables to test for correlation. They are used to investigate whether one factor influences another — not to rank and prioritize defect frequencies.

---

## Question 4

A software development team discovers a defect after the product has been deployed to production. Investigation reveals the error was present in the original requirements document but was never caught during design review or testing. According to the Rule of Ten, approximately how does the cost to fix this defect compare to fixing it during requirements?

- A) It costs approximately the same regardless of when the defect is found
- B) It costs approximately 10 times more because the defect passed through design review
- C) It costs approximately 100 to 1,000 times more because it passed through multiple phases undetected
- D) It costs less because fewer resources are needed for a simple post-deployment patch

**Correct Answer: C**

The Rule of Ten states that the cost to fix a defect multiplies by approximately 10 for each phase it passes through undetected. A defect originating in requirements and found after production deployment has passed through at least two to three additional phases, resulting in a cost roughly 100 to 1,000 times higher than if found during requirements.

Distractor Analysis:

- **Why C is correct:** Requirements → design → development → testing → deployment represents multiple phase transitions. Each transition multiplies the correction cost by approximately 10. A defect found at deployment rather than at requirements represents two to three order-of-magnitude cost increase, plus the external impact of deployed production errors.
- **Why A is incorrect:** The Rule of Ten explicitly contradicts this. Defect correction cost is strongly correlated with how late the defect is found. Early detection is the economic foundation of quality management investment.
- **Why B is incorrect:** Passing through one additional phase (requirements to design) would represent approximately 10x. But the scenario describes a defect found after production deployment — it passed through design, development, and testing before external discovery, representing multiple 10x multiplications.
- **Why D is incorrect:** Post-deployment fixes are the most expensive defect corrections. They require change management, user communication, emergency deployment processes, potential rollback planning, and reputational management — costs that far exceed a simple in-development bug fix.

---

## Question 5

A quality team is conducting an Ishikawa analysis on the problem "data migration failures occur in 15% of records processed." Under which cause category would "migration scripts were written without documented testing procedures" most appropriately be placed?

- A) Machines
- B) Materials
- C) Manpower
- D) Methods

**Correct Answer: D**

Methods refers to the processes, procedures, and work instructions used to perform the work. A missing testing procedure for migration scripts is a process gap — a Methods-category root cause.

Distractor Analysis:

- **Why D is correct:** Methods covers processes, procedures, standards, and work instructions. "Scripts written without documented testing procedures" indicates a procedural gap in how the migration work was supposed to be performed — the definition of a Methods category cause.
- **Why A is incorrect:** Machines refers to systems, hardware, software tools, and technical infrastructure. The issue described is not a problem with the tools themselves but with the procedures used when working with those tools.
- **Why B is incorrect:** Materials refers to data, documentation, and input quality. Missing testing documentation is a process gap, not a material quality issue. The scripts themselves might be considered materials, but the absent procedure is a Methods problem.
- **Why C is incorrect:** Manpower refers to skills, training, staffing, and human capability. If the cause were "developers lacked migration experience," that would be Manpower. The cause described is a missing procedure, not a people capability gap.

---

## Question 6

A monthly quality metric for a software release pipeline shows data points at 14%, 15%, 13%, 16%, 14%, 15%, and 17% defect rate over seven consecutive months. The process mean is 18% and the LCL is 10%. No individual point falls below the LCL. Is the process in control?

- A) Yes — all points are within the control limits, so the process is in control
- B) No — all seven points fall below the process mean, triggering the Rule of Seven
- C) Yes — the consistently low values indicate outstanding performance that does not require investigation
- D) No — the LCL has been breached by the consistently low values

**Correct Answer: B**

The Rule of Seven states that seven or more consecutive data points on the same side of the process mean indicate a non-random pattern even when all points fall within control limits. All seven readings fall below the 18% mean, indicating the process has shifted and requires investigation.

Distractor Analysis:

- **Why B is correct:** Control limits are necessary but not sufficient for declaring a process in control. The Rule of Seven identifies systematic process shifts that the control limits alone cannot detect. Seven consecutive points below the mean indicates the process has changed in a non-random way — investigation is required even though the numbers look "good."
- **Why A is incorrect:** Being within control limits is only one condition for statistical control. The Rule of Seven identifies an additional out-of-control signal that applies even when individual points are within limits. Ignoring non-random patterns is a control chart interpretation error.
- **Why C is incorrect:** Consistently below-mean performance is not inherently good — it signals that something changed in the process. If the change is positive (a process improvement was implemented), it should be identified, documented, and the control limits recalculated. Unknown process changes require investigation regardless of direction.
- **Why D is incorrect:** No individual point is below the LCL of 10%. The lowest reading is 13%, which is above the LCL. The LCL has not been breached. The out-of-control signal is the Rule of Seven pattern, not a limit violation.

---

## Question 7

An organization is implementing small, ongoing improvements to its project management processes through team suggestions, daily retrospectives, and incremental procedure updates. No large-scale redesign is planned — the focus is on marginal gains made consistently over time by all team members. Which quality improvement philosophy describes this approach?

- A) Six Sigma
- B) PDCA
- C) Kaizen
- D) TQM

**Correct Answer: C**

Kaizen describes a philosophy of small, continuous, incremental improvements made by all members of an organization over time. It contrasts with breakthrough improvement methodologies like Six Sigma, which target specific high-impact defects using statistical data analysis.

Distractor Analysis:

- **Why C is correct:** The description precisely matches Kaizen's defining characteristics: incremental (not breakthrough) improvements, made continuously, by everyone on the team, accumulated over time. Kaizen does not require statistical expertise or large-scale redesign.
- **Why A is incorrect:** Six Sigma targets specific, measurable defect reduction to fewer than 3.4 per million opportunities using the data-intensive DMAIC process. It is a breakthrough methodology requiring statistical analysis — the opposite of the informal, incremental improvement described.
- **Why B is incorrect:** PDCA is a structured improvement cycle (Plan-Do-Check-Act) used to design, test, evaluate, and standardize specific changes. While PDCA supports continuous improvement, it is a formal process framework, not a cultural philosophy of daily incremental gains by all team members.
- **Why D is incorrect:** Total Quality Management (TQM) is an enterprise-wide commitment to quality culture. While it shares Kaizen's organization-wide participation emphasis, TQM is a broader management system. The scenario specifically describes incremental daily team-level improvements, which is the core definition of Kaizen.

---

## Question 8

Which of the following correctly sequences the three quality management processes in the order they occur within the project lifecycle?

- A) Control Quality → Manage Quality → Plan Quality Management
- B) Manage Quality → Plan Quality Management → Control Quality
- C) Plan Quality Management → Control Quality → Manage Quality
- D) Plan Quality Management → Manage Quality → Control Quality

**Correct Answer: D**

Quality Planning (Plan Quality Management) occurs during Planning. Quality Assurance (Manage Quality) occurs during Executing. Quality Control (Control Quality) occurs during Monitoring and Controlling. The processes follow the standard project process group sequence.

Distractor Analysis:

- **Why D is correct:** The three quality processes follow the same sequence as the process groups they belong to: Plan (Planning) → Manage/QA (Executing) → Control/QC (Monitoring and Controlling). Standards are defined first, processes are audited second, deliverables are inspected third.
- **Why A is incorrect:** This reverses the entire sequence. Control Quality cannot precede Manage Quality because QC inspects deliverables that are produced during execution, which is governed by QA. And neither can precede planning.
- **Why B is incorrect:** Manage Quality (Executing) cannot precede Plan Quality Management (Planning). You cannot audit the processes before defining what those processes should be in the Quality Management Plan.
- **Why C is incorrect:** This places Control Quality (Monitoring and Controlling) before Manage Quality (Executing), which is reversed. Deliverables are produced during execution (governed by QA) before they can be inspected during monitoring and control (QC).

---

## Question 9

A company invests $80,000 in developer quality training, automated testing tools, and documented code standards. As a result, post-deployment defect rates drop by 60%, reducing customer support costs from $200,000 to $80,000 annually. How should the $80,000 investment be classified, and what does this scenario illustrate about the Cost of Quality?

- A) The $80,000 is an external failure cost; the scenario shows that failure costs are always unavoidable
- B) The $80,000 is a prevention cost; the scenario illustrates that prevention investment reduces external failure costs
- C) The $80,000 is an appraisal cost; the scenario shows that testing always reduces defect rates
- D) The $80,000 is an internal failure cost; the scenario shows that rework reduces future defects

**Correct Answer: B**

Training, automated testing tools, and code standards are prevention-category investments — money spent to prevent defects from occurring. The reduction in customer support costs demonstrates that prevention investment directly reduces external failure costs, which is the foundational principle of the Cost of Quality framework.

Distractor Analysis:

- **Why B is correct:** Prevention costs include training programs, process design, quality planning, and standards development. All three items in the scenario (training, automated testing tools designed to catch errors before they occur, code standards) are prevention investments. The outcome — reduced external failure costs — demonstrates the ROI of prevention spending.
- **Why A is incorrect:** External failure costs are costs incurred when defects reach the customer — the $200,000 in support costs is the external failure cost, not the $80,000 investment. Training and tools that prevent defects are prevention costs by definition.
- **Why C is incorrect:** Appraisal costs involve evaluating completed deliverables — testing finished code, conducting inspections, performing audits. While automated testing has an appraisal component, the training and code standards elements are prevention. The scenario emphasizes proactive defect prevention, not evaluation of completed outputs.
- **Why D is incorrect:** Internal failure costs are incurred when defects are found before delivery — rework, debugging, re-testing. The scenario describes an investment made before work begins to prevent defects, not a cost incurred after defects are found internally.

---

## Question 10

A project manager reviews the Quality Management Plan and notices it was created during planning but has not been updated in six months. The project has since added three new integration components and changed vendors twice. Which quality management principle does failing to update the plan violate?

- A) The plan is a baseline document and should never be changed once approved
- B) The Quality Management Plan must remain current and reflect the actual project conditions throughout the project lifecycle
- C) Updating the plan requires sponsor approval and is rarely necessary
- D) Quality management plans apply only to the original project scope and do not need to update for scope changes

**Correct Answer: B**

The Quality Management Plan is a living subsidiary plan that must be updated to reflect changes in project scope, technology, vendors, and processes. A six-month-old plan that does not account for new integrations and vendor changes provides no valid quality governance for the current project state.

Distractor Analysis:

- **Why B is correct:** Project management plans are baselines, but baselines are subject to change control. When scope, technology, or vendor relationships change, the quality standards, metrics, and processes must be re-evaluated and updated to remain relevant. An outdated plan provides false assurance and may miss quality requirements for new components.
- **Why A is incorrect:** Baselines are approved reference points, not frozen documents. The integrated change control process exists specifically to allow controlled updates to project plans when circumstances change. A plan that cannot be updated is not a tool — it is a liability.
- **Why C is incorrect:** Some Quality Management Plan updates do require sponsor awareness or approval (particularly changes to quality standards or significant resource additions). But the requirement is to keep the plan current — the statement that updates are "rarely necessary" directly contradicts quality management principles.
- **Why D is incorrect:** New integration components and new vendors introduce new quality requirements, new acceptance criteria, and new failure modes. Quality management explicitly applies to all project scope, including scope additions. Excluding new scope from the quality plan is a process failure.
