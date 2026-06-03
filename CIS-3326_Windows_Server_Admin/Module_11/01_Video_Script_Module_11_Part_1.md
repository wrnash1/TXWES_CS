# Video Script: Module 11 — Windows Server Security: BitLocker, EFS, and Firewall (Part 1)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Production Notes

**Recorded by:** Professor Nash | Texas Wesleyan University

**Estimated runtime:** 13–15 minutes

**Part 1 focus:** Concepts — Windows Defender Firewall with Advanced Security,
BitLocker Drive Encryption, Encrypting File System (EFS), and how these three
security layers work together to protect Windows Server.

---

## Opening

Welcome to Module 11. This module is all about securing Windows Server at
three distinct layers: the network perimeter with Windows Defender Firewall,
the volume at rest with BitLocker, and individual files with EFS.

Security is not a single layer — it is a stack. If an attacker gets through
the firewall, disk encryption means they cannot read the data on a stolen
drive. If they can read the volume, EFS means they still cannot open specific
sensitive files without the right certificate. Understanding each layer and
when to apply it is the goal of this module.

---

## Section 1 — Windows Defender Firewall with Advanced Security

Windows Defender Firewall has been part of Windows since Windows XP Service
Pack 2. On Windows Server, the version you will work with is called Windows
Defender Firewall with Advanced Security — abbreviated WFAS. It is a
stateful, host-based firewall.

[SHOW SCREEN: Windows Defender Firewall with Advanced Security console open]
[Alt-text: The WFAS MMC snap-in showing the three profiles: Domain, Private, and Public in the left pane.]

There are three firewall profiles.

**Domain profile** activates automatically when the computer is joined to a
domain and can communicate with a domain controller. This is the profile active
on your servers in the corporate network.

**Private profile** activates when the network is marked as private — such as
a home or small office network where the user trusts the environment.

**Public profile** activates on untrusted networks — airports, coffee shops,
any location where the computer cannot verify the network. This profile is the
most restrictive by default.

The correct profile activates automatically based on network discovery. On a
domain-joined server in the office, the Domain profile is always active.

---

## Section 2 — Inbound and Outbound Rules

Firewall rules control what traffic is allowed through the firewall. There are
two directions.

**Inbound rules** control traffic arriving at the server. By default, Windows
Server blocks most inbound traffic unless a rule explicitly allows it. When you
install a server role like DNS or DHCP, Windows automatically creates the
required inbound rules.

**Outbound rules** control traffic leaving the server. By default, all outbound
traffic is allowed unless a rule explicitly blocks it.

[SHOW SCREEN: WFAS Inbound Rules list]
[Alt-text: WFAS console showing the Inbound Rules list with multiple rules. Some show green check marks (enabled, allow) and some show red circles (enabled, block).]

Each rule can be scoped in multiple ways:

- **Program** — allow or block based on the executable file path
- **Port** — allow or block based on TCP or UDP port number
- **Protocol** — allow or block based on IP protocol (TCP, UDP, ICMP)
- **IP address** — scope the rule to specific remote IP addresses or subnets
- **Service** — apply the rule only to a specific Windows service

For the exam, remember the evaluation order: rules with Block action take
precedence over rules with Allow action within the same category.

---

## Section 3 — Connection Security Rules

Beyond traffic filtering, WFAS also manages Connection Security Rules.
These use IPsec to encrypt or authenticate traffic between specific computers.

Connection Security rules are separate from allow/block rules. A Connection
Security rule says "traffic between Computer A and Computer B must be
authenticated using Kerberos" — it doesn't allow or deny the traffic itself,
it defines the security requirements for the connection.

Connection Security rules are important for internal server-to-server
communication where you want to ensure packets have not been tampered with
in transit.

---

## Section 4 — Managing Firewall Rules with PowerShell

```powershell
# View all enabled inbound rules
Get-NetFirewallRule -Direction Inbound -Enabled True |
    Select-Object Name, DisplayName, Action, Profile

# Create a new inbound allow rule for a custom application
New-NetFirewallRule `
    -DisplayName "Allow Custom App TCP 8080" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 8080 `
    -Action Allow `
    -Profile Domain

# Block a specific outbound port
New-NetFirewallRule `
    -DisplayName "Block Outbound Telnet" `
    -Direction Outbound `
    -Protocol TCP `
    -RemotePort 23 `
    -Action Block

# Disable a rule by name
Disable-NetFirewallRule -DisplayName "Allow Custom App TCP 8080"

# Enable a rule
Enable-NetFirewallRule -DisplayName "File and Printer Sharing (Echo Request - ICMPv4-In)"
```

The `New-NetFirewallRule`, `Get-NetFirewallRule`, `Enable-NetFirewallRule`, and
`Disable-NetFirewallRule` cmdlets are the PowerShell interface to WFAS.

---

## Section 5 — BitLocker Drive Encryption

BitLocker encrypts entire volumes. If a server's hard drive is removed and
connected to another computer, the data is unreadable without the BitLocker
recovery key.

