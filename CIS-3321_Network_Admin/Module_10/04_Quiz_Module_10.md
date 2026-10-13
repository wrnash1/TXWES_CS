# Quiz: Module 10 — Network Services

## Course: CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Question 1

A network engineer is troubleshooting a new office with 50 workstations. All workstations display an IP address of 169.254.x.x and cannot reach any network resources. The DHCP server is located on a different subnet and the engineer notices the router interface facing the new office has no `ip helper-address` configured. What is the specific cause of the failure and which protocol message is being blocked?

A) The DHCP server has a scope exhaustion problem — all 50 addresses in the pool are already leased to the new workstations and no addresses remain for other clients

B) The router is blocking the DHCP Discover broadcast because routers do not forward broadcasts between subnets by default, and no relay agent exists to forward it to the DHCP server

C) The DNS server is unreachable, preventing the workstations from resolving the DHCP server's hostname before contacting it

D) The DHCP server's firewall is blocking inbound connections on TCP port 67, preventing the DHCP Discover from being received

Correct Answer: B) The router is blocking the DHCP Discover broadcast because routers do not forward broadcasts between subnets by default, and no relay agent exists to forward it to the DHCP server

Distractor Analysis:

Why A is incorrect: Scope exhaustion would mean clients received DHCP responses but the pool was full. A 169.254.x.x address indicates the client received no DHCP response at all — not a full scope. If the scope were exhausted, some clients might get valid addresses while others fell back to APIPA.

Why C is incorrect: DHCP does not use DNS. The client sends a Discover directly to the broadcast address 255.255.255.255 — it does not need to resolve a hostname to contact the DHCP server. DNS is irrelevant to DHCP address acquisition.

Why D is incorrect: DHCP uses UDP, not TCP, and the relevant ports are 67 (server) and 68 (client). More importantly, the core problem described — no relay agent — means the Discover never reaches the server at all, regardless of firewall rules.

---

### Question 2

A DHCP administrator needs to ensure that the IP address printer at 192.168.10.75 always resolves to the same address after power cycles, while avoiding the need to statically configure the IP address on the printer itself. Which DHCP feature accomplishes this?

A) Create a DHCP exclusion for 192.168.10.75 so that the address is never assigned dynamically to any device, then configure the printer with a static IP

B) Shorten the lease duration to 1 hour so the printer is guaranteed to renew its lease before any address can be reassigned to a different device

C) Create a DHCP reservation that binds the printer's MAC address to 192.168.10.75 so the server always assigns that specific address to that device

D) Configure a superscope that prioritizes 192.168.10.75 as the first address in the pool so that the first DHCP request always receives that address

Correct Answer: C) Create a DHCP reservation that binds the printer's MAC address to 192.168.10.75 so the server always assigns that specific address to that device

Distractor Analysis:

Why A is incorrect: An exclusion prevents the address from being dynamically assigned, but the printer would then need to be manually configured with a static IP — the question specifically requires avoiding static configuration on the device itself. A reservation accomplishes both goals simultaneously.

Why B is incorrect: A short lease time does not guarantee address consistency. When the lease expires, the DHCP server assigns the next available address from the pool, not necessarily the same one the printer previously held. Only a reservation ensures the same address every time.

Why D is incorrect: Superscopes combine multiple scopes for administrative purposes — they do not prioritize specific addresses or bind addresses to specific devices. Nothing guarantees the first address goes to the printer.

---

### Question 3

A campus network has a single DHCP server serving 12 VLANs. The administrator runs `show ip dhcp pool` on the DHCP server and sees that the VLAN_STUDENT scope (192.168.50.0/24) has 0 available addresses, 250 active leases, and a configured lease time of 24 hours. The student lab is nearly empty mid-afternoon, but devices from the morning lab session have not returned their leases. Which two actions resolve the immediate exhaustion and prevent recurrence?

A) Expand the scope to include the 192.168.51.0/24 subnet using a superscope, and reduce the lease time to 2 hours so that addresses from disconnected devices are reclaimed faster

B) Increase the lease time to 48 hours so that active students maintain their leases longer, and configure a DHCP reservation for every student device

C) Enable DHCP Snooping on the student VLAN and configure all student switch ports as untrusted to block DHCP traffic from student devices

