# Quiz: Module 09 — DNS and DHCP Services in Windows Server

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points.

---

## Question 1

You are configuring DNS for a new Windows Server domain. Your manager requires that
only domain-joined computers be allowed to register DNS records automatically, and
that DNS records replicate to all domain controllers without manual zone transfer
configuration. Which DNS zone type and dynamic update setting satisfy both requirements?

A. Standard Primary zone with Nonsecure and Secure dynamic updates

B. AD-Integrated Primary zone with Secure dynamic updates

C. Secondary zone with Nonsecure dynamic updates

D. Stub zone with Secure dynamic updates

**Correct Answer: B**

**Distractor Analysis:**

- **A** — Standard Primary stores data in a flat file and requires manual zone
  transfer configuration for replication. Nonsecure and Secure allows
  unauthenticated clients to register records, violating the requirement.

- **B** — Correct. AD-Integrated stores DNS in Active Directory, replicating
  automatically with AD replication. Secure dynamic updates require domain
  credentials, allowing only domain-joined computers to register records.

- **C** — Secondary zones are read-only and cannot accept dynamic updates at all.

- **D** — Stub zones contain only SOA, NS, and glue A records. They do not
  accept dynamic registrations from clients.

---

## Question 2

Your DNS administrator enables scavenging on the DNS server using
`Set-DnsServerScavenging -ScavengingState $true`. The next day, stale records
are still accumulating in the `txwes.edu` zone. What is the most likely cause?

A. The scavenging interval is set to 0 days

B. Zone-level aging has not been enabled on the `txwes.edu` zone

C. The DNS Server service must be restarted before scavenging takes effect

D. Scavenging only applies to secondary zones, not AD-Integrated zones

**Correct Answer: B**

**Distractor Analysis:**

- **A** — A scavenging interval of 0 would disable the schedule, but the
  question states scavenging was enabled with the cmdlet. The fundamental
  issue is that both conditions must be met.

- **B** — Correct. Scavenging requires two independent settings: server-level
  scavenging enabled AND zone-level aging enabled on each specific zone.
  Enabling only the server has no effect on individual zones.

- **C** — The DNS Server service does not need to be restarted; scavenging
  settings take effect immediately.

- **D** — Scavenging applies to any zone type, including AD-Integrated zones.

---

## Question 3

A technician installs the DHCP Server role on a member server in the `txwes.edu`
domain. After creating and activating a scope, client computers receive
169.254.x.x addresses instead of addresses from the scope. What is the most
likely cause?

A. The DHCP scope exclusion range is configured incorrectly

B. The DHCP server has not been authorized in Active Directory

C. The DNS domain name scope option has not been configured

D. The lease duration is set too short

**Correct Answer: B**

**Distractor Analysis:**

- **A** — An incorrect exclusion range would reduce available addresses but
  would not cause clients to receive APIPA addresses.

- **B** — Correct. APIPA addresses (169.254.x.x) indicate the client received
  no DHCP response. In a Windows domain, the DHCP Server service detects
  whether the server is authorized in AD. An unauthorized server does not
  respond to client requests.

- **C** — A missing DNS domain name option (Option 015) would cause the client
  to lack a DNS suffix but would not prevent IP assignment.

- **D** — Lease duration affects how long an IP is held, not whether the
  server responds at all.

---

## Question 4

A campus printer must always receive IP address 192.168.10.150 from DHCP. The
network administrator creates a DHCP reservation for the printer's MAC address
bound to 192.168.10.150. A new technician notices that 192.168.10.150 is within
the scope range (192.168.10.100–200) and manually configures the printer with a
static IP of 192.168.10.150, removing it from DHCP. What risk does this create?

A. The DHCP server will assign 192.168.10.150 to another client because the
   reservation was removed

B. The reservation address is still never assigned to other DHCP clients, so
   there is no risk

C. Clients that previously communicated with the printer will lose connectivity
   because the PTR record will be deleted

