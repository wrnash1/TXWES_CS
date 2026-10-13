# Video Script: Module 09 — Incident Response: Containment and Recovery

## Course: CIS-4332 Cyber Analyst

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

## Estimated Duration: 20-22 minutes

---

## SEGMENT 1 — Opening (0:00–1:30)

Welcome back. In Module 08 we covered the Detection and Analysis phase of the NIST incident response lifecycle — how to triage alerts, classify them, determine scope, and escalate with a structured note. You know how to recognize that an incident is happening and how to communicate what you have found.

Today we move into Phase 3 of the NIST lifecycle: Containment, Eradication, and Recovery. This is where you act. The analysis is done. You have a confirmed incident. Now you need to stop it from spreading, remove the threat completely, and bring the environment back to a verified-clean operational state.

I want to frame this module with a principle that will serve you on the exam and in the job: the sequence matters. Contain first. Then eradicate. Then recover. Violating that order leads to reinfection, evidence loss, or incomplete remediation. Every exam scenario question in this domain is testing whether you know the correct sequence and can apply it to a realistic situation.

---

## SEGMENT 2 — Containment: Short-Term and Long-Term (1:30–5:00)

[SHOW DIAGRAM: Short-term vs. long-term containment side by side with timeline arrow]

Containment has two phases, and the exam tests both.

Short-term containment is your immediate response. The goal is to stop the attacker from accessing any more of your environment right now — before you even fully understand the scope of what happened. The critical point is that short-term containment must not destroy evidence. This is where most analysts make a costly mistake: they shut down the compromised system.

Shutting down a system destroys volatile memory. When a machine is powered off, you lose everything in RAM — running processes, network connections, injected code, decrypted credentials in memory. That data is gone permanently. The correct short-term containment action for a running compromised system is EDR network isolation. The EDR agent cuts the system's network access while leaving it powered on. The attacker's C2 connection drops. Lateral movement stops. But the system is still running, RAM is intact, and you can collect forensic evidence.

Other short-term containment actions include: blocking the malicious IP at the firewall, disabling the compromised user account in Active Directory, revoking active session tokens or API keys, and temporarily blocking the C2 domain in your DNS resolver. All of these actions stop the attacker's access without touching the affected systems themselves.

Long-term containment is what happens after you have collected initial evidence and while you are working through a thorough response. It involves more durable measures that give the organization time to fully remediate without leaving the environment exposed. Long-term containment might include rebuilding a heavily compromised system on a hardened baseline while the original remains isolated, deploying temporary compensating controls like enhanced monitoring or additional firewall rules, or restricting the scope of a compromised service account while you reset credentials across all affected systems.

Think of short-term containment as the tourniquet and long-term containment as the splint. The tourniquet stops the bleeding immediately. The splint keeps things stable while you get to the operating room.

---

## SEGMENT 3 — Eradication (5:00–9:00)

After containment, you eradicate. This means completely removing every trace of the threat from every affected system.

[SHOW DIAGRAM: Five-step eradication checklist as numbered flow]

Step one: Remove all malware artifacts. Every malicious file, every dropped binary, every encoded script that the attacker deployed. Do not assume you found everything in the initial triage. Search for all IOCs identified during scope determination, including those found through pivoting. If the malware had multiple components, they all need to go.

Step two: Remove all persistence mechanisms. This is the step that most often gets missed and causes reinfection. Attackers do not rely on a single persistence mechanism. A typical intrusion might use a registry run key, a scheduled task, a malicious service, and a startup folder entry — all pointing to the same payload. You need to find and remove all of them. Use your EDR to query every system in scope for the known persistence IOCs. A system that had the C2 domain queried is potentially compromised — check its persistence mechanisms even if the main hash was not found there.

Step three: Reset all compromised credentials. Any account that may have been accessed by the attacker during the incident needs its password reset. This includes the account used for initial access, any accounts the attacker may have discovered through credential dumping, and any service accounts the attacker authenticated with during lateral movement. If you are not sure which accounts were accessed, reset everything in the affected scope. Credentials that are not reset are a free re-entry point.

Step four: Patch the exploited vulnerability. If the attacker got in through an unpatched Apache server, a vulnerable VPN appliance, or a phishing-exploited macro execution path — that vulnerability must be closed before the system goes back online. Recovering a system with the same exploited vulnerability on it is not recovery. It is inviting the same attack to happen again.

Step five: Verify eradication. Do not declare eradication complete based on manual removal alone. Run a targeted EDR hunt query for all known IOCs across all systems in scope. Run an authenticated vulnerability scan against affected hosts to confirm the patched vulnerability is remediated. Document the verification results. Eradication is only complete when the verification evidence exists in the incident ticket.

---

## SEGMENT 4 — Recovery (9:00–13:30)

Recovery is the process of returning affected systems to normal, verified-clean operations. There are three approaches, and the right one depends on the severity of the compromise and the criticality of the system.

The first approach is restoration from a verified backup. If a pre-infection backup exists and has been validated as clean — meaning the backup predates the initial compromise and has not been modified by the attacker — you restore from it. This is generally the fastest path for workstations and non-critical servers. The critical qualification is "verified." A backup that was taken after initial compromise may contain the malware. Check your backup timestamps against the estimated time of initial compromise before you restore.

The second approach is reimaging from a clean baseline. For systems that cannot be trusted to be fully eradicated — heavily compromised systems, or systems where the backup integrity is uncertain — a full reimage is the right answer. You deploy a fresh OS image, reinstall required applications, and restore only data from verified clean sources. This approach is slower but provides the highest confidence that no malware artifacts remain.

