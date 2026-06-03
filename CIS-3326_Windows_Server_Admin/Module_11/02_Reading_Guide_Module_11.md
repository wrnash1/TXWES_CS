# Reading Guide: Module 11 — Windows Server Security: BitLocker, EFS, and Firewall

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

Module 11 covers Windows Server host security at three layers: the network
perimeter (Windows Defender Firewall with Advanced Security), volume-level
encryption (BitLocker Drive Encryption), and file-level encryption (EFS).
This reading guide provides reference tables, architecture diagrams, PowerShell
command reference, 8 exam tips, a glossary, and a study checklist.

---

## 1. Security Layer Architecture

```text
Threat: Network Attack          → Defend with: Windows Defender Firewall (WFAS)
Threat: Physical Drive Theft    → Defend with: BitLocker Drive Encryption
Threat: Unauthorized File Access
        by other OS-level users  → Defend with: EFS (Encrypting File System)
```

These three controls operate independently and complement each other. A server
hardened with all three requires an attacker to defeat the network perimeter,
then find a way to read an encrypted volume, then overcome per-file encryption
even if the volume is mounted.

---

## 2. Windows Defender Firewall with Advanced Security

### Firewall Profiles

| Profile | When Active | Default Inbound | Default Outbound |
|---|---|---|---|
| Domain | Computer can reach a domain controller | Block | Allow |
| Private | Network marked as Private (trusted) | Block | Allow |
| Public | Untrusted/unknown networks | Block | Allow |

Profile selection is automatic — Windows evaluates the network and applies the
appropriate profile. All three profiles can be active simultaneously on different
network adapters.

### Rule Priority and Evaluation

Rules with Block action take precedence over Allow rules within the same
category. Explicit rules take precedence over default behavior.

### Rule Scope Components

| Scope Parameter | Controls |
|---|---|
| Direction | Inbound or Outbound |
| Protocol | TCP, UDP, ICMP, Any |
| Local Port | Port on this server |
| Remote Port | Port on the connecting client |
| Local IP Address | IP of this server's interface |
| Remote IP Address | IP or subnet of the remote host |
| Program | Executable file path |
| Service | Windows service name |
| Profile | Domain, Private, Public, or Any |

### Common Built-In Inbound Rules (Enabled by Role)

| Server Role | Rule Created | Port |
|---|---|---|
| DNS Server | DNS (UDP-In), DNS (TCP-In) | 53 |
| DHCP Server | DHCP Server (UDP-In) | 67 |
| RD Gateway | RD Gateway (TCP-In) | 443 |
| File and Printer Sharing | SMB (TCP-In) | 445 |
| Remote Desktop | Remote Desktop (TCP-In) | 3389 |
| WinRM | Windows Remote Management (HTTP-In) | 5985 |

---

## 3. BitLocker Drive Encryption

### BitLocker Protector Modes

| Mode | What Is Required at Boot | Suitable For |
|---|---|---|
| TPM only | Nothing (automatic) | Servers in locked data centers |
| TPM + PIN | TPM + numeric/alphanumeric PIN | High-security workstations |
| TPM + USB startup key | TPM + USB drive inserted | Environments where PIN is impractical |
| Password (no TPM) | Password | Systems without TPM (not recommended) |
| Recovery key only | 48-digit recovery key | Emergency unlocking only |

### BitLocker Encryption Algorithms

| Algorithm | Strength | Notes |
|---|---|---|
| XTS-AES 128-bit | Strong | Default on Windows 10/Server 2016+ |
| XTS-AES 256-bit | Stronger | Recommended for high-security environments |
| AES-CBC 128-bit | Legacy | For compatibility with older systems |
| AES-CBC 256-bit | Legacy | For compatibility with older systems |

### Recovery Key Storage Options

| Storage Location | Best For |
|---|---|
| Active Directory (on-premises) | Domain-joined servers; standard enterprise practice |
| Azure AD | Cloud-managed or hybrid environments |
| USB flash drive | Offline environments; physical key custody |
| File on separate volume | Admin-managed backup |
| Printed copy | Physical archive (secure storage required) |

### BitLocker Phases

```text
1. BitLocker feature installed (Install-WindowsFeature -Name BitLocker)
2. TPM verified (Get-TPM)
3. BitLocker enabled on volume (Enable-BitLocker -MountPoint "D:" ...)
4. Encryption in progress (VolumeStatus: EncryptionInProgress)
5. Encryption complete (VolumeStatus: FullyEncrypted, ProtectionStatus: On)
6. Recovery key backed up to AD (Backup-BitLockerKeyProtector)
```

---