D. The DHCP scope will automatically expand to avoid the static address

**Correct Answer: A**

**Distractor Analysis:**

- **A** — Correct. A DHCP reservation binds a specific IP to a MAC address and
  prevents that IP from being assigned to any other client. If the reservation
  is removed (or the printer is taken off DHCP), the IP re-enters the dynamic
  pool and may be assigned to another device, causing an IP conflict.

- **B** — The reservation prevents re-assignment only while it exists. Without
  the reservation entry, the DHCP server has no mechanism to protect that IP.

- **C** — PTR record deletion is unrelated to the reservation mechanism and
  does not cause IP conflicts.

- **D** — DHCP scopes do not automatically expand or contract based on static
  assignments outside the server's reservation table.

---

## Question 5

You need to configure two DHCP servers so that if the primary server fails,
the secondary server immediately begins responding to client requests using
the same scope. During normal operation only the primary server responds.
Which DHCP failover mode should you configure?

A. Load Sharing with a 50/50 pool split

B. Hot Standby with the primary server as Active

C. Load Sharing with a 95/5 pool split

D. Hot Standby with the secondary server as Active

**Correct Answer: B**

**Distractor Analysis:**

- **A** — Load Sharing keeps both servers active simultaneously and splits
  the address pool. This does not match the requirement for only the primary
  to respond during normal operation.

- **B** — Correct. Hot Standby mode designates one server as Active (handles
  all leases during normal operation) and one as Standby (only activates when
  the Active server is unreachable). This matches the described requirement.

- **C** — A 95/5 Load Sharing split resembles Hot Standby in pool size but
  still keeps both servers active for 5% of requests.

- **D** — If the secondary is Active in Hot Standby, the primary becomes the
  Standby. This inverts the desired behavior.

---

## Question 6

You add a conditional forwarder for `partner.com` pointing to `10.200.1.10`
using `Add-DnsServerConditionalForwarderZone -ReplicationScope Domain`. A user
queries `www.partner.com`. How does DC1 resolve this name?

A. DC1 queries root hints and walks the DNS hierarchy to find `partner.com`

B. DC1 forwards the query directly to `10.200.1.10` without querying root hints

C. DC1 checks the local zone cache and returns NXDOMAIN if no record is found

D. DC1 forwards the query to the standard forwarder (8.8.8.8) before trying
   the conditional forwarder

**Correct Answer: B**

**Distractor Analysis:**

- **A** — Root hints are used only when no forwarder matches the queried
  domain. A conditional forwarder for `partner.com` matches `www.partner.com`
  and takes precedence over root hints.

- **B** — Correct. A conditional forwarder routes all queries matching the
  configured domain name directly to the specified server. The query for
  `www.partner.com` matches the `partner.com` conditional forwarder and is
  sent to `10.200.1.10`.

- **C** — NXDOMAIN would only be returned if the local server were authoritative
  for the zone. The conditional forwarder delegates external queries.

- **D** — Conditional forwarders take precedence over standard forwarders.
  A query matching a conditional forwarder domain is sent to the conditional
  forwarder's target, not the standard forwarder.

---

## Question 7

After promoting DC1 as the first domain controller for `txwes.edu`, a
technician reports that client computers can resolve hostnames but cannot log
on to the domain. You run `Resolve-DnsName -Name "_ldap._tcp.dc._msdcs.txwes.edu"
-Type SRV` and receive no results. What is the most likely cause?

A. The DHCP server has not been authorized in Active Directory

B. The reverse lookup zone has not been created

C. The SRV records for Active Directory were not registered in DNS

D. The conditional forwarder for `txwes.edu` is misconfigured

**Correct Answer: C**

**Distractor Analysis:**

- **A** — DHCP authorization affects IP address assignment. Clients can
  already resolve hostnames, meaning they have connectivity and DNS is working
  for A records.

- **B** — The reverse lookup zone handles IP-to-hostname lookups. Its absence
  does not prevent SRV record registration or domain logon.

