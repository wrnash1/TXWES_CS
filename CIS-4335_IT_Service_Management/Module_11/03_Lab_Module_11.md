# Lab Activity: Module 11 — Service Level Management

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Total Points:** 100
**Certification Alignment:** ITIL 4 Foundation

---

## Scenario: Meridian Regional Health Network

Meridian Regional Health Network (MRHN) is a nonprofit health system operating three hospitals and twelve outpatient clinics across a mid-sized metropolitan area. The IT department supports approximately 6,400 clinical and administrative staff. IT services include the Electronic Health Record (EHR) system, a patient scheduling platform, clinical imaging systems, and standard enterprise infrastructure.

MRHN's IT leadership recently completed a review of its Service Level Management practice. The review surfaced several problems:

* The SLA with clinical departments was written three years ago and has not been reviewed since
* All SLA metrics are currently green, but the most recent clinical staff satisfaction survey gave IT a 31% satisfaction rating
* Internal infrastructure teams do not have documented performance commitments tied to the SLA
* A cloud vendor providing off-site backup services for patient records has no formal contractual performance commitments in place
* SLA metrics include "average server CPU utilization" and "monthly backup job completion rate" — neither metric appears on any clinical staff survey as a concern

You will work through four exercises that diagnose these problems and apply Service Level Management practices to address them.

---

## Exercise 1: Agreement Type Classification (25 points)

Read each situation below. For each situation, identify the agreement type that should govern the relationship: SLA, OLA, or UC. Then write one sentence explaining your classification.

### Situation 1

The MRHN IT department has committed to 99.8% monthly availability for the EHR system and a maximum 4-hour resolution time for P2 incidents affecting clinical care. This commitment is made to the hospital's Chief Medical Officer on behalf of all clinical departments.

Agreement type: _______________

Explanation: _______________

---

### Situation 2

The network infrastructure team within MRHN IT is being asked to commit to 99.9% monthly availability for the hospital network backbone and a maximum 30-minute response time when P1 incidents involve network connectivity. This commitment is made to the MRHN IT service management office.

Agreement type: _______________

Explanation: _______________

---

### Situation 3

A third-party company provides off-site encrypted storage and backup retrieval services for MRHN patient records. The IT department needs this vendor to guarantee a maximum 4-hour restore time for any requested patient data set and 99.5% monthly service availability.

Agreement type: _______________

Explanation: _______________

---

### Situation 4

The MRHN database administration team has committed to maintaining 99.95% availability on the EHR database cluster and completing all scheduled maintenance windows within a 2-hour window on the third Sunday of each month. This commitment is internal to the IT department.

Agreement type: _______________

Explanation: _______________

---

### Situation 5

A software vendor provides the patient scheduling platform under a multi-year hosting arrangement. MRHN IT requires the vendor to maintain 99.7% uptime during business hours, provide advance notice of maintenance windows, and resolve P1 incidents within 2 hours.

Agreement type: _______________

Explanation: _______________

---

### Situation 6

The MRHN IT service desk team has agreed with the service management office to answer 90% of incoming calls within 45 seconds, resolve 75% of EHR-related issues at first contact, and maintain an average handling time under 10 minutes for standard service requests.

Agreement type: _______________

Explanation: _______________

---

### Grading Criteria — Exercise 1

| Points | Criteria |
|---|---|
| 22–25 | All six classifications correct with accurate, precise explanations identifying the parties and the nature of each relationship |
| 17–21 | Four or five classifications correct; explanations mostly accurate but with minor gaps in reasoning |
| 11–16 | Three classifications correct; explanations incomplete or partially inaccurate |
| 0–10 | Fewer than three correct; agreement types confused with each other |

---

## Exercise 2: Watermelon SLA Analysis (25 points)

The current MRHN SLA with clinical departments includes the following metrics:

| Metric | Target | Current Performance |
|---|---|---|
| Monthly server availability | 99.5% | 99.8% — meeting target |
| Average server CPU utilization | Below 70% | 64% — meeting target |
| Monthly backup job completion rate | 98% | 99.1% — meeting target |
| Network latency (internal) | Below 5ms | 3.2ms — meeting target |
| P1 incident response time | Within 15 minutes | 11-minute average — meeting target |

The clinical staff satisfaction survey identified these top IT pain points:

1. EHR patient record load time exceeds 12 seconds during morning shift change (7–9 AM) — staff report this as a daily workflow disruption
2. The patient scheduling platform is unavailable for roughly 20 minutes every other Wednesday morning — staff describe this as "unpredictable downtime that disrupts appointment scheduling"
3. Clinical imaging systems take 45–90 seconds to load high-resolution images — radiologists report this as a significant productivity barrier

### Exercise 2 — Part A

Explain why this SLA is a watermelon SLA. Use specific evidence from the data above.

### Exercise 2 — Part B