D) Restart the DHCP service on the server to force all leases to expire simultaneously, then reconfigure the scope with a larger address range

Correct Answer: A) Expand the scope to include the 192.168.51.0/24 subnet using a superscope, and reduce the lease time to 2 hours so that addresses from disconnected devices are reclaimed faster

Distractor Analysis:

Why B is incorrect: Increasing lease time makes the problem worse by holding addresses for disconnected devices even longer. Reservations for every student device is operationally impractical and still does not solve the exhaustion — it only moves which addresses are assigned.

Why C is incorrect: DHCP Snooping prevents rogue DHCP servers and limits spoofed Discover rates — it does not reclaim leases or expand address pools. Marking all student ports untrusted does not resolve scope exhaustion; it only prevents students from acting as DHCP servers, which is not the problem described.

Why D is incorrect: Restarting the DHCP service and expiring all leases simultaneously would cause every active student device to lose its IP address at once, creating a network outage for current users. This is a destructive approach with no benefit over the correct actions.

---

### Question 4

A network administrator runs `nslookup mail.company.com` and receives a "Non-authoritative answer" with the correct IP address. A junior administrator interprets this as meaning the DNS data might be wrong and insists on running additional verification queries. Is the junior administrator's concern valid?

A) Yes — non-authoritative answers are served from expired cache entries and may no longer reflect the current DNS record; the authoritative server should always be queried directly for operational decisions

B) No — non-authoritative means the answer came from the resolver's cache, which is valid data that has not yet exceeded its TTL; it correctly reflects the DNS record as of the last authoritative lookup

C) Yes — the non-authoritative label specifically indicates the DNS record type cannot be resolved by a CNAME lookup and requires a direct A record query to confirm the IP address

D) No — non-authoritative answers are returned only by root servers and TLD servers; they are more reliable than answers from authoritative name servers because they aggregate data from multiple zones

Correct Answer: B) No — non-authoritative means the answer came from the resolver's cache, which is valid data that has not yet exceeded its TTL; it correctly reflects the DNS record as of the last authoritative lookup

Distractor Analysis:

Why A is incorrect: The non-authoritative label indicates the answer was cached — not that the cache has expired. Resolvers enforce TTL; if the TTL had expired, the resolver would have re-queried the authoritative server and the cached answer would have been refreshed. A non-authoritative answer is valid until its TTL expires.

Why C is incorrect: The non-authoritative label has nothing to do with CNAME records or record type resolution. It applies to any record type (A, AAAA, MX, etc.) served from cache, regardless of whether a CNAME chain is involved.

Why D is incorrect: Non-authoritative answers come from caching resolvers, not root or TLD servers. Root and TLD servers provide referrals (not full answers) during the iterative resolution process; those referrals are handled internally by the resolver before the client receives any response.

---

### Question 5

A user reports that email sent to her @company.com address is not being delivered. Investigation shows the A record for mail.company.com exists and resolves correctly. However, when querying the MX record for company.com, the output shows `company.com mail exchanger = 10 badserver.external.org`. What is the problem and which DNS record type has been compromised?

A) The A record for mail.company.com has been deleted — the existing A record is a cached entry that will expire, after which all mail delivery will fail

B) The MX record for company.com has been modified to point to an unauthorized mail server, which means incoming email is being delivered to an attacker-controlled server instead of the legitimate mail server

C) The NS record for company.com has expired, causing DNS resolvers to forward mail queries to external DNS servers that return incorrect results

D) The SOA serial number has not been incremented after a zone change, causing secondary DNS servers to serve stale MX records while the primary has the correct record

Correct Answer: B) The MX record for company.com has been modified to point to an unauthorized mail server, which means incoming email is being delivered to an attacker-controlled server instead of the legitimate mail server

Distractor Analysis:

Why A is incorrect: The question states the A record for mail.company.com resolves correctly. The problem is the MX record, which directs email delivery, not the A record that resolves the legitimate mail server's hostname.

Why C is incorrect: If the NS records had expired or been compromised, the symptom would be broader DNS failure for the entire domain — not specifically email delivery to an unauthorized server. The MX record is the record that specifically routes email.

Why D is incorrect: An SOA serial number issue would cause secondary servers to serve the old (potentially correct) MX record rather than the new (compromised) one. The scenario as described — where queries return a bad MX record — indicates the MX record itself was modified, not a zone transfer timing issue.

