# Reading Guide: Module 11 — Service Management Practices: Service Level Management

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4335 &BULL; IT SERVICE MANAGEMENT & ITIL FRAMEWORKS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** ITIL 4 Foundation

---

## Overview

Service Level Management (SLM) is the practice responsible for setting clear, business-based targets for service performance and ensuring that delivery is measured, reported, and managed against those targets. It is one of the most relationship-focused practices in the ITIL 4 framework — its success depends on honest, ongoing engagement between the service provider and its customers as much as it depends on technical monitoring.

Use this guide alongside the Module 11 video lecture and ITIL 4 Foundation study resources.

---

## Purpose of Service Level Management

ITIL 4 defines the purpose of Service Level Management as:

> To set clear, business-based targets for service levels, and to ensure that delivery of services is properly assessed, monitored, and managed against these targets.

Three ideas are embedded in this definition.

**Business-based targets** — Targets must reflect what the business actually needs, not what is convenient to measure technically. A target like "disk I/O latency under 4 milliseconds" may be easy to monitor but meaningless to a business analyst who needs to run quarterly close reports.

**Assessed and monitored** — Performance must be continuously measured. An SLA that is signed but never tracked is not an active management tool — it is a legal document waiting to become a dispute.

**Managed against targets** — When performance falls short of a target, SLM is responsible for identifying the gap, understanding the cause, and driving corrective action.

---

## The Three Agreement Types

This is the highest-tested area within the SLM topic on the ITIL 4 Foundation exam.

| Agreement Type | Full Name | Parties Involved | Nature |
|---|---|---|---|
| SLA | Service Level Agreement | Service provider and customer | Documented agreement on services and expected service levels |
| OLA | Operational Level Agreement | Service provider and internal support team | Internal commitment that underpins the SLA |
| UC | Underpinning Contract | Service provider and external supplier | Legally binding contract with a third party |

### Service Level Agreement (SLA)

An SLA is a documented agreement between a service provider and a customer. It identifies the services to be delivered and specifies the expected level of service. The SLA is the primary artifact of Service Level Management — it is what the customer signs up to and what the provider commits to deliver.

A well-formed SLA contains:

* Measurable service level targets — availability percentages, response time targets, resolution time targets, throughput thresholds
* Definitions of how each metric will be measured and reported
* Procedures for what happens when targets are not met — escalation paths, service credits, remediation plans
* A defined review cadence — how often the SLA will be formally revisited

### Operational Level Agreement (OLA)

An OLA is an agreement between the service provider and an internal team within the same organization. Internal support teams — a network team, a database administration team, a desktop support team — make specific performance commitments that collectively enable the provider to meet its SLA with the customer.

Example: If the SLA commits to 99.5% monthly availability for the order management system, the OLA with the network team might require 99.7% network availability, the OLA with the database team might require 99.8% database availability, and the OLA with the application support team might require 99.9% application server availability. Each internal OLA provides the headroom needed to absorb failures at one layer without breaching the overall SLA.

### Underpinning Contract (UC)

A UC is a legally binding contract between the service provider and an external third-party supplier. When components of service delivery depend on external vendors — a cloud infrastructure provider, a network carrier, a software maintenance organization — the UC defines the minimum performance commitments that supplier must meet.

The UC gives the service provider contractual recourse if an external supplier's failures cause SLA breaches with the customer.

---

## The Agreement Hierarchy

The three agreement types exist in a layered structure.

```text
Customer
   ↕ SLA
Service Provider
   ↕ OLA          ↕ UC
Internal Teams    External Suppliers
```

The SLA defines the customer-facing commitment. OLAs and UCs define the internal and external commitments that make it possible to meet the SLA. If OLAs and UCs are not aligned with the SLA — if internal teams or external suppliers are only committed to performance levels that cannot support the SLA target — SLA breaches become structurally inevitable.

---

## What Makes a Good SLA?

