# Lab Assignment: Module 06 – Cloud Networking & Hybrid Architectures

## CSC-6361 Advanced Computer Networks | Graduate Level

## Due: Tuesday, December 1, 2026 at 11:59 PM CST (Extended — Thanksgiving Week)

---

## Lab Overview

**Estimated Time:** 3–4 hours
**Tools Required:** Cisco Packet Tracer (free — download at netacad.com)
**Deliverables:** (1) Completed `.pkt` Packet Tracer file, (2) Professional Lab Report (PDF)

This lab simulates a Cisco SD-WAN hybrid WAN environment using IOS router features available in Packet Tracer. Because Packet Tracer does not natively support Viptela SD-WAN software, we use **GRE tunnels as the data-plane analog** for SD-WAN overlay tunnels, **BGP as the overlay routing protocol analog for OMP**, and **route-maps as the policy analog for SD-WAN centralized data policy**. This simulation approach is explicitly aligned with the CCNP ENCOR lab methodology for environments without SD-WAN controller access.

By completing this lab you will demonstrate mastery of:

- WAN underlay/overlay separation (the core SD-WAN architectural concept).
- GRE tunnel configuration as an overlay transport.
- BGP session establishment and prefix advertisement over an overlay.
- Route-map based policy — simulating SD-WAN path preference (primary WAN vs. backup WAN).
- Verification of overlay routing and failover behavior.

---

## Lab Topology

```text
                    [INTERNET CLOUD / WAN UNDERLAY]
                   /                              \
    10.0.12.0/30  /                                \ 10.0.23.0/30
                 /                                  \
[vEdge-HQ] ----+---- 10.0.13.0/30 ----------------[vEdge-Branch2]
 R1              \                                /  R3
 Lo0:1.1.1.1      \                              /
                [vEdge-Branch1]
                 R2
                 Lo0: 2.2.2.2

LAN SEGMENTS:
  vEdge-HQ:       192.168.10.0/24  (Gi0/0 toward LAN)
  vEdge-Branch1:  192.168.20.0/24  (Gi0/0 toward LAN)
  vEdge-Branch2:  192.168.30.0/24  (Gi0/0 toward LAN)

OVERLAY TUNNELS (GRE — simulating SD-WAN IPsec tunnels):
  Tunnel10: HQ ↔ Branch1  (primary path)
  Tunnel20: HQ ↔ Branch2  (primary path)
  Tunnel30: Branch1 ↔ Branch2 (secondary/backup path)
```

---

## Addressing Table

| Device | Interface | IP Address | Description |
|---|---|---|---|
| vEdge-HQ (R1) | Gi0/0 | 192.168.10.1/24 | HQ LAN gateway |
| vEdge-HQ (R1) | Gi0/1 | 10.0.12.1/30 | WAN underlay to Branch1 |
| vEdge-HQ (R1) | Gi0/2 | 10.0.13.1/30 | WAN underlay to Branch2 |
| vEdge-HQ (R1) | Lo0 | 1.1.1.1/32 | System IP (router-ID) |
| vEdge-HQ (R1) | Tunnel10 | 172.16.10.1/30 | GRE overlay to Branch1 |
| vEdge-HQ (R1) | Tunnel20 | 172.16.20.1/30 | GRE overlay to Branch2 |
| vEdge-Branch1 (R2) | Gi0/0 | 192.168.20.1/24 | Branch1 LAN gateway |
| vEdge-Branch1 (R2) | Gi0/1 | 10.0.12.2/30 | WAN underlay to HQ |
| vEdge-Branch1 (R2) | Gi0/2 | 10.0.23.1/30 | WAN underlay to Branch2 |
| vEdge-Branch1 (R2) | Lo0 | 2.2.2.2/32 | System IP (router-ID) |
| vEdge-Branch1 (R2) | Tunnel10 | 172.16.10.2/30 | GRE overlay to HQ |
| vEdge-Branch1 (R2) | Tunnel30 | 172.16.30.1/30 | GRE overlay to Branch2 |
| vEdge-Branch2 (R3) | Gi0/0 | 192.168.30.1/24 | Branch2 LAN gateway |
| vEdge-Branch2 (R3) | Gi0/1 | 10.0.13.2/30 | WAN underlay to HQ |
| vEdge-Branch2 (R3) | Gi0/2 | 10.0.23.2/30 | WAN underlay to Branch1 |
| vEdge-Branch2 (R3) | Lo0 | 3.3.3.3/32 | System IP (router-ID) |
| vEdge-Branch2 (R3) | Tunnel20 | 172.16.20.2/30 | GRE overlay to HQ |
| vEdge-Branch2 (R3) | Tunnel30 | 172.16.30.2/30 | GRE overlay to Branch1 |

