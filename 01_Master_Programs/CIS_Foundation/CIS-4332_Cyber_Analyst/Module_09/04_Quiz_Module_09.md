# Quiz: Module 09 — Incident Response: Containment and Recovery

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer.

---

## Question 1

Which DNS email authentication record cryptographically signs outbound email messages using a private key, allowing receiving mail servers to verify the message was not tampered with in transit?

- A) SPF (Sender Policy Framework) — publishes a list of authorized sending IP addresses in DNS to prevent spoofed sender addresses
- B) DKIM (DomainKeys Identified Mail) — adds a digital signature to email headers that receiving servers validate using a public key published in DNS
- C) DMARC (Domain-based Message Authentication, Reporting, and Conformance) — specifies the policy action for messages that fail SPF and DKIM checks
- D) MX (Mail Exchange) — specifies which mail servers are authorized to receive email for a domain

Correct Answer: B

Distractor Analysis:

- A is incorrect. SPF authorizes sending IP addresses via a DNS TXT record but does not use cryptographic signing. It verifies the sending server's IP, not message integrity.
- B is correct. DKIM uses asymmetric cryptography — the sending server signs the email with its private key, and the receiving server retrieves the corresponding public key from DNS to validate the signature. This confirms both sender identity and message integrity.
- C is incorrect. DMARC is a policy layer that sits on top of SPF and DKIM; it defines what to do when those checks fail (quarantine, reject, none) and provides reporting. It does not itself sign messages.
- D is incorrect. MX records route inbound email to the correct mail server; they have no role in authentication or message signing.

---

## Question 2

In incident response, which of the following most accurately defines short-term containment?

- A) Rebuilding a compromised system from a known-clean baseline image after the threat has been fully eradicated and all persistence mechanisms have been removed
- B) Immediate actions taken to stop an active attack from spreading further — such as EDR network isolation or blocking a malicious IP — while preserving evidence and keeping the system running for forensic collection
- C) The process of identifying all systems affected by the same malware campaign by pivoting on shared IOCs across SIEM log data and EDR telemetry
- D) Conducting a post-incident lessons-learned review to identify gaps in detection capability and update IR runbooks based on findings from the resolved incident

Correct Answer: B

Distractor Analysis:

- A is incorrect. Rebuilding from a clean baseline describes the Recovery phase, which occurs after eradication — not short-term containment. Recovery restores operation; containment stops the spread.
- B is correct. Short-term containment prioritizes speed — stopping lateral movement and C2 communication immediately — without destroying the evidence on the compromised system. EDR network isolation is the canonical short-term containment action: it severs network access while leaving the running system intact for memory forensics.
- C is incorrect. Pivoting on shared IOCs to identify additional affected systems is scoping activity that occurs during the Detection and Analysis phase, before or alongside containment — it is not containment itself.
- D is incorrect. Post-incident lessons-learned review is the final phase of the NIST IR lifecycle (Post-Incident Activity) — it occurs after the incident is fully resolved, not during the active response.

---

## Question 3

An incident responder has confirmed and contained a ransomware infection on a Windows workstation using EDR network isolation. The team is now preparing for eradication. Which action must be completed before the system can be returned to production?

- A) Restore the system from the most recent backup without performing any further analysis, since the backup predates the infection
- B) Remove all malware artifacts, delete attacker-created persistence mechanisms, reset compromised credentials, and patch the exploited vulnerability — then verify no threats remain with a post-eradication scan
- C) Re-enable the network connection on the isolated workstation to test whether the ransomware binary reactivates when C2 access is restored
- D) Submit the malware hash to a threat intelligence feed and wait for confirmation before proceeding with any eradication steps

Correct Answer: B

Distractor Analysis:

- A is incorrect. Restoring from backup without addressing the root cause (the exploited vulnerability and any remaining persistence) will result in reinfection as soon as the attacker retries the same attack vector. Eradication must close the attack path before recovery.
- B is correct. Complete eradication requires: (1) removing all malicious files and processes, (2) eliminating persistence mechanisms (scheduled tasks, registry run keys, malicious services), (3) resetting all credentials that may have been harvested, and (4) patching the initial vulnerability. The post-eradication scan confirms the environment is clean before recovery begins.
- C is incorrect. Re-enabling network access on a system still containing active ransomware would restore C2 connectivity to the attacker — this is the opposite of containment and would cause active harm.
- D is incorrect. Waiting for threat intelligence confirmation is a useful enrichment step; it does not replace the eradication actions required to remove the threat from the compromised system and is not a prerequisite for eradication.

