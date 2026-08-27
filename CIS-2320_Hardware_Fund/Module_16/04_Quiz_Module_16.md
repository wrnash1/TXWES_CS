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

---

### Question 11

A technician installs a new PCIe 4.0 NVMe SSD in a workstation that has a PCIe 3.0 motherboard. The SSD is detected and the system boots correctly. What will the technician observe regarding the SSD's performance?

- A) The SSD will not function because PCIe 4.0 devices are electrically incompatible with PCIe 3.0 slots and will damage the motherboard's PCIe controller
- B) The SSD will operate at PCIe 3.0 speeds — approximately half the maximum throughput of the PCIe 4.0 spec — because PCIe is backward compatible and the link will negotiate to the highest mutually supported generation
- C) The SSD will operate at full PCIe 4.0 speeds because the NVMe protocol overrides the PCIe generation limit and commands the slot to operate at the higher specification
- D) The SSD will operate correctly but only in SATA compatibility mode, which reduces its maximum throughput to approximately 600 MB/s regardless of PCIe generation

Correct Answer: B — The SSD operates at PCIe 3.0 speeds due to backward-compatible negotiation.

PCIe is fully backward and forward compatible at the physical connector level. When a PCIe 4.0 device is installed in a PCIe 3.0 slot, the link negotiates to PCIe 3.0, which provides approximately half the per-lane bandwidth of PCIe 4.0 (PCIe 3.0 x4 provides approximately 3.9 GB/s vs. PCIe 4.0 x4's approximately 7.9 GB/s). The device functions correctly but at reduced throughput. Answer A is incorrect because PCIe is designed for cross-generation compatibility — no electrical damage occurs from installing a newer-generation device in an older slot. Answer C is incorrect because the PCIe link speed is determined by hardware negotiation between both endpoints; the NVMe protocol layer cannot override the physical layer's speed limitation. Answer D is incorrect because NVMe SSDs in M.2 or PCIe slots do not fall back to SATA mode — they continue to use the NVMe protocol over whatever PCIe generation the link negotiates.

---

### Question 12

A workstation's BIOS/UEFI is configured with Secure Boot enabled. A technician installs a new Linux distribution that does not include a signed UEFI shim loader. After installation, the system refuses to boot the new OS. What is the most technically accurate explanation?

- A) Linux is incompatible with UEFI firmware and requires Legacy/CSM mode to be enabled before any Linux distribution can boot
- B) Secure Boot validates the cryptographic signature of the bootloader against keys stored in the UEFI db (allowed signatures database). If the bootloader is not signed by a key in the db, Secure Boot rejects it and the system will not boot the OS
- C) The Linux installation overwrote the Windows Boot Manager, and Secure Boot requires Windows Boot Manager to be present as the first boot entry before any other OS can boot
- D) Secure Boot blocks all software installations from USB drives; the Linux OS booted and installed from USB but cannot boot from the hard drive because Secure Boot only permits USB-sourced boot media

Correct Answer: B — Secure Boot rejects the bootloader because its signature is not in the UEFI allowed signatures database.

Secure Boot uses PKI (Public Key Infrastructure) to verify bootloader integrity. The UEFI firmware checks the bootloader's digital signature against keys stored in the db (allowed signatures database). Modern Linux distributions ship with a Microsoft-signed shim.efi loader specifically to enable Secure Boot compatibility without requiring end-users to add custom keys. A distribution without a signed shim must either have its bootloader certificate added to the UEFI db manually (key enrollment), or Secure Boot must be disabled. Answer A is incorrect because most modern Linux distributions support UEFI Secure Boot through signed shim loaders. Answer C is incorrect because Secure Boot is a signature verification mechanism, not a requirement to have Windows Boot Manager present. Answer D is incorrect because Secure Boot applies to any boot path regardless of storage medium — it validates signatures on all bootloaders regardless of whether they came from USB or internal storage.

---

### Question 13

A technician is replacing a failed CPU in a workstation. After seating the new CPU, applying thermal paste, and reassembling the cooler, the system does not POST and there are no beep codes. The DRAM LED and CPU LED on the motherboard are both lit. What should the technician check first?

- A) Replace the RAM immediately because the DRAM LED indicates the RAM is incompatible with the new CPU
- B) Verify that the CPU is fully seated in the socket with the load lever fully latched, that the correct CPU generation is installed for this motherboard, and that no bent pins (LGA socket) or broken pins (PGA CPU) are present
- C) Flash the BIOS/UEFI to the latest version immediately — no-POST after CPU replacement always requires a firmware update before the system will initialize
- D) Connect the system to a UPS (Uninterruptible Power Supply) because power fluctuations during CPU installation cause both DRAM and CPU diagnostic LEDs to illuminate simultaneously

Correct Answer: B — Verify CPU seating, compatibility, and socket pin condition before any other action.

