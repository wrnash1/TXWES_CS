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

---

### Question 11

A Security Champion proposes that the team's SAST gate should be set to fail the build on any HIGH or CRITICAL finding. Six months later, the gate pass rate has fallen to 40% and engineers have started adding `// nosec` comments without review to bypass the gate. Which transformation failure mode is occurring?

- A) Security as Bottleneck — the security team is preventing deployments by requiring approval for every finding
- B) Tool-First Culture — security tools were deployed without engineer training, leading to tool abuse rather than genuine remediation
- C) Alert Fatigue — the gate is generating too many findings, causing engineers to suppress rather than fix them, undermining the security gate's effectiveness
- D) Security Theater — the security team claims the tools are working because they are deployed, but the escape rate has increased

Correct Answer: C — Alert fatigue occurs when the volume of security findings overwhelms engineers' capacity to triage and fix them, causing them to suppress findings with bypass mechanisms (`// nosec`, suppression annotations) rather than remediating them. The result is the opposite of the intended security outcome: the gate appears active but findings are ignored. The correct response is to tune the gate to a manageable finding rate, address the backlog systematically, and establish a governed suppression process with Security Champion review.

Distractor Analysis:

- Why A is incorrect: Security as Bottleneck occurs when the security team controls all decisions and engineers wait for approval. The scenario describes an automated gate that engineers bypass themselves — there is no approval bottleneck. The engineers are circumventing the control rather than waiting for security.
- Why B is incorrect: Tool-First Culture describes deploying security tools without training, resulting in engineers not understanding findings. The scenario describes engineers who do understand the gate well enough to bypass it with `// nosec` — the problem is gate volume, not understanding.
- Why D is incorrect: Security Theater describes the appearance of security without effectiveness (e.g., running scans but not acting on findings). The scenario is more specific: engineers are actively undermining the gate rather than simply not acting on findings. The mechanism (nosec bypass proliferation) is the alert fatigue failure mode.

---

### Question 12

A DSOMM assessment places a newly formed DevSecOps team at Level 1 across all dimensions. The team wants to advance to Level 2 as quickly as possible. Which two actions have the highest impact on advancing from Level 1 to Level 2 in the Culture dimension?

- A) Deploy OPA Gatekeeper to enforce PodSecurity admission policies and install Trivy operator for continuous scanning
- B) Identify one Security Champion per team and provide them with an OWASP Top 10 training course; establish a shared security findings backlog visible to both development and security teams
- C) Conduct an annual penetration test and present findings to the engineering leadership team
- D) Deploy a full SAST, SCA, container scanning, and secrets scanning pipeline across all repositories

Correct Answer: B — DSOMM Level 2 in the Culture dimension requires that security awareness is formalized and distributed — Security Champions are identified and receive training, and security knowledge is shared across teams rather than siloed in the security function. Establishing a shared backlog creates visibility and shared accountability. These are cultural and organizational actions, not tool deployments.

Distractor Analysis:

- Why A is incorrect: OPA Gatekeeper and Trivy operator are tool deployments that advance the Infrastructure/Compliance dimensions. Culture dimension advancement requires organizational and behavioral changes — champion identification, training, and shared accountability structures.
- Why C is incorrect: An annual penetration test is a Level 3 or assessment activity. DSOMM Level 2 Culture requires daily-workflow integration of security — champions in sprints, training resources, and shared backlog. Annual point-in-time tests do not address the distribution and daily integration that characterizes Level 2 Culture.
- Why D is incorrect: Full pipeline deployment advances the CI/CD Controls dimension (Security Testing in SAMM). Culture advancement requires the organizational foundation: people, training, and shared ownership — not tool suite completeness.

---

### Question 13

Which DORA metric is most directly improved by reducing the Critical Escape Rate in a DevSecOps pipeline?

- A) Deployment Frequency — because fewer security incidents means deployments can happen more often
- B) Lead Time for Changes — because fixing security findings earlier in the pipeline reduces overall time to production
- C) Change Failure Rate — because escaped critical vulnerabilities cause incidents that result in failed deployments or emergency rollbacks, directly increasing the Change Failure Rate
- D) Mean Time to Recovery — because escaped vulnerabilities that cause incidents take longer to recover from than non-security incidents

