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

---

## Question 11

A DHCP server has a pool defined for 192.168.10.0/24 with exclusions for .1 through .10. A client sends a DHCP Discover. The server responds with an Offer containing 192.168.10.11. The client sends a Request, but before the server sends an Acknowledge, the server pings 192.168.10.11 and receives a reply. What happens next?

- A) The server sends the Acknowledge anyway and adds 192.168.10.11 to the binding table
- B) The server marks 192.168.10.11 as a conflict, moves to the next available address, and sends a new Offer
- C) The server sends a DHCP NAK to the client and terminates the process
- D) The server ignores the ping reply because only ARP is used for conflict detection

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: If the server detects the address is already in use (via ping probe), it does not assign that address. Proceeding would create an IP conflict on the network.
- B is correct: Cisco IOS DHCP servers perform a ping probe before finalizing the offer. If a ping reply is received, the server records the address in the conflict table (`show ip dhcp conflict`), skips that address, selects the next available one, and sends a new Offer to the client. This protects against conflicts with hosts statically configured using addresses from the dynamic range.
- C is incorrect: A DHCP NAK is sent when the server determines a client's requested address is incorrect (e.g., the client moved to a new subnet and requests its old address). It is not sent when the server detects a conflict during its own probe.
- D is incorrect: Cisco IOS uses ICMP ping (not ARP) for conflict detection on the server side. Clients use ARP (gratuitous ARP after receiving an address) for their own conflict detection.

---

## Question 12

A network engineer configures `ip dhcp snooping` globally but forgets to add `ip dhcp snooping vlan 10`. What is the result for VLAN 10 clients?

- A) DHCP snooping applies to all VLANs automatically when enabled globally
- B) VLAN 10 clients are unaffected — DHCP functions normally without snooping enforcement on that VLAN
- C) All DHCP traffic on VLAN 10 is dropped because the VLAN is not in the snooping database
- D) DHCP snooping only activates on VLAN 1 by default when enabled globally

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `ip dhcp snooping` alone enables the feature globally but does not activate it on any specific VLAN. DHCP snooping must be explicitly enabled per VLAN using `ip dhcp snooping vlan <id>`.
- B is correct: DHCP snooping only enforces its rules on VLANs where it has been explicitly enabled. If VLAN 10 is not listed in the `ip dhcp snooping vlan` command, snooping does not inspect or filter DHCP packets on that VLAN. Clients in VLAN 10 receive DHCP responses normally regardless of port trust state.
- C is incorrect: DHCP traffic on a VLAN without snooping enabled is simply not inspected — it is forwarded normally. Snooping does not drop traffic on VLANs where it is not enabled.
- D is incorrect: Cisco IOS does not apply snooping to VLAN 1 by default. No VLAN has snooping applied automatically — each must be explicitly configured.

---

## Question 13

Which DHCP message type does a client send to formally accept a DHCP offer after receiving it from the server?

- A) DHCP Discover
- B) DHCP Acknowledge
- C) DHCP Request
- D) DHCP Inform

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: DHCP Discover is the first message — the broadcast sent by a client that has no IP address and is searching for any available DHCP server. It is not used to accept an offer.
- B is incorrect: DHCP Acknowledge (ACK) is sent by the server as the final message, confirming the lease and delivering the full configuration. The client does not send an Acknowledge.
- C is correct: After receiving an Offer, the client broadcasts a DHCP Request to formally request the offered address from the specific server. This broadcast also notifies other servers (which may have also replied with offers) that their offers were not selected. The server then responds with a DHCP ACK to finalize the lease.
- D is incorrect: DHCP Inform is sent by a client that already has a static IP address but wants to obtain other configuration parameters (such as DNS server information) from the DHCP server. It is not part of the standard address-acquisition process.

---

## Question 14

An engineer runs `show ip dhcp binding` on a Cisco IOS DHCP server and sees no entries, but clients claim to have received IP addresses. What is the most likely explanation?