The third approach is in-place remediation. For systems where eradication was thorough and verified, and where a rebuild is not practical — a production database server, for example — you may perform in-place remediation: manual removal, patching, credential reset, and persistence cleanup, followed by verification. This approach is appropriate when the scope of compromise was limited and the verification evidence is strong.

[SHOW DIAGRAM: Recovery validation checklist as five-item list]

Regardless of which recovery approach you use, you must complete validation before returning the system to production.

First: confirm the attack vector is closed. The exploited vulnerability must be patched. Do a targeted scan to verify. If you recovered from backup but did not patch, you are back at square one.

Second: confirm the EDR agent reports no active threats. After recovery, run a full EDR scan. No alerts, no suspicious processes, no network connections to known-bad infrastructure.

Third: run IOC hunt queries for all known indicators. Take every IOC from the incident — every hash, IP, domain, registry key, scheduled task name — and run a hunt query across the recovered system and all systems in scope. All queries should return negative.

Fourth: verify user functionality. Before closing the ticket, confirm the system owner can log in and that business-critical applications are functioning normally. A recovered system that cannot perform its intended function is not ready for production.

Fifth: document everything. The recovery validation evidence — scan output, hunt query results, functionality confirmation — must be attached to the incident ticket. This is your proof that the incident is genuinely resolved and that the attacker no longer has access.

---

## SEGMENT 5 — Ransomware Response (13:30–16:30)

Ransomware deserves specific attention because it has a different operational sequence than other malware and because exam questions frequently test ransomware response decisions.

[SHOW DIAGRAM: Ransomware response decision flow — contain, assess, eradicate, recover]

Step one is contain immediately. Every minute a ransomware infection is running, more files are being encrypted. Immediate EDR network isolation of every confirmed and potentially compromised system is the priority. Do not wait for a full scope determination before containing what you have confirmed.

Step two is assess backup integrity. This happens before you can recover, and it is more complex for ransomware than for other malware. Many ransomware operators delete or encrypt Volume Shadow Copies — the built-in Windows backup mechanism — before they start encrypting files. If the shadow copies are gone, local backups are gone. Check: are external or cloud backups intact? Are they from a date before the infection? Are they in a location the ransomware could reach?

Step three is assess the ransom decision. Organizations should not pay ransom without exhausting every recovery alternative first. Payment does not guarantee decryption. Payment funds further criminal operations. Payment may violate sanctions regulations depending on the ransomware group. The decision to pay, if made at all, requires executive and legal involvement — it is not an IR team decision.

Step four is eradicate before you restore. You do not restore a system from backup and then reconnect it to a network that still contains active ransomware. If you have ten systems in scope and only five have been confirmed and contained, the other five are still potentially infected. Restore into an isolated environment, verify clean, then reconnect to a network that has been cleared.

Step five is patch before reconnecting. Whatever the ransomware exploited to get in — a VPN vulnerability, a phishing-delivered macro, RDP with weak credentials — that vector must be closed before restored systems go back online.

---

## SEGMENT 6 — Post-Incident Activity (16:30–19:00)

Phase 4 of the NIST lifecycle is Post-Incident Activity. It happens after the incident is fully resolved — after systems are back in production and the attacker no longer has access. This phase is often skipped under pressure to move on to the next alert, but it is where the organization actually improves.

The lessons-learned review is a structured meeting that asks four questions: What happened? What did we do well? What could we have done better? What do we need to change?

From the lessons-learned review comes a specific set of outputs. Playbook updates — if this incident exposed a gap in the phishing playbook, update it. Detection rule updates — if the attacker's initial activity did not trigger any alert, create the detection. Infrastructure changes — if a vulnerable service enabled the attack, track the remediation in the vulnerability management program.

Management and regulatory reporting is the second post-incident output. For incidents involving protected data — PII, PHI, financial data, payment card data — there may be mandatory notification requirements. HIPAA breach notification, PCI DSS incident reporting, SEC disclosure for material incidents. The IR team's documentation of timeline, scope, and impact feeds directly into these reports.

Metrics reporting is the third output. Mean time to detect, mean time to contain, mean time to recover — these are the operational metrics that measure whether the security program is improving. Dwell time — the time between initial compromise and detection — is the most important single IR metric. A low dwell time means your detection is working. A high dwell time means attackers are operating in your environment undetected.

---

## SEGMENT 7 — Module Summary and Lab Preview (19:00–21:30)

Let me bring this together.

Containment stops the spread without destroying evidence. Short-term containment uses EDR isolation, account disablement, and blocking. Long-term containment provides stability during extended response. Never shut down a running compromised system as your first action.

Eradication requires removing every artifact, every persistence mechanism, resetting all compromised credentials, patching the exploited vulnerability, and verifying the result. All five steps. In scope means every system identified through IOC pivoting — not just the original alert host.

Recovery uses the appropriate approach — backup restoration, reimage, or in-place remediation — followed by a five-item validation checklist before return to production. Confirm the attack vector is closed before you put the system back online.

Post-incident activity produces lessons learned, playbook updates, and required reporting. It is how the organization gets measurably better after every incident.

In the lab this week, you will work through a complete containment and recovery scenario for the Meridian Financial Services incident introduced in Module 08. You will make containment decisions, build an eradication checklist for a multi-system scope, document a recovery validation plan, and write a post-incident summary suitable for management reporting.

For the CySA+ exam: know the NIST phase boundaries, know the correct containment actions by scenario, and know the difference between eradication and recovery. Those three concepts appear repeatedly across Domain 1 and Domain 3.

I will see you in the lab.

---

Texas Wesleyan University | CIS-4332 Cyber Analyst | Professor Nash
