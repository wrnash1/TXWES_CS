# Quiz: Module 15 — Security Champions and DevSecOps Culture

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

Instructions: Select the single best answer for each question. Review the distractor analysis after completing the quiz.

---

### Question 1

An organization has 80 development engineers across 10 teams. According to the OWASP Security Champion program model, what is the recommended minimum number of Security Champions, and what is the primary reason for that ratio?

- A) 1 champion total — one centralized champion can coordinate security for all teams through a shared ticket queue
- B) 10 champions (one per team) — the model requires one champion per team so that each team has a security liaison present in its daily workflow and sprint ceremonies
- C) 80 champions (every engineer) — everyone must become a security champion before DevSecOps can be effective
- D) 2–3 champions total — security knowledge should be concentrated in the most senior engineers rather than distributed

Correct Answer: B — The OWASP Security Champion model recommends one champion per team or approximately one per eight to ten engineers. The rationale is that each development team needs a security liaison who is present in that team's daily standup, sprint planning, and code review — not accessible through a shared queue. With 10 teams, 10 champions ensures coverage across all team workflows. A single centralized champion cannot attend 10 teams' ceremonies or triage 80 engineers' findings.

Distractor Analysis:

- Why A is incorrect: A single champion for 80 engineers creates the same bottleneck problem as the centralized security team model. The champion program exists specifically to distribute security responsibility. One champion would be overwhelmed and unable to be present in individual team workflows.
- Why C is incorrect: Not every engineer needs to be a Security Champion. The champion model identifies engineers with security interest and provides them elevated training and authority — it is a distributed specialist model, not a universal certification requirement.
- Why D is incorrect: Concentrating security knowledge in a few senior engineers contradicts the program's distribution goal. Security champions at any seniority level are effective; what matters is curiosity, availability, and team presence.

---

### Question 2

A development team's Security Champion is reviewing a sprint planning meeting. The team plans to add a new integration with a third-party payment processing API. At what phase should the Champion engage, and what is the most appropriate artifact to produce?

- A) After the feature is deployed to production — so that real traffic can be used to validate the integration's security behavior during a DAST scan
- B) During sprint planning — the Champion should flag the new external integration as a trust boundary crossing and initiate a lightweight threat model before implementation begins
- C) During code review — the Champion should review the pull request implementing the integration for common vulnerabilities like missing input validation and hardcoded API keys
- D) After the SCA scan flags a vulnerable library in the payment SDK — the Champion should then escalate to the security team

Correct Answer: B — A new third-party payment API integration introduces a new trust boundary crossing (data leaving the organization's controlled environment) and a new external entity in the system. These are trigger conditions for threat modeling under the sprint-cadence threat modeling model. The Champion should engage at sprint planning — before implementation — and initiate a lightweight threat model to identify required security controls (mTLS, input validation, secrets management, audit logging of transactions) that will be built into the implementation rather than retrofitted.

Distractor Analysis:

- Why A is incorrect: Engaging post-deployment means any security design flaws (insufficient authorization, missing audit logging, improper error handling exposing payment data) are already in production. The champion's highest-value engagement is upstream at design time.
- Why C is incorrect: Code review is valuable and Champions should review the PR — but code review occurs after implementation decisions are made. A Champion who only engages at code review will find implementation-level issues but will miss design-level issues like inadequate scope of authorization or missing audit logging architecture.
- Why D is incorrect: Waiting for an SCA finding means the integration is already implemented and deployed. Dependency vulnerabilities in the payment SDK may exist from day one; the Champion's role is proactive, not reactive to tool alerts.

---

### Question 3

An engineering organization tracks four DORA metrics and reports the following values: Deployment Frequency = once per week; Lead Time for Changes = 3 days; Change Failure Rate = 22%; Mean Time to Recovery = 4 days. A security incident caused by a critical CVE that reached production — which should have been blocked by the SCA gate — contributed to two production incidents this quarter. Which DORA metric most directly reflects the security pipeline's failure to prevent these incidents?

- A) Deployment Frequency — because deploying once per week is too infrequent to catch security issues quickly
- B) Lead Time for Changes — because the 3-day lead time means security fixes take too long to reach production
- C) Change Failure Rate — because security incidents that require emergency hotfixes or rollbacks are counted as deployment failures in the Change Failure Rate metric
- D) Mean Time to Recovery — because the 4-day recovery time indicates the security team is understaffed and cannot respond to incidents quickly enough

