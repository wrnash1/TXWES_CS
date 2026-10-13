# Video Script: Module 13 — Quality Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Production Notes

- Slides: Ishikawa diagram built progressively on screen; Pareto chart animated with cumulative percentage line
- Graphics: QA vs. QC comparison visual; process improvement cycle (PDCA)
- Tone: Practical and process-oriented — connect diagrams to real IT defect scenarios
- Screen segment: Walk through a simple Pareto chart construction in a spreadsheet

---

## Segment 1 — Introduction: Quality Is Not Testing (0:00–2:30)

[SHOW SLIDE: Title — "Module 13: Quality Management"]

Welcome back to CIS-3310. I'm Professor Nash. Module 13 is Quality Management, and I want to start with a statement that surprises most students: quality management is not the same as testing.

[PAUSE — 2 seconds]

Testing is one small component of quality management. Quality management is the entire system by which a project defines what quality means, builds processes to achieve it, monitors whether those processes are working, and improves continuously. It starts in planning and runs all the way through project closure.

[SHOW SLIDE: "The Cost of Poor Quality"]

Here is a practical way to think about why quality management matters. The cost of fixing a defect increases by a factor of ten for every phase it passes through undetected. A defect found during requirements costs $1 to fix. The same defect found during testing costs $10. Found during integration testing: $100. Found by the customer after delivery: $1,000 or more — and that does not count the reputational damage.

[PAUSE — 2 seconds]

This is called the Rule of Ten, and it is the fundamental economic argument for investing in quality early rather than catching defects late. Quality management is ultimately a cost-management strategy.

[SHOW SLIDE: "Quality Management Process Overview"]

The quality management process has three components: Plan Quality Management (planning), Manage Quality — also called Quality Assurance (executing), and Control Quality (monitoring and controlling). We will work through all three today, and then spend significant time on the tools: Ishikawa diagrams, Pareto charts, control charts, and the PDCA improvement cycle.

---

## Segment 2 — Quality Planning (2:30–6:00)

[SHOW SLIDE: "Plan Quality Management"]

Quality planning is the process of identifying quality standards that are relevant to the project and documenting how the project will satisfy those standards. The output is the Quality Management Plan.

[PAUSE — 2 seconds]

The Quality Management Plan defines: quality standards (what does quality mean for this deliverable?), quality metrics (how will quality be measured?), quality processes (what procedures will be followed?), QA and QC activities, and tools and techniques to be used. It also defines the quality baseline — the acceptable performance targets against which actual results will be compared.

[SHOW SLIDE: "Defining Quality — Fitness for Use"]

Quality in project management has a specific definition: conformance to requirements and fitness for use. Conformance to requirements means the deliverable meets its specifications. Fitness for use means it actually satisfies the customer's need.

[PAUSE — 2 seconds]

These two dimensions can diverge. A software system that perfectly meets every written requirement but crashes whenever two users access it simultaneously does not meet the customer's need. Writing better requirements is part of quality planning — not just testing.

[SHOW SLIDE: "Cost of Quality — Four Categories"]

The Cost of Quality framework breaks quality-related spending into four categories. You need these for the Project+ exam.

Prevention costs: money spent to prevent defects from occurring in the first place. Training, process design, quality planning, code reviews. Investing here reduces total quality cost.

Appraisal costs: money spent to evaluate whether quality standards are being met. Testing, inspections, audits, peer reviews. This is quality checking.

Internal failure costs: costs of defects found before delivery — rework, scrap, debugging. Higher than prevention costs but lower than external failure.

External failure costs: costs of defects found after delivery to the customer — warranty repairs, customer support, system rollbacks, reputation damage. The most expensive category.

[PAUSE — 2 seconds]

The key principle: money spent on prevention is always cheaper than money spent on external failure. Prevention reduces appraisal costs, which reduces internal failure costs, which eliminates external failure costs. The Cost of Quality framework gives organizations a way to analyze whether their quality investment allocation makes sense.

---

## Segment 3 — Quality Assurance vs. Quality Control (6:00–10:00)

[SHOW SLIDE: "QA vs. QC — The Most Tested Quality Distinction"]

The distinction between Quality Assurance and Quality Control is one of the most frequently tested concepts on the Project+ exam. Let me give you the clearest possible definition of each.

[PAUSE — 2 seconds]

Quality Assurance, or QA, is process-focused. It asks: Are we following the right processes to produce quality outcomes? QA evaluates the processes and practices used to develop deliverables. It is proactive. It happens during execution. A QA activity might be an audit of whether the development team is following the peer review process that was defined in the Quality Management Plan.

[SHOW SLIDE: "Quality Assurance — Process Audits"]

QA is performed by the project team or a quality audit function. Its goal is process improvement — finding weaknesses in how work is being done so processes can be corrected before defects occur. QA does not examine deliverables directly; it examines the processes that create deliverables.

