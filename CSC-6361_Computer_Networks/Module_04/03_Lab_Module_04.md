# Lab Assignment: Module 04 – Enterprise Security & Infrastructure Hardening
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, November 15, 2026 at 11:59 PM CST

---

## Lab Overview
**Estimated Time:** 3–4 hours
**Tools Required:** Cisco Packet Tracer (free)
**Deliverables:** (1) Completed `.pkt` file, (2) Professional Lab Report (PDF)

This lab implements a comprehensive security hardening baseline on a campus network including AAA, named extended ACLs, DHCP Snooping, Dynamic ARP Inspection, Port Security, and SSH-only management access.

---

## Lab Topology

```
[MGMT Admin PC] ──── [L3-Core-SW] ────── [L2-Access-SW] ──── [PC-Employee]
                          |                     |
                    [Router-GW]           [PC-Attacker]
                          |
                     [ISP/Internet]
```

**Devices:**
| Device | Type | IP Address | Role |
|---|---|---|---|
| L3-Core-SW | Multilayer Switch (3650) | VLAN10 SVI: 10.10.10.1/24, VLAN99: 10.99.99.1/24 | Core switch with ACLs and routing |
| L2-Access-SW | Switch (2960) | VLAN99 (Mgmt): 10.99.99.10/24 | Access switch with L2 security |
| Router-GW | Router | Gi0/0: 10.10.10.2/24, Gi0/1: 203.0.113.1/30 | Gateway/DHCP server |
| PC-Employee | PC | DHCP from Router-GW (VLAN10) | Legitimate user |
| PC-Attacker | PC | Manually set — simulate attacker | Attack testing |
| MGMT Admin PC | PC | 10.99.99.100/24 | Administrative management |

---

## Lab Instructions

### Part 1: Baseline Configuration & AAA (15 pts)
1. Build the physical topology in Packet Tracer and configure all IP addresses.
2. On L3-Core-SW and Router-GW, configure local AAA authentication (since Packet Tracer does not support external TACACS+ server):
```
! On Router-GW and L3-Core-SW:
username admin privilege 15 secret Admin@Secure1
username readonly privilege 1 secret ReadOnly@1

aaa new-model
aaa authentication login default local
aaa authorization exec default local

line vty 0 15
 login authentication default
 transport input ssh
 exec-timeout 10 0

ip ssh version 2
crypto key generate rsa modulus 2048
```
3. Verify: SSH from Admin PC to Router-GW using `admin` credentials. Must succeed. Attempt SSH with wrong password — must fail.

**Screenshot Checkpoint 1:** `show aaa sessions` on Router-GW. Successful SSH session shown.

### Part 2: Named Extended ACL for Traffic Filtering (20 pts)
On Router-GW, create a named extended ACL that:
- Permits SSH from the management VLAN (10.99.99.0/24) to router interfaces only.
- Permits ICMP from the internal 10.10.10.0/24 network to any destination.
- Permits HTTP (80) and HTTPS (443) from internal network to internet.
- Permits established TCP return traffic.
- Denies and logs everything else.

```
ip access-list extended INTERNAL-OUT
 permit tcp 10.99.99.0 0.0.0.255 host 10.10.10.2 eq 22
 permit tcp 10.99.99.0 0.0.0.255 host 203.0.113.1 eq 22
 permit icmp 10.10.10.0 0.0.0.255 any
 permit tcp 10.10.10.0 0.0.0.255 any eq 80
 permit tcp 10.10.10.0 0.0.0.255 any eq 443
 permit tcp any 10.10.10.0 0.0.0.255 established
 deny ip any any log

interface GigabitEthernet0/0
 ip access-group INTERNAL-OUT in
```

**Screenshot Checkpoint 2:** `show ip access-lists INTERNAL-OUT` — show hit counters after sending permitted traffic and one denied packet. Denied traffic must show a log entry.

### Part 3: DHCP Snooping on the Access Switch (20 pts)
Configure DHCP Snooping on L2-Access-SW:
```
ip dhcp snooping
ip dhcp snooping vlan 10

! Trust only the uplink to the L3-Core-SW (which relays to Router-GW DHCP)
interface GigabitEthernet0/1
 ip dhcp snooping trust

! Untrusted access ports — rate limit DHCP
interface range FastEthernet0/1-10
 ip dhcp snooping limit rate 15
```

**Attack Test:** Connect PC-Attacker to an access port. Configure it as a "DHCP server" (in Packet Tracer, manually configure it with a static IP that conflicts with the DHCP scope). Attempt to send a DHCP Offer from PC-Attacker's port — DHCP Snooping should drop it.

