# Reading Guide: Module 13 — Unified Communications and Collaboration

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Overview

This reading guide supports Module 13 video lectures and prepares you for the quiz and the CompTIA Network+ N10-008 exam. UC and VoIP topics appear in Domain 1 (Networking Concepts) and Domain 2 (Infrastructure). Pay particular attention to QoS terminology, codec bandwidth values, and SIP call flow — these are frequently tested.

**Estimated Reading Time:** 55–70 minutes

---

## Part 1: Unified Communications Foundations

### 1.1 UC Platform Components

A Unified Communications platform integrates multiple real-time communication services:

- Voice calling (VoIP)
- Video conferencing
- Instant messaging and presence
- Voicemail and unified messaging
- Web/desktop collaboration and screen sharing
- Mobile integration

Common enterprise UC platforms:

- Microsoft Teams (cloud-based)
- Cisco Unified Communications Manager (CUCM) — on-premises IP PBX
- Avaya Aura — enterprise telephony
- Zoom Phone — cloud UCaaS
- RingCentral — cloud UCaaS

### 1.2 VoIP Codec Reference

| Codec | Bandwidth (payload only) | Bandwidth with overhead (20 ms) | Quality | Notes |
|---|---|---|---|---|
| G.711 | 64 Kbps | ~87 Kbps | Toll-quality | North America: G.711u; Europe: G.711a |
| G.729 | 8 Kbps | ~24–31 Kbps | Good | Compressed; widely used for WAN |
| G.722 | 64 Kbps | ~87 Kbps | HD voice | Wideband; better frequency range than G.711 |
| G.726 | 16–40 Kbps | varies | Moderate | ADPCM compression |
| Opus | 6–510 Kbps | adaptive | Excellent | WebRTC, Zoom; adaptive bitrate |

Overhead calculation for G.711 at 20 ms packetization:

- Payload: 160 bytes (64 Kbps × 20 ms)
- RTP header: 12 bytes
- UDP header: 8 bytes
- IP header: 20 bytes
- Total: 200 bytes per packet × 50 packets/sec = 80,000 bytes/sec = 640 Kbps? No — recalculate: 200 bytes × 8 bits × 50 pps = 80,000 bps = 80 Kbps

Note: Different sources calculate overhead slightly differently based on framing. CompTIA exam uses approximately 87 Kbps for G.711 and 31 Kbps for G.729 per call including all headers.

---

## Part 2: SIP — Session Initiation Protocol

### 2.1 SIP Architecture Components

| Component | Function |
|---|---|
| User Agent (UA) | Endpoint — initiates or receives sessions (IP phone, softphone) |
| SIP Proxy | Routes SIP requests between UAs |
| SIP Registrar | Records UA location (IP/port) from REGISTER requests |
| Redirect Server | Returns contact address; client contacts destination directly |
| B2BUA | Acts as both UA client and server; typical IP PBX function |

### 2.2 SIP Methods

| Method | Purpose |
|---|---|
| REGISTER | UA registers current address with registrar |
| INVITE | Initiate a session |
| ACK | Confirm final response to INVITE |
| BYE | Terminate an established session |
| CANCEL | Cancel a pending INVITE (before answer) |
| OPTIONS | Query server/endpoint capabilities |
| REFER | Transfer a call to another party |
| NOTIFY | Deliver event notifications (voicemail, presence) |

### 2.3 SIP Response Codes

| Range | Class | Examples |
|---|---|---|
| 1xx | Provisional | 100 Trying, 180 Ringing, 183 Session Progress |
| 2xx | Success | 200 OK |
| 3xx | Redirection | 301 Moved Permanently, 302 Moved Temporarily |
| 4xx | Client error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 486 Busy Here |
| 5xx | Server error | 500 Internal Server Error, 503 Service Unavailable |
| 6xx | Global failure | 600 Busy Everywhere, 603 Decline |

### 2.4 SIP Call Flow

A basic SIP call between two phones through a proxy:

1. Phone A → Proxy: INVITE (SDP with codec offer)
2. Proxy → Phone B: INVITE
3. Phone B → Proxy → Phone A: 100 Trying
4. Phone B → Proxy → Phone A: 180 Ringing (phone B rings)
5. Phone B answered → Phone B → Proxy → Phone A: 200 OK (SDP with codec answer)
6. Phone A → Phone B: ACK (three-way handshake complete)
7. RTP media flows directly: Phone A ↔ Phone B (bypasses proxy)
8. Call ends: Phone A (or B) → Proxy: BYE
9. Proxy → Phone B (or A): BYE
10. Phone B → Proxy → Phone A: 200 OK

Key exam point: RTP media typically flows directly between endpoints after signaling — it does not pass through the SIP proxy.

### 2.5 SDP — Session Description Protocol

SDP (Session Description Protocol) is carried inside SIP INVITE and 200 OK messages. It describes:

- Media type (audio, video)
- IP address and UDP port for RTP
- Supported codecs (in priority order)
- Packetization interval

