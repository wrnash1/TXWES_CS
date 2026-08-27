# Reading Guide: Module 09 — Problem and Change Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: ITIL 4 Foundation

---

## Overview

Module 09 covers two tightly integrated ITIL 4 practices. Problem Management addresses
the underlying causes of service failures. Change Enablement ensures that modifications
to services and infrastructure are authorized, assessed, and deployed safely.

Both practices are consistently high-weight on the ITIL 4 Foundation exam. Together they
represent the "prevent and control" layer of IT operations.

---

## Practice 1: Problem Management

### Problem Management Purpose

To reduce the likelihood and impact of incidents by identifying actual and potential causes
of incidents, and managing workarounds and known errors.

### Core Definitions

| Term | Definition |
|---|---|
| Problem | A cause, or potential cause, of one or more incidents |
| Known Error | A problem that has been analyzed, where the root cause is documented and a workaround exists |
| Workaround | A solution that reduces or eliminates the impact of an incident or problem for which a full resolution is not yet available |
| Known Error Database (KEDB) | A repository storing known errors, their root causes, and their workarounds |
| Root Cause | The underlying reason a problem occurs — addressing it prevents recurrence |
| Root Cause Analysis (RCA) | A structured investigation to identify the root cause of a problem |
| Problem Record | A record documenting all information about a problem through its lifecycle |
| Post-Incident Review (PIR) | A structured review after a major incident — the primary trigger for reactive problem management |

### Reactive vs. Proactive Problem Management

| Type | Trigger | Goal | Example |
|---|---|---|---|
| Reactive | One or more incidents have occurred | Identify root cause; prevent recurrence | P1 incident PIR raises a problem record |
| Proactive | No incident yet; risk identified | Prevent the incident from occurring | Architecture review identifies a single point of failure |

Both types are equally valid and important. High-maturity organizations do both.

### Problem Lifecycle

| Stage | Description |
|---|---|
| 1. Problem Identification | Problem record created from incident, trend, PIR, or proactive analysis |
| 2. Problem Categorization | Classified by service, component, technology domain, and business impact |
| 3. Problem Prioritization | Priority set based on potential incident frequency and impact |
| 4. Investigation and Diagnosis | RCA performed; root cause sought |
| 5. Known Error Creation | Root cause identified; workaround documented; KEDB entry created |
| 6. Resolution | Permanent fix designed; change record raised |
| 7. Problem Closure | Fix deployed and verified; problem record closed; KEDB updated |

### Known Error Database (KEDB) — Key Facts

- Created and maintained by Problem Management
- Consulted by Incident Management during diagnosis to apply known workarounds
- Each entry includes: Problem ID, description, affected services, root cause, workaround,
  status (open / fix in progress / resolved), and linked change record
- Reduces average incident resolution time by enabling immediate workaround application
- Must be kept current — stale entries reduce trust and utility

### Root Cause Analysis Techniques

| Technique | Description | Best Used When |
|---|---|---|
| 5 Whys | Ask "Why?" five times from the symptom to the root cause | Linear cause chains; quick investigations |
| Fishbone Diagram (Ishikawa) | Maps causes across People, Process, Technology, Environment categories | Complex multi-dimensional problems |
| Fault Tree Analysis | Top-down logical tree of failure combinations | High-complexity, safety-critical systems |
| Timeline Analysis | Reconstructs the sequence of events leading to the incident | Major incidents with multiple contributing factors |
| Pareto Analysis | Identifies the 20% of causes producing 80% of incidents | Trend-based prioritization |

### Problem Management Maturity Comparison

| Maturity Level | Characteristics |
|---|---|
| Reactive only | Problems raised only after PIRs; no proactive analysis; KEDB poorly maintained |
| Structured | Defined problem lifecycle; KEDB actively maintained; RCA used consistently |
| Proactive | Trend analysis and health reviews generate proactive problem records; KEDB integrated with service desk |
| Optimized | Predictive analytics identify risks before incidents; problem elimination tracked as a KPI |

