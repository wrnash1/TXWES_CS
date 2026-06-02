# Lab Activity: Module 07 - Display Technologies and Connectors

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

**Certification Alignment:** Domain 1.1 — Install and configure laptop hardware | Domain 3.1 — Install and configure display components

**Estimated Completion Time:** 60-75 minutes

**Submission:** Upload your completed lab worksheet (PDF or Word document) to the Canvas Lab 07 assignment by the posted deadline.

---

### Lab Overview

This lab develops three skills assessed on the CompTIA A+ Core 1 exam: display connector identification, resolution and refresh rate compatibility analysis, and multi-monitor signal path tracing. You will work from connector descriptions, specification tables, and setup diagrams. No physical hardware is required, though students who have access to monitors, cables, or a computer with a discrete GPU are encouraged to examine physical connectors alongside the worksheet.

There are three parts:

- Part 1 — Display Connector Identification
- Part 2 — Resolution and Refresh Rate Compatibility Analysis
- Part 3 — Multi-Monitor Signal Path Tracing

Complete all three parts and answer all observation questions before submitting.

---

### Safety and Handling Notes (for students examining physical monitors or cables)

If you have access to a physical monitor or PC for this exercise, observe the following:

- Power off the monitor before connecting or disconnecting any display cable to avoid static discharge to the panel driver board
- Never press on the LCD or OLED panel surface — the panel is fragile and can be permanently damaged by pressure
- Do not force any connector into a port; display connectors are keyed and will only insert in one orientation
- Older CRT monitors contain extremely high-voltage circuitry — never open a CRT housing

---

## Part 1 — Display Connector Identification

### Part 1 Overview

Below are descriptions of eight display connectors, cables, or related components. For each item, complete the identification table by recording the connector name, pin count, whether it carries audio, whether it supports MST daisy-chaining, and the signal type (digital, analog, or both).

Use your reading guide glossary, comparison tables, and video lecture notes as references.

### Part 1 Identification Table

| Item # | Item Description | Connector Name | Pin Count | Carries Audio? | MST Daisy-Chain? | Signal Type |
|---|---|---|---|---|---|---|
| 1 | A 19-pin trapezoidal connector; most common connector on consumer TVs and monitors; found on gaming consoles; carries both video and audio on one cable | | | | | |
| 2 | A 20-pin connector with one angled corner preventing incorrect insertion; preferred for high-refresh-rate PC monitors; supports multi-monitor from one output via MST hub | | | | | |
| 3 | A connector with a 24-pin block and a flat blade alongside it; no four-pin cross-cluster present; carries digital signal only; can passively adapt to HDMI | | | | | |
| 4 | A connector with a 24-pin block, a flat blade, and four additional pins arranged in a cross-shaped cluster; carries both digital and analog signals; can passively adapt to VGA | | | | | |
| 5 | A 15-pin three-row connector, typically blue; carries only analog video; signal quality degrades with cable length; found on legacy projectors | | | | | |
| 6 | A small connector found on older Apple MacBooks and some laptops; approximately half the size of its full-size counterpart; supports MST; adapts to HDMI with a passive adapter | | | | | |
| 7 | An external device with one DisplayPort input port and three DisplayPort output ports; allows a single GPU output to drive three independent monitors simultaneously | | | | | |
| 8 | A cable variant with a trapezoidal connector that is noticeably smaller than full-size; found on compact cameras, tablets, and some laptops; 19 pins; does not support MST | | | | | |

### Part 1 Observation Questions

Answer each question in 2-4 complete sentences.

**Observation 1A:** Items 3 and 4 look almost identical from a distance. Explain the specific physical feature a technician should look for to distinguish them, and describe a real-world scenario where confusing the two would cause a problem for a user.

*Your answer:*

---

**Observation 1B:** A customer wants to connect a new high-refresh-rate gaming monitor (DisplayPort input only) to an older GPU that has only HDMI and DVI-D outputs. Describe the most appropriate connection solution. Explain whether a passive adapter is sufficient or whether an active converter is required, and identify any resolution or refresh rate limitation the customer should be aware of.

