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
