# Video Script: Module 09 — DNS and DHCP Services in Windows Server (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Introduction

Welcome back to CIS-3326 Windows Server Administration.

I am Professor Nash. Module 09 covers two foundational network services that
every Windows domain depends on: DNS and DHCP.

DNS — the Domain Name System — translates hostnames to IP addresses. Without
DNS, Active Directory does not function at all. DHCP — the Dynamic Host
Configuration Protocol — automatically assigns IP addresses to client computers.
Together, these two services form the network identity layer that everything
else in your infrastructure builds on.

Part 1 covers the concepts and architecture of both services. Part 2 covers
installation, configuration, and troubleshooting with PowerShell.

---

## Section 1: DNS — The Foundation of Active Directory

Before we discuss DNS configuration, let us understand why DNS is so critical
to Active Directory.

When a client computer joins a domain and a user logs on, the following DNS
lookups happen in milliseconds:

1. The client looks up the SRV record `_ldap._tcp.dc._msdcs.txwes.edu` to find
   a domain controller.

2. The client contacts the domain controller found in the SRV record.

3. The client looks up the Kerberos KDC service via another SRV record.

4. Authentication proceeds.

If DNS is broken, none of this works. The user sees "The domain could not be
contacted." The fix is almost always DNS.

Windows Server DNS is tightly integrated with Active Directory through
**AD-Integrated DNS zones**, which store DNS records as Active Directory objects
rather than in flat text files.

---

## Section 2: DNS Zone Types

Windows Server DNS supports several zone types:

### Primary Zone

The authoritative read-write copy of a zone. DNS changes are made here. In a
non-AD-integrated environment, this is a flat file on the DNS server.

### Secondary Zone

A read-only copy of a zone obtained from a Primary zone server via zone transfer.
Provides redundancy and distributes query load. Secondary zones receive updates
through zone transfer, not through direct editing.

### Stub Zone

A stripped-down zone that contains only the SOA record, NS records, and A records
for the zone's authoritative name servers. Used to help DNS servers locate the
authoritative servers for a delegated child zone without maintaining a full
secondary copy.

### AD-Integrated Primary Zone

The recommended configuration for Windows domain environments. Zone data is
stored in Active Directory as objects rather than text files. This provides:

- **Multi-master replication** — any domain controller running DNS can accept
  zone record updates.

- **Secure dynamic updates** — only domain-joined computers with valid
  credentials can register or update their DNS records.

- **Automatic replication** — zone data replicates with AD replication; no
  separate DNS zone transfer configuration is needed.

For Active Directory environments, always use AD-Integrated zones.

---

## Section 3: DNS Record Types

Here are the DNS record types that appear most frequently in Windows environments:

- **A record** — maps a hostname to an IPv4 address.
  Example: `DC1.txwes.edu` resolves to `192.168.10.10`

- **AAAA record** — maps a hostname to an IPv6 address.

- **PTR record** — reverse lookup; maps an IP address to a hostname.
  Example: `10.10.168.192.in-addr.arpa` resolves to `DC1.txwes.edu`

- **CNAME record** — canonical name alias; maps one name to another name.
  Example: `mail.txwes.edu` maps to `DC1.txwes.edu`

- **MX record** — mail exchanger; specifies the server responsible for
  receiving email for the domain.

- **SRV record** — service record; used by Active Directory to advertise the
  locations of domain controllers, KDCs, and Global Catalog servers.

- **NS record** — name server; identifies the authoritative DNS servers for
  a zone.

- **SOA record** — Start of Authority; contains the primary name server and
  administrative contact for the zone, along with serial number and TTL values.

---

## Section 4: DNS Forwarders and Conditional Forwarders

By default, a Windows DNS server uses **root hints** to resolve names for
zones it is not authoritative for — it queries root servers and walks the DNS
hierarchy to find the authoritative server.

**Forwarders** simplify this. You configure a forwarder to send all non-local
DNS queries to a specified external server such as your ISP's DNS server, Google
8.8.8.8, or your corporate upstream DNS.

```text
Without forwarders: txwes.edu DNS → Root hints → .edu TLD → Authoritative
With forwarders:    txwes.edu DNS → Forwarder (8.8.8.8) → Google resolves it
```

**Conditional Forwarders** take this further. They forward queries for a
specific domain to a specific server.

Use case: If you have a partner company's domain `partner.com`, you create a
conditional forwarder for `partner.com` pointing to the partner company's DNS
server. Queries for `*.partner.com` go directly to their DNS server, while all
other external queries go to your normal forwarder.

