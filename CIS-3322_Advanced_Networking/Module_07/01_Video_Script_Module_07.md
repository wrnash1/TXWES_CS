# Video Script: Module 07 - Inter-VLAN Routing Solutions

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 3: IP Connectivity - 25%)
**Estimated Duration:** 22 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Record in 1080p with a clean slide backdrop
- Use Packet Tracer 8.x for both router-on-a-stick and Layer 3 switch SVI demonstrations
- Show side-by-side comparison of both methods
- Insert [SHOW DIAGRAM] markers as full-screen overlays
- Pause 2 seconds after each CCNA Exam Tip callout

---

## Section 1: Introduction - Why VLANs Need a Router [00:00 - 03:00]

Welcome to Module 07. I am Professor Nash. Today we solve a problem that every network engineer faces: VLANs create logical broadcast boundaries, but how do devices in different VLANs communicate with each other?

By design, VLANs are isolated. VLAN 10 (Engineering) and VLAN 20 (Sales) cannot exchange traffic at Layer 2. They need a Layer 3 device to route between them. That is where inter-VLAN routing comes in.

[SHOW DIAGRAM: Two VLANs shown as separate broadcast bubbles on a switch. An arrow showing an IP packet that needs to travel from VLAN 10 to VLAN 20 being blocked at the VLAN boundary, with a question mark showing the missing routing step]

There are three methods for inter-VLAN routing:

- Legacy method: separate physical router interface per VLAN (not scalable, rarely used)
- Router-on-a-stick (ROAS): one physical router interface with multiple logical subinterfaces
- Layer 3 switch with SVIs: preferred method for modern campus networks

Today we cover the last two methods in detail with full configuration walkthroughs.

---

## Section 2: Router-on-a-Stick (ROAS) [03:00 - 10:00]

