# Quiz: Module 13 — Unified Communications and Collaboration

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. This quiz covers Module 13 video lectures and reading guide material.

---

## Questions

### Question 1

Which VoIP codec provides toll-quality (PSTN-equivalent) audio and uses approximately 87 Kbps of bandwidth per call including IP/UDP/RTP header overhead?

- A) G.729
- B) G.722
- C) G.711
- D) Opus

Correct Answer: C

Explanation: G.711 is the uncompressed, toll-quality codec used as the standard for PSTN-equivalent voice. At 64 Kbps payload with 20 ms packetization, including IP/UDP/RTP headers, total per-call bandwidth is approximately 87 Kbps. G.729 uses only 8 Kbps payload (approximately 31 Kbps with overhead).

---

### Question 2

What is the maximum recommended one-way latency for acceptable VoIP call quality according to ITU-T G.114?

- A) 50 ms
- B) 150 ms
- C) 300 ms
- D) 600 ms

Correct Answer: B

Explanation: ITU-T G.114 recommends a maximum one-way latency of 150 ms for acceptable voice quality. Up to 400 ms is the absolute practical limit before conversations become unworkable. 600 ms is characteristic of GEO satellite — unacceptable for VoIP.

---

### Question 3

In a SIP call, which method is used to terminate an already-established call session?

- A) CANCEL
- B) REGISTER
- C) BYE
- D) OPTIONS

Correct Answer: C

Explanation: BYE terminates an established SIP session. CANCEL is used to abort a pending INVITE before the call is answered. REGISTER is used by a UA to record its address with a SIP registrar. OPTIONS queries capabilities.

---

### Question 4

Which protocol carries the actual voice audio between two VoIP endpoints after the SIP signaling completes?

- A) SIP
- B) H.225
- C) RTP
- D) RTCP

Correct Answer: C

Explanation: RTP (Real-time Transport Protocol) carries the voice and video media streams. SIP handles signaling (call setup/teardown). RTCP provides quality feedback statistics alongside RTP. H.225 is an H.323 signaling protocol.

---

### Question 5

What is the DSCP value used to mark voice RTP packets for the highest QoS priority treatment?

- A) DSCP 0 (Best Effort)
- B) DSCP 24 (CS3)
- C) DSCP 34 (AF41)
- D) DSCP 46 (EF)

Correct Answer: D

Explanation: DSCP 46 is the Expedited Forwarding (EF) per-hop behavior — the highest priority DSCP class used specifically for voice RTP media. CS3 (DSCP 24) is used for call signaling. AF41 (DSCP 34) is used for interactive video. DSCP 0 is best-effort default.

---

### Question 6

A network engineer notices that VoIP users are reporting choppy audio even though packet loss is near zero and average latency is acceptable. Which issue is most likely causing the choppy audio?

- A) Insufficient codec bandwidth
- B) High jitter causing packets to arrive at inconsistent intervals
- C) The SIP proxy is dropping INVITE messages
- D) RTCP is consuming too much bandwidth

Correct Answer: B

Explanation: Choppy audio with low packet loss and acceptable average latency is the classic symptom of high jitter. Jitter causes packets to arrive in bursts — the jitter buffer attempts to smooth this but if jitter exceeds the buffer depth, packets are played out at wrong intervals or dropped.

---

### Question 7

Which H.323 component provides address translation and call admission control, routing calls between H.323 terminals on behalf of the network administrator?

- A) MCU (Multipoint Control Unit)
- B) Gateway
- C) Gatekeeper
- D) Terminal

Correct Answer: C

Explanation: The H.323 Gatekeeper provides address translation (resolving H.323 aliases to IP addresses), admission control (deciding whether to allow calls), and bandwidth management. The MCU bridges multipoint conferences. The Gateway translates between H.323 and other networks (such as PSTN).

---

### Question 8

A company deploys IP phones on access switch ports. The phones are on VLAN 20 (voice) and each phone has a PC connected through the phone's built-in switch port on VLAN 10 (data). The phones tag their own traffic with VLAN 20. Which switch port configuration mode enables this design?

- A) Trunk port — allows all VLANs
- B) Access port with voice VLAN configured
- C) Routed port with subinterfaces
- D) Private VLAN port with isolated secondary VLAN

Correct Answer: B

Explanation: An access port with a voice VLAN configured carries untagged data traffic on the access VLAN (VLAN 10) and tagged voice traffic on the voice VLAN (VLAN 20). The IP phone tags its own RTP and SIP traffic with the voice VLAN ID. This is the standard enterprise IP phone deployment model.

