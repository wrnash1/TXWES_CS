# Lab Activity: Module 10 - Troubleshooting Boot Issues

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 5.3 | CompTIA A+ Core 2 (220-1102) — Domain 3.1
**Total Points:** 100
**Submission:** Upload your completed lab document to the Canvas assignment portal before the due date.

---

## Overview

This lab has three parts. Part 1 is a boot failure scenario analysis exercise using the four-stage diagnostic framework. Part 2 is a UEFI navigation and boot order exercise. Part 3 is a POST and BSOD stop code diagnostic exercise. No physical hardware disassembly is required for any part, though if you have access to a PC you are encouraged to complete the optional observation steps noted within.

---

## Part 1 — Boot Failure Scenario Analysis (40 points)

### Part 1 Directions

Read each scenario below. For each one, identify the boot stage where the failure occurred, explain the most likely root cause, and describe the correct first diagnostic step. Use the four-stage framework from the Reading Guide and lecture.

Boot stages to reference: Stage 1 (Power On), Stage 2 (POST), Stage 3 (Bootloader), Stage 4 (OS Load).

---

### Scenario 1 — The Office Desktop That Will Not Start (8 points)

A technician is called to an office where a desktop PC refuses to start. When the power button is pressed, the power LED lights up, the CPU fan spins, and the case fans spin — but the screen remains completely black and the system emits three long beeps approximately two seconds after power-on. The system then stops beeping and sits with fans running but no display.

**Question 1A:** At which boot stage did the failure occur? Explain your reasoning in 1-2 sentences.

Your answer: ___________________________________________

**Question 1B:** Based on the symptom (three long beeps, no display), what component is most likely failing? What type of BIOS is most consistent with this beep pattern?

Your answer: ___________________________________________

**Question 1C:** Describe the first two physical diagnostic steps the technician should take, in the order they should be performed.

Step 1: ___________________________________________

Step 2: ___________________________________________

---

### Scenario 2 — The "No Bootable Device" Message (8 points)

A small business owner asks a technician to upgrade a PC from a 512 GB SATA SSD to a 2 TB NVMe SSD. The technician clones the OS from the old SATA SSD to the new NVMe SSD using cloning software, confirms the clone completed successfully, then removes the old SATA drive and installs the NVMe SSD in the M.2 slot. On reboot, the screen displays "No bootable device found." The NVMe drive is visible in the BIOS storage device list.

**Question 2A:** At which boot stage did the failure occur? Explain your reasoning in 1-2 sentences.

Your answer: ___________________________________________

**Question 2B:** What is the most likely root cause? Why does the NVMe drive being visible in the BIOS storage list not resolve the error automatically?

Your answer: ___________________________________________

**Question 2C:** Describe the exact steps the technician should take to resolve this issue without reinstalling Windows.

Your answer: ___________________________________________

---

### Scenario 3 — The Windows Blue Screen Loop (8 points)

A user's Windows 11 laptop worked normally yesterday. Today, it powers on, shows the manufacturer's splash screen briefly, displays the Windows loading animation for approximately 10 seconds, then shows a blue screen with the stop code INACCESSIBLE_BOOT_DEVICE. The system automatically restarts and the cycle repeats. The user did not install any new software or hardware yesterday.

**Question 3A:** At which boot stage did the failure occur? Explain your reasoning in 1-2 sentences.

Your answer: ___________________________________________

**Question 3B:** What does the stop code INACCESSIBLE_BOOT_DEVICE specifically indicate about which component or system is failing?

Your answer: ___________________________________________

**Question 3C:** List three specific things a technician should check or test, in order of most-likely to least-likely cause, to diagnose this BSOD. For each item, explain in one sentence what you are checking and why.

Check 1: ___________________________________________

Check 2: ___________________________________________

Check 3: ___________________________________________

---

### Scenario 4 — The Silent System (8 points)

A technician builds a new PC from components. When the power button is pressed for the first time, absolutely nothing happens: no fans, no LEDs, no sounds, no display. The power cable is confirmed plugged into both the wall outlet and the PSU. The outlet is confirmed working by plugging in a phone charger.

**Question 4A:** At which boot stage did the failure occur? Explain your reasoning in 1-2 sentences.