When both CPU and DRAM diagnostic LEDs are lit after a CPU replacement, the most likely causes are: the CPU is not fully seated (load plate not fully latched), the CPU is not compatible with the current BIOS version (requires a BIOS update with the old CPU installed first), or socket pins are damaged. Physical inspection and seating verification is the correct first step — it costs nothing and resolves the most common cause. A BIOS update may be needed for CPU compatibility, but attempting it before verifying physical seating is premature. Answer A is incorrect because the DRAM LED lighting alongside the CPU LED after a CPU swap suggests the CPU initialization failure is causing memory initialization to also fail — the RAM itself is likely not the root cause. Answer C is incorrect because BIOS updates cannot be performed when the system cannot POST; the procedure would require using the old CPU to update first, then reinstalling the new CPU. Answer D is incorrect because UPS is not relevant to a diagnostic LED pattern that appeared immediately after hardware replacement.

---

### Question 14

A user reports that their computer is running slowly. Task Manager shows CPU usage is at 100% sustained, with a single process consuming 95% of CPU. The user has not installed any new software. Which of the following is the most appropriate next step?

- A) Immediately upgrade the CPU to a higher-core-count model because 100% CPU usage definitively indicates the processor is insufficient for the user's workload
- B) Identify the process consuming 95% CPU by name and PID, research whether it is a legitimate system process or a known malware signature, then run a full antimalware scan — unexplained sustained CPU usage from an unknown process is a common indicator of cryptocurrency mining malware or a runaway process
- C) Increase the pagefile size in Windows virtual memory settings because 100% CPU usage is always caused by insufficient RAM causing excessive paging that stresses the CPU
- D) Restart the computer immediately without identifying the process — a restart clears all processes and permanently resolves CPU spikes regardless of the root cause

Correct Answer: B — Identify the consuming process and investigate for malware before taking any other action.

Unexplained sustained 100% CPU usage from a process not recognized by the user is a classic indicator of malware (particularly cryptomining software) or a legitimate process in a runaway state (memory leak, infinite loop). The correct A+ troubleshooting approach is to identify the specific process name in Task Manager, verify it against known-good Windows process lists, and run a malware scan. Answer A is incorrect because a hardware upgrade is an expensive last resort that should only be considered after software and malware causes are eliminated. Answer C is incorrect because 100% CPU is not caused by insufficient RAM directly — memory pressure causes paging (disk activity), which can contribute to slowness, but Task Manager showing 95% CPU consumption by one process indicates a CPU-bound issue, not a RAM issue. Answer D is incorrect because restarting without identification does not permanently resolve the issue — malware starts again at boot; a runaway process may reoccur immediately.

---

### Question 15

A technician receives a laptop with a physically cracked LCD that needs replacement. Before ordering the replacement panel, the technician reads the existing panel's label and records the part number. When searching for the part number, the technician finds two replacement options at the same price: one with a 45% NTSC color gamut and one with a 72% NTSC color gamut. The laptop is used for graphic design. Which should the technician recommend, and why?

- A) The 45% NTSC panel — lower gamut panels consume less power, extending the laptop's battery life, which is more important for a mobile graphic design user than color accuracy
- B) The 72% NTSC panel — a wider color gamut means the panel can display a broader range of colors, which is important for graphic design work where accurate color reproduction is required
- C) Either panel is equivalent — color gamut percentage is a marketing specification with no real-world effect on displayed color accuracy for graphic design applications
- D) The 45% NTSC panel — graphic design applications internally remap all colors to sRGB, making the physical panel's gamut irrelevant for professional work

Correct Answer: B — The 72% NTSC panel is better for graphic design because it reproduces a wider range of colors.

Color gamut measures the range of colors a display can reproduce. A 45% NTSC panel maps roughly to sRGB coverage (about 72% of the sRGB color space), while a 72% NTSC panel approaches full sRGB and covers more of the Adobe RGB space. For graphic design — where accurate color reproduction affects output quality and ensures designs look correct on screen before printing — a wider gamut panel is the correct recommendation. Answer A is incorrect because the power consumption difference between gamut variants of the same panel is negligible and should not override the professional requirement for color accuracy. Answer C is incorrect because color gamut is a measurable physical characteristic of the panel's backlight and color filter array — it directly affects displayed color accuracy. Answer D is incorrect because applications cannot compensate for a panel that cannot physically reproduce colors outside its gamut; color management in software is constrained by the panel's physical color reproduction capability.

---

### Question 16

A technician is replacing the thermal paste on a CPU that has been in service for four years. After cleaning the old paste with isopropyl alcohol, the technician applies a new pea-sized drop of non-conductive thermal paste in the center of the IHS. The cooler is then reseated. This is the correct procedure. Which of the following best explains why the thermal paste application size matters?

