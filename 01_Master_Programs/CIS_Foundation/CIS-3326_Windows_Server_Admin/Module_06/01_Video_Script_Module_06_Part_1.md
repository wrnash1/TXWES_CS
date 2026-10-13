# Video Script: Module 06 - DNS and DHCP Server Roles (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 06 - DNS and DHCP Server Roles

**Part:** 1 of 2 — Concepts, Theory, and Architecture

**Estimated Duration:** 14 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Introduction]

**[SHOW SCREEN: Course title slide — Module 06]**

Welcome to Module 06. I am Professor Nash. Active Directory cannot function without DNS. DHCP makes IP addressing manageable at scale. Together these two roles form the network-services foundation of every Windows environment.

In Module 02 we referenced DNS SRV records constantly. In Module 03 we set our DNS client to point to the DC before promotion. Every module has touched DNS. Now we are going to build a complete understanding of how Windows DNS works, how to deploy and configure DHCP, and how these services integrate with Active Directory.

This module maps to AZ-800 objectives: "Implement and manage DNS" and "Implement and manage DHCP."

---

### [SEGMENT 2 — DNS Fundamentals]

**[SHOW SCREEN: Diagram showing the DNS query resolution process from client to local DNS to root to TLD to authoritative]**

[Alt-text: A flowchart showing a client querying a DNS server, the DNS server checking its cache, querying a root server for TLD delegation, then querying the authoritative server for the domain, and returning the answer to the client.]

DNS — Domain Name System — is the internet's phone book. It translates hostnames into IP addresses. When you type `www.example.com`, your computer sends a DNS query to its configured DNS server. That server resolves the name through a hierarchical lookup process and returns the IP address.

For internal Windows Server environments, DNS does something additional and critical: it stores **Service Locator (SRV) records** that tell domain-joined clients where to find Active Directory services. Without correctly functioning DNS, there is no domain logon, no Group Policy, no file share by name — nothing that depends on name resolution works.

**DNS Record Types:**

| Record Type | Purpose | Example |
|---|---|---|
| A | Maps hostname to IPv4 address | `DC1.corp.local → 192.168.10.10` |
| AAAA | Maps hostname to IPv6 address | `DC1.corp.local → fe80::1` |
| CNAME | Alias pointing to another hostname | `mail.corp.local → mailserver.corp.local` |
| MX | Mail exchanger for a domain | Routes email for `corp.local` to Exchange server |
| PTR | Reverse lookup — IP to hostname | `192.168.10.10 → DC1.corp.local` |
| SRV | Service locator — maps service name to server | `_ldap._tcp.corp.local → DC1.corp.local:389` |
| SOA | Start of Authority — identifies zone authority | Defines primary DNS server for a zone |
| NS | Name Server — lists authoritative DNS servers | Lists which servers are authoritative for corp.local |

---

### [SEGMENT 3 — DNS Zones]

**[SHOW SCREEN: DNS Manager showing zone types — Primary, Secondary, Stub, Active Directory-Integrated]**

[Alt-text: DNS Manager console showing three forward lookup zones with icons indicating Primary Zone, Secondary Zone, and Active Directory-Integrated Zone.]

A DNS zone is a database of records for a specific domain. Windows Server DNS supports several zone types.

**Primary Zone:** The writable master copy of the zone. Stored as a flat `.dns` text file on the primary DNS server. Only one primary zone exists per zone name. Administrators make all changes here.

**Secondary Zone:** A read-only copy of a primary zone, replicated via zone transfer. Used to distribute DNS query load and provide redundancy. Secondary zones are updated through zone transfers triggered by change notifications from the primary.

**Stub Zone:** Contains only the essential delegation records (NS, SOA, and glue A records) for a zone. It tells a DNS server which DNS servers are authoritative for a given zone without hosting the full zone data. Used for conditional forwarding and delegation in large environments.

**Active Directory-Integrated Zone:** The recommended zone type for domains. Zone data is stored in the Active Directory database itself, not in a flat file. It replicates to all Domain Controllers that run DNS automatically through AD replication — no manual zone transfer configuration required. It also supports Secure Only dynamic updates, ensuring only authenticated domain computers can register or update records.

The key advantage of AD-integrated zones: they replicate with AD, provide multi-master updates (any DC can modify the zone), and eliminate the need for manual zone transfer configuration.

---

### [SEGMENT 4 — Dynamic Updates]

**[SHOW SCREEN: DNS Zone Properties — Dynamic Update settings: None, Nonsecure and Secure, Secure Only]**

