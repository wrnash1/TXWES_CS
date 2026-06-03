# Reading Guide: Module 10 — Service Level Management and SLAs

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: ITIL 4 Foundation

---

## Overview

Service Level Management (SLM) is the practice responsible for setting, monitoring, and
managing the performance commitments made between IT and its customers. It sits at the
intersection of business relationship management and operational delivery.

SLM is a consistent exam topic on the ITIL 4 Foundation and has direct applicability to
virtually every IT role. This guide covers SLA design, OLAs and UCs, breach management,
service review meetings, reporting, and XLAs.

---

## Service Level Management Purpose

To set clear business-based targets for service performance so that the delivery of a
service can be properly assessed, monitored, and managed against those targets.

---

## Core Definitions

| Term | Definition |
|---|---|
| Service Level Agreement (SLA) | A documented agreement between the service provider and a customer identifying services required and expected level of service |
| Operational Level Agreement (OLA) | An agreement between an IT service provider and another part of the same organization that assists in the provision of services |
| Underpinning Contract (UC) | A contract between an IT service provider and a third-party supplier governing their contribution to service delivery |
| Service Level Target | A specific measurable commitment within an SLA (e.g., P2 incidents resolved within 4 hours) |
| Service Level Requirement | The customer's stated needs for a service, used as the basis for designing SLAs |
| SLA Breach | A failure to meet one or more service level targets during a measurement period |
| Service Review Meeting | A regular structured meeting between IT and the customer to assess performance and alignment |
| XLA (Experience Level Agreement) | An agreement or target focused on the quality of user experience rather than technical delivery metrics |
| Availability | The ability of a service to perform its agreed function when required; expressed as a percentage |
| Mean Time to Restore (MTTR) | Average time to restore a service following an incident |

---

## The Three-Tier Agreement Structure

### Tier Definitions and Relationships

| Tier | Agreement Type | Parties | Purpose |
|---|---|---|---|
| 1 | SLA | IT provider ↔ Customer | Defines the IT-to-business service commitment |
| 2 | OLA | IT team ↔ IT team (internal) | Aligns internal teams to support the SLA |
| 3 | UC | IT provider ↔ Third-party supplier | Ensures supplier performance underpins the SLA |

### Why All Three Tiers Must Be Aligned

SLA breaches frequently originate at Tier 2 or Tier 3:

- If the infrastructure team's OLA response time is 3 hours but the SLA promises
  4-hour resolution, there is no margin for service desk handling time — the SLA will
  be breached systematically.
- If the cloud provider's UC guarantees 99.5% availability but the SLA promises 99.9%,
  the SLA cannot be reliably met when the provider has even a brief outage.

Alignment rule: OLA targets must be tighter than SLA targets. UC guarantees must meet
or exceed SLA availability commitments.

---

## SLA Design — Required Components

A complete SLA must contain:

| Component | Description |
|---|---|
| Service description | What is included; what is explicitly excluded |
| Service hours | Availability window (24/7, business hours 8 AM–6 PM, etc.) |
| Availability target | Percentage uptime commitment per measurement period |
| Performance targets | Response time, throughput, error rate limits |
| Priority-based resolution targets | P1–P5 acknowledgment and resolution times |
| Support model | Contact channels; escalation path |
| Measurement and reporting | How compliance is calculated; report cadence |
| Breach notification | When and how breaches are communicated |
| Review schedule | Frequency of formal SLA review |
| Exceptions | Planned maintenance, force majeure, customer-caused issues |

### Availability Calculation

```text
Availability % = ((Agreed Service Time − Downtime) / Agreed Service Time) × 100
```

Example: 720-hour month; 3.6 hours downtime.

```text
((720 − 3.6) / 720) × 100 = 99.5%
```

### Common SLA Design Mistakes