[PAUSE — 2 seconds]

If QA discovers that the team has been skipping the required code review step, the team should immediately reinstitute the review process before the next development sprint. QA is prescriptive — it tells you how work should be done.

[SHOW SLIDE: "Quality Control — Deliverable Inspection"]

Quality Control, or QC, is product-focused. It asks: Does this specific deliverable meet quality standards? QC inspects, tests, and measures actual outputs to determine whether they conform to specifications.

[PAUSE — 2 seconds]

QC is reactive — it occurs after a deliverable has been produced. A QC activity might be running a full regression test suite against a software build, inspecting a network configuration against a standards checklist, or reviewing a project document against acceptance criteria.

[SHOW SLIDE: "QA vs. QC Comparison Table"]

| Dimension | Quality Assurance (QA) | Quality Control (QC) |
|-----------|----------------------|---------------------|
| Focus | Process | Product/Deliverable |
| Timing | During execution (proactive) | After production (reactive) |
| Question | Are we doing it right? | Did we do it right? |
| Output | Process improvements | Defect findings, acceptance decisions |
| Tools | Audits, process checklists | Inspections, testing, Pareto charts |
| Process Group | Executing | Monitoring and Controlling |

[PAUSE — 3 seconds]

Memorize that table. The exam will present a scenario and ask whether QA or QC is being performed. If someone is checking a process or auditing a procedure, that is QA. If someone is inspecting, testing, or measuring a deliverable, that is QC.

---

## Segment 4 — Quality Tools: Ishikawa Diagrams (10:00–14:00)

[SHOW SLIDE: "Quality Tools — The Magnificent Seven"]

Quality management has a set of standard analytical tools often called the Seven Basic Quality Tools or the Seven QC Tools. Today we will focus on the two most tested on the Project+ exam: Ishikawa diagrams and Pareto charts. We will also touch on control charts.

[SHOW SLIDE: "Ishikawa Diagram — Also Called Fishbone or Cause-and-Effect"]

The Ishikawa diagram — also called a fishbone diagram because of its shape, or a cause-and-effect diagram — is a visual tool for identifying the root causes of a problem. It was developed by Dr. Kaoru Ishikawa and became a cornerstone of quality management in the 1960s.

[PAUSE — 2 seconds]

The structure is straightforward. The problem — also called the effect — is placed in a box on the right side. A horizontal arrow points to it. From that arrow, diagonal branches extend to represent major cause categories. From each category branch, smaller branches represent specific contributing causes.

[SHOW SLIDE: "Ishikawa — The 6M Categories for IT Projects"]

The most common cause categories for IT projects use the 6M framework: Methods, Machines (equipment/systems), Materials (data, documents), Measurement, Manpower (people/skills), and Mother Nature (environment). Some IT versions substitute Environment for Mother Nature and add Management as a seventh category.

[PAUSE — 2 seconds]

Example: The problem is "Production deployment failures occur 30% of the time." We build an Ishikawa diagram to find root causes. Under Methods, we might identify "no pre-deployment checklist." Under Machines, "test environment does not match production configuration." Under Manpower, "deployments performed by junior staff without oversight." Under Management, "no change freeze policy before major releases."

[SHOW SLIDE: "Why Ishikawa Is Powerful"]

The Ishikawa diagram forces systematic thinking about root causes rather than jumping to solutions. The most natural human response to a problem is to fix the most obvious symptom. The Ishikawa process slows that impulse and asks: what actually caused this? Fixing a symptom without addressing the root cause produces the same problem repeatedly.

[PAUSE — 2 seconds]

On the Project+ exam, Ishikawa diagram questions typically describe a team analyzing root causes of a recurring defect or failure. If the scenario involves identifying contributing causes categorized by process, people, equipment, and environment, the tool being described is an Ishikawa diagram.

---

## Segment 5 — Quality Tools: Pareto Charts and Control Charts (14:00–18:00)

[SHOW SLIDE: "Pareto Chart — The 80/20 Principle Made Visual"]

The Pareto chart is a bar chart combined with a cumulative line graph. It displays defect categories ranked from most frequent to least frequent, and shows the cumulative percentage of total defects. It is based on the Pareto principle — the observation that roughly 80% of problems come from 20% of causes.

[PAUSE — 2 seconds]

In quality management, the Pareto chart answers one critical question: where should we focus our improvement efforts to get the greatest reduction in defects? By ranking causes by frequency, it makes the answer visually obvious.

[SHOW SLIDE: "Reading a Pareto Chart"]

Here is how to read a Pareto chart. The left vertical axis shows the count or frequency of each defect type. The right vertical axis shows the cumulative percentage from 0% to 100%. The bars are arranged left to right from most frequent to least frequent. The cumulative line rises from left to right.

