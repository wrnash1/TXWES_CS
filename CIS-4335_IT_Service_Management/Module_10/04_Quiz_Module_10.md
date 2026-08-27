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

---

### Question 11 (5 points)

A cloud hosting company signs a contract with a corporate client promising 99.95% monthly availability for the client's e-commerce platform. The hosting company relies on a network provider whose contract guarantees 99.9% uptime. What problem does this arrangement create?

- A) No problem — 99.9% is close enough to 99.95% to be acceptable.
- B) The underpinning contract does not fully support the SLA; the network provider's allowable downtime exceeds the SLA's allowable downtime.
- C) The SLA is invalid because it is higher than the OLA target.
- D) The network provider's contract is an OLA because both companies are IT organizations.

#### Q11 Correct Answer: B

#### Q11 Distractor Analysis

- A is incorrect. The 0.05% gap may seem small but at monthly scale (720 hours) it represents approximately 21 minutes of additional acceptable downtime at the supplier level beyond what the SLA permits. This creates an unhedged risk.
- C is incorrect. An SLA does not need to match an OLA target. OLAs are internal supporting agreements; the SLA is the external customer commitment.
- D is incorrect. A UC is defined by the relationship being with an external third-party supplier. The fact that both parties are IT companies is irrelevant — the contract is between two separate organizations, making it a UC.

---

### Question 12 (5 points)

An IT service provider's monthly SLA report shows 99.92% availability for the trading platform — above the 99.9% target. However, a quarterly customer survey gives the service a 2.1 out of 5.0 satisfaction rating. The customer's main complaint is that when outages do occur, they receive no communication until the issue is already resolved.

What does this scenario most directly illustrate?

- A) The SLA is incorrectly drafted and the availability target is too low.
- B) Technical SLA compliance does not guarantee a positive customer experience — XLAs or experience metrics are needed alongside SLAs.
- C) The customer satisfaction score is invalid because it conflicts with the technical SLA data.
- D) The customer's expectations are unreasonable given the 99.92% achieved availability.

#### Q12 Correct Answer: B

#### Q12 Distractor Analysis

- A is incorrect. The SLA target may be appropriate; the problem is communication during outages, not the availability target level.
- C is incorrect. Customer satisfaction data is a valid and important measurement dimension. Technical compliance and experience quality are independent measurements.
- D is incorrect. Poor communication during outages is a legitimate service failure regardless of uptime percentage. Customer frustration is not "unreasonable" when the provider fails to communicate.

---

### Question 13 (5 points)

A service desk manager proposes adding the following metric to the monthly SLA report: "Percentage of incidents where users confirmed they could complete their core work task within one hour of resolution." Which XLA measurement method does this represent?

- A) Net Promoter Score
- B) Customer Effort Score
- C) Outcome-based measurement
- D) Post-interaction satisfaction survey

#### Q13 Correct Answer: C — Outcome-based measurement

#### Q13 Distractor Analysis

- A is incorrect. Net Promoter Score asks about likelihood to recommend, not about whether a specific task was completed.
- B is incorrect. Customer Effort Score measures ease of getting a resolution, not whether the business outcome was achieved.
- D is incorrect. A post-interaction satisfaction survey measures subjective satisfaction, not the functional outcome of whether work was completed.

---

### Question 14 (5 points)

An organization's SLA with its logistics client defines a P1 resolution target of 2 hours. The infrastructure team's OLA to the service desk defines a 60-minute handback time for escalated P1 tickets. Which statement correctly assesses these targets?

- A) The OLA is correctly set — 60 minutes leaves adequate time for the service desk to manage resolution within the 2-hour SLA.
- B) The OLA should be tighter — 60 minutes leaves only 60 minutes for the service desk, which is insufficient margin if the escalation path is used twice.
- C) The SLA target should be 60 minutes to match the OLA.
- D) OLAs do not need to align with SLA targets.

#### Q14 Correct Answer: A

#### Q14 Distractor Analysis

- A is correct because a 60-minute OLA for infrastructure escalation leaves 60 minutes remaining in the 2-hour SLA window — a reasonable structure if there is only one escalation tier. The targets are aligned.
- B may be worth considering for complex escalation chains, but as stated for a single escalation path, 60 minutes remaining is a workable margin.
- C is incorrect. SLA targets are set based on customer needs and business requirements, not adjusted downward to match internal OLAs.
- D is incorrect. OLAs must support SLA delivery — alignment between OLAs and SLAs is a core Service Level Management principle.

---

### Question 15 (5 points)

Which of the following correctly describes the purpose of a Service Level Requirement (SLR)?

- A) A legally binding document that defines penalty clauses for SLA breaches
- B) The customer's initial expression of service performance needs before an SLA is negotiated
- C) A technical specification document produced by the IT infrastructure team
- D) A synonym for an OLA — used when the agreement is with an internal team

#### Q15 Correct Answer: B

#### Q15 Distractor Analysis

- A is incorrect. An SLR is a pre-negotiation statement of needs, not a binding document with penalties. Penalty clauses belong in the SLA itself or in the commercial contract.
- C is incorrect. SLRs are produced by the customer (or jointly with the customer) to express business needs, not by the IT infrastructure team.
- D is incorrect. SLR and OLA are entirely different terms. An SLR is a customer requirement document; an OLA is an internal support agreement between IT teams.

---

### Question 16 (5 points)

An IT department has been measuring and reporting SLA compliance for three years but has never conducted a formal service review meeting with the business. What is the most significant consequence of this omission?

