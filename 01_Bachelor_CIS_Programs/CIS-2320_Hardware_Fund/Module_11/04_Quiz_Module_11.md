# Quiz: Module 11 - Network Hardware & Connectors

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 2.1, Domain 2.2
**Texas Wesleyan University | Professor Nash**
**Total Questions: 10 | Points: 10 (1 point each)**

---

## Questions

### Question 1

Which category of copper cable supports 10 Gbps speeds at a maximum distance of 100 meters?

- A) Cat5
- B) Cat5e
- C) Cat6
- D) Cat6a

Correct Answer: D

- Why D is correct: Cat6a (Category 6 Augmented) is the only copper twisted-pair category that supports 10 Gbps at the full 100-meter horizontal run defined by TIA-568. It achieves this through heavier shielding, tighter conductor specifications, and larger insulation than Cat6.
- Why A is incorrect: Cat5 is a legacy standard rated for 100 Mbps at 100 meters. It is obsolete and does not support Gigabit or 10 Gigabit Ethernet.
- Why B is incorrect: Cat5e supports 1 Gbps at 100 meters. It does not support 10 Gbps at any distance.
- Why C is incorrect: Cat6 supports 10 Gbps only at distances up to 55 meters. At longer distances — including any run from 56 to 100 meters — Cat6 falls back to 1 Gbps.

---

### Question 2

Which of the following most accurately describes the difference between Cat5e, Cat6, and Cat6a?

- A) Three generations of twisted-pair Ethernet cable where Cat5e supports 1 Gbps at 100 m, Cat6 supports 10 Gbps at up to 55 m, and Cat6a supports 10 Gbps at the full 100 m — all three use the same RJ-45 connector but differ in conductor gauge, twist rate, and crosstalk shielding.
- B) Three fiber optic cable standards where Cat5e uses single-mode fiber, Cat6 uses multimode fiber, and Cat6a uses armored plenum-rated fiber for in-wall installations in commercial buildings.
- C) Three coaxial cable standards used for cable internet connections, where the category number indicates the maximum frequency the cable can carry in MHz rather than a data transfer speed.
- D) Three Power over Ethernet standards where Cat5e delivers 15.4 W, Cat6 delivers 30 W, and Cat6a delivers 60 W of power to connected devices such as IP cameras and VoIP phones.

Correct Answer: A

- Why A is correct: This accurately describes the speed, distance, and connector characteristics of all three categories as tested on the CompTIA A+ exam, including the critical Cat6 55-meter limitation for 10 Gbps operation.
- Why B is incorrect: Cat5e, Cat6, and Cat6a are all copper twisted-pair cables, not fiber optic. Fiber optic cables use entirely different connector standards (LC, SC, ST) and are categorized by core size and mode, not by Cat ratings.
- Why C is incorrect: Cat ratings apply to twisted-pair copper Ethernet cables. Coaxial cable used for cable internet is classified by RG standards (such as RG-6 and RG-59), not Cat ratings.
- Why D is incorrect: PoE power delivery levels are defined by IEEE 802.3 standards (802.3af = 15.4 W, 802.3at = 30 W, 802.3bt = 60–100 W) and are determined by the switch port's PoE budget, not by the cable category alone.

---

### Question 3

A technician is running a new Ethernet cable to a workstation 80 meters from the network closet. The organization plans to upgrade to 10 Gbps switching in the next 12 months. Which cable category should the technician install now to support the future upgrade without re-cabling?

- A) Cat5e — it supports 1 Gbps today and can be software-upgraded to 10 Gbps when the switches are replaced
- B) Cat6 — it supports 10 Gbps and will handle the 80-meter run after the switch upgrade
- C) Cat6a — it supports 10 Gbps at the full 100-meter distance and will support the planned upgrade without re-cabling
- D) Cat3 — it is the most cost-effective option and can be bonded in pairs to achieve 10 Gbps throughput

Correct Answer: C

