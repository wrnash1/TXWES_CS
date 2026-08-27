# Quiz: Module 12 — Wide Area Networks

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. This quiz covers Module 12 video lectures and reading guide material.

---

## Questions

### Question 1

Which of the following correctly defines the demarcation point in a WAN connection?

- A) The router interface where IP addressing begins
- B) The physical boundary between the carrier's network and the customer's network
- C) The firewall appliance separating the WAN from the LAN
- D) The logical point where the ISP assigns a public IP address

Correct Answer: B

Explanation: The demarcation point (demarc) is the physical boundary — typically the network interface device (NID) — where carrier responsibility ends and customer responsibility begins. Equipment on the carrier side of the demarc belongs to the carrier; equipment on the customer side is CPE.

---

### Question 2

A company needs to connect two offices in the same metropolitan area with a point-to-point Ethernet service. The carrier will provide a single virtual connection between the two sites. Which Metro Ethernet service type applies?

- A) E-Tree
- B) E-LAN
- C) E-Line
- D) E-Ring

Correct Answer: C

Explanation: E-Line is the Metro Ethernet Forum point-to-point service type — a single virtual Ethernet connection between two sites. E-LAN is multipoint-to-multipoint. E-Tree is hub-and-spoke. E-Ring is not a MEF standard service type.

---

### Question 3

What is the bandwidth of a T3 (DS3) leased line?

- A) 1.544 Mbps
- B) 6.312 Mbps
- C) 44.736 Mbps
- D) 155.52 Mbps

Correct Answer: C

Explanation: A T3 (DS3) provides 44.736 Mbps — equivalent to 28 T1 circuits (28 × 1.544 Mbps). 1.544 Mbps is a T1. 155.52 Mbps is OC-3. 6.312 Mbps is T2.

---

### Question 4

In an MPLS network, which device is responsible for adding a label to an incoming IP packet at the edge of the MPLS cloud?

- A) Label Switch Router (LSR)
- B) Label Edge Router (LER)
- C) Virtual Routing and Forwarding (VRF) instance
- D) Forwarding Equivalence Class (FEC) table

Correct Answer: B

Explanation: The Label Edge Router (LER) — also called the Provider Edge (PE) router — adds (pushes) labels onto packets entering the MPLS network and removes (pops) them on exit. LSRs are core routers that forward based on labels but do not add or remove them.

---

### Question 5

A company is evaluating WAN options for a remote field office in a location where fiber and cable are unavailable. Employees will conduct daily video conferencing sessions. Which WAN technology best meets these requirements?

- A) GEO satellite — 75 Mbps, 650 ms latency
- B) LEO satellite — 200 Mbps, 30 ms latency
- C) ADSL — 8 Mbps, 10 ms latency
- D) T1 leased line — 1.544 Mbps, 5 ms latency

Correct Answer: B

Explanation: LEO satellite (e.g., Starlink) provides adequate bandwidth and latency suitable for video conferencing. GEO satellite's 650 ms latency makes interactive video conferencing unacceptable. ADSL and T1 are terrestrial options not available at the remote location per the scenario.

---

### Question 6

Which of the following is a key advantage of SD-WAN over traditional MPLS-only WAN architecture for a cloud-first enterprise?

- A) SD-WAN provides dedicated private circuits between all sites
- B) SD-WAN enables direct internet breakout for SaaS traffic at the branch, avoiding data center backhaul
- C) SD-WAN requires less CPE hardware than MPLS
- D) SD-WAN eliminates the need for encryption on all WAN links

Correct Answer: B

Explanation: Traditional MPLS architecture backhauled all traffic (including SaaS) through the central data center. SD-WAN enables direct internet breakout at the branch for cloud and SaaS traffic, dramatically reducing latency and data center bandwidth consumption.

---

### Question 7

A WAN optimization appliance has reduced a 10 GB backup transfer to 500 MB by recognizing previously transmitted data blocks. Which WAN optimization technique does this describe?

- A) Compression
- B) Traffic shaping
- C) Data deduplication
- D) Protocol optimization

Correct Answer: C

Explanation: Data deduplication identifies repeated data patterns and replaces them with short reference tokens in subsequent transfers. The result — 10 GB reduced to 500 MB — is a 95% reduction consistent with deduplication of backup data. Compression alone cannot achieve this level of reduction.

---

### Question 8

Which cellular WAN technology offers speeds up to 4 Gbps but is limited to dense urban areas due to very short signal range and poor building penetration?

- A) 4G LTE-Advanced
- B) 5G Sub-6 GHz
- C) 5G mmWave
- D) HSPA+

Correct Answer: C