Correct Answer: C — Change Failure Rate measures the percentage of deployments that result in degraded service requiring remediation. Security incidents caused by vulnerabilities reaching production — and requiring emergency patches, hotfixes, or rollbacks — are counted as deployment failures in this metric. At 22%, the organization is in the low-performance band. Two security incidents caused by escaped CVEs directly increased the Change Failure Rate. The SCA gate failure is therefore directly visible in this metric.

Distractor Analysis:

- Why A is incorrect: Deployment frequency affects how quickly security fixes can be deployed once identified, but does not directly measure whether the pipeline is catching vulnerabilities. Low deployment frequency may slow recovery but is not the metric that captures escaped CVEs causing failures.
- Why B is incorrect: Lead Time for Changes measures the speed of delivering changes, including security patches. While a 3-day lead time slows emergency security response, the security pipeline failure — CVEs escaping the SCA gate — is captured in Change Failure Rate, not Lead Time.
- Why D is incorrect: MTTR measures time-to-recover after a failure, which reflects incident response capability. While 4 days is poor MTTR, the question asks which metric reflects the pipeline's failure to prevent the incidents — which is Change Failure Rate, not MTTR. MTTR would improve if incident response improved, not if the SCA gate were fixed.

---

### Question 4

A DevSecOps maturity assessment using DSOMM places an organization at Level 1 for the Culture dimension. The assessment evidence shows: Security Champions exist on two of fifteen teams; security training completion is 15%; no security KPIs are tracked. The organization wants to reach Level 2. Which combination of initiatives most directly advances Culture from Level 1 to Level 2?

- A) Deploy three additional security scanning tools (DAST, IaC scanning, fuzzing) and increase pipeline gate coverage from 40% to 80% of repositories
- B) Identify Security Champions on all 15 teams, provide structured OWASP-based training to all champions, and begin tracking two security KPIs (MTTD and MTTR-Security) in engineering leadership reviews
- C) Hire four additional Application Security engineers to increase the central security team's capacity for finding remediation
- D) Mandate that all engineers complete a 4-hour annual security compliance training before the end of the fiscal year

Correct Answer: B — DSOMM Level 2 for Culture requires Security Champions identified across teams with informal training and basic security KPIs tracked. The initiative described in B directly addresses all three Level 2 criteria: champion coverage across all teams, structured OWASP-based training, and KPI tracking. These are the specific culture-dimension requirements that distinguish Level 1 (ad hoc, no coverage) from Level 2 (structured, distributed, measured).

Distractor Analysis:

- Why A is incorrect: Deploying additional scanning tools advances the Build and Test dimensions of DSOMM, not the Culture dimension. Culture maturity is measured by champion program coverage, training completion, and metric tracking — not tool count or pipeline coverage.
- Why C is incorrect: Hiring more central security engineers increases the central team's capacity but does not address the Culture dimension gaps: champion distribution, training completion, or KPI tracking. A larger central team may actually deepen the bottleneck problem if it reinforces centralized ownership rather than distributed responsibility.
- Why D is incorrect: Mandatory annual compliance training addresses the training gap partially, but a 4-hour annual video does not constitute "structured training" as defined by DSOMM Level 2. DSOMM Level 2 requires role-appropriate training for champions, not generic compliance awareness for all engineers. Additionally, this initiative does not address champion coverage or KPI tracking.

---

### Question 5

An organization's Security Champion reports that the pipeline SAST tool is generating 180 false positive findings per week. Engineers on the team have begun ignoring all SAST output. The Security Gate Pass Rate has dropped to 40% because developers are abandoning the pipeline by pushing directly to staging. Which corrective action addresses the root cause, and which KPI will most directly improve as a result?

