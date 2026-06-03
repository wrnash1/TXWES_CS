# Quiz: Module 11 — DHCP and DNS Configuration

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

## Questions: 10 | Points: 10 (1 point each)

---

## Question 1

A network engineer configures a Cisco IOS router as a DHCP server for the 10.20.0.0/24 subnet. The router's LAN interface is 10.20.0.1 and several printers use static addresses in the range 10.20.0.2–10.20.0.15. Which commands correctly configure the pool and prevent those static addresses from being assigned dynamically?

- A) `ip dhcp pool LAN` then `network 10.20.0.0 255.255.255.0` then `default-router 10.20.0.1` — no exclusion needed
- B) `ip dhcp excluded-address 10.20.0.1 10.20.0.15` then `ip dhcp pool LAN` with `network 10.20.0.0 255.255.255.0` and `default-router 10.20.0.1`
- C) `ip dhcp pool LAN` then `network 10.20.0.0 255.255.255.0` then `excluded-address 10.20.0.1 10.20.0.15`
- D) `ip dhcp excluded-address 10.20.0.0 10.20.0.15` then `ip dhcp pool LAN` with `network 10.20.0.1 255.255.255.255`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Without an excluded-address command, the DHCP server will include 10.20.0.1 through 10.20.0.15 in the dynamic pool. The gateway address and printer static addresses could be handed out to other clients, causing IP conflicts.
- B is correct: `ip dhcp excluded-address` is a global configuration command that must be entered before (or separately from) the pool configuration. Reserving 10.20.0.1 through 10.20.0.15 removes the gateway and all static printer addresses from the dynamic range. The pool then defines the subnet and gateway correctly.
- C is incorrect: `excluded-address` is not a valid DHCP pool subcommand. The command must be issued in global configuration mode as `ip dhcp excluded-address`, not inside the pool configuration.
- D is incorrect: Excluding 10.20.0.0 (the network address) is unnecessary — network addresses are never assigned to hosts. Using `network 10.20.0.1 255.255.255.255` would define a /32 pool for a single host rather than the entire /24 subnet.

---

## Question 2

A company has a single Cisco IOS DHCP server at 172.16.0.5 serving three branch subnets. Each branch is separated from the server by a router. What must be configured on each branch router to allow DHCP to function?

- A) A static route on the DHCP server pointing to each branch subnet
- B) `ip helper-address 172.16.0.5` on the router interface facing each branch subnet
- C) `ip dhcp relay 172.16.0.5` in global configuration on each router
- D) A DHCP pool on each branch router that references the central server

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: While routing between the router and the DHCP server is required, a static route alone does not cause the router to forward DHCP broadcasts. The `ip helper-address` command is specifically required to convert broadcasts to unicast and forward them to the server.
- B is correct: `ip helper-address` applied to the router interface that faces the client subnet converts the DHCP broadcast to a unicast packet destined for the DHCP server address. It populates the giaddr field so the server knows which subnet scope to use for the response.
- C is incorrect: `ip dhcp relay` is not a valid Cisco IOS command. The correct command is `ip helper-address` applied at the interface level, not in global configuration.
- D is incorrect: Creating pools on the branch routers would make those routers act as independent local DHCP servers, not relays. The scenario requires relaying to a central server, not distributing DHCP server function.

---

## Question 3

DHCP snooping is enabled on a Cisco Catalyst switch. A network administrator reports that legitimate DHCP clients on an access VLAN are no longer receiving IP addresses even though the DHCP server is reachable. What is the most likely cause?

- A) DHCP snooping must be disabled on access VLANs — it only works on trunk VLANs
- B) The uplink port connecting the switch to the DHCP server's router has not been configured as trusted
- C) DHCP snooping is blocking all UDP traffic on the switch, including data traffic
- D) The DHCP server IP address must be manually entered in the DHCP snooping configuration

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: DHCP snooping is designed to work on access VLANs. It is enabled per VLAN with `ip dhcp snooping vlan <id>` and is intended to protect exactly the access layer where client devices connect.
- B is correct: When DHCP snooping is enabled, all ports are untrusted by default. DHCP server messages (Offer and Acknowledge) arriving on untrusted ports are dropped. The uplink port facing the legitimate DHCP server or the relay router must be explicitly configured with `ip dhcp snooping trust`. Without this, Offer packets from the server are discarded at the switch and clients never receive a response.
- C is incorrect: DHCP snooping inspects DHCP packets specifically — it does not block all UDP traffic. The switch forwards non-DHCP traffic normally regardless of snooping configuration.
- D is incorrect: DHCP snooping does not require manual entry of the server IP address. It classifies ports as trusted or untrusted and validates DHCP messages based on port trust state and the binding table.

