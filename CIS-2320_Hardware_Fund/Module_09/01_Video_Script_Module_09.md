# Video Script: Module 09 - Peripheral Devices and Interfaces

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Estimated Duration:** 22-24 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.2 and Domain 1.2
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

**Slides needed:**

- Slide 1: Title card — "Module 09: Peripheral Devices and Interfaces"
- Slide 2: USB version comparison table (2.0, 3.0, 3.1 Gen 1, 3.1 Gen 2, 3.2, USB4)
- Slide 3: USB connector type chart — Type-A, Type-B, Mini-B, Micro-B, Type-C (photos or diagrams)
- Slide 4: Thunderbolt version comparison (TB1 through TB4) with lightning bolt icon callout
- Slide 5: KVM switch diagram — two PCs sharing one keyboard, monitor, mouse
- Slide 6: Authentication factors chart — something you know / have / are
- Slide 7: Smart card vs. biometric scanner — use case comparison table
- Slide 8: End card with study resources

**Components to show on camera (if available):**

- [SHOW COMPONENT] USB Type-A male connector (blue USB 3.0 and white USB 2.0 side by side)
- [SHOW COMPONENT] USB Type-C cable
- [SHOW COMPONENT] Thunderbolt cable (with lightning bolt icon visible)
- [SHOW COMPONENT] USB fingerprint reader or smart card reader
- [SHOW COMPONENT] KVM switch device or diagram printout

**Key exam traps to address in the script:**

- USB Type-C is a connector shape, NOT a speed standard — a Type-C port can deliver USB 2.0 speeds
- Thunderbolt 3 and 4 use the USB-C physical connector but are not USB-C cables
- USB 3.0 blue color coding is on ports and connectors — use this to identify version quickly
- Smart card = "something you have"; biometric = "something you are" — these are tested as MFA factors
- KVM switches are hardware-agnostic; they do not require matching OS on connected computers

---

## [00:00 - 02:30] Introduction and Module Overview

[SHOW SLIDE: Title card — "Module 09: Peripheral Devices and Interfaces"]

Welcome back, class. I am Professor Nash, and this is Module 09: Peripheral Devices and Interfaces.

Today's module covers everything that connects to your PC from the outside — the cables, ports, and devices that allow you to input data, output video and audio, store files externally, and authenticate securely. These topics appear throughout the CompTIA A+ Core 1 exam under Domain 3.2 (cable types and connectors) and Domain 1.2 (peripheral ports).

I want to start with a confession: peripheral and interface topics are some of the most misunderstood on the A+ exam. Not because they are technically complex — the concepts themselves are straightforward — but because the exam is very deliberate about testing the difference between a connector's physical shape and its actual performance capability. We are going to spend significant time on that distinction today.

[PAUSE — 3 seconds]

By the end of this module you will be able to identify USB connector types by appearance, state the correct transfer speed for each USB version, explain what Thunderbolt is and how it differs from USB-C, describe what a KVM switch does and when to use one, and identify smart card readers and biometric scanners as authentication peripherals tied to specific MFA factor categories.

Let's get started.

---

## [02:30 - 08:30] Section 1 — USB Standards: Versions, Speeds, and Color Coding

[SHOW SLIDE: USB version comparison table]

[SHOW COMPONENT: USB Type-A connectors — blue 3.0 and white 2.0 side by side]

USB stands for Universal Serial Bus. It is the most widely used peripheral interface standard in computing. Every A+ technician must know the USB version hierarchy cold, because the exam will describe a scenario where a device is performing below expected speed and ask you to identify the bottleneck.

Here is the USB version hierarchy you need to memorize:

USB 1.1: Maximum speed 12 Mbps. Rarely encountered today but may appear on older equipment or in historical context questions.

USB 2.0: Maximum speed 480 Mbps. The marketing name for this is "Hi-Speed USB." This is the version you find on older ports and on budget devices. The connector is white or black on most devices.

USB 3.0: Maximum speed 5 Gbps. The marketing name is "SuperSpeed USB." This is the version most commonly identified by its blue color coding on ports and male connectors. When you see a blue USB-A port, it is USB 3.0 or higher. USB 3.0 was later renamed USB 3.1 Gen 1 and then USB 3.2 Gen 1x1 in the ever-expanding USB naming scheme — but the speed is the same: 5 Gbps.