The exchange of SDP between caller and callee is the codec negotiation — each party advertises what it supports and they agree on a common format.

---

## Part 3: H.323

### 3.1 H.323 Architecture

| Component | Function |
|---|---|
| Terminal | H.323 endpoint (IP phone, video endpoint) |
| Gateway | Translates H.323 to PSTN or other networks |
| Gatekeeper | Optional — provides address translation, admission control, bandwidth management |
| MCU (Multipoint Control Unit) | Enables multipoint audio/video conferences |

### 3.2 H.323 Protocol Suite

| Protocol | Function |
|---|---|
| H.225 | Call setup and signaling |
| H.245 | Capability exchange and media channel control |
| RAS | Registration, Admission, Status — between terminals and gatekeeper |
| RTP/RTCP | Media transport |
| H.235 | Security (authentication, encryption) |

### 3.3 H.323 vs. SIP Comparison

| Feature | H.323 | SIP |
|---|---|---|
| Standard body | ITU-T | IETF |
| Year introduced | 1996 | 1999 |
| Message encoding | Binary (ASN.1) | Text (UTF-8) |
| Architecture | Hierarchical, complex | Peer-to-peer capable, simpler |
| Firewall traversal | Difficult | Easier (still requires ALG or SBC) |
| Current status | Legacy (still deployed) | Dominant modern standard |

---

## Part 4: RTP and RTCP

### 4.1 RTP — Real-time Transport Protocol

RTP (RFC 3550) provides end-to-end delivery for real-time audio and video.

Key header fields:

- **Payload type (PT)**: Identifies the codec. Defined in RFC 3551.
- **Sequence number**: Sequential number for each packet — receiver detects gaps (packet loss) and reorders if needed.
- **Timestamp**: Media clock value — used for synchronization and jitter buffer operation.
- **SSRC**: Synchronization Source — unique identifier for the RTP stream source.

RTP runs over UDP — not TCP. Reliability is not needed because late retransmissions are useless for real-time media.

### 4.2 RTCP — RTP Control Protocol

RTCP provides quality monitoring feedback. It uses the RTP port + 1 (if RTP is on UDP 16384, RTCP is on UDP 16385).

RTCP report types:

- **SR (Sender Report)**: Statistics from the sender — packets sent, bytes sent, NTP timestamp.
- **RR (Receiver Report)**: Statistics from receivers — fraction lost, cumulative packets lost, jitter, last SR received.
- **SDES (Source Description)**: Describes source (SSRC, CNAME canonical name).
- **BYE**: Indicates end of participation.

RTCP data is used by network management systems and UC platforms to monitor call quality and detect issues.

---

## Part 5: QoS for Voice and Video

### 5.1 Voice and Video Performance Requirements

| Metric | Acceptable Threshold | Notes |
|---|---|---|
| One-way latency | Under 150 ms (ITU G.114) | Up to 400 ms is absolute maximum |
| Round-trip latency | Under 300 ms | Double the one-way value |
| Jitter | Under 30 ms | Addressed by jitter buffer |
| Packet loss | Under 1% | Concealment algorithms handle brief losses |

### 5.2 DSCP Markings for Voice and Video

| Traffic Type | DSCP Value | DSCP Name | PHB |
|---|---|---|---|
| Voice RTP | 46 (101110) | EF | Expedited Forwarding |
| Interactive video | 34 (100010) | AF41 | Assured Forwarding Class 4 |
| Call signaling (SIP) | 24 (011000) | CS3 | Class Selector 3 |
| Best-effort data | 0 | BE | Best Effort |
| Network management | 48 (110000) | CS6 | Class Selector 6 |

### 5.3 CoS — Class of Service (Layer 2)

CoS uses the 3-bit PCP field in the 802.1Q VLAN tag:

| CoS Value | Traffic Type |
|---|---|
| 7 | Network control |
| 6 | Internetwork control |
| 5 | Voice (EF equivalent) |
| 4 | Video conferencing |
| 3 | Critical applications / signaling |
| 2 | Excellent effort |
| 1 | Background |
| 0 | Best effort (default) |

### 5.4 Queuing Mechanisms

#### FIFO (First In, First Out)

No prioritization — all packets served in order received. Default for most interfaces. Unacceptable for voice on congested links.

#### Priority Queuing (PQ)

Four fixed priority queues (high, medium, normal, low). Higher queues always served first. Risk: lower queues can starve during heavy high-priority traffic.

#### Class-Based Weighted Fair Queuing (CBWFQ)

Multiple queues with minimum bandwidth guarantees per class. Proportional sharing of remaining bandwidth. No strict priority — voice still experiences variable queuing delay under congestion.

#### Low Latency Queuing (LLQ)

Combines strict priority queue for voice (policed to prevent starvation) with CBWFQ for other classes. The recommended Cisco mechanism for VoIP. Voice gets absolute priority up to the policed bandwidth limit; other classes share remaining bandwidth via CBWFQ.

### 5.5 Jitter Buffer

The jitter buffer holds incoming RTP packets briefly before playback to smooth arrival-time variation.

