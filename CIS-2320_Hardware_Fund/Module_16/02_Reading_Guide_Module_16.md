# Reading Guide: Module 16 - Final Exam Preparation

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

---

### Introduction

Welcome to Module 16 — Final Exam Preparation. This is the capstone module of CIS-2320 Hardware Fundamentals. Rather than introducing new hardware topics, this module consolidates the high-yield concepts from all fifteen previous modules into a structured review aligned with the five CompTIA A+ Core 1 (220-1101) exam domains. By the end of this guide you will have a single-source reference covering the most frequently tested topics, the most common exam traps, a domain-by-domain study checklist, and a complete list of port numbers, cable specifications, connector types, and component relationships tested on the 220-1101 exam.

Your goal this week is to identify any remaining gaps in your hardware, connectivity, troubleshooting, and printer knowledge and close those gaps before the final assessment. Work through this guide systematically, then complete the final lab practical. Do not skip the exam tips section — those eight specific traps account for a disproportionate share of missed questions on the A+ Core 1 exam.

---

### Section 1: A+ Core 1 Exam Domain Map

The CompTIA A+ Core 1 (220-1101) exam covers five domains with the following approximate weights:

- Domain 1 — Mobile Devices: 15%
- Domain 2 — Networking: 20%
- Domain 3 — Hardware: 25%
- Domain 4 — Virtualization and Cloud Computing: 11%
- Domain 5 — Hardware and Network Troubleshooting: 29%

Domains 3 and 5 together account for 54% of the exam. If time is limited, prioritize those two domains. Domain 4 is the smallest but contains distinct terminology (hypervisor types, cloud models) that is consistently tested with minimal overlap from other domains.

The exam contains up to 90 questions completed in 90 minutes. Passing score is 675 on a scale of 100 to 900. Question types include single-answer multiple choice, multiple-select (choose two or three), drag-and-drop ordering, and performance-based questions simulating real tasks.

---

### Section 2: Domain 1 Review — Mobile Devices

**Bluetooth Technology:**
Bluetooth operates in the 2.4 GHz ISM band. Standard consumer device range is approximately 10 meters (Class 2). Bluetooth 5.0 extends range to approximately 40 meters and improves throughput. Pairing uses SSP (Secure Simple Pairing) with four association models: Numeric Comparison (six-digit PIN on both devices), Passkey Entry (code entered on one device), Just Works (automatic, no user confirmation — for headsets and accessories), and Out of Band (NFC tap-to-pair).

Key Bluetooth profiles: A2DP — stereo audio streaming. HFP — hands-free voice calls. HID — keyboards and mice. SPP — serial data for industrial devices.

Bluetooth pairing failure: most commonly caused by (1) peripheral not in active pairing mode, or (2) peripheral already bonded to another device.

**Cellular Data Generations:**

- 3G: 1 to 10 Mbps, HSPA+ standard, largely decommissioned in the US as of 2022.
- 4G LTE: 10 to 100 Mbps typical, uses SIM or eSIM for carrier authentication.
- 5G sub-6 GHz: moderate speed improvement over LTE, similar range to LTE towers.
- 5G mmWave: 500 Mbps to 1+ Gbps, very short range (hundreds of meters), cannot penetrate walls.
- Device hardware radio determines which generation is supported — carrier plan upgrade does not change hardware capability.

**Wi-Fi Standards:**

- 802.11b: 2.4 GHz, 11 Mbps
- 802.11g: 2.4 GHz, 54 Mbps
- 802.11n (Wi-Fi 4): dual-band, up to 600 Mbps
- 802.11ac (Wi-Fi 5): 5 GHz, multi-Gbps with MU-MIMO
- 802.11ax (Wi-Fi 6): dual-band, OFDMA, optimized for dense deployments

WPA2-Personal uses a shared passphrase (PSK). WPA2-Enterprise uses 802.1X/EAP per-user credentials authenticated against a RADIUS server — either PEAP (username/password) or EAP-TLS (certificate).

**USB Connector Types:**

- USB Type-A: rectangular, standard host connector
- USB Type-B: square with beveled top corners, printer/device connector
- Micro-USB: small asymmetrical trapezoid, older Android devices
- USB Type-C: oval symmetrical reversible, modern devices
- Lightning: Apple proprietary flat 8-pin, iPhones through iPhone 14