Correct Answer: C — Change Failure Rate (CFR) measures the percentage of deployments that result in a degraded service or require remediation (rollback, hotfix, incident). A critical vulnerability that escapes to production and is discovered via an external report or incident is a direct Change Failure Rate event. Reducing the escape rate reduces the number of deployments that lead to incidents, which directly reduces CFR toward the elite performer benchmark (<5%).

Distractor Analysis:

- Why A is incorrect: Deployment Frequency is driven by batch size, CI/CD maturity, and release process, not directly by security escape rate. Fewer security incidents may enable more confident deployments, but this is an indirect relationship.
- Why B is incorrect: Lead Time for Changes is driven by CI/CD pipeline speed, PR review time, and test execution time. Fixing findings earlier reduces rework time, which can reduce lead time, but this is an indirect effect compared to the direct CFR impact of escaped vulnerabilities.
- Why D is incorrect: MTTR (Mean Time to Recovery) measures how quickly the team recovers after an incident. Escape Rate affects whether incidents occur (CFR), not how fast recovery happens after an incident. MTTR is influenced by incident response maturity, not primarily by the escape rate.

---

### Question 14

A security team proposes requiring all developers to complete a 40-hour annual security training course as part of the Security Champion program. A DevSecOps leader argues this approach is suboptimal. What is the DevSecOps-aligned alternative?

- A) Require a 20-hour course instead — the issue is duration, not approach
- B) Use just-in-time security training: provide context-sensitive guidance at the point where the security issue appears — such as inline documentation in the SAST finding, Secure Coding guidelines in the PR template, and targeted training for Security Champions on the specific vulnerability types their team encounters most frequently
- C) Require the security team to conduct all training for all engineers quarterly — centralized training ensures consistency
- D) Make all security training optional — forcing developers to learn security creates resentment that undermines the culture change

Correct Answer: B — DevSecOps-aligned security training is contextual and continuous, not annual and generic. Just-in-time training surfaces security knowledge at the moment of relevance (when a SAST finding appears, when a PR introduces a new vulnerability pattern). Security Champions receive targeted deep training relevant to their team's technology stack. This approach has higher knowledge retention and adoption rates than periodic generic training.

Distractor Analysis:

- Why A is incorrect: Reducing the duration from 40 to 20 hours addresses course length but not the fundamental problem — annual, decontextualized training has low retention and does not change daily engineering behavior. The timing and context of training matter more than duration.
- Why C is incorrect: Centralized security-team-delivered training replicates the centralized security bottleneck model. It does not scale to 80 engineers and does not build security knowledge within the development teams where it is needed.
- Why D is incorrect: Making all training optional undermines the program. The Security Champion model requires commitment from identified champions who receive structured training. The criticism of mandatory training is about the format (annual, generic), not the principle of requiring learning.

---

### Question 15

An organization's DevSecOps pipeline consistently shows a Security Gate Pass Rate of 95% for one team and 45% for another team. Both teams use the same tools and gate configurations. What is the most likely root cause of the difference, and what is the correct investigative approach?

- A) The 45% team is producing lower-quality code — replace the team lead
- B) Investigate whether the 45% team's codebase has a higher density of existing security debt, whether findings are from new code or legacy code, and whether the team's Security Champion is actively helping triage and remediate findings
- C) Lower the pass threshold for the 45% team to match the 95% team — the difference indicates the threshold is incorrectly calibrated
- D) The security tools are producing more false positives for the 45% team's technology stack — disable the tool for that team

Correct Answer: B — A large gate pass rate difference between teams using the same tools is a diagnostic signal, not a definitive conclusion. The correct response is investigation: Is the 45% team working in a legacy codebase with accumulated security debt that is only now being measured? Are findings from new code written this sprint or from pre-existing code? Is the Security Champion engaged? Is the team getting support from the security function to prioritize and fix findings? The answer to these questions determines the correct intervention.

Distractor Analysis:

- Why A is incorrect: A low gate pass rate reflects the state of the codebase and process, not the quality of the team personnel. Making personnel decisions based on a single metric without investigation is poor management and would damage the psychological safety needed for DevSecOps culture change.
- Why C is incorrect: Lowering thresholds for one team eliminates the measurement's value and allows security debt to accumulate unchecked. The goal is to understand and fix the root cause, not to make the metric look better.
- Why D is incorrect: Disabling a security tool for a team because it is finding more issues is the opposite of the correct response. If a technology stack has more findings, the tool is working correctly. The correct response is to triage findings, prioritize remediation, and support the team — not to eliminate detection.