| Mistake | Problem | Better Approach |
|---|---|---|
| Vague targets ("respond promptly") | Unmeasurable; creates dispute | Specific: "P2 acknowledged within 15 min" |
| Provider-centered metrics (server uptime) | Doesn't reflect user experience | User-perspective: "service accessible to users" |
| No customer input | Misses what the business actually values | Joint design workshops with business stakeholders |
| No exception clauses | Creates conflict during maintenance | Define planned maintenance windows explicitly |
| Static targets | Become outdated as business needs change | Annual review minimum; triggered review on major change |

---

## SLA Monitoring and Breach Management

### Monitoring Requirements

Effective SLA monitoring requires:

- Real-time dashboards showing current status against all targets
- Near-breach alerts (75% and 90% of target window consumed)
- Automated SLA timers on every ticket
- Trend dashboards showing performance over rolling 3/6/12-month periods
- CMDB integration — mapping incidents to services and SLA commitments

### SLA Breach Process

| Step | Action |
|---|---|
| 1. Detection | SLA breach identified — ideally before closure via near-breach alerts |
| 2. Documentation | Breach recorded with incident record, cause, and timeline |
| 3. Proactive communication | Customer notified as soon as breach is confirmed — do not wait for the monthly report |
| 4. Root cause analysis | Was it a technology failure, process failure, OLA breach, or UC breach? |
| 5. Improvement action | Breach feeds into the improvement register with an owner and due date |
| 6. Report inclusion | Breach included honestly in the next SLA report with cause and corrective action |

### Breach Categories

| Breach Type | Root Cause | Response |
|---|---|---|
| Technical breach | Infrastructure, application, or network failure | Incident → Problem → Change cycle |
| Process breach | Service desk or team missed escalation or SLA timer | Process review; workflow fix; training |
| OLA breach | Internal supporting team failed their commitment | OLA review; escalation; staffing |
| UC breach | Supplier failed their contractual obligation | Vendor escalation; contract review; penalty clause |

---

## Service Review Meetings

### Meeting Purpose and Frequency

Service review meetings are regular structured governance sessions between IT and the
customer to assess performance, manage the relationship, and drive alignment.

Typical frequency: monthly for standard services; weekly for critical services during
improvement periods.

### Standard Agenda

| Agenda Item | Purpose |
|---|---|
| Performance vs. SLA targets | Review actual vs. committed performance; identify trends |
| Major incident review | Status of P1/P2 incidents; PIR outcomes |
| Upcoming changes | Changes that will affect the customer in the next period |
| Problem Management status | Open known errors; expected resolution timelines |
| Improvement initiatives | Progress on current initiatives; new items from feedback |
| Customer satisfaction feedback | Survey results; qualitative feedback |
| SLA target review | Are current targets still relevant and appropriate? |
| Action items | Owners, due dates, and follow-up from previous meeting |

### Best Practices for Service Review Meetings

- Distribute performance reports at least 48 hours before the meeting
- Do not surprise customers with bad news in the meeting — communicate breaches
  proactively when they occur
- Record action items with specific owners and due dates
- Follow up on previous meeting action items before adding new ones
- Keep the meeting forward-looking — past performance is context, not the focus

---

## SLA Reporting Standards

### Report Components

| Component | Description |
|---|---|
| Availability trend | Monthly availability percentage charted over 6–12 months |
| Incident volume by priority | P1–P5 incident counts; trend direction |
| SLA compliance rate | Percentage of tickets resolved within target per priority level |
| Breach summary | Number and type of breaches; root causes; corrective actions |
| Average resolution time | Actual vs. target resolution time by priority |
| Customer satisfaction | Survey scores or NPS if measured |

### Reporting Principles

- Report honestly — manipulating or excluding breach data destroys trust permanently
- Every breach must have a documented cause and a corrective action
- Show trends, not just point-in-time data
- Make reports readable for non-technical stakeholders
- Include a forward-looking section — what is being done to improve next period

---

## Experience Level Agreements (XLAs)

### XLA Definition and Purpose

