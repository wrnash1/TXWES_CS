# Quiz: Module 14 - Physical Layer – Cabling Standards and Installation
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A network technician has just finished running a new Cat6 cable from a wall outlet to a patch panel in the telecommunications room. The cable measures 87 meters. After terminating both ends, the technician tests the cable and discovers that all 8 pins are connected but the link does not function at gigabit speed. The technician suspects the far-end pair mapping is incorrect. Which wiring standard should be used on BOTH ends of the cable to create a functional straight-through patch cable that connects the workstation to the switch?

A) T568A on the wall outlet end and T568B on the patch panel end — this crossover configuration is required for direct workstation-to-switch connections in commercial installations
B) T568B on both ends — this is the most common commercial wiring standard in the US, and using the same standard on both ends creates a straight-through patch cable
C) T568A on both ends — the A standard must be used for horizontal cabling runs because it provides superior crosstalk rejection compared to T568B in Cat6 installations
D) Either T568A on both ends or T568B on both ends is acceptable for gigabit, but the wire pairs must be swapped at pin positions 1–2 and 7–8 to support full-duplex operation

*   **Correct Answer:** B) T568B on both ends — this is the most common commercial wiring standard in the US, and using the same standard on both ends creates a straight-through patch cable
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Using T568A on one end and T568B on the other creates a crossover cable — this is used to connect two like devices (switch-to-switch, PC-to-PC) and would not provide a working straight-through connection from the workstation to the switch. A crossover on a modern switch with Auto-MDIX may happen to function, but this is not the correct standard termination practice.
    *   *Why C is incorrect:* T568A is a valid wiring standard, and using it on both ends does create a valid straight-through cable. However, T568A is not required for Cat6, and it is less common in US commercial installations than T568B. The key principle is that both ends must match — not that T568A is required over T568B.
    *   *Why D is incorrect:* There is no pin-swapping modification required for full-duplex or gigabit operation. The T568A and T568B standards define a complete 8-conductor wiring sequence; both standards natively support 1000BASE-T when used consistently on both ends of the cable without any modification.

---

**Question 2**
A field technician is installing structured cabling in a new office building. The horizontal cable runs from the telecommunications room patch panel to each work area outlet must comply with TIA-568 standards. The IT manager asks the technician to confirm the maximum allowable distances. Which values correctly describe the TIA-568 horizontal cabling distance limits?

A) The permanent link (wall outlet to patch panel, solid-core cable only) may not exceed 100 meters; patch cords at each end add up to an additional 10 meters for a total channel of 110 meters
B) The permanent link may not exceed 90 meters; the total channel including all patch cords at both ends may not exceed 100 meters
C) The permanent link may not exceed 100 meters; patch cords are not counted against the distance limit because they use stranded cable with lower insertion loss than solid-core cable
D) There is no fixed distance limit for horizontal cabling — the limit depends on the cable category; Cat5e supports 50 meters, Cat6 supports 75 meters, and Cat6a supports 100 meters at 10GbE speeds

*   **Correct Answer:** B) The permanent link may not exceed 90 meters; the total channel including all patch cords at both ends may not exceed 100 meters
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The permanent link limit is 90 meters, not 100 meters. The 100-meter figure is the total channel limit (permanent link plus all patch cords), not a separate permanent link limit. Extending patch cords beyond the 10-meter allocation (the difference between 90m permanent and 100m channel) would push the total channel over the 100-meter limit and cause signal degradation at gigabit speeds.
    *   *Why C is incorrect:* Patch cords absolutely count against the total channel distance limit. The 100-meter total channel budget includes the permanent link (90m max) plus patch cords at both ends (10m total). Using stranded vs. solid-core cable affects flexibility and bend radius, not whether patch cords are included in the distance budget.
    *   *Why D is incorrect:* The 100-meter total channel limit applies to all copper twisted-pair categories (Cat5e, Cat6, Cat6a) for 1000BASE-T and 10GBASE-T over the specified channel length. Cat6a supports 10GbE at the same 100-meter channel limit — the limit does not vary by category.