---

### Question 6

A network administrator is configuring NTP for a medium-sized enterprise. The company's internal NTP servers currently synchronize to pool.ntp.org. After a WAN outage lasting 90 minutes, branch office workstations were unable to authenticate to the domain. Post-incident review shows branch office clocks drifted 7 minutes during the outage. Which protocol failed due to the clock drift, and what is the standard maximum tolerance?

A) SNMP — network management systems reject polling responses when agent timestamps differ from the manager by more than 5 minutes

B) DHCP — lease renewal fails when client and server clocks differ by more than 5 minutes because lease timestamps are verified against server time

C) Kerberos — authentication tickets are rejected when the clock skew between the client and the KDC (Key Distribution Center) exceeds 5 minutes

D) RADIUS — remote authentication rejects 802.1X credentials when the session timestamp in the RADIUS Access-Request is outside the 5-minute tolerance window

Correct Answer: C) Kerberos — authentication tickets are rejected when the clock skew between the client and the KDC (Key Distribution Center) exceeds 5 minutes

Distractor Analysis:

Why A is incorrect: SNMP does not have a 5-minute clock skew tolerance that causes polling failures. SNMP GET/SET operations are not timestamp-validated in a way that would cause authentication failures due to NTP drift.

Why B is incorrect: DHCP lease renewal does not validate timestamps between client and server clocks. DHCP lease timers are based on the server's tracking of when the lease was issued — not compared against client-side time.

Why D is incorrect: RADIUS authentication for 802.1X validates user credentials (username/password or certificates) but does not enforce a 5-minute clock skew tolerance. The "clock skew too great" error is specific to the Kerberos protocol used for Active Directory authentication.

---

### Question 7

An organization needs to configure DNS so that internal users querying `intranet.company.com` receive the private IP address 10.10.5.100, while external internet users querying the same hostname receive the public IP address 203.0.113.50. Which DNS configuration accomplishes this?

A) Configure a CNAME record pointing intranet.company.com to the public IP, and a PTR record mapping the private IP for internal reverse lookups

B) Configure split-brain DNS (split-horizon) — maintain an internal DNS zone for company.com with the private A record, and a separate external DNS zone with the public A record

C) Configure conditional forwarding on the internal DNS server to forward all company.com queries to an external DNS server that returns both the public and private records based on source IP

D) Configure the internal DNS server with two A records for intranet.company.com — one with the private IP and one with the public IP — and allow DNS round-robin to serve both addresses

Correct Answer: B) Configure split-brain DNS (split-horizon) — maintain an internal DNS zone for company.com with the private A record, and a separate external DNS zone with the public A record

Distractor Analysis:

Why A is incorrect: A CNAME record creates an alias pointing to another hostname, not to an IP address directly. CNAME records cannot point to IP addresses. PTR records are for reverse DNS only. Neither accomplishes split-brain address serving.

Why C is incorrect: Conditional forwarding routes queries for a domain to a specific DNS server — it does not serve different answers based on whether the client is internal or external. External DNS servers do not typically maintain private IP records.

Why D is incorrect: Configuring both public and private IPs as A records for the same hostname would cause DNS round-robin, alternately returning both addresses to all clients — internal and external alike. External clients receiving the private IP (10.10.5.100) would be unable to reach the resource. This does not achieve the desired separation.

---

### Question 8

A switch administrator is enabling DHCP Snooping on a managed access switch. The switch has the following port connections: GigabitEthernet0/1 connects to an uplink trunk to the distribution layer (where the DHCP server resides). GigabitEthernet0/2 through GigabitEthernet0/24 connect to workstations. Which ports should be configured as DHCP Snooping trusted?

A) All ports should be trusted so that the switch does not interfere with DHCP traffic from any direction

B) Only GigabitEthernet0/1 (the trunk uplink) should be trusted; all workstation ports (0/2–0/24) should be untrusted

C) GigabitEthernet0/2 through 0/24 should be trusted because workstations are the clients that need to send DHCP Discovers; GigabitEthernet0/1 should be untrusted because servers do not generate DHCP traffic

D) No ports need to be trusted if the DHCP server is on a different VLAN — DHCP Snooping only applies within a VLAN

