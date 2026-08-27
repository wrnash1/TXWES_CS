# Quiz: Module 09 — Network Services: DNS, DHCP, and NTP

## Course: CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Question 1

A DNS administrator needs to configure the company's domain so that email sent to @example.com is delivered to the correct mail server. Which DNS record type must be created?

A) A record — maps the mail server's hostname to its IPv4 address for delivery routing

B) CNAME record — creates an alias from the mail server hostname to the domain's canonical name

C) MX record — identifies the mail server responsible for accepting email for the domain, with a priority value

D) PTR record — resolves the mail server's IP address back to its hostname for reverse DNS lookup

Correct Answer: C) MX record — identifies the mail server responsible for accepting email for the domain, with a priority value

Distractor Analysis:

Why A is incorrect: An A record maps a hostname to an IPv4 address — it does not direct email delivery for a domain. While the mail server itself likely has an A record, the MX record is what tells other mail servers where to send email for the domain.

Why B is incorrect: A CNAME record creates a hostname alias — it is not used to designate a mail server for a domain. CNAME records cannot be used as MX record targets.

Why D is incorrect: A PTR record is used for reverse DNS lookup (IP to hostname) — it does not configure email delivery routing.

---

### Question 2

A network administrator receives a support ticket: a workstation on VLAN 20 cannot obtain an IP address from the DHCP server located on VLAN 1. Workstations on VLAN 1 obtain addresses normally. The VLAN 20 interface has an IP address of 192.168.20.1 and the DHCP server is at 192.168.1.50. Which configuration resolves this issue?

A) Create a DHCP reservation on the server mapping the VLAN 20 interface MAC address to 192.168.20.1

B) Configure ip helper-address 192.168.1.50 on the VLAN 20 switch virtual interface to relay DHCP broadcasts to the server

C) Add a static route on the DHCP server pointing 192.168.20.0/24 to the default gateway

D) Configure the workstations on VLAN 20 with static IP addresses in the 192.168.20.0/24 range

Correct Answer: B) Configure ip helper-address 192.168.1.50 on the VLAN 20 switch virtual interface to relay DHCP broadcasts to the server

Distractor Analysis:

Why A is incorrect: A DHCP reservation maps a specific MAC address to a specific IP — it does not allow DHCP broadcasts from VLAN 20 to cross the Layer 3 boundary to reach the server on VLAN 1.

Why C is incorrect: A static route on the DHCP server allows it to send reply packets to VLAN 20, but the DHCP client's initial Discover is a broadcast that cannot be routed — the relay agent is still required to convert the broadcast to a unicast.

Why D is incorrect: Configuring static IPs bypasses DHCP entirely and creates additional administrative overhead. It does not fix the relay configuration.

---

### Question 3

A security engineer reviews authentication failures showing "clock skew too great" errors for multiple workstations. Which service failure is causing these errors, and what is the standard maximum tolerance?

A) DNS — the domain controller cannot resolve workstation hostnames because TTL on A records has expired

B) DHCP — workstations are receiving expired IP leases that no longer match the domain controller subnet

C) NTP — clocks are not synchronized; Kerberos authentication fails when clock skew exceeds 5 minutes

D) RADIUS — the authentication server is rejecting credentials because the session token timestamp is out of range

Correct Answer: C) NTP — clocks are not synchronized; Kerberos authentication fails when clock skew exceeds 5 minutes

Distractor Analysis:

Why A is incorrect: DNS TTL expiration does not generate "clock skew" errors. A DNS failure produces name resolution errors, not clock skew authentication failures.

Why B is incorrect: Expired DHCP leases cause IP address issues and connectivity loss, not Kerberos authentication errors.

Why D is incorrect: RADIUS is used for 802.1X and VPN authentication, not Kerberos. The "clock skew too great" error is specific to the Kerberos protocol.

---

### Question 4

A user reports they can access websites by IP address but cannot browse by hostname. Which service has failed, and what is the first troubleshooting step?

A) DHCP has failed — run ipconfig /release and ipconfig /renew to obtain a new IP address

