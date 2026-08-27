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

---

## Part 9 — Challenge Exercise

### Challenge 1: SLA Failure Mode Diagnosis

A regional bank's IT department has maintained a formal SLA with its retail banking division for three years. The SLA reports green every month: 99.8% availability, 96% of P2 tickets closed within the 4-hour target, and 100% of planned maintenance windows communicated in advance. Despite this, the retail banking VP submitted a formal complaint last quarter stating that "IT never delivers on what matters to the business."

An investigation surfaces the following:

* The 99.8% availability figure measures server uptime at the data center, not whether the online banking portal is accessible to customers.
* P2 tickets are closed within 4 hours, but "closed" means the technical fault is resolved — customers are not notified, and business users often discover the fix only by retrying the service.
* The SLA has not been reviewed or renegotiated since it was written three years ago. In that period the bank launched a mobile app, added two new third-party integrations, and expanded hours of operation from 12/5 to 24/7.
* No OLA exists between the Application Support team and the Network Operations team. When network issues affect the portal, neither team has a documented response time obligation to the other.
* There is no XLA or customer satisfaction measurement in place.

1. Identify all SLA failure modes present in this scenario. For each, name the failure mode using the terminology from the Module 11 reading guide, describe the specific evidence from the scenario, and explain the business consequence.

2. The bank's SLA reports green every month while the VP considers service quality poor. Name this specific failure mode and explain in two sentences why it is more damaging to the business relationship than an honest SLA breach report would be.

3. Redesign the availability target to be customer-outcome-centered rather than provider-centered. Write the new target in measurable terms and explain why it better reflects the ITIL 4 Guiding Principle "Focus on value."

4. Draft one OLA between the Application Support team and the Network Operations team. Include: parties involved, at least two specific targets, and one consequence clause if the OLA is consistently missed.

### Challenge 2: SLM Practice Integration

A logistics company is implementing ITIL 4 for the first time. Their IT manager asks: "We have Incident Management and Continual Improvement already working well. Do we really need Service Level Management as a separate practice? Can't we just track incidents and improve over time?"

1. Construct a counter-argument explaining why SLM is a distinct and necessary practice even when Incident Management and Continual Improvement are already in place. Use at least two specific concepts from the Module 11 reading guide.

2. Describe a scenario in which Incident Management data alone would give management a false picture of service quality — and explain how an SLA review meeting would surface the truth that incident records cannot.

3. The logistics company's busiest period is November–December (holiday shipping season). Their current SLA has no exception clauses and no seasonal target adjustments. Identify two specific risks this creates and propose one SLA design change that would address both risks without reducing accountability.

### Reflection Questions

1. The Module 11 reading guide states that SLM is a relationship management practice, not a contract administration function. What is the practical difference between these two orientations, and what does an IT team do differently under each? Support your answer with a specific example from the lab scenarios in this module.

2. An organization achieves 100% SLA compliance for six consecutive months but its Net Promoter Score drops from +22 to -8 over the same period. Using ITIL 4 concepts from this module, explain what is most likely happening and what the organization should do next. Your answer must reference at least two specific SLM mechanisms (e.g., service review meeting, XLA, watermelon SLA, OLA alignment).
