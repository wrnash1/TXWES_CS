# Lab Activity: Module 06 - DNS and DHCP Server Roles

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Lab Overview

In this lab you will install and configure both the DNS and DHCP Server roles on DC1. You will create a DHCP scope for the `192.168.10.0/24` network, configure scope options, add an exclusion range, create a MAC-based reservation, verify DNS zone configuration, and enable DNS aging on the `corp.local` zone.

**Estimated Time:** 75-90 minutes

**Prerequisites:**

- Module 05 lab complete: corp.local domain is running on DC1 with the OU structure in place
- DC1 is reachable at `192.168.10.10`
- PowerShell running as Domain Administrator

**Learning Objectives:**

- Install DNS and DHCP roles using PowerShell
- Authorize a DHCP server in Active Directory
- Create and configure a DHCP scope with exclusion range and scope options
- Create a DHCP reservation by MAC address
- Configure DHCP Failover in Hot Standby mode (conceptual — single-server lab)
- Verify DNS zone type and dynamic update settings
- Enable DNS aging and scavenging on the corp.local zone
- Use PowerShell to verify all configurations

---

### Part 1 — Install DNS and DHCP Roles

#### Step 1.1 — Verify DNS Role

DNS is typically installed automatically when AD DS is promoted. Verify it is present before installing DHCP.

```powershell
# Check current installation state for both roles
Get-WindowsFeature -Name DNS, DHCP | Select-Object Name, InstallState
```

If DNS shows `InstallState: Installed`, proceed to Step 1.2. If not:

```powershell
Install-WindowsFeature -Name DNS -IncludeManagementTools
```

#### Step 1.2 — Install DHCP Role

```powershell
# Install DHCP Server role with management tools
Install-WindowsFeature -Name DHCP -IncludeManagementTools

# Confirm installation completed
Get-WindowsFeature -Name DHCP | Select-Object Name, InstallState
```

Both roles should show `InstallState: Installed`.

#### Step 1.3 — Post-Install DHCP Security Groups

After installing DHCP, create the default security groups in AD:

```powershell
# Add DHCP security groups to Active Directory
Add-DhcpServerSecurityGroup

# Notify Server Manager that DHCP post-install is complete
Set-ItemProperty `
    -Path "HKLM:\SOFTWARE\Microsoft\ServerManager\Roles\12" `
    -Name "ConfigurationState" `
    -Value 2
```

Take **Screenshot 1** — PowerShell output showing `InstallState: Installed` for both DNS and DHCP.

---

### Part 2 — Authorize DHCP Server in Active Directory

#### Step 2.1 — Authorize the DHCP Server

```powershell
# Authorize DC1 as a DHCP server in Active Directory
Add-DhcpServerInDC -DnsName "DC1.corp.local" -IPAddress 192.168.10.10

# Verify the server appears in the authorized list
Get-DhcpServerInDC
```

The output should show `DnsName: DC1.corp.local` with `IPAddress: 192.168.10.10`.

Take **Screenshot 2** — `Get-DhcpServerInDC` output confirming authorization.

---

### Part 3 — Create and Configure a DHCP Scope

#### Step 3.1 — Create the Scope

```powershell
# Create a DHCP scope for the 192.168.10.0/24 network
Add-DhcpServerv4Scope `
    -Name "CorpNetwork" `
    -StartRange 192.168.10.100 `
    -EndRange 192.168.10.200 `
    -SubnetMask 255.255.255.0 `
    -Description "Main office client scope" `
    -State Active
```

#### Step 3.2 — Add an Exclusion Range

Addresses `.100` through `.110` will be reserved for statically configured infrastructure devices (switches, APs, printers with static IPs).

```powershell
# Exclude addresses already in use by static devices
Add-DhcpServerv4ExclusionRange `
    -ScopeId 192.168.10.0 `
    -StartRange 192.168.10.100 `
    -EndRange 192.168.10.110
```