## 4. Encrypting File System (EFS)

### EFS Encryption Process

```text
User encrypts a file:
  1. Windows generates a random File Encryption Key (FEK) for this file
  2. FEK is encrypted with the user's EFS public certificate
  3. Encrypted FEK is stored in the file's Data Decryption Field (DDF)
  4. File content is encrypted with the FEK using symmetric encryption (AES)

User opens the file:
  1. Windows reads the encrypted FEK from DDF
  2. User's private key (from certificate store) decrypts the FEK
  3. FEK decrypts the file content — transparent to the user

Another user attempts to open the file:
  1. Their private key cannot decrypt the FEK
  2. Access is denied — file content is unreadable
```

### EFS vs. BitLocker Comparison

| Feature | EFS | BitLocker |
|---|---|---|
| Scope | Individual files and folders | Entire volume |
| Encryption tied to | User certificate (per-user) | Volume key (hardware/TPM) |
| Protection against | Other users on same OS | Physical drive removal |
| Transparent to owner | Yes (automatic) | Yes (auto-unlock with TPM) |
| Requires NTFS | Yes | No (works on FAT32 too) |
| Data Recovery Agent | Yes (DRA certificate) | Recovery key |
| Use case | Sensitive files on shared server | Laptop/server disk encryption |

### EFS Key Operations

| Operation | Command |
|---|---|
| Encrypt a file | `cipher /e filename` |
| Decrypt a file | `cipher /d filename` |
| Encrypt a folder recursively | `cipher /e /s:foldername` |
| List encrypted files (no key update) | `cipher /u /n` |
| Update EFS keys (after cert change) | `cipher /u` |

### Data Recovery Agent (DRA)

The DRA is a special account (typically Domain Administrator) whose EFS
certificate is stored in Group Policy. A copy of each file's FEK is encrypted
with the DRA's public key and stored in the file's Data Recovery Field (DRF).
If the original user's certificate is lost, the DRA can still decrypt the file.

DRA is configured in Group Policy at:
Computer Configuration → Windows Settings → Security Settings →
Public Key Policies → Encrypting File System

---

## 5. PowerShell Command Reference

```powershell
# ── Windows Defender Firewall ─────────────────────────────────────────
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction
Get-NetFirewallRule -Direction Inbound -Enabled True | Select-Object DisplayName, Action
New-NetFirewallRule -DisplayName "Name" -Direction Inbound -Protocol TCP `
    -LocalPort 8080 -Action Allow -Profile Domain
Enable-NetFirewallRule  -DisplayName "Name"
Disable-NetFirewallRule -DisplayName "Name"
Remove-NetFirewallRule  -DisplayName "Name"
Set-NetFirewallProfile  -Profile Domain -DefaultInboundAction Block

# ── BitLocker ─────────────────────────────────────────────────────────
Get-TPM | Select-Object TpmPresent, TpmReady, TpmEnabled
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus
Enable-BitLocker -MountPoint "D:" -TpmProtector
Enable-BitLocker -MountPoint "D:" -RecoveryPasswordProtector
Disable-BitLocker -MountPoint "D:"
Suspend-BitLocker -MountPoint "D:"              # suspend for maintenance
Resume-BitLocker  -MountPoint "D:"
(Get-BitLockerVolume "D:").KeyProtector         # view key protectors and recovery password
Backup-BitLockerKeyProtector -MountPoint "D:" -KeyProtectorId <id>

# ── EFS ───────────────────────────────────────────────────────────────
cipher /e "C:\file.txt"                         # encrypt file
cipher /d "C:\file.txt"                         # decrypt file
cipher /e /s:"C:\Folder"                        # encrypt folder recursively
cipher /u /n                                    # list encrypted files
Get-Item Cert:\CurrentUser\My |
    Where-Object {$_.EnhancedKeyUsageList -like "*Encrypting File System*"}
Export-PfxCertificate -Cert $cert -FilePath "backup.pfx" -Password (...)
```

---

## 6. Firewall Rule Architecture

```text
Network Packet Arrives:
    │
    ▼
Is there an explicit Block rule matching this packet?
    │ Yes → DROP
    │ No
    ▼
Is there an explicit Allow rule matching this packet?
    │ Yes → ALLOW
    │ No
    ▼
Apply Default Behavior for this Profile:
    Inbound:  Block (default)
    Outbound: Allow (default)
