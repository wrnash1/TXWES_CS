# Video Script: Module 10 — Service Level Management and SLAs

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: ITIL 4 Foundation

---

## Introduction (0:00–1:30)

Welcome to Module 10. I'm Professor Nash, and today we are talking about promises.

Every IT service rests on a promise: "We will deliver this service at this level of
quality, with this availability, and if we fail, here is what we will do." Service Level
Management is the practice that defines, monitors, and manages those promises.

In this module we cover:

- What SLAs, OLAs, and Underpinning Contracts are and how they relate
- How to design an effective SLA
- How to monitor SLA performance and manage breaches
- Service review meetings and SLA reporting
- The emerging concept of XLAs — Experience Level Agreements

[SHOW DIAGRAM: SLM ecosystem — Customer/SLA/IT Provider/OLA/Support Teams/UC/Suppliers]

Service Level Management is consistently tested on the ITIL 4 Foundation exam, and it
is one of the practices with the most real-world immediate applicability for every student
in this course who will work in IT.

[PAUSE]

---

## Section 1: SLM Fundamentals (1:30–4:30)

### The Purpose of Service Level Management

ITIL 4 defines the purpose of Service Level Management as: to set clear business-based
targets for service performance so that the delivery of a service can be properly assessed,
monitored, and managed against those targets.

[SHOW DIAGRAM: SLM as the bridge between business expectations and IT delivery]

The key insight here is "business-based targets." SLAs are not technical specifications.
They describe service performance from the customer's perspective. A customer does not
care that your server uptime is 99.9% — they care that the payroll system is available
every Thursday when they run payroll.

### The Three-Tier Agreement Structure

ITIL 4 describes a three-tier structure that governs service level commitments from end
to end:

#### Tier 1 — Service Level Agreement (SLA)

The SLA is an agreement between the IT service provider and a customer. It defines the
service, the performance targets, and the consequences of non-compliance. It is the
top-level promise to the business.

#### Tier 2 — Operational Level Agreement (OLA)

The OLA is an internal agreement between different teams within the IT organization that
support each other to deliver the SLA. Example: the service desk has an SLA with the
business to resolve P2 incidents within 4 hours. The infrastructure team has an OLA with
the service desk to respond to escalated P2 tickets within 2 hours.

#### Tier 3 — Underpinning Contract (UC)

The UC is an external contract with a third-party supplier. When IT depends on a vendor
to meet SLA commitments, the vendor's contract must underpin those commitments. Example:
if your SLA promises 99.9% availability, and you depend on a cloud provider, your cloud
contract must guarantee at least 99.9% availability.

[SHOW DIAGRAM: Three-tier structure — SLA at top, OLAs in middle, UCs at base]

[PAUSE]

Why does this hierarchy matter? Because SLA breaches often happen at the OLA or UC level.
If your infrastructure team misses their OLA response time, your SLA gets breached. If
your cloud vendor suffers an outage beyond their UC, your SLA gets breached. The three
tiers must be aligned.

---

## Section 2: SLA Design (4:30–8:30)

### What Goes in an SLA?

A well-designed SLA is specific, measurable, and agreed upon by both parties. It should
contain at minimum:

[SHOW DIAGRAM: SLA anatomy — key sections labeled]

1. **Service description** — what service is covered; what is explicitly out of scope
2. **Service hours** — when the service is available (24/7, business hours, etc.)
3. **Availability target** — expressed as a percentage (e.g., 99.5% monthly)
4. **Performance targets** — response times, transaction throughput, error rates
5. **Priority-based resolution targets** — P1 through P5 resolution SLAs
6. **Support model** — how users contact IT; escalation paths
7. **Measurement and reporting** — how compliance is measured; report frequency
8. **Breach notification** — how and when breaches are communicated
9. **Review schedule** — when the SLA is formally reviewed for relevance
10. **Exceptions** — conditions outside IT control (planned maintenance, force majeure)

### Common SLA Design Mistakes

