# Video Script: Module 06 - DNS and DHCP Server Roles (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 06 - DNS and DHCP Server Roles

**Part:** 2 of 2 — Demonstrations, PowerShell Commands, Exam Tips, and Lab Preview

**Estimated Duration:** 11 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Recap and Demo Overview]

Welcome back to Module 06. In Part 1 we covered DNS record types, zone types, dynamic updates, forwarders, DHCP DORA, scopes, reservations, failover modes, and DHCP authorization. In Part 2 I will demonstrate installing and configuring both DNS and DHCP using PowerShell, walk through a DHCP scope configuration, and show DNS troubleshooting commands.

---

### [SEGMENT 2 — Demo: Install DNS and DHCP Roles]

**[SHOW SCREEN: PowerShell console on Windows Server]**

[Alt-text: PowerShell console showing Install-WindowsFeature commands for DNS and DHCP Server roles.]

```powershell
# Install DNS Server role (if not already installed during AD DS promotion)
Install-WindowsFeature -Name DNS -IncludeManagementTools

# Install DHCP Server role with management tools
Install-WindowsFeature -Name DHCP -IncludeManagementTools

# Verify both are installed
Get-WindowsFeature -Name DNS, DHCP | Select-Object Name, InstallState
```

Both features should show `InstallState: Installed` when complete.

---

### [SEGMENT 3 — Demo: Authorize DHCP Server and Create a Scope]

**[SHOW SCREEN: PowerShell showing DHCP authorization and scope creation]**

[Alt-text: PowerShell console showing Add-DhcpServerInDC command and New-DhcpServerv4Scope command with output confirming scope creation.]

```powershell
# Authorize the DHCP server in Active Directory
Add-DhcpServerInDC -DnsName "SRV-CORE-01.corp.local" -IPAddress 192.168.10.10

# Verify authorization
Get-DhcpServerInDC

# Create a DHCP scope for the 192.168.10.0/24 network
Add-DhcpServerv4Scope `
    -Name "CorpNetwork" `
    -StartRange 192.168.10.100 `
    -EndRange 192.168.10.200 `
    -SubnetMask 255.255.255.0 `
    -Description "Main office client scope" `
    -State Active

# Add an exclusion range for statically configured devices
Add-DhcpServerv4ExclusionRange `
    -ScopeId 192.168.10.0 `
    -StartRange 192.168.10.100 `
    -EndRange 192.168.10.110
```

---

### [SEGMENT 4 — Demo: Configure Scope Options and a Reservation]

**[SHOW SCREEN: PowerShell showing scope option and reservation commands]**

[Alt-text: PowerShell console showing Set-DhcpServerv4OptionValue and Add-DhcpServerv4Reservation commands.]

```powershell
# Set scope options — gateway, DNS, domain suffix
Set-DhcpServerv4OptionValue `
    -ScopeId 192.168.10.0 `
    -Router 192.168.10.1 `
    -DnsServer 192.168.10.10, 192.168.10.20 `
    -DnsDomain "corp.local"

# Create a reservation for a network printer
Add-DhcpServerv4Reservation `
    -ScopeId 192.168.10.0 `
    -IPAddress 192.168.10.115 `
    -ClientId "00-50-56-AB-12-34" `
    -Description "Floor3 HP LaserJet"

# Verify scope configuration
Get-DhcpServerv4Scope | Select-Object Name, ScopeId, StartRange, EndRange, SubnetMask, State

# Verify reservations
Get-DhcpServerv4Reservation -ScopeId 192.168.10.0
```

---

### [SEGMENT 5 — Demo: Configure DHCP Failover]

**[SHOW SCREEN: PowerShell showing Add-DhcpServerv4Failover command]**

[Alt-text: PowerShell console showing the Add-DhcpServerv4Failover cmdlet configuring Hot Standby failover between two DHCP servers.]

```powershell
# Configure DHCP Failover in Hot Standby mode between two servers
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

The `-SharedSecret` parameter sets the authentication key between the two DHCP servers. The `-MaxClientLeadTime` determines how long the standby server waits before taking over after losing contact with the primary.

---

### [SEGMENT 6 — Demo: DNS Configuration and Record Management]

**[SHOW SCREEN: PowerShell showing DNS zone and record management commands]**

[Alt-text: PowerShell console showing Get-DnsServerZone, Add-DnsServerResourceRecord, and Resolve-DnsName commands.]

```powershell
# View all DNS zones on this server
Get-DnsServerZone | Select-Object ZoneName, ZoneType, DynamicUpdate, ReplicationScope

# Create a new static A record
Add-DnsServerResourceRecordA `
    -ZoneName "corp.local" `
    -Name "appserver" `
    -IPv4Address "192.168.10.50"

# Create a CNAME alias
Add-DnsServerResourceRecordCName `
    -ZoneName "corp.local" `
    -Name "app" `
    -HostNameAlias "appserver.corp.local."

# Add a conditional forwarder for a partner domain
Add-DnsServerConditionalForwarderZone `
    -Name "partner.com" `
    -MasterServers 10.10.1.1 `
    -ReplicationScope Forest