---

### Question 9

Why is NAT problematic for SIP VoIP calls?

- A) SIP uses TCP which NAT cannot translate
- B) SIP embeds IP addresses in the application-layer SDP payload that NAT does not rewrite
- C) NAT blocks UDP port 5060 by default
- D) SIP requires a dedicated public IP per call

Correct Answer: B

Explanation: SIP carries SDP (Session Description Protocol) in the message body, which includes the IP address and port that RTP media should be sent to. NAT rewrites the IP header addresses but does not rewrite the embedded SDP addresses — causing the remote end to send RTP to an unreachable private IP address.

---

### Question 10

Which queuing mechanism is recommended for networks carrying VoIP traffic, providing strict priority forwarding for voice while giving guaranteed minimum bandwidth to other traffic classes?

- A) FIFO (First In, First Out)
- B) Priority Queuing (PQ) with four fixed queues
- C) Low Latency Queuing (LLQ)
- D) Weighted Fair Queuing (WFQ)

Correct Answer: C

Explanation: Low Latency Queuing (LLQ) combines a strict priority queue for voice (policed to prevent starvation of other classes) with Class-Based Weighted Fair Queuing (CBWFQ) for other traffic types. This is Cisco's recommended mechanism and the standard answer for the Network+ exam when asked about VoIP QoS queuing.

---

### Question 11

Which VoIP codec uses 64 Kbps and provides uncompressed, toll-quality audio — the same quality as the traditional PSTN — but requires significantly more bandwidth than compressed alternatives?

- A) G.729
- B) G.711
- C) G.722
- D) Opus

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* G.729 is a compressed codec using only 8 Kbps — it provides acceptable quality for WAN VoIP but is not uncompressed toll-quality audio. It requires roughly 1/8 the bandwidth of G.711.
- *Why B is correct:* G.711 uses Pulse Code Modulation (PCM) at 64 Kbps per direction — the same encoding used on the traditional PSTN telephone network. It is the highest quality standard VoIP codec but requires the most bandwidth.
- *Why C is incorrect:* G.722 is a wideband (HD voice) codec at 48–64 Kbps that actually provides better than toll quality — it covers a wider frequency range (50 Hz–7 kHz vs. G.711's 300 Hz–3.4 kHz). While it uses similar bandwidth to G.711, it is not the "uncompressed PSTN-equivalent" codec.
- *Why D is incorrect:* Opus is a modern variable-bitrate codec (6–510 Kbps) used in WebRTC. It is not the traditional PSTN-equivalent codec referenced in Network+ exam contexts.

---

### Question 12

What is the maximum acceptable one-way latency for a VoIP call according to the ITU G.114 recommendation?

- A) 30 ms
- B) 100 ms
- C) 150 ms
- D) 400 ms

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* 30 ms is the maximum acceptable jitter threshold — not the one-way latency limit. Jitter and latency are separate metrics with different thresholds.
- *Why B is incorrect:* 100 ms is a target for excellent voice quality, but the ITU G.114 standard specifies 150 ms as the maximum for acceptable quality, not 100 ms.
- *Why C is correct:* ITU G.114 specifies 150 ms as the maximum one-way latency for acceptable voice quality. Beyond 150 ms, users begin to notice the delay. The absolute maximum for any voice path is 400 ms, but calls exceeding 150 ms are considered degraded.
- *Why D is incorrect:* 400 ms is the absolute maximum beyond which voice calls become unusable (satellite phone quality). ITU G.114 specifies 150 ms as the design target for acceptable quality.

---

### Question 13

In a SIP call setup, which SIP method is sent by the caller to initiate a call, and what protocol carries the actual voice media once the call is established?

- A) SIP OPTIONS initiates the call; HTTP carries the voice media
- B) SIP INVITE initiates the call; RTP carries the voice media
- C) SIP REGISTER initiates the call; RTCP carries the voice media
- D) SIP BYE initiates the call; SDP carries the voice media

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* SIP OPTIONS is used to query a SIP server for its capabilities — it does not initiate calls. HTTP carries web content, not voice media in VoIP.
- *Why B is correct:* The SIP INVITE message initiates a call session by sending the caller's SDP (Session Description Protocol) body with codec preferences and RTP port information to the callee. Once the call is established (200 OK + ACK), RTP (Real-time Transport Protocol) carries the actual voice media over UDP.
- *Why C is incorrect:* SIP REGISTER is used by an IP phone to register its current IP address with a SIP registrar/proxy so incoming calls can be routed to it. It does not initiate calls. RTCP is the RTP Control Protocol used for quality monitoring, not media transport.
- *Why D is incorrect:* SIP BYE terminates a call — it is used at the end of a session, not the beginning. SDP is embedded in SIP messages as a body to negotiate media parameters — it does not carry actual voice samples.