---

## Question 4

After eradicating ransomware from a workstation, the IR team restores the system from a verified pre-infection backup. Before returning the workstation to production, which validation step is most critical?

- A) Run a password audit tool against the restored system to confirm all local account passwords meet the current complexity policy
- B) Verify the exploited vulnerability that allowed initial compromise is patched on the restored system, confirm the EDR agent reports no active threats, and test that the attack vector is no longer exploitable
- C) Compare the restored system's hostname and IP configuration against the asset inventory to confirm it matches pre-incident records
- D) Survey the workstation's primary user to confirm they have not received any additional suspicious emails since the incident was contained

Correct Answer: B

Distractor Analysis:

- A is incorrect. A password audit is a good security hygiene step but does not validate that the root cause of the incident has been remediated. If the exploited vulnerability is still present on the restored system, the attacker can reinfect regardless of password strength.
- B is correct. Recovery validation must confirm three things: (1) the system is clean (EDR reports no active threats), (2) the initial attack vector is closed (the exploited vulnerability is patched), and (3) the fix is verified (targeted scan or test confirms the vulnerability is gone). Without this validation, the restored system is as vulnerable as the original.
- C is incorrect. Verifying hostname and IP configuration is an asset management check; it does not validate that the security issue that caused the incident has been resolved.
- D is incorrect. Surveying the user for suspicious emails is a useful awareness step but does not validate that the compromised system has been properly remediated and secured before returning to production.

---

## Question 5

An organization wants to minimize the time between initial compromise detection and successful containment to reduce attacker dwell time. Which two controls together best achieve this goal?

- A) Deploy full-disk encryption on all endpoints and configure automatic BitLocker recovery key management through Active Directory
- B) Deploy EDR agents with automated network isolation capability that triggers when a high-confidence malware alert fires, and maintain pre-approved IR playbooks that authorize Tier 1 analysts to initiate isolation without waiting for Tier 2 approval
- C) Require all remote access connections to use VPN with certificate-based authentication and disable split-tunnel configurations
- D) Enforce a patch management policy requiring critical patches to be deployed within 72 hours of release across all production systems

Correct Answer: B

Distractor Analysis:

- A is incorrect. Full-disk encryption protects data at rest on powered-off devices; it has no effect on attacker dwell time once a system is actively compromised and running.
- B is correct. Dwell time reduction requires both fast detection-to-containment technology (EDR automated isolation executes in seconds when a high-confidence alert fires) and fast human decision authority (pre-approved playbooks eliminate approval delays that extend attacker access). Together these collapse the detection-to-containment window from hours to minutes.
- C is incorrect. VPN with certificate auth improves remote access security but does not affect how quickly a detected compromise on an already-connected endpoint is contained.
- D is incorrect. A 72-hour patch window reduces the attack surface by closing vulnerabilities, which reduces initial compromise risk — but it does not affect containment speed after a compromise has already been detected.

---

## Question 6

A confirmed malware infection is contained on endpoint WS-SALES-11. The IR team begins eradication, removes the malware binary from disk, and returns the system to production. Three days later, the same malware hash reappears on WS-SALES-11 and the C2 connection is re-established. What was the most likely cause of re-infection?

- A) The malware's C2 server was not blocked at the network firewall during the initial containment phase
- B) A persistence mechanism — such as a registry run key or scheduled task — was not removed during eradication, causing the malware to reinstall itself at user logon
- C) The EDR agent on WS-SALES-11 was not updated with the latest threat intelligence signatures before the system was returned to production
- D) The user on WS-SALES-11 received a new phishing email containing the same malware after the system was returned to production

Correct Answer: B

Distractor Analysis:

- A is incorrect. If the C2 IP was not blocked, the re-established connection would be expected — but the reappearance of the same malware hash from an internal source (without a new download) points to persistence, not a new external delivery. A firewall block would prevent C2 communication but not prevent local persistence from re-executing.
- B is correct. Incomplete eradication — specifically missing a persistence mechanism — is the most common cause of re-infection after apparent remediation. A registry run key or scheduled task pointing to the malware binary will recreate the file if the binary was removed but the persistence entry remained. The malware reinstalls itself on the next user logon.
- C is incorrect. EDR signature updates affect detection capability, not the presence of an unremoved persistence mechanism. Even a fully updated EDR will see the malware re-execute if the scheduled task is still active.
- D is incorrect. A new phishing delivery would typically produce a different execution chain and possibly a different hash — a lure document delivering the dropper rather than the direct binary reappearance described. The identical hash reappearance points to a local persistence mechanism, not a new delivery.