Correct Answer: B) Only GigabitEthernet0/1 (the trunk uplink) should be trusted; all workstation ports (0/2–0/24) should be untrusted

Distractor Analysis:

Why A is incorrect: Trusting all ports defeats the purpose of DHCP Snooping entirely. The critical protection DHCP Snooping provides is dropping DHCP Offers from untrusted ports. If all ports are trusted, rogue DHCP servers on workstation ports would be permitted to send Offers unchallenged.

Why C is incorrect: Workstation ports should be untrusted — a workstation should never send a DHCP Offer. DHCP Offers come from servers. Marking workstation ports as untrusted means if a rogue DHCP server or a misconfigured device on those ports sends an Offer, the switch drops it. The uplink (toward the legitimate server) should be trusted.

Why D is incorrect: DHCP Snooping operates per-VLAN and applies regardless of whether the DHCP server is on the same VLAN or a different one. The relay agent delivers DHCP traffic across subnets, but the switch still inspects DHCP messages on all local ports within the VLAN.

---

### Question 9

An administrator needs to configure Dynamic DNS so that workstations automatically update their DNS A records when their DHCP leases change. The environment uses Active Directory with Windows Server DNS and DHCP. A security engineer raises a concern that allowing any device to create DNS records could enable an attacker to register false hostnames in the internal zone. Which feature addresses this concern while still allowing automatic DNS updates?

A) Disable DDNS entirely and configure all workstation A records as static entries managed by the DNS administrator

B) Configure the DNS zone as a stub zone — stub zones only allow NS and SOA records and cannot accept DDNS updates from unauthorized clients

C) Enable Secure DDNS — DNS records created via Kerberos-authenticated updates can only be modified or deleted by the same authenticated client that created them, preventing rogue devices from overwriting legitimate records

D) Increase the DNS record TTL to 86400 seconds — longer TTL means existing records remain cached longer, making it harder for attackers to inject new records

Correct Answer: C) Enable Secure DDNS — DNS records created via Kerberos-authenticated updates can only be modified or deleted by the same authenticated client that created them, preventing rogue devices from overwriting legitimate records

Distractor Analysis:

Why A is incorrect: Disabling DDNS and managing all records statically solves the security concern but eliminates the operational benefit of automatic updates. In large environments with hundreds of DHCP clients, static DNS management creates significant administrative overhead and introduces human error.

Why B is incorrect: A stub zone contains only NS and SOA records — it holds delegation information for a child zone, not host records. Configuring the zone as a stub zone would eliminate all A records and break name resolution for the domain entirely. Stub zones are not a DDNS security mechanism.

Why D is incorrect: TTL controls how long cached records remain valid — it has no effect on whether unauthorized clients can create or modify DNS records. An attacker could still inject records; they would just persist in cache longer once injected.

---

### Question 10

A network architect is designing NTP infrastructure for an organization with a main data center and four branch offices connected via MPLS. The current design has all branch workstations and servers synchronized directly to time.google.com over the internet. The architect is concerned about reliability and wants internal NTP servers. Which design is most resilient?

A) Configure one internal NTP server in the data center synchronized to an external stratum 1 source; configure all branch devices to synchronize to that single internal server

B) Configure two internal NTP servers in the data center, both synchronized to external stratum 1 sources; configure each branch office with a local stratum 3 NTP server synchronized to both data center servers; configure all branch devices to use their local branch NTP server with the data center servers as fallback

C) Configure all branch devices to synchronize to pool.ntp.org directly, and configure the data center servers to synchronize to a GPS-connected stratum 1 device; do not connect branch NTP to data center

D) Configure the PDC Emulator in the data center as the sole NTP server; configure all branch domain controllers to synchronize to the PDC Emulator; configure all workstations to synchronize to their local branch domain controller

Correct Answer: B) Configure two internal NTP servers in the data center, both synchronized to external stratum 1 sources; configure each branch office with a local stratum 3 NTP server synchronized to both data center servers; configure all branch devices to use their local branch NTP server with the data center servers as fallback

Distractor Analysis:

Why A is incorrect: A single internal NTP server is a single point of failure. If that server goes down or the WAN connection to the data center fails, all branch devices lose their NTP source and begin drifting. This is exactly the scenario the architect wants to avoid.

