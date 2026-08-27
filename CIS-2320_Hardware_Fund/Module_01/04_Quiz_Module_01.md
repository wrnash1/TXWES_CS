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

---

### Question 11

A technician is about to install a new SSD into a PC. They work on a carpet-covered floor and do not have an ESD wrist strap. Which of the following is the BEST alternative ESD mitigation step?

- A) Work quickly so the static charge does not have time to build up
- B) Touch an unpainted metal surface of the PC chassis frequently throughout the installation
- C) Place the SSD on the anti-static bag's outer surface while preparing the drive bay
- D) Blow compressed air over the SSD to neutralize surface charge before installation

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Periodically touching the unpainted metal interior of the chassis equalizes the technician's static potential with the chassis ground. This is the recommended alternative when a wrist strap is unavailable. It must be done on unpainted metal — paint is an insulator.
- *Why A is incorrect:* Static charge builds as quickly as a person moves. Working faster does not reduce the charge — it may actually increase it by creating more friction with carpet and clothing.
- *Why C is incorrect:* The outer surface of an anti-static bag can accumulate and hold charge. Placing a component on the outside of the bag — rather than inside it — can expose the component to the very charge the bag was designed to prevent.
- *Why D is incorrect:* Compressed air can create a triboelectric (friction-based) charge on the component surface. It is used for dust removal, not static mitigation.

---

### Question 12

Which of the following describes an M.2 slot's key configuration that supports ONLY NVMe (PCIe) SSDs and is NOT backward compatible with SATA-based M.2 drives?

- A) B key
- B) B+M key
- C) M key
- D) E key

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* An M-key M.2 slot supports PCIe/NVMe drives exclusively. The physical notch on the left side of the connector accepts only M-keyed devices. Most modern motherboards use M-key slots for high-speed NVMe SSDs.
- *Why A is incorrect:* A B-key slot supports SATA-based M.2 drives and some PCIe x2 NVMe drives. It is the older configuration less common on modern motherboards.
- *Why B is incorrect:* A B+M keyed drive has notches at both positions and fits in both B-key and M-key slots, providing backward compatibility. It is the drive key type, not a slot that restricts to NVMe only.
- *Why D is incorrect:* The E key is used for Wi-Fi and Bluetooth M.2 cards (CNVi interface), not for storage drives.

---

### Question 13

A system technician installs two identical 16 GB DDR4 sticks into a motherboard with four DIMM slots. Slots are numbered 1–4, with slots 1 and 3 colored gray and slots 2 and 4 colored black. To enable dual-channel operation, where should the modules be installed?

- A) Slots 1 and 2 (adjacent slots, same side)
- B) Slots 1 and 3 (matching-color slots)
- C) Slots 2 and 4 (matching-color slots)
- D) Either B or C, depending on which pair the motherboard manual specifies as the primary dual-channel pair

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* Dual-channel is enabled by installing matching modules in the correctly paired slots — always consult the motherboard manual. Most boards use slots 2 and 4 as the primary dual-channel pair when only two modules are installed (because they connect to different memory channels on the CPU). Some boards prefer 1 and 3. The color-coded guide gives the visual cue, but the manual provides the authoritative answer.
- *Why A is incorrect:* Installing modules in adjacent slots (1 and 2) typically places both sticks on the same memory channel, which does not enable dual-channel mode. They would run in single-channel.
- *Why B is incorrect:* While slots 1 and 3 are the same color (suggesting they are a matched pair), many boards designate slots 2 and 4 as the recommended pair for two-module configurations. Choosing B without verifying the manual could yield single-channel performance.
- *Why C is incorrect:* Same reasoning as B — slots 2 and 4 are often correct, but the board manual must confirm the specific pairing before installation.

---

### Question 14

Which of the following voltages does a standard ATX PSU provide to PC components? (Select the combination that is MOST accurate for the A+ exam.)

