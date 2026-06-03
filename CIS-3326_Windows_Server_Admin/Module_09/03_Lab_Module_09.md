# Lab Activity: Module 09 — DNS and DHCP Services in Windows Server

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Lab Overview

In this lab you will install and configure DNS and DHCP on DC1, create an
AD-Integrated reverse lookup zone, add DNS records, configure a forwarder and
conditional forwarder, enable DNS scavenging, create a DHCP scope with exclusions
and reservations, configure scope options, and verify with PowerShell.

**Estimated Time:** 75-90 minutes

**Prerequisites:**

- Module 08 lab complete: DC1 is a domain controller for txwes.edu

- DNS is already installed on DC1 (installed with AD DS)

- DC1 IP address: 192.168.10.10

- PowerShell running as Domain Administrator

**Learning Objectives:**

- Verify and configure the AD-Integrated DNS zone

- Create a reverse lookup zone using `Add-DnsServerPrimaryZone`

- Add A, PTR, and CNAME records with DNS PowerShell cmdlets

- Configure a standard forwarder and conditional forwarder

- Enable DNS scavenging on the server and zone levels

- Install, authorize, and configure a DHCP scope

- Add exclusions, reservations, and scope options

---

## Part 1 — Verify and Configure the DNS Zone

### Step 1.1 — Verify the Existing Zone

```powershell
# View all DNS zones
Get-DnsServerZone | Select-Object ZoneName, ZoneType, IsDsIntegrated, DynamicUpdate

# Confirm txwes.edu is AD-integrated with Secure updates
Get-DnsServerZone -Name "txwes.edu" |
    Select-Object ZoneName, ZoneType, IsDsIntegrated, DynamicUpdate, ReplicationScope
```

The `txwes.edu` zone should show ZoneType: Primary, IsDsIntegrated: True,
DynamicUpdate: Secure.

### Step 1.2 — Create the Reverse Lookup Zone

```powershell
# Create a reverse lookup zone for the 192.168.10.0/24 subnet
Add-DnsServerPrimaryZone `
    -NetworkId "192.168.10.0/24" `
    -ReplicationScope Domain `
    -DynamicUpdate Secure

# Verify the reverse zone
Get-DnsServerZone -Name "10.168.192.in-addr.arpa" |
    Select-Object ZoneName, ZoneType, IsDsIntegrated, DynamicUpdate
```

Take **Screenshot 1** — `Get-DnsServerZone` showing both `txwes.edu` and
`10.168.192.in-addr.arpa` as AD-Integrated with Secure dynamic updates.

---

## Part 2 — Create and Manage DNS Records

### Step 2.1 — Add an A Record

```powershell
# Add an A record for a web server
Add-DnsServerResourceRecordA `
    -ZoneName "txwes.edu" `
    -Name "webserver" `
    -IPv4Address "192.168.10.20" `
    -TimeToLive (New-TimeSpan -Hours 1)

# Verify the A record
Get-DnsServerResourceRecord -ZoneName "txwes.edu" -RRType A |
    Select-Object HostName, RecordData
```

### Step 2.2 — Add a PTR Record

```powershell
# Add a PTR record for the web server in the reverse zone
Add-DnsServerResourceRecordPtr `
    -ZoneName "10.168.192.in-addr.arpa" `
    -Name "20" `
    -PtrDomainName "webserver.txwes.edu."

# Verify PTR record
Get-DnsServerResourceRecord -ZoneName "10.168.192.in-addr.arpa" -RRType Ptr |
    Select-Object HostName, RecordData
```

### Step 2.3 — Add a CNAME Record

```powershell
# Add a CNAME alias pointing www to webserver
Add-DnsServerResourceRecordCName `
    -ZoneName "txwes.edu" `
    -Name "www" `
    -HostNameAlias "webserver.txwes.edu."

# Verify CNAME
Get-DnsServerResourceRecord -ZoneName "txwes.edu" -RRType CName |
    Select-Object HostName, RecordData