[SHOW DIAGRAM: A switch connected to a router via a single trunk link. The router's interface is divided into three subinterfaces: G0/0.10, G0/0.20, G0/0.30 each labeled with their VLAN and IP address]

Router-on-a-stick uses a single physical router interface connected to the switch's trunk port. The physical interface is subdivided into logical subinterfaces — one per VLAN. Each subinterface is configured with:

1. An 802.1Q encapsulation command identifying which VLAN it serves
2. An IP address in that VLAN's subnet (which becomes the default gateway for hosts in that VLAN)

### Configuration Walkthrough

First, configure the switch trunk port:

```ios
SW1(config)# interface GigabitEthernet0/1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20,30
SW1(config-if)# end
```

On the router, bring up the physical interface (no IP address on the parent interface):

```ios
R1(config)# interface GigabitEthernet0/0
R1(config-if)# no shutdown
R1(config-if)# no ip address
```

Create subinterfaces for each VLAN:

```ios
R1(config)# interface GigabitEthernet0/0.10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 192.168.10.1 255.255.255.0

R1(config)# interface GigabitEthernet0/0.20
R1(config-subif)# encapsulation dot1Q 20
R1(config-subif)# ip address 192.168.20.1 255.255.255.0

R1(config)# interface GigabitEthernet0/0.30
R1(config-subif)# encapsulation dot1Q 30
R1(config-subif)# ip address 192.168.30.1 255.255.255.0
R1(config)# end
```

CCNA Exam Tip: The `encapsulation dot1Q [vlan-id]` command must be entered before the `ip address` command on a subinterface. Forgetting this is the most common router-on-a-stick configuration mistake. The subinterface will reject the IP address if encapsulation is not set first.

### Limitation of Router-on-a-Stick

All inter-VLAN traffic must traverse the single physical link between the switch and router. This becomes a bandwidth bottleneck in high-traffic environments. ROAS is appropriate for smaller networks or lab scenarios, but Layer 3 switch SVIs are the preferred solution for enterprise deployments.

---

## Section 3: Layer 3 Switch SVIs [10:00 - 16:30]

[SHOW DIAGRAM: A Cisco Catalyst 3650 (multilayer switch) with three SVIs labeled VLAN 10, VLAN 20, VLAN 30, each showing an IP address. End devices connect directly to the same switch via access ports. No external router required for inter-VLAN routing]

A Layer 3 switch performs routing internally using Switched Virtual Interfaces (SVIs). Each SVI is a virtual interface that represents one VLAN. Assigning an IP address to an SVI makes the switch the default gateway for all hosts in that VLAN.

Inter-VLAN traffic routed by SVIs stays within the switch's hardware. Traffic does not need to exit to an external router and return. This makes SVI-based routing far more efficient and scalable.

### SVI Configuration Walkthrough

Enable IP routing on the multilayer switch (required — without this, SVIs cannot route):

```ios
MLS1(config)# ip routing
```

Create VLANs and SVIs:

```ios
MLS1(config)# vlan 10
MLS1(config-vlan)# name ENGINEERING
MLS1(config-vlan)# vlan 20
MLS1(config-vlan)# name SALES
MLS1(config-vlan)# exit

MLS1(config)# interface vlan 10
MLS1(config-if)# ip address 192.168.10.1 255.255.255.0
MLS1(config-if)# no shutdown

MLS1(config)# interface vlan 20
MLS1(config-if)# ip address 192.168.20.1 255.255.255.0
MLS1(config-if)# no shutdown
```

Assign access ports to VLANs:

```ios
MLS1(config)# interface FastEthernet0/1
MLS1(config-if)# switchport mode access
MLS1(config-if)# switchport access vlan 10
```

Verify SVI state:

```ios
MLS1# show ip interface brief
MLS1# show interfaces vlan 10
```

CCNA Exam Tip: An SVI is only in the `up/up` state when at least one access port in that VLAN is active. If VLAN 10 has no active ports, the SVI shows `up/down`. This is a critical troubleshooting point — check `show vlan brief` to confirm at least one port is in that VLAN and is up.

---

## Section 4: Method Comparison and Troubleshooting [16:30 - 19:30]

[SHOW DIAGRAM: Side-by-side comparison table showing Router-on-a-Stick vs Layer 3 Switch SVIs across six rows: Hardware needed, Traffic path, Scalability, Configuration complexity, Best use case, CCNA test focus]

| Criteria | Router-on-a-Stick | Layer 3 Switch SVIs |
|---|---|---|
| Hardware | External router + switch | Multilayer switch only |
| Traffic path | Exits switch, enters router, returns | Stays within switch hardware |
| Scalability | Limited by single physical link | High — hardware-assisted routing |
| Configuration | Subinterfaces + trunk on switch | SVIs + ip routing on switch |
| Best for | Small networks, labs | Enterprise campus networks |

### Troubleshooting Checklist

Router-on-a-stick common issues:

- Parent interface is down: run `no shutdown` on the parent physical interface, not just the subinterfaces
- `encapsulation dot1Q` missing or wrong VLAN ID on subinterface
- Switch port not set to trunk mode, or VLAN not in allowed list

Layer 3 switch SVI common issues:

- `ip routing` not enabled globally — SVIs will not route
- SVI is `up/down` — no active ports in that VLAN (`show vlan brief` to check)
- VLAN not created in VLAN database — SVI comes up but has no associated ports

---

## Section 5: Lab Preview and Exam Readiness [19:30 - 22:00]

This week's lab has two parts: Part 1 uses router-on-a-stick with a 1941 router, and Part 2 replaces the external router with a Catalyst 3650 multilayer switch using SVIs. You will verify inter-VLAN routing in both topologies using ping between hosts in different VLANs.

Key verification commands:

```ios
R1# show ip route
MLS1# show ip route
MLS1# show ip interface brief
MLS1# show interfaces vlan 10
```

For additional study, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

---

## End Card

Module 07 Complete
Next: Module 08 - OSPFv2 Routing Concepts and Setup
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