*Your answer:*

---

**Observation 1C:** Item 7 is a DisplayPort MST hub. Explain how MST allows one GPU port to drive multiple independent displays, and state which competing connector standard cannot use an MST hub for the same purpose. Why is this capability important for compact workstations that have limited GPU output ports?

*Your answer:*

---

## Part 2 — Resolution and Refresh Rate Compatibility Analysis

### Part 2 Overview

The table below lists ten display setup scenarios. Each scenario specifies a monitor's target resolution and refresh rate, the cable type and version being used, and whether the GPU supports the output. For each scenario, determine whether the setup will display at the advertised specification, and if not, identify the specific limiting factor and suggest the minimum cable upgrade needed.

### Part 2 Compatibility Analysis Table

| # | Target Resolution | Target Refresh Rate | Cable Used | GPU Supports Output? | Will It Display at Target Spec? | If Not: Limiting Factor | Minimum Cable Fix |
|---|---|---|---|---|---|---|---|
| 1 | 4K (3840x2160) | 60Hz | HDMI 1.4 | Yes | | | |
| 2 | 4K (3840x2160) | 30Hz | HDMI 1.4 | Yes | | | |
| 3 | 1080p (1920x1080) | 144Hz | HDMI 2.0 | Yes | | | |
| 4 | 4K (3840x2160) | 120Hz | HDMI 2.0 | Yes | | | |
| 5 | 4K (3840x2160) | 60Hz | DisplayPort 1.2 | Yes | | | |
| 6 | 4K (3840x2160) | 144Hz | DisplayPort 1.4 | Yes | | | |
| 7 | 1440p (2560x1440) | 165Hz | HDMI 2.0 | Yes | | | |
| 8 | 1080p (1920x1080) | 60Hz | VGA | Yes (analog output) | | | |
| 9 | 4K (3840x2160) | 60Hz | HDMI 2.0 | No (GPU max: 1080p@60Hz) | | | |
| 10 | 8K (7680x4320) | 60Hz | HDMI 2.1 | Yes | | | |

Reference for your analysis:

- HDMI 1.4: max 4K@30Hz
- HDMI 2.0: max 4K@60Hz
- HDMI 2.1: max 4K@120Hz, 8K@60Hz
- DisplayPort 1.2: max 4K@60Hz
- DisplayPort 1.4: max 4K@144Hz, 8K@60Hz
- VGA: analog only; maximum practical resolution is 1920x1200; no 4K support

### Part 2 Observation Questions

**Observation 2A:** Scenarios 1 and 2 use identical hardware (same monitor, same GPU, same cable version) but produce different results. Explain why Scenario 2 works while Scenario 1 does not. What does this tell a technician about the relationship between cable version, resolution, and refresh rate?

*Your answer:*

---

**Observation 2B:** In Scenario 9, the GPU itself is the limiting factor rather than the cable. A customer insists they just need to "buy a better cable" to display 4K@60Hz. Is this correct? Explain what the cable can and cannot solve, and what the customer would actually need to upgrade to achieve the target specification.

*Your answer:*

---

## Part 3 — Multi-Monitor Signal Path Tracing

### Part 3 Overview

The description below defines a three-monitor workstation setup. Read the configuration carefully, then complete the signal path table and answer the observation questions. Identify any errors in the configuration that would prevent a display from working at its specified settings.

### Workstation Setup Description

A graphic designer's workstation has the following hardware:

- GPU: NVIDIA mid-range card with two DisplayPort 1.4 outputs, one HDMI 2.0 output, and one DVI-D output
- Monitor A: 27-inch 4K IPS monitor, native resolution 3840x2160, 60Hz, one DisplayPort input, one HDMI 2.0 input — connected via the GPU's HDMI 2.0 port using an HDMI 1.4 cable
- Monitor B: 24-inch 1440p IPS monitor, native resolution 2560x1440, 144Hz, one DisplayPort 1.4 input — connected via the GPU's first DisplayPort 1.4 port using a DisplayPort 1.4 cable
- Monitor C: 22-inch 1080p VGA-only legacy monitor, native resolution 1920x1080, 60Hz, VGA input only — connected via the GPU's DVI-D output using a passive DVI-D to VGA adapter

### Part 3 Signal Path Table

For each monitor, trace the complete signal path from GPU port to display, identify the cable and connector types in use, state whether the connection will achieve the monitor's native resolution at the target refresh rate, and if not, identify the specific problem.

| Monitor | GPU Port Used | Cable/Adapter Used | Monitor Input Port | Achieves Native Resolution and Refresh Rate? | If Not: Specific Problem |
|---|---|---|---|---|---|
| A | | | | | |
| B | | | | | |
| C | | | | | |

### Part 3 Configuration Error Questions

**Error Analysis 3A:** Monitor A is not displaying at 4K@60Hz even though both the GPU and the monitor support it. Identify the exact component in the signal path that is the limiting factor, explain why it causes the problem, and state the minimum change needed to fix it.

*Your answer:*

---

**Error Analysis 3B:** Monitor C is connected via a passive DVI-D to VGA adapter. Explain whether this connection will work. If it does not work, identify the specific reason and describe what the technician should use instead to connect this VGA-only monitor to the DVI-D port.

*Your answer:*

---

**Error Analysis 3C:** The designer decides to add a fourth monitor (Monitor D) — a 1080p@60Hz display with one HDMI 2.0 input and one DisplayPort 1.4 input. The GPU's remaining available output is the second DisplayPort 1.4 port. Which input on Monitor D should the designer use to connect to this port, and is a DisplayPort-to-HDMI adapter required or should a native cable be used? Justify your answer.

*Your answer:*

---

### Deliverables and Submission

Submit one document (PDF or Word) containing:

1. Completed Part 1 Identification Table with all eight items filled in
2. Answers to all three Part 1 Observation Questions
3. Completed Part 2 Compatibility Analysis Table for all ten scenarios
4. Answers to both Part 2 Observation Questions
5. Completed Part 3 Signal Path Table for all three monitors
6. Answers to all three Part 3 Error Analysis Questions

Upload to the Canvas Lab 07 assignment portal before the posted deadline.

---

### Grading Rubric

| Section | Points Possible | Criteria |
|---|---|---|
| Part 1 — Identification Table (8 items) | 16 pts | 2 pts per item: connector name correct (1 pt) + at least two other fields correct (1 pt) |
| Part 1 — Observation Questions (3) | 12 pts | 4 pts each: technically accurate, complete sentences, correct terminology |
| Part 2 — Compatibility Table (10 scenarios) | 20 pts | 2 pts per scenario: correct Yes/No determination (1 pt) + correct factor or fix where applicable (1 pt) |
| Part 2 — Observation Questions (2) | 8 pts | 4 pts each: demonstrates understanding of bandwidth, cable version, and GPU limitations |
| Part 3 — Signal Path Table (3 monitors) | 12 pts | 4 pts per monitor: port correct (1), cable correct (1), correct Yes/No (1), problem identified if applicable (1) |
| Part 3 — Error Analysis Questions (3) | 12 pts | 4 pts each: identifies correct problem, correct fix, correct terminology |
| **Total** | **80 pts** | |

---

### Troubleshooting Reference

If you are unsure about a connector, cable version, or compatibility determination, refer to the following resources before submitting:

- Reading Guide Section 3 (Connector Comparison Table), Section 4 (HDMI Bandwidth Reference), and Section 5 (DisplayPort Bandwidth Reference)
- Professor Messer's CompTIA A+ Core 1 free course at [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- CompTIA A+ exam objectives Domain 3.1 at [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a)
