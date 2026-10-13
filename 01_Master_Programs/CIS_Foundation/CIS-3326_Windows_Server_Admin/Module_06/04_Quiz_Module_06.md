# Quiz: Module 06 - DNS and DHCP Server Roles

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Instructions

Select the best answer for each question. Each question is worth 10 points. Review your Reading Guide and video notes before beginning.

---

### Question 1

A Windows Server DNS administrator wants to ensure that only domain-joined computers can dynamically register DNS records in the company's internal DNS zones, preventing rogue or non-domain devices from polluting the zone with false records. Which DNS zone configuration satisfies this requirement?

A) A standard primary zone stored as a text file on the primary DNS server, with dynamic updates set to "Nonsecure and Secure."

B) An Active Directory-integrated zone with dynamic updates set to "Secure only," so only authenticated domain computers can register records.

C) A secondary zone replicated from the primary server, with all dynamic updates disabled at the secondary.

D) A stub zone that contains only NS and SOA records, preventing any dynamic registration.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: "Nonsecure and Secure" allows any client — including non-domain devices — to register DNS records without authentication, which is exactly the problem the question describes.
  - Why C is incorrect: Secondary zones are read-only replicas and cannot accept dynamic updates at all. They do not solve the authentication requirement and would prevent legitimate client registration.
  - Why D is incorrect: Stub zones contain only delegation records (NS, SOA, and glue A records). They are used for conditional forwarding and delegation, not for hosting client records.

---

### Question 2

A company has two file servers — one in New York and one in Los Angeles. Users currently use `\\NY-FS01\Data` and `\\LA-FS01\Data`. Management wants users to access all company files through the single path `\\company.local\SharedData`. Which Windows Server technology creates this unified path?

A) DNS CNAME records pointing `SharedData.company.local` to both server names simultaneously.

B) DHCP Option 015 (DNS Domain Name) configured to redirect share path resolution.

C) DFS Namespaces (DFSN), which creates a virtual namespace that maps `\\company.local\SharedData` to shares on multiple underlying servers.

D) A WINS server that maps the NetBIOS name `SharedData` to the IP addresses of both file servers.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: DNS CNAME records resolve a hostname to another hostname — they do not create an SMB share namespace. The underlying server name is still exposed.
  - Why B is incorrect: DHCP Option 015 sets the DNS suffix appended to unqualified hostnames. It has no capability to redirect SMB share paths.
  - Why D is incorrect: WINS maps NetBIOS names to IP addresses for legacy name resolution. It has no concept of SMB namespace aggregation and is deprecated in modern environments.

---

### Question 3

A network administrator is configuring DHCP for a new subnet (192.168.10.0/24). The network printers on this subnet must always receive the same IP address so that users can print reliably. Which DHCP feature ensures a specific printer always receives the same IP address based on its MAC address?

A) DHCP Superscope, which combines multiple scopes to serve large subnets with consistent addresses.

B) DHCP Exclusion Range, which removes a block of addresses from the pool so they can be assigned statically on the device.

C) DHCP Reservation, which maps a specific MAC address to a specific IP address so the device always receives the same lease.

D) DHCP Split Scope, which divides the address pool between two DHCP servers for redundancy.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: A DHCP Superscope is used to serve multiple logical subnets from a single DHCP server on the same physical segment. It does not bind specific addresses to specific devices.
  - Why B is incorrect: An exclusion range removes addresses from the pool so DHCP never leases them — the device must be statically configured. There is no enforcement that the device actually uses the intended address; a reservation provides that guarantee.
  - Why D is incorrect: DHCP Split Scope distributes the address pool between two DHCP servers for redundancy. It does not associate specific addresses with specific devices.

---

### Question 4

An organization's DHCP server goes offline for maintenance. During the outage, new client computers are unable to obtain IP addresses. Which DHCP high-availability feature, when configured in advance, would have allowed clients to continue receiving leases during the DHCP server outage?

A) DHCP Superscope configured with an overlapping IP range as a backup pool.

B) DHCP Failover configured in Hot Standby mode, where a partner server takes over automatically when the primary is unreachable.

C) DHCP Audit Logging enabled on a secondary server to replay lease assignments during an outage.

D) DNS Dynamic Update configured to register DHCP leases, allowing clients to use DNS for IP assignment.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Overlapping scopes on two separate DHCP servers without failover coordination would cause IP address conflicts, not high availability. DHCP Failover coordinates the address pool to prevent conflicts.
  - Why C is incorrect: DHCP Audit Logging records lease activity to a log file for auditing and troubleshooting. It does not enable a secondary server to serve DHCP leases during an outage.
  - Why D is incorrect: DNS Dynamic Update registers client hostnames in DNS — it is not a DHCP service or address assignment mechanism. Clients still require a DHCP server to receive an IP address.

