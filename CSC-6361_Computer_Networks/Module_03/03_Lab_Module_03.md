# Lab Assignment: Module 03 – WAN Technologies: GRE over IPsec with OSPF
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, November 8, 2026 at 11:59 PM CST

---

## Lab Overview
**Estimated Time:** 3–4 hours
**Tools Required:** Cisco Packet Tracer (free)
**Deliverables:** (1) Completed `.pkt` file, (2) Professional Lab Report (PDF)

This lab simulates a multi-site enterprise WAN. You will configure GRE tunnels between three sites, encrypt them with IPsec, and run OSPF across the tunnels so all sites share routing information. This mirrors a real-world hub-and-spoke VPN design over the public internet.

---

## Lab Topology

```
                     [ISP CLOUD]
                    /            \
           [HQ-R] ── Internet ── [BRANCH-A-R]
                \
                 \── Internet ── [BRANCH-B-R]

Subnets:
  HQ LAN:       192.168.10.0/24
  Branch-A LAN: 192.168.20.0/24
  Branch-B LAN: 192.168.30.0/24
  ISP Links:    10.0.0.0/30 (HQ to ISP), 10.0.1.0/30 (A to ISP), 10.0.2.0/30 (B to ISP)
  GRE Tunnel 0 (HQ↔A): 172.16.1.0/30
  GRE Tunnel 1 (HQ↔B): 172.16.2.0/30
```

**Device Assignments:**
| Device | WAN IP (toward ISP) | LAN Interface | LAN Subnet |
|---|---|---|---|
| HQ-R | 10.0.0.1/30 | Gi0/1 | 192.168.10.1/24 |
| ISP-R | 10.0.0.2/30 (to HQ), 10.0.1.2/30 (to A), 10.0.2.2/30 (to B) | N/A | N/A |
| BRANCH-A-R | 10.0.1.1/30 | Gi0/1 | 192.168.20.1/24 |
| BRANCH-B-R | 10.0.2.1/30 | Gi0/1 | 192.168.30.1/24 |
| PC-HQ | — | 192.168.10.10/24, GW: 192.168.10.1 | |
| PC-A | — | 192.168.20.10/24, GW: 192.168.20.1 | |
| PC-B | — | 192.168.30.10/24, GW: 192.168.30.1 | |

---

## Lab Instructions

### Part 1: Build the Physical Topology & Configure IP Addressing (10 pts)
1. Place 4 routers (HQ-R, ISP-R, BRANCH-A-R, BRANCH-B-R) and 3 PCs in Packet Tracer.
2. Connect routers per the topology and assign IP addresses to all physical interfaces.
3. On ISP-R, configure static routes (or a simple routing protocol) so the three routers can ping each other's WAN interfaces. Verify with ping before proceeding.

**Screenshot Checkpoint 1:** `show ip interface brief` on HQ-R. Ping from HQ-R (10.0.0.1) to Branch-A (10.0.1.1) and Branch-B (10.0.2.1) — all must succeed.

### Part 2: Configure GRE Tunnels (20 pts)
Create GRE tunnel interfaces between HQ and each branch.

**On HQ-R:**
```
interface Tunnel0
 ip address 172.16.1.1 255.255.255.252
 tunnel source GigabitEthernet0/0
 tunnel destination 10.0.1.1
 ip mtu 1400
 ip tcp adjust-mss 1360

interface Tunnel1
 ip address 172.16.2.1 255.255.255.252
 tunnel source GigabitEthernet0/0
 tunnel destination 10.0.2.1
 ip mtu 1400
 ip tcp adjust-mss 1360
```

**On BRANCH-A-R:**
```
interface Tunnel0
 ip address 172.16.1.2 255.255.255.252
 tunnel source GigabitEthernet0/0
 tunnel destination 10.0.0.1
 ip mtu 1400
 ip tcp adjust-mss 1360
```

**On BRANCH-B-R:**
```
interface Tunnel1
 ip address 172.16.2.2 255.255.255.252
 tunnel source GigabitEthernet0/0
 tunnel destination 10.0.0.1
 ip mtu 1400
 ip tcp adjust-mss 1360
```

**Screenshot Checkpoint 2:** `show interface Tunnel0` on HQ-R (Line protocol should be up). Ping from HQ-R (172.16.1.1) to Branch-A tunnel IP (172.16.1.2) — must succeed.

