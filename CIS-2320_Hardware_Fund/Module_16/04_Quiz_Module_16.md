# Quiz: Module 16 - Final Exam Preparation (Comprehensive Review)

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

---

### Question 1

A technician needs to run Ethernet cable from a network closet to a workstation 78 meters away. The connection must support 10 Gbps. Which cable category is required?

- A) Cat5e
- B) Cat6
- C) Cat6a
- D) Cat3

Correct Answer: C — Cat6a

Cat6a supports 10 Gbps at the full 100-meter horizontal run standard. Cat6 supports 10 Gbps only to 55 meters — at 78 meters it reverts to 1 Gbps, making it insufficient for this requirement. Cat5e is limited to 1 Gbps at any distance. Cat3 is a legacy 10 Mbps standard used for telephone wiring.

---

### Question 2

A technician installs two DDR4 RAM modules in a new desktop workstation. After boot, the system runs noticeably slower than expected for memory-intensive tasks. Investigation reveals both modules are in slots A1 and A2. What should the technician do to achieve the expected performance?

- A) Enable XMP in the BIOS, which activates dual-channel mode regardless of physical slot placement.
- B) Move one module from slot A2 to slot B1 so the modules occupy the paired A1/B1 slots required for dual-channel operation.
- C) Replace both modules with ECC RAM, because non-ECC DDR4 cannot operate in dual-channel mode on consumer motherboards.
- D) Install a third matching module in slot B2 to create a triple-channel configuration, which is required for full DDR4 bandwidth.

Correct Answer: B — Move one module to slot B1 to form the A1/B1 paired dual-channel configuration.

Dual-channel RAM requires matching modules in the motherboard's designated paired slots — typically A1/B1 or A2/B2, not adjacent slots on the same channel (A1/A2). Installing in the same-channel adjacent slots produces single-channel operation at lower bandwidth. XMP controls RAM speed profiles, not channel configuration. ECC RAM is a reliability feature unrelated to dual-channel. Consumer DDR4 platforms are dual-channel, not triple-channel.

---

### Question 3

A laser printer is producing pages where toner smears easily when touched. The image is sharp and correctly positioned before touching. The toner cartridge was replaced three weeks ago. Which EP process step has most likely failed, and which component is responsible?

- A) Charging step — the primary corona wire or charge roller is failing, preventing the drum from holding a uniform negative charge.
- B) Transferring step — the transfer roller is worn, causing toner to be deposited too heavily on the paper surface.
- C) Fusing step — the fuser assembly is not applying sufficient heat or pressure to permanently bond toner into the paper fibers.
- D) Exposing step — the laser diode is degrading, causing toner to adhere to background areas that are not fully discharged.

Correct Answer: C — Fusing step failure; the fuser assembly is not bonding the toner to the paper.

Toner that smears when touched is the definitive fuser failure symptom. The fusing step uses a heated roller and a pressure roller to melt toner particles into paper fibers. If either the heat or pressure is insufficient, toner reaches the paper via the transfer step (producing a sharp visible image) but is not bonded — it wipes off when touched. Charging failure produces a gray background or faded output. Transfer failure produces faint or incomplete output, not smearing. Exposing failure produces missing or incorrect content.

---

### Question 4

A user reports that email on their phone no longer shows recent messages that they read and deleted on their laptop. The same messages they deleted on the laptop still appear unread on the phone. Which protocol is most likely configured on both devices, and what is the correct fix?

- A) IMAP is configured; IMAP is designed to maintain separate local copies on each device. Switch to POP3 to enable synchronization.
- B) SMTP is configured for incoming mail; replace it with IMAP on both devices to restore synchronization.
- C) POP3 is configured on one or both devices; POP3 downloads messages locally without server-side synchronization. Configure IMAP on both devices to synchronize mailbox state across all devices.
- D) The mail server has exceeded its storage quota; quota overruns prevent synchronization and require the IT department to increase the mailbox size limit.

Correct Answer: C — POP3 is configured; switch both devices to IMAP.