---

### Question 5

A DNS administrator notices that clients are resolving an internal hostname to an incorrect IP address even after the DNS A record was updated. The TTL on the record is set to 3600 seconds. What is the most likely cause, and what is the correct immediate remediation?

A) The secondary DNS zone has not transferred the updated record; force a zone transfer from the primary by running `dnscmd /ZoneRefresh`.

B) Client DNS caches are holding the old record for up to the TTL duration; flush the client cache with `ipconfig /flushdns` and force the DNS server cache to clear with `dnscmd /ClearCache`.

C) The DHCP server assigned a conflicting IP address that overrides the DNS record; release and renew the client IP with `ipconfig /release` and `ipconfig /renew`.

D) The DNS forwarder is returning a cached result from an upstream server; restart the DNS Server service on the forwarder.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: If the zone is AD-integrated, there are no secondary zones requiring manual zone transfers. If the zone is primary, and the record was updated on the authoritative server, zone transfer is not the issue.
  - Why C is incorrect: DHCP assigns IP addresses to client interfaces and does not override DNS A records. Releasing and renewing the DHCP lease does not affect what IP address a DNS record resolves to.
  - Why D is incorrect: Internal DNS queries for `corp.local` names are answered by the authoritative internal DNS server, not forwarded to an external forwarder. The forwarder is irrelevant for internal name resolution.

---

### Question 6

An administrator runs the following PowerShell command and receives no output. What is the most likely explanation?

```powershell
Get-DhcpServerInDC
```

A) The DHCP Server role is not installed on any server in the domain.

B) No DHCP servers have been authorized in Active Directory for this domain.

C) The DHCP service is stopped on DC1 but the server remains authorized.

