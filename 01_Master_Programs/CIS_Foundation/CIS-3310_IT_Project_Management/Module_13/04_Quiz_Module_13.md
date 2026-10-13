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

---

## Question 11

Which quality framework uses the DMAIC cycle (Define, Measure, Analyze, Improve, Control)?

- A) PDCA (Plan-Do-Check-Act)
- B) ISO 9001
- C) Six Sigma
- D) Kaizen

**Correct Answer:** C) Six Sigma

**Distractor Analysis:**

- *Why C is correct:* DMAIC is the core improvement methodology of Six Sigma. It is a data-driven, structured approach to eliminating defects: Define the problem, Measure current performance, Analyze root causes, Improve the process, and Control to sustain gains.
- *Why A is incorrect:* PDCA is Deming's Plan-Do-Check-Act cycle — a four-step continuous improvement model. It predates Six Sigma and is a separate framework.
- *Why B is incorrect:* ISO 9001 is an international quality management system standard focused on documentation, process consistency, and customer satisfaction — not specifically associated with DMAIC.
- *Why D is incorrect:* Kaizen is a Japanese philosophy of continuous, incremental improvement often implemented through small team activities. It does not use the DMAIC structure.

---

## Question 12

What does a Fishbone (Ishikawa) Diagram help a quality team accomplish?

- A) Track defect frequency over time to identify statistical trends
- B) Identify and organize the potential root causes of a specific quality problem into categories
- C) Display the cumulative percentage of defects by category to prioritize improvement
- D) Monitor a process variable against statistical control limits to detect special cause variation

**Correct Answer:** B) Identify and organize the potential root causes of a specific quality problem into categories.

**Distractor Analysis:**

- *Why B is correct:* The Fishbone (Ishikawa or cause-and-effect) diagram is a brainstorming and visual organization tool. The team places the problem at the "head" and organizes potential causes into branches (e.g., People, Process, Technology, Environment) to systematically identify root causes.
- *Why A is incorrect:* Tracking defect frequency over time describes a Run Chart or Control Chart — tools that monitor process performance, not root cause analysis tools.
- *Why C is incorrect:* Displaying cumulative defect percentages describes a Pareto Chart — the prioritization tool based on the 80/20 principle.
- *Why D is incorrect:* Monitoring a process variable against control limits describes a Control Chart — the statistical process control tool.

---

## Question 13

The four steps of the PDCA (Deming) cycle in correct order are:

- A) Plan → Do → Control → Act
- B) Plan → Do → Check → Act
- C) Define → Do → Check → Adjust
- D) Plan → Deliver → Check → Adjust

**Correct Answer:** B) Plan → Do → Check → Act

**Distractor Analysis:**

- *Why B is correct:* PDCA stands for Plan (establish objectives and processes), Do (implement on a small scale), Check (evaluate results against the plan), Act (standardize successful changes or return to Plan if unsuccessful). This is the correct four-step sequence.
- *Why A is incorrect:* "Control" is the fourth step of DMAIC (Six Sigma), not PDCA. The fourth PDCA step is "Act."
- *Why C is incorrect:* "Define" is the first step of DMAIC. PDCA begins with "Plan." The last step is also "Act," not "Adjust."
- *Why D is incorrect:* "Deliver" and "Adjust" are not PDCA steps. This is a fabricated distractor.

---

## Question 14

A quality manager is analyzing defect data and finds that out of 500 total defects, the top three categories account for 420 defects. What does this tell the team, and what should they do?

- A) The data is invalid — 80% of defects should always come from exactly 20% of categories.
- B) The top three categories (84% of defects) are the "vital few" — the team should focus quality improvement resources on these categories first.
- C) All five categories should be addressed simultaneously since the total defect count is too high.
- D) The bottom categories should be fixed first because they are easier to address quickly.

**Correct Answer:** B) The top three categories (84% of defects) are the "vital few" — the team should focus quality improvement resources on these categories first.

**Distractor Analysis:**

- *Why B is correct:* 420/500 = 84%. The Pareto principle guides the team to address the highest-frequency categories first. Even though 84% slightly exceeds the classic "80%" threshold, the principle still holds: concentrate limited improvement resources on the categories causing the most harm.
- *Why A is incorrect:* The 80/20 rule is a guideline, not a mathematical law that always produces exactly 80%. Real-world data varies. The principle is about concentrating effort on the dominant causes.
- *Why C is incorrect:* Simultaneously addressing all categories spreads resources too thin and produces less improvement per dollar invested. Pareto-based prioritization is more efficient.
- *Why D is incorrect:* Fixing the easiest categories first (regardless of impact) is an effort-optimization strategy, not a quality improvement strategy. The Pareto principle prioritizes by impact magnitude, not by implementation difficulty.

