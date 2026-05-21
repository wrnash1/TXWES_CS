# Reading Guide: Module 12 - PowerShell for Server Administration

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 12 – PowerShell for Server Administration**! This week's study material covers Windows PowerShell as the primary scripting and automation tool for Windows Server administrators. PowerShell is not just a supplement to the GUI — it is increasingly the primary interface for managing Azure, Active Directory, and Windows Server at scale. PowerShell skills are tested directly on both the AZ-800 and AZ-801 exams.

As a student, you will learn the PowerShell pipeline, how to use the ActiveDirectory module to manage AD objects, how to configure remoting for managing multiple servers, and how to write basic scripts and functions for repetitive administrative tasks. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **PowerShell Pipeline**: The mechanism that passes the output of one cmdlet directly as input to the next cmdlet using the `|` character. Objects — not plain text — are passed through the pipeline, allowing the next cmdlet to access properties and methods of the objects directly.
* **Execution Policy**: A safety setting that controls whether PowerShell scripts (.ps1 files) can run. Common values: `Restricted` (no scripts), `RemoteSigned` (local scripts run freely; downloaded scripts require a digital signature), `Bypass` (no restrictions). Set with `Set-ExecutionPolicy`.
* **PowerShell Remoting (WinRM)**: The Windows Remote Management (WinRM) service enables PowerShell commands to run on remote computers. Enabled with `Enable-PSRemoting`. Use `Enter-PSSession` for interactive one-to-one sessions or `Invoke-Command` to run a script block on one or many computers simultaneously.
* **Desired State Configuration (DSC)**: A PowerShell-based management framework that declaratively defines the desired configuration state of a server (e.g., "this role must be installed," "this service must be running"). DSC continuously monitors and corrects drift from the defined state.
* **PowerShell Module**: A package of cmdlets, functions, and resources grouped for a specific technology (e.g., the `ActiveDirectory` module, the `NetAdapter` module). Modules are imported with `Import-Module` and can be installed from the PowerShell Gallery with `Install-Module`.
* **Get-Help / Get-Command**: The built-in PowerShell discovery tools. `Get-Command *keyword*` finds cmdlets related to a topic. `Get-Help <cmdlet> -Examples` shows usage examples. `Get-Member` reveals the properties and methods of an object passed through the pipeline.

---

### 2. Certification Exam Tips

* **Know the verb-noun convention**: All PowerShell cmdlets follow a Verb-Noun naming pattern (e.g., `Get-ADUser`, `Set-ADUser`, `New-ADGroup`, `Remove-ADUser`). AZ-800 exam questions that ask "which cmdlet performs X" can often be answered by matching the correct verb (Get, Set, New, Remove, Enable, Disable) to the noun.
* **`Invoke-Command` for bulk operations**: When a task must be run on multiple servers simultaneously, `Invoke-Command -ComputerName server1, server2 -ScriptBlock {...}` is the correct approach — not logging into each server individually. This is the most efficient pattern for enterprise administration.
* **Execution policy is not a security boundary**: A common distractor is treating Execution Policy as a hard security control. It is a convenience setting that an administrator or attacker with local admin rights can override with `-ExecutionPolicy Bypass`. Real script security requires code signing with trusted certificates.
* **Microsoft Learn Reference**: Review PowerShell documentation at [Microsoft Learn – PowerShell Documentation](https://learn.microsoft.com/en-us/powershell/) and the [ActiveDirectory module reference](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) for all AD cmdlets tested on AZ-800.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the PowerShell remoting and scripting documentation at [Microsoft Learn: PowerShell Documentation](https://learn.microsoft.com/en-us/powershell/) and the Active Directory module reference at [Microsoft Learn: ActiveDirectory Module](https://learn.microsoft.com/en-us/powershell/module/activedirectory/). Focus on `Invoke-Command`, `Enter-PSSession`, and the most common AD management cmdlets.
* **Required Video:** Watch the video lecture on **PowerShell for Server Administration** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will enable PowerShell Remoting, use `Invoke-Command` to run a script block on a remote server, create a batch of AD user accounts from a CSV file using `Import-Csv` and `New-ADUser`, and write a script that queries all AD users in a specified OU and exports the results to a CSV file.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the PowerShell documentation at [Microsoft Learn: PowerShell Documentation](https://learn.microsoft.com/en-us/powershell/).
* [ ] Read the ActiveDirectory module reference at [Microsoft Learn: ActiveDirectory Module](https://learn.microsoft.com/en-us/powershell/module/activedirectory/).
* [ ] Watch the video lecture on **PowerShell for Server Administration** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