- Why C is correct: At 80 meters, Cat6 only supports 10 Gbps up to its 55-meter limit — the run would be limited to 1 Gbps even with 10 Gbps switches. Cat6a supports 10 Gbps at up to 100 meters, making it the correct forward-compatible choice for this 80-meter run.
- Why A is incorrect: Cable categories are physical hardware standards. Cat5e cannot be software-upgraded to support 10 Gbps. The copper conductors, twist rate, and insulation physically limit Cat5e to 1 Gbps.
- Why B is incorrect: Cat6 supports 10 Gbps only at distances up to 55 meters. At 80 meters, a Cat6 cable falls back to 1 Gbps even with 10 Gbps switches installed, requiring re-cabling to achieve the target speed.
- Why D is incorrect: Cat3 is a legacy standard rated for 10 Mbps. It cannot be bonded or otherwise upgraded to achieve 10 Gbps and is not used in modern Ethernet installations.

---

### Question 4

A technician terminates a patch cable and tests it with a cable tester. Pins 1 and 2 show continuity but pins 3 and 6 fail. The cable was intended as a straight-through T568B patch cable. What is the most likely cause?

- A) The cable is a crossover cable because T568B requires pins 3 and 6 to be disconnected on one end to create the transmit/receive swap
- B) The green pair (pins 3 and 6 in T568B) was not fully inserted into the RJ-45 plug before crimping, leaving those conductors without contact with the plug's metal IDC pins
- C) The cable tester is defective and requires calibration; pins 3 and 6 always show false failures on Cat5e cables due to impedance mismatch
- D) Pins 3 and 6 are reserved for PoE power delivery and will not show continuity in a standard data cable test

Correct Answer: B

- Why B is correct: The most common cause of individual pin failures after crimping is that one or more conductors were not pushed fully forward to the front of the RJ-45 plug before the crimp was applied. The green pair occupies pins 3 and 6 in T568B and must be seated at the tip of the plug for the metal IDC pins to pierce the wire insulation and make contact.
- Why A is incorrect: T568B straight-through cables use all eight pins on both ends. A crossover cable swaps the green and orange pairs between ends but all pins still carry a signal — no pins are intentionally disconnected in any correctly made Ethernet cable.
- Why C is incorrect: Cable testers reliably detect open circuits on individual pins. A consistent failure on specific pins indicates a physical wiring fault, not a tester calibration issue.
- Why D is incorrect: PoE uses all four pairs simultaneously including pins 3 and 6 for data. No pins are reserved exclusively for power or excluded from a standard data continuity test.

---

### Question 5

A network technician must connect two buildings with a fiber optic run of 400 meters. The connection must support 10 Gbps and minimize signal loss. Which fiber optic type and connector combination is most appropriate?

- A) Multimode fiber with ST connectors — multimode is the only fiber type compatible with ST bayonet connectors, and ST is required for runs over 300 meters
- B) Single-mode fiber with LC connectors — single-mode fiber supports longer distances with lower signal loss and LC connectors are the standard in modern enterprise fiber installations
- C) Cat6a copper with RJ-45 connectors — copper twisted-pair is preferred for outdoor inter-building runs because fiber is not rated for direct-burial installation
- D) Multimode fiber with SC connectors — multimode provides higher bandwidth than single-mode at distances under 500 meters and SC connectors are required by TIA-568 for inter-building runs

Correct Answer: B

- Why B is correct: Single-mode fiber uses a 9-micron core that allows light to travel in a single path, dramatically reducing attenuation over long distances. It supports 10 Gbps well beyond 400 meters. LC connectors are the dominant connector in current enterprise and data center fiber deployments.
- Why A is incorrect: ST connectors are not restricted to multimode fiber, and they are a legacy connector type not used in new installations. ST connectors are not required for any particular distance range.
- Why C is incorrect: Cat6a copper is limited to 100 meters maximum and cannot support a 400-meter inter-building run under any circumstances. Direct-burial rated fiber is widely available and used for outdoor inter-building runs.
- Why D is incorrect: Multimode fiber is rated for shorter distances — typically 300–550 meters at 10 Gbps depending on the fiber grade — and at 400 meters the margin is very thin. Single-mode is the appropriate choice for reliable 10 Gbps at this distance. TIA-568 does not mandate SC connectors for inter-building runs.

---

### Question 6

A technician is installing cable in the plenum space above a drop ceiling where the air-handling system circulates return air throughout the building. Which cable jacket rating is required for this installation, and why?

- A) PVC-rated cable — it is the least expensive option and sufficient for any in-building installation regardless of location
- B) Riser-rated (CMR) cable — riser cable is specifically designed for horizontal runs above drop ceilings and is required by the NEC in plenum spaces
- C) Plenum-rated (CMP) cable — fire codes require low-smoke, self-extinguishing cable in air-handling spaces because burning PVC produces toxic gases that would circulate through the HVAC system
- D) Shielded twisted-pair cable — shielded cable is required in all ceiling installations because the metal shielding provides fire resistance equivalent to plenum rating

