# Quiz: Module 15 — Post-Report Cleanup and Debriefing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002) — Domain 5: Reporting and Communication

---

### Question 1

Why is post-engagement cleanup a required phase of every professional penetration test?

- A) To improve the target network's performance by removing scanning traffic and temporary
  connections
- B) To ensure all backdoors, shells, persistence mechanisms, created accounts, and uploaded
  tools are removed — leaving the client's environment in its pre-test state so real attackers
  cannot leverage artifacts left by the tester
- C) To give the penetration tester time to compile screenshots and organize notes before
  writing the report
- D) To reset the engagement scope documentation so the client can request a follow-up test
  at no additional cost

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Cleanup is a professional and ethical obligation. Backdoors, shells,
  and persistence mechanisms installed during testing are fully functional attack tools. If
  left in place, real attackers could discover and use them — potentially causing more harm
  than the original vulnerabilities the tester was hired to find. Testers provide a signed
  cleanup attestation confirming all artifacts have been removed.
- *Why A is incorrect:* While testing activities do generate network traffic, performance
  improvement is not the reason for cleanup. Cleanup focuses on removing persistent access
  artifacts — not optimizing bandwidth or clearing connection state.
- *Why C is incorrect:* Note organization and screenshot compilation are documentation tasks
  that occur throughout the engagement — not post-engagement cleanup activities. Cleanup is
  specifically about removing attack tools and access mechanisms from client systems.
- *Why D is incorrect:* Cleanup has no relationship to scope documentation or follow-up
  engagement pricing. It is a security-focused activity that restores the target environment
  to its original state, independent of any commercial considerations.

---

### Question 2

A penetration tester finishes an engagement and realizes three days after delivering the
report that they left a Meterpreter persistence service installed on a domain controller.
What is the correct professional response?

- A) Wait until the client schedules a retest, then remove the artifact during that visit
- B) Immediately notify the client, schedule a removal session, remove the artifact, and
  provide an updated cleanup attestation documenting the oversight and remediation
- C) Remotely uninstall the service without telling the client to avoid damaging the business
  relationship
- D) Include the oversight in the after-action review notes and address it in the next
  engagement's methodology update

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Transparency is non-negotiable when a cleanup failure is discovered.
  The client has a live persistence mechanism on their most sensitive server — a domain
  controller — that they are unaware of. They cannot make informed security decisions without
  knowing this. The tester must notify the client immediately, remove the artifact under
  authorized access, and update the cleanup documentation. Delaying or concealing the issue
  compounds the risk and the professional liability.
- *Why A is incorrect:* Waiting for a retest — potentially weeks or months away — leaves a
  fully functional backdoor on a domain controller during that entire window. This is
  unacceptable from both an ethical and a liability standpoint.
- *Why C is incorrect:* Accessing the client system to remove the artifact without
  notification — even to fix a mistake — is unauthorized access under the letter of the
  original engagement authorization, which has expired. Any post-engagement system access
  requires explicit client authorization. Concealing the oversight also violates professional
  standards.
- *Why D is incorrect:* Documenting the lesson without correcting the immediate problem
  leaves the backdoor in place. The after-action review is the correct venue for
  methodology improvement — not a substitute for addressing an active security risk.

---

### Question 3

Which of the following best describes the purpose of chain of custody in penetration testing?

- A) It is a legal requirement that pentesters obtain written permission from law enforcement
  before testing systems that may contain evidence of criminal activity
- B) It is documentation tracking who collected, handled, stored, and transferred evidence —
  from initial capture to final disposition — establishing that evidence is authentic and
  has not been tampered with
- C) It refers to the sequence in which findings are reported, from most critical to least
  critical, ensuring executives review the highest-risk items first
- D) It is the process of transferring engagement deliverables from the tester to the client's
  legal counsel for contractual compliance review

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Chain of custody is borrowed from forensic investigation practice and
  applied to penetration testing to establish evidence integrity. In a dispute — about scope,
  about whether a finding was real, or in the rare event a test becomes part of a legal
  proceeding — properly documented chain of custody makes evidence defensible. It answers:
  who captured this screenshot, when, on what system, and has it been modified since capture?
- *Why A is incorrect:* Chain of custody is not a law enforcement permission process. Law
  enforcement involvement in a penetration test is extraordinary and unrelated to the
  evidence-tracking meaning of the term.
