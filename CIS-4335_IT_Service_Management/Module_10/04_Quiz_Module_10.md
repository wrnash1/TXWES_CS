# Quiz: Module 10 — Service Level Management and SLAs

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Total Questions: 10 | Points: 10 (1 pt each)

## Certification Alignment: ITIL 4 Foundation

---

## Instructions

Select the single best answer for each question. Questions are scenario-based and aligned
to the ITIL 4 Foundation exam style. Each question is followed by the correct answer and
a distractor analysis explaining why the other options are incorrect.

---

### Question 1

An IT service provider has agreed with a hospital client that the patient records system
will be available 99.9% of the time each month. This agreement is documented and signed
by both the IT Director and the hospital's Chief Operating Officer.

Which ITIL 4 term BEST describes this agreement?

- A) Operational Level Agreement (OLA)
- B) Underpinning Contract (UC)
- C) Service Level Agreement (SLA)
- D) Service Level Requirement (SLR)

#### Q1 Correct Answer: C — Service Level Agreement (SLA)

#### Q1 Distractor Analysis

- A (OLA) is incorrect. An OLA is an internal agreement between teams within the same
  IT organization. This agreement is between the IT provider and an external customer.
- B (UC) is incorrect. A UC is a contract with a third-party supplier. The hospital is
  a customer, not a supplier.
- D (SLR) is incorrect. A Service Level Requirement is the customer's expression of
  need before an agreement is reached. This is the finalized, signed agreement — an SLA.

---

### Question 2

A company's SLA promises 99.5% monthly availability for its HR system. In November, the
system was unavailable for 5.4 hours. November has 720 hours.

What was the actual availability percentage, and was the SLA target met?

- A) 99.25% — SLA breached
- B) 99.5% — SLA met exactly
- C) 99.75% — SLA met
- D) 98.9% — SLA breached

#### Q2 Correct Answer: A — 99.25%, SLA breached

#### Q2 Distractor Analysis

- B is incorrect. The calculation: ((720 − 5.4) / 720) × 100 = 99.25%, which is below
  the 99.5% target. The SLA was breached.
- C is incorrect. 99.75% would require only 1.8 hours of downtime. With 5.4 hours
  of downtime the actual figure is 99.25%.
- D is incorrect. 98.9% would require approximately 7.9 hours of downtime. The actual
  downtime was 5.4 hours, producing 99.25%.

---

### Question 3

The service desk team has an internal commitment to the infrastructure team: they will
provide first-line triage and documentation for all escalated server incidents within
30 minutes of receipt.

Which ITIL 4 term describes this internal commitment?

- A) Service Level Agreement (SLA)
- B) Underpinning Contract (UC)
- C) Operational Level Agreement (OLA)
- D) Key Performance Indicator (KPI)

#### Q3 Correct Answer: C — Operational Level Agreement (OLA)

#### Q3 Distractor Analysis

- A (SLA) is incorrect. An SLA is between the service provider and a customer. This is
  an internal commitment between two teams within the same IT organization.
- B (UC) is incorrect. A UC is with a third-party external supplier. Both the service
  desk and infrastructure team are internal IT teams.
- D (KPI) is incorrect. A KPI is a performance measurement metric, not an agreement.
  This is a documented commitment between teams — an OLA.

---

### Question 4

An IT organization's SLA with a manufacturing company promises 99.8% availability for
the production management system. The IT organization hosts the system on a cloud
platform whose contract guarantees 99.5% availability.

Which statement BEST describes the risk created by this arrangement?

- A) There is no risk — the cloud provider's 99.5% guarantee is sufficient for any SLA
- B) The Underpinning Contract does not adequately support the SLA; a cloud outage at
  or above 0.2% could cause an SLA breach
- C) The SLA should be revised to 99.5% to match the cloud contract
- D) This is an OLA misalignment, not a UC issue

#### Q4 Correct Answer: B

#### Q4 Distractor Analysis

- A is incorrect. The 0.3% gap between the UC (99.5%) and the SLA (99.8%) means the
  provider has committed more to the customer than the supplier has committed to the
  provider. Any cloud outage exceeding the UC allowance causes an SLA breach.
- C is incorrect. Revising the SLA down to match the UC would reduce the commitment to
  the customer. The correct response is to either renegotiate the UC upward or accept
  the risk knowingly — not automatically reduce customer expectations.
- D is incorrect. A UC is specifically the contract with a third-party supplier. This is
  a UC alignment issue, not an OLA issue (which governs internal teams).

---

### Question 5

An IT team discovers at the end of the month that they breached the availability SLA for
the finance system by 0.4%. The SLA report is scheduled to go out to the customer in
two weeks. The team resolves the underlying incident and considers waiting until the
report to inform the customer.

According to ITIL 4 best practice, what should the team do?

- A) Wait for the monthly report — this is the agreed communication channel for SLA results
- B) Inform the customer of the breach proactively as soon as it is confirmed
- C) Request that the breach be excluded from this month's report since the system has
  been restored
- D) Raise the breach internally only; customers should not be informed of individual
  breaches

#### Q5 Correct Answer: B

#### Q5 Distractor Analysis