Correct Answer: C

- Why C is correct: Plenum-rated (CMP) cable uses a fluoropolymer jacket that produces minimal smoke and is self-extinguishing. The National Electrical Code requires it in air-handling plenum spaces because toxic fumes from burning standard PVC cable would be distributed throughout the building by the HVAC system.
- Why A is incorrect: PVC-rated cable produces toxic chlorine gas when burned and is explicitly prohibited by fire code in plenum spaces. Its lower cost does not override code compliance requirements.
- Why B is incorrect: Riser-rated cable is designed to prevent vertical flame spread between floors in conduit runs — it is not approved for plenum (air-handling) spaces. Riser rating is a lower standard than plenum rating.
- Why D is incorrect: Shielded twisted-pair cable addresses electromagnetic interference, not fire safety. Shielded cable does not carry a plenum fire rating unless it is also specifically rated CMP; the shielding alone provides no fire resistance equivalent.

---

### Question 7

Which of the following correctly describes the physical difference between an RJ-45 and an RJ-11 connector, and identifies the correct application for each?

- A) RJ-45 is an 8P8C connector used for Ethernet data connections; RJ-11 is a 6P2C connector used for telephone and DSL lines. RJ-45 is wider than RJ-11, and an RJ-11 plug can fit loosely into an RJ-45 socket but will not create a valid data connection.
- B) RJ-45 and RJ-11 are both 8-contact connectors; RJ-45 is used for Ethernet and RJ-11 is used for Ethernet over telephone wiring. They are electrically identical but physically differ in color — RJ-45 is gray and RJ-11 is yellow by industry convention.
- C) RJ-11 is the larger connector used for Ethernet and supports all four twisted pairs; RJ-45 is the smaller connector used for telephone lines and carries only two conductors. RJ-45 was replaced by RJ-11 in modern Ethernet installations after 2010.
- D) RJ-45 uses a bayonet twist-lock mechanism while RJ-11 uses a push-pull latch. Both carry data and both are compatible with Gigabit Ethernet switches; the choice depends only on the wall jack type already installed.

Correct Answer: A

- Why A is correct: This accurately describes the pin count (8P8C vs 6P2C), width, and application for each connector. The physical fit of RJ-11 into an RJ-45 socket is a real-world installation trap that the A+ exam tests directly.
- Why B is incorrect: RJ-45 and RJ-11 are not electrically identical. RJ-45 carries eight conductors for four twisted pairs; RJ-11 carries two active conductors. They are not color-coded by convention.
- Why C is incorrect: RJ-45 is the larger, 8-contact connector used for Ethernet. RJ-11 is smaller and used for telephone. The description reverses the two connectors entirely.
- Why D is incorrect: RJ-45 and RJ-11 are modular connectors with plastic locking tabs, not bayonet or push-pull fiber-style connectors. RJ-11 is not compatible with Gigabit Ethernet and cannot replace RJ-45 in any Ethernet installation.

---

### Question 8

A technician is adding a new LC fiber patch cable to a server's SFP+ port in a data center. When looking at a duplex LC cable, what do the two connectors represent, and does the orientation matter?

- A) The two connectors represent the power and ground conductors of the fiber link; they must be connected with the power connector on the left and the ground connector on the right, matching the SFP+ port polarity markings.
- B) The two connectors carry the transmit (Tx) and receive (Rx) fiber strands respectively; orientation matters because the Tx strand from one device must connect to the Rx port of the other device, and the connectors are typically marked or color-coded.
- C) The two connectors are redundant and carry identical signals for failover; either connector can be plugged into either port of the SFP+ transceiver because the equipment auto-detects which fiber is active.
- D) The two connectors represent two independent Gigabit Ethernet channels that bond together for 2 Gbps throughput; they must both be connected simultaneously for the link to initialize at full speed.

Correct Answer: B