---

## Question 7

During an IR investigation, a responder discovers that a compromised system's Volume Shadow Copies have all been deleted. The system has a daily incremental backup on an on-premises backup server and a weekly full backup in an immutable cloud storage bucket. The on-premises backup server is on the same VLAN as the compromised system. Which recovery option is safest to use?

- A) Use the most recent daily incremental backup from the on-premises server, since it provides the most current data and will minimize data loss
- B) Use the weekly full backup from the immutable cloud storage bucket, because the on-premises server's backup may have been accessed and corrupted by the attacker
- C) Delete the shadow copies on the backup server as well to ensure no infected snapshots are accidentally restored during recovery
- D) Restore directly from the running compromised system using live imaging tools to capture the current disk state before the ransomware deletes more files

Correct Answer: B

Distractor Analysis:

- A is incorrect. The on-premises backup server is on the same VLAN as the compromised system. Ransomware routinely traverses network shares to encrypt backup files. If the ransomware had network access to the backup server, the daily incrementals may be encrypted or corrupted. Using an on-premises backup from the same VLAN without first verifying its integrity is a significant risk.
- B is correct. Immutable cloud storage is specifically designed to be unmodifiable — even by compromised credentials or malware with network access. The immutable bucket backup cannot have been modified by the ransomware. Although it is older (weekly versus daily), it is the only backup with a high-confidence guarantee of integrity in this scenario.
- C is incorrect. Deleting shadow copies on the backup server destroys potential recovery data. The correct action is to verify backup integrity, not to delete backup artifacts.
- D is incorrect. Restoring from a running compromised system images the infected disk state — including the ransomware and all encrypted files. This is not a recovery procedure; it is copying the problem.

---

## Question 8

An IR team completes ransomware eradication, restores three affected workstations from clean backups, patches the exploited vulnerability on all three, and returns them to production. The next morning, one of the three workstations is reinfected with the same ransomware. The other two workstations remain clean. What is the most likely explanation?

- A) The immutable backup used for that workstation contained an older version of the ransomware binary that was not detected by the EDR agent during the restoration scan
- B) The patch for the exploited vulnerability was applied to the two clean workstations but not to the re-infected workstation before it was returned to production
- C) The EDR network isolation was not lifted until after the patch was applied on the re-infected workstation, which prevented the Windows Update service from downloading the patch
- D) The ransomware's C2 server sends re-infection payloads to previously observed victim IP addresses on a scheduled basis regardless of whether the host was cleaned

Correct Answer: B

Distractor Analysis:

- A is incorrect. If the immutable backup contained the ransomware binary, the EDR post-recovery scan would have detected it. Additionally, immutable backups cannot be modified — they represent a clean pre-infection state. The scenario specifies the two clean workstations remain unaffected, pointing to a differential between the three systems.
- B is correct. Recovery validation requires confirming the exploited vulnerability is patched on every restored system before return to production. If patching was missed on one of the three workstations, that system has the same vulnerability that allowed the original compromise — the attacker's attack path is still open. The re-infection of exactly one of the three workstations is consistent with one system missing the patch.
- C is incorrect. EDR network isolation prevents internet and LAN access, which could affect patch download — but the scenario states the patch was applied (to the two clean workstations). The question is about differential outcome after recovery, not about patch delivery mechanics.
- D is incorrect. Ransomware C2 infrastructure does send commands to beaconing hosts, but a host that has been restored, patched, and had its EDR cleaned would not beacon to the C2 — there is no active malware to initiate the connection. Re-infection by C2 callback requires the malware to already be running on the endpoint.

---

## Question 9

Which phase of the NIST SP 800-61 incident response lifecycle includes conducting a lessons-learned review, updating IR playbooks based on incident findings, and calculating mean time to detect and mean time to recover metrics?

- A) Phase 2 — Detection and Analysis
- B) Phase 3 — Containment, Eradication, and Recovery
- C) Phase 4 — Post-Incident Activity
- D) Phase 1 — Preparation