---

### Question 16

The OWASP Software Assurance Maturity Model (SAMM) has five business functions. Which business function directly covers the security testing activities in a CI/CD pipeline (SAST, DAST, SCA)?

- A) Governance — because pipeline security gates enforce organizational security policy
- B) Construction — because security testing activities produce secure code artifacts
- C) Verification — because Verification covers security testing including code review, automated security testing, and requirements-driven testing
- D) Operations — because CI/CD pipeline execution is an operational activity

Correct Answer: C — SAMM's Verification business function encompasses all security testing activities: security requirements-driven testing, automated security testing in pipelines (SAST, DAST, SCA), and manual security review. The Verification function's maturity model specifically addresses how well the organization tests software against security requirements before release. Improving SAMM Verification maturity is directly measured by expanding and strengthening pipeline security gates.

Distractor Analysis:

- Why A is incorrect: SAMM Governance covers security policy, compliance, and risk management. While pipeline gates enforce policy, the testing activities themselves are in Verification, not Governance.
- Why B is incorrect: SAMM Construction covers security requirements, threat modeling, and secure architecture and design. It addresses what security properties the software should have, not how they are tested. Testing is Verification.
- Why D is incorrect: SAMM Operations covers incident management, operational vulnerability management, and environment monitoring. CI/CD pipeline execution is a delivery mechanism, but the security testing it performs is classified under Verification.

---

### Question 17

A Security Champion notices that engineers on their team are consistently marking SAST findings as false positives without review. The Champion wants to establish a governed suppression process. Which approach best balances velocity with security governance?

- A) Remove the ability for engineers to mark any finding as a false positive — only the security team can suppress findings
- B) Require that suppression annotations (`// nosec`, `# noqa`) be reviewed and approved in the PR by the Security Champion, who validates the false positive claim and adds a justification comment
- C) Accept all suppression requests automatically and report them weekly to the security team for retroactive review
- D) Turn off the SAST gate entirely until the backlog is cleared, then re-enable it

Correct Answer: B — Security Champions are positioned precisely for this role: they have the security knowledge to evaluate whether a suppression claim is valid and the team presence to review it in the PR workflow. Requiring Champion review of suppression annotations in the PR creates a lightweight governance checkpoint that does not block velocity (it is part of the existing PR review process) while preventing unilateral false positive declarations that bypass the security gate.

Distractor Analysis:

- Why A is incorrect: Requiring only the security team to suppress findings reintroduces the centralized security bottleneck. For a team of 8 engineers generating dozens of SAST findings, requiring central security review of every suppression request is not scalable and undermines the purpose of the Champion model.
- Why C is incorrect: Retroactive weekly review means suppressed findings have already been deployed. If a suppression was incorrectly granted, the finding may already be in production. The governance checkpoint must occur before merge, not after deployment.
- Why D is incorrect: Disabling the gate eliminates all detection. The finding backlog problem should be addressed by triaging and categorizing the backlog — not by removing the detection capability while the backlog is addressed.

---

### Question 18

Which combination of metrics provides the most complete picture of a DevSecOps program's effectiveness for an executive quarterly review?

- A) Number of SAST rules enabled and number of security tools deployed
- B) DORA Change Failure Rate, MTTR-Security for Critical findings, Critical Escape Rate, and Security Gate Pass Rate trending over four quarters
- C) Total number of security findings identified and total number of findings closed this quarter
- D) Number of Security Champions trained and number of security training hours delivered

Correct Answer: B — An effective executive security dashboard shows both outcomes (Critical Escape Rate — are we preventing critical findings from reaching production?) and efficiency (MTTR-Security — how fast do we fix them when found?). DORA Change Failure Rate connects security effectiveness to business delivery performance. Security Gate Pass Rate trending shows pipeline health over time. Together, these four metrics tell a coherent story: how often critical vulnerabilities escape (outcome), how fast we respond (efficiency), what impact security incidents have on deployment success (business impact), and whether the pipeline is becoming more or less effective (trend).