- A) The SLA reports are technically invalid without a review meeting signature.
- B) The IT department loses the opportunity to understand evolving customer needs, address relationship issues, and collaborate on service improvements.
- C) The absence of review meetings means SLA targets automatically revert to default values.
- D) The business is legally entitled to terminate the SLA agreement.

#### Q16 Correct Answer: B

#### Q16 Distractor Analysis

- A is incorrect. SLA reports are not invalidated by the absence of review meetings.
- C is incorrect. SLA targets do not revert or change automatically based on whether review meetings occur.
- D is incorrect. While a persistent lack of review meetings may indicate a relationship in poor health, automatic legal termination is not an ITIL 4 consequence.

---

### Question 17 (5 points)

A Service Level Manager proposes introducing watermelon reporting to the board of directors as something to watch out for. What does "watermelon reporting" describe?

- A) Reporting that uses color coding — green on the outside, red on the inside — meaning SLA metrics appear green but underlying customer experience is poor
- B) A specific XLA measurement tool that measures satisfaction in layers
- C) A reporting style where only positive metrics are included and breaches are omitted
- D) A monthly SLA report format that uses three sections: RAG status, trend lines, and corrective actions

#### Q17 Correct Answer: A

#### Q17 Distractor Analysis

- A is correct. "Watermelon reporting" is an industry term describing reports that appear green (passing) on summary metrics while hiding red (failing) experience data underneath — like a watermelon that is green outside but red inside.
- B is incorrect. Watermelon reporting is not a tool; it is a cautionary term for misleading reporting.
- C is incorrect. Omitting breach data is dishonest reporting, but watermelon reporting specifically refers to the combination of technical compliance with hidden poor experience — not just omission.
- D is incorrect. A RAG status report format is a legitimate reporting tool; the watermelon term is a criticism of a specific misleading pattern.

---

### Question 18 (5 points)

An IT organization has agreed to provide a core banking application with 99.8% availability during business hours (8 AM–6 PM, Monday–Friday). In a given month, the application is unavailable for 2 hours during a planned Saturday maintenance window and for 30 minutes on a Tuesday at 9 AM. How much downtime counts toward the SLA?

- A) 2.5 hours total — both the Saturday maintenance and Tuesday outage count.
- B) 30 minutes — only the Tuesday business-hours outage counts.
- C) 0 minutes — planned maintenance windows are always excluded from SLA calculations.
- D) 2 hours — only the Saturday maintenance window counts because it was longer.

#### Q18 Correct Answer: B

#### Q18 Distractor Analysis

- A is incorrect. The SLA covers availability only during agreed service hours (8 AM–6 PM, Monday–Friday). Saturday is outside the service window, so that downtime does not count against the SLA.
- C is incorrect. Planned maintenance windows are only excluded if they are outside the agreed service hours OR if the SLA explicitly carves them out. The Tuesday outage occurred during business hours and counts regardless of whether it was planned.
- D is incorrect. The Saturday maintenance window is outside service hours and is not counted. Only the Tuesday business-hours downtime counts.

---

### Question 19 (5 points)

A customer reports that their service desk satisfaction scores have dropped despite the IT team consistently meeting all technical SLA targets. The IT director argues the SLA is fine because all targets are green. An ITSM consultant disagrees. What is the consultant most likely to recommend?

- A) Raise all SLA targets to force IT to work harder.
- B) Conduct exit interviews with dissatisfied users to identify which aspects of the experience are failing, and introduce XLA measurements alongside the existing SLA metrics.
- C) Remove the customer satisfaction measurement because it conflicts with objective SLA data.
- D) Notify the customer that their complaints are invalid because all SLA targets are being met.

#### Q19 Correct Answer: B

#### Q19 Distractor Analysis

- A is incorrect. Raising SLA targets without understanding the experience failure may produce more pressure without addressing the actual gap.
- C is incorrect. Removing experience measurement because it produces uncomfortable data is the opposite of good service management practice.
- D is incorrect. Customer satisfaction is a legitimate and important service quality signal. Dismissing it because technical metrics are green reflects a provider-centric view that ITIL 4 explicitly moves away from.

---

### Question 20 (5 points)

An organization's Service Level Manager notices that the SLA for the customer relationship management (CRM) system has not been reviewed in four years. The business has expanded significantly, the user base has tripled, and a new regulatory requirement now mandates 99.9% availability during all business hours. The current SLA requires only 99% availability with no business-hours specification. What action should the Service Level Manager take?

- A) Leave the SLA unchanged — it is still technically valid since both parties signed it.
- B) Inform the customer that their SLA is no longer relevant and issue a new one without negotiation.
- C) Initiate a formal SLA review with the customer to update targets to reflect current business requirements, including the regulatory availability mandate.
- D) Raise an emergency change to update the SLA immediately without customer input.

#### Q20 Correct Answer: C

#### Q20 Distractor Analysis

- A is incorrect. An SLA that no longer reflects the business reality or regulatory requirements fails its purpose regardless of its legal validity. ITIL 4 requires SLAs to be reviewed regularly and kept aligned with current needs.
- B is incorrect. Issuing a new SLA without customer input violates the collaborative SLA negotiation principle. Customers are co-designers of service commitments.
- D is incorrect. Emergency change is an incident/problem management tool, not a mechanism for updating customer agreements. SLA revisions follow a negotiated process.

---

Module 10 Quiz | CIS-4335 IT Service Management | Texas Wesleyan University