- **C** — Correct. Active Directory relies on SRV records such as
  `_ldap._tcp.dc._msdcs.txwes.edu` for clients to locate domain controllers.
  If the `netlogon` service on DC1 did not register these records, or if DNS
  has a problem accepting dynamic updates, domain logon fails.

- **D** — A conditional forwarder routes external queries. The `txwes.edu`
  zone is local; a conditional forwarder would not affect internal SRV record
  resolution.

---

## Question 8

A DHCP scope covers 192.168.10.100–192.168.10.200. An exclusion range is
configured for 192.168.10.100–192.168.10.109. A reservation is configured for
192.168.10.150 bound to MAC `00-AA-BB-CC-DD-EE`. Which addresses can the DHCP
server dynamically assign to clients without reservations?

A. 192.168.10.100–192.168.10.200 minus 192.168.10.150

B. 192.168.10.110–192.168.10.200

C. 192.168.10.110–192.168.10.149 and 192.168.10.151–192.168.10.200

D. 192.168.10.100–192.168.10.109 and 192.168.10.150

**Correct Answer: C**

**Distractor Analysis:**

- **A** — This ignores the exclusion range. The excluded addresses
  (100–109) are withheld from the dynamic pool.

- **B** — This correctly removes the excluded range but ignores the
  reservation. A reserved address is never dynamically assigned to a
  non-matching client.

- **C** — Correct. The exclusion removes .100–.109 from the pool. The
  reservation removes .150 from dynamic assignment. The remaining dynamic
  pool is .110–.149 and .151–.200.

- **D** — These are the excluded and reserved addresses — the opposite
  of what is dynamically assignable.

---

## Question 9

A network administrator enables DNS scavenging with default intervals:
no-refresh 7 days, refresh 7 days, scavenging 7 days. A workstation registers
a DNS record on Monday and is decommissioned the same day without removing its
DNS record. Assuming the scavenging cycle runs on schedule, on what day is the
stale record deleted?

A. The following Monday (7 days later)

B. The Monday after that (14 days later)

C. Monday three weeks later (21 days later)

D. Monday four weeks later (28 days later)

**Correct Answer: C**

**Distractor Analysis:**

- **A** — 7 days covers only the no-refresh interval. The record cannot
  even be refreshed during this period, let alone deleted.

- **B** — 14 days covers the no-refresh and refresh intervals. The record
  becomes stale at 14 days, but the scavenging cycle has not run yet.

- **C** — Correct. Total time = no-refresh (7) + refresh (7) + scavenging
  interval (7) = 21 days. The record becomes eligible for deletion after
  14 days, and scavenging deletes it when the next scavenging cycle runs at
  day 21.

- **D** — 28 days exceeds the correct calculation. The scavenging interval
  adds 7 days after the record becomes stale, not 14.

---

## Question 10

You configure a DHCP reservation for a device at scope level. You also configure
scope-level Option 006 (DNS Servers) with `192.168.10.10`. You configure a
reservation-level Option 006 with `192.168.10.10` and `192.168.10.11`. Which
DNS servers will the reserved device receive?

A. Only `192.168.10.10` from the scope-level option

B. Only `192.168.10.10` and `192.168.10.11` from the reservation-level option

C. Both options are merged, so the device receives three DNS server entries

D. The server-level option overrides reservation-level options

**Correct Answer: B**

**Distractor Analysis:**

- **A** — Scope-level options are overridden by reservation-level options
  when both configure the same option code. The higher-specificity level wins.

- **B** — Correct. DHCP option precedence from lowest to highest is:
  server level, scope level, reservation level. Reservation-level options
  override scope-level options for the same option code. The device receives
  Option 006 from the reservation.

- **C** — DHCP options are not merged across levels for the same option code.
  The highest-priority level's value replaces lower-level values.

- **D** — Server-level options are the lowest priority, overridden by both
  scope-level and reservation-level options.

---

