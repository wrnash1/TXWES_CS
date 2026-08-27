# Quiz: Module 04 – Enterprise Security & Infrastructure Hardening
## CSC-6361 Advanced Computer Networks | Graduate Level
## 10 Questions | 30-Minute Time Limit | 1 Attempt
## Due: Sunday, November 15, 2026 at 11:59 PM CST

---

### Question 1 (Multiple Choice — 10 pts)
A network engineer configures `aaa authentication login default group TACACS+ local`. The TACACS+ server goes offline. What happens when an administrator attempts to log in via SSH?

- A) The login fails immediately because TACACS+ is the primary method. ❌
- B) The router uses the local username database as a fallback, and login succeeds if valid local credentials are provided. ✅
- C) The router locks out all SSH sessions until TACACS+ is restored. ❌
- D) The router falls back to no authentication and grants access without credentials. ❌

**Answer:** B — The keyword `local` at the end of the AAA authentication statement is the fallback method. If the TACACS+ server group is unreachable, the router uses the locally configured username database. This is a critical design requirement — without the fallback, a TACACS+ outage would lock all administrators out of every network device.

---

### Question 2 (Multiple Choice — 10 pts)
Which key difference makes TACACS+ preferred over RADIUS for managing Cisco network devices?

- A) RADIUS uses TCP; TACACS+ uses UDP, making TACACS+ faster. ❌
- B) TACACS+ encrypts the entire payload and supports per-command authorization, allowing fine-grained control over which commands each user can execute. ✅
- C) RADIUS supports 802.1X authentication; TACACS+ does not. ❌
- D) TACACS+ is an open IEEE standard; RADIUS is Cisco proprietary. ❌

**Answer:** B — TACACS+ is preferred for device administration because: (1) the entire payload is encrypted (not just the password), and (2) authorization can be configured per-command — for example, allowing a junior engineer to run `show` commands but not `no shutdown` or `configure terminal`. RADIUS encrypts only the password and combines authentication and authorization, providing less granularity.

---

### Question 3 (Multiple Choice — 10 pts)
An access-list is applied inbound on a router's WAN interface. The list contains:
```
permit tcp any 10.10.0.0 0.0.255.255 established
deny ip any any log
```
What type of traffic does this ACL permit?

- A) All TCP traffic from any source to the 10.10.0.0/16 network. ❌
- B) Only TCP traffic with the ACK or RST bit set destined for the 10.10.0.0/16 network — return traffic for sessions initiated from inside. ✅
- C) All traffic to the 10.10.0.0/16 network with the SYN flag set. ❌
- D) ICMP echo replies from any source to the internal network. ❌

**Answer:** B — The `established` keyword matches TCP packets with the ACK or RST bit set, which are characteristic of return traffic in an established connection. A TCP SYN-only packet (a new connection attempt from outside) would not match and would hit the `deny ip any any log`.

---

### Question 4 (Multiple Choice — 10 pts)
DHCP Snooping is enabled on a switch for VLAN 10. A legitimate access switch (AS-2) is connected to an uplink port. An administrator mistakenly configures AS-2's uplink port as untrusted. What will happen?

- A) Only DHCP Request packets from AS-2 will be dropped. ❌
- B) DHCP Offer and DHCP Ack packets forwarded through that port from the DHCP server will be dropped, causing devices connected to AS-2 to fail to receive DHCP addresses. ✅
- C) The switch will automatically detect AS-2 as a trusted device and override the configuration. ❌
- D) DHCP traffic will still pass normally — untrusted ports only block rogue servers. ❌

**Answer:** B — Untrusted ports drop DHCP server messages (Offer, Ack, Nak). If a legitimate uplink to another switch (which relays DHCP responses from the server) is set to untrusted, those responses are dropped before they reach end devices, causing DHCP failures for all devices downstream.

---

### Question 5 (Multiple Choice — 10 pts)
Dynamic ARP Inspection (DAI) is enabled on VLAN 20. A host that received its IP address via static assignment (not DHCP) is connected to an untrusted port. All ARP packets from this host are being dropped. What is the most likely cause?