---

### Question 14

An administrator notices that voice call quality is excellent within the LAN but degrades significantly over the WAN link during peak business hours. Which network performance metric is most likely causing the WAN-specific degradation?

- A) MAC address table overflow on the WAN edge switch
- B) Congestion on the WAN link causing queuing delay, jitter, and packet loss
- C) DNS resolution failures for the SIP proxy server
- D) MTU mismatch between the LAN switches and the WAN router

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* MAC address table overflow affects Layer 2 switching within the LAN — it has no impact on WAN performance. Voice quality is described as good on the LAN, which rules out Layer 2 switching issues.
- *Why B is correct:* WAN links typically have lower bandwidth than LAN segments. During peak hours, data traffic competes with voice for WAN capacity. Without QoS, voice packets sit in the same queue as large data transfers, causing queuing delay (added latency), jitter (variable queuing wait times), and potential packet drops — all of which degrade call quality.
- *Why C is incorrect:* DNS resolution happens at call setup, not during the call itself. If DNS were failing, calls would not establish at all — not degrade in quality mid-call during peak hours.
- *Why D is incorrect:* An MTU mismatch causes packet fragmentation and reassembly overhead. While this can affect performance, it would be consistent across all hours, not specifically worsen during peak business hours as described.

---

### Question 15

Which DSCP value is assigned to voice RTP traffic and represents the Expedited Forwarding (EF) Per-Hop Behavior?

- A) DSCP 0 (Best Effort)
- B) DSCP 46 (Expedited Forwarding)
- C) DSCP 34 (Assured Forwarding AF41)
- D) DSCP 48 (Class Selector 6)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* DSCP 0 is the default "Best Effort" marking — no priority treatment. Voice traffic must never be marked as Best Effort.
- *Why B is correct:* DSCP 46 (binary 101110) is the Expedited Forwarding (EF) marking, defined in RFC 3246. It instructs network devices to place this traffic in the strict priority queue, minimizing queuing delay and jitter. EF is the standard marking for VoIP RTP media packets.
- *Why C is incorrect:* DSCP 34 is AF41 (Assured Forwarding Class 4, Drop Precedence 1) — used for interactive video conferencing. Video and voice have different DSCP markings because their traffic characteristics and priority requirements differ slightly.
- *Why D is incorrect:* DSCP 48 is CS6 (Class Selector 6) — used for network management traffic (routing protocols, network infrastructure). It is not assigned to VoIP RTP media.

---

### Question 16

What is the primary difference between SIP and H.323 as VoIP signaling protocols?

- A) SIP uses UDP only; H.323 uses TCP only — making SIP faster but less reliable.
- B) SIP is a text-based protocol aligned with HTTP/MIME conventions; H.323 is a binary protocol suite originally designed for traditional telecom standards.
- C) SIP handles both signaling and media transport; H.323 handles only signaling.
- D) H.323 is an open internet standard; SIP is a Cisco proprietary protocol.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both SIP and H.323 can use either TCP or UDP. SIP commonly uses UDP for speed and TCP for reliability; H.323 uses TCP for signaling. Neither is limited to a single transport.
- *Why B is correct:* SIP was designed with internet principles in mind, using plain text messages similar to HTTP (with methods like INVITE, BYE, ACK). H.323 was derived from the ITU-T telecom standards community and uses binary ASN.1 encoding — more complex and harder to debug. This architectural difference is why SIP became the dominant modern standard.
- *Why C is incorrect:* Neither SIP nor H.323 handles media transport directly. Both use RTP for the actual voice/video media stream. Signaling (call setup) and media transport are separate functions in both protocols.
- *Why D is incorrect:* Both are open standards. H.323 is an ITU-T standard (not just one protocol — it's a protocol suite). SIP is an IETF standard (RFC 3261). Neither is Cisco-proprietary.

---

### Question 17

A company configures a Voice VLAN on all access switch ports. What specific benefit does a dedicated Voice VLAN provide compared to running voice and data traffic on the same VLAN?

- A) It eliminates the need for QoS because VoIP phones automatically receive priority treatment on a dedicated VLAN.
- B) It provides consistent QoS marking, Layer 2 isolation from data traffic, and simplified troubleshooting for voice performance issues.
- C) It doubles the available bandwidth for voice traffic by separating it from the data VLAN.
- D) It prevents IP phones from communicating with the internet, enhancing call security.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A Voice VLAN does not eliminate the need for QoS configuration. The VLAN separation makes it easier to apply QoS policies consistently (e.g., marking all traffic on the Voice VLAN with DSCP EF), but QoS must still be explicitly configured on switch ports and WAN interfaces.
- *Why B is correct:* A dedicated Voice VLAN provides three key benefits: (1) all traffic on the VLAN can be uniformly QoS-marked; (2) voice traffic is isolated from broadcast storms and security threats in the data VLAN; (3) when troubleshooting voice quality, administrators can easily isolate voice VLAN traffic in captures and logs.
- *Why C is incorrect:* VLANs do not create additional bandwidth — they separate broadcast domains. The physical switch ports still share the same physical capacity.
- *Why D is incorrect:* Voice VLANs do not block internet access. IP phones still require network access to reach SIP proxies, PSTN gateways, and sometimes cloud calling services — many of which are internet-facing.