An XLA shifts the measurement focus from technical delivery metrics to the quality of
the user experience. SLAs answer "Did IT meet the technical target?" XLAs answer "Did
the user actually have a good experience?"

### SLA vs. XLA Comparison

| Dimension | SLA Measurement | XLA Measurement |
|---|---|---|
| Availability | 99.8% uptime | Did users feel the service was reliably available? |
| Resolution time | 87% of P2 tickets closed within 4 hours | Was the resolution process easy and clear for the user? |
| First-call resolution | 84% FCR rate | Did users feel confident after one contact? |
| Communication | Breach communicated within 30 min | Did users feel informed and supported during the outage? |

### XLA Measurement Methods

| Method | Description |
|---|---|
| Post-interaction survey | 1–3 question survey after ticket closure (satisfaction, ease, likelihood to recommend) |
| Net Promoter Score (NPS) | "How likely are you to recommend IT services?" (0–10 scale) |
| Customer Effort Score (CES) | "How easy was it to get your issue resolved?" (1–7 scale) |
| Sentiment analysis | Natural language analysis of ticket comments, chat logs, survey responses |
| Outcome-based measurement | "Were you able to complete your work following the resolution?" |

### SLAs and XLAs as Complementary Lenses

SLAs without XLAs: IT is technically compliant but users may still be frustrated.

XLAs without SLAs: User experience is positive but technical commitments are undefined
and unmeasurable.

Best practice: maintain both. SLAs ensure the floor is maintained. XLAs ensure the
ceiling of experience is pursued.

---

## Practice Maturity Comparison — SLM

| Maturity Level | Characteristics |
|---|---|
| Informal | No formal SLAs; service quality defined informally; no breach tracking |
| Defined | SLAs exist but may be provider-centered; limited monitoring; annual reporting |
| Measured | Real-time SLA dashboards; proactive breach communication; monthly service reviews |
| Optimized | XLAs in use alongside SLAs; outcome-based targets; customer co-design; predictive analytics |

---

## ITIL 4 Foundation Exam Tips — Module 10

### High-frequency exam topics

- Definition and purpose of SLA, OLA, and UC
- The three-tier agreement structure and why alignment matters
- Purpose of Service Level Management
- What an SLA should contain
- Proactive breach communication — do not wait for monthly reports
- The difference between SLAs (technical) and XLAs (experience)

### Common distractor traps

- Confusing OLA (internal) with UC (external/supplier) — OLAs are between IT teams;
  UCs are with third-party vendors
- Assuming SLAs are IT documents — they are agreements with customers; business input
  is essential
- Thinking SLA compliance means the service is good — XLAs exist because compliance
  and experience can diverge
- Assuming that meeting technical SLA targets automatically means value was delivered —
  ITIL 4's "focus on value" principle requires measuring outcomes

---

## Glossary — Module 10 Terms

| Term | Definition |
|---|---|
| SLA | Agreement between service provider and customer defining service targets |
| OLA | Internal IT-to-IT team agreement supporting SLA delivery |
| UC | Contract between IT provider and external supplier |
| SLA Breach | Failure to meet a committed service level target |
| Service Review Meeting | Structured periodic governance meeting between IT and customer |
| XLA | Experience Level Agreement — measures user experience quality |
| Availability | Percentage of agreed service time during which the service functions correctly |
| MTTR | Mean Time to Restore — average incident restoration time |
| NPS | Net Promoter Score — likelihood to recommend metric |
| CES | Customer Effort Score — ease of resolution metric |

---

## Further Study Resources

- Axelos ITIL 4 Foundation publication — Chapter 5.2 (Service Level Management)
- ITIL 4 Foundation sample exam papers — filter for SLM and agreement scenarios
- Axelos Practice Guide: Service Level Management (detailed SLM reference)
- XLA Manifesto — itSMF UK publication on experience-level measurement

---

Module 10 Reading Guide | CIS-4335 IT Service Management | Texas Wesleyan University