- A) DAI is incompatible with statically configured hosts. ❌
- B) The host's MAC-to-IP binding does not exist in the DHCP Snooping binding table because it was not dynamically assigned. DAI requires a valid binding table entry to permit ARP from untrusted ports. ✅
- C) The host's MAC address is blocked by Port Security. ❌
- D) DAI only inspects ARP Requests, not ARP Replies. ❌

**Answer:** B — DAI validates ARP against the DHCP Snooping binding table by default. Statically configured hosts have no binding table entry, so all their ARP traffic is dropped on untrusted ports. Resolution: create a **static ARP inspection entry** for the host: `ip arp inspection filter ARP-ACL vlan 20` or add the host to the binding table manually.

---

### Question 6 (Scenario — 10 pts)
A network engineer runs `show port-security interface FastEthernet0/5` and sees:
```
Port Security              : Enabled
Port Status                : Secure-shutdown
Violation Mode             : Shutdown
Last Source Address        : 00E0.A3B4.C5D6
Security Violation Count   : 1
```
What happened, and what must the engineer do to restore the port?

- A) The port exceeded its maximum allowed MAC count and was automatically disabled. To restore: `interface FastEthernet0/5` → `shutdown` → `no shutdown`. ✅
- B) The port received a BPDU and BPDU Guard shut it down. ❌
- C) The port security max-mac count should be increased to 0 to disable the limit. ❌
- D) The port will automatically recover after the errdisable recovery timer expires. ❌ (Only if `errdisable recovery cause psecure-violation` is configured)

**Answer:** A — `Secure-shutdown` status means Port Security placed the port in err-disabled state after detecting a MAC violation (a new MAC address appeared beyond the configured maximum). To recover: `shutdown` then `no shutdown` on the interface. If automatic recovery is desired, configure `errdisable recovery cause psecure-violation`.

---

### Question 7 (Multiple Choice — 10 pts)
An enterprise is deploying Control Plane Policing (CoPP). Which two traffic types should typically be included in the CoPP policy with rate limiting? (Select two)

- A) OSPF hello and LSA packets destined for the router CPU ✅
- B) MPLS-forwarded traffic passing through the data plane ❌
- C) ICMP packets addressed to the router itself (e.g., management pings) ✅
- D) NAT translations in the fast-path ❌

**Answer:** A and C — CoPP rate-limits traffic destined for the router's CPU (the control and management planes). OSPF hellos/LSAs and ICMP to the router are CPU-bound and can be used in flood attacks. MPLS forwarded traffic and NAT translations are data plane operations handled by hardware ASICs and are NOT subject to CoPP.

---

### Question 8 (Scenario — 10 pts)
A BGP peer is advertising 2,000,000 routes to your edge router. Your router has a `maximum-prefix 750000 80` statement configured. Describe exactly what will happen when the peer's route count reaches 600,000 and again when it exceeds 750,000.

- A) At 600,000: the BGP session is torn down. At 750,000: warning log only. ❌
- B) At 600,000 (80% of 750,000): a syslog warning is generated but the session continues. At 750,000: the BGP session is torn down and must be manually cleared or will wait for a restart timer. ✅
- C) At both thresholds: only a log message is generated; the engineer must manually tear down the session. ❌
- D) The router automatically filters excess routes without disrupting the BGP session. ❌

**Answer:** B — The `80` in `maximum-prefix 750000 80` is the warning threshold percentage. When 600,000 routes (80% of 750,000) are received, IOS logs a warning but continues the session. When the hard limit of 750,000 is exceeded, the BGP session is torn down. The `restart` keyword can configure an automatic restart timer. Without `restart`, the session stays down until manually cleared with `clear ip bgp neighbor`.

---

### Question 9 (Short Answer — 10 pts)
Explain the difference between a standard ACL and an extended ACL in terms of: (1) what they can match on, (2) where they should be placed on the network, and (3) give a real-world use case for each. (3–4 sentences)