---

## Question 4

A network engineer is troubleshooting a DHCP client that is receiving an APIPA address (169.254.x.x) instead of a configured IP address from the DHCP server. The DHCP server is on a different subnet. Which condition would cause this specific symptom?

- A) The DHCP pool lease time is set too short and is expiring before the client can renew
- B) The `ip helper-address` command is missing from the interface on the gateway router facing the client subnet
- C) The DHCP pool's excluded-address range covers the entire pool and no addresses are available
- D) The DHCP server is configured with the wrong subnet mask for the client's network

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A short lease time would cause frequent renewals but the client would still receive valid IP addresses during each lease period. An APIPA address indicates the client received no DHCP response at all, not that the lease expired.
- B is correct: APIPA (Automatic Private IP Addressing) is assigned by the client's operating system when no DHCP response is received within the timeout period. When the DHCP server is on a different subnet, DHCP broadcasts cannot reach it without a relay agent. A missing `ip helper-address` on the gateway interface means broadcasts are never forwarded, resulting in no server response and an APIPA fallback.
- C is incorrect: A fully exhausted pool would cause the server to send a DHCP NAK (negative acknowledgment) or simply not respond, which could also result in APIPA. However, the question specifies the DHCP server is on a different subnet — the relay issue is the more direct and common cause of this symptom in that topology.
- D is incorrect: A wrong subnet mask in the pool would cause the client to receive an IP with an incorrect mask. The client would still receive an IP address — it would just have the wrong mask. It would not fall back to APIPA because the response was received.

---

## Question 5

Which DNS record type is used to resolve a fully qualified domain name to an IPv6 address?

- A) A record
- B) PTR record
- C) AAAA record
- D) MX record

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: An A record maps a hostname to an IPv4 (32-bit) address. The "A" stands for Address, but specifically IPv4 only. For example, `www.example.com` resolving to `93.184.216.34`.
- B is incorrect: A PTR record is used for reverse DNS lookup — mapping an IP address back to a hostname. It does not resolve hostnames to IPv6 addresses.
- C is correct: AAAA records map hostnames to IPv6 (128-bit) addresses. The name "AAAA" reflects that IPv6 is four times the length of IPv4 (four A's vs one A). For example, `www.example.com` resolving to `2606:2800:220:1:248:1893:25c8:1946`.
- D is incorrect: MX (Mail Exchanger) records identify the mail server responsible for receiving email for a domain. They do not resolve hostnames to IP addresses.

---

## Question 6

A client at 192.168.1.50 sends a DNS query for `mail.company.com`. The query is sent to an internal DNS server that is configured for split-horizon DNS. The internal DNS zone for `company.com` has an A record for `mail.company.com` pointing to 10.5.1.20. The public DNS zone has the same name pointing to 203.0.113.20. Which response does the internal client receive?

- A) 203.0.113.20 — the public IP, because DNS always uses the authoritative public record
- B) 10.5.1.20 — the internal IP, because the client queries the internal DNS server which returns the internal zone record
- C) Both addresses, because split-horizon DNS returns all matching records to the client
- D) No response, because split-horizon DNS blocks internal clients from resolving internal names

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The client is querying the internal DNS server, not a public DNS server. The internal server returns records from the internal zone. The public record is served only to external clients querying the public DNS infrastructure.
- B is correct: Split-horizon DNS maintains separate zone files for the same domain — one for internal clients and one for external clients. The internal DNS server returns the internal A record (10.5.1.20) for `mail.company.com`. This ensures internal clients reach the mail server directly using the internal IP rather than traversing NAT.
- C is incorrect: DNS responses contain the records matching the query from the zone being served. A split-horizon DNS server returns one set of records (internal or external) based on the client's source, not both simultaneously.
- D is incorrect: Split-horizon DNS does not block internal resolution — it enhances it. Internal clients receive more accurate (internal) responses rather than being blocked.

---

## Question 7

A Cisco IOS router is configured as a DHCP server. The `show ip dhcp conflict` command shows several entries. What do these entries indicate?

