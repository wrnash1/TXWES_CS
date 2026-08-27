# Quiz: Module 01 — Introduction to DevSecOps

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Submit answers through the Canvas quiz interface.

---

## Question 1

Which principle describes the practice of integrating security activities earlier in the software development lifecycle to reduce remediation cost?

- A) Security by obscurity
- B) Shift-left security
- C) Defense in depth
- D) Zero-trust architecture

### Q1 — Correct Answer: B

### Q1 — Distractor Analysis

- A) Security by obscurity is hiding implementation details to prevent attack — unrelated to lifecycle timing.
- C) Defense in depth describes layered security controls — a valid concept but not about SDLC timing.
- D) Zero-trust architecture is a network and identity model — not an SDLC philosophy.

---

## Question 2

According to the IBM Systems Sciences Institute data cited in this module, approximately how much more expensive is it to fix a security defect in production compared to fixing it during the design phase?

- A) 5 times more expensive
- B) 15 times more expensive
- C) 30–100 times more expensive
- D) 2 times more expensive

### Q2 — Correct Answer: C

### Q2 — Distractor Analysis

- A) 5x is the cost multiplier for the coding phase, not production.
- B) 15x falls between integration testing and system testing — not the production figure.
- D) 2x drastically understates the exponential cost growth of late-stage defect discovery.

---

## Question 3

In the CALMS DevOps maturity framework, what does the letter "L" stand for?

- A) Logging
- B) Lean
- C) Lateral
- D) Lifecycle

### Q3 — Correct Answer: B

### Q3 — Distractor Analysis

- A) Logging is an operational practice but is not one of the five CALMS pillars.
- C) Lateral has no meaning in the CALMS framework.
- D) Lifecycle is relevant to DevSecOps generally but is not a CALMS pillar.

---

## Question 4

What does STRIDE stand for in the context of threat modeling?

- A) Security, Testing, Risk, Infrastructure, Design, Execution
- B) Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- C) Scanning, Tracking, Remediation, Identification, Detection, Encryption
- D) Source, Target, Risk, Impact, Defense, Exploitation

### Q4 — Correct Answer: B

### Q4 — Distractor Analysis

- A) These words sound security-related but do not form a recognized threat modeling framework.
- C) This is a made-up sequence of security process terms, not STRIDE.
- D) This is a plausible-sounding but incorrect definition with no industry basis.

---

## Question 5

Which of the following is the primary difference between SAST and DAST?

- A) SAST requires a running application; DAST analyzes source code statically
- B) SAST analyzes source code without running it; DAST tests a running application
- C) SAST is used only for containers; DAST is used only for cloud infrastructure
- D) SAST and DAST are different names for the same technique

### Q5 — Correct Answer: B

### Q5 — Distractor Analysis

- A) This reverses the definitions of SAST and DAST — a common exam trap.
- C) Neither SAST nor DAST is limited to containers or cloud infrastructure.
- D) SAST and DAST are fundamentally different techniques with different tool sets and use cases.

---

## Question 6

A developer team wants to prevent AWS secret keys from being committed to GitHub. Which DevSecOps tool category addresses this requirement?

- A) Dynamic Application Security Testing (DAST)
- B) Secrets detection / pre-commit hooks
- C) Container image scanning
- D) Infrastructure as Code scanning

### Q6 — Correct Answer: B

### Q6 — Distractor Analysis

- A) DAST tests running web applications for runtime vulnerabilities — it does not inspect Git commits.
- C) Container image scanning looks for CVEs in OS packages and libraries, not source code secrets.
- D) IaC scanning checks Terraform and CloudFormation for misconfigurations, not Git commit secrets.

---

## Question 7

Which framework, published by the Department of Defense in 2019, helped standardize DevSecOps adoption across federal agencies?

- A) NIST Cybersecurity Framework (CSF)
- B) DoD Enterprise DevSecOps Reference Design
- C) OWASP DevSecOps Guideline
- D) CIS Controls v8

### Q7 — Correct Answer: B

### Q7 — Distractor Analysis

- A) The NIST CSF is a risk management framework — not a DevSecOps pipeline reference design.
- C) OWASP has DevSecOps resources but did not publish the 2019 federal reference document.
- D) CIS Controls are configuration hardening benchmarks, not a DevSecOps pipeline model.