```

### Step 2.4 — Test Resolution

```powershell
# Test forward resolution
Resolve-DnsName -Name "webserver.txwes.edu" -Server "192.168.10.10"
Resolve-DnsName -Name "www.txwes.edu" -Server "192.168.10.10"

# Test reverse resolution
Resolve-DnsName -Name "192.168.10.20" -Server "192.168.10.10"
```

Take **Screenshot 2** — `Resolve-DnsName` output showing successful forward
and reverse resolution for `webserver.txwes.edu` and `192.168.10.20`.

---

## Part 3 — Configure Forwarders

### Step 3.1 — Add a Standard Forwarder

```powershell
# Add Google DNS as a forwarder for external queries
Add-DnsServerForwarder -IPAddress "8.8.8.8","8.8.4.4" -PassThru

# Verify forwarders
Get-DnsServerForwarder
```

### Step 3.2 — Add a Conditional Forwarder

```powershell
# Create a conditional forwarder for a simulated partner domain
Add-DnsServerConditionalForwarderZone `
    -Name "partner.com" `
    -MasterServers "10.200.1.10" `
    -ReplicationScope Domain

# Verify conditional forwarder
Get-DnsServerZone | Where-Object {$_.ZoneType -eq "Forwarder"} |
    Select-Object ZoneName, MasterServers
```

Take **Screenshot 3** — `Get-DnsServerForwarder` and conditional forwarder zone
output showing both configured.

---

## Part 4 — Enable DNS Scavenging

### Step 4.1 — Enable Server-Level Scavenging

```powershell
# Enable scavenging on the DNS server
Set-DnsServerScavenging `
    -ScavengingState $true `
    -ScavengingInterval 7.00:00:00 `
    -PassThru

# Verify server scavenging settings
Get-DnsServerScavenging
```

### Step 4.2 — Enable Zone-Level Aging

```powershell
# Enable aging on the txwes.edu zone
Set-DnsServerZoneAging `
    -ZoneName "txwes.edu" `
    -Aging $true `
    -NoRefreshInterval 7.00:00:00 `
    -RefreshInterval 7.00:00:00

# Verify zone aging settings
Get-DnsServerZoneAging -ZoneName "txwes.edu"
```

Take **Screenshot 4** — `Get-DnsServerScavenging` and `Get-DnsServerZoneAging`
output showing scavenging and aging both enabled.

---

## Part 5 — Install and Configure DHCP

### Step 5.1 — Install the DHCP Role

```powershell
# Install DHCP Server role
Install-WindowsFeature -Name DHCP -IncludeManagementTools

# Verify
Get-WindowsFeature -Name DHCP | Select-Object Name, InstallState
```

### Step 5.2 — Authorize the DHCP Server

```powershell
# Authorize DC1 as a DHCP server in Active Directory
Add-DhcpServerInDC -DnsName "DC1.txwes.edu" -IPAddress 192.168.10.10

# Verify authorization
Get-DhcpServerInDC
```

### Step 5.3 — Create the DHCP Scope

```powershell
# Create the main campus DHCP scope
Add-DhcpServerv4Scope `
    -Name "TXWES_Main_Campus" `
    -StartRange "192.168.10.100" `
    -EndRange "192.168.10.200" `
    -SubnetMask "255.255.255.0" `
    -Description "Main campus client address pool" `
    -LeaseDuration (New-TimeSpan -Days 8) `
    -State Active

# Verify scope
Get-DhcpServerv4Scope | Select-Object Name, ScopeId, StartRange, EndRange, State
```

### Step 5.4 — Add an Exclusion Range

```powershell
# Exclude .100-.109 for static devices
Add-DhcpServerv4ExclusionRange `
    -ScopeId "192.168.10.0" `
    -StartRange "192.168.10.100" `
    -EndRange "192.168.10.109"

# Verify exclusion
Get-DhcpServerv4ExclusionRange -ScopeId "192.168.10.0"
```

Take **Screenshot 5** — `Get-DhcpServerv4Scope` and exclusion range output.

---

## Part 6 — Configure Scope Options and Reservations

### Step 6.1 — Set Scope Options

```powershell
# Configure gateway, DNS, and domain name options
Set-DhcpServerv4OptionValue `
    -ScopeId "192.168.10.0" `
    -Router "192.168.10.1" `
    -DnsServer "192.168.10.10" `
    -DnsDomain "txwes.edu"

