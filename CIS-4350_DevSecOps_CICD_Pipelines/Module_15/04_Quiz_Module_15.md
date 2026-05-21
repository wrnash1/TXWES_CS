# Quiz: Module 15 - Security Metrics and Dashboards in CI/CD

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
How does automated pipeline logging support regulatory compliance audits?

* A) It compiles Python scripts and JavaScript bundles before they are submitted to auditors for review
* B) It provides immutable, time-stamped audit trails proving that every code release was scanned, tested, and authorized through the defined process — with system-generated records that auditors can independently verify
* C) It permanently deletes code history after each release to ensure sensitive pre-production code is not visible to auditors
* D) It accelerates database query speeds by caching frequently accessed compliance report queries
* **Correct Answer:** B) Auditors require proof that release procedures were followed on every deployment; CI/CD pipeline logs serve as immutable operational records that demonstrate each security gate ran and passed.
* **Distractor Analysis:**
  * *Why B is correct:* Compliance frameworks like SOC 2, PCI-DSS, and ISO 27001 require evidence that controls operated continuously, not just at audit time. Pipeline logs — stored in tamper-evident centralized logging — provide per-deployment evidence: scan results, approval records, commit SHAs, and deployment timestamps.
  * *Why A is incorrect:* CI/CD pipeline logging records execution events and outcomes; it does not compile code or prepare artifacts for auditor submission.
  * *Why C is incorrect:* Deleting code history would destroy audit evidence and violate data retention requirements under most compliance frameworks. Audit trails must be preserved, not deleted.
  * *Why D is incorrect:* Database query caching is a performance optimization concern. Pipeline logs are structured event records, not database query results.

---

**Question 2**
Which of the following most accurately describes "Compliance as Code" in a DevSecOps context?

* A) The practice of asking developers to document their security activities in a shared compliance tracking spreadsheet updated at the end of each sprint
* B) The practice of expressing security and compliance requirements as version-controlled, executable policy code (such as OPA Rego or Conftest policies) that is automatically enforced in CI/CD pipelines and Kubernetes admission control on every deployment
* C) A manual audit process where a compliance officer reviews all pull requests for security policy adherence before they can be merged
* D) The use of compliance management software (such as ServiceNow GRC) to track open audit findings and assign remediation owners
* **Correct Answer:** B) Compliance as Code transforms compliance requirements from static documentation into executable, automatically enforced policies that run on every pipeline trigger — providing continuous compliance assurance rather than periodic audit snapshots.
* **Distractor Analysis:**
  * *Why B is correct:* Tools like OPA Gatekeeper, Conftest, and Checkov express compliance rules as code. Every pipeline run or Kubernetes API call is evaluated against these rules automatically, generating a pass/fail result that constitutes machine-verifiable compliance evidence.
  * *Why A is incorrect:* Spreadsheet-based tracking is a manual, periodic, error-prone process. Compliance as Code specifically addresses the limitations of manual tracking by automating enforcement and evidence generation.
  * *Why C is incorrect:* Manual pull request review by a compliance officer is a human review process. While valuable, it is not "Compliance as Code" — it does not scale with pipeline velocity and produces no machine-verifiable evidence.
  * *Why D is incorrect:* GRC software tracks findings and remediation workflows; it does not enforce compliance policies at pipeline or admission time. Compliance as Code operates preventively, not as a tracking tool.

---

**Question 3**
A DevSecOps team tracks "Mean Time to Remediate (MTTR) Critical CVEs" as a security metric. The current MTTR is 42 days. Which pipeline improvement would most directly reduce this metric?

* A) Add a daily Slack message reminding developers to review open CVE tickets in the issue tracker
* B) Configure automated Dependabot or Renovate pull requests that propose dependency updates immediately when a new CRITICAL CVE is published, linked to the pipeline's SCA scan findings
* C) Increase the frequency of manual security reviews from quarterly to monthly
* D) Archive all CRITICAL CVE findings older than 30 days to reduce the active backlog count
* **Correct Answer:** B) Automated dependency update PRs — triggered immediately on CVE disclosure and pre-validated by the pipeline's SCA gate — reduce MTTR by eliminating the manual discovery-to-fix-PR workflow latency.
* **Distractor Analysis:**
  * *Why B is correct:* Dependabot and Renovate create pull requests automatically when a new CVE is matched to an installed dependency version. The update PR runs through the full CI pipeline (SCA, SAST, tests) before merge, ensuring the fix is validated. This can reduce MTTR from weeks to days by automating the patch initiation step.
  * *Why A is incorrect:* Slack reminders rely on developer attention and action; they do not automate any part of the detection-to-fix workflow. MTTR improvement requires reducing cycle time, not increasing notification frequency.
  * *Why C is incorrect:* Monthly manual reviews still leave up to 30 days between a CVE publication and its detection in the review cycle. Automated scanning detects the CVE immediately; the bottleneck is typically the time from detection to merged fix, not detection frequency.
  * *Why D is incorrect:* Archiving findings reduces the reported backlog count but does not remediate any vulnerabilities — the CVEs remain in the deployed software. Reducing MTTR requires fixing CVEs, not hiding them in an archive.

