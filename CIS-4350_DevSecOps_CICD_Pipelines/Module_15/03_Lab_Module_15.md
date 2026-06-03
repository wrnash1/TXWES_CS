# Lab Activity: Module 15 — Security Champions Program Design and DevSecOps Maturity Assessment

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 90–120 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Overview

In this lab you will perform a structured DevSecOps maturity assessment using the OWASP SAMM framework, design a Security Champion program for a fictional organization, define DORA and security KPIs with target values, and produce an organizational transformation roadmap. This lab is primarily a design and analysis exercise — it mirrors the type of organizational design questions tested on the DSOE exam and builds the practical skills needed to lead DevSecOps adoption in an enterprise environment.

---

### Learning Objectives

By completing this lab you will be able to:

- Apply the OWASP SAMM five business functions to assess a described organization's maturity
- Design a Security Champion program with defined selection criteria, training plan, and governance structure
- Define a DORA + security KPI measurement framework with targets and data sources
- Identify the transformation failure mode present in a described scenario and prescribe corrective actions
- Produce a six-month DevSecOps improvement roadmap prioritized by maturity model gaps

---

### Prerequisites

- Completed reading of Module 15 reading guide
- Familiarity with the OWASP SAMM five business functions and three maturity levels
- Familiarity with DORA metrics and security KPIs from the video lecture
- A text editor or word processor for written deliverables

---

### Lab Structure

This lab has four parts:

- Part 1: SAMM Maturity Assessment
- Part 2: Security Champion Program Design
- Part 3: KPI Framework Definition
- Part 4: Transformation Roadmap

---

### Scenario: Meridian Health Systems

You have been hired as a DevSecOps consultant for Meridian Health Systems, a regional healthcare technology company with 400 engineers across 20 development teams. Meridian builds cloud-native web applications and mobile APIs that handle protected health information (PHI) and are subject to HIPAA technical safeguards.

**Current state:**

- Meridian has one central Application Security team of six engineers
- SAST (Semgrep) and SCA (OWASP Dependency-Check) are deployed to the CI pipeline but set to warn-only — they have never blocked a deployment
- Container image scanning (Trivy) was added six months ago; the finding backlog has grown to 3,200 open items including 140 critical findings that have not been remediated
- There is no formal Security Champion program — one engineer on the payments team informally reviews security PRs when asked
- Security training is a 30-minute annual compliance video; no developer has completed OWASP Top 10 training
- DORA metrics are not tracked; the engineering leadership team does not know the organization's deployment frequency or change failure rate
- The security team reviews deployment requests in a shared email queue; average review time is 4.5 business days
- Three production security incidents in the past 12 months involved CVEs that were present in the Trivy backlog at the time of the incident

---

### Part 1: SAMM Maturity Assessment (30 minutes)

Using the OWASP SAMM five business functions (Governance, Design, Implementation, Verification, Operations) and three maturity levels per practice, assess Meridian's current state.

#### Task 1.1 — Assess Implementation: Secure Build

Using the scenario description, determine Meridian's current SAMM maturity level for the Secure Build practice. Write a one-paragraph justification citing specific evidence from the scenario.

Guiding questions:

- Are security tools deployed? Are they enforced?
- Are findings tracked to closure with defined SLAs?
- Is security debt visible as an engineering metric?

#### Task 1.2 — Assess Verification: Security Testing

Determine Meridian's current SAMM maturity level for the Security Testing practice. Write a one-paragraph justification citing specific evidence from the scenario.

Guiding questions:

- Is security testing automated or manual?
- Is security testing integrated in the pipeline or performed periodically?
- Are security test results tracked and trended?

#### Task 1.3 — Assess Governance: Security Champions and Training

Determine Meridian's current SAMM maturity level for the Education and Guidance practice (part of the Governance function). Write a one-paragraph justification.

Guiding questions:

- Is security training mandatory or optional?
- Is security expertise distributed into development teams?
- Do developers receive contextual security guidance during development?

#### Task 1.4 — SAMM Gap Summary Table

Complete the following table based on your assessments:

| SAMM Practice | Current Level | Target Level (12 months) | Key Gap |
|---|---|---|---|
| Secure Build | | | |
| Secure Deployment | | | |
| Security Testing | | | |
| Education and Guidance | | | |
| Incident Management | | | |

---

### Part 2: Security Champion Program Design (30 minutes)

Design a Security Champion program for Meridian Health Systems.

#### Task 2.1 — Champion Identification Plan

Define the process for identifying Security Champions across Meridian's 20 teams. Your plan must address:

- Selection method (self-nomination, manager nomination, or invitation-based)
- Eligibility criteria (minimum technical experience, time availability requirements)
- Target number of champions across 20 teams with 400 engineers
- Timeline for initial cohort recruitment (Week 1 through Week 8)

#### Task 2.2 — Training Curriculum

Design a 90-day training curriculum for newly onboarded Security Champions. Include:

- Week 1–2: Foundational knowledge (specify topics and resources — OWASP, SANS, or equivalent)
- Week 3–6: Hands-on skills (specify lab exercises — CTF, WebGoat, or equivalent)
- Week 7–10: Pipeline integration skills (specify what champions will learn about Meridian's specific tools)
- Week 11–12: Assessment and certification (describe how completion is verified)

#### Task 2.3 — Champion Authority and Governance

Define the formal authorities and responsibilities of Meridian Security Champions:

- What types of pull requests require Champion review?
- How does a Champion escalate a finding they cannot resolve independently?
- What is the Champion's role in sprint planning?
- How often does the champion community meet, and what is the agenda?

#### Task 2.4 — Career Recognition

Describe two concrete career recognition mechanisms for Meridian Security Champions. For each, explain why it is effective at sustaining long-term champion engagement.

---

### Part 3: KPI Framework Definition (20 minutes)

Define the measurement framework Meridian should implement to track DevSecOps program effectiveness.

#### Task 3.1 — DORA Baseline Measurement

Meridian does not currently track DORA metrics. For each of the four DORA metrics, specify:

- What data source at Meridian would provide this measurement (GitHub, Jira, PagerDuty, deployment logs, etc.)
- What Meridian's current estimated value is based on the scenario (estimate with justification)
- What the 12-month target value should be given Meridian's context

Present your answer in a table with columns: Metric, Data Source, Estimated Current Value, 12-Month Target.

#### Task 3.2 — Security KPI Definition

For each of the following security KPIs, define the measurement method, current estimated value, and 12-month target for Meridian:

- Mean Time to Detect (MTTD)
- Mean Time to Remediate critical findings (MTTR-Security)
- Critical Finding Escape Rate
- Security Gate Pass Rate

#### Task 3.3 — Dashboard Design

Describe a security metrics dashboard for Meridian's engineering leadership. For each panel in the dashboard, specify: metric displayed, visualization type (trend line, gauge, table, etc.), alert threshold, and audience (team level vs. leadership level).

Your dashboard must include at least six panels.

---

### Part 4: Transformation Roadmap (20 minutes)

#### Task 4.1 — Failure Mode Identification

Review the Meridian scenario and identify which of the three DevSecOps transformation failure modes are present. For each failure mode present, cite specific evidence from the scenario and prescribe the corrective action.

Failure modes to evaluate:

- Security as bottleneck
- Tool accumulation without process
- Security theater

#### Task 4.2 — Six-Month Roadmap

Produce a six-month transformation roadmap for Meridian. Structure the roadmap as a table with columns: Month, Initiative, SAMM Practice Impacted, Expected KPI Impact, Owner (role, not name).

Your roadmap must:

- Include at least one initiative per month
- Address all three failure modes identified in Task 4.1
- Sequence initiatives so that foundational items (process, training) precede dependent items (mandatory gates, expanded tooling)
- Show a plausible trajectory from DSOMM Level 1 to DSOMM Level 2 in six months

#### Task 4.3 — Executive Summary

Write a 200–250 word executive summary addressed to Meridian's CISO. The summary must:

- Describe the current security program maturity using SAMM language
- Identify the three highest-risk gaps
- Present the six-month roadmap at a strategic level
- State the expected improvement in two to three measurable KPIs at the end of six months
- Close with a recommendation for the first action to take

---

### Deliverables

Submit all four parts as a single document. Format requirements:

- Tables formatted as described in each task
- Justification paragraphs of 100–150 words each
- Executive summary of 200–250 words
- Total estimated length: 1,200–1,800 words plus tables

Submit via Canvas LMS before the module deadline.

---

### Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| SAMM Assessment (Part 1) | 25 | Correct level assignments with evidence-based justifications; gap table complete |
| Champion Program Design (Part 2) | 25 | Realistic program with all four components addressed; training curriculum includes OWASP/SANS resources |
| KPI Framework (Part 3) | 25 | All metrics defined with sources, estimates, and targets; dashboard has 6+ panels with correct visualization types |
| Transformation Roadmap (Part 4) | 25 | All three failure modes identified; roadmap is sequenced correctly; executive summary is accurate and professional |
| **Total** | **100** | |