For each of the three clinical pain points identified in the survey, write a replacement SLA metric that would measure what actually matters to the clinical staff. Express each metric in business outcome language (not infrastructure language).

### Exercise 2 — Part C

Explain what process failure allowed this watermelon SLA to persist for three years without correction. What SLM activity should have caught this disconnect?

---

### Grading Criteria — Exercise 2

| Points | Criteria |
|---|---|
| 22–25 | All three parts fully addressed; watermelon SLA concept accurately applied with specific evidence; replacement metrics are customer-facing and measurable; process failure correctly identified as absence of regular customer engagement and service reviews |
| 17–21 | Two of three parts fully addressed; watermelon SLA identified but replacement metrics are partially technical or vague |
| 11–16 | One part fully addressed; watermelon SLA identified without evidence; replacement metrics missing or infrastructure-focused |
| 0–10 | Watermelon SLA concept not demonstrated; no evidence-based analysis |

---

## Exercise 3: SLA and Supporting Agreement Alignment (25 points)

MRHN IT is rebuilding its SLA for the EHR system. The proposed SLA targets are:

* EHR availability: 99.5% monthly (excludes scheduled maintenance windows)
* EHR patient record load time: Under 5 seconds for 95% of requests during business hours
* P1 EHR incident response: First responder engaged within 10 minutes
* P1 EHR incident resolution: Service restored within 2 hours

The EHR system depends on the following internal and external components:

| Component | Owner | Current Committed Performance |
|---|---|---|
| Hospital network | Internal network team | No formal commitment — best effort |
| EHR database cluster | Internal DBA team | No formal commitment — best effort |
| EHR application servers | Internal server team | No formal commitment — best effort |
| Off-site backup and DR | External vendor (CloudSafe Inc.) | No formal commitment — verbal agreement only |

### Exercise 3 — Part A

Identify the alignment gap between the proposed SLA targets and the current state of supporting agreements. Explain why this gap creates structural SLA risk.

### Exercise 3 — Part B

For each of the four components in the table, recommend a specific performance target for the supporting agreement. Explain how each target was derived from the SLA commitments above.

### Exercise 3 — Part C

For the CloudSafe Inc. relationship, identify the appropriate agreement type and explain what should happen if CloudSafe fails to meet the committed performance targets.

---

### Grading Criteria — Exercise 3

| Points | Criteria |
|---|---|
| 22–25 | Alignment gap clearly articulated; supporting agreement targets logically derived from SLA targets with headroom reasoning; UC correctly identified for CloudSafe with contractual recourse explained |
| 17–21 | Gap identified; most targets reasonable; agreement type for CloudSafe correct but recourse explanation incomplete |
| 11–16 | Gap partially identified; some targets arbitrary; OLA/UC distinction partially correct |
| 0–10 | Alignment concept not demonstrated; agreement types confused |

---

## Exercise 4: Service Review and Continual Improvement Integration (25 points)

MRHN IT is establishing a formal service review process for its EHR SLA. The service management office is designing the agenda and governance structure for quarterly service reviews with clinical leadership.

### Exercise 4 — Part A

Design a service review agenda for a 60-minute quarterly meeting between MRHN IT and the hospital's clinical leadership. Your agenda must include at least five distinct agenda items and specify the purpose of each item.

### Exercise 4 — Part B

Following the most recent service review, the IT team identifies that EHR patient record load times during morning shift change (7–9 AM) are consistently at 14 seconds — well above the 5-second target in the new SLA. Write a brief summary (5–8 sentences) of how this performance gap should be handled across the following three practices:

* Service Level Management
* Problem Management
* Continual Improvement

### Exercise 4 — Part C

Apply one ITIL 4 Guiding Principle to justify why regular service reviews are essential for an effective SLM practice. Name the principle and explain the connection.

---

### Grading Criteria — Exercise 4

| Points | Criteria |
|---|---|
| 22–25 | Service review agenda is complete and realistic; all five items have clear purposes; performance gap handled correctly across all three practices with accurate practice-specific actions named; Guiding Principle correctly identified and applied |
| 17–21 | Agenda mostly complete; gap handled across two of three practices correctly; Guiding Principle identified with partial explanation |
| 11–16 | Agenda present but incomplete; gap handled by one practice only; Guiding Principle vague or incorrectly applied |
| 0–10 | Agenda missing or generic; practice relationships not demonstrated |

---

## Deliverables

Submit your completed lab document to Canvas by the due date shown in the course schedule. Your submission should address all four exercises in sequence. Label each exercise and each part clearly.

Your responses should use precise ITIL 4 terminology. Vague references to "better agreements" or "improving communication" without naming specific ITIL 4 concepts (SLA, OLA, UC, watermelon SLA, service review, continual improvement) will not earn full credit.

---

Module 11 Lab | CIS-4335 IT Service Management | Texas Wesleyan University