---

## Question 8

What is the role of a "security champion" in a DevSecOps organization?

- A) The CISO who approves all deployments before they go to production
- B) An external auditor who conducts annual penetration tests
- C) A developer embedded in a team who has extra security training and serves as a security liaison
- D) A dedicated security engineer who reviews every pull request manually

### Q8 — Correct Answer: C

### Q8 — Distractor Analysis

- A) The CISO operates at an organizational level and is not embedded in each dev team.
- B) An external auditor performs periodic assessments — not a day-to-day team role.
- D) Having a dedicated engineer manually review every PR is the traditional bottleneck model DevSecOps replaces.

---

## Question 9

Security as Code refers to which practice?

- A) Writing exploits in Python to test application security
- B) Encoding security policies and controls as version-controlled, testable files
- C) Storing source code in an encrypted repository
- D) Using machine learning to detect security threats in real time

### Q9 — Correct Answer: B

### Q9 — Distractor Analysis

- A) Writing exploits is offensive security testing — unrelated to Security as Code as a governance concept.
- C) Encrypting a repository is a storage security control, not the Security as Code philosophy.
- D) ML-based threat detection is a valid monitoring technique but is not what Security as Code means.

---

## Question 10

Conway's Law is relevant to DevSecOps because it suggests that:

- A) All software must be delivered in under 24 hours to be considered DevSecOps-compliant
- B) Organizations produce systems that mirror their communication structures, so siloed security teams produce siloed security
- C) Security tools must be open source to be used in a DevSecOps pipeline
- D) Compliance requirements always override security architecture decisions

### Q10 — Correct Answer: B

### Q10 — Distractor Analysis

- A) Conway's Law makes no statement about delivery speed or time constraints.
- C) Conway's Law is about organizational communication structure — not tool licensing.
- D) Conway's Law describes organizational dynamics — it does not address compliance vs. architecture hierarchy.

---

Quiz — Module 01 | CIS-4350 | Texas Wesleyan University | Professor Nash

---

### Question 11 (5 points)

Which of the following best describes the PASTA threat modeling methodology?

- A) A checklist of six threat categories applied to data flow diagrams
- B) A risk-centric, seven-stage process that aligns threat analysis with business objectives
- C) A penetration testing framework used exclusively during the Test phase
- D) A policy language for encoding security controls in Kubernetes

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) describes STRIDE, not PASTA. PASTA (Process for Attack Simulation and Threat Analysis) takes a business risk perspective rather than a checklist approach.
  - C) PASTA is a threat modeling methodology performed during planning, not a pentest framework used in the Test phase.
  - D) describes OPA/Rego, which is unrelated to PASTA.

---

### Question 12 (5 points)

In a GitHub Actions workflow, what is the purpose of setting `fetch-depth: 0` on the `actions/checkout` step when running a secrets scanner?

- A) It reduces the download size of the repository to speed up the pipeline
- B) It ensures the full Git history is checked out so secrets in older commits are also scanned
- C) It prevents the runner from caching any credentials to disk
- D) It restricts checkout to the default branch only

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `fetch-depth: 0` actually increases download size by fetching all history — it does not reduce it.
  - C) Credential caching is controlled by the credential helper, not the fetch-depth setting.
  - D) `fetch-depth: 0` retrieves all branches and all history — it does not restrict to a single branch.

---

### Question 13 (5 points)

What is a Software Bill of Materials (SBOM), and when in the DevSecOps lifecycle is it typically generated?

- A) A budget document listing the cost of all security tools; generated during the Plan phase
- B) An inventory of all software components, libraries, and their versions; generated at Release
- C) A report from DAST scanning listing all discovered web application vulnerabilities
- D) A container manifest that specifies the base image and exposed ports

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) An SBOM documents software components, not financial costs.
  - C) A DAST report lists runtime vulnerabilities — it is not an SBOM and is produced during the Test phase.
  - D) A Dockerfile or container manifest describes build instructions, not a comprehensive component inventory.

---

### Question 14 (5 points)

Which metric measures the average time between a vulnerability being discovered in a pipeline scan and the corresponding fix being merged?

