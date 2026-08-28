# Video Script: Module 15 — Security Operations (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00–0:45]

Welcome back. This is Module 15, Part 2. In Part 1 we covered the SOC structure, SIEM platforms, SOAR automation, and vulnerability scanning with Nessus. Now we complete the Security Operations picture with patch management, configuration management baselines, change control procedures, and security metrics.

These topics are heavily tested in SY0-701 Domain 4 — Security Operations — so let's get into it.

---

### [SECTION 1: Patch Management — 0:45–4:00]

Patch management is the systematic process of identifying, acquiring, testing, and deploying software updates to fix vulnerabilities, bugs, and performance issues. It is one of the most impactful security controls an organization can operate — the majority of successful attacks exploit known, patchable vulnerabilities.

**The patch management lifecycle:**

**Step 1 — Inventory.** You cannot patch what you do not know you have. The first step is maintaining an accurate asset inventory — every operating system, application, firmware, and library across your environment. Tools like Nessus, Microsoft SCCM, Qualys, and Ansible can automate discovery.

**Step 2 — Monitor.** Subscribe to vendor security advisories, the NIST National Vulnerability Database (NVD), and threat intelligence feeds. When a new patch is released, you need to know about it quickly — especially for critical vulnerabilities like zero-days or actively exploited CVEs.

**Step 3 — Risk assessment.** Not every patch requires immediate deployment. Assess each patch based on:

- CVSS score of the underlying vulnerability
- Whether the vulnerability is being actively exploited in the wild
- Whether affected systems are internet-facing or internal
- Business criticality of the affected system

**Step 4 — Test.** Deploy the patch to a non-production test environment first. Patches can break applications, drivers, or configurations in unexpected ways. Testing reduces production risk.

**Step 5 — Deploy.** Roll out patches according to priority. Use defined maintenance windows to minimize business disruption. Automate patch deployment where possible using tools like WSUS (Windows Server Update Services), SCCM, or Ansible.

**Step 6 — Verify.** Confirm that the patch was successfully applied. Re-scan with Nessus or equivalent to verify the vulnerability is resolved.

**Step 7 — Document.** Maintain records of what was patched, when, on which systems, and by whom. This documentation supports compliance audits and incident response.

**Patch management SLAs** — many organizations define internal SLAs by severity:

- Critical: patch within 24–72 hours
- High: patch within 7–14 days
- Medium: patch within 30 days
- Low: patch within 90 days

**Compensating controls** — when a patch cannot be immediately deployed (legacy systems, vendor-unsupported software), deploy compensating controls: network segmentation, host-based firewall rules, IPS signatures, or enhanced monitoring to reduce risk while awaiting a patch window.

For the Security+ exam: understand the full patch lifecycle, know why testing before production deployment matters, and understand compensating controls for systems that cannot be patched.

---

### [SECTION 2: Configuration Management Baselines — 4:00–7:00]

A configuration management baseline is a documented, approved standard configuration for a specific type of system or device. It defines the minimum security settings that every system of that type must have before being deployed into production.

**Why baselines matter:**

- Systems deployed without hardening are vulnerable from day one
- Baselines ensure consistency — every web server, every workstation, every router starts from the same secure foundation
- Baselines provide a reference point for detecting unauthorized changes (drift)

**Baseline sources:**

**CIS Benchmarks** — the Center for Internet Security publishes detailed hardening benchmarks for hundreds of platforms: Windows Server, Ubuntu Linux, macOS, Cisco IOS, Microsoft Azure, AWS. These are freely available and widely considered the gold standard for configuration baselines.

**DISA STIGs** — the Defense Information Systems Agency publishes Security Technical Implementation Guides for US government and defense contractor systems. STIGs are extremely detailed and mandatory for DoD environments.

**Vendor hardening guides** — Microsoft, Red Hat, Cisco, and others publish their own hardening documentation.

**What a baseline typically covers:**

- Services and protocols to disable (unnecessary services increase attack surface)
- Password policy requirements (minimum length, complexity, lockout)
- Audit and logging configuration (what events to log)
- Network settings (firewall rules, port restrictions)
- User account management (default accounts disabled, administrator renamed)
- Encryption settings (TLS version minimums, disabled cipher suites)
- Application whitelisting or allowlisting

**Configuration drift** occurs when a system diverges from its baseline over time — due to ad-hoc changes, software installations, or misconfiguration. Security tools like Tripwire, AIDE, and CIS-CAT continuously monitor systems and alert when drift is detected.

**Hardening** is the process of applying a baseline to a new system before deployment. Key hardening steps include:

- Remove or disable unnecessary services and accounts
- Apply all current patches before deployment
- Enable host-based firewall
- Enable security logging and forward to SIEM
- Apply the applicable CIS Benchmark

For the Security+ exam: know what a baseline is, know CIS Benchmarks and DISA STIGs as sources, and understand configuration drift and hardening.

---

### [SECTION 3: Change Control — 7:00–10:00]

Change control — also called change management — is the formal process for requesting, reviewing, approving, and implementing changes to IT systems and infrastructure. It exists to prevent unauthorized or poorly tested changes from causing outages or introducing security vulnerabilities.

