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

---

### Question 11 (5 points)

A server administrator needs to create a firewall rule that allows inbound ICMP
echo requests (ping) only from computers on the `10.0.0.0/8` subnet, using the
Domain profile. Which PowerShell command is correct?

- A) `New-NetFirewallRule -DisplayName "Allow ICMP" -Direction Inbound -Protocol ICMPv4 -Action Allow -Profile Domain -RemoteAddress "10.0.0.0/8"`
- B) `New-NetFirewallRule -DisplayName "Allow ICMP" -Direction Inbound -Protocol ICMP -Action Allow -Profile Domain -LocalAddress "10.0.0.0/8"`
- C) `New-NetFirewallRule -DisplayName "Allow ICMP" -Direction Outbound -Protocol ICMPv4 -Action Allow -Profile Domain -RemoteAddress "10.0.0.0/8"`
- D) `Set-NetFirewallRule -DisplayName "File and Printer Sharing (Echo Request - ICMPv4-In)" -Enabled True`

- **Correct Answer: A**
- **Distractor Analysis:**
  - **A** — Correct. `-Protocol ICMPv4` specifies the correct protocol. `-Direction Inbound` allows incoming ping requests. `-RemoteAddress "10.0.0.0/8"` restricts the rule to source addresses in the `10.x.x.x` range. `-Profile Domain` limits activation to the domain network.
  - **B** — `-Protocol ICMP` is not a valid value for `New-NetFirewallRule`; the correct value is `ICMPv4`. Also, `-LocalAddress` specifies the destination (local server) address, not the source (remote) address.
  - **C** — `-Direction Outbound` would control pings leaving the server, not pings arriving from the subnet. An inbound direction is needed to allow remote hosts to ping the server.
  - **D** — This enables the built-in echo request rule, which allows pings from any source. It does not restrict to a specific subnet or profile.

---

### Question 12 (5 points)

An administrator wants to export an EFS certificate and private key from one
server so it can be imported to a second server, allowing a user to decrypt their
EFS-encrypted files from either machine. Which file format should be used for the
export?

- A) `.cer` (DER-encoded binary X.509) — contains only the public certificate
- B) `.pfx` (PKCS #12) — contains both the certificate and the private key
- C) `.p7b` (PKCS #7) — contains the certificate chain without the private key
- D) `.crl` (Certificate Revocation List) — contains revoked certificate serials

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — A `.cer` file contains only the public certificate. Without the private key, the second server cannot decrypt the FEK stored in the DDF, so EFS decryption would fail.
  - **B** — Correct. A `.pfx` file (PKCS #12 format) bundles the certificate and its private key together in a password-protected container. Importing the `.pfx` on the second server gives the user the private key needed to decrypt EFS-encrypted files.
  - **C** — A `.p7b` file contains a certificate chain (public certificates only). It does not include the private key and cannot be used for EFS decryption on another machine.
  - **D** — A `.crl` file lists revoked certificates. It has no role in certificate export or EFS key migration.

---

### Question 13 (5 points)

A domain administrator configures a Data Recovery Agent by running
`cipher /r:DRAKey` and then importing the resulting certificate into Group Policy.
What does `cipher /r:DRAKey` generate?

- A) A self-signed EFS certificate for the DRA account stored in Active Directory
- B) A `.cer` and `.pfx` file pair containing a recovery certificate and private key for use as a DRA
- C) A Group Policy template that automatically assigns DRA status to the Administrator account
- D) A symmetric encryption key used to re-encrypt all existing EFS files on the domain

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `cipher /r` does not store anything in Active Directory directly. It generates two files on the local file system.
  - **B** — Correct. `cipher /r:DRAKey` generates `DRAKey.cer` (public certificate, imported into GPO as the DRA certificate) and `DRAKey.pfx` (private key, stored securely offline). The `.cer` is added to the EFS recovery agents policy so new EFS files include a DRF encrypted with the DRA's public key.
  - **C** — Group Policy templates (`.admx`) define registry-based settings. `cipher /r` produces certificate files, not GPO templates.
  - **D** — The DRA does not re-encrypt existing files. Files encrypted before the DRA was configured do not have a DRF for the new DRA. Only files encrypted after the policy applies contain a DRF.

---

### Question 14 (5 points)

A server is running Windows Server 2022 with BitLocker enabled on the C: drive
using TPM+PIN mode. A help desk technician needs to reboot the server remotely
for a patch but does not know the PIN. Which action allows the reboot to complete
without requiring the PIN at startup?