Explanation: 5G mmWave (millimeter wave) uses extremely high frequencies (24–100 GHz) that provide multi-gigabit speeds but have very short range and are blocked by walls and obstacles. 5G Sub-6 GHz has better range and penetration but lower peak speeds. 4G LTE-A tops out around 300 Mbps.

---

### Question 9

What does zero-touch provisioning mean in the context of SD-WAN?

- A) All WAN traffic is transmitted without encryption
- B) New branch edge devices automatically configure themselves by contacting the SD-WAN controller on first boot without manual intervention
- C) SD-WAN routes traffic without inspecting packet headers
- D) WAN links are established without requiring any physical cabling

Correct Answer: B

Explanation: Zero-touch provisioning (ZTP) allows new SD-WAN edge devices to be shipped to a branch location and self-configure automatically upon connection to the internet — no on-site technician or manual configuration required. This significantly reduces deployment time and cost.

---

### Question 10

A company's primary 50 Mbps MPLS circuit fails. Traffic automatically reroutes over a backup 4G LTE link within one second without any manual intervention. Which SD-WAN capability enabled this behavior?

- A) Data deduplication
- B) Zero-touch provisioning
- C) Dynamic path selection with sub-second failover
- D) Application-aware routing policy enforcement

Correct Answer: C

Explanation: Dynamic path selection continuously monitors WAN link quality (latency, jitter, packet loss) and automatically steers traffic to the best available path — failing over to backup transports in sub-second time when the primary link degrades or fails. This is a core SD-WAN differentiator versus traditional static routing failover.

---

### Question 11

Which WAN technology uses a permanent, dedicated physical circuit between two endpoints with a fixed bandwidth that is exclusively reserved for that customer at all times, regardless of whether data is being transmitted?

- A) Frame Relay
- B) Metro Ethernet E-Line
- C) MPLS VPN
- D) Leased line (dedicated circuit)

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Frame Relay is a packet-switched WAN technology that uses virtual circuits (PVCs) with committed information rates (CIR) — bandwidth is shared with other customers. It is not a dedicated physical circuit.
- *Why B is incorrect:* Metro Ethernet E-Line is a carrier Ethernet service that may use shared infrastructure. While it provides a logical point-to-point connection, the underlying physical bandwidth may be shared.
- *Why C is incorrect:* MPLS VPN is a packet-switched service where multiple customer traffic flows share the MPLS core infrastructure. MPLS provides traffic isolation but not dedicated bandwidth.
- *Why D is correct:* A leased line (dedicated circuit such as a T1 or T3) provides an exclusive, permanently allocated physical connection between two sites. The entire bandwidth is available to the customer 24/7 regardless of utilization, and no other customers share the circuit.

---

### Question 12

What is the purpose of a CSU/DSU (Channel Service Unit/Data Service Unit) in a WAN connection?

- A) To encrypt all WAN traffic before it leaves the customer premises
- B) To terminate the digital circuit from the carrier and convert the line signal to a format compatible with the customer's router serial interface
- C) To assign IP addresses to WAN-connected devices using DHCP
- D) To provide Wi-Fi access for remote WAN sites

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A CSU/DSU does not perform encryption. Encryption on WAN links is handled by VPN devices or IPsec-capable routers.
- *Why B is correct:* The CSU/DSU terminates the T1/T3 circuit from the carrier at the customer premises. The CSU (Channel Service Unit) connects to the carrier line and handles signal conditioning; the DSU (Data Service Unit) converts the carrier signal to the serial interface format used by the customer's router.
- *Why C is incorrect:* IP address assignment is a function of DHCP servers or manual configuration — not the CSU/DSU. The CSU/DSU operates at Layer 1 and has no IP addressing function.
- *Why D is incorrect:* A CSU/DSU is a wired serial interface device for T-carrier circuits. It has no wireless capability.

---

### Question 13

In an MPLS network, the Label Switched Path (LSP) is predetermined before packets flow. What is the key performance advantage of label-based forwarding over traditional IP routing for traffic traversing the MPLS core?

- A) MPLS labels use fewer bits than IP addresses, reducing packet header size and increasing throughput.
- B) Label lookup at core P routers is faster than IP longest-prefix routing table lookups, enabling line-rate forwarding.
- C) MPLS eliminates packet fragmentation by enforcing a fixed MTU across the entire WAN.
- D) MPLS labels are encrypted, preventing competitors from analyzing traffic patterns.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* MPLS labels (4 bytes) add overhead rather than reducing it compared to standard IP. The performance benefit is in lookup speed, not header size reduction.
- *Why B is correct:* Traditional IP routing requires longest-prefix match lookups in large routing tables at every hop. MPLS P routers perform simple label swap operations — a fixed-length exact match — which is significantly faster and enables deterministic line-rate forwarding in the MPLS core.
- *Why C is incorrect:* MPLS does not enforce a fixed MTU. MPLS Path MTU Discovery handles fragmentation concerns. MTU mismatches can actually be a problem in MPLS networks due to the extra label stack overhead.
- *Why D is incorrect:* MPLS labels are not encrypted. MPLS provides traffic isolation via VRFs and labels, but confidentiality requires additional encryption (IPsec or TLS) applied separately.

