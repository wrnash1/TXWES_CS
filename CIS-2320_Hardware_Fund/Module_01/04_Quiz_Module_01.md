# Quiz: Module 01 — Introduction to PC Hardware & Safety

## Course: CIS-2320 Hardware Fundamentals

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3: Hardware

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the primary danger of handling a RAM module without ESD protection?

- A) Electric shock to the technician from the module's stored charge
- B) The module may be permanently damaged by electrostatic discharge that the technician cannot feel
- C) The module will lose its stored data if touched with bare hands
- D) The module's pins will corrode if skin oils make contact with the edge connector

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* ESD damage can occur from a discharge of as little as 10 volts — far below the 3,000–4,000 volts a human needs to feel a spark. The damage is invisible and can cause immediate failure or gradual degradation. RAM is a CMOS device with nanometer-scale transistor traces that are destroyed by ESD.
- *Why A is incorrect:* RAM modules do not store dangerous charge. The technician is not at risk of electrical shock from a RAM module — the ESD risk runs the other direction (from the technician to the component).
- *Why C is incorrect:* RAM is volatile and loses data when power is removed, but touching the module does not cause data loss. ESD can destroy the module's circuits, but skin contact alone (without static discharge) does not erase stored data.
- *Why D is incorrect:* While technicians should avoid touching edge connectors for cleanliness reasons, skin oils do not cause the catastrophic and immediate risk that ESD poses.

---

### Question 2

In the context of PC hardware safety, what is grounding?

- A) Connecting the PC chassis and the technician to a common electrical potential so no static discharge can occur between them
- B) Installing the motherboard on metal standoffs to prevent short circuits against the case
- C) Formatting a drive to its factory default partition table
- D) Applying thermal paste between the CPU and heat sink to ground out excess heat

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Grounding equalizes the electrical potential between the technician and the components. When both are at the same potential, no discharge can flow between them — eliminating ESD risk. The ESD wrist strap achieves this by connecting the technician to the PC chassis through a 1-megaohm resistor.
- *Why B is incorrect:* Using standoffs to mount a motherboard is correct practice for preventing short circuits, but it is not the definition of grounding in the ESD safety context.
- *Why C is incorrect:* This describes low-level disk formatting — an unrelated storage concept.
- *Why D is incorrect:* Thermal paste manages heat transfer, not electrical grounding.

---

### Question 3

A technician powers down a PC, turns off the power strip, and immediately opens the case to replace a RAM module. What is wrong with this procedure?

- A) The technician should have removed the RAM before powering down
- B) The power strip should remain on so the chassis stays grounded through the outlet
- C) The power cord was not unplugged from the wall outlet, so the PSU may still retain charge
- D) Turning off the power strip is equivalent to unplugging the cord — the procedure is correct

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Turning off a power strip removes the AC supply but leaves the power cord physically connected. The PSU's internal capacitors can retain charge even when the strip is off. The correct procedure is to physically unplug the power cord from the wall outlet or power strip socket, then press the power button to drain residual capacitor charge from the motherboard.
- *Why A is incorrect:* RAM is replaced after the system is powered down — not before. Removing RAM from a running system causes data loss and potentially damages the module and motherboard.
- *Why B is incorrect:* This is a specific A+ exam distractor. Leaving the cord plugged in does not "keep the chassis grounded" in a safe way. It keeps live voltage available to the PSU, which is the hazard the procedure is designed to eliminate.
- *Why D is incorrect:* Turning off a power strip and unplugging a cord are not equivalent. The cord's physical connection to the PSU means capacitors can still retain charge.

---

### Question 4

Which of the following best explains why a technician should press the PC's power button after unplugging the power cord?

