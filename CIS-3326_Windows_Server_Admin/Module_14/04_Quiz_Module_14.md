# Quiz: Module 14 — Windows Server Security

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Microsoft Windows Server Administration

---

Instructions: Select the best answer for each question. Each question is worth 10 points.

---

### Question 1

A Windows Defender Antivirus scan is needed immediately on a server that has no GUI. Which PowerShell command initiates a quick scan?

- A) `Invoke-MpScan -Type Quick`
- B) `Start-MpScan -ScanType QuickScan`
- C) `Start-DefenderScan -Mode Quick`
- D) `Get-MpComputerStatus -ScanNow`

**Answer**: B

**Explanation**: `Start-MpScan -ScanType QuickScan` initiates a quick scan using the Windows Defender PowerShell module. The other options reference cmdlets or parameters that do not exist.

---

### Question 2

A Windows Server 2022 administrator creates a firewall Allow rule for TCP port 443 inbound on the Domain profile. However, an existing Block rule for the same port and profile exists. What happens when HTTPS traffic arrives on port 443?

- A) The Allow rule takes effect because it was created after the Block rule
- B) Both rules apply and traffic is allowed but flagged in the event log
- C) The Block rule takes effect because Block always overrides Allow in WFAS
- D) Windows prompts the administrator to resolve the conflict

**Answer**: C

**Explanation**: In Windows Firewall with Advanced Security, Block rules always take precedence over Allow rules within the same category and profile. Rule creation order does not affect priority.

---

### Question 3

Which JEA configuration file type defines what specific commands a role is permitted to run?

- A) Session Configuration File (.pssc)
- B) Role Capability File (.psrc)
- C) PowerShell Module Manifest (.psd1)
- D) Script Configuration File (.ps1)

**Answer**: B

**Explanation**: The Role Capability File (.psrc) defines the specific cmdlets, functions, and external commands available to a particular role. The Session Configuration File (.pssc) defines who can connect and which Role Capability Files apply to which user groups.

---

### Question 4

A JEA session is configured with `-RunAsVirtualAccount`. What does this mean for the commands run inside the session?

- A) Commands run as the connecting user's own identity with full administrator rights
- B) Commands run as a temporary local administrator account that exists only for the session duration
- C) Commands run as the SYSTEM account with all permissions on the domain
- D) Commands run as a read-only guest account with no write permissions

**Answer**: B

**Explanation**: `-RunAsVirtualAccount` causes JEA to create a temporary local administrator account for the session. This account has local admin rights but the user connecting only sees the commands defined in the Role Capability file. The virtual account is destroyed when the session ends.

---

### Question 5

Credential Guard prevents which specific type of attack?

- A) Brute-force dictionary attacks against user passwords
- B) SQL injection attacks against database servers
- C) Pass-the-Hash attacks where an attacker uses a stolen NTLM hash to authenticate
- D) Denial-of-service attacks against Windows Server network services

**Answer**: C

**Explanation**: Credential Guard isolates NTLM hashes and Kerberos tickets inside a Virtualization-Based Security container. This prevents attackers who have gained local admin rights from extracting credential material from LSASS memory and using it for Pass-the-Hash or Pass-the-Ticket lateral movement.

---

### Question 6

An organization has 2,000 workstations all imaged with the same local Administrator password. An attacker compromises one machine and recovers the local admin password hash. Which technology prevents the attacker from using this hash to log into all other machines?

- A) Windows Defender Antivirus
- B) Credential Guard
- C) Just Enough Administration
- D) Local Administrator Password Solution (LAPS)

**Answer**: D

**Explanation**: LAPS assigns a unique, randomly generated local Administrator password to each machine and stores it in Active Directory. Even if an attacker recovers the local admin hash from one machine, it is only valid on that one machine and cannot be used for lateral movement.

---

### Question 7

What Windows Security event ID indicates a failed logon attempt?

- A) 4624
- B) 4625
- C) 4720
- D) 4740

**Answer**: B

**Explanation**: Event ID 4625 is logged when a logon attempt fails. Event 4624 is a successful logon. Event 4720 is a user account created event. Event 4740 is a user account locked out event.

---

### Question 8

A JEA endpoint is configured with `TranscriptDirectory = "C:\JEALogs"`. What information is stored in the transcript files?

- A) Only the names of users who connected and the duration of their sessions
- B) A complete record of every command entered and every output returned during each JEA session
- C) Only failed commands and error messages from JEA sessions
- D) Encrypted copies of the role capability files used during each session

**Answer**: B

**Explanation**: JEA transcripts record every command entered and every output returned during a session, providing a full audit trail. This is a significant security and compliance benefit — administrators always know exactly what was done through a JEA endpoint.

---

### Question 9

Which Windows Server 2022 feature replaced the need to install the separate Microsoft LAPS download, and added support for storing passwords in Azure AD with encryption at rest?

- A) Windows Defender Credential Guard
- B) Windows LAPS (built into Windows)
- C) Azure AD Password Protection
- D) Microsoft Entra LAPS Extension

**Answer**: B

**Explanation**: Windows LAPS was introduced as a built-in feature in Windows Server 2022 and Windows 11 22H2. It replaces the separately downloaded legacy LAPS tool and adds Azure AD support, password encryption at rest in AD, and passphrase generation.

---

### Question 10

An administrator wants to verify that Credential Guard is running on a Windows Server 2022 system. Which PowerShell command provides this information?

- A) `Get-BitLockerVolume | Select-Object CredentialGuardStatus`
- B) `Get-WindowsFeature -Name CredentialGuard`
- C) `Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard`
- D) `Test-CredentialGuard -ComputerName localhost`

**Answer**: C

**Explanation**: The `Win32_DeviceGuard` WMI class in the `root\Microsoft\Windows\DeviceGuard` namespace provides status information about Virtualization-Based Security features including Credential Guard. The `CredentialGuardRunning` and `SecurityServicesRunning` properties show the current status.

---

End of Quiz — Module 14
