# Lab Activity: Module 16 - Final Exam Preparation

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

---

## Overview

This final lab practical spans all fifteen modules of CIS-2320 Hardware Fundamentals and directly simulates the types of questions and tasks you will encounter on the CompTIA A+ Core 1 (220-1101) exam. The lab has three parts: component and connector identification from descriptions, scenario-based diagnostic exercises using the seven-step troubleshooting methodology, and a structured review of the official exam registration process.

Students who complete this lab with full documentation are, in the assessors' experience, well-prepared for the certification exam. Take your time. Write complete sentences for all analytical questions.

**Total Points: 100**
**Due:** See Canvas assignment for deadline.

---

## Prerequisites

Before beginning this lab, confirm the following:

- You have reviewed the Module 16 reading guide, including the domain map, the high-yield rapid reference table, and all eight certification exam tips.
- You have worked through the quizzes from Modules 14, 15, and 16.
- You have reviewed at least three additional prior module quizzes, focusing on modules where you scored below 80%.
- You have access to the Module 16 Canvas module for the component identification images.

---

## Part 1: Component and Connector Identification (35 Points)

### Part 1 Objective

Identify hardware components, connectors, and specifications from descriptions, and demonstrate the ability to match components to their correct use cases — the type of knowledge tested directly in Domain 3 questions on the A+ Core 1 exam.

### Part 1 Background

The CompTIA A+ exam presents photographs and descriptions of components and asks candidates to identify them by name, specification, or use case. This exercise builds that identification skill across the full breadth of course content — storage, RAM, power supply connectors, display connectors, network cables, and USB connectors.

### Part 1 Procedure

#### Component Identification Exercise (20 points)

For each of the twenty component or connector descriptions below, provide: (a) the component or connector name, and (b) one sentence stating a key specification or use-case fact a technician must know about it.

Description 1: A rectangular power connector with 24 individual pins arranged in two rows of 12. It plugs into the largest connector on the motherboard.

Description 2: An 8-pin power connector that plugs into a dedicated socket near the CPU socket on the motherboard. It is sometimes built as a 4+4 pin split.

Description 3: A storage interface connector carrying a thin, flat cable with a small L-shaped data connector (7 pins) and a separate wider power connector (15 pins).

Description 4: A storage form factor that fits into a slot directly on the motherboard, measuring either 42 mm or 80 mm in length, available in both SATA and NVMe protocol variants.

Description 5: A network cable connector with 8 conductors arranged in two rows of 4, with a locking plastic clip on the top. Used for Ethernet connections.

Description 6: A network cable connector with 6 conductors, slightly narrower than Connector 5. Commonly used for telephone landline connections.

Description 7: A fiber optic connector with a small square push-pull design. No locking tab. Associated with older fiber installations.

Description 8: A fiber optic connector with a small form factor and a locking tab mechanism. The most common connector type in modern data center fiber installations.

Description 9: A display connector with 15 pins in three rows inside a trapezoidal shell. Carries only analog video signal. Legacy connector found on older monitors and projectors.

Description 10: A display connector with multiple pins in a flat rectangular shell, capable of carrying digital video, audio, and data. The only mainstream display connector that supports monitor daisy-chaining via MST.

Description 11: A RAM module with 288 pins. Full-size form factor for desktop motherboards. Fourth-generation DDR standard.

Description 12: A RAM module with 260 pins. Smaller form factor for laptop motherboards. Fourth-generation DDR standard.

Description 13: A rectangular slot on a motherboard, approximately 89 mm long. Designed for graphics cards and other high-bandwidth add-in cards. The longest standard PCIe slot size.

Description 14: A rectangular slot on a motherboard, approximately 25 mm long. The shortest standard PCIe slot, used for sound cards and low-bandwidth network cards.

Description 15: A USB connector that is oval in shape, symmetrical, and reversible — can be inserted in either orientation. Standard on modern smartphones and laptops.

Description 16: A USB connector that is rectangular, approximately 12 mm wide. The standard host-side connector found on computers, chargers, and hubs.