Your answer: ___________________________________________

**Question 4B:** List three possible causes for a completely dead system at Stage 1 that a technician should check in a new build scenario.

Cause 1: ___________________________________________

Cause 2: ___________________________________________

Cause 3: ___________________________________________

**Question 4C:** A common new-build mistake is forgetting to connect the front panel power button header to the motherboard. If this is the cause, the system will not power on via the case button. Describe an alternative method a technician can use to test whether the motherboard itself powers on, without using the case power button.

Your answer: ___________________________________________

---

### Scenario 5 — The Driver-Caused BSOD (8 points)

A Windows 10 workstation was working correctly until the user updated their graphics card driver. Immediately after the driver update and reboot, the system shows a BSOD with the stop code IRQL_NOT_LESS_OR_EQUAL. The system restarts automatically and shows the BSOD again on every reboot attempt in normal Windows mode.

**Question 5A:** At which boot stage did the failure occur, and what does the stop code IRQL_NOT_LESS_OR_EQUAL indicate as the root cause category?

Your answer: ___________________________________________

**Question 5B:** The user cannot access Windows normally because the BSOD appears on every reboot. What Windows startup option should the technician use to access the system and address the driver, and how is it accessed when normal boot is failing?

Your answer: ___________________________________________

**Question 5C:** Once the technician has accessed the system using the method described in 5B, describe the specific steps to resolve the driver-caused BSOD.

Your answer: ___________________________________________

---

## Part 2 — UEFI Boot Order Navigation Exercise (30 points)

### Part 2 Overview

This part simulates UEFI boot order configuration tasks. Answer each question as if you are navigating a UEFI setup interface. Use the Reading Guide Section 5 for reference.

---

### Question 2-1 — Accessing UEFI Setup (5 points)

A technician needs to enter UEFI setup on a PC immediately after a RAM upgrade. The PC is from three different manufacturers in the table below. For each one, state the most common key used to enter UEFI setup and the most common key to access a one-time boot device menu (without permanently changing boot order).

| Manufacturer | UEFI Setup Key | One-Time Boot Menu Key |
|---|---|---|
| Dell desktop | | |
| HP laptop | | |
| ASUS motherboard (generic) | | |

---

### Question 2-2 — Reading a Boot Order List (5 points)

A UEFI boot order screen shows the following priority list:

1. USB Drive: SanDisk Ultra USB 3.0
2. Network: Intel(R) I219-V PXE
3. Windows Boot Manager (NVMe SSD: Samsung 980 Pro)
4. DVD Drive: ASUS DRW-24B3LT

The user turns on the PC and a bootable USB drive is not inserted. Describe exactly what the firmware will do, step by step, as it works through this list, and what the user will see on screen.

Your answer: ___________________________________________

---

### Question 2-3 — Fixing a Boot Order Problem (10 points)

Based on the boot order in Question 2-2, the user notices their PC always tries to boot from USB before the Windows SSD. This causes a 3-5 second delay on every startup while the firmware times out on the USB device. They want Windows to boot immediately without the delay.

**Part A:** Describe the change that should be made to the boot order and why it solves the delay.

Your answer: ___________________________________________

**Part B:** The user also asks: "Should I remove USB from the boot order entirely so it is never tried?" Write a 2-3 sentence response explaining the trade-off and what you recommend.

Your answer: ___________________________________________

---

### Question 2-4 — Secure Boot Scenario (10 points)

A technician creates a bootable USB recovery drive using a Linux-based recovery tool (GParted Live). The target PC is a modern laptop with UEFI and Secure Boot enabled. The USB drive is correctly listed in the UEFI boot order as the first device. When the technician reboots, the system briefly shows the UEFI splash screen and then immediately boots into Windows instead of the USB drive.

**Part A:** What is the most likely technical reason the USB drive is being skipped even though it is first in the boot order?

Your answer: ___________________________________________

**Part B:** Describe the exact steps to resolve this so the USB drive boots successfully. Include where in the UEFI interface the relevant setting is found and what change must be made.

Your answer: ___________________________________________

**Part C:** After completing the recovery task, what should the technician do before returning the laptop to the user?

Your answer: ___________________________________________

