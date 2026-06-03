# Quiz: Module 11 — Windows Server Security: BitLocker, EFS, and Firewall

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
Review your Reading Guide and video notes before beginning.

---

## Question 1

A Windows Server administrator needs to allow inbound TCP traffic on port 8443
for a custom HTTPS application, but only when the server is connected to the
corporate domain network. Which PowerShell command creates this rule correctly?

A) `New-NetFirewallRule -DisplayName "HTTPS App" -Direction Outbound -Protocol TCP -LocalPort 8443 -Action Allow -Profile Domain`

B) `New-NetFirewallRule -DisplayName "HTTPS App" -Direction Inbound -Protocol TCP -LocalPort 8443 -Action Allow -Profile Domain`

C) `New-NetFirewallRule -DisplayName "HTTPS App" -Direction Inbound -Protocol UDP -LocalPort 8443 -Action Allow -Profile Any`

D) `Add-NetFirewallRule -DisplayName "HTTPS App" -Port 8443 -Action Allow -Profile Domain`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `-Direction Outbound` would control traffic leaving the
    server, not arriving. A web application listening on port 8443 needs an
    Inbound rule.
  - Why C is incorrect: `-Protocol UDP` is incorrect for an HTTPS application,
    which uses TCP. Using `-Profile Any` would also allow the rule on Public and
    Private profiles, not just Domain.
  - Why D is incorrect: `Add-NetFirewallRule` is not a valid PowerShell cmdlet.
    The correct cmdlet is `New-NetFirewallRule`.

---

## Question 2

A Windows Server has three network adapters: one connected to the corporate
LAN (which can reach a domain controller), one connected to a Wi-Fi hotspot,
and one connected to a hotel network. Which firewall profiles are active on
each adapter?

A) Domain profile on all three, because the server is domain-joined.

B) Domain profile on the corporate LAN adapter; Public profile on the Wi-Fi
hotspot and hotel network adapters.

C) Domain profile on the corporate LAN adapter; Private profile on the Wi-Fi
hotspot; Public profile on the hotel network.

D) The administrator must manually assign profiles to each adapter through the
Network and Sharing Center.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Domain profile activates only on the adapter that
    can reach a domain controller. Other adapters use Public or Private based
    on network type, not domain membership.
  - Why C is incorrect: Without the user designating the Wi-Fi hotspot as a
    Private network, Windows defaults to Public for any unknown or unverified
    network. Private profile requires explicit trust designation.
  - Why D is incorrect: Windows automatically selects profiles based on network
    detection. Administrators do not manually assign profiles per adapter.

---

## Question 3

A company's IT security policy requires all server hard drives to be protected
so that if a drive is physically removed and connected to another computer, the
data cannot be read. Which Windows Server feature satisfies this requirement?

A) EFS (Encrypting File System), because it encrypts files individually so they
cannot be opened by other users.

B) NTFS permissions, because the access control list prevents unauthorized users
from reading the drive's content.

C) BitLocker Drive Encryption, because it encrypts the entire volume and the
decryption key is bound to the server's TPM.

D) Windows Defender Firewall, because blocking inbound connections prevents
attackers from accessing drive contents over the network.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: EFS protection depends on the certificate store. If the
    drive is attached to another OS, EFS is not designed to protect against
    physical drive removal the way BitLocker is.
  - Why B is incorrect: NTFS permissions are enforced by the Windows kernel. If
    the drive is attached to another OS or accessed through a bootable
    environment, NTFS permissions are bypassed entirely.
  - Why D is incorrect: Windows Defender Firewall protects against network-
    based attacks. It has no effect on physical drive theft.

---

## Question 4

An administrator is preparing to apply a BIOS firmware update to a BitLocker-
protected server. If they do not take any action before the update, what will
happen after the server restarts?

A) BitLocker will disable automatically to allow the BIOS update to complete.

B) The server will boot normally because BitLocker TPM-only mode does not check
BIOS integrity.

C) The TPM will detect the BIOS change and refuse to release the BitLocker key,
requiring the 48-digit recovery key to unlock the drive.

D) BitLocker will re-encrypt the drive with a new key after detecting the
firmware change.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: BitLocker does not automatically disable for firmware
    updates. The administrator must run `Suspend-BitLocker` before the update.
  - Why B is incorrect: The TPM measures the BIOS and boot environment as part
    of the Platform Configuration Registers. A BIOS change alters PCR values,
    causing the TPM to refuse to release the sealed key.
  - Why D is incorrect: BitLocker does not automatically re-encrypt with a new
    key. The original key cannot be retrieved, so the drive becomes inaccessible
    without the recovery key.

---

## Question 5

A user encrypts a file using EFS and then leaves the organization. The IT
department needs to access the contents of that file. The user's account has
been deleted and their certificate store is no longer available. Under which
condition can the IT department still access the file?

A) The IT department can always access EFS-encrypted files by using the local
Administrator account, which bypasses EFS encryption.

B) The file can be accessed if a Data Recovery Agent (DRA) certificate was
configured in Group Policy before the file was encrypted.

C) EFS-encrypted files can be decrypted by resetting the user's password in
Active Directory and logging in as that user.