- A) DHCP bindings are only displayed while clients are actively transmitting data
- B) The DHCP server has reloaded since the last leases were assigned, and the binding table was not saved to NVRAM
- C) The clients received addresses from a different DHCP server, not from this router
- D) The binding table is only populated after the lease fully expires and is renewed

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: DHCP bindings persist in the binding table for the duration of the lease regardless of whether clients are active. The table displays all current valid leases.
- B is incorrect: While Cisco IOS can optionally save the DHCP binding database to a file (using `ip dhcp database`), a reload does not explain the absence of bindings for clients that currently have valid IPs. On reload, the server would re-issue leases and populate the table again on first client request.
- C is correct: If `show ip dhcp binding` is empty but clients have valid IPs, those clients obtained their addresses from another DHCP server on the network — either a rogue server, a second legitimate server, or a DHCP relay pointing elsewhere. This is also a sign that DHCP snooping may not be enabled, allowing rogue servers to respond.
- D is incorrect: DHCP bindings are added to the table when leases are granted — not after expiration. The table shows active leases, not expired ones.

---

## Question 15

A DNS resolver has a cached A record for `www.example.com` with a TTL of 300 seconds. A client queries the resolver 200 seconds after the record was cached. What TTL value is returned to the client?

- A) 300 seconds (the original TTL as set by the authoritative server)
- B) 100 seconds (the remaining time before the cached record expires)
- C) 0 seconds (TTL is not included in resolver responses)
- D) The resolver re-queries the authoritative server before responding to reset the TTL to 300

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: DNS resolvers do not return the original TTL from the authoritative server. They return the remaining TTL — the time left before the cached record expires. This prevents clients from caching the record longer than the authoritative server intended.
- B is correct: DNS resolvers decrement the TTL as time passes. If the record was cached with a TTL of 300 and 200 seconds have elapsed, the resolver returns the record with a TTL of 100 seconds (300 − 200). The client caches the record for its remaining 100 seconds.
- C is incorrect: TTL is always included in DNS responses. It is a mandatory field that tells the recipient how long to cache the record.
- D is incorrect: A resolver re-queries the authoritative server only after the cached TTL expires (reaches 0). As long as a valid cached record exists, the resolver serves it without contacting the authoritative server.

---

## Question 16

Which command on a Cisco router shows the IP addresses assigned to DHCP clients along with their MAC addresses and lease expiration times?

- A) `show ip dhcp pool`
- B) `show ip dhcp server statistics`
- C) `show ip dhcp binding`
- D) `show ip dhcp conflict`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `show ip dhcp pool` displays pool configuration details — subnet, total addresses, addresses in use, and available count. It does not list individual client bindings.
- B is incorrect: `show ip dhcp server statistics` shows aggregate counters — total messages sent and received, total bindings, and pool information. It does not display per-client IP-to-MAC mappings.
- C is correct: `show ip dhcp binding` is the primary command for viewing the active DHCP lease table. It displays each assigned IP address, the client's hardware (MAC) address, the lease start time, the lease expiration time, and the binding type. This is the first command to run when troubleshooting DHCP client address assignment.
- D is incorrect: `show ip dhcp conflict` displays IP addresses that the DHCP server detected were already in use when it tried to assign them. It does not show current valid client bindings.

---

## Question 17

An enterprise campus network uses a Cisco IOS router as a DHCP relay for three different VLANs. The DHCP server is on a centralized server VLAN at 10.1.1.10. Which interface configuration is required on the Layer 3 switch performing inter-VLAN routing?

- A) `ip helper-address 10.1.1.10` on the server VLAN's SVI only
- B) `ip helper-address 10.1.1.10` on each of the three client-facing VLAN SVIs
- C) `ip dhcp relay 10.1.1.10` in global configuration on the Layer 3 switch
- D) `ip helper-address 10.1.1.10` on the physical uplink port toward the server

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The helper-address on the server VLAN SVI would relay DHCP broadcasts from the server VLAN to itself, which is not meaningful. The relay must be configured on the SVIs where client broadcasts originate.
- B is correct: `ip helper-address` must be applied to each SVI (VLAN interface) that faces client devices. When a DHCP Discover broadcast arrives on a client VLAN, the SVI with the helper-address forwards it as a unicast to the DHCP server at 10.1.1.10, including the giaddr field so the server knows which subnet scope to use.
- C is incorrect: `ip dhcp relay` is not a valid Cisco IOS command. The correct command is `ip helper-address` in interface configuration mode.
- D is incorrect: Applying the helper-address to the physical uplink would only relay broadcasts that arrive on that specific physical interface. The three client VLANs use SVIs, and broadcasts arrive on those logical interfaces — not the physical uplink.

