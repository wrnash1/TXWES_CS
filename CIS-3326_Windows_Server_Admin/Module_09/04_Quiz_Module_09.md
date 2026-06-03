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
