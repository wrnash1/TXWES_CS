# Reading Guide: Module 02 - Motherboards and Form Factors

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5

---

### Introduction

Welcome to Module 02 — Motherboards and Form Factors. The motherboard is the central circuit board that physically connects and electrically coordinates every major component in a desktop or laptop PC. This week you will learn how form factor standards determine physical size, mounting hole placement, and case compatibility; how chipsets manage communication between the CPU and all peripherals; and how PCIe expansion slots enable system upgrades and add-on cards.

These topics are directly tested on the CompTIA A+ Core 1 (220-1101) exam under Domain 3.5. As a practicing technician you must be able to identify the correct form factor for a given case, explain what a chipset does at a functional level, match expansion cards to appropriate slot types, and diagnose symptoms caused by a failed CMOS battery. Study every section of this guide before beginning the lab.

---

### 1. High-Yield Glossary

#### ATX (Advanced Technology eXtended)

ATX is the dominant full-size desktop motherboard form factor, measuring 12 inches x 9.6 inches (305 mm x 244 mm). The ATX standard was introduced by Intel in 1995 and defines not only board dimensions but also mounting hole positions (enabling any ATX board to fit any ATX case), the location of the rear I/O panel cutout, and the 24-pin main power connector layout. A full ATX board typically supports five to seven PCIe expansion slots and four to eight RAM slots. ATX is the correct choice when maximum expandability is the priority.

#### Micro-ATX (mATX)

Micro-ATX measures 9.6 inches x 9.6 inches (244 mm x 244 mm) — a perfect square. It is a direct descendant of ATX and is backward-compatible with standard ATX cases because ATX cases include additional mounting holes sized for the smaller board. Micro-ATX boards typically provide two to four PCIe slots and two to four RAM slots, making them suitable for budget desktops and office workstations. The 24-pin ATX power connector is the same. Micro-ATX is the correct answer when a customer needs a board that fits an existing ATX case but wants fewer slots at a lower price.

#### Mini-ITX

Mini-ITX measures 6.7 inches x 6.7 inches (170 mm x 170 mm) and is designed for small form factor (SFF) systems such as home theater PCs, embedded industrial systems, and compact living room builds. Mini-ITX boards typically provide one PCIe x16 slot and two RAM slots. They fit inside some ATX and Micro-ATX cases using adapter hardware, but are purpose-built for SFF enclosures. Expandability is severely limited; choose this form factor only when physical space is the primary constraint.

#### Chipset / PCH (Platform Controller Hub)

A chipset is a set of integrated circuits on the motherboard that manages data flow between the CPU, RAM, storage devices, USB controllers, audio, and expansion slots. In legacy systems, this function was split across two chips — the Northbridge (handling CPU, RAM, and PCIe) and the Southbridge (handling USB, SATA, and PCI). Modern Intel and AMD platforms consolidate this into a single PCH chip.

The chipset determines:

- Which CPU generations and socket types are compatible with the board
- How many USB, SATA, and PCIe lanes are natively available
- Whether CPU overclocking is supported (e.g., Intel Z-series chipsets unlock overclocking; B-series does not)
- Maximum supported RAM speed and capacity

#### PCIe (PCI Express) Expansion Slots

PCI Express is the universal high-speed serial interface standard for connecting expansion cards to the motherboard. PCIe slots are categorized by lane count:

- **x1** — 1 lane; shortest slot; used for sound cards, basic NICs, some Wi-Fi cards
- **x4** — 4 lanes; medium slot; used for NVMe SSD adapters, RAID controllers
- **x8** — 8 lanes; medium-long slot; used for some network and storage HBAs
- **x16** — 16 lanes; longest slot; required for dedicated graphics cards (GPUs)

PCIe bandwidth scales with generation and lane count. PCIe 3.0 x16 provides approximately 16 GB/s bidirectional; PCIe 4.0 x16 provides approximately 32 GB/s; PCIe 5.0 x16 provides approximately 64 GB/s.

#### PCIe Backward Compatibility

PCIe is physically and electrically backward-compatible across generations (3.0, 4.0, 5.0 — same connector, negotiates to the lower speed) and across lane counts in one direction: a shorter (lower lane count) card fits and operates in a longer (higher lane count) slot. A PCIe x1 card will function in a PCIe x16 slot. A PCIe x16 card requires an x16 slot and will not physically fit in a shorter slot.