- Why B is correct: Duplex fiber optic links require separate transmit and receive fibers. The Tx output of one device must connect to the Rx input of the other device across the link. LC duplex connectors are typically marked with A/B, colored differently, or have a polarity key to indicate which strand is Tx and which is Rx. Swapping them results in a link-down condition.
- Why A is incorrect: Fiber optic cables carry light signals, not electrical power or ground. There are no power and ground conductors in a fiber cable, and SFP+ transceivers do not have power/ground polarity markings for the fiber connectors.
- Why C is incorrect: The two fibers in a duplex pair carry different signals (Tx and Rx) and are not redundant. Connecting them to the wrong ports results in no link, not automatic failover.
- Why D is incorrect: A duplex fiber link is a single full-duplex channel — one fiber for each direction — not two bonded Ethernet channels. Link aggregation involves multiple complete cable links, not the two fibers of a single duplex connection.

---

### Question 9

A new technician crimps ten patch cables for a wiring closet installation. After testing all ten, three cables show a reversed pair condition — the tester shows that pins 1 and 2 are swapped and pins 3 and 6 are swapped compared to the expected T568B result. What is the most likely cause?

- A) The technician used Cat6a cable, which reverses pin positions 1 and 2 by design to accommodate the heavier conductors used in augmented-category cables
- B) The technician accidentally wired one end of those three cables using T568A instead of T568B, producing a partial crossover rather than a consistent straight-through pinout
- C) The cable tester has incorrect reference settings and is displaying reversed results for all Cat5e cables regardless of how they are wired
- D) The RJ-45 plugs were inserted upside-down on the failed cables, which reverses the physical contact order and produces a reverse reading on the tester

Correct Answer: B

- Why B is correct: T568A and T568B differ precisely in that the orange pair (pins 1/2) and green pair (pins 3/6) are swapped. If one end is wired T568A and the other T568B, the tester will show those specific pins appearing crossed or reversed — which is the exact symptom described. This is the definition of an unintentional partial crossover.
- Why A is incorrect: Cat6a does not change pin assignments. The T568A and T568B standards apply identically to Cat5e, Cat6, and Cat6a. There is no category-specific reversal of pin positions.
- Why C is incorrect: A cable tester reporting a reversed pair would show this on every cable tested if the reference were wrong. Three out of ten cables failing with the same pattern indicates a wiring error on those specific cables, not a tester malfunction.
- Why D is incorrect: RJ-45 plugs are keyed and can only be inserted in one orientation — the retaining tab and the gold pins are on fixed sides. An upside-down insertion is physically prevented by the plug geometry.

---

### Question 10

Which fiber optic connector type uses a bayonet-style twist-lock coupling mechanism, has a round body with a protruding ceramic ferrule, and is most commonly found in enterprise wiring installations from the 1990s and early 2000s?

- A) LC (Lucent Connector) — the compact push-pull connector used on modern SFP transceivers and high-density patch panels
- B) SC (Subscriber Connector) — the square-bodied push-pull connector common in data centers and ISP fiber-to-the-premises installations
- C) ST (Straight Tip) — the round, bayonet-coupled legacy connector found in older enterprise campus fiber installations
- D) MTP/MPO (Multi-fiber Push-On) — the high-density connector that terminates 12 or 24 fibers in a single plug, used in modern parallel-optics data center cabling

Correct Answer: C

- Why C is correct: The ST (Straight Tip) connector is uniquely identified by its round cylindrical body and bayonet twist-lock mechanism. It is a legacy connector still present in buildings wired in the 1990s and early 2000s and is no longer used in new installations.
- Why A is incorrect: The LC connector uses a push-pull latch mechanism, not a bayonet twist-lock. LC is a small, modern connector associated with current enterprise and data center environments — the opposite of what is described.
- Why B is incorrect: The SC connector has a square body and uses a push-pull mechanism, not a round body or bayonet coupling. SC is used in older data centers and ISP installations but is physically distinct from ST.
- Why D is incorrect: MTP/MPO connectors are multi-fiber, high-density connectors used in modern parallel-optics cabling inside data centers. They are rectangular, much larger than ST, and use a completely different coupling method. MTP/MPO is not a primary exam topic on A+ Core 1.

---

### Question 11

A network technician is installing a new gigabit switch in a small office. All existing cables from wall jacks to workstations are Cat5 (not Cat5e). The switch supports 1000BASE-T (Gigabit Ethernet). What is the most likely result when the workstations are connected?

