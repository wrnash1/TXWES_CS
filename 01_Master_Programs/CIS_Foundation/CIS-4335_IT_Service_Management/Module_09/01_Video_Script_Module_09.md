# Video Script: Module 09 — Problem and Change Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: ITIL 4 Foundation

---

## Introduction (0:00–1:30)

Welcome to Module 09. I'm Professor Nash. In the last module we talked about putting out
fires — Incident Management is all about restoring service fast. Today we talk about
preventing the fires from starting, and about making controlled changes safely.

This module covers two practices that work hand in hand:

- **Problem Management** — finding and eliminating the root causes of incidents
- **Change Enablement** — ensuring that modifications to services and infrastructure
  are authorized, tested, and deployed safely

[SHOW DIAGRAM: Incident → Problem → Change cycle]

These practices are among the top-tested areas on the ITIL 4 Foundation exam, and they
are among the most misunderstood in real IT organizations. By the end of this module you
will be able to distinguish reactive from proactive problem management, explain the known
error database, describe root cause analysis techniques, classify the three change types,
explain the CAB, and describe how the change schedule works.

[PAUSE]

---

## Section 1: Problem Management Fundamentals (1:30–5:00)

### What Is a Problem?

ITIL 4 defines a **problem** as a cause, or potential cause, of one or more incidents.
Read that carefully: the cause OR POTENTIAL cause. Problems can be identified reactively
after incidents occur, or proactively before any incident happens.

[SHOW DIAGRAM: Problem as root cause feeding multiple incidents]

The key distinction from incidents:

- **Incident goal:** Restore service fast — root cause is irrelevant in the moment
- **Problem goal:** Find the root cause and eliminate it — speed is less important than
  accuracy

### Reactive vs. Proactive Problem Management

**Reactive problem management** is triggered by incidents. One or more incidents occur,
and a problem record is raised to investigate why they happened. This is the most common
entry point for problem management.

Examples of reactive triggers:

- A P1 incident is resolved — the Post-Incident Review raises a problem record
- The same P3 incident recurs three times in a month — a problem record is raised
- Incident trend analysis shows 30% of tickets involve a specific application

**Proactive problem management** identifies potential problems before any incident occurs.
It is driven by:

- Infrastructure reviews and health assessments
- Trend analysis on monitoring data
- Vendor security bulletins and known vulnerabilities
- Architecture reviews that identify single points of failure

[PAUSE]

Proactive problem management is harder to prioritize — there is no burning fire demanding
attention. But it delivers the highest value by preventing incidents that would have
otherwise occurred.

---

## Section 2: The Problem Lifecycle (5:00–9:00)

### Problem Lifecycle Stages

[SHOW DIAGRAM: Problem lifecycle — Problem Identification → Categorization → Prioritization → Investigation → Known Error → Change/Resolution → Closure]

1. **Problem Identification** — A problem record is created, either from an incident,
   a pattern, or proactive analysis. The problem is distinct from any individual incident.

2. **Problem Categorization** — The problem is categorized by affected service, component,
   technology domain, and business impact.

3. **Problem Prioritization** — Priority is assigned based on the potential impact and
   frequency of associated incidents. A problem affecting a P1-level service is
   prioritized higher than one affecting a P5 service.

4. **Problem Investigation and Diagnosis** — Root cause analysis (RCA) is performed.
   This is the analytical heart of Problem Management.

5. **Known Error Identification** — When a root cause is identified and a workaround is
   available, the problem becomes a **known error**. The known error is documented in
   the Known Error Database (KEDB).

6. **Resolution** — A permanent fix is identified. A change record is raised to implement
   it. The problem is not closed until the change is deployed and verified.

7. **Problem Closure** — After resolution is confirmed, the problem record is closed.
   The KEDB entry is updated to reflect the permanent fix.

[PAUSE]

### The Known Error Database (KEDB)

The KEDB is a repository of known errors — problems where the root cause has been
identified and a workaround is documented. It is one of the most valuable operational
tools in IT service management.

[SHOW DIAGRAM: KEDB structure — Problem ID, Description, Root Cause, Workaround, Status, Change Record link]

When a service desk agent receives an incident, they check the KEDB first. If a known
error matches, they can apply the documented workaround immediately — cutting resolution
time dramatically.

Key point: a known error is not fixed yet. The workaround reduces impact, but the
permanent fix still requires a change. The KEDB bridges the gap between "we know what's
wrong" and "we've permanently fixed it."

---

## Section 3: Root Cause Analysis Techniques (9:00–12:00)

Problem Management lives or dies on the quality of root cause analysis. ITIL 4 does not
prescribe a specific RCA technique — organizations choose based on context. Here are the
most important ones you need to know.

[SHOW DIAGRAM: RCA techniques overview]

### The 5 Whys

Start with the symptom and ask "Why?" five times. Each answer becomes the next question.

Example:

- Why did the database fail? — The disk was full.
- Why was the disk full? — Log files were not being purged.
- Why were log files not being purged? — The automated log cleanup job failed.
- Why did the cleanup job fail? — A configuration change broke the job schedule.
- Why was the configuration change not tested? — No change management process was followed.

Root cause: absence of a change management process. The fix is not "clear the disk" —
the fix is to implement change management and repair the cleanup job configuration.

[PAUSE]

### Fishbone Diagram (Ishikawa)

The fishbone diagram maps causes across multiple categories — People, Process, Technology,
Environment — to the central problem effect. It is particularly useful when causes are
complex and multidimensional.

[SHOW DIAGRAM: Fishbone diagram with four cause categories]

### Fault Tree Analysis