- A) It signals the OS to save open files before the system shuts down completely
- B) It drains residual charge stored in the motherboard's capacitors
- C) It resets the CMOS settings to factory defaults
- D) It discharges the ESD wrist strap before attaching it to the chassis

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* After unplugging the power cord, the motherboard's capacitors may retain residual voltage. Pressing the power button sends the shutdown signal through the board, allowing those capacitors to discharge safely. Without this step, touching components immediately after unplugging can result in a brief shock or component damage from residual voltage.
- *Why A is incorrect:* The OS already shut down in Step 1 of the safety procedure. Pressing the power button after unplugging does not communicate with the OS — the system has no power.
- *Why C is incorrect:* CMOS settings are preserved by the coin-cell CMOS battery, not by power-button presses. Resetting CMOS requires removing the battery or shorting the CMOS clear jumper.
- *Why D is incorrect:* The ESD wrist strap is attached after pressing the power button, not before. The power button press has nothing to do with the wrist strap.

---

### Question 5

What is the purpose of the 1-megaohm resistor inside an ESD wrist strap?

- A) It amplifies the static charge so it can discharge faster into the chassis
- B) It limits current flow through the strap to prevent electrical shock to the technician while continuously draining static charge
- C) It measures resistance on the motherboard to verify ESD safety before work begins
- D) It stores static charge temporarily until the technician touches the chassis

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The 1 MΩ resistor is a safety component. It limits the current that could flow through the wrist strap if the technician accidentally contacted live voltage. At 120V AC, Ohm's Law gives I = V/R = 120/1,000,000 = 0.00012 A — far below the 10 mA threshold for harmful shock. The resistor simultaneously allows continuous, slow static drain while protecting the technician.
- *Why A is incorrect:* The resistor limits current — it does not amplify or accelerate discharge. A lower resistance would drain faster, but pose greater shock risk.
- *Why C is incorrect:* The resistor is a passive component in the cable, not a measurement instrument.
- *Why D is incorrect:* The strap continuously drains charge — it does not store it.

---

### Question 6

A technician receives a new CPU in the mail. The CPU arrives in a silver-gray bag with a metallic sheen. What type of bag is this, and what should the technician do before removing the CPU?

- A) It is a static-shielding anti-static bag; the technician should put on an ESD wrist strap and attach it to the chassis before opening the bag
- B) It is a standard padded shipping bag; the technician can remove the CPU directly and install it immediately
- C) It is a thermal bag designed to keep the CPU at a stable temperature during shipping; open it in a cool room
- D) It is a grounded bag that transfers charge from the CPU as it is opened; no additional precautions are needed

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The metallic silver-gray bag is an anti-static (static-shielding) bag. It protects the component from external static by conducting charge around the outside of the bag. Before opening it, the technician must be grounded — ESD wrist strap on, clipped to the PC chassis — so no discharge occurs when they reach inside.
- *Why B is incorrect:* The bag is not a standard shipping envelope. It is specifically designed for ESD-sensitive components. Treating it as ordinary packaging and skipping ESD precautions risks damaging the CPU.
- *Why C is incorrect:* Anti-static bags are not thermal bags. Temperature-sensitive components use insulated foam packaging, not metallized bags.
- *Why D is incorrect:* Anti-static bags protect the component passively while sealed, but they do not substitute for proper grounding during installation. Touching the CPU while ungrounded still creates ESD risk.

---

### Question 7

Which connector provides the main power from the PSU to the motherboard?

- A) 4-pin Molex connector
- B) 8-pin PCIe power connector
- C) 24-pin ATX connector
- D) 15-pin SATA power connector

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The 24-pin ATX connector is the main power connector between the PSU and the motherboard. It is a wide, two-row connector (two rows of 12 pins) that plugs into a matching 24-pin socket on the right edge of the motherboard. This connector provides all the DC voltages the motherboard distributes to its components.
- *Why A is incorrect:* The 4-pin Molex connector is a legacy connector used for older drives and some case fans. It does not provide motherboard power.
- *Why B is incorrect:* The 8-pin PCIe power connector powers high-end discrete GPUs — it plugs into the graphics card, not the motherboard.
- *Why D is incorrect:* The 15-pin SATA power connector powers SATA storage drives — it also plugs into drives, not the motherboard.