- A) Too much paste increases the thermal resistance between the IHS and the cooler because the paste layer becomes too thick — paste conducts heat less efficiently than direct metal-to-metal contact, so excess paste creates a larger insulating gap
- B) Too much paste improves thermal performance because more paste fills more microscopic gaps, but the excess must be carefully wiped away after mounting because it causes electrical shorts on nearby capacitors
- C) The exact amount of paste does not matter as long as full coverage is achieved — thermal paste spreads to an even layer during mounting regardless of initial quantity
- D) A pea-sized amount is sufficient only for CPUs with surface areas smaller than 150mm squared; for larger desktop CPUs, four corner dots must be used instead

Correct Answer: A — Excess paste creates a thicker layer that increases thermal resistance rather than improving heat transfer.

Thermal paste fills microscopic air gaps between the CPU IHS and the cooler contact surface. However, thermal paste itself is less thermally conductive than metal. A thin, even layer maximizes the benefit of gap-filling while minimizing the insulating effect of the paste itself. Too much paste causes a thick layer that transfers heat less efficiently than a thin layer — and excess paste can spread to surrounding areas where it is not needed. A pea-sized center drop typically spreads to provide full IHS coverage under mounting pressure without overflow. Answer B is incorrect because non-conductive thermal paste does not cause electrical shorts regardless of quantity, but excess paste is still wasteful and creates a thicker thermal layer. Answer C is incorrect because while paste does spread during mounting, the initial amount determines the final layer thickness — too much paste spreads too far beyond the IHS or creates an uneven thick layer. Answer D is incorrect because the pea/center dot method is applicable to all standard consumer CPUs including large IHS designs; larger CPUs may benefit from an X-pattern or line application, but the specific size-based rule stated is not a recognized standard.

---

### Question 17

A user's workstation has 32 GB of DDR4 RAM installed in four slots (4 × 8 GB). The user wants to upgrade to 64 GB. The motherboard manual states: "Maximum memory: 64 GB; Supports dual-channel DDR4 in 2-DIMM or 4-DIMM configurations." Which upgrade path is correct?

- A) Remove all four existing 8 GB sticks and install two 32 GB sticks in slots 1 and 3 — this provides 64 GB in dual-channel mode using the paired slot configuration
- B) Add two additional 8 GB sticks in the empty slots — since all four slots are already filled, this configuration is not possible and the user must purchase a new motherboard
- C) Replace all four 8 GB sticks with four 16 GB sticks (4 × 16 GB = 64 GB) — or alternatively, remove all four and install two 32 GB sticks in the dual-channel slot pair
- D) Add a 32 GB DIMM in any open slot — mixing 8 GB and 32 GB sticks in the same system is fully supported and will result in 64 GB total at the full dual-channel speed

Correct Answer: C — Replace all four 8 GB sticks with 4 × 16 GB sticks, or remove all and install 2 × 32 GB in the dual-channel slot pair.

With all four slots already occupied by 8 GB sticks, the only path to 64 GB is to replace the existing sticks. Option 1: replace all four with 4 × 16 GB = 64 GB in quad-channel (or dual-channel on most consumer platforms). Option 2: remove all four and install 2 × 32 GB = 64 GB in the paired dual-channel slots. Answer A partially describes Option 2 but incorrectly states only two sticks can be used when the manual explicitly supports 4-DIMM configurations. Answer B is incorrect because all four slots are already occupied — there are no empty slots to add to. Answer D is incorrect because mixing 8 GB and 32 GB sticks is possible but requires all sticks to be at the same speed/timing to operate in dual-channel, and the math of 4 × 8 GB + 1 × 32 GB = 64 GB would require five slots, which this motherboard does not have.

---

### Question 18

A laser printer outputs pages where the right half of each page is completely blank (white) but the left half prints normally. The blank area has a sharp, straight boundary running vertically down the center of the page. What component should the technician investigate first?

- A) The paper tray's right side paper guide is set too wide, restricting paper movement and blocking toner from adhering to the right side of the page during the transfer stage
- B) The laser scanning unit (LSU) or the mirror that reflects the laser beam across the drum may have failed for the portion of the scan corresponding to the right side — the laser is not writing to the right half of the drum, leaving it uniformly charged and therefore attracting no toner
- C) The fuser assembly's right heating element has burned out, allowing toner to transfer to the paper but not bond to the right side during the fusing stage
- D) The toner cartridge is low on toner, and since toner flows from right to left during development, the right side depletes first and produces blank output

Correct Answer: B — The laser scanning unit is not writing to the right half of the drum; the LSU or mirror assembly should be investigated.

