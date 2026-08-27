# Reading Guide: Module 09 - Peripheral Devices and Interfaces

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.2 and Domain 1.2

---

## Introduction

Module 09 covers the external connectivity standards that attach input devices, output devices, storage, and security hardware to a PC. These topics are some of the most frequently tested on the CompTIA A+ Core 1 exam because they appear in scenario questions about slow peripheral performance, incorrect cable selection, multi-system desk configurations, and enterprise authentication deployments.

The most important concept in this entire module is the distinction between a connector's physical shape and its actual data transfer speed. The exam deliberately constructs questions that exploit the assumption that a USB Type-C connector means USB 3.x or Thunderbolt speed. Mastering this distinction before exam day is essential.

Read this guide completely before beginning the lab. Pay close attention to the USB version table, the connector identification section, and the exam traps.

---

## Section 1 — USB Standards: Complete Version Hierarchy

USB (Universal Serial Bus) is the dominant peripheral interface standard for connecting keyboards, mice, external drives, cameras, audio interfaces, hubs, and countless other devices. The version hierarchy must be memorized for the A+ exam.

### USB Version Speed Reference Table

| USB Version | Marketing Name | Max Transfer Speed | Connector Types | Color Code (Type-A) |
|---|---|---|---|---|
| USB 1.1 | Full-Speed USB | 12 Mbps | Type-A, Type-B | White/Black |
| USB 2.0 | Hi-Speed USB | 480 Mbps | Type-A, Type-B, Mini-B, Micro-B | White/Black |
| USB 3.0 / 3.1 Gen 1 / 3.2 Gen 1x1 | SuperSpeed USB | 5 Gbps | Type-A, Type-B, Type-C | Blue |
| USB 3.1 Gen 2 / 3.2 Gen 2x1 | SuperSpeed USB 10Gbps | 10 Gbps | Type-A, Type-C | Blue or Teal (varies) |
| USB 3.2 Gen 2x2 | SuperSpeed USB 20Gbps | 20 Gbps | Type-C only | N/A |
| USB4 Gen 2x2 | USB4 | 20 Gbps | Type-C only | N/A |
| USB4 Gen 3x2 | USB4 40Gbps | 40 Gbps | Type-C only | N/A |
| Thunderbolt 3 | — | 40 Gbps | USB-C physical connector | Lightning bolt icon |
| Thunderbolt 4 | — | 40 Gbps (stricter cert) | USB-C physical connector | Lightning bolt icon |

**Note on naming:** USB 3.0 has been renamed multiple times by the USB Implementers Forum. The A+ exam uses the original numbering (USB 2.0, USB 3.0, USB 3.1 Gen 2). Know the original names and their speeds.

### The Blue Port Rule

USB 3.0 and its successors introduced a color-coding convention: USB 3.x Type-A ports and male connectors are manufactured in blue. This is the fastest field identification method for USB version. If a port is white or black, assume USB 2.0 unless labeled otherwise. If a port is blue, it is USB 3.0 or higher.

---

## Section 2 — USB Connector Types

Knowing each connector type by appearance is tested on the A+ exam through physical identification questions and scenario questions describing cable compatibility issues.

### USB Connector Identification Reference

| Connector Name | Physical Description | Common Use Cases |
|---|---|---|
| USB Type-A (male) | Flat rectangle, wider than tall | Host-side connector: PCs, laptops, hubs, chargers |
| USB Type-A (female) | Flat rectangular port | USB ports on desktops, hubs, power strips |
| USB Type-B (male) | Square with beveled top corners | Printers, scanners, older external drives |
| USB Mini-B (male) | Trapezoidal, 5-pin | Older cameras, MP3 players, GPS units |
| USB Micro-B (male) | Very thin, 5-pin, asymmetric | Smartphones (2010-2018), older accessories |
| USB Micro-B 3.0 (male) | Wider than Micro-B, two-part body | USB 3.0 portable hard drives |
| USB Type-C (male) | Small oval, reversible (no wrong way) | Modern laptops, phones, peripherals, Thunderbolt |