D) The file can be recovered using Windows Server Backup if a backup was taken
after the file was encrypted.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: EFS encryption is not bypassed by the local
    Administrator or any administrator account. Even a Domain Admin cannot
    open an EFS-encrypted file without the correct certificate private key
    or a DRA.
  - Why C is incorrect: Resetting the password does not recover the EFS
    certificate private key. The private key is tied to the original user
    profile and certificate.
  - Why D is incorrect: Windows Server Backup backs up encrypted files in their
    encrypted state. Restoring the backup does not decrypt the files — the same
    certificate is still required after restoration.

---

## Question 6

A domain administrator runs `cipher /u /n` on a server. What does this command
display?

A) All EFS certificates stored in the current user's certificate store, along
with their thumbprints and expiration dates.

B) All EFS-encrypted files accessible to the current user, listed without
updating the encryption keys.

C) All users on the domain who have currently open EFS-encrypted files.

D) All volumes on the server that are not encrypted with BitLocker.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The cipher command with `/u /n` operates on files, not
    certificates. For certificate information, use `Get-Item Cert:\CurrentUser\My`.
  - Why C is incorrect: `cipher /u /n` reports files accessible to the user
    running the command, not a domain-wide scan of other users' activity.
  - Why D is incorrect: The cipher command is specific to EFS file encryption.
    BitLocker status is reported by `Get-BitLockerVolume`.

---

## Question 7

An administrator needs to temporarily disable BitLocker protection on a server
drive before applying a firmware update, without fully decrypting the volume.
Which command is correct?

A) `Disable-BitLocker -MountPoint "C:"`

B) `Stop-BitLocker -MountPoint "C:" -Suspend`

C) `Suspend-BitLocker -MountPoint "C:"`

D) `Set-BitLockerVolume -MountPoint "C:" -ProtectionStatus Suspended`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `Disable-BitLocker` fully decrypts the volume, which
    takes significant time and removes all protection permanently until
    re-enabled. For a temporary maintenance window, `Suspend-BitLocker` is
    the correct command.
  - Why B is incorrect: `Stop-BitLocker` is not a valid BitLocker PowerShell
    cmdlet. The correct cmdlet for temporary suspension is `Suspend-BitLocker`.
  - Why D is incorrect: `Set-BitLockerVolume` is not a valid BitLocker cmdlet.
    BitLocker volume settings are managed through `Enable-BitLocker`,
    `Disable-BitLocker`, `Suspend-BitLocker`, and `Resume-BitLocker`.

---

## Question 8

An administrator creates an Allow rule for TCP port 443, but a Block rule for
the same port and protocol already exists. What happens when traffic arrives
on port 443?

A) The Allow rule takes precedence because it was created more recently.

B) The Block rule takes precedence because Block rules always override Allow
rules in Windows Defender Firewall.

C) Windows prompts the administrator to choose which rule applies.

D) Both rules are applied simultaneously, resulting in traffic being allowed
and logged.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Rule precedence in WFAS is based on action type, not
    creation order. Block rules override Allow rules regardless of when they
    were created.
  - Why C is incorrect: Windows Defender Firewall does not prompt the
    administrator at traffic arrival time. Rules are evaluated automatically.
  - Why D is incorrect: When conflicting rules exist, WFAS applies the more
    restrictive rule (Block) rather than applying both simultaneously.

---

## Question 9

A user reports that they cannot open a file they own that was previously
encrypted with EFS. They recently had their computer replaced and their user
profile was recreated. What is the most likely cause?

A) EFS encryption was automatically removed when the computer was replaced
because EFS is a machine-specific feature.

B) The user's EFS private key certificate was not migrated to the new computer,
so Windows cannot decrypt the file encryption key.

C) EFS files cannot be accessed after a computer replacement because the file
system metadata is invalidated.

D) The file is now read-only because EFS encryption prevents modification after
the encrypting computer is decommissioned.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: EFS encryption is tied to the user's certificate, not
    the machine. The file remains encrypted; the issue is the missing private
    key certificate on the new computer.
  - Why C is incorrect: EFS metadata travels with the file. The issue is the
    absence of the private key needed to decrypt the FEK stored in the DDF,
    not invalid metadata.
  - Why D is incorrect: EFS-encrypted files do not become read-only when the
    encrypting computer is decommissioned. The file is inaccessible (not
    read-only) without the correct private key.

---

## Question 10

A security administrator wants to verify that Windows Defender Firewall is
blocking all inbound traffic by default on the Domain profile. Which PowerShell
command confirms this?

A) `Test-NetConnection -ComputerName localhost -Port 0`

B) `Get-NetFirewallProfile -Profile Domain | Select-Object Name, DefaultInboundAction`

C) `Get-NetFirewallRule -Profile Domain | Where-Object {$_.Action -eq "Block"}`

D) `Get-NetFirewallSetting | Select-Object DefaultInboundAction`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Test-NetConnection` tests whether a TCP connection can
    be established — it does not report firewall profile configuration settings.
  - Why C is incorrect: This lists explicit Block rules, not the profile's
    default action for unmatched traffic. `Get-NetFirewallProfile` is the
    correct cmdlet for per-profile default behavior.
  - Why D is incorrect: `Get-NetFirewallSetting` retrieves global firewall
    settings, not per-profile default actions.