A precise, sharp vertical boundary between printed and blank areas is a strong indicator of a laser scanning failure. The LSU sweeps the laser beam across the drum using a rotating polygon mirror. If a mirror facet is damaged, a beam path obstruction exists, or the scanning motor has failed for a portion of its sweep, the laser will not discharge the drum in that half. The uniformly charged right half of the drum repels toner (in typical negative-charge toner systems), producing a completely white right half on the page. Answer A is incorrect because paper guide settings affect paper alignment and feeding, not a sharp vertical boundary between printed and blank halves. Answer C is incorrect because fuser failure produces smearing, offset, or toner that wipes off — not a sharp half-page blank area. Answer D is incorrect because toner depletion causes fading and light print across the entire page gradually, not a sharp half-page boundary.

---

### Question 19

A technician builds a new PC and cables everything correctly. On first power-on, the system starts for approximately 2 seconds, then immediately shuts off. When the power button is pressed again, the same behavior repeats. What is the most likely cause?

- A) The PSU is failing to deliver 12V to the CPU power connector — the CPU starts to initialize and immediately detects the undervoltage and initiates an emergency shutdown
- B) The CPU thermal protection is triggering because the cooler was not installed or the cooler is installed with no thermal paste, causing the CPU to reach thermal shutdown temperature within the 2-second window
- C) The BIOS requires configuration before the system will boot normally — the 2-second power cycle is the BIOS requesting user input during initial setup
- D) The RAM sticks are installed in the wrong slots — installing RAM in non-dual-channel slots causes an immediate hardware protection shutdown on modern Intel and AMD platforms

Correct Answer: B — The CPU cooler is missing or improperly seated, causing immediate thermal shutdown.

A brand-new PC that starts briefly then shuts off (and repeats consistently) is a classic symptom of CPU thermal protection. Modern CPUs have thermal shutdown protection that triggers within seconds if the cooler is absent, improperly seated, or missing thermal paste — the CPU heats to TJMax almost immediately without heat dissipation. This is the expected and correct behavior (protecting the CPU from damage). The fix is to power off, verify cooler installation, verify thermal paste application, and retry. Answer A is incorrect because a PSU 12V undervoltage would typically prevent POST entirely rather than causing a 2-second start-shutdown cycle. Answer C is incorrect because no consumer BIOS version implements a 2-second power cycle as a "request for input" — BIOS configuration is accessed after POST completes via a keyboard shortcut. Answer D is incorrect because RAM in incorrect slots causes a no-POST or beep code condition, not a 2-second power cycle — the system might not display output but would not shut itself off as thermal protection does.

---

### Question 20

A technician completes a PC build and performs the first boot. The system POSTs and reaches the Windows desktop. During the BIOS setup review before OS installation, the technician notices that the XMP/EXPO profile for the DDR5-6000 kit is not enabled and the RAM is running at DDR5-4800 (JEDEC base speed). What should the technician do, and what is the risk of enabling XMP/EXPO?

- A) Leave the RAM at DDR5-4800 — XMP/EXPO profiles are unsupported overclocking settings that void the CPU warranty on all platforms and should never be enabled on production systems
- B) Enable the XMP (Intel) or EXPO (AMD) profile in BIOS to configure the RAM to run at its rated DDR5-6000 speed — the risk is that XMP/EXPO represents an overclocked state beyond JEDEC specifications, and some systems may experience instability with specific RAM kit and CPU/motherboard combinations, requiring adjustment of subtimings or voltage
- C) Replace the RAM with DDR5-4800 rated sticks — DDR5-6000 RAM can only run at its rated speed in a DDR5-6000 certified motherboard and cannot be enabled through BIOS settings
- D) Enable XMP/EXPO and then immediately run Prime95 for 24 hours — stress testing is mandatory after any XMP profile activation per Intel and AMD requirements before the system is considered stable for production use

Correct Answer: B — Enable XMP/EXPO to achieve the rated DDR5-6000 speed; be aware that XMP/EXPO is technically an overclocked profile.

DDR5-6000 RAM ships configured for the JEDEC DDR5-4800 default to ensure POST compatibility with all systems. The XMP (eXtreme Memory Profile, Intel) or EXPO (Extended Profiles for Overclocking, AMD) profile stores the manufacturer's validated timings and voltage for the rated speed. Enabling it in BIOS configures the memory controller to run the RAM at the advertised speed. This is the expected and standard configuration step for any high-speed RAM kit. The risk is that XMP/EXPO is technically an overclocked profile — not all CPU memory controllers or motherboards are equally capable of sustaining every DDR5-6000 kit stably, and some adjustment may be needed. Answer A is incorrect because XMP/EXPO is widely supported and does not void CPU warranties on typical consumer platforms — it is a standard documented feature. Answer C is incorrect because DDR5-6000 RAM can absolutely be configured to its rated speed via XMP/EXPO on compatible platforms. Answer D is incorrect because 24-hour stress testing is a user's choice for validation, not a mandatory step required by Intel or AMD after XMP activation.
