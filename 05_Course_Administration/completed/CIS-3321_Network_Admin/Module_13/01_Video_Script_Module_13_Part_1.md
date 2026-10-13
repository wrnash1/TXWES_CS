# Video Script: Module 13 — Unified Communications and Collaboration (Part 1 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

## Introduction

Welcome to Module 13 of CIS-3321 Network Administration. I am Professor Nash. This module covers Unified Communications and Collaboration — the technologies that carry voice, video, and real-time data across IP networks.

If you have ever used Microsoft Teams, Zoom, or a VoIP desk phone at work, you have already been a consumer of the technologies we cover here. The question for network administrators is not whether to support these technologies, but how to support them well — because the network requirements for real-time communication are significantly different from those for ordinary data traffic.

Part 1 covers VoIP architecture, the SIP and H.323 protocols, and the specific network characteristics that real-time communication requires. Part 2 covers Quality of Service mechanisms, bandwidth planning, UC platforms, and practical design considerations.

This material maps to Domain 1 and Domain 2 of the CompTIA Network+ N10-008 exam.

---

## Section 1: What Is Unified Communications?

Unified Communications, or UC, is the integration of multiple communication services into a single coherent platform. Rather than having separate systems for voice calls, video meetings, instant messaging, voicemail, and email, a UC platform brings them together under one interface.

The "unified" aspect matters for the network because all of these services now traverse the same IP network infrastructure — the same switches, routers, and WAN links that carry file transfers and web browsing. This convergence creates both efficiency and complexity.

Common UC platform components:

- Voice over IP (VoIP) calling
- Video conferencing
- Instant messaging and presence (showing online/available/busy status)
- Voicemail with email integration (unified messaging)
- Web and desktop sharing (collaboration)
- Mobile integration (extending desk phone to smartphones)

Examples of UC platforms: Microsoft Teams, Cisco Unified Communications Manager (CUCM), Avaya Aura, Zoom Phone, RingCentral.

---

## Section 2: Voice over IP — Fundamentals

Voice over IP, or VoIP, transmits voice calls as digital data packets over an IP network rather than through a traditional circuit-switched telephone network (PSTN).

### How VoIP Works

In a traditional PSTN call, analog voice signals travel over dedicated copper circuits. VoIP replaces this with a digital process:

1. The analog voice signal from a microphone is digitized by an Analog-to-Digital Converter (ADC).
2. The digital audio is compressed by a voice codec (coder-decoder) to reduce bandwidth.
3. The compressed audio is packetized — broken into small packets — and sent across the IP network using the Real-time Transport Protocol (RTP).
4. At the receiving end, packets are reassembled, decoded, and converted back to analog audio by a Digital-to-Analog Converter (DAC).

This entire process introduces delay — called latency — and must happen fast enough that the conversation feels natural to both parties.

### VoIP Codecs

A codec compresses and decompresses audio. The choice of codec determines both audio quality and bandwidth consumption.

Common VoIP codecs:

- **G.711**: The most common codec. Provides toll-quality voice (PSTN-equivalent). Uncompressed — uses 64 Kbps per call. Two variants: G.711a (A-law, used in Europe) and G.711u (mu-law, used in North America and Japan).
- **G.729**: Compressed codec. Uses 8 Kbps per call — 8x more bandwidth-efficient than G.711. Audio quality is slightly lower but acceptable for most business calls. Widely used over WAN links where bandwidth is constrained.
- **G.722**: Wideband codec. Uses 64 Kbps but captures a broader frequency range than G.711, resulting in higher-definition audio — "HD voice." Used in modern UC endpoints.
- **Opus**: Modern, versatile open-source codec used in WebRTC, Zoom, and many modern UC platforms. Adapts bitrate dynamically from 6 Kbps to 510 Kbps.

### Bandwidth Per VoIP Call

The codec bandwidth is just the payload — you must also add protocol headers:

- RTP header: 12 bytes
- UDP header: 8 bytes
- IP header: 20 bytes
- Ethernet header: 14 bytes (Layer 2)

With G.711 (10 ms packetization interval, 80-byte payload), total per-packet size is approximately 134 bytes. With 100 packets per second (10 ms interval), that is approximately 107.2 Kbps including overhead — often rounded to 87.2 Kbps for planning at 20 ms intervals.

For exam purposes, remember: **G.711 = approximately 87 Kbps per call (with overhead at 20 ms)** and **G.729 = approximately 24–31 Kbps per call with overhead**.

---

## Section 3: SIP — Session Initiation Protocol

SIP is the dominant VoIP signaling protocol. The Network+ exam tests SIP heavily.

### What SIP Does

SIP is an application-layer signaling protocol defined in RFC 3261. It handles the establishment, modification, and termination of communication sessions. SIP is responsible for:

- Locating users (address resolution)
- Signaling call setup — "ring the phone"
- Negotiating call parameters — what codec to use, which port for media
- Tearing down calls — hanging up

SIP does not carry the actual voice audio — that is handled by RTP. SIP is the "signaling" protocol; RTP is the "media" protocol.

### SIP Architecture

SIP uses a client-server model with several key components:

- **SIP User Agent (UA)**: An endpoint that initiates or receives SIP sessions. A SIP phone, softphone application, or video conference endpoint is a UA.
- **SIP Proxy Server**: Routes SIP requests between UAs. Receives a REGISTER or INVITE and forwards it toward the destination.
- **SIP Registrar**: A server that accepts REGISTER requests from UAs and records their current location (IP address and port). Allows the proxy to find users.
- **SIP Redirect Server**: Responds to SIP requests with the contact address of the called party, redirecting the UA to contact that address directly.
- **Back-to-Back User Agent (B2BUA)**: Acts as both a UA client and server — terminates one SIP session and creates a new one. IP PBX systems typically function as B2BUAs.

