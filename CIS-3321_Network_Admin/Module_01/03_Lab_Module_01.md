# Lab Activity: Module 01 – Networking Fundamentals and the OSI Model
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Lab Overview

**Lab Title:** OSI Model Observation and Star Topology Construction

**Format:** Cisco Packet Tracer Simulation

**Estimated Time:** 60–75 minutes

**Points:** 100 points total

**Prerequisites:**

- Cisco Packet Tracer installed (free download at netacad.com with free account)
- Module 01 video lectures watched (both Part 1 and Part 2)
- Module 01 Reading Guide reviewed

**Learning Objectives:**

By completing this lab, you will be able to:

- Build a functional star topology network in Cisco Packet Tracer
- Assign static IP addresses to hosts and verify connectivity
- Use the ping command to test Layer 3 ICMP connectivity
- Use Packet Tracer Simulation Mode to observe Layer 2 frames and Layer 3 packets in transit
- Identify encapsulation headers at different OSI layers within captured PDUs

---

### Background

The OSI model is not just a chart on a slide — it describes real processes that occur every time data crosses a network. In this lab, you will observe the OSI model in action. When you use Packet Tracer's Simulation Mode, you can pause a transmission and inspect the headers that have been added at each layer. This is encapsulation made visible.

The lab is divided into two parts. Part 1 focuses on building the topology and testing basic connectivity. Part 2 uses Simulation Mode to observe OSI layer behavior at the frame and packet level.

---

### Part 1: Build a Star Topology and Test IP Connectivity

**Objective:** Create a star topology with three hosts connected to a switch, assign IP addresses, and verify connectivity using ping.

#### Step 1: Launch Packet Tracer and Place Devices

1. Open Cisco Packet Tracer.
2. From the bottom device panel, select the End Devices category.
3. Drag three PCs onto the workspace. Label them PC0, PC1, and PC2.
4. From the Network Devices category, select Switches.
5. Drag one Cisco 2960 switch onto the workspace. Place it in the center.

#### Step 2: Connect the Devices

1. In the bottom toolbar, click the Connections category (lightning bolt icon).
2. Select the straight-through copper cable (solid line).
3. Click PC0, select FastEthernet0, then click the switch and select any available FastEthernet port (e.g., Fa0/1).
4. Repeat for PC1 (connect to Fa0/2) and PC2 (connect to Fa0/3).
5. Observe that after a few seconds, all link lights turn green, indicating a successful Layer 1 physical connection.

#### Step 3: Assign Static IP Addresses

1. Click on PC0 to open its configuration window.
2. Click the Desktop tab, then click IP Configuration.
3. Select Static, then enter:
   - IP Address: 192.168.1.10
   - Subnet Mask: 255.255.255.0
   - Default Gateway: (leave blank for now)
4. Close the window.
5. Repeat for PC1:
   - IP Address: 192.168.1.20
   - Subnet Mask: 255.255.255.0
6. Repeat for PC2:
   - IP Address: 192.168.1.30
   - Subnet Mask: 255.255.255.0

#### Step 4: Test Connectivity with Ping

1. Click on PC0, go to the Desktop tab, and click Command Prompt.
2. Type the following command and press Enter:

   `ping 192.168.1.20`

3. You should see four successful replies from 192.168.1.20 with round-trip times.
4. Now ping PC2:

   `ping 192.168.1.30`

5. Record your results in the table below:

**Lab Part 1 Results Table:**

| Source | Destination IP | Packets Sent | Packets Received | % Success |
|--------|---------------|--------------|------------------|-----------|
| PC0    | 192.168.1.20  |              |                  |           |
| PC0    | 192.168.1.30  |              |                  |           |

6. Take a screenshot showing the successful ping output in the PC0 Command Prompt window.

> **Troubleshooting Note:** If ping fails, verify that both PCs are using the same subnet mask (255.255.255.0) and that the last octet of each IP address is unique. Also confirm the switch port link lights are green.

---

### Part 2: OSI Layer Observation Using Simulation Mode

