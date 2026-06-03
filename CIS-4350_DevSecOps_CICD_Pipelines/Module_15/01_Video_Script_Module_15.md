# Video Script: Module 15 — Security Champions and DevSecOps Culture

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 22–26 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–2:30)

Welcome back to CIS-4350. I am Professor Nash. In previous modules we have built the full technical stack of a DevSecOps program: SAST, SCA, container scanning, secrets management, Kubernetes security, OPA policy enforcement, threat modeling, SIEM integration, and compliance as code. Every one of those tools requires engineers to write security configurations, respond to pipeline findings, and make daily decisions that affect your organization's security posture.

But here is the hard truth: tools do not secure software. People do. A security program where only a security team reviews findings will never scale to the speed of modern software delivery. When a central security team of ten engineers is responsible for reviewing the output of five hundred developers, the math does not work. Findings pile up, remediation is delayed, and the security function becomes a bottleneck rather than an accelerator.

This module covers the cultural and organizational side of DevSecOps: how to embed security expertise inside development teams through Security Champion programs, how to train developers to think about security, how to use gamification to make security learning engaging, how to measure both delivery performance and security effectiveness using DORA metrics and security KPIs, how to assess your organization's maturity using DevSecOps maturity models, and how to lead the organizational transformation that makes DevSecOps sustainable.

The DSOE exam tests these topics under the Culture and Organizational Transformation domain. Cultural change is harder to measure than a pipeline configuration, but it is the multiplier that determines whether every other control in this course actually gets implemented and maintained.

---

### SEGMENT 2 — The Security Champion Model (2:30–7:00)

A Security Champion is a developer, DevOps engineer, or QA engineer who has a genuine interest in security and who serves as a security liaison for their team. Champions are not security professionals — they are engineers who bridge the gap between the central security team and their development team.

The Security Champion model was formalized by OWASP in the Software Assurance Maturity Model and has been independently adopted by organizations including Spotify, Google, and the UK's National Cyber Security Centre. The model recognizes that security cannot be owned by a single team — it must be distributed across the organization while remaining coordinated.

A Security Champion program has three structural components.

**Identification and recruitment.** Champions are typically self-selected — engineers who raise security concerns in pull requests, who attend security training voluntarily, or who ask questions about threat modeling. Security teams should actively encourage these engineers rather than waiting for a formal nomination process. Target one champion per team or per eight to ten engineers. Champions do not need to be senior — curiosity and initiative matter more than seniority.

**Training and enablement.** Champions need structured training that goes beyond compliance awareness. Effective champion training covers secure coding for the languages and frameworks used by the team, OWASP Top 10 and how it applies to the team's codebase, how to read and triage SAST and SCA findings, how to conduct a lightweight threat model review, and how to escalate findings to the security team. SANS Secure Coding courses and OWASP's Web Security Testing Guide are the standard training resources aligned with DSOE certification objectives.

**Authority and integration.** Champions must have formal authority within their team's engineering workflow. This means Champions are required reviewers on pull requests that touch authentication, authorization, or data handling. Champions attend sprint planning to flag security requirements. Champions are the first escalation point for pipeline security findings. Champions participate in the security team's weekly champion sync, where they surface emerging issues and receive updated threat intelligence.

The champion model creates a distributed security function that operates at the speed of development teams rather than at the speed of a central security queue. The DSOE exam tests the champion model in organizational design questions: what is the recommended ratio of champions to engineers, what training is appropriate, and how do champions interact with the central security team.

---

### SEGMENT 3 — Developer Security Training (7:00–11:00)

The champion model identifies security-motivated engineers and gives them formal authority. Developer security training extends security awareness to every engineer, not just champions.

**SANS Secure Development training.** SANS offers the SEC542, SEC522, and DEV541 courses focused on web application security, cloud security, and secure DevOps respectively. These courses are intensive and expensive — appropriate for security champions and senior engineers who need deep technical knowledge. The DEV541 course, Secure DevOps and Cloud Application Security, directly aligns with DSOE exam objectives.

**OWASP resources.** OWASP provides free, high-quality training resources that every developer on a team should know: the OWASP Top 10 (updated 2021), the OWASP Application Security Verification Standard (ASVS), the OWASP Testing Guide, and the OWASP Cheat Sheet Series. The OWASP Top 10 is the minimum security awareness baseline — every engineer should understand what injection, broken access control, and cryptographic failures look like in code.

**Security in onboarding.** Organizations that wait until engineers encounter a security finding to train them have already lost. Effective DevSecOps programs integrate security training into engineering onboarding: new engineers complete OWASP Top 10 training in their first week, complete a secure coding module in their first month, and are assigned a Security Champion mentor before they write their first pull request.

