# Lab Activity: Module 05 — Service Value Chain Activities

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Total Points:** 100
**Certification Alignment:** ITIL 4 Foundation

---

## Overview

This lab requires you to map real organizational scenarios to Service Value Chain activities, design value streams, and analyze how practices connect to SVC activities. No software tools or terminal commands are required. All work is analytical and written.

Submit all exercises as a single document to the Canvas assignment portal by the posted deadline.

---

## Scenario: Northgate Community College IT Department

Northgate Community College has 8,500 enrolled students and 640 staff members. The IT department supports 23 services including the student information system, the learning management system (LMS), email, campus Wi-Fi, the library database system, and the classroom audiovisual infrastructure.

The IT director, Maria, is working to align the department with ITIL 4. She has asked you to help map the department's activities to the Service Value Chain.

---

## Exercise 1: SVC Activity Identification (25 points)

For each of the ten activities listed below, identify which of the six SVC activities it belongs to, name the activity, and write a one-sentence explanation of why that activity applies.

Activities to classify:

1. The IT helpdesk team responds to a student's report that the LMS is showing an error when submitting assignments.
2. The IT director meets with the Provost and academic department chairs to understand their technology needs for the coming academic year.
3. The IT team purchases and configures 12 new videoconferencing units for updated classrooms.
4. The IT department analyzes three months of incident data and identifies that 35% of incidents relate to a known VPN configuration issue that has not yet been permanently resolved.
5. IT leadership develops a three-year technology roadmap aligned to the college's strategic plan.
6. A development team builds a new mobile app for student ID card functions.
7. The IT team designs the architecture for a new identity and access management system, including the integration points with the student information system.
8. A student submits a request through the IT portal to have her email forwarded to an external address, and a technician processes the request.
9. The IT team reviews performance metrics from the past quarter and identifies that average incident resolution time has increased by 18%, then initiates an improvement project.
10. The IT director shares a service availability report with the Vice President of Academic Affairs, showing current uptime across all 23 services.

### Rubric — Exercise 1

| Score | Criteria |
|---|---|
| 23–25 | Nine or ten correctly identified with accurate, specific explanations |
| 18–22 | Seven or eight correctly identified; explanations present but one or two are vague |
| 12–17 | Five or six correctly identified; explanations incomplete for several |
| 0–11 | Fewer than five correctly identified; SVC framework not demonstrated |

---

## Exercise 2: Value Stream Design (30 points)

Design a complete value stream for each of the two scenarios below. For each scenario, list the SVC activities in order, describe what specifically happens in that activity within the Northgate context, and identify one practice that enables that activity.

Scenario A: A new student arrives on campus and needs her IT accounts created, her device registered on the campus network, and access to the LMS and student email provisioned.

Scenario B: The campus Wi-Fi network across the library building fails during finals week. Students and staff in the library lose connectivity. The service desk receives 40 calls in 20 minutes.

Your value streams must include at least four SVC activities each. Present each value stream as a numbered, sequential list with activity name, description of what happens, and practice identified.

### Rubric — Exercise 2

| Score | Criteria |
|---|---|
| 27–30 | Both value streams include four or more activities; each step clearly described in the Northgate context; practices correctly identified |
| 22–26 | Both value streams present; three or four activities each; most descriptions specific; most practices correct |
| 15–21 | One value stream fully developed; other is partial; some practices incorrect or missing |
| 0–14 | Only one value stream attempted; fewer than three activities; SVC framework not clearly applied |

---

## Exercise 3: Improve Activity Analysis (20 points)

Maria's team has collected the following data over the past quarter:

* Average incident resolution time: 4.2 hours (target: 2 hours)
* Percentage of incidents resolved at first contact: 31% (target: 65%)
* Top five incident categories: VPN connectivity (35%), LMS access errors (22%), email client configuration (18%), printer failures (14%), classroom AV failures (11%)
* Three major outages: LMS (4 hours), campus Wi-Fi zone 3 (6 hours), student information system (2 hours)
* Student satisfaction score for IT services: 3.1 out of 5.0

