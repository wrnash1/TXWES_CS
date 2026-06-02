# Video Script: Module 05 - Group Policy Objects: Creation and Management (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 05 - Group Policy Objects (GPOs): Creation and Management

**Part:** 2 of 2 — Demonstrations, PowerShell Commands, Exam Tips, and Lab Preview

**Estimated Duration:** 12 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Recap and Demo Overview]

Welcome back to Module 05. In Part 1 we covered GPO architecture, LSDOU processing, Enforced and Block Inheritance, Computer vs. User Configuration, Security Filtering, WMI Filters, and Loopback Processing. In Part 2 I will demonstrate creating and linking a GPO in GPMC, configuring Security Filtering, running gpresult for troubleshooting, and show the PowerShell GPO management cmdlets.

---

### [SEGMENT 2 — Demo: Create a GPO in GPMC]

**[SHOW SCREEN: Server Manager — Tools — Group Policy Management]**

[Alt-text: Server Manager with the Tools menu open and Group Policy Management selected.]

Open Server Manager, click Tools, and select Group Policy Management. The GPMC tree shows your domain, sites, and GPOs.

**[SHOW SCREEN: GPMC — Group Policy Objects container — right-click — New]**

[Alt-text: GPMC showing the Group Policy Objects container right-clicked with the New option highlighted in the context menu.]

Expand your domain. Right-click Group Policy Objects and select New. Name the GPO `CORP_IT_Security_Baseline`. Click OK.

The GPO now exists in the repository but is not yet linked to any OU or container. It has no effect until it is linked.

---

### [SEGMENT 3 — Demo: Edit the GPO]

**[SHOW SCREEN: GPME opening with Computer Configuration and User Configuration nodes]**

[Alt-text: Group Policy Management Editor showing the Computer Configuration and User Configuration trees for CORP_IT_Security_Baseline.]

Right-click the GPO and select Edit. This opens the Group Policy Management Editor.

Navigate to: Computer Configuration > Policies > Windows Settings > Security Settings > Account Policies > Password Policy.

**[SHOW SCREEN: Password Policy settings in GPME]**

[Alt-text: Group Policy Management Editor showing Password Policy settings including Minimum password length set to 14 characters.]

Double-click "Minimum password length." Enable it and set it to 14 characters. Click OK.

Now navigate to: Computer Configuration > Policies > Administrative Templates > Control Panel > Personalization.

Double-click "Password protect the screen saver." Set it to Enabled. Then set "Screen saver timeout" to 600 seconds (10 minutes).

Close the GPME. The GPO is configured but still unlinked.

---

### [SEGMENT 4 — Demo: Link the GPO to an OU]

**[SHOW SCREEN: GPMC — right-clicking the IT OU — Link an Existing GPO]**

[Alt-text: GPMC tree showing the IT OU right-clicked with Link an Existing GPO option highlighted.]

In the GPMC tree, right-click the `IT` OU (under Departments). Select "Link an Existing GPO." Choose `CORP_IT_Security_Baseline` from the list. Click OK.

**[SHOW SCREEN: GPMC showing the linked GPO under the IT OU with its link order]**

[Alt-text: GPMC showing CORP_IT_Security_Baseline listed under the IT OU with Link Order 1.]

The GPO now appears linked to the IT OU. The link order is 1, meaning it has the highest precedence among GPOs linked to this OU.

---

### [SEGMENT 5 — Demo: Configure Security Filtering]

**[SHOW SCREEN: GPMC — Scope tab of the linked GPO — Security Filtering section]**

[Alt-text: GPMC Scope tab showing the Security Filtering section with Authenticated Users listed.]

Click the linked GPO. Go to the Scope tab. Under Security Filtering, you see "Authenticated Users" — this means all authenticated domain objects in the OU receive this policy.

To restrict to only the IT Admins group:

1. Click "Authenticated Users" and click Remove
2. Click Add, search for `G_ITAdmins`, click OK

Now only members of `G_ITAdmins` will receive the Computer Configuration settings from this GPO.

Note: if this GPO has Computer Configuration settings, I also need to ensure domain computers can read the GPO. Click the Delegation tab, click Add, choose `Domain Computers`, and set to Read (not Apply Group Policy).

---

### [SEGMENT 6 — Demo: Force Policy Refresh and Verify]

**[SHOW SCREEN: PowerShell showing gpupdate and gpresult commands]**

[Alt-text: PowerShell console showing gpupdate /force command output and gpresult /r output showing Applied GPOs.]

On a domain-joined workstation, open an elevated command prompt or PowerShell and run:

```cmd
gpupdate /force
```

This immediately refreshes both Computer Configuration and User Configuration policies. The command outputs "Computer Policy update has completed successfully" and "User Policy update has completed successfully" when done.

```cmd
gpresult /r
```

`gpresult /r` shows a text summary of all applied GPOs for the current computer and user. Look for your GPO name under "Applied Group Policy Objects."

```cmd
gpresult /h C:\GPReport.html
```

This generates a full HTML report saved to `C:\GPReport.html`. Open it in a browser for the complete Resultant Set of Policy (RSoP) — every setting, every GPO, and every filtered/denied policy with reasons.

---

### [SEGMENT 7 — Demo: Diagnose a GPO Not Applying]