- A) +3.3V, +5V, +12V, and −12V
- B) +5V, +12V, and +24V
- C) +12V and +5V only
- D) +3.3V, +5V, +12V, −12V, and +5VSB

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* A standard ATX PSU provides +3.3V (logic circuits), +5V (drives, older components), +12V (motors, CPU VRMs, PCIe), −12V (legacy serial ports), and +5VSB (standby voltage that keeps the motherboard powered for wake-on-LAN even when "off"). The A+ exam includes −12V and +5VSB in the full voltage rail list.
- *Why A is incorrect:* This answer omits +5VSB. The standby rail is explicitly tested on the A+ exam and enables features such as wake-on-LAN and USB charging when the system is powered off.
- *Why B is incorrect:* +24V is not an ATX output rail. The 24-pin connector carries multiple voltages — it is not a single 24V rail.
- *Why C is incorrect:* This omits multiple required rails (+3.3V, −12V, +5VSB). While +12V and +5V are the most heavily loaded rails, the others exist and are tested.

---

### Question 15

A technician is replacing a CPU in an LGA1700 socket and accidentally bends two of the socket pins. What is the most likely consequence?

- A) The CPU is damaged and must be replaced
- B) The motherboard is damaged and may require replacement
- C) The thermal paste bond is broken and overheating will occur at next boot
- D) The bent pins will self-correct when the CPU retention bracket is tightened

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* In LGA (Land Grid Array) sockets, the pins are on the motherboard socket — not on the CPU. Bending those pins damages the motherboard socket, which is far more expensive to repair or replace than a CPU. This is a key A+ exam distinction between LGA and PGA sockets.
- *Why A is incorrect:* The CPU has flat contact pads in LGA design — there are no pins on the CPU. The CPU itself is not the component damaged by bending socket pins.
- *Why C is incorrect:* Thermal paste and the heat sink seating are unrelated to bent socket pins. Overheating is a separate issue caused by improper thermal interface, not pin damage.
- *Why D is incorrect:* Bent socket pins do not self-correct under pressure from the retention bracket. Attempting to force the CPU onto bent pins further damages both the socket and the CPU pads.

---

### Question 16

What is the purpose of standoff screws when mounting a motherboard in a PC case?

- A) They hold the CPU retention bracket in place during shipping
- B) They elevate the motherboard off the case floor to prevent electrical short circuits between the motherboard traces and the metal case
- C) They adjust the PCIe slot height to align with expansion card brackets
- D) They secure the PSU to the case wall without requiring additional screws

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Standoffs are threaded brass or aluminum spacers that screw into the case mounting plate first. The motherboard then screws into the standoffs, elevating the PCB surface off the metal case by ~5mm. Without standoffs, the PCB solder joints and traces on the back of the motherboard would contact the metal case, causing short circuits.
- *Why A is incorrect:* CPU retention brackets are secured to the motherboard directly with dedicated screws or clips. Standoffs have nothing to do with CPU mounting hardware.
- *Why C is incorrect:* PCIe slot height is determined by the motherboard and case design. Standoffs set the motherboard at the correct I/O shield height — they do not independently adjust PCIe bracket alignment.
- *Why D is incorrect:* The PSU is mounted to the case using its own four screws at the rear panel. Standoffs are only used for the motherboard.

---

### Question 17

A PC powers on and the CPU fan spins, but there is no POST beep and no video output. Which of the following is the MOST likely cause related to hardware covered in Module 01?

- A) The operating system files are corrupted
- B) The GPU driver is outdated
- C) RAM is not properly seated in the DIMM slots
- D) The SATA data cable is disconnected from the storage drive

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* A system that powers on but does not complete POST (no beep or video) most commonly indicates a RAM seating issue. During POST, the system must detect and initialize RAM before it can display anything on screen. Improperly seated RAM causes POST to halt immediately. The A+ exam frequently uses this symptom to test RAM troubleshooting knowledge.
- *Why A is incorrect:* OS corruption causes errors after POST completes. If there is no POST and no video at all, the OS has not been reached yet.
- *Why B is incorrect:* GPU driver issues occur at the OS level, after the system has booted. They cause display problems in Windows, not a complete failure before POST.
- *Why D is incorrect:* A disconnected SATA data cable prevents the OS from loading from the drive, but POST would still complete and display an error such as "No boot device found." The system would still show video output.

---

### Question 18