Correct Answer: C

Distractor Analysis:

- A is incorrect. Phase 2 (Detection and Analysis) is where alerts are triaged, incidents are classified, scope is determined, and severity is assigned. It does not include post-incident review or metrics calculation — those activities require the incident to be fully resolved first.
- B is incorrect. Phase 3 (Containment, Eradication, and Recovery) is where responders stop the attack, remove the threat, and restore operations. It is the active response phase. Lessons-learned review and playbook updates are retrospective activities that occur after Phase 3 is complete.
- C is correct. Phase 4 (Post-Incident Activity) encompasses all retrospective activities that follow incident closure: the formal lessons-learned meeting, playbook and detection rule updates, IR metrics reporting (MTTD, MTTR, dwell time), and regulatory reporting if required. NIST SP 800-61 specifically names this phase as the mechanism for continuous improvement.
- D is incorrect. Phase 1 (Preparation) is the proactive work done before incidents occur — building the IR capability, writing playbooks, training staff, and deploying tools. Preparation does not involve reviewing a resolved incident.

---

## Question 10

During the eradication phase of a phishing-delivered malware incident, the IR team removes the malware binary and the confirmed registry run key persistence entry from the affected endpoint. The team declares eradication complete. What critical step did the team most likely omit?

- A) The team did not search for additional persistence mechanisms — such as scheduled tasks, malicious services, or WMI subscriptions — that may have been installed alongside the registry run key
- B) The team did not generate a new corporate security awareness training module based on the phishing email content before completing eradication
- C) The team did not submit the malware binary hash to a public threat intelligence sharing platform before removing the file from disk
- D) The team did not reimage the affected endpoint from a clean baseline image rather than performing manual artifact removal

Correct Answer: A

Distractor Analysis:

- A is correct. A registry run key is one persistence mechanism — it is rarely the only one. Sophisticated malware and even commodity RATs typically establish multiple persistence layers: a registry run key, a scheduled task, a startup folder entry, and potentially a malicious service. Removing only the confirmed persistence entry while not verifying that no other persistence mechanisms exist is the most common eradication failure and the most common cause of re-infection after apparent remediation.
- B is incorrect. Security awareness training updates are a post-incident activity that may follow from the lessons-learned review — they are not part of the eradication checklist and do not affect whether the threat has been removed from the affected system.
- C is incorrect. Sharing threat intelligence is a valuable community contribution but is not a required eradication step. Delaying eradication to share intelligence would extend the incident unnecessarily.
- D is incorrect. Reimaging is one recovery approach — the highest-confidence approach — but in-place remediation (manual removal) is a legitimate recovery method when eradication is thorough and verified. The question identifies what was omitted from the eradication process, not what recovery method to use.

---

## Question 11 (5 points)

A ransomware incident has encrypted 80% of a file server's data. The IR team identifies the ransomware strain and confirms that no decryptor is publicly available. Backups exist from 72 hours ago. Which sequence correctly reflects the proper IR response order before restoring from backup?

- A) Restore from backup → identify the initial access vector → eradicate malware → resume normal operations
- B) Contain the affected systems → eradicate all malware and persistence mechanisms → validate backup integrity → restore from backup → verify restoration → resume operations
- C) Restore from backup first to minimize downtime → then investigate how the attack occurred → eradicate remaining threats
- D) Pay the ransom to receive the decryptor → then eradicate the malware → report to management

Correct Answer: B

Distractor Analysis:

- A is incorrect. Restoring from backup before eradicating the malware and identifying the initial access vector is the most common ransomware recovery mistake. If the attacker's persistence mechanisms are still present or the entry point is not closed, the restored data will be re-encrypted within hours.
- B is correct. The correct sequence is: contain (stop ongoing damage) → eradicate (remove all malware, persistence, and credentials used by the attacker) → verify backup integrity (confirm the backup is uninfected) → restore → validate → resume. Each step is a prerequisite for the next.
- C is incorrect. Restoring before eradication is a critical error. The attacker's foothold remains active and will re-encrypt the restored data. This sequence has been observed in real-world incidents causing organizations to pay ransom twice.
- D is incorrect. Paying ransom is not a recommended response by CISA, FBI, or any major IR framework. It does not guarantee decryption, funds criminal organizations, and does not eliminate the attacker's presence in the environment.