---

## Lab Instructions

### Part 1: Build the Topology and Configure the WAN Underlay (20 pts)

The underlay represents the physical WAN transport layer — in real SD-WAN this is the ISP circuits (MPLS, internet, LTE). Here, we use OSPF on the physical interfaces to simulate underlay reachability.

**Step 1:** Open Cisco Packet Tracer. Place 3 routers (use Cisco 4321 or equivalent). Label them vEdge-HQ, vEdge-Branch1, vEdge-Branch2.

**Step 2:** Connect routers with straight-through Ethernet cables per the topology diagram. Assign all physical interface IP addresses from the addressing table.

**Step 3:** Configure OSPF Process 10 on all underlay interfaces (Gi0/1, Gi0/2, and Lo0 on each router). Use Area 0 for all underlay interfaces. This is the "underlay routing protocol."

```cisco
! vEdge-HQ (R1) — underlay OSPF
router ospf 10
 router-id 1.1.1.1
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.13.0 0.0.0.3 area 0
 network 1.1.1.1 0.0.0.0 area 0
 passive-interface GigabitEthernet0/0
```

Apply equivalent configuration on Branch1 and Branch2 for their underlay interfaces and loopbacks.

**Screenshot Checkpoint 1:** Run `show ip ospf neighbor` on all three routers. Verify two OSPF neighbors appear on vEdge-HQ. Run `show ip route ospf` on vEdge-HQ — verify it sees 2.2.2.2/32 and 3.3.3.3/32 (branch loopbacks) via OSPF. These routes represent "underlay reachability" — the foundation that will carry GRE tunnel traffic.

---

### Part 2: Build the GRE Overlay Tunnels — Simulating SD-WAN IPsec Data Plane (25 pts)

In SD-WAN, vEdge devices build IPsec tunnels directly between each other once OMP has distributed TLOC information. Here, GRE tunnels simulate those data-plane tunnels. The tunnel source is the local loopback (analogous to the VTEP IP / system-IP in SD-WAN). The tunnel destination is the remote router's loopback.

**Step 1:** Configure Tunnel10 on vEdge-HQ and vEdge-Branch1:

```cisco
! vEdge-HQ (R1) — Tunnel10 to Branch1
interface Tunnel10
 description SD-WAN-ANALOG HQ-to-Branch1
 ip address 172.16.10.1 255.255.255.252
 tunnel source Loopback0
 tunnel destination 2.2.2.2
 no shutdown

! vEdge-Branch1 (R2) — Tunnel10 to HQ
interface Tunnel10
 description SD-WAN-ANALOG Branch1-to-HQ
 ip address 172.16.10.2 255.255.255.252
 tunnel source Loopback0
 tunnel destination 1.1.1.1
 no shutdown
```

**Step 2:** Configure Tunnel20 between vEdge-HQ and vEdge-Branch2 following the same pattern (source: Lo0, destination: remote Lo0, address from table).

**Step 3:** Configure Tunnel30 between vEdge-Branch1 and vEdge-Branch2 (the backup direct path between branches).

**Step 4:** Verify GRE tunnel interfaces are up/up using `show interfaces tunnel10` on each router. Verify cross-tunnel pings succeed: from vEdge-HQ, ping 172.16.10.2 (Branch1 tunnel endpoint). A successful ping confirms the GRE overlay is functioning over the OSPF underlay.

**Screenshot Checkpoint 2:** `show interfaces tunnel10` on vEdge-HQ — confirm Line protocol is up. `show interfaces tunnel20` on vEdge-HQ — confirm up. Ping from vEdge-HQ to 172.16.10.2 and 172.16.20.2 — both must succeed.

---

### Part 3: Configure BGP on the Overlay — Simulating OMP (25 pts)

In SD-WAN, OMP distributes site prefixes (LAN subnets) via vSmart to all vEdge devices. Here, BGP running over the GRE overlay tunnels simulates this prefix distribution. The LAN subnets (192.168.x.0/24) are the "OMP vRoutes."