*Submit answers to Canvas by the due date shown in the course schedule.*

---

### Question 11 (5 points)

You need to create a reverse lookup zone for the subnet `192.168.20.0/24` on DC1.
Which PowerShell command creates the correct AD-Integrated reverse lookup zone?

- A) `Add-DnsServerPrimaryZone -Name "20.168.192.in-addr.arpa" -ReplicationScope Domain`
- B) `Add-DnsServerPrimaryZone -Name "192.168.20.in-addr.arpa" -ReplicationScope Domain`
- C) `Add-DnsServerSecondaryZone -Name "20.168.192.in-addr.arpa" -ZoneFile "20.168.192.in-addr.arpa.dns"`
- D) `Add-DnsServerPrimaryZone -NetworkId "192.168.20.0/24" -ZoneFile "reverse.dns"`

- **Correct Answer: A**
- **Distractor Analysis:**
  - **A** — Correct. Reverse lookup zones follow the octets in reverse order. For `192.168.20.0/24`, the zone name is `20.168.192.in-addr.arpa`. `-ReplicationScope Domain` creates an AD-Integrated zone replicated to all DCs.
  - **B** — The octets are not reversed. `192.168.20.in-addr.arpa` is not a valid reverse zone name for this subnet.
  - **C** — A Secondary zone requires a master server and uses file-based storage, not AD integration. The zone name is correct but the zone type and storage are wrong.
  - **D** — `-NetworkId` is a valid parameter that auto-generates the zone name, but `-ZoneFile` creates a file-backed zone, not an AD-Integrated zone. Use `-ReplicationScope` for AD integration.

---

### Question 12 (5 points)

A technician runs `nslookup` to verify that DC1 has registered its SRV records after
domain promotion. Which `nslookup` command confirms that the LDAP SRV record for
`txwes.edu` exists?

- A) `nslookup -type=SRV _ldap._tcp.dc._msdcs.txwes.edu`
- B) `nslookup -type=A dc1.txwes.edu`
- C) `nslookup -type=MX txwes.edu`
- D) `nslookup -type=PTR 192.168.10.10`

- **Correct Answer: A**
- **Distractor Analysis:**
  - **A** — Correct. LDAP SRV records are stored under `_ldap._tcp.dc._msdcs.<domain>`. Using `-type=SRV` queries the DNS server for that service locator record, which domain clients use to find domain controllers.
  - **B** — `-type=A` queries for a host address record. It confirms DC1 has an A record but does not verify SRV record registration.
  - **C** — `-type=MX` queries for mail exchanger records, which are unrelated to domain controller location.
  - **D** — `-type=PTR` queries a reverse lookup zone for a hostname. It verifies pointer records, not SRV records.

---

### Question 13 (5 points)

Your organization has two separate subnets: `10.1.0.0/24` (Building A) and
`10.2.0.0/24` (Building B). A single DHCP server services both subnets via relay
agents. You create two separate scopes. Which DHCP feature lets you manage both
scopes as a single administrative unit and activate/deactivate them together?

- A) DHCP Failover
- B) Split Scope
- C) Superscope
- D) Multicast Scope

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — DHCP Failover provides redundancy between two DHCP servers for the same scope. It does not group separate scopes for administrative management.
  - **B** — Split Scope divides a single scope across two DHCP servers for redundancy. It does not group distinct subnets.
  - **C** — Correct. A Superscope is an administrative grouping of multiple child scopes. It allows an administrator to activate, deactivate, and manage multiple scopes together — useful when a single server handles multiple subnets.
  - **D** — A Multicast Scope assigns multicast IP addresses (Class D range 224.0.0.0–239.255.255.255) to multicast applications. It is unrelated to unicast subnet management.

---

### Question 14 (5 points)

A Windows client has cached a DNS record for `server1.txwes.edu` that now points
to an old IP address. The DNS administrator has already updated the A record on
the DNS server. Which command on the client clears the local DNS resolver cache
so the next query retrieves the updated record?