Distractor Analysis:

- Why A is incorrect: Tool count and rule count are input metrics (activity measures), not outcome metrics. They show what the program has deployed, not whether it is working. A program with 20 tools and 10,000 rules could have a 100% escape rate if findings are ignored.
- Why C is incorrect: Total findings opened and closed measures throughput but not quality or impact. Without context about severity distribution and whether escapes are occurring, these numbers do not tell whether the security investment is preventing incidents.
- Why D is incorrect: Champion count and training hours are program adoption metrics that are useful for tracking the culture transformation. They do not measure security effectiveness — a team could have 20 trained champions and still have high escape rates if the pipeline is poorly configured.

---

### Question 19

During a DevSecOps maturity assessment, a team reports: "We run SAST, SCA, and container scans in CI. We have Security Champions. We conduct quarterly threat modeling. Our MTTD is 4 hours and MTTR is 3 days for critical findings. We review DORA metrics in engineering leadership meetings." What DSOMM maturity level does this profile best represent?

- A) Level 1 — Initial
- B) Level 2 — Basic Adoption
- C) Level 3 — High Adoption
- D) Level 4 — Continuous Improvement

Correct Answer: C — Level 3 (High Adoption) is characterized by: full pipeline gate suite across all finding categories (SAST, SCA, container, secrets, IaC), formal Security Champion program, threat modeling integrated into the development process, and security and DORA KPIs reviewed at leadership level. The profile matches Level 3 well: gates are comprehensive, champions exist, threat modeling is practiced (quarterly, though sprint-cadence would be Level 4), and KPIs are leadership-visible.

Distractor Analysis:

- Why A is incorrect: Level 1 organizations have no formal security program in the pipeline. This team has deployed multiple scanning tools, has champions, and reviews KPIs — all of which are well beyond Level 1.
- Why B is incorrect: Level 2 teams have mandatory SAST and SCA gates and identified champions but lack the full gate suite, formal programs, and KPI integration with engineering leadership. This team has all of those, placing them above Level 2.
- Why D is incorrect: Level 4 (Continuous Improvement) requires automation of security coverage metrics into engineering dashboards, sprint-cadence threat modeling (not quarterly), and security improvement metrics (escape rate trending to zero) as leadership-level OKRs. The quarterly threat modeling cadence and absence of continuous improvement automation places this team at Level 3, not Level 4.

---

### Question 20

A developer asks a Security Champion: "Why should I care about DevSecOps? Security is the security team's job." Which response best represents the core DevSecOps culture argument?

- A) "Because the company policy requires it and you could be fired for security violations."
- B) "Because fixing a vulnerability after production deployment costs 30 times more than fixing it during development, and when you find and fix issues earlier in your own code, you protect your users and reduce the incident workload that would otherwise fall back to your sprint."
- C) "Because security tools run automatically in CI now — you don't actually need to do anything differently."
- D) "Because security is a compliance requirement and we need to pass our next audit."

Correct Answer: B — The DevSecOps culture argument is grounded in practical developer self-interest and user protection, not compliance obligation or threat. The cost-of-defect curve (vulnerabilities cost exponentially more to fix later) is a concrete, credible argument. Connecting security to protecting users makes it a values-based argument. Connecting it to reduced sprint disruption (fewer incident-driven interruptions) makes it personally relevant. This is the Security Champion's value proposition to skeptical developers.

Distractor Analysis:

- Why A is incorrect: Rule-based arguments ("policy requires it") may achieve compliance behavior but do not build genuine security culture. Engineers who follow security practices only to avoid punishment will find ways around controls when they can. The goal is intrinsic motivation, not fear of consequences.
- Why C is incorrect: "Tools run automatically — you don't need to do anything" is factually false (engineers must understand and act on findings) and counterproductive to culture change. It positions security as someone else's problem, which is the opposite of DevSecOps.
- Why D is incorrect: Compliance framing ("pass our audit") is a valid business reason but is not the DevSecOps culture argument. It positions security as a bureaucratic checkbox rather than a quality attribute of the engineer's own work. The Security Champion model requires connecting security to the engineer's professional identity and values.

---

Quiz — Module 15 | CIS-4350 | Texas Wesleyan University | Professor Nash