Not all SLAs are effective. ITIL 4 identifies several patterns of SLA failure.

| Failure Mode | Description | Remedy |
|---|---|---|
| Watermelon SLA | Metrics are technically green but the customer experiences significant pain in unmeasured areas | Engage customers to identify what actually matters; redesign metrics |
| Unused SLA | Signed once, filed, never referenced again until a dispute | Build regular service reviews into the operating model |
| Unrealistic targets | Targets set beyond the provider's actual capability | Baseline actual performance before setting targets |
| Technically oriented SLA | Metrics expressed in infrastructure terms the customer does not understand | Translate metrics into business outcome language |

### The Watermelon SLA

The watermelon SLA is a specific, named ITIL 4 concept. It occurs when the SLA is technically compliant — all dashboard tiles are green — but the customer is experiencing significant service quality problems in areas the SLA does not measure.

The name captures the problem visually: green on the outside, red on the inside.

This failure mode arises when SLA metrics are chosen based on what is easy to monitor rather than what the customer actually cares about. The fix is customer engagement: active conversations with users and business stakeholders to understand their pain points, followed by SLA redesign that measures the outcomes they experience, not the infrastructure metrics that are convenient to collect.

---

## Customer Engagement in SLM

ITIL 4 is explicit that Service Level Management is a relationship management practice, not a contract administration function. The goal is not to avoid SLA breaches by writing cleverly narrow commitments — it is to build genuine trust by delivering what the customer needs and demonstrating that delivery transparently.

Customer engagement activities in SLM include:

* **Initial SLA development** — Understanding what the customer needs before writing any targets requires listening and exploration, not just presenting a standard SLA template.
* **Regular service reviews** — Periodic structured meetings where actual service performance is reviewed against SLA targets, trends are discussed, and problems are surfaced before they become crises.
* **SLA revision** — As the business evolves, the SLA must evolve with it. Customer engagement ensures the provider knows when the business has changed and targets need updating.
* **Satisfaction measurement** — Surveys, feedback sessions, and informal conversations that go beyond the metrics to understand how customers actually experience the service day to day.

---

## Service Level Management and Related Practices

| Related Practice | Relationship |
|---|---|
| Incident Management | Incident impact on availability and response times directly affects SLA performance; major incidents trigger SLA breach reporting |
| Problem Management | Recurring SLA breaches pointing to the same root cause become candidates for Problem Management |
| Continual Improvement | SLA performance gaps feed the Continual Improvement Register as improvement initiative candidates |
| Service Desk | Service Desk response and resolution times must align with SLA commitments; SLA targets translate directly into Service Desk operational targets |
| Monitoring and Event Management | Monitoring data is the source of SLA performance measurement; monitoring accuracy determines reporting reliability |
| Change Enablement | Changes that affect monitored services can impact SLA compliance; the change schedule should account for SLA implications |

---

## SLM and the ITIL 4 Guiding Principles

| Guiding Principle | Application to SLM |
|---|---|
| Focus on value | SLA metrics must reflect what creates value for the customer, not what is easy to measure |
| Start where you are | Baseline actual service performance before setting targets — do not guess or aspirationally commit |
| Progress iteratively with feedback | SLA reviews provide the feedback cycle for improvement; do not wait for annual reviews |
| Collaborate and promote visibility | Involve customers in SLA design; make performance data visible and accessible |
| Think and work holistically | OLAs and UCs must collectively support the SLA; no single team can be optimized in isolation |
| Keep it simple and practical | Fewer, meaningful metrics are better than comprehensive dashboards nobody reads |
| Optimize and automate | Automate SLA performance data collection where possible to ensure accuracy and reduce manual effort |

---

## ITIL 4 Foundation Exam Tips — Module 11

1. Know the three agreement types and who each party is. On the exam, read the parties carefully: customer-provider equals SLA, internal teams equal OLA, external supplier equals UC.