### The Type-C Critical Distinction

USB Type-C is a connector form factor — a physical shape specification. It is not a speed standard. A device with a USB-C port may support:

- USB 2.0 at 480 Mbps (common on budget phones and accessories)
- USB 3.1 Gen 1 at 5 Gbps
- USB 3.1 Gen 2 at 10 Gbps
- USB4 at 20 or 40 Gbps
- Thunderbolt 3 or 4 at 40 Gbps
- DisplayPort Alt Mode (video output)
- HDMI Alt Mode (video output)
- Power Delivery (up to 240W with USB PD 3.1)

The only way to determine the actual capability of a USB-C port is to read the device's specifications or look for additional labeling (lightning bolt for Thunderbolt, USB speed rating label, power delivery rating).

---

## Section 3 — Thunderbolt Interface

### Thunderbolt Version Comparison

| Version | Max Speed | Physical Connector | Key Capabilities | Identification |
|---|---|---|---|---|
| Thunderbolt 1 | 10 Gbps | Mini DisplayPort | Daisy-chaining up to 6 devices | Lightning bolt icon |
| Thunderbolt 2 | 20 Gbps | Mini DisplayPort | Aggregated channels; 4K display support | Lightning bolt icon |
| Thunderbolt 3 | 40 Gbps | USB Type-C | USB4, DisplayPort, PCIe, 100W charging | Lightning bolt + USB-C |
| Thunderbolt 4 | 40 Gbps | USB Type-C | Stricter TB3 requirements; mandatory 40Gbps, dual 4K displays | Lightning bolt + USB-C |

### What Thunderbolt Carries Over One Cable

Thunderbolt 3 and 4 are remarkable because a single cable simultaneously carries:

- PCIe data (enables eGPUs — external graphics cards — and Thunderbolt docks)
- DisplayPort video (up to two 4K displays or one 8K display)
- USB data (backwards compatible with USB devices)
- Power Delivery (up to 100W for laptop charging)

This multi-protocol capability over a single cable is what distinguishes Thunderbolt from standard USB-C, even though they share the same physical connector.

### Cable Compatibility Rules

Understanding what cable works in what port prevents field mistakes and is tested on the exam.

