# Lab Activity: Module 11 — Switching: VLANs, STP, and EtherChannel

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Overview

This lab has two parts. Part 1 uses Cisco Packet Tracer to configure VLANs, trunk ports, and inter-VLAN routing using Router-on-a-Stick. Part 2 configures EtherChannel between two switches using LACP and verifies the channel with show commands. Together these exercises reinforce VLAN design, 802.1Q trunking, STP behavior, and link aggregation concepts from the lecture.

Estimated Time: 65–80 minutes

Required Tools:

- Cisco Packet Tracer 8.x (free download at netacad.com with a free account)

---

### Learning Objectives

By the end of this lab, you will be able to:

1. Create VLANs on a Cisco switch and assign ports to the correct VLAN.
2. Configure a trunk port between a switch and a router for 802.1Q encapsulation.
3. Configure Router-on-a-Stick with subinterfaces for inter-VLAN routing.
4. Configure an EtherChannel bundle using LACP Active mode.
5. Verify VLAN, trunk, STP, and EtherChannel configuration using show commands.
6. Interpret the output of show vlan brief, show interfaces trunk, show spanning-tree, and show etherchannel summary.

---

### Part 1: VLAN Configuration and Inter-VLAN Routing

#### Part 1 Step 1: Build the Topology

Open Packet Tracer and create the following topology:

Switch (SW1):

- Fa0/1: connects to Router Fa0/0 (trunk link)
- Fa0/2: connects to PC-Finance (VLAN 10)
- Fa0/3: connects to PC-HR (VLAN 20)
- Fa0/4: connects to PC-Engineering (VLAN 30)

Router (R1):

- Fa0/0: connects to SW1 Fa0/1 (trunk link — one physical interface, three subinterfaces)

Add three PCs:

- PC-Finance: IP via DHCP or static 192.168.10.10/24, gateway 192.168.10.1
- PC-HR: IP via DHCP or static 192.168.20.10/24, gateway 192.168.20.1
- PC-Engineering: IP via DHCP or static 192.168.30.10/24, gateway 192.168.30.1

#### Part 1 Step 2: Create VLANs on SW1

```cisco
vlan 10
 name Finance
!
vlan 20
 name HR
!
vlan 30
 name Engineering
```

#### Part 1 Step 3: Assign Access Ports

```cisco
interface FastEthernet0/2
 switchport mode access
 switchport access vlan 10
!
interface FastEthernet0/3
 switchport mode access
 switchport access vlan 20
!
interface FastEthernet0/4
 switchport mode access
 switchport access vlan 30
```

#### Part 1 Step 4: Configure the Trunk Port

```cisco
interface FastEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 switchport trunk native vlan 999
```

Note: In Packet Tracer you may need to configure `switchport trunk encapsulation dot1q` before `switchport mode trunk` depending on the switch model used.

#### Part 1 Step 5: Configure Router Subinterfaces

On R1, configure subinterfaces for each VLAN:

```cisco
interface FastEthernet0/0
 no shutdown
!
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
!
interface FastEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
!
interface FastEthernet0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
```

#### Part 1 Step 6: Verify and Test

On SW1, run:

```cisco
show vlan brief
show interfaces trunk
show interfaces FastEthernet0/2 switchport
```

From PC-Finance, ping PC-HR (192.168.20.10). The ping should succeed because traffic goes through the router subinterfaces.

From PC-Finance, ping PC-Engineering (192.168.30.10). This should also succeed.

Lab Questions — Part 1:

Question 1: Run show vlan brief on SW1. How many VLANs appear, and what is the significance of VLAN 1 appearing even though you did not create it? What default ports are assigned to VLAN 1?

Question 2: Run show interfaces trunk on SW1. What information does this command show for FastEthernet0/1? Specifically, what does the "VLANs allowed and active in management domain" column show, and why does it matter?

Question 3: When PC-Finance (192.168.10.10) sends a ping to PC-HR (192.168.20.10), describe the complete Layer 2 and Layer 3 path the packet takes. Include the VLAN tags added and removed at each step.

Question 4: Why is it necessary to create a subinterface for each VLAN on the router rather than just one interface? What would happen if you tried to configure two IP addresses on the same physical interface with no subinterfaces?

---

### Part 2: EtherChannel Configuration with LACP

#### Part 2 Step 1: Extend the Topology

Add a second switch (SW2) to the topology. Connect SW1 and SW2 with four physical links:

- SW1 Fa0/5 to SW2 Fa0/5
- SW1 Fa0/6 to SW2 Fa0/6
- SW1 Fa0/7 to SW2 Fa0/7
- SW1 Fa0/8 to SW2 Fa0/8

Add a PC to SW2:

- PC-Finance-2: 192.168.10.20/24, gateway 192.168.10.1, connected to SW2 Fa0/2 (access port, VLAN 10)

#### Part 2 Step 2: Observe STP Before EtherChannel

