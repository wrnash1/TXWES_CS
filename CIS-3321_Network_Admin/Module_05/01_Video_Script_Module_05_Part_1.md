# Video Script: Module 05 – Network Infrastructure: Cables, Switches, Routers
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 1 of 2 | Estimated Duration: 13–15 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CIS-3321 Network Administration | Module 05: Network Infrastructure — Cables, Switches, and Routers | Texas Wesleyan University"]

---

### Section 1: Introduction

[00:00 – 01:00]

[SHOW SLIDE: Professor Nash on camera with module title card]

Welcome to Module 05. I'm Professor Nash. We have spent four modules on addressing models, protocols, and logical addressing. Now we get physical. In this module, we look at the actual hardware that makes networks run: the cables, the switches, and the routers. These are the devices and media you will physically install, configure, and troubleshoot throughout your career. They also appear heavily on the Network+ exam — both in theoretical questions and in troubleshooting scenarios.

Part 1 covers copper cabling standards and fiber optic fundamentals. Part 2 covers switch operation, router function, and specialty devices like Layer 3 switches and PoE.

---

### Section 2: Copper Cabling — Twisted Pair

[01:00 – 05:30]

[SHOW DIAGRAM: A cross-section diagram of a twisted-pair Ethernet cable. Shows the outer jacket, four pairs of twisted copper wires inside, with each pair color-coded (orange, blue, green, brown). Labels identify the RJ-45 plug at one end.]

[Alt-text: A cross-section diagram of a Cat6 Ethernet cable. The outer jacket is removed to reveal four color-coded twisted wire pairs: orange and white-orange, blue and white-blue, green and white-green, brown and white-brown. An RJ-45 eight-position connector is shown at the end of the cable.]

Twisted-pair copper cable is the backbone of virtually every wired LAN in existence. You will be familiar with it as the cable that runs from your computer to a wall jack. Let's look at the specific standards.

**Cat5e** — Enhanced Category 5 cable. Cat5e supports up to 1 Gbps (Gigabit Ethernet) at the maximum distance of 100 meters. This is the absolute minimum cable category recommended for any new installation. Older Cat5 (without the "e") is limited to 100 Mbps and should not be used for new work.

**Cat6** — Category 6 cable. Cat6 supports 1 Gbps at 100 meters or 10 Gbps at up to 55 meters. The shorter 10 Gbps distance is due to alien crosstalk — interference between adjacent cables in a bundle. Cat6 uses a plastic separator (spline) between the pairs to reduce crosstalk. This is the current standard for new enterprise installations.

**Cat6a** — Augmented Category 6. Cat6a fully eliminates alien crosstalk and supports 10 Gbps at the full 100-meter distance. It is thicker and less flexible than Cat6. Cat6a is required when you need 10 Gbps between a desktop or device and the wiring closet at full 100-meter distance.

**Cat7 and Cat8** — Higher specifications than Cat6a. Cat8 supports 25–40 Gbps but only at very short distances (30 meters) and is primarily used for data center rack cabling.

The maximum segment length for twisted-pair Ethernet is 100 meters (328 feet). This is one of the most frequently tested numbers on the Network+ exam. If a cable run exceeds 100 meters, signal attenuation degrades performance and link quality. The solution is to add a network switch at or before 100 meters to regenerate the signal.

All twisted-pair Ethernet uses 8P8C connectors — commonly called RJ-45. Both ends of a standard patch cable use the same wiring standard, either T568A or T568B.

> **Network+ Exam Tip:** The 100-meter maximum is the single most important cable distance to memorize. Cat5e supports 1G at 100m. Cat6 supports 10G at 55m (not 100m). Cat6a supports 10G at 100m. These three lines cover the vast majority of cable category questions on the exam.

---

### Section 3: Fiber Optic Cabling

[05:30 – 09:00]

[SHOW DIAGRAM: Two fiber cross-sections side by side. Left: Single-mode fiber — narrow core (8–10 µm), one light ray traveling in a straight line, labeled "Long distance, laser light source." Right: Multi-mode fiber — wider core (50–62.5 µm), multiple light rays reflecting at angles, labeled "Shorter distance, LED/VCSEL light source."]

[Alt-text: Two fiber optic cross-section diagrams shown side by side. The left diagram shows single-mode fiber with a very narrow core of 8 to 10 micrometers diameter. One light ray is shown traveling in a straight line through the center. The label reads "Single-mode: long distance (100+ km), laser light source, higher cost." The right diagram shows multi-mode fiber with a wider core of 50 to 62.5 micrometers. Multiple light rays are shown entering at different angles and reflecting off the inner cladding boundary. The label reads "Multi-mode: shorter distance (up to 550 m), LED or VCSEL source, lower cost for short runs."]

