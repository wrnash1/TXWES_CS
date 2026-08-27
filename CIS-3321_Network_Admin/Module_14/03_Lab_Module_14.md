# Lab: Module 14 — Network Troubleshooting Methodology

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Lab Overview

This lab practices the CompTIA seven-step troubleshooting methodology using Cisco Packet Tracer to diagnose pre-configured network faults, and uses Windows or Linux commands to practice real diagnostic workflows. You will document your troubleshooting process following the seven-step model for each scenario — the process documentation is as important as finding the fix.

**Estimated Time:** 90–120 minutes

**Required Tools:**

- Cisco Packet Tracer 8.x (free — netacad.com)
- Windows or Linux terminal (commands built-in to OS)
- Lab report template (your own document with the seven-step headers)

---

## Instructions

For each lab scenario, complete a seven-step troubleshooting worksheet documenting your process:

1. Problem statement (what you identified)
2. Theory of probable cause (your hypotheses ranked most to least likely)
3. Test results (what commands or checks you ran and what they showed)
4. Plan of action (specific fix you will apply)
5. Implementation (steps taken)
6. Verification (how you confirmed the fix worked)
7. Documentation summary (one paragraph describing the incident)

---

## Part 1: Packet Tracer Fault Isolation — Layer 1 and Layer 2

### Part 1 Objective

Diagnose and resolve physical and switching layer problems in a pre-built topology.

### Step 1: Build the Fault Topology

Build the following topology in Packet Tracer:

- One 2960 switch
- Four PCs (PC0–PC3)
- Connect all four PCs to the switch on FastEthernet0/1 through FastEthernet0/4

Configure the PCs with static IPs:

- PC0: 192.168.1.10 / 255.255.255.0 / gateway 192.168.1.1
- PC1: 192.168.1.20 / 255.255.255.0 / gateway 192.168.1.1
- PC2: 192.168.1.30 / 255.255.255.0 / gateway 192.168.1.1
- PC3: 192.168.1.40 / 255.255.255.0 / gateway 192.168.1.1

Verify all four PCs can ping each other.

### Step 2: Introduce Fault 1 — VLAN Isolation

On the switch, move PC2's port to VLAN 10 and PC3's port to VLAN 20 (all other ports remain on default VLAN 1):

```bash
interface FastEthernet0/3
 switchport access vlan 10

interface FastEthernet0/4
 switchport access vlan 20
```

Now test connectivity:

- PC0 pings PC1: should succeed (both VLAN 1)
- PC0 pings PC2: should fail (different VLAN)
- PC0 pings PC3: should fail (different VLAN)
- PC2 pings PC3: should fail (different VLANs)

Apply the seven-step worksheet:

- In Step 1, document the exact symptoms (which pings fail, which succeed).
- In Step 2, list your top hypothesis before checking the switch.
- In Step 3, check `show vlan brief` to confirm your theory.
- In Steps 4–5, correct PC2 and PC3 back to VLAN 1.
- In Step 6, re-verify all four pings succeed.

### Step 3: Introduce Fault 2 — IP Misconfiguration

Change PC1's IP address to 192.168.2.20 (wrong subnet) without changing the gateway.

Test:

- PC0 pings PC1: should fail
- PC1 pings gateway 192.168.1.1: should fail (different subnet)

Apply the seven-step worksheet:

- In Step 3, use `ipconfig` on PC1 and PC0 to identify the mismatch.
- Document the specific Layer 3 cause.

### Checkpoint 1

Screenshot: `show vlan brief` from Fault 1 (before fix). Screenshot: `ipconfig` from PC1 showing wrong subnet in Fault 2. Submit both seven-step worksheets.

---

## Part 2: Packet Tracer Fault Isolation — Layer 3

### Part 2 Objective

Diagnose routing problems using diagnostic commands.

### Step 4: Build a Multi-Router Topology

Place three routers (R1, R2, R3) and one PC behind each router:

- R1 LAN: 10.1.1.0/24, PC1 = 10.1.1.10
- R2 LAN: 10.2.2.0/24, PC2 = 10.2.2.10
- R3 LAN: 10.3.3.0/24, PC3 = 10.3.3.10
- R1–R2 link: 172.16.1.0/30
- R2–R3 link: 172.16.2.0/30

Configure static routes on all three routers for full connectivity. Verify that PC1 can ping PC3.

### Step 5: Introduce Fault 3 — Missing Route

Remove the static route from R1 that points toward R3's network:

```bash
no ip route 10.3.3.0 255.255.255.0 172.16.1.2
```

Symptom: PC1 cannot reach PC3. PC1 can still reach PC2.

Apply the seven-step worksheet. In Step 3, use these commands:

```bash
show ip route
tracert 10.3.3.10
```

The traceroute from PC1 will show the path dying after R1 or R2 — identifying where the missing route is. Document which router is missing the route and for which destination network.

### Step 6: Introduce Fault 4 — Wrong Default Gateway

After restoring the missing route, change PC2's default gateway to an incorrect address (e.g., 10.2.2.99 instead of 10.2.2.1).

Symptom: PC2 can ping devices on its own subnet (10.2.2.0/24) but cannot reach any other network.

Apply the seven-step worksheet. In Step 3, use `ipconfig` on PC2 and `ping 10.1.1.10` to confirm the fault pattern.

### Checkpoint 2

Screenshot: `show ip route` from R1 with missing route, and again after the fix. Screenshot: `ipconfig` from PC2 with wrong gateway. Submit both seven-step worksheets.

---

## Part 3: Command-Line Diagnostic Practice (Windows/Linux)

### Part 3 Objective

Practice the diagnostic commands from the module on your real host machine.

### Step 7: Document Your Host Network Configuration

Open a terminal or command prompt and run `ipconfig /all` (Windows) or `ip addr show && ip route` (Linux).

In your lab report, document:

- Your IP address and subnet mask
- Default gateway
- DNS server(s)
- DHCP server (Windows) or whether DHCP is in use
- MAC address of your primary interface

### Step 8: Test Reachability with Ping

Run the following pings and record results (latency and whether each succeeds):

- `ping 127.0.0.1` — loopback (tests local TCP/IP stack)
- `ping <your default gateway>` — tests Layer 1-3 to the gateway
- `ping 8.8.8.8` — tests internet reachability by IP
- `ping google.com` — tests DNS resolution and internet reachability

For any failed ping, describe at which layer the problem would be located.

### Step 9: Trace the Path

Run `tracert google.com` (Windows) or `traceroute google.com` (Linux). Record:

- Number of hops to google.com
- Latency at each of the first three hops
- Which hop (if any) shows high latency or packet loss

### Step 10: DNS Test

Run `nslookup google.com` and `nslookup texas-wesleyan.edu`. Record:

- The resolved IP address for each
- Which DNS server responded
- If either fails, document the error message

### Step 11: ARP Cache

Run `arp -a`. Record the MAC address of your default gateway. This confirms Layer 2 ARP resolution is working between your host and the gateway.

### Checkpoint 3

Screenshots of all command outputs from Steps 7–11, embedded in the lab report.

---

## Part 4: Troubleshooting Scenario Written Exercise

### Part 4 Objective

Apply the seven-step methodology to a written scenario without using Packet Tracer.

### Step 12: Analyze the Scenario

Read the following scenario and complete a full seven-step troubleshooting worksheet for it:

Scenario: A receptionist at a law firm calls the help desk and says she cannot send or receive emails. She says "the internet has been broken since this morning." You remote into her workstation and observe: she can open websites by IP address (e.g., typing 8.8.8.8 into the browser shows Google's page). She cannot open any website by name. Outlook shows "Cannot connect to server — check network connection." Other employees in the office are working normally.

Complete all seven steps:

- Step 1: What is the specific, precise problem statement?
- Step 2: List three hypotheses in order of likelihood. Which OSI layer does each implicate?
- Step 3: What commands or checks would you run to test each hypothesis?
- Step 4: What is your plan of action once the cause is identified?
- Step 5: What is the fix?
- Step 6: How would you verify the problem is fully resolved?
- Step 7: Write a one-paragraph incident documentation summary.

### Checkpoint 4

Submit the completed seven-step worksheet for the written scenario.

---

## Lab Report Requirements

Submit a PDF containing:

1. Checkpoint 1: Both seven-step worksheets from Part 1 and required screenshots.
2. Checkpoint 2: Both seven-step worksheets from Part 2 and required screenshots.
3. Checkpoint 3: All command output screenshots from Part 3.
4. Checkpoint 4: Written scenario seven-step worksheet.
5. Reflection (150–200 words): Why is documenting each troubleshooting step (Step 7) important even for problems you resolve quickly? Describe one situation — real or hypothetical — where skipping documentation could cause a significant problem later.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — VLAN and IP fault worksheets + screenshots | 20 |
| Part 2 — Routing fault worksheets + screenshots | 20 |
| Part 3 — Command output screenshots and analysis | 20 |
| Part 4 — Written scenario seven-step worksheet | 30 |
| Reflection paragraph | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

These advanced steps extend the Module 14 lab with complex fault scenarios, advanced diagnostic command interpretation, and a structured escalation decision exercise.

### Challenge Step 1: Diagnose a Multi-Layer Fault Using `show` Commands

In Packet Tracer, introduce the following simultaneous faults into your existing topology (from Parts 1–2):

1. Set one switch port to half-duplex manually:
   ```
   interface FastEthernet0/3
    duplex half
   ```
2. Assign the wrong VLAN to one port:
   ```
   interface FastEthernet0/4
    switchport access vlan 99
   ```
   (VLAN 99 does not exist or has no IP routing.)
3. Remove the default gateway from one PC.

Now, without looking at the configurations you just applied, perform a systematic diagnosis from the affected PC:

1. Run `ipconfig` on the affected PC — record the full output.
2. Attempt to ping the default gateway — record the result.
3. Attempt to ping the DNS server — record the result.
4. On the switch, run `show interfaces FastEthernet0/3` — record the duplex and speed fields plus input error counts.
5. On the switch, run `show vlan brief` — identify any ports assigned to non-existent VLANs.
6. Apply the seven-step methodology: document your identification, hypothesis, test, and fix for each of the three faults.

**Challenge Question 1:** In a real enterprise network, these three faults (duplex mismatch, VLAN misconfiguration, missing gateway) could each cause different user symptoms. Match each fault to its most likely user symptom: (a) "I can't get to the internet but can reach local servers," (b) "The network is very slow," (c) "I can't reach anything on the network at all." Explain the diagnostic command that would confirm each fault before any configuration change is made.

### Challenge Step 2: OTDR Trace Interpretation Exercise

Review the following OTDR trace description and answer the analysis questions in your lab report:

An OTDR test was performed on a 500-meter single-mode fiber run between two buildings. The trace shows:

- 0–5 meters: High back-reflection spike (launch condition)
- 5–320 meters: Gradual uniform slope of −0.35 dB/km attenuation
- 320 meters: Sharp spike followed by a 3.2 dB loss event
- 320–490 meters: Gradual slope resumes at −0.35 dB/km
- 490 meters: End of fiber back-reflection

Answer the following in your lab report:

1. What does the high back-reflection spike at 0–5 meters represent, and is it expected?
2. What does the 3.2 dB loss event at 320 meters most likely indicate? List three possible physical causes at that location.
3. The fiber run is designed to support 10GBase-LR (10 Gbps, 1310 nm, maximum attenuation budget: 6.7 dB). Calculate the total attenuation from 5 meters to 490 meters including the 320-meter event. Does the link meet the power budget?
4. If the technician finds the 320-meter point is inside a conduit junction box, what should be physically inspected and in what order?

**Challenge Question 2:** What is the difference between back-reflection (Fresnel reflection) and insertion loss (attenuation) on an OTDR trace? Which type of event does each indicate, and how does a technician distinguish between a dirty connector and a physical break when both produce a loss event on the OTDR?

### Challenge Step 3: Escalation Decision Framework

A network technician encounters the following five trouble scenarios. For each scenario, decide whether to: (a) resolve independently, (b) escalate to Tier 2 network engineering, or (c) escalate to the carrier/vendor. Justify each decision.

1. A user's workstation is assigned 169.254.x.x — the DHCP server is reachable and the scope shows available addresses; the port shows up/up.
2. A T1 WAN circuit between HQ and Branch-A has been down for 20 minutes; the CSU/DSU shows no signal from the carrier; a ticket was opened with the carrier 10 minutes ago.
3. An MPLS VPN route is missing from the routing table; the PE router configuration looks correct; the carrier's NOC says the circuit is up on their end.
4. A switch port shows "err-disabled" status — Port Security has shut it down due to a MAC violation; the technician does not have change authorization for production switches.
5. Six concurrent users are reporting intermittent packet loss; Wireshark shows TCP retransmissions; the WAN interface utilization shows 98% for the past 30 minutes.

**Challenge Question 3:** For scenario 5 (98% WAN utilization causing packet loss), describe the complete escalation documentation a Tier 1 technician should prepare before handing off to Tier 2. What specific data (commands, outputs, timestamps, user impact) should be captured, and why does thorough documentation at handoff reduce total resolution time?

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
