# Quiz: Module 01 - DevOps Fundamentals and the DevSecOps Mindset

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

What does the term "shift-left" mean in DevSecOps methodology?

- A) Moving the development team to a different office location to be closer to the security team
- B) Integrating security practices, scanning, and testing earlier in the software development lifecycle
- C) Postponing security testing until after production deployment to avoid slowing development
- D) Aligning script text to the left margin in CI/CD configuration files

#### Q1 Correct Answer

B — Shift-left moves security checks to the earliest feasible SDLC phase — at commit or pull request — so vulnerabilities are caught when they are cheapest to fix and the developer still has full context on the code.

#### Q1 Distractor Analysis

- *Why A is incorrect:* Shift-left is a workflow timing concept, not a physical or organizational relocation.
- *Why C is incorrect:* Delaying security testing until production is the opposite of shift-left and maximizes remediation cost.
- *Why D is incorrect:* The term refers to placement on the SDLC timeline, not text formatting or file structure.

---

### Question 2

Which statement most accurately describes the DevSecOps cultural principle?

- A) Security is exclusively the responsibility of the dedicated security team and should not slow down developers
- B) Security controls, scanning, and responsibility are shared among developers, operations, and security throughout the CI/CD pipeline
- C) DevSecOps replaces the need for penetration testing and manual code review entirely
- D) Security checks should be performed only at the final production deployment gate to avoid pipeline slowdown

#### Q2 Correct Answer

B — The core DevSecOps principle is that security belongs to everyone: developers own secure coding, operations owns secure infrastructure, security teams own tooling and policy — all simultaneously and continuously.

#### Q2 Distractor Analysis

- *Why A is incorrect:* Siloing security within one team is the traditional model that DevSecOps explicitly replaces.
- *Why C is incorrect:* DevSecOps augments but does not replace manual security activities like penetration testing.
- *Why D is incorrect:* A single late-stage gate is the opposite of shift-left and reintroduces the bottleneck DevSecOps is designed to eliminate.

---

### Question 3

At which SDLC phase should Static Application Security Testing (SAST) be triggered in a DevSecOps pipeline?

- A) After the application is deployed to production, as the full codebase is then available
- B) Only during scheduled quarterly security audits to avoid slowing daily builds
- C) At the code commit or pull request stage, before merging into the main branch
- D) During the design phase, before any code is written

#### Q3 Correct Answer

C — SAST analyzes source code without execution, making it ideal for the earliest code-available stage — commit or pull request — providing immediate developer feedback while context is fresh.

#### Q3 Distractor Analysis

- *Why A is incorrect:* Waiting until production means vulnerabilities have already been built, tested, and shipped, making them far more costly to fix.
- *Why B is incorrect:* Quarterly audits break the continuous feedback loop that is central to DevSecOps and allow vulnerabilities to accumulate.
- *Why D is incorrect:* SAST requires source code to analyze; it cannot run before code exists. Threat modeling is the appropriate design-phase security activity.

---

### Question 4

A development team discovers a SQL injection vulnerability during a post-production penetration test. Which DevSecOps improvement would most directly have prevented this from reaching production?

- A) Adding a web application firewall rule after deployment to filter malicious SQL input
- B) Requiring developers to attend annual security awareness training
- C) Integrating a SAST scanner into the pull request pipeline to flag SQL string concatenation patterns before merge
- D) Performing a manual code review once per sprint by a senior developer

#### Q4 Correct Answer

C — SAST tools configured with SQL injection rules flag unsafe string concatenation at the pull request stage, blocking the merge before the vulnerability can reach production.

#### Q4 Distractor Analysis

- *Why A is incorrect:* A WAF is a compensating control applied after deployment. It does not fix the vulnerable code and represents the opposite of shift-left.
- *Why B is incorrect:* Annual training alone does not provide the automated, consistent enforcement that a pipeline security gate provides on every commit.
- *Why D is incorrect:* Manual code review is inconsistent, does not scale, and is subject to reviewer fatigue. Automated SAST provides coverage on every change without these limitations.

---

### Question 5

A team wants to prevent hardcoded API keys and passwords from being committed to Git. Which pipeline control best addresses this risk at the earliest possible point?

- A) Require all developers to memorize credentials rather than writing them down
- B) Integrate a secrets scanning tool such as Gitleaks as a pre-commit hook to detect credential patterns before commits are finalized
- C) Enable full disk encryption on all developer workstations
- D) Store credentials in source code comments marked as private

#### Q5 Correct Answer

B — Pre-commit hooks run on the developer's machine before `git commit` finalizes, meaning the secret never enters the local commit object or remote repository. This is the earliest possible shift-left gate for secrets.

#### Q5 Distractor Analysis

- *Why A is incorrect:* Human memory is unreliable and does not prevent accidental commits. Automated enforcement is required for consistent protection.
- *Why C is incorrect:* Disk encryption protects data at rest on the device but does not prevent a developer from committing plaintext credentials to a remote repository.
- *Why D is incorrect:* Source code comments are fully visible in the repository and in Git history. Marking them private provides no technical protection.

---

### Question 6

Which of the following best describes the role of a "security champion" in a DevSecOps organization?