A top-down logical diagram that models how component failures combine to produce a system
failure. Used for high-complexity, safety-critical systems.

### Timeline Analysis

Reconstructing the sequence of events leading to the incident — useful for major incidents
where multiple changes or events contributed. The war room scribe's notes are invaluable here.

---

## Section 4: Change Enablement — Fundamentals (12:00–15:00)

### What Is a Change?

ITIL 4 defines a **change** as the addition, modification, or removal of anything that
could have a direct or indirect effect on services.

[SHOW DIAGRAM: Change scope — hardware, software, process, documentation, contracts, supplier agreements]

The key word is "anything." A change is not just a server upgrade. Updating a firewall
rule, modifying an SLA, replacing a supplier, changing a process document — these are
all changes that require management.

### The Three Change Types

ITIL 4 categorizes changes into three types:

[SHOW DIAGRAM: Three change types — Standard, Normal, Emergency]

**Standard Change:**

- Pre-authorized; follows a documented, tested procedure
- Low risk; well understood; occurs frequently
- Examples: password reset enablement, routine OS patch via pre-approved maintenance
  window, adding an existing user to a distribution group
- No CAB review required; pre-approved by the organization

**Normal Change:**

- Requires assessment, authorization, and scheduling before implementation
- Goes through the Change Advisory Board (CAB) for review
- Can be routine or significant — the key is that it needs evaluation
- Examples: deploying a new application, upgrading database software, major network
  reconfiguration

**Emergency Change:**

- Must be implemented as soon as possible due to urgent business need
- Usually triggered by a P1 incident requiring an immediate configuration fix
- Assessment and authorization are accelerated but not skipped — an Emergency CAB
  (ECAB) or pre-authorized senior approver reviews it
- Full documentation and PIR required after implementation
- Examples: hotfix to restore a critical service, emergency firewall rule to block
  an active exploit

[PAUSE]

---

## Section 5: The Change Advisory Board and Change Schedule (15:00–18:30)

### The Change Advisory Board (CAB)

The CAB is a group that supports the authorization and planning of normal changes. It is
not a bureaucratic gatekeeping body — its purpose is to bring diverse expertise together
to assess risk and coordinate deployment.

[SHOW DIAGRAM: CAB composition — IT, Business, Security, Operations, Applications, Supplier representatives]

Typical CAB participants:

- IT Service Manager (chair)
- Infrastructure and operations representatives
- Application team representatives
- Security and compliance representative
- Business stakeholder representatives
- Supplier/vendor representatives as needed

The CAB reviews change requests and assesses:

- Technical risk (what could go wrong?)
- Business impact (who is affected, when?)
- Rollback plan (how do we undo this if it fails?)
- Deployment timing (does it conflict with business events, other changes?)
- Testing evidence (has this been validated?)

[PAUSE]

### Emergency CAB

For emergency changes, the full CAB cannot be assembled quickly enough. The ECAB is a
smaller, pre-designated group with authority to approve emergency changes on behalf of
the full CAB. Typical membership: IT Director, Security Lead, and the relevant technical
lead.

### The Change Schedule (Forward Schedule of Change)

The change schedule — also called the Forward Schedule of Change — is the authorized
timeline of all approved changes. Its purposes:

- Prevents change collisions (two changes affecting the same system on the same night)
- Enables business planning (users and stakeholders know when changes are happening)
- Coordinates maintenance windows across teams
- Provides a historical record for post-incident correlation

[SHOW DIAGRAM: Change schedule as a Gantt-style timeline with change windows marked]

When a P1 incident occurs, one of the first questions in the war room is: "What changes
were deployed in the last 48 hours?" The change schedule answers that question
immediately.

---

## Section 6: Problem and Change Working Together (18:30–20:00)

Problem Management and Change Enablement have a direct handoff relationship:

[SHOW DIAGRAM: Problem → Known Error → Change Request → Change Implementation → Problem Closure]

1. Problem Management identifies root cause
2. A permanent fix is designed
3. A change record is raised (standard, normal, or emergency depending on urgency)
4. The CAB reviews and approves the change
5. The fix is deployed
6. Problem Management verifies the fix resolved the root cause
7. The problem record is closed; the KEDB entry is updated

Without Change Enablement, Problem Management cannot implement fixes safely. Without
Problem Management, Change Enablement has no strategic driver — changes happen reactively
without addressing systemic causes.

[PAUSE]

---

## Module Summary and Exam Tips (20:00–22:00)

Module 09 covered two critical ITIL 4 practices.

**Problem Management** addresses the root cause of incidents. It operates reactively
(triggered by incidents) and proactively (identifying risks before incidents occur). The
lifecycle moves from identification through investigation to known error documentation
and eventual resolution via a change. The KEDB stores known errors with their workarounds.

**Change Enablement** governs modifications to services. The three change types are
Standard (pre-authorized), Normal (CAB review required), and Emergency (accelerated
authorization for urgent situations). The CAB assesses risk and coordinates timing. The
change schedule prevents conflicts and enables planning.

[SHOW DIAGRAM: Summary table — Problem Management lifecycle and Change type comparison]

For the ITIL 4 Foundation exam:

- Know the definition of a problem (cause or potential cause of incidents)
- Know the difference between reactive and proactive problem management
- Know what a known error is and the purpose of the KEDB
- Know the three change types and when each is used
- Know the purpose of the CAB
- Know that Emergency changes still require authorization (just accelerated)

[PAUSE]

Module 10 covers Service Level Management and SLAs — how IT makes and keeps promises to
stakeholders. See you there.

---

End of Module 09 Video Script

Estimated delivery: 22 minutes at average instructional pace