- A) Run `Disable-BitLocker -MountPoint "C:"` before rebooting
- B) Run `Suspend-BitLocker -MountPoint "C:"` before rebooting
- C) Run `Resume-BitLocker -MountPoint "C:"` before rebooting
- D) Delete the TPM key from the server's BIOS before rebooting

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Disable-BitLocker` fully decrypts the volume. This is a lengthy process and permanently removes BitLocker protection until re-enabled.
  - **B** — Correct. `Suspend-BitLocker` temporarily bypasses the TPM+PIN check for the next reboot, placing the volume key in a cleartext state. After one restart, BitLocker protection automatically resumes and the PIN is required again on subsequent boots.
  - **C** — `Resume-BitLocker` re-enables protection on a suspended volume. Running it before a reboot would have no effect if the volume is not currently suspended.
  - **D** — Deleting the TPM key from BIOS would permanently destroy the sealed encryption key, making the drive inaccessible and requiring the 48-digit recovery key. This is destructive and not appropriate for a routine reboot.

---

### Question 15 (5 points)

An administrator wants to view all currently enabled inbound firewall rules on a
server, showing only the rule display name, protocol, local port, and action.
Which PowerShell pipeline accomplishes this?

- A) `Get-NetFirewallRule -Direction Inbound -Enabled True | Get-NetFirewallPortFilter | Select-Object DisplayName, Protocol, LocalPort, Action`
- B) `Get-NetFirewallRule -Direction Inbound -Enabled True | Select-Object DisplayName, Protocol, LocalPort, Action`
- C) `Get-NetFirewallRule -Direction Inbound -Enabled True | Format-Table DisplayName, Action`
- D) `Get-NetFirewallRule -Direction Inbound -Enabled True | Select-Object DisplayName, Action | Get-NetFirewallPortFilter`

- **Correct Answer: A**
- **Distractor Analysis:**
  - **A** — Correct. `Get-NetFirewallRule` returns rule objects that do not directly expose port and protocol properties. Piping to `Get-NetFirewallPortFilter` retrieves the associated port filter objects, which contain `Protocol` and `LocalPort`. `Select-Object` then extracts the desired properties.
  - **B** — `Get-NetFirewallRule` objects do not contain `Protocol` or `LocalPort` as direct properties. These properties live in the associated port filter object, requiring the `Get-NetFirewallPortFilter` step.
  - **C** — This returns only `DisplayName` and `Action`. It does not include protocol or port information, making it insufficient for the stated requirement.
  - **D** — The pipeline order is reversed. `Select-Object` reduces the object before the port filter is retrieved, and `Get-NetFirewallPortFilter` cannot meaningfully process `Select-Object` output.

---

### Question 16 (5 points)

BitLocker is enabled on a data volume (`D:`) with no TPM (using a password
protector only). An administrator runs `Get-BitLockerVolume -MountPoint "D:"` and
sees `VolumeStatus: FullyEncrypted` and `ProtectionStatus: Off`. What does this
state indicate?

- A) The volume is not encrypted; `FullyEncrypted` is a reporting error
- B) BitLocker protection is suspended — the volume is encrypted but the key is stored in cleartext, allowing it to boot without the password
- C) The password protector was removed and the volume cannot be decrypted
- D) The volume is encrypted but the password protector has expired

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `VolumeStatus: FullyEncrypted` accurately reflects that encryption is applied to all sectors. The `ProtectionStatus: Off` is a distinct field indicating the protection state, not an error.
  - **B** — Correct. `ProtectionStatus: Off` combined with `VolumeStatus: FullyEncrypted` means BitLocker is suspended. The volume data is encrypted, but the key is exposed in a cleartext VMK on disk, bypassing the password requirement. This typically occurs after `Suspend-BitLocker` is run or the protector is removed.
  - **C** — If the protector is removed, `ProtectionStatus` would show `Off` and `KeyProtector` would be empty, but the volume remains encrypted (the key is stored unprotected). It can still be decrypted using the recovery key if one exists.
  - **D** — BitLocker password protectors do not expire. They remain valid until explicitly changed or removed.

---

### Question 17 (5 points)

A security policy requires that all outbound connections from a server to remote
computers be authenticated using Kerberos before communication is allowed. Which
type of firewall rule in Windows Defender Firewall with Advanced Security
enforces this requirement?

- A) Outbound rule with Action set to Allow and authentication not configured
- B) Inbound rule with Action set to Allow if secure
- C) Connection Security Rule with Rule Type set to Isolation
- D) Connection Security Rule with Rule Type set to Authentication Exemption

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — A standard Allow rule permits traffic without requiring authentication. It does not enforce Kerberos or any other authentication before communication.
  - **B** — An inbound rule with "Allow if secure" permits traffic only if it arrives with IPsec authentication, but this controls inbound traffic to the server, not outbound connections to remote computers.
  - **C** — Correct. A Connection Security Rule with type Isolation requires IPsec authentication (Kerberos, NTLM, or certificate) for connections to and from the server based on the configured conditions. Isolation rules enforce that communication only occurs with authenticated peers.
  - **D** — An Authentication Exemption rule explicitly exempts specified computers from IPsec authentication requirements. This is the opposite of what is needed.

---

### Question 18 (5 points)

A server administrator runs `Get-BitLockerVolume` and observes that the `C:`
drive has two key protectors: `Tpm` and `RecoveryPassword`. An analyst asks what
the RecoveryPassword protector is and when it would be used. What is the correct
explanation?

- A) RecoveryPassword is a 48-digit numeric key used to unlock the drive when the TPM cannot release the encryption key — for example, after a BIOS change or too many failed PIN attempts
- B) RecoveryPassword is the administrator's domain password, stored by BitLocker as a backup in case the TPM is removed
- C) RecoveryPassword is a symmetric key derived from the TPM that is only usable on the original hardware
- D) RecoveryPassword is a certificate thumbprint used to authenticate the drive to Active Directory

- **Correct Answer: A**
- **Distractor Analysis:**
  - **A** — Correct. The RecoveryPassword protector stores a 48-digit numeric recovery key. It activates when the TPM cannot release the VMK — caused by platform measurement changes (BIOS update, boot configuration changes) or when the TPM is cleared. The recovery key bypasses the TPM check and unlocks the volume.
  - **B** — RecoveryPassword is not derived from any user password. It is a randomly generated 48-digit key independent of any domain or user credentials.
  - **C** — The recovery password is specifically designed to work independently of hardware. Its purpose is to allow access when the original TPM is unavailable or its measurements have changed.
  - **D** — RecoveryPassword is a numeric key, not a certificate thumbprint. Certificate-based BitLocker protectors use a separate `Certificate` protector type.

---

### Question 19 (5 points)

You want to configure Windows Defender Firewall via Group Policy to block all
inbound traffic on the Public profile by default while allowing all inbound
traffic on the Domain profile. You also want to log dropped packets on the Public
profile to `C:\Logs\pfirewall.log`. Which GPO path contains these settings?

- A) Computer Configuration > Policies > Windows Settings > Security Settings > Windows Defender Firewall with Advanced Security
- B) Computer Configuration > Policies > Administrative Templates > Network > Windows Firewall
- C) User Configuration > Policies > Windows Settings > Security Settings > Windows Defender Firewall
- D) Computer Configuration > Preferences > Control Panel Settings > Windows Firewall

- **Correct Answer: A**
- **Distractor Analysis:**
  - **A** — Correct. Windows Defender Firewall with Advanced Security is configured under Computer Configuration > Policies > Windows Settings > Security Settings. This node contains per-profile settings including default inbound/outbound actions and logging configuration.
  - **B** — The Administrative Templates > Network > Windows Firewall path contains legacy Windows Firewall settings for older OS versions. WFAS configuration is in the Security Settings node.
  - **C** — Firewall policy is a Computer Configuration setting, not a User Configuration setting. User-level firewall rules are not supported in this way.
  - **D** — Group Policy Preferences > Control Panel Settings manages some firewall settings on older Windows versions. WFAS policy enforcement is done through Security Settings, not Preferences, which are advisory rather than enforced.

---

### Question 20 (5 points)

An EFS-encrypted file is copied from an NTFS volume to a FAT32 USB drive. What
happens to the encryption?

- A) The file remains encrypted on the FAT32 drive because EFS encryption is stored in an alternate data stream
- B) Windows decrypts the file automatically during the copy and stores the plaintext on the FAT32 drive
- C) The copy operation fails with an error because encrypted files cannot be copied to non-NTFS volumes
- D) The file is copied in encrypted form, but a warning is displayed that encryption will not be enforced on FAT32

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — EFS metadata (DDF/DRF) is stored in NTFS alternate data streams. FAT32 does not support alternate data streams or the NTFS EFS attribute, so encryption cannot be preserved.
  - **B** — Correct. When an EFS-encrypted file is copied to a volume that does not support EFS (such as FAT32, ReFS without EFS support, or a network share without EFS), Windows automatically decrypts the file during the copy operation. The destination file is stored in plaintext. This is a significant data security risk if users copy sensitive files to USB drives.
  - **C** — Windows does not block the copy operation. It silently decrypts the file during the transfer, which is why user education about this behavior is important.
  - **D** — Windows does not display a warning about EFS decryption during file copy operations. The decryption occurs silently, which makes this behavior a common source of accidental data exposure.