Fiber optic cable transmits data as pulses of light through a glass or plastic core. It is immune to electromagnetic interference (EMI), can span much longer distances than copper, and provides higher bandwidth. However, it is more expensive to install and terminate than copper.

**Single-Mode Fiber (SMF)** — A very narrow core, typically 8–10 micrometers in diameter. The small core allows only a single mode (ray) of light to travel through the fiber. This eliminates modal dispersion (signal spreading over distance), enabling transmission over very long distances — from several kilometers to over 100 km. SMF uses laser light sources. Common connector types include LC and SC. SMF is used for campus backbone connections, WAN links, and long-haul fiber runs.

**Multi-Mode Fiber (MMF)** — A wider core, typically 50 or 62.5 micrometers. Multiple modes of light travel through the fiber simultaneously, reflecting off the inner cladding at various angles. Multiple light paths cause modal dispersion, limiting the distance before the signal degrades. MMF is rated by the OM designation — OM1 and OM2 are older standards; OM3 supports 10 Gbps at 300 meters; OM4 supports 10 Gbps at 400 meters; OM5 supports 100 Gbps at 150 meters. MMF uses LED or VCSEL (Vertical Cavity Surface Emitting Laser) light sources, which are less expensive than the lasers in SMF transceivers. MMF is used within buildings and data centers where distances are shorter.

Common fiber connector types: LC (small form factor, most common in enterprise), SC (square connector, "push-pull"), ST (bayonet-style, legacy), MTP/MPO (multi-fiber trunk cables for data centers).

> **Network+ Exam Tip:** The key distinguishing facts between SMF and MMF are core size (narrow vs. wide), light source (laser vs. LED/VCSEL), and distance capability (kilometers vs. hundreds of meters). When the exam asks about a 25-km backbone link, the answer is always SMF. When it asks about a 200-meter data center run, MMF works fine.

---

### Section 4: Cable Types — Straight-Through, Crossover, Rollover

[09:00 – 11:30]

[SHOW DIAGRAM: Three cable diagrams side by side. Left: Straight-through cable — both ends labeled T568B, connecting a PC to a Switch. Center: Crossover cable — one end T568A, one end T568B, connecting a Switch to a Switch. Right: Rollover/Console cable — labeled "console port access," shown connecting a laptop to a router's console port.]

[Alt-text: Three cable diagrams. Left: A straight-through cable with T568B on both ends connecting a PC icon to a Switch icon. Center: A crossover cable with T568B on one end and T568A on the other connecting two Switch icons, with a note "Connect like devices." Right: A flat rollover cable connecting a laptop serial or USB port to a router's RJ-45 console port, labeled "Initial configuration access."]

Beyond the category rating, cables are also differentiated by how the pairs are wired at each end.

**Straight-Through Cable** — Both ends of the cable use the same wiring standard (T568A on both ends, or T568B on both ends). Used to connect unlike devices: workstation to switch, switch to router. This is the standard patch cable you use for all typical network connections.

**Crossover Cable** — One end uses T568A and the other uses T568B. This crosses the transmit and receive pairs, allowing like devices to communicate directly: switch to switch, router to router, PC to PC. In modern networks, this is largely obsolete because virtually all network equipment supports Auto-MDIX — a feature that automatically detects the cable type and configures the port's transmit and receive pins accordingly. The exam still tests this conceptually, but you will rarely need to physically create a crossover cable.

**Rollover/Console Cable** — Also called a Cisco console cable. It is a flat cable (often light blue) with an RJ-45 connector on one end and a DB9 serial connector (or USB adapter) on the other. Pin assignments are reversed end-to-end — pin 1 connects to pin 8, pin 2 to pin 7, and so on. This cable is used exclusively to connect a PC to the console port of a Cisco router or switch for initial out-of-band configuration, before network-based remote access (SSH) is configured.

---

### Section 5: Part 1 Summary

[11:30 – 13:00]

[SHOW SLIDE: Summary bullet list]

In Part 1, we covered twisted-pair cable standards — Cat5e, Cat6, and Cat6a — with their speed and distance ratings. We examined single-mode fiber for long distances and multi-mode fiber for shorter campus and data center runs. We distinguished straight-through, crossover, and rollover cables by their wiring convention and use case.

In Part 2, we examine how switches and routers operate, how switches build and use MAC address tables, and specialty technologies like Layer 3 switches and Power over Ethernet.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 1*
