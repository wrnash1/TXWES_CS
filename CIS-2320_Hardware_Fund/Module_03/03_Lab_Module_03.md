# Lab Activity: Module 03 - Processors (CPUs) and Cooling

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5
**Estimated Completion Time:** 60–90 minutes
**Submission:** Canvas LMS — Module 03 Lab Assignment

---

## Overview

In this lab you will examine a CPU and its corresponding motherboard socket, perform or observe a CPU installation and thermal paste application, and analyze real-world cooling failure scenarios. The objective is to build the hands-on identification and installation skills tested on the CompTIA A+ exam and required in entry-level technician roles.

No terminal commands are used in this lab. All work involves physical hardware observation, procedure documentation, and written analysis.

If physical hardware is not available at your station, your instructor will provide close-up reference photographs and a labeled CPU/socket diagram. Complete all tables, procedures, and questions using those materials.

---

## Safety and Handling Requirements

Before handling any CPU or motherboard:

- Wear an ESD wrist strap or touch a grounded metal surface before picking up any component.
- Handle CPUs by their edges only. Never touch the contact pads (LGA CPU) or pins (PGA CPU) on the underside.
- Never apply downward force to seat a PGA CPU. The ZIF lever provides all clamping force.
- Never touch the pins inside an LGA socket. One bent pin can render the motherboard non-functional.
- Apply thermal paste only after confirming the CPU is fully seated and the retention mechanism is closed.
- Use isopropyl alcohol (90% or higher) on a lint-free cloth or coffee filter to clean old thermal paste before applying new compound.

---

## Part 1: CPU and Socket Identification

### Step 1 — Identify the CPU and socket type

Obtain the CPU and motherboard assigned to your station. Examine both components carefully. Fill in the identification table:

| Field                                          | Your Observation |
|------------------------------------------------|------------------|
| CPU manufacturer (Intel / AMD)                 |                  |
| CPU model name or number (if printed on IHS)   |                  |
| Socket type (LGA / PGA / BGA)                  |                  |
| Socket name (e.g., LGA1700, AM4, AM5)          |                  |
| Where are the pins located (CPU or socket)?    |                  |
| Number of contact pins or pads (if countable)  |                  |
| Retention mechanism (lever / clip / ZIF lever) |                  |
| Is the CPU field-replaceable? (Yes / No)       |                  |

### Step 2 — Locate the alignment marker

Every socketed CPU has an alignment marker — a small triangle or notch on one corner — that must align with a corresponding marker on the socket before seating.