Description 17: A USB connector that is square with beveled top corners. Found on the peripheral-side of printers and external storage docks.

Description 18: A power connector with four pins in a 2x2 arrangement, used to power older devices and some case fans in legacy systems.

Description 19: A 6-pin or 8-pin power connector that supplies supplemental power directly to a graphics card. Required on GPUs that draw more power than the PCIe slot can provide.

Description 20: An Apple proprietary connector with 8 pins arranged in a flat, symmetrical blade design. Used on iPhones through the iPhone 14 generation.

#### Specification Matching Exercise (15 points)

For each scenario below, identify the correct specification or component and explain your reasoning in one to two sentences.

Scenario 1: A technician is running new Ethernet cable to a workstation 85 meters from the network closet. The connection must support 10 Gbps. Which cable category is required, and why is the alternative category insufficient?

Scenario 2: A new workstation has two 16 GB DDR4 RAM modules. The motherboard has four slots labeled A1, A2, B1, and B2. Where should the two modules be installed to enable dual-channel operation, and what happens if they are installed in A1 and A2 instead?

Scenario 3: A technician is building a budget workstation and needs to add a discrete GPU. The GPU requires an 8-pin PCIe power connector but the PSU only has a single 6+2 pin PCIe cable. Is this PSU cable compatible with the GPU's 8-pin requirement? Explain.

Scenario 4: A server administrator needs to configure storage with the following requirements: minimum three drives, one drive failure tolerance, and read performance better than a single drive. Which RAID level should be used?

Scenario 5: A user's laptop has a USB-C port. They connect a USB-C external hard drive and measure transfer speeds of only 25 MB/s. The drive is rated for 400 MB/s. What is the most likely cause of the speed discrepancy?

#### Part 1 Grading Rubric

- Twenty component/connector identifications with key fact (1 point each): 20 points
- Five specification matching scenarios with correct answer and reasoning: 15 points (3 points each)

---

## Part 2: Scenario-Based Diagnostic Exercises (40 Points)

### Part 2 Objective

Apply the CompTIA A+ seven-step troubleshooting methodology to realistic hardware and network failure scenarios, documenting each step taken and the reasoning behind it.

### Part 2 Background

Domain 5 (Hardware and Network Troubleshooting) accounts for 29% of the A+ Core 1 exam — the single largest domain. Exam questions present a symptom and ask which troubleshooting step comes next, which component to test first, or which tool to use. Practicing the seven-step methodology in writing reinforces both the process and the domain vocabulary. For each scenario below, document your work using the seven-step structure.

### Part 2 Procedure

Work through all four diagnostic scenarios. For each scenario, structure your written response using the seven steps. You do not need to resolve the scenario with certainty — the goal is to demonstrate correct methodology: gathering information, forming a theory, testing it systematically, and documenting your reasoning.

#### Diagnostic Scenario 1: No Video Output on Desktop (10 points)

A user calls the help desk reporting that their desktop PC powers on (fans spin, power LED activates, keyboard lights flash) but the monitor displays no video — just a black screen with "No Signal" shown briefly before the screen goes dark. The monitor works on another computer. The PC was working yesterday. No changes were made by the user.

Document your response through all seven troubleshooting steps. Include: what information you would gather in Step 1, what theories you would consider in Step 2 (list at least three in order of likelihood), how you would test the most probable theory in Step 3, and what resolution steps you would implement in Step 5.

#### Diagnostic Scenario 2: Laptop Does Not Power On (10 points)

A user reports their laptop will not turn on at all when the power button is pressed. The AC adapter is plugged in. A small LED on the adapter body is illuminated, indicating the adapter is receiving power from the wall outlet. The user says the laptop was working this morning but stopped responding after a meeting.

Document your response through all seven troubleshooting steps. Note at least two different hardware components you would investigate and explain why each is a suspect given the described symptoms. Explain why you would not begin by reinstalling the operating system.

#### Diagnostic Scenario 3: Laser Printer Produces Smeared Output (10 points)

