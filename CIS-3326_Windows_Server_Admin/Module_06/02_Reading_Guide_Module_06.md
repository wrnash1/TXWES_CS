# Reading Guide: Module 06 - DNS and DHCP Server Roles

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

---

### Overview

Module 06 covers the two network infrastructure services that every Windows Server environment depends on: DNS for name resolution and DHCP for IP address assignment. Both are critical for Active Directory to function. This reading guide provides reference tables, an architecture diagram, exam tips, a glossary, and a study checklist.

**Certification Alignment:** AZ-800 — "Implement and manage DNS" and "Implement and manage DHCP"

---

### 1. DNS Record Types

| Record Type | Purpose | Example |
|---|---|---|
| A | Maps hostname to IPv4 address | `DC1.corp.local → 192.168.10.10` |
| AAAA | Maps hostname to IPv6 address | `DC1.corp.local → fe80::1` |
| CNAME | Alias pointing to another hostname | `mail.corp.local → mailserver.corp.local` |
| MX | Mail exchanger for a domain | Routes email for `corp.local` to Exchange server |
| PTR | Reverse lookup — IP to hostname | `192.168.10.10 → DC1.corp.local` |
| SRV | Service locator — maps service name to server | `_ldap._tcp.corp.local → DC1.corp.local:389` |
| SOA | Start of Authority — identifies zone authority | Defines primary DNS server and zone parameters |
| NS | Name Server — lists authoritative DNS servers | Lists which servers are authoritative for the zone |
| TXT | Text records — used for SPF, domain verification | `v=spf1 include:corp.local ~all` |

---

### 2. DNS Zone Types

| Zone Type | Storage | Writable | Replication Method | Best Use |
|---|---|---|---|---|
| Primary | Flat `.dns` file on disk | Yes — read/write | Manual zone transfer | Standalone DNS, non-AD environments |
| Secondary | Flat file, copy from primary | No — read-only | Zone transfer from primary | DNS load distribution, redundancy |
| Stub | Flat file, partial data only | No | Zone transfer of NS/SOA/glue only | Delegation, conditional forwarding |
| AD-Integrated | Active Directory database | Yes — multi-master | AD replication (automatic) | Recommended for all AD environments |

**Key point:** AD-Integrated zones replicate to all Domain Controllers running DNS automatically through AD replication. No manual zone transfer configuration is required. They support Secure Only dynamic updates, ensuring only authenticated domain members can register records.

---

### 3. Dynamic Update Settings

| Setting | Who Can Register | Use Case |
|---|---|---|
| None | Nobody — all records are static | Public-facing zones, high-security environments |
| Nonsecure and Secure | Any device, authenticated or not | Never use for internal AD zones |
| Secure Only | Only authenticated domain members | Correct setting for all internal AD-integrated zones |

**Rule:** Internal AD zones = AD-Integrated + Secure Only. Any scenario asking for authenticated-only DNS registration means both.

---

### 4. DNS Forwarders and Conditional Forwarders

| Feature | Behavior | Use Case |
|---|---|---|
| Forwarders | All unresolved queries go to a configured upstream server | Forwarding external internet queries to ISP/firewall DNS |
| Conditional Forwarders | Queries for a specific domain go to a specific server | Multi-forest resolution, partner domain queries |
| Root Hints | Fallback — walks full recursive resolution from root servers | Last resort when forwarders unavailable |

**Rule:** Use forwarders in corporate environments. Root hints create unnecessary internet traffic. Use Conditional Forwarders for inter-forest DNS resolution.

---

### 5. DNS Aging and Scavenging

| Parameter | Default Value | Purpose |
|---|---|---|
| No-refresh interval | 7 days | Prevents timestamp updates immediately after registration |
| Refresh interval | 7 days | Period during which clients can refresh timestamps |
| Total before eligible | 14 days | No-refresh + Refresh = time before record can be scavenged |
| Scavenging interval | Configurable | How often the server removes stale records |

**Key points:**

- Only dynamically registered records are eligible for scavenging. Static records are never scavenged.
- Aging must be enabled on both the DNS server AND the individual zone.
- Run `dnscmd /StartScavenging` to trigger manual scavenging.

---

### 6. DHCP DORA Process

