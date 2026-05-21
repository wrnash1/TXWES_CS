# Quiz: Module 11 - Network Hardware & Connectors
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which category of copper cable supports 10 Gbps speeds at a maximum distance of 100 meters?
*   A) Cat5
*   B) Cat5e
*   C) Cat6
*   D) Cat6a
*   **Correct Answer:** D) Cat6a supports 10 Gbps up to 100m. Cat6 supports 10 Gbps only up to 55m.
*   **Distractor Analysis:**
    *   *Why correct:* Cat6a supports 10 Gbps up to 100m. Cat6 supports 10 Gbps only up to 55m.
    *   Cat5 is limited to 100 Mbps. Cat5e supports 1 Gbps.

---

**Question 2**
In the context of PC networking, which of the following most accurately describes **Cat5e vs Cat6 vs Cat6a**?
*   A) Three generations of twisted-pair Ethernet cable where Cat5e supports 1 Gbps at 100m, Cat6 supports 10 Gbps at up to 55m, and Cat6a supports 10 Gbps at the full 100m — all three use the same RJ-45 connector but differ in conductor gauge, twist rate, and crosstalk shielding.
*   B) Three fiber optic cable standards where Cat5e uses single-mode fiber, Cat6 uses multimode fiber, and Cat6a uses armored plenum-rated fiber for in-wall installations in commercial buildings.
*   C) Three coaxial cable standards used for cable internet connections, where the category number indicates the maximum frequency the cable can carry in MHz rather than a data transfer speed.
*   D) Three power over Ethernet (PoE) standards where Cat5e delivers 15.4W, Cat6 delivers 30W, and Cat6a delivers 60W of power to connected devices such as IP cameras and VoIP phones.
*   **Correct Answer:** A) Three generations of twisted-pair Ethernet cable where Cat5e supports 1 Gbps at 100m, Cat6 supports 10 Gbps at up to 55m, and Cat6a supports 10 Gbps at the full 100m — all three use the same RJ-45 connector but differ in conductor gauge, twist rate, and crosstalk shielding.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the speed, distance, and connector characteristics of Cat5e, Cat6, and Cat6a as tested on the CompTIA A+ exam, including the critical Cat6 55m limitation for 10 Gbps.
    * *Why B is incorrect:* Cat5e, Cat6, and Cat6a are all copper twisted-pair cables, not fiber optic; fiber optic cables use entirely different connector standards (LC, SC, ST) and are categorized by single-mode vs. multimode, not by Cat ratings.
    * *Why C is incorrect:* Cat ratings apply to twisted-pair copper Ethernet cables, not coaxial cables; coaxial cable used for cable internet is classified by RG standards (RG-6, RG-59), not Cat ratings.
    * *Why D is incorrect:* PoE power levels are defined by IEEE 802.3 standards (802.3af = 15.4W, 802.3at = 30W, 802.3bt = 60/100W) and apply to the switch port and cable combination, not to the cable category alone.


---

**Question 3**
A technician is running a new Ethernet cable to a workstation 80 meters from the network closet. The organization plans to upgrade to 10 Gbps switching in the next 12 months. Which cable category should the technician install now to support the future upgrade without re-cabling?
*   A) Cat5e — it supports 1 Gbps today and can be software-upgraded to 10 Gbps when the switches are replaced
*   B) Cat6 — it supports 10 Gbps and will handle the 80-meter run after the switch upgrade
*   C) Cat6a — it supports 10 Gbps at the full 100-meter distance and will support the planned upgrade without re-cabling
*   D) Cat3 — it is the most cost-effective option and can be bonded in pairs to achieve 10 Gbps throughput
*   **Correct Answer:** C) Cat6a — it supports 10 Gbps at the full 100-meter distance and will support the planned upgrade without re-cabling
*   **Distractor Analysis:**
    * *Why C is correct:* At 80 meters, Cat6 only supports 10 Gbps up to 55 meters — the run would be limited to 1 Gbps. Cat6a supports 10 Gbps at up to 100 meters, making it the correct forward-compatible choice for this 80-meter run.
    * *Why A is incorrect:* Cable categories are physical hardware standards; Cat5e cannot be software-upgraded to support 10 Gbps. The copper conductors, twist rate, and shielding of Cat5e physically limit it to 1 Gbps.
    * *Why B is incorrect:* Cat6 supports 10 Gbps only at distances up to 55 meters; at 80 meters, a Cat6 cable would fall back to 1 Gbps even with 10 Gbps switches, requiring re-cabling to achieve 10 Gbps.
    * *Why D is incorrect:* Cat3 is a legacy cable standard rated for 10 Mbps; it cannot be bonded or upgraded to achieve 10 Gbps and is not used in modern Ethernet installations.