[SHOW SCREEN: BitLocker Drive Encryption control panel showing a protected drive]
[Alt-text: BitLocker Drive Encryption control panel with the C: drive showing a padlock icon and "BitLocker on" status.]

BitLocker uses the Trusted Platform Module — the TPM — as the hardware root of
trust. The TPM is a chip on the server's motherboard that stores cryptographic
keys in hardware. At boot time, the TPM verifies the boot integrity and
releases the BitLocker encryption key only if the boot environment has not
been tampered with.

### TPM Modes

**TPM only** — the key is stored entirely in the TPM. The drive unlocks
automatically at boot without any user interaction. This is the most common
mode for servers.

**TPM + PIN** — requires both the TPM and a PIN entered at boot. More secure
but requires someone to enter the PIN every time the server restarts.

**TPM + USB startup key** — requires both the TPM and a USB drive inserted
at boot. Used in environments where the PIN requirement is operationally
difficult.

**Password only (no TPM)** — available but not recommended. The key is
protected only by a password with no hardware attestation.

### BitLocker and the Recovery Key

Every BitLocker-protected volume has a recovery key — a 48-digit numerical
code. If the TPM cannot unlock the drive (because the BIOS changed, a new
boot device was added, or the TPM itself failed), the recovery key is the only
way to unlock the volume.

Recovery key storage options: Active Directory, Azure AD, a USB drive, a file,
or printed. For servers in an enterprise, storing recovery keys in Active
Directory is standard practice.

---

## Section 6 — BitLocker on Windows Server

On Windows Server, BitLocker is installed as a feature, not automatically.

```powershell
# Install BitLocker feature and management tools
Install-WindowsFeature -Name BitLocker -IncludeManagementTools

# Verify TPM status before enabling BitLocker
Get-TPM
```

[SHOW SCREEN: Get-TPM output]
[Alt-text: PowerShell output showing TpmPresent:True, TpmReady:True, TpmEnabled:True, TpmActivated:True.]

```powershell
# Enable BitLocker on C: drive with TPM only, recovery key to AD
Enable-BitLocker `
    -MountPoint "C:" `
    -TpmProtector `
    -RecoveryKeyPath "C:\BitLockerKeys" `
    -RecoveryKeyProtector
```

For backing up the recovery key to Active Directory.

```powershell
Backup-BitLockerKeyProtector `
    -MountPoint "C:" `
    -KeyProtectorId (Get-BitLockerVolume -MountPoint "C:").KeyProtector[0].KeyProtectorId
```

---

## Section 7 — Encrypting File System (EFS)

EFS is a file-level encryption feature built into NTFS. Unlike BitLocker
which encrypts an entire volume, EFS encrypts individual files and folders.
The encryption is transparent to the user who encrypted the file — they open
it normally. Other users, even administrators, cannot open it.

[SHOW SCREEN: File Properties dialog with Encrypt contents to secure data checkbox]
[Alt-text: Windows file Properties dialog showing Advanced Attributes with the Encrypt contents to secure data checkbox checked. The file name shows in green in Explorer.]

EFS uses public key cryptography. When a user encrypts a file, the following
steps occur:

1. A symmetric encryption key is generated for that file.
2. That symmetric key is encrypted with the user's EFS public certificate.
3. The encrypted symmetric key is stored with the file.
4. Only the holder of the corresponding private key can decrypt the file.

This means EFS encryption is tied to the user's certificate. If the certificate
is lost (without a data recovery agent or backup), the file is permanently
inaccessible.

### Data Recovery Agents

In an enterprise, the domain administrator is typically designated as a Data
Recovery Agent (DRA). The DRA has a special EFS certificate that can decrypt
any EFS-encrypted file on the domain. This is a safety net for situations where
a user's certificate is lost.

```powershell
# Get the current EFS certificate for a user
Get-Item Cert:\CurrentUser\My | Where-Object {$_.EnhancedKeyUsageList -match "Encrypting File System"}
```

### When to Use EFS vs. BitLocker

This comparison is important for the exam.

BitLocker protects a volume at rest — against physical theft of the drive.
EFS protects specific files from unauthorized access by other users on the
same system, even when the volume is mounted and accessible.

Use BitLocker for full drive protection. Use EFS for sensitive files that
multiple users on the same system should not access. They complement each other.

---

## Module Summary

Windows Server security at three layers.

Windows Defender Firewall with Advanced Security: stateful host-based firewall
with three profiles (Domain, Private, Public), inbound and outbound rules, and
connection security rules for IPsec.

BitLocker Drive Encryption: full volume encryption using the TPM as hardware
root of trust. TPM-only mode for servers. Recovery keys stored in Active
Directory. Protects against physical drive theft.

EFS: file-level encryption using the user's certificate. Transparent to the
encrypting user. Other users, including administrators, cannot read the file
without the correct private key. Data Recovery Agents provide enterprise-level
recovery.

In Part 2 we will configure all three features in demos. See you there.

---

Module 11 Part 1 — End of Script
