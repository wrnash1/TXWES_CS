# Video Script: Module 01 - Windows Server Installation and Editions (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 01 - Windows Server Installation and Editions

**Part:** 2 of 2 — Demonstrations, PowerShell Commands, Exam Tips, and Lab Preview

**Estimated Duration:** 11 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Recap and Part 2 Overview]

Welcome back. In Part 1, we covered the Windows Server edition model, the Server Core versus Desktop Experience decision, post-installation configuration requirements, and activation. In Part 2, I am going to demonstrate these concepts hands-on — we will walk through sconfig on Server Core, set a static IP address with PowerShell, and I will close with targeted exam tips and a preview of this week's lab.

---

### [SEGMENT 2 — Live Demo: Booting into Server Core]

**[SHOW SCREEN: VirtualBox VM running Windows Server 2022 Standard Core — black console with Administrator login prompt]**

[Alt-text: A VirtualBox virtual machine window showing the Windows Server Core login prompt on a black console screen with no graphical elements.]

Here I have a freshly installed Windows Server 2022 Standard Core VM in VirtualBox. Notice what you do not see: no taskbar, no Start menu, no desktop icons. Just a command prompt after login. This is your entire working environment on Server Core.

The first thing I always do on a fresh Server Core install is type `sconfig` and press Enter.

**[SHOW SCREEN: sconfig numbered menu]**

[Alt-text: The sconfig menu with numbered options: 1 Domain/Workgroup, 2 Computer Name, 3 Add Local Administrator, 4 Configure Remote Management, 5 Windows Update Settings, 6 Download and Install Updates, 7 Remote Desktop, 8 Network Settings, 9 Date and Time, 10 Telemetry Settings, 11 Windows Activation, 12 Log Off User, 13 Restart Server, 14 Shut Down Server, 15 Exit to Command Line.]

The menu gives us 15 options. For first-boot configuration we care about options 2, 7, and 8 in that order.

I will press 2 to change the computer name. It prompts for a new name. I type `SRV-CORE-01` and press Enter. It asks whether to restart now — I choose Yes. The server reboots and comes back with the new name.

After reboot I type `sconfig` again and press 8 for Network Settings. It lists all network adapters. I select adapter index 1. Then I press 1 to set the network adapter address. I choose S for Static, enter the IP address `192.168.10.10`, subnet mask `255.255.255.0`, and default gateway `192.168.10.1`. Back at the adapter menu, I press 2 to set DNS servers and enter `192.168.10.1`.

That covers the sconfig workflow. Fast and effective for interactive first-boot setup.

---

### [SEGMENT 3 — Live Demo: PowerShell First-Boot Configuration]

**[SHOW SCREEN: PowerShell console on Server Core]**

[Alt-text: A Windows Server Core PowerShell console showing command input and output for network configuration cmdlets.]

Now let me show the equivalent PowerShell approach — this is what you would use in an automated deployment script.

From the Server Core command prompt, type `powershell` and press Enter to launch a PowerShell session.

```powershell
# Step 1: Rename the computer
Rename-Computer -NewName "SRV-CORE-01" -Restart
```

After the reboot, log back in and open PowerShell again.

```powershell
# Step 2: Identify the network adapter name
Get-NetAdapter
```

This lists all adapters with their names and statuses. Note the name in the first column — typically "Ethernet" or "Ethernet0."

```powershell
# Step 3: Assign a static IP address
New-NetIPAddress `
    -InterfaceAlias "Ethernet" `
    -IPAddress "192.168.10.10" `
    -PrefixLength 24 `
    -DefaultGateway "192.168.10.1"

# Step 4: Set the DNS server
Set-DnsClientServerAddress `
    -InterfaceAlias "Ethernet" `
    -ServerAddresses "192.168.10.1"

# Step 5: Verify the configuration
Get-NetIPAddress -InterfaceAlias "Ethernet"
Get-DnsClientServerAddress -InterfaceAlias "Ethernet"
```

**[SHOW SCREEN: Output of Get-NetIPAddress showing the assigned static IP]**

[Alt-text: PowerShell console output showing the assigned IP address 192.168.10.10 with prefix length 24 on the Ethernet interface.]

You can see the static IP is now assigned. The `Get-DnsClientServerAddress` output shows the DNS server is set correctly.

```powershell
# Step 6: Enable Remote Management (already on by default on domain-joined servers,
#          but explicit on workgroup servers)
Enable-PSRemoting -Force

# Step 7: Enable Remote Desktop
Set-ItemProperty `
    -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" `
    -Name "fDenyTSConnections" `
    -Value 0

Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
```

Those two blocks enable PowerShell remoting and Remote Desktop respectively. With these in place, you can manage this server entirely from a remote Windows Admin Center instance or from another PowerShell session using `Enter-PSSession`.

---

### [SEGMENT 4 — Demo: Joining a Domain from PowerShell]

**[SHOW SCREEN: PowerShell console — Add-Computer command]**

[Alt-text: PowerShell console showing the Add-Computer cmdlet with domain name and credential parameters.]