- A) Pipeline Gate Pass Rate
- B) Escape Rate
- C) Mean Time to Remediate (MTTR)
- D) Vulnerability Density

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Pipeline Gate Pass Rate measures the percentage of builds that pass all gates — not time to fix.
  - B) Escape Rate measures the percentage of vulnerabilities that reach production, not remediation time.
  - D) Vulnerability Density measures the number of vulnerabilities per 1,000 lines of code, not elapsed time.

---

### Question 15 (5 points)

The CALMS pillar of "Measurement" in a DevSecOps context primarily supports which outcome?

- A) Justifying tool purchases to the CISO based on license cost comparisons
- B) Enabling data-driven decisions about security posture and process improvement over time
- C) Measuring individual developer productivity through lines-of-code metrics
- D) Documenting compliance evidence for annual audits only

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Measurement in CALMS is about process telemetry and improvement, not procurement justification.
  - C) Lines-of-code metrics are generally discouraged as a developer performance measure and are not the CALMS intent.
  - D) CALMS Measurement provides continuous feedback, not a once-a-year audit data collection exercise.

---

### Question 16 (5 points)

Which of the following describes the "Escape Rate" metric in DevSecOps?

- A) The percentage of pipeline runs that fail due to tool configuration errors
- B) The percentage of known vulnerabilities that were not caught by pipeline gates and reached production
- C) The time elapsed between a CVE being published and a patch being applied
- D) The number of secrets committed to source control per month

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Pipeline configuration failures are tracked separately and are not what Escape Rate measures.
  - C) That describes patch lag or vulnerability exposure window, not Escape Rate.
  - D) Committed secrets are tracked by secrets-detection tooling and reported as a count, not the Escape Rate metric.

---

### Question 17 (5 points)

HashiCorp Vault is primarily used in a DevSecOps pipeline to address which concern?

- A) Scanning container images for known CVEs before deployment
- B) Centrally storing, managing, and dynamically injecting secrets so they are never hardcoded in code or environment files
- C) Running static analysis on Terraform templates for configuration drift
- D) Generating signed SBOMs for every container image pushed to a registry

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Container image scanning is the role of tools like Trivy or Grype, not Vault.
  - C) Terraform static analysis is performed by tools like tfsec or checkov, not Vault.
  - D) SBOM generation is performed by tools like Syft or CycloneDX, not Vault.

---

### Question 18 (5 points)

Which statement correctly characterizes the "three ways" of DevOps (as described by Gene Kim)?

- A) Plan, Build, Release — the three sequential gates before any deployment
- B) Flow, Feedback, and Continual Learning and Experimentation
- C) Culture, Automation, and Lean — a subset of the CALMS framework
- D) People, Process, and Technology — the classic IT service management triad

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Plan, Build, Release describes a CI/CD phase model, not the Three Ways.
  - C) Culture, Automation, and Lean are three of the five CALMS pillars, not the Three Ways.
  - D) People, Process, Technology is an ITSM framework triad, unrelated to the Three Ways.

---

### Question 19 (5 points)

A team uses Semgrep in their CI pipeline. Semgrep belongs to which DevSecOps tool category?

- A) Dynamic Application Security Testing (DAST)
- B) Container image scanning
- C) Static Application Security Testing (SAST)
- D) Infrastructure as Code (IaC) scanning

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) DAST tools like OWASP ZAP test running applications — Semgrep analyzes source code without executing it.
  - B) Container image scanners like Trivy inspect OS packages and layers — Semgrep works on source code.
  - D) IaC scanners like checkov or tfsec analyze Terraform/CloudFormation — Semgrep is a general-purpose code analysis engine.

---

### Question 20 (5 points)

What is the primary security risk that OWASP Dependency-Check is designed to detect?

- A) Misconfigurations in Kubernetes RBAC policies
- B) Known CVEs in open-source libraries included in a project's build dependencies
- C) Hardcoded API keys and passwords in application source code
- D) SQL injection vulnerabilities in database query strings

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Kubernetes RBAC misconfiguration is addressed by IaC or policy scanners, not dependency checkers.
  - C) Hardcoded secrets are detected by secrets-scanning tools like gitleaks or truffleHog.
  - D) SQL injection detection is a SAST or DAST concern — dependency checkers focus on vulnerable third-party packages.