- A) The workstations will connect at 1 Gbps because Cat5 cable physically carries the frequency required for Gigabit Ethernet
- B) The workstations will connect at 100 Mbps at most, because Cat5 cable is only rated to support Fast Ethernet (100BASE-TX), not the four-pair signaling required for Gigabit Ethernet
- C) The workstations will fail to connect entirely because Gigabit switches will not negotiate down to lower speeds
- D) The workstations will connect at 1 Gbps, but cable runs longer than 10 meters will experience packet loss

Correct Answer: B

- Why B is correct: Cat5 cable is rated for 100 Mbps (100BASE-TX). Gigabit Ethernet (1000BASE-T) requires all four pairs to be used simultaneously with higher-frequency signaling that Cat5 does not reliably support. The switch and NIC will auto-negotiate down to 100 Mbps, which is the maximum reliable speed for Cat5.
- Why A is incorrect: While Cat5 wire can physically carry some higher-frequency signals, it is not tested or certified to the crosstalk and attenuation specifications required for 1000BASE-T. Connecting at 1 Gbps reliably on Cat5 is not guaranteed and is not the expected outcome in a standards-compliant installation.
- Why C is incorrect: Gigabit Ethernet switches support auto-negotiation (IEEE 802.3u) and will negotiate down to 100 Mbps or even 10 Mbps with lower-capability cables and devices. A complete connection failure is not the expected result.
- Why D is incorrect: Cat5 cable limitations are related to frequency and crosstalk specifications, not a specific distance threshold below 100 meters. The 100-meter maximum segment length applies equally to Cat5, Cat5e, and Cat6.

---

### Question 12

A technician needs to connect a PC directly to another PC for a file transfer without a switch or router. The PC NICs support auto-MDI/MDIX. Which cable type should the technician use?

- A) A rollover (console) cable, because peer-to-peer PC connections always require a rollover cable to prevent signal collisions
- B) Either a straight-through or a crossover cable — auto-MDI/MDIX on both NICs will automatically detect the cable type and adjust the transmit and receive pairs accordingly
- C) A crossover cable only, because straight-through cables require a switch in the signal path to route packets correctly between two end devices
- D) A fiber patch cable with LC connectors, because copper Ethernet cables cannot carry data between two PCs at distances greater than one meter

Correct Answer: B

- Why B is correct: Auto-MDI/MDIX (IEEE 802.3ab) is a NIC feature that automatically detects whether the connected cable is straight-through or crossover and reconfigures the internal transmit/receive pairs to match. When both NICs support auto-MDI/MDIX, either cable type works for a direct PC-to-PC connection.
- Why A is incorrect: A rollover cable is a Cisco console management cable with a specific pinout (pin 1 to pin 8, pin 2 to pin 7, etc.) used to connect a serial terminal to a router or switch console port. It is not used for Ethernet data transfer between PCs.
- Why C is incorrect: While a crossover cable was historically required for direct PC-to-PC Ethernet connections (before auto-MDI/MDIX), modern NICs with auto-MDI/MDIX make the distinction unnecessary. A straight-through cable works equally well when both NICs support this feature.
- Why D is incorrect: Copper Ethernet cables (Cat5e and above) support 1000BASE-T at distances up to 100 meters. A fiber patch cable is not required for short direct connections between PCs, and LC fiber connectors require matching fiber NICs or transceivers that standard PCs do not have.

---

### Question 13

A technician is troubleshooting intermittent connectivity on a newly installed Cat6 cable run that is 95 meters long. The cable passes through a server room with 3-phase electrical panels. Which factor is most likely causing the intermittent issues?

- A) The cable run is approaching the 100-meter maximum length limit, and Cat6 cable degrades linearly beyond 90 meters for any installation
- B) Electromagnetic interference (EMI) from the nearby electrical panels is inducing noise on the unshielded cable; the solution is to reroute the cable away from the panels or replace it with shielded twisted pair (STP/F-UTP) cable
- C) Cat6 cable is not compatible with server room environments because the temperature fluctuations cause the insulation to expand and contract, breaking the conductor connections
- D) The 95-meter run requires a signal repeater to be installed at the 50-meter midpoint because Cat6 cable can only carry data reliably at half the standard maximum distance in electrically noisy environments

Correct Answer: B