B) DNS has failed — run `nslookup www.example.com` to confirm whether the DNS server is responding

C) The default gateway is unreachable — run ping to the default gateway to verify Layer 3 connectivity

D) NTP has failed — synchronize the workstation clock and retry the hostname lookup

Correct Answer: B) DNS has failed — run `nslookup www.example.com` to confirm whether the DNS server is responding

Distractor Analysis:

Why A is incorrect: The user can already reach IP addresses on the internet, confirming DHCP has provided a valid IP configuration. DHCP failure would prevent all IP connectivity.

Why C is incorrect: The user can already reach destinations by IP — the default gateway and internet routing are confirmed working. The only broken function is hostname-to-IP translation.

Why D is incorrect: NTP failure causes Kerberos and certificate validation issues, not hostname resolution failure.

---

### Question 5

A network administrator needs to harden the DNS, DHCP, and NTP infrastructure against common attacks: (1) DNS cache poisoning, (2) rogue DHCP servers, and (3) NTP amplification attacks. Which combination of controls best addresses all three?

A) Enable DNSSEC on all authoritative zones, configure DHCP snooping on all access switches, and restrict NTP to respond only to trusted client IP ranges using ACLs

B) Increase DNS TTL values to 86400 seconds, assign static IPs to all DHCP clients, and disable NTP on all network devices

C) Configure split-horizon DNS, enable DHCP relay agents on all VLANs, and upgrade to NTPv4

D) Deploy a DNSSEC-validating recursive resolver, enable DHCP failover for redundancy, and configure NTP authentication using MD5 keys

Correct Answer: A) Enable DNSSEC on all authoritative zones, configure DHCP snooping on all access switches, and restrict NTP to respond only to trusted client IP ranges using ACLs

Distractor Analysis:

Why A is correct: DNSSEC digitally signs DNS records, preventing cache poisoning (requirement 1). DHCP snooping drops unauthorized DHCP server responses from untrusted ports (requirement 2). NTP ACLs restrict which hosts the server responds to, preventing amplification (requirement 3).

Why B is incorrect: Increasing TTL does not prevent cache poisoning. Static IPs remove DHCP entirely. Disabling NTP creates Kerberos and certificate validation failures.

Why C is incorrect: Split-horizon DNS controls record visibility, not cache poisoning. DHCP relay agents forward broadcasts — they do not block rogue servers. NTPv4 alone does not prevent amplification without access controls.

Why D is incorrect: A DNSSEC-validating resolver protects clients but not the authoritative zone itself. DHCP failover provides redundancy, not rogue server prevention. NTP MD5 authentication authenticates peers but does not prevent amplification from external hosts.

---

### Question 6

A network administrator runs nslookup and sees the response labeled "Non-authoritative answer." What does this indicate?

A) The DNS server is not authorized to make changes to the zone and returned an error

B) The answer was served from the resolver's cache rather than directly from the domain's authoritative name server

C) The DNS record returned is for a CNAME alias and cannot be used directly to reach the destination

D) The DNS server found no matching record and returned a best-guess approximation from a nearby zone

Correct Answer: B) The answer was served from the resolver's cache rather than directly from the domain's authoritative name server

Distractor Analysis:

Why A is incorrect: Non-authoritative does not mean unauthorized or in error. It simply means the answer came from a caching resolver that previously resolved the query. This is normal behavior for most queries.

Why C is incorrect: CNAME chains do not produce the non-authoritative label specifically. The label applies to any cached response regardless of record type.

Why D is incorrect: A non-authoritative answer is a complete and valid cached response. If no record existed, the server would return NXDOMAIN — an explicit error, not a non-authoritative answer.

---

### Question 7

A Windows workstation is assigned the IP address 169.254.47.12 with subnet mask 255.255.0.0. The user cannot access any network resources. What is the most likely cause?

A) The workstation has been assigned an IPv6 link-local address and cannot communicate using IPv4

B) The DHCP server assigned a duplicate IP and the workstation detected the conflict, reverting to the APIPA range

