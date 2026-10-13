# Video Script — Module 03, Part 2: Application Attacks and Software Vulnerabilities (Applied and Exam Strategy)

## CIS-4328 Information Security | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CompTIA Security+ (SY0-701) Complete Training Course &bull; Module 03</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy" title="Professor Messer &bull; CompTIA Security+ (SY0-701) Complete Training Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Professor Messer &bull; CompTIA Security+ (SY0-701) Complete Training Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

### Instructor: Professor Nash | CompTIA Security+ SY0-701 Alignment

### Estimated Duration: 11 minutes

---

## Opening

**[INSTRUCTOR ON CAMERA]**

Welcome back to Module 03. In Part 1 we covered the major application attack categories: injection attacks, XSS, CSRF, memory exploitation, and directory traversal. In Part 2 we will connect these to secure development principles, discuss static and dynamic testing, and work through SY0-701-style scenarios.

---

## Section 1 — Secure Coding Principles

**[SHOW DIAGRAM: Secure Software Development Lifecycle. Six phases from left to right: Requirements, Design, Development, Testing, Deployment, Maintenance. Below each phase, a security activity: Requirements = Threat Modeling; Design = Security Architecture Review; Development = Secure Coding Guidelines; Testing = SAST and DAST; Deployment = Penetration Testing; Maintenance = Patch Management.]**

**[Alt-text: Horizontal six-phase SDLC diagram. Phase 1: Requirements — Threat Modeling. Phase 2: Design — Security Architecture Review. Phase 3: Development — Secure Coding Guidelines. Phase 4: Testing — SAST and DAST. Phase 5: Deployment — Penetration Testing. Phase 6: Maintenance — Patch Management and Vulnerability Scanning. Caption: Security activities at each SDLC phase.]**

The most cost-effective place to address application vulnerabilities is during development — not after deployment. The cost of fixing a flaw increases by an order of magnitude at each lifecycle stage.

**Input Validation** — every piece of input from outside the application boundary must be treated as untrusted and validated against expected type, format, length, and range before processing. This single principle defeats injection attacks and directory traversal.

**Output Encoding** — all data written to output channels — HTML, SQL, OS commands, LDAP — must be encoded for that specific context. HTML encoding, SQL parameterization, and OS command escaping are each different and context-specific.

**Principle of Least Privilege** — application components and database accounts should run with only the permissions required for their specific function.

**Error Handling** — applications must not reveal internal implementation details, stack traces, database structure, or server paths in error messages visible to users. Error details belong in server-side logs.

**Secure Defaults** — features not required should be disabled. Default credentials must be changed before deployment.

---

## Section 2 — Static and Dynamic Analysis

**[SHOW DIAGRAM: Two-column comparison. Left column: Static Analysis (SAST) — runs at development time, examines source code without executing, finds hardcoded credentials and injection patterns. Right column: Dynamic Analysis (DAST) — runs against a live application, sends test inputs and analyzes responses, finds runtime authentication and session management flaws.]**

**[Alt-text: Two-column table. Left column header: SAST — Static Application Security Testing. Content: Runs without executing code. Examines source, bytecode, or binaries. Finds injection flaws, hardcoded secrets, insecure functions. Right column header: DAST — Dynamic Application Security Testing. Content: Requires running application. Sends inputs and observes outputs. Finds authentication flaws, runtime injection, session management issues.]**

**Static Application Security Testing (SAST)** analyzes source code, bytecode, or binaries without executing the program. It identifies hardcoded credentials, dangerous function calls, missing input validation, and SQL query construction from string concatenation.

**Dynamic Application Security Testing (DAST)** tests a running application by sending inputs and analyzing outputs. It finds vulnerabilities that only manifest during execution — authentication flaws, session management weaknesses, and runtime injection vulnerabilities.

**Fuzzing** sends large volumes of random, malformed, or unexpected input to discover how an application handles edge cases. Applications that crash on fuzzed input may have buffer overflow or input handling vulnerabilities.

**Penetration Testing** is an authorized, goal-oriented attack simulation combining automated tools with manual exploitation to identify and demonstrate exploitable vulnerabilities.

---

## Section 3 — Vulnerability Scoring