# View DNS server forwarders
Get-DnsServerForwarder
```

---

### [SEGMENT 7 — Demo: DNS Troubleshooting Commands]

**[SHOW SCREEN: PowerShell showing DNS diagnostic commands]**

[Alt-text: PowerShell console showing nslookup queries and ipconfig /flushdns output.]

```powershell
# Test name resolution using PowerShell
Resolve-DnsName -Name "DC1.corp.local" -Type A
Resolve-DnsName -Name "_ldap._tcp.corp.local" -Type SRV

# Query a specific DNS server
Resolve-DnsName -Name "DC1.corp.local" -Server "192.168.10.10"

# Flush DNS client cache
ipconfig /flushdns

# Show current DNS client cache
ipconfig /displaydns

# Clear DNS server cache (run on DNS server)
Clear-DnsServerCache -ComputerName "SRV-CORE-01"

# Or using dnscmd
dnscmd /ClearCache

# Force zone transfer on secondary zone
dnscmd /ZoneRefresh corp.local
```

---

### [SEGMENT 8 — Demo: Reverse Lookup Zone]

**[SHOW SCREEN: DNS Manager showing a reverse lookup zone for 192.168.10.x]**

[Alt-text: DNS Manager console showing a reverse lookup zone named 10.168.192.in-addr.arpa with PTR records for each host.]

Reverse lookup zones allow IP address-to-hostname resolution — the opposite of normal DNS. They are important for diagnostic tools, email server verification, and some security products.

```powershell
# Create a reverse lookup zone
Add-DnsServerPrimaryZone `
    -NetworkId "192.168.10.0/24" `
    -ReplicationScope Forest

# Add a PTR record
Add-DnsServerResourceRecordPtr `
    -ZoneName "10.168.192.in-addr.arpa" `
    -Name "10" `
    -PtrDomainName "DC1.corp.local."

# Test reverse lookup
Resolve-DnsName -Name "192.168.10.10" -Type PTR
```

---

### [SEGMENT 9 — Exam Tips]

**[SHOW SCREEN: Exam tips slide for Module 06]**

**Exam Tip 1:** AD-integrated zones with Secure Only dynamic updates are the correct configuration for internal Windows DNS. Any scenario asking for authenticated-only DNS registration means AD-integrated + Secure Only.

**Exam Tip 2:** DHCP Reservation vs. Exclusion Range. Reservation = always gives a specific IP to a specific MAC. Exclusion = removes addresses from pool so you can statically assign them. The device gets a guaranteed address only with a reservation.

**Exam Tip 3:** DHCP Failover modes. Hot Standby = one active, one standby (simpler). Load Balance = both active, split pool (better distribution). DHCP Split Scope is the old/deprecated approach — do not confuse it with Failover.

**Exam Tip 4:** DNS TTL caching. When a DNS record is updated, existing caches hold the old value until the TTL expires. Fix: `ipconfig /flushdns` on the client, `Clear-DnsServerCache` on the server.

**Exam Tip 5:** DHCP Authorization in AD prevents rogue DHCP servers. `Add-DhcpServerInDC` authorizes a server. Unauthorized servers refuse to serve leases to domain-joined clients.

**Exam Tip 6:** Conditional Forwarders vs. Forwarders. Regular Forwarders send all unresolved queries to the same upstream. Conditional Forwarders route queries for a specific domain to a specific server. Use Conditional Forwarders for inter-forest and partner-domain resolution.

---

### [SEGMENT 10 — Lab Preview]

**[SHOW SCREEN: Lab 06 instructions document]**

This week's lab walks you through installing the DHCP role on DC1, creating a scope for `192.168.10.0/24`, configuring scope options (gateway, DNS, domain suffix), creating a reservation for a printer MAC address, and enabling DNS aging on the `corp.local` zone.

Your deliverables are screenshots of the configured DHCP scope in DHCP Manager, the reservation entry, and `Get-DhcpServerv4Scope` PowerShell output.

---

### [SEGMENT 11 — Module 06 Summary]

**[SHOW SCREEN: Summary slide]**

DNS translates names to IP addresses and stores AD service locator records. AD-integrated zones replicate with AD and support Secure Only dynamic updates. Forwarders handle external queries. Aging and scavenging remove stale records. DHCP automates IP address assignment through the DORA process. Scopes, exclusions, and reservations control the address pool. DHCP Failover provides high availability. DHCP authorization prevents rogue servers.

Module 07 covers File and Print Services — the server roles that most end users interact with directly. See you there.

---

### Additional Resources

- [Deploy DNS Server](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-deploy-wps)
- [DHCP Server deployment](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-deploy-wps)
- [DHCP Failover reference](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn338978(v=ws.11))
- [DNS aging and scavenging](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc758485(v=ws.10))

---

*End of Part 2. Proceed to the Reading Guide, Lab, Quiz, and Discussion for Module 06.*