- Why B is correct: Electrical panels and motors generate significant EMI that can couple into adjacent unshielded twisted pair (UTP) cables, causing noise and packet errors at any cable length. Shielded cable (STP, F-UTP, or S/FTP) provides a grounded shield that blocks EMI. Rerouting away from EMI sources is the preferred solution when possible.
- Why A is incorrect: Cat6 cable does not degrade linearly at a specific sub-100-meter threshold. The 100-meter limit is based on signal attenuation across the full run; a 95-meter run within specification does not have inherently elevated error rates based on length alone.
- Why C is incorrect: Cat6 cable is rated for a broad temperature range and is used in server rooms routinely. Temperature fluctuation does not break conductors within standard operating environments.
- Why D is incorrect: Ethernet does not use signal repeaters at cable midpoints. A repeater or switch would be used to extend runs beyond 100 meters, but a 95-meter run does not require one — the issue here is EMI, not distance.

---

### Question 14

Which of the following correctly describes the purpose of an SFP (Small Form-factor Pluggable) transceiver in a network switch?

- A) An SFP is a cooling module that attaches to high-speed switch ports to prevent overheating when the switch operates at 10 Gbps line rate
- B) An SFP is a hot-swappable module that converts between electrical signals and the optical or copper signaling required by a specific cable type, allowing a single switch model to support multiple media types (multimode fiber, single-mode fiber, or copper) by swapping the appropriate SFP
- C) An SFP is a firmware chip installed on a switch motherboard that stores the MAC address table and spanning tree protocol configuration for each port
- D) An SFP is a passive cable adapter that converts an RJ-45 port on a switch to an LC fiber connector without any active electronic components

Correct Answer: B

- Why B is correct: SFP (Small Form-factor Pluggable) transceivers are hot-swappable media modules inserted into SFP cages on switches, routers, and other network equipment. Each SFP module contains the electro-optical components for a specific interface type (e.g., 1000BASE-SX for multimode fiber, 1000BASE-LX for single-mode fiber, or 1000BASE-T for copper). Swapping SFPs allows one switch model to support many different link media types.
- Why A is incorrect: SFP modules are not cooling components. Heat management in switches is handled by internal fans and chassis airflow design, not by port-mounted modules.
- Why C is incorrect: MAC address tables and spanning tree protocol state are maintained by the switch's CPU and ASIC logic, stored in volatile memory on the switch's main board. This function is entirely unrelated to SFP modules.
- Why D is incorrect: An SFP transceiver is an active electronic device — it contains a laser (for fiber) or signal conditioning electronics (for copper). A passive adapter cannot convert between fundamentally different signaling methods such as electrical-to-optical.

---

### Question 15

A technician connects a patch cable from a wall jack to a laptop and gets no link light on the NIC or the switch port. The same cable works in a different wall jack. The laptop works when connected directly to the switch. What is the most likely cause?

- A) The laptop NIC is failing because the link light absence proves the NIC cannot detect any signal regardless of cable or switch port
- B) The patch panel port corresponding to the problematic wall jack has a broken or unpunched conductor; the physical wall-to-patch-panel cable run or punch-down connection is faulty
- C) The switch port assigned to that wall jack must be administratively disabled in the switch configuration and requires a managed switch interface to re-enable it
- D) The Cat6 cable run from the wall jack to the patch panel exceeds 100 meters and must be replaced with a fiber run to support that distance

Correct Answer: B

- Why B is correct: The troubleshooting results isolate the fault to the specific wall jack infrastructure: the same cable works in another jack, and the laptop works with a direct connection. The fault is in the physical path between that wall jack and its patch panel termination — a broken conductor at the punch-down block, an unpunched pair, or a damaged run segment are all possible causes.
- Why A is incorrect: The laptop NIC successfully establishes a link when connected directly to the switch, confirming the NIC is functional. The fault is specific to the wall jack path, not the NIC.
- Why C is incorrect: An administratively disabled switch port would still affect direct connections in the same way. More importantly, the troubleshooting shows the laptop connects directly to the switch, which suggests the switch port itself is not the issue.
- Why D is incorrect: Standard office cable runs from wall jacks to patch panels are typically 10-15 meters. A 100-meter run would be unusual in a standard office environment and would be identified during initial installation, not discovered through this specific symptom pattern.

---

### Question 16

A network administrator needs to connect two buildings 300 meters apart. Copper Ethernet cable cannot be used. Which physical media type is appropriate?

