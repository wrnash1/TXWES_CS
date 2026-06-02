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
