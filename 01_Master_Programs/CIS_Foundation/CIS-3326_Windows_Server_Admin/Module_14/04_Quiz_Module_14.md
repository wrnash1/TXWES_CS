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

---

### Question 11 (5 points)

An administrator wants to view the current Windows Defender antivirus definition
version and the date of the last successful update on a server running Server
Core. Which PowerShell command shows this information?

- A) `Get-WindowsFeature -Name Windows-Defender | Select-Object Name, InstallState`
- B) `Get-MpComputerStatus | Select-Object AntivirusSignatureVersion, AntivirusSignatureLastUpdated`
- C) `Get-MpPreference | Select-Object SignatureVersion, LastUpdate`
- D) `Get-DefenderStatus -Property SignatureVersion, LastUpdated`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Get-WindowsFeature` reports whether the Defender feature is installed, not signature version or update dates.
  - **B** — Correct. `Get-MpComputerStatus` returns the Windows Defender status object including `AntivirusSignatureVersion` (definition build number) and `AntivirusSignatureLastUpdated` (timestamp of the last successful update).
  - **C** — `Get-MpPreference` returns Defender configuration settings such as exclusions and scan schedules. It does not return signature version or last update timestamps.
  - **D** — `Get-DefenderStatus` is not a valid PowerShell cmdlet. The correct cmdlet is `Get-MpComputerStatus`.

---

### Question 12 (5 points)

A JEA role capability file grants `Get-Service` and `Restart-Service` commands
to the HelpDesk role. A HelpDesk user connects to the JEA endpoint and attempts
to run `Stop-Service -Name Spooler`. What happens?

- A) The command succeeds because `Stop-Service` is implicitly allowed alongside `Restart-Service`
- B) The command fails because `Stop-Service` is not listed in the role capability file
- C) The command succeeds but is logged as an unauthorized action
- D) The JEA session terminates and the user is disconnected

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — JEA is a whitelist model, not a blacklist. Only explicitly listed commands are permitted. Related commands are not implicitly included.
  - **B** — Correct. JEA's role capability file defines the exact list of permitted commands. `Stop-Service` was not listed, so attempting to run it produces a "term is not recognized" or "not authorized" error within the JEA session. The session continues but the command is denied.
  - **C** — Unauthorized commands in JEA are blocked, not just logged. The user receives an error; the command does not execute.
  - **D** — JEA does not terminate the session when a blocked command is attempted. The user remains connected and can continue running permitted commands.

---

### Question 13 (5 points)

Windows LAPS (built-in, introduced in Windows Server 2022 / Windows 11 22H2)
stores local Administrator passwords in Active Directory. Which AD attribute
stores the managed password?

- A) `ms-Mcs-AdmPwd` (legacy LAPS attribute)
- B) `msLAPS-Password` (Windows LAPS encrypted attribute)
- C) `userPassword` (standard AD password attribute)
- D) `unicodePwd` (domain account password hash)

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `ms-Mcs-AdmPwd` is the attribute used by the legacy (Microsoft) LAPS download. Windows LAPS (built-in) uses a separate attribute set with optional encryption at rest.
  - **B** — Correct. Windows LAPS stores the managed password in the `msLAPS-Password` attribute (encrypted) or `msLAPS-PasswordExpirationTime` for the expiry timestamp. These attributes are added to the AD schema by `Update-LapsADSchema`.
  - **C** — `userPassword` is a standard LDAP attribute for directory service passwords. Windows domain accounts do not use this attribute for domain logon.
  - **D** — `unicodePwd` is the attribute used when setting domain user account passwords programmatically. It stores a hashed value for domain accounts, not local administrator passwords managed by LAPS.

---

### Question 14 (5 points)

Attack Surface Reduction (ASR) rules are configured via Group Policy or
Intune. An ASR rule blocks Office applications from creating child processes.
A user reports that a legitimate macro in Word is now failing to run a helper
application. What is the correct approach to allow the specific application
while keeping the ASR rule active for all other scenarios?

- A) Disable the ASR rule entirely to restore macro functionality
- B) Set the ASR rule to Audit mode to log the block without enforcing it
- C) Add the helper application's full path to the ASR exclusion list for that specific rule
- D) Uninstall Windows Defender to allow the macro to run freely

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — Disabling the ASR rule removes protection for all processes, not just the specific helper application. This is unnecessarily broad.
  - **B** — Audit mode logs blocks instead of enforcing them, which means all previously blocked actions now succeed. This removes protection from all processes matching the rule, not just the specific application.
  - **C** — Correct. ASR rules support per-path exclusions. Adding the specific helper application's executable path to the exclusion list allows that process to be created by Office applications while the rule continues to block all other unauthorized child process creation.
  - **D** — Uninstalling Windows Defender removes all antivirus and ASR protection from the server. This is never an appropriate response to a legitimate application compatibility issue.

---

### Question 15 (5 points)

A security administrator runs `Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4740}` and finds 500 lockout events for a specific service account within one hour. Event ID 4740 indicates which security event?

- A) A user account was deleted
- B) A user account was locked out due to too many failed logon attempts
- C) A privileged user used special logon rights
- D) A user password was changed

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Event ID 4726 indicates a user account was deleted. Event 4740 is specifically for lockout events.
  - **B** — Correct. Event ID 4740 is "A user account was locked out." When a service account generates 500 lockout events in an hour, it typically indicates a service or scheduled task is configured with an old password that was recently changed, causing repeated authentication failures.
  - **C** — Event ID 4672 indicates "Special privileges assigned to new logon" — a privileged account logged on with sensitive rights. This is different from a lockout.
  - **D** — Event ID 4723 indicates a user attempted to change their own password. Event ID 4724 indicates an administrator reset a password. Neither is Event 4740.

---

### Question 16 (5 points)

A JEA session configuration file sets `SessionType = RestrictedRemoteServer`.
What capabilities does a user in this session type have?

- A) Full PowerShell language mode with all installed modules available
- B) No PowerShell — only a command-line interface with limited tools
- C) A constrained endpoint with only explicitly permitted cmdlets available and no arbitrary scripting
- D) Read-only access to all PowerShell cmdlets with no write operations allowed

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — `RestrictedRemoteServer` is precisely designed to restrict the language mode and available commands. Full language mode would be `FullLanguage`, which is the default PowerShell mode — not JEA.
  - **B** — JEA sessions are PowerShell sessions, not command-line interfaces. Users can run the PowerShell cmdlets explicitly permitted in their role capability file.
  - **C** — Correct. `SessionType = RestrictedRemoteServer` configures the session with `NoLanguage` mode, disabling arbitrary scripting, variable assignment beyond simple use, and access to .NET types. Only cmdlets explicitly listed in the associated Role Capability file are available.
  - **D** — JEA does not distinguish between read and write at the session type level. Access is controlled by which cmdlets and parameters are listed in the role capability file, not by a read-only constraint.

---

### Question 17 (5 points)

An administrator wants to retrieve the LAPS-managed local Administrator password
for a computer named `WORKSTATION42` from Active Directory. Which PowerShell
command retrieves the password using Windows LAPS (built-in)?

- A) `Get-ADComputer -Identity WORKSTATION42 -Properties ms-Mcs-AdmPwd | Select-Object ms-Mcs-AdmPwd`
- B) `Get-LapsADPassword -Identity WORKSTATION42 -AsPlainText`
- C) `Get-ADObject -Identity WORKSTATION42 -Properties msLAPS-Password`
- D) `Get-LocalUser -Name Administrator -ComputerName WORKSTATION42`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `ms-Mcs-AdmPwd` is the legacy LAPS attribute. Windows LAPS (built-in) uses `msLAPS-Password` and the `Get-LapsADPassword` cmdlet, not the legacy attribute.
  - **B** — Correct. `Get-LapsADPassword -Identity WORKSTATION42 -AsPlainText` retrieves and decrypts the Windows LAPS-managed password for the specified computer. The caller must have Read permission on the `msLAPS-Password` attribute, which is typically granted to the computer's OU administrators or a designated LAPS readers group.
  - **C** — `Get-ADObject` can read raw AD attributes but does not decrypt the encrypted `msLAPS-Password` attribute. The `Get-LapsADPassword` cmdlet handles decryption.
  - **D** — `Get-LocalUser` queries local user accounts on the remote computer, which requires admin access to the remote machine — it does not retrieve the LAPS password stored in Active Directory.

---

### Question 18 (5 points)

A Windows Server has Credential Guard enabled. An attacker gains local
administrator access to the server and attempts to use Mimikatz to dump LSASS
memory for NTLM hashes. What result does the attacker encounter?

- A) Mimikatz successfully extracts all cached credentials because local admin access bypasses Credential Guard
- B) Mimikatz is blocked by Windows Defender Antivirus before it can execute
- C) Mimikatz can read LSASS memory but finds no usable credential material — secrets are stored in the VBS-isolated LSAIso process
- D) Credential Guard prevents local admin access entirely, so the attacker cannot reach the point of running Mimikatz

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — Credential Guard specifically prevents this scenario. Even with local admin rights, LSASS memory no longer contains the actual NTLM hashes or Kerberos ticket material — those are stored in the isolated LSAIso process, which is inaccessible from the normal OS environment.
  - **B** — Credential Guard is independent of antivirus. Windows Defender may or may not detect Mimikatz, but the question asks what Credential Guard specifically does. Credential Guard operates at the hypervisor level, not the antivirus level.
  - **C** — Correct. Credential Guard moves NTLM hashes and Kerberos tickets into the Virtualization-Based Security isolated process (LSAIso). When Mimikatz reads LSASS memory in the normal OS context, it finds stub values that cannot be used for Pass-the-Hash or Pass-the-Ticket attacks.
  - **D** — Credential Guard does not prevent local admin access. It protects credential material stored in LSASS. An attacker who gains local admin access can still run tools, but those tools cannot extract the protected secrets.

---

### Question 19 (5 points)

An administrator runs `auditpol /get /subcategory:"Account Lockout"` and sees
`Failure: No Auditing`. What security monitoring gap does this create?

- A) Failed logon attempts will not generate Event ID 4625 in the Security log
- B) Account lockout events (Event ID 4740) will not be recorded in the Security log
- C) LAPS password retrievals will not be audited
- D) JEA session connections will not be logged

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Event ID 4625 (failed logon) is controlled by the "Logon" audit subcategory, not "Account Lockout." Disabling "Account Lockout" auditing does not affect failed logon event generation.
  - **B** — Correct. The "Account Lockout" audit subcategory controls whether Event ID 4740 (account locked out) is written to the Security log. Without failure auditing on this subcategory, lockout events are silently discarded. This makes it impossible to detect and investigate repeated brute-force attempts that trigger lockouts.
  - **C** — LAPS password retrievals are audited through the "Directory Service Access" audit subcategory on the AD object, not the "Account Lockout" subcategory.
  - **D** — JEA session connections are logged through PowerShell transcripts and WinRM event logs, not through the "Account Lockout" audit subcategory.

---

### Question 20 (5 points)

Windows Defender Application Control (WDAC) is configured in enforcement mode
with a policy that only allows signed Microsoft binaries and specifically approved
application paths. An administrator needs to run an unsigned PowerShell script
for a maintenance task. What is the correct way to handle this situation?

- A) Temporarily disable WDAC enforcement for the duration of the maintenance task
- B) Run the script in WDAC audit mode to bypass enforcement while logging the execution
- C) Sign the script with a code signing certificate that is trusted by the WDAC policy, or add a path exception to the policy
- D) Rename the script to have a `.txt` extension to bypass WDAC file type restrictions

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — Temporarily disabling WDAC enforcement removes protection from all unauthorized code, not just the maintenance script. This creates a window of vulnerability and is not a controlled or auditable approach.
  - **B** — Audit mode logs but does not block. Switching to audit mode means all currently blocked applications also become allowed — this removes protection domain-wide during the maintenance window.
  - **C** — Correct. The proper approach within a WDAC policy is to either sign the script with an approved code signing certificate, or add a specific path or hash rule to the policy that permits this known-good script. Both methods maintain enforcement while allowing the legitimate exception.
  - **D** — WDAC evaluates files based on their content, hash, publisher signature, and path rules — not file extensions. Renaming a file does not bypass WDAC controls.

End of Quiz — Module 14