- A) Cat6a with signal boosters every 100 meters — Cat6a supports extended runs with in-line amplifiers
- B) Single-mode fiber optic cable — it supports distances of several kilometers at Gigabit and 10 Gigabit speeds, well beyond the 100-meter copper Ethernet limit
- C) Coaxial cable (RG-6) — it supports longer distances than twisted pair and is the standard for inter-building connections
- D) USB 3.2 Gen 2 Active Extension cable — active USB cables extend the 100-meter Ethernet limitation for distances up to 300 meters

Correct Answer: B

- Why B is correct: Single-mode fiber optic cable supports Ethernet distances of several kilometers (1000BASE-LX supports up to 5 km; 10GBASE-LR supports up to 10 km). For 300-meter inter-building links, single-mode fiber is the correct and standard solution. Multimode fiber (1000BASE-SX) could also work for 300 meters depending on the cable grade.
- Why A is incorrect: Cat6a copper Ethernet has a hard maximum segment length of 100 meters regardless of repeaters or boosters. In-line amplifiers do not extend the Ethernet standard copper distance limitation because the 100-meter limit is based on signal quality standards, not simple signal strength.
- Why C is incorrect: Coaxial cable (RG-6) is used for cable TV (CATV) and DOCSIS cable modem connections, not for standard Ethernet interconnects between buildings. Modern Ethernet does not use coaxial cable for access network connections.
- Why D is incorrect: USB is a peripheral interface protocol, not a network infrastructure protocol. USB extension cables cannot carry Ethernet or replace fiber for building-to-building network connections.

---

### Question 17

A technician is testing a newly terminated Cat6 cable with a wire map tester and sees the following result: pairs 1-2 and 3-6 show as crossed. Pairs 4-5 and 7-8 test correctly. What does this indicate?

- A) The cable has a broken conductor on pins 4 and 5 and must be reterminated from scratch
- B) One end of the cable is wired to the T568A standard and the other end is wired to the T568B standard, producing a crossover cable — which may be intentional or an error depending on the intended use
- C) The cable is correctly wired as a straight-through cable and the tester is displaying false positives due to Cat6 impedance differences
- D) The RJ-45 plugs were inserted upside-down at both ends, swapping all even and odd pins simultaneously

Correct Answer: B

- Why B is correct: T568A and T568B pin assignments differ only in that the orange pair (pins 1/2) and green pair (pins 3/6) are swapped between the two standards. A cable with T568A on one end and T568B on the other is the definition of an Ethernet crossover cable, which was historically used for direct device-to-device connections. The tester result showing exactly pins 1/2 and 3/6 crossed is the expected result for this wiring.
- Why A is incorrect: A broken conductor appears as an open circuit on the tester — the affected pin shows no continuity at all, not a crossed/swapped reading. Crossed pins indicate intentional or unintentional standard mixing, not a broken wire.
- Why C is incorrect: Cat6 cable uses the same T568A/T568B pinout as Cat5e. There are no impedance-related exceptions to the wire map test that would cause a false positive for crossed pairs.
- Why D is incorrect: Inserting an RJ-45 plug upside-down is not physically possible — the plug body and retaining clip are asymmetric and the plug will not seat or latch if inserted incorrectly.

---

### Question 18

Which of the following best explains why shielded twisted pair (STP) cable requires proper grounding to be effective?

- A) The shield in STP cable stores electrical charge from data signals to boost transmission distance, and grounding dissipates this charge safely at the end of the run
- B) The metallic shield works as an EMI barrier only when it is connected to an electrical ground; an ungrounded or improperly grounded shield can actually act as an antenna that amplifies rather than blocks interference
- C) Grounding the STP shield allows the cable to carry both data and 48V PoE power simultaneously without interference between the two signals
- D) STP cable requires grounding because the twisted pairs alone cannot prevent EMI — the ground wire carries the data signal while the twisted pairs provide redundant backup transmission

Correct Answer: B

- Why B is correct: A metallic shield blocks EMI by providing a path for induced currents to flow to ground rather than into the data conductors. If the shield is not grounded (or is grounded at only one end in certain configurations), it cannot dissipate induced currents and can instead act as an antenna that re-radiates the interference into the data pairs.
- Why A is incorrect: The shield does not store charge for distance extension. Signal attenuation in copper cables is handled by cable quality, conductor size, and proper termination — not by the shield.
- Why C is incorrect: PoE (Power over Ethernet) carries DC power on the same data pairs as data signals through phantom powering. The shield's grounding is unrelated to PoE operation; PoE works identically on both UTP and STP cables.
- Why D is incorrect: The twisted pairs are the data conductors in both UTP and STP cable. The ground wire (if present as a drain wire) assists with shield grounding but does not carry data signals. The twisted pair structure itself provides baseline noise rejection through differential signaling.