USB 3.1 Gen 2: Maximum speed 10 Gbps. Marketing name "SuperSpeed USB 10Gbps." Also called USB 3.2 Gen 2x1 in the current naming standard. Some ports use a red or teal color coding for USB 3.1 Gen 2, but this is not universal — look for port labeling or documentation.

USB4: Maximum speed 40 Gbps. This is the newest generation and uses the USB-C connector exclusively. USB4 at 40 Gbps matches Thunderbolt 3 and 4 speeds.

[PAUSE — 2 seconds]

**A+ Exam Tip:** The exam will state a USB version by its original number — USB 2.0, USB 3.0, USB 3.1 Gen 2. Memorize the speeds: 2.0 = 480 Mbps, 3.0 = 5 Gbps, 3.1 Gen 2 = 10 Gbps, Thunderbolt 3/4 = 40 Gbps.

Now let's talk about connector shapes, because this is where students get confused.

[SHOW SLIDE: USB connector type chart]

USB Type-A: The flat rectangular connector most people recognize. This is the standard host-side connector on PCs, laptops, and hubs. USB 2.0 Type-A is white or black. USB 3.0 Type-A is blue.

USB Type-B: A square-ish connector used on devices like printers and scanners. Less common today but still appears on the exam.

USB Mini-B: A smaller connector used on older cameras and MP3 players. Largely replaced by Micro-B.

USB Micro-B: Even smaller, used on smartphones and accessories from approximately 2010-2018. Still common on budget accessories.

USB Type-C: A small, oval, reversible connector — meaning it can be inserted either way. This is the critical one. Type-C is a connector shape, not a speed standard.

[PAUSE — 2 seconds]

Write this down: A USB Type-C port may deliver USB 2.0 speeds (480 Mbps), USB 3.x speeds, or Thunderbolt speeds — entirely depending on the host controller inside the device. The connector shape tells you nothing about the speed. Read the device specifications.

---

## [08:30 - 13:30] Section 2 — Thunderbolt Interface

[SHOW SLIDE: Thunderbolt version comparison table]

[SHOW COMPONENT: Thunderbolt cable with lightning bolt icon]

Thunderbolt is a high-speed interface developed by Intel, originally in partnership with Apple. Thunderbolt 1 and 2 used the Mini DisplayPort physical connector. Starting with Thunderbolt 3, Intel switched to the USB Type-C physical connector — and this is where most of the confusion on the exam comes from.

Thunderbolt 3: 40 Gbps maximum. Uses USB-C physical connector. Can carry USB data, DisplayPort video, and PCIe signals simultaneously over a single cable. Can supply up to 100 watts of power for laptop charging. Thunderbolt 3 ports and cables are marked with a lightning bolt icon.

Thunderbolt 4: 40 Gbps maximum (same speed as TB3, but with stricter minimum requirements). All Thunderbolt 4 ports must support 40 Gbps, two 4K displays or one 8K display, USB4, and PCIe data. TB4 is essentially a more rigorous and consistent certification of TB3 capabilities.

[PAUSE — 2 seconds]

**A+ Exam Tip:** Thunderbolt 3 and 4 cables are NOT interchangeable with standard USB-C cables for full Thunderbolt performance. A standard USB-C cable plugged into a Thunderbolt 4 port will work — but at USB speeds, not Thunderbolt speeds. A Thunderbolt cable works in a USB-C port as a USB-C cable. The port and cable must both be Thunderbolt to get Thunderbolt performance.

The lightning bolt icon is your field identification tool. If the port on a laptop has a lightning bolt next to it, it is Thunderbolt. If it has only the USB trident symbol, it is USB — regardless of connector shape.

**Summary of the Type-C trap:** When the A+ exam describes a device connected via USB-C performing at only 480 Mbps, the correct diagnosis is that either the port or the cable supports only USB 2.0. The Type-C connector alone does not guarantee high speed.

---

## [13:30 - 17:30] Section 3 — KVM Switches

[SHOW SLIDE: KVM switch diagram]

KVM stands for Keyboard, Video, Mouse. A KVM switch is a hardware device that allows a single set of peripherals — one keyboard, one monitor, and one mouse — to control two or more computers by physically switching the USB and video connections between them.

Why do technicians use KVM switches? In data centers, server rooms, and multi-machine desk setups, it is impractical to have a separate keyboard, monitor, and mouse for every machine. A KVM switch lets you manage multiple systems from one console. Enterprise KVM switches can manage dozens of rack-mounted servers from a single rack-mounted console. Consumer-grade KVM switches typically handle two to four desktop computers.

