# Video Script: Module 11 — Windows Server Security: BitLocker, EFS, and Firewall (Part 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Production Notes

**Recorded by:** Professor Nash | Texas Wesleyan University

**Estimated runtime:** 11–13 minutes

**Part 2 focus:** PowerShell and GUI demos — configure Windows Defender Firewall
rules, enable BitLocker with TPM, back up recovery keys to AD, configure EFS on
a file, verify data recovery agent. Exam tips and lab preview.

---

## Opening

Welcome back to Module 11. In Part 1 we covered how Windows Defender Firewall,
BitLocker, and EFS work conceptually. Now let's open PowerShell and configure
all three.

---

## Demo 1 — Windows Defender Firewall: View and Create Rules

Let's start with the firewall. Open an elevated PowerShell console.

[SHOW SCREEN: PowerShell window open as Administrator]
[Alt-text: Blue PowerShell console window with PS C:\> prompt.]

View the current firewall profiles to confirm the Domain profile is active.

```powershell
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
```

[SHOW SCREEN: Get-NetFirewallProfile output]
[Alt-text: PowerShell output showing three rows: Domain (Enabled:True, DefaultInboundAction:Block, DefaultOutboundAction:Allow), Private (same), Public (same).]

All three profiles are enabled. Good. Now let's look at existing inbound rules.

```powershell
Get-NetFirewallRule -Direction Inbound -Enabled True -Action Allow |
    Select-Object DisplayName, Profile, Action |
    Sort-Object DisplayName |
    Select-Object -First 10
```

[SHOW SCREEN: Partial inbound rules list]
[Alt-text: PowerShell table showing 10 inbound allow rules with their display names and profiles.]

Now let's create a custom inbound rule. Suppose we have a custom web application
that listens on TCP port 8443.

```powershell
New-NetFirewallRule `
    -DisplayName "Allow Custom HTTPS App Port 8443" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 8443 `
    -Action Allow `
    -Profile Domain `
    -Description "Allows inbound TCP 8443 for the internal web application"
```

[SHOW SCREEN: New-NetFirewallRule success output]
[Alt-text: PowerShell output confirming the new rule was created with Name, DisplayName, and Enabled:True.]

Verify the rule was created.

```powershell
Get-NetFirewallRule -DisplayName "Allow Custom HTTPS App Port 8443" |
    Select-Object DisplayName, Direction, Action, Profile, Enabled
```

Now let's also block an outbound port. Block Telnet on port 23 — no server
should be initiating Telnet connections.

```powershell
New-NetFirewallRule `
    -DisplayName "Block Outbound Telnet TCP 23" `
    -Direction Outbound `
    -Protocol TCP `
    -RemotePort 23 `
    -Action Block `
    -Profile Any
```

To view all block rules.

```powershell
Get-NetFirewallRule -Action Block | Select-Object DisplayName, Direction, Enabled
```

---

## Demo 2 — Enable BitLocker on a Data Drive

For a server, let's enable BitLocker on a data drive (D:) rather than the OS
drive, to avoid the complexity of pre-boot authentication in a lab.

First, verify the TPM.

```powershell
Get-TPM | Select-Object TpmPresent, TpmReady, TpmEnabled
```

[SHOW SCREEN: Get-TPM output]
[Alt-text: PowerShell output showing TpmPresent:True, TpmReady:True, TpmEnabled:True.]

Install the BitLocker feature if not already installed.

```powershell
Get-WindowsFeature -Name BitLocker | Select-Object Name, InstallState

Install-WindowsFeature -Name BitLocker, RSAT-Feature-Tools-BitLocker -IncludeManagementTools
```

Enable BitLocker on D: with a recovery password protector.

```powershell
Enable-BitLocker `
    -MountPoint "D:" `
    -RecoveryPasswordProtector
```

[SHOW SCREEN: Enable-BitLocker output]
[Alt-text: PowerShell output showing KeyProtector with RecoveryPassword type and a 48-digit recovery password.]

Check the BitLocker status.

```powershell
Get-BitLockerVolume -MountPoint "D:" |
    Select-Object MountPoint, EncryptionMethod, VolumeStatus, ProtectionStatus
```

[SHOW SCREEN: Get-BitLockerVolume output]
[Alt-text: PowerShell output showing MountPoint:D:, EncryptionMethod:XtsAes256, VolumeStatus:EncryptionInProgress, ProtectionStatus:Off.]

The VolumeStatus shows EncryptionInProgress — BitLocker is encrypting the
drive in the background. Protection will show On once encryption completes.

To view the recovery key.

```powershell
(Get-BitLockerVolume -MountPoint "D:").KeyProtector |
    Where-Object {$_.KeyProtectorType -eq "RecoveryPassword"} |
    Select-Object KeyProtectorId, RecoveryPassword
```