**Just-in-time training.** The most effective security training is contextual — delivered at the moment an engineer encounters a real finding. When a SAST tool flags an SQL injection vulnerability, a link to the OWASP SQL Injection cheat sheet in the pipeline failure message is more impactful than a training video watched six months earlier. Tools like Semgrep, Snyk, and Checkmarx support security education annotations that explain findings and link to remediation guidance. This just-in-time model reduces time-to-fix and improves learning retention.

**Measuring training effectiveness.** Training that is not measured is not managed. Track: percentage of developers who have completed baseline security training, number of repeat findings of the same vulnerability type per team (a leading indicator that training is not working), and security champion certification completion rate. Use these metrics to identify teams that need additional support and to demonstrate training program ROI to leadership.

---

### SEGMENT 4 — Gamification and Engagement (11:00–13:30)

Security training competes with every other engineering priority for developer attention. Gamification applies game design principles — points, leaderboards, challenges, and rewards — to security activities to increase engagement and sustain participation over time.

**Capture the Flag (CTF) exercises.** CTFs present engineers with deliberately vulnerable applications and challenge them to find and exploit vulnerabilities. CTFs are highly effective for security champions and developers who want hands-on experience. Platforms like HackTheBox, TryHackMe, and OWASP WebGoat provide structured CTF environments suitable for all skill levels. An organization running a monthly internal CTF with a leaderboard creates healthy competition and surfaces engineers with strong security instincts.

**Bug bounty programs.** Bug bounty programs — both internal and external — incentivize security findings with monetary rewards or recognition. Internal bug bounties allow engineers to earn rewards by finding vulnerabilities in production systems or staging environments before external researchers do. Even a small internal bounty program (gift cards, public recognition, preferred parking) can significantly increase security engagement.

**Security awareness scorecards.** Teams can be scored on security metrics: number of critical findings open beyond SLA, percentage of pipeline runs with zero security gate failures, time-to-remediate by finding severity. Publishing team scorecards (not individual scorecards — team accountability without individual blame) creates positive peer pressure and makes security performance visible to engineering leadership.

**Recognition and career development.** The most sustainable motivator for security champions is recognition and career advancement. Organizations that create a formal Security Champion certification path — with defined skill levels, public recognition, and documented impact on performance reviews — see higher champion retention and engagement than those that treat the role as informal volunteer work.

---

### SEGMENT 5 — DORA Metrics and Security KPIs (13:30–17:30)

DORA — the DevOps Research and Assessment organization — produced the most rigorous large-scale research on software delivery performance. Their four core metrics have become the industry standard for measuring DevOps effectiveness.

**Deployment Frequency** — How often code is deployed to production. Elite performers deploy multiple times per day. This metric reflects both technical capability (pipeline automation) and organizational trust (confidence that the pipeline catches problems before they reach production).

**Lead Time for Changes** — The time from a code commit to that commit running in production. Elite performers achieve less than one day. Long lead times indicate either manual process bottlenecks or slow pipeline stages — including security scans that are not optimized for speed.

**Change Failure Rate** — The percentage of deployments that cause a production incident requiring a hotfix, rollback, or patch. Elite performers achieve less than 15%. Security vulnerabilities that reach production and require an emergency patch appear in this metric — connecting security quality to delivery quality.

**Mean Time to Recovery (MTTR)** — The time to restore service after a production failure. Elite performers recover in less than one hour. Security incidents are a subset of production failures — the SIEM and incident response capabilities from earlier modules directly affect MTTR for security events.

These four metrics collectively measure delivery throughput (deployment frequency, lead time) and delivery stability (change failure rate, MTTR). The key insight from DORA research is that high performers achieve both high throughput AND high stability — they are not in tension.

**Security KPIs layered on DORA.** DevSecOps organizations extend the DORA framework with security-specific metrics:

- **Mean Time to Detect (MTTD)** — The average time between a vulnerability being introduced and its detection. Measures the effectiveness of the scanning pipeline.
- **Mean Time to Remediate (MTTR for Security)** — The average time from finding detection to validated fix in production. Distinguished from DORA MTTR by its focus on security findings rather than service outages.
- **Critical Finding Escape Rate** — The percentage of critical severity findings that reach production without being caught by the pipeline. Should trend to zero.
- **Security Gate Pass Rate** — The percentage of pipeline runs that pass all security gates without human override. High override rates indicate gates that are too noisy or that are blocking valid deployments.
- **Champion Training Completion Rate** — Percentage of designated champions with current training certifications.

The DSOE exam tests these metrics in questions about how to demonstrate DevSecOps program value to leadership and how to identify improvement areas in a pipeline.

---

### SEGMENT 6 — DevSecOps Maturity Models (17:30–21:00)

Maturity models give organizations a structured framework for assessing their current DevSecOps capability and planning improvement roadmaps. They prevent the common failure mode where organizations implement isolated tools without building the processes and culture needed to sustain them.