The laser printer in the accounting department produces pages where printed content is fully visible but smears when touched. The toner cartridge was replaced last week as routine maintenance and has printed approximately 200 pages since replacement. No other changes were made to the printer.

Document your response through all seven troubleshooting steps. In Step 2, identify the EP process stage responsible for this symptom and name the specific component most likely failing. In Step 3, describe a non-destructive test you would perform before ordering replacement parts. In Step 5, describe the corrective action.

#### Diagnostic Scenario 4: Workstation Cannot Reach Internet But Others Can (10 points)

A workstation on a corporate network can connect to local network resources (file server, print server, internal applications) but cannot browse the internet or reach any external address. Other workstations on the same switch and subnet connect to the internet normally. The affected workstation's IP address, subnet mask, and DNS server settings appear correct in the network adapter settings.

Document your response through all seven troubleshooting steps. In Step 2, identify at least two probable causes given that local connectivity works but internet connectivity does not. Reference the OSI model to explain at which layer(s) the problem likely exists. In Step 3, describe the specific command-line tests you would run and what each test result would tell you.

#### Part 2 Grading Rubric

- Each scenario: correct seven-step structure used, reasonable theories proposed, correct component or tool identified, methodology followed without jumping to conclusions — 10 points each.
- Partial credit: scenarios that demonstrate understanding of the methodology but miss one step or propose an incomplete theory — 7 to 9 points.
- Minimal credit: scenarios where methodology is not followed but the correct answer is eventually identified — 4 to 6 points.

---

## Part 3: Exam Registration Verification (25 Points)

### Part 3 Objective

Confirm awareness of the CompTIA A+ Core 1 exam format, scoring, and registration process, and document your personal exam preparation plan.

### Part 3 Background

Earning the CompTIA A+ certification requires passing two exams: Core 1 (220-1101) and Core 2 (220-1102). CIS-2320 Hardware Fundamentals prepares you for Core 1. Passing both exams earns the A+ credential, which is valid for three years and renewable through CompTIA's CE (Continuing Education) program.

### Part 3 Procedure

#### Exam Format Knowledge Check (10 points)

Answer the following questions about the CompTIA A+ Core 1 exam in complete sentences. Your answers should reflect the official exam specifications.

Question A: What is the maximum number of questions on the A+ Core 1 (220-1101) exam, and how much time is allotted?

Question B: What is the passing score for the A+ Core 1 exam, expressed on the CompTIA scale?

Question C: Name the five exam domains and their approximate percentage weights.

Question D: What are the four question types used on the A+ Core 1 exam? Briefly describe what performance-based questions involve.

Question E: How long is the CompTIA A+ certification valid after passing, and what is required to renew it?

#### Personal Exam Preparation Plan (15 points)

Write a structured exam preparation plan of at least 200 words covering the following elements:

Element 1 — Self-assessment: Identify two to three specific topic areas from this course where you feel least confident. Be specific — name the domain, the topic, and the specific concept (for example: "Domain 3 — I am uncertain about RAID level minimum drive counts and fault tolerance").

Element 2 — Study plan: For each weak area identified, describe the specific action you will take to address it before the exam (specific module reading guide sections, specific Professor Messer videos at professormesser.com, practice question sets).

Element 3 — Exam logistics: State whether you plan to test at a Pearson VUE testing center or through online proctoring. Describe one action you will take this week to move toward your exam registration (visiting comptia.org, contacting the testing center, or confirming your registration if already scheduled).

Element 4 — Timeline: State your target exam date and describe a realistic study schedule for the days between now and that date.

#### Part 3 Grading Rubric

- Five exam format knowledge questions (2 points each): 10 points
- Personal exam preparation plan with all four elements addressed, minimum 200 words, specific and actionable: 15 points

---

## Submission Instructions

Compile your complete lab report as a single document with clearly labeled sections for Parts 1, 2, and 3. Include all component identifications, scenario responses structured using the seven troubleshooting steps, and your personal preparation plan. Export as PDF and upload to the Module 16 Lab Assignment in Canvas by the posted deadline.

