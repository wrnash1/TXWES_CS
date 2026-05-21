# Quiz: Module 01 - DevOps Fundamentals and the DevSecOps Mindset

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What does the term "shift-left" mean in DevSecOps methodology?

* A) Moving the development team to another office location
* B) Integrating security practices, scanning, and testing earlier in the software development lifecycle
* C) Postponing security testing until after production deployment
* D) Aligning script text to the left margin in configuration files
* **Correct Answer:** B) Shift-left brings security scanners directly into the developer's commit pipeline, resolving issues before deployments occur.
* **Distractor Analysis:**
  * *Why B is correct:* Shift-left moves security checks to the earliest feasible SDLC phase — at commit or pull request — so vulnerabilities are caught when they are cheapest to fix.
  * *Why A is incorrect:* Shift-left is a workflow timing concept, not a physical or organizational relocation.
  * *Why C is incorrect:* Delaying security testing until production is the opposite of shift-left and maximizes remediation cost.
  * *Why D is incorrect:* The term refers to the software development lifecycle timeline, not text formatting.

---

**Question 2**
Which of the following most accurately describes the DevSecOps cultural principle?

* A) Security is exclusively the responsibility of the dedicated security team and should not slow down developers
* B) Security controls, scanning, and responsibility are shared among developers, operations, and security throughout the CI/CD pipeline
* C) DevSecOps replaces the need for penetration testing and manual code review entirely
* D) Security checks should be performed only at the final production deployment gate to avoid pipeline slowdown
* **Correct Answer:** B) DevSecOps integrates security as a shared responsibility across all roles at every pipeline stage, not a handoff at the end.
* **Distractor Analysis:**
  * *Why B is correct:* The core DevSecOps principle is that security belongs to everyone — developers own secure coding, operations owns secure infrastructure, and security teams own tooling and policy — all simultaneously.
  * *Why A is incorrect:* Siloing security within one team is the traditional model that DevSecOps explicitly replaces.
  * *Why C is incorrect:* DevSecOps augments but does not replace manual security testing activities like penetration testing.
  * *Why D is incorrect:* A single late-stage gate is the opposite of shift-left and reintroduces the bottleneck DevSecOps is designed to eliminate.

---

**Question 3**
At which SDLC phase should Static Application Security Testing (SAST) be triggered in a DevSecOps pipeline?

* A) After the application is deployed to production, as the full codebase is then available
* B) Only during scheduled quarterly security audits to avoid slowing daily builds
* C) At the code commit or pull request stage, before merging into the main branch
* D) During the design phase, before any code is written
* **Correct Answer:** C) Running SAST at commit/pull request catches insecure code patterns while the context is fresh and before the vulnerability propagates downstream.
* **Distractor Analysis:**
  * *Why C is correct:* SAST analyzes source code without execution, making it ideal for the earliest code-available stage — commit or pull request — providing immediate developer feedback.
  * *Why A is incorrect:* Waiting until production means vulnerabilities have already been built, tested, and shipped, making them far more costly to fix.
  * *Why B is incorrect:* Quarterly audits break the continuous feedback loop that is central to DevSecOps.
  * *Why D is incorrect:* SAST requires source code to analyze; it cannot run before code exists. Threat modeling is the appropriate design-phase activity.

---

**Question 4**
A development team discovers a SQL injection vulnerability during a post-production penetration test. Which DevSecOps improvement would most directly have prevented this from reaching production?

* A) Adding a web application firewall (WAF) rule after deployment
* B) Requiring developers to attend annual security awareness training
* C) Integrating a SAST scanner into the pull request pipeline to flag SQL string concatenation patterns before merge
* D) Performing a manual code review once per sprint by a senior developer
* **Correct Answer:** C) A SAST tool configured with SQL injection rules would flag unsafe string concatenation at the pull request stage, blocking the merge before the vulnerability could reach production.
* **Distractor Analysis:**
  * *Why C is correct:* SAST tools like Semgrep and SonarQube have rules targeting SQL concatenation anti-patterns; integrating them as a required pipeline gate directly prevents this class of vulnerability from merging.
  * *Why A is incorrect:* A WAF is a compensating control applied after deployment — it does not fix the vulnerable code and represents the opposite of shift-left.
  * *Why B is incorrect:* Annual training alone does not provide the automated, consistent enforcement that a pipeline security gate provides on every commit.
  * *Why D is incorrect:* Manual code review is inconsistent and does not scale; automated SAST provides coverage on every change without reviewer fatigue.

---

**Question 5**
A team wants to prevent hardcoded API keys and passwords from being committed to Git. Which pipeline control best addresses this risk?

* A) Require all developers to memorize credentials rather than writing them down
* B) Integrate a secrets scanning tool (such as Gitleaks or truffleHog) as a pre-commit hook and CI pipeline gate to detect credential patterns before they are merged
* C) Enable full disk encryption on all developer workstations
* D) Store credentials in code comments marked as "private — do not share"
* **Correct Answer:** B) Secrets scanners detect credential patterns (API key formats, high-entropy strings, private key headers) in committed files, blocking the push or merge before the secret enters Git history.
* **Distractor Analysis:**
  * *Why B is correct:* Tools like Gitleaks run regex and entropy checks against staged or committed files, catching secrets at the earliest possible point before they enter version control history where they are extremely difficult to fully remove.
  * *Why A is incorrect:* Human memory is unreliable and does not prevent accidental commits; automated enforcement is required.
  * *Why C is incorrect:* Disk encryption protects data at rest on the device but does not prevent a developer from committing plaintext credentials to a remote repository.
  * *Why D is incorrect:* Source code comments are fully visible in the repository and in Git history; marking them "private" provides no technical protection.
