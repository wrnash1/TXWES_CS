# Video Script: Module 09 — DNS and DHCP Services in Windows Server (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Introduction

Welcome back. I am Professor Nash.

In Part 1 we covered DNS zone types, record types, forwarders, scavenging, and
the DHCP DORA process, scope configuration, superscopes, and DHCP failover.

In Part 2 we install and configure DNS and DHCP using PowerShell on DC1, create
an AD-integrated DNS zone, add records, configure a forwarder, enable scavenging,
create a DHCP scope with reservations, and configure DHCP failover. We close
with verification and exam tips.

---

## Section 1: Installing DNS and DHCP

DNS is automatically installed with the Active Directory Domain Services role.
If you need to add DNS or DHCP to a standalone server:

```powershell
# Install DNS Server role
Install-WindowsFeature -Name DNS -IncludeManagementTools

# Install DHCP Server role
Install-WindowsFeature -Name DHCP -IncludeManagementTools

# Verify both are installed
Get-WindowsFeature -Name DNS, DHCP | Select-Object Name, InstallState
```

After installing DHCP, you must authorize the server in Active Directory before
it can respond to client requests. An unauthorized DHCP server is blocked from
issuing leases in a domain environment.

```powershell
# Authorize the DHCP server in Active Directory
Add-DhcpServerInDC -DnsName "DC1.txwes.edu" -IPAddress 192.168.10.10

# Verify the DHCP server is authorized
Get-DhcpServerInDC
```

---

## Section 2: Creating an AD-Integrated DNS Zone

When Active Directory is installed on DC1, the `txwes.edu` forward lookup zone
is automatically created as AD-integrated. Let us look at it and then create a
reverse lookup zone.

```powershell
# View existing DNS zones
Get-DnsServerZone | Select-Object ZoneName, ZoneType, IsDsIntegrated, DynamicUpdate

# Create a reverse lookup zone for the 192.168.10.0/24 subnet
Add-DnsServerPrimaryZone `
    -NetworkId "192.168.10.0/24" `
    -ReplicationScope Domain `
    -DynamicUpdate Secure

# Verify the reverse zone was created
Get-DnsServerZone -Name "10.168.192.in-addr.arpa"
```

The `-ReplicationScope Domain` parameter stores the zone in AD and replicates
it to all domain controllers that run DNS in the domain. `-DynamicUpdate Secure`
ensures only authenticated computers can register DNS records.

---

## Section 3: Managing DNS Records

```powershell
# Add an A record (hostname to IP)
Add-DnsServerResourceRecordA `
    -ZoneName "txwes.edu" `
    -Name "webserver" `
    -IPv4Address "192.168.10.20" `
    -TimeToLive (New-TimeSpan -Hours 1)

# Add a CNAME record (alias)
Add-DnsServerResourceRecordCName `
    -ZoneName "txwes.edu" `
    -Name "www" `
    -HostNameAlias "webserver.txwes.edu."

# Add a PTR record manually (reverse lookup)
Add-DnsServerResourceRecordPtr `
    -ZoneName "10.168.192.in-addr.arpa" `
    -Name "20" `
    -PtrDomainName "webserver.txwes.edu."

# View all A records in the zone
Get-DnsServerResourceRecord -ZoneName "txwes.edu" -RRType A |
    Select-Object HostName, RecordData

# Remove a DNS record
Remove-DnsServerResourceRecord `
    -ZoneName "txwes.edu" `
    -RRType A `
    -Name "webserver" `
    -RecordData "192.168.10.20" `
    -Force
```

---

## Section 4: Configuring DNS Forwarders

```powershell
# Add a forwarder — send all non-local queries to Google DNS
Add-DnsServerForwarder -IPAddress "8.8.8.8","8.8.4.4" -PassThru

# View configured forwarders
Get-DnsServerForwarder

# Remove a forwarder
Remove-DnsServerForwarder -IPAddress "8.8.8.8"

# Create a conditional forwarder for a partner domain
Add-DnsServerConditionalForwarderZone `
    -Name "partner.com" `
    -MasterServers "10.200.1.10" `
    -ReplicationScope Domain

# View conditional forwarders
Get-DnsServerZone | Where-Object {$_.ZoneType -eq "Forwarder"} |
    Select-Object ZoneName, MasterServers
```

The `-ReplicationScope Domain` parameter on the conditional forwarder stores
it in AD, replicating it to all domain DCs automatically — so you only need
to configure it once.

---

## Section 5: Enabling DNS Scavenging

```powershell
# Enable scavenging on the DNS server
Set-DnsServerScavenging `
    -ScavengingState $true `
    -ScavengingInterval 7.00:00:00 `
    -PassThru

# Enable aging and scavenging on a specific zone
Set-DnsServerZoneAging `
    -ZoneName "txwes.edu" `
    -Aging $true `
    -NoRefreshInterval 7.00:00:00 `
    -RefreshInterval 7.00:00:00

# View scavenging settings
Get-DnsServerScavenging
Get-DnsServerZoneAging -ZoneName "txwes.edu"

# Trigger an immediate scavenge
Start-DnsServerScavenging -Force
```

Remember: scavenging must be enabled in both the server-level settings and the
individual zone settings. Enabling one without the other has no effect.

---

## Section 6: Creating a DHCP Scope

```powershell
# Create a new DHCP scope for the 192.168.10.0/24 subnet
Add-DhcpServerv4Scope `
    -Name "TXWES Main Campus" `
    -StartRange "192.168.10.100" `
    -EndRange "192.168.10.200" `
    -SubnetMask "255.255.255.0" `
    -Description "Main campus client network" `
    -LeaseDuration (New-TimeSpan -Days 8) `
    -State Active