# Verify scope options
Get-DhcpServerv4OptionValue -ScopeId "192.168.10.0" |
    Select-Object OptionId, Name, Value
```

### Step 6.2 — Create a Reservation

```powershell
# Create a reservation for the campus printer
Add-DhcpServerv4Reservation `
    -ScopeId "192.168.10.0" `
    -IPAddress "192.168.10.150" `
    -ClientId "00-11-22-33-44-55" `
    -Description "Main campus HP LaserJet" `
    -Name "Campus_Printer_01"

# Verify reservation
Get-DhcpServerv4Reservation -ScopeId "192.168.10.0" |
    Select-Object IPAddress, ClientId, Name, Description
```

Take **Screenshot 6** — Scope options and reservation output.

---

## Part 7 — Verification Summary

```powershell
Write-Host "=== DNS Zones ===" -ForegroundColor Cyan
Get-DnsServerZone | Select-Object ZoneName, ZoneType, IsDsIntegrated

Write-Host "=== DNS Forwarders ===" -ForegroundColor Cyan
Get-DnsServerForwarder

Write-Host "=== DNS Scavenging ===" -ForegroundColor Cyan
Get-DnsServerScavenging | Select-Object ScavengingState, ScavengingInterval

Write-Host "=== DHCP Authorization ===" -ForegroundColor Cyan
Get-DhcpServerInDC

Write-Host "=== DHCP Scope ===" -ForegroundColor Cyan
Get-DhcpServerv4Scope | Select-Object Name, ScopeId, State

Write-Host "=== DHCP Options ===" -ForegroundColor Cyan
Get-DhcpServerv4OptionValue -ScopeId "192.168.10.0"

Write-Host "=== DHCP Reservations ===" -ForegroundColor Cyan
Get-DhcpServerv4Reservation -ScopeId "192.168.10.0"

Write-Host "=== DHCP Statistics ===" -ForegroundColor Cyan
Get-DhcpServerv4ScopeStatistics -ScopeId "192.168.10.0"
```

Take **Screenshot 7** — Full verification summary output.

---

## Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1** — Both DNS zones as AD-Integrated with Secure dynamic updates.

**Screenshot 2** — `Resolve-DnsName` showing forward and reverse resolution.

**Screenshot 3** — Standard and conditional forwarder configured.

**Screenshot 4** — Server scavenging and zone aging both enabled.

**Screenshot 5** — DHCP scope with exclusion range.

**Screenshot 6** — Scope options and reservation.

**Screenshot 7** — Full verification summary.

---

## Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| DNS zones configured | 15 | Screenshot 1 shows AD-integrated zones |
| DNS record resolution | 15 | Screenshot 2 shows forward and reverse resolution |
| Forwarders configured | 10 | Screenshot 3 shows standard and conditional forwarder |
| Scavenging enabled | 10 | Screenshot 4 shows both server and zone scavenging enabled |
| DHCP scope and exclusion | 20 | Screenshot 5 shows correct scope and exclusion |
| Scope options and reservation | 20 | Screenshot 6 shows options and reservation configured |
| Verification summary | 10 | Screenshot 7 shows all services active |

---

## Troubleshooting Notes

If `Resolve-DnsName` returns "DNS name does not exist," verify the record was
created correctly:

```powershell
Get-DnsServerResourceRecord -ZoneName "txwes.edu" -RRType A
```

If `Add-DhcpServerInDC` fails with "Access denied," verify you are running
PowerShell as a Domain Administrator.

If the DHCP scope shows as Inactive after creation, activate it:

```powershell
Set-DhcpServerv4Scope -ScopeId "192.168.10.0" -State Active
```

If clients receive 169.254.x.x (APIPA) addresses, verify the DHCP Server
service is running and the server is authorized:

```powershell
Get-Service -Name DHCPServer | Select-Object Status, StartType
Get-DhcpServerInDC
```