When labeling cable connections on an ATX motherboard, a student correctly notes that the 4-pin or 8-pin square connector near the CPU socket is NOT the same as the 24-pin ATX connector. What is the specific function of the 4/8-pin connector?

- A) It provides power specifically to the CPU voltage regulator modules (VRMs)
- B) It provides standby power to the motherboard when the system is turned off
- C) It connects the front panel power button to the motherboard
- D) It provides dedicated power to the PCIe x16 slot for the GPU

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The 4-pin (or 8-pin EPS) connector near the CPU socket delivers +12V power specifically to the CPU's Voltage Regulator Modules (VRMs). The VRMs step down the +12V to the precise lower voltages the CPU cores require (typically 1–1.5V). High-end CPUs draw significant amperage and need this dedicated supply rather than sharing the 24-pin bus.
- *Why B is incorrect:* Standby power (+5VSB) is delivered through the 24-pin ATX connector. The 4/8-pin CPU connector is only active when the system is running.
- *Why C is incorrect:* The front panel power button connects via a 2-pin header at the bottom of the motherboard (part of the front panel connector group). It is a signal wire, not a power connector.
- *Why D is incorrect:* The PCIe x16 slot receives some power through the motherboard (delivered via the 24-pin connector), but discrete GPUs requiring more power use a separate 6-pin or 8-pin PCIe power connector from the PSU — which plugs directly into the GPU, not the motherboard.

---

### Question 19

Which of the following best describes the difference between volatile and non-volatile memory, and correctly categorizes RAM and an NVMe SSD?

- A) Both RAM and NVMe SSD are volatile — both lose data without power
- B) RAM is volatile (loses data without power); NVMe SSD is non-volatile (retains data without power)
- C) RAM is non-volatile because it retains BIOS configuration; NVMe SSD is volatile because it requires a power cycle to write new data
- D) Both RAM and NVMe SSD are non-volatile because both use solid-state technology

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Volatile memory requires constant power to retain data — RAM stores active program data in capacitor-based cells that discharge when power is removed. Non-volatile memory retains data without power through persistent physical state changes in NAND flash cells. NVMe SSDs use NAND flash and retain data after power loss.
- *Why A is incorrect:* NVMe SSDs are non-volatile. They are designed specifically to persist data across power cycles — that is their primary purpose as a storage device.
- *Why C is incorrect:* RAM does not retain BIOS settings. The CMOS battery and UEFI flash storage retain BIOS settings. RAM is a temporary working memory that loses all content when the system powers down.
- *Why D is incorrect:* "Solid-state" refers to the absence of moving parts, not to non-volatility. DRAM (used in RAM modules) is solid-state technology but is volatile. Non-volatility is determined by the storage mechanism, not the presence or absence of moving parts.

---

### Question 20

A technician needs to move a workstation across the building to a new office. The system was recently upgraded with a discrete GPU. When the technician sets up the PC at the new desk and connects the monitor to the motherboard's built-in video port, there is no display output. What is the MOST likely explanation?

- A) The monitor cable was damaged during transport
- B) The discrete GPU disabled the integrated graphics in the BIOS, so video output only works through the GPU's ports
- C) The CMOS battery died during transport, resetting the video output settings
- D) The PCIe x16 slot lost power because the GPU's PCIe power cable came loose

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* When a discrete GPU is installed, many motherboards automatically disable the CPU's integrated graphics in BIOS/UEFI. The monitor must be connected to the discrete GPU's display ports (HDMI, DisplayPort) — not the motherboard's rear I/O video port. This is a very common A+ scenario tested in Domain 3.
- *Why A is incorrect:* Cable damage is possible but statistically uncommon from a normal office move. More importantly, the more likely explanation is the integrated graphics being disabled — the A+ exam trains you to identify the most probable cause first.
- *Why C is incorrect:* CMOS batteries do not die from being moved. They are coin cells rated for 3–7 years of standby use. Even if the battery died, it would cause incorrect date/time — not a video output failure.
- *Why D is incorrect:* A loose PCIe power cable would cause the GPU to fail to initialize (often accompanied by a POST beep code), but the question states the PC is connecting to the motherboard's port — the GPU's power status is not the issue here.