# Add an exclusion range for static devices (servers, printers)
Add-DhcpServerv4ExclusionRange `
    -ScopeId "192.168.10.0" `
    -StartRange "192.168.10.100" `
    -EndRange "192.168.10.109"

# Configure scope options (gateway, DNS, domain name)
Set-DhcpServerv4OptionValue `
    -ScopeId "192.168.10.0" `
    -Router "192.168.10.1" `
    -DnsServer "192.168.10.10" `
    -DnsDomain "txwes.edu"

# Verify the scope
Get-DhcpServerv4Scope | Select-Object Name, ScopeId, StartRange, EndRange, State
Get-DhcpServerv4OptionValue -ScopeId "192.168.10.0"
```

---

## Section 7: Creating a DHCP Reservation

Reservations permanently bind a specific IP address to a specific device based
on its MAC address. The device always receives the same IP from DHCP.

```powershell
# Create a reservation for the campus printer
Add-DhcpServerv4Reservation `
    -ScopeId "192.168.10.0" `
    -IPAddress "192.168.10.150" `
    -ClientId "00-11-22-33-44-55" `
    -Description "Main campus HP LaserJet" `
    -Name "Campus_Printer_01"

# View all reservations in the scope
Get-DhcpServerv4Reservation -ScopeId "192.168.10.0" |
    Select-Object IPAddress, ClientId, Name, Description

# Remove a reservation
Remove-DhcpServerv4Reservation `
    -ScopeId "192.168.10.0" `
    -IPAddress "192.168.10.150"
```

---

## Section 8: Configuring DHCP Failover

DHCP failover requires two DHCP servers. In our example, DC1 (192.168.10.10)
is the primary and DC2 (192.168.10.11) is the partner.

```powershell
# Configure DHCP failover in Hot Standby mode
Add-DhcpServerv4Failover `
    -Name "TXWES-DHCP-Failover" `
    -PartnerServer "DC2.txwes.edu" `
    -ScopeId "192.168.10.0" `
    -Mode HotStandby `
    -ServerRole Active `
    -ReservePercent 5 `
    -AutoStateTransition $true `
    -MaxClientLeadTime (New-TimeSpan -Hours 1)

# View failover configuration
Get-DhcpServerv4Failover

# To configure Load Sharing mode instead:
# -Mode LoadBalance -LoadBalancePercent 50
```

The `-MaxClientLeadTime` parameter controls how long the standby server waits
before taking over when it can no longer contact the active server. Setting this
to 1 hour means clients continue renewing leases during a brief outage without
the standby server prematurely activating.

---

## Section 9: Verifying DNS and DHCP

```powershell
# ── DNS Verification ──────────────────────────────────────────────
# Test forward resolution
Resolve-DnsName -Name "DC1.txwes.edu" -Server "192.168.10.10"

# Test reverse resolution
Resolve-DnsName -Name "192.168.10.10" -Server "192.168.10.10"

# Use nslookup interactively
nslookup DC1.txwes.edu 192.168.10.10

# Check SRV records (critical for AD authentication)
Resolve-DnsName -Name "_ldap._tcp.dc._msdcs.txwes.edu" -Type SRV

# ── DHCP Verification ─────────────────────────────────────────────
# View all active leases
Get-DhcpServerv4Lease -ScopeId "192.168.10.0" |
    Select-Object IPAddress, ClientId, HostName, LeaseExpiryTime

# On a client — force DHCP renewal
ipconfig /release
ipconfig /renew
ipconfig /all

# View DHCP statistics
Get-DhcpServerv4ScopeStatistics -ScopeId "192.168.10.0"
```

---

## Section 10: Exam Tips

**Exam Tip 1** — AD-Integrated zones are multi-master and use secure dynamic
updates. The exam will describe a scenario requiring AD-level security or
automatic replication — the answer is AD-Integrated zone.

**Exam Tip 2** — Scavenging must be enabled on the DNS server AND the specific
zone. Enabling only one has no effect. The exam may describe stale records
accumulating — the answer involves enabling both scavenging settings.

**Exam Tip 3** — DHCP servers must be authorized in Active Directory before
they can respond to clients in a domain. An unauthorized DHCP server is silently
ignored by domain clients. If a DHCP server is installed but clients receive
APIPA addresses (169.254.x.x), check authorization first.

**Exam Tip 4** — DHCP reservations use MAC addresses, not hostnames. The client
always receives the reserved IP. Reservations are inside the scope range but are
never assigned to other clients.

**Exam Tip 5** — Hot Standby vs. Load Sharing. Hot Standby = one active, one
passive (good for DR). Load Sharing = both active, split pool (good for
performance). The exam will describe which scenario fits which mode.

**Exam Tip 6** — Conditional Forwarders route queries for a specific domain to
a specific DNS server. Use these for partner domain resolution, split DNS, or
hybrid scenarios where on-premises and cloud DNS servers handle different
namespaces.

---

## Wrap-Up

In this two-part module we covered DNS and DHCP from architecture through
hands-on PowerShell configuration.

You now understand AD-Integrated DNS zones, record management, forwarder
configuration, scavenging, and the complete DHCP scope lifecycle including
exclusions, reservations, scope options, and failover.

Head to the Reading Guide for reference tables, then complete Lab 09 where you
will build DNS and DHCP from scratch in your lab environment.

See you in Module 10 — File and Print Services.