In a production environment, back this key up to Active Directory.

```powershell
$keyId = (Get-BitLockerVolume -MountPoint "D:").KeyProtector |
    Where-Object {$_.KeyProtectorType -eq "RecoveryPassword"} |
    Select-Object -ExpandProperty KeyProtectorId

Backup-BitLockerKeyProtector -MountPoint "D:" -KeyProtectorId $keyId
```

After running this, the recovery key is stored in AD under the computer object
and can be retrieved by a domain administrator if the drive needs to be unlocked.

---

## Demo 3 — Encrypt a File with EFS

EFS works through Windows Explorer properties. Let's see both the GUI and
PowerShell approaches.

First, create a test file.

```powershell
New-Item -Path "C:\Sensitive\HR_Report.txt" -ItemType File -Force
Set-Content -Path "C:\Sensitive\HR_Report.txt" -Value "Confidential HR data"
```

Now encrypt it with PowerShell using the cipher command-line tool.

```powershell
cipher /e "C:\Sensitive\HR_Report.txt"
```

[SHOW SCREEN: cipher /e command output]
[Alt-text: Command window showing cipher output confirming the file was encrypted.]

In Windows Explorer, the file name appears in green to indicate EFS encryption.

[SHOW SCREEN: Windows Explorer showing HR_Report.txt in green]
[Alt-text: Windows Explorer with HR_Report.txt file name displayed in green text, indicating EFS encryption.]

Verify EFS status.

```powershell
cipher /u /n
```

This lists all EFS-encrypted files on the system for the current user.

To encrypt an entire folder so that all new files are automatically encrypted.

```powershell
cipher /e /s:"C:\Sensitive"
```

Now let's look at the EFS certificate.

```powershell
Get-Item Cert:\CurrentUser\My |
    Where-Object {$_.EnhancedKeyUsageList -like "*Encrypting File System*"} |
    Select-Object Subject, Thumbprint, NotAfter
```

[SHOW SCREEN: EFS certificate details]
[Alt-text: PowerShell output showing the EFS certificate Subject, Thumbprint, and expiration date.]

This certificate is what encrypts the file encryption key. Backing up this
certificate is essential. If the certificate is lost and there is no Data
Recovery Agent, the encrypted file is permanently unreadable.

Export the EFS certificate for backup.

```powershell
$cert = Get-Item Cert:\CurrentUser\My |
    Where-Object {$_.EnhancedKeyUsageList -like "*Encrypting File System*"}

Export-PfxCertificate `
    -Cert $cert `
    -FilePath "C:\CertBackup\EFS_Backup.pfx" `
    -Password (ConvertTo-SecureString "BackupP@ss!" -AsPlainText -Force)
```

---

## Demo 4 — Data Recovery Agent Verification

In an enterprise domain, the domain administrator's account automatically
becomes the Data Recovery Agent. In Group Policy, the EFS DRA certificate is
deployed through Computer Configuration, Windows Settings, Security Settings,
Public Key Policies, Encrypting File System.

[SHOW SCREEN: Group Policy Management Editor showing EFS DRA certificate]
[Alt-text: Group Policy Management Editor showing the Encrypting File System node under Public Key Policies with a DRA certificate listed.]

With the DRA configured, any encrypted file on the domain can be decrypted by
the domain administrator even if the encrypting user's certificate is lost.

---

## Exam Tips

**Exam Tip 1** — Windows Defender Firewall profile selection: the Domain profile
activates automatically when the computer can communicate with a domain
controller. You do not manually switch profiles — Windows detects the network
type and applies the correct profile.

**Exam Tip 2** — BitLocker vs. EFS: BitLocker protects the entire volume from
physical theft. EFS protects individual files from unauthorized access by other
users on the same running system. They address different threats and complement
each other.

**Exam Tip 3** — BitLocker TPM-only mode: the drive unlocks automatically at
boot with no user interaction. If the boot environment changes (BIOS update,
new boot device), the TPM will refuse to release the key and the recovery key
is required.

**Exam Tip 4** — EFS certificate backup: always export and back up the user's
EFS certificate with the private key. Without it and without a DRA, an
encrypted file is permanently inaccessible — even by administrators.

**Exam Tip 5** — cipher command: know the key flags: /e encrypts, /d decrypts,
/u /n lists all encrypted files without updating keys, /s applies recursively to
a directory. The cipher command works on NTFS volumes only.

---

## Lab Preview

In Lab 11, you will create and test inbound and outbound firewall rules using
both the WFAS console and PowerShell, enable BitLocker on a data volume with
a recovery password, back up the recovery key, encrypt a file and folder with
EFS, and verify the EFS certificate. Complete all parts and submit the required
screenshots.

See you in the quiz.

---

Module 11 Part 2 — End of Script