C) The workstation was unable to reach a DHCP server and self-assigned an APIPA address in the 169.254.0.0/16 range

D) The workstation's static IP was entered incorrectly and the address falls outside the valid subnet range

Correct Answer: C) The workstation was unable to reach a DHCP server and self-assigned an APIPA address in the 169.254.0.0/16 range

Distractor Analysis:

Why A is incorrect: 169.254.x.x is IPv4 APIPA, not an IPv6 address. IPv6 link-local addresses begin with fe80::/10.

Why B is incorrect: IP address conflicts cause the workstation to stop using the conflicting address and generate a conflict notification — not an APIPA assignment. APIPA specifically indicates no DHCP server was reachable.

Why D is incorrect: APIPA addresses are automatically self-assigned by Windows when DHCP fails. Incorrect static IP entry would not result in the 169.254.0.0/16 range unless intentionally set there.

---

### Question 8

An organization needs an internal database server with private IP 10.10.10.100 to be accessible from the internet at a dedicated public IP that partner companies can always reach at the same address. Which NAT type is appropriate?

A) PAT (Port Address Translation) — many internal hosts share one public IP differentiated by port numbers

B) Dynamic NAT — the database server is assigned a public IP from a pool each time it initiates a connection

C) Static NAT — a permanent one-to-one mapping is created between 10.10.10.100 and a specific public IP address

D) NAT Overload — port numbers track sessions so multiple internal servers share the same public IP

Correct Answer: C) Static NAT — a permanent one-to-one mapping is created between 10.10.10.100 and a specific public IP address

Distractor Analysis:

Why A is incorrect: PAT is designed for outbound internet access by multiple internal hosts sharing one public IP — it does not provide a fixed, predictable public address for inbound connections from partner companies.

Why B is incorrect: Dynamic NAT assigns addresses from a pool when the internal host initiates connections — the public IP is not permanent. Partners cannot reliably connect to an address that changes with each connection.

Why D is incorrect: NAT Overload is another name for PAT — same limitations as option A for inbound connectivity to a fixed public address.

---

### Question 9

A DNS administrator is troubleshooting email delivery failures. The MX record for example.com points to mail.example.com. A follow-up A record query for mail.example.com returns no result. What is the cause of the delivery failure?

A) The MX record priority of 10 is too high — email servers require MX priorities of 5 or lower to accept mail

B) The MX record points to mail.example.com but no A record exists for that hostname, so sending servers cannot resolve the mail exchanger's IP address

C) The MX record uses the wrong record type — email routing requires an AAAA record, not an MX record

D) The nslookup output shows the MX record is cached (non-authoritative) and the actual MX record may differ

Correct Answer: B) The MX record points to mail.example.com but no A record exists for that hostname, so sending servers cannot resolve the mail exchanger's IP address

Distractor Analysis:

Why A is incorrect: MX priority values have no fixed maximum. Priority 10 is a standard value. Lower numbers indicate higher priority — priority 10 is perfectly valid and would not cause delivery failures.

Why C is incorrect: MX records are the correct record type for email routing. An AAAA record is used for IPv6 address resolution, not mail server identification.

Why D is incorrect: The non-authoritative label means the response came from cache — the data is valid. The problem is the missing A record for the mail exchanger hostname, not the caching status of the MX record.

---

### Question 10

A company has a single DHCP server serving three VLANs: VLAN 10, 20, and 30. Each VLAN has its own scope on the DHCP server. What configuration ensures clients on each VLAN receive addresses from the correct scope?

A) Configure the DHCP server with a superscope encompassing all three subnets, allowing clients from any VLAN to receive any available address

B) Configure ip helper-address pointing to the DHCP server on the Layer 3 interface for each VLAN, so the relayed DHCP Discover includes the gateway interface IP, allowing the server to select the correct scope

C) Create a separate DHCP server on each VLAN and disable inter-VLAN routing

D) Configure each client with a DHCP client ID matching their VLAN number so the server can identify which scope to assign

