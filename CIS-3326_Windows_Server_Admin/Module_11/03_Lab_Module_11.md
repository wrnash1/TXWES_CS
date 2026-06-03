# Lab Activity: Module 11 — Windows Server Security: BitLocker, EFS, and Firewall

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Lab Overview

In this lab you will configure Windows Defender Firewall rules using both the
GUI console and PowerShell, enable BitLocker on a data volume with a recovery
password, back up the recovery key to Active Directory, and encrypt files and
folders using EFS.

**Estimated Time:** 75–90 minutes

**Prerequisites:**

- DC1 is running Windows Server 2022 and is a domain controller for txwes.edu
- You are logged in as a Domain Administrator
- PowerShell console is open with Administrator privileges
- A secondary volume (D:) exists or can be created; if not, use a VHD

**Learning Objectives:**

- Create inbound and outbound firewall rules with `New-NetFirewallRule`
- Manage firewall rules with `Get-NetFirewallRule`, `Enable-NetFirewallRule`, `Disable-NetFirewallRule`
- Enable BitLocker on a data volume using `Enable-BitLocker`
- Back up BitLocker recovery keys to Active Directory
- Encrypt files and folders using the `cipher` command
- Verify EFS certificate and export it for backup

---

## Part 1 — Windows Defender Firewall Rules

### Step 1.1 — View Current Firewall Profile Settings

```powershell
Get-NetFirewallProfile |
    Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
```

Take **Screenshot 1** — `Get-NetFirewallProfile` output showing all three
profile settings.

### Step 1.2 — View Existing Inbound Allow Rules

```powershell
Get-NetFirewallRule -Direction Inbound -Enabled True -Action Allow |
    Select-Object DisplayName, Profile, Action |
    Sort-Object DisplayName |
    Select-Object -First 15
```

### Step 1.3 — Create a Custom Inbound Allow Rule

```powershell
New-NetFirewallRule `
    -DisplayName "Lab11 - Allow TCP 8080 Inbound" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 8080 `
    -Action Allow `
    -Profile Domain `
    -Description "Lab 11 test rule - allows inbound TCP 8080 on Domain profile"
```

Verify the rule was created.

```powershell
Get-NetFirewallRule -DisplayName "Lab11 - Allow TCP 8080 Inbound" |
    Select-Object DisplayName, Direction, Protocol, Action, Profile, Enabled
```

### Step 1.4 — Create a Custom Outbound Block Rule

```powershell
New-NetFirewallRule `
    -DisplayName "Lab11 - Block Outbound Telnet TCP 23" `
    -Direction Outbound `
    -Protocol TCP `
    -RemotePort 23 `
    -Action Block `
    -Profile Any `
    -Description "Lab 11 test rule - blocks outbound Telnet"
```

### Step 1.5 — Test Disabling and Re-Enabling a Rule

```powershell
# Disable the inbound rule
Disable-NetFirewallRule -DisplayName "Lab11 - Allow TCP 8080 Inbound"

# Verify it is disabled
Get-NetFirewallRule -DisplayName "Lab11 - Allow TCP 8080 Inbound" |
    Select-Object DisplayName, Enabled

# Re-enable the rule
Enable-NetFirewallRule -DisplayName "Lab11 - Allow TCP 8080 Inbound"
```

### Step 1.6 — View Both Lab Rules Together

```powershell
Get-NetFirewallRule -DisplayName "Lab11*" |
    Select-Object DisplayName, Direction, Action, Enabled
```

Take **Screenshot 2** — Both Lab11 rules showing correct Direction, Action,
and Enabled status.

### Step 1.7 — Get Port Details for a Rule

```powershell
Get-NetFirewallRule -DisplayName "Lab11 - Allow TCP 8080 Inbound" |
    Get-NetFirewallPortFilter |
    Select-Object Protocol, LocalPort, RemotePort
```

---

## Part 2 — BitLocker Drive Encryption

### Step 2.1 — Prepare a Data Volume

If D: does not exist, create a virtual hard disk and initialize it.

```powershell
# Check if D: exists
Get-PSDrive -Name D -ErrorAction SilentlyContinue

