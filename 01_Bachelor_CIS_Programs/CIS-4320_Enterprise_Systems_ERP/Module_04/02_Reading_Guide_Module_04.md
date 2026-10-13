# Reading Guide: Module 04 - ERP Implementation Lifecycle

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4320 &BULL; ENTERPRISE SYSTEMS & ERP ARCHITECTURE</text>
    
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


## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Introduction

ERP implementations are among the most complex organizational undertakings in business. They touch every department, change how people do their jobs, require massive data migration, and cost millions of dollars. Understanding the implementation lifecycle — the phases, the roles, the risks, and the quality gates — is essential for anyone working in enterprise systems. This module covers the SAP Activate methodology, the Salesforce implementation approach, change management, testing phases, data migration basics, go-live, and hypercare.

---

## Section 1: High-Yield Glossary

**SAP Activate**
SAP's official implementation methodology for S/4HANA, built on agile delivery principles, Fit-to-Standard process design, and continuous testing. SAP Activate has six phases: Discover, Prepare, Explore, Realize, Deploy, and Run.

**Fit-to-Standard**
SAP's recommended approach where the company's processes are adapted to match SAP's standard processes rather than customizing SAP to match the company. Reduces implementation cost and upgrade risk. Fit-to-Standard workshops are the primary activity of the SAP Activate Explore phase.

**Delta Design Document**
The output of the Explore phase Fit-to-Standard workshops. It documents all gaps between standard SAP functionality and the company's requirements and records the decision for each gap: process adaptation, system configuration, or custom development.

**Change Management**
The organizational discipline of preparing, enabling, and supporting people through a significant change. In ERP implementations, change management addresses resistance to new workflows, system adoption, and the behavior change required for the new system to deliver its intended business value.

**Stakeholder**
Any person, group, or organization affected by, interested in, or able to influence the ERP implementation. Active stakeholder engagement — especially from senior leadership — is a critical change management activity.

**Super-User**
A departmental employee who receives advanced training on the ERP system and serves as a first-line coach and support resource for colleagues after go-live. Super-users bridge the gap between IT support and frontline workers and are more trusted by colleagues than outside consultants.

**User Acceptance Testing (UAT)**
The final testing phase before go-live, conducted by real business users executing their actual work scenarios in the configured system. UAT verifies that the system meets operational requirements. Business user sign-off on UAT is the formal approval to proceed to go-live.

**Unit Testing**
Testing individual configuration components or custom code in isolation to verify they function as designed. Unit testing is IT-led and is the first quality check in the testing progression.

**Integration Testing**
Testing of end-to-end process scenarios that cross multiple modules or systems to verify they work correctly together. Integration testing validates that inter-module data flows and system integrations produce correct results.

**Performance Testing**
Testing under peak load conditions to validate that system response times and throughput remain acceptable when processing realistic transaction volumes. Critical for high-volume periodic processes like payroll, MRP runs, and financial period closes.

**Data Migration**
The process of moving data from legacy systems into the new ERP using the ETL (Extract, Transform, Load) cycle. Migration requires data cleansing to ensure quality, validation to confirm completeness, and a rollback plan in case critical errors are discovered during cutover.

**ETL (Extract, Transform, Load)**
The three-step data migration process. Extract: pull data from the legacy source system. Transform: clean, reformat, deduplicate, and map data to the target system's schema and business rules. Load: write the transformed data into the target ERP.

**Cutover**
The precisely managed sequence of steps executed during the final go-live weekend: legacy system freeze, final data extraction and load, migration validation, UAT confirmation, legacy system lockout, and new system activation.

**Hypercare**
The intensive post-go-live support period (typically 2-8 weeks) during which the full project team remains available to resolve issues quickly. Hypercare ends when defined exit criteria are met and the system transitions to normal operations support.

**Rollback Plan**
A documented contingency procedure for reverting to the legacy system if critical errors are discovered during cutover validation that cannot be resolved within the go-live window.

---

## Section 2: SAP Activate Phase Reference

| Phase | Primary Activities | Key Deliverable | Who Leads |
|---|---|---|---|
| Discover | Solution evaluation, business case, SAP Best Practice review | Project business case, initial scope | Business sponsor, SAP pre-sales |
| Prepare | Project governance, team formation, landscape setup, PMO | Project plan, system landscapes, risk register | Project Manager |
| Explore | Fit-to-Standard workshops, gap analysis, process design | Delta design document, gap list, approved TO-BE processes | Functional consultants, business process owners |
| Realize | System configuration, custom development, data migration programs, integration build, unit and integration testing | Configured system, tested components, migration scripts | Functional and technical consultants |
| Deploy | User training, data migration execution, UAT, cutover planning and execution | Trained users, migrated data, go-live sign-off | Deployment lead, change management team |
| Run | Hypercare, ongoing operations, continuous improvement, future wave planning | Stable production system, optimized processes | Operations team, internal center of excellence |