Before configuring EtherChannel, run on SW1:

```cisco
show spanning-tree vlan 10
```

Observe which ports are in Forwarding state and which are in Blocking state. With four redundant links between the switches and no EtherChannel, STP will block three of the four links to prevent a loop. Record which ports are blocked.

#### Part 2 Step 3: Configure EtherChannel on SW1

```cisco
interface range FastEthernet0/5 - 8
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 channel-group 1 mode active
```

#### Part 2 Step 4: Configure EtherChannel on SW2

```cisco
interface range FastEthernet0/5 - 8
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 channel-group 1 mode active
```

#### Part 2 Step 5: Verify EtherChannel

On SW1, run:

```cisco
show etherchannel summary
show interfaces Port-Channel1
show spanning-tree vlan 10
```

The show etherchannel summary output should show four ports (Fa0/5–Fa0/8) listed as P (bundled in port-channel). The Port-Channel1 interface should be Up. show spanning-tree should now show Port-Channel1 as a single logical link in Forwarding state, with no individual member ports blocked.

#### Part 2 Step 6: Test Connectivity Across EtherChannel

From PC-Finance (on SW1), ping PC-Finance-2 (on SW2) at 192.168.10.20. The ping should succeed, with traffic crossing the EtherChannel bundle.

Lab Questions — Part 2:

Question 5: Before configuring EtherChannel (Step 2), STP blocked three of the four links between SW1 and SW2. Why did STP block these ports? What would happen on the network if STP had not blocked them?

Question 6: After configuring EtherChannel (Step 5), show spanning-tree shows Port-Channel1 instead of individual FastEthernet ports. Explain why this is significant. What is the effective bandwidth available between the two switches now compared to before EtherChannel?

Question 7: In Step 3, the channel-group command uses mode active. What protocol does this invoke? What mode would you use on SW2 if you wanted to use the minimum possible negotiation messaging while still forming the channel?

Question 8: EtherChannel load-balances on a per-flow basis. Explain what this means. If PC-Finance sends a large file transfer to PC-Finance-2, will that traffic use all four physical links simultaneously? Why or why not?

Question 9: A classmate suggests using `channel-group 1 mode on` (static EtherChannel) instead of LACP. What is the risk of using static mode compared to LACP, and in what situation might static mode be the only available option?

Question 10: If one of the four physical links in the EtherChannel bundle loses link (for example, the cable is unplugged from SW1 Fa0/7), what happens to the EtherChannel? Does traffic stop? Does STP reconverge? Explain the behavior.

---

### Deliverables

Submit the following in a single PDF or Word document:

1. Part 1 Topology Screenshot — Packet Tracer topology with all devices labeled and connected.

2. Part 1 Verification Screenshots — show vlan brief and show interfaces trunk output from SW1.

3. Part 1 Ping Screenshots — Successful ping from PC-Finance to PC-HR and from PC-Finance to PC-Engineering.

4. Part 1 Written Responses — Answers to Questions 1 through 4 in complete sentences.

5. Part 2 Pre-EtherChannel STP Screenshot — show spanning-tree output showing blocked ports before EtherChannel.

6. Part 2 EtherChannel Screenshots — show etherchannel summary and show spanning-tree output after EtherChannel is configured.

7. Part 2 Ping Screenshot — Successful ping across EtherChannel.

8. Part 2 Written Responses — Answers to Questions 5 through 10 in complete sentences.

---

### Grading Rubric (100 Points Total)

| Item | Points |
|------|--------|
| Part 1 topology screenshot — all devices labeled | 5 |
| Part 1 show vlan brief — VLANs and ports correct | 8 |
| Part 1 show interfaces trunk — trunk visible, VLANs listed | 8 |
| Part 1 ping screenshots — both cross-VLAN pings successful | 8 |
| Question 1 — VLAN 1 behavior explained | 6 |
| Question 2 — show interfaces trunk interpreted correctly | 6 |
| Question 3 — Layer 2/3 path described accurately | 8 |
| Question 4 — subinterface purpose explained | 6 |
| Part 2 pre-EtherChannel STP screenshot — blocked ports visible | 6 |
| Part 2 show etherchannel summary — P flags and bundle visible | 8 |
| Part 2 show spanning-tree — Port-Channel1 in forwarding | 6 |
| Part 2 ping screenshot — cross-EtherChannel ping successful | 4 |
| Question 5 — STP blocking reason explained | 6 |
| Question 6 — EtherChannel STP benefit explained | 6 |
| Question 7 — LACP protocol and Passive mode identified | 4 |
| Question 8 — per-flow load balancing explained | 4 |
| Question 9 — static On mode risk stated | 3 |
| Question 10 — link failure behavior explained | 2 |
| Total | 100 |

---

### Submission Instructions

Save your document as: Lab11_Firstname_Lastname.pdf

Submit to the Module 11 Lab assignment in the course LMS before the posted deadline.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