Why C is incorrect: Having branches synchronize directly to pool.ntp.org and keeping data center NTP separate creates two independent time domains. If they drift apart, devices that authenticate across the WAN (workstations to data center domain controllers) will experience Kerberos failures. Internal NTP infrastructure must be unified.

Why D is incorrect: This design places the PDC Emulator as the sole authoritative NTP source within the organization — which is standard for Windows Active Directory. However, it does not address the branch office resilience problem. If the MPLS fails, branch domain controllers lose their NTP source and drift. The correct design adds local NTP servers at branches to maintain accuracy during data center connectivity outages.

---

### Question 11

A DHCP server has an address pool of 192.168.1.1–192.168.1.200 with a lease time of 24 hours. After a campus event, all 200 addresses were leased. New devices are now being denied addresses. What is the most immediate corrective action?

- A) Restart the DHCP server to clear all lease records.
- B) Shorten the lease time so existing leases expire sooner and addresses become available more quickly.
- C) Add a second DHCP server with the same scope to share the load.
- D) Disable DHCP and configure all devices with static IP addresses.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Restarting the DHCP server clears all lease records from memory, causing all current devices to lose their IP addresses. Devices would re-request addresses, but the pool is still exhausted — all 200 addresses would be re-leased immediately, solving nothing.
- *Why B is correct:* Shortening the lease time causes existing leases to expire sooner. Devices that have disconnected from the network (after the event) will not renew, and those addresses will return to the available pool. This is the appropriate short-term adjustment without interrupting current active clients.
- *Why C is incorrect:* Running two DHCP servers with the same scope causes IP address conflicts — both servers would assign the same addresses to different clients. Proper split-scope configuration (each server owns half the pool) would help but is not the "most immediate" single corrective action.
- *Why D is incorrect:* Disabling DHCP and configuring hundreds of devices with static addresses is operationally impractical and extremely time-consuming. It would cause significant downtime.

---

### Question 12

Which DHCP option number is used to specify the default gateway (router) for a DHCP client?

- A) Option 1
- B) Option 3
- C) Option 6
- D) Option 15

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* DHCP Option 1 specifies the subnet mask — it defines the network boundary, not the default gateway.
- *Why B is correct:* DHCP Option 3 specifies the router (default gateway) for the client. This is one of the most commonly configured DHCP scope options alongside Option 6 (DNS servers) and Option 15 (domain name).
- *Why C is incorrect:* DHCP Option 6 specifies the DNS server IP addresses — it tells the client which DNS server to use for name resolution.
- *Why D is incorrect:* DHCP Option 15 specifies the DNS domain name (e.g., company.local) — it defines the domain the client should use for DNS suffixes.

---

### Question 13

What is the purpose of the T2 timer in DHCP lease management, and what percentage of the lease duration does it typically represent?

- A) T2 is the initial lease request timer (25% of lease duration) — used during the DORA Discover phase.
- B) T2 is the rebinding timer (87.5% of lease duration) — if the client cannot renew with the original server, it broadcasts a Request to any available DHCP server.
- C) T2 is the grace period timer (100% of lease duration) — the client is given extra time after lease expiry before losing its address.
- D) T2 is the conflict detection timer (50% of lease duration) — the server pings the address before assigning it to verify no conflicts.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* 25% does not correspond to the T2 timer. The T1 timer fires at 50% of lease duration for unicast renewal with the original server.
- *Why B is correct:* The T2 (rebinding) timer fires at 87.5% of the lease duration. At this point, if the client has not successfully renewed via T1 unicast attempts, it broadcasts a DHCP Request to any DHCP server on the network to obtain a new lease, even from a different server.
- *Why C is incorrect:* There is no 100% grace period timer defined as T2 in the DHCP standard. After the lease fully expires, the client must release the address and begin a new DORA process.
- *Why D is incorrect:* DHCP conflict detection is a server-side feature where the server pings an address before assigning it — this is a separate mechanism, not the T2 timer. T2 is a client-side rebinding timer.

---

### Question 14

An administrator reviews a DNS zone file and sees the following record:
`192.168.1.50.in-addr.arpa. IN PTR server01.company.com.`
What type of DNS record is this, and what is its purpose?