POP3 downloads messages from the server — typically deleting them — and stores them locally on the downloading device only. Actions on one device (reading, deleting) are not reflected elsewhere. IMAP keeps messages on the server and synchronizes state (read status, deletions, folder placement) across all connected devices. Answer A is wrong because IMAP is the solution, not the problem. Answer B is wrong because SMTP is an outgoing-only protocol and cannot be configured for incoming mail. Answer D is wrong because quota issues cause delivery failures and bounce messages, not cross-device synchronization divergence.

---

### Question 5

A technician is selecting a display connector for a workstation that must drive two external monitors connected in a daisy-chain configuration from a single output port on the GPU. Which connector type supports this requirement?

- A) HDMI 2.1
- B) VGA
- C) DVI-D
- D) DisplayPort

Correct Answer: D — DisplayPort

DisplayPort supports MST (Multi-Stream Transport), which allows multiple monitors to be daisy-chained from a single DisplayPort output. HDMI does not support daisy-chaining — it is a point-to-point connection only. VGA carries only analog video and has no daisy-chain capability. DVI-D carries digital video but also does not support daisy-chaining.

---

### Question 6

A server administrator is configuring a storage array with four identical 4 TB drives. The requirements are: maximum fault tolerance, usable capacity of at least 8 TB, and the array must survive the simultaneous failure of two drives. Which RAID level meets all three requirements?

- A) RAID 0 — stripes data across all four drives for maximum performance and full 16 TB capacity.
- B) RAID 5 — uses distributed parity across three drives, tolerating one drive failure with 12 TB usable capacity.
- C) RAID 10 — mirrors two pairs of drives; can tolerate one failure per mirrored pair (two total failures across different pairs), providing 8 TB usable capacity.
- D) RAID 1 — mirrors two drives and stripes the other two separately, providing 8 TB capacity with two-drive failure tolerance.

Correct Answer: C — RAID 10

RAID 10 (also written RAID 1+0) mirrors pairs of drives and then stripes across the mirrors. With four 4 TB drives it provides 8 TB usable capacity. It can survive two simultaneous drive failures as long as the two failed drives are not both in the same mirrored pair. RAID 0 has no fault tolerance — any drive failure loses all data. RAID 5 tolerates only one drive failure; two simultaneous failures would destroy the array. The description in option D does not match any standard RAID level.

---

### Question 7

A technician connects a USB-C cable from a laptop to a USB-C external SSD rated at 10 Gbps. Actual transfer speed measures only 480 Mbps. The cable is certified for USB 3.2 Gen 2. Which is the most likely explanation?

- A) USB-C cables are limited to 480 Mbps regardless of certification; to achieve 10 Gbps the cable must be replaced with a Thunderbolt cable using a different connector shape.
- B) The laptop's USB-C port is USB 2.0 protocol; the connector is physically USB-C but the port's implementation is USB 2.0, which caps throughput at 480 Mbps.
- C) The external SSD requires a driver update before USB 3.2 speeds are available; 480 Mbps is the default speed before the driver is installed.
- D) The file system on the external SSD must be formatted as exFAT before USB 3.2 Gen 2 speeds are available; NTFS limits USB-C throughput to 480 Mbps.

Correct Answer: B — The laptop's USB-C port operates at USB 2.0 protocol; the connector shape is USB-C but the speed is determined by the port's protocol implementation.

USB Type-C is a connector shape, not a speed specification. A manufacturer can wire a USB-C port to USB 2.0, USB 3.x, or Thunderbolt protocol. The 480 Mbps measurement matches USB 2.0 exactly. The cable's USB 3.2 Gen 2 certification is irrelevant when the host port is USB 2.0 — the connection negotiates at the lower speed. File system format does not cap USB transfer speeds. Driver issues produce connection errors, not a clean speed cap at exactly 480 Mbps.

---

### Question 8

According to the CompTIA A+ seven-step troubleshooting methodology, what is the correct first action when a user reports a hardware problem?

- A) Replace the most likely failed component with a known-good spare to determine if the hardware is the cause.
- B) Reinstall the operating system to eliminate software as a variable before examining hardware.
- C) Identify the problem by gathering information from the user, determining what symptoms are present, and establishing when and under what conditions the problem occurs.
- D) Escalate the ticket to a senior technician, because hardware diagnosis requires specialized expertise beyond the first-step scope.