How does switching work? Most KVM switches use either a physical button on the device body or a keyboard hotkey sequence — typically pressing Scroll Lock twice followed by a number key — to cycle between connected machines. When you switch, both the video signal and the USB keyboard/mouse connection are redirected to the selected computer. The other computer remains powered on but loses keyboard, mouse, and monitor access until you switch back.

[PAUSE — 2 seconds]

**A+ Exam Tip:** KVM switches are OS-agnostic. The exam may describe a KVM switch connecting a Windows machine and a Linux machine, and ask whether this is a valid configuration. It is — KVM switches pass hardware signals, not software commands. They do not care what OS is running on the connected machines.

A common troubleshooting scenario: After switching to Computer 2, the monitor shows a blank screen but keyboard and mouse work. The most likely cause is a disconnected or unseated video cable between Computer 2 and the KVM switch — not a monitor or OS failure. When USB switches correctly but video does not, follow the video cable.

---

## [17:30 - 20:30] Section 4 — Authentication Peripherals: Smart Cards and Biometrics

[SHOW SLIDE: Authentication factors chart]

[SHOW COMPONENT: USB fingerprint reader or smart card reader]

Our final topic this module is authentication peripherals — devices that help prove a user's identity to a computer system. Understanding these devices requires knowing the three multi-factor authentication (MFA) categories:

Something you know: A password, PIN, or security question answer. Knowledge-based.

Something you have: A physical object you possess — a smart card, a hardware token, a one-time code generator. Possession-based.

Something you are: A physical biometric characteristic — fingerprint, iris pattern, facial geometry, voice print. Inherence-based.

[SHOW SLIDE: Smart card vs. biometric scanner comparison table]

A smart card reader is a peripheral that reads the embedded cryptographic chip in a physical smart card. Smart cards are used in government (Common Access Card, or CAC) and corporate environments for workstation login. The card stores a cryptographic certificate that is presented to the authentication system when inserted into the reader. Because the user must physically possess the card, smart card authentication represents the "something you have" factor.

A biometric scanner reads a physical characteristic of the user's body. Fingerprint scanners are the most common — they capture the ridge pattern of a finger and compare it against an enrolled template. Iris scanners, facial recognition cameras, and voice recognition systems also fall in this category. Biometric authentication represents the "something you are" factor.

Both devices require driver installation on the host OS. Windows integrates both through the Windows Hello framework and the PC/SC standard for smart card middleware.

[PAUSE — 2 seconds]

**A+ Exam Tip:** The exam will describe a multi-factor authentication scenario and ask which factor category a given device represents. Smart card = something you have. Fingerprint = something you are. Password = something you know. These are tested precisely — do not mix them up.

A common distractor pairs a biometric scanner with "something you have." Biometrics are physical characteristics of your body — they belong to you, but they cannot be taken from you and given to someone else the way a physical card can. That distinction separates "something you are" from "something you have."

---

## [20:30 - 22:30] Closing and Lab Preview

[SHOW SLIDE: End card]

Let's recap what we covered today. USB version hierarchy: 2.0 at 480 Mbps, 3.0 at 5 Gbps with blue connectors, 3.1 Gen 2 at 10 Gbps, Thunderbolt 3/4 at 40 Gbps. USB Type-C is a connector shape only — it does not guarantee any specific speed. Thunderbolt cables and standard USB-C cables are not interchangeable for Thunderbolt performance. KVM switches share one console across multiple computers and are OS-agnostic. Smart cards = something you have. Biometrics = something you are.

Your lab for this module has three parts: identifying USB connector types and versions from photographs, analyzing a KVM setup scenario, and tracing an authentication deployment scenario through its MFA factor categories. There is no physical hardware required, but if your lab environment includes a PC, I encourage you to find and photograph at least one USB 3.0 (blue) port and one USB-C port for your own reference.

Check Canvas for lab, quiz, and discussion deadlines. For additional study, Professor Messer's free A+ Core 1 course at professormesser.com covers USB standards, Thunderbolt, and peripheral devices with excellent connector identification charts.

See you in the discussion.

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 free course notes and video: professormesser.com (navigate to 220-1101, Domain 3.2 and Domain 1.2)
- CompTIA A+ Exam Objectives (220-1101): comptia.org (free download, review Domain 3.2 and 1.2 connector and peripheral objectives)
