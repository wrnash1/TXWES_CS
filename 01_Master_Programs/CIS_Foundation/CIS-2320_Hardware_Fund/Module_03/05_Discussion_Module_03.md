# Discussion Forum: Module 03 - Processors (CPUs) and Cooling

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

## Instructions

Read all three scenarios below. Choose one scenario to respond to for your initial post. Clearly state which scenario you selected at the top of your post. Your initial post must be 175–225 words and must address all three sub-questions for your chosen scenario. By Sunday, write a substantive reply to at least two classmates who responded to different scenarios than your own.

---

## Scenario A — The Wrong Socket

A customer brings in a desktop PC they are building at home. They purchased an AMD Ryzen 7 5800X processor (AM4, PGA socket) and an AMD B550 motherboard. When they attempt to seat the CPU, they push down hard on it trying to get it to click into place. After several attempts, the CPU pins are visibly bent and the system will not POST.

Respond to all three of the following:

1. Explain what the customer did wrong during the installation. Describe the correct procedure for seating a PGA CPU in a ZIF socket, including what the alignment marker does and why no downward force should ever be applied.
2. Now that the pins are bent, describe the technician's repair options. Are bent PGA CPU pins always fatal to the CPU? What factors determine whether the repair is worth attempting?
3. If the customer had purchased an Intel Core i7-12700K (LGA1700) instead, would the same type of damage have occurred from pressing down? Explain how the damage scenario differs between LGA and PGA sockets when excessive force is applied.

---

## Scenario B — The Recurring Thermal Shutdown

A small office has a workstation that has been shutting down randomly for the past month. The shutdowns happen after approximately 10–15 minutes of moderate use and always require the machine to cool down before it will restart. The machine is two years old and has not been serviced since purchase. A previous technician replaced the RAM and the PSU but the problem persists.

Respond to all three of the following:

1. Based on the symptom pattern — operational for 10–15 minutes then shutdown, recovers after cooling — identify the most likely cause. Explain the mechanism by which modern CPUs protect themselves from sustained high temperatures.
2. The previous technician replaced both the RAM and the PSU without resolving the problem. Explain why each of those replacements would not have fixed this specific issue, and what the technician should have investigated instead.
3. Describe the complete repair procedure you would perform, including which component you would inspect first, how you would diagnose the exact failure point, and the step-by-step corrective action you would take.

---

## Scenario C — Upgrading a Laptop CPU

A customer asks you to upgrade the CPU in their two-year-old budget laptop to a faster processor. They have already purchased what they believe is a compatible CPU based on matching the chip series name. You open the laptop service manual and discover the current CPU is a BGA-soldered component.

Respond to all three of the following:

1. Explain to the customer what BGA packaging means and why the CPU cannot be upgraded in the field. What does the customer need to understand about how mobile processors differ from desktop processors in terms of replaceability?
2. The customer is frustrated and asks why laptop manufacturers use BGA instead of socketed CPUs. Provide a technically accurate explanation of the advantages BGA offers in the context of mobile and thin device design, even though it eliminates field repairability.
3. If this laptop were a higher-end model from a different manufacturer and used a socketed mobile CPU (MXM or similar), how would the upgrade conversation be different? What compatibility checks would still be required even with a socketed mobile CPU?

---

## Discussion Rubric (10 Points Total)

Initial Post — 6 points:

- 5–6 pts: Addresses all three sub-questions with technical accuracy, appropriate terminology, and clear reasoning. Meets the 175–225 word count requirement.
- 3–4 pts: Addresses most sub-questions but lacks technical detail, contains inaccuracies, or does not meet the word count.
- 0–2 pts: Incomplete, missing, or does not engage with the scenario content.

Peer Responses — 4 points:

- 4 pts: Responds constructively to at least two classmates who chose different scenarios. Adds new information, corrects an error, or extends the discussion with a relevant example or follow-up question.
- 2 pts: Responds to only one classmate, or responses are superficial and do not add substance to the discussion.
- 0 pts: No peer responses submitted by Sunday at 11:59 PM.

---

A note from Professor Nash: CPU and cooling problems are among the most common hardware calls you will take as a technician. The three scenarios this week are not hypothetical — variations of each happen in shops and on-site visits every week. The socket damage scenario in particular is one that many beginner builders encounter. Understanding why it happens and how to explain it to a customer is just as important as knowing the technical fix. Push yourself to be precise in your answers — "the CPU got hot" is not an explanation; "the CPU reached TJMax and the BIOS initiated thermal protection shutdown" is.