- *Why C is incorrect:* Reporting findings from most critical to least critical is a report
  formatting and prioritization practice — it has no relationship to the term "chain of
  custody." Chain of custody specifically refers to evidence handling and documentation.
- *Why D is incorrect:* Delivering deliverables to legal counsel may be part of an engagement
  but is a contract administration activity — not what chain of custody means.

---

### Question 4

During a retest, a penetration tester attempts to exploit the same SQL injection vulnerability
documented in the original report. The original attack path using sqlmap is now blocked by
a Web Application Firewall rule. However, manual testing reveals that a different parameter
in the same application is still injectable using a different payload. What is the correct
remediation status to assign this finding?

- A) Remediated — the original exploitation path was blocked successfully
- B) Not Remediated — the vulnerability was not fixed because SQL injection is still present
  somewhere in the application
- C) Partially Remediated — the original finding's specific attack path was blocked, but the
  root cause (lack of parameterized queries) remains unresolved, as evidenced by a new
  injection point
- D) Out of Scope — the new injection parameter was not identified in the original finding
  and cannot be assessed under the retest authorization

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Partial remediation occurs when the immediate fix addresses the
  symptom but not the root cause. Adding a WAF rule blocks the specific payload documented
  in the original report but does not fix the underlying CWE-89 (Improper Neutralization of
  Special Elements in SQL Commands). The application still concatenates user input into SQL
  queries — it is just that one specific path is now filtered. The root cause remedy is
  parameterized queries applied throughout the codebase.
- *Why A is incorrect:* Calling this Remediated when another injectable parameter exists
  misrepresents the security state of the application. The client would believe the problem
  is fixed when it is not. This would be a professionally deficient and potentially harmful
  classification.
- *Why B is incorrect:* "Not Remediated" implies the original finding was completely
  unaddressed. The client did take action — they deployed a WAF rule — and that action
  did block the original exploitation path. Partial credit is appropriate. "Not Remediated"
  should be reserved for cases where the original attack path still succeeds unchanged.
- *Why D is incorrect:* The retest is scoped to the original vulnerability class (SQL
  injection in the login form area) and the new finding is directly related to the same
  root cause. While the specific parameter is newly identified, it confirms that the
  remediation was incomplete — which is precisely what the retest is designed to reveal.
  Calling it out-of-scope would allow the client to falsely believe the issue is resolved.

---

### Question 5

A client's CISO reviews the final report and informs the tester that Finding FIND-007
(a High-severity insecure direct object reference in the billing API) will not be remediated
because the development cost exceeds the available budget. What must the tester do?

- A) Remove FIND-007 from the final report to prevent it from appearing in an audit since
  the client cannot fix it
- B) Escalate FIND-007 to Critical severity to force the client to reconsider the decision
- C) Document FIND-007 as "Risk Accepted by Client" in the report, recording the name of
  the authorizing stakeholder and the date of acceptance
- D) Deliver two versions of the report — one with FIND-007 for internal use and one without
  it for executive and audit distribution

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Risk acceptance is a legitimate and documented business decision.
  Organizations regularly carry residual risk when remediation costs exceed the risk's
  expected impact. The tester's role is to accurately document both the finding and the
  client's decision. A "Risk Accepted" status with the authorizing stakeholder's name and
  date creates an audit trail that protects both parties. The finding is not deleted —
  it remains in the report with its original severity rating.
- *Why A is incorrect:* Removing confirmed findings falsifies the report. A pentest report
  must accurately reflect all findings regardless of remediation decisions. Removing
  FIND-007 would be unethical, potentially fraudulent, and would destroy the document's
  value as an accurate security assessment.
- *Why B is incorrect:* CVSS severity ratings are determined by the technical characteristics
  of the vulnerability, not by the client's remediation budget. Artificially inflating a
  severity rating to coerce a business decision corrupts the assessment's integrity and
  exposes the tester to credibility damage.
- *Why D is incorrect:* Producing two versions of a report — one with and one without a
  finding — is deeply unprofessional and potentially fraudulent if the "clean" version is
  presented to auditors. There is one authoritative report. All stakeholders receive the same
  complete document.

---

### Question 6