---

## Question 12 (5 points)

During a ransomware IR engagement, the IR team discovers that Volume Shadow Copies (VSS) on all affected servers were deleted. What does this finding indicate about the attacker's sophistication and how does it affect the recovery options?

- A) VSS deletion is automatic behavior by Windows during ransomware; it does not indicate attacker sophistication
- B) VSS deletion is a deliberate attacker action designed to eliminate the fastest recovery path — it forces the organization to rely on offline backup copies and indicates a more sophisticated adversary who researched Windows recovery mechanisms before deploying ransomware
- C) VSS deletion means no recovery is possible without paying the ransom
- D) VSS deletion only affects desktop systems; server data can still be recovered from VSS on domain controllers

Correct Answer: B

Distractor Analysis:

- A is incorrect. VSS deletion is not automatic Windows behavior. It is a deliberate attacker action executed via `vssadmin delete shadows /all /quiet`, `wmic shadowcopy delete`, or similar commands. Ransomware families explicitly include this step to eliminate easy recovery paths.
- B is correct. Deleting VSS copies before encryption is a well-documented ransomware pre-encryption step (ATT&CK T1490 — Inhibit System Recovery). It demonstrates the attacker understood Windows recovery mechanisms and deliberately removed the fastest recovery option. The organization must now rely on offline backup copies, which extends recovery time.
- C is incorrect. VSS deletion eliminates one recovery path but does not eliminate recovery entirely. Offline backups, cloud backups, and in some cases vendor-provided decryptors remain viable options.
- D is incorrect. VSS is a per-volume service and is not limited to domain controllers. Servers and workstations all maintain their own VSS snapshot stores which can all be deleted by a privileged attacker.

---

## Question 13 (5 points)

An IR team is responding to a confirmed intrusion on a hospital's network. The affected hosts include an employee workstation and a patient data server. Which containment approach is most appropriate given the criticality of the patient data server?

- A) Shut down the patient data server immediately to prevent further compromise
- B) Apply short-term network-based containment (block the server at the switch/firewall level) while preserving its availability for authorized clinical operations, and pursue long-term containment through isolation and credential rotation
- C) Do nothing to the patient data server — HIPAA prohibits security teams from interrupting access to patient records systems
- D) Restore the patient data server from backup immediately before investigating whether it is compromised

Correct Answer: B

Distractor Analysis:

- A is incorrect. Shutting down a patient data server in a hospital environment could disrupt clinical operations and patient care. IR decisions in healthcare must balance security response with patient safety — immediate shutdown is rarely appropriate for critical clinical systems.
- B is correct. Network-based containment isolates the server from the threat while preserving its ability to serve authorized clinical users on isolated segments. This is the standard approach for critical infrastructure during IR — contain the threat without eliminating availability. Long-term containment follows after clinical impact is assessed.
- C is incorrect. HIPAA does not prohibit security response to active threats — it requires protection of patient data, which includes active incident response. Security teams have both the authority and obligation to respond to active intrusions affecting PHI.
- D is incorrect. Restoring from backup before investigation destroys forensic evidence and assumes the current system is fully compromised without verification. Investigation must precede restoration decisions.

---

## Question 14 (5 points)

Which of the following actions during the containment phase most effectively prevents an attacker with compromised service account credentials from pivoting to additional systems?

- A) Blocking the attacker's source IP at the perimeter firewall
- B) Resetting the compromised service account password, revoking active sessions, and temporarily disabling the account until investigation is complete
- C) Running a full vulnerability scan on all servers to identify what CVEs the attacker may have exploited
- D) Reimaging the initially compromised endpoint

Correct Answer: B

Distractor Analysis:

- A is incorrect. Blocking the external source IP may stop inbound communication but does not invalidate the compromised credential. An attacker using valid credentials through legitimate services (VPN, cloud portal) can continue lateral movement even if the original entry IP is blocked.
- B is correct. If the attacker has valid credentials for a service account, the credential is the attack vector — not a specific IP or system. Resetting the password, revoking all active sessions using those credentials, and disabling the account eliminates the attacker's authentication capability across the entire environment.
- C is incorrect. Running a vulnerability scan during active containment adds network noise, may alert the attacker to increased detection activity, and does not prevent the attacker from using valid credentials to move laterally right now.
- D is incorrect. Reimaging the initially compromised endpoint addresses persistence on that system but does not invalidate the compromised credentials that the attacker can use from any other compromised host or external access point.

