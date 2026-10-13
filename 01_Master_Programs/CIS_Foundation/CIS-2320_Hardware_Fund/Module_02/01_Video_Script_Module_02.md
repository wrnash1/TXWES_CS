# Video Script: Module 02 - Motherboards and Form Factors

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Estimated Duration:** 22-24 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5: Given a scenario, install and configure motherboards, CPUs, and add-on cards
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

**SHOW COMPONENT cues** indicate points where the camera should cut to or overlay a close-up of the physical component being described. Have the following components staged before recording:

- One full-size ATX motherboard (any generation)
- One Micro-ATX motherboard
- One Mini-ITX motherboard (if available; otherwise use reference image)
- A ruler or measuring tape for dimension demonstration
- A PCIe x1, x4, and x16 card or slot close-up image
- A CR2032 CMOS battery
- A CMOS clear jumper block

**Key exam traps to call out explicitly during recording:**

- PCIe physical backward compatibility (smaller card fits larger slot — allowed)
- CMOS battery symptom (date/time reset, not a no-boot scenario)
- Micro-ATX fits ATX cases, but Mini-ITX does NOT reliably fit ATX cases without an adapter

**Safety notes:**

- Remind students to use an ESD strap or touch a grounded metal surface before handling any motherboard
- Never force-insert an expansion card; align the card with the slot guide rail before seating

---

## Section 1: Introduction and Certification Alignment [00:00 - 03:30]

**[CAMERA: Instructor on camera, title card "Module 02 — Motherboards and Form Factors" displayed behind or overlaid]**

"Welcome back, class. I am Professor Nash, and this is CIS-2320 Hardware Fundamentals at Texas Wesleyan University. Today we are covering Module 02: Motherboards and Form Factors.

This is one of the most important modules in the course, and it is tested heavily on the CompTIA A+ Core 1 exam under Domain 3.5. If you are planning to sit for your A+ certification — and you should be — you will see motherboard form factor and expansion slot questions. Guaranteed.

Here is what we are going to cover today. First, motherboard form factors: ATX, Micro-ATX, and Mini-ITX. Second, chipsets and what they actually do. Third, expansion slots — specifically PCIe and how lane counts affect what cards you can use. Fourth, power connectors, BIOS/UEFI, and the CMOS battery. And fifth, I will walk you through exactly what to expect in this week's lab.

Let me make something clear upfront: a motherboard is not just a circuit board that things plug into. The motherboard is the central nervous system of the entire computer. It determines what CPU you can use, how much RAM you can install, what storage you can connect, and how much you can expand the system later. Choosing the wrong form factor for a build is a costly mistake a real technician cannot afford to make.

Let's get into it."

**[PAUSE — 3 seconds]**

---

## Section 2: Form Factors — ATX, Micro-ATX, and Mini-ITX [03:30 - 09:00]

**[CAMERA: Cut to component table]**

**[SHOW COMPONENT: Place ATX motherboard flat on the table. Hold up a ruler showing the 12-inch length and 9.6-inch width]**

"This is an ATX motherboard. ATX stands for Advanced Technology eXtended, and it has been the standard full-size desktop form factor since 1995. The dimensions are 12 inches by 9.6 inches. When you pick up any standard full tower or mid tower desktop case, this is the board it was designed to hold.

Count the expansion slots along the bottom edge — you will typically see five to seven PCIe slots on a full ATX board. Count the RAM slots — usually four, sometimes eight on high-end boards. That expandability is the entire reason ATX is still the dominant form factor for desktops.

The ATX standard also defines where the mounting holes go, where the rear I/O panel cutout is located, and what the 24-pin main power connector looks like. All of that is standardized so that any ATX board fits any ATX case.

**[SHOW COMPONENT: Place Micro-ATX board next to the ATX board. Show the size difference]**

Now look at this Micro-ATX board. It is 9.6 inches by 9.6 inches — a perfect square. It is smaller than ATX, but here is the critical fact for the exam: **Micro-ATX is backward-compatible with standard ATX cases.** An ATX case has extra mounting holes to accommodate the smaller Micro-ATX board. You will see this as a scenario question on the A+ exam: 'A customer wants a smaller board in their existing ATX case — which form factor should the technician use?' The answer is Micro-ATX.