**[SHOW DIAGRAM: CVSS severity scale. Horizontal bar from 0 to 10. Colored sections: 0.0 = None; 0.1-3.9 = Low; 4.0-6.9 = Medium; 7.0-8.9 = High; 9.0-10.0 = Critical. Below the scale, three metric groups: Base (inherent), Temporal (exploit availability), Environmental (org relevance).]**

**[Alt-text: Horizontal severity bar. Left to right: None (0.0), Low (0.1-3.9), Medium (4.0-6.9), High (7.0-8.9), Critical (9.0-10.0). Below the bar, three boxes: Base Metrics — inherent characteristics of the vulnerability; Temporal Metrics — current exploit availability and patch status; Environmental Metrics — relevance to the specific organization.]**

**CVSS — Common Vulnerability Scoring System** rates vulnerability severity on a scale of 0 to 10. Three metric groups: Base (inherent characteristics), Temporal (exploit availability and patch status), and Environmental (relevance to the organization's specific context). A Critical score of 9.0–10.0 represents remote exploitation with no authentication and full system compromise.

**CVE — Common Vulnerabilities and Exposures** is a public dictionary of known vulnerabilities with unique identifiers. Once published, a CVE provides both defenders and attackers with documentation of the vulnerability.

Organizations prioritize patching based on CVSS score, asset criticality, and whether active public exploits exist.

---

## Section 4 — Exam Scenario Walkthroughs

**[INSTRUCTOR ON CAMERA]**

Three Module 03 scenarios.

**Scenario A:**

A developer builds a web form that constructs a database query by concatenating the user's input directly into the query string. An attacker submits a crafted input that terminates the original query and appends a command to return all records from the users table including password hashes. What is the attack and what is the correct fix?

Answer: SQL injection. The fix is parameterized queries. The query structure is defined first and user input is bound as a parameter. The database engine treats bound parameters as data, never as executable SQL syntax.

**Scenario B:**

A security analyst finds that user-submitted comments on a community forum execute JavaScript in other users' browsers when those users view the comment thread. The analyst demonstrates that the script can steal authenticated session cookies. What vulnerability is present and what two defenses address it?

Answer: Stored XSS. Defense one: output encoding — encode user-supplied content before inserting it into HTML. Defense two: HttpOnly cookie flag — prevents JavaScript from reading session cookies even if XSS executes.

**Scenario C:**

A SAST tool identifies three instances where the application builds file paths by appending user-supplied filenames to a base directory without validation. What vulnerability is this and what is the fix?

Answer: Directory traversal. The fix is to validate user-supplied filenames against an allowlist of permitted values, or to canonicalize paths and confirm they remain within the expected base directory before any file access.

---

## Section 5 — Exam-Day Decision Tree for Module 03

**[INSTRUCTOR ON CAMERA]**

Here is your Module 03 exam-day decision tree.

Attack targets a database via user input — SQL injection. Fix: parameterized queries.

Malicious script executes in another user's browser on a legitimate site — XSS. Stored in a database = stored XSS. In a URL requiring a click = reflected XSS. Fix: output encoding, CSP, HttpOnly cookies.

Authenticated user's browser submits unintended request to a trusted site — CSRF. Fix: CSRF tokens, SameSite cookie attribute.

Data written past a buffer boundary overwrites return address or adjacent memory — buffer overflow. OS defenses: ASLR, DEP/NX, stack canaries.

Application navigates outside its permitted directory using path sequences — directory traversal. Fix: path validation and allowlisting.

Server-side application makes requests to internal resources on behalf of attacker — SSRF. Fix: outbound URL restriction.

Match the scenario to the pattern first, then select the correct defense. These six cover the large majority of Module 03 exam questions.

Visit **professormesser.com** for video lectures and **comptia.org** for official exam objectives.

---

## Closing

**[INSTRUCTOR ON CAMERA]**

Module 03 is complete. Application attacks are the layer between the network perimeter and the data. Understanding both the attack mechanics and the defensive coding patterns prepares you for the exam and for real-world security work.

Complete the Reading Guide, Lab, Quiz, and Discussion before the deadline. See you in Module 04 — Network Attacks.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 03 Part 2

Proprietary and Confidential. Not for disclosure outside of authorized course use.