- A) An A record — maps the IP address 192.168.1.50 to the hostname server01.company.com
- B) A PTR record — used for reverse DNS lookup to resolve an IP address to a hostname
- C) A CNAME record — creates an alias from the IP address to the canonical hostname
- D) An NS record — identifies server01.company.com as the name server for the 192.168.1.0/24 subnet

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* An A record maps a hostname to an IP address (forward lookup). The record shown is in the `in-addr.arpa` zone, which is exclusively used for reverse DNS lookups.
- *Why B is correct:* A PTR (Pointer) record provides reverse DNS — given an IP address, it returns the associated hostname. PTR records are stored in the `in-addr.arpa` zone with the octets of the IP address written in reverse order. This record maps 192.168.1.50 back to `server01.company.com`.
- *Why C is incorrect:* A CNAME record creates an alias between two hostnames. It does not involve IP addresses or the `in-addr.arpa` reverse zone.
- *Why D is incorrect:* An NS (Name Server) record identifies the authoritative name servers for a domain. It does not appear in the format shown and does not perform reverse IP lookups.

---

### Question 15

An IPAM system alerts an administrator that DHCP Scope utilization for the 10.20.0.0/24 subnet has reached 92%. What is the most appropriate immediate action?

- A) Expand the DHCP lease to 7 days to reduce the frequency of renewals and lower utilization.
- B) Evaluate scope utilization trends, shorten the lease time to recover lapsed leases faster, and plan to expand the subnet or split it into multiple VLANs.
- C) Remove all static IP reservations in the scope to free up addresses.
- D) Delete the scope and reconfigure it with a smaller subnet to consolidate unused addresses.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Increasing the lease time to 7 days would make the utilization problem worse — addresses held by devices that have disconnected would be unavailable for longer before expiring and returning to the pool.
- *Why B is correct:* At 92% utilization, the scope is near exhaustion. Shortening the lease time recycles addresses from disconnected devices faster. IPAM trend analysis helps determine whether utilization is growing steadily (requiring a long-term subnet expansion or VLAN segmentation plan) or spiky (manageable with lease time adjustment).
- *Why C is incorrect:* Removing DHCP reservations would cause those devices to receive random addresses rather than their reserved addresses, breaking any services that depend on known IP addresses (DNS entries, ACLs, print server configurations).
- *Why D is incorrect:* Deleting the scope and reconfiguring with a smaller subnet would reduce the available address space, making the exhaustion problem worse — not better.

---

### Question 16

A company's DHCP server is on VLAN 1 (10.0.1.0/24) and serves clients on VLAN 20 (172.16.20.0/24). The Layer 3 switch interface for VLAN 20 is assigned 172.16.20.1/24. After configuring `ip helper-address 10.0.1.5` on the VLAN 20 interface, clients still receive APIPA addresses. Which of the following is the most likely cause?

- A) The DHCP server does not have a scope defined for the 172.16.20.0/24 network.
- B) The `ip helper-address` command requires a restart of the switch to take effect.
- C) VLAN 20 clients must have a static default gateway before DHCP can function.
- D) `ip helper-address` only works for UDP port 69 (TFTP), not DHCP.

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The `ip helper-address` correctly forwards DHCP Discovers to the DHCP server with the VLAN 20 gateway IP (172.16.20.1) in the giaddr field. However, if the DHCP server does not have a scope configured for the 172.16.20.0/24 subnet, it will not respond to those relayed requests — and clients fall back to APIPA.
- *Why B is incorrect:* The `ip helper-address` command takes effect immediately in IOS — no switch restart is required. Changes to interface configuration are applied when entered.
- *Why C is incorrect:* DHCP clients do not need a static default gateway configured before requesting a DHCP lease. The entire purpose of DHCP is to provide the gateway, IP address, and DNS automatically.
- *Why D is incorrect:* `ip helper-address` by default forwards multiple UDP protocols including DHCP (ports 67/68), TFTP (port 69), DNS (port 53), and others. DHCP is one of its primary functions.

---

### Question 17

What does it mean when a DNS response is labeled "non-authoritative"?