---

## Question 15 (5 points)

A lessons-learned review following a successful phishing incident identifies that the initial phishing email bypassed the email gateway because the malicious attachment was a password-protected ZIP file. The password was included in the email body. Which remediation recommendation addresses the root cause of the gateway bypass?

- A) Train users to never open ZIP files received by email
- B) Configure the email gateway to quarantine or flag password-protected archive attachments when the password appears in the same email message body
- C) Upgrade the email gateway software to the latest version
- D) Require all employees to use MFA on their email accounts

Correct Answer: B

Distractor Analysis:

- A is incorrect. Training users to never open ZIP files would block legitimate business use of ZIP archives. User training alone is also the lowest-effectiveness control for technical bypass techniques.
- B is correct. The root cause is that password-protected archives bypass content inspection, and attackers include the password in the email body to enable the victim to decrypt the payload themselves. Gateway rules that detect password-protected archives containing a password in the email body text — or that quarantine all encrypted archives — directly address this bypass technique.
- C is incorrect. The bypass technique works by design against all email gateways that cannot inspect encrypted archive content. A software version update does not change the fundamental limitation of encrypted archive inspection.
- D is incorrect. MFA protects account access but does not prevent the initial phishing email from being delivered or the user from opening the attachment. The root cause is email gateway bypass, not account credential theft.

---

## Question 16 (5 points)

An organization experiences a data breach affecting 75,000 customer records containing names, email addresses, and hashed passwords. Which regulatory notification requirement is most relevant and what is the typical notification timeline?

- A) No notification is required since only hashed passwords were exposed, not plaintext credentials
- B) HIPAA requires notification within 72 hours since the breach involves customer records
- C) Depending on applicable state breach notification laws and potentially GDPR (if EU subjects are involved), notification to affected individuals and regulators is required — GDPR mandates supervisory authority notification within 72 hours of discovery
- D) Notification is only required if the organization is a publicly traded company filing with the SEC

Correct Answer: C

Distractor Analysis:

- A is incorrect. Hashed passwords can be cracked, especially if weak hashing algorithms (MD5, SHA-1 without salting) were used. Most breach notification laws define personal data broadly — names and email addresses combined with hashed passwords typically trigger notification requirements regardless of encryption state.
- B is incorrect. HIPAA applies to protected health information (PHI) held by covered entities — healthcare providers, health plans, and their business associates. Customer records from a general organization that do not contain health information are not subject to HIPAA.
- C is correct. State breach notification laws (all 50 U.S. states have enacted them) and GDPR (if EU residents' data is involved) apply to this breach. GDPR specifically requires notification to the supervisory authority within 72 hours of discovery and to affected data subjects without undue delay when high risk to rights and freedoms is established.
- D is incorrect. Breach notification laws are not limited to publicly traded companies. All organizations handling personal data may have notification obligations depending on jurisdiction, regardless of public listing status.

---

## Question 17 (5 points)

During post-incident recovery, a system administrator restores a file server from a backup taken 5 days before the intrusion was detected. The intruder had been active in the environment for 11 days before detection. What significant risk does this recovery approach introduce?

- A) The restored backup may be infected because the backup was taken 5 days before detection but the attacker may have been present for 11 days — meaning the backup was created during active attacker dwell time
- B) Restoring from a 5-day-old backup violates NIST SP 800-61 requirements for 24-hour recovery
- C) The restored files will have incorrect timestamps because backup restoration modifies file metadata
- D) Backup restoration always reintroduces the ransomware payload that encrypted the original files

Correct Answer: A

Distractor Analysis:

- A is correct. If the attacker was active for 11 days before detection but the backup is only 5 days old, the backup was created 6 days into the attack. The attacker may have already planted persistence mechanisms, backdoors, or modified files before the backup was taken. Restoring from this backup does not guarantee a clean system — it may restore an already-compromised state. This is why backup integrity verification (checking for tampering, checking backup dates against earliest-known attacker activity) is critical before restoration.
- B is incorrect. NIST SP 800-61 does not mandate a 24-hour recovery requirement. Recovery timelines are organization-defined based on RTO and are not specified in the NIST guide.
- C is incorrect. Backup restoration processes typically preserve original file timestamps as part of the restore operation. Timestamp modification is not a systematic risk of the restoration process itself.
- D is incorrect. Backup restoration reintroduces the state of files at backup time — not the ransomware payload. If the backup predates ransomware encryption, the restored files should be their original unencrypted versions (though they may still contain attacker-planted malware if the backup was taken during attacker dwell time).