Correct Answer: B) Configure ip helper-address pointing to the DHCP server on the Layer 3 interface for each VLAN, so the relayed DHCP Discover includes the gateway interface IP, allowing the server to select the correct scope

Distractor Analysis:

Why A is incorrect: A superscope combines multiple scopes but without proper relay configuration, DHCP broadcasts still cannot cross VLAN boundaries. Scope selection is based on gateway address in the relayed packet, not superscope membership.

Why C is incorrect: Deploying separate DHCP servers per VLAN creates administrative overhead and eliminates centralized management. Disabling inter-VLAN routing would break all cross-VLAN communication.

Why D is incorrect: DHCP client IDs are optional identifiers used for reservations, not for scope selection. Scope selection is based on the gateway address (giaddr field) in the relayed DHCP packet.

---

### Question 11

A DHCP server is configured with a scope for 192.168.50.0/24 with the range 192.168.50.10–192.168.50.200 and a lease time of 8 hours. A workstation requests an IP address and receives 192.168.50.75. After 4 hours, the workstation attempts to renew its lease. Which step of the DHCP process is the renewal, and what transport is used?

- A) A new DHCP Discover broadcast — the workstation has forgotten its lease
- B) A unicast DHCP Request sent directly to the DHCP server that issued the original lease
- C) A unicast DHCP Offer sent from the server to the client unprompted
- D) A broadcast DHCP Request because the client cannot yet use unicast

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A DHCP Discover broadcast is only sent when a client has no IP address and no knowledge of a DHCP server. At renewal time (50% of lease), the client already knows its assigned IP and the server's IP.
- *Why B is correct:* At the 50% lease point (T1 timer), the client sends a unicast DHCP Request directly to the server that granted the original lease, requesting renewal. Unicast is used because the client has an IP address and knows the server's address.
- *Why C is incorrect:* DHCP Offers are sent by the server in response to client Discovers. The server does not proactively send Offers to renew leases without a client request.
- *Why D is incorrect:* A broadcast DHCP Request is used during the initial DORA process before the client has been assigned an IP. After the initial assignment, renewals use unicast.

---

### Question 12

Which DNS record type is used to define a human-readable alias that maps one hostname to another canonical hostname?

- A) A record
- B) PTR record
- C) CNAME record
- D) SRV record

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* An A record maps a hostname directly to an IPv4 address — not to another hostname alias.
- *Why B is incorrect:* A PTR record performs reverse DNS — it maps an IP address back to a hostname. It is the opposite of a CNAME alias.
- *Why C is correct:* A CNAME (Canonical Name) record creates an alias from one hostname to another. For example, `www.example.com CNAME example.com` means `www` is an alias for the canonical name `example.com`. Querying the alias returns the canonical name, which is then resolved to an IP.
- *Why D is incorrect:* An SRV record specifies the location of a specific service (host and port) for a domain — it is used for service discovery (e.g., SIP, XMPP), not for simple hostname aliasing.

---

### Question 13

An administrator checks the system time on a critical authentication server and finds it is 6 minutes ahead of the actual time. Kerberos authentication is failing for all users connecting to this server. What is the most likely cause?

- A) The NTP server is unreachable and the server's clock drifted beyond the maximum tolerated skew.
- B) The authentication failures are unrelated to time — the Kerberos service is misconfigured.
- C) The maximum clock skew tolerance for Kerberos is 15 minutes — a 6-minute offset should not cause failures.
- D) The server is using the wrong NTP stratum — only stratum 1 servers can be used for Kerberos.

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Kerberos has a maximum clock skew tolerance of 5 minutes (300 seconds) by default. A 6-minute offset exceeds this limit, causing Kerberos to reject tickets as potentially replayed. Accurate time synchronization via NTP is a prerequisite for Kerberos authentication.
- *Why B is incorrect:* The scenario explicitly describes a time offset that exceeds Kerberos limits — this is the direct cause of the authentication failure. The Kerberos service itself is working correctly.
- *Why C is incorrect:* The Kerberos maximum clock skew is 5 minutes by default, not 15 minutes. A 6-minute offset exceeds this limit and causes authentication failures.
- *Why D is incorrect:* Kerberos does not require a stratum 1 NTP source. Any accurate, synchronized NTP source is acceptable. Stratum 2 and lower servers are routinely used for Kerberos clients.

