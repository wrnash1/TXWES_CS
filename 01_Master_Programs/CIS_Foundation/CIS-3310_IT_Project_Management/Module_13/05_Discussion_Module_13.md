# Discussion Forum: Module 13 — Quality Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Overview

Choose one of the three scenarios below (A, B, or C). Write an initial post responding to all three sub-questions for your chosen scenario in complete sentences. Then reply to at least two classmates who chose different scenarios.

---

## Scenario A — The Team That Skipped QA

A regional insurance company launched an 18-month policy administration system replacement project. The project manager, under pressure to demonstrate rapid progress, cut the Quality Assurance process entirely from the execution phase, reasoning that the development team was experienced and the testing phase (Quality Control) would catch any problems before delivery. The development team never received a formal process audit. No one verified whether developers were following the defined code review procedure or the change logging process. At the conclusion of the development phase, the QC testing team ran a full regression suite and found 847 defects — an unusually high number. An audit conducted post-testing revealed that 61% of defects were traceable to developers skipping the peer code review procedure that had been defined in the Quality Management Plan.

Sub-questions for Scenario A:

1. Explain precisely why eliminating QA while keeping QC is a flawed quality strategy. What is the specific purpose of QA that QC cannot replace? Use the process group classification of each activity in your answer.
2. Apply the Rule of Ten to this scenario. The code review procedure, if followed, would have caught defects during development. Instead, they were found during testing (QC). Estimate the relative cost difference between catching a defect during peer review versus catching it during QC testing, and explain how this cost difference compounds when defects reach production.
3. Design a corrective QA plan for the remaining project phases. Describe at least two specific QA activities the PM should implement immediately, identify which process group they belong to, and explain how each activity would reduce the risk of additional defects reaching QC.

Your initial post should be 175–225 words and address all three sub-questions in complete sentences.

---

## Scenario B — The Defect That Was Always There

A logistics company deployed a new transportation management system (TMS) to 12 distribution centers. Over the first 90 days post-deployment, the help desk received 1,240 tickets related to route optimization errors. An Ishikawa analysis conducted by the quality team identified the following root causes: the routing algorithm was calibrated for a highway network that had been updated six months prior and never re-synced; the testing environment did not replicate the actual production data volume; and the user acceptance testing team had not included any drivers or dispatchers who use the system daily. The system passed all formal QC inspections before deployment.

Sub-questions for Scenario B:

1. The system passed formal QC inspections yet failed in production. What does this reveal about the limitations of Quality Control as a standalone quality strategy? Which of the three root causes identified in the Ishikawa analysis was most preventable through better Quality Assurance during execution, and why?
2. Conduct a basic Pareto-style analysis of the three root causes. If the route calibration error accounts for 65% of the 1,240 tickets, the testing environment gap accounts for 25%, and the UAT team composition gap accounts for 10%, which cause should receive the most immediate improvement resources and what specific action should be taken?
3. Using the PDCA cycle, design an improvement initiative specifically for the root cause you identified in sub-question 2. Describe what happens at each of the four PDCA steps — Plan, Do, Check, and Act — for that specific improvement initiative.

Your initial post should be 175–225 words and address all three sub-questions in complete sentences.

---

## Scenario C — Quality vs. Speed

A financial technology startup is developing a payment processing platform. The CTO sets a "quality is everyone's job" culture and invests heavily in developer training, automated testing infrastructure, pair programming, and documented coding standards. The total investment in these quality prevention activities is $320,000 — approximately 18% of the project budget. The VP of Engineering pushes back, arguing that this is excessive spending on processes that slow delivery and that "we should just test more at the end." The PM must make the case to leadership for the current quality investment approach.

Sub-questions for Scenario C:

1. Using the Cost of Quality framework, construct the argument in favor of the $320,000 prevention investment. Classify the investment by cost category, identify what categories of costs it is designed to reduce, and explain the economic logic connecting prevention spending to reduced total quality cost. Use specific cost category names from the reading guide.
2. The VP suggests increasing end-of-cycle testing instead. Classify this suggestion by Cost of Quality category and explain why shifting quality spending from prevention to appraisal — while reducing neither internal nor external failure costs — typically results in higher total quality cost, not lower.
3. A payment processing platform has a zero-tolerance risk profile for post-deployment defects because financial errors directly harm customers and trigger regulatory consequences. How does this risk profile strengthen the case for prevention-heavy quality investment? Connect your answer to the Rule of Ten and the relative cost of external failure in a regulated financial services environment.

Your initial post should be 175–225 words and address all three sub-questions in complete sentences.

---

## Participation Requirements

- Initial Post: Due Wednesday at 11:59 PM
- Peer Responses: Due Sunday at 11:59 PM — respond to at least two classmates who chose different scenarios

Strong peer responses apply a specific quality concept not addressed in the original post — such as control chart interpretation, the Kaizen vs. Six Sigma distinction, a specific Cost of Quality calculation, or the PDCA cycle applied to a different root cause. Peer responses must be at least 60 words each.

---

## Discussion Rubric — 10 Points Total

### Initial Post — 6 Points

- 5–6 pts: All three sub-questions addressed accurately using quality management terminology from the module. Post is 175–225 words. Analysis connects concepts (QA/QC, Cost of Quality, PDCA, Pareto) to specific scenario facts rather than restating definitions.
- 3–4 pts: Most sub-questions addressed but with terminology errors, missing process group placements, or generic answers that could apply to any scenario.
- 0–2 pts: Post missing, substantially incomplete, or demonstrates misunderstanding of QA vs. QC, quality tools, or Cost of Quality concepts.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies to classmates on different scenarios. Each reply extends the quality analysis with an additional concept — cost calculation, alternative root cause, control chart interpretation, or PDCA application — not addressed in the original post. Minimum 60 words each.
- 2 pts: One qualifying peer response, or both are surface-level ("great analysis, I agree").
- 0 pts: No peer responses submitted by Sunday at 11:59 PM.

---

## Professor Nash's Note

Quality management is the discipline that sits at the intersection of engineering, economics, and culture. The tools in this module — Ishikawa diagrams, Pareto charts, control charts, PDCA — are well over fifty years old and are still in daily use in IT organizations because they work. They work because they force precision about two things that humans naturally avoid: identifying the actual root cause of a problem rather than the most convenient cause, and allocating limited improvement resources to the problems that matter most rather than the ones that are most visible. If you take one principle from this module into your career, let it be this: invest in prevention early, measure continuously, and fix the vital few first. Everything else follows from those three habits.
