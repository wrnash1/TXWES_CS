# Video Script: Module 13 — Unified Communications and Collaboration (Part 2 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

## Introduction

Welcome back to Part 2 of Module 13. In Part 1 we covered VoIP fundamentals, codecs, SIP architecture and call flow, H.323, and RTP. Now we focus on what the network administrator must do to ensure voice and video calls actually work well — Quality of Service, jitter buffers, the key performance metrics the exam tests, and practical UC platform considerations.

---

## Section 1: Why QoS Is Critical for Voice and Video

When voice and video packets share network infrastructure with ordinary data traffic, they face a fundamental problem: other traffic doesn't care about delay. A large file transfer doesn't notice if its packets are delayed 200 milliseconds. A conversation does.

The human ear and brain are remarkably sensitive to inconsistent delay. Even a call with perfect audio quality on average will feel choppy and unnatural if packets arrive at inconsistent intervals.

This is why network engineers implement Quality of Service — QoS — mechanisms to give voice and video traffic preferential treatment. QoS does not add bandwidth. Instead, it manages how existing bandwidth is shared, ensuring that real-time traffic always gets the queue position, forwarding priority, and bandwidth guarantee it needs.

---

## Section 2: Key Performance Metrics for Real-Time Traffic

Before covering QoS mechanisms, you must understand the four performance metrics that matter for voice and video. The Network+ exam tests these definitions and their acceptable thresholds directly.

### Latency (Delay)

Latency is the time it takes for a packet to travel from source to destination. In a voice call, latency affects how natural the conversation feels.

The ITU-T G.114 standard recommends a one-way latency of no more than 150 ms for acceptable voice quality. Up to 400 ms is the absolute maximum — above 400 ms, callers start talking over each other constantly.

Sources of latency in VoIP:

- Propagation delay: Speed of light through the medium
- Serialization delay: Time to place bits on the wire
- Processing delay: Codec compression/decompression time
- Queuing delay: Time packets wait in router/switch queues
- Network delay: Routing through multiple hops

Of these, queuing delay is the one QoS can control.

### Jitter

Jitter is variation in latency — the inconsistency of packet arrival times. Even if average latency is acceptable, high jitter causes voice audio to sound choppy because packets arrive in bursts rather than at regular intervals.

Acceptable jitter for voice: under 30 ms.

Jitter is addressed by the jitter buffer at the receiving endpoint (covered shortly).

### Packet Loss

Packet loss occurs when packets are dropped — typically due to congestion in router queues. UDP does not retransmit lost packets, so lost voice packets result in audio dropouts.

Acceptable packet loss for voice: under 1%.

At higher loss rates, voice quality degrades noticeably. VoIP codecs use concealment algorithms to hide brief losses, but sustained packet loss degrades calls severely.

### Bandwidth

Voice calls require a consistent, reserved amount of bandwidth for the duration of the call. If bandwidth is not available, packets get delayed or dropped — increasing latency and packet loss.

Know the codec bandwidth requirements:

- G.711: approximately 87 Kbps per call (including IP/UDP/RTP overhead at 20 ms)
- G.729: approximately 31 Kbps per call (including overhead)
- HD video (720p): approximately 1.5–3 Mbps per stream
- HD video (1080p): approximately 3–6 Mbps per stream

---

## Section 3: Jitter Buffers

The jitter buffer is a component in VoIP endpoints and media gateways that compensates for variable packet arrival times.

How it works: incoming RTP packets are held briefly in a buffer before being played out. The buffer smooths out arrival-time variations — if packets arrive in a burst, the buffer absorbs them; if packets arrive late, the buffer provides continuity.

Jitter buffer trade-off: larger buffers absorb more jitter but add more delay. Smaller buffers minimize delay but may not compensate for high jitter.

Most modern endpoints use adaptive jitter buffers that dynamically adjust the buffer depth based on observed network conditions — growing when jitter increases, shrinking when conditions improve.

---

## Section 4: QoS Mechanisms

Now let us cover the actual QoS mechanisms. These are testable on the Network+ exam.

### Packet Marking — DSCP

Differentiated Services Code Point (DSCP) is the primary QoS marking mechanism for IP networks. DSCP uses the 6-bit DSCP field in the IP header's Type of Service (ToS) byte to mark packets with their forwarding class.

Key DSCP values:

- **EF (Expedited Forwarding) — DSCP 46 (101110)**: The highest priority class. Used for voice RTP media. Guarantees low latency, low jitter, low loss. Voice packets should always be marked EF.
- **AF41, AF42, AF43 (Assured Forwarding)**: Used for video conferencing. AF41 has highest drop preference within the AF4 class.
- **CS3 (Class Selector 3)**: Used for call signaling (SIP, H.225).
- **BE (Best Effort) — DSCP 0**: Default. No special treatment. Ordinary data traffic.

DSCP is a per-hop behavior — each router and switch in the path must be configured to honor DSCP markings and apply appropriate scheduling and queuing policies.

### Layer 2 Marking — CoS

Class of Service (CoS) is the Layer 2 QoS marking mechanism for Ethernet. It uses the 3-bit Priority Code Point (PCP) field in the 802.1Q VLAN tag header.

CoS values range from 0 (lowest) to 7 (highest):

- CoS 5: Voice RTP
- CoS 4: Video conferencing
- CoS 3: Call signaling
- CoS 0: Best-effort data

CoS markings are used within switched LAN segments. At Layer 3 boundaries (routers), CoS is typically mapped to DSCP and vice versa.

### Traffic Classification

Before you can prioritize traffic, you must identify it. Classification methods:

- **Port-based**: Classify based on UDP/TCP port numbers. SIP typically uses UDP port 5060. RTP uses dynamically assigned UDP ports in the range 16384–32767 (Cisco) or 1024–65535 (varies by vendor).
- **DSCP-based**: Trust incoming DSCP markings from endpoints.
- **Deep Packet Inspection (DPI)**: Inspect application-layer content to identify traffic — used when port-based classification is insufficient.
- **NBAR (Network-Based Application Recognition)**: Cisco proprietary DPI classification engine.

### Queuing Mechanisms

After classification and marking, queuing determines how packets are scheduled for transmission on congested interfaces.

- **Priority Queuing (PQ)**: Strict priority — higher-priority queues are always served before lower-priority queues. Voice gets absolute priority. Risk: lower-priority queues can starve.
- **Low Latency Queuing (LLQ)**: Cisco's recommended mechanism for VoIP. Combines strict priority for voice with Class-Based Weighted Fair Queuing (CBWFQ) for other traffic classes. Voice gets a dedicated, policed bandwidth allocation; other classes share remaining bandwidth proportionally.
- **Weighted Fair Queuing (WFQ)**: Allocates bandwidth proportionally based on weights. No strict priority.
- **FIFO (First In, First Out)**: No differentiation — all packets served in order received. Default on high-speed interfaces. Insufficient for voice.

For the exam: LLQ is the recommended QoS queuing strategy for networks with VoIP traffic.

### Traffic Shaping and Policing

- **Traffic shaping**: Delays excess traffic by buffering packets until the rate falls within the defined limit. Smooths bursts. Introduces delay but no packet drop.
- **Traffic policing**: Drops or re-marks packets that exceed the defined rate. Immediate — no buffering. Causes packet loss for bursts.

Shaping is preferred for data traffic. Policing is appropriate for enforcing SLAs at network edges.

### Call Admission Control

Call Admission Control (CAC) prevents oversubscription of WAN bandwidth by voice calls. When a new call would exceed the configured voice bandwidth limit, CAC rejects the call with a busy signal rather than allowing the call and degrading quality for all existing calls.

CAC is configured on IP PBX systems and WAN edge routers. Without CAC, a single congested WAN link can degrade call quality for all concurrent calls simultaneously.

---

## Section 5: VoIP Bandwidth Planning

To plan bandwidth for VoIP, use this formula:

Total VoIP bandwidth = Number of concurrent calls × Bandwidth per call (including overhead)

Example:
A branch office makes 50 concurrent calls using G.729:

50 × 31 Kbps = 1,550 Kbps = approximately 1.55 Mbps

This assumes bidirectional calls — you need 1.55 Mbps in each direction.

Add overhead for signaling traffic (SIP messages): typically 5–10% of voice bandwidth.

Add overhead for codec variation and burst: typically 20% buffer.

Final planned bandwidth: 1,550 Kbps × 1.25 = approximately 1.94 Mbps. Round up to 2 Mbps reserved for voice.

---

## Section 6: UC Platform Network Design

### Voice VLAN

Best practice is to place VoIP phones on a dedicated Voice VLAN, separate from the data VLAN. Benefits:

- QoS marking can be applied consistently to all voice VLAN traffic
- Security isolation — voice traffic is not on the same broadcast domain as user data
- Simplifies troubleshooting — voice traffic is identifiable by VLAN

Most enterprise IP phones support "inline VLAN" — the phone connects to a switch port configured for a data VLAN (for an attached PC) and a voice VLAN simultaneously. The phone tags its own traffic with the voice VLAN ID.

### Network Address Translation Issues

NAT is problematic for SIP and H.323 because VoIP signaling messages embed IP addresses in the application payload (SDP bodies, H.323 header fields). NAT changes the IP header but does not update the embedded application-layer addresses — causing the media stream to be sent to the wrong address.

Solutions:

- **ALG (Application Layer Gateway)**: NAT device inspects SIP/H.323 packets and rewrites embedded addresses. Included in most routers but can be unreliable.
- **STUN (Session Traversal Utilities for NAT)**: Client-side mechanism to discover external IP address and port. Used heavily in WebRTC applications.
- **Session Border Controller (SBC)**: Enterprise-grade device that handles NAT traversal, security, and protocol normalization for SIP trunks.

### Firewall Considerations

SIP and H.323 use dynamically negotiated UDP ports for RTP media. Traditional stateless ACLs cannot handle this well — you would need to open a wide range of UDP ports, which is a security risk.

Solutions:

- **Stateful inspection**: The firewall tracks SIP signaling and automatically opens the negotiated RTP port pairs.
- **Session Border Controller**: Terminates SIP sessions at the enterprise edge, normalizing media ports.
- **Application Layer Gateway**: Built into many enterprise firewalls.

---

## Summary of Part 2

Key points from Part 2:

- Latency, jitter, packet loss, and bandwidth are the four metrics that define VoIP/video quality. Acceptable thresholds: latency under 150 ms, jitter under 30 ms, packet loss under 1%.
- Jitter buffers smooth out variable packet arrival at the receiver — adaptive jitter buffers adjust dynamically.
- DSCP is the Layer 3 QoS marking field. EF (DSCP 46) is used for voice RTP. CoS is the Layer 2 marking in 802.1Q headers.
- LLQ is the recommended queuing mechanism for VoIP — strict priority for voice, CBWFQ for other classes.
- CAC prevents bandwidth oversubscription by blocking new calls when the limit is reached.
- Voice VLANs isolate voice traffic. NAT and firewalls require special handling (ALG, STUN, SBC, stateful inspection).

Module 13 is complete. Complete the Reading Guide, Lab, Quiz, and Discussion to reinforce these concepts. Module 14 covers the CompTIA Network+ troubleshooting methodology and hardware troubleshooting.
