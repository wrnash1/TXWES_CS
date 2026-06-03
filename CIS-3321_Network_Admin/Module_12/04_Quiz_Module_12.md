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