---

## Question 15

What is Kaizen, and how does it differ from Six Sigma?

- A) Kaizen is a statistical defect elimination methodology; Six Sigma is a continuous improvement philosophy.
- B) Kaizen emphasizes small, incremental, continuous improvements made by all employees; Six Sigma uses a structured data-driven methodology (DMAIC) focused on reducing defect rates to near zero.
- C) They are identical methodologies with different names used in different countries.
- D) Kaizen uses DMAIC; Six Sigma uses PDCA.

**Correct Answer:** B) Kaizen emphasizes small, incremental, continuous improvements made by all employees; Six Sigma uses a structured data-driven methodology (DMAIC) focused on reducing defect rates to near zero.

**Distractor Analysis:**

- *Why B is correct:* Kaizen (Japanese for "change for better") is a philosophy of ongoing improvement through small, daily changes at every level of the organization. Six Sigma is a more formal, statistical methodology targeting near-zero defects (3.4 defects per million opportunities) using the DMAIC cycle.
- *Why A is incorrect:* The descriptions are reversed. Kaizen is the continuous improvement philosophy; Six Sigma is the statistical methodology.
- *Why C is incorrect:* They are distinct methodologies with different origins, tools, and application scopes. They can be used together (Lean Six Sigma) but are not identical.
- *Why D is incorrect:* Kaizen does not use DMAIC (that is Six Sigma's method). Six Sigma does not use PDCA as its core cycle (though PDCA influenced quality thinking generally).

---

## Question 16

A control chart for a software build process shows 8 consecutive data points below the center line, all within the UCL/LCL boundaries. What should the quality manager conclude?

- A) The process is in control because no points exceed the control limits.
- B) The process shows a non-random pattern (Rule of Seven violation) suggesting a systematic shift that should be investigated even though limits were not breached.
- C) Eight points below the mean is normal statistical variation and requires no action.
- D) The process can be improved by raising the UCL to accommodate the lower data points.

**Correct Answer:** B) The process shows a non-random pattern (Rule of Seven violation) suggesting a systematic shift that should be investigated even though limits were not breached.

**Distractor Analysis:**

- *Why B is correct:* The Rule of Seven states that seven or more consecutive points on the same side of the mean signals a non-random shift. Eight consecutive points below the mean exceeds this threshold — it indicates the process has systematically changed (improved or degraded) and investigation is warranted.
- *Why A is incorrect:* Being within control limits is necessary but not sufficient to conclude a process is in control. The Rule of Seven detects systematic patterns that control limits alone cannot catch.
- *Why C is incorrect:* Eight consecutive points on one side of the mean is not normal variation. In a truly random process, the probability of this occurring by chance is extremely low — it signals something systematic.
- *Why D is incorrect:* Adjusting the UCL to accommodate data patterns defeats the purpose of statistical process control. Control limits are calculated from process data, not adjusted to match desired outcomes.

---

## Question 17

Which of the following BEST describes the purpose of Quality Assurance (QA) in the PDCA cycle?

- A) QA occurs in the "Check" step — it evaluates completed deliverables for defects.
- B) QA occurs primarily in the "Plan" and "Do" steps — it designs processes and audits process adherence to prevent defects.
- C) QA replaces the "Act" step by documenting all improvements for future reference.
- D) QA is not part of PDCA — it is exclusive to Six Sigma.

**Correct Answer:** B) QA occurs primarily in the "Plan" and "Do" steps — it designs processes and audits process adherence to prevent defects.

**Distractor Analysis:**

- *Why B is correct:* QA is proactive and process-oriented. In PDCA terms, QA contributes to Plan (designing quality processes and standards) and Do (auditing that processes are being followed correctly). Its goal is to prevent defects before deliverables are produced.
- *Why A is incorrect:* Evaluating completed deliverables for defects describes Quality Control (QC), not QA. QC fits in the Check step. QA is upstream, process-focused work.
- *Why C is incorrect:* The Act step involves standardizing successful improvements or re-looping. QA does not replace it — it contributes to the entire cycle through process governance.
- *Why D is incorrect:* QA is a universal quality management concept applicable to PDCA, Six Sigma, ISO, and all other quality frameworks. It is not exclusive to Six Sigma.