**Model Answer:** A **standard ACL** matches only on the source IP address and should be placed as close to the destination as possible (to avoid blocking traffic unnecessarily before it reaches its destination). Example use case: restricting which hosts can access a specific VTY line with `access-class`. An **extended ACL** matches on source IP, destination IP, protocol, and source/destination port numbers, and should be placed as close to the source as possible to drop unwanted traffic early and save bandwidth on the network. Example use case: blocking all traffic except HTTP/HTTPS from the internal network to the internet on the router's LAN-facing interface. Extended ACLs are far more powerful and are the standard for enterprise traffic filtering.

---

### Question 10 (Short Answer — 10 pts)
A security auditor reviewing your BGP configuration says that MD5 authentication on BGP sessions "provides false security" because MD5 is cryptographically weak. Is the auditor correct? What does BGP MD5 authentication actually protect against, and what would you recommend as a more robust alternative? (3–4 sentences)

**Model Answer:** The auditor is partially correct. BGP MD5 authentication (RFC 2385) uses MD5 to authenticate TCP segments in the BGP session, which does protect against **session hijacking and spoofed BGP UPDATE messages** from unauthorized parties who do not know the shared secret — it is not entirely worthless. However, MD5's cryptographic weaknesses mean that a sophisticated attacker with enough resources could potentially forge valid MD5-authenticated segments. **RFC 5925 (TCP Authentication Option — TCP-AO)** is the recommended modern replacement, supporting stronger HMAC algorithms (HMAC-SHA-1, HMAC-SHA-256). Additionally, combining BGP MD5 or TCP-AO with **GTSM (Generalized TTL Security Mechanism — RFC 5082)** — which sets the TTL to 255 so only directly connected peers can send BGP packets — provides a strong layered defense.

---

> **Instructor Note — Questions 11–20:** These 10 questions are worth **5 pts each** (50 pts total). Enter as a separate quiz section or append to the existing quiz. Same format rules apply.

---

### Question 11 (Multiple Choice — 5 pts)
An engineer is configuring TACACS+ authorization and wants to allow a specific network operator to run only `show` commands at privilege level 1 and no configuration commands. Which configuration on the TACACS+ server and router correctly enforces this per-command authorization?

- A) Set the user's privilege level to 15 on the TACACS+ server and use `aaa authorization commands 15 default group TACACS+ local`. ❌
- B) Set the user's privilege level to 1 on the TACACS+ server, configure `aaa authorization commands 1 default group TACACS+ local` on the router, and define a permit list on the TACACS+ server for only `show` commands at privilege 1. ✅
- C) Configure `aaa authorization exec default group TACACS+ local` — this automatically restricts commands per user. ❌
- D) Create a named ACL on the router that blocks configuration mode access and apply it to the VTY line. ❌

**Answer:** B — Per-command authorization in TACACS+ requires: (1) the AAA authorization statement on the router specifying the privilege level (`aaa authorization commands 1 default group TACACS+ local`), (2) the TACACS+ server having a permit/deny list for each command at that privilege level for the user. The TACACS+ server is queried for every command the user attempts — if the server denies `configure terminal`, the command is blocked. This granularity is impossible with RADIUS, which does not support per-command authorization.

**Distractor Analysis:**
- A: Privilege 15 grants full access — the opposite of what is needed.
- C: `aaa authorization exec` only controls whether the user gets an EXEC shell, not which commands they can run.
- D: ACLs filter IP traffic, not CLI command access.

---

### Question 12 (Multiple Choice — 5 pts)
A network engineer applies the following CoPP policy map to the control plane:
```
policy-map COPP-POLICY
 class ICMP-CLASS
  police rate 64000 bps
 class BGP-CLASS
  police rate 2000000 bps
 class class-default
  drop
```
A legitimate BGP peer at 1.2.3.4 suddenly cannot maintain its BGP session during a period of high ICMP traffic. What is the most likely root cause?

- A) The `class-default drop` is blocking BGP packets that were not classified into BGP-CLASS. ❌
- B) The ICMP-CLASS rate limit is too low — an ICMP flood is consuming CPU before BGP packets are processed. ❌
- C) BGP traffic from 1.2.3.4 is not being matched by BGP-CLASS and is falling into `class-default drop`, because the BGP-CLASS ACL or class-map does not include that peer's IP. ✅
- D) CoPP cannot police both ICMP and BGP simultaneously on the same control plane. ❌