- A) Remove the SAST tool from the pipeline entirely to restore developer productivity; track only container scanning and SCA going forward
- B) Set the SAST gate to warn-only so developers can see findings without being blocked; the pass rate will improve as a result
- C) Tune the SAST ruleset to suppress known false positive patterns; pilot the tuned configuration on the Champion's team; measure true positive rate over 30 days before rolling out broadly; the Security Gate Pass Rate will improve as the signal-to-noise ratio improves
- D) Escalate the false positive problem to the CISO to authorize a six-month procurement process for a replacement SAST tool

Correct Answer: C — The root cause is a noisy SAST configuration with a high false positive rate, which has eroded developer trust in the tool. The correct response is to tune the ruleset — suppressing known false positive patterns (for example, findings that consistently appear in test files or in framework-generated code) — and validate the tuned configuration on the Champion's team before broader rollout. As the false positive rate decreases, the true positive rate improves, developers re-engage with findings, and the Security Gate Pass Rate recovers because legitimate builds are no longer falsely flagged.

Distractor Analysis:

- Why A is incorrect: Removing SAST entirely eliminates a critical shift-left control. The problem is ruleset configuration, not the presence of SAST. Removing the tool does not fix the root cause; it eliminates security coverage for an entire finding category.
- Why B is incorrect: Setting the gate to warn-only converts the SAST gate from a security control to security theater. Developers who are already ignoring findings will continue to ignore them. The pass rate will nominally improve (nothing blocks the build) but security effectiveness will not improve — and critical findings will reach production.
- Why D is incorrect: A six-month procurement process is not the appropriate response to a SAST configuration problem. SAST ruleset tuning is a configuration activity that a Security Champion and the security team can perform in days or weeks with the existing tool. Procurement would introduce a 6-month gap in SAST coverage.

---

### Question 6

An organization conducts an OWASP SAMM assessment and finds that its Secure Build practice is at Level 2. To advance to Level 3, the assessment identifies the following requirement: "Security defects are tracked as first-class engineering work items with defined SLAs by severity, and security debt is reported as a metric in engineering leadership reviews alongside technical debt." What process change is required to meet this Level 3 criterion?

- A) Implement a new SAST tool that can automatically create Jira tickets for every finding, replacing the manual finding review process
- B) Establish a formal vulnerability management process: SAST/SCA findings create engineering tickets in the team's backlog with severity-based SLAs (Critical: 24h, High: 7d, Medium: 30d), finding age is tracked in the team's sprint metrics, and security debt (total open finding count by severity) is reported in quarterly engineering leadership reviews
- C) Train the Security Champion to perform weekly reviews of all SAST findings and close findings that cannot be exploited in the current deployment environment
- D) Increase SAST scanning frequency from per-commit to hourly scans on the main branch to generate more timely finding data

Correct Answer: B — SAMM Level 3 for Secure Build requires that security defects are treated with the same rigor as functional defects: tracked in the engineering backlog, assigned SLAs by severity, and reported as a program-level metric in leadership reviews. This requires a formal vulnerability management process — not just a tool change. The process change described in B (tickets with SLAs, sprint metric integration, leadership-level security debt reporting) addresses all three Level 3 requirements.

Distractor Analysis:

- Why A is incorrect: Automating ticket creation is a Level 2 activity — it makes findings visible and trackable. Level 3 requires SLA governance and leadership-level reporting, which are process requirements beyond automation. Creating tickets automatically does not ensure they are resolved within defined SLAs or that the aggregate security debt is reported to leadership.
- Why C is incorrect: The Champion closing findings based on exploitability assessment is a triage activity, not a Level 3 maturity indicator. SAMM Level 3 requires systematic SLA-based tracking and leadership reporting — not individual champion judgment calls about which findings to close.
- Why D is incorrect: Increasing scan frequency generates more data points but does not advance the SAMM Secure Build Level 3 criterion, which is about tracking and governance, not scan frequency. Hourly scans on the same codebase will produce the same findings more often; the maturity gap is in how findings are managed after detection.

---

### Question 7

During a DevSecOps transformation retrospective, the security team reports that three production security incidents in the past quarter involved CVEs that were present in the Trivy container scan backlog at the time of each incident. The Trivy gate is configured to fail builds with CRITICAL findings, but engineers are regularly overriding the gate via a single-click approval button that requires no documented justification. Which failure mode is present, and what governance change directly addresses it?