**Objective:** Use Packet Tracer Simulation Mode to inspect the PDU headers added at each OSI layer during a ping transmission.

#### Step 1: Switch to Simulation Mode

1. In the bottom right of the Packet Tracer window, locate the mode toggle. It reads "Realtime." Click it to switch to "Simulation."
2. In the Simulation Panel on the right, ensure ICMP is checked in the Event List Filters. If no filters are shown, click "Show All/None" and then check only ICMP.

#### Step 2: Generate a Ping in Simulation Mode

1. Click on PC0 and open the Command Prompt (Desktop tab).
2. Type `ping 192.168.1.20` and press Enter.
3. Switch focus back to the main Packet Tracer workspace. You will see a small ICMP packet icon appear near PC0, waiting for you to step through the simulation.

#### Step 3: Step Through the Simulation

1. Click the Play button once in the Simulation Panel to advance one step.
2. Click the envelope icon (PDU) that appears on the topology diagram. A PDU Information window opens.
3. In the PDU Information window, click the Outbound PDU Details tab.
4. Answer the following questions in your lab report:

**Simulation Observation Questions:**

**Question A:** In the Outbound PDU Details, find the Ethernet II frame header. What is the value of the Destination MAC Address field for the first ping from PC0? (Hint: it may initially show as a broadcast FF:FF:FF:FF:FF:FF for ARP.)

**Question B:** Find the IP header section. What are the Source IP and Destination IP address values in this packet? Which OSI layer corresponds to these fields?

**Question C:** Find the ICMP section. What type value is shown? (Type 8 = Echo Request, Type 0 = Echo Reply.) Which OSI layer does ICMP operate at?

**Question D:** Based on your observations, list the headers present in the PDU from outermost to innermost (Layer 2 to Layer 7 application). This demonstrates encapsulation.

#### Step 4: Observe the Return Path

1. Continue stepping through the simulation using the Play (one step) button.
2. Observe the packet traveling from PC0 to the switch, then from the switch to PC1.
3. When the packet arrives at PC1, observe that the destination MAC address now matches PC1's MAC address (the switch replaced the broadcast ARP response with a unicast address).
4. Take a screenshot showing the PDU Information window with the IP header fields visible.

---

### Deliverables

Submit the following to the Canvas assignment dropbox:

**Deliverable 1 (20 points):** A screenshot of the Packet Tracer workspace showing the completed star topology with green link lights on all three PCs.

**Deliverable 2 (30 points):** A screenshot showing successful ping output from PC0 to both PC1 and PC2 in the Command Prompt window.

**Deliverable 3 (30 points):** A screenshot of the PDU Information window in Simulation Mode showing the Outbound PDU Details with the Ethernet, IP, and ICMP layers visible.

**Deliverable 4 (20 points):** A typed summary (100–150 words) answering Simulation Observation Questions A through D. Submit this as a text entry in the Canvas assignment or as a separate Word/PDF document.

---

### Grading Rubric

| Deliverable | Points | Full Credit Criteria |
|-------------|--------|----------------------|
| Star topology screenshot | 20 | All 3 PCs and 1 switch visible, all link lights green, devices labeled |
| Successful ping screenshot | 30 | Ping output shows 4/4 packets received for both target IPs |
| PDU Information screenshot | 30 | Window clearly shows Ethernet, IP, and ICMP header fields |
| Written summary | 20 | All 4 questions answered with accurate OSI layer references |
| **Total** | **100** | |

---

### Common Issues and Fixes

**Issue:** Ping shows "Request timed out."

**Fix:** Check IP addresses and subnet masks on all PCs. Ensure all are in the 192.168.1.0/24 range with mask 255.255.255.0. Confirm switch port link lights are green.

**Issue:** Simulation Mode shows no ICMP events.

**Fix:** In the Event List Filters, click "Edit Filters" and ensure ICMP is checked. Then re-run the ping.

**Issue:** PDU information window shows only Layer 1 and 2.

**Fix:** Ensure you click the envelope icon that appears after the ARP exchange completes. The first event may be ARP (Layer 2 only). Wait for the ICMP echo request event.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