### SAP Activate — Fit-to-Standard Workshop Structure

```text
[Business Process Owner presents current process]
                    |
[SAP Consultant demonstrates standard SAP process]
                    |
          [Comparison and Discussion]
                    |
        [XOR: Standard covers requirement?]
               |            |
             YES             NO
               |             |
  [Document as standard]  [Document gap]
                               |
              [Decision: Adapt process? Configure? Customize?]
                    |              |              |
             [Best option]   [Acceptable]   [Last resort]
```

---

## Section 3: Testing Phase Progression

### Testing Hierarchy

```text
[Performance Testing]     -- Technical, load/stress validation
        |
[User Acceptance Testing] -- Business users, real scenarios, formal sign-off
        |
[Integration Testing]     -- Functional team, end-to-end cross-module
        |
[Unit Testing]            -- IT/functional, individual components
```

Higher levels of testing do not replace lower levels — they build on them. A defect found at the unit level costs a fraction of one found at UAT, which costs a fraction of one found after go-live.

### UAT Best Practices

- Business users (not IT) run the test scenarios
- Scenarios must mirror real business workflows, not abstract system checks
- Test data must be representative of production data volumes and complexity
- Defects are logged in a formal tracking system with severity ratings
- UAT is complete only when all Critical and High severity defects are resolved and closed
- Formal sign-off document is signed by business process owners before go-live proceeds

### Defect Severity Classification

| Severity | Definition | Go-Live Decision |
|---|---|---|
| Critical | System-wide failure; core business process cannot execute | Must fix before go-live |
| High | Key function broken; significant workaround required | Must fix before go-live |
| Medium | Non-critical function affected; acceptable workaround exists | Fix in first post-go-live release |
| Low | Minor display or cosmetic issue; no business impact | Fix in planned update |

---

## Section 4: Change Management Framework

### The ADKAR Model (Applied to ERP)

ADKAR is one of the most widely used change management frameworks in ERP projects:

| ADKAR Element | ERP Application |
|---|---|
| Awareness | Why is the company changing ERP? What problem does it solve? |
| Desire | What's in it for me? How will the new system make my job better? |
| Knowledge | How do I use the new system to do my specific job? |
| Ability | I can actually perform my job tasks in the new system (demonstrated in practice) |
| Reinforcement | Leadership recognizes and rewards use of the new system; old behaviors are not tolerated |

### Common Change Management Failures in ERP Projects

| Failure Mode | Symptom | Consequence |
|---|---|---|
| No executive sponsorship | Leadership does not mention the project; no consequences for non-adoption | Employees deprioritize training and adoption |
| Training too late, too technical | Training delivered 1 week before go-live; focuses on software clicks not business processes | Users cannot perform their jobs in the new system on day one |
| No super-user network | Only consultants available for post-go-live support | Long support queues; employees revert to old tools |
| Communication blackout | Employees receive no updates between kick-off and go-live | Rumors, fear, and resistance grow |
| Big bang without parallel run | Legacy system turned off immediately; no fallback | Critical failures have no immediate recovery path |

---

## Section 5: Data Migration Planning

### The ETL Cycle

```text
[Source System(s)]
       |
   [EXTRACT]
  Raw data pulled as-is from legacy systems
  (exports, APIs, direct database queries)
       |
  [TRANSFORM]
  Data cleansing: deduplication, format standardization
  Field mapping: source field → target field
  Enrichment: adding required fields missing in source
  Validation rules: business logic checks before load
       |
    [LOAD]
  Data written to target ERP via import tools
  (SAP LSMW/BAPI, Salesforce Data Loader)
       |
  [VALIDATE]
  Record count reconciliation
  Sample record quality review
  Business process smoke testing with migrated data
```

### Migration Waves

Most ERP implementations migrate data in waves corresponding to go-live scope:

- Wave 1 (before go-live): Master data — vendor masters, customer masters, material masters, chart of accounts
- Wave 2 (go-live weekend): Open transactional data — open purchase orders, open sales orders, open invoices, current inventory balances
- Wave 3 (post-go-live): Historical data — closed transactions for reporting and analytics

Historical data migration is often deferred to after go-live to reduce go-live risk.

---

## Section 6: Go-Live Readiness Checklist

Before any ERP system goes live, the following gates must pass:

- All Critical and High UAT defects are resolved and closed
- UAT formal sign-off documents are signed by all business process owners
- Data migration validation confirms record counts match source and no critical fields are blank
- User training completion rate meets the defined threshold (typically 90%+)
- Support model is in place: helpdesk procedures, escalation paths, super-user schedule
- Rollback plan is documented and all team members know their roles
- System performance tests pass under peak load conditions
- Integration tests confirm all connected systems exchange data correctly
- Cutover runbook is complete with step-by-step instructions, owner for each step, and estimated times

---

## Section 7: Salesforce Implementation Lifecycle

