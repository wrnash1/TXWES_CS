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

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
