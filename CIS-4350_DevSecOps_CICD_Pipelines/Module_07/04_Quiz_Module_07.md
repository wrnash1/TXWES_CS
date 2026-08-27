# Quiz: Module 07 — Application Security Testing in CI/CD

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Submit answers through the Canvas quiz interface.

---

## Question 1

A developer pushes code that introduces a SQL injection vulnerability. Which security testing type is most likely to detect this vulnerability before the application is deployed?

- A) DAST — Dynamic Application Security Testing
- B) SAST — Static Application Security Testing
- C) Penetration testing
- D) Container image scanning

### Q1 — Correct Answer: B

### Q1 — Distractor Analysis

- A) DAST requires a running application and runs after deployment — it would detect this after deployment, not before.
- C) Penetration testing is a periodic manual activity — it does not operate on every code push.
- D) Container image scanning looks for CVEs in OS packages and libraries — it does not analyze application source code logic.

---

## Question 2

OWASP ZAP is run against a production application using the baseline scan mode. Why is this considered safer than running the full scan mode against production?

- A) Baseline scan mode is faster than full scan mode
- B) Baseline scan is passive only — it does not send attack payloads that could corrupt production data
- C) Baseline scan mode requires authentication credentials that full scan mode does not
- D) Baseline scan mode only scans the homepage, reducing network impact

### Q2 — Correct Answer: B

### Q2 — Distractor Analysis

- A) Speed is a secondary consideration — safety of production data is the primary reason.
- C) Authentication is optional in both modes — it is not the distinguishing factor.
- D) Baseline scan crawls the full application — it is not limited to the homepage.

---

## Question 3

SonarQube's Quality Gate is used in a CI pipeline. What happens when the Quality Gate condition is violated?

- A) SonarQube emails the repository owner but allows the pipeline to continue
- B) SonarQube blocks the pipeline with a non-zero exit code, preventing the PR from merging
- C) SonarQube automatically creates a pull request with remediation suggestions
- D) SonarQube quarantines the build artifact until a security review is completed

### Q3 — Correct Answer: B

### Q3 — Distractor Analysis

- A) Email notification is a supplementary feature — the Quality Gate enforces a pipeline block, not just a notification.
- C) SonarQube does not auto-create PRs — that is a feature of some IDE integrations, not the CI Quality Gate.
- D) Build artifact quarantine is not a SonarQube feature — it enforces the gate at the analysis step.

---

## Question 4

OWASP Dependency-Check is run with the `--failOnCVSS 7` flag. A dependency scan finds three vulnerabilities: one CVSS 9.8, one CVSS 6.5, and one CVSS 4.2. What is the pipeline behavior?

- A) The pipeline passes because the majority of findings are below 7.0
- B) The pipeline fails because the CVSS 9.8 finding meets the threshold
- C) The pipeline fails for the CVSS 9.8 and 6.5 findings but not the 4.2
- D) The pipeline pauses for manual review of all three findings

### Q4 — Correct Answer: B

### Q4 — Distractor Analysis

- A) The threshold is applied per finding, not as an average — a single finding at 9.8 is sufficient to trigger failure.
- C) `--failOnCVSS 7` fails on scores 7.0 and above only — CVSS 6.5 is below the threshold.
- D) Manual review pause is not a Dependency-Check feature — it exits with a non-zero code.

---

## Question 5

What is the primary use case for storing an SBOM with every software release?

- A) SBOMs replace the need for dependency scanning in CI pipelines
- B) SBOMs allow rapid identification of which releases contain a specific component when a new CVE is published
- C) SBOMs are required by Docker Hub to allow image publishing
- D) SBOMs reduce the size of container images by eliminating duplicate libraries

### Q5 — Correct Answer: B

### Q5 — Distractor Analysis

- A) SBOMs complement dependency scanning — they do not replace it.
- C) Docker Hub does not require SBOMs for image publishing.
- D) SBOMs are metadata documents — they do not affect container image contents or size.

---

## Question 6

Which SBOM format was developed by OWASP and includes support for VEX (Vulnerability Exploitability Exchange)?

- A) SPDX
- B) CycloneDX
- C) SWID
- D) OpenSBOM

### Q6 — Correct Answer: B

### Q6 — Distractor Analysis

- A) SPDX is maintained by the Linux Foundation, not OWASP, and has limited VEX support.
- C) SWID (Software Identification Tags) is a different software identification standard, not an SBOM format.
- D) "OpenSBOM" is not a recognized standard SBOM format.

---

## Question 7

Semgrep uses a `nosemgrep` inline comment to suppress a finding. From a DevSecOps process perspective, what is the significance of this suppression being in the source code rather than in an external configuration file?

- A) Source code suppressions are processed faster than config file suppressions
- B) In-code suppressions are version-controlled alongside the code, creating an auditable record of accepted risk that goes through code review
- C) In-code suppressions are automatically synced to the SIEM for alerting
- D) Source code suppressions cannot be bypassed by developers, making them more secure

### Q7 — Correct Answer: B

### Q7 — Distractor Analysis