---

## Practice 2: Change Enablement

### Change Enablement Purpose

To maximize the number of successful IT changes by ensuring that risks have been properly
assessed, authorizing changes to proceed, and managing the change schedule.

### Change Enablement Key Terms

| Term | Definition |
|---|---|
| Change | The addition, modification, or removal of anything that could have a direct or indirect effect on services |
| Change Request | A formal proposal for a change — also called an RFC (Request for Change) |
| Change Model | A repeatable approach for handling a specific type of change |
| Change Authority | The person or group with authorization to approve a specific change type |
| Change Advisory Board (CAB) | A group that supports authorization and planning of normal changes |
| Emergency CAB (ECAB) | A smaller, pre-designated group authorized to approve emergency changes quickly |
| Change Schedule | The authorized timeline of all approved changes — also called the Forward Schedule of Change |
| Rollback Plan | Pre-defined steps to reverse a change if it causes problems |
| Post-Implementation Review | A review after a change is deployed to verify success and capture lessons learned |

### The Three Change Types

| Change Type | Authorization | Risk Level | Examples |
|---|---|---|---|
| Standard | Pre-authorized; no CAB needed | Low; well understood | Password reset policy, routine patch via approved window, adding user to existing group |
| Normal | CAB review and approval required | Variable; must be assessed | New application deployment, database upgrade, major network change |
| Emergency | Accelerated authorization (ECAB or senior approver) | High urgency; may be high risk | Hotfix for active P1, emergency firewall rule for active exploit |

Key exam point: Emergency changes still require authorization — the process is accelerated,
not bypassed. Full documentation and a post-implementation review are still mandatory.

### Normal Change Process Flow

```text
Change Request submitted
  → Initial assessment by Change Manager
  → Technical review and risk assessment
  → CAB review (impact, risk, rollback, timing)
  → Authorization granted (or rejected with feedback)
  → Scheduled on Change Schedule
  → Implementation
  → Post-Implementation Review
  → Change record closed
```

### Change Advisory Board (CAB) — Composition and Role

| Participant | Role in CAB |
|---|---|
| IT Service Manager (chair) | Facilitates review; ensures complete assessment |
| Infrastructure representative | Assesses technical feasibility and operational risk |
| Application team representative | Assesses application-specific impact |
| Security representative | Reviews security implications and compliance |
| Business stakeholder | Assesses business impact and timing acceptability |
| Supplier representative (as needed) | Required when third-party components are involved |

CAB responsibilities:

- Review change requests for completeness and risk
- Assess conflict with other scheduled changes
- Approve, reject, or defer changes
- Ensure rollback plans are adequate
- Verify testing evidence

### Change Schedule — Purpose and Use

| Use Case | How the Schedule Helps |
|---|---|
| Conflict prevention | Ensures two changes to the same system are not scheduled simultaneously |
| Business planning | Users and stakeholders know when changes are happening and can plan accordingly |
| Incident correlation | When a P1 occurs, recent changes are immediately visible as potential causes |
| Resource planning | Operations teams can plan staffing for change windows |
| Compliance evidence | Provides an auditable record of when changes were approved and implemented |

### Change Types Comparison — Common Exam Traps

| Scenario | Correct Change Type | Common Mistake |
|---|---|---|
| Applying a vendor emergency security patch after a zero-day exploit is confirmed | Emergency | Students sometimes say "standard" because patches can be routine |
| Deploying a tested, pre-approved script to add users to Active Directory | Standard | Students sometimes say "normal" because it involves user accounts |
| Upgrading a database from v10 to v11 in production | Normal | Students sometimes say "standard" because upgrades are common |
| Applying a hotfix to restore a P1 during a war room | Emergency | Students sometimes say "normal" because there is still a review |

---

## Problem Management and Change Enablement — Integration