---

### Question 14

What is the purpose of a DNS TTL (Time to Live) value associated with a DNS record?

- A) It limits the number of DNS hops between the client and the authoritative server before the query expires.
- B) It specifies how long a DNS resolver may cache a record before it must query the authoritative server again for a fresh copy.
- C) It sets the maximum number of times a DNS record can be queried before it expires.
- D) It defines the lease period for the IP address returned in a DNS A record response.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* DNS hop limiting is performed by a separate mechanism (the recursion depth and timeout). TTL in a DNS record is a caching duration, not a hop counter.
- *Why B is correct:* The TTL value in a DNS resource record tells resolvers (caches) how many seconds they may cache the record and serve it in response to queries before the cached copy expires and a fresh query to the authoritative name server is required.
- *Why C is incorrect:* DNS records do not have a query count limit. They can be queried indefinitely. TTL is time-based, not query-count-based.
- *Why D is incorrect:* IP address lease periods are a DHCP concept, not a DNS concept. DNS A records do not manage IP address leases — that is the responsibility of the DHCP server.

---

### Question 15

A DNS resolver performs a query for `mail.company.com`. The authoritative DNS server for `company.com` responds but directs the resolver to another DNS server for further information. This type of DNS response is called:

- A) A recursive response
- B) A non-authoritative response
- C) An iterative (referral) response
- D) A negative cache response (NXDOMAIN)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A recursive response is when the DNS server does all the resolution work itself and returns the final IP address to the client. The scenario describes a referral, not a full recursive answer.
- *Why B is incorrect:* A non-authoritative response is a cached answer from a resolver — it indicates the answer came from cache, not that a referral was made.
- *Why C is correct:* An iterative (or referral) response occurs when a DNS server does not have the answer itself but responds with a referral to another DNS server that is closer to the authoritative source. The resolver must then query the referred server. This is how root servers and TLD servers respond.
- *Why D is incorrect:* NXDOMAIN (Non-Existent Domain) is the response when the queried hostname does not exist in DNS. It is a negative answer, not a referral.

---

### Question 16

Which NTP stratum number describes an NTP server that synchronizes directly from a GPS receiver or atomic clock hardware reference?

- A) Stratum 0
- B) Stratum 1
- C) Stratum 2
- D) Stratum 3

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Stratum 0 refers to the physical precision time source itself (GPS receiver, atomic clock, CDMA signal) — it is not a network-accessible NTP server. Stratum 0 devices cannot serve NTP directly over the network.
- *Why B is correct:* Stratum 1 NTP servers are directly connected to a stratum 0 reference (GPS, atomic clock via hardware interface). They are the primary NTP servers that other NTP infrastructure synchronizes from.
- *Why C is incorrect:* Stratum 2 servers synchronize from stratum 1 servers. They are one hop removed from the hardware reference.
- *Why D is incorrect:* Stratum 3 servers synchronize from stratum 2 servers. They are two hops removed from the hardware reference. Higher stratum numbers indicate increasing distance from the authoritative time source.

---

### Question 17

An administrator configures a Cisco router as a DHCP relay agent by entering the command `ip helper-address 10.0.0.1` on the VLAN 30 interface. What does this command accomplish?

