# Video Script: Module 10 — Application Security (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Pre-Roll Slate

**[SHOW SLIDE: Course title card — "CIS-4328 Information Security | Module 10 | Texas Wesleyan University"]**

---

## Opening — Part 2 Recap

**[INSTRUCTOR ON CAMERA]**

Welcome back. In Part 1 we worked through the first seven OWASP Top 10 categories. In Part 2 we finish the list, then spend the second half on the secure development lifecycle — the practices that prevent these vulnerabilities from shipping in the first place.

---

## Section 1 — A08: Software and Data Integrity Failures

**[SHOW SLIDE: A08 heading — CI/CD pipeline diagram]**

A08 covers situations where code and data integrity is not verified. This includes untrusted plugins or libraries loaded without integrity checks, and insecure CI/CD pipelines where an attacker can inject malicious code into the build process.

The SolarWinds supply chain attack of 2020 is the defining example for this category. Attackers compromised the SolarWinds build environment and inserted malicious code — SUNBURST — directly into legitimate software updates. Because the resulting binaries were signed with the real SolarWinds certificate, organizations trusted and deployed them. Approximately 18,000 organizations installed the compromised update.

Defenses include code signing, cryptographic hash verification of third-party packages, pipeline integrity controls, and Subresource Integrity checks for web-loaded scripts.

---

## Section 2 — A09: Security Logging and Monitoring Failures

**[SHOW SLIDE: A09 heading — SIEM dashboard screenshot]**

A09 addresses the inability to detect, escalate, and respond to active breaches. Without sufficient logging and monitoring, attackers can maintain persistence for months before detection. The Verizon Data Breach Investigations Report consistently finds that the median dwell time — the period between initial compromise and detection — exceeds weeks for many organizations.

Logging failures include not logging authentication events, not alerting on brute-force attempts, storing logs locally where attackers can delete them, and failing to monitor logs at all.

Countermeasures include centralized log aggregation in a SIEM, alerting on anomalous patterns, tamper-evident log storage, and defined incident response procedures that rely on log evidence.

---

## Section 3 — A10: Server-Side Request Forgery

**[SHOW SLIDE: A10 heading — SSRF attack diagram]**

SSRF is the newest Top 10 category, elevated from a note in 2017 to its own category in 2021 because of its rising prevalence in cloud environments. In an SSRF attack, an attacker causes the server to make HTTP requests to an attacker-controlled destination — or, more dangerously, to internal resources that should not be accessible from the internet.

In cloud environments, the most valuable SSRF target is the instance metadata service, or IMDS, at `169.254.169.254`. On AWS, a GET request to that address from within the instance returns temporary credentials for the instance's IAM role. An attacker who can trigger SSRF can retrieve those credentials and gain access to cloud resources.

Countermeasures include input validation of all server-side URL parameters, block-listing internal IP ranges, disabling redirects on outbound fetches, and network segmentation that prevents application servers from making arbitrary internal connections.

---

## Section 4 — Cross-Site Scripting (XSS)

**[SHOW SLIDE: XSS attack flow diagram — stored vs. reflected]**

While XSS does not have its own A0X number in the 2021 list, it falls under A03 Injection and remains heavily tested on Security+. XSS occurs when an attacker injects malicious client-side script into web pages viewed by other users.

There are three types. Reflected XSS occurs when malicious script is embedded in a URL parameter. The server reflects the script back in the response and the victim's browser executes it. This requires the victim to click a crafted link.

Stored XSS, also called persistent XSS, occurs when malicious script is saved in the application — a comment field, a profile name — and served to every user who views that content. Stored XSS is more dangerous because it does not require per-victim social engineering.

DOM-based XSS occurs entirely in the browser. The malicious script manipulates the Document Object Model without the payload ever reaching the server.

Countermeasures include output encoding, a Content Security Policy header, HttpOnly and Secure cookie flags, and input validation.

---

## Section 5 — The Secure Software Development Lifecycle

**[SHOW SLIDE: SDLC phase wheel — Requirements, Design, Development, Testing, Deployment, Maintenance]**

Now let's talk about how to build software that resists these attacks from the start. The Secure SDLC integrates security activities into every phase of development rather than treating it as a final checkpoint before release.

In the **Requirements phase**, teams gather security requirements alongside functional requirements. This includes regulatory requirements, data classification requirements, and threat modeling kickoffs.