- A) A dedicated penetration tester who reports directly to the CISO and owns all security decisions
- B) A developer embedded in a product team who receives extra security training and bridges the team and the dedicated security organization
- C) An automated pipeline bot that reviews pull requests for security vulnerabilities
- D) A compliance officer who reviews code changes for regulatory requirements before deployment

#### Q6 Correct Answer

B — Security champions are developers within product teams who act as security ambassadors, handling first-level security questions, promoting secure coding practices, and escalating to the security team when needed.

#### Q6 Distractor Analysis

- *Why A is incorrect:* A penetration tester performs offensive security testing; this is a distinct role from a security champion and does not describe the team-embedded model.
- *Why C is incorrect:* Automated pipeline tools are technology, not people. A security champion is a human role with a cultural and educational function.
- *Why D is incorrect:* Compliance officers focus on regulatory requirements; security champions focus on developer security education and secure coding practices within their teams.

---

### Question 7

In a DevSecOps pipeline, Software Composition Analysis (SCA) is primarily concerned with which of the following?

- A) Scanning first-party application source code for insecure coding patterns such as SQL injection
- B) Scanning third-party open-source dependencies and libraries for known CVEs and license violations
- C) Testing a running application by sending crafted HTTP requests to discover runtime vulnerabilities
- D) Scanning container images for OS-level package vulnerabilities before pushing to a registry

#### Q7 Correct Answer

B — SCA tools analyze the dependency tree (package.json, requirements.txt, pom.xml) against vulnerability databases like the NVD to identify known CVEs in libraries the application depends on.

#### Q7 Distractor Analysis

- *Why A is incorrect:* Scanning first-party source code for coding pattern vulnerabilities is SAST, not SCA.
- *Why C is incorrect:* Sending crafted HTTP requests to a running application describes DAST, not SCA.
- *Why D is incorrect:* Scanning container images for OS-level package vulnerabilities is container image scanning (tools like Trivy or Grype), a distinct category from SCA.

---

### Question 8

Which DevSecOps feedback loop scenario best demonstrates the shortest possible time from vulnerability introduction to developer notification?

- A) A weekly scheduled pipeline job that scans the entire repository and emails a report to the security team
- B) A pre-commit hook on the developer's workstation that blocks the commit if a vulnerability pattern is detected
- C) A nightly build that runs SAST and creates tickets assigned to the developer's manager
- D) A quarterly penetration test report that lists vulnerabilities discovered in production

#### Q8 Correct Answer

B — A pre-commit hook fires before the commit is created on the developer's local machine — the absolute earliest possible detection point, with zero delay between introduction and notification.

#### Q8 Distractor Analysis

- *Why A is incorrect:* Weekly scheduled jobs introduce up to a 7-day lag, during which the developer has moved on and lost context on the code.
- *Why C is incorrect:* Nightly builds introduce overnight lag and routing through a manager adds additional delay, making the feedback loop significantly longer than a pre-commit hook.
- *Why D is incorrect:* Quarterly penetration tests are the longest possible feedback loop — vulnerabilities may have been in production for months before discovery.

---

### Question 9

Which sequence correctly represents the shift-left order of security tool placement from earliest to latest in a DevSecOps pipeline?

- A) DAST, SCA, SAST, secrets scanning
- B) Secrets scanning, SAST, SCA, DAST
- C) SCA, SAST, DAST, secrets scanning
- D) SAST, secrets scanning, DAST, SCA

#### Q9 Correct Answer

B — Secrets scanning runs at pre-commit (earliest), SAST runs at commit and pull request, SCA runs at build when dependencies are downloaded, and DAST runs at staging against the running application (latest of this set).

#### Q9 Distractor Analysis

- *Why A is incorrect:* DAST requires a running application and is among the latest stages; placing it first inverts the shift-left model entirely.
- *Why C is incorrect:* SCA requires the build system to download dependencies and cannot run before code is committed; placing it before SAST is out of order.
- *Why D is incorrect:* Secrets scanning should run at pre-commit before SAST; this sequence places SAST first, which is a later pipeline stage.

---

### Question 10

An organization's security team insists on manually reviewing every pull request before it can merge, causing a 3-day wait per PR. Which DevSecOps approach best resolves this bottleneck while maintaining security?

- A) Eliminate security review entirely to restore development velocity
- B) Automate SAST, SCA, and secrets scanning as required pipeline status checks on every PR, reserving manual security review for high-risk changes only
- C) Require developers to self-certify that their code has no security issues before submitting a PR
- D) Move security review to a monthly batch process to reduce interruptions for the security team

#### Q10 Correct Answer

B — Automating the mechanical parts of security review handles the majority of routine PRs without manual intervention, while preserving human review for genuinely high-risk changes where human judgment adds value.

#### Q10 Distractor Analysis

- *Why A is incorrect:* Eliminating security review removes essential protection and violates the DevSecOps principle of continuous security.
- *Why C is incorrect:* Developer self-certification is unverifiable and inconsistent — automated enforcement is required for reliable security posture.
- *Why D is incorrect:* Monthly batch reviews create a multi-week feedback loop, reintroduce the exact bottleneck DevSecOps is designed to eliminate, and allow vulnerabilities to accumulate across many PRs before detection.