#### BIOS / UEFI

BIOS (Basic Input/Output System) is firmware stored in a flash chip on the motherboard that initializes hardware components during the Power-On Self-Test (POST) and then hands off control to the operating system bootloader. UEFI (Unified Extensible Firmware Interface) is the modern replacement for legacy BIOS. UEFI supports drives larger than 2 TB (GPT partition table), provides a graphical interface, enables Secure Boot, and supports faster boot times. For the A+ exam, know that UEFI replaced BIOS and that "entering BIOS" and "entering UEFI setup" describe the same action on modern systems.

#### CMOS and the CMOS Battery

CMOS (Complementary Metal-Oxide-Semiconductor) is a small amount of battery-backed memory on the motherboard that stores BIOS/UEFI settings: system date and time, boot order, CPU and RAM speed settings, and security passwords. The CMOS battery is a CR2032 lithium coin cell located on the motherboard surface. It provides approximately 5–10 years of standby power to preserve settings when the system is fully unplugged.

Symptom of a dead CMOS battery: The system date and time reset to a default value on every startup, often accompanied by a "CMOS checksum error" or "CMOS settings lost" message during POST. The system will still boot; it simply loses saved settings between power cycles.

#### CMOS Clear Jumper

The CMOS clear jumper is a three-pin header block located near the CMOS battery. Moving the jumper from the default position (pins 1–2) to the clear position (pins 2–3) for 5–10 seconds, then returning it to the default position, resets all BIOS/UEFI settings to factory defaults. Technicians use this procedure to recover from a forgotten BIOS password, a failed overclock that prevents POST, or any misconfigured BIOS setting that leaves the system unbootable.

#### 24-Pin ATX Power Connector

The 24-pin ATX connector from the power supply unit (PSU) is the primary power input for the entire motherboard. It supplies multiple voltage rails (+3.3V, +5V, +12V) to the board. A separate 4-pin or 8-pin EPS connector near the CPU socket supplies dedicated power to the processor voltage regulator module (VRM). Both connectors must be seated for the system to boot.

#### Rear I/O Panel

The rear I/O panel is the cluster of external ports on the back of the motherboard that align with a cutout in the case. Common rear I/O ports include USB-A (2.0, 3.0, 3.1, 3.2), USB-C, DisplayPort, HDMI (from onboard graphics), audio jacks, Ethernet (RJ-45), and PS/2. An I/O shield — a metal bracket included with the motherboard — snaps into the case cutout to cover gaps around these ports.

---

### 2. Form Factor Comparison Table

| Specification        | ATX           | Micro-ATX     | Mini-ITX      |
|----------------------|---------------|---------------|---------------|
| Dimensions           | 12 x 9.6 in   | 9.6 x 9.6 in  | 6.7 x 6.7 in  |
| PCIe Slots (typical) | 5-7           | 2-4           | 1 (x16)       |
| RAM Slots (typical)  | 4-8           | 2-4           | 2             |
| Fits ATX Case        | Yes           | Yes           | Adapter only  |
| Fits mATX Case       | No            | Yes           | Adapter only  |
| Power Connector      | 24-pin ATX    | 24-pin ATX    | 24-pin ATX    |
| Typical Use Case     | Full desktop  | Budget/office | HTPC / SFF    |

---

### 3. PCIe Slot Quick Reference

| Slot Type | Physical Length | Max Bandwidth (PCIe 4.0) | Typical Use         |
|-----------|-----------------|--------------------------|---------------------|
| x1        | Shortest        | ~2 GB/s                  | Sound, Wi-Fi, NIC   |
| x4        | Medium          | ~8 GB/s                  | NVMe adapter, RAID  |
| x8        | Medium-long     | ~16 GB/s                 | HBA, some GPUs      |
| x16       | Longest         | ~32 GB/s                 | Dedicated GPU       |

---

### 4. Connector and Component Identification Reference

Motherboard power connectors:

- 24-pin ATX main power — wide rectangular connector, supplies the board
- 4-pin or 8-pin EPS CPU power — square connector near CPU socket, powers VRM
- 4-pin Molex — legacy peripheral power (some fan hubs, older drives)
- SATA power — L-shaped, 15-pin, from PSU to storage drives