#### Step 3.3 — Configure Scope Options

```powershell
# Set gateway, DNS servers, and domain suffix for the scope
Set-DhcpServerv4OptionValue `
    -ScopeId 192.168.10.0 `
    -Router 192.168.10.1 `
    -DnsServer 192.168.10.10, 192.168.10.20 `
    -DnsDomain "corp.local"
```

#### Step 3.4 — Verify Scope Configuration

```powershell
# Verify scope summary
Get-DhcpServerv4Scope | Select-Object Name, ScopeId, StartRange, EndRange, SubnetMask, State

# Verify exclusion range
Get-DhcpServerv4ExclusionRange -ScopeId 192.168.10.0

# Verify scope options
Get-DhcpServerv4OptionValue -ScopeId 192.168.10.0
```

Take **Screenshot 3** — DHCP Manager showing the CorpNetwork scope with Address Pool, Exclusions visible in the console tree.

---

### Part 4 — Create a DHCP Reservation

A network printer on floor 3 has MAC address `00-50-56-AB-12-34` and needs a consistent IP address.

#### Step 4.1 — Add the Reservation

```powershell
# Create a reservation for the floor 3 printer
Add-DhcpServerv4Reservation `
    -ScopeId 192.168.10.0 `
    -IPAddress 192.168.10.115 `
    -ClientId "00-50-56-AB-12-34" `
    -Description "Floor3 HP LaserJet"

# Verify the reservation
Get-DhcpServerv4Reservation -ScopeId 192.168.10.0
```

Take **Screenshot 4** — `Get-DhcpServerv4Reservation` output showing the printer reservation.

---

### Part 5 — Verify DNS Configuration

#### Step 5.1 — Check Zone Type and Dynamic Updates

```powershell
# List all DNS zones with type and update settings
Get-DnsServerZone | Select-Object ZoneName, ZoneType, DynamicUpdate, ReplicationScope
```

Verify that `corp.local` shows:

- `ZoneType: Primary`
- `DynamicUpdate: Secure`
- `ReplicationScope: Forest` (or Domain)

If DynamicUpdate shows `NonsecureAndSecure`, correct it:

```powershell
# Set Secure Only dynamic updates
Set-DnsServerPrimaryZone -Name "corp.local" -DynamicUpdate Secure
```

#### Step 5.2 — Add a Static DNS A Record

```powershell
# Add an A record for a test application server
Add-DnsServerResourceRecordA `
    -ZoneName "corp.local" `
    -Name "appserver" `
    -IPv4Address "192.168.10.50"

# Verify the record was created
Resolve-DnsName -Name "appserver.corp.local" -Type A
```

#### Step 5.3 — Test Reverse Lookup

```powershell
# Create the reverse lookup zone if it does not exist
Add-DnsServerPrimaryZone `
    -NetworkId "192.168.10.0/24" `
    -ReplicationScope Forest

# Test reverse lookup for DC1
Resolve-DnsName -Name "192.168.10.10" -Type PTR
```

Take **Screenshot 5** — `Get-DnsServerZone` output showing corp.local with Secure dynamic updates.

---

### Part 6 — Enable DNS Aging and Scavenging

#### Step 6.1 — Enable Aging on the Zone

```powershell
# Enable aging on the corp.local zone with default intervals
Set-DnsServerZoneAging -Name "corp.local" -Aging $true `
    -NoRefreshInterval 7.00:00:00 `
    -RefreshInterval 7.00:00:00

# Verify aging settings
Get-DnsServerZoneAging -Name "corp.local"
```

#### Step 6.2 — Enable Scavenging on the Server

```powershell
# Enable automatic scavenging on the DNS server
Set-DnsServerScavenging -ScavengingState $true -ScavengingInterval 7.00:00:00

# Trigger a manual scavenging pass
Start-DnsServerScavenging