---

### Question 14

A company with three branch offices needs any-to-any private connectivity so that each branch can communicate directly with every other branch without routing all traffic through the headquarters. Which WAN technology is best suited for this requirement?

- A) Point-to-point leased line between headquarters and each branch
- B) MPLS VPN with a full-mesh or hub-and-spoke topology
- C) Dedicated T1 leased lines between every pair of branches
- D) GEO satellite broadband at each branch location

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Point-to-point leased lines from headquarters to each branch create a hub-and-spoke topology — branch-to-branch traffic must traverse headquarters, adding latency and consuming headquarters bandwidth.
- *Why B is correct:* MPLS VPN allows carriers to provision any-to-any connectivity between multiple sites using VRFs and the MPLS core. Any site can communicate directly with any other site without traffic flowing through a central hub.
- *Why C is incorrect:* Dedicated T1s between every pair of branches is technically correct for any-to-any connectivity but is extremely expensive and impractical with n(n-1)/2 circuits needed. For even 10 branches: 45 circuits required.
- *Why D is incorrect:* GEO satellite provides connectivity but with 600+ ms latency — unacceptable for interactive business applications, and satellite provides access to the internet, not private any-to-any WAN connectivity.

---

### Question 15

What is the difference between jitter and latency in the context of WAN performance, and which type of application is most adversely affected by high jitter?

- A) Latency is the total one-way packet delay; jitter is variation in that delay between consecutive packets. VoIP and video conferencing are most affected by high jitter.
- B) Latency measures packet loss percentage; jitter measures throughput variation. File transfer applications are most affected.
- C) Latency and jitter are interchangeable terms describing WAN delay. All applications are equally affected.
- D) Jitter is the extra delay caused by encryption overhead; latency is the raw physical propagation delay. Encrypted VPN tunnels experience the most jitter.

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Latency is the time for a packet to travel from source to destination (one-way) or round-trip (RTT). Jitter is the variation (standard deviation) in latency between consecutive packets. VoIP and real-time video conferencing are severely affected by jitter because receiving applications must play out audio/video in a smooth stream — variable packet arrival timing causes choppy or distorted audio/video.
- *Why B is incorrect:* Latency is not packet loss. Packet loss is a separate metric. Jitter is not throughput variation — throughput is a bandwidth measurement.
- *Why C is incorrect:* Latency and jitter are distinct metrics. All applications are not equally affected — latency-tolerant applications (file transfers, email) can sustain high latency and jitter much better than real-time applications.
- *Why D is incorrect:* Encryption overhead contributes a small processing delay (part of overall latency) but is not the definition of jitter. Jitter is caused by varying queuing delays at network nodes, not encryption processing.

---

### Question 16

Which WAN service model involves the customer connecting their equipment to a carrier-provided Metro Ethernet Network Interface Device (NID) and the carrier delivering Ethernet frames between customer sites?

- A) SONET/SDH TDM circuit
- B) Metro Ethernet (MEF Carrier Ethernet)
- C) ADSL broadband internet
- D) Multipoint Frame Relay

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* SONET/SDH is an optical carrier TDM circuit technology that provides dedicated bandwidth using time-division multiplexing. Customers connect via serial interfaces, not Ethernet. SONET does not use Ethernet NID termination for customer-facing services.
- *Why B is correct:* Metro Ethernet (Carrier Ethernet) delivers WAN services using Ethernet interfaces and protocols. The carrier deploys a NID at the customer premises with an Ethernet handoff, and the carrier's Ethernet network (metro or wide area) connects sites using E-Line, E-LAN, or E-Tree services.
- *Why C is incorrect:* ADSL (Asymmetric DSL) is a broadband internet access technology using telephone lines — it provides internet access, not private WAN connectivity between enterprise sites.
- *Why D is incorrect:* Frame Relay is a legacy packet-switched WAN technology that uses serial interfaces and virtual circuits (PVCs) — not Metro Ethernet NID termination.

---

### Question 17

A company uses SD-WAN and routes Microsoft Teams voice calls over an MPLS link (lowest latency) while routing Office 365 email over broadband internet (lowest cost). What SD-WAN capability is being used?

