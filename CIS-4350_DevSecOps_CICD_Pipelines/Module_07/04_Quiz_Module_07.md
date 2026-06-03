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
