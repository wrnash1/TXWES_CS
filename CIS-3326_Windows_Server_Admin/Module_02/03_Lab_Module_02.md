# Lab Activity: Module 02 - Active Directory Domain Services Overview

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Lab Overview

In this lab you will install the AD DS role on the Windows Server Core VM from Module 01, promote it to a Domain Controller for a new forest, and then explore the resulting directory structure using both PowerShell cmdlets and Active Directory Users and Computers. This lab creates the domain environment that all subsequent module labs will build upon.

**Estimated Time:** 75-90 minutes

**Prerequisites:**

- Module 01 lab complete: VM named `SRV-CORE-01` with static IP `192.168.10.10/24`
- PowerShell remoting enabled on the VM

**Learning Objectives:**

- Install the AD DS server role using PowerShell
- Promote a server to a Domain Controller using `Install-ADDSForest`
- Explore the default OU and container structure post-promotion
- Query FSMO role holders using PowerShell and netdom
- Verify domain health using `Get-ADDomain` and `dcdiag`

---

### Part 1 — Install the AD DS Role

#### Step 1.1 — Open PowerShell on SRV-CORE-01

Log in to the server. At the command prompt, type `powershell` and press Enter.

#### Step 1.2 — Install AD Domain Services

```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools -Verbose
```

The `-IncludeManagementTools` switch installs the AD DS management tools including the PowerShell AD module (RSAT-AD-PowerShell) and the command-line tools. The `-Verbose` switch shows detailed progress output.

**[SHOW SCREEN: PowerShell output showing feature installation progress and Success: True confirmation]**

Installation takes several minutes. When complete, you should see `Success : True` in the output. Do not reboot yet — the server is not yet a Domain Controller.

#### Step 1.3 — Verify the Feature is Installed

```powershell
Get-WindowsFeature -Name AD-Domain-Services
```

The output should show `Install State: Installed` for the AD-Domain-Services feature.

---

### Part 2 — Promote the Server to Domain Controller

#### Step 2.1 — Create a New Forest

Run the following command to promote the server and create a new forest. You will be prompted for the Safe Mode Administrator Password (DSRM password):

```powershell
Install-ADDSForest `
    -DomainName "corp.local" `
    -DomainNetBIOSName "CORP" `
    -ForestMode "WinThreshold" `
    -DomainMode "WinThreshold" `
    -InstallDns `
    -Force
```

Parameter explanations:

- `-DomainName "corp.local"` — the fully qualified DNS name of the new forest root domain
- `-DomainNetBIOSName "CORP"` — the legacy NetBIOS name (15 characters max, no dots)
- `-ForestMode "WinThreshold"` — sets forest functional level to Windows Server 2016+
- `-DomainMode "WinThreshold"` — sets domain functional level to Windows Server 2016+
- `-InstallDns` — installs and configures the DNS Server role automatically
- `-Force` — suppresses confirmation prompts

#### Step 2.2 — Set the DSRM Password

When prompted for `SafeModeAdministratorPassword`, enter a strong password. This password is used to log in to Directory Services Restore Mode — a special boot mode for AD DS recovery. Record this password securely; losing it can make domain recovery impossible.

#### Step 2.3 — Wait for Reboot

The server will automatically restart after promotion is complete. After the reboot, log in using `CORP\Administrator` (domain administrator). Notice that your logon prompt now includes the domain prefix.

---

### Part 3 — Explore the Domain with PowerShell

#### Step 3.1 — Query Domain Information

```powershell
Get-ADDomain
```

Review the output. Note these fields:

- `DNSRoot` — should show `corp.local`
- `NetBIOSName` — should show `CORP`
- `DomainMode` — functional level
- `PDCEmulator` — which DC holds the PDC Emulator role
- `RIDMaster` — which DC holds the RID Master role
- `InfrastructureMaster` — which DC holds the Infrastructure Master role

#### Step 3.2 — Query Forest Information

```powershell
Get-ADForest
```

Note the `SchemaMaster` and `DomainNamingMaster` fields.