### Part 3: Configure IPsec Encryption on the GRE Tunnels (30 pts)
Configure IPsec to encrypt all GRE tunnel traffic. Use IKEv1 (ISAKMP) since Packet Tracer has limited IKEv2 support.

**On HQ-R and BRANCH-A-R (mirror config):**
```
! Phase 1 — ISAKMP Policy
crypto isakmp policy 10
 encryption aes 256
 hash sha256
 authentication pre-share
 group 14
 lifetime 86400

! Pre-shared key
crypto isakmp key VPNkey1234 address 10.0.1.1   ! (On HQ-R, pointing to Branch-A)

! Phase 2 — Transform Set
crypto ipsec transform-set GRE-TS esp-aes 256 esp-sha256-hmac
 mode transport

! Crypto Map — apply to protect GRE traffic between tunnel endpoints
crypto map VPN-MAP 10 ipsec-isakmp
 set peer 10.0.1.1
 set transform-set GRE-TS
 match address GRE-ACL

! Access list matching GRE traffic (protocol 47 = GRE)
ip access-list extended GRE-ACL
 permit gre host 10.0.0.1 host 10.0.1.1

! Apply crypto map to WAN interface
interface GigabitEthernet0/0
 crypto map VPN-MAP
```

Repeat for HQ-R ↔ BRANCH-B-R with the corresponding peer addresses.

**Screenshot Checkpoint 3:** After triggering traffic over the tunnel: `show crypto isakmp sa` — verify a ISAKMP SA is established (QM_IDLE state). `show crypto ipsec sa` — verify encrypt/decrypt packet counters are incrementing.

### Part 4: Run OSPF Across the GRE Tunnels (25 pts)
Configure OSPF to run over the GRE tunnel interfaces so all three sites learn each other's LAN routes.

**On HQ-R:**
```
router ospf 1
 router-id 1.1.1.1
 network 192.168.10.0 0.0.0.255 area 0
 network 172.16.1.0 0.0.0.3 area 0
 network 172.16.2.0 0.0.0.3 area 0
 passive-interface GigabitEthernet0/0
 passive-interface GigabitEthernet0/1
```

**On BRANCH-A-R:**
```
router ospf 1
 router-id 2.2.2.2
 network 192.168.20.0 0.0.0.255 area 0
 network 172.16.1.0 0.0.0.3 area 0
 passive-interface GigabitEthernet0/0
 passive-interface GigabitEthernet0/1
```

Repeat on BRANCH-B-R with router-id 3.3.3.3 and network 192.168.30.0.

**Screenshot Checkpoint 4:** `show ip ospf neighbor` on HQ-R (should show 2 OSPF neighbors via tunnels). `show ip route ospf` on HQ-R (should show 192.168.20.0 and 192.168.30.0 as OSPF routes).

### Part 5: End-to-End Verification (15 pts)
1. Ping from PC-HQ (192.168.10.10) to PC-A (192.168.20.10) and PC-B (192.168.30.10). All must succeed.
2. `show crypto ipsec sa` on HQ-R — verify encrypted packet counts increased after the pings.
3. Traceroute from PC-HQ to PC-A — the path should go through the tunnel (note: ISP-R should NOT appear in the traceroute since GRE encapsulates the packet).

---

## Lab Report Requirements
1. **Topology Diagram** — annotated Packet Tracer screenshot.
2. **All 4 Screenshot Checkpoints** — labeled and annotated.
3. **Key Configurations** — full running config for HQ-R.
4. **Analysis Section (2–3 paragraphs):**
   - Explain why `ip mtu 1400` and `ip tcp adjust-mss 1360` are configured on the tunnel interfaces. What happens without them?
   - Explain why IPsec `mode transport` (not `mode tunnel`) is used when encrypting GRE tunnels. What is the difference in how the packet is encapsulated?
   - Describe one scenario where this hub-and-spoke GRE/IPsec design would be inadequate and a full-mesh design would be preferable.
5. **Troubleshooting Log:** Document one issue encountered and resolution.

---

## Grading Rubric
| Component | Points |
|---|---|
| Physical Topology & IP Addressing (Part 1) | 10 |
| GRE Tunnel Configuration (Part 2) | 20 |
| IPsec Encryption (Part 3) | 30 |
| OSPF over GRE (Part 4) | 25 |
| End-to-End Verification (Part 5) | 15 |
| **Total** | **100** |
