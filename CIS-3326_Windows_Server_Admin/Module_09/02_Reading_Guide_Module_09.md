# Reading Guide: Module 09 — DNS and DHCP Services in Windows Server

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3326 &BULL; WINDOWS SERVER ADMINISTRATION & ACTIVE DIRECTORY</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

Module 09 covers DNS and DHCP — the network identity services that underpin
Active Directory. This reading guide provides reference tables for zone types,
record types, scope options, DHCP failover, PowerShell commands, exam tips,
a glossary, and a study checklist.

---

## 1. DNS Zone Types Reference

| Zone Type | Read-Write | Storage | Replication | Use Case |
|---|---|---|---|---|
| Primary | Yes | Flat file on one server | Zone transfer (manual) | Simple environments |
| Secondary | No (read-only) | Flat file on one server | Zone transfer from primary | DNS redundancy |
| Stub | Records NS/SOA/A only | Flat file or AD | Zone transfer | Point to delegated zone's NS records |
| AD-Integrated Primary | Yes (multi-master) | Active Directory | AD replication (automatic) | All Windows domain environments |

**AD-Integrated is always the correct choice for domain environments.** It
provides secure dynamic updates, multi-master writes, and automatic replication
without configuring zone transfers.

---

## 2. DNS Dynamic Update Types

| Setting | Behavior |
|---|---|
| None | Dynamic updates are disabled — all records must be added manually |
| Nonsecure and Secure | Any client can register DNS records — not recommended |
| Secure only | Only authenticated (domain-joined) clients can register records |

**Best practice:** Use Secure only for AD-Integrated zones.

---

## 3. DNS Record Types Quick Reference

| Record | Purpose | Example |
|---|---|---|
| A | Hostname to IPv4 | `DC1.txwes.edu` resolves to `192.168.10.10` |
| AAAA | Hostname to IPv6 | `DC1.txwes.edu` resolves to `fe80::1` |
| PTR | IP to hostname (reverse) | `10.10.168.192.in-addr.arpa` resolves to `DC1.txwes.edu` |
| CNAME | Alias to canonical name | `www.txwes.edu` maps to `webserver.txwes.edu` |
| MX | Mail exchange server | `txwes.edu` mail to `mail.txwes.edu` |
| SRV | Service location (used by AD) | `_ldap._tcp.dc._msdcs.txwes.edu` maps to DC1 |
| NS | Zone's name server | `txwes.edu` NS maps to `DC1.txwes.edu` |
| SOA | Zone metadata (primary server, serial, TTL) | `txwes.edu` SOA maps to `DC1.txwes.edu` |

SRV records are automatically created by Active Directory — do not modify them
manually unless troubleshooting.

---

## 4. DNS Scavenging Timeline

```text
Record registered → No-refresh interval (7 days default)
                    During this period: record cannot be refreshed (timestamp locked)
                  → Refresh interval (7 days default)
                    During this period: record MUST be refreshed or it becomes stale
                  → Scavenging runs (every 7 days default)
                    Stale records are deleted

Total time to deletion: 7 + 7 + 7 = 21 days (default)
```

Both conditions must be true for a record to be scavenged:

1. Scavenging is enabled on the DNS server.

2. Aging is enabled on the specific DNS zone.

---

## 5. DHCP DORA Process

```text
Client                              DHCP Server
  │                                      │
  │──── DHCPDISCOVER (broadcast) ───────►│  "Is there a DHCP server?"
  │◄─── DHCPOFFER ──────────────────────│  "Here is an available IP: 192.168.10.101"
  │──── DHCPREQUEST (broadcast) ────────►│  "I accept that IP offer"
  │◄─── DHCPACK ────────────────────────│  "Confirmed. Lease is yours for 8 days."
  │
  │  Client configures adapter with:
  │  IP: 192.168.10.101, Mask, Gateway, DNS, Domain
```

The DHCPREQUEST is still a broadcast even though the client knows the server's
address. This allows other DHCP servers that sent offers to reclaim their offered
addresses.

---

## 6. DHCP Scope Options Reference

| Option | Code | Value Delivered |
|---|---|---|
| Router (Default Gateway) | 003 | Default gateway IP address |
| DNS Servers | 006 | DNS server IP addresses |
| DNS Domain Name | 015 | Domain suffix (e.g., txwes.edu) |
| WINS/NBNS Servers | 044 | WINS server address |
| WINS/NBT Node Type | 046 | NetBIOS node type |

Options can be set at three levels (highest priority wins):

1. Server level — applies to all scopes on this server.

2. Scope level — applies to this scope only.

3. Reservation level — applies to a specific reserved client only.

---

## 7. DHCP Failover Modes Comparison

| Feature | Hot Standby | Load Sharing |
|---|---|---|
| Primary role | One Active, one Standby | Both Active |
| Address pool division | Active holds ~95%, Standby holds ~5% | Split by configured % (default 50/50) |
| Failover trigger | Standby activates when Active is unreachable | Both always active |
| Use case | DR and redundancy focus | Performance and redundancy combined |