---

## Section 5: DNS Scavenging

Over time, DNS zones accumulate stale records — IP addresses that were
registered by computers that have since been decommissioned, moved, or have
changed addresses. These stale records cause resolution failures and name
collisions.

**DNS Scavenging** is the automatic cleanup mechanism that removes stale dynamic
DNS records based on a time-based aging algorithm.

Key scavenging concepts:

- **No-refresh interval** — the period after registration during which the
  record cannot be refreshed. Default: 7 days.

- **Refresh interval** — the period after the no-refresh interval during which
  the record must be refreshed or it is considered stale and eligible for
  deletion. Default: 7 days.

- **Scavenging period** — how often the DNS server checks for and removes
  stale records. Default: 7 days.

Total time before a stale record is deleted = no-refresh + refresh + scavenging
= 21 days by default.

Scavenging must be enabled on **both** the DNS server and the specific zone for
it to take effect.

---

## Section 6: DHCP Fundamentals

**DHCP (Dynamic Host Configuration Protocol)** automates IP address assignment.
Without DHCP, every device on your network requires manual IP configuration.
With DHCP, a client computer broadcasts a request and the DHCP server responds
with an IP address, subnet mask, default gateway, DNS server address, and lease
duration.

The DHCP conversation uses four messages, remembered with the acronym **DORA**:

1. **Discover** — client broadcasts: "Is there a DHCP server?"

2. **Offer** — DHCP server responds with an available IP address and lease terms.

3. **Request** — client broadcasts: "I want the IP that server offered."

4. **Acknowledge** — server confirms the assignment and the client configures
   its adapter.

---

## Section 7: DHCP Scope Configuration

A **scope** is a pool of IP addresses that a DHCP server can assign to clients
on a specific subnet.

Key scope components:

- **Scope address range** — the start and end IP addresses of the pool.

- **Subnet mask** — defines the network boundary.

- **Exclusion ranges** — IP addresses within the scope range that should not
  be assigned, reserved for static devices like servers and printers.

- **Reservations** — a specific IP address permanently bound to a specific
  client based on the client's MAC address. The client always receives the same
  IP address.

- **Lease duration** — how long a client holds the assigned IP before it must
  renew. Default: 8 days. Shorter leases suit high-turnover environments.

- **Scope options** — additional configuration delivered with the lease: Option
  003 (Default Gateway), Option 006 (DNS Servers), Option 015 (DNS Domain Name),
  Option 044 (WINS Server).

---

## Section 8: DHCP Superscopes and Failover

### Superscopes

A **superscope** is a container that groups multiple scopes on the same DHCP
server. Superscopes are used when a single network segment has multiple logical
IP subnets — a configuration called multinetting. By grouping scopes into a
superscope, the DHCP server can serve clients on any of the subnets from the
same network interface.

### DHCP Failover

**DHCP Failover** provides redundancy by partnering two DHCP servers. Both
servers share scope information so that if one fails, the other continues
serving leases.

Two failover modes:

- **Hot Standby** — one server is Active and handles all lease assignments.
  The Standby partner only activates if the active server becomes unavailable.
  Typically the standby server holds a small reserve of addresses (default 5%).

- **Load Sharing** — both servers actively handle lease requests. The scope's
  address pool is divided between the two servers according to a configured
  percentage, with 50/50 as the default.

---

## Wrap-Up: Part 1 Summary

Let us review what we covered in Part 1:

- DNS is the foundation of Active Directory. AD-Integrated zones are the
  recommended type — they provide multi-master replication and secure dynamic
  updates.

- Zone types: Primary (read-write), Secondary (read-only replica), Stub (NS/SOA
  only), AD-Integrated Primary (stored in AD, multi-master).

- DNS record types: A, AAAA, PTR, CNAME, MX, SRV, NS, SOA.

- Forwarders send unresolved queries upstream. Conditional Forwarders route
  queries for a specific domain to a specific server.

- DNS Scavenging cleans stale records using no-refresh, refresh, and scavenging
  intervals — all must be enabled on both the server and the zone.

- DHCP uses the DORA handshake to assign IP configuration to clients.

- Scope configuration includes ranges, exclusions, reservations, lease duration,
  and scope options.

- Superscopes group multiple scopes for multinetting. DHCP Failover provides
  redundancy in Hot Standby or Load Sharing mode.

In Part 2 we install and configure both services using PowerShell, create
scopes and reservations, configure forwarders, and verify with `nslookup` and
`ipconfig /all`.

See you in Part 2.