---

**Question 4**
A security dashboard shows the following trend over three months: Month 1: 85% of pipeline builds passed all security gates. Month 2: 91% passed. Month 3: 96% passed. What does this trend indicate, and what is the most likely explanation?

* A) The security gates are becoming less effective because too many builds are now passing, suggesting the scanning tools are producing more false positives
* B) The DevSecOps program is maturing positively — teams are writing more secure code, remediating vulnerabilities faster, and the security feedback loop is working effectively to reduce defect introduction rates
* C) The pipeline is becoming slower because security gates are running on more builds, causing developer frustration and the need to simplify the pipeline
* D) The increasing pass rate indicates that the security tools have been disabled or threshold criteria have been lowered, reducing the rigor of the security gate
* **Correct Answer:** B) A steadily improving pipeline gate pass rate indicates that developers are incorporating security feedback, writing more secure code proactively, and that the DevSecOps program's shift-left feedback loops are reducing vulnerability introduction rates.
* **Distractor Analysis:**
  * *Why B is correct:* In a well-functioning DevSecOps program, increased gate pass rates over time reflect genuine security improvement — developers learning from scan feedback, adopting secure patterns, and fixing vulnerabilities earlier in the cycle. This is the intended outcome of continuous security feedback.
  * *Why A is incorrect:* A rising pass rate does not inherently indicate more false positives. False positive rates should be tracked separately and would typically show up as specific rule findings being disputed, not as an overall pass rate change.
  * *Why C is incorrect:* Pipeline execution time is independent of pass/fail rates. The trend data provided is about security outcomes, not pipeline duration. More builds passing does not mean the pipeline is slower.
  * *Why D is incorrect:* While tool disablement would also produce a rising pass rate, this interpretation requires additional evidence (e.g., finding counts dropping to zero, scan step durations approaching zero). In the absence of such evidence, the positive trend interpretation (genuine improvement) is the correct default reading.

---

**Question 5**
An organization is preparing for a PCI-DSS audit of their production deployment process. The auditor requests evidence that all production deployments were: (a) built from reviewed, approved code, (b) scanned by an automated security tool, and (c) deployed by an authorized, automated process — not manually. Which set of artifacts satisfies all three requirements?

* A) The organization's written deployment policy document and the security team's attestation that the process was followed correctly during the audit period
* B) CI/CD pipeline audit logs showing each production deployment's triggering pull request (with reviewer approvals), SAST/SCA scan step results (with pass/fail exit codes), and pipeline-initiated deployment events — all linked to specific commit SHAs and stored in a tamper-evident centralized log
* C) A post-deployment penetration test report confirming no critical vulnerabilities were found in the current production environment
* D) Screenshots taken by the deployment engineer showing that the build, scan, and deploy steps ran successfully for a representative sample of deployments during the audit period
* **Correct Answer:** B) Pipeline audit logs provide system-generated, per-deployment evidence for all three requirements: reviewer approvals (code review evidence), scan step results (automated security scanning evidence), and pipeline-initiated deployment events (authorized, automated deployment evidence).
* **Distractor Analysis:**
  * *Why B is correct:* Modern CI/CD platforms log every event with timestamps, actor identities, and step outcomes. These logs — covering reviewer identities, scan tool exit codes, and deployment pipeline run IDs — provide the PCI-DSS Level 1 evidence required for continuous compliance, not just point-in-time assertions.
  * *Why A is incorrect:* Written policies and team attestations are documentation of intent, not evidence of execution. PCI-DSS auditors require operational evidence that controls actually ran on each production deployment, not assertions that the policy exists.
  * *Why C is incorrect:* A penetration test report provides point-in-time evidence about the current state of the application but does not demonstrate that each individual deployment followed the required process. It also does not address code review or automated scanning evidence per deployment.
  * *Why D is incorrect:* Screenshots from a deployment engineer are easily fabricated, incomplete, and do not cover the full audit period. They are also manual in nature — not system-generated records — and would not satisfy the requirement for automated, tamper-evident audit trails.
