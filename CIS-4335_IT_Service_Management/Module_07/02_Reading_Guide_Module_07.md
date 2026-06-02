# Reading Guide: Module 07 — Service Management Practices: Change Enablement

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** ITIL 4 Foundation

---

## Purpose of This Guide

This reading guide supports Module 07 of CIS-4335. Change Enablement is one of the most frequently tested ITIL 4 Foundation topics. The three change types, the role of the CAB, and the relationship between Change Enablement and Deployment Management appear on the exam in multiple scenario forms. Master every concept in this guide before attempting the quiz or lab.

---

## 1. Purpose of Change Enablement

The purpose of Change Enablement is to maximize the number of successful IT and service changes by ensuring that risks are properly assessed, authorizing changes to proceed, and managing the change schedule.

Key points about this purpose statement:

* The goal is to maximize successful changes — not to minimize the number of changes
* Risk assessment is required before authorization
* Authorization is a formal governance activity, not a rubber stamp
* The change schedule is an explicit output of the practice

---

## 2. Definition of a Change

A change is the addition, modification, or removal of anything that could have a direct or indirect effect on services.

This definition is intentionally broad. Changes include software deployments, configuration updates, infrastructure modifications, process changes, and documentation revisions — anything that touches a service or its supporting components.

---

## 3. The Three Change Types

| Change Type | Definition | Authorization | Examples |
|---|---|---|---|
| Standard | Pre-authorized, low-risk, well-understood, follows documented procedure | Pre-authorized — no individual review per occurrence | Password reset, user account provisioning, routine security patch from approved list |
| Normal | Requires individual risk assessment and authorization | Appropriate change authority; CAB advisory input for high-risk items | OS upgrade, network reconfiguration, major application deployment |
| Emergency | Must be implemented immediately to resolve a major incident or prevent critical failure | Expedited — ECAB or senior authority; full documentation after | Zero-day vulnerability patch, emergency rollback, critical routing change |

### Standard Changes in Depth

Standard changes are pre-authorized as a class of change, not as individual instances. Before a change type is classified as standard, the change authority must:

* Document the complete procedure
* Assess and accept the associated risks
* Formally pre-authorize the change type

Once pre-authorized, individual occurrences of that change type may proceed without additional review. The pre-authorization review is the governance — each execution simply follows the approved procedure.

### Normal Changes in Depth

Normal changes are the largest category. Each normal change requires its own risk assessment and authorization. Key considerations:

* Risk level determines who authorizes — a low-risk normal change may require only a single IT manager; a high-risk change may require senior leadership and CAB advisory input
* The change record must document scope, risk assessment, rollback plan, and implementation window
* The change schedule records the planned date and coordinates with other changes

### Emergency Changes in Depth

Emergency changes are not a license to skip governance. They are a mechanism for expedited governance. Key requirements:

* Authorization must still be obtained — before implementation when at all possible, or as close to implementation as possible in genuine time-critical situations
* The Emergency CAB or a designated senior authority provides the expedited authorization
* Full documentation must follow implementation
* A post-implementation review assesses whether the emergency was handled appropriately

---

## 4. The Change Advisory Board (CAB)

| Aspect | Detail |
|---|---|
| What it is | An advisory body that supports the change authority |
| What it does | Reviews and makes recommendations on high-risk or high-impact normal changes |
| Authorization power | None — the CAB advises; the change authority authorizes |
| Membership | Varies by change; includes subject-matter experts relevant to the change under review |
| When it convenes | For high-risk or high-impact normal changes; not required for all normal changes |
| Emergency variant | Emergency CAB (ECAB) — smaller, on-call group for expedited emergency change authorization |

The single most important CAB concept for the exam: the CAB advises. The change authority authorizes. These are not the same thing.

---

## 5. The Change Schedule

The change schedule is a document that lists all authorized changes and their planned implementation dates.

Purposes of the change schedule:

* Coordinates planned changes to prevent conflicts (two changes to the same system at the same time)
* Communicates upcoming changes to affected stakeholders
* Allows the service desk to anticipate potential service disruptions and prepare
* Provides a baseline for post-implementation review — what was planned versus what occurred
* Identifies blackout periods — times when changes should not be scheduled due to business events or other constraints

---

## 6. Change Enablement and Related Practices

| Relationship | Change Enablement Role | Other Practice Role |
|---|---|---|
| Deployment Management | Authorizes the change; determines what and when | Executes the physical move into the live environment |
| Release Management | Authorizes individual changes that make up a release | Groups changes into releases; manages sequencing and scheduling |
| Service Configuration Management | Uses configuration data to assess risk and identify dependencies | Maintains accurate records of configuration items and their relationships |
| Incident Management | Emergency changes may be triggered by major incidents | Incident Management resolves the incident; Change Enablement governs the fix |
| Problem Management | Problem investigations may identify changes needed to eliminate root causes | Problem Management identifies the need; Change Enablement governs the change |