[SHOW DIAGRAM: Good SLA vs. Bad SLA examples]

- **Too vague:** "IT will respond to issues promptly." — This is unmeasurable. Replace
  with: "P2 incidents will be acknowledged within 15 minutes and resolved within 4 hours."
- **Provider-centered metrics:** Measuring server uptime rather than user-experienced
  availability. A server can be "up" while users cannot access the service.
- **No customer input:** SLAs written by IT without business input fail to capture what
  actually matters to the customer.
- **No exception clauses:** An SLA without defined maintenance windows creates conflict
  when planned downtime is needed.
- **Static targets:** Business needs change. An SLA written three years ago may no longer
  reflect current requirements.

[PAUSE]

### Availability Calculation

Availability is most commonly expressed as a percentage of uptime in a measurement period.

The formula:

Availability % = ((Agreed Service Time − Downtime) / Agreed Service Time) × 100

Example: A service is available 24/7 (720 hours/month). In one month it experiences
3.6 hours of unplanned downtime.

Availability = ((720 − 3.6) / 720) × 100 = 99.5%

If the SLA target is 99.5%, this month is compliant — barely.

[SHOW DIAGRAM: Availability calculation with visual dial]

---

## Section 3: SLA Monitoring and Breach Management (8:30–12:00)

### Monitoring SLA Performance

SLA performance must be monitored continuously, not just at month-end reporting. Effective
SLA monitoring includes:

- **Real-time dashboards** — showing current availability and ticket status against targets
- **Near-breach alerts** — warning when a ticket is approaching its SLA deadline
- **Trend analysis** — identifying services or teams where performance is degrading over time
- **Automated SLA timers** — starting when a ticket is created, pausing during agreed
  customer hold periods, alerting at 75% and 90% of the target window

[SHOW DIAGRAM: SLA dashboard with traffic-light status indicators]

[PAUSE]

### SLA Breach Management

An SLA breach occurs when a committed target is not met. Breaches must be:

1. **Detected promptly** — ideally before closure, while restoration is still in progress
2. **Documented** — the breach is recorded with the incident, its cause, and the timeline
3. **Communicated** — the customer is notified of the breach as soon as it is confirmed;
   not after the monthly report
4. **Root-caused** — was it a technology failure, a process failure, a staffing issue, or
   an OLA/UC failure by a supporting team?
5. **Remediated** — the breach feeds into the improvement register

A critical ITIL 4 principle: **do not wait for the customer to discover a breach**. Proactive
communication when a breach occurs demonstrates accountability and protects trust. Customers
who discover breaches from their own reports lose confidence faster than those who are
proactively informed.

### SLA Breach Categories

| Breach Type | Cause | Response |
|---|---|---|
| Technical breach | Infrastructure, application, or network failure | Incident → Problem → Change cycle |
| Process breach | Service desk missed escalation or SLA timer | Process review; training; workflow fix |
| OLA breach | Internal supporting team missed their commitment | OLA review; escalation; staffing assessment |
| UC breach | Supplier failed to meet their contractual obligation | Vendor escalation; contract review; potential penalty |

---

## Section 4: Service Review Meetings and SLA Reporting (12:00–15:30)

### Service Review Meetings

The service review meeting — sometimes called the Monthly Service Review or Service
Performance Review — is a structured meeting between IT and the customer to assess service
performance, discuss trends, and align on improvement priorities.

[SHOW DIAGRAM: Service review meeting agenda structure]

A well-run service review meeting covers:

1. Performance against SLA targets (month, trend, year-to-date)
2. Major incidents and their resolution status
3. Upcoming changes that affect the customer
4. Problem Management status — open known errors and expected resolution timelines
5. Improvement initiatives in progress or planned
6. Customer satisfaction feedback
7. SLA target review — are current targets still relevant?
8. Next period action items and owners

[PAUSE]

The service review meeting is not a complaint session. It is a structured governance
mechanism for maintaining the customer-provider relationship and driving continuous alignment.