Types:

- **Static jitter buffer**: Fixed depth. Simple but wastes buffer on low-jitter networks or drops packets on high-jitter networks.
- **Adaptive jitter buffer**: Adjusts depth dynamically based on observed jitter. Minimizes added delay while absorbing network jitter. Used in most modern endpoints.

Trade-off: deeper buffer = better jitter absorption but higher latency. The buffer adds to total one-way delay.

### 5.6 Call Admission Control

CAC prevents voice quality degradation from oversubscription. When a new call would exceed the WAN voice bandwidth limit, CAC rejects the call with a busy signal.

Without CAC: 50 calls on a link sized for 30 calls = all 50 calls experience poor quality simultaneously.

With CAC: 30 calls succeed; calls 31–50 receive busy signal. The 30 active calls maintain acceptable quality.

CAC is typically configured on the IP PBX or SIP proxy, and optionally on WAN routers.

---

## Part 6: Network Design for VoIP and UC

### 6.1 Voice VLAN Design

Best practice: dedicated Voice VLAN separate from data VLAN.

Benefits:

- Consistent QoS marking for all voice traffic
- Layer 2 security isolation
- Simplified troubleshooting
- QoS policy applied by VLAN at the access switch

Typical access switch port configuration:

- Native VLAN (untagged): data VLAN for PC
- Voice VLAN (tagged with voice VLAN ID): VoIP phone traffic

### 6.2 NAT Traversal Issues

SIP and H.323 embed IP addresses in the application payload (SDP body). NAT rewrites IP headers but not payload — resulting in mismatched addresses for RTP streams.

Solutions:

- **ALG (Application Layer Gateway)**: NAT device inspects and rewrites SIP/H.323 payloads. Included in most routers but can cause issues with encrypted SIP.
- **STUN (Session Traversal Utilities for NAT)**: Client-side mechanism to discover external NAT mapping. Used in WebRTC.
- **TURN (Traversal Using Relays around NAT)**: Relay server provides media traversal when direct path is blocked.
- **ICE (Interactive Connectivity Establishment)**: Framework combining STUN and TURN to find best media path.
- **Session Border Controller (SBC)**: Enterprise-grade NAT traversal, security, and protocol normalization for SIP trunks.

### 6.3 Bandwidth Planning Formula

Total voice bandwidth = Concurrent calls × Per-call bandwidth (with overhead)

Example — G.711, 30 concurrent calls:

30 × 87 Kbps = 2,610 Kbps = 2.61 Mbps (each direction)

Add 20% buffer: 2.61 × 1.20 = 3.13 Mbps required per direction.

---

## Key Terms Glossary

- **ALG**: Application Layer Gateway — NAT helper for SIP/H.323.
- **B2BUA**: Back-to-Back User Agent — terminates and re-originates SIP sessions.
- **CAC**: Call Admission Control — prevents voice bandwidth oversubscription.
- **CoS**: Class of Service — Layer 2 QoS marking (802.1Q PCP field).
- **DSCP**: Differentiated Services Code Point — Layer 3 QoS marking in IP header.
- **EF**: Expedited Forwarding — DSCP 46; used for voice RTP.
- **G.711**: 64 Kbps uncompressed voice codec; toll-quality.
- **G.729**: 8 Kbps compressed voice codec; widely used for WAN.
- **Gatekeeper**: H.323 component providing address translation and admission control.
- **Jitter**: Variation in packet delay.
- **Jitter buffer**: Endpoint buffer that smooths variable packet arrival times.
- **LLQ**: Low Latency Queuing — strict priority for voice plus CBWFQ.
- **MCU**: Multipoint Control Unit — H.323 conference bridging.
- **RTP**: Real-time Transport Protocol — carries voice/video media over UDP.
- **RTCP**: RTP Control Protocol — quality monitoring feedback.
- **SBC**: Session Border Controller — SIP NAT traversal and security device.
- **SDP**: Session Description Protocol — codec and media parameter negotiation.
- **SIP**: Session Initiation Protocol — dominant VoIP signaling protocol.
- **STUN**: Session Traversal Utilities for NAT.
- **UC**: Unified Communications.
- **VoIP**: Voice over IP.

---

## Review Questions

1. What are the four network performance metrics critical for VoIP quality? State the acceptable threshold for each.

2. Calculate the WAN bandwidth required for 45 concurrent G.729 calls including overhead, plus a 20% buffer.

3. Describe the SIP call setup sequence from INVITE to the beginning of RTP media flow.

4. What is the difference between SIP and RTP in a VoIP call? Which handles signaling and which handles media?

5. Compare H.323 and SIP. Give two reasons why SIP has become the dominant modern standard.

6. What is DSCP EF and why is it used for voice RTP specifically?

7. Why is NAT problematic for VoIP, and what are three solutions?

8. What is Low Latency Queuing (LLQ) and why is it preferred over simple priority queuing for VoIP?

9. What is Call Admission Control and what problem does it solve?

10. Explain the trade-off involved in configuring a jitter buffer depth.