USB Type-C is a connector shape, not a speed specification. A USB-C port may be USB 2.0, USB 3.x, or Thunderbolt. The host port's published specification determines actual speed.

**Email Protocol Ports:**

| Protocol | Function | Plain Port | Encrypted Port |
|----------|----------|------------|----------------|
| IMAP | Receive (sync, server-based) | 143 | 993 (SSL/TLS) |
| POP3 | Receive (download, removes from server) | 110 | 995 (SSL/TLS) |
| SMTP | Send | 25 (server relay) | 587 (STARTTLS), 465 (SSL) |

IMAP keeps messages on the server and synchronizes across multiple devices. POP3 downloads and removes messages — not suitable for multi-device users. SMTP is outgoing only.

---

### Section 3: Domain 2 Review — Networking

**Network Cable Categories:**

| Category | Maximum Speed | Maximum Distance |
|----------|--------------|-----------------|
| Cat5e | 1 Gbps | 100 meters |
| Cat6 | 1 Gbps (100m) / 10 Gbps (55m) | 100 meters |
| Cat6a | 10 Gbps | 100 meters |
| Cat7 | 10 Gbps | 100 meters |

For any 10 Gbps run exceeding 55 meters, Cat6a is required. Cat6 reverts to 1 Gbps beyond 55 meters.

**Network Connector Types:**
RJ-45 — 8-wire modular connector for Ethernet. RJ-11 — 6-wire modular connector (4 used) for telephone. LC — small-form-factor fiber connector with locking tab, common in data centers. SC — square push-pull fiber connector. ST — round bayonet-twist fiber connector, older installations.

**T568A vs T568B:**
T568B is the standard for new installations in North America. The wire order (from pin 1): white/orange, orange, white/green, blue, white/blue, green, white/brown, brown. Both ends of a patch cable use the same standard (straight-through). A crossover cable uses T568A on one end and T568B on the other — used for direct device-to-device connection without a switch.

**Network Devices:**
Hub — Layer 1, broadcasts to all ports, half-duplex, obsolete. Switch — Layer 2, uses MAC address table to forward frames to specific ports, full-duplex. Router — Layer 3, uses IP addresses and routing tables to route packets between networks. Firewall — filters traffic based on rules, may operate at Layer 3 through Layer 7.

**Fiber Optic:**
Single-mode fiber (SMF) — 9 micron core, uses a laser light source, supports long distances (kilometers). Multi-mode fiber (MMF) — 50 or 62.5 micron core, uses LED light source, shorter distances (up to approximately 550 meters at 10 Gbps with OM3).

**2.4 GHz Wi-Fi Non-Overlapping Channels:** 1, 6, and 11. When deploying multiple access points in the same area, assign different non-overlapping channels to avoid interference.

---

### Section 4: Domain 3 Review — Hardware

**CPU Sockets:**
Intel LGA sockets — pins on the motherboard socket, flat contact pads on the CPU. Common current sockets: LGA 1700 (12th/13th gen Core). AMD AM4 — PGA socket, pins on the CPU. AMD AM5 — LGA socket, pins on the motherboard. Inserting a CPU into the wrong socket can destroy the pins and is not recoverable.

**RAM:**
DDR3 — 240 pins. DDR4 — 288 pins. DDR5 — 288 pins with a different notch position than DDR4. DIMM — full-size 288-pin module for desktops. SODIMM — small outline, 260 pins (DDR4), for laptops and small form-factor systems.

Dual-channel operation requires matching modules in paired slots. Most motherboards pair slots as A1/B1 and A2/B2. Installing both modules in A1/A2 (same channel) runs single-channel. XMP (Extreme Memory Profile) enables overclocked speed profiles stored on the RAM; it does not activate dual-channel.

**Expansion Slots:**
PCIe x1 — sound cards, USB expansion, network cards. PCIe x4 — NVMe expansion cards. PCIe x8 — some GPUs, RAID controllers. PCIe x16 — graphics cards, highest-throughput add-in cards. PCIe is backward compatible — an x1 card works in an x4 or x16 slot (at x1 speeds).