D) The command requires the `-ComputerName` parameter to specify the domain controller to query.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Get-DhcpServerInDC` queries the AD Configuration partition for the authorized servers list — it does not check whether the DHCP role is installed on any server. An installed but unauthorized server would still return no output.
  - Why C is incorrect: The DHCP service state (running or stopped) does not affect what appears in the AD authorization list. An authorized server that is stopped still appears in `Get-DhcpServerInDC` output.
  - Why D is incorrect: `Get-DhcpServerInDC` queries the local domain's AD Configuration partition and does not require a `-ComputerName` parameter. It returns the domain-wide list of authorized DHCP servers.

---

### Question 7

A DNS zone has aging enabled with a No-refresh interval of 7 days and a Refresh interval of 7 days. A client computer registered its A record on Monday. On what day does the record first become eligible for scavenging?

A) The following Monday (7 days after registration).

B) The following Monday plus 7 days — 14 days after registration.

C) Immediately after the Refresh interval expires, regardless of the No-refresh interval.

D) Only after an administrator manually runs `Start-DnsServerScavenging`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The No-refresh interval (7 days) must expire first, then the Refresh interval (another 7 days) must expire. Total = 14 days before scavenging eligibility, not 7.
  - Why C is incorrect: The Refresh interval does not start until after the No-refresh interval expires. The two intervals are sequential, not parallel.
  - Why D is incorrect: Manual scavenging initiates the scavenging process but records only become eligible after the full aging period elapses. Running the scavenge manually before the 14-day aging period would not remove a record registered on Monday.

---

### Question 8

An administrator needs to configure DNS so that queries for `partner.com` are forwarded to the partner company's DNS server at `10.10.1.1`, while all other external queries continue to resolve through the ISP's DNS server at `203.0.113.1`. Which DNS feature provides this behavior?

A) Configure a second forwarder entry pointing to `10.10.1.1` after the ISP entry `203.0.113.1`.

B) Configure a Conditional Forwarder for `partner.com` pointing to `10.10.1.1`, while the general Forwarder remains set to `203.0.113.1`.

C) Create a Stub Zone for `partner.com` with `10.10.1.1` as the master server.

D) Enable Root Hints and add `10.10.1.1` as a custom root server for the `.com` TLD.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Regular Forwarders are tried in order and the server tries each one for any query it cannot resolve. Adding a second forwarder entry does not selectively route queries for a specific domain to a specific server.
  - Why C is incorrect: A Stub Zone stores only delegation records (NS, SOA, glue A) for the zone. It tells the DNS server which servers are authoritative for `partner.com` but does not route queries the same way a Conditional Forwarder does, and it requires zone transfer access to the partner server.
  - Why D is incorrect: Root Hints contain the addresses of internet root servers. Adding a partner DNS server as a root hint would route all `.com` queries to the partner, not just `partner.com` queries — and it would also break normal internet resolution.

---

### Question 9

After installing the DHCP role on a Windows Server 2022 domain member server, the administrator creates a scope and activates it. Clients on the subnet receive APIPA addresses (`169.254.x.x`) instead of DHCP leases. What is the most likely cause?

A) The DHCP scope overlaps with the existing DNS zone for the subnet.

B) The DHCP server has not been authorized in Active Directory, so it refuses to serve leases to domain-joined clients.

C) The DHCP service cannot start until a Windows Server restart completes the role installation.

D) The DHCP scope's exclusion range covers the entire address pool, leaving no addresses available to lease.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: DNS zones and DHCP scopes are independent services. A DHCP scope address range does not conflict with a DNS zone — they serve different functions and are not aware of each other's configuration.
  - Why C is incorrect: DHCP role installation on Windows Server 2022 typically does not require a restart before the service starts. The most common reason leases are not served on a domain-joined server is missing authorization.
  - Why D is incorrect: An exclusion range covering the entire pool would cause leases to fail, but the question states the administrator just created and activated the scope — an exhausted exclusion range is unlikely immediately after setup. Authorization failure is the most common cause of APIPA in a domain environment after DHCP installation.

---

### Question 10

Which PowerShell command creates a DHCP scope named "BranchOffice" for the `10.0.5.0/24` network with an address range from `10.0.5.50` to `10.0.5.150` and sets it to Active immediately?

A) `New-DhcpServerv4Scope -Name "BranchOffice" -Network 10.0.5.0/24 -Range 10.0.5.50-10.0.5.150 -Enable`

B) `Add-DhcpServerv4Scope -Name "BranchOffice" -StartRange 10.0.5.50 -EndRange 10.0.5.150 -SubnetMask 255.255.255.0 -State Active`

C) `Set-DhcpServerv4Scope -Name "BranchOffice" -StartRange 10.0.5.50 -EndRange 10.0.5.150 -SubnetMask 255.255.255.0 -Activate`

D) `Add-DhcpScope -NetworkId 10.0.5.0 -Mask 255.255.255.0 -Range 10.0.5.50 10.0.5.150 -Name "BranchOffice"`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `New-DhcpServerv4Scope` is not a valid DHCP PowerShell cmdlet. The correct cmdlet for creating a new scope is `Add-DhcpServerv4Scope`. The `-Network` and `-Range` parameters shown are also not valid for this cmdlet.
  - Why C is incorrect: `Set-DhcpServerv4Scope` modifies an existing scope — it does not create a new one. Using `Set-` on a scope that does not yet exist would produce an error. The `-Activate` parameter is also not valid for this cmdlet.
  - Why D is incorrect: `Add-DhcpScope` is not a valid PowerShell cmdlet. All Windows Server DHCP cmdlets follow the `Add-DhcpServerv4*` / `Get-DhcpServerv4*` / `Set-DhcpServerv4*` naming pattern.

---

### Question 11 (5 points)

An administrator creates a conditional forwarder for `partner.com` pointing to `10.10.1.1`. Queries for `partner.com` are failing. The administrator can ping `10.10.1.1` successfully from the DNS server. What should be checked next?

- A) Whether the DNS Server service needs to be restarted after creating a conditional forwarder
- B) Whether port 53 (UDP and TCP) is allowed through the firewall between the DNS server and `10.10.1.1`
- C) Whether the conditional forwarder needs to be set as Enforced in Active Directory
- D) Whether the corp.local forward lookup zone is configured to allow non-secure dynamic updates

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: DNS conditional forwarders take effect immediately without a service restart. The DNS Server service does not need to be restarted after adding a forwarder.
  - Why C is incorrect: The "Enforce" option in DNS conditional forwarder settings means the forwarder is authoritative for that zone. It does not relate to firewall or network connectivity issues.
  - Why D is incorrect: The corp.local dynamic update setting controls which clients can register records in the local zone. It has no effect on outbound forwarding queries to external servers.

---

### Question 12 (5 points)

A company has a main office subnet `10.0.1.0/24` and a branch office subnet `10.0.2.0/24`. Both are served by the same DHCP server. There is a DHCP relay agent on the router between the two subnets. Which DHCP configuration is required to serve both subnets from a single DHCP server?

- A) One DHCP scope with a superscope spanning both subnets
- B) Two separate DHCP scopes — one for each subnet — because each scope corresponds to one logical network
- C) One DHCP scope with two exclusion ranges covering the second subnet
- D) Two DHCP servers — one per subnet — because DHCP cannot serve multiple subnets from one server

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A superscope is used to logically group multiple scopes when multiple logical IP networks share the same physical segment (multinet scenario). It is not required for serving multiple separate subnets through a relay agent.
  - Why C is incorrect: Exclusion ranges remove addresses from an existing scope's pool. They cannot extend a scope to serve a different subnet or network.
  - Why D is incorrect: A single DHCP server can serve multiple subnets. The DHCP relay agent on the router forwards DHCP broadcasts from the remote subnet to the DHCP server, which responds using the scope that matches the relay agent's IP address.

---

### Question 13 (5 points)

Which DNS record type would an administrator create to allow email to be sent to addresses at `corp.local` by directing SMTP traffic to the correct mail server?

- A) A record pointing `mail.corp.local` to the Exchange server IP
- B) MX record pointing `corp.local` to the mail server hostname with a priority value
- C) SRV record for `_smtp._tcp.corp.local` pointing to the Exchange server
- D) CNAME record from `smtp.corp.local` to the Exchange server hostname

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: An A record resolves a hostname to an IP address. While mail servers also have A records, the A record itself does not tell other mail servers where to deliver email for the `corp.local` domain. That is the purpose of the MX record.
  - Why C is incorrect: An SRV record for `_smtp._tcp` is not a standard email routing mechanism. MX records are the authoritative record type for mail exchanger designation in DNS.
  - Why D is incorrect: A CNAME is an alias. While it can resolve a name to another hostname, it does not designate a server as a mail exchanger for a domain. RFC standards explicitly prohibit using CNAME records as MX record targets.

---

### Question 14 (5 points)

A DHCP administrator wants to ensure all clients in the `192.168.10.0/24` scope receive `192.168.10.1` as their default gateway and `192.168.10.10` as their DNS server. Where should these values be configured?

- A) As DHCP server-level options that apply to all scopes on the server
- B) As scope options on the `192.168.10.0/24` scope specifically
- C) As DHCP reservations for the gateway and DNS server addresses
- D) As exclusion ranges that reserve those IPs for infrastructure devices

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Server-level options apply to all scopes on the DHCP server. Configuring them at the server level is appropriate if the same gateway and DNS apply to all scopes, but scope-level options are more targeted when different scopes need different values.
  - Why C is incorrect: Reservations bind a MAC address to a specific IP address for client devices. The gateway and DNS server addresses are infrastructure values provided to clients — they are not themselves clients receiving leases.
  - Why D is incorrect: Exclusion ranges remove addresses from the lease pool so DHCP never assigns them. They do not tell clients which gateway or DNS server to use.

---

### Question 15 (5 points)

An administrator needs to find all active DHCP leases on the `192.168.10.0` scope to audit which clients are currently connected. Which PowerShell command retrieves this information?

- A) `Get-DhcpServerv4Lease -ScopeId 192.168.10.0`
- B) `Get-DhcpServerv4Scope -ScopeId 192.168.10.0 -ShowLeases`
- C) `Show-DhcpServerv4Lease -Network 192.168.10.0`
- D) `Get-DhcpServerv4Statistics -ScopeId 192.168.10.0 | Select-Object Leases`

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: `Get-DhcpServerv4Scope` returns scope configuration details such as address range, state, and lease duration. It does not have a `-ShowLeases` parameter and does not return active lease records.
  - Why C is incorrect: `Show-DhcpServerv4Lease` is not a valid PowerShell cmdlet. The correct verb for retrieving lease data is `Get-`.
  - Why D is incorrect: `Get-DhcpServerv4Statistics` returns aggregate statistics such as total addresses, addresses in use, and available addresses — not the individual lease records with hostname and MAC information.

---

### Question 16 (5 points)

What is the purpose of enabling DNS Record Scavenging, and what risk does it mitigate?

- A) It compresses DNS zone files to reduce SYSVOL storage usage
- B) It removes stale DNS records left by computers that were decommissioned or renamed without deregistering their DNS records, preventing resolution of non-existent hosts
- C) It prevents unauthorized clients from registering DNS records in the zone
- D) It synchronizes DNS records between primary and secondary zones faster than standard zone transfers

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: DNS scavenging has no effect on file compression or SYSVOL storage. Zone file size is managed through normal record deletion, not scavenging.
  - Why C is incorrect: Preventing unauthorized DNS registration is controlled by the Dynamic Update setting (Secure Only). Scavenging removes old records; it does not authenticate new registrations.
  - Why D is incorrect: Zone transfer speed is unrelated to scavenging. Zone transfers are governed by replication schedule settings and the AD replication topology, not scavenging intervals.

---

### Question 17 (5 points)

A DNS server is configured with Root Hints. An administrator adds an external forwarder at `8.8.8.8`. How does the DNS server decide whether to use the forwarder or Root Hints for an external query?

- A) Root Hints are always used first; forwarders are only tried if Root Hints fail
- B) The DNS server uses the forwarder first; if the forwarder fails or is unavailable, it falls back to Root Hints
- C) Forwarders and Root Hints are queried simultaneously, and the faster response wins
- D) Root Hints are disabled automatically once a forwarder is configured

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Root Hints are the fallback mechanism, not the primary. The DNS server contacts its configured forwarder first. Root Hints are only used if the forwarder does not respond.
  - Why C is incorrect: DNS does not query both simultaneously. The forwarder is tried first; Root Hints are the sequential fallback.
  - Why D is incorrect: Configuring a forwarder does not disable Root Hints. They remain available as a fallback. An administrator can explicitly disable Root Hints use (the "Use root hints if no forwarders are available" checkbox), but they are not automatically removed.

---

### Question 18 (5 points)

An administrator sets the DHCP lease duration for the main office scope to 8 days. What is the practical effect of a very long lease duration compared to a very short one?

- A) Long leases reduce network traffic by requiring clients to renew less frequently, but waste IP addresses if clients leave the network without releasing their leases
- B) Long leases increase DNS scavenging frequency because clients update their DNS records more often
- C) Short leases reduce DHCP server load because fewer lease records are stored in the database
- D) Short leases guarantee that clients always receive the same IP address across reboots

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: Lease duration and DNS scavenging are independent configurations. A long DHCP lease does not cause more frequent DNS updates. DNS records are refreshed on their own TTL cycle.
  - Why C is incorrect: Short leases actually increase DHCP server load because clients must renew more frequently, generating more DHCPREQUEST/DHCPACK traffic and more database writes.
  - Why D is incorrect: Consistent IP assignment across reboots requires a DHCP reservation tied to the MAC address. Lease duration only affects how long a lease is valid, not whether the same address is reissued.

---

### Question 19 (5 points)

An administrator configures DHCP Failover in Load Balance mode with a 60/40 split between two DHCP servers. What does the 60/40 configuration mean?

- A) Server 1 serves leases for 60% of the time; Server 2 serves leases for the remaining 40%
- B) 60% of the IP address pool is managed by Server 1 and 40% by Server 2; both servers are always active simultaneously
- C) Server 1 holds 60 days of lease history; Server 2 holds 40 days
- D) Server 1 handles renewals and Server 2 handles new leases, split 60/40 by request type

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Load Balance mode does not mean time-based rotation between servers. Both servers are simultaneously active, each managing a portion of the address pool.
  - Why C is incorrect: The 60/40 percentage refers to the address pool split, not lease history retention durations.
  - Why D is incorrect: DHCP Failover Load Balance mode splits the address pool, not the request type. Both servers handle both renewals and new requests for their respective portions of the pool.

---

### Question 20 (5 points)

A client workstation running `ipconfig /all` shows an IPv4 address of `169.254.23.45` with a subnet mask of `255.255.0.0`. What does this address indicate, and what is the most likely cause?

- A) The workstation is using a statically configured APIPA address assigned by the administrator for a test network
- B) The workstation failed to obtain a DHCP lease and self-assigned an Automatic Private IP Addressing (APIPA) address; the DHCP server is unreachable
- C) The workstation received a DHCP lease from an unauthorized DHCP server on a different subnet
- D) The workstation has a duplicate IP conflict with another device and Windows assigned a fallback address

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: APIPA addresses in the `169.254.0.0/16` range are automatically self-assigned by Windows when no DHCP server responds. They are not administratively assigned and are not intended for use as static addresses.
  - Why C is incorrect: If the workstation received a lease from any DHCP server, it would have a valid routable address, not an APIPA address. APIPA only activates when no DHCP response is received at all.
  - Why D is incorrect: IP address conflicts in Windows result in the second device losing its address and showing a limited connectivity warning, but the address shown would be the conflicting address, not an APIPA address. APIPA results specifically from DHCP unavailability.
