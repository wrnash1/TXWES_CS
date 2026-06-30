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