**Answer:** C — CoPP relies on class-maps (typically backed by ACLs or DSCP/protocol matches) to classify traffic. If the BGP-CLASS class-map does not correctly match TCP port 179 from 1.2.3.4, that BGP traffic falls to `class-default`, which is configured to drop all unclassified traffic. The fix is to verify the BGP-CLASS ACL or match condition explicitly includes the peer address and TCP port 179. A CoPP audit after every BGP peering change is a critical operational practice.

**Distractor Analysis:**
- A: This is partially correct but is not the most specific root cause — it does not explain why BGP specifically failed while ICMP was running.
- B: An ICMP flood consuming CPU would be rate-limited by ICMP-CLASS — that is exactly what CoPP prevents.
- D: CoPP processes classes sequentially and handles multiple traffic types without conflict.

---

### Question 13 (Multiple Choice — 5 pts)
What is the primary security benefit of enabling **IP Source Guard** on switch access ports, and what must be configured first for IP Source Guard to function?

- A) IP Source Guard prevents MAC spoofing by binding a port to a specific MAC address. DHCP Snooping is required first. ❌
- B) IP Source Guard drops packets whose source IP address does not match the DHCP Snooping binding table entry for that port, preventing IP address spoofing. DHCP Snooping must be enabled and the binding table populated before IP Source Guard can enforce bindings. ✅
- C) IP Source Guard encrypts traffic at Layer 2. No prerequisites are required. ❌
- D) IP Source Guard prevents rogue DHCP servers by rate-limiting DHCP traffic on untrusted ports. ❌

**Answer:** B — IP Source Guard (IPSG) filters inbound packets on untrusted access ports by comparing the source IP in each packet against the DHCP Snooping binding table. If a host uses a static IP or a spoofed IP that does not match the binding table, the packet is dropped. This stops an attacker who has gained physical access to a port from spoofing another host's IP address to intercept traffic or bypass ACLs. DHCP Snooping must be configured first to build the binding table that IPSG consults.

**Distractor Analysis:**
- A: Port Security (not IPSG) provides MAC-based binding. IPSG binds to IP addresses.
- C: IPSG is a filtering mechanism, not encryption.
- D: DHCP rate limiting on untrusted ports is a DHCP Snooping feature, not IPSG.

---

### Question 14 (Multiple Choice — 5 pts)
An enterprise is deploying MACsec (IEEE 802.1AE) on uplinks between access switches and distribution switches. Which statement about MACsec is correct?

- A) MACsec encrypts Layer 3 headers only — it does not protect Layer 2 Ethernet frames. ❌
- B) MACsec operates at Layer 2 and encrypts the entire Ethernet frame payload (from the EtherType field onward), providing hop-by-hop confidentiality and integrity on each physical link segment. ✅
- C) MACsec is an end-to-end encryption standard that operates identically to IPsec at the transport layer. ❌
- D) MACsec can only be deployed on WAN links and is not supported on switch-to-switch campus links. ❌

**Answer:** B — MACsec (IEEE 802.1AE) provides hop-by-hop encryption at Layer 2. It encrypts the payload of each Ethernet frame between directly connected devices — each switch decrypts incoming frames and re-encrypts outbound frames. This means an attacker who taps the physical cable between two switches sees only encrypted data. Unlike IPsec (which is end-to-end at Layer 3), MACsec protects each link segment independently, making it ideal for protecting campus backbone links where physical access is a risk.

**Distractor Analysis:**
- A: MACsec encrypts the entire Ethernet payload starting from the EtherType, including Layer 3 headers and above.
- C: IPsec is end-to-end at Layer 3; MACsec is hop-by-hop at Layer 2 — they are complementary, not equivalent.
- D: MACsec is supported on Cisco Catalyst switches, ISR/ASR routers, and is well-suited to campus switch-to-switch uplinks.

---

### Question 15 (Multiple Choice — 5 pts)
An SNMPv3 configuration uses `authNoPriv` security level. A junior engineer argues that this provides complete security because all SNMP messages are authenticated. What critical security gap does this configuration leave?

