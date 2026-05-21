# Quiz: Module 09 - Incident Response – Containment and Recovery
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which DNS email authentication record cryptographically signs outbound email messages using a private key, allowing receiving mail servers to verify the message was not tampered with in transit?

*   A) SPF (Sender Policy Framework) — publishes a list of authorized sending IP addresses in DNS to prevent spoofed sender addresses
*   B) DKIM (DomainKeys Identified Mail) — adds a digital signature to email headers that receiving servers validate using a public key published in DNS
*   C) DMARC (Domain-based Message Authentication, Reporting, and Conformance) — specifies the policy action for messages that fail SPF and DKIM checks
*   D) MX (Mail Exchange) — specifies which mail servers are authorized to receive email for a domain
*   **Correct Answer:** B) DKIM (DomainKeys Identified Mail) — adds a digital signature to email headers that receiving servers validate using a public key published in DNS.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SPF authorizes sending IP addresses via a DNS TXT record but does not use cryptographic signing. It verifies the sending server's IP, not message integrity.
    *   *Why B is correct:* DKIM uses asymmetric cryptography — the sending server signs the email with its private key, and the receiving server retrieves the corresponding public key from DNS to validate the signature. This confirms both sender identity and message integrity.
    *   *Why C is incorrect:* DMARC is a policy layer that sits on top of SPF and DKIM; it defines what to do when those checks fail (quarantine, reject, none) and provides reporting. It does not itself sign messages.
    *   *Why D is incorrect:* MX records route inbound email to the correct mail server; they have no role in authentication or message signing.

---

**Question 2**
In incident response, which of the following most accurately defines **short-term containment**?

*   A) Rebuilding a compromised system from a known-clean baseline image after the threat has been fully eradicated and all persistence mechanisms have been removed
*   B) Immediate actions taken to stop an active attack from spreading further — such as EDR network isolation or blocking a malicious IP — while preserving evidence and keeping the system running for forensic collection
*   C) The process of identifying all systems affected by the same malware campaign by pivoting on shared IOCs across SIEM log data and EDR telemetry
*   D) Conducting a post-incident lessons-learned review to identify gaps in detection capability and update IR runbooks based on findings from the resolved incident
*   **Correct Answer:** B) Immediate actions taken to stop an active attack from spreading further — such as EDR network isolation or blocking a malicious IP — while preserving evidence and keeping the system running for forensic collection.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Rebuilding from a clean baseline describes the Recovery phase, which occurs after eradication — not short-term containment. Recovery restores operation; containment stops the spread.
    *   *Why B is correct:* Short-term containment prioritizes speed — stopping lateral movement and C2 communication immediately — without destroying the evidence on the compromised system. EDR network isolation is the canonical short-term containment action: it severs network access while leaving the running system intact for memory forensics.
    *   *Why C is incorrect:* Pivoting on shared IOCs to identify additional affected systems is scoping activity that occurs during the Detection and Analysis phase, before or alongside containment — it is not containment itself.
    *   *Why D is incorrect:* Post-incident lessons-learned review is the final phase of the NIST IR lifecycle (Post-Incident Activity) — it occurs after the incident is fully resolved, not during the active response.

---

**Question 3**
An incident responder has confirmed and contained a ransomware infection on a Windows workstation using EDR network isolation. The team is now preparing for eradication. Which action must be completed before the system can be returned to production?

