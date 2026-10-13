# Discussion Forum: Module 11 — Windows Server Security: BitLocker, EFS, and Firewall

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion applies Windows Server security concepts to real-world
enterprise design and troubleshooting scenarios. Choose one scenario below,
answer all three sub-questions, and engage substantively with at least two
classmates.

---

### Scenario A — Windows Defender Firewall Rule Design

A regional hospital has recently expanded its network infrastructure to include
a new Windows Server 2022 file server (FS01) that hosts patient records. The
server is domain-joined and is connected to both the corporate LAN and a
separate clinical research VLAN. The IT security team has the following
requirements:

- Inbound SMB (TCP 445) should be allowed only from the corporate LAN subnet
  (172.16.10.0/24), not from the research VLAN.
- All inbound Telnet (TCP 23) connections must be explicitly blocked on all
  profiles.
- RDP (TCP 3389) must be allowed from a specific IT admin workstation at
  172.16.10.50 only.

1. For each of the three requirements, describe the specific firewall rule
   parameters needed (Direction, Protocol, Port, Remote Address, Action,
   Profile). Do not write the PowerShell commands yet — describe what each
   rule should do at a conceptual level.

2. Write the `New-NetFirewallRule` PowerShell command for each of the three
   rules. Use appropriate display names and scope all rules to the Domain
   profile unless a different profile is required by the scenario.

3. The security team later discovers that inbound RDP traffic is still being
   allowed from addresses other than 172.16.10.50, even though they created
   the scoped rule. After investigation, they find that a second, broader Allow
   rule for RDP exists. Explain how Windows Defender Firewall evaluates
   multiple Allow rules for the same port, and describe the correct way to
   ensure only the scoped rule applies.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

### Scenario B — BitLocker Deployment for a Branch Office

A financial services company is deploying 12 new Windows Server 2022 servers
to branch offices across 4 states. All servers will be domain-joined and housed
in unsecured server closets (not data centers) due to space constraints. The
CISO has mandated full-disk encryption on all servers. The IT team must also
ensure that recovery keys are accessible to the corporate IT staff in case of
a TPM failure.

1. Recommend the BitLocker protector mode for these servers. Justify your
   recommendation by explaining why TPM-only mode is appropriate for servers
   in this deployment context, and explain what "sealed to the TPM" means in
   terms of boot-time key release.

2. Describe how the IT team should configure recovery key storage so that
   corporate IT staff can retrieve keys remotely in case of TPM failure or
   BIOS update. Include the PowerShell commands that enable BitLocker with a
   recovery password and back up that password to Active Directory.

3. One of the branch office servers needs a BIOS update. A junior IT
   administrator asks: "Do I need to decrypt the drive first?" Explain the
   correct procedure, identify the specific PowerShell command used before
   the BIOS update, and explain what happens to protection status during
   and after the maintenance window.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

### Scenario C — EFS and Data Recovery in a Regulated Environment

A law firm uses Windows Server 2022 as a file server. Senior attorneys encrypt
their client case files using EFS to prevent paralegals and other staff from
accessing them. The firm's IT director is concerned about data loss risk if an
attorney leaves suddenly. A junior IT administrator suggests: "We can always
just use the Administrator account to open the files if someone leaves."

1. Explain why the junior administrator's suggestion is incorrect. Describe
   how EFS actually prevents access even by administrators, referencing the
   role of the File Encryption Key (FEK), the Data Decryption Field (DDF),
   and the user's certificate private key.

2. Explain what a Data Recovery Agent is, how it is configured in a domain
   environment, and why it must be configured before files are encrypted
   (not after) to be effective. Describe where the DRA is configured in
   Group Policy.

3. An attorney encrypts a document using EFS on their workstation and then
   moves to a new laptop. They report they cannot open the file from the new
   laptop. Identify the most likely cause, describe what should have been done
   when the attorney's profile was set up on the new laptop, and explain what
   the IT department can do now to restore access.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

### Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario,
  answer all three sub-questions
- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates;
  minimum 60 words each
- In peer replies: evaluate the accuracy of their firewall rule design or
  BitLocker configuration, and add one technical consideration they did not
  mention

---

### Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

### Professor Nash's Note

The "Administrator can bypass EFS" misconception is one I hear from students
every time I teach this module. EFS was specifically designed so that no
administrator can open an encrypted file without the correct private key or a
pre-configured DRA. I have seen organizations lose years of data because
someone encrypted files, left the organization, and there was no DRA in place.
The DRA configuration must be done before encryption happens — that is the
critical sequence.

On BitLocker and BIOS updates: I have seen administrators decrypt entire server
drives before firmware updates because they did not know about
`Suspend-BitLocker`. A full decryption and re-encryption of a terabyte drive
takes hours. `Suspend-BitLocker` takes seconds and achieves the same result for
the maintenance window. Know the difference.

For Scenario A: the hospital firewall scenario is based on a real deployment.
The lesson from that engagement was that every organization has a "why is RDP
still open" story. Building scoped rules with remote address filtering from the
start is the right approach — retrofitting it later is painful.
