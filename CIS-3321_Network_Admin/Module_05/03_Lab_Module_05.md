# Lab Activity: Module 05 – Network Infrastructure: Cables, Switches, Routers
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Lab Overview

**Lab Title:** Switch MAC Address Table Observation and Hub vs. Switch Behavior Comparison

**Format:** Cisco Packet Tracer Simulation

**Estimated Time:** 60–75 minutes

**Points:** 100 points total

**Prerequisites:**

- Module 05 video lectures watched (both Part 1 and Part 2)
- Module 05 Reading Guide reviewed
- Cisco Packet Tracer installed

**Learning Objectives:**

By completing this lab, you will be able to:

- Build a switched Ethernet network in Cisco Packet Tracer
- Observe how a switch populates its MAC address table through traffic
- Use the show mac address-table command to verify learned MAC addresses
- Use Simulation Mode to observe the difference between switch unicast forwarding and unknown unicast flooding
- Compare traffic behavior on a hub versus a switch

---

### Background

The MAC address table (CAM table) is what makes a switch intelligent. By learning which device is on which port, a switch can forward frames only to the correct destination — dramatically reducing unnecessary traffic compared to a hub. This lab makes that behavior visible and measurable.

---

### Part 1: Build a Switched Network and Observe MAC Learning

#### Step 1: Build the Topology

1. Open Cisco Packet Tracer.
2. Place four PCs: PC0, PC1, PC2, PC3.
3. Place one Cisco 2960 switch in the center.
4. Connect each PC to the switch using straight-through copper cables:
   - PC0 → FastEthernet0/1
   - PC1 → FastEthernet0/2
   - PC2 → FastEthernet0/3
   - PC3 → FastEthernet0/4
5. Confirm all link lights turn green after a few seconds.

#### Step 2: Assign IP Addresses to All PCs

Configure each PC (Desktop tab → IP Configuration → Static):

- PC0: 192.168.1.10 / 255.255.255.0
- PC1: 192.168.1.20 / 255.255.255.0
- PC2: 192.168.1.30 / 255.255.255.0
- PC3: 192.168.1.40 / 255.255.255.0

#### Step 3: Clear the Switch MAC Table (Start Fresh)

Click the switch → CLI tab. Enter privileged mode and clear the table:

```
enable
clear mac address-table dynamic
show mac address-table
```

Confirm the table is empty (or contains only static entries).

#### Step 4: Generate Traffic Between Two PCs

1. Click PC0 → Desktop → Command Prompt.
2. Type: `ping 192.168.1.20`
3. After the ping completes, return to the switch CLI.

#### Step 5: Observe the MAC Address Table

```
show mac address-table
```

Record the current table entries:

| VLAN | MAC Address | Type    | Port         |
|------|-------------|---------|--------------|
|      |             |         |              |
|      |             |         |              |

**Question 1:** After pinging from PC0 to PC1, how many MAC addresses appear in the table? Which ports are they associated with? Why are MAC addresses from PC2 and PC3 not yet in the table?

#### Step 6: Ping All PCs

From PC0, ping PC2 and PC3:

```
ping 192.168.1.30
ping 192.168.1.40
```

Then run `show mac address-table` again.

**Question 2:** How many entries are now in the MAC address table? Is the table fully populated? Explain why pinging from PC0 causes the switch to learn all four MAC addresses rather than just PC0's.

---

### Part 2: Observe Unknown Unicast Flooding vs. Known Unicast Forwarding

#### Step 1: Switch to Simulation Mode

In Packet Tracer, switch to Simulation mode (bottom right). Filter events to show only ICMP.

#### Step 2: Clear the MAC Table Again

In the switch CLI:

```
enable
clear mac address-table dynamic
```

#### Step 3: Send One Ping in Simulation Mode

1. From PC0's Command Prompt, type `ping 192.168.1.20` and press Enter.
2. In Simulation mode, click Play once to advance the first step.
3. Observe the ICMP packet icon leaving PC0.

#### Step 4: Watch the Flooding Behavior

Before the switch knows PC1's MAC, the first ICMP Echo Request will be preceded by an ARP request. Watch the ARP request:

- Does the switch send it to only one port, or does it flood to all ports?
- Note which ports receive the frame.

**Question 3:** When the switch receives the ARP request and the destination MAC is unknown (FF:FF:FF:FF:FF:FF broadcast), which ports does it send the frame to? Is this flooding or forwarding? What OSI layer is the switch operating at when it makes this decision?

#### Step 5: Watch the Known Unicast Forwarding

After the ARP reply returns from PC1, the switch now knows PC1's MAC address.

1. Continue stepping through the simulation.
2. Observe the next ICMP Echo Request (the ping itself).
3. Watch which ports the switch uses to forward the packet.

**Question 4:** After the ARP exchange completes and the switch has learned PC1's MAC, does the ICMP packet go to all ports or only to the port connected to PC1? What does this demonstrate about the switch's forwarding behavior for known unicast frames?

---

### Part 3: Hub vs. Switch Comparison

#### Step 1: Add a Hub Segment

1. In Realtime mode, add a new Hub device from the Hubs section of the device panel.
2. Connect two new PCs (PC4 and PC5) to the hub.
3. Connect the hub to the switch's FastEthernet0/5 port using a straight-through cable.
4. Assign IPs:
   - PC4: 192.168.1.50 / 255.255.255.0
   - PC5: 192.168.1.60 / 255.255.255.0

