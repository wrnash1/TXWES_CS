# Lab Activity: Module 07 - Process Modeling with BPMN

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University
**Total Points:** 100

---

## Overview

This lab gives you hands-on practice modeling a business process using BPMN. You will analyze a case study, draw an as-is process model, identify inefficiencies, and draw an improved to-be process model. You will also answer analysis questions about gateway selection and modeling rules. No software installation or terminal commands are required. You may use any diagramming tool (draw.io, Lucidchart, PowerPoint, or hand-drawn and photographed).

---

## Case Study: Brightwood Insurance — Claims Processing

Brightwood Insurance processes auto insurance claims submitted by policyholders. A BA has observed the current process and documented the following steps:

- A policyholder calls the claims hotline and a claims agent takes the initial report by phone, manually recording it on paper.
- The agent creates a claim record in the system and mails a paper claim form to the policyholder.
- The policyholder completes the paper form and mails it back. The agent waits for the form to arrive (average wait: 5 business days).
- When the form arrives, the agent scans it and enters the data into the system.
- The agent assigns an adjuster to the claim. The adjuster reviews the claim and decides whether to approve or deny it.
- If approved, the agent calculates the payment amount and sends it to a supervisor for a second review and approval.
- The supervisor approves the payment. The agent processes the payment and mails a check to the policyholder.
- If denied, the agent mails a denial letter to the policyholder.
- The policyholder can appeal a denial. If an appeal is received, a senior adjuster reviews it and either overturns (approve) or upholds (deny) the original decision.

Brightwood is building a new digital claims portal to improve this process. The future-state process should allow policyholders to submit claims online, eliminate the paper form, allow photo uploads for damage documentation, run initial eligibility checks automatically, and reduce the supervisor approval threshold to claims over $5,000 only.

---

## Part 1: As-Is BPMN Process Model — 35 Points

### Part 1 Instructions

Draw an as-is (current-state) BPMN process model for the Brightwood Insurance claims processing case study.

Your diagram must include:

- At least two pools (Policyholder and Brightwood Insurance)
- Lanes within the Brightwood Insurance pool for at least two roles (Claims Agent and Adjuster, at minimum)
- All activities from the as-is process, labeled with descriptive task names
- At least one Exclusive Gateway modeling a decision point (approved vs. denied)
- Correct sequence flow within each pool (solid arrows)
- Correct message flow between pools (dashed arrows with open arrowheads)
- Start Event and End Event(s) in the appropriate pool(s)

### Grading Rubric — Part 1

| Criterion | Points |
|---|---|
| At least two pools correctly labeled | 4 |
| At least two lanes within Brightwood pool with role names | 4 |
| All major as-is activities present and labeled | 10 |
| At least one Exclusive Gateway with correct notation and labeled branches | 6 |
| Sequence flow stays within pools; message flow crosses pools correctly | 7 |
| Start and End Events present and correctly typed | 4 |

Part 1 Total: 35 points

---

## Part 2: As-Is Process Analysis — 20 Points

### Part 2 Instructions

After drawing your as-is BPMN model, answer the following questions in complete sentences. Each answer should be 3–5 sentences.

Question 1: Identify at least three specific inefficiencies visible in the as-is process. For each inefficiency, name the activity or handoff where it occurs and explain why it is a problem.

Question 2: The current process requires supervisor approval for every payment regardless of amount. Identify which BPMN gateway type you would use in the to-be model to route high-value claims (over $5,000) through supervisor approval and route low-value claims directly to payment. Explain why this gateway type is correct for this decision.

Question 3: The appeal subprocess (reviewing a denied claim) is a compound activity with its own internal steps. Identify which BPMN symbol you would use to represent the appeal process in the top-level diagram without showing all its internal steps. Explain what that symbol communicates to a reader.

### Grading Rubric — Part 2

| Criterion | Points |
|---|---|
| Question 1: Three specific inefficiencies identified with activities named (7 pts) | 7 |
| Question 2: Correct gateway type identified with justification (7 pts) | 7 |
| Question 3: Correct BPMN symbol identified with explanation (6 pts) | 6 |

Part 2 Total: 20 points

---

## Part 3: To-Be BPMN Process Model — 30 Points

### Part 3 Instructions

Draw a to-be (future-state) BPMN process model incorporating the improvements described in the case study.

Your to-be diagram must include:

- The same pool structure as Part 1 (Policyholder, Brightwood Insurance with lanes)
- A digital submission path replacing the paper form process
- An Exclusive Gateway routing claims over $5,000 to supervisor approval and claims $5,000 or under directly to payment processing
- A Service Task (marked with a gear icon) representing the automated eligibility check
- Correct message flow for the online claim submission from Policyholder to Brightwood Insurance
- At least one Intermediate Event representing the claim acknowledgment sent to the policyholder after submission
- Start Event and End Event(s) in the appropriate pool(s)

### Grading Rubric — Part 3

| Criterion | Points |
|---|---|
| Digital submission path replaces paper form process | 6 |
| Exclusive Gateway correctly models the $5,000 threshold decision with labeled branches | 8 |
| Service Task with gear icon represents automated eligibility check | 4 |
| Intermediate Event represents claim acknowledgment | 4 |
| Correct sequence flow and message flow placement | 5 |
| Start and End Events present | 3 |

Part 3 Total: 30 points

---

## Part 4: Reflection — 15 Points

### Part 4 Instructions

Write a reflection of 150–200 words comparing your as-is and to-be models. Your reflection must address all three of the following:

1. Identify the most significant efficiency gain achieved in the to-be model and explain why it matters to the business.
2. Identify one risk or challenge the to-be process introduces that the as-is process did not have, and describe how a BA might mitigate it.
3. Explain how BPMN — specifically its use of pools, lanes, and gateways — made it easier to identify and communicate the process changes compared to a plain narrative description.

### Grading Rubric — Part 4

| Criterion | Points |
|---|---|
| Significant efficiency gain identified with business impact explained | 5 |
| Risk or challenge identified with mitigation approach described | 5 |
| BPMN's value as a communication tool explained with specific references to diagram elements | 5 |

Part 4 Total: 15 points

---

## Submission Instructions

Combine all four parts into one document with clearly labeled sections. For diagram parts, embed the diagram image or include a link to the shared diagram file. For written parts, type your responses directly in the document. Submit to the Canvas Module 07 Lab assignment by the due date shown in the course calendar.
