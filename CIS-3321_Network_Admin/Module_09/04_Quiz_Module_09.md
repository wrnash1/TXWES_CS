# Quiz: Module 09 - Network Services – DNS, DHCP, and NTP
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A DNS administrator needs to configure the company's domain so that email sent to @example.com is delivered to the correct mail server. Which DNS record type must be created?
A) A record — maps the mail server's hostname to its IPv4 address for delivery routing
B) CNAME record — creates an alias from the mail server hostname to the domain's canonical name
C) MX record — identifies the mail server responsible for accepting email for the domain, with a priority value
D) PTR record — resolves the mail server's IP address back to its hostname for reverse DNS lookup
*   **Correct Answer:** C) MX record — identifies the mail server responsible for accepting email for the domain, with a priority value
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An A record maps a hostname to an IPv4 address — it does not direct email delivery for a domain. While the mail server itself likely has an A record, the MX record is what tells other mail servers where to send email for the domain.
    *   *Why B is incorrect:* A CNAME record creates a hostname alias — it is not used to designate a mail server for a domain. CNAME records cannot be used for MX record targets, and using a CNAME to alias the mail server hostname would not configure email routing.
    *   *Why D is incorrect:* A PTR record is used for reverse DNS lookup (IP to hostname) — it does not configure email delivery routing. PTR records are important for mail server reputation but do not direct incoming mail.

---

**Question 2**
A network administrator receives a support ticket: a workstation on VLAN 20 cannot obtain an IP address from the DHCP server located on VLAN 1. Workstations on VLAN 1 obtain addresses normally. The VLAN 20 interface on the Layer 3 switch has an IP address of 192.168.20.1. The DHCP server is at 192.168.1.50. Which configuration resolves this issue?
A) Create a DHCP reservation on the server mapping the VLAN 20 interface MAC address to 192.168.20.1
B) Configure `ip helper-address 192.168.1.50` on the VLAN 20 switch virtual interface to relay DHCP broadcasts to the server
C) Add a static route on the DHCP server pointing 192.168.20.0/24 to the default gateway
D) Configure the workstations on VLAN 20 with a static IP address in the 192.168.20.0/24 range
*   **Correct Answer:** B) Configure `ip helper-address 192.168.1.50` on the VLAN 20 switch virtual interface to relay DHCP broadcasts to the server
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A DHCP reservation maps a specific MAC address to a specific IP — it does not solve the problem that DHCP broadcast messages from VLAN 20 never reach the server on VLAN 1. The broadcasts are still dropped at the Layer 3 boundary.
    *   *Why C is incorrect:* Adding a static route on the DHCP server allows it to route packets to VLAN 20, but the DHCP client's initial Discover is a broadcast that cannot be routed — the relay agent on the VLAN 20 interface is still required to convert the broadcast to a unicast before it can cross the Layer 3 boundary.
    *   *Why D is incorrect:* Configuring static IPs is a workaround that bypasses DHCP entirely — it does not fix the relay configuration and creates additional administrative overhead. The question asks what resolves the DHCP relay issue.

---

**Question 3**
A security engineer is reviewing authentication failures in the domain controller logs. The logs show "clock skew too great" errors for multiple workstations attempting to authenticate. Which service, if misconfigured, is causing these failures, and what is the standard maximum clock skew tolerance?
A) DNS — the domain controller cannot resolve the workstation hostnames because the TTL on A records has expired
B) DHCP — workstations are receiving expired IP leases that no longer match the domain controller's subnet expectations
C) NTP — clocks are not synchronized; Kerberos authentication fails when clock skew exceeds 5 minutes
D) RADIUS — the authentication server is rejecting credentials because the session token timestamp is out of range
*   **Correct Answer:** C) NTP — clocks are not synchronized; Kerberos authentication fails when clock skew exceeds 5 minutes
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DNS TTL expiration does not generate "clock skew" errors. A DNS failure would produce name resolution errors or "host not found" messages — not clock skew authentication failures.
    *   *Why B is incorrect:* Expired DHCP leases cause IP address issues and connectivity loss — not Kerberos authentication errors. DHCP lease expiration produces different error messages related to address assignment, not time skew.
    *   *Why D is incorrect:* RADIUS is used for 802.1X and VPN authentication — not Kerberos. The "clock skew too great" error message is specific to the Kerberos protocol, which requires synchronized clocks and enforces a default 5-minute maximum skew.