#### Step 2: Test Traffic in Simulation Mode

Switch to Simulation Mode. From PC4, ping PC5.

**Question 5:** Observe the behavior of the hub. When PC4 sends a frame destined for PC5, which devices connected to the hub receive the frame (including PC5 and the switch)? How does this contrast with switch forwarding behavior observed in Part 2?

**Question 6:** What is a collision domain? Is the hub segment (PC4, PC5, and the hub port on the switch) one collision domain or multiple? How does this compare to the switch's individual ports?

---

### Deliverables

Submit the following to the Canvas assignment dropbox:

**Deliverable 1 (25 points):** Screenshots of the switch MAC address table after Step 5 (partial) and Step 6 (full). Include answers to Questions 1 and 2 typed below the screenshots.

**Deliverable 2 (25 points):** Screenshots from Simulation Mode showing the ARP flooding behavior (Step 4) and the known unicast forwarding behavior (Step 5). Include answers to Questions 3 and 4.

**Deliverable 3 (25 points):** Screenshot showing the hub segment in the topology and the simulation of hub flooding behavior. Include answers to Questions 5 and 6.

**Deliverable 4 (25 points):** A typed analysis (150–200 words) comparing hub and switch performance. Address: why switches replaced hubs, how MAC address learning enables efficient forwarding, and what the difference between a collision domain and a broadcast domain means for network design.

---

### Grading Rubric

| Deliverable | Points | Full Credit Criteria |
|-------------|--------|----------------------|
| MAC table screenshots and answers | 25 | Both partial and full MAC table captured; Questions 1–2 answered correctly |
| Simulation flooding/forwarding screenshots | 25 | Flooding and unicast forwarding screenshots captured; Questions 3–4 answered with correct OSI layer references |
| Hub topology and behavior screenshot | 25 | Hub segment visible; flooding behavior documented; Questions 5–6 answered correctly |
| Written analysis | 25 | 150–200 words; accurate technical comparison; collision vs. broadcast domain distinction correct |
| **Total** | **100** | |

---

### Common Issues and Fixes

**Issue:** MAC address table shows entries before Step 3 clearing.

**Fix:** Run `clear mac address-table dynamic` from privileged exec mode on the switch before generating test traffic.

**Issue:** Simulation Mode shows no ICMP events.

**Fix:** In Simulation Panel, click Edit Filters and ensure ICMP and ARP are checked. Both are needed to observe the ARP exchange that precedes the first ping.

**Issue:** Hub does not appear in device panel.

**Fix:** Hubs are in the "Hubs" subcategory under Network Devices, not under Switches. Look specifically for the Hub category.

---

## Part 9 — Challenge Exercise

These advanced steps extend Module 05 with STP observation and EtherChannel configuration.

### Challenge Step 1: Observe Spanning Tree Protocol in Packet Tracer

1. Build a topology with three interconnected Cisco 2960 switches forming a triangle (Switch1–Switch2, Switch2–Switch3, Switch1–Switch3).
2. Assign IP addresses to the switch management VLANs:
   - Switch1 VLAN 1: 192.168.1.1/24
   - Switch2 VLAN 1: 192.168.1.2/24
   - Switch3 VLAN 1: 192.168.1.3/24
3. On each switch, run `show spanning-tree vlan 1` and record:
   - Which switch is the Root Bridge
   - The Bridge Priority and MAC address of the root bridge
   - Which ports on the non-root switches are in Forwarding state vs. Blocking state

**Challenge Question 1:** Explain why one of the three redundant links between the switches is in Blocking state. What would happen to that blocked port if the active link connecting the root bridge to another switch failed? Which STP port role and state would the previously blocked port transition to, and how long does IEEE 802.1D STP take to converge?

### Challenge Step 2: Force a Root Bridge Election

1. On Switch1, reduce the spanning tree priority to force it to become the root bridge:
   ```
   spanning-tree vlan 1 priority 4096
   ```
2. Wait for STP to reconverge (approximately 30–50 seconds in Packet Tracer).
3. Run `show spanning-tree vlan 1` on all three switches again.

**Challenge Question 2:** After forcing Switch1 to become the root, which ports changed from Forwarding to Blocking (or vice versa)? Write out the complete port role assignment (Root Port, Designated Port, Alternate Port) for each switch after reconvergence. How does the `priority` value affect which switch becomes the root bridge?

### Challenge Step 3: Configure EtherChannel Between Two Switches

1. Add a second link between Switch1 and Switch2 (connect Fa0/2 on each to each other using a second straight-through cable).
2. Without EtherChannel, STP should block one of the two links. Verify this with `show spanning-tree`.
3. Configure LACP EtherChannel on both switches to aggregate both links:
   ```
   interface range fa0/1 - 2
   channel-group 1 mode active
   ```
4. Verify with `show etherchannel summary` — the bundle should show `SU` (in use, layer 2) with both interfaces aggregated.

**Challenge Question 3:** After configuring EtherChannel, how does STP treat the two physical links? What is the effective bandwidth of the aggregated link? Why does EtherChannel solve the problem of STP blocking redundant parallel links between the same two switches?

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