---

**Question 4**
A technician terminates a patch cable and tests it with a cable tester. Pins 1 and 2 show continuity but pins 3 and 6 fail. The cable was intended as a straight-through T568B patch cable. What is the most likely cause?
*   A) The cable is a crossover cable because T568B requires pins 3 and 6 to be disconnected on one end to create the transmit/receive swap
*   B) The green pair (pins 3 and 6 in T568B) was not fully inserted into the RJ-45 plug before crimping, leaving those conductors without contact with the plug's metal pins
*   C) The cable tester is defective and requires calibration; pins 3 and 6 always show false failures on Cat5e cables due to impedance mismatch
*   D) Pins 3 and 6 are reserved for PoE power delivery and will not show continuity in a standard data cable test
*   **Correct Answer:** B) The green pair (pins 3 and 6 in T568B) was not fully inserted into the RJ-45 plug before crimping, leaving those conductors without contact with the plug's metal pins
*   **Distractor Analysis:**
    * *Why B is correct:* The most common cause of individual pin failures after crimping is that one or more conductors were not pushed fully forward to the front of the RJ-45 plug before the crimp was applied; the green pair occupies pins 3 and 6 in T568B and must be seated at the tip of the plug for the metal IDC pins to pierce the insulation.
    * *Why A is incorrect:* T568B straight-through cables use all eight pins on both ends; a crossover cable swaps the green and orange pairs between ends but all pins still carry a signal — no pins are intentionally disconnected.
    * *Why C is incorrect:* Cable testers are reliable for detecting open circuits on individual pins; a consistent failure on pins 3 and 6 indicates a physical wiring fault, not a tester calibration issue.
    * *Why D is incorrect:* PoE uses all four pairs simultaneously including pins 3 and 6; no pins are reserved exclusively for power and excluded from data continuity testing.


---

**Question 5**
A network technician must connect two buildings with a fiber optic run of 400 meters. The connection must support 10 Gbps and minimize signal loss over the distance. Which fiber optic type and connector combination is most appropriate?
*   A) Multimode fiber with ST connectors — multimode is the only fiber type compatible with ST bayonet connectors, and ST is required for runs over 300 meters
*   B) Single-mode fiber with LC connectors — single-mode fiber supports longer distances with lower signal loss and LC connectors are the standard in modern enterprise fiber installations
*   C) Cat6a copper with RJ-45 connectors — copper twisted-pair is preferred for outdoor inter-building runs because fiber is not rated for direct-burial installation
*   D) Multimode fiber with SC connectors — multimode fiber provides higher bandwidth than single-mode at distances under 500 meters and SC connectors are required by TIA-568 for all inter-building runs
*   **Correct Answer:** B) Single-mode fiber with LC connectors — single-mode fiber supports longer distances with lower signal loss and LC connectors are the standard in modern enterprise fiber installations
*   **Distractor Analysis:**
    * *Why B is correct:* Single-mode fiber uses a narrower core that allows light to travel in a single path, dramatically reducing signal attenuation over long distances; it supports 10 Gbps and beyond at distances well beyond 400 meters. LC connectors are the dominant connector in current enterprise and data center fiber deployments due to their compact size and reliability.
    * *Why A is incorrect:* ST connectors are not restricted to multimode fiber, and they are a legacy connector type; ST connectors are not required for any particular distance and are largely replaced by LC in modern installations.
    * *Why C is incorrect:* Cat6a copper is limited to 100 meters maximum; it cannot support a 400-meter inter-building run under any circumstances. Fiber is routinely used for inter-building runs including direct-burial rated outdoor versions.
    * *Why D is incorrect:* Multimode fiber is limited to shorter distances (typically 300–500 meters at 10 Gbps depending on the grade) and has higher attenuation than single-mode over longer runs; for a 400-meter run requiring reliable 10 Gbps, single-mode is the correct choice. TIA-568 does not mandate SC connectors for inter-building runs.
