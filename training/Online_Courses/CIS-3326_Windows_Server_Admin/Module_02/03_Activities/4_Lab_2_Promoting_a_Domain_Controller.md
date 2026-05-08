### 4. Lab 2: Promoting a Domain Controller
**Objective:** Install the AD DS role and create a new forest.
**Instructions:**
1. Boot your Windows Server Core VM from Lab 1.
2. In the PowerShell prompt, install the AD DS role:
   `Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools`
3. Promote the server to a Domain Controller in a brand new forest named `corp.local`:
   `Install-ADDSForest -DomainName corp.local -InstallDns`
4. When prompted for a SafeModeAdministratorPassword, provide a secure password and remember it. Press 'A' to accept all prompts. The server will reboot.
5. Once rebooted, log in. You will notice your prompt now says `CORP\Administrator`.
**Deliverable:** Take a screenshot of your PowerShell window after running the command `Get-ADDomain`. Submit this screenshot to Blackboard.

---
