# Lab Activity: Module 13 - Laptop Components and Disassembly

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 1.3
**Texas Wesleyan University | Professor Nash**
**Total Points: 100**

---

## Overview

This lab develops the identification, procedural, and diagnostic skills tested on the CompTIA A+ Core 1 exam for laptop hardware. You will identify internal laptop components from descriptions and diagrams, document the correct disassembly order for specific repair scenarios, and analyze real-world symptom scenarios to determine which component is failing and why.

No physical disassembly is required unless you have access to a practice laptop. All exercises are designed to be completed using diagrams, reference materials, and structured written responses.

**Learning Objectives:**

- Identify laptop components (battery, Wi-Fi card, RAM, SSD, ZIF connectors, display assembly, DC power jack) from descriptions and labeled diagrams
- State the mandatory first step before any laptop internal service
- Document the correct procedural order for common laptop repairs
- Apply symptom-to-component diagnostic reasoning for battery, display, and power jack failures
- Distinguish SO-DIMM from DIMM and M.2 NVMe from M.2 SATA by key characteristics

**Estimated Completion Time:** 60-90 minutes

**Submission:** Submit your completed lab document (typed responses) to Canvas by the posted due date.

---

## Part 1 — Laptop Component Identification (30 points)

### Part 1A — Component Identification Table

For each description below, write the component name and provide one identifying characteristic that distinguishes it from similar components.

| Description | Component Name | One Distinguishing Characteristic |
|-------------|---------------|----------------------------------|
| Stores the operating system and user data; uses an M key or B+M key slot; available in SATA or NVMe (PCIe) variants; retained by one screw; no antenna cables attached | | |
| Provides wireless network connectivity; seated in an M.2 or Mini-PCIe slot; has two or three thin coaxial cables connected via MHF4 snap-on connectors | | |
| System memory in laptop form factor; approximately 67 mm long; seated at an angle and retained by two spring clips; electrically identical to desktop equivalent but physically smaller | | |
| Powers the laptop; must be disconnected before any internal service; may be removable (external latch) or integrated (JST connector to motherboard) | | |
| A passive flat flex cable connector with a rotating lock bar; cable slides in and out only when the lock bar is in the open position | | |
| The port where the AC adapter barrel connector plugs in; failure causes intermittent charging that changes with cable angle; may be mounted directly on motherboard or on a daughter sub-board | | |
| Connects the LCD panel to the motherboard; routes through the hinge assembly; older version uses LVDS; modern version uses eDP | | |

---

### Part 1B — Component Location in a Laptop Interior

A laptop has been opened and the following items are visible. Match each item to its location description. Write the component name next to each location.

| Location in Laptop Interior | Component Present |
|-----------------------------|-------------------|
| Small rectangular card near the center of the motherboard; has one retaining screw; two colored wires with tiny circular connectors attached to its top edge | |
| Two matching rectangular slots along one edge of the motherboard; one slot is occupied by a module seated at approximately 30 degrees | |
| Rectangular multi-wire connector plugged into a socket on the motherboard near the battery bay; disconnecting this is Step 1 of any internal service | |
| Flat ribbon cable emerging from the hinge tube and connecting to a small ZIF socket on the motherboard | |
| Thin card in a single-screw slot; no cables attached; reads as a storage device in the operating system | |

---

### Part 1C — Safety Procedure Ordering Exercise

The following steps for replacing a laptop's internal Wi-Fi card are listed out of order. Write the numbers 1 through 9 next to each step to indicate the correct sequence.

| Step Description | Correct Order (1–9) |
|-----------------|-------------------|
| Remove the bottom panel screws and lift the panel | |
| Power off the laptop completely | |
| Disconnect the MHF4 antenna cables using a spudger | |
| Disconnect the AC adapter from the laptop and from the wall | |
| Note which color antenna cable connects to which pin (main and auxiliary) | |
| Remove the retaining screw and lift the old Wi-Fi card out at an angle | |
| Press and hold the power button for 5 seconds to discharge residual energy | |
| Remove or disconnect the battery | |
| Insert the new Wi-Fi card at an angle, seat it, reinstall the retaining screw, and reconnect antenna cables | |

---

## Part 2 — Disassembly Order Documentation (30 points)

### Part 2A — Repair Scenario Disassembly Steps

For each repair scenario below, list the components that must be removed or disconnected in order before the target component can be accessed. Write the steps in sequence. Not every scenario requires the same steps — identify only what is necessary for that specific repair.

**Scenario 1 — Replacing the RAM in a laptop with an integrated battery and a single bottom panel:**