| Cable Type | In USB-C Port | In Thunderbolt Port |
|---|---|---|
| Standard USB-C cable | Full USB speed (per port's USB version) | Works at USB speed only — no Thunderbolt |
| Thunderbolt 3/4 cable | Works at USB speed only | Full Thunderbolt speed |
| Thunderbolt 3 cable in TB4 port | Works at Thunderbolt 3 speed | Full Thunderbolt 4 speed |

---

## Section 4 — KVM Switches

### What KVM Stands For and Why It Is Used

KVM = Keyboard, Video, Mouse. A KVM switch routes the signals from one keyboard, one monitor, and one mouse to multiple computers and allows the user to select which computer receives those signals at any given moment.

**Primary use cases:**

- Data center and server room management: A single rack-mounted console controls dozens of servers without a monitor/keyboard for each server.
- Developer and administrator desks: Managing a personal laptop and a work desktop from one keyboard and monitor.
- Lab environments: Students or technicians cycling through multiple test machines from one console.

### How KVM Switching Works

Physical button switching: Most consumer KVM switches have a button on the device body. Pressing the button cycles through connected computers in sequence.

Keyboard hotkey switching: Most KVM switches also support a hotkey combination — typically double-pressing the Scroll Lock key followed by a number — to jump directly to a specific connected computer.

When the switch is activated: The USB keyboard and mouse signals are rerouted to the selected computer. The monitor's video input is switched to the video output of the selected computer. The deselected computer loses keyboard, mouse, and display but remains powered on and running.

### KVM Troubleshooting

| Symptom | Most Likely Cause | Resolution |
|---|---|---|
| Keyboard/mouse switch correctly but monitor is blank | Missing or unseated video cable from PC 2 to KVM switch | Check and reseat video cable on KVM input port for PC 2 |
| Monitor switches but keyboard/mouse do not respond | USB cable from PC to KVM switch is disconnected or failed | Check USB cable from affected PC to KVM switch |
| KVM switch does not switch at all | Hotkey sequence not supported by this KVM model | Use physical button; check KVM manual for correct hotkey |
| Cursor appears sluggish on one connected PC | USB hub inside KVM adding latency | Use KVM's direct USB ports if available; update KVM firmware |

---

## Section 5 — Authentication Peripherals

### Multi-Factor Authentication (MFA) Factor Categories

The A+ exam tests authentication factors as part of both hardware and security domains. Know all three categories:

| Factor Category | Definition | Examples |
|---|---|---|
| Something you know | Knowledge held by the user | Password, PIN, security question answer |
| Something you have | Physical object possessed by the user | Smart card, hardware token, one-time code device |
| Something you are | Physical characteristic of the user's body | Fingerprint, iris scan, facial geometry, voice print |

MFA requires two or more of these factors simultaneously. A smart card plus a PIN uses "something you have" plus "something you know" — that is two factors.

### Smart Card Readers

A smart card reader is a peripheral that reads an embedded cryptographic chip in a physical card. The chip stores a digital certificate used to authenticate the cardholder to a computer system or network.

**Government use:** The U.S. Department of Defense Common Access Card (CAC) and the civilian Personal Identity Verification (PIV) card are the most well-known implementations. Employees insert the card into a USB reader attached to their workstation, and Windows authenticates the user using the card's certificate without a traditional password.

**Corporate use:** Enterprise smart card programs issue employees cards that serve as both building access badges and computer login credentials.

**Authentication factor:** Something you have — possession of the physical card is required. If the card is not present, authentication fails regardless of password knowledge.

**Driver requirement:** Smart card readers require PC/SC (Personal Computer/Smart Card) middleware drivers. Windows includes built-in smart card support; the reader device itself typically requires a USB driver from the manufacturer.

### Biometric Scanners

Biometric scanners authenticate users based on unique physical characteristics. The most common types are:

| Type | How It Works | Common Deployment |
|---|---|---|
| Fingerprint scanner | Optical or capacitive sensor captures fingerprint ridge pattern | Laptop built-in, USB accessory, phone unlock |
| Iris scanner | Infrared camera captures iris pattern | High-security facilities, newer laptops |
| Facial recognition camera | Infrared depth camera maps facial geometry | Windows Hello on modern laptops |
| Voice recognition | Microphone captures voice print | Hands-free access systems |

**Authentication factor:** Something you are — the physical characteristic is inherent to the user's body and cannot be transferred to another person.

**Enrollment requirement:** Biometric authentication requires an initial enrollment step where the user registers their biometric sample. Windows Hello manages fingerprint and face enrollment under Settings > Accounts > Sign-in options.

---

## Section 6 — High-Yield Glossary

**USB (Universal Serial Bus):** A serial interface standard for connecting peripheral devices to a host computer. Versions include 1.1 (12 Mbps), 2.0 (480 Mbps), 3.0 (5 Gbps), 3.1 Gen 2 (10 Gbps).

**USB Type-A:** The standard flat rectangular host-side USB connector. Blue coloring indicates USB 3.0 or higher. White or black indicates USB 2.0.

**USB Type-B:** A square-profile device-side USB connector used on printers and scanners.

**USB Micro-B:** A small asymmetric connector used on smartphones and accessories from approximately 2010-2018.

**USB Type-C:** A small oval reversible connector. A connector shape specification only — does not indicate speed. Supports USB 2.0 through USB4 and Thunderbolt 3/4 depending on host port.

**Thunderbolt 3/4:** A high-speed interface from Intel using the USB-C physical connector. Supports 40 Gbps data, DisplayPort video, PCIe, and 100W power delivery over a single cable. Identified by lightning bolt icon on port or cable.

**KVM Switch (Keyboard, Video, Mouse):** A hardware device that routes one keyboard, monitor, and mouse set to multiple connected computers. Switching is via button or keyboard hotkey. OS-agnostic.

**Smart Card:** A physical card with an embedded cryptographic chip used for authentication. Represents the "something you have" MFA factor.

**Smart Card Reader:** A peripheral device that reads the cryptographic chip in a smart card. Connected via USB. Requires PC/SC drivers.

**Biometric Scanner:** A device that reads a physical characteristic of a user (fingerprint, iris, face) for authentication. Represents the "something you are" MFA factor.

**CAC (Common Access Card):** The U.S. Department of Defense smart card used for both physical building access and computer authentication.

**PIV (Personal Identity Verification):** The civilian U.S. government smart card standard.

**MFA (Multi-Factor Authentication):** An authentication method requiring two or more independent factor categories. A password alone is single-factor; a smart card plus PIN is two-factor.

**Windows Hello:** Microsoft's biometric authentication framework supporting fingerprint, iris, and facial recognition for Windows login.

**Hot-Plug:** The ability to connect or disconnect a device while the computer is powered on and have the OS detect it automatically. USB is a hot-plug interface; older interfaces like PS/2 were not.

**DisplayPort Alt Mode:** A capability of USB-C ports that allows them to output DisplayPort video signals while still being a USB-C connector. Requires the host port to support Alt Mode.

**Power Delivery (USB PD):** A USB standard that allows USB-C cables and ports to negotiate and deliver higher power levels for charging laptops and other high-power devices. USB PD 3.1 supports up to 240W.

---

## Section 7 — Certification Exam Tips

**Trap 1 — Type-C implies high speed.** The most common Module 09 exam trap: a scenario describes a device connected via USB-C performing at only 480 Mbps. Students assume Type-C means USB 3.x. The correct answer is that the host port or cable supports only USB 2.0. The connector shape has no bearing on the speed.

**Trap 2 — Thunderbolt cable in USB-C port.** A scenario may describe a user connecting a Thunderbolt cable between two devices and asking why Thunderbolt speeds are not achieved. If either the source or destination port lacks a Thunderbolt controller (no lightning bolt icon), the connection operates at USB speeds only.

**Trap 3 — KVM switch requires matching operating systems.** KVM switches are purely hardware signal switchers. They work regardless of what OS is running on connected computers. Any answer choice that restricts KVM functionality based on OS type is incorrect.

**Trap 4 — Biometric is "something you have."** Biometrics — fingerprint, iris, face — represent "something you are," not "something you have." This is a frequently tested MFA categorization error. Physical objects (cards, tokens) are "something you have."

**Trap 5 — Smart card reader performs biometric authentication.** A smart card reader reads a chip in a physical card. It does not read fingerprints or body characteristics. If the exam describes fingerprint verification, the answer is a biometric scanner, not a smart card reader.

**Trap 6 — USB 3.0 speed described in MB/s instead of Gbps.** The exam may quote transfer speeds in MB/s (megabytes per second) instead of Gbps (gigabits per second). USB 2.0 theoretical max is approximately 60 MB/s. USB 3.0 theoretical max is approximately 625 MB/s. Convert as needed: divide Gbps by 8 to get approximate GB/s.

**Trap 7 — USB version based on color alone.** While blue = USB 3.0 is a reliable rule for Type-A ports, some manufacturers use different or non-standard colors. Always verify with documentation when exact USB version matters. Color coding is a quick field heuristic, not a specification requirement.

**Trap 8 — KVM blank monitor after switching.** When a KVM switch changes correctly for keyboard and mouse but the monitor stays blank on the second computer, the cause is almost always a missing or disconnected video cable between the second PC and the KVM switch. Do not diagnose a monitor failure or an OS issue before checking physical cable connections.

---

## Section 8 — Study Checklist

- [ ] Memorize the USB version speed table: 2.0 = 480 Mbps, 3.0 = 5 Gbps, 3.1 Gen 2 = 10 Gbps, Thunderbolt 3/4 = 40 Gbps.
- [ ] Be able to identify each USB connector type (Type-A, Type-B, Mini-B, Micro-B, Type-C) by description.
- [ ] Explain in your own words why USB Type-C does not guarantee a specific transfer speed.
- [ ] Describe what a Thunderbolt port carries over one cable and how to identify a Thunderbolt port vs. a USB-C port.
- [ ] Describe what a KVM switch does, how switching is triggered, and why it is OS-agnostic.
- [ ] State the MFA factor category for a smart card (something you have) and a biometric scanner (something you are).
- [ ] Review the eight exam traps in Section 7 and be able to explain why each distractor is wrong.
- [ ] Read the peripheral devices and interfaces section in Professor Messer's CompTIA A+ study notes at professormesser.com (220-1101 section).
- [ ] Watch Professor Messer's video on USB standards and peripheral devices at professormesser.com.
- [ ] Complete the Module 09 Lab before attempting the quiz.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 free study notes and video course: professormesser.com (220-1101 section, Domains 3.2 and 1.2)
- CompTIA A+ Exam Objectives (220-1101): comptia.org (free download; review Domain 3.2 cable types and Domain 1.2 connector types)

---

## 9. Supplemental Resources

The following free resources supplement Module 09 content on USB standards, peripheral connectivity, and authentication devices.

1. **Professor Messer — CompTIA A+ Core 1 (220-1101) USB and Peripheral Devices**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Video lectures covering USB versions, connector types, Thunderbolt, KVM switches, and authentication peripherals aligned to Domain 3.2 and Domain 1.2 — the primary exam objectives for this module.

1. **USB Implementers Forum (USB-IF) — USB Developer Resources**
   URL: [https://www.usb.org/developers](https://www.usb.org/developers)
   Relevance: The official standards body for USB publishes free specification summaries, connector diagrams, and certified product lists. The USB naming convention history (USB 3.0 → 3.1 Gen 1 → 3.2 Gen 1x1) is explained in official USB-IF documentation, which is authoritative for exam questions about version naming.

1. **SpeedGuide.net — USB Speed Reference**
   URL: [https://www.speedguide.net/articles/usb-speed-reference-5569](https://www.speedguide.net/articles/usb-speed-reference-5569)
   Relevance: Concise free reference table comparing USB 1.1 through USB 3.2 Gen 2x2 speeds, connector types, and real-world throughput figures. Useful for verifying the speed hierarchy and understanding the gap between theoretical maximum and practical transfer rates.

1. **NIST SP 800-63B — Digital Identity Guidelines (Authentication)**
   URL: [https://pages.nist.gov/800-63-3/sp800-63b.html](https://pages.nist.gov/800-63-3/sp800-63b.html)
   Relevance: The National Institute of Standards and Technology's free, authoritative publication defining the three MFA factor categories (something you know, something you have, something you are) used directly in CompTIA A+ exam questions about smart cards, biometric scanners, and TOTP tokens.

1. **Plugable Technologies — Thunderbolt and USB-C Explained**
   URL: [https://plugable.com/blogs/news/thunderbolt-vs-usb-c-what-s-the-difference](https://plugable.com/blogs/news/thunderbolt-vs-usb-c-what-s-the-difference)
   Relevance: Free article clearly explaining the physical vs. protocol distinction between USB-C and Thunderbolt connectors — the most commonly tested trap on the A+ exam regarding peripheral interfaces. Includes cable identification tips and real-world compatibility scenarios.