```text
Client                          DHCP Server
  |                                  |
  |--- DHCP Discover (broadcast) --->|  Step 1: Client looks for any DHCP server
  |                                  |
  |<-- DHCP Offer (IP + options) ----|  Step 2: Server offers an available address
  |                                  |
  |--- DHCP Request (broadcast) ---->|  Step 3: Client accepts the offer (broadcast so
  |                                  |          other servers know the offer was taken)
  |<-- DHCP Acknowledge (confirm) ---|  Step 4: Server confirms the lease assignment
```

DORA = Discover, Offer, Request, Acknowledge

- Steps 1 and 3 are **broadcasts** — clients do not yet have an IP address
- Step 2 delivers: IP address, subnet mask, default gateway, DNS servers, lease duration
- Step 4 confirms the lease is active

---

### 7. DHCP Scope Configuration

| Component | Purpose | Example |
|---|---|---|
| Scope | Range of addresses the server can lease on a subnet | `192.168.10.100` – `192.168.10.200` |
| Exclusion Range | Addresses within scope range that DHCP will never lease | `192.168.10.100` – `192.168.10.110` |
| Reservation | Binds a specific IP to a specific MAC address | `00-50-56-AB-12-34 → 192.168.10.115` |
| Lease Duration | How long a client holds an address before renewal | Default: 8 days |

**Exclusion vs. Reservation:**

- Exclusion = removes addresses from pool for static assignment outside DHCP
- Reservation = DHCP still manages the address, but always gives it to one MAC

---

### 8. DHCP Scope Options

| Option Code | Purpose | Example Value |
|---|---|---|
| 003 Router | Default gateway for clients | `192.168.10.1` |
| 006 DNS Servers | DNS server IP addresses | `192.168.10.10`, `192.168.10.20` |
| 015 DNS Domain Name | DNS suffix appended to unqualified queries | `corp.local` |
| 044 WINS Servers | Legacy WINS server address | Rarely configured today |

---

### 9. DHCP Failover Modes

| Mode | How It Works | Who Serves Leases | Best Use |
|---|---|---|---|
| Hot Standby | Active server handles all leases; Standby takes over only on failure | One server at a time | Simpler management, low-traffic sites |
| Load Balance | Both servers share the pool (default 50/50); both serve leases simultaneously | Both servers | Better distribution, high-availability sites |

**Key points:**

- DHCP Failover uses a shared secret (`-SharedSecret`) to authenticate the two servers
- `-MaxClientLeadTime` determines how long the standby waits before taking over
- DHCP Split Scope (old approach) is deprecated — do not confuse it with Failover

---

### 10. DHCP Authorization in Active Directory

Authorization is stored in the Configuration partition of the AD forest. When a DHCP server starts, it queries AD to verify authorization. An unauthorized DHCP server refuses to serve leases to domain-joined clients.

```powershell
# Authorize a DHCP server
Add-DhcpServerInDC -DnsName "SRV-CORE-01.corp.local" -IPAddress 192.168.10.10

# Verify authorized servers
Get-DhcpServerInDC
```

**Key point:** Standalone (non-domain) DHCP servers do not perform authorization checks. Domain-joined and authorized DHCP servers are the only way to prevent rogue DHCP from serving incorrect addresses.

---

### 11. DNS and DHCP PowerShell Reference

```powershell
# ── DNS ──────────────────────────────────────────────────────────────
# Install DNS role
Install-WindowsFeature -Name DNS -IncludeManagementTools

# List all zones
Get-DnsServerZone | Select-Object ZoneName, ZoneType, DynamicUpdate

# Add an A record
Add-DnsServerResourceRecordA -ZoneName "corp.local" -Name "appserver" -IPv4Address "192.168.10.50"

# Add a CNAME
Add-DnsServerResourceRecordCName -ZoneName "corp.local" -Name "app" -HostNameAlias "appserver.corp.local."

# Add a conditional forwarder
Add-DnsServerConditionalForwarderZone -Name "partner.com" -MasterServers 10.10.1.1 -ReplicationScope Forest

# Create a reverse lookup zone
Add-DnsServerPrimaryZone -NetworkId "192.168.10.0/24" -ReplicationScope Forest

# Test resolution
Resolve-DnsName -Name "DC1.corp.local" -Type A
Resolve-DnsName -Name "192.168.10.10" -Type PTR

# Flush caches
ipconfig /flushdns
Clear-DnsServerCache -ComputerName "SRV-CORE-01"

# ── DHCP ─────────────────────────────────────────────────────────────
# Install DHCP role
Install-WindowsFeature -Name DHCP -IncludeManagementTools

# Authorize server
Add-DhcpServerInDC -DnsName "SRV-CORE-01.corp.local" -IPAddress 192.168.10.10

# Create scope
Add-DhcpServerv4Scope -Name "CorpNetwork" -StartRange 192.168.10.100 `
    -EndRange 192.168.10.200 -SubnetMask 255.255.255.0 -State Active