- A) Processing speed is not a relevant security consideration for suppressions.
- C) SIEM integration is not a feature of Semgrep inline suppressions.
- D) Developers can add or remove `nosemgrep` comments — the security value is auditability through code review, not bypass prevention.

---

## Question 8

A pipeline runs Semgrep SAST and OWASP Dependency-Check, but an XSS vulnerability in the application's JavaScript is not detected. Why might this happen?

- A) The CVSS quality gate threshold is set too high
- B) SAST may not detect all XSS variants, and Dependency-Check only scans library versions — neither tool exercises the running application's output rendering
- C) Semgrep does not support JavaScript rule sets
- D) OWASP Dependency-Check only works for Java dependencies

### Q8 — Correct Answer: B

### Q8 — Distractor Analysis

- A) The quality gate threshold affects what findings fail the pipeline — it does not affect whether the XSS is detected in the first place.
- C) Semgrep has JavaScript and TypeScript rule sets — the limitation is not language support but the runtime rendering context.
- D) OWASP Dependency-Check supports multiple ecosystems including Node.js.

---

## Question 9

Syft is used to generate an SBOM, and then Grype is run against it. What is Grype's function in this workflow?

- A) Grype reformats the SBOM from CycloneDX to SPDX format
- B) Grype signs the SBOM with a cryptographic signature for supply chain integrity
- C) Grype scans the SBOM's component inventory against vulnerability databases to identify CVEs
- D) Grype uploads the SBOM to the GitHub Security tab for display

### Q9 — Correct Answer: C

### Q9 — Distractor Analysis

- A) SBOM format conversion is handled by separate tools — Grype is a vulnerability scanner.
- B) SBOM signing is handled by cosign or similar tools — Grype does not sign artifacts.
- D) GitHub Security tab upload requires SARIF format and the codeql-action/upload-sarif action — not Grype.

---

## Question 10

In a DevSecOps pipeline, DAST must run after SAST. What is the primary architectural reason for this sequencing?

- A) DAST produces SARIF output that SAST requires as input
- B) DAST requires a deployed, running application — it cannot scan source code
- C) DAST takes longer than SAST and must run in a separate stage to avoid pipeline timeout
- D) DAST and SAST use the same scanner engine and cannot run simultaneously

### Q10 — Correct Answer: B

### Q10 — Distractor Analysis

- A) SARIF is an output format — DAST does not consume SAST's SARIF as input.
- C) Duration is a practical consideration but not the architectural reason — DAST simply cannot function without a running application.
- D) DAST and SAST use completely different analysis engines and can run in parallel when both have their prerequisites met.

---

Quiz — Module 07 | CIS-4350 | Texas Wesleyan University | Professor Nash

---

### Question 11 (5 points)

A SonarQube Quality Gate is configured with three conditions: coverage must be at least 80%, no new Critical issues, and reliability rating must be A. A build has 79% coverage, zero new Critical issues, and reliability rating A. What is the Quality Gate result?

- A) Pass — the reliability and critical issue conditions are met
- B) Fail — the coverage condition is not met, and all conditions must pass
- C) Warning — the coverage is close enough to trigger a warning, not a fail
- D) Pass — Quality Gates require a majority of conditions to pass, not all

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) All configured conditions must pass for the Quality Gate to succeed — partial compliance is not sufficient.
  - C) SonarQube Quality Gates use hard pass/fail conditions — there is no "warning" state for a gate.
  - D) Quality Gates require all conditions to pass — there is no majority-rules logic.

---

### Question 12 (5 points)

OWASP ZAP's authenticated scan requires configuring a session management script. Why is authentication important for DAST coverage?

- A) Unauthenticated scans run slower because ZAP cannot cache session tokens
- B) Without authentication, ZAP can only scan publicly accessible endpoints and misses all vulnerabilities in protected functionality
- C) ZAP requires authentication to generate SARIF output
- D) Unauthenticated scans automatically trigger WAF rules that block ZAP's scanner IP

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Session caching has no meaningful impact on scan speed — coverage is the concern.
  - C) SARIF output is independent of authentication configuration.
  - D) WAF blocking is a possible operational challenge but is not the reason authentication is needed for coverage.

---

### Question 13 (5 points)

The OWASP Top 10 category A01:2021 (Broken Access Control) is best detected by which combination of tools?

- A) SAST alone — Semgrep has rules for all access control patterns
- B) DAST combined with authenticated testing — access control failures require exercising the running application with different user roles
- C) Container image scanning — access control vulnerabilities are encoded in the image layers
- D) Dependency-Check — broken access control is caused by vulnerable third-party libraries

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) SAST can identify some access control patterns but cannot test authorization logic that depends on runtime session state.
  - C) Container image scanning detects OS and library CVEs — it does not analyze application authorization logic.
  - D) Dependency-Check finds known CVEs in libraries — broken access control typically refers to application-level logic flaws, not library vulnerabilities.

---

### Question 14 (5 points)

A VEX (Vulnerability Exploitability Exchange) document states that a CVE in a dependency has status `not_affected` with justification `component_not_present`. What does this mean?