# Verify server scavenging settings
Get-DnsServerScavenging
```

Take **Screenshot 6** — `Get-DnsServerZoneAging` output confirming aging is enabled on corp.local.

---

### Part 7 — PowerShell Summary Verification

Run a final verification to confirm all configurations are in place.

```powershell
# DHCP summary
Write-Host "=== DHCP Authorization ===" -ForegroundColor Cyan
Get-DhcpServerInDC

Write-Host "=== DHCP Scopes ===" -ForegroundColor Cyan
Get-DhcpServerv4Scope | Select-Object Name, ScopeId, StartRange, EndRange, State

Write-Host "=== DHCP Exclusions ===" -ForegroundColor Cyan
Get-DhcpServerv4ExclusionRange -ScopeId 192.168.10.0

Write-Host "=== DHCP Reservations ===" -ForegroundColor Cyan
Get-DhcpServerv4Reservation -ScopeId 192.168.10.0

Write-Host "=== DNS Zones ===" -ForegroundColor Cyan
Get-DnsServerZone | Select-Object ZoneName, ZoneType, DynamicUpdate

Write-Host "=== DNS Aging (corp.local) ===" -ForegroundColor Cyan
Get-DnsServerZoneAging -Name "corp.local"
```

Take **Screenshot 7** — The full PowerShell summary output showing all configured components.

---

### Optional Challenge: Configure DHCP Failover (Conceptual)

In a multi-server lab environment, this command configures Hot Standby failover between two DHCP servers. Read through the command and understand each parameter.

```powershell
# Requires a second DC/DHCP server (SRV-CORE-02.corp.local)
Add-DhcpServerv4Failover `
    -Name "Corp-DHCP-Failover" `
    -PartnerServer "SRV-CORE-02.corp.local" `
    -ScopeId 192.168.10.0 `
    -Mode HotStandby `
    -SharedSecret "DHCPSharedSecret123!" `
    -AutoStateTransition $true `
    -MaxClientLeadTime 1:00:00

# Verify failover configuration
Get-DhcpServerv4Failover
```

Identify which parameter sets the authentication key between the two DHCP servers, and which parameter determines how long the standby server waits before taking over. Be prepared to answer this on the quiz.

---

### Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1 — Role installation:** PowerShell output showing `InstallState: Installed` for DNS and DHCP.

**Screenshot 2 — DHCP authorization:** `Get-DhcpServerInDC` output showing DC1.corp.local as authorized.

**Screenshot 3 — DHCP scope in DHCP Manager:** DHCP Manager console tree showing the CorpNetwork scope with Address Pool and Exclusions visible.

**Screenshot 4 — Reservation:** `Get-DhcpServerv4Reservation` output showing the Floor3 HP LaserJet reservation.

**Screenshot 5 — DNS zone verification:** `Get-DnsServerZone` output showing corp.local with Secure dynamic updates.

**Screenshot 6 — DNS aging:** `Get-DnsServerZoneAging` output showing aging enabled on corp.local.

**Screenshot 7 — PowerShell summary:** Full summary output from Part 7 showing all DHCP and DNS configurations.

---

### Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| DHCP role installed and authorized | 15 | Screenshots 1 and 2 show installed state and authorized server |
| DHCP scope created with exclusion and scope options | 25 | Screenshot 3 shows scope in DHCP Manager with correct range |
| DHCP reservation created | 15 | Screenshot 4 shows MAC-to-IP reservation |
| DNS zone verified with Secure dynamic updates | 20 | Screenshot 5 shows corp.local zone with correct update setting |
| DNS aging enabled on corp.local zone | 10 | Screenshot 6 shows aging enabled with correct intervals |
| PowerShell summary output | 15 | Screenshot 7 shows all configurations present and correct |

---

### Troubleshooting Notes

If `Add-DhcpServerInDC` returns "Access Denied," verify you are running PowerShell as a Domain Administrator account (not a local admin).

