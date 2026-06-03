# Lab: Module 13 — Unified Communications and Collaboration

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Lab Overview

This lab uses Cisco Packet Tracer to configure a VoIP network with IP phones, a call manager (CUCM simulation), voice VLANs, and QoS markings. You will also perform bandwidth calculations and analyze VoIP quality metrics. Part 4 uses Wireshark to capture and inspect RTP traffic characteristics.

**Estimated Time:** 90–120 minutes

**Required Tools:**

- Cisco Packet Tracer 8.x (free — netacad.com)
- Wireshark 4.x (free — wireshark.org) with a sample RTP capture file (provided or downloadable from wireshark.org/docs/wsug_html_chunked/AppTools.html)
- Calculator or spreadsheet for bandwidth calculations

---

## Part 1: VoIP Network Build in Packet Tracer

### Part 1 Objective

Configure a small VoIP network with IP phones, a router acting as CUCM, voice VLANs, and QoS-enabled switches. Verify that IP phones register and calls complete.

### Step 1: Build the Topology

Place the following in the Packet Tracer logical workspace:

- One 2811 Router (acts as CUCM/Call Manager)
- Two 2960 switches (Switch1 — Floor 1, Switch2 — Floor 2)
- Four Cisco IP Phones (7960 model) — two connected to each switch
- Two PCs — one connected to each switch via the phone's built-in switch port

Connect devices:

- Router FastEthernet0/0 → Switch1 (trunk port)
- Switch1 uplink → Switch2 (trunk port)
- IP Phones connect to switch access ports
- PCs connect to phone pass-through ports

### Step 2: Configure VLANs on Switches

On both switches, create two VLANs:

- VLAN 10 — name: DATA
- VLAN 20 — name: VOICE

Configure access ports for the IP phones:

```bash
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 20
 spanning-tree portfast
```

Repeat for all phone-connected ports. Configure trunk ports between switches and toward the router with both VLANs allowed.

### Step 3: Configure the Router as Call Manager

On the 2811 router, configure sub-interfaces for each VLAN:

```bash
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0

interface FastEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
```

Enable DHCP on the router to assign IPs and provide CUCM Option 150 (TFTP server address) to the phones:

```bash
ip dhcp pool DATA
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8

ip dhcp pool VOICE
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 option 150 ip 192.168.20.1

ip dhcp excluded-address 192.168.10.1 192.168.10.10
ip dhcp excluded-address 192.168.20.1 192.168.20.10
```

Configure Telephony Service (Packet Tracer CUCM simulation):

```bash
telephony-service
 max-ephones 4
 max-dn 4
 ip source-address 192.168.20.1 port 2000
 auto assign 1 to 4

ephone-dn 1
 number 1001

ephone-dn 2
 number 1002

ephone-dn 3
 number 1003

ephone-dn 4
 number 1004
```

### Step 4: Verify Phone Registration

After the phones receive DHCP addresses and contact the CUCM, they should display their assigned extension numbers. Verify by checking each phone's display.

From Phone 1001, dial Phone 1003 — a call should complete across the inter-switch trunk.

### Checkpoint 1

Screenshot each IP phone showing its assigned extension. Screenshot a successful call in progress between Phone 1001 and Phone 1003.

---

## Part 2: QoS Configuration

### Part 2 Objective

Configure DSCP marking and queuing policies on the router to prioritize voice traffic.

### Step 5: Configure QoS Policy

Create a class map to identify voice traffic (from VLAN 20):

```bash
class-map match-any VOICE-TRAFFIC
 match ip dscp ef

class-map match-any SIGNALING
 match ip dscp cs3
```

Create a policy map with LLQ for voice:

```bash
policy-map VOIP-QOS
 class VOICE-TRAFFIC
  priority 512
 class SIGNALING
  bandwidth 64
 class class-default
  fair-queue
```

Apply the policy to the WAN-facing interface (in this lab, apply to the FastEthernet0/0 interface):

```bash
interface FastEthernet0/0
 service-policy output VOIP-QOS
```

### Step 6: Verify QoS Policy

Use `show policy-map interface FastEthernet0/0` to verify the policy is active. During an active call, observe the packet counters for the VOICE-TRAFFIC class increment.

### Checkpoint 2