---

## Part 3 — POST Diagnostic and BSOD Stop Code Reference (30 points)

### Part 3A — Beep Code Interpretation Table (15 points)

Complete the table. For each beep code pattern and BIOS type, identify the component most likely failing and recommend the first physical diagnostic step.

| Beep Pattern | BIOS Type | Most Likely Failing Component | First Physical Diagnostic Step |
|---|---|---|---|
| Continuous short beeps | AMI | | |
| 1 long beep, 2 short beeps | AMI | | |
| 1 short beep, then system continues booting normally | Award/Phoenix | | |
| 1 long beep, 3 short beeps | Award/Phoenix | | |
| 5 short beeps | AMI | | |

### Part 3B — BSOD Stop Code Analysis (15 points)

For each BSOD stop code below, identify the root cause category, list one specific hardware or software component to check first, and describe how you would begin diagnosing it.

| Stop Code | Root Cause Category | First Component to Check | Initial Diagnostic Step |
|---|---|---|---|
| INACCESSIBLE_BOOT_DEVICE | | | |
| PAGE_FAULT_IN_NONPAGED_AREA | | | |
| IRQL_NOT_LESS_OR_EQUAL | | | |
| MEMORY_MANAGEMENT | | | |
| CRITICAL_PROCESS_DIED | | | |

---

## Optional Observation Exercises (Not Graded)

If you have access to a Windows PC, complete the following for your own learning:

**Observation 1:** Reboot your PC and attempt to enter UEFI setup by pressing the appropriate key at startup. Navigate to the boot order section and record the devices listed and their current priority order. Take a screenshot if possible. Do not make any changes.

**Observation 2:** In Windows, open Event Viewer (search "Event Viewer" in the Start menu). Navigate to Windows Logs > System. Filter for "Critical" events. If any recent critical events appear, note the event source and description. This is where Windows records significant hardware or driver errors short of a BSOD.

**Observation 3:** In Windows, search for "Windows Memory Diagnostic" and note where the tool is located. You do not need to run the scan — just locate it and note that it requires a reboot to execute.

---

## Deliverables and Submission

Submit one document containing all of the following:

1. Part 1 — All five scenario responses: stage identification, root cause, and diagnostic steps for each (Scenarios 1-5)
2. Part 2 — UEFI table (Question 2-1), boot order walkthrough (2-2), boot order fix and Secure Boot responses (2-3, 2-4)
3. Part 3 — Beep code table complete (3A, 5 rows) and BSOD stop code table complete (3B, 5 rows)

Accepted formats: PDF, DOCX, or Google Docs link with comment access enabled.

---

## Grading Rubric

| Section | Points Possible | Criteria |
|---|---|---|
| Part 1 — Scenario 1 (Desktop beep codes) | 8 | Correct stage ID (2 pts); correct component + BIOS type (3 pts); two valid ordered diagnostic steps (3 pts) |
| Part 1 — Scenario 2 (No bootable device) | 8 | Correct stage ID (2 pts); correct root cause with explanation of why BIOS detection alone is insufficient (3 pts); correct resolution steps without reinstall (3 pts) |
| Part 1 — Scenario 3 (BSOD loop) | 8 | Correct stage ID (2 pts); accurate stop code interpretation (3 pts); three valid ordered diagnostic checks with reasoning (3 pts) |
| Part 1 — Scenario 4 (Silent system) | 8 | Correct stage ID (2 pts); three valid Stage 1 causes (3 pts); correct jumper/shorting pin alternative power-on method (3 pts) |
| Part 1 — Scenario 5 (Driver BSOD) | 8 | Correct stage ID and stop code interpretation (3 pts); correct startup mode identified (2 pts); correct driver removal steps (3 pts) |
| Part 2 — UEFI Navigation (Questions 2-1 through 2-4) | 30 | Q2-1: 5 pts (correct keys per manufacturer); Q2-2: 5 pts (accurate step-by-step firmware behavior); Q2-3: 10 pts (correct fix + trade-off analysis); Q2-4: 10 pts (Secure Boot diagnosis + resolution + re-enable step) |
| Part 3A — Beep Code Table | 15 | 3 pts per row: correct component (1.5 pts) + correct first step (1.5 pts) |
| Part 3B — BSOD Stop Code Table | 15 | 3 pts per row: correct root cause category (1 pt) + correct component (1 pt) + valid diagnostic step (1 pt) |
| **Total** | **100** | |