- A) Tool accumulation without process — the organization should remove Trivy and replace it with a more effective scanning tool that cannot be overridden
- B) Security theater — the override mechanism makes the CRITICAL finding gate functionally equivalent to warn-only; the fix is to require documented justification and manager approval for any override, with override usage tracked as a KPI reported to engineering leadership
- C) Security as bottleneck — the fix is to reduce the security team's review requirements and allow developers to self-approve all security findings
- D) Security theater — the fix is to remove the override capability entirely and require all CRITICAL findings to be remediated before any deployment can proceed

Correct Answer: B — The described scenario is Security Theater: a gate exists that nominally blocks CRITICAL findings, but a trivial single-click override with no oversight makes the block functionally meaningless. Incidents caused by backlogged findings confirm the gate is not providing actual security benefit. The fix is to add governance to the override: require documented justification (why the deployment must proceed despite the finding), manager approval, and track override usage as a KPI. This maintains operational flexibility while restoring the gate's security value.

Distractor Analysis:

- Why A is incorrect: The failure mode is Security Theater (the gate is bypassed without oversight), not Tool Accumulation Without Process (which describes unmanaged finding backlogs without ownership). Replacing Trivy does not address an override governance problem — a new tool would be bypassed the same way.
- Why C is incorrect: Security as Bottleneck describes centralized security review that blocks development velocity. The described scenario has the opposite problem: overrides are too easy, not too hard. Removing security review requirements would worsen the theater problem.
- Why D is incorrect: Removing overrides entirely is operationally impractical and creates legitimate bottlenecks when a known false positive blocks a time-critical deployment. Governance (documented approval, tracked usage) is the correct response — it maintains emergency flexibility while ensuring overrides are deliberate, documented decisions rather than reflexive habit.

---

### Question 8

A DevSecOps team wants to measure Mean Time to Detect (MTTD) for vulnerabilities introduced into the codebase. They define MTTD as the time between a vulnerable dependency version being committed to a repository and the SCA scan flagging that dependency as a known CVE. Currently the SCA scan runs only in the CI pipeline on pull requests to the main branch. Which change most directly reduces MTTD?

- A) Add a DAST scan to the staging environment so that runtime behavior can detect the vulnerability's exploitation before it reaches production
- B) Configure Dependabot or a scheduled SCA scan to run daily on all repository branches — including feature branches — so that CVE matches are detected as soon as the NVD database is updated, regardless of whether a PR has been opened
- C) Require developers to manually check the NVD database for newly published CVEs against their project's dependency list every Monday morning
- D) Move the SCA scan from pull request time to post-deployment time, so that it runs against the exact artifact deployed to production rather than the pre-build dependency manifest

Correct Answer: B — MTTD is minimized by detecting vulnerabilities as early as possible after their introduction. The current model only detects on PR-to-main — a dependency may sit on a feature branch for days or weeks before a PR is opened. Additionally, a CVE may be published for an already-installed dependency after the last PR merge. Dependabot and scheduled daily SCA scans address both gaps: they scan all branches and run independently of commit triggers, so a newly published CVE is detected within 24 hours regardless of developer activity.

Distractor Analysis:

- Why A is incorrect: DAST detects runtime behavior and requires the application to be deployed to a running environment. It cannot detect a CVE in a library by scanning HTTP responses — it detects exploitable behavior. DAST does not reduce MTTD for dependency vulnerabilities; that is the domain of SCA.
- Why C is incorrect: Manual NVD checks are the pre-automation baseline that SCA tools replaced. Manual checks are inconsistent, error-prone, and do not scale. They would not reduce MTTD compared to automated scanning; they would likely increase it due to human inconsistency.
- Why D is incorrect: Moving SCA to post-deployment means the vulnerability must first reach production before being detected. This maximizes MTTD rather than minimizing it — it is a shift-right approach that contradicts the shift-left principle central to DevSecOps.

---

### Question 9

A DSOMM assessment places an organization's pipeline security at Level 3 (high adoption) across all technical dimensions. However, the Culture dimension is at Level 1. The CISO asks why Level 3 technical maturity has not produced a corresponding reduction in security incidents. What is the most likely explanation?

