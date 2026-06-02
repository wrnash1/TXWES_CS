# Lab Activity: Module 05 - Spanning Tree Protocol (STP & RSTP)

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 60-75 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will observe and manipulate Spanning Tree Protocol on a three-switch topology in Cisco Packet Tracer. You will inspect the default STP election, force a specific switch to become root bridge, identify port roles, configure PortFast and BPDU Guard on access ports, and analyze STP behavior after a topology change.

This lab maps to CCNA 200-301 exam objectives 2.5 (describe and configure Rapid PVST+ operation) and 2.6 (configure and verify PortFast and BPDU Guard).

---

## Objectives

By completing this lab you will be able to:

- Read `show spanning-tree` output and identify root bridge, root ports, designated ports, and blocked ports
- Manipulate STP root bridge election by adjusting Bridge Priority
- Configure PortFast on access ports
- Configure BPDU Guard and observe err-disabled behavior
- Predict which ports are blocked in a given topology and verify with show commands

---

## Equipment List

Use the following devices in Packet Tracer:

- 3x Cisco Catalyst 2960-24TT switches (SW1, SW2, SW3)
- 2x PCs (PC1 and PC2)
- Straight-through Ethernet cables for all connections

---

## Topology

Connect devices as follows:

- SW1 Gi0/1 to SW2 Gi0/1
- SW1 Gi0/2 to SW3 Gi0/1
- SW2 Gi0/2 to SW3 Gi0/2
- SW1 Fa0/1 to PC1
- SW3 Fa0/1 to PC2

This creates a triangle (loop) between three switches, which STP will break by blocking one port.

---

## Part 1: Observing Default STP Behavior

### Step 1: Configure Hostnames

Set hostnames on all three switches before configuring STP:

```ios
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW1
SW1(config)# end
```

Repeat for SW2 and SW3.

### Step 2: Inspect Default STP Before Manipulation

On each switch, examine the default STP state:

```ios
SW1# show spanning-tree
```

Record the following from the output of each switch:

- This switch's own Bridge ID (Priority + MAC)
- Whether this switch is the root bridge
- For each port: the role (Root, Designated, Desgn) and state (FWD, BLK, LRN, LIS)

From the three `show spanning-tree` outputs, determine:

- Which switch is the root bridge, and why (compare the BIDs from all three)
- Which port on each non-root switch is the Root Port
- Which port in the triangle is in Blocking state

### Step 3: Verify the Root Bridge Decision

The switch with the lowest BID is root. Default priority is 32768. If all three switches have default priority, compare their MAC addresses to determine root.

From SW1's output, look for the line showing "Root ID Priority" and "Root ID Address". Compare to "Bridge ID Priority" and "Bridge ID Address" on the same switch. If Root ID equals Bridge ID, this switch is the root.

Record your findings in your deliverables.

---

## Part 2: Manipulating the Root Bridge Election

### Step 4: Force SW1 to Be Root for VLAN 1

Change SW1's Bridge Priority to ensure it wins the root bridge election:

```ios
SW1# configure terminal
SW1(config)# spanning-tree vlan 1 priority 4096
SW1(config)# end
```

Allow STP to reconverge (wait 5-10 seconds in Packet Tracer) then verify:

```ios
SW1# show spanning-tree vlan 1
```

Confirm that SW1 is now the root bridge. Check that the Root ID Priority and Address now match SW1's own Bridge ID.

### Step 5: Force SW2 to Be Secondary Root

Configure SW2 as the secondary root (backup root if SW1 fails):

```ios
SW2# configure terminal
SW2(config)# spanning-tree vlan 1 root secondary
SW2(config)# end
```

The `root secondary` macro sets SW2's priority to 28672.

Verify SW2's priority:

```ios
SW2# show spanning-tree vlan 1
```

Confirm SW2's Bridge Priority is 28672 and it is not currently the root.

### Step 6: Identify New Port Roles After Root Change

With SW1 as root, run `show spanning-tree` on all three switches again. Record the new port roles:

- All ports on SW1 should be Designated (it is root)
- Each non-root switch (SW2 and SW3) should have exactly one Root Port
- One port in the triangle should still be in Blocking state (now on SW3 or SW2 depending on path cost)

---

## Part 3: PortFast and BPDU Guard

### Step 7: Configure PortFast on PC-Facing Ports