[PAUSE — 2 seconds]

The 80/20 rule tells you to look for the point where the cumulative line crosses 80%. The defect categories to the left of that point account for 80% of all defects. If you fix only those categories, you eliminate the majority of your quality problems. This is called Pareto analysis or vital few versus trivial many.

[SHOW SLIDE: "Pareto Example — Software Defect Analysis"]

Example: A software QA team logs 150 defects during testing. Analysis shows:

- Input validation errors: 62 defects (41%)
- Authentication failures: 38 defects (25%) — cumulative 66%
- API response errors: 22 defects (15%) — cumulative 81%
- UI rendering bugs: 15 defects (10%) — cumulative 91%
- Other: 13 defects (9%) — cumulative 100%

The 80% line is crossed after API response errors — the third bar. Fixing input validation, authentication, and API errors would eliminate 81% of all defects. That is where the team should concentrate resources.

[PAUSE — 2 seconds]

On the Project+ exam, Pareto chart questions typically describe a team needing to prioritize which defect types to address. If the scenario involves ranking problems by frequency to identify the vital few, the tool is a Pareto chart.

[SHOW SLIDE: "Control Charts — Monitoring Process Stability"]

A control chart tracks a quality metric over time to determine whether a process is in statistical control — operating within acceptable variation limits. The chart shows an upper control limit (UCL), a lower control limit (LCL), and a center line representing the process mean.

[PAUSE — 2 seconds]

A process is in control when data points fall within the control limits and show no patterns. Warning signs include: a data point outside the control limits (special cause variation), or seven consecutive points on one side of the center line (called the Rule of Seven — indicating a process shift even though individual points are within limits).

---

## Segment 6 — PDCA and Process Improvement (18:00–21:00)

[SHOW SLIDE: "The PDCA Cycle — Continuous Improvement"]

The foundation of all quality improvement frameworks is the PDCA cycle, also called the Deming Cycle or Shewhart Cycle. PDCA stands for Plan, Do, Check, Act.

[PAUSE — 2 seconds]

Plan: Identify the problem or improvement opportunity. Establish hypotheses about root causes. Design the change or solution.

Do: Implement the change on a small scale — a pilot or test environment.

Check: Evaluate the results of the pilot. Did the change produce the desired improvement? Use data to measure.

Act: If the check confirms improvement, standardize the change and implement broadly. If not, return to Plan and revise the hypothesis.

[SHOW SLIDE: "PDCA in IT Projects"]

In IT project quality management, PDCA operates at two levels. At the project level, it drives improvements to project processes — for example, improving the code review process based on defect data. At the product level, it drives improvements to the product being built — for example, iterating on a feature based on user testing results.

[PAUSE — 2 seconds]

The key characteristic of PDCA is that it is a cycle, not a one-time fix. After Act, you return to Plan for the next improvement cycle. Quality improvement is continuous — there is always a next opportunity to improve.

[SHOW SLIDE: "Continuous Improvement vs. Breakthrough Improvement"]

Two improvement philosophies appear on the Project+ exam. Kaizen is Japanese for "change for the better" and describes small, continuous incremental improvements made by everyone in the organization. Kaizen improvements accumulate over time.

Six Sigma is a data-driven methodology targeting defect reduction to fewer than 3.4 defects per million opportunities. Six Sigma uses a structured process called DMAIC: Define, Measure, Analyze, Improve, Control. Six Sigma is breakthrough improvement — targeted at eliminating specific defect causes with statistical precision.

---

## Segment 7 — Closing Summary (21:00–23:00)

[SHOW SLIDE: "Module 13 Key Takeaways"]

Quality management is a proactive discipline that begins in planning and runs through every phase of the project. The three components are Plan Quality Management (defining standards and metrics), Quality Assurance (process audits during execution), and Quality Control (deliverable inspection during monitoring and controlling).

[PAUSE — 2 seconds]

QA is process-focused and proactive. QC is product-focused and reactive. Ishikawa diagrams identify root causes. Pareto charts prioritize which causes to fix. Control charts monitor whether a process remains in statistical control. PDCA drives continuous improvement.

[PAUSE — 2 seconds]

The Cost of Quality principle is your economic anchor: prevention and appraisal costs are always cheaper than external failure costs. Invest in quality early.

[SHOW SLIDE: "Coming Up — Module 14"]

You have now completed four of the most heavily tested IT project management domains on the CompTIA Project+ exam. Module 14 continues the journey. Complete the quality tools lab, take the quiz, and post your discussion response before Wednesday.

Well done. I will see you in Module 14.

[SHOW SLIDE: End card — Texas Wesleyan University | CIS-3310 | Professor Nash]

---

*End of Module 13 Video Script*

*Total estimated runtime: 21–23 minutes*