*   A) Restore the system from the most recent backup without performing any further analysis, since the backup predates the infection
*   B) Remove all malware artifacts, delete attacker-created persistence mechanisms, reset compromised credentials, and patch the exploited vulnerability — then verify no threats remain with a post-eradication scan
*   C) Re-enable the network connection on the isolated workstation to test whether the ransomware binary reactivates when C2 access is restored
*   D) Submit the malware hash to VirusTotal and wait for at least three antivirus engines to confirm detection before proceeding with any eradication steps
*   **Correct Answer:** B) Remove all malware artifacts, delete attacker-created persistence mechanisms, reset compromised credentials, and patch the exploited vulnerability — then verify no threats remain with a post-eradication scan.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Restoring from backup without addressing the root cause (the exploited vulnerability and any remaining persistence) will result in reinfection as soon as the attacker retries the same attack vector. Eradication must close the attack path before recovery.
    *   *Why B is correct:* Complete eradication requires: (1) removing all malicious files and processes, (2) eliminating persistence mechanisms (scheduled tasks, registry run keys, malicious services), (3) resetting all credentials that may have been harvested, and (4) patching the initial vulnerability. The post-eradication scan confirms the environment is clean before recovery begins.
    *   *Why C is incorrect:* Re-enabling network access on a system still containing active ransomware would restore C2 connectivity to the attacker — this is the opposite of containment and would cause active harm.
    *   *Why D is incorrect:* Waiting for VirusTotal confirmation is a threat intelligence step; it does not replace the eradication actions required to remove the threat from the compromised system and is not a prerequisite for eradication.

---

**Question 4**
After eradicating ransomware from a workstation, the IR team restores the system from a verified pre-infection backup. Before returning the workstation to production, which validation step is most critical?

*   A) Run a password audit tool against the restored system to confirm all local account passwords meet the current complexity policy
*   B) Verify the exploited vulnerability that allowed initial compromise is patched on the restored system, confirm the EDR agent reports no active threats, and test that the attack vector is no longer exploitable
*   C) Compare the restored system's hostname and IP configuration against the asset inventory to confirm it matches pre-incident records
*   D) Survey the workstation's primary user to confirm they have not received any additional suspicious emails since the incident was contained
*   **Correct Answer:** B) Verify the exploited vulnerability that allowed initial compromise is patched on the restored system, confirm the EDR agent reports no active threats, and test that the attack vector is no longer exploitable.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A password audit is a good security hygiene step but does not validate that the root cause of the incident has been remediated. If the exploited vulnerability is still present on the restored system, the attacker can reinfect regardless of password strength.
    *   *Why B is correct:* Recovery validation must confirm three things: (1) the system is clean (EDR reports no active threats), (2) the initial attack vector is closed (the exploited vulnerability is patched), and (3) the fix is verified (targeted scan or test confirms the vulnerability is gone). Without this validation, the restored system is as vulnerable as the original.
    *   *Why C is incorrect:* Verifying hostname and IP configuration is an asset management check; it does not validate that the security issue that caused the incident has been resolved.
    *   *Why D is incorrect:* Surveying the user for suspicious emails is a useful awareness step but does not validate that the compromised system has been properly remediated and secured before returning to production.

---

**Question 5**
An organization wants to minimize the time between initial compromise detection and successful containment to reduce attacker dwell time. Which two controls together best achieve this goal?

*   A) Deploy full-disk encryption on all endpoints and configure automatic BitLocker recovery key management through Active Directory
*   B) Deploy EDR agents with automated network isolation capability that triggers when a high-confidence malware alert fires, and maintain pre-approved IR playbooks that authorize Tier 1 analysts to initiate isolation without waiting for Tier 2 approval
*   C) Require all remote access connections to use VPN with certificate-based authentication and disable split-tunnel configurations
*   D) Enforce a patch management policy requiring critical patches to be deployed within 72 hours of release across all production systems
*   **Correct Answer:** B) Deploy EDR agents with automated network isolation capability that triggers when a high-confidence malware alert fires, and maintain pre-approved IR playbooks that authorize Tier 1 analysts to initiate isolation without waiting for Tier 2 approval.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Full-disk encryption protects data at rest on powered-off devices; it has no effect on attacker dwell time once a system is actively compromised and running.
    *   *Why B is correct:* Dwell time reduction requires both fast detection-to-containment technology (EDR automated isolation executes in seconds when a high-confidence alert fires) and fast human decision authority (pre-approved playbooks eliminate approval delays that extend attacker access). Together these collapse the detection-to-containment window from hours to minutes.
    *   *Why C is incorrect:* VPN with certificate auth improves remote access security but does not affect how quickly a detected compromise on an already-connected endpoint is contained.
    *   *Why D is incorrect:* A 72-hour patch window reduces the attack surface by closing vulnerabilities, which reduces initial compromise risk — but it does not affect containment speed after a compromise has already been detected.