- A) The DNS response contains incorrect or potentially outdated information that should not be trusted.
- B) The DNS response was served from a resolver's cache and was not obtained directly from the authoritative name server during this transaction.
- C) The DNS server that answered does not have the record and is referring the client to another server.
- D) The DNS record has expired and must be re-queried before use.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Non-authoritative does not mean incorrect or untrustworthy. It simply indicates the answer came from cache rather than directly from the authoritative server. The data was accurate when originally fetched and remains valid as long as the TTL has not expired.
- *Why B is correct:* A non-authoritative response means the answering DNS resolver (cache) obtained the record from the authoritative server at some earlier time and is now serving the cached copy. The answer is valid as long as the TTL has not expired.
- *Why C is incorrect:* A referral (iterative response) occurs when a DNS server does not have the answer and directs the resolver to another server. This is different from a non-authoritative cached response.
- *Why D is incorrect:* If a DNS record's TTL has expired in cache, the resolver re-queries the authoritative server before serving the record. An expired record would trigger a fresh authoritative query rather than a non-authoritative response.

---

### Question 18

A network administrator wants to ensure that all external DNS queries from corporate workstations are logged for security auditing. Which DNS architecture change implements this while maintaining internet name resolution?

- A) Configure all workstations to use 8.8.8.8 directly and capture packets on the internet gateway.
- B) Deploy an internal DNS forwarder that receives all client queries, logs them, and forwards unresolved queries to the upstream DNS server.
- C) Disable DNS caching on all workstations to force every query to go to the authoritative server.
- D) Configure all workstations with a hosts file containing entries for commonly visited websites.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Capturing packets at the gateway is technically possible but requires deep packet inspection of all DNS traffic. This is less controlled and harder to manage than a centralized DNS logging server.
- *Why B is correct:* An internal DNS forwarder acts as the single DNS exit point for all corporate clients. It receives all queries, can log them with user/IP attribution, enforces DNS filtering policies, and forwards unresolved queries to upstream resolvers. This is the standard enterprise DNS logging architecture.
- *Why C is incorrect:* Disabling DNS caching forces every query to the authoritative server, dramatically increasing DNS query load and latency. It does not centralize logging — queries would still go directly to external servers unless a forwarder is in place.
- *Why D is incorrect:* A hosts file only covers entries explicitly listed in the file. It cannot scale to cover all internet hostnames and does not log queries.

---

### Question 19

What NTP stratum number indicates that a device is unsynchronized and its time should not be trusted?

- A) Stratum 0
- B) Stratum 10
- C) Stratum 15
- D) Stratum 16

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Stratum 0 indicates a high-precision reference clock (GPS, atomic). It is the most accurate stratum level, not unsynchronized.
- *Why B is incorrect:* Stratum 10 is a valid synchronized stratum — 10 hops from the reference clock. While further removed from accuracy, it indicates a device IS synchronized.
- *Why C is incorrect:* Stratum 15 is the maximum valid stratum for a synchronized NTP client. It is valid but of lower accuracy.
- *Why D is correct:* Stratum 16 in NTP means the device is unsynchronized. An NTP source advertising stratum 16 should not be used for time synchronization — it indicates the device has lost contact with its upstream NTP source and is operating on its own free-running clock.

---

### Question 20

A company uses IPAM (IP Address Management) software. What is the primary operational benefit IPAM provides over managing IP addresses in spreadsheets?

- A) IPAM replaces the need for DNS and DHCP servers entirely by managing all IP assignments directly.
- B) IPAM provides automated discovery, real-time utilization visibility, integration with DNS and DHCP, and audit history — reducing errors and preventing scope exhaustion surprises.
- C) IPAM encrypts all IP address assignments to prevent attackers from knowing the network topology.
- D) IPAM eliminates the need for network documentation because the database replaces all IP address records.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* IPAM does not replace DNS and DHCP servers — it integrates with them to provide management and visibility. DNS and DHCP remain separate infrastructure components.
- *Why B is correct:* IPAM centralizes IP address tracking, integrates with DHCP servers to show real-time scope utilization, integrates with DNS to ensure forward/reverse records exist, provides automated scanning to discover untracked devices, and maintains an audit log of all address assignments and changes.
- *Why C is incorrect:* IPAM does not encrypt IP address assignments. Network addressing information is a management data concern, not a confidentiality encryption concern.
- *Why D is incorrect:* The IPAM database IS the network documentation — it supplements and replaces manual spreadsheets. It does not make network documentation unnecessary; it automates and improves it.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