```

---

## 7. Exam Tips

**Exam Tip 1** — The Domain firewall profile activates automatically when the
computer can reach a domain controller. It is not manually selected. On a
domain-joined server connected to the corporate network, Domain profile is
always active.

**Exam Tip 2** — BitLocker requires TPM version 1.2 or higher. Without a TPM,
you can enable BitLocker with a USB startup key only (not TPM + USB — just USB
as the sole protector), or you can configure a Group Policy exception to allow
password-only BitLocker.

**Exam Tip 3** — EFS requires NTFS. You cannot encrypt files on FAT32 or
exFAT volumes with EFS. BitLocker can encrypt any volume type.

**Exam Tip 4** — EFS encryption is per-user. If User A encrypts a file, User
B cannot open it even if User B has NTFS Full Control permission on that file.
NTFS permissions and EFS encryption are independent security controls.

**Exam Tip 5** — Data Recovery Agents: in a domain environment, the default
DRA is the domain administrator. DRA is configured through Group Policy, not
manually per-computer. Without a DRA, lost EFS certificates mean permanent
data loss.

**Exam Tip 6** — BitLocker recovery key: the 48-digit numerical recovery key
is the emergency unlock mechanism when the TPM cannot release the volume key
(BIOS update, hardware change, TPM failure). Always back up the recovery key
to AD before you need it.

**Exam Tip 7** — `Suspend-BitLocker` is used before applying firmware updates
or BIOS changes, not `Disable-BitLocker`. Suspending temporarily disables
protection without decrypting the volume. After the update, protection resumes
automatically on next reboot.

**Exam Tip 8** — Firewall rules with Block action always take precedence over
Allow rules. If you create an Allow rule for port 443 and there is also a
Block rule for port 443, the Block rule wins.

---

## 8. Glossary

| Term | Definition |
|---|---|
| Windows Defender Firewall with Advanced Security (WFAS) | Host-based stateful firewall built into Windows Server; manages inbound/outbound rules and IPsec connection security |
| Firewall Profile | A set of firewall rules that activates based on the network environment: Domain, Private, or Public |
| Inbound Rule | Firewall rule controlling traffic arriving at the server |
| Outbound Rule | Firewall rule controlling traffic leaving the server |
| Connection Security Rule | IPsec rule in WFAS that authenticates or encrypts traffic between two computers |
| BitLocker Drive Encryption | Windows feature that encrypts entire volumes using AES encryption and a TPM as hardware root of trust |
| TPM | Trusted Platform Module — a hardware chip that stores cryptographic keys and verifies boot integrity |
| Recovery Key | 48-digit numerical code used to unlock a BitLocker-protected volume when the TPM cannot release the key |
| XTS-AES | BitLocker encryption algorithm; 128-bit or 256-bit; default in Windows Server 2016 and later |
| EFS | Encrypting File System — NTFS feature that encrypts individual files using the user's certificate |
| File Encryption Key (FEK) | Per-file symmetric key generated by EFS; encrypted with the user's public certificate |
| Data Decryption Field (DDF) | Metadata stored with an EFS file containing the FEK encrypted for the file owner |
| Data Recovery Field (DRF) | Metadata stored with an EFS file containing the FEK encrypted for the Data Recovery Agent |
| Data Recovery Agent (DRA) | Domain account (typically Administrator) with a certificate that can decrypt any EFS file on the domain |
| cipher | Windows command-line tool for managing EFS encryption |
| Suspend-BitLocker | Temporarily disables BitLocker protection without decrypting; used before firmware updates |

---

## 9. Study Checklist

- Watch Module 11 Part 1 video (WFAS profiles, inbound/outbound rules, BitLocker TPM modes, EFS process)
- Watch Module 11 Part 2 video (PowerShell demos: firewall rules, BitLocker, EFS, DRA)
- Memorize the three WFAS profiles and when each activates
- Know BitLocker protector modes (TPM only, TPM+PIN, TPM+USB, password)
- Know the difference between BitLocker (volume) and EFS (file-level) and what threat each addresses
- Know the EFS encryption process: FEK, DDF, DRF, and the role of the user certificate
- Know the purpose of the Data Recovery Agent and how to configure it via Group Policy
- Know `Suspend-BitLocker` vs. `Disable-BitLocker` and when each is appropriate
- Complete Lab 11 and submit required screenshots

---

## Additional Resources

- [Windows Defender Firewall with Advanced Security overview](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/windows-firewall-with-advanced-security)
- [BitLocker overview](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/bitlocker-overview)
- [Encrypting File System overview](https://learn.microsoft.com/en-us/windows/win32/fileio/file-encryption)
- [BitLocker PowerShell cmdlets](https://learn.microsoft.com/en-us/powershell/module/bitlocker/)

---

*Review all sections before beginning Lab 11, Quiz 11, and Discussion 11.*