**Why change control matters from a security perspective:**

- Unauthorized changes are a leading cause of security incidents
- Attackers who gain privileged access often make unauthorized changes to maintain persistence
- Change records provide an audit trail that is essential during incident investigation

**The change management process:**

**Step 1 — Change Request (CR).** The person or team requesting the change submits a formal request describing: what will change, why, which systems are affected, what the rollback plan is, and the proposed maintenance window.

**Step 2 — Change Advisory Board (CAB) review.** The CAB — typically composed of representatives from IT operations, security, business units, and management — reviews change requests. The CAB assesses risk and authorizes or rejects the change.

**Emergency changes** bypass the full CAB review when immediate action is required (e.g., zero-day patch, active incident response). Emergency changes still require post-implementation review.

**Step 3 — Testing.** Changes are tested in a non-production environment prior to production deployment. The test results and sign-off are documented.

**Step 4 — Scheduled deployment.** Changes are deployed during an approved maintenance window. Communication is sent to affected stakeholders.

**Step 5 — Verification.** After deployment, the change is validated. Monitoring is increased to detect any unexpected consequences.

**Step 6 — Rollback if needed.** If the change causes problems, the documented rollback plan is executed. Systems return to their pre-change state.

**Step 7 — Documentation.** All steps, approvals, outcomes, and issues are documented in the change management system. This creates the audit trail.

**Change types:**

- **Standard change** — pre-approved, low-risk, well-understood procedure (e.g., scheduled monthly patching). Does not require individual CAB approval each time.
- **Normal change** — requires full CAB review and approval.
- **Emergency change** — expedited approval process for urgent situations.

For the Security+ exam: know the CAB, understand the purpose of rollback plans, and recognize that unauthorized changes are a security concern — they appear in incident scenario questions.

---

### [SECTION 4: Security Metrics — 10:00–13:00]

Security metrics translate security program activities into measurable outcomes that can be communicated to management, used to drive decisions, and tracked over time to demonstrate improvement.

**Why metrics matter:**

Without metrics, you cannot demonstrate that security investments are working, prioritize resources rationally, or identify trends that require attention.

**Operational security metrics:**

- **Mean Time to Detect (MTTD)** — average time from incident occurrence to SOC detection. Benchmark target: under 1 hour for critical incidents.
- **Mean Time to Respond (MTTR)** — average time from detection to containment. Shorter is better.
- **Mean Time to Patch (MTTP)** — average time from patch release to deployment. Critical patches should be under 72 hours for internet-facing systems.
- **Vulnerability count by severity** — tracked over time to show whether the organization is reducing its attack surface.
- **Patch compliance rate** — percentage of systems patched within the defined SLA. Target is 95%+ for critical patches.
- **Phishing simulation click rate** — percentage of employees who click on simulated phishing emails. Used to measure and drive security awareness training effectiveness.
- **Number of open critical vulnerabilities** — a direct measure of current exposure.
- **Security training completion rate** — percentage of employees who have completed mandatory security awareness training.

**Risk-based metrics:**

- **Risk Score** — aggregate score representing the organization's current risk posture, typically derived from asset criticality, vulnerability severity, and threat intelligence.
- **Third-party risk ratings** — vendor risk scores from platforms like BitSight, SecurityScorecard, or internal assessments.

**Reporting metrics to leadership:**

Security metrics for executive audiences should be translated from technical measures to business impact language. Instead of "we have 47 critical CVEs open," say "47 critical vulnerabilities affecting 12 revenue-generating systems are awaiting patches — they represent a potential breach risk estimated at $2.3M based on our risk model."

**Key Performance Indicators (KPIs) vs. Key Risk Indicators (KRIs):**

- **KPI** — measures the performance of the security program (e.g., patch compliance rate, training completion)
- **KRI** — measures current risk exposure (e.g., number of unpatched critical vulnerabilities, percentage of systems without EDR)

For the Security+ exam: MTTD and MTTR are the most commonly tested operational metrics. Know what they measure and why lower values are better.

---

### [CLOSING — 13:00–15:00]

Here is your Part 2 summary:

- Patch management follows a seven-step lifecycle: inventory, monitor, assess, test, deploy, verify, document. Define SLAs by severity level.
- Configuration baselines establish a secure starting point for every system type. CIS Benchmarks and DISA STIGs are the primary baseline sources. Watch for configuration drift.
- Change control prevents unauthorized and poorly tested changes through a formal CAB review process. Rollback plans are mandatory. Emergency changes get expedited approval but still require documentation.
- Security metrics provide measurable evidence of program effectiveness. MTTD and MTTR are key operational metrics. KPIs measure performance; KRIs measure risk exposure.

This completes Module 15. The lab will give you hands-on practice with vulnerability scanning and patch prioritization. The quiz will test both operational concepts and exam-day scenario skills.

Module 16 is our final module — full exam preparation for the Security+ SY0-701. We will review all five domains and work through practice questions together.

I will see you there.

---

*End of Part 2 Script*