The Change Enablement / Deployment Management distinction is the most commonly tested relationship. Change Enablement is governance (assessment and authorization). Deployment Management is execution (moving the change into production).

---

## 7. Guiding Principles Applied to Change Enablement

| Principle | Application to Change Enablement |
|---|---|
| Focus on Value | Every change should trace back to a business outcome; changes without value add risk without benefit |
| Progress Iteratively with Feedback | Decompose large changes into smaller increments; assess and review after each stage |
| Keep It Simple and Practical | Match the authorization process to the level of risk; do not apply heavyweight governance to low-risk standard changes |
| Optimize and Automate | Automate standard changes to reduce human error and free capacity for high-risk decisions |
| Think and Work Holistically | Consider the full impact of a change across all services, systems, and stakeholders |

---

## 8. ITIL v3 vs. ITIL 4 Terminology

| ITIL v3 Term | ITIL 4 Term | Key Difference |
|---|---|---|
| Change Management (process) | Change Enablement (practice) | "Practice" is broader than "process" — includes people, partners, tools, and information |
| Change Manager | Change authority (role) | ITIL 4 uses role-based language rather than job title |
| RFC (Request for Change) | Change request | Conceptually similar; ITIL 4 language is more accessible |
| Forward Schedule of Changes (FSC) | Change schedule | Same concept; updated terminology |

---

## 9. ITIL 4 Foundation Exam Tips

1. **Memorize the three change types.** Know the definition, the authorization model, and an example for each. Expect scenario questions that ask you to classify a described change.

2. **The CAB advises; it does not authorize.** This is the single most tested CAB concept. Any answer choice saying the CAB approves or authorizes a change is wrong.

3. **Emergency changes still require authorization.** The exam will offer answer choices that say emergency changes can be implemented without authorization. Those are wrong. The process is expedited, not eliminated.

4. **Change Enablement vs. Deployment Management.** If the scenario describes assessing risk and deciding whether to proceed, that is Change Enablement. If the scenario describes physically deploying software or rolling out a configuration to production systems, that is Deployment Management.

5. **Standard changes are pre-authorized as a class.** The authorization happens once when the change type is established. Individual occurrences do not require new authorization.

6. **The change schedule prevents conflicts.** If a question describes coordinating timing of changes or communicating planned changes to stakeholders, the answer involves the change schedule.

7. **Change Enablement is preventive governance, not reactive recovery.** If the scenario describes restoring service after a disruption, that is Incident Management.

8. **ITIL 4 uses "practice" not "process."** Change Management is ITIL v3 language. The exam will not penalize you for thinking in process terms, but the correct ITIL 4 answer uses "practice."

---

## 10. Key Terms Glossary

**Change** — The addition, modification, or removal of anything that could have a direct or indirect effect on services.

**Change authority** — The individual or group with the power to authorize a change to proceed.

**Change Advisory Board (CAB)** — A group that provides advisory support to the change authority by reviewing and recommending on high-risk or high-impact normal changes.

**Change Enablement** — The ITIL 4 practice whose purpose is to maximize the number of successful IT and service changes by ensuring risks are properly assessed, authorizing changes to proceed, and managing the change schedule.

**Change record** — A document that captures the details of a change, including scope, risk assessment, rollback plan, implementation window, and authorization.

**Change schedule** — A document listing all authorized changes and their planned implementation dates.

**Emergency change** — A change that must be implemented as quickly as possible to resolve a major incident or prevent a critical service failure.

**Emergency CAB (ECAB)** — A smaller, on-call group of senior decision-makers who can be convened quickly to provide expedited authorization for emergency changes.

**Normal change** — A change that requires individual risk assessment and authorization before implementation.

**Standard change** — A pre-authorized, low-risk, well-understood change that follows a documented procedure and does not require individual authorization per occurrence.

---

## 11. Required Resources

* ITIL 4 Foundation official resources: axelos.com
* Module 07 video lecture (Professor Nash, approximately 20–24 minutes)

---

## 12. Study Checklist

* [ ] Watch the Module 07 video lecture in full.
* [ ] Write the definition of a change from memory.
* [ ] List the three change types and the authorization model for each.
* [ ] Explain the role of the CAB in your own words — specifically what it does and does not do.
* [ ] Describe the difference between Change Enablement and Deployment Management.
* [ ] Describe the purpose of the change schedule.
* [ ] Apply the three change types to five real-world IT scenarios.
* [ ] Review the exam tips and identify which concepts need reinforcement.
* [ ] Complete the Module 07 Lab Activity.
* [ ] Take the Module 07 Quiz.
* [ ] Post your initial discussion response by Wednesday at 11:59 PM.
* [ ] Reply to at least two classmates by Sunday at 11:59 PM.