- A) `authNoPriv` does not authenticate the SNMP manager — any device can send SNMP requests. ❌
- B) `authNoPriv` authenticates messages (preventing tampering) but does not encrypt the SNMP payload — SNMP GET responses containing sensitive configuration data are transmitted in plaintext and can be captured by a network eavesdropper. ✅
- C) `authNoPriv` is not supported on Cisco IOS devices; only `noAuthNoPriv` and `authPriv` are valid. ❌
- D) `authNoPriv` does not support SHA authentication — only MD5. ❌

**Answer:** B — SNMPv3 has three security levels: `noAuthNoPriv` (no authentication, no encryption), `authNoPriv` (HMAC authentication but no encryption), and `authPriv` (authentication + AES/DES encryption). With `authNoPriv`, the SNMP payload — including GET responses that may contain interface configurations, routing tables, and community strings — is sent in cleartext. An attacker passively capturing traffic on the management VLAN could read all SNMP data. For a production network, `authPriv` with AES-128 or AES-256 is the only acceptable SNMPv3 configuration.

**Distractor Analysis:**
- A: Authentication (HMAC-SHA or HMAC-MD5) does verify the identity of the SNMP manager — this is not the gap.
- C: All three SNMPv3 security levels are supported on Cisco IOS.
- D: Cisco IOS supports both SHA and MD5 for SNMPv3 authentication; SHA is strongly preferred.

---

### Question 16 (Scenario — 5 pts)
A router's running configuration shows:
```
ip access-list extended MGMT-ACL
 10 permit tcp host 10.99.99.100 any eq 22
 20 deny ip any any log

line vty 0 15
 access-class MGMT-ACL in
 transport input ssh
```
A network administrator at 10.99.99.200 attempts to SSH to the router and is denied. What is the single most specific cause and fix?

- A) The ACL is applied in the wrong direction — `in` should be `out`. ❌
- B) `transport input ssh` and an ACL cannot coexist on the same VTY line. ❌
- C) The administrator's source IP (10.99.99.200) does not match the `host 10.99.99.100` permit statement in MGMT-ACL — only .100 is permitted. Add a permit statement for the administrator's IP or use `permit tcp 10.99.99.0 0.0.0.255 any eq 22`. ✅
- D) SSH on the VTY requires `login authentication default` — without it, the ACL is not enforced. ❌

**Answer:** C — The `host` keyword in the ACL matches only the single IP address 10.99.99.100 for SSH access. The administrator at 10.99.99.200 hits the implicit deny at line 20 and is blocked. The fix is to broaden the permit to the entire management subnet (`permit tcp 10.99.99.0 0.0.0.255 any eq 22`) or add a specific entry for .200. This is a common production issue when management access lists are too narrow — always document and plan for multiple admin workstations.

**Distractor Analysis:**
- A: `in` on `access-class` is correct — it filters inbound connection attempts to the VTY.
- B: `transport input ssh` and `access-class` are designed to work together; this is a standard hardening configuration.
- D: `login authentication default` controls the authentication method; the ACL is enforced regardless.

---

### Question 17 (Multiple Choice — 5 pts)
Which command verifies that BGP MD5 authentication is active and functioning between two BGP peers, and what output field specifically confirms the MD5 session is authenticated?

- A) `show ip bgp summary` — the "State/PfxRcd" column shows "MD5" when authenticated. ❌
- B) `show ip bgp neighbors [peer-IP]` — the output includes "BGP neighbor is ... Options: (V4 Capability, Route refresh Capability, **Established**, **MD5 Message Digests**)" and shows the session state as Established. ✅
- C) `show ip route bgp` — the routing table flags indicate MD5-authenticated routes with a special marker. ❌
- D) `debug ip bgp [peer-IP] events` — the debug output logs each MD5 hash exchange. ❌

**Answer:** B — `show ip bgp neighbors [peer-IP]` displays the full neighbor session details, including "MD5 Message Digests" in the Options field and "External BGP neighbor configured for session open authentication" when MD5 is active. If the session is in Established state with MD5 listed, authentication is working. If the password is mismatched, the session will be in Idle/Active state with TCP connection failures, and `debug ip bgp` would show "MD5 digest is wrong."