**OWASP SAMM (Software Assurance Maturity Model)** is the most widely used open-source maturity model for software security. SAMM defines five business functions — Governance, Design, Implementation, Verification, and Operations — each with three practices, each practice with three maturity levels. SAMM provides assessment tools that produce a scored maturity profile across all fifteen practice areas.

In the context of DevSecOps, the SAMM practices most relevant to CI/CD security are:

- **Secure Build (Implementation)** — Covers SAST, SCA, and pipeline security gate requirements. Level 1 is ad hoc scanning; Level 3 is mandatory gates with tracked remediation SLAs.
- **Security Testing (Verification)** — Covers DAST, fuzzing, and penetration testing integration. Level 1 is periodic manual testing; Level 3 is automated security regression tests run on every deployment.
- **Operational Management (Operations)** — Covers secrets management, patch management, and runtime security monitoring. Level 1 is manual processes; Level 3 is fully automated with defined response playbooks.

**DSOMM (DevSecOps Maturity Model)** is a OWASP project specifically designed for DevSecOps pipeline maturity. It defines four levels across dimensions including Build, Deploy, Test, Monitor, and Culture. Level 1 is basic awareness; Level 4 is continuous improvement with automated measurement. DSOMM is the model most closely aligned with DSOE exam objectives.

**Using maturity models.** Organizations should conduct a SAMM or DSOMM assessment annually and use the results to drive a security roadmap. The assessment output identifies which practices are at Level 1 and which are ready to advance to Level 2 or 3. Maturity model assessments also provide defensible evidence for security program investment — showing leadership where the organization stands against industry benchmarks and what investment is required to improve.

---

### SEGMENT 7 — Organizational Transformation (21:00–23:30)

Every technical control in this course requires organizational change to implement. Engineers must change how they write code. Teams must add security review steps to their sprint workflow. Leadership must accept that security gates will occasionally delay deployments and must not pressure teams to override them. These are not technical problems — they are organizational change management problems.

**The three failure modes of DevSecOps transformation:**

**Security as bottleneck.** When the security team owns all findings and all remediation decisions, they become a bottleneck. Development teams perceive security as a blocker rather than an enabler. The fix is to push authority and responsibility to teams: Security Champions own first-level triage, teams own remediation SLAs, the security team owns policy and tooling, not individual findings.

**Tool accumulation without process.** Organizations that install twelve security tools without defining who reviews findings, what the remediation SLA is, or what the escalation path is for critical findings will see tool adoption plateau and finding backlogs grow. Tool acquisition is easy. Process change is hard. DevSecOps transformation must include process design alongside tool deployment.

**Security theater.** When security gates are set to "warn-only" and overrides require no approval, the gates provide no actual security benefit — only the appearance of security. Leadership pressure to ship faster without addressing root causes is the most common driver of security theater. Effective DevSecOps programs have clear policies for when a gate may be overridden, who must approve an override, and how override usage is tracked and reported.

**The organizational transformation model:**

Start with a pilot team — a team with a willing champion, a manageable codebase, and supportive management. Implement the full pipeline there, measure DORA + security KPIs, and build the success story. Use the pilot results to socialize the model to other teams. Champions from the pilot team become the trainers for the next wave.

Expand team by team, not tool by tool. Each team that adopts the full pipeline adds their champion to the network, creates peer pull for adjacent teams, and contributes to the organizational security measurement baseline.

---

### SEGMENT 8 — Wrap-Up (23:30–25:00)

Security Champion programs distribute security expertise to where decisions are made: inside development teams. Developer training, gamification, and just-in-time security education make security accessible to every engineer. DORA metrics and security KPIs provide the measurement framework to demonstrate program value and identify improvement areas. Maturity models — OWASP SAMM and DSOMM — give organizations a roadmap for continuous improvement. Organizational transformation requires addressing the structural failure modes: security as bottleneck, tool accumulation, and security theater.

The DSOE exam tests culture and organizational topics alongside technical pipeline topics. Expect scenario questions about Security Champion program design, which DORA metric reflects security quality, how to use a maturity model to prioritize investment, and how to address organizational resistance to DevSecOps adoption.

In the final module — Module 16 — we consolidate everything across all fifteen modules in preparation for the DSOE certification exam. We will review all exam domains, work through twenty practice questions, and build the mental model for approaching scenario-based exam questions.

See you in Module 16.

---

### PRODUCTION NOTES

- Slide: Security Champion model diagram — Champion role connecting development team to central security team
- Slide: DORA four metrics with elite performer benchmarks
- Slide: Security KPIs layered on DORA (MTTD, MTTR-security, escape rate, pass rate)
- Slide: OWASP SAMM five business functions with maturity level scale
- Slide: DSOMM four levels overview
- Slide: Three failure modes of DevSecOps transformation
- Screen share: OWASP SAMM online assessment tool (https://owaspsamm.org/assessment/)
- Screen share: DSOMM interactive spreadsheet or OWASP DSOMM tool