---

## Question 18

A project team is performing root cause analysis on a recurring server timeout issue. They use a Fishbone diagram and identify that the timeout occurs because of insufficient memory allocation in the application server configuration. What should the team do NEXT in the quality improvement process?

- A) Close the issue and report it as resolved since the root cause is identified.
- B) Develop a corrective action to increase the memory allocation, implement it, and monitor the results.
- C) Add the issue to the Risk Register as a new threat.
- D) Escalate to the project sponsor before taking any action on the server configuration.

**Correct Answer:** B) Develop a corrective action to increase the memory allocation, implement it, and monitor the results.

**Distractor Analysis:**

- *Why B is correct:* Root cause identification is a diagnosis step — it does not resolve the problem. The team must implement a corrective action (the fix), verify it resolves the issue, and monitor to confirm the improvement holds. This follows the PDCA Do → Check → Act sequence.
- *Why A is incorrect:* Identifying the root cause is not the same as resolving it. Closing the issue before implementing a fix leaves the defect in place.
- *Why C is incorrect:* An ongoing performance issue being actively diagnosed and corrected is not a new risk — it is a current problem. Adding it to the Risk Register at this point confuses issue management with risk management.
- *Why D is incorrect:* A server configuration adjustment is an operational fix within the team's authority. Escalating a routine technical correction to the sponsor is unnecessary overhead and delays resolution.

---

## Question 19

How does the "Act" step of the PDCA cycle differ from simply completing a task?

- A) The Act step involves assigning new tasks to team members for the next cycle.
- B) The Act step involves standardizing the successful change across the organization or returning to Plan to address remaining issues — ensuring the improvement is embedded, not just completed once.
- C) The Act step requires sponsor approval before any changes can be finalized.
- D) The Act step closes the quality process permanently and documents findings in the Risk Register.

**Correct Answer:** B) The Act step involves standardizing the successful change across the organization or returning to Plan to address remaining issues — ensuring the improvement is embedded, not just completed once.

**Distractor Analysis:**

- *Why B is correct:* Act is the institutionalization step. If the Do step produced a successful improvement (confirmed in Check), Act means embedding the new process as the standard so it persists. If the improvement was insufficient, Act means looping back to Plan with new information. Either way, the cycle continues — quality improvement is never "done."
- *Why A is incorrect:* Assigning new tasks is an operational activity, not the PDCA Act step. Act is about systemic standardization, not task assignment.
- *Why C is incorrect:* Sponsor approval may be needed for significant changes to baselines, but the Act step as defined in PDCA is about standardizing or re-planning — not a governance approval gate.
- *Why D is incorrect:* PDCA is cyclical, not terminal. Closing the process permanently contradicts the continuous improvement philosophy. The Risk Register is not a PDCA artifact.

---

## Question 20

A project manager notices that defect rates increased after a new developer joined the team. A Fishbone diagram analysis identifies inadequate onboarding and coding standard training as root causes. Which Cost of Quality category should the project invest in to prevent recurrence?

- A) External failure costs — reimburse customers for the defects
- B) Internal failure costs — increase the budget for rework
- C) Prevention costs — develop a formal onboarding and coding standards training program for new team members
- D) Appraisal costs — add more code review cycles to catch defects earlier

**Correct Answer:** C) Prevention costs — develop a formal onboarding and coding standards training program for new team members.

**Distractor Analysis:**

- *Why C is correct:* The root cause is inadequate training — a process gap that produces defects before they happen. The most cost-effective and targeted response is prevention investment: designing a formal onboarding program that ensures new developers understand and apply the required standards from day one.
- *Why A is incorrect:* External failure costs are incurred when defects reach customers. Reimbursing customers is reactive and expensive — not a quality improvement investment.
- *Why B is incorrect:* Increasing the rework budget accepts the defects and funds their correction — this is internal failure cost spending. It does not prevent the problem; it funds dealing with it after the fact.
- *Why D is incorrect:* Adding code review cycles increases appraisal costs — these catch defects earlier but do not prevent them. The root cause is training, not insufficient review. More reviews without fixing the training gap means reviewing the same categories of errors indefinitely.
