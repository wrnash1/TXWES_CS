# Lab Activity: Module 01 - Windows Server Installation and Editions

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Lab Overview

In this lab you will deploy a Windows Server 2022 Standard Core virtual machine, perform all required first-boot configuration tasks using both the `sconfig` utility and PowerShell, verify your configuration, and enable remote management. This server will be reused and extended in subsequent module labs, so accurate configuration now is important.

**Estimated Time:** 60-90 minutes

**Prerequisites:**

- VirtualBox 7.x or later installed on your workstation
- Windows Server 2022 Evaluation ISO downloaded from Microsoft Evaluation Center
- At least 4 GB RAM allocated to the VM, 60 GB dynamic disk, one NAT or Host-Only network adapter

**Learning Objectives:**

- Install Windows Server 2022 Standard Core from ISO
- Use sconfig to configure hostname and static IP
- Use PowerShell to verify and extend network configuration
- Enable PowerShell remoting and Remote Desktop
- Document configuration with screenshots

---

### Part 1 — Install Windows Server 2022 Standard Core

#### Step 1.1 — Create the Virtual Machine

Open VirtualBox and click New. Configure the VM with these settings:

- Name: `WS2022-CORE-01`
- Type: Microsoft Windows
- Version: Windows 2022 (64-bit)
- RAM: 2048 MB minimum (4096 MB recommended)
- Hard Disk: Create a new virtual hard disk, VDI, dynamically allocated, 60 GB

#### Step 1.2 — Attach the ISO

In the VM Settings, go to Storage. Under the IDE controller, click the empty optical drive and attach your Windows Server 2022 Evaluation ISO.

#### Step 1.3 — Run Setup

Start the VM and boot from the ISO. Work through the Windows Server setup wizard:

1. Select language, time, and keyboard — click Next
2. Click Install Now
3. On the edition selection screen, choose **Windows Server 2022 Standard (Server Core)** — do NOT select Desktop Experience
4. Accept the license terms
5. Choose Custom: Install Windows only (advanced)
6. Select the unallocated disk space and click Next
7. Wait for setup to complete and the server to reboot automatically

#### Step 1.4 — Set the Administrator Password

After the final reboot, the console prompts you to set the Administrator password. Use a strong password you will remember throughout this course (minimum 12 characters, uppercase, lowercase, number, symbol). Press Enter to confirm.

You will be logged in to a command prompt. This sparse black console is the Server Core environment.

---

### Part 2 — First-Boot Configuration with sconfig

#### Step 2.1 — Launch sconfig

At the command prompt, type:

```cmd
sconfig
```

Press Enter. The sconfig numbered menu appears.

#### Step 2.2 — Change the Computer Name

Press `2` and Enter to select Computer Name. When prompted, type:

```text
SRV-CORE-01
```

Press Enter. When asked to restart, press `Y`. The server reboots.

Log back in with the Administrator password after reboot.

#### Step 2.3 — Configure a Static IP Address

Type `sconfig` again and press Enter.

Press `8` to open Network Settings. The adapter list appears. Press `1` to select the first adapter (index 1).

Press `1` again to set the network adapter address. Choose `S` for Static.

Enter the following values when prompted:

- IP Address: `192.168.10.10`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.10.1`

Press Enter after each value.

#### Step 2.4 — Configure DNS

Still in the adapter submenu, press `2` to set DNS servers.

Enter the DNS server address: `192.168.10.1`

Press Enter. Type `4` to return to the main sconfig menu, then `15` to exit to the command line.

---

### Part 3 — Verification and Extended Configuration with PowerShell

#### Step 3.1 — Open PowerShell

At the command prompt, type:

```cmd
powershell
```

Press Enter. Your prompt changes to `PS C:\Users\Administrator>`.

#### Step 3.2 — Verify Hostname

```powershell
hostname
```

Expected output: `SRV-CORE-01`

#### Step 3.3 — Verify IP Configuration

```powershell
Get-NetIPAddress -InterfaceAlias "Ethernet" -AddressFamily IPv4
```

Expected output should show `IPAddress: 192.168.10.10` and `PrefixLength: 24`.

```powershell
Get-DnsClientServerAddress -InterfaceAlias "Ethernet"
```

Expected output should show `ServerAddresses: {192.168.10.1}`.

#### Step 3.4 — Enable PowerShell Remoting

```powershell
Enable-PSRemoting -Force
```

This enables the WinRM service and configures the firewall rule to accept incoming PowerShell remoting connections.

#### Step 3.5 — Enable Remote Desktop

```powershell
Set-ItemProperty `
    -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" `
    -Name "fDenyTSConnections" `
    -Value 0

Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
```

#### Step 3.6 — Verify Remote Desktop Registry Value

```powershell
Get-ItemProperty `
    -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" `
    -Name "fDenyTSConnections"
```

Expected output: `fDenyTSConnections : 0` (zero means Remote Desktop is enabled).

#### Step 3.7 — View System Information Summary

```powershell
Get-ComputerInfo | Select-Object CsName, OsName, OsVersion, WindowsProductName
```

This displays the computer name, OS name, version, and edition. Verify that the edition shows "Standard" and Core installation is confirmed by the absence of "Desktop Experience" in the product name.

---

### Part 4 — Optional Challenge: Join a Workgroup

If your lab environment does not include an Active Directory domain, join a named workgroup instead.

```powershell
Add-Computer -WorkgroupName "TXWES-LAB" -Restart
```

After the reboot, verify workgroup membership:

```powershell
(Get-WmiObject Win32_ComputerSystem).Workgroup
```

Expected output: `TXWES-LAB`

---

### Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1 — sconfig screen:** Take a screenshot of the sconfig main menu after configuration, showing the hostname `SRV-CORE-01` at the top of the menu display.

**Screenshot 2 — PowerShell IP verification:** Take a screenshot showing the output of `Get-NetIPAddress` and `Get-DnsClientServerAddress` confirming `192.168.10.10/24` and DNS `192.168.10.1`.

**Screenshot 3 — Remote Desktop registry value:** Take a screenshot showing the output of `Get-ItemProperty` confirming `fDenyTSConnections : 0`.

**Screenshot 4 — System information:** Take a screenshot of the `Get-ComputerInfo` output showing the computer name and edition.

---

### Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| VM deployed with Server Core (not Desktop Experience) | 15 | Screenshot shows command prompt only, no GUI |
| Hostname set to SRV-CORE-01 | 20 | sconfig menu header or hostname command output |
| Static IP 192.168.10.10/24 configured | 20 | Get-NetIPAddress output matches |
| DNS 192.168.10.1 configured | 15 | Get-DnsClientServerAddress output matches |
| Remote Desktop enabled (fDenyTSConnections = 0) | 15 | Registry value screenshot |
| System info screenshot showing Standard Core | 15 | Get-ComputerInfo output submitted |

---

### Troubleshooting Notes

If `New-NetIPAddress` returns an error about a conflicting IP, the DHCP-assigned address may still be present. Remove it first:

```powershell
Remove-NetIPAddress -InterfaceAlias "Ethernet" -Confirm:$false
New-NetIPAddress -InterfaceAlias "Ethernet" `
    -IPAddress "192.168.10.10" -PrefixLength 24 `
    -DefaultGateway "192.168.10.1"
```

If the adapter name is not "Ethernet," run `Get-NetAdapter` to find the correct name and substitute it in all commands.
