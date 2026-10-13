# Video Script: Module 14 — Windows Server Security (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

### Introduction

Welcome back to Module 14. In Part 1 we covered Windows Defender Antivirus, Windows Firewall with Advanced Security, and security auditing. In Part 2, we tackle three technologies focused on limiting what attackers can do once they are inside: Just Enough Administration, Credential Guard, and the Local Administrator Password Solution.

These three technologies address the same fundamental attack pattern: lateral movement. After gaining initial access to one system, attackers move across the network by reusing credentials or exploiting overprivileged accounts. JEA, Credential Guard, and LAPS each break a different link in that chain.

---

### Section 1: Just Enough Administration

Just Enough Administration, or JEA, is a PowerShell security feature that allows you to create constrained administrative endpoints. Instead of giving a helpdesk operator full administrative rights on all servers just to reset passwords, JEA lets you give them access to a PowerShell endpoint where the only thing they can do is run `Reset-ADAccountPassword`.

The principle behind JEA is **least privilege** — users should have access to exactly the capabilities they need, nothing more.

JEA has two configuration file types.

**Session Configuration File (.pssc)**: Defines who can connect to the endpoint, what PowerShell version and language mode is available, and which Role Capability files apply to which users or groups.

**Role Capability File (.psrc)**: Defines what a specific role can do — which cmdlets, scripts, and external programs are available, and optionally what parameters and values can be used.

```powershell
# Create a Role Capability file directory
New-Item -Path "C:\JEADemo\RoleCapabilities" -ItemType Directory -Force

# Create a Role Capability file for a DNS admin role
New-PSRoleCapabilityFile `
    -Path "C:\JEADemo\RoleCapabilities\DNSAdmin.psrc" `
    -VisibleCmdlets @{
        Name = "Get-DnsServerResourceRecord"
        Name = "Add-DnsServerResourceRecord"
        Name = "Remove-DnsServerResourceRecord"
    } `
    -VisibleFunctions "Restart-Service" `
    -VisibleExternalCommands "C:\Windows\system32\ipconfig.exe"
```

```powershell
# Create a Session Configuration file
New-PSSessionConfigurationFile `
    -Path "C:\JEADemo\JEAConfig.pssc" `
    -SessionType RestrictedRemoteServer `
    -RunAsVirtualAccount `
    -RoleDefinitions @{
        "CONTOSO\DNS Admins" = @{
            RoleCapabilityFiles = "C:\JEADemo\RoleCapabilities\DNSAdmin.psrc"
        }
    }

# Register the JEA endpoint
Register-PSSessionConfiguration `
    -Path "C:\JEADemo\JEAConfig.pssc" `
    -Name "JEA_DNSAdmin" `
    -Force
```

The `-RunAsVirtualAccount` parameter is critical: when a helpdesk operator connects through this endpoint, their commands run under a temporary virtual administrator account on the local machine — but they can only run the cmdlets you explicitly listed. The operator never has direct administrative credentials and cannot escape the sandbox to run arbitrary commands.

---

### Section 2: Connecting to a JEA Endpoint

From a client workstation, a user connects to a JEA endpoint just like any other PSSession, but specifying the configuration name:

```powershell
# Connect to the JEA endpoint as a helpdesk operator
Enter-PSSession -ComputerName "DNSServer01" `
    -ConfigurationName "JEA_DNSAdmin" `
    -Credential (Get-Credential)
```

Once connected, the operator can run only the commands defined in the role capability file. Attempting to run any other command returns "the term is not recognized."

JEA also supports transcription — automatically logging every command entered and every output returned in the constrained session. This provides a complete audit trail of everything done through the JEA endpoint.

```powershell
# Enable transcript logging in the session configuration
New-PSSessionConfigurationFile `
    -Path "C:\JEADemo\JEAConfig.pssc" `
    -TranscriptDirectory "C:\JEATranscripts" `
    -SessionType RestrictedRemoteServer `
    -RunAsVirtualAccount
```

---

### Section 3: Credential Guard

Credential Guard is a virtualization-based security feature that isolates the Windows credential store (specifically the LSASS process) inside a protected Hyper-V container called a Virtual Secure Mode (VSM) trustlet. This prevents attackers who have gained admin rights on a machine from extracting credential hashes using tools like Mimikatz.

Without Credential Guard, an attacker with local administrator rights can dump NTLM hashes and Kerberos tickets from the LSASS process memory. Those credentials can then be used to authenticate to other systems — this is called Pass-the-Hash or Pass-the-Ticket.

With Credential Guard, the credential material is stored inside the VSM container, which the attacker cannot access even with full admin rights on the host OS.

Requirements for Credential Guard:

- 64-bit processor with SLAT support
- UEFI firmware (Generation 2 VM or physical server with UEFI)
- Virtualization-based security (VBS) must be supported and enabled
- Windows Server 2016 or later

```powershell
# Check if VBS and Credential Guard are enabled
Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard |
    Select-Object VirtualizationBasedSecurityStatus,
        CredentialGuardRunning,
        SecurityServicesRunning