**[SHOW SCREEN: gpresult /r output showing Applied GPOs and Denied GPOs sections]**

[Alt-text: Command prompt showing gpresult /r output with sections for Applied Group Policy Objects and Denied GPOs with reason codes.]

If a GPO is not applying, `gpresult /r` will show it in the "Denied GPOs" section with a reason code. The common reason codes:

- "Inaccessible" — the client cannot read the GPO due to a permission or SYSVOL issue. Check Security Filtering and SYSVOL replication.
- "Disabled" — the GPO link is disabled in GPMC. Re-enable the link.
- "Empty" — the GPO has no settings configured. Add settings.
- "Inaccessible WMI filter" — the WMI filter returned FALSE or an error. Check WMI filter syntax and scope.

---

### [SEGMENT 8 — PowerShell GPO Management]

**[SHOW SCREEN: PowerShell showing GroupPolicy module cmdlets]**

[Alt-text: PowerShell console showing various Group Policy cmdlets including New-GPO, New-GPLink, and Get-GPResultantSetOfPolicy.]

```powershell
# Create a new GPO
New-GPO -Name "CORP_HR_UserPolicy" -Domain "corp.local"

# Link GPO to an OU
New-GPLink `
    -Name "CORP_HR_UserPolicy" `
    -Target "OU=HR,OU=Departments,DC=corp,DC=local" `
    -LinkEnabled Yes `
    -Enforced No

# View all GPOs in the domain
Get-GPO -All | Select-Object DisplayName, CreationTime, ModificationTime

# Get GPO report as HTML
Get-GPOReport -Name "CORP_IT_Security_Baseline" -ReportType HTML -Path "C:\GPOReport.html"

# Force policy refresh on a remote computer
Invoke-GPUpdate -Computer "WS-IT-001" -Force

# Force policy refresh on all computers in an OU
Get-ADComputer -Filter * -SearchBase "OU=IT,OU=Departments,DC=corp,DC=local" |
    ForEach-Object { Invoke-GPUpdate -Computer $_.Name -Force }

# Get RSoP for a specific user and computer combination
Get-GPResultantSetOfPolicy -Computer "WS-IT-001" -User "CORP\dprince" -ReportType HTML -Path "C:\RSoP.html"
```

---

### [SEGMENT 9 — Exam Tips]

**[SHOW SCREEN: Exam tips slide for Module 05]**

**Exam Tip 1:** LSDOU — OU wins over Domain in normal processing. But "Enforced" reverses this and wins over everything. And "Enforced" always beats "Block Inheritance."

**Exam Tip 2:** `gpresult /r` for quick text output. `gpresult /h report.html` for full RSoP HTML report. Know when to use each: `/r` for quick diagnosis, `/h` for thorough analysis.

**Exam Tip 3:** Security Filtering with the Deny ACE approach: keep "Authenticated Users" as Read, add a Deny "Apply Group Policy" for the excluded group. This ensures computers can still read the GPO for Computer Configuration processing.

**Exam Tip 4:** WMI Filters are dynamic — they evaluate at each refresh. No group maintenance required. Use them for OS version or hardware targeting.

**Exam Tip 5:** Loopback Processing in Replace mode overwrites user-OU policies with computer-OU policies. Merge mode combines them with computer-OU winning conflicts. Replace mode is for kiosk/shared computer scenarios.

**Exam Tip 6:** `Invoke-GPUpdate -Computer <name> -Force` is the remote equivalent of `gpupdate /force`. Know this cmdlet — it is the answer whenever a scenario asks to remotely refresh Group Policy on multiple machines.

---

### [SEGMENT 10 — Lab Preview]

**[SHOW SCREEN: Lab 05 instructions document]**

This week's lab builds on the user and group structure from Module 04. You will create and link three GPOs in the `corp.local` domain: a domain-wide password policy GPO, an IT OU security baseline GPO with Security Filtering, and a Kiosk GPO with Loopback Processing enabled.

After creating each GPO, you will run `gpresult /r` to verify application and generate an HTML RSoP report. Your deliverables are screenshots of the GPMC showing all three GPOs linked, and the `gpresult /r` output confirming the expected GPO is applied.

---

### [SEGMENT 11 — Module 05 Summary]

**[SHOW SCREEN: Summary slide]**

Group Policy is the central configuration management mechanism in every Windows domain. GPOs consist of a GPC in AD and a GPT in SYSVOL. LSDOU processing order determines which policy wins when settings conflict. Enforced and Block Inheritance modify inheritance. Computer vs. User Configuration determines when policies apply. Security Filtering and WMI Filters target policies to specific groups or machine conditions. Loopback Processing handles shared computer scenarios.

Module 06 moves to infrastructure roles — DNS and DHCP — the network services that Active Directory depends on. See you there.

---

### Additional Resources

- [Group Policy overview](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11))
- [gpresult command reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult)
- [Invoke-GPUpdate cmdlet reference](https://learn.microsoft.com/en-us/powershell/module/grouppolicy/invoke-gpupdate)
- [Loopback Processing](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/loopback-processing-of-group-policy)

---

*End of Part 2. Proceed to the Reading Guide, Lab, Quiz, and Discussion for Module 05.*