---

### Question 8

What is the difference between an LGA socket and a PGA socket?

- A) LGA sockets are used only in servers; PGA sockets are used only in consumer desktops
- B) LGA sockets have pins in the socket on the motherboard; PGA sockets have pins on the processor itself
- C) LGA sockets support DDR5 RAM only; PGA sockets support DDR4 RAM only
- D) LGA sockets require no thermal paste; PGA sockets require thermal paste applied to the socket, not the CPU

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* LGA (Land Grid Array) places the pins on the socket — the CPU has flat contact pads. Intel has used LGA for consumer desktops since LGA775. AMD moved to LGA with the AM5 socket. PGA (Pin Grid Array) places the pins on the processor — the socket has holes. AMD used PGA through AM4.
- *Why A is incorrect:* Both socket types appear in consumer desktops. LGA is used by Intel and AMD AM5 in mainstream consumer platforms. Server platforms use different sockets (LGA4189, SP5) but the LGA/PGA distinction is not server-vs-consumer.
- *Why C is incorrect:* RAM generation (DDR4 vs DDR5) is determined by the memory controller in the CPU and the motherboard chipset, not by whether the CPU socket is LGA or PGA.
- *Why D is incorrect:* Thermal paste is always applied between the CPU heat spreader and the heat sink — regardless of socket type. Socket type does not affect thermal paste application.

---

### Question 9

A technician opens a PC and identifies a small circular silver battery sitting in a holder on the motherboard surface. What is this component, and what happens if it dies?

- A) It is the CPU backup battery; if it dies, the CPU reverts to minimum clock speed until replaced
- B) It is the CMOS battery (CR2032); if it dies, the BIOS/UEFI loses its stored settings and the system clock resets
- C) It is a capacitor for the PCIe bus; if it dies, the GPU will not receive power at startup
- D) It is the POST indicator battery; if it dies, the power button LED will not illuminate during boot

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The coin-cell battery on the motherboard is the CMOS battery, typically a CR2032 (3V lithium). It maintains BIOS/UEFI configuration settings (boot order, overclocking settings, hardware enable/disable) and the real-time clock (RTC) when the system has no main power. When it dies, the system typically resets to BIOS defaults and shows an incorrect date/time on every boot.
- *Why A is incorrect:* There is no "CPU backup battery." CPU clock speed is governed by BIOS settings and power management — not a separate battery.
- *Why C is incorrect:* PCIe bus power comes from the PSU via the motherboard's power regulation circuitry, not from a coin-cell battery.
- *Why D is incorrect:* The POST LED and power button LED are powered through the motherboard's front panel header when the system has main power — they do not use a separate battery.

---

### Question 10

A technician needs to replace a failed PSU. They open the old PSU's case to inspect the capacitors before discarding it. Why is this dangerous?

- A) Opening the PSU voids its warranty, which is a legal liability for the technician
- B) The PSU contains large capacitors that can store lethal voltage even after the unit has been unplugged for an extended period
- C) The PSU fan may spin unexpectedly and injure the technician's fingers
- D) The internal transformer generates a magnetic field that can erase nearby hard drives

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* PSU capacitors — particularly the large electrolytic capacitors on the primary AC side — can store dangerous charge at high voltage (hundreds of volts) for extended periods after the unit is unplugged. There is no safe way for a field technician to discharge these capacitors without specialized equipment. The A+ exam rule is absolute: if a PSU fails, replace it. Never open it.
- *Why A is incorrect:* Warranty concerns are irrelevant when the unit is already failed and being discarded. More importantly, the real risk is physical — the warranty answer trivializes a lethal hazard.
- *Why C is incorrect:* While a spinning fan could cause minor cuts, it is not the primary danger. The stored high-voltage charge in the capacitors is the lethal risk.
- *Why D is incorrect:* PSU transformers do produce electromagnetic fields, but they are not strong enough to erase magnetic storage at normal distances. This is not the reason to avoid opening a PSU.