Motherboard headers (internal):

- CPU_FAN — 4-pin PWM header for CPU cooler fan; BIOS monitors this header for fan failure
- SYS_FAN — 3-pin or 4-pin header for case fans
- USB 2.0 header — 9-pin block; connects front-panel USB 2.0 ports to board
- USB 3.0 header — 19-pin block; connects front-panel USB 3.0 ports to board
- Front panel header — power switch, reset switch, power LED, HDD LED (individual 2-pin connectors)

Storage interfaces:

- SATA III — 7-pin data connector on board; 6 Gb/s; connects 2.5-inch and 3.5-inch drives
- M.2 slot — keyed slot on board surface for NVMe or SATA M.2 SSDs; B key, M key, or B+M key

---

### 5. Certification Exam Tips

**Tip 1 — Form factor case compatibility:** Micro-ATX is backward-compatible with ATX cases. Mini-ITX is NOT reliably compatible with ATX cases without an adapter. The exam frequently tests this distinction in scenario format: "Which board fits in the existing ATX mid-tower?" — the answer is ATX or Micro-ATX, never Mini-ITX as the primary answer.

**Tip 2 — PCIe physical compatibility direction:** A smaller card (x1) fits in a larger slot (x16). This is always allowed and is the correct answer when the exam describes a technician using the only available open slot. The reverse — x16 card into x1 slot — is physically impossible.

**Tip 3 — CMOS battery symptom is NOT a no-boot:** A dead CMOS battery causes the system to lose date/time settings and show a CMOS checksum error. The system still boots. Do not select "system will not POST" as the symptom of a dead CMOS battery.

**Tip 4 — Chipset defines CPU compatibility, not the socket alone:** Two boards with the same socket may have different chipsets. The chipset determines which CPU generations are officially supported. When upgrading a CPU, always verify chipset compatibility in addition to socket type.

**Tip 5 — UEFI replaced BIOS; Secure Boot is a UEFI feature:** Legacy BIOS does not support Secure Boot or GPT drives over 2 TB. The A+ exam distinguishes legacy BIOS from UEFI. Know that UEFI is the current standard on all modern boards.

**Tip 6 — The 8-pin CPU power connector:** Forgetting to connect the 4-pin or 8-pin CPU power connector is a common assembly error. The symptom is a board that powers on momentarily then shuts down, or does not POST at all. This is distinct from a dead CMOS battery.

**Tip 7 — PCIe generation cross-compatibility:** A PCIe 3.0 card in a PCIe 4.0 slot operates at PCIe 3.0 speeds. This is correct behavior, not a fault. The exam may test whether you know that cross-generation PCIe operation is valid.

**Tip 8 — I/O shield installation:** The I/O shield must be installed in the case before the motherboard is seated. Forgetting it after the board is installed requires removing the board to insert it. This is a procedural knowledge question the exam has tested.

---

### 6. Study Checklist

- [ ] Memorize ATX, Micro-ATX, and Mini-ITX dimensions and typical slot counts from the comparison table.
- [ ] Be able to explain what a chipset does and why it determines CPU compatibility.
- [ ] Know PCIe lane counts (x1, x4, x8, x16) and their typical use cases.
- [ ] Understand PCIe backward compatibility rules: smaller card fits larger slot; not the reverse.
- [ ] Know the symptom of a dead CMOS battery and how the CMOS clear jumper is used.
- [ ] Distinguish BIOS from UEFI and identify features exclusive to UEFI (Secure Boot, GPT support).
- [ ] Review the connector identification section and be able to name each connector by physical description.
- [ ] Read the Professor Messer study notes for the 220-1101 motherboard section at [professormesser.com](https://www.professormesser.com/).
- [ ] Watch the Professor Messer free video on motherboards and form factors from the [220-1101 course](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/).
- [ ] Complete the Module 02 lab and submit your deliverable by the Canvas deadline.
- [ ] Post your Module 02 discussion response by Wednesday at 11:59 PM.

---

### Additional Resources

- [Professor Messer CompTIA A+ Core 1 (220-1101) Free Course — Motherboards and Form Factors](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- [CompTIA A+ Certification Official Page and Exam Objectives](https://www.comptia.org/certifications/a)
