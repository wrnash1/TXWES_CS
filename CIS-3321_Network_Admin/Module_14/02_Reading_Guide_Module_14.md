# Reading Guide: Module 14 - Physical Layer – Cabling Standards and Installation
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 14 – Physical Layer: Cabling Standards and Installation**! The physical layer is the foundation of every network, and the CompTIA Network+ N10-009 exam tests practical cabling knowledge extensively in Domain 5.0 (Network Troubleshooting, 23%). You must know cable types, connector standards, wiring specifications (T568A/B), structured cabling components, and the tools used to install, test, and certify physical network infrastructure. This module also covers common physical layer problems and how to diagnose them.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **T568A / T568B**: Two wiring standards for terminating 8P8C (RJ-45) connectors on twisted-pair copper cable. T568B is the more common commercial standard in the US. Both ends of a cable must use the same standard for a straight-through patch cable. Mixing T568A on one end and T568B on the other creates a crossover cable.
*   **568A Pin Order**: White/Green, Green, White/Orange, Blue, White/Blue, Orange, White/Brown, Brown.
*   **568B Pin Order**: White/Orange, Orange, White/Green, Blue, White/Blue, Green, White/Brown, Brown.
*   **Horizontal Cabling**: The cabling segment from the telecommunications room (TR) patch panel to the work area outlet. Maximum distance of 90 meters for permanent link; total channel (including patch cords) = 100 meters per TIA-568 standards.
*   **Backbone Cabling**: The cabling that connects telecommunications rooms, equipment rooms, and entrance facilities within or between buildings. Also called vertical cabling.
*   **Patch Panel**: A passive termination device in the telecommunications room where horizontal cable runs are terminated on the back (110-punchdown) and patch cords connect to switches on the front. Provides a manageable cross-connect point.
*   **110 Punch-Down Tool (Krone Tool)**: A hand tool used to terminate solid copper conductors into 110 or 66 IDC (Insulation Displacement Connector) blocks and patch panels. The tool seats the conductor and cuts excess wire in one stroke.
*   **Cable Tester**: A basic tool that verifies all 8 wires in a UTP cable are connected and in the correct pin order (straight-through or crossover). Detects opens, shorts, reversed pairs, and split pairs. Does not measure attenuation or return loss.
*   **Cable Certifier**: An advanced testing instrument that measures actual cable performance against TIA/ISO category standards (Cat5e, Cat6, Cat6a). Measures attenuation, NEXT (Near-End Crosstalk), return loss, and propagation delay. Required for certifying new cabling installations.
*   **Tone Generator and Probe (Fox and Hound)**: A two-piece tool for tracing cable runs. The tone generator is connected to one end of the cable; the inductive probe is swept along the wall/ceiling/floor to detect the tonal signal emitted and locate where the cable runs.
*   **OTDR (Optical Time-Domain Reflectometer)**: A fiber optic testing instrument that sends a light pulse into a fiber and measures reflections to locate breaks, splices, bends, and connectors along the fiber run. Shows distance to faults.
*   **Fiber Optic Connectors**: Common types: LC (Lucent Connector — small form factor, common in data centers), SC (Subscriber Connector — square push-pull, common in enterprise), ST (Straight Tip — bayonet twist, legacy), MPO/MTP (multi-fiber array connector, used with ribbon fiber in high-density applications).
*   **Attenuation**: The loss of signal strength as it travels along a cable. Measured in dB. Caused by resistance, capacitance, and absorption in copper cable, or by scattering and absorption in fiber. Exceeding distance limits causes excessive attenuation and link failures.
*   **Crosstalk**: Unwanted signal coupling between adjacent twisted pairs in a copper cable. NEXT (Near-End Crosstalk) occurs at the same end as the transmitter. FEXT (Far-End Crosstalk) occurs at the opposite end. Higher cable categories have better crosstalk rejection.
*   **EMI (Electromagnetic Interference)**: Interference from external electrical sources (motors, fluorescent lights, power cables) that induces noise into copper cable. Shielded twisted pair (STP/FTP/SFTP) cables and maintaining separation from power cables mitigate EMI.
*   **Structured Cabling Components**: TIA-568 defines six subsystems: Entrance Facility, Equipment Room, Backbone Cabling, Telecommunications Room, Horizontal Cabling, and Work Area. Understanding these components helps answer exam questions about where faults occur.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** Physical layer cabling falls under **Domain 5.0 – Network Troubleshooting (23%)** and **Domain 2.0 – Network Implementations (20%)**. Cable identification, connector types, and physical troubleshooting tools are heavily tested.
*   **T568A vs T568B — what the exam tests**: You do not need to memorize every pin order, but you must know: T568B is the most common commercial standard; mixing A on one end and B on the other = crossover cable; Auto-MDIX on modern switches makes crossover cables obsolete for most uses.
*   **Horizontal cable maximum distances**: 90 meters for the permanent link (wall to patch panel), 100 meters total channel including patch cords. The exam will present a scenario with a cable run slightly over 100 meters and ask why the link is unreliable.
*   **Tool selection by task**: Terminate RJ-45 = crimper; punch down patch panel = 110 punchdown tool; test wire order = cable tester; certify Cat6a performance = cable certifier; trace cable through a wall = tone generator/probe; locate fiber break = OTDR.
*   **NEXT vs Attenuation**: NEXT is caused by crosstalk (nearby wire coupling signal), cured by proper cable category and twisting. Attenuation is signal loss over distance, cured by shortening cable runs or using fiber. The exam presents symptoms and asks which physical layer problem is occurring.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) covers cabling standards, connector types, structured cabling, and physical layer troubleshooting tools in the Network Implementations and Troubleshooting sections.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **Physical Layer Cabling and Structured Cabling Standards** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Focus on the TIA-568 structured cabling subsystems, cable category specifications, and fiber connector types.
*   **Required Video:** Watch Professor Messer's **Copper Cabling**, **Fiber Optic Cabling**, **Network Connectors**, and **Cable Management** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).

---

### Lab & Command Integration
In this week's hands-on lab, you will terminate RJ-45 connectors using T568B wiring on Cat6 cable, punch down patch panel ports using a 110 punchdown tool, verify continuity and pin order with a cable tester, practice identifying fiber connector types (LC, SC, ST) on physical samples or diagrams, and use a tone generator and probe to trace a cable run through a simulated structured cabling environment.

---

### 3. Study Checklist
*   [ ] Know T568A and T568B wiring — which creates a straight-through cable vs. crossover cable.
*   [ ] Know the horizontal cabling distance limits: 90m permanent link, 100m total channel.
*   [ ] Know all key cabling tools and their specific use cases (crimper, punchdown, tester, certifier, OTDR, tone/probe).
*   [ ] Know fiber connector types: LC, SC, ST, MPO/MTP — and their use cases.
*   [ ] Understand attenuation and crosstalk (NEXT) — causes, symptoms, and solutions.
*   [ ] Know the six TIA-568 structured cabling subsystems.
*   [ ] Read the **Physical Layer Cabling** chapters in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's cabling and connector videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