[Alt-text: DNS Zone Properties General tab showing the Dynamic Updates dropdown with options None, Nonsecure and Secure, and Secure Only selected.]

Dynamic DNS updates allow DNS client computers and DHCP servers to automatically register and update their DNS records. In a Windows domain, workstations register their own A records in DNS when they obtain an IP address.

Three dynamic update options:

**None:** No dynamic updates allowed. All records must be created manually. Appropriate for public-facing zones or highly locked-down environments.

**Nonsecure and Secure:** Both authenticated domain computers and unauthenticated machines can register records. Do not use this for internal zones — any device on the network can register any hostname, including spoofed entries.

**Secure Only:** Only authenticated domain members can register and update their own records in the zone. This is the correct setting for all internal AD-integrated zones. It prevents rogue devices from registering false DNS records.

---

### [SEGMENT 5 — DNS Forwarders and Conditional Forwarders]

**[SHOW SCREEN: DNS Server Properties — Forwarders tab showing upstream DNS addresses]**

[Alt-text: DNS Server Properties Forwarders tab showing two forwarding addresses and the Use root hints if no forwarders are available checkbox.]

When a DNS server receives a query for a name it is not authoritative for (e.g., `google.com` from an internal DNS server), it needs somewhere to send that query. This is where forwarders come in.

**Forwarders:** You configure the internal DNS server to forward all external queries to a specific upstream DNS server — typically your ISP's DNS, your firewall's DNS, or a public resolver like `8.8.8.8`. The internal server queries the forwarder; the forwarder resolves the external name and returns the answer.

**Conditional Forwarders:** More targeted. Instead of forwarding all external queries, you configure forwarding for a specific domain name. If the query is for `partner.com`, forward to the partner company's DNS. If the query is for `vendor.net`, forward to the vendor's DNS. All other queries resolve normally.

Conditional forwarders are essential in multi-forest environments where DNS resolution needs to cross forest boundaries for a specific partner domain.

**Root Hints:** The fallback when no forwarder is configured or the forwarder is unavailable. Root hints contain the IP addresses of the root DNS servers for the internet. The DNS server walks the full recursive resolution path. In a corporate environment, you should always use forwarders — root hints create unnecessary external internet traffic and slower resolution.

---

### [SEGMENT 6 — DNS Scavenging and Aging]

**[SHOW SCREEN: DNS Zone Properties — Aging tab]**

[Alt-text: DNS Zone Properties Aging/Scavenging tab showing No-refresh interval and Refresh interval settings.]

Dynamic DNS creates a maintenance problem: when computers change IP addresses or are decommissioned, their old DNS records may remain in the zone forever — stale records that can cause resolution failures or security issues.

**DNS Aging and Scavenging** solves this automatically. When aging is enabled on a zone, each dynamically registered record gets a timestamp. The aging mechanism has two intervals:

- **No-refresh interval (default 7 days):** The period during which a record's timestamp is not refreshed even if the client re-registers. This prevents constant write activity on the zone.
- **Refresh interval (default 7 days):** After the no-refresh period, clients can refresh their record timestamps. Records with timestamps older than the refresh interval become eligible for scavenging.
- **Scavenging interval:** How often the DNS server automatically removes stale records.

Total aging before scavenging = no-refresh + refresh = 14 days by default.

Important: Only dynamically registered records are eligible for scavenging. Manually created static records are never scavenged.

---

### [SEGMENT 7 — DHCP Fundamentals]

**[SHOW SCREEN: Diagram showing DHCP DORA process — Discover, Offer, Request, Acknowledge]**

[Alt-text: A four-step DORA diagram showing: 1 Client broadcasts Discover, 2 DHCP Server sends Offer with available IP, 3 Client broadcasts Request for offered IP, 4 Server sends Acknowledge confirming the lease.]

DHCP — Dynamic Host Configuration Protocol — automatically assigns IP addresses and network configuration to client computers. The four-step DORA process:

1. **Discover:** Client broadcasts a DHCP Discover message looking for any DHCP server on the network.
2. **Offer:** DHCP server responds with an IP address offer, including subnet mask, gateway, lease time, and DNS server addresses.
3. **Request:** Client broadcasts acceptance of the offered address (broadcast so other DHCP servers know the offer was accepted).
4. **Acknowledge:** DHCP server confirms the lease assignment.

DHCP eliminates the need to manually configure static IP addresses on client workstations — which would be completely impractical in a network with thousands of clients.

---

### [SEGMENT 8 — DHCP Scopes, Reservations, and Options]