---

## Question 18

What is the purpose of the `giaddr` (gateway IP address) field in a DHCP packet?

- A) It specifies the IP address of the default gateway that the DHCP server should assign to the client
- B) It is populated by the DHCP relay agent with its own interface address to tell the server which subnet scope to use
- C) It identifies the client's current IP address before a renewal
- D) It specifies the address of the DNS server configured in the DHCP pool

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The default gateway for the client is delivered by the DHCP server in the `default-router` option (Option 3). The `giaddr` is a relay-agent field that identifies the relay, not the gateway the client should use.
- B is correct: When a DHCP relay agent (configured with `ip helper-address`) forwards a client's Discover or Request to the DHCP server, it inserts its own interface IP address into the `giaddr` field. The server reads `giaddr` to determine which subnet the client is on and selects the appropriate scope/pool for the response. Without `giaddr`, the server would not know which subnet's address range to use.
- C is incorrect: The client's current IP address in a renewal is carried in the `ciaddr` (client IP address) field, not `giaddr`. During initial discovery, `ciaddr` is 0.0.0.0.
- D is incorrect: DNS server information is delivered in DHCP Option 6 — separate from any header fields. The `giaddr` field has nothing to do with DNS configuration.

---

## Question 19

A client sends a DHCP Request broadcast after receiving offers from two DHCP servers. Server A offered 172.16.5.50 and Server B offered 172.16.5.51. The client selects Server A's offer. What happens to Server B's offered address?

- A) Server B's address 172.16.5.51 remains permanently reserved and is never reused
- B) Server B sees the broadcast Request and recognizes the client selected Server A; Server B returns 172.16.5.51 to its available pool
- C) Server B sends a DHCP NAK to the client to prevent it from using Server A's address
- D) Server B immediately offers 172.16.5.51 to the next client without waiting for the first client to respond

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: DHCP servers do not permanently reserve offered addresses. An offer is tentative — the address is held briefly while awaiting the Request. If the server sees the broadcast Request selecting a different server, the tentative hold is released.
- B is correct: The DHCP Request is broadcast so all DHCP servers on the segment receive it. The Request includes the Server Identifier option specifying which server was chosen (Server A's IP). Server B sees this and understands its offer was declined. Server B releases 172.16.5.51 back to its available pool for future offers to other clients.
- C is incorrect: A DHCP NAK is sent when a server wants to reject a client's request for a specific address — typically when the client is requesting an address that doesn't belong to the server's scope or that is already in use. Server B would not NAK a valid transaction between the client and Server A.
- D is incorrect: DHCP servers do not re-offer addresses that are tentatively held for a pending transaction until the offer times out or the server receives confirmation the offer was declined.

---

## Question 20

An engineer needs to verify that DHCP snooping is actively filtering DHCP traffic on a Cisco Catalyst switch. Which command output would confirm that an untrusted port has dropped a DHCP server message?

- A) `show ip dhcp binding`
- B) `show ip dhcp snooping statistics`
- C) `show ip dhcp snooping`
- D) `show interfaces status`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `show ip dhcp binding` on a switch (when configured as a relay or with DHCP snooping) shows the snooping binding table — a list of known client MAC/IP/VLAN/port associations. It does not show drop counters.
- B is correct: `show ip dhcp snooping statistics` displays counters for DHCP messages processed by the snooping feature, including messages forwarded and messages dropped. The "Messages Dropped" counter increments when a DHCP server message (Offer or ACK) arrives on an untrusted port, confirming that snooping is actively filtering rogue DHCP traffic.
- C is incorrect: `show ip dhcp snooping` displays the current snooping configuration — which VLANs have snooping enabled, the option 82 setting, and per-interface trust state. It does not show packet counters or drop statistics.
- D is incorrect: `show interfaces status` shows physical interface state (connected, notconnect, speed, duplex, VLAN assignment). It has no relationship to DHCP snooping filtering activity.
