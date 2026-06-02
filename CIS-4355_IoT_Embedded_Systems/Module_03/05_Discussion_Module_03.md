# Discussion Forum – Module 03: Embedded Programming – C and MicroPython Basics

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Initial Post Due:** Wednesday 11:59 PM
**Peer Responses Due:** Sunday 11:59 PM
**Total Points:** 10

---

## Overview

This discussion asks you to think critically about embedded programming language choices and the security implications of low-level C code. You will choose one of three scenarios, apply Module 03 concepts, and engage substantively with two classmates.

---

## Scenario A: Medical Infusion Pump Firmware

A medical device manufacturer is developing firmware for an IV infusion pump that controls drug delivery rates with precision in microliter-per-hour increments. The pump runs on an ARM Cortex-M3 microcontroller with 64 KB of SRAM and 512 KB of flash. The firmware must respond to flow-rate alarm conditions within 10 milliseconds. A software engineer on the team proposes writing the entire firmware in MicroPython to accelerate development. The lead safety engineer objects.

In 175–225 words, address all of the following:

- Explain whether the safety engineer's objection is technically justified, citing at least two specific properties of MicroPython that conflict with the requirements of this application.
- Describe what memory allocation strategy the firmware should use and why dynamic allocation with `malloc()` is unsuitable for a safety-critical medical device.
- Identify one embedded C coding vulnerability that would be particularly dangerous in firmware controlling drug delivery (for example, an integer overflow in a dose calculation) and describe a specific coding practice that prevents it.

---

## Scenario B: Open-Source IoT Weather Station

A developer publishes an open-source MicroPython weather station project for the ESP32. The project reads temperature, humidity, barometric pressure, and wind speed, then publishes readings over Wi-Fi to a home automation dashboard. The project has 3,000 GitHub stars. A security researcher downloads the project and discovers the Wi-Fi SSID and password are hardcoded as string literals in `config.py`, which is included in the published repository.

In 175–225 words, address all of the following:

- Identify which OWASP IoT Top 10 item this represents and explain precisely how the vulnerability is exploited (for example, using the `strings` utility on a firmware binary, or reading the source directly from the repository).
- Explain the broader risk: if this device is deployed in 3,000 homes, what is the potential impact of the credential exposure?
- Propose a specific remediation: describe how the project should store Wi-Fi credentials securely on an ESP32, using MicroPython's filesystem or a provisioning workflow, without ever committing credentials to version control.

---

## Scenario C: Industrial Conveyor Belt Controller

An automotive factory uses an Arduino Mega to control conveyor belt speed and position sensors on an assembly line. The firmware has been running unmodified for 8 years. A production incident occurs when the belt speed unexpectedly jumps to maximum, damaging a batch of parts. Investigation reveals the firmware reads speed commands over UART from a supervisory system and stores them in a `char cmdBuffer[20]` using `strcpy()`. No one can explain what the supervisory system sent that day.

In 175–225 words, address all of the following:

- Hypothesize how a buffer overflow in the `strcpy()` call could have caused the belt to jump to maximum speed, explaining specifically what adjacent memory could have been overwritten and how that overwrite could produce unexpected behavior in the `loop()` function.
- Explain why this firmware survived 8 years without failure before this incident, and describe the category of conditions that can cause a latent buffer overflow to suddenly manifest.
- Propose three specific changes to the firmware that would prevent this class of vulnerability, using the embedded C concepts from Module 03.

---

## Discussion Rubric

| Component | Criteria | Points |
|---|---|---|
| Initial Post | Addresses all three bullet points with technical accuracy | 3 |
| Initial Post | Uses specific terminology from Module 03 (buffer overflow, static allocation, volatile, MicroPython REPL, etc.) | 2 |
| Initial Post | Meets 175–225 word count | 1 |
| Peer Response 1 | Substantive technical engagement (minimum 60 words) | 2 |
| Peer Response 2 | Substantive technical engagement (minimum 60 words) | 2 |
| Total | | 10 |

---

## Professor Nash's Notes

Each scenario has a correct technical answer — these are not purely opinion questions. If your classmate proposes a mitigation that is technically incorrect or incomplete, you are expected to respectfully point that out and offer the correct approach. Citing a specific function, language feature, or OWASP item strengthens any peer response. Generic agreement receives zero points.

---

End of Discussion – Module 03
