# Video Script: Module 15 — Post-Report Cleanup and Debriefing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4333. I am Professor Nash, and this is Module 15: Post-Report Cleanup
and Debriefing.

Last module we focused on the report itself. This module covers everything that happens after
the report is delivered — and there is more to that phase than most new pentesters expect.
Post-engagement responsibilities include removing every artifact you placed on client systems,
preserving and handling evidence correctly, verifying remediation when clients ask you back
for a retest, and conducting a thorough lessons-learned review with your own team.

Failing to complete post-engagement cleanup is not a minor oversight. It is an ethical and
legal liability. Tools, backdoors, and created accounts left on client systems are live
attack surface. If a real attacker exploits something you installed and forgot to remove,
the consequences for the client — and potentially for you — are serious.

This module aligns to PenTest+ Domain 5: Reporting and Communication, which you have been
working through across Modules 14 and 15. Let us begin with cleanup.

---

## SEGMENT 2 — Post-Engagement Cleanup (1:30–6:00)

### What Must Be Removed

Every artifact created during the engagement must be inventoried and removed. This is not
optional — it is a professional obligation, and in many engagements you will sign a cleanup
attestation confirming completion. The categories of artifacts to remove include:

**Shells and backdoors**: Any reverse shell listener, bind shell, web shell, or persistent
implant. This includes Meterpreter agents, Empire stagers, Netcat listeners, and any custom
C2 (command-and-control) beacons. Remove the files and terminate the associated processes.

