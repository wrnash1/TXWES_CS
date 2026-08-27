# Reading Guide: Module 09 — Incident Response: Containment and Recovery

## Course: CIS-4332 Cyber Analyst

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Introduction

Phase 3 of the NIST SP 800-61 incident response lifecycle — Containment, Eradication, and Recovery — is where analyst action transforms from analysis into resolution. Detection tells you what happened. Containment stops the damage. Eradication removes the threat. Recovery restores operations. Each step depends on the previous one: recovering before eradicating invites reinfection; eradicating before containing allows the attacker to spread further during remediation. This module covers all three sub-phases and connects them to ransomware response, post-incident activity, and the CySA+ exam domain expectations.

---

## Section 1 — Containment

### 1.1 Short-Term vs. Long-Term Containment

| Attribute | Short-Term Containment | Long-Term Containment |
|---|---|---|
| Timing | Immediate — within minutes of confirmed incident | After initial evidence collection; during extended response |
| Primary goal | Stop active attacker access and lateral movement now | Provide stable controlled environment during full remediation |
| Evidence impact | Must not destroy volatile evidence | May involve more disruptive actions (rebuild, reimage) |
| Typical actions | EDR network isolation, block malicious IP, disable compromised account, revoke session tokens | Rebuild compromised system, restrict service account scope, deploy temporary compensating controls |
| Business continuity impact | Minimal — system stays running | May require planned downtime |
| CySA+ test focus | Isolation vs. shutdown distinction | Long-term containment as stopgap before full recovery |

### 1.2 Containment Actions Reference

| Action | When to Use | What It Stops |
|---|---|---|
| EDR network isolation | Running compromised system — volatile evidence needed | C2 communication, lateral movement — system stays powered on |
| Firewall block (malicious IP) | C2 IP identified in any system in scope | Outbound beaconing from any host to that IP |
| DNS sinkhole (malicious domain) | C2 domain identified | All endpoints from resolving that domain |
| Account disable (Active Directory) | User account compromised or used for lateral movement | Authentication with that account from any system |
| Session token / API key revocation | Cloud service or application account compromised | Attacker-controlled active sessions |
| VLAN isolation | Critical server segment affected | Network reachability from infected hosts to critical assets |

### 1.3 Why Not Shutdown

Shutting down a compromised system is a common analyst instinct that creates an evidence catastrophe. Volatile data lost on shutdown:

- Running processes and process memory (injected code may only exist in RAM)
- Active network connections (live C2 connections visible only while running)
- Decrypted credentials in memory (LSASS memory — attacker's harvest from credential dumping)
- Encryption keys (may allow file decryption in ransomware cases if captured before shutdown)
- Unwritten disk buffers (unsaved log entries)

EDR network isolation severs the attacker's access without touching the system's running state. This is the correct action for all scenarios where the system is still running and evidence collection is needed.

---

## Section 2 — Eradication

### 2.1 Five-Step Eradication Checklist

```text
ERADICATION CHECKLIST

Step 1: REMOVE ALL MALWARE ARTIFACTS
  - Delete all identified malicious files across all in-scope systems
  - Remove dropped executables, scripts, encoded payloads
  - Use all IOCs from scope determination as search targets
  - Include systems identified through C2 domain queries, not just hash matches

Step 2: REMOVE ALL PERSISTENCE MECHANISMS
  - Query EDR for all known persistence IOCs across all in-scope systems
  - Registry run keys: HKCU\...\Run, HKLM\...\Run, HKLM\...\RunOnce
  - Scheduled tasks: query all tasks and compare against known-good baseline
  - Malicious services: query services and look for attacker-created service names
  - Startup folder entries
  - WMI subscriptions: common persistence mechanism missed by basic cleanup
  - All persistence mechanisms must be removed — not just the primary one found

Step 3: RESET ALL COMPROMISED CREDENTIALS
  - Reset password on initial access account
  - Reset all accounts accessed during lateral movement
  - Reset service accounts the attacker authenticated with
  - Revoke and regenerate API keys and certificates used during incident
  - When in doubt about scope: reset all accounts in affected OU

Step 4: PATCH EXPLOITED VULNERABILITY
  - Identify the initial access vulnerability
  - Apply vendor patch or configuration fix
  - If patch is not yet available: implement compensating control
  - Document patch application with version confirmation

Step 5: VERIFY ERADICATION
  - Run EDR hunt query for ALL known IOCs across ALL in-scope systems
  - Run authenticated vulnerability scan to confirm patched CVE is remediated
  - Check persistence mechanism query results: all negative
  - Document verification results in incident ticket
  - ERADICATION IS NOT COMPLETE UNTIL VERIFICATION EVIDENCE EXISTS
```

### 2.2 Common Eradication Failures

| Failure | Consequence |
|---|---|
| Removing primary binary but missing persistence | Malware reinstalls itself at next user login |
| Patching on one system but not all in scope | Attacker regains access through unpatched system |
| Not resetting credentials used during lateral movement | Attacker re-enters with known working credentials |
| Declaring eradication complete without verification scan | Undetected remnant triggers re-compromise within days |
| Eradicating before full scope is confirmed | Remaining uncontained systems reinfect remediated ones |

---

## Section 3 — Recovery

### 3.1 Recovery Approach Selection

| Approach | When to Use | Confidence Level | Speed |
|---|---|---|---|
| Restore from verified backup | Pre-infection backup confirmed clean; backup timestamp predates compromise | High if backup integrity verified | Fast — hours |
| Reimage from clean baseline | Compromise was deep; backup integrity uncertain; system heavily modified by attacker | Very high | Moderate — 4-8 hours per system |
| In-place remediation | Production system where rebuild is not practical; eradication was thorough and verified | Moderate — depends on eradication thoroughness | Fast but riskiest |

### 3.2 Backup Integrity Verification

Before restoring from backup, verify:

1. Backup timestamp predates the estimated initial compromise time
2. Backup storage location was not accessible by the attacker (offline backup, immutable cloud backup, air-gapped media)
3. Backup hash or integrity check passes
4. Ransomware has not encrypted or deleted the backup files

For ransomware specifically: check whether Volume Shadow Copies were deleted. Many ransomware families run vssadmin delete shadows commands before beginning file encryption. If shadow copies are gone, external offline backups may be the only option.

### 3.3 Recovery Validation Checklist

```text
RECOVERY VALIDATION — BEFORE RETURNING TO PRODUCTION

[ ] 1. Attack vector closed
    Confirm exploited vulnerability is patched on the recovered system.
    Run targeted vulnerability scan or service version check.
    A system restored from backup but not patched will be reinfected.

[ ] 2. EDR reports no active threats
    Run full EDR scan on recovered system.
    No active alerts, no suspicious processes, no malicious network connections.

[ ] 3. IOC hunt queries negative
    Run hunt query for every IOC from the incident:
      - File hashes
      - Registry key paths and values
      - Scheduled task names
      - Service names
      - Mutex names
    All results must be negative before return to production.

[ ] 4. User functionality verified
    System owner confirms login and business-critical applications function.
    A technically clean but non-functional system is not production-ready.

[ ] 5. Documentation complete
    Scan output attached to incident ticket.
    Hunt query results attached.
    Patch version confirmation attached.
    System owner sign-off documented.
    Return-to-production timestamp recorded.
```

---

## Section 4 — Ransomware Response Workflow

### 4.1 Ransomware-Specific Response Sequence

| Step | Action | Why |
|---|---|---|
| 1 | Contain immediately — EDR isolate all confirmed and suspected systems | Every running minute encrypts more files |
| 2 | Assess backup integrity — check shadow copies, offline/cloud backups, timestamps | Cannot plan recovery without knowing backup status |
| 3 | Assess ransom payment decision | Payment requires executive and legal involvement; never pay without exhausting alternatives |
| 4 | Eradicate before restoring | Restoring into an environment that still has active ransomware causes immediate reinfection |
| 5 | Patch before reconnecting | Initial access vector must be closed before restored systems rejoin the network |

### 4.2 Ransomware Backup Assessment Questions

- Was vssadmin delete shadows run? Check Windows Event Log 4688 (process creation) for vssadmin, wmic shadowcopy delete, bcdedit commands.
- Do offline or cloud backups exist that predate the infection?
- Are backup files accessible from the infected systems? If yes, they may be encrypted too.
- What is the oldest clean restore point available?
- What is the acceptable data loss window (RPO — Recovery Point Objective)?

---

## Section 5 — Post-Incident Activity

### 5.1 Lessons-Learned Review

The lessons-learned meeting should occur within five business days of incident closure while details are fresh. Required attendees: IR team leads, system owners of affected assets, CISO or security manager.

| Review Question | Output |
|---|---|
| What happened and what was the timeline? | Accurate incident timeline for records and reporting |
| What did we detect successfully? | Confirmation of working controls |
| What did we miss or detect late? | Detection gap identification |
| What slowed down our response? | Process or authority gap identification |
| What playbook updates are needed? | Specific playbook change items |
| What new detection rules are needed? | SIEM/EDR rule development backlog items |

### 5.2 Post-Incident Reporting Obligations

| Regulation / Standard | Trigger | Timeline |
|---|---|---|
| HIPAA Breach Notification | PHI of 500+ individuals disclosed | 60 days from discovery |
| PCI DSS Incident Reporting | Payment card data compromise | Immediate — within 24 hours to card brands |
| SEC Material Incident Disclosure | Material cybersecurity incident | 4 business days from materiality determination |
| GDPR Breach Notification | EU personal data breach | 72 hours from awareness |
| State Breach Notification Laws | PII of state residents disclosed | Varies by state (30-90 days typical) |

### 5.3 Key IR Metrics

| Metric | Definition | Why It Matters |
|---|---|---|
| Mean Time to Detect (MTTD) | Average time from initial compromise to first detection | Measures detection effectiveness |
| Mean Time to Contain (MTTC) | Average time from detection to successful containment | Measures response speed |
| Mean Time to Recover (MTTR) | Average time from containment to full service restoration | Measures remediation efficiency |
| Dwell Time | Time from initial compromise to detection | Most important single IR metric — attacker access window |
| Re-infection Rate | Percentage of contained systems reinfected after recovery | Measures eradication thoroughness |

---

## CySA+ Exam Tips

Exam Tip 1: The containment, eradication, recovery sequence is mandatory. Exam scenario questions will offer shortcuts — restoring before eradication, or patching without containing. Recognize these as wrong answers.

Exam Tip 2: EDR network isolation is correct; shutdown is wrong. When a scenario presents a running compromised system, the correct containment action preserves volatile evidence. Network isolation does. Shutdown does not.

Exam Tip 3: Eradication must address all persistence mechanisms — not just the initial malware binary. The exam will present scenarios where re-infection occurs. The root cause is almost always missed persistence.

Exam Tip 4: Credential reset scope is broader than most analysts assume. Any account the attacker may have touched — not just the directly compromised account — must be reset. Lateral movement means the attacker harvested credentials from every system they accessed.

Exam Tip 5: Recovery validation must confirm the attack vector is closed. Restoring from backup without patching the exploited vulnerability is explicitly tested as wrong on the exam.

Exam Tip 6: For ransomware questions, backup assessment precedes recovery planning. Before any restore decision, determine whether backups are clean, accessible, and pre-date the infection.

Exam Tip 7: Post-incident activity is Phase 4 of NIST SP 800-61. Lessons-learned review, playbook updates, and regulatory reporting are Phase 4 activities — not part of Phase 3. The exam may ask which phase specific activities belong to.

Exam Tip 8: Dwell time is the most important IR metric. Questions about measuring IR effectiveness most frequently point to dwell time as the indicator of detection capability. Lower dwell time = better detection.

---

## Glossary

- Containment: Actions taken to stop an incident from spreading before eradication begins
- Dwell Time: Time between initial compromise and detection; the attacker's undetected access window
- Eradication: Complete removal of threat artifacts, persistence mechanisms, and exploitation conditions from all affected systems
- EDR Network Isolation: EDR capability that severs a system's network access while leaving it powered on for evidence collection
- Immutable Backup: Backup storage that cannot be modified or deleted, even by compromised credentials — ransomware-resistant
- In-Place Remediation: Recovery by cleaning and patching the affected system without reimaging
- Lessons-Learned Review: Post-incident structured review producing detection gaps, playbook updates, and infrastructure recommendations
- MTTD: Mean Time to Detect — average time from compromise to first detection alert
- MTTR: Mean Time to Recover — average time from containment to full service restoration
- Reimage: Wiping and reinstalling a system from a clean OS baseline — highest-confidence recovery method
- Recovery Point Objective (RPO): Maximum acceptable data loss window; determines how far back in time a backup restore can go
- Recovery Time Objective (RTO): Maximum acceptable downtime before service must be restored
- Volatile Evidence: Data that exists only in RAM and is lost permanently on system shutdown
- Volume Shadow Copy (VSS): Windows built-in backup mechanism; frequently targeted for deletion by ransomware before encryption begins

---

## Study Checklist

- [ ] Explain the difference between short-term and long-term containment with two examples of each
- [ ] Explain why EDR network isolation is preferred over shutdown for a running compromised system
- [ ] List the five steps of the eradication checklist in order without notes
- [ ] Describe three persistence mechanisms that must be checked during eradication
- [ ] Explain the three recovery approaches and when each is appropriate
- [ ] Describe the five-item recovery validation checklist
- [ ] Explain the ransomware-specific response sequence and why eradication must precede recovery
- [ ] Describe how to assess backup integrity before a ransomware recovery
- [ ] Name four post-incident reporting obligations and their triggers
- [ ] Define dwell time and explain why it is the most important IR metric
- [ ] Review all eight exam tips
- [ ] Complete the Module 09 Lab
- [ ] Complete the Module 09 Quiz
- [ ] Post initial response to the Module 09 Discussion by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

**1. NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide**
<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf>
The foundational NIST publication defining the four-phase IR lifecycle. The full document (88 pages) covers preparation, detection and analysis, containment/eradication/recovery, and post-incident activity in detail. Sections 3.1 through 3.4 directly correspond to the content of this module and are the primary source for CySA+ IR phase questions.

**2. CISA — Ransomware Guide (Joint CISA/MS-ISAC)**
<https://www.cisa.gov/stopransomware/ransomware-guide>
The definitive U.S. government guidance document on ransomware response, covering preparation, detection, containment, eradication, recovery, and post-incident steps specific to ransomware. The guide includes the VSS deletion prevention hardening steps, backup protection strategies, and recovery sequencing covered in Section 4 of this module.

**3. FBI — IC3 Ransomware Reporting Portal**
<https://www.ic3.gov/>
The FBI Internet Crime Complaint Center's reporting portal for cybercrime including ransomware. Reviewing the portal's reporting guidance and recent ransomware advisories illustrates the federal reporting obligations and investigation support processes described in Section 6 of this guide. Law enforcement reporting after ransomware incidents is strongly encouraged and may provide decryptor resources in some cases.