The RAM slot is directly accessible from the bottom panel once it is removed. List the preparation and access steps in order.

Steps in order:

1.
2.
3.
4.
5.

What tool is needed to remove the bottom panel screws on most modern laptops?

*Your answer:*

**Scenario 2 — Replacing the LCD panel on a laptop with an LED-backlit non-touchscreen display:**

List the disassembly steps in order, from closing the laptop to having the old panel fully disconnected and removed.

Steps in order:

1.
2.
3.
4.
5.
6.
7.
8.

**Question 2A-1:** A technician skips removing the bezel rubber plugs and attempts to pry the bezel directly. What is the likely result, and how should the technician have proceeded instead?

*Your answer:*

**Question 2A-2:** After replacing an LCD panel, the technician reassembles the lid and discovers the display still shows no image. What component connection should the technician check first, and how would they access it without fully disassembling the lid again?

*Your answer:*

---

### Part 2B — ZIF Connector Procedure

A technician is replacing a laptop keyboard. The keyboard's flex cable connects to a ZIF connector on the motherboard. Answer the following questions.

**Question 2B-1:** Describe how to confirm the ZIF lock bar is in the open position before removing the flex cable. What does the lock bar look like in the open vs closed position?

*Your answer:*

**Question 2B-2:** A technician reports that after removing the flex cable, the ZIF lock bar broke off. What likely caused this, and what is the repair consequence?

*Your answer:*

**Question 2B-3:** After installing the new keyboard and locking the ZIF bar, the keyboard does not respond to any key presses. What is the most likely cause, and what should the technician do to resolve it?

*Your answer:*

---

## Part 3 — Symptom-to-Component Diagnostic Analysis (40 points)

### Part 3A — Symptom Identification Table

For each symptom description, identify the most likely failing component and explain your reasoning in one sentence.

| Symptom | Most Likely Failing Component | One-Sentence Reasoning |
|---------|------------------------------|----------------------|
| Laptop charges normally when the AC adapter cable is held straight, but stops charging when the cable bends slightly to the left | | |
| Laptop screen is very dim — the image is visible when you shine a flashlight on it at an angle, but the built-in display produces almost no light; laptop is from 2009 | | |
| After a RAM upgrade, the laptop immediately powers off during the POST screen; the original RAM stick works correctly | | |
| Wi-Fi connection drops entirely after the user picks up the laptop and moves across the room, even though the original Wi-Fi worked fine before a technician replaced the screen | | |
| Laptop display shows the correct image but a thin strip across the top-left corner is permanently dark; the rest of the screen is normal; laptop is two years old | | |
| Laptop does not recognize the new M.2 SSD installed by a technician; the old SATA SSD worked fine; the replacement is an NVMe drive | | |

---

### Part 3B — Full Scenario Analysis

Read each scenario carefully and provide a complete written response covering all questions asked.

**Scenario 1:**
A user brings in a laptop and says: "My laptop doesn't charge anymore. I've tried two different chargers and neither one works." The technician plugs in a known-good AC adapter from an identical model laptop. The battery indicator does not light up at all, and the laptop only operates on battery. When asked about the history of the problem, the user says it started about a month ago and seemed fine one day and dead the next — there was no gradual worsening.

Based on this symptom description, which component is most likely failing — the DC power jack, the battery, or an internal power circuit on the motherboard? Justify your answer using the distinguishing symptom characteristics covered in the Reading Guide. What is the first diagnostic step the technician should take before disassembly, and what would confirm the diagnosis?

*Your answer (aim for 75–100 words):*

**Scenario 2:**
A corporate IT department manages 200 identical business laptops, all three years old. An administrator wants to upgrade all 200 from 8 GB to 16 GB of RAM. Before ordering 200 SO-DIMM upgrade kits, the administrator asks the technician to verify the upgrade is possible.

Explain what the technician must verify in the service manual before confirming the upgrade. Name at least three specific items that must be checked. Then explain what the technician would find if the RAM turns out to be soldered, and what the organization's options would be in that case.

*Your answer (aim for 75–100 words):*

**Scenario 3:**
A user drops their laptop from desk height and it still boots, but the display now has a large crack across the upper-right corner with an irregular dark area spreading from the crack. The user asks if the screen can be repaired for less than the cost of a new laptop. The laptop is two years old and uses an LED-backlit non-touchscreen display.

Explain what has physically failed inside the display assembly, whether repair is possible for a technician at the A+ skill level, and describe the sequence of steps the technician would follow to perform the repair. Also state what tool is specifically required to avoid cracking the bezel during removal.

