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