---

**Question 4**
A user reports they can access websites by IP address (e.g., http://93.184.216.34) but cannot browse by hostname (e.g., http://www.example.com). Which service has failed, and what is the first troubleshooting step?
A) DHCP has failed — run `ipconfig /release` and `ipconfig /renew` to obtain a new IP address from the server
B) DNS has failed — run `nslookup www.example.com` to confirm whether the configured DNS server is responding to queries
C) The default gateway is unreachable — run `ping 93.184.216.34` to verify basic IP routing to the internet
D) NTP has failed — synchronize the workstation clock using `w32tm /resync` and retry the hostname lookup
*   **Correct Answer:** B) DNS has failed — run `nslookup www.example.com` to confirm whether the configured DNS server is responding to queries
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The user can already reach IP addresses on the internet, which proves DHCP has provided a valid IP configuration including a working default gateway. DHCP failure would prevent all IP connectivity, not just hostname resolution.
    *   *Why C is incorrect:* The user can already ping 93.184.216.34 successfully by IP — the default gateway and internet routing are confirmed working. The only broken function is hostname-to-IP translation, which is exclusively a DNS function.
    *   *Why D is incorrect:* NTP failure causes clock synchronization issues affecting Kerberos authentication and certificate validation — it does not prevent hostname resolution. A failed NTP service would not explain why IP access works but hostname access does not.

---

**Question 5**
A network administrator needs to harden the DNS, DHCP, and NTP infrastructure against common attacks. Which combination of controls best addresses (1) DNS cache poisoning, (2) rogue DHCP servers on the network, and (3) NTP amplification attacks used in DDoS?
A) Enable DNSSEC on all authoritative zones, configure DHCP snooping on all access switches, and restrict NTP to respond only to trusted client IP ranges using access control lists.
B) Increase DNS TTL values to 86400 seconds, assign static IP addresses to all DHCP clients, and disable NTP on all network devices.
C) Configure split-horizon DNS to serve different records internally and externally, enable DHCP relay agents on all VLANs, and upgrade to NTPv4.
D) Deploy a DNSSEC-validating recursive resolver, enable DHCP failover between two servers for redundancy, and configure NTP authentication using MD5 keys.
*   **Correct Answer:** A) Enable DNSSEC on all authoritative zones, configure DHCP snooping on all access switches, and restrict NTP to respond only to trusted client IP ranges using access control lists.
*   **Distractor Analysis:**
    *   *Why A is correct:* DNSSEC prevents cache poisoning by digitally signing DNS records (requirement 1); DHCP snooping on switches drops unauthorized DHCP server responses from untrusted ports, eliminating rogue DHCP servers (requirement 2); NTP ACLs restrict which hosts the NTP server responds to, preventing it from being used as an amplification reflector (requirement 3).
    *   *Why B is incorrect:* Increasing TTL reduces query frequency but does not prevent cache poisoning — a poisoned record will simply persist longer. Static IPs remove DHCP entirely rather than securing it. Disabling NTP eliminates time synchronization security, which creates Kerberos and certificate validation failures.
    *   *Why C is incorrect:* Split-horizon DNS controls what records external vs. internal clients see — it does not prevent cache poisoning. DHCP relay agents forward broadcasts between subnets — they do not block rogue DHCP servers. NTPv4 is the current standard but version alone does not prevent amplification attacks without access controls.
    *   *Why D is incorrect:* A DNSSEC-validating resolver protects clients from receiving poisoned records but does not protect the authoritative zone itself from being targeted — DNSSEC on authoritative zones is required. DHCP failover provides redundancy, not rogue server prevention. NTP MD5 authentication authenticates peers to prevent unauthorized time sources but does not prevent amplification attacks from external hosts.