### SLA Reporting

SLA reports should be:

- **Regular** — monthly at minimum; weekly for critical services
- **Clear** — executives should understand them without a technical background
- **Honest** — do not manipulate metrics or exclude breaches; trust is built on transparency
- **Actionable** — every breach should have an associated root cause and improvement action
- **Trended** — show performance over time, not just the current period

[SHOW DIAGRAM: Sample SLA report — availability trend chart, breach summary table, top incident categories]

Key metrics in an SLA report:

- Availability percentage (actual vs. target)
- Incident volumes by priority
- SLA compliance percentage by priority
- Average and maximum resolution times
- Breach count and breach rate
- Customer satisfaction score (if measured)

---

## Section 5: Experience Level Agreements (XLAs) (15:30–18:30)

### What Is an XLA?

An Experience Level Agreement is an emerging concept that measures the quality of the
user experience rather than just the technical delivery metrics.

[SHOW DIAGRAM: SLA vs. XLA comparison — technical metrics vs. experience metrics]

SLAs measure things that are easy to measure: uptime percentage, ticket closure time,
first-call resolution rate. But these metrics can all be green while users are still
frustrated. Consider:

- Resolution time SLA: met (resolved in 3 hours against a 4-hour target)
- User experience: the user had to call three times, was transferred twice, received
  no proactive updates, and was given an incorrect workaround on the first call

Technically compliant. Experientially terrible.

XLAs attempt to capture what matters to users: Did the interaction feel easy? Did IT
communicate proactively? Was the user able to do their job during the incident? Did the
solution last or did they have to call back?

[PAUSE]

### XLA Measurement Approaches

XLAs are typically measured through:

- **Post-interaction surveys** — short (1–3 question) satisfaction surveys after ticket
  closure
- **Net Promoter Score (NPS)** — "How likely are you to recommend IT services to a
  colleague?" (0–10 scale)
- **Customer Effort Score (CES)** — "How easy was it to get your issue resolved?"
- **Sentiment analysis** — analyzing language in ticket comments, chat logs, and email
  responses
- **Outcome-based measurement** — "Were you able to complete your work after the
  resolution?"

### SLAs and XLAs Together

SLAs and XLAs are complementary, not competing. SLAs ensure minimum technical standards
are met. XLAs ensure that meeting those standards actually creates a good experience.

[SHOW DIAGRAM: SLA + XLA together — two lenses on service quality]

ITIL 4 emphasizes the guiding principle "Focus on value" — and user experience is an
important dimension of value. XLAs are how we measure whether users actually perceive
the value IT claims to deliver.

---

## Module Summary and Exam Tips (18:30–20:30)

Module 10 covered Service Level Management.

The **three-tier agreement structure**: SLA (IT provider to customer), OLA (internal team
to team), UC (IT to external supplier). All three must be aligned for SLA compliance to
be achievable.

**SLA design** must be specific, measurable, and business-based. Common mistakes include
vague targets, provider-centered metrics, and static targets that do not evolve with
business needs.

**SLA monitoring and breach management** requires continuous real-time tracking, proactive
breach communication, and root cause analysis of every breach.

**Service review meetings** are structured governance sessions for assessing performance,
managing the relationship, and driving alignment between IT and the business.

**XLAs** measure user experience — what it felt like to receive the service — as a
complement to the technical metrics in SLAs.

[SHOW DIAGRAM: Module 10 summary — SLA ecosystem, key terms, and XLA contrast]

For the ITIL 4 Foundation exam:

- Know the definitions of SLA, OLA, and UC and how they relate
- Know the purpose of Service Level Management
- Know what an SLA should contain
- Know the difference between SLAs and XLAs
- Understand that SLA breaches require proactive communication, not just reporting

[PAUSE]

Module 11 covers Continual Improvement — the practice that makes everything else better
over time. See you there.

---

End of Module 10 Video Script

Estimated delivery: 21 minutes at average instructional pace
