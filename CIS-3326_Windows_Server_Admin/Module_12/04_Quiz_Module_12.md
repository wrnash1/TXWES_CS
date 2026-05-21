# Quiz: Module 12 - PowerShell for Server Administration

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

An administrator wants to retrieve all Active Directory user accounts whose passwords have not been changed in more than 90 days and export the results to a CSV file. Which PowerShell approach correctly accomplishes this using the pipeline?

A) Use `Get-ADUser -Filter *` and write a separate script to loop through each user, call `Get-ADUserPassword`, and manually build the CSV output.
B) Use `Get-ADUser -Filter {PasswordLastSet -lt (Get-Date).AddDays(-90)} -Properties PasswordLastSet | Export-Csv -Path stale.csv -NoTypeInformation`.
C) Use `Search-ADAccount -PasswordNeverExpires | Export-Csv -Path stale.csv` because this cmdlet retrieves accounts with unchanged passwords.
D) Use `net user /domain > stale.csv` because the net user command exports password age data to files directly.

* **Correct Answer:** B) Use `Get-ADUser -Filter {PasswordLastSet -lt (Get-Date).AddDays(-90)} -Properties PasswordLastSet | Export-Csv -Path stale.csv -NoTypeInformation`.
* **Distractor Analysis:**
  * *Why A is incorrect:* There is no `Get-ADUserPassword` cmdlet. The correct approach uses `-Properties PasswordLastSet` on `Get-ADUser` and pipes the output directly to `Export-Csv`, which is the idiomatic PowerShell pipeline pattern rather than a manual loop.
  * *Why C is incorrect:* `Search-ADAccount -PasswordNeverExpires` retrieves accounts whose passwords are set to never expire — a different attribute than PasswordLastSet age. It would not identify accounts whose passwords have simply not been changed in 90 days.
  * *Why D is incorrect:* The `net user` command outputs basic account information in a fixed-width text format. It does not provide PasswordLastSet data in a structured format suitable for CSV export, and piping it to a file produces plain text, not CSV.

---

### Question 2

An administrator needs to run the same PowerShell command on 50 remote servers simultaneously to collect the current Windows service status. Which PowerShell feature enables parallel execution across multiple remote computers in a single command?

A) `Enter-PSSession` with a loop that connects to each server sequentially, collecting output before moving to the next server.
B) `Invoke-Command -ComputerName (Get-Content servers.txt) -ScriptBlock { Get-Service }`, which sends the script block to all listed computers in parallel using WinRM.
C) `New-PSSession` run once on the local machine, which automatically fans out commands to all domain-joined servers.
D) PowerShell Remoting must be enabled on the local machine only; remote servers accept connections without any configuration.

* **Correct Answer:** B) `Invoke-Command -ComputerName (Get-Content servers.txt) -ScriptBlock { Get-Service }`, which sends the script block to all listed computers in parallel using WinRM.
* **Distractor Analysis:**
  * *Why A is incorrect:* `Enter-PSSession` creates a single interactive session to one remote computer at a time. Looping through 50 servers with `Enter-PSSession` executes sequentially, not in parallel, and requires manual interaction for each connection.
  * *Why C is incorrect:* `New-PSSession` creates a persistent connection to a specified remote computer — it does not automatically discover or fan out to all domain-joined servers. A computer list or session array must be explicitly provided.
  * *Why D is incorrect:* PowerShell Remoting (WinRM) must be enabled on the remote servers that will receive commands, not just the local machine. The `Enable-PSRemoting` cmdlet must be run on each target server, or it can be enabled via Group Policy.

---

### Question 3

A junior administrator attempts to run a downloaded PowerShell script on a Windows Server and receives the error: "File cannot be loaded because running scripts is disabled on this system." What is the most appropriate remediation in a managed enterprise environment?

A) Run `Set-ExecutionPolicy Unrestricted` on the server to permanently allow all scripts from any source to run without restriction.
B) Rename the script file from `.ps1` to `.bat` so that Windows executes it as a batch file, bypassing the execution policy.
C) Run `Set-ExecutionPolicy RemoteSigned` so that locally created scripts run without signing while downloaded scripts require a trusted digital signature.
D) Right-click the script file and select "Run as Administrator" — elevated privileges automatically bypass the execution policy restriction.