---

### Question 18

Which network component is deployed at the border between an enterprise SIP trunk and the service provider's VoIP network to handle NAT traversal, security policy enforcement, and protocol normalization?

- A) IP PBX (Private Branch Exchange)
- B) MCU (Multipoint Control Unit)
- C) Session Border Controller (SBC)
- D) STUN server

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* An IP PBX manages internal call routing and features (extensions, voicemail, call transfer) within the enterprise. It is not positioned at the enterprise-to-carrier border for NAT traversal and protocol normalization.
- *Why B is incorrect:* An MCU (Multipoint Control Unit) is an H.323 component that bridges multi-party video conferencing — it is not a SIP trunk border device.
- *Why C is correct:* The Session Border Controller (SBC) sits at the enterprise-to-carrier SIP trunk boundary. It handles: NAT traversal (SIP ALG equivalent for enterprise-scale), security (DoS protection, SIP normalization), protocol translation (between different SIP dialects), media relay, and call admission control at the enterprise border.
- *Why D is incorrect:* STUN (Session Traversal Utilities for NAT) is a lightweight client-side protocol used in WebRTC to discover external NAT mappings. It is not an enterprise-grade border device like an SBC.

---

### Question 19

What happens when Call Admission Control (CAC) is configured and the number of concurrent calls reaches the configured maximum?

- A) All existing calls are dropped simultaneously to free capacity for the highest-priority calls.
- B) New call attempts receive a busy signal or rejection, while existing calls continue with guaranteed quality.
- C) CAC automatically compresses all active calls to G.729 to free bandwidth for additional calls.
- D) The IP PBX increases transmit power to compensate for the bandwidth limitation.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* CAC protects existing calls by refusing new ones — it never drops active calls to make room for new ones. Dropping existing calls would defeat the purpose of quality protection.
- *Why B is correct:* When CAC determines that accepting a new call would push the WAN voice bandwidth over the configured threshold, it rejects the new call. The caller receives a busy signal or a call rejected response. All existing calls continue on the WAN link with guaranteed bandwidth and quality.
- *Why C is incorrect:* CAC does not automatically change codec settings on active calls. Codec negotiation happens at call setup via SDP. CAC is a policy enforcement function, not a codec management function.
- *Why D is incorrect:* "Transmit power" refers to wireless RF — it has no relevance to IP PBX bandwidth management or WAN capacity.

---

### Question 20

Which protocol continuously monitors RTP stream quality metrics (jitter, packet loss, round-trip time) and sends periodic reports to call endpoints without carrying any actual voice media?

- A) SIP
- B) RTCP (RTP Control Protocol)
- C) SRTP (Secure RTP)
- D) SDP (Session Description Protocol)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* SIP handles call signaling (INVITE, BYE, REGISTER) — it does not monitor active RTP stream quality.
- *Why B is correct:* RTCP (RTP Control Protocol) runs alongside RTP on adjacent UDP ports. It periodically (typically every 5 seconds) sends Sender Reports (SR) and Receiver Reports (RR) between call endpoints containing statistics on packets sent, packets lost, interarrival jitter, and round-trip delay. This data is used for call quality monitoring and diagnostics.
- *Why C is incorrect:* SRTP (Secure Real-time Transport Protocol) is the encrypted version of RTP — it carries encrypted voice media. It does not perform quality monitoring; a separate SRTCP (Secure RTCP) handles control functions alongside SRTP.
- *Why D is incorrect:* SDP (Session Description Protocol) is embedded in SIP messages to negotiate codecs, media ports, and session parameters during call setup. It does not monitor quality during an active call.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