- A) It assigns the router the IP address 10.0.0.1 as a secondary address on the VLAN 30 interface.
- B) It configures the router to forward DHCP broadcast messages from VLAN 30 clients to the DHCP server at 10.0.0.1 as unicast packets.
- C) It instructs the DHCP server at 10.0.0.1 to create a new scope for the VLAN 30 subnet automatically.
- D) It creates a static DHCP reservation for MAC address 10.0.0.1 in the VLAN 30 scope.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The `ip helper-address` command is not used for address assignment on the interface — that is done with `ip address`. It configures broadcast forwarding for DHCP and other UDP protocols.
- *Why B is correct:* `ip helper-address` configures the router's Layer 3 interface to forward DHCP broadcasts (and other specified UDP broadcasts) to the specified server as unicast packets. This allows clients in VLAN 30 to reach a DHCP server on a different subnet. The router inserts its VLAN 30 interface IP in the giaddr field of the forwarded packet, allowing the DHCP server to identify the correct scope.
- *Why C is incorrect:* The router command does not automatically create DHCP scopes on the server. Scopes must be manually configured on the DHCP server by an administrator.
- *Why D is incorrect:* DHCP reservations are based on MAC addresses configured on the DHCP server, not on IP addresses configured on a router interface.

---

### Question 18

A company uses split-horizon DNS (split DNS). What is the purpose of this configuration?

- A) To distribute DNS queries across multiple authoritative servers for load balancing.
- B) To return different DNS answers to internal clients versus external clients for the same hostname.
- C) To prevent DNS queries from leaving the internal network by blocking UDP port 53.
- D) To duplicate DNS zones across two datacenters for redundancy.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Distributing DNS queries across multiple servers for load balancing uses round-robin DNS or anycast DNS — not split-horizon DNS.
- *Why B is correct:* Split-horizon (split-brain) DNS maintains separate DNS views for internal and external networks. Internal clients receive private IP addresses for company resources (e.g., 10.0.0.50 for `mail.company.com`), while external clients receive the public IP address. This allows internal clients to use direct private paths while external clients use public-facing addresses.
- *Why C is incorrect:* Blocking UDP port 53 would break DNS entirely. Split DNS has nothing to do with firewall rules blocking DNS traffic.
- *Why D is incorrect:* Duplicating zones for redundancy is called DNS secondary zones or zone transfer replication — not split-horizon DNS.

---

### Question 19

Which attack targets DNS resolvers by inserting false DNS records into their cache, causing clients to be directed to attacker-controlled IP addresses?

- A) DNS amplification attack
- B) DNS zone transfer attack
- C) DNS cache poisoning
- D) DNS tunneling

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A DNS amplification attack exploits open DNS resolvers to reflect large DNS responses at a DDoS victim by sending small queries with a spoofed source IP. It is a volumetric DDoS attack — not a record falsification attack.
- *Why B is incorrect:* A DNS zone transfer attack involves an unauthorized AXFR request to retrieve the complete DNS zone file, exposing all hostnames. It is a reconnaissance attack, not a cache manipulation attack.
- *Why C is correct:* DNS cache poisoning involves inserting forged DNS records into a resolver's cache. When a legitimate client queries the resolver for a domain, the poisoned cache returns the attacker's IP address instead of the real one, redirecting the client to a malicious server. DNSSEC is the countermeasure.
- *Why D is incorrect:* DNS tunneling encodes data within DNS queries and responses to create a covert communication channel, bypassing firewalls. It does not involve poisoning DNS caches.

---

### Question 20

A network administrator runs `nslookup -type=SOA example.com` and receives a response. What information is contained in an SOA (Start of Authority) record?

- A) The list of all IP addresses assigned to example.com's web server
- B) The hostnames of all mail servers responsible for example.com
- C) The primary authoritative nameserver, administrator email, zone serial number, and refresh/retry/expiry timers
- D) The IPv6 AAAA records for the example.com nameservers

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* IP addresses for web servers are stored in A records, not SOA records.
- *Why B is incorrect:* Mail server hostnames are stored in MX records, not SOA records.
- *Why C is correct:* The SOA (Start of Authority) record is the first record in a DNS zone and contains: the primary nameserver (MNAME), the administrator's email address in DNS format (RNAME), the zone serial number (used to detect zone changes during transfers), and the refresh/retry/expiry timers that control how secondary DNS servers synchronize with the primary.
- *Why D is incorrect:* IPv6 addresses for nameservers are stored in AAAA records, not in the SOA record itself.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