- A) The DSOMM model is inaccurate — technical controls at Level 3 should eliminate security incidents regardless of cultural maturity
- B) Level 3 technical controls require Level 3 cultural maturity to be effective. Without Security Champions triaging findings, teams taking ownership of SLAs, and leadership reviewing security KPIs, Level 3 pipeline gates are regularly overridden, finding backlogs are unmanaged, and the technical controls become security theater despite their technical sophistication
- C) The organization should invest in Level 4 technical tooling before addressing cultural maturity — more advanced tools will eventually drive cultural change organically
- D) Security incidents are caused by zero-day vulnerabilities that no level of pipeline maturity can prevent; culture is irrelevant to incident frequency

Correct Answer: B — Technical controls require human processes and cultural accountability to function as intended. A Level 3 pipeline with mandatory gates, image signing, and OPA policies is rendered ineffective by Level 1 culture: engineers override gates without oversight, finding backlogs are unmanaged because no team owns remediation SLAs, and security metrics are not reviewed so nobody notices the growing backlog. Culture is the multiplier on technical effectiveness — without it, sophisticated tools produce security theater.

Distractor Analysis:

- Why A is incorrect: The DSOMM model explicitly distinguishes technical and cultural dimensions because they are independently assessable and independently improvable. Technical Level 3 without cultural support is a recognized failure mode, not a model inaccuracy.
- Why C is incorrect: Adding Level 4 technical tooling on a Level 1 cultural foundation would worsen the imbalance. More tools generate more findings, more overrides, and more backlog — all of which require cultural infrastructure (champions, SLAs, leadership KPIs) to manage. Tools do not organically create culture.
- Why D is incorrect: While zero-day vulnerabilities are a real category of risk, the question describes a systematic discrepancy between technical maturity and incident reduction — a pattern that cannot be explained by zero-days alone. Zero-days account for a small fraction of production security incidents; the majority involve known CVEs in unpatched dependencies or misconfigurations caught by properly enforced pipeline gates.

---

### Question 10

An organization measures the following security KPIs for Q1: MTTD = 72 hours; MTTR-Security for critical findings = 21 days; Critical Escape Rate = 8%; Security Gate Pass Rate = 71%. The security team must present a prioritized improvement plan. Which KPI should be the highest priority to improve, and why?

- A) Security Gate Pass Rate — because it is the lowest absolute value and improving it will directly increase deployment velocity
- B) Critical Escape Rate — because an 8% escape rate means that critical vulnerabilities are reaching production, and each escaped critical finding represents a potential security incident with compliance, regulatory, and reputational consequences that outweigh the operational impact of the other metrics
- C) MTTD — because 72 hours is a long detection time and reducing it will automatically fix all other KPIs
- D) MTTR-Security — because 21 days is too long and remediating faster is always the most important security activity

Correct Answer: B — Critical Escape Rate is the highest-priority KPI because it directly measures whether security controls are preventing critical vulnerabilities from reaching production. An 8% escape rate means that for every 100 critical findings, 8 are deployed to production where they are exploitable. The other metrics (MTTD, MTTR, gate pass rate) affect how efficiently the program operates; the escape rate measures whether the program is achieving its fundamental security goal. A critical finding in production represents the highest-impact failure state — it is the outcome that all other security pipeline controls exist to prevent.

Distractor Analysis:

- Why A is incorrect: Security Gate Pass Rate at 71% indicates significant noise or genuine security debt in the pipeline, but a low pass rate does not directly mean vulnerabilities are escaping. The override approval process and gate configuration determine whether a low pass rate is operationally impactful. Escape Rate is the direct measure of pipeline effectiveness.
- Why C is incorrect: Reducing MTTD improves detection speed but does not automatically improve MTTR, pass rate, or escape rate — each KPI has independent contributing factors. MTTD at 72 hours is suboptimal but not the most critical failure indicator; the escape rate represents actual breached security perimeter.
- Why D is incorrect: MTTR-Security at 21 days for critical findings is a serious problem, but it is secondary to the escape rate question. Slow remediation means open findings exist for too long — but if they are caught by the pipeline and not escaping to production, the risk is manageable. An 8% escape rate means critical vulnerabilities are bypassing all controls and entering production, which is the more severe failure condition.