```

Enabling Credential Guard via Group Policy:

Navigate to: Computer Configuration > Administrative Templates > System > Device Guard > Turn On Virtualization Based Security

Set "Credential Guard Configuration" to "Enabled with UEFI lock" for maximum security (prevents disabling without physical access to change UEFI settings).

---

### Section 4: Local Administrator Password Solution (LAPS)

LAPS solves one of the most dangerous and common security problems in Windows environments: the reuse of the local administrator password across all machines.

In many organizations, every workstation and server has the same local Administrator password, set during imaging. An attacker who discovers this password on one machine can use it to authenticate as local administrator on every other machine in the organization — gaining instant lateral movement capability.

LAPS assigns a unique, randomly generated password to the local Administrator account on each machine and stores that password in Active Directory, protected by ACLs. The password automatically rotates on a configurable schedule.

LAPS architecture:

- A Group Policy Client Side Extension (CSE) runs on each managed computer
- At each Group Policy refresh, the CSE checks whether the local admin password has expired
- If expired, it generates a new random password, sets it on the local Admin account, and stores the new password in the computer's AD object
- Authorized users (IT staff) retrieve the current password from AD using LAPS tooling

```powershell
# Install the LAPS PowerShell module (Windows LAPS, built into Server 2022)
# or install legacy LAPS from Microsoft Download Center

# For Windows LAPS (built-in to Windows Server 2022 and Windows 11 22H2+)
# Update the AD schema
Update-LapsADSchema

# Configure LAPS policy on an OU via Group Policy or directly:
Set-LapsADComputerSelfPermission -Identity "OU=Workstations,DC=contoso,DC=com"

# View the current LAPS password for a computer
Get-LapsADPassword -Identity "DESKTOP01" -AsPlainText
```

The `Get-LapsADPassword` command is only available to users with read access to the LAPS password attribute — controlled by AD ACLs. This means only designated IT staff can retrieve passwords, not general users.

---

### Section 5: Windows LAPS vs. Legacy LAPS

Windows Server 2022 and Windows 11 22H2 introduced Windows LAPS, a rebuilt version of the original Microsoft LAPS product. Key improvements in Windows LAPS:

- Built into Windows — no separate software installation
- Supports Azure AD in addition to on-premises Active Directory
- Supports password encryption at rest in AD (legacy LAPS stored in plaintext attribute)
- Supports automatic account management (can target any local account, not just Administrator)
- Supports passphrase generation as an alternative to random character passwords

---

### Section 6: Putting It All Together — Defense in Depth

Let's look at how these five security technologies layer together.

An attacker has phished one helpdesk user and gained access to their workstation.

Layer 1 — **Windows Firewall**: Prevents the attacker from directly connecting to server ports they shouldn't reach (e.g., SMB on port 445 from that workstation subnet).

Layer 2 — **Windows Defender**: Detects and blocks known malware tools the attacker tries to download or execute.

Layer 3 — **LAPS**: The attacker tries the local admin password on nearby machines. Because LAPS has given every machine a unique password, the compromised workstation's local admin password does not work on any other machine.

Layer 4 — **Credential Guard**: The attacker escalates to local admin on the compromised workstation and tries to dump LSASS. Credential Guard prevents credential extraction from the VSM container.

Layer 5 — **JEA**: Even if a privileged account is compromised, JEA limits what that account can do on server endpoints. An account that can only run DNS management cmdlets cannot install software or access sensitive files.

Layer 6 — **Auditing**: Every failed login, every privileged operation, every JEA transcript is logged. The security team detects the attack through SIEM alerts on anomalous event patterns.

No single layer stops a sophisticated attacker. All six layers together make the attack extremely difficult, time-consuming, and detectable.

---

### Summary

In this two-part module, we covered the full Windows Server security toolkit: Windows Defender Antivirus, Windows Firewall with Advanced Security, security auditing, Just Enough Administration, Credential Guard, and LAPS. These technologies together implement a defense-in-depth strategy that is directly tested on Microsoft certification exams and used daily in enterprise environments.

In Module 15, we go deep on PowerShell automation and Desired State Configuration — the tools that make all of this security configuration manageable at scale. See you there.