The tradeoff is that Micro-ATX boards typically have four or fewer expansion slots and two to four RAM slots. They are popular for budget builds and office workstations where expandability is not a priority.

**[SHOW COMPONENT: Show Mini-ITX image or board]**

Mini-ITX is the smallest of the three. It measures 6.7 inches by 6.7 inches. These boards are designed for home theater PCs, embedded systems, and compact builds where physical space is the primary constraint. Mini-ITX boards typically have only one PCIe x16 slot and two RAM slots. They physically fit inside some ATX and Micro-ATX cases, but they are purpose-built for small form factor enclosures.

Here is the exam trap with Mini-ITX: the question might say a customer wants the smallest possible motherboard for a new compact build. Mini-ITX. But if the question says the customer wants a board that fits inside their existing standard ATX case and wants fewer slots at lower cost, that is Micro-ATX, not Mini-ITX.

**[PAUSE — 3 seconds]**

Let me give you a quick comparison to lock these numbers in."

**[CAMERA: Slide with comparison table]**

"ATX: 12 by 9.6 inches, up to 7 expansion slots, up to 8 RAM slots. Micro-ATX: 9.6 by 9.6 inches, up to 4 expansion slots, 2 to 4 RAM slots, fits ATX cases. Mini-ITX: 6.7 by 6.7 inches, 1 PCIe x16 slot, 2 RAM slots, requires SFF case or adapter. Write that table down. It will be on the quiz."

---

## Section 3: Chipsets [09:00 - 13:30]

**[CAMERA: Slide showing a motherboard diagram with chipset labeled]**

"Now let's talk about chipsets. If the CPU is the brain of the computer, the chipset is the brain's management team. It is a group of integrated circuits — historically two chips called the Northbridge and Southbridge, but in modern systems it has been consolidated into a single chip called the Platform Controller Hub, or PCH.

The chipset manages all of the data traffic between the CPU and everything else: RAM, storage controllers, USB ports, audio, expansion slots. Think of it as a traffic controller at a busy intersection. Without the chipset, the CPU would have no organized way to communicate with any peripheral.

Here is why the chipset matters for your job as a technician: **the chipset determines CPU compatibility.** If a customer brings in a board and says they want to upgrade their processor, the first thing you check is the chipset. An Intel Z790 chipset supports 12th and 13th generation Intel Core processors in an LGA1700 socket. An AMD X670 chipset supports Ryzen 7000 series processors in an AM5 socket. You cannot swap an Intel CPU into an AMD board and vice versa — the socket and chipset are entirely different.

The chipset also determines what features are available: how many USB ports, whether the board supports PCIe 5.0, whether overclocking is unlocked. Two boards with the same socket but different chipsets can have very different capabilities. A Z-series Intel chipset unlocks overclocking; a B-series Intel chipset does not.

For the A+ exam, you do not need to memorize every chipset model number. You need to understand what the chipset does — manage communication between the CPU and peripherals — and that it determines CPU and feature compatibility. That is the testable knowledge."

**[PAUSE — 3 seconds]**

---

## Section 4: Expansion Slots — PCIe and Lane Counts [13:30 - 18:30]

**[CAMERA: Close-up of motherboard PCIe slots]**

**[SHOW COMPONENT: Point to each slot type on the board]**

"PCI Express, or PCIe, is the standard interface for expansion cards. Every GPU, NVMe adapter, Wi-Fi card, and most sound cards connect to the motherboard via a PCIe slot. Let me show you the slot types.

**[SHOW COMPONENT: Point to the short x1 slot]**

This is a PCIe x1 slot. It is the shortest physical slot on the board. x1 means one lane of PCIe bandwidth. With PCIe 3.0, that is about 1 GB/s of throughput. These slots are used for single-function cards — sound cards, basic network cards, certain SSDs.

**[SHOW COMPONENT: Point to the x4 and x8 slots]**

The medium-length slots are x4 and x8. Four lanes or eight lanes respectively. PCIe 3.0 x4 gives you about 4 GB/s. These are used for NVMe SSD adapter cards, RAID controllers, and some network cards.

**[SHOW COMPONENT: Point to the long x16 slot]**