**Screenshot Checkpoint 3:** `show ip dhcp snooping statistics` — show forwarded and dropped DHCP packet counts. The DHCP Offer from the attacker port must appear in the dropped counter.

### Part 4: Dynamic ARP Inspection (20 pts)
Enable DAI on L2-Access-SW (requires DHCP Snooping binding table to be populated):
```
ip arp inspection vlan 10

interface GigabitEthernet0/1
 ip arp inspection trust
```

**Attack Test:** On PC-Attacker, manually configure a static ARP entry claiming the gateway's IP (10.10.10.1) belongs to the attacker's MAC address. The attacker's port is untrusted. Send a gratuitous ARP from PC-Attacker. DAI must drop it.

**Screenshot Checkpoint 4:** `show ip arp inspection vlan 10` — verify forwarded and dropped ARP packet statistics. `show ip dhcp snooping binding` — verify PC-Employee has a valid binding.

### Part 5: Port Security (15 pts)
On L2-Access-SW, configure Port Security on the PC-Employee and PC-Attacker ports:
```
interface FastEthernet0/1   ! PC-Employee
 switchport mode access
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation restrict

interface FastEthernet0/2   ! PC-Attacker port
 switchport mode access
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation restrict
```

**Attack Test:** Disconnect PC-Attacker and connect a second PC to the same port. Port Security should detect the new MAC address as a violation.

**Screenshot Checkpoint 5:** `show port-security interface FastEthernet0/2` — show violation count incremented. Port must not be in err-disabled state (restrict mode).

### Part 6: Management Plane Hardening Verification (10 pts)
1. Confirm SSH is the only remote access method: `show line vty 0 15` — input transport should show only SSH.
2. Attempt Telnet to Router-GW from Admin PC — must fail.
3. Confirm banner is displayed on SSH login attempt.
4. `show ip ssh` — verify SSH version 2, RSA key generated.

---

## Lab Report Requirements
1. **Topology Diagram** — annotated screenshot.
2. **All 5 Screenshot Checkpoints** — labeled and annotated.
3. **Key Configurations** — full running config of L2-Access-SW.
4. **Analysis Section (2–3 paragraphs):**
   - Explain why the local AAA fallback (`aaa authentication login default local`) is critical in production and what would happen without it.
   - DHCP Snooping drops Offer/ACK on untrusted ports. Why is this the correct behavior, and what would happen to a legitimate DHCP server connected to an access port without proper trust configuration?
   - Port Security with `restrict` mode logs violations but does not shut down the port. In what scenario would you choose `shutdown` mode instead?
5. **Troubleshooting Log** — one issue encountered and resolved.

---

## Grading Rubric
| Component | Points |
|---|---|
| AAA Configuration (Part 1) | 15 |
| Named Extended ACL (Part 2) | 20 |
| DHCP Snooping (Part 3) | 20 |
| Dynamic ARP Inspection (Part 4) | 20 |
| Port Security (Part 5) | 15 |
| Management Plane Verification (Part 6) | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Reflexive ACL for Stateful Filtering
1. On your lab router, create a named extended ACL called `OUTBOUND_TRAFFIC` that permits TCP and UDP traffic from the internal LAN (192.168.1.0/24) outbound, and uses the `reflect INTERNAL_SESSIONS` keyword to create a dynamic reflexive ACL.
2. Create a second ACL called `INBOUND_TRAFFIC` that evaluates the reflexive ACL using `evaluate INTERNAL_SESSIONS` and denies everything else.
3. Apply `OUTBOUND_TRAFFIC` outbound on the WAN interface and `INBOUND_TRAFFIC` inbound on the WAN interface.
4. Test by initiating a TCP session from the LAN side and verifying the return traffic is permitted, then attempt an unsolicited inbound connection and verify it is dropped.

### Challenge 2: SNMPv3 with AuthPriv Security Level
1. Configure SNMPv3 on your router with a user named `netadmin`, using SHA authentication (password: `Auth@12345`) and AES-128 encryption (password: `Priv@12345`).
2. Configure a view named `MGMT_VIEW` that includes the entire MIB tree (`1.3.6.1`).
3. Associate the user with an SNMPv3 group named `MGMT_GROUP` using `priv` (AuthPriv) security level.
4. From a management station, use an SNMPv3-capable tool (or `snmpwalk -v3`) to retrieve system information and verify the encrypted communication.

### Reflection Questions
1. You are asked to choose between TACACS+ and RADIUS for authenticating network administrators who need per-command authorization on Cisco routers. Which protocol do you choose and why? What specific feature makes your choice clearly superior for this use case?
2. A colleague argues that CoPP is unnecessary overhead on a well-secured internal network. Construct a specific attack scenario that demonstrates why CoPP is valuable even on a network with strong perimeter security.