**Question 1-A:** Locate the triangle alignment marker on your CPU. Which corner is it on (describe its position relative to the CPU's physical orientation)?

Your answer:

**Question 1-B:** What is the purpose of this alignment marker, and what physical consequence occurs if a technician attempts to force a CPU into the socket in the wrong orientation?

Your answer:

### Step 3 — Examine the CPU architecture specifications

Using the CPU model identified in Step 1, look up or use the instructor-provided spec sheet to complete the following table:

| Specification               | Value |
|-----------------------------|-------|
| Number of physical cores    |       |
| Number of threads           |       |
| Base clock speed (GHz)      |       |
| Boost/Turbo clock speed (GHz) |     |
| L3 cache size (MB)          |       |
| TDP (Thermal Design Power, watts) |  |

**Question 1-C:** Based on the core and thread count you recorded, does this CPU support Hyper-Threading (Intel) or SMT (AMD)? How can you tell from the numbers alone?

Your answer:

---

## Part 2: CPU Installation and Thermal Paste Application

### Step 4 — CPU installation procedure

Follow these steps for your assigned socket type. Document each step with a brief observation note or photo.

For an LGA socket:

1. Open the retention lever fully by pressing down and moving it to the side.
2. Lift the load plate to the fully open position.
3. Remove the protective plastic cover from the socket (keep it — it protects the socket if the board is stored).
4. Align the CPU so the triangle marker on the CPU corner matches the triangle marker on the socket corner. The CPU should drop in with zero force.
5. Lower the load plate over the CPU and engage the retention lever, applying firm downward pressure at the lever tip until it clicks under the hook.

For a PGA socket:

1. Open the ZIF lever by pressing it sideways and lifting it to the fully vertical position.
2. Align the CPU so the triangle marker on the CPU corner matches the triangle marker on the socket corner.
3. Lower the CPU straight into the socket. It drops in with zero force — do not push down.
4. Lower the lever back to the horizontal position and engage the locking hook.

**Question 2-A:** During installation, did the CPU require any downward force to seat? What does this tell you about the socket's design intent?

Your answer:

**Question 2-B:** After closing the retention lever, what visual check can you perform to confirm the CPU is seated correctly before proceeding?

Your answer:

### Step 5 — Thermal paste application

Apply thermal paste to a demonstration CPU IHS (do not apply to a CPU that is not being cooled — paste that sits exposed collects dust and debris).

1. If this is a replacement: clean the IHS with isopropyl alcohol on a lint-free cloth. Clean the base of the heat sink the same way. Allow both surfaces to dry completely.
2. Place a single pea-sized dot of thermal paste in the center of the IHS. The dot should be approximately 3–4 mm in diameter.
3. Do not spread the paste manually.
4. Note the color and consistency of the paste.

**Question 2-C:** Why should you not manually spread the thermal paste before seating the heat sink?

Your answer:

**Question 2-D:** What happens if significantly too much thermal paste is applied? Describe at least two potential consequences.

Your answer:

### Step 6 — Heat sink installation and fan header connection

1. Lower the heat sink straight down onto the CPU, aligning the mounting holes with the motherboard standoffs.
2. Secure the mounting hardware in a cross pattern (tighten diagonal corners alternately) to apply even pressure across the IHS.
3. Confirm the heat sink does not rock or shift on the CPU surface.
4. Connect the 4-pin PWM fan cable to the CPU_FAN header. Note the label on the header printed on the board surface.

**Question 2-E:** Why is it important to tighten the heat sink mounting hardware in a cross (diagonal) pattern rather than tightening each corner fully before moving to the next?

Your answer:

**Question 2-F:** The CPU_FAN header has four pins. Name the function of each pin.

Your answer:

---

## Part 3: Cooling Failure Scenario Analysis

Read each scenario and write a 3–5 sentence response identifying the most likely cause and the correct repair action.

### Scenario A — Repeated Thermal Shutdown

A user reports that their desktop PC runs fine for about 8–10 minutes before shutting down without warning. After the system cools for a few minutes, it powers back on normally. The CPU fan is spinning and the case has adequate ventilation. The user mentions the PC has not been opened in three years.

**Question 3-A:** What is the most likely cause of this thermal shutdown pattern? What repair should the technician perform?

Your answer:

### Scenario B — CPU Fan Error at POST

A technician builds a new PC and powers it on for the first time. The system reaches the BIOS POST screen, then displays a "CPU Fan Error — Press F1 to continue" message. The technician checks the fan and it appears to be spinning. The system boots into Windows normally after pressing F1, and CPU temperatures appear stable.

**Question 3-B:** What is the most likely cause of this specific POST error message, and what should the technician check first? Why does the BIOS generate this error even if the system runs fine afterward?

Your answer:

### Scenario C — Laptop CPU Failure

A laptop brought in for repair has been diagnosed with a failed CPU. The technician opens the laptop service manual and discovers the processor is a BGA package soldered to the system board.

**Question 3-C:** What repair options are available to this technician? What should the technician tell the customer about cost and timeline expectations for this repair?

Your answer:

---

## Deliverables and Submission

Submit the following to Canvas by the Module 03 lab deadline:

1. Completed Part 1 identification and specification tables.
2. Written answers to all questions (1-A through 3-C).
3. One photograph showing the thermal paste dot applied to the CPU IHS before heat sink installation, or an annotation on a reference image indicating where and how much paste to apply.
4. One photograph showing the CPU_FAN header connection, or an annotated reference image identifying the header location.

---

## Grading Rubric

| Component                                                              | Points  |
|------------------------------------------------------------------------|---------|
| Part 1 tables and identification questions complete and accurate        | 25      |
| Part 2 installation procedure questions correct and detailed            | 35      |
| Part 3 scenario analysis demonstrates understanding of cooling concepts | 30      |
| Required photographs or annotated images submitted                     | 10      |
| **Total**                                                              | **100** |

Partial credit is awarded for answers showing correct reasoning with minor inaccuracies. No credit is awarded for blank responses or generic answers that do not engage with the scenario details.

---

## Part 9 — Challenge Exercise

These advanced steps are optional and are not included in the standard grading rubric.

### Challenge Step 1 — Live CPU Temperature and Throttle Observation

Using HWiNFO64 (free download at [https://www.hwinfo.com/](https://www.hwinfo.com/)) on any available Windows system:

1. Launch HWiNFO64 in Sensors-only mode.
1. Locate the CPU temperature readings for each core and the CPU package temperature.
1. Record the idle temperatures after the system has been at desktop for 5 minutes.
1. Open a stress test tool such as Prime95 (free at [https://www.mersenne.org/download/](https://www.mersenne.org/download/)) or run a CPU-intensive task (video encoding, a compilation job).
1. Record the temperatures under sustained load for 5 minutes.
1. Observe whether the CPU clock speed drops below base clock during the test (look for "CPU Core Speed" or "CPU Clock" in HWiNFO). If it does, you are observing thermal throttling in real time.
1. Document: idle temps, load temps, whether throttling occurred, and what that tells you about the system's cooling adequacy.

### Challenge Step 2 — Thermal Paste Spread Pattern Inspection

Apply a pea-sized dot of thermal paste to a clean piece of glass or smooth plastic (not a real CPU — this is a practice exercise):

1. Press a flat object (a glass plate, acrylic sheet, or the base of an unused heat sink) straight down onto the paste dot with even pressure, simulating heat sink mounting.
1. Carefully lift the top surface. Observe and photograph the spread pattern.
1. In your notes, describe whether the paste spread evenly from center outward, whether there are any voids (gaps in coverage), and whether any paste reached the edge of the contact area.
1. Repeat the experiment with a deliberately oversized amount of paste. Observe and document the overflow behavior.
1. Write a 2–3 sentence conclusion explaining what "proper amount" means in terms of the spread pattern result, and why both too little and too much paste produce suboptimal thermal interfaces.

### Challenge Step 3 — CPU Specification Research and Cooling Recommendation

Select any two desktop CPUs — one with a 65W TDP and one with a 125W TDP — from AMD or Intel's current lineup:

1. Use the manufacturer's ARK (Intel) or product page (AMD) to document: socket type, core count, TDP, boost clock, and release year.
1. Research one suitable aftermarket air cooler for each CPU using PCPartPicker ([https://pcpartpicker.com/products/cpu-cooler/](https://pcpartpicker.com/products/cpu-cooler/)). The cooler's TDP rating must meet or exceed the CPU's TDP.
1. Create a comparison table showing the CPU TDP, cooler TDP rating, cooler price, and cooler form factor (tower vs. low-profile vs. AIO).
1. Write a one-paragraph justification for your cooler selection for each CPU, explaining why you matched that cooler to that processor based on thermal headroom, budget, and form factor considerations.