```powershell
# Join the server to a domain
Add-Computer `
    -DomainName "corp.local" `
    -Credential (Get-Credential) `
    -OUPath "OU=Servers,DC=corp,DC=local" `
    -Restart
```

When you run this, a credential dialog appears. Enter a domain administrator account. The server joins the domain, moves the computer object to the specified OU, and reboots. After reboot it is domain-joined and visible in Active Directory Users and Computers.

The `-OUPath` parameter is optional — without it the computer account lands in the default Computers container. Best practice is always to specify the OU so the computer object is placed correctly from the start.

---

### [SEGMENT 5 — Demo: Server Manager on Desktop Experience]

**[SHOW SCREEN: Server Manager — Dashboard view on Desktop Experience]**

[Alt-text: Server Manager dashboard showing the Welcome tile, role summary panels for AD DS and DNS, and the Manage menu in the top right corner.]

On a Desktop Experience installation, Server Manager opens automatically at login. The Dashboard shows a summary of installed roles, recent events, and performance alerts.

The Manage menu in the top right gives you Add Roles and Features — which is how you install server roles on a Desktop Experience server. We will use Add Roles and Features extensively in later modules to install Active Directory Domain Services, DNS, DHCP, and other roles.

The Local Server tile in the left panel shows your computer name, IP address, domain membership, and key settings like Remote Desktop status and Windows Firewall state. This is your quick-reference panel after first boot.

---

### [SEGMENT 6 — Exam Tips]

**[SHOW SCREEN: Slide listing 6 exam tips for Module 01]**

Here are the six most important exam tips for Module 01 topics.

**Exam Tip 1:** When the scenario says "smallest attack surface" or "fewest components requiring patches," the answer is Server Core. Never Nano Server for traditional roles.

**Exam Tip 2:** `sconfig` is the interactive first-boot tool for Server Core. PowerShell cmdlets `Rename-Computer`, `New-NetIPAddress`, and `Set-DnsClientServerAddress` are the scriptable equivalents.

**Exam Tip 3:** Standard edition allows two VMs per license. Datacenter allows unlimited. If a scenario mentions running eight or more VMs on one host, Datacenter is more cost-effective.

**Exam Tip 4:** KMS requires a minimum of five servers requesting activation before the KMS host begins issuing activations. MAK is for isolated machines and has a finite activation pool.

**Exam Tip 5:** You can upgrade Standard to Datacenter in-place using `DISM /online /Set-Edition`. Downgrade requires a reinstall. This is a common exam distractor.

**Exam Tip 6:** Windows Admin Center communicates over WinRM (ports 5985 and 5986). It requires no agent on managed nodes. It is deployed on-premises, not in Azure.

---

### [SEGMENT 7 — Lab Preview]

**[SHOW SCREEN: Lab instructions document for Module 01]**

This week's lab has two parts.

In Part 1, you will deploy a Windows Server 2022 Standard Core VM in VirtualBox using the Evaluation ISO, then use sconfig to set the hostname to `SRV-CORE-01` and configure a static IP address of `192.168.10.10/24`.

In Part 2, you will open PowerShell and verify your configuration using `Get-NetIPAddress` and `Get-DnsClientServerAddress`. Then you will enable Remote Desktop using the PowerShell commands I demonstrated.

Your deliverable is a screenshot of the sconfig screen showing your hostname and IP address, and a screenshot of your PowerShell verification output. Both screenshots go into Canvas before the due date.

The lab builds the server instance that we will continue to configure in Module 02 when we begin Active Directory Domain Services installation.

---

### [SEGMENT 8 — Module 01 Summary]

**[SHOW SCREEN: Summary slide listing key takeaways]**

Let us close with the key takeaways from Module 01.

Windows Server 2022 comes in Standard, Datacenter, and Essentials editions. Standard and Datacenter are the editions relevant to this course and the AZ-800 exam. Edition choice determines VM licensing and advanced feature availability.

Server Core omits the GUI, reduces attack surface, uses less RAM, and requires fewer reboots. Desktop Experience provides the full graphical shell for administrators who need it.

Post-installation configuration requires a hostname, static IP, DNS configuration, and domain membership. Use sconfig for interactive Server Core setup; use PowerShell cmdlets for scripted or automated deployments.

Activation uses KMS for enterprise environments and MAK for isolated deployments.

In Module 02, we will build on this foundation and introduce the architecture of Active Directory Domain Services. I will see you there. Take care.

---

### Additional Resources

- [Configure a Server Core installation](https://learn.microsoft.com/en-us/windows-server/administration/server-core/server-core-administration)
- [sconfig command reference](https://learn.microsoft.com/en-us/windows-server/administration/server-core/server-core-sconfig)
- [New-NetIPAddress cmdlet reference](https://learn.microsoft.com/en-us/powershell/module/nettcpip/new-netipaddress)
- [Windows Admin Center deployment](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/deploy/install)

---

*End of Part 2. Proceed to the Reading Guide, Lab, Quiz, and Discussion for Module 01.*