```text
Incident occurs
  → Incident Management restores service
  → Post-Incident Review raises Problem record
  → Problem Management performs RCA
  → Root cause identified → Known Error documented in KEDB
  → Permanent fix designed → Change Request raised
  → Change Enablement authorizes and schedules fix
  → Fix deployed → Problem Management verifies resolution
  → Problem record closed → KEDB updated
```

Without this integration, Problem Management identifies causes but cannot implement
fixes. Change Enablement implements fixes but without strategic direction from Problem
Management it may be addressing symptoms rather than root causes.

---

## ITIL 4 Foundation Exam Tips — Module 09

### High-frequency exam topics

- Definition of a problem (cause or potential cause of incidents)
- Definition of a known error (problem with identified root cause and workaround)
- Purpose and structure of the KEDB
- Reactive vs. proactive problem management
- The three change types and when each is used
- Emergency changes still require authorization — accelerated, not bypassed
- Purpose of the CAB
- The change schedule (Forward Schedule of Change)

### Common distractor traps

- Confusing problem with incident — incidents are symptoms; problems are causes
- Assuming all changes go through the CAB — standard changes are pre-authorized
- Assuming emergency changes skip all authorization — they require ECAB or senior approver
- Confusing the change schedule with a project plan — the change schedule is operational,
  not strategic
- Assuming the KEDB is maintained by the service desk — it is maintained by Problem
  Management

---

## Glossary — Module 09 Terms

| Term | Definition |
|---|---|
| Problem | Cause or potential cause of one or more incidents |
| Known Error | Problem with documented root cause and workaround |
| KEDB | Known Error Database — repository of known errors and workarounds |
| RCA | Root Cause Analysis — structured investigation to find the underlying cause |
| 5 Whys | RCA technique: ask "why" five times to reach root cause |
| Fishbone Diagram | RCA tool mapping causes across People, Process, Technology, Environment |
| Change | Addition, modification, or removal of anything affecting services |
| Standard Change | Pre-authorized, low-risk, repeatable change |
| Normal Change | Requires CAB assessment and authorization |
| Emergency Change | Urgent change requiring accelerated authorization |
| CAB | Change Advisory Board — group that reviews and authorizes normal changes |
| ECAB | Emergency CAB — smaller group authorized to approve emergency changes |
| Change Schedule | Authorized timeline of all approved changes |
| Rollback Plan | Pre-defined steps to reverse a change if it fails |

---

## Further Study Resources

- Axelos ITIL 4 Foundation publication — Chapter 5.2 (Problem Management) and
  Chapter 5.3 (Change Enablement)
- ITIL 4 Foundation sample exam papers — filter for problem management and change scenarios
- AXELOS Practice Guides — detailed practice descriptions for Problem Management and
  Change Enablement (available through MyITIL)

---

---

## Supplemental Resources

**1. AXELOS — ITIL 4 Problem Management Practice**
<https://www.axelos.com/resource-hub/blog/itil-4-problem-management>
Official AXELOS description of the Problem Management practice including reactive and proactive modes, the problem lifecycle, and the Known Error Database. Core reference for Foundation exam preparation on this practice.

**2. AXELOS — ITIL 4 Change Enablement Practice**
<https://www.axelos.com/resource-hub/blog/itil-4-change-enablement>
Official AXELOS guidance on change types (standard, normal, emergency), CAB structure, the Change Schedule, and how change enablement integrates with DevOps continuous delivery. Essential for the change management exam section.

**3. Atlassian — Root Cause Analysis Techniques**
<https://www.atlassian.com/incident-management/incident-response/root-cause-analysis>
A practitioner guide covering the 5 Whys, fishbone diagram, and fault tree analysis techniques used in Problem Management. Includes worked examples from IT incident scenarios that directly apply to this module's RCA exercises.

---

Module 09 Reading Guide | CIS-4335 IT Service Management | Texas Wesleyan University
