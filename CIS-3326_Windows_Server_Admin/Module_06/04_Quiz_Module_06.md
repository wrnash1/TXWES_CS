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