**PSU Connectors:**
24-pin ATX — main motherboard power. 8-pin EPS12V — CPU power (sometimes split as 4+4 pin). 6-pin PCIe — GPU power (older/lower-power GPUs). 8-pin PCIe — GPU power (higher-power GPUs). Some high-end GPUs use two 8-pin connectors or a 16-pin connector. SATA power — drives. Molex 4-pin — older devices, some fans.

PSU wattage is the maximum deliverable power. Efficiency rating (80 Plus tiers: Standard, Bronze, Silver, Gold, Platinum, Titanium) describes the percentage of AC input converted to DC output — higher tiers waste less power as heat. Efficiency rating does not limit or add to deliverable wattage.

**Storage:**
SATA III — 6 Gbps, approximately 550 MB/s for SSDs. NVMe PCIe 3.0 x4 — approximately 3,500 MB/s. NVMe PCIe 4.0 x4 — approximately 7,000 MB/s. M.2 is a physical form factor that can carry either SATA or NVMe protocol — the motherboard slot specification and the drive's key notch determine compatibility.

RAID Levels:

- RAID 0 (Striping): Minimum 2 drives. No fault tolerance. Full combined capacity. Best performance.
- RAID 1 (Mirroring): Minimum 2 drives. Tolerates 1 drive failure. 50% usable capacity.
- RAID 5 (Striping with Parity): Minimum 3 drives. Tolerates 1 drive failure. Capacity = (n-1) drives.
- RAID 10 (Mirror + Stripe): Minimum 4 drives. Tolerates 1 failure per mirror pair. Capacity = 50% of total.

**Display Connectors:**
VGA — analog video only, legacy. DVI — digital or analog, legacy. HDMI — digital video and audio, no daisy-chain. DisplayPort — digital video, audio, and data; supports MST (Multi-Stream Transport) for monitor daisy-chaining. Thunderbolt 3/4 — uses USB-C connector, supports DisplayPort Alt Mode, daisy-chaining supported. If a scenario requires daisy-chaining monitors, DisplayPort is the answer. HDMI cannot daisy-chain.

**Laser Printing EP Process:**

| Step | Action | Component | Failure Symptom |
|------|--------|-----------|----------------|
| 1 — Cleaning | Removes residual toner from drum | Cleaning blade | Ghosting (faint prior image) |
| 2 — Charging | Applies uniform negative charge to drum | Primary corona / charge roller | Gray background, faded streaks |
| 3 — Exposing | Laser discharges selected drum areas | Laser diode, polygon mirror | Missing content, blank sections |
| 4 — Developing | Toner adheres to discharged areas | Developer roller, toner | Faded or uneven output |
| 5 — Transferring | Toner moves from drum to paper | Transfer roller / corona | Faint or incomplete transfer |
| 6 — Fusing | Heat and pressure bond toner to paper | Fuser roller, pressure roller | Smearing when touched |

Mnemonic: Could Children Ever Do That Fast?

---

### Section 5: Domain 4 Review — Virtualization and Cloud Computing

**Hypervisors:**
Type 1 (bare-metal) — runs directly on hardware, no host OS. Examples: VMware ESXi, Microsoft Hyper-V (server), Citrix XenServer. Used in enterprise data centers for production workloads.
Type 2 (hosted) — runs on top of a standard OS. Examples: VMware Workstation, Oracle VirtualBox. Used for development, testing, and learning environments.

**Cloud Service Models:**
IaaS (Infrastructure as a Service) — virtualized compute, storage, and networking. Customer manages OS and above. Examples: AWS EC2, Azure Virtual Machines.
PaaS (Platform as a Service) — managed runtime environment. Customer manages only their application code. Examples: Azure App Service, Google App Engine.
SaaS (Software as a Service) — fully managed application. Customer only uses the software. Examples: Microsoft 365, Salesforce, Google Workspace.

**Cloud Deployment Models:**
Public cloud — multi-tenant, managed by a cloud provider, accessible via internet.
Private cloud — single-tenant, managed by or for one organization, may be on-premises or hosted.
Hybrid cloud — combination of public and private cloud resources with interconnection.
Community cloud — shared among organizations with common regulatory or mission requirements.