#### Step 3.3 — Query All FSMO Roles

```powershell
netdom query fsmo
```

All five FSMO roles should list your Domain Controller (`SRV-CORE-01.corp.local`).

#### Step 3.4 — List All Domain Controllers

```powershell
Get-ADDomainController -Filter *
```

You should see one DC — `SRV-CORE-01` — with `IsGlobalCatalog: True`.

#### Step 3.5 — Run a Domain Health Check

```powershell
dcdiag /v
```

`dcdiag` runs a suite of diagnostic tests against the Domain Controller. Look for `passed test` entries. In a fresh single-DC lab, all tests should pass. Any failures should be investigated before proceeding to subsequent labs.

---

### Part 4 — Explore Using Active Directory Users and Computers

If you have RSAT tools installed on a Windows 10/11 workstation joined to corp.local, open Active Directory Users and Computers from Administrative Tools. Alternatively, if you installed a Desktop Experience VM for lab purposes, open it from Server Manager Tools.

#### Step 4.1 — View Default Containers

Expand the `corp.local` domain. Identify and record the purpose of each default container:

- Builtin
- Computers
- Domain Controllers
- ForeignSecurityPrincipals
- Users

#### Step 4.2 — Create the Department OU Structure

Right-click `corp.local`, choose New, then Organizational Unit. Create the following OU hierarchy:

- `Departments` (top-level OU)
  - `HR` (child of Departments)
  - `IT` (child of Departments)
  - `Finance` (child of Departments)
- `Servers` (top-level OU)
- `Workstations` (top-level OU)

Leave "Protect container from accidental deletion" enabled on all OUs.

#### Step 4.3 — Verify OU Creation with PowerShell

```powershell
Get-ADOrganizationalUnit -Filter * | Select-Object Name, DistinguishedName
```

Confirm all OUs you created appear in the output with the correct Distinguished Names.

---

### Part 5 — Optional Challenge: Move the Server Computer Account

Move the `SRV-CORE-01` computer account from the Domain Controllers OU to a new OU named `DomainControllers_Prod` to practice object movement.

```powershell
# First, create the new OU
New-ADOrganizationalUnit -Name "DomainControllers_Prod" `
    -Path "DC=corp,DC=local" `
    -ProtectedFromAccidentalDeletion $true

# View the current computer account DN
Get-ADComputer -Identity "SRV-CORE-01" | Select-Object DistinguishedName

# Note: Moving a DC computer account requires caution in production
# In this lab, observe but do not move the DC account to avoid breaking GPO inheritance
```

---

### Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1 — AD DS role installation:** PowerShell output showing `Install-WindowsFeature` completing with `Success : True`.

**Screenshot 2 — Get-ADDomain output:** Full output of `Get-ADDomain` showing domain name, FSMO role holders, and functional level.

**Screenshot 3 — netdom query fsmo:** Output listing all five FSMO roles assigned to your DC.

**Screenshot 4 — OU structure:** Output of `Get-ADOrganizationalUnit -Filter *` showing the Departments, HR, IT, Finance, Servers, and Workstations OUs.

---

### Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| AD DS role installed successfully | 15 | Feature install screenshot shows Success: True |
| Domain corp.local created | 20 | Get-ADDomain shows DNSRoot: corp.local |
| All 5 FSMO roles on DC | 20 | netdom query fsmo screenshot |
| OU hierarchy created correctly | 25 | Get-ADOrganizationalUnit output shows all 6 OUs |
| dcdiag passes all tests | 20 | No failed tests in dcdiag /v output |

---

### Troubleshooting Notes

If `Install-ADDSForest` fails with a DNS prerequisite error, verify that the network adapter's DNS is set to `127.0.0.1` or the server's own IP before promoting.

```powershell
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "127.0.0.1"
```

If the DSRM password prompt does not appear interactively (common on Server Core), provide it as a secure string parameter:

```powershell
$password = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force
Install-ADDSForest -DomainName "corp.local" -SafeModeAdministratorPassword $password `
    -InstallDns -Force
```