---

### Question 19

A company is installing a wireless access point in a location 60 meters from the nearest network switch, and there is no power outlet nearby. Which technology allows the access point to receive both data connectivity and electrical power over a single Cat6 cable from the switch?

- A) USB Power Delivery (USB PD) — the Cat6 cable is terminated with USB-C adapters at both ends to carry 65W of power alongside the Ethernet signal
- B) Power over Ethernet (PoE) — IEEE 802.3af/at/bt standards allow Ethernet switches with PoE capability to deliver DC power over the same twisted pair cable used for data, eliminating the need for a separate power outlet at the access point
- C) Modular AC injection — a device installed at the patch panel injects 120V AC onto the unused pairs in the Cat6 cable, which the access point's internal transformer converts to the required DC voltage
- D) The switch's spanning tree protocol (STP) reserves two pairs in the Cat6 cable for power delivery when it detects a PoE-capable device; no additional hardware is required beyond the standard switch

Correct Answer: B

- Why B is correct: Power over Ethernet (PoE) is the IEEE 802.3 standard for delivering DC power over Ethernet cables to powered devices (PDs) such as wireless access points, IP cameras, and VoIP phones. A PoE-capable switch provides both data and power over the same Cat5e/Cat6 cable without requiring a separate AC outlet at the device location.
- Why A is incorrect: USB Power Delivery is a USB charging protocol for USB-C devices. It is not used with Cat6 Ethernet cabling and does not integrate with Ethernet networking infrastructure. Ethernet cabling cannot be terminated with USB-C connectors.
- Why C is incorrect: Injecting 120V AC onto Ethernet cable pairs would destroy the cable, the switch port, and any connected devices. PoE uses carefully regulated low-voltage DC (typically 48V nominal) delivered over the data pairs within strict IEEE current limits.
- Why D is incorrect: Spanning tree protocol (STP) is a Layer 2 network loop-prevention protocol that has nothing to do with power delivery. PoE detection and power delivery is handled by the switch's PoE controller circuitry, not by spanning tree protocol.

---

### Question 20

A technician is setting up a small office network and is deciding between a managed switch and an unmanaged switch. The office has 12 workstations and one VoIP phone system that requires QoS (Quality of Service) prioritization. Which switch type is required, and why?

- A) An unmanaged switch is sufficient because QoS is handled entirely by the router and the switch only forwards frames based on MAC addresses without any quality-of-service awareness
- B) A managed switch is required because QoS (Quality of Service) configuration — including 802.1p traffic prioritization, DSCP marking, and port-based priority queuing — is a management feature only available on managed switches
- C) A managed switch is required only if the office has more than 24 ports; a 12-port unmanaged switch can be configured for QoS through the Windows Network and Sharing Center on each workstation
- D) An unmanaged switch supports QoS automatically for any device that uses RJ-45 connectors, because the RJ-45 standard includes QoS signaling in its pin assignments

Correct Answer: B

- Why B is correct: Quality of Service (QoS) requires the switch to prioritize certain traffic types (such as VoIP audio) over others (such as bulk file transfers) using IEEE 802.1p priority bits or DSCP markings. This requires per-port configuration, priority queuing, and traffic classification — all management features exclusive to managed switches. An unmanaged switch forwards all frames equally with no traffic prioritization capability.
- Why A is incorrect: While routers can perform some QoS functions at Layer 3, VoIP QoS within a LAN segment requires Layer 2 priority handling at the switch level. An unmanaged switch cannot differentiate or prioritize traffic types regardless of router configuration.
- Why C is incorrect: Windows network settings can mark traffic with DSCP values, but those markings are only honored by managed network equipment that reads and acts on them. An unmanaged switch ignores all QoS markings. The port count is irrelevant to QoS capability.
- Why D is incorrect: RJ-45 is a physical connector standard that defines pin assignments for electrical connections only. It has no protocol-level QoS signaling capability. QoS is a software and ASIC function of the switch hardware, not a property of the connector.