# If D: does not exist, create a VHD (run in elevated PS)
New-VHD -Path "C:\VHDs\DataDisk.vhdx" -SizeBytes 5GB -Dynamic |
    Mount-VHD -Passthru |
    Initialize-Disk -PassThru |
    New-Partition -AssignDriveLetter -UseMaximumSize |
    Format-Volume -FileSystem NTFS -NewFileSystemLabel "DataVol" -Confirm:$false
```

### Step 2.2 — Verify BitLocker Feature

```powershell
Get-WindowsFeature -Name BitLocker | Select-Object Name, DisplayName, InstallState
```

If not installed.

```powershell
Install-WindowsFeature -Name BitLocker, RSAT-Feature-Tools-BitLocker `
    -IncludeManagementTools -Restart
```

### Step 2.3 — Check TPM Status

```powershell
Get-TPM | Select-Object TpmPresent, TpmReady, TpmEnabled, TpmActivated
```

Take **Screenshot 3** — `Get-TPM` output showing TPM status values.

### Step 2.4 — Enable BitLocker with a Recovery Password

```powershell
Enable-BitLocker `
    -MountPoint "D:" `
    -RecoveryPasswordProtector
```

This enables BitLocker using only a recovery password protector. The 48-digit
recovery password will be displayed in the output — copy it.

### Step 2.5 — Check Encryption Status

```powershell
Get-BitLockerVolume -MountPoint "D:" |
    Select-Object MountPoint, EncryptionMethod, VolumeStatus, ProtectionStatus, EncryptionPercentage
```

Take **Screenshot 4** — `Get-BitLockerVolume` output showing D: with
EncryptionMethod, VolumeStatus, and ProtectionStatus.

### Step 2.6 — View the Recovery Key

```powershell
(Get-BitLockerVolume -MountPoint "D:").KeyProtector |
    Where-Object {$_.KeyProtectorType -eq "RecoveryPassword"} |
    Select-Object KeyProtectorType, RecoveryPassword, KeyProtectorId
```

### Step 2.7 — Back Up Recovery Key to Active Directory

```powershell
$vol = Get-BitLockerVolume -MountPoint "D:"

$keyId = ($vol.KeyProtector |
    Where-Object {$_.KeyProtectorType -eq "RecoveryPassword"}).KeyProtectorId

Backup-BitLockerKeyProtector -MountPoint "D:" -KeyProtectorId $keyId
```

No output on success. Verify the key was stored in AD by checking the
computer object in Active Directory Users and Computers under the BitLocker
Recovery tab.

### Step 2.8 — Suspend BitLocker (Simulate Pre-Maintenance)

```powershell
Suspend-BitLocker -MountPoint "D:"

Get-BitLockerVolume -MountPoint "D:" |
    Select-Object MountPoint, ProtectionStatus
```

ProtectionStatus should show `Suspended`.

```powershell
# Resume protection
Resume-BitLocker -MountPoint "D:"

Get-BitLockerVolume -MountPoint "D:" |
    Select-Object MountPoint, ProtectionStatus
```

---

## Part 3 — Encrypting File System (EFS)

### Step 3.1 — Create Test Files

```powershell
New-Item -Path "C:\LabSecure" -ItemType Directory -Force | Out-Null

Set-Content -Path "C:\LabSecure\Confidential.txt" `
    -Value "This file contains confidential HR data."

Set-Content -Path "C:\LabSecure\Financial.txt" `
    -Value "This file contains financial projections."

Set-Content -Path "C:\LabSecure\Public.txt" `
    -Value "This file is not confidential."
```

### Step 3.2 — Encrypt a Single File

```powershell
cipher /e "C:\LabSecure\Confidential.txt"
```

Verify the file is encrypted.

```powershell
cipher "C:\LabSecure"
```

Files marked with E are encrypted. Files marked with U are unencrypted.

Take **Screenshot 5** — `cipher` directory listing showing Confidential.txt
marked as encrypted (E) and other files marked unencrypted (U).

### Step 3.3 — Encrypt an Entire Folder

```powershell
cipher /e /s:"C:\LabSecure"
```

All existing files in the folder are now encrypted. New files created in this
folder will also be automatically encrypted.

Verify all files are encrypted.

```powershell
cipher "C:\LabSecure"
```

### Step 3.4 — List All Encrypted Files for This User

```powershell
cipher /u /n
```

Take **Screenshot 6** — `cipher /u /n` output listing EFS-encrypted files.

### Step 3.5 — View the EFS Certificate

```powershell
Get-Item Cert:\CurrentUser\My |
    Where-Object {$_.EnhancedKeyUsageList -like "*Encrypting File System*"} |
    Select-Object Subject, Thumbprint, NotAfter, Issuer