What is the primary purpose of a penetration test after-action review (AAR)?

- A) To present lessons learned from the engagement to the client's security team so they can
  improve their defensive monitoring
- B) To conduct an internal team review of what was planned versus what happened, identify
  what went well and what needs improvement, and capture institutional knowledge for future
  engagements
- C) To document all vulnerabilities that were identified but not exploited during the
  engagement so they can be included in a supplemental report
- D) To review the client's remediation progress and determine whether a retest is warranted

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The AAR is an internal team activity — not shared with the client.
  Its purpose is professional development and methodology improvement. The four AAR
  questions (what was supposed to happen, what actually happened, what went well, what needs
  improvement) create a structured framework for capturing lessons that improve future
  engagements. Over time, documented AARs reveal recurring patterns that drive methodology
  and tooling updates.
- *Why A is incorrect:* Presenting lessons learned to the client's team is a component of
  the client debrief — a different activity. The AAR is strictly internal. Sharing internal
  team retrospectives with clients would be inappropriate and could expose the firm's
  methodology limitations.
- *Why C is incorrect:* Unexploited vulnerabilities may appear in a findings section marked
  as "identified but not confirmed" — but that is a report content decision, not an AAR
  purpose. The AAR reviews the engagement process and team performance, not finding inventory.
- *Why D is incorrect:* Retest scheduling is a client communication activity that happens
  during the post-engagement follow-up period. The AAR is a separate internal process focused
  on team and methodology improvement, not on the client's remediation timeline.

---

### Question 7

A penetration tester discovers a critical zero-day vulnerability in a widely-used commercial
VPN appliance while testing a client's network. The vulnerability exists in the vendor's
product, not in anything the client built. What is the correct professional response?

- A) Include the finding in the client's report with full exploitation details and publish
  the technical details on a security research blog immediately
- B) Keep the finding private and never disclose it — publishing vendor vulnerabilities
  without authorization violates responsible disclosure norms
- C) Coordinate with the client, then notify the vendor through their responsible disclosure
  or bug bounty program, following the vendor's disclosure timeline before any public release
- D) Report the vulnerability only to the client and leave vendor notification to the client's
  discretion — the tester's obligation ends at the client relationship

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Responsible disclosure is the industry-standard process for handling
  third-party product vulnerabilities. The correct sequence is: notify the client (since the
  disclosure may reference their environment), then file with the vendor's responsible
  disclosure or bug bounty program. Follow the vendor's timeline — typically 90 days before
  public disclosure. This process balances the public's right to know about vulnerabilities
  with the vendor's need for time to produce a patch, protecting the broader user community.
- *Why A is incorrect:* Immediate public disclosure of a zero-day without notifying the
  vendor first is "full disclosure" or irresponsible disclosure. It exposes every organization
  running the affected VPN appliance to exploitation before a patch exists. This approach is
  harmful to the broader security ecosystem and may violate legal agreements.
- *Why B is incorrect:* Permanent non-disclosure of a critical vulnerability in a widely
  deployed product leaves all users at risk indefinitely. Responsible disclosure is not
  about silencing findings — it is about timing disclosure to minimize harm. Permanent
  silence is not an ethical option for critical vulnerabilities.
- *Why D is incorrect:* The tester has a professional obligation to initiate responsible
  disclosure for significant third-party product vulnerabilities, regardless of what the
  client chooses to do. Leaving vendor notification entirely to the client is an abdication
  of professional responsibility, particularly for a critical vulnerability that affects
  users beyond the client's organization.

---

### Question 8

Which of the following activities is NOT a component of post-engagement cleanup?

- A) Removing scheduled tasks and cron jobs created during testing
- B) Deleting local user accounts created to facilitate privilege escalation testing
- C) Updating the client's patch management policy to address identified vulnerabilities
- D) Removing web shells uploaded to the target web server during the engagement

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct (i.e., why this is NOT a cleanup activity):* Updating the client's patch
  management policy is a remediation activity — something the client performs in response to
  findings. Post-engagement cleanup is the tester's responsibility: removing tools, accounts,
  and access mechanisms that the tester installed. Policy changes are the client's
  responsibility and are driven by the remediation guidance in the report, not by the tester
  directly modifying client processes.