# Add exclusion range
Add-DhcpServerv4ExclusionRange -ScopeId 192.168.10.0 `
    -StartRange 192.168.10.100 -EndRange 192.168.10.110

# Set scope options
Set-DhcpServerv4OptionValue -ScopeId 192.168.10.0 `
    -Router 192.168.10.1 -DnsServer 192.168.10.10, 192.168.10.20 -DnsDomain "corp.local"

# Add a reservation
Add-DhcpServerv4Reservation -ScopeId 192.168.10.0 `
    -IPAddress 192.168.10.115 -ClientId "00-50-56-AB-12-34" -Description "Floor3 HP LaserJet"

# Configure failover
Add-DhcpServerv4Failover -Name "Corp-DHCP-Failover" `
    -PartnerServer "SRV-CORE-02.corp.local" -ScopeId 192.168.10.0 `
    -Mode HotStandby -SharedSecret "DHCPSharedSecret123!" -AutoStateTransition $true

# Verify scope and reservations
Get-DhcpServerv4Scope | Select-Object Name, ScopeId, StartRange, EndRange, State
Get-DhcpServerv4Reservation -ScopeId 192.168.10.0
```

---

### 12. DNS and DHCP Architecture Reference

```text
┌─────────────────────────────────────────────────────────┐
│                     corp.local Forest                    │
│                                                         │
│  ┌──────────────┐         ┌──────────────┐             │
│  │  DC1 / DNS1  │◄──AD──► │  DC2 / DNS2  │             │
│  │  192.168.10.10│         │ 192.168.10.20│             │
│  │  DHCP Primary│         │  DHCP Standby│             │
│  └──────┬───────┘         └──────┬───────┘             │
│         │                        │                      │
│         └─────── DHCP Failover ──┘                      │
│                  (Hot Standby)                          │
│                                                         │
│  DNS Zone: corp.local (AD-Integrated, Secure Only)      │
│  Forwarders: 8.8.8.8, 8.8.4.4                          │
│  DHCP Scope: 192.168.10.0/24                            │
│    Pool:    .100 – .200                                 │
│    Exclude: .100 – .110 (static devices)               │
│    Reserve: .115 (Floor3 printer MAC)                   │
└─────────────────────────────────────────────────────────┘
```

---

### 13. Exam Tips

**Exam Tip 1:** AD-integrated zones with Secure Only dynamic updates are always the correct choice for internal Windows DNS. The question will describe a need for authenticated registration — the answer is AD-Integrated + Secure Only.

**Exam Tip 2:** DHCP Reservation vs. Exclusion Range. Reservation = always gives a specific IP to a specific MAC address (DHCP manages it). Exclusion = removes addresses from the pool entirely so they can be statically configured on the device.

**Exam Tip 3:** DHCP Failover modes. Hot Standby = one active, one passive. Load Balance = both active, split pool. DHCP Split Scope is the old/deprecated method — it is NOT the same as DHCP Failover.

**Exam Tip 4:** DNS TTL caching. After a record is updated, clients and servers cache the old value until the TTL expires. Immediate fix: `ipconfig /flushdns` on the client, `Clear-DnsServerCache` or `dnscmd /ClearCache` on the server.

**Exam Tip 5:** DHCP Authorization prevents rogue DHCP servers. `Add-DhcpServerInDC` authorizes a server. Unauthorized servers will not serve leases to domain-joined clients. Standalone servers skip this check — domain-joined DHCP is the only defense.

**Exam Tip 6:** Conditional Forwarders vs. Forwarders. Regular Forwarders route all unresolved queries upstream. Conditional Forwarders route only queries for a specific domain to a specific DNS server. Use Conditional Forwarders for inter-forest and partner-domain resolution.

**Exam Tip 7:** DNS SRV records are registered by the Netlogon service on each DC. If SRV records are missing, restart the Netlogon service: `Restart-Service Netlogon`. Verify with `nslookup -type=SRV _ldap._tcp.corp.local`.