**[SHOW SCREEN: DHCP Manager showing a scope with its exclusions, reservations, and scope options]**

[Alt-text: DHCP Manager console tree showing a scope named 192.168.10.0/24 with child nodes for Address Pool, Address Leases, Reservations, and Scope Options.]

A **DHCP Scope** is a range of IP addresses that the DHCP server can assign to clients on a specific subnet. One scope per subnet.

**Key scope concepts:**

**Address Pool:** The range of addresses the scope can lease. Example: `192.168.10.100` to `192.168.10.200`.

**Exclusion Range:** Addresses within the scope range that the DHCP server will never lease. Use exclusions to protect addresses you have statically assigned to servers, printers, or network equipment. Example: exclude `192.168.10.100` to `192.168.10.110` for static devices.

**DHCP Reservation:** Binds a specific IP address to a specific client by MAC address. The reserved address is always offered to that client regardless of normal lease assignment. Use reservations for devices like printers and servers that need consistent addressing but you want managed through DHCP rather than static configuration.

**Scope Options:** Additional configuration delivered to clients with each lease. Common options:

| Option | Purpose | Example |
|---|---|---|
| 003 Router | Default gateway | `192.168.10.1` |
| 006 DNS Servers | DNS server addresses | `192.168.10.10`, `192.168.10.20` |
| 015 DNS Domain Name | DNS suffix for search | `corp.local` |
| 044 WINS Servers | Legacy WINS server (rarely needed) | Not typically configured |

---

### [SEGMENT 9 — DHCP High Availability: Failover]

**[SHOW SCREEN: Diagram showing DHCP Failover topology with Active/Passive (Hot Standby) and Load Balance modes]**

[Alt-text: Two diagrams showing DHCP Failover modes: Hot Standby where Primary handles all leases and Standby takes over only if Primary fails; and Load Balance where both servers share the scope address pool and both serve leases simultaneously.]

A single DHCP server is a critical single point of failure. If it goes offline, new clients and renewals fail.

**DHCP Failover** solves this by coordinating a single scope between two DHCP servers.

**Load Balance mode:** Both servers share the address pool. By default the pool is split 50/50 between the two servers. Both actively serve leases simultaneously. If one fails, the other serves from the entire pool.

**Hot Standby mode:** One server is Active and handles all leases normally. The Standby server only activates and serves leases if the Active server is unreachable. Simpler to manage but all active load is on one server.

DHCP Failover eliminates the address conflict problems that occurred with the old "split scope" approach (where each server had a non-overlapping range), which required careful manual management and did not truly provide failover.

---

### [SEGMENT 10 — DHCP Authorization in Active Directory]

**[SHOW SCREEN: DHCP Manager showing Authorized DHCP Servers in the domain]**

[Alt-text: DHCP Manager console showing the domain with an authorized DHCP server icon and a rogue DHCP server shown as unauthorized.]

In an Active Directory domain, DHCP servers must be **authorized** before they can serve leases to domain-joined clients. This prevents rogue DHCP servers from handing out incorrect IP addresses and potentially hijacking network traffic.

Authorization is stored in the Configuration partition of the AD forest. When a DHCP server starts, it queries AD to verify it is authorized. If it is not found in the authorized list, it refuses to serve leases.

Non-domain DHCP servers (standalone) do not perform authorization checks — they serve leases regardless. This is why corporate networks should have domain-joined and authorized DHCP servers to prevent unauthorized DHCP from operating.

```powershell
# Authorize a DHCP server in Active Directory
Add-DhcpServerInDC -DnsName "DHCP1.corp.local" -IPAddress 192.168.10.30

# Verify authorized DHCP servers
Get-DhcpServerInDC
```

---

### [SEGMENT 11 — Summary and Part 2 Preview]

**[SHOW SCREEN: Summary slide]**

Part 1 covered DNS record types, zone types (primary, secondary, stub, AD-integrated), dynamic update security, forwarders and conditional forwarders, aging and scavenging, DHCP DORA process, scopes with exclusions and reservations, scope options, DHCP failover modes, and DHCP authorization.

In Part 2 we will install and configure both DNS and DHCP using Server Manager and PowerShell, demonstrate configuring a scope, setting up a reservation, and verify DNS resolution.

---

### Additional Resources

- [DNS Server overview](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-overview)
- [DHCP Server overview](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-deploy-wps)
- [DHCP Failover](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn338978(v=ws.11))
- [DNS Aging and Scavenging](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc758485(v=ws.10))

---

*End of Part 1. Continue to Part 2 for demonstrations, PowerShell commands, exam tips, and lab preview.*