- A) The vulnerability exists but the team has decided to accept the risk
- B) The vulnerable component is listed in the SBOM but is not actually present in the deployed artifact
- C) The vulnerability has been patched in the next release of the dependency
- D) The CVE has been disputed and is no longer in the NVD database

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Accepted risk would use the VEX status `affected` with a remediation statement — `component_not_present` has a specific meaning.
  - C) Patch availability would be reflected in the CVE record — VEX documents the exploitability in a specific product, not upstream patch status.
  - D) CVE dispute is handled through the NVD/MITRE process — VEX documents the vendor's assessment of exploitability, independent of CVE status.

---

### Question 15 (5 points)

Snyk integrates into a GitHub repository and automatically opens pull requests. Under which circumstance does Snyk open a pull request?

- A) When it detects a new developer has been added to the repository
- B) When it identifies a dependency with a known vulnerability and a fixed version is available
- C) When a SAST scan produces more than 10 findings
- D) When a container image push is detected in the repository's Dockerfile

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Snyk monitors dependencies and code, not team membership.
  - C) Snyk's PR generation is triggered by vulnerability findings with available fixes — not finding counts from SAST.
  - D) Snyk can scan Dockerfiles but auto-PR generation is driven by dependency fix availability, not image push events.

---

### Question 16 (5 points)

A development team runs `semgrep --config=auto` in their CI pipeline. The `auto` configuration means:

- A) Semgrep automatically detects the programming language and selects community-maintained rules from the Semgrep registry for that language
- B) Semgrep generates its own rules by analyzing the codebase for patterns
- C) Semgrep runs in auto-fix mode and automatically remediates all findings
- D) Semgrep uses only the OWASP Top 10 ruleset regardless of language

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Semgrep does not generate rules from the codebase — rules are written by humans and stored in the registry.
  - C) Auto-fix (autofix) is a separate optional flag — `--config=auto` refers to rule selection, not remediation.
  - D) `auto` selects the full relevant rule set for the detected language — it is not limited to the OWASP Top 10 rules.

---

### Question 17 (5 points)

Which SBOM component field is most useful for matching a dependency against the NVD CVE database?

- A) The component's license identifier (e.g., MIT, Apache-2.0)
- B) The component's CPE (Common Platform Enumeration) or PURL (Package URL)
- C) The component's SHA-256 hash
- D) The component's source repository URL

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) License identifiers are used for compliance tracking — they are not used to look up CVEs.
  - C) SHA-256 hashes identify a specific binary artifact but are not how the NVD organizes CVE records — CPE and PURL are the standard identifiers.
  - D) Source repository URLs are informational — CVE databases use standardized identifiers like CPE, not arbitrary URLs.

---

### Question 18 (5 points)

A pipeline runs OWASP ZAP baseline scan against a staging environment and produces 45 alerts. The team wants to fail the pipeline only on High and Critical risk alerts. How is this configured?

- A) Use the `-l` flag to set the minimum alert level: `zap-baseline.py -l HIGH`
- B) Use a ZAP Automation Framework plan with `failThreshold: high`
- C) Both A and B are valid approaches depending on whether using the legacy CLI or the Automation Framework
- D) ZAP always fails on all alert levels — per-severity thresholds require Burp Suite Enterprise

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) The `-l` flag is valid for the legacy `zap-baseline.py` script — it is a correct approach for the CLI mode.
  - B) The Automation Framework `failThreshold` is the modern approach — it is also a correct approach.
  - D) ZAP fully supports per-severity thresholds through both mechanisms — Burp Suite is not required.

---

### Question 19 (5 points)

The CycloneDX SBOM format includes a `dependencies` section that maps components to their transitive dependencies. Why is transitive dependency tracking important for security?

- A) Transitive dependencies are always more vulnerable than direct dependencies
- B) A vulnerability in a deeply nested transitive dependency is still exploitable and must be identified for complete risk assessment
- C) Transitive dependency tracking is required by US Executive Order 14028
- D) Tools like Dependency-Check only scan transitive dependencies, not direct dependencies

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Vulnerability severity is not related to dependency depth — transitive dependencies are not inherently more vulnerable.
  - C) EO 14028 requires SBOMs but does not specifically mandate transitive dependency tracking as a distinct requirement.
  - D) Dependency-Check scans both direct and transitive dependencies — it is not limited to one or the other.

---

### Question 20 (5 points)

A security team wants to enforce that every new GitHub release must have an associated SBOM artifact attached before the release is published. Which GitHub feature enforces this policy?

- A) A branch protection rule requiring SBOM status checks
- B) A GitHub Actions workflow triggered on `release: types: [published]` that generates and attaches the SBOM, or a pre-publish environment protection gate requiring the SBOM job to pass
- C) A CODEOWNERS file requiring security team review of every release tag
- D) A GitHub Actions workflow triggered on `push` that generates SBOMs for every commit

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Branch protection rules apply to branch merges, not release publishing events.
  - C) CODEOWNERS handles code review requirements — it does not enforce artifact attachment to releases.
  - D) Generating SBOMs on every commit does not ensure the SBOM is attached to the release artifact — the trigger must be aligned with the release event.