### Key SIP Methods

SIP messages use request methods similar to HTTP:

- **REGISTER**: UA registers its current address with the registrar.
- **INVITE**: Initiate a call — "I want to establish a session with you."
- **ACK**: Acknowledges the final response to INVITE — completes the three-way handshake.
- **BYE**: Terminates an established session.
- **CANCEL**: Cancels a pending INVITE before it is answered.
- **OPTIONS**: Queries the capabilities of a SIP server or endpoint.

### SIP Response Codes

SIP uses numeric response codes modeled after HTTP:

- **1xx**: Provisional — 100 Trying, 180 Ringing
- **2xx**: Success — 200 OK
- **3xx**: Redirection — 302 Moved Temporarily
- **4xx**: Client error — 400 Bad Request, 401 Unauthorized, 486 Busy Here
- **5xx**: Server error — 503 Service Unavailable
- **6xx**: Global failure — 600 Busy Everywhere

### SIP Call Flow — Basic Example

1. Phone A sends INVITE to SIP Proxy.
2. Proxy sends INVITE to Phone B.
3. Phone B sends 180 Ringing back through proxy.
4. Phone B is answered — sends 200 OK.
5. Phone A sends ACK.
6. RTP media stream flows directly between Phone A and Phone B.
7. Either party sends BYE to terminate.
8. The other party responds 200 OK.

This pattern — INVITE / 180 Ringing / 200 OK / ACK — is tested directly on the Network+ exam.

### SDP — Session Description Protocol

When a SIP INVITE is sent, it carries an SDP (Session Description Protocol) body that describes the media parameters: what codecs are supported, the IP address and UDP port for RTP, and the media type. SDP negotiation ensures both endpoints agree on the audio format before the call begins.

---

## Section 4: H.323 — The Legacy Standard

H.323 is an older ITU-T standard for multimedia communication over packet networks. While largely replaced by SIP in modern deployments, it still exists in many enterprise voice systems and appears on the Network+ exam.

### H.323 Architecture

H.323 uses a hierarchical architecture with specific component names:

- **Terminal**: An H.323 endpoint (IP phone, video conference unit).
- **Gateway**: Translates between H.323 networks and other networks (such as PSTN). Critical for connecting VoIP to the traditional phone network.
- **Gatekeeper**: Optional but important component. Provides address translation, admission control, and bandwidth management. All H.323 calls can be routed through the gatekeeper.
- **Multipoint Control Unit (MCU)**: Enables multipoint conferences — bridges multiple H.323 endpoints into a conference call.

### H.323 Protocols

H.323 is actually a suite of protocols:

- **H.225**: Call signaling and setup (equivalent to SIP for setup)
- **H.245**: Call control — negotiates media channels and codecs
- **RAS (Registration, Admission, Status)**: Communication between terminals and the gatekeeper
- **RTP/RTCP**: Media transport (same as SIP uses)

### H.323 vs. SIP

| Feature | H.323 | SIP |
|---|---|---|
| Origin | ITU-T (1996) | IETF (1999) |
| Architecture | Complex, hierarchical | Simple, peer-to-peer capable |
| Message format | Binary ASN.1 | Text-based (like HTTP) |
| Firewall friendliness | Difficult (dynamic ports) | Better (but still challenging) |
| Modern usage | Legacy enterprise, video endpoints | Dominant modern standard |
| Extensibility | Limited | Highly extensible |

For the exam: SIP is the modern dominant standard. H.323 is legacy. Both use RTP for media transport.

---

## Section 5: RTP and RTCP

Regardless of whether SIP or H.323 is used for signaling, the actual voice and video data is carried by RTP.

### RTP — Real-time Transport Protocol

RTP (RFC 3550) provides end-to-end delivery services for real-time data including audio and video. RTP runs over UDP because:

- UDP has lower overhead than TCP (no connection setup, no retransmission)
- Real-time media cannot wait for retransmission — a late packet is worse than a lost packet for voice
- The application layer handles any necessary error correction

RTP headers include:

- Payload type: identifies the codec (G.711, G.729, etc.)
- Sequence number: allows the receiver to detect missing or out-of-order packets
- Timestamp: enables synchronization and jitter buffer operation

### RTCP — RTP Control Protocol

RTCP runs alongside RTP (on the next consecutive UDP port) and provides quality feedback:

- Reports on packet loss, jitter, and round-trip delay
- Sender Reports (SR): generated by the transmitter with statistics
- Receiver Reports (RR): generated by receivers with quality metrics
- RTCP data is used for monitoring call quality and troubleshooting

---

## Summary of Part 1

Key points from Part 1:

- Unified Communications converges voice, video, messaging, and collaboration onto a single IP network.
- VoIP converts voice to digital packets using codecs. G.711 = ~87 Kbps, G.729 = ~31 Kbps per call including headers.
- SIP is the dominant signaling protocol. Key methods: INVITE, ACK, BYE, REGISTER, CANCEL.
- SIP call flow: INVITE → 180 Ringing → 200 OK → ACK → RTP media → BYE → 200 OK.
- H.323 is the legacy ITU-T standard with Terminals, Gateways, Gatekeepers, and MCUs.
- RTP carries the actual media using UDP. RTCP provides quality feedback statistics.

In Part 2, we will cover Quality of Service mechanisms — how to make sure voice and video get the network treatment they require — along with bandwidth planning formulas, jitter buffers, and UC platform design considerations.

See you in Part 2.