This is the PCIe x16 slot — the long one. Sixteen lanes. With PCIe 4.0, that is up to 32 GB/s bidirectional. This is where graphics cards go. GPUs require the full bandwidth of an x16 slot to perform properly.

Here is the backward compatibility rule, and this is absolutely an exam question: **A smaller PCIe card physically fits into a larger PCIe slot, and it will work.** An x1 card will fit and operate in an x16 slot. The card will only use one lane of bandwidth, but it is electrically compatible and will function. The exam might describe a technician inserting an x1 Wi-Fi card into an x16 slot because that is the only open slot — that is a valid installation.

The reverse is not true by default. An x16 card requires an x16 slot. You cannot insert a full-size GPU into an x1 slot — it will not physically fit.

**[PAUSE — 3 seconds]**

One more thing about PCIe: generations. PCIe 3.0, 4.0, and 5.0 are all physically the same connector. An older PCIe 3.0 card inserted into a PCIe 4.0 slot will negotiate down to PCIe 3.0 speed and operate correctly. This cross-generation compatibility is by design. The exam may test whether you know that a newer card in an older slot will still function — it will, just at the lower generation's bandwidth."

---

## Section 5: Power Connectors, BIOS/UEFI, and CMOS Battery — Lab Prep [18:30 - 22:00]

**[CAMERA: Return to component table]**

**[SHOW COMPONENT: 24-pin ATX power connector on board]**

"Two more areas you need to know for the exam and for the lab this week: the power connectors and the CMOS battery.

The main motherboard power connector is a 24-pin ATX connector from the power supply. This supplies power to the entire board. There is also a separate 4-pin or 8-pin CPU power connector near the CPU socket — this supplies power specifically to the processor. Both connectors must be connected for the system to POST. A common mistake when assembling a system is connecting the 24-pin but forgetting the CPU power connector — the board will either not start or will start and immediately shut down.

**[SHOW COMPONENT: CMOS battery on the board — small silver coin cell]**

Now, the CMOS battery. This is a CR2032 lithium coin cell battery. Its job is to maintain the BIOS or UEFI settings — including the date, time, and boot order — when the system is completely unplugged from wall power. When the CMOS battery dies, the system resets the clock to a default date every time it boots. That is the symptom: incorrect date and time on every startup, usually combined with a CMOS checksum error message during POST.

**[SHOW COMPONENT: CMOS clear jumper — point to the three-pin jumper block near the battery]**

Adjacent to the CMOS battery you will typically find a CMOS clear jumper. This is a three-pin jumper block. Moving the jumper from its default position — pins 1 and 2 — to the clear position — pins 2 and 3 — and then back will reset all BIOS settings to factory defaults. Technicians use this when a BIOS password is forgotten or settings are misconfigured and the system will not boot. You will locate this jumper during the lab.

In this week's lab, you will examine a motherboard and document the form factor, identify each PCIe slot by type, locate the CMOS battery and clear jumper, and answer analysis questions about component compatibility. Your completed observation table and answers are your deliverable. Read the lab instructions carefully before you start."

---

## End Card [22:00 - 23:00]

**[CAMERA: Instructor on camera]**

"That covers Module 02. Let's recap the key points. ATX is 12 by 9.6 inches — the standard desktop form factor. Micro-ATX is 9.6 by 9.6 inches, smaller but backward-compatible with ATX cases. Mini-ITX is 6.7 by 6.7 inches, compact, one PCIe x16 slot, for SFF builds only. The chipset manages CPU-to-peripheral communication and determines CPU compatibility. PCIe x16 is for graphics cards; smaller cards fit larger slots but not the reverse. The CMOS battery maintains date and time; a dead battery means reset clock settings on every boot.

Complete the reading guide, take the quiz, and submit the lab by the due dates in Canvas. The discussion post is due Wednesday night.

I will see you in Module 03, where we will open up the CPU conversation and talk about everything from socket types to thermal paste. See you then."

---

## Additional Resources

- [Professor Messer CompTIA A+ Core 1 (220-1101) free course — motherboard and form factor sections](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- [CompTIA A+ Core 1 official exam objectives (Domain 3.5)](https://www.comptia.org/certifications/a)
