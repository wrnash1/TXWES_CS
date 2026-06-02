# Discussion Forum: Module 06 - Power Supplies and System Cooling

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

---

### Overview

This discussion asks you to apply what you learned in Module 06 to realistic workplace scenarios involving power supply selection, connector identification, and thermal management. Choose one of the three scenarios below and respond to all three sub-questions within it. Your initial post should be 175–225 words and must use accurate technical terminology from the module. You are not required to respond to the same scenario as your peers.

---

### Scenario A — The Failing Build

A customer drops off a newly self-built gaming PC that will not POST. They report that all fans spin for a few seconds and then the system powers off. They purchased a 550W 80 Plus Bronze PSU for a system with a 125W CPU and a 250W GPU. They connected the 24-pin ATX cable but are not sure about the smaller cable near the top of the motherboard. The GPU has a single 8-pin PCIe power connector that is also connected.

Respond to all three of the following:

1. Identify the most likely missing or incorrect cable connection. Name the connector, explain what it powers, and describe where it is located on the motherboard.
2. The customer asks whether the 550W 80 Plus Bronze PSU is adequate for their build. Using the TDP figures provided (125W CPU + 250W GPU), add reasonable estimates for the remaining components and apply the 25% headroom method to determine whether 550W is sufficient or whether an upgrade is needed. Show your calculation.
3. The customer mentions they want to upgrade to an 80 Plus Gold PSU because they heard it "gives the PC more power." Correct this misconception and explain what the Gold certification actually means for their system and their electricity bill.

---

### Scenario B — The Overheating Workstation

An IT department reports that a video editing workstation is crashing after about 30 minutes of rendering, even though CPU and GPU utilization appear normal. A technician opens the case and finds the following: the front intake fans are running but their airflow arrows point outward; the rear exhaust fan is running but its arrow points into the case; the top exhaust fans are correctly installed. The case has no dust filters on the front panel, and the intake slots are visibly clogged with dust.

Respond to all three of the following:

1. Identify all fan orientation errors in the described configuration. For each incorrect fan, state what it is actually doing in its current state and what the correct orientation should be.
2. Explain the overall airflow problem this combination of errors creates. Using the front-to-back, bottom-to-top airflow model, describe how heat is being trapped or recirculated and which components are most at risk.
3. After fixing the fan orientations, the technician counts three front intake fans and one rear exhaust fan. Is this positive or negative pressure? What is the practical implication for dust management in a workstation environment, and what additional hardware change would most improve dust control?

---

### Scenario C — The PSU Sizing Debate

A small business is purchasing five identical desktop workstations for an office. Each workstation will have a 65W CPU, integrated graphics only, 16 GB of RAM (two sticks), one NVMe SSD, and a standard ATX motherboard. A vendor is offering two PSU options for these builds: a 400W 80 Plus Bronze unit and a 650W 80 Plus Gold unit. The 650W option costs $30 more per unit.

Respond to all three of the following:

1. Using the wattage calculation method from the module, estimate the total system load for one of these workstations and apply the 25% headroom buffer to determine the minimum recommended PSU wattage. Based on your calculation, which PSU option is the minimum appropriate choice?
2. The purchasing manager argues for the 650W Gold units, saying the higher efficiency will save money on electricity over time. Evaluate this argument. Is the Gold unit justified for these specific workstations, or is the Bronze unit the better business decision? Consider load percentage and efficiency performance.
3. One of the workstations will occasionally be used for light video encoding using the CPU — no GPU involvement. The technician is concerned the PSU may struggle under that load. Explain whether this concern is valid based on your wattage calculation, and describe the symptom a user would experience if the PSU were actually undersized during an encoding task.

---

### Grading Rubric — 10 Points Total

Initial Post — 6 Points (due Wednesday at 11:59 PM):

- 5–6 pts: Addresses all three sub-questions with technical accuracy, uses correct terminology from the module (connector names, pin counts, wattage calculation method, efficiency tier definitions, airflow terms), and meets the 175–225 word count.
- 3–4 pts: Addresses most sub-questions but lacks technical detail, uses vague or incorrect terminology, or falls short of the word count.
- 0–2 pts: Post is missing, addresses fewer than two sub-questions, or contains significant factual errors.

Peer Responses — 4 Points (due Sunday at 11:59 PM):

- 4 pts: Replies to at least two classmates with substantive technical additions — for example, identifying a calculation error and showing the correct result, providing an alternative connector scenario, or expanding on an airflow concept the peer did not fully address.
- 2 pts: Replies to only one peer, or responses are brief and non-technical (e.g., "I agree with your analysis!").
- 0 pts: No peer responses submitted.

Peer responses must be at least 50 words each and must add new technical content, not simply restate the peer's answer.

---

### Professor Nash's Note

One of the most practical skills you will use in this field is PSU sizing — and one of the most common mistakes I see in the field is a technician who either undersizes a PSU and causes instability or massively oversizes it and wastes a client's budget. The calculation method in this module is straightforward once you practice it. Use this discussion as a chance to work through that calculation in a real-ish context and get feedback from your peers. I look forward to reading your reasoning.