Use BGP AS 65000 for all three routers (iBGP). The BGP router-ID for each router is its loopback IP.

**Step 1:** Configure BGP on vEdge-HQ:

```cisco
! vEdge-HQ (R1) — BGP overlay (simulating OMP)
router bgp 65000
 bgp router-id 1.1.1.1
 bgp log-neighbor-changes
 neighbor 172.16.10.2 remote-as 65000
 neighbor 172.16.10.2 description Branch1-overlay-peer
 neighbor 172.16.10.2 update-source Loopback0
 neighbor 172.16.20.2 remote-as 65000
 neighbor 172.16.20.2 description Branch2-overlay-peer
 neighbor 172.16.20.2 update-source Loopback0
 !
 address-family ipv4
  network 192.168.10.0 mask 255.255.255.0
  neighbor 172.16.10.2 activate
  neighbor 172.16.20.2 activate
 exit-address-family
```

**Step 2:** Configure BGP on vEdge-Branch1 (R2). Peers: 172.16.10.1 (HQ) and 172.16.30.2 (Branch2). Advertise network 192.168.20.0/24.

**Step 3:** Configure BGP on vEdge-Branch2 (R3). Peers: 172.16.20.1 (HQ) and 172.16.30.1 (Branch1). Advertise network 192.168.30.0/24.

**Screenshot Checkpoint 3:** `show ip bgp summary` on vEdge-HQ — verify both BGP neighbors are in `Established` state with `Up/Down` showing a non-zero uptime. `show ip bgp` on vEdge-Branch1 — verify 192.168.10.0/24 (HQ LAN) and 192.168.30.0/24 (Branch2 LAN) are present in the BGP table.

---

### Part 4: Apply Route-Map Policy — Simulating SD-WAN Path Preference (20 pts)

In SD-WAN, a centralized data policy sets preferred TLOCs for specific traffic. Here, a route-map on vEdge-Branch1 simulates this: LAN traffic to HQ (192.168.10.0/24) should prefer the direct HQ tunnel (Tunnel10), with Branch2 as a fallback via Tunnel30.

**Step 1:** On vEdge-Branch1 (R2), create a route-map that sets LOCAL_PREF 200 for routes received from HQ (172.16.10.1 — the direct path), and LOCAL_PREF 100 for routes received from Branch2 (172.16.30.2 — the indirect path):

```cisco
! vEdge-Branch1 (R2) — policy simulating SD-WAN path preference
route-map PREFER-DIRECT permit 10
 set local-preference 200

route-map PREFER-BACKUP permit 10
 set local-preference 100

router bgp 65000
 address-family ipv4
  neighbor 172.16.10.1 route-map PREFER-DIRECT in
  neighbor 172.16.30.2 route-map PREFER-BACKUP in
 exit-address-family
```

**Step 2:** Verify that `show ip bgp 192.168.10.0` on Branch1 shows the path via 172.16.10.1 (direct HQ tunnel) with LOCAL_PREF 200 as the best path (marked with `>`), and the path via 172.16.30.2 (Branch2 relay) with LOCAL_PREF 100 as a valid but non-best path.

**Step 3:** Simulate a path failure. Shut down Tunnel10 on vEdge-Branch1:

```cisco
! vEdge-Branch1 — simulate primary path failure
interface Tunnel10
 shutdown
```

Wait 30 seconds for BGP reconvergence. Verify that `show ip bgp 192.168.10.0` now shows the Branch2 relay path (172.16.30.2) as the new best path. Verify connectivity: ping from vEdge-Branch1 to 192.168.10.1 (HQ LAN) via the backup path.

**Screenshot Checkpoint 4:** `show ip bgp 192.168.10.0` before and after Tunnel10 shutdown — show the path preference shift. `show ip route bgp` before and after — confirm routing table update. Ping from Branch1 to 192.168.10.1 after Tunnel10 shutdown — must succeed (proving backup path works).

**Step 4:** Bring Tunnel10 back up (`no shutdown`) and verify traffic reverts to the preferred direct path.

---

## Lab Report Requirements (Graduate Standard)

Your PDF lab report must include:

1. **Topology Diagram** — a clean, labeled screenshot of your Packet Tracer topology with all router names, interface labels, and IP addresses visible.
2. **All 4 Screenshot Checkpoints** — annotated (label what each screenshot demonstrates).
3. **Configuration Listings** — the full running configuration for vEdge-HQ (R1) and vEdge-Branch1 (R2).
4. **Analysis Section (Required — 2–3 paragraphs):**
   - Explain the underlay/overlay separation principle you implemented. Why does the overlay (BGP over GRE) not need to know about the underlay topology (OSPF) — and how does this map to the SD-WAN vEdge/OMP relationship?
   - Explain what happened during the Tunnel10 failure scenario. How does BGP local preference simulate SD-WAN data policy path preference? What is the key limitation of this simulation compared to real SD-WAN BFD-based failover?
   - Describe how you would extend this lab topology to simulate an SD-WAN policy that routes video conferencing traffic (DSCP EF) over the direct HQ path only — what additional IOS features would you use, and how do they map to SD-WAN centralized data policy?
5. **Troubleshooting Log** — a brief log of at least one issue you encountered (or deliberately introduced) and how you resolved it.

---

## Grading Rubric

| Component | Points |
|---|---|
| Topology Build + Underlay OSPF (Part 1) | 20 |
| GRE Overlay Tunnels (Part 2) | 25 |
| BGP Overlay Routing — OMP Analog (Part 3) | 25 |
| Route-Map Policy — Path Preference + Failover (Part 4) | 20 |
| Lab Report Analysis (Graduate Standard) | 10 |
| **Total** | **100** |

**Submission:** Upload both the `.pkt` file AND the PDF report to Canvas Module 06 Lab Assignment by Tuesday, December 1, 2026 at 11:59 PM CST.

---

## Part 9 — Challenge Exercise

### Challenge 1: Analyze SD-WAN Policy Configuration

1. Review the Cisco DevNet SD-WAN sandbox documentation at [https://developer.cisco.com/sdwan](https://developer.cisco.com/sdwan). Identify the four components of the SD-WAN control plane and describe the role of each in your own words — connecting each to the GRE/BGP analog you used in the lab.
2. In the Cisco SD-WAN Design Guide (Chapter 4), read the centralized data policy section. Design on paper a data policy that routes video conferencing traffic (DSCP EF) preferentially over an MPLS transport TLOC color. Write the policy logic as pseudocode: match condition, action, fallback action.
3. Explain how the control policy differs from the data policy in SD-WAN, and give a specific use case where you would use a control policy instead of a data policy to achieve a hub-and-spoke topology.
4. Reflect: In your lab, BGP local preference controlled path selection globally (for all prefixes from a neighbor). How does SD-WAN data policy improve on this by enabling per-application path selection? What real-world operational benefit does this provide?

### Challenge 2: VXLAN Overlay Design Document

1. Design a VXLAN fabric for a small data center with 4 leaf switches (Leaf-1 through Leaf-4) and 2 spine switches (Spine-1, Spine-2). Assign VTEP IP addresses from the 172.16.100.0/24 range (one loopback per leaf). Assign VNIs starting at 10001 for three tenant VLANs: VLAN 10 (Finance), VLAN 20 (Engineering), VLAN 30 (Guest).
2. Write the key NX-OS configuration elements for Leaf-1: the `interface nve 1` section, VNI-to-VLAN mappings, and EVPN route-target assignments using the format `<ASN>:<VNI>`.
3. Explain how EVPN Type 2 (MAC/IP) and Type 5 (IP Prefix) routes work together in your design to enable inter-subnet routing without a centralized L3 gateway at the spine layer (distributed anycast gateway model).
4. Identify two failure scenarios in your design (e.g., single leaf failure, spine failure) and describe how the EVPN control plane enables the fabric to recover automatically.

### Reflection Questions

1. A CTO asks you to justify the cost of migrating from a traditional MPLS WAN ($2,000/month/site for 200 sites) to SD-WAN with broadband internet plus LTE backup ($400/month/site). The MPLS provider guarantees 99.99% uptime and 20ms latency. What are the three strongest technical arguments for migration, and what trade-offs would you honestly disclose regarding latency variability and security?
2. Compare VXLAN with MPLS L2VPN as data center overlay technologies. For what specific use cases is VXLAN clearly superior (hint: think about hypervisor integration and VNI scale), and where does MPLS still maintain advantages (hint: think about existing SP infrastructure and QoS integration)?
