# Quiz: Module 06 - DNS and DHCP Server Roles

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

A Windows Server DNS administrator wants to ensure that only domain-joined computers can dynamically register DNS records in the company's internal DNS zones, preventing rogue or non-domain devices from polluting the zone with false records. Which DNS zone configuration satisfies this requirement?

A) A standard primary zone stored as a text file on the primary DNS server, with dynamic updates set to "Nonsecure and Secure."
B) An Active Directory-integrated zone with dynamic updates set to "Secure only," so only authenticated domain computers can register records.
C) A secondary zone replicated from the primary server, with all dynamic updates disabled at the secondary.
D) A stub zone that contains only NS and SOA records, preventing any dynamic registration.

* **Correct Answer:** B) An Active Directory-integrated zone with dynamic updates set to "Secure only," so only authenticated domain computers can register records.
* **Distractor Analysis:**
  * *Why A is incorrect:* "Nonsecure and Secure" dynamic updates allow any client — including non-domain devices — to register DNS records without authentication, creating the exact security problem the question describes.
  * *Why C is incorrect:* Secondary zones are read-only replicas and cannot accept dynamic updates at all — they do not solve the authentication requirement and would break legitimate client registration.
  * *Why D is incorrect:* A stub zone contains only delegation records (NS, SOA, and glue A records) and is used for conditional forwarding and delegation — it does not host client records and cannot accept dynamic registrations.

---

### Question 2

A company has two file servers — one in New York and one in Los Angeles. Users currently use `\\NY-FS01\Data` and `\\LA-FS01\Data`. Management wants users to access all company files through the single path `\\company.local\SharedData`. Which Windows Server technology creates this unified path?

A) DNS CNAME records pointing `SharedData.company.local` to both server names simultaneously.
B) DHCP Option 015 (DNS Domain Name) configured to redirect share path resolution.
C) DFS Namespaces (DFSN), which creates a virtual namespace that maps `\\company.local\SharedData` to shares on multiple underlying servers.
D) A WINS server that maps the NetBIOS name `SharedData` to the IP addresses of both file servers.

* **Correct Answer:** C) DFS Namespaces (DFSN), which creates a virtual namespace that maps `\\company.local\SharedData` to shares on multiple underlying servers.
* **Distractor Analysis:**
  * *Why A is incorrect:* DNS CNAME records resolve a hostname to another hostname or IP address — they do not create an SMB namespace. A CNAME pointing to a server name still exposes the underlying server name when the share is opened.
  * *Why B is incorrect:* DHCP Option 015 sets the DNS domain suffix appended to unqualified hostnames — it has no capability to redirect or aggregate SMB share paths.
  * *Why D is incorrect:* WINS maps NetBIOS names to IP addresses for legacy name resolution and has no concept of SMB namespace aggregation. It is also a legacy technology deprecated in modern Windows Server environments.

---

### Question 3

A network administrator is configuring DHCP for a new subnet (192.168.10.0/24). The network printers on this subnet must always receive the same IP address so that users can print reliably. Which DHCP feature ensures a specific printer always receives the same IP address based on its MAC address?

A) DHCP Superscope, which combines multiple scopes to serve large subnets with consistent addresses.
B) DHCP Exclusion Range, which removes a block of addresses from the pool so they can be assigned statically on the device.
C) DHCP Reservation, which maps a specific MAC address to a specific IP address so the device always receives the same lease.
D) DHCP Split Scope, which divides the address pool between two DHCP servers for redundancy.

* **Correct Answer:** C) DHCP Reservation, which maps a specific MAC address to a specific IP address so the device always receives the same lease.
* **Distractor Analysis:**
  * *Why A is incorrect:* A DHCP Superscope is used to serve multiple logical subnets from a single DHCP server when multiple IP subnets share the same physical network segment. It does not bind specific addresses to specific devices.
  * *Why B is incorrect:* An exclusion range removes addresses from the pool so that the DHCP server never leases them — this allows the addresses to be configured statically on the device itself. However, it provides no enforcement that the device actually uses the intended address; a DHCP Reservation provides that guarantee via MAC binding.
  * *Why D is incorrect:* DHCP Split Scope (or DHCP Failover) distributes the address pool between two DHCP servers for redundancy. It does not associate specific addresses with specific devices.

---

### Question 4

An organization's DHCP server goes offline for maintenance. During the outage, new client computers are unable to obtain IP addresses. Which DHCP high-availability feature, when configured in advance, would have allowed clients to continue receiving leases during the DHCP server outage?

A) DHCP Superscope configured with an overlapping IP range as a backup pool.
B) DHCP Failover configured in Hot Standby mode, where a partner server takes over automatically when the primary is unreachable.
C) DHCP Audit Logging enabled on a secondary server to replay lease assignments during an outage.
D) DNS Dynamic Update configured to register DHCP leases, allowing clients to use DNS for IP assignment.

* **Correct Answer:** B) DHCP Failover configured in Hot Standby mode, where a partner server takes over automatically when the primary is unreachable.
* **Distractor Analysis:**
  * *Why A is incorrect:* Overlapping scopes on two separate DHCP servers without failover coordination would cause IP address conflicts, not high availability. Failover coordinates the address pool between the servers to prevent this.
  * *Why C is incorrect:* DHCP Audit Logging records lease activity to a log file for auditing and troubleshooting purposes — it does not enable a secondary server to serve DHCP leases during a primary server outage.
  * *Why D is incorrect:* DNS Dynamic Update registers hostnames for DHCP clients in DNS — it is not a DHCP service or address assignment mechanism. Clients still require a DHCP server to receive an IP address.

---

### Question 5

A DNS administrator notices that clients are resolving an internal hostname to an incorrect IP address even after the DNS A record was updated. The TTL on the record is set to 3600 seconds. What is the most likely cause, and what is the correct immediate remediation?

A) The secondary DNS zone has not transferred the updated record; force a zone transfer from the primary by running `dnscmd /ZoneRefresh`.
B) Client DNS caches are holding the old record for up to the TTL duration; flush the client cache with `ipconfig /flushdns` and force the DNS server cache to clear with `dnscmd /ClearCache`.
C) The DHCP server assigned a conflicting IP address that overrides the DNS record; release and renew the client IP with `ipconfig /release` and `ipconfig /renew`.
D) The DNS forwarder is returning a cached result from an upstream server; restart the DNS Server service on the forwarder.

* **Correct Answer:** B) Client DNS caches are holding the old record for up to the TTL duration; flush the client cache with `ipconfig /flushdns` and force the DNS server cache to clear with `dnscmd /ClearCache`.
* **Distractor Analysis:**
  * *Why A is incorrect:* If the zone is AD-integrated, there are no secondary zones requiring manual zone transfers — AD replication handles distribution. If the update was made on an authoritative server and has already replicated, secondary zone transfer is not the issue.
  * *Why C is incorrect:* DHCP assigns IP addresses to client interfaces and does not override DNS A records. The DNS record for a server or device is what determines which IP address clients resolve — renewing the DHCP lease would not fix an incorrect DNS record that was already updated.
  * *Why D is incorrect:* If the DNS A record was updated on the internal authoritative server, the forwarder is irrelevant for internal name resolution. Internal DNS queries for `corp.local` names are answered by the authoritative internal DNS server, not forwarded to an external forwarder.