- A) `ipconfig /release`
- B) `ipconfig /flushdns`
- C) `ipconfig /registerdns`
- D) `Clear-DnsServerCache`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `ipconfig /release` releases the DHCP-assigned IP address. It does not affect the DNS resolver cache.
  - **B** — Correct. `ipconfig /flushdns` clears the client-side DNS resolver cache. The next query for `server1.txwes.edu` goes to the DNS server and retrieves the updated record.
  - **C** — `ipconfig /registerdns` triggers the client to re-register its own A and PTR records in DNS. It does not flush cached records.
  - **D** — `Clear-DnsServerCache` clears the DNS server's cache on the server side. It has no effect on a client's local resolver cache.

---

### Question 15 (5 points)

You examine the DHCP audit log on DC1 and find Event ID 11 repeated multiple
times for the same MAC address within one minute. What does Event ID 11 indicate
in a DHCP audit log?

- A) A new lease was successfully issued
- B) A lease was renewed by a client
- C) A request was declined because the address is already in use
- D) The DHCP service was paused

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — Event ID 10 indicates a new lease was issued. Event ID 11 indicates a different condition.
  - **B** — Event ID 12 indicates a lease renewal. Renewals are expected and occur periodically.
  - **C** — Correct. Event ID 11 is "Decline" — the client sent a DHCPDECLINE message because it detected the offered address is already in use on the network (conflict detected via ARP probe). Repeated declines for the same MAC may indicate IP address conflicts or a rogue device.
  - **D** — DHCP service pause events use different log entries. Event ID 11 is specifically a client decline event.

---

### Question 16 (5 points)

An administrator needs to add a conditional forwarder for `lab.internal` pointing
to `172.16.0.1` so that DNS queries for that domain route to the lab's DNS server.
Which PowerShell command accomplishes this?