Written responses must use complete sentences. Lists are acceptable for component identifications and step-by-step documentation but must include explanatory sentences for all analytical questions. Late submissions receive a 10-point deduction per day unless an extension has been approved by Professor Nash before the deadline.

---

## Part 9 — Challenge Exercise

These advanced steps are optional and are not included in the standard grading rubric.

### Challenge Step 1 — Performance-Based Question (PBQ) Simulation

CompTIA A+ Core 1 includes Performance-Based Questions (PBQs) that require clicking, dragging, matching, or ordering answers rather than selecting from a list. Practice the following PBQ-style exercises:

1. Without any reference materials, write out the complete laser EP process in order — all six stages, the responsible component for each stage, and one print quality defect that the failure of each component produces. Time yourself: the goal is to complete this exercise in under 90 seconds. Then check your answers against Module 15 content. Repeat until you can complete it correctly from memory within the time limit.
1. From memory, draw or write out the T568B pinout for all eight pins of an RJ-45 connector, the IPv4 address classes (A, B, C, D, E) with their default subnet masks and address ranges, and the OSI model seven layers with one protocol or device example at each layer. These three tables collectively cover a significant portion of the A+ Core 1 exam's network content.
1. Research what types of PBQs appear on the CompTIA A+ Core 1 exam (drag-and-drop network topology, cable matching, BIOS/UEFI navigation simulation) and describe in 2–3 sentences the study strategy that best prepares you for PBQ-style questions compared to the multiple-choice preparation strategy used throughout this course.

### Challenge Step 2 — Timed Mixed-Domain Practice Assessment

Using the ExamCompass free practice exam simulator (examcompass.com) or any available A+ Core 1 practice question bank, complete the following self-assessment:

1. Take a full-length timed practice exam (90 questions, 90 minutes) without reference materials. After completing the exam, record your score by domain and identify which of the five Core 1 domains (Mobile Devices, Networking, Hardware, Virtualization and Cloud, Hardware and Network Troubleshooting) had the lowest accuracy. Document your per-domain scores.
1. For each question you answered incorrectly, write a one-sentence explanation of why the correct answer is correct and why your chosen answer was incorrect. This active error analysis process is more effective for retention than simply re-reading the correct answer.
1. Based on your domain accuracy results, create a targeted study schedule for the 14 days before your exam appointment — allocating review time proportionally to your weakest domains. For example, if Hardware Troubleshooting is 60% of your errors and you have 14 study sessions remaining, assign approximately 8-9 sessions to troubleshooting content and distribute the remaining sessions across stronger domains for maintenance review.

### Challenge Step 3 — Hardware Identification Speed Drill

Build fluency with hardware identification by completing the following exercises against a time limit:

1. Using PCPartPicker (pcpartpicker.com), select one complete PC build from the community-submitted completed builds section. For each component in the build, identify: the form factor (ATX/M-ATX/ITX for motherboard, DIMM/SO-DIMM for RAM, 2.5"/3.5"/M.2 for storage), the interface type (SATA/NVMe/PCIe), and the wattage impact on PSU selection. Calculate the total estimated system wattage and verify whether the listed PSU wattage provides at least a 20% headroom margin above the estimated load.
1. Time yourself identifying the following from memory in under 2 minutes (write or verbalize each answer): (a) the difference between an LGA and PGA CPU socket and which AMD and Intel platforms use each; (b) the number of pins on DDR3, DDR4, and DDR5 DIMMs; (c) the PCIe slot sizes (x1, x4, x8, x16) and their typical use cases; (d) the four RAID levels (0, 1, 5, 10) with minimum drive count and fault tolerance for each. These four topics appear in multiple-choice and scenario questions across the exam.
1. Write a one-page study summary in your own words (no copy-paste) covering the five topics you found most difficult across the entire 16-module course. This active recall and synthesis exercise is one of the most research-supported methods for consolidating knowledge before a certification exam. Submit this summary as an additional deliverable with your Module 16 lab if you choose to complete this challenge step.