2. The watermelon SLA is a named ITIL 4 concept. If an exam scenario describes an organization meeting all SLA targets while customers are dissatisfied, the answer will involve watermelon SLA and the fix will involve customer engagement and metric redesign.

3. SLAs must be business-based. Technically oriented metrics that the customer does not understand or care about are a failure mode, not a best practice.

4. An SLA signed once and never reviewed is not functioning as intended. SLM requires ongoing engagement and regular service reviews.

5. OLAs support the SLA — they define what internal teams commit to in order to collectively enable the provider to meet the SLA commitment. They are not the same as the SLA.

6. UCs are legally binding contracts with external suppliers — they carry legal weight that OLAs do not.

7. SLM is not a monitoring function. Monitoring and Event Management produces the data; SLM uses that data to assess and manage performance.

8. Do not confuse SLM with the Service Desk. The Service Desk handles user interactions. SLM manages the formal agreements about what level of service will be delivered.

---

## Key Terms Glossary — Module 11

| Term | Definition |
|---|---|
| Service Level Management (SLM) | The practice of setting and managing clear, business-based service level targets |
| Service Level Agreement (SLA) | A documented agreement between a service provider and a customer specifying expected service levels |
| Operational Level Agreement (OLA) | An agreement between a service provider and an internal team that supports the SLA |
| Underpinning Contract (UC) | A legally binding contract between a service provider and an external supplier |
| Watermelon SLA | An SLA where metrics appear compliant but customer experience is poor in unmeasured areas |
| Service Review | A periodic meeting where actual service performance is assessed against SLA targets |
| Service Level Target | A specific, measurable commitment included in an SLA |
| Customer Engagement | Ongoing interaction with customers to understand needs, review performance, and maintain trust |
| XLA | Experience Level Agreement — an emerging supplement to SLAs focusing on customer experience outcomes |

---

## Required Reading

* ITIL 4 Foundation publication — chapter on the Service Level Management practice
* Axelos ITIL 4 Foundation sample questions — filter for SLA, OLA, UC, and watermelon scenarios
* Axelos ITIL 4 Foundation practice exam at [axelos.com](https://www.axelos.com)

---

## Study Checklist

* [ ] Define the purpose of Service Level Management in your own words
* [ ] Explain the difference between an SLA, an OLA, and a UC — including the parties involved for each
* [ ] Describe the watermelon SLA failure mode and explain how to fix it
* [ ] List four failure modes of ineffective SLAs
* [ ] Explain why SLM is considered a relationship management practice rather than a contract administration function
* [ ] Describe at least three customer engagement activities that SLM requires
* [ ] Explain how SLM relates to Incident Management, Problem Management, and Continual Improvement
* [ ] Apply the Guiding Principle "Focus on value" to the design of an SLA

---

Module 11 Reading Guide | CIS-4335 IT Service Management | Texas Wesleyan University

---

## Supplemental Resources

**1. AXELOS — ITIL 4 Service Level Management Practice Guide**
<https://www.axelos.com/resource-hub/blog/itil-4-service-level-management>
Official AXELOS overview of the Service Level Management practice, covering SLA design, OLA and UC alignment, service review meetings, and the shift from technical metrics to experience-level agreements. Essential for Foundation exam preparation and practical SLM implementation.

**2. Freshservice — Watermelon SLA: What It Is and How to Avoid It**
<https://freshservice.com/itsm/sla-management-guide>
Practitioner-focused guide that explains the watermelon SLA failure mode — green on the outside, red on the inside — and provides actionable strategies for aligning technical metrics with genuine customer experience outcomes. Includes breach prevention and escalation automation techniques.

**3. itSMF UK — XLA Manifesto**
<https://xla-manifesto.com>
The industry reference document on Experience Level Agreements, authored by leading ITSM practitioners. Explains why XLAs complement rather than replace SLAs, how to design measurable experience targets, and how to use NPS, CES, and outcome-based measurement alongside traditional service level metrics.