Screenshot the `show policy-map interface` output showing the VOIP-QOS policy applied and active packet counters.

---

## Part 3: Bandwidth Calculations

### Part 3 Objective

Calculate VoIP bandwidth requirements for several deployment scenarios.

### Step 7: Bandwidth Calculation Exercises

Complete the following calculations in your lab report. Show all work.

Scenario A — Branch Office Sizing (G.729):

- 35 concurrent calls using G.729 codec
- Packetization: 20 ms
- Per-call bandwidth with overhead: 31 Kbps
- Add 20% overhead buffer for signaling and burst

Calculate: (a) minimum raw voice bandwidth, (b) total with buffer, (c) can this fit on a T1 (1.544 Mbps) alongside 500 Kbps of data traffic?

Scenario B — Corporate HQ (G.711):

- 150 concurrent calls using G.711 codec
- Per-call bandwidth with overhead: 87 Kbps
- WAN link available: 50 Mbps
- CAC limit: 80% of link reserved for non-voice traffic

Calculate: (a) total voice bandwidth required, (b) voice bandwidth as a percentage of the 50 Mbps link, (c) what is the maximum additional concurrent calls the remaining link capacity can support?

Scenario C — Video Conferencing:

- 20 simultaneous HD video conference sessions
- Each session: 3 Mbps bidirectional
- Available WAN bandwidth: 200 Mbps
- Voice calls running simultaneously: 100 × G.711

Calculate: (a) total video bandwidth, (b) total voice bandwidth, (c) combined utilization as a percentage of 200 Mbps, (d) recommended DSCP markings for each traffic type.

### Checkpoint 3

Include completed calculations and recommendations in the lab report.

---

## Part 4: RTP Traffic Analysis with Wireshark

### Part 4 Objective

Analyze a pre-captured RTP stream to identify VoIP quality metrics and packet characteristics.

### Step 8: Open a RTP Capture

Download a sample VoIP PCAP file from the Wireshark sample captures page (wiki.wireshark.org/SampleCaptures — search for "SIP" or "VoIP"). Alternatively, use any VoIP PCAP provided by your instructor.

Open the file in Wireshark.

### Step 9: Analyze the RTP Stream

1. Apply the filter `rtp` to isolate RTP packets.
2. Navigate to Telephony > RTP > RTP Streams to view the RTP stream summary.
3. Select the audio stream and click Analyze.

Record the following from the RTP stream analysis:

- Source IP and port
- Destination IP and port
- Payload type (codec identifier)
- Total packets in stream
- Packet loss percentage
- Maximum delta (jitter proxy)
- Mean jitter

1. Apply the filter `sip` to view SIP signaling packets.
2. Identify the INVITE, 180 Ringing, 200 OK, ACK, and BYE messages.
3. Examine the SDP body in the INVITE — identify the offered codecs and the proposed RTP port.

### Step 10: Quality Assessment

Using the values you recorded, answer these questions in your lab report:

- Does the packet loss percentage meet the acceptable threshold for voice (under 1%)?
- Does the jitter value meet the acceptable threshold (under 30 ms)?
- Based on the payload type number, what codec is in use?
- What SIP method does the caller use to end the call?

### Checkpoint 4

Screenshot the Wireshark RTP stream analysis window showing the metrics. Screenshot one SIP INVITE packet with the SDP body expanded showing codec list and RTP port.

---

## Lab Report Requirements

Submit a PDF report containing:

1. Checkpoint 1: Phone registration and active call screenshots.
2. Checkpoint 2: QoS policy verification output.
3. Checkpoint 3: All bandwidth calculations with work shown and final recommendations.
4. Checkpoint 4: RTP analysis screenshot and written answers to quality assessment questions.
5. Reflection (150–200 words): Why is UDP used instead of TCP for RTP voice transport? What happens to call quality if packet loss exceeds 5%? How does the jitter buffer help, and what is its limitation?

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Phone registration and call screenshots | 20 |
| Part 2 — QoS policy configuration and verification | 20 |
| Part 3 — Bandwidth calculations (all three scenarios) | 25 |
| Part 4 — Wireshark RTP analysis and quality assessment | 25 |
| Reflection paragraph | 10 |
| **Total** | **100** |