Write a structured analysis (minimum 175 words) addressing all three of the following:

1. What does the Improve activity do with this data? Describe specifically how the Improve activity processes this information and what outputs it should produce.
2. Identify two specific improvement initiatives that this data suggests. For each, identify which other SVC activity would need to be involved in implementing the improvement.
3. How does the Improve activity's relationship with all other SVC activities make it possible to address improvement across the entire SVC — not just in Deliver and Support, where most of these metrics originate?

### Rubric — Exercise 3

| Score | Criteria |
|---|---|
| 18–20 | All three questions answered with accurate SVC terminology; analysis is specific to the data provided |
| 14–17 | Two of three questions answered thoroughly; Improve's role mostly accurate |
| 10–13 | All three addressed but analysis is superficial; Improve's cross-SVC role not fully explained |
| 0–9 | Fewer than two questions adequately answered; Improve activity not understood |

---

## Exercise 4: Practice-to-Activity Mapping (25 points)

For each of the six practices listed below, identify which SVC activity it primarily enables, explain why in one to two sentences, and identify one secondary SVC activity it also contributes to with a one-sentence explanation.

Practices to map:

1. Incident Management
2. Service Level Management
3. Change Enablement
4. Knowledge Management
5. Deployment Management
6. Problem Management

### Rubric — Exercise 4

| Score | Criteria |
|---|---|
| 23–25 | All six practices correctly mapped to primary and secondary activities with accurate explanations |
| 18–22 | Five correctly mapped; secondary activity explanations present for most |
| 12–17 | Four correctly mapped; secondary activities partially correct; explanations thin |
| 0–11 | Fewer than four correctly mapped; practice-to-activity relationship not demonstrated |

---

## Submission Instructions

Compile all four exercises into a single document with clear headings. Label each numbered item before your response. Submit to the Module 05 Lab assignment in Canvas by the posted deadline.

---

## Part 9 — Challenge Exercise

### Challenge 1: Value Stream Redesign

A regional bank's IT department handles customer loan application processing through the following informal steps: (1) a banker emails the IT help desk requesting access to the loan origination system for a new hire, (2) an IT technician manually creates the account two to four days later, (3) no testing or confirmation is sent to the banker, (4) the new hire discovers the account has wrong permissions on their first day and calls the help desk again.

1. Map each of the four existing steps to the SVC activity it most closely represents (or note if a required SVC activity is missing).
2. Redesign this process as a formal value stream. List the SVC activities in the order you would include them and write one sentence for each explaining what work happens at that step in this specific context.
3. Identify two ITIL 4 practices that would provide the capability needed at two of the steps in your redesigned value stream.

### Challenge 2: Multi-Activity Scenario Analysis

Read the following scenario and answer the questions below.

Apex Logistics is launching a new real-time package tracking service. The project team has completed vendor selection (GPS tracking hardware and a cloud API provider), developed the mobile application, conducted load testing, and is preparing the go-live deployment. Two weeks post-launch, the operations team notices that GPS refresh rates are slower than the contracted 30-second interval during peak delivery hours. The team opens a formal improvement initiative to renegotiate the cloud API contract and optimize the data pipeline.

1. Identify all SVC activities that appear in this scenario and provide a one-sentence explanation of where each appears.
2. The post-launch GPS performance problem — which SVC activity is primarily responsible for detecting this issue, and which activity processes the formal improvement initiative?

### Reflection Questions

1. The Improve activity connects bidirectionally to all other SVC activities. Based on this module, explain in your own words why this architectural choice is more effective than placing improvement at the end of a linear service lifecycle (as ITIL v3's CSI phase did).
2. Consider a service you use frequently (a food delivery app, a campus IT system, an e-commerce site). Describe one improvement that the provider could make that would require all six SVC activities to be involved. Briefly explain which activity would handle each aspect of that improvement.