**Distractor Analysis:**
- A: `show ip bgp summary` does not show authentication details — only prefix counts and session state.
- C: Routing table entries carry no authentication metadata.
- D: Debug commands are correct for diagnosing failures, but `show ip bgp neighbors` is the standard verification command.

---

### Question 18 (Multiple Choice — 5 pts)
An enterprise security team requires that all SNMP polling use authentication and encryption, and that only the network management system at 10.50.50.10 is permitted to query devices. Which SNMPv3 configuration elements correctly enforce both requirements simultaneously?

- A) Configure a community string with `snmp-server community SECURE_STRING RO` and apply an ACL to permit only 10.50.50.10. ❌
- B) Configure SNMPv3 with `authPriv` security level, assign the NMS user to a group with read access to a defined view, and apply an ACL to the SNMP group or community restricting access to 10.50.50.10. ✅
- C) Configure SNMPv3 `noAuthNoPriv` and rely on the management VLAN firewall for IP restriction. ❌
- D) Configure SNMPv3 `authNoPriv` with SHA and an ACL — this provides both authentication and source IP restriction simultaneously. ❌

**Answer:** B — SNMPv3 `authPriv` satisfies the encryption requirement; the access restriction to the NMS IP (10.50.50.10) is enforced via an ACL associated with the SNMP group. The complete configuration involves: `snmp-server group MGMT_GROUP v3 priv access NMS-ACL`, `snmp-server user netadmin MGMT_GROUP v3 auth sha [authpass] priv aes 128 [privpass]`, and an ACL `NMS-ACL` permitting only 10.50.50.10. This is the gold standard for SNMP security on enterprise infrastructure.

**Distractor Analysis:**
- A: SNMPv2c community strings provide no encryption and are transmitted in plaintext — this does not meet "encryption" requirement.
- C: `noAuthNoPriv` provides neither authentication nor encryption — relying on VLAN firewalls alone is defense-in-depth failure.
- D: `authNoPriv` satisfies authentication but not encryption — SNMP GET responses would still be readable in plaintext.

---

### Question 19 (Short Answer — 5 pts)
Explain the concept of a **BGP prefix filter** using a prefix-list and describe a specific scenario where failing to implement one could cause a serious outage. Include the IOS commands to configure and apply a basic inbound prefix filter. (3–4 sentences)

**Model Answer:** A BGP prefix filter uses an `ip prefix-list` to explicitly permit or deny specific network prefixes received from (or sent to) a BGP peer — it controls which routes enter or leave the BGP table. Without an inbound prefix filter, a BGP peer can advertise any number of prefixes including bogon addresses (RFC 1918 space, 0.0.0.0/0, or full default routes), which could override legitimate routes and blackhole traffic — a scenario called **BGP route hijacking** that has caused real-world internet outages. For example, if an ISP peer accidentally advertises 0.0.0.0/0 to your router without a filter, your router installs it as the default route, potentially routing all traffic toward that peer instead of your legitimate default gateway. The configuration is: `ip prefix-list INBOUND-FILTER seq 10 permit 203.0.113.0/24` (allowing only expected prefixes), then `router bgp 65000` → `neighbor 1.2.3.4 prefix-list INBOUND-FILTER in`.

---

### Question 20 (Short Answer — 5 pts)
Describe the **management plane hardening** practice of restricting VTY access using an ACL combined with `transport input ssh`, and explain why using Telnet for device management is a critical security risk even on a private management VLAN. (2–3 sentences)

**Model Answer:** Applying `access-class [ACL] in` on VTY lines restricts SSH access to only the IP addresses defined in the ACL (typically the management VLAN or a dedicated jump host), combined with `transport input ssh` which blocks Telnet entirely so only SSH connections are accepted regardless of ACL entries. Telnet transmits all data — including usernames, passwords, and every command typed — in cleartext over the network, meaning anyone with access to a network tap, mirror port, or compromised switch on the management VLAN can capture administrator credentials in real time with tools like Wireshark. Even on a private management VLAN, insider threats, compromised infrastructure, or a misconfigured SPAN session could expose those credentials — SSH with RSA-2048 or higher keys eliminates this risk by encrypting the entire management session.