- A) `Add-DnsServerForwarder -IPAddress 172.16.0.1 -PassThru`
- B) `Add-DnsServerConditionalForwarderZone -Name "lab.internal" -MasterServers 172.16.0.1`
- C) `New-DnsServerZone -Name "lab.internal" -ReplicationScope Domain`
- D) `Set-DnsServerForwarder -IPAddress 172.16.0.1 -UseRootHint $false`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Add-DnsServerForwarder` adds a standard forwarder that handles all unresolved queries. It does not restrict forwarding to a specific domain name.
  - **B** — Correct. `Add-DnsServerConditionalForwarderZone` creates a zone of type conditional forwarder. `-Name` specifies the domain whose queries should be forwarded, and `-MasterServers` specifies the target DNS server IP.
  - **C** — `New-DnsServerZone` creates a primary or secondary zone, making the server authoritative for that domain — not appropriate for forwarding to another server.
  - **D** — `Set-DnsServerForwarder` modifies global forwarder settings. It does not create domain-specific conditional forwarding rules.

---

### Question 17 (5 points)

A DNS zone has aging enabled with a no-refresh interval of 7 days and a refresh
interval of 7 days. A client workstation's A record has a timestamp of 08:00 on
Day 1. The workstation successfully renews its DHCP lease at 10:00 on Day 3 and
again at 08:00 on Day 10. Will the DNS record timestamp be updated on Day 3?

- A) Yes — any DHCP renewal triggers a DNS record refresh
- B) No — the record is within the no-refresh interval and cannot be updated yet
- C) Yes — secure dynamic updates always refresh the timestamp on renewal
- D) No — dynamic updates are only accepted from domain controllers

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — DHCP renewal does attempt to refresh DNS, but the DNS server rejects refresh requests during the no-refresh interval to reduce replication traffic.
  - **B** — Correct. The no-refresh interval (7 days here) prevents DNS from updating a record's timestamp before it expires. Day 3 is within the no-refresh interval, so the refresh attempt at Day 3 is rejected. The record can first be refreshed after Day 8 (Day 1 + 7 days).
  - **C** — Secure dynamic updates restrict who can update records but do not bypass the no-refresh interval.
  - **D** — Domain-joined computers with Secure Only updates can register and refresh their own records. Clients — not only DCs — are authorized to update their own A records.

---

### Question 18 (5 points)

You run `Get-DhcpServerv4ScopeStatistics -ScopeId 192.168.10.0` and notice the
`PercentageInUse` is 97%. Which action best addresses the risk of address
exhaustion while minimizing disruption?

- A) Reduce the lease duration from 8 days to 1 day to reclaim addresses faster
- B) Extend the scope range by modifying the end address with `Set-DhcpServerv4Scope`
- C) Enable DHCP Failover in Load Balance mode with a second DHCP server
- D) Delete all existing leases to free the address pool immediately

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Reducing lease duration causes more frequent renewals and increases DHCP server load. It does not add addresses to the pool; it only reclaims expired leases faster.
  - **B** — Correct. `Set-DhcpServerv4Scope -ScopeId 192.168.10.0 -EndRange <new end>` expands the scope's assignable range, directly increasing the number of available addresses. This is the most direct solution to address exhaustion.
  - **C** — DHCP Failover distributes leases across two servers but does not increase the total number of addresses in the scope. Both servers share the same pool.
  - **D** — Deleting all leases forces all clients to request new leases simultaneously, causing network disruption. It does not increase the pool size.

---

### Question 19 (5 points)

You need to verify that DC1's DNS server is successfully resolving external names
using its configured forwarder (`8.8.8.8`). Which PowerShell command tests name
resolution from the perspective of the DNS server itself (not the local client resolver)?

- A) `Resolve-DnsName -Name "microsoft.com"`
- B) `Test-NetConnection -ComputerName "microsoft.com" -Port 443`
- C) `Resolve-DnsName -Name "microsoft.com" -Server 127.0.0.1`
- D) `nslookup microsoft.com 8.8.8.8`

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — `Resolve-DnsName` without `-Server` uses the client's configured DNS server, which may not be DC1. This tests client resolution, not the server's forwarder configuration.
  - **B** — `Test-NetConnection` tests TCP connectivity to port 443. It does not test DNS resolution behavior.
  - **C** — Correct. `-Server 127.0.0.1` directs the query to the local DNS service on DC1. If the result resolves correctly, DC1's forwarder is working. This tests the server's resolution chain including its forwarder.
  - **D** — `nslookup microsoft.com 8.8.8.8` queries `8.8.8.8` directly, bypassing DC1's DNS service. This tests Google's resolver, not DC1's forwarder configuration.

---

### Question 20 (5 points)

A DNS administrator creates a delegation in the `txwes.edu` zone pointing
`lab.txwes.edu` to a separate DNS server at `10.50.0.5`. A client queries DC1
for `fileserver.lab.txwes.edu`. How does DC1 resolve this query?

- A) DC1 checks its local zone file for `fileserver.lab.txwes.edu` and returns NXDOMAIN
- B) DC1 recognizes the delegation and refers the client to `10.50.0.5` to complete the query
- C) DC1 forwards the query to its configured standard forwarder
- D) DC1 returns the NS record for `lab.txwes.edu` and caches the delegation

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — DC1 is not authoritative for `lab.txwes.edu` — it delegated that namespace. It does not search its own zone file for records in the delegated subdomain.
  - **B** — Correct. A DNS delegation creates an NS record in the parent zone pointing to the child zone's authoritative server. DC1 follows the delegation and refers the query to `10.50.0.5`, which is authoritative for `lab.txwes.edu`. The client receives the answer from the delegated server.
  - **C** — Standard forwarders handle queries for domains the server has no zone information about. Because DC1 has a delegation record for `lab.txwes.edu`, it follows the delegation rather than forwarding to an external server.
  - **D** — Returning only the NS record and caching is recursive resolution behavior. DC1, as a recursive resolver, pursues the full answer on behalf of the client rather than returning a referral to the client directly.