---

**Question 3**
A network administrator needs to identify which physical cable in a bundle behind a drop ceiling connects to port 14 on a patch panel in the wiring closet. The cable bundle contains 24 Cat6 cables with no labels visible at the ceiling end. The administrator has access to the patch panel and both ends of the cable runs. Which tool is the most efficient for locating and tracing the specific cable?

A) Cable certifier — connect the certifier's main unit to patch panel port 14 and use the remote unit at the ceiling end to measure attenuation and identify the correct cable pair by loss signature
B) OTDR (Optical Time-Domain Reflectometer) — inject a light pulse into the cable at the patch panel and scan the ceiling end with the OTDR receiver to identify the cable by reflectance pattern
C) Tone generator and probe (fox and hound) — connect the tone generator to patch panel port 14 and sweep the inductive probe along the cable bundle at the ceiling end to locate the cable emitting the tonal signal
D) Cable tester — connect the main unit to patch panel port 14 and the remote unit to each cable at the ceiling end sequentially until the tester reports a complete 8-wire match, identifying the correct cable

*   **Correct Answer:** C) Tone generator and probe (fox and hound) — connect the tone generator to patch panel port 14 and sweep the inductive probe along the cable bundle at the ceiling end to locate the cable emitting the tonal signal
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A cable certifier measures performance parameters (attenuation, NEXT, return loss) and verifies whether a cable meets a category specification — it is not designed to identify or locate an unknown cable in a bundle. The certifier requires both the main and remote units to be connected to known cable ends, which defeats the purpose when the goal is to find the unknown end.
    *   *Why B is incorrect:* An OTDR is a fiber optic testing instrument that sends light pulses into a fiber strand to locate breaks, splices, and connectors. It cannot be used on copper twisted-pair cable. Using an OTDR on a copper cable would not function and could damage the instrument.
    *   *Why D is incorrect:* A cable tester verifies that a known cable is correctly wired — it requires both ends to be accessible and connected simultaneously. To use a tester, the technician would need to individually connect each of the 24 cables at the ceiling end to the remote unit, which is extremely time-consuming compared to the tone generator and probe approach.

---

**Question 4**
A network engineer is reviewing the results of a new Cat6a installation. The cable certifier reports that three of the cable runs have failed the NEXT (Near-End Crosstalk) test, even though their total length is only 45 meters. The physical cable runs are away from power cables and fluorescent lighting. Which is the most likely cause of the NEXT failures?

A) Attenuation — the cables are too long and the signal is losing strength before reaching the far end, causing the certifier to interpret the loss as crosstalk at the near end
B) EMI (Electromagnetic Interference) — external electrical noise from nearby equipment is coupling into the cable pairs and increasing the measured crosstalk values
C) Improper termination — the cable pairs were untwisted too much during termination at the keystone jacks or patch panel, reducing the crosstalk rejection designed into the twisted-pair geometry
D) Impedance mismatch — the Cat6a cable is terminated into Cat5e keystone jacks rated for a lower frequency, and the impedance difference creates signal reflections that the certifier reports as crosstalk

*   **Correct Answer:** C) Improper termination — the cable pairs were untwisted too much during termination at the keystone jacks or patch panel, reducing the crosstalk rejection designed into the twisted-pair geometry
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Attenuation is signal loss over distance — a 45-meter run is well within the 90-meter permanent link limit and would not produce excessive attenuation. More importantly, attenuation and NEXT are distinct failure modes: attenuation is measured end-to-end, while NEXT is measured at the same end as the transmitter. A short cable will not produce NEXT failures due to length.
    *   *Why B is incorrect:* EMI from external sources causes noise that affects the entire cable run, and the engineer already noted the cables are routed away from power cables and fluorescent lights. More importantly, EMI manifests as alien crosstalk (AXT) or interference from outside the cable — not as NEXT, which is unwanted coupling between pairs within the same cable at the termination point.
    *   *Why D is incorrect:* Using Cat5e keystone jacks on Cat6a cable would indeed be a termination mismatch problem, but it would primarily cause impedance and return loss failures rather than NEXT. A Cat5e jack on Cat6a cable would also typically be identified by physical inspection. The more common cause of NEXT failures on short runs is excessive pair untwisting during termination, which is the primary source of near-end coupling in field installations.