PC1 connects to SW1 Fa0/1 and PC2 connects to SW3 Fa0/1. Configure PortFast on these access ports:

```ios
SW1# configure terminal
SW1(config)# interface FastEthernet0/1
SW1(config-if)# spanning-tree portfast
SW1(config-if)# end
```

Repeat on SW3 Fa0/1.

### Step 8: Configure BPDU Guard

Add BPDU Guard to the same ports to protect against unauthorized switch connections:

```ios
SW1# configure terminal
SW1(config)# interface FastEthernet0/1
SW1(config-if)# spanning-tree bpduguard enable
SW1(config-if)# end
```

Repeat on SW3 Fa0/1.

### Step 9: Test BPDU Guard Behavior

To observe BPDU Guard in action, disconnect PC1 from SW1 Fa0/1 in Packet Tracer. Then connect a switch (place a new 2960 in the topology) to SW1 Fa0/1. This new switch will send BPDUs, triggering BPDU Guard.

Run:

```ios
SW1# show interfaces FastEthernet0/1
```

Look for the line `FastEthernet0/1 is err-disabled` in the output. This confirms BPDU Guard triggered.

To recover the port:

```ios
SW1# configure terminal
SW1(config)# interface FastEthernet0/1
SW1(config-if)# shutdown
SW1(config-if)# no shutdown
SW1(config-if)# end
```

---

## Part 4: Verification and Troubleshooting

### Step 10: Full STP Verification

Run the following on SW1 and document the output:

```ios
SW1# show spanning-tree
SW1# show spanning-tree vlan 1
SW1# show spanning-tree interface GigabitEthernet0/1 detail
```

The detailed interface output shows path cost, port priority, and port ID.

### Step 11: Troubleshooting Scenarios

Work through each scenario and document your analysis.

Scenario A: After configuring SW1 as root with priority 4096, a new switch (SW4) is added to the topology with a Bridge Priority of 0 (the minimum). What effect does this have on the STP topology, and what Cisco feature should be configured on SW1's uplink toward SW4 to prevent SW4 from taking over the root bridge role?

Expected answer: SW4 with priority 0 will outbid SW1 (priority 4096) and become the new root bridge, disrupting the planned topology. Root Guard should be configured on SW1's port facing SW4. With Root Guard enabled, if a superior BPDU is received on that port, it enters root-inconsistent (blocking) state instead of becoming a Root Port.

Scenario B: A helpdesk report says PC1 is taking 30 seconds to get a DHCP address after plugging in. Which STP feature resolves this, and what is the risk if it is improperly applied?

Expected answer: PortFast eliminates the 30-second Listening and Learning phases on access ports, allowing immediate forwarding. The risk: if PortFast is applied to a port that connects to another switch, STP is bypassed and a bridging loop can form.

Scenario C: After configuring BPDU Guard on SW1 Fa0/1, the port goes err-disabled. The administrator ran `no shutdown` to recover it, but it immediately went err-disabled again. What is the likely cause?

Expected answer: A switch is still connected to Fa0/1 and continues sending BPDUs. Each time the port recovers, it immediately receives a BPDU and BPDU Guard triggers again. The root cause (the connected switch) must be removed before the port can remain up.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show spanning-tree` output from each of the three switches before priority manipulation (Step 2), with the root bridge, Root Ports, and Blocked port identified and annotated
2. Screenshot of `show spanning-tree vlan 1` from SW1 after setting priority to 4096, confirming SW1 is root
3. Port role diagram: draw the three-switch triangle topology and label each port with its STP role (Root, Designated, or Blocked) after SW1 becomes root
4. Screenshot showing err-disabled state on Fa0/1 after BPDU Guard triggers
5. Screenshot of successful port recovery after shutdown/no shutdown
6. Written answers to Troubleshooting Scenarios A, B, and C (3-5 sentences each)

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| Pre-Manipulation STP Screenshots | 20 | All three show spanning-tree outputs captured with correct annotations |
| Root Bridge Manipulation | 15 | SW1 shown as root with correct priority in output |
| Port Role Diagram | 20 | All six port roles correctly labeled on the triangle topology diagram |
| BPDU Guard Demonstration | 20 | Err-disabled triggered and documented; port recovery shown |
| Troubleshooting Scenarios | 25 | Correct analysis for all three scenarios (A=8, B=8, C=9) |

Partial credit awarded for demonstrably attempted but incomplete work.
