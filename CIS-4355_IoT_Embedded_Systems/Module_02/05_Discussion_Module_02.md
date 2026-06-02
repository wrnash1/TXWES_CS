# Discussion Forum – Module 02: Microcontrollers – Arduino and Raspberry Pi Basics

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Initial Post Due:** Wednesday 11:59 PM
**Peer Responses Due:** Sunday 11:59 PM
**Total Points:** 10

---

## Overview

This discussion asks you to apply your knowledge of microcontroller and single-board computer capabilities to realistic IoT design decisions. You will choose one of three scenarios, analyze it using the technical concepts from Module 02, and respond substantively to two classmates.

---

## Scenario A: Smart Wildlife Monitoring Collar

A conservation organization wants to attach GPS and temperature monitoring collars to 500 wolves in Yellowstone National Park. Each collar must transmit a location and body-temperature reading once per hour. The collar must operate for 18 months on a sealed, non-replaceable battery pack. No cellular coverage exists for 70 percent of the monitored range, so data is buffered locally and uploaded when the animal comes within range of a LoRa base station.

In 175–225 words, address all of the following:

- Explain why a microcontroller rather than a Raspberry Pi is the appropriate core platform for this collar, citing at least two specific technical constraints from the scenario.
- Identify which Arduino-class communication interfaces (UART, SPI, I2C) would likely be used to connect the GPS module and temperature sensor, and justify each choice.
- Describe one hardware security concern relevant to this device (such as an exposed debug port or unencrypted local storage of location data) and propose a mitigation.

---

## Scenario B: University Makerspace Equipment Monitor

Texas Wesleyan's engineering makerspace wants to monitor power consumption on 20 laser cutters, 3D printers, and CNC mills. Each machine should have a current sensor that logs energy use every 30 seconds, displays live consumption on a small OLED screen, and uploads daily summaries to a campus web dashboard over Wi-Fi. A lab manager can SSH into each monitor unit to check logs remotely.

In 175–225 words, address all of the following:

- Explain why a Raspberry Pi is a better choice than an Arduino Uno for this application, citing at least two capabilities from the scenario that require an SBC rather than a microcontroller.
- Identify which communication interface (I2C, SPI, or ADC) you would use for the current sensor and for the OLED display, and justify each choice.
- Describe one security risk introduced by enabling SSH access on all 20 units and propose a specific mitigation that follows least-privilege principles.

---

## Scenario C: Automated Greenhouse Control System

A small commercial greenhouse uses soil moisture sensors, air temperature and humidity sensors, and motorized vent actuators to maintain optimal growing conditions. The system must respond to a soil-moisture drop within 5 seconds by activating a drip irrigation valve. It must also log all sensor readings to a local SQLite database for weekly trend analysis and generate PDF reports for the owner. The system runs on 120V AC power and has reliable Wi-Fi.

In 175–225 words, address all of the following:

- Argue for a hybrid design using both a microcontroller and a Raspberry Pi, explaining specifically which functions each platform handles and why each function maps to that platform.
- Identify the communication interface that the microcontroller would use to send sensor data to the Raspberry Pi, and explain why you chose it over the alternatives.
- Explain one GPIO voltage compatibility concern that arises when connecting the microcontroller's outputs to the Raspberry Pi's inputs, and describe the circuit solution.

---

## Discussion Rubric

| Component | Criteria | Points |
|---|---|---|
| Initial Post | Addresses all three bullet points for the chosen scenario with technical accuracy | 3 |
| Initial Post | Uses specific technical terms from Module 02 (GPIO, I2C, SPI, ADC, BCM, PWM, sketch, etc.) | 2 |
| Initial Post | Meets the 175–225 word count requirement | 1 |
| Peer Response 1 | Provides substantive technical feedback or an alternative design perspective (minimum 60 words) | 2 |
| Peer Response 2 | Provides substantive technical feedback or an alternative design perspective (minimum 60 words) | 2 |
| Total | | 10 |

---

## Professor Nash's Notes

You must choose exactly one scenario and address all three bullets within the word count. Posts that attempt two scenarios receive credit for neither. Your peer responses must engage with the technical substance of your classmate's post — question a design choice, propose an alternative interface selection, or add a constraint they did not consider. Responses limited to agreement or praise receive zero credit.

---

End of Discussion – Module 02