If `Get-DnsServerZone` is not recognized, verify the DNS Server role is installed and import the module:

```powershell
Import-Module DnsServer
```

If `Resolve-DnsName` returns "Server failed," verify the DNS client on DC1 points to `127.0.0.1` or `192.168.10.10` as its DNS server:

```powershell
Get-DnsClientServerAddress -InterfaceAlias "Ethernet"
```

If the reverse lookup PTR record test fails, verify the `10.168.192.in-addr.arpa` reverse zone was created in Step 5.3.

---

## Part 9 — Challenge Exercise

### Challenge 1: Configure a Conditional Forwarder and Test Resolution

Conditional forwarders route DNS queries for specific domains to designated servers. Practice creating one and verifying resolution behavior.

1. Create a conditional forwarder for the fictional partner domain `partner.local` pointing to `8.8.8.8` (using a public DNS server as a stand-in for a partner DNS server):

   ```powershell
   Add-DnsServerConditionalForwarderZone `
       -Name "partner.local" `
       -MasterServers 8.8.8.8 `
       -ReplicationScope Forest
   ```

2. Verify the conditional forwarder was created:

   ```powershell
   Get-DnsServerZone | Where-Object { $_.ZoneName -eq "partner.local" }
   ```

3. Test how the DNS server handles a query for `partner.local` (the query will fail to resolve since `8.8.8.8` doesn't know about `partner.local`, but you should see the forwarding attempt in DNS debug logging):

   ```powershell
   Resolve-DnsName -Name "anyhost.partner.local" -Server 127.0.0.1
   ```

4. Enable DNS debug logging to capture the forwarded query attempt, then disable it after reviewing the log:

   ```powershell
   Set-DnsServerDiagnostics -All $true
   # Re-run the Resolve-DnsName command above
   # View the DNS debug log:
   Get-Content "C:\Windows\System32\dns\dns.log" | Select-Object -Last 20
   Set-DnsServerDiagnostics -All $false
   ```

   Document in your notes: what IP address did the debug log show the query being forwarded to?

### Challenge 2: Analyze DHCP Lease Database and Test Scope Exhaustion

Understanding the DHCP lease database and what happens when a scope is exhausted is critical for production troubleshooting.

1. View all active leases in the `192.168.10.0` scope and count how many are in use:

   ```powershell
   $leases = Get-DhcpServerv4Lease -ScopeId 192.168.10.0
   $leases | Select-Object IPAddress, HostName, ClientId, LeaseExpiryTime
   Write-Host "Total active leases: $($leases.Count)"
   ```

2. View the scope statistics to see how many addresses are available vs. in use:

   ```powershell
   Get-DhcpServerv4ScopeStatistics -ScopeId 192.168.10.0
   ```

3. Calculate the maximum capacity of your scope. Based on the Start Range and End Range configured in Part 2 of this lab (minus the exclusion range), determine: how many addresses could potentially be leased? Show the calculation in your lab notes.

4. Examine the DHCP audit log to see recent lease activity:

   ```powershell
   $logPath = "C:\Windows\System32\dhcp"
   $today = Get-Date -Format "ddd"
   Get-Content "$logPath\DhcpSrvLog-$today.log" | Select-Object -Last 30
   ```

   Identify the event ID code for a lease being granted (hint: look for ID 10 in the log format). Document what event ID 11 represents.

### Reflection Questions

1. Your conditional forwarder for `partner.local` sends queries to `8.8.8.8`. In a real enterprise scenario, you would point this at the partner company's actual DNS server. Explain why a conditional forwarder is more secure than simply listing the partner DNS server as a second general forwarder — consider what would happen to your other external DNS queries.
2. DHCP scope exhaustion causes new clients to receive APIPA addresses and lose network connectivity. Describe two proactive monitoring approaches an administrator should implement to detect a scope approaching exhaustion before it becomes critical. Name any specific Windows Server tool or PowerShell cmdlet that would provide this alert.