- *Why A is incorrect (is a cleanup activity):* Scheduled tasks and cron jobs are persistence
  mechanisms. Any scheduled task or cron job created during testing must be removed during
  cleanup. They are active execution paths that could be exploited by real attackers.
- *Why B is incorrect (is a cleanup activity):* User accounts created during testing represent
  valid credentials in the client's authentication systems. If left in place, these accounts
  could be used by attackers who discover them. Account deletion is a required cleanup step.
- *Why D is incorrect (is a cleanup activity):* Web shells are among the highest-risk testing
  artifacts because they are accessible via HTTP from anywhere — including from the internet
  if the server is externally reachable. Removing web shells is one of the most critical
  cleanup steps.

---

### Question 9

A penetration tester's engagement log shows the following artifact was created during testing:
`HKCU\Software\Microsoft\Windows\CurrentVersion\Run` value `svcupdate` pointing to
`C:\Users\testuser\AppData\Local\Temp\update.exe`. What type of artifact is this and where
must the tester look to verify it has been removed?

- A) A scheduled task; verified by running `schtasks /query /fo LIST` on the target
- B) A registry persistence mechanism; verified by checking the Run key in the Windows
  Registry after deletion
- C) A service installation; verified by running `sc query svcupdate` on the target
- D) A WMI subscription; verified by running `Get-WMIObject -Namespace root\subscription
  -Class __FilterToConsumerBinding` in PowerShell

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` registry key
  is the classic Windows user-level auto-run persistence location. Any value added here
  executes the specified binary when the user logs in. This is one of the most common
  persistence mechanisms in Windows environments. Verification requires checking the key
  in the Registry Editor or with `reg query
  "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"` after deletion to confirm the value
  no longer exists.
- *Why A is incorrect:* `schtasks /query` lists scheduled tasks — entries in the Windows
  Task Scheduler. A registry Run key is a distinct persistence mechanism from a scheduled
  task. Both exist, but they are checked differently. The `schtasks` command would not show
  a Run key entry.
- *Why C is incorrect:* `sc query` queries Windows services. A registry Run key is not a
  service — it does not appear in the Services control panel or service registry. Services
  are installed under `HKLM\SYSTEM\CurrentControlSet\Services`, not under the user's Run key.
- *Why D is incorrect:* The PowerShell WMI query checks for WMI event subscription
  persistence — a more sophisticated technique using WMI filters and consumers. A registry
  Run key is a simpler and entirely different persistence mechanism.

---

### Question 10

A penetration tester must securely destroy engagement evidence files at the end of the
contractual retention period. Which action meets the standard for secure data destruction?

- A) Move the evidence folder to the Recycle Bin and empty it
- B) Delete the files using `rm` on Linux or `del` on Windows
- C) Use a tool that overwrites the storage blocks with random data before deletion,
  or encrypt the container and discard the key, ensuring data cannot be recovered
- D) Archive the files to a cloud backup service before deletion — the cloud copy satisfies
  retention requirements and local deletion completes destruction

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Standard file deletion (Recycle Bin, `rm`, `del`) removes the
  filesystem pointer to a file but does not overwrite the data blocks on disk. Data recovery
  tools can reconstruct deleted files from unoverwritten storage. Secure destruction requires
  either: (1) overwriting storage blocks with random or zero data using tools like `shred`
  on Linux, `sdelete` on Windows, or VeraCrypt wipe operations; or (2) encrypting the
  container and cryptographically erasing (discarding) the encryption key — making the data
  permanently unreadable even if the storage blocks are recovered.
- *Why A is incorrect:* Moving files to the Recycle Bin and emptying it is standard deletion
  — identical in security terms to pressing Delete. The data blocks remain on disk and are
  recoverable with basic forensic tools. This does not meet any standard for secure
  destruction.
- *Why B is incorrect:* `rm` and `del` are standard deletion commands that unlink the
  filesystem entry without overwriting data. On SSDs, the situation is even less certain due
  to wear-leveling. Standard deletion is not secure destruction.
- *Why D is incorrect:* Uploading to a cloud backup service before local deletion does the
  opposite of destruction — it creates an additional copy of sensitive client data in a
  third-party system. This would likely violate the engagement contract's data handling
  provisions and potentially applicable privacy regulations.

---

*End of Module 15 Quiz*