---

## Reference Notes

All answers should be based on the Reading Guide, lecture notes, and module content. For beep code questions, the Reading Guide Section 3 tables are the authoritative reference for this course. For BSOD stop codes, the Reading Guide Section 4 table covers all required stop codes. Additional reference at professormesser.com (220-1101 Domain 5.3) and comptia.org.

---

## Part 9 — Challenge Exercise

These advanced steps are optional and are not included in the standard grading rubric.

### Challenge Step 1 — BSOD Minidump Analysis with BlueScreenView

Download the free portable utility BlueScreenView from NirSoft ([https://www.nirsoft.net/utils/blue_screen_view.html](https://www.nirsoft.net/utils/blue_screen_view.html)) and run it on any available Windows computer:

1. Launch BlueScreenView and examine any minidump files that exist from previous BSOD events (stored in `C:\Windows\Minidump\`). For each dump file found, record: the stop code name, the date and time of the crash, the faulting module name (driver or system file), and the memory address of the fault. If no dump files exist on your system (which means no recent BSODs have occurred), research and describe what information a minidump file contains and why it is more useful for diagnosis than reading only the on-screen stop code during the BSOD.
1. For each stop code you find (or for any three stop codes from the Reading Guide Section 4 table if no dumps are available), research the most common hardware and software causes and document your findings in a table with columns: Stop Code, Most Common Cause, Diagnostic Tool, Resolution.
1. Write 2–3 sentences explaining why Windows generates both a stop code visible on the BSOD screen and a minidump file written to disk, and describe a scenario where having the minidump file would provide information that the on-screen stop code alone cannot.

### Challenge Step 2 — UEFI Boot Configuration Lab

On any available Windows PC with UEFI firmware, access the UEFI setup utility and perform the following research tasks (read-only — do not change settings on a production machine):

1. Navigate to the boot configuration section and document: the current boot order (list all entries), whether Secure Boot is enabled or disabled, whether the firmware mode is set to UEFI or Legacy/CSM, and whether Fast Boot is enabled. Take a photograph or screenshot if permitted, or sketch the boot order screen layout in your lab document.
1. Locate the Secure Boot key management section (it may be under Security, Boot, or Advanced). Document what categories of keys are listed (PK, KEK, db, dbx) and describe in one sentence what each category controls. Research the difference between the "Restore Factory Keys" and "Clear All Secure Boot Keys" options and explain in 2–3 sentences when a technician would use each one.
1. Without making any changes, describe the exact steps required to temporarily disable Secure Boot to install an older Linux distribution that does not support Secure Boot, and the steps required to re-enable it safely afterward. Explain why re-enabling Secure Boot after OS installation is considered a security best practice.

### Challenge Step 3 — Boot Repair with Windows Recovery Environment

Using Windows installation media (a bootable USB drive created from a Windows 11 ISO) or the Windows Recovery Environment accessible from the boot menu, practice or research the following boot repair commands:

1. Document the complete command sequence a technician would run in the Windows Recovery Environment Command Prompt to repair a PC with a corrupt BCD store. Include the commands: `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /scanos`, and `bootrec /rebuildbcd` — explain what each command does and in what order they should be run, and why running them out of order can fail.
1. Research the `bcdedit` command and document: how to view the current BCD entries (`bcdedit /enum all`), how to add a Linux boot entry to the Windows Boot Manager, and what the `{bootmgr}`, `{current}`, and `{default}` identifiers represent. Explain in 2–3 sentences why `bcdedit` is more powerful than `bootrec` for advanced multi-boot configurations.
1. Write a step-by-step procedure a technician would follow to recover a PC displaying "INACCESSIBLE_BOOT_DEVICE" after a SATA controller mode was accidentally changed from AHCI to IDE in the BIOS. Include both the BIOS fix and the Windows Registry fix (loading the HKLM\SYSTEM hive offline and enabling the iaStorV and storahci services) that allows Windows to boot after the mode change.