Correct Answer: C — Identify the problem by gathering information.

Step 1 of the A+ troubleshooting methodology is always to identify the problem — gather information from the user, ask what symptoms appear, when the problem started, and what changed before it started. Replacing hardware before understanding the problem risks replacing the wrong component. Reinstalling the OS before diagnosing the problem introduces unnecessary disruption and skips multiple steps. Escalation is Step 5 (implement the solution or escalate) and only applies when the solution exceeds the technician's authority or capability — not as a first step.

---

### Question 9

A technician is selecting a PSU for a new workstation build. The GPU requires 300 W, the CPU requires 125 W, and all other components combined require approximately 75 W. The technician selects a 600 W 80 Plus Gold PSU. A colleague suggests the efficiency rating is too low and will prevent the system from receiving adequate power. Is the colleague correct?

- A) Yes — the 80 Plus Gold efficiency rating limits DC output to 80% of wattage, so a 600 W unit only delivers 480 W, which is less than the 500 W required.
- B) No — the 80 Plus Gold rating describes the efficiency of AC-to-DC conversion (approximately 90% at 50% load), not a cap on deliverable DC wattage. The PSU delivers its full 600 W rated output regardless of efficiency tier.
- C) Yes — 80 Plus Gold PSUs are certified only for office workloads; a gaming or workstation GPU requires an 80 Plus Platinum or Titanium PSU to receive full power delivery to the PCIe connectors.
- D) No — but the PSU is still insufficient because 600 W is below the recommended 20% headroom minimum of 750 W for this component set.

Correct Answer: B — The colleague is incorrect. Efficiency rating describes conversion efficiency, not a cap on output wattage.

The 80 Plus certification tiers (Bronze, Silver, Gold, Platinum, Titanium) measure what percentage of AC input power is successfully converted to DC output versus lost as heat. A 600 W 80 Plus Gold PSU delivers up to 600 W of DC power to components — the Gold rating means it wastes less AC power as heat compared to a Bronze unit, not that it delivers less power. The total component draw in this scenario is 500 W; a 600 W PSU provides 100 W of headroom, which is acceptable. Answer D is wrong because 20% headroom on 500 W is 600 W — this PSU meets that threshold exactly.

---

### Question 10

A technician is troubleshooting a workstation that successfully connects to local network resources but cannot reach any internet addresses. Running ipconfig shows a valid IP address, subnet mask, and DNS server address. Pinging the default gateway by IP address succeeds. Pinging an external IP address (8.8.8.8) fails. What is the most likely cause?

- A) The workstation's network cable is damaged; a damaged cable allows local traffic but blocks internet traffic due to the longer signal path to external servers.
- B) The workstation's NIC has failed; a partially failed NIC allows local communication but cannot transmit packets beyond the local subnet boundary.
- C) The default gateway device (router) is not routing packets to the internet — either the router has lost its upstream WAN connection or a routing or firewall rule is blocking outbound traffic from this workstation.
- D) The DNS server address is incorrect; when DNS fails, the workstation can only communicate with devices on the local subnet and cannot resolve any internet addresses.

Correct Answer: C — The default gateway (router) is not routing packets to the internet; the WAN connection or a routing/firewall rule is the likely cause.

The symptom sequence narrows the fault precisely: local resources are reachable (Layer 2 and Layer 3 local routing work), the default gateway responds to ping (the gateway itself is up and the route to it works), but pinging an external IP by address fails. Because the ping uses an IP address directly (not a hostname), DNS is not involved — DNS failure would not cause ping-by-IP to fail. The failure point is beyond the gateway — either the router has lost its upstream internet connection, or a routing table entry or firewall rule is blocking this workstation's outbound traffic. Answer A is wrong because a cable problem would affect all network connectivity, not just internet access. Answer B is wrong because a failed NIC would not produce a consistent boundary at the subnet edge. Answer D is wrong because pinging 8.8.8.8 by IP address bypasses DNS entirely.