- A) Zero-touch provisioning
- B) Data deduplication
- C) Application-aware routing
- D) WAN compression

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Zero-touch provisioning automates the configuration of new edge devices — it is a deployment capability, not a traffic routing capability.
- *Why B is incorrect:* Data deduplication removes redundant data from transferred files to reduce WAN traffic volume — it does not make routing decisions based on application type.
- *Why C is correct:* Application-aware routing (also called policy-based routing in SD-WAN) uses deep packet inspection (DPI) to identify the application generating traffic and then routes each application according to a defined policy — latency-sensitive apps on low-latency links, bulk traffic on cost-efficient links.
- *Why D is incorrect:* WAN compression reduces the size of data transmitted over WAN links using algorithms like LZ compression. It does not make application-specific routing decisions.

---

### Question 18

What is the function of VRF (Virtual Routing and Forwarding) in an MPLS VPN service?

- A) VRF encrypts all MPLS-tagged packets to ensure customer data privacy.
- B) VRF creates separate, isolated routing table instances on the Provider Edge router — allowing the carrier to serve multiple customers with overlapping IP address spaces.
- C) VRF assigns MPLS label values and manages the label distribution protocol.
- D) VRF provides QoS priority queuing for voice and video traffic within the MPLS core.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* VRF provides logical isolation through separate routing tables, but it does not encrypt packets. MPLS by itself does not encrypt customer data.
- *Why B is correct:* VRF allows a single physical PE router to maintain multiple independent routing table instances — one per customer (or per VPN). This enables the carrier to support customers with overlapping private IP address spaces (e.g., two customers both using 10.0.0.0/8) without conflict, because each customer's routes are in a separate VRF.
- *Why C is incorrect:* Label distribution is handled by LDP (Label Distribution Protocol) or RSVP-TE — not VRF. VRF is about routing table isolation, not label management.
- *Why D is incorrect:* MPLS QoS is implemented through traffic classification, DiffServ markings, and priority queuing configurations on the MPLS routers — not through VRF. VRF provides isolation, not quality of service.

---

### Question 19

A company's ADSL connection has a download speed of 24 Mbps and an upload speed of 3 Mbps. An employee complains that video uploads to a cloud service are very slow while video streaming (downloads) works fine. What characteristic of ADSL explains this?

- A) ADSL is optimized for symmetric traffic and both directions should perform equally — the problem is latency, not bandwidth.
- B) ADSL is asymmetric — download speeds are significantly higher than upload speeds by design. The slow upload reflects the inherent limitation of the technology.
- C) ADSL uses a separate frequency band for uploads that is more susceptible to interference from other services.
- D) ADSL requires a T1 bonding circuit to achieve adequate upload performance.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* ADSL is explicitly asymmetric (the "A" in ADSL stands for Asymmetric). Upload and download speeds are fundamentally different by design.
- *Why B is correct:* ADSL (Asymmetric DSL) is designed with much higher download capacity than upload — a ratio of approximately 8:1 is common. This design was based on the assumption that residential users download more than they upload. The 24/3 Mbps ratio described is typical ADSL performance. Heavy uploaders (video content creators, cloud backup) experience the upload limitation acutely.
- *Why C is incorrect:* While different frequency bands are used for upstream and downstream in ADSL (upstream uses lower frequencies, downstream uses higher), the performance asymmetry is fundamental to the technology design, not an interference vulnerability.
- *Why D is incorrect:* T1 bonding (inverse multiplexing) is a way to aggregate T1 circuits for more bandwidth — it is not a requirement for ADSL and is a separate WAN technology entirely.

---

### Question 20

Which of the following WAN connectivity options typically requires a provider to provision a dedicated physical circuit between two customer sites, can take weeks to months to deploy, but provides guaranteed bandwidth and SLA commitments?

- A) Broadband cable internet
- B) 4G LTE with SIM card
- C) MPLS or leased line with carrier SLA
- D) VPN over public internet

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Broadband cable internet can be provisioned relatively quickly (days to weeks for residential-grade service) but is a shared, best-effort medium with no dedicated bandwidth or WAN SLA.
- *Why B is incorrect:* 4G LTE with a SIM card can be activated very quickly (often same-day) by inserting a SIM into a cellular WAN router. It has no dedicated circuit and no WAN-to-WAN SLA.
- *Why C is correct:* Carrier MPLS and leased lines (T1, T3, fiber Ethernet) require physical provisioning of dedicated circuits — this process typically takes 45–90 days or longer. In exchange, customers receive guaranteed bandwidth, defined latency SLAs, and carrier-managed reliability commitments. This is the defining characteristic of carrier-grade WAN services.
- *Why D is incorrect:* A VPN over the public internet uses existing broadband connectivity with no dedicated provisioning required. It provides encrypted tunnels but inherits the public internet's best-effort, no-SLA characteristics.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