---

## Question 18 (5 points)

An organization's IR playbook specifies that all confirmed ransomware incidents must be reported to the FBI's Internet Crime Complaint Center (IC3) within 72 hours. This reporting obligation is best classified as which type of requirement?

- A) A regulatory requirement mandated by federal law
- B) An organizational policy requirement documented in the IR playbook — voluntary reporting aligned with federal guidance but not legally mandated for all private sector organizations
- C) A HIPAA requirement applicable to any organization regardless of industry
- D) A PCI DSS requirement applicable only to organizations that process payment cards

Correct Answer: B

Distractor Analysis:

- A is incorrect. IC3 reporting is not universally legally mandated for all private sector organizations. CISA and FBI strongly encourage reporting, and certain industries (critical infrastructure) have reporting requirements under CIRCIA, but IC3 reporting is generally voluntary for most private sector entities.
- B is correct. If the organization's IR playbook specifies IC3 reporting within 72 hours, that is an internal policy commitment. It reflects best-practice alignment with federal guidance and may support law enforcement investigation, but it is an organizational policy requirement, not a universal federal legal mandate.
- C is incorrect. HIPAA applies specifically to covered entities and business associates handling protected health information. It does not extend to all organizations experiencing ransomware.
- D is incorrect. PCI DSS has its own incident reporting requirements (notification to card brands and acquiring bank), but these are specific to payment card data compromise — not ransomware incidents generally.

---

## Question 19 (5 points)

After completing eradication of a Cobalt Strike beacon infection, the IR team confirms: the malware binary was deleted, the C2 IP was blocked, the compromised service account password was reset, and the registry run key was removed. What additional verification step is most important before declaring eradication complete?

- A) Verify that the antivirus software is updated and running on the affected system
- B) Run a full vulnerability scan to identify what CVE enabled the initial compromise
- C) Perform a comprehensive persistence mechanism audit — check scheduled tasks, services, WMI subscriptions, startup folders, and any remaining Cobalt Strike-specific artifacts (named pipes, injected processes) — and verify no lateral movement occurred to additional systems
- D) Submit the file hash to VirusTotal to confirm it is classified as malicious by multiple AV engines

Correct Answer: C

Distractor Analysis:

- A is incorrect. Antivirus running and updated is a good health check but does not verify that all persistence mechanisms were removed. Many Cobalt Strike artifacts are not detected by traditional antivirus.
- B is incorrect. Vulnerability scanning identifies configuration weaknesses, not active attacker persistence mechanisms. It is a useful post-incident hygiene step but does not verify eradication completeness.
- C is correct. Cobalt Strike and similar post-exploitation frameworks commonly create multiple persistence layers and may have enabled lateral movement before detection. A thorough persistence audit checking all persistence mechanism categories and a lateral movement assessment of adjacent systems is the critical eradication verification step before declaring the incident resolved.
- D is incorrect. VirusTotal detection rates confirm the file is malicious after the fact. Confirming the file is classified as malicious serves no verification purpose after it has already been deleted.

---

## Question 20 (5 points)

Which metric most directly measures the effectiveness of an organization's incident containment capability?

- A) Mean Time to Detect (MTTD)
- B) Number of incidents escalated to Tier 2 per month
- C) Mean Time to Contain (MTTC) — the average time from detection to successful isolation of the threat
- D) Number of security awareness training sessions completed per quarter

Correct Answer: C

Distractor Analysis:

- A is incorrect. MTTD measures detection speed — how quickly the SOC identifies a threat after it enters the environment. It measures detection capability, not containment capability.
- B is incorrect. Escalation volume measures SOC workflow activity and triage accuracy, not how quickly threats are contained after escalation.
- C is correct. Mean Time to Contain (MTTC) is the specific metric that measures containment effectiveness — how much time elapses between when an incident is detected and when the threat is successfully isolated and stopped from causing further damage. A low MTTC indicates effective containment processes and tooling.
- D is incorrect. Security awareness training metrics measure training program activity, not incident response speed or effectiveness.