| Phase | Key Activities | Primary Tools |
|---|---|---|
| Discovery | Stakeholder interviews, process mapping, requirements documentation | Interviews, BPMN diagrams |
| Design | Object model design, security model, integration architecture, UX wireframes | Data model diagrams, profile/permission matrix |
| Build | Custom objects/fields, validation rules, flows, approval processes, integration | Salesforce Setup, Flow Builder |
| Test | Unit testing, integration testing, UAT | Sandbox environment, test scripts |
| Deploy | Change set deployment to production, user training, go-live | Change sets, Salesforce Deploy |
| Hypercare | Defect triage, user support, rapid fixes | Salesforce Cases, monitoring dashboards |

Salesforce sandbox environments are the primary staging and testing environments. The sandbox types used in implementations are:

- **Developer sandbox:** Individual developer testing; refreshed on demand
- **Developer Pro sandbox:** Larger developer sandbox for integration testing
- **Partial Copy sandbox:** Includes a representative sample of production data; used for UAT
- **Full sandbox:** Complete copy of production data and configuration; used for final UAT and cutover rehearsal

---

## Section 8: Certification Exam Tips

1. **SAP Activate phase names and activities are directly tested.** Memorize: Discover (business case), Prepare (project setup), Explore (Fit-to-Standard workshops), Realize (build), Deploy (go-live), Run (operations). The Explore-Fit-to-Standard pairing is the most commonly tested fact.

2. **UAT is business-user-led, not IT-led.** When an exam question asks who conducts UAT, the answer is always business users, not developers or consultants. UAT sign-off is also business-led.

3. **Change management failure is the most common cause of ERP project failure — not technical failure.** When exam questions describe poor adoption, manual workarounds, or low system usage after go-live, the answer is change management.

4. **Testing follows a sequence: unit → integration → UAT → performance.** Do not skip levels. Each level builds on the previous. Questions may ask which testing type is most appropriate for a described scenario.

5. **Data quality before go-live is non-negotiable.** If a question describes a scenario where the team discovers significant data problems close to go-live, the correct answer is to delay and remediate — not to proceed and fix post-go-live.

6. **Rollback plans are required, not optional.** ERP go-live without a documented rollback plan is a critical project risk. If the go-live fails validation, the team needs a clear path back to the legacy system.

7. **Hypercare is a distinct post-go-live phase with a defined end.** It is not the same as normal operations support. Hypercare has exit criteria; when they are met, the system transitions to steady-state support.

8. **Salesforce sandboxes exist for testing.** Full sandbox is the most production-equivalent; Partial Copy is the standard UAT environment. Developer sandboxes are for unit testing. The sandbox hierarchy is tested on the Salesforce Admin exam and relevant for Associate as well.

---

## Section 9: Required Trailhead and Study Resources

Complete before attempting the quiz:

- **Salesforce Trailhead — Salesforce Developer Experience**
  URL: trailhead.salesforce.com — search "Sandbox Basics"
  Covers Salesforce sandbox types and their use in the implementation lifecycle.

- **Salesforce Trailhead — Change Management Basics**
  URL: trailhead.salesforce.com — search "Change Management"
  Connects Salesforce project best practices to change management principles.

---

## Section 10: Study Checklist

- Memorize the six SAP Activate phases and the primary activity of each.
- Build a mental table: Explore phase → Fit-to-Standard workshops → Delta design document.
- Study the testing progression diagram. Know which type is business-user-led.
- Read through the ADKAR model and connect each element to a specific ERP implementation activity.
- Review the data migration ETL diagram. Know which phase is the most error-prone.
- Study the go-live readiness checklist. Know what "UAT sign-off" means and who provides it.
- Complete the Trailhead Sandbox Basics module.
- Watch the Module 04 video lecture.
- Complete Lab 04.
- Post to Discussion Forum 04 by Wednesday at 11:59 PM.
- Complete Quiz 04 (10 questions).

---

## 9. Supplemental Resources

**1. SAP Learning — SAP Activate Methodology Overview**
<https://learning.sap.com/learning-journeys/implement-sap-s-4hana-cloud-public-edition-with-sap-activate>
Official SAP learning journey covering the full SAP Activate methodology phases, workstreams, and key deliverables. Directly maps to the Explore-Realize-Deploy framework covered in this module and tested on the SAP Associate exam.

**2. Prosci — ADKAR Model for Change Management**
<https://www.prosci.com/methodology/adkar>
The definitive explanation of the ADKAR change management model from Prosci, its developer. Includes case studies on applying ADKAR in ERP implementations and free resources for building awareness and desire among resistant stakeholders.

**3. Salesforce Trailhead — Sandbox Basics**
<https://trailhead.salesforce.com/content/learn/modules/starting_force_com/starting_developer_console>
Covers Salesforce sandbox types (Developer, Developer Pro, Partial Copy, Full) and their role in the implementation lifecycle. Understanding sandbox use in deployment pipelines is tested in both Salesforce Associate and Administrator certification exams.