*Your answer (aim for 75–100 words):*

---

## Deliverables and Grading Rubric

Submit your completed lab responses as a single typed document to the Canvas assignment portal.

| Component | Points |
|-----------|--------|
| Part 1A — Component identification table (7 rows, 2 pts each) | 14 pts |
| Part 1B — Location matching (5 items, 2 pts each) | 10 pts |
| Part 1C — Safety procedure ordering (9 steps, partially ordered) | 6 pts |
| Part 2A — Disassembly steps + questions 2A-1 and 2A-2 | 14 pts |
| Part 2B — ZIF connector questions (3 questions, 4 pts each) | 12 pts |
| Part 3A — Symptom identification table (6 rows, 2 pts each) | 12 pts |
| Part 3B — Scenario analysis (3 scenarios, 11 pts each, approximately) | 32 pts |
| **Total** | **100 pts** |

**Grading Notes:**

- Component names must be correct and specific. "A cable" is not an acceptable answer where a specific connector type is expected.
- Disassembly step sequences must be in the correct order. Partial credit is awarded for correct steps in the wrong position only if the error is minor.
- Scenario analysis responses must demonstrate reasoning — state what the symptom tells you and why that points to the component you identified.

---

## Part 9 — Challenge Exercise

These advanced steps are optional and are not included in the standard grading rubric.

### Challenge Step 1 — iFixit Disassembly Guide Analysis

Visit iFixit (ifixit.com) and select a laptop disassembly guide for any model available on the site (recommended: a ThinkPad, MacBook, or Dell XPS model, as these have comprehensive guides with full photo documentation):

1. Read the full disassembly guide and document: the total number of disassembly steps, the number of distinct screw types used (note which Torx, Phillips, or proprietary bits are required), and the sequence in which major components are removed. Identify the step that represents the "point of no return" — the step after which the disassembly cannot be easily reversed without a specific replacement part.
1. Identify and describe three specific steps in the guide where the technician must take an action to prevent ESD damage or component damage that is not immediately obvious from the step description alone (for example, a step that requires touching a grounding point before touching a sensitive component, or a step where improper tool angle can crack the chassis). Explain why each step poses a risk and what the correct technique is.
1. After reviewing the guide, write a 2–3 sentence evaluation of whether the guide's difficulty rating matches your assessment of the actual complexity, referencing at least two specific steps that you believe are harder or easier than the rating suggests and explaining your reasoning.

### Challenge Step 2 — Laptop Battery Lifecycle Calculation

Using Battery University data (batteryuniversity.com) and the battery specifications of a specific laptop model:

1. Research the rated cycle count for a lithium-ion laptop battery (use a specific laptop model's battery spec sheet or the general Li-ion cycle life of 300–500 cycles to 80% capacity). Calculate: if a student charges their laptop to 100% once per day from 20%, how many months until the battery reaches 80% of original capacity? Show your calculation and identify the assumptions you made.
1. Research the effect of charge level on battery longevity: compare the cycle life of a battery charged to 100% vs. a battery kept between 20-80% charge. Document the approximate difference in cycle count and calculate how many additional months of 80%+ capacity the student would gain by adopting a 20-80% charging habit.
1. Write 2–3 sentences explaining why many modern laptops (including Apple MacBook, Lenovo ThinkPad, and Dell XPS models) include a "battery health mode" or "conservation mode" that caps charging at 80%, and describe the trade-off between daily runtime and long-term battery longevity that this mode represents.

### Challenge Step 3 — Display Panel Cross-Reference Research

Practice the panel identification workflow a technician uses when ordering a replacement display:

1. Choose any laptop model and locate the original display panel's part number by researching the laptop's service manual (available from the manufacturer's support site) or by looking up the model on a parts database such as LaptopScreen.com or Parts-People.com. Document the panel specifications: size, resolution, panel type (TN/IPS/OLED), connector type (eDP 30-pin or 40-pin, or LVDS), backlight type, and the part number.
1. Using the panel specification from step 1, find at least two compatible aftermarket replacement panels from different manufacturers that would function correctly as substitutes. Document the part numbers and note any specification differences (such as color gamut or brightness) that would be meaningful to a user.
1. Write 2–3 sentences explaining why a technician should verify the eDP connector pin count (30-pin vs. 40-pin) before purchasing a replacement panel, and describe what physical and visual symptom a technician would observe if a 30-pin eDP panel were connected to a 40-pin eDP cable (or vice versa) on a laptop motherboard.