- A) Clients that have been denied DHCP leases due to ACL restrictions on the DHCP pool
- B) IP addresses that were found to already be in use when the DHCP server attempted to assign them, indicating manual configuration conflicts
- C) Duplicate DHCP server responses from rogue DHCP servers competing with the Cisco router
- D) Addresses in the excluded-address range that the DHCP server is tracking as reserved

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Cisco IOS DHCP does not support ACL-based lease restrictions that would generate conflict entries. The conflict table has a specific purpose unrelated to access control.
- B is correct: Before assigning an address from the pool, a Cisco IOS DHCP server pings the address to verify it is not already in use. If the ping receives a reply, the server marks that address as conflicted and moves to the next available address. Conflict entries indicate devices that are statically configured with addresses from the dynamic range. The fix is to either exclude those addresses from the pool or change the static device configurations.
- C is incorrect: DHCP snooping and the binding table track rogue server activity. The conflict table specifically records addresses the Cisco server itself found to be in use when it tried to assign them.
- D is incorrect: Excluded addresses never appear in the conflict table. They are never offered by the DHCP server in the first place, so there is no opportunity for a conflict to be detected.

---

## Question 8

During DNS resolution for `www.texaswesley.edu`, a recursive resolver sends an iterative query to a root name server. What does the root name server return?

- A) The IP address of `www.texaswesley.edu`
- B) The IP address of the authoritative name server for `texaswesley.edu`
- C) A referral to the `.edu` TLD name server
- D) A CNAME record redirecting to the actual hostname

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Root name servers do not store A records for specific hostnames. They only know which servers are authoritative for top-level domains. Resolving a complete hostname requires multiple query steps.
- B is incorrect: The root name server does not know the authoritative server for `texaswesley.edu` specifically — it only knows who handles `.edu`. The .edu TLD server is the next step that would point toward the authoritative server for `texaswesley.edu`.
- C is correct: Root name servers respond to iterative queries with a referral to the appropriate TLD (top-level domain) name server. For `www.texaswesley.edu`, the root server returns the address of the `.edu` TLD server. The recursive resolver then queries the TLD server, which refers to the authoritative server for `texaswesley.edu`, which finally returns the A record.
- D is incorrect: Root name servers do not return CNAME records. CNAMEs are stored at authoritative servers for specific domains and are returned only in the final resolution step.

---

## Question 9

A router is configured with `no ip domain-lookup` in global configuration. A network administrator types a mistyped command that the router cannot recognize. What is the effect of the `no ip domain-lookup` configuration?

- A) The router blocks all DNS resolution from DHCP clients behind it
- B) The router immediately returns an error instead of attempting to resolve the mistyped text as a hostname via DNS
- C) The router disables DHCP services that rely on the `domain-name` pool parameter
- D) The router stops advertising its own hostname to neighboring routers via routing protocols

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `no ip domain-lookup` disables DNS resolution on the router itself — it does not affect DNS forwarding or DHCP services for downstream clients. Clients can still query their DNS server normally.
- B is correct: By default, when a Cisco IOS router encounters an unrecognized input, it attempts to resolve the text as a hostname using DNS. This causes a long delay (up to 30 seconds) while the router waits for a DNS timeout. `no ip domain-lookup` disables this behavior, causing the router to immediately return an error message. This is a common lab best practice.
- C is incorrect: The `domain-name` parameter in a DHCP pool is delivered to clients as a configuration parameter. It is not dependent on the router's own DNS lookup being enabled or disabled.
- D is incorrect: DNS lookup has no relationship to routing protocol advertisement of hostnames. Routing protocols advertise network prefixes and router IDs, not hostnames.

---

## Question 10

An engineer configures a Cisco DHCP pool and sets the `default-router` to 192.168.5.1 and `dns-server` to 10.0.0.53. A client receives an IP from the pool but cannot resolve hostnames. Pinging 10.0.0.53 from the client succeeds. What is the most likely cause?

- A) The DHCP pool lease time is too short and the DNS settings expire before the client uses them
- B) The DNS server at 10.0.0.53 is not configured to respond to queries for the client's requested domain
- C) The `dns-server` command in the DHCP pool was not saved to NVRAM before the router reloaded
- D) The `ip domain-lookup` command is missing from the DHCP pool configuration

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: DHCP lease time governs IP address assignment duration, not DNS TTL. DNS configuration parameters delivered via DHCP are persistent in the client OS until the lease is renewed with different parameters or manually changed.
- B is correct: The client can reach the DNS server (confirmed by ping), so the IP connectivity, DHCP assignment, and routing are all working correctly. The failure is at the DNS application layer. The DNS server at 10.0.0.53 is either not authoritative for the queried domain, has no forwarding configured to public DNS, or is configured to refuse certain client queries. This is a DNS server configuration issue, not a DHCP configuration issue.
- C is incorrect: If the router reloaded without saving, the DHCP pool itself would be missing and clients would not receive any IP address. The scenario confirms clients are receiving IPs from the pool, so the configuration survived.
- D is incorrect: `ip domain-lookup` is a router-level command that controls whether the router itself performs DNS resolution. It is not a DHCP pool subcommand and does not affect what DNS settings are delivered to clients.