**Persistence mechanisms**: Scheduled tasks, cron jobs, registry run keys, startup folder
entries, WMI subscriptions, and service installations created to maintain access. Check
the common persistence locations: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`,
`/etc/cron.d/`, `/etc/rc.local`, Task Scheduler in Windows, and any service entries you
created.

**Created user accounts**: Any local or domain accounts you created during the engagement.
Document the username and creation timestamp, then delete the account and verify deletion.
In Active Directory environments, verify the account no longer appears in `net user /domain`
output.

**Uploaded tools and payloads**: Binary files, scripts, payloads, and wordlists transferred
to target systems. Common staging locations include `C:\Windows\Temp\`, `/tmp/`, `/var/tmp/`,
and user profile directories. Remove these files and verify with a directory listing.

**Modified configurations**: Any firewall rule, network ACL, system setting, or application
configuration you altered to facilitate the engagement. Restore original values. If you
disabled Windows Defender to test persistence, re-enable it.

**Network listeners and tunnels**: SSH tunnels, SOCKS proxies, pivot listeners, and port
forwards established during the engagement. Close these connections and verify no unexpected
listening ports remain.

### The Cleanup Checklist

Use a systematic checklist approach. The best practice is to log every action you take during
the engagement — every tool dropped, every account created, every configuration changed. This
log is your cleanup guide. During cleanup you work through the log in reverse order, removing
what you added.

Many pentest teams maintain a running engagement log file that records:

- Timestamp of the action
- Target host IP and hostname
- Action taken (file uploaded, account created, persistence mechanism installed)
- File path or registry key affected
- Cleanup action required and completion status

A signed cleanup attestation is delivered to the client confirming that all artifacts have
been removed. This protects both parties.

### Why Cleanup Matters Legally and Ethically

Consider this scenario: you installed a Meterpreter agent on a server during an engagement
and the cleanup checklist entry was overlooked. Two months later, a real attacker discovers
the dormant agent, activates it, and uses it to exfiltrate customer data. Depending on how
this is investigated, the tester who left the agent may face civil liability claims and
potentially regulatory scrutiny.

Beyond legal exposure, leaving tools on client systems violates the fundamental professional
promise of penetration testing: "We are here to help you find and fix vulnerabilities, not
to create new ones."

---

## SEGMENT 3 — Evidence Handling and Chain of Custody (6:00–9:30)

### What Is Chain of Custody?

Chain of custody is the documented record of who collected, handled, stored, and transferred
evidence — from the moment it was captured to its final disposition. It is borrowed from
forensic investigation practice and applied to penetration testing to establish that evidence
is authentic and has not been tampered with.

For penetration testing, chain of custody matters for two reasons:

1. **Client assurance**: The client needs confidence that your evidence screenshots and
   output files accurately represent what was found, not fabricated or manipulated data.
2. **Legal protection**: In rare cases where a penetration test becomes a legal matter —
   a dispute about scope violations, or a security incident investigation — properly
   documented evidence with intact chain of custody is defensible. Improperly handled
   evidence is not.

### Evidence Collection Standards

Capture evidence in real-time during the engagement. Do not recreate screenshots from memory
after the fact. Key standards include:

- **Timestamps visible**: Ensure your testing machine's system clock is visible in
  screenshots, either in screen captures or in terminal output. Many testers run
  `date` commands before and after key actions.
- **Tester's IP visible**: Your IP address appearing in tool output (e.g., a reverse shell
  connection from your machine) proves the action was performed from the authorized testing
  host.
- **Unmodified output**: Save raw tool output as text files in addition to screenshots.
  Raw files are harder to manipulate and easier to reference than screenshots.
- **Hash verification**: For binary evidence files, compute and record SHA-256 hashes at
  the time of collection. This allows you to prove the file has not been modified.

### Evidence Storage and Destruction

Store engagement evidence in an encrypted container or encrypted storage volume. Use full-disk
encryption (BitLocker, VeraCrypt, or FileVault) on your testing laptop and use an additional
encrypted vault (such as a VeraCrypt container) for engagement evidence files.

Evidence retention periods are defined in the engagement contract. A typical retention period
is 30–90 days post-report delivery, after which evidence is securely destroyed. Secure
destruction means overwriting or cryptographically erasing the storage — not simply deleting
files.

When delivering evidence to a client (for example, raw scan outputs they requested), use
encrypted file transfer: encrypted email with PGP/GPG, a secure file transfer portal, or
password-protected archives with the password transmitted via a separate channel.

---

## SEGMENT 4 — Retesting and Remediation Verification (9:30–13:00)

### What Is a Retest?

A retest — also called a remediation verification or follow-on assessment — is a
bounded engagement in which the tester returns to the client environment to verify that
previously identified findings have been successfully remediated. The retest is typically
scoped to the specific vulnerabilities from the original engagement, not a full re-assessment.

Retests are scheduled in advance and governed by a brief statement of work that references
the original engagement and defines:

- Which specific findings (by ID: FIND-001, FIND-002, etc.) are in scope for verification
- The testing window
- What constitutes verification success (the finding can no longer be exploited using the
  original method)

### How to Verify Remediation

For each finding in scope, the tester attempts to reproduce the original vulnerability using
the same method documented in the report. The outcome is one of three statuses:

**Remediated**: The original exploitation path no longer succeeds. Document the verification
attempt, the result, and the verification date. Update the finding status in the retest report.

**Partially Remediated**: The original exploitation path is blocked but an alternative path
to the same vulnerability class still succeeds, or the root cause has not been fully addressed.
Document both what was fixed and what remains. Issue a partial remediation finding.

**Not Remediated**: The vulnerability remains exploitable using the original method. Document
the verification attempt and failure, and restate the original risk rating.

### The Retest Report

A retest report is a shorter document than the original engagement report. It typically
contains:

- Reference to the original report (date, engagement ID)
- A table listing each finding, its original risk rating, the verification method used,
  and its current remediation status
- Narrative notes on any partially remediated findings
- A new attestation statement covering the retest scope and dates

Some clients request a "clean bill of health" letter — a one-page executive summary confirming
that all critical and high findings have been successfully remediated. This is commonly used
to satisfy auditor, regulatory, or cyber insurance requirements.

### Scope Discipline in Retesting

The retest scope is bounded by the original findings. If during retesting you discover a new
vulnerability unrelated to the original engagement, you do not exploit it as part of the
retest. Document the observation and bring it to the client's attention as an out-of-scope
finding that warrants a separate engagement.

---

## SEGMENT 5 — Lessons Learned and After-Action Review (13:00–16:00)

### The After-Action Review

An after-action review (AAR) is an internal team discussion conducted after the engagement
deliverables are complete. It is separate from the client debrief and is not shared with the
client. The purpose is to improve your team's methodology, tooling, and processes for future
engagements.

A structured AAR answers four questions:

1. **What was supposed to happen?** — What did the rules of engagement, scope, and testing
   plan call for?
2. **What actually happened?** — What did the engagement actually achieve? Where did the
   testing plan succeed or break down?
3. **What went well?** — Techniques, tools, communication approaches, and timeline management
   that worked effectively and should be repeated.
4. **What needs improvement?** — Obstacles encountered, tools that failed or were unavailable,
   scope misunderstandings, communication gaps, or findings that were almost missed.

### Documenting Lessons Learned

AARs should be documented — not just discussed verbally. A brief structured document (one
to two pages) capturing the four questions creates institutional knowledge. Over time, these
documents reveal patterns: recurring tooling gaps, client communication issues that need
better handling, or methodological blind spots.

Lessons-learned outputs may include updates to:

- The firm's pentest methodology documentation
- Tool configuration standards or playbooks
- Pre-engagement scoping questionnaire templates
- Report template improvements

### Personal Professional Development

Module 15 is also a moment to reflect on your own development as a practitioner. What did
you learn during this engagement? What would you do differently? What technique or tool
would you like to research and add to your personal toolkit before the next engagement?

Building a habit of self-reflection and continuous learning is what separates effective
senior pentesters from testers who plateau after a few years.

---

## SEGMENT 6 — Post-Engagement Client Communication (16:00–18:30)

### Follow-Up Communication

After report delivery and the initial debrief, maintain a communication channel with the
client for a defined follow-up period — typically 30 days. During this window, the client's
team will be reading the report, discussing findings, and beginning remediation planning.
They will have questions.

Common follow-up questions include:

- "Can you help us understand finding FIND-003 better? Our developers are not sure what
  code change is needed."
- "The vendor for our firewall says this vulnerability is a false positive. Can you review
  their response?"
- "We are prioritizing which findings to fix first — can you walk us through your
  recommended sequencing?"

Respond to these questions promptly and completely. Your value to the client does not end
at report delivery.

### Scheduling the Retest

During the debrief or follow-up period, discuss retest scheduling. Retests are most valuable
when scheduled 30–60 days after report delivery — enough time for the client team to
implement fixes, but not so long that the fixes sit unverified.

When a client indicates they will not be scheduling a retest (common with budget-constrained
organizations), document this in your follow-up communication and note that unverified
remediation carries residual risk.

### Maintaining Engagement Records

Retain all engagement documentation — contracts, rules of engagement, testing logs, report
drafts, and final deliverables — for the retention period specified in your contract. After
that period, execute secure destruction procedures and document the destruction.

Engagement records are your protection if a dispute arises about scope, timing, or findings.
Without documentation, disputes are difficult to resolve in your favor.

---

## SEGMENT 7 — Legal and Ethical Obligations Post-Engagement (18:30–21:00)

### Ongoing NDA Obligations

As discussed in Module 14, your NDA obligations survive the engagement. Do not discuss client
findings, vulnerabilities, or infrastructure publicly. Do not use findings from one client
engagement to benefit another client. Each client's confidential information is a separate
protected asset.

### Responsible Disclosure and Third-Party Findings

During your engagement you may discover a vulnerability in a third-party commercial product
(a vendor application, a network appliance, or a security tool) rather than in the client's
own custom software. This creates a responsible disclosure situation.

You have an obligation to notify the vendor through their responsible disclosure or bug
bounty program. Coordinate with your client — they should typically be informed before you
file the disclosure, since the disclosure may reference their environment. Follow the vendor's
disclosure timeline process and do not publish details before a patch is available.

### Scope Violations and Unauthorized Access

If during the engagement you discover that you inadvertently accessed a system or resource
outside the authorized scope — through a routing misconfiguration, a pivot that went further
than intended, or a misidentified IP address — stop immediately and notify the client and
your firm's legal counsel. Document exactly what happened, what systems were accessed, and
what actions were taken on those systems.

Scope violations must be disclosed, not concealed. Attempting to cover up an accidental
scope violation compounds the problem and may convert an honest mistake into intentional
unauthorized access.

### Data Handling After Engagement Completion

All client data retained during the engagement — extracted files, captured credentials,
database dumps used as evidence — must be destroyed according to the contract terms. This
includes:

- Deleting files from testing laptops and external drives
- Wiping lab virtual machines used during the engagement
- Removing cloud storage copies
- Documenting the destruction

Treat client data with the same seriousness as the cleanup of your tools on their systems.

---

## SEGMENT 8 — Summary and PenTest+ Exam Points (21:00–24:00)

Module 15 covers the professional obligations that occur after the report is delivered.

Post-engagement cleanup requires removing every artifact: shells, backdoors, created accounts,
uploaded tools, modified configurations, and network listeners. Maintain an engagement log
during testing so cleanup is systematic and complete. Provide a signed cleanup attestation.

Chain of custody establishes that evidence is authentic and unmodified. Capture timestamps
and tester IP in screenshots, hash evidence files, store evidence encrypted, and destroy
evidence per contract terms.

Retests verify that previously identified findings have been remediated. Report remediation
status as Remediated, Partially Remediated, or Not Remediated. Scope retests to the original
findings only.

After-action reviews improve your team's methodology and document institutional knowledge.

Post-engagement client communication includes responding to questions, scheduling retests,
and maintaining records for the contractual retention period.

Legal obligations post-engagement include NDA compliance, responsible disclosure of
third-party product vulnerabilities, transparent reporting of scope violations, and secure
data destruction.

For the PenTest+ exam, Domain 5 questions test these topics through scenario-based questions.
Expect scenarios asking what to do when cleanup is incomplete, how to handle a discovered
scope violation, what chain of custody means in practice, and how to structure a retest report.

Quiz and lab for Module 15 are on Canvas. Module 16 is our final module — PenTest+ exam
preparation and capstone. See you there.

---

*End of Module 15 Video Script*
