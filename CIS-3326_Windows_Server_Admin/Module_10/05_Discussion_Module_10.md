# Discussion Forum: Module 10 — File and Print Services in Windows Server

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

This week's discussion applies File and Print Services concepts to real-world
design and troubleshooting scenarios. Choose one scenario below, answer all
three sub-questions, and engage substantively with at least two classmates.

---

## Scenario A — Departmental File Share Design

A law firm is deploying a new file server. Three departments must store files
on the server: Partners, Associates, and Paralegals. Security requirements
state that Partners can read and modify all files in all three folders, Associates
can read and modify their own folder but only read the Partners folder, and
Paralegals can only read all three folders. Users must not see folders they
cannot access when browsing the share.

1. Design the NTFS permission structure for the three folders. For each folder,
   specify the group name, NTFS permission level, and propagation scope. Explain
   which NTFS permission level grants create, modify, and delete without allowing
   the user to change permissions or take ownership.

2. Describe the share permission configuration you would apply. Identify the
   best-practice approach and explain why managing a single permission set is
   preferable to managing both share and NTFS permissions separately. Identify
   the PowerShell cmdlet that enables the feature preventing Paralegals from
   seeing the Partners and Associates folders.

3. A Partner reports that after logging on through a Remote Desktop session,
   she can read files in the Associates folder but cannot modify them, even
   though her NTFS permission on that folder is Modify. Explain whether this
   is expected behavior, what permission is limiting her, and what change, if
   any, is needed to resolve it.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

## Scenario B — DFS Namespace Migration

A university is consolidating file storage from four department file servers
onto two new high-capacity servers. Currently, users access data via direct
UNC paths: `\\FacServer\FacData`, `\\StaffServer\StaffData`,
`\\ITServer\ITData`, and `\\LibServer\LibData`. The IT director wants a
single unified access path and the ability to migrate physical data between
servers without notifying users or updating any scripts.

1. Design the DFS Namespace structure. Identify the namespace root path,
   the four DFS folder names and their initial targets, the namespace type,
   and the PowerShell cmdlets to create the root and each folder. Explain
   why a domain-based namespace is preferred over a stand-alone namespace
   for this environment.

2. After the namespace is deployed, the university migrates Faculty data from
   `\\FacServer\FacData` to `\\NewServer1\FacData`. Describe exactly what
   change must be made in DFS to ensure users continue accessing faculty files
   without any change to their shortcuts, mapped drives, or scripts. Identify
   the PowerShell cmdlet to make this change.

3. A staff member reports that `\\txwes.edu\Shared\Staff` no longer resolves
   after the migration. `Get-DfsnFolder -Path "\\txwes.edu\Shared\Staff"`
   returns the folder with State: Offline. Describe the troubleshooting steps
   you would take to diagnose and restore access, including the specific cmdlets
   you would use.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

## Scenario C — Print Server Troubleshooting

A hospital deploys a central print server hosting 12 shared printers across
three nursing floors. Four printers per floor are configured as a single printer
pool per floor. After a weekend maintenance window, nurses on Floor 2 report
that print jobs submit successfully but nothing prints. Floor 1 and Floor 3
printers work normally. A technician checks Print Management and sees 47 jobs
stuck in the Floor 2 queue with status "Sent to printer." All four physical
printers on Floor 2 have power and network connectivity.

1. Identify the three most likely causes for print jobs showing "Sent to
   printer" without output. For each cause, identify the diagnostic step and
   the PowerShell cmdlet or command you would use to check it.

2. Explain the printer pooling requirement that must be verified when four
   physical printers share a single logical printer. Identify what would happen
   if a technician during the maintenance window replaced one of the four Floor 2
   printers with a different model that required a different driver.

3. To clear the stuck queue and restore printing as quickly as possible,
   describe the steps you would take in order. Identify whether restarting the
   Spooler service would clear stuck jobs, and explain the impact on other
   floors if the Spooler is restarted on the shared print server.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

## Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario,
  answer all three sub-questions.

- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates;
  minimum 60 words each.

- In peer replies: evaluate the accuracy of their permission design, DFS
  configuration, or troubleshooting approach, and add one consideration or
  edge case they did not mention.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

## Professor Nash's Note

Scenario A tests the single most common source of help-desk escalations I see
from junior administrators: "I set the permission but it's not working." In
almost every case, the administrator set either NTFS or share permissions but
forgot the interaction between the two — or forgot that RDP sessions are NTFS
only. Scenario C is drawn from a real-world incident at a healthcare client.
The 47 stuck jobs were caused by a driver mismatch on one of the four pooled
printers after a hardware swap during maintenance — a single wrong driver in
a pool silently corrupts the entire pool's output queue. The technician spent
two hours before discovering that removing the mismatched printer from the pool
port list immediately restored printing on the other three devices. Keep that
in mind: pool behavior is only as reliable as the driver consistency of every
device in the pool.