* **Correct Answer:** C) Run `Set-ExecutionPolicy RemoteSigned` so that locally created scripts run without signing while downloaded scripts require a trusted digital signature.
* **Distractor Analysis:**
  * *Why A is incorrect:* `Unrestricted` allows all scripts — including unsigned scripts from untrusted internet sources — to run without any warning or block. This is the least secure execution policy and is not appropriate for managed production servers.
  * *Why B is incorrect:* Renaming a `.ps1` file to `.bat` does not convert PowerShell syntax to valid batch commands; the script would produce syntax errors or unexpected behavior. Execution policy applies to the PowerShell engine, not to batch file processing.
  * *Why D is incorrect:* Running as Administrator elevates the process token for privilege purposes but does not change or bypass the PowerShell execution policy. The execution policy is a separate session-level or machine-level setting evaluated independently of the caller's privilege level.

---

### Question 4

An administrator needs to create 200 new user accounts in Active Directory from a CSV file that contains columns for GivenName, Surname, and Department. Which PowerShell technique efficiently accomplishes this without manually running a command for each user?

A) Open Active Directory Users and Computers, use the Import function under the Action menu to bulk-import the CSV file directly.
B) Use `Import-Csv users.csv | ForEach-Object { New-ADUser -GivenName $_.GivenName -Surname $_.Surname -Department $_.Department -Name "$($_.GivenName) $($_.Surname)" }` to pipeline CSV rows into account creation.
C) Use `New-ADUser -Import users.csv` because the `-Import` parameter accepts a CSV file path for bulk account creation.
D) Use `dsadd user` in a batch loop because legacy tools process CSV files faster than PowerShell cmdlets for large imports.

* **Correct Answer:** B) Use `Import-Csv users.csv | ForEach-Object { New-ADUser -GivenName $_.GivenName -Surname $_.Surname -Department $_.Department -Name "$($_.GivenName) $($_.Surname)" }` to pipeline CSV rows into account creation.
* **Distractor Analysis:**
  * *Why A is incorrect:* Active Directory Users and Computers (ADUC) does not have a native CSV import function in the GUI. Bulk account creation from CSV files is a command-line and scripting operation, not a GUI operation.
  * *Why C is incorrect:* `New-ADUser` does not have an `-Import` parameter. The correct pattern is to use `Import-Csv` to read the CSV file and pipe each row as an object to `New-ADUser`, referencing column names as properties.
  * *Why D is incorrect:* `dsadd user` is a legacy command-line tool that does not natively accept CSV file input. It would require additional scripting to parse the CSV, and PowerShell with `Import-Csv` is the modern, recommended approach for bulk AD operations.

---

### Question 5

An administrator wants to use PowerShell Desired State Configuration (DSC) to ensure that the Web Server (IIS) role is installed on a set of servers and that its configuration remains consistent even if someone manually removes it. Which DSC concept describes this self-correcting behavior?

A) DSC Push mode, which sends the configuration to the server once and logs any future drift without automatically correcting it.
B) DSC idempotency — DSC resources are designed so that applying a configuration multiple times produces the same result, and the Local Configuration Manager periodically checks and reapplies the declared state to correct drift.
C) DSC Pull mode only corrects configuration drift if an administrator manually triggers a consistency check by running `Start-DscConfiguration`.
D) DSC uses Group Policy as its enforcement engine, so IIS role drift is corrected at the next Group Policy refresh interval.

* **Correct Answer:** B) DSC idempotency — DSC resources are designed so that applying a configuration multiple times produces the same result, and the Local Configuration Manager periodically checks and reapplies the declared state to correct drift.
* **Distractor Analysis:**
  * *Why A is incorrect:* DSC Push mode does deliver the configuration to the target node, and the Local Configuration Manager (LCM) on the node will periodically re-check and reapply it based on the `ConfigurationModeFrequencyMins` setting — it does not merely log drift without correcting it.
  * *Why C is incorrect:* In DSC Pull mode the LCM automatically contacts the pull server and checks for configuration updates on a scheduled interval. Manual invocation of `Start-DscConfiguration` is not required for automatic drift correction; the LCM handles this autonomously.
  * *Why D is incorrect:* DSC is an independent configuration management platform built into PowerShell and WinRM. It does not use Group Policy as its enforcement engine. Group Policy and DSC are separate technologies that can coexist but operate independently.