---

**Question 5**
A network team is deploying structured cabling for a new three-story office building. The building has one main equipment room (MER) on the first floor and one telecommunications room (TR) per floor. Each floor has 60 workstations. The fiber backbone runs between the MER and each TR. Copper horizontal cabling runs from each TR to the work area outlets. The team must also ensure the installation can be tested and certified to TIA-568 Cat6 standards. Which combination of tools, standards, and components correctly satisfies all requirements?

A) Use Cat6 UTP for horizontal runs terminated with T568B on both ends; use multimode fiber for backbone runs between the MER and TRs; install patch panels in each TR for horizontal cable termination; verify with a cable certifier for Cat6 performance and an OTDR for fiber continuity
B) Use Cat6 UTP for horizontal runs terminated with T568A on the MER end and T568B on the workstation end to create a crossover for each run; use single-mode fiber for all backbone runs; use a cable tester to certify Cat6 compliance at each workstation outlet
C) Use Cat5e UTP for horizontal runs since Cat6 is only required for 10GbE runs over 55 meters; use coaxial cable for backbone runs between floors; terminate all horizontal runs with T568A on both ends; test with a tone generator and probe
D) Use Cat6 UTP for horizontal runs terminated with T568B on both ends; use backbone cabling limited to 90 meters per TIA-568 horizontal distance rules; terminate all fiber at the MER only (no TR patch panels) to minimize connection points; certify with a cable tester

*   **Correct Answer:** A) Use Cat6 UTP for horizontal runs terminated with T568B on both ends; use multimode fiber for backbone runs between the MER and TRs; install patch panels in each TR for horizontal cable termination; verify with a cable certifier for Cat6 performance and an OTDR for fiber continuity
*   **Distractor Analysis:**
    *   *Why A is correct:* Cat6 UTP with T568B on both ends creates correctly wired straight-through horizontal cables. Multimode fiber (OM3/OM4) is the standard choice for intra-building backbone runs up to several hundred meters. Patch panels in each TR are required by TIA-568 structured cabling for the horizontal cross-connect point. A cable certifier verifies Cat6 performance parameters (attenuation, NEXT, return loss); an OTDR locates faults and verifies continuity on fiber backbone runs.
    *   *Why B is incorrect:* Using T568A on one end and T568B on the other creates crossover cables — every workstation connection would be wired as a crossover, preventing proper operation (except on switches with Auto-MDIX). A cable tester verifies pin-to-pin continuity and wire order but does not measure attenuation, NEXT, or return loss — it cannot certify Cat6 compliance.
    *   *Why C is incorrect:* Cat5e can support 1000BASE-T (gigabit) at 100 meters but does not meet Cat6 performance specifications — if the requirement is Cat6 certification, Cat5e cannot be substituted. Coaxial cable is not used for structured building backbone cabling in modern TIA-568 installations. A tone generator and probe is a cable-tracing tool, not a certification instrument.
    *   *Why D is incorrect:* The 90-meter limit is the horizontal cabling permanent link limit — backbone cabling between the MER and TRs has its own distance specifications (up to 90 meters for copper backbone, up to 2,000 meters for multimode fiber backbone under TIA-568) and is governed by different distance rules than horizontal cabling. Omitting TR patch panels violates the TIA-568 structured cabling subsystem architecture, which requires a cross-connect at each TR. A cable tester does not certify Cat6 — a cable certifier is required.