---

## 8. DNS PowerShell Quick Reference

```powershell
# ── Zone Management ───────────────────────────────────────────────
Get-DnsServerZone
Add-DnsServerPrimaryZone -Name "txwes.edu" -ReplicationScope Domain -DynamicUpdate Secure
Add-DnsServerPrimaryZone -NetworkId "192.168.10.0/24" -ReplicationScope Domain

# ── Record Management ─────────────────────────────────────────────
Add-DnsServerResourceRecordA `
    -ZoneName "txwes.edu" -Name "host1" -IPv4Address "192.168.10.50"
Add-DnsServerResourceRecordCName `
    -ZoneName "txwes.edu" -Name "www" -HostNameAlias "host1.txwes.edu."
Add-DnsServerResourceRecordPtr `
    -ZoneName "10.168.192.in-addr.arpa" -Name "50" -PtrDomainName "host1.txwes.edu."
Get-DnsServerResourceRecord -ZoneName "txwes.edu" -RRType A
Remove-DnsServerResourceRecord -ZoneName "txwes.edu" -RRType A -Name "host1" `
    -RecordData "192.168.10.50" -Force

# ── Forwarders ────────────────────────────────────────────────────
Add-DnsServerForwarder -IPAddress "8.8.8.8","8.8.4.4"
Get-DnsServerForwarder
Add-DnsServerConditionalForwarderZone -Name "partner.com" `
    -MasterServers "10.200.1.10" -ReplicationScope Domain

# ── Scavenging ────────────────────────────────────────────────────
Set-DnsServerScavenging -ScavengingState $true -ScavengingInterval 7.00:00:00
Set-DnsServerZoneAging -ZoneName "txwes.edu" -Aging $true
Start-DnsServerScavenging -Force

# ── Verification ──────────────────────────────────────────────────
Resolve-DnsName -Name "DC1.txwes.edu"
nslookup DC1.txwes.edu 192.168.10.10
```

---

## 9. DHCP PowerShell Quick Reference

```powershell
# ── Server Authorization ──────────────────────────────────────────
Add-DhcpServerInDC -DnsName "DC1.txwes.edu" -IPAddress 192.168.10.10
Get-DhcpServerInDC

# ── Scope Management ─────────────────────────────────────────────
Add-DhcpServerv4Scope `
    -Name "Main" -StartRange "192.168.10.100" -EndRange "192.168.10.200" `
    -SubnetMask "255.255.255.0" -State Active
Get-DhcpServerv4Scope

# ── Exclusions ────────────────────────────────────────────────────
Add-DhcpServerv4ExclusionRange `
    -ScopeId "192.168.10.0" -StartRange "192.168.10.100" -EndRange "192.168.10.110"

# ── Scope Options ─────────────────────────────────────────────────
Set-DhcpServerv4OptionValue -ScopeId "192.168.10.0" `
    -Router "192.168.10.1" -DnsServer "192.168.10.10" -DnsDomain "txwes.edu"

# ── Reservations ──────────────────────────────────────────────────
Add-DhcpServerv4Reservation -ScopeId "192.168.10.0" `
    -IPAddress "192.168.10.150" -ClientId "00-11-22-33-44-55" -Name "Printer01"
Get-DhcpServerv4Reservation -ScopeId "192.168.10.0"

# ── Failover ──────────────────────────────────────────────────────
Add-DhcpServerv4Failover -Name "Failover01" -PartnerServer "DC2.txwes.edu" `
    -ScopeId "192.168.10.0" -Mode HotStandby -ServerRole Active -ReservePercent 5
Get-DhcpServerv4Failover

# ── Leases and Stats ──────────────────────────────────────────────
Get-DhcpServerv4Lease -ScopeId "192.168.10.0"
Get-DhcpServerv4ScopeStatistics -ScopeId "192.168.10.0"
```

---

## 10. DNS and DHCP Architecture Overview

```text
Client (192.168.10.50)
    │
    │ Step 1: DHCP DORA → receives 192.168.10.50, GW 192.168.10.1, DNS 192.168.10.10
    │ Step 2: DNS lookup → DC1.txwes.edu → 192.168.10.10
    │ Step 3: DNS SRV → _ldap._tcp.dc._msdcs.txwes.edu → DC1
    │
    ▼
DC1 (192.168.10.10)
    ├── DNS Server
    │     ├── Zone: txwes.edu (AD-Integrated, Secure Updates)
    │     ├── Zone: 10.168.192.in-addr.arpa (reverse)
    │     ├── Forwarder: 8.8.8.8
    │     └── Conditional Forwarder: partner.com → 10.200.1.10
    │
    └── DHCP Server
          ├── Scope: 192.168.10.100–200 (8-day lease)
          ├── Exclusion: 192.168.10.100–109
          ├── Reservation: 192.168.10.150 → 00-11-22-33-44-55
          ├── Options: Router, DNS, DnsDomain
          └── Failover: Hot Standby with DC2 (5% reserve)