**Virtualization Concepts:**
Virtual machines (VMs) share the physical host's CPU, RAM, and storage. Each VM has its own virtualized hardware and runs its own OS. VMs are isolated from one another — a failure or compromise in one VM does not directly affect other VMs on the same host. Snapshots capture a VM's state at a point in time and allow rollback to that state.

---

### Section 6: Domain 5 Review — Hardware and Network Troubleshooting

**The Seven-Step Troubleshooting Methodology:**

Step 1 — Identify the problem: Gather information from the user. Ask when it started, what changed before it started, whether the problem is consistent or intermittent. Replicate the problem if possible.

Step 2 — Establish a theory of probable cause: Consider the most common causes first (Occam's razor). Do not tunnel on one cause before considering alternatives.

Step 3 — Test the theory to determine cause: Perform the simplest test that confirms or refutes the theory. If the theory is confirmed, proceed. If not, establish a new theory and test it.

Step 4 — Establish a plan of action: Determine the full solution, including any side effects or additional steps needed to restore full functionality.

Step 5 — Implement the solution or escalate: Execute the plan. If the solution is beyond the technician's scope, authority, or access, escalate to the appropriate team.

Step 6 — Verify full system functionality: Confirm the original problem is resolved and that the fix has not introduced new issues. Implement preventive measures where appropriate.

Step 7 — Document findings, actions, and outcomes: Record what the problem was, what caused it, what was done to fix it, and the result. This documentation protects the technician and helps future troubleshooting.

**Hardware Troubleshooting Quick Reference:**

No POST, no video, no fans: Check power supply output, 24-pin ATX connection, CPU power connector.
POST completes but no OS: Check boot order in BIOS/UEFI, check storage device health.
System powers on but no video: Check GPU seating, check monitor connection and input selection.
System boots then shuts off: Check CPU thermal paste and cooling, check for overheating.
RAM errors or blue screens: Reseat RAM, test individual modules, check for dual-channel slot configuration errors.
Intermittent storage access: Run SMART diagnostics, check SATA/power connectors.

**Network Troubleshooting Commands:**

- ping: tests basic IP connectivity. `ping 8.8.8.8` tests internet routing. `ping localhost` tests local TCP/IP stack.
- ipconfig (Windows) / ifconfig (Linux/macOS): displays IP address, subnet mask, default gateway, and DNS server configuration.
- tracert (Windows) / traceroute (Linux/macOS): displays each hop between source and destination, showing where connectivity fails.
- nslookup: tests DNS name resolution. If ping by IP works but ping by hostname fails, the issue is DNS.
- netstat: displays active network connections and listening ports.

**OSI Model for Troubleshooting (Layer 1 → Layer 7):**
Start at Layer 1 (Physical) — check cables, link lights, and physical connections. Move to Layer 2 (Data Link) — check switch port, VLAN assignment, and MAC address table. Move to Layer 3 (Network) — check IP address, subnet mask, default gateway. Move up through Transport (ports), Session, Presentation, and Application as needed. Most hardware-related network problems resolve at Layers 1 through 3.

---

### Section 7: High-Yield Topic Rapid Reference

This section consolidates the most frequently tested specific values from across all fifteen modules.

Port Numbers: IMAP 143/993. POP3 110/995. SMTP 25/587/465. HTTP 80. HTTPS 443. FTP 20 (data) and 21 (control). SSH 22. Telnet 23. DNS 53. DHCP 67 (server) and 68 (client). RDP 3389. SMB 445.

Cable Specifications: Cat5e = 1 Gbps at 100m. Cat6 = 10 Gbps at 55m, 1 Gbps at 100m. Cat6a = 10 Gbps at 100m. Single-mode fiber = kilometers. Multi-mode fiber = hundreds of meters.

RAM Pin Counts: DDR3 DIMM = 240 pins. DDR4 DIMM = 288 pins. DDR5 DIMM = 288 pins (different notch). DDR4 SODIMM = 260 pins.

USB Speeds: USB 2.0 = 480 Mbps. USB 3.2 Gen 1 = 5 Gbps. USB 3.2 Gen 2 = 10 Gbps. Thunderbolt 3/4 = 40 Gbps.

RAID Minimums: RAID 0 = 2 drives. RAID 1 = 2 drives. RAID 5 = 3 drives. RAID 10 = 4 drives.

PSU 80 Plus Tiers (efficiency at 50% load, approximately): Standard = 80%. Bronze = 85%. Silver = 88%. Gold = 90%. Platinum = 92%. Titanium = 96%.

---

### Section 8: Certification Exam Tips

Tip 1 — PSU efficiency rating vs wattage. The A+ exam asks why a PSU "cannot power" a system. The answer is always insufficient wattage — the total combined power draw of all components exceeds the PSU's rated output. Efficiency rating is never the limiting factor for what a PSU can power.

Tip 2 — DisplayPort for daisy-chaining. If a scenario requires connecting multiple monitors in a daisy-chain configuration from a single output port, DisplayPort MST is the answer. HDMI does not support daisy-chaining. Thunderbolt supports DisplayPort Alt Mode and can daisy-chain, but DisplayPort is the direct answer.

Tip 3 — Dual-channel RAM slot placement. Dual-channel requires matching modules in paired slots — A1/B1 or A2/B2, not A1/A2. Installing in adjacent same-channel slots runs single-channel. XMP does not affect channel configuration.

Tip 4 — Cat6 at 10 Gbps over 55 meters. Cat6 only supports 10 Gbps up to 55 meters; beyond that it falls back to 1 Gbps. Any scenario with a 10 Gbps requirement and a run longer than 55 meters requires Cat6a.

Tip 5 — Smearing equals fusing; faint equals transfer. These two symptom-to-stage mappings are the most tested laser printer troubleshooting distinctions. Toner that rubs off = fuser. Toner that is faint or partially missing = transfer roller.

Tip 6 — USB Type-C speed is set by the port, not the connector. The connector shape is identical across USB 2.0 and Thunderbolt 4 implementations. The host port's specification — printed in the device specs, not visible on the connector — determines maximum speed.

Tip 7 — Seven-step troubleshooting order matters. The exam presents a scenario and asks what the technician should do first. "First" almost always means gathering information and identifying the problem — not jumping to replacement or reinstallation. Work through the methodology in order.

Tip 8 — Layer 2 vs Layer 3 device selection. Questions describing communication between devices on the same network need a switch (Layer 2). Questions describing communication between two different networks or subnets need a router (Layer 3). Selecting a switch when a router is needed — or vice versa — is the most common network device identification error.

---

### Required Review Activities

Complete the following before the final assessment:

- Required Review: Work through all fifteen module reading guides and identify any glossary terms you cannot define from memory. For each gap, return to the relevant module's reading guide and review that section before proceeding.
- Required Video Review: Watch the Module 16 video lecture and any domain segments from Professor Messer's CompTIA A+ 220-1101 course at professormesser.com that correspond to your identified weak areas.
- Practice Questions: Work through at least 30 practice questions from Professor Messer's practice exam materials at professormesser.com before attempting the final assessment.

---

### Final Study Checklist

- [ ] State all six EP process steps in order without notes and name the responsible component for each.
- [ ] Write out all email port numbers from memory: IMAP, POP3, SMTP (all variants).
- [ ] Identify the minimum drive count for RAID 0, 1, 5, and 10 and state the fault tolerance of each.
- [ ] State the maximum speed and distance for Cat5e, Cat6, and Cat6a.
- [ ] Explain why USB Type-C connector shape does not determine transfer speed.
- [ ] Explain the difference between WPA2-Personal and WPA2-Enterprise authentication.
- [ ] List the seven troubleshooting methodology steps in order.
- [ ] Name the three cloud service models (IaaS, PaaS, SaaS) and describe what each provides.
- [ ] Explain the difference between a Type 1 and Type 2 hypervisor.
- [ ] Identify the display connector that supports monitor daisy-chaining.
- [ ] State the dual-channel RAM slot pairing rule (which slots must be used).
- [ ] Explain the difference between a switch and a router in terms of OSI layer and function.
- [ ] Complete the Module 16 final lab practical.
- [ ] Register for or confirm your CompTIA A+ 220-1101 exam appointment at comptia.org.