```

Take **Screenshot 7** — EFS certificate details showing Subject, Thumbprint,
and expiration date.

### Step 3.6 — Export the EFS Certificate for Backup

```powershell
New-Item -Path "C:\CertBackup" -ItemType Directory -Force | Out-Null

$cert = Get-Item Cert:\CurrentUser\My |
    Where-Object {$_.EnhancedKeyUsageList -like "*Encrypting File System*"}

Export-PfxCertificate `
    -Cert $cert `
    -FilePath "C:\CertBackup\EFS_AdminCert.pfx" `
    -Password (ConvertTo-SecureString "EFS@Backup2024!" -AsPlainText -Force)

# Verify the export
Test-Path "C:\CertBackup\EFS_AdminCert.pfx"
```

### Step 3.7 — Decrypt a File

```powershell
cipher /d "C:\LabSecure\Financial.txt"

# Verify it is now unencrypted
cipher "C:\LabSecure"
```

Financial.txt should now show U (unencrypted).

---

## Part 4 — Firewall Rule Cleanup

Remove the test rules created in Part 1.

```powershell
Remove-NetFirewallRule -DisplayName "Lab11 - Allow TCP 8080 Inbound" -Confirm:$false
Remove-NetFirewallRule -DisplayName "Lab11 - Block Outbound Telnet TCP 23" -Confirm:$false

# Verify removal
Get-NetFirewallRule -DisplayName "Lab11*" -ErrorAction SilentlyContinue
```

No output confirms the rules were removed.

---

## Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1** — `Get-NetFirewallProfile` output showing all three profile
configurations.

**Screenshot 2** — Both Lab11 firewall rules with correct Direction, Action,
and Enabled status.

**Screenshot 3** — `Get-TPM` output showing TPM status.

**Screenshot 4** — `Get-BitLockerVolume` output showing D: encryption status.

**Screenshot 5** — `cipher` directory listing showing Confidential.txt
encrypted.

**Screenshot 6** — `cipher /u /n` output listing encrypted files.

**Screenshot 7** — EFS certificate details from certificate store.

---

## Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| Firewall profiles viewed | 10 | Screenshot 1 shows all three profile configurations |
| Firewall rules created | 20 | Screenshot 2 shows both rules with correct settings |
| TPM verified | 10 | Screenshot 3 shows TPM status |
| BitLocker enabled | 20 | Screenshot 4 shows D: encrypted with protection status |
| EFS file encryption | 20 | Screenshot 5 shows file encrypted via cipher |
| Encrypted files listed | 10 | Screenshot 6 shows cipher /u /n output |
| EFS certificate viewed | 10 | Screenshot 7 shows certificate details |

---

## Troubleshooting Notes

If `Get-TPM` shows TpmPresent:False, the virtual machine or physical server
does not have a TPM. Enable TPM in the VM settings (Generation 2 VMs support
virtual TPM) or configure BitLocker to work without TPM via Group Policy:
Computer Configuration → Administrative Templates → Windows Components →
BitLocker Drive Encryption → Operating System Drives → Require additional
authentication at startup.

If `cipher /e` fails with "Access is denied," ensure the file is on an NTFS
volume and the user account has Write permissions. EFS does not work on FAT32
or ReFS volumes.

If the EFS certificate does not appear in `Get-Item Cert:\CurrentUser\My`,
encrypt any file with `cipher /e` first — Windows auto-generates an EFS
certificate on first use.

```powershell
# Verify the volume file system before using EFS
Get-Volume -DriveLetter C | Select-Object DriveLetter, FileSystem
```