**Exam Tip 8:** Reverse lookup zones store PTR records (IP→hostname). They are not created automatically — you must create the reverse lookup zone and add PTR records. They are required for mail server verification, some diagnostic tools, and security products.

---

### 14. Glossary

| Term | Definition |
|---|---|
| DNS | Domain Name System — translates hostnames to IP addresses |
| Zone | A database of DNS records for a specific domain namespace |
| AD-Integrated Zone | DNS zone stored in the AD database; replicates with AD |
| Secure Only | Dynamic update setting allowing only authenticated domain members to register records |
| Forwarder | Upstream DNS server that receives queries the local server cannot resolve |
| Conditional Forwarder | Routes queries for a specific domain name to a designated server |
| Root Hints | IP addresses of internet root DNS servers; used when forwarders fail |
| Aging | Timestamping of dynamic DNS records to enable stale-record detection |
| Scavenging | Automatic removal of DNS records whose timestamps exceed the aging threshold |
| DHCP | Dynamic Host Configuration Protocol — automates IP address assignment |
| DORA | Discover, Offer, Request, Acknowledge — the four-step DHCP lease process |
| Scope | A range of IP addresses the DHCP server can lease on a specific subnet |
| Exclusion Range | Addresses within a scope that DHCP will never lease |
| Reservation | A scope entry binding a specific MAC address to a specific IP address |
| Scope Options | Additional configuration (gateway, DNS, domain name) delivered with each lease |
| DHCP Failover | Windows Server feature coordinating one scope between two DHCP servers for HA |
| Hot Standby | DHCP Failover mode where one server is active and one is passive |
| Load Balance | DHCP Failover mode where both servers actively serve leases from a shared pool |
| Authorization | AD-based approval that a DHCP server must have before serving domain-joined clients |
| PTR Record | Reverse DNS record mapping an IP address to a hostname |
| SRV Record | DNS record mapping a service name (e.g., `_ldap`) to a server and port |
| TTL | Time To Live — how long a DNS record is cached before the client must re-query |

---

### 15. Study Checklist

- Watch Module 06 Part 1 video (DNS concepts and DHCP fundamentals)
- Watch Module 06 Part 2 video (PowerShell demos, exam tips, lab preview)
- Review all DNS record types and be able to identify the correct record for a given scenario
- Know the four DNS zone types and when to use each
- Memorize the three dynamic update settings and which one is correct for internal AD DNS
- Understand Forwarders vs. Conditional Forwarders vs. Root Hints
- Know the aging and scavenging intervals and what they protect against
- Be able to explain the DHCP DORA process step by step
- Know the difference between an exclusion range and a reservation
- Know the difference between Hot Standby and Load Balance DHCP Failover modes
- Know why DHCP Authorization in AD prevents rogue DHCP servers
- Review all PowerShell commands in Section 11 — these appear on the exam and in the lab
- Complete Lab 06 and submit required screenshots

---

### Additional Resources

- [DNS Server overview](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-overview)
- [DNS zone management](https://learn.microsoft.com/en-us/windows-server/networking/dns/manage-dns-zones)
- [DHCP Server deployment](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-deploy-wps)
- [DHCP Failover reference](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn338978(v=ws.11))
- [DNS aging and scavenging](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc758485(v=ws.10))

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 06 topics:

**1. Microsoft Learn — Implement DNS for Windows Server**
<https://learn.microsoft.com/en-us/training/modules/implement-dns-for-windows-server/>
Covers DNS zone types, record management, forwarders, conditional forwarders, and zone delegation with sandbox exercises aligned to AZ-800.

**2. Microsoft Learn — Implement DHCP**
<https://learn.microsoft.com/en-us/training/modules/implement-dhcp/>
Hands-on module covering DHCP scope creation, options configuration, reservations, and DHCP Failover setup with Load Balance and Hot Standby modes.

**3. Microsoft Docs — DNS troubleshooting guide**
<https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-dns-guidance>
Systematic guide for diagnosing DNS resolution failures, SRV record issues, and zone transfer problems — directly applicable to dcdiag DNS test failures encountered in labs.

**4. Microsoft Docs — DHCP logging and auditing**
<https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top>
Official DHCP documentation covering audit log interpretation, rogue server detection, and DHCP event IDs — useful for understanding the security implications of DHCP authorization covered in Questions 6 and 9.

---

*Review all sections before beginning Lab 06, Quiz 06, and Discussion 06.*