- A is incorrect. Waiting for the monthly report is not consistent with ITIL 4 best
  practice. Proactive communication when a breach occurs — not when it is scheduled to
  be reported — is the standard that builds customer trust.
- C is incorrect. Excluding breach data from SLA reports is dishonest and fundamentally
  undermines the purpose of service level reporting.
- D is incorrect. Customers have the right to know when service commitments are not met.
  Concealing breach information from customers is contrary to every ITIL 4 guiding
  principle, especially "Be transparent."

---

### Question 6

Which of the following BEST describes the purpose of an Experience Level Agreement (XLA)?

- A) To replace SLAs with user experience targets that eliminate the need for technical
  measurement
- B) To measure the quality of user experience as a complement to technical SLA metrics
- C) To define the experience standards for IT staff during incident response
- D) To document the agreed experience between IT teams in place of an OLA

#### Q6 Correct Answer: B

#### Q6 Distractor Analysis

- A is incorrect. XLAs complement SLAs — they do not replace them. Technical measurements
  remain necessary; XLAs add an experience dimension alongside them.
- C is incorrect. XLAs measure the experience of service consumers (users and customers),
  not IT staff operations.
- D is incorrect. XLAs are not internal IT agreements. They measure end-user experience
  and are relevant to the customer-facing service relationship.

---

### Question 7

A service review meeting agenda includes reviewing performance against SLA targets,
discussing the previous month's P1 incidents, reviewing upcoming changes that will
affect the customer, and updating action items.

Which ITIL 4 practice does this meeting belong to?

- A) Incident Management
- B) Problem Management
- C) Service Level Management
- D) Change Enablement

#### Q7 Correct Answer: C — Service Level Management

#### Q7 Distractor Analysis

- A (Incident Management) is incorrect. Incident Management governs the response to
  individual incidents. The service review meeting is a governance and relationship
  management activity within SLM.
- B (Problem Management) is incorrect. Problem Management may be discussed at the meeting
  (open known errors), but the meeting itself is an SLM governance mechanism.
- D (Change Enablement) is incorrect. Upcoming changes may be reviewed at the meeting,
  but the meeting's purpose — assessing service performance and managing the customer
  relationship — is an SLM function.

---

### Question 8

A customer satisfaction survey asks users: "How easy was it to get your IT issue
resolved?" on a 1–7 scale. The results are tracked monthly and included in SLA reports.

Which XLA measurement method does this represent?

- A) Net Promoter Score (NPS)
- B) Customer Effort Score (CES)
- C) Post-interaction satisfaction survey
- D) Outcome-based measurement

#### Q8 Correct Answer: B — Customer Effort Score (CES)

#### Q8 Distractor Analysis

- A (NPS) is incorrect. Net Promoter Score asks "How likely are you to recommend IT
  services to a colleague?" on a 0–10 scale. This question asks about ease of resolution,
  not likelihood to recommend.
- C (Post-interaction satisfaction survey) is a broader category that could include many
  question types. The specific "How easy was it?" framing on a 1–7 scale is the defining
  characteristic of CES.
- D (Outcome-based measurement) is incorrect. Outcome-based measurement asks whether the
  user could complete their work after the resolution — a functional question, not an
  effort/ease question.

---

### Question 9

Which of the following is NOT a required component of a well-designed SLA according
to ITIL 4 Service Level Management?

- A) Availability target expressed as a percentage
- B) Priority-based resolution targets for P1 through P5
- C) A list of all IT staff responsible for delivering the service
- D) A breach notification timeline and method

#### Q9 Correct Answer: C

#### Q9 Distractor Analysis

- A is incorrect as a choice — availability targets ARE a required component of an SLA.
  This option describes something that belongs in an SLA.
- B is incorrect as a choice — priority-based resolution targets ARE required. SLAs must
  define response and resolution commitments by priority level.
- D is incorrect as a choice — breach notification IS required. Customers must know how
  and when they will be informed of breaches.
- C is the correct answer because a list of individual IT staff is not an SLA component.
  SLAs define commitments and governance structures, not personnel rosters. Staff
  assignments belong in operational documentation, not customer agreements.

---

### Question 10

According to ITIL 4, which of the following BEST describes why OLA targets must be
tighter than SLA targets?

- A) OLAs are more important than SLAs and therefore require higher standards
- B) The SLA represents the total available time; OLA targets must leave margin for
  service desk handling and other activities within the overall resolution window
- C) OLAs are audited by external bodies; SLAs are only internal documents
- D) Tighter OLA targets allow IT teams to charge higher prices for their services

#### Q10 Correct Answer: B

#### Q10 Distractor Analysis

- A is incorrect. OLAs and SLAs serve different purposes and neither is inherently more
  important. The SLA is the customer-facing commitment; OLAs support that commitment
  internally.
- C is incorrect. The opposite is true in most organizations — SLAs are external customer
  agreements that may be subject to audit and contractual penalties. OLAs are internal.
- D is incorrect. OLA targets are operational performance standards, not pricing mechanisms.
  They exist to ensure the SLA can be reliably met, not to justify charges.

---

Module 10 Quiz | CIS-4335 IT Service Management | Texas Wesleyan University