```

---

## 11. Exam Tips

**Exam Tip 1** — AD-Integrated zones are multi-master with Secure dynamic
updates. Any scenario requiring AD-level security or no-configuration replication
points to AD-Integrated.

**Exam Tip 2** — Scavenging requires enabling on both the server and the zone.
A scenario where only one is enabled means stale records still accumulate.

**Exam Tip 3** — DHCP servers must be authorized in AD. An unauthorized DHCP
server is blocked from responding to domain clients. Clients that receive APIPA
addresses (169.254.x.x) often have an unauthorized or unavailable DHCP server.

**Exam Tip 4** — Reservations are MAC-address based. A reservation inside the
scope range permanently binds one IP to one device. Other clients never receive
that IP even if the reserved device is offline.

**Exam Tip 5** — Hot Standby failover = one active, one passive (DR scenario).
Load Sharing = both active with a split pool (performance + redundancy scenario).

**Exam Tip 6** — SRV records are automatically registered by Active Directory.
If AD clients cannot find domain controllers, verify that SRV records exist in
DNS: `_ldap._tcp.dc._msdcs.<domain>` and `_kerberos._tcp.dc._msdcs.<domain>`.

---

## 12. Glossary

| Term | Definition |
|---|---|
| DNS | Domain Name System — translates hostnames to IP addresses |
| AD-Integrated zone | DNS zone stored in Active Directory; provides multi-master updates and automatic replication |
| Stub zone | DNS zone containing only SOA, NS, and A records for the zone's name servers |
| Secondary zone | Read-only DNS zone updated via zone transfer from a primary server |
| Conditional Forwarder | DNS forwarder that routes queries for a specific domain to a specific server |
| Scavenging | Automatic removal of stale dynamic DNS records based on no-refresh and refresh intervals |
| DHCP | Dynamic Host Configuration Protocol — automatically assigns IP configuration to network clients |
| Scope | A pool of IP addresses that a DHCP server can assign to clients on a subnet |
| Exclusion range | A range of addresses within a scope that the DHCP server will not assign |
| Reservation | A permanent IP-to-MAC address binding ensuring a device always receives the same IP |
| Scope options | Additional configuration (gateway, DNS servers) delivered to DHCP clients with their lease |
| Lease duration | The time period for which a DHCP-assigned IP address is valid |
| DORA | Discover-Offer-Request-Acknowledge — the four-message DHCP handshake |
| Superscope | A container grouping multiple DHCP scopes for multinetting scenarios |
| DHCP Failover | A redundancy configuration pairing two DHCP servers to share scope information |
| Hot Standby | DHCP failover mode where one server is active and one is passive |
| Load Sharing | DHCP failover mode where both servers actively handle requests with a split address pool |
| APIPA | Automatic Private IP Addressing — 169.254.x.x addresses assigned when no DHCP server responds |

---

## 13. Study Checklist

- Watch Module 09 Part 1 video (DNS zone types, record types, forwarders, scavenging, DHCP DORA, scopes, failover)

- Watch Module 09 Part 2 video (PowerShell installation, zone creation, record management, scope, reservations, failover, verification)

- Know all DNS zone types and when to use each

- Know AD-Integrated zone benefits over standard primary zones

- Know the scavenging timeline and the two-level enablement requirement

- Know the DORA handshake and every component of a DHCP scope

- Know DHCP failover Hot Standby vs. Load Sharing

- Review all PowerShell commands in Sections 8 and 9

- Complete Lab 09 and submit required screenshots

---

## Additional Resources

- [DNS overview for Windows Server](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top)
- [DHCP overview for Windows Server](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top)
- [DNS scavenging configuration](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc753378(v=ws.11))
- [DHCP failover configuration](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn338978(v=ws.11))

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 09 topics:

**1. Microsoft Learn — Implement and manage DNS for Windows Server**
<https://learn.microsoft.com/en-us/training/modules/implement-windows-server-dns/>
Hands-on module covering DNS zone types, AD-Integrated zones, forwarders, conditional forwarders, and dynamic updates with sandbox exercises aligned to the AZ-800 exam.

**2. Microsoft Docs — DHCP failover overview**
<https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-failover>
Full explanation of DHCP Failover architecture including Hot Standby and Load Sharing modes, partner server configuration, shared secret requirements, and failover state machine behavior.

**3. Microsoft Docs — DNS aging and scavenging**
<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc757041(v=ws.10)>
Detailed reference covering the no-refresh and refresh interval mechanics, how timestamps are set, the two-level enablement requirement (server + zone), and how the scavenging cycle deletes stale records.

**4. Microsoft Docs — DHCP scope options reference**
<https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-subnet-options>
Covers DHCP option precedence (server → scope → reservation), how scope options are inherited, and commonly used option codes (003 Router, 006 DNS Servers, 015 DNS Domain Name) with configuration guidance.

---

*Review all sections before beginning Lab 09, Quiz 09, and Discussion 09.*