In the **Design phase**, architects perform threat modeling using frameworks like STRIDE — Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege. Each threat is mapped to a design countermeasure. Secure design principles like least privilege, defense in depth, and fail-safe defaults are applied.

In the **Development phase**, developers follow secure coding standards. Peer code review with a security checklist is applied. Static analysis tools are integrated into the IDE.

In the **Testing phase**, both static and dynamic testing tools are run. Penetration testing and security review occur before release approval.

In the **Deployment phase**, the build pipeline enforces code signing and artifact integrity checks. Infrastructure is provisioned using hardened baselines.

In the **Maintenance phase**, the team monitors for new CVEs in dependencies, responds to vulnerability disclosures, and applies patches.

---

## Section 6 — SAST and DAST

**[SHOW SLIDE: SAST vs. DAST comparison table]**

Two testing approaches dominate Security+ exam questions on application testing: SAST and DAST.

**SAST** stands for Static Application Security Testing. It analyzes source code, bytecode, or compiled binaries without executing the application. SAST tools can find SQL injection patterns, buffer overflow risks, hardcoded credentials, and insecure API calls by reading the code. SAST is often integrated directly into the IDE or the code commit pipeline. The key phrase is "white-box" — the tool has visibility into the code internals.

Common SAST tools include Checkmarx, SonarQube, Veracode Static Analysis, and Semgrep.

**DAST** stands for Dynamic Application Security Testing. It tests the running application by sending crafted inputs and analyzing responses. DAST tools simulate an attacker's perspective — they do not have access to source code. DAST is "black-box" testing. It can find runtime issues that SAST misses because it observes actual application behavior.

Common DAST tools include OWASP ZAP, Burp Suite, and Nikto.

A mature security program uses both. SAST catches issues early in development when they are cheapest to fix. DAST validates the running application in a staging or pre-production environment.

**IAST** — Interactive Application Security Testing — is a third approach worth knowing. IAST agents instrument the application at runtime, sitting inside the running application and observing it from the inside. This combines the code-level visibility of SAST with the runtime accuracy of DAST.

---

## Section 7 — Code Signing

**[SHOW SLIDE: Code signing certificate chain diagram]**

Code signing is the process of applying a digital signature to software to verify its origin and integrity. A developer obtains a code-signing certificate from a trusted Certificate Authority. Before publishing, the developer uses their private key to sign the compiled binary. Users or operating systems verify the signature using the developer's public key certificate before executing the software.

Code signing provides two guarantees. First, **authenticity** — the software came from a specific, identified developer. Second, **integrity** — the binary has not been modified since signing.

Code signing does not guarantee the software is free of malware. The SolarWinds breach demonstrates this — the malicious code was signed because attackers compromised the legitimate build environment. But it does prevent third-party tampering after the build.

The Security+ exam tests code signing in the context of supply chain security and software integrity. Expect questions about what code signing proves, what it does not prove, and how it relates to the certificate trust chain.

---

## Section 8 — Security in CI/CD Pipelines

**[SHOW SLIDE: CI/CD pipeline stages with security gates highlighted]**

Modern software development uses Continuous Integration and Continuous Delivery pipelines. Code commits automatically trigger builds, tests, and deployments. Security gates inserted into this pipeline enforce security policy without manual bottlenecks.

A typical secure pipeline includes the following gates. At commit, a pre-commit hook blocks secrets from entering the repository. On pull request, SAST scans run automatically and must pass before merge. On build, dependency vulnerability scanning checks for known CVEs in all packages. On staging deployment, DAST scans run against the deployed application. Before production release, a final artifact signature verification confirms the binary matches what was built.

The term for integrating security into DevOps is DevSecOps. The "shift left" philosophy means moving security activities earlier in the lifecycle — to the left side of the timeline — where defects are less expensive to fix.

---

## Closing

**[INSTRUCTOR ON CAMERA]**

Application security is where the attacker meets the software. The OWASP Top 10 is your map of the ten most-traveled attack routes. The secure SDLC, SAST, DAST, and code signing are your engineering controls to close those routes before they reach production.

For the Security+ exam, know every OWASP category, understand the SAST versus DAST distinction, and be able to explain what code signing does and does not guarantee.

Complete the Reading Guide, the Lab, the Quiz, and the Discussion for Module 10. Module 11 moves into Incident Response — what happens when a breach does occur. I'll see you there.

---

*End of Part 2*
