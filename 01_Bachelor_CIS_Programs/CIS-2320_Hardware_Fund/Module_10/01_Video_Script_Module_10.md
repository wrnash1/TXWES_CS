# Video Script: Module 10 - Troubleshooting Boot Issues

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Estimated Duration:** 22-24 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 5.3 | CompTIA A+ Core 2 (220-1102) — Domain 3.1
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

**Slides needed:**

- Slide 1: Title card — "Module 10: Troubleshooting Boot Issues"
- Slide 2: The four boot stages diagram — Power On → POST → Bootloader → OS Load
- Slide 3: POST failure indicators — beep codes, on-screen codes, motherboard LED indicators
- Slide 4: AMI vs. Award/Phoenix beep code reference table (common patterns)
- Slide 5: BSOD anatomy — stop code, module name, memory address, QR code
- Slide 6: Common BSOD stop codes table with root cause
- Slide 7: UEFI boot order navigation screenshot (generic UEFI interface)
- Slide 8: Boot failure decision tree — which stage failed and what to check
- Slide 9: End card with study resources

**Components to show on camera (if available):**

- [SHOW COMPONENT] Motherboard with diagnostic LED array (Q-Code display or POST LEDs)
- [SHOW COMPONENT] PC with side panel off — pointing to RAM slots for reseating demo
- [SHOW COMPONENT] Bootable USB drive
- [SHOW COMPONENT] Screenshot of a BSOD on screen (printed or displayed)

**Key exam traps to address in the script:**

- "Operating System Not Found" after drive swap = boot order issue, not OS corruption
- Beep codes before video output means GPU has NOT been initialized — POST is still running
- BSOD means POST and bootloader completed — the OS loaded before the crash
- A blank screen with no beeps and no display can mean GPU failure OR power delivery issue — not just the same thing
- UEFI Secure Boot can prevent booting from unsigned USB drives — must be temporarily disabled for recovery media
- Continuous beeping patterns are almost always RAM — single isolated beeps have different meanings

---

## [00:00 - 02:30] Introduction and The Four Boot Stages

[SHOW SLIDE: Title card — "Module 10: Troubleshooting Boot Issues"]

Welcome back, class. I am Professor Nash, and this is Module 10: Troubleshooting Boot Issues.

This module covers what happens between the moment you press the power button and the moment you see your desktop. That sequence — power on, POST, bootloader, OS load — is where the vast majority of hardware-related failures manifest. When a technician walks up to a computer that will not start, their entire job in the first two minutes is to figure out which of those four stages failed. That answer determines everything else they do.

[SHOW SLIDE: The four boot stages diagram]

[PAUSE — 3 seconds]

Let me walk you through the four stages so we have a shared vocabulary for the rest of this module.

Stage 1 — Power On: The power supply delivers regulated DC voltage to the motherboard. The motherboard asserts the Power Good signal to the CPU. The CPU comes out of reset and begins executing the first instruction stored at the firmware reset vector — a fixed memory address that points to the BIOS or UEFI firmware chip.

Stage 2 — POST: Power-On Self-Test. This is firmware code executing on the CPU, testing the system's hardware before any operating system is involved. POST checks the CPU, RAM, storage controllers, video hardware, and other essential components in sequence. If a critical fault is found, POST halts and reports the error. POST completion is indicated by the single short beep you hear on most systems before the OS loads.

Stage 3 — Bootloader: POST hands control to the bootloader — a small program stored in the first sectors of the boot device. On UEFI systems, this is an EFI application in the EFI System Partition. On legacy BIOS systems, this is the Master Boot Record. The bootloader's job is to find the OS kernel and load it into memory.

Stage 4 — OS Load: The operating system kernel takes control from the bootloader. Device drivers are loaded, services start, and the login screen appears.

[PAUSE — 2 seconds]

Every boot failure fits into one of these four stages. A beep code with no display? Stage 2 — POST. "No bootable device found"? Stage 3 — Bootloader. Blue screen during startup? Stage 4 — OS Load. We are going to work through each failure type in detail.

---

## [02:30 - 08:30] Section 1 — POST Failures and Beep Codes

[SHOW SLIDE: POST failure indicators]

[SHOW COMPONENT: Motherboard with diagnostic LED array]

POST failures are the most challenging category because they happen before video output is available. If the GPU has not been initialized, the monitor shows nothing — and that blank screen is your first clue that the failure is at the POST stage.

When POST cannot display an error on screen, it communicates through three channels: beep codes, numeric POST codes on a display built into the motherboard, and LED indicators on the motherboard.

Let's talk about beep codes first. The onboard speaker — a small piezo buzzer on most motherboards — emits a pattern of short and long beeps corresponding to a specific fault. The key thing to understand is that beep codes are manufacturer-specific.

[SHOW SLIDE: AMI vs. Award/Phoenix beep code reference table]

[SHOW COMPONENT: Motherboard close-up on speaker header]

AMI BIOS (American Megatrends) uses one pattern. Award BIOS and Phoenix BIOS use different patterns. This is why the first thing you do when you hear a beep code is look up the motherboard's manual or the BIOS manufacturer's documentation — you cannot reliably interpret a beep pattern without knowing the BIOS maker.

That said, there are common patterns worth knowing for the A+ exam.

On most AMI BIOS systems: one long beep followed by two short beeps typically indicates a video card fault. Continuous short beeps or repeating short beeps typically indicate a RAM failure. One short beep at the end of POST — with no additional beeps — typically means POST completed successfully.

On most Award/Phoenix BIOS systems: one long and two short beeps indicates a video failure. Three long beeps indicates a RAM or keyboard controller issue. One short beep indicates success.

**A+ Exam Tip:** When the exam describes a blank screen with repeating beeps, the answer is almost always a RAM failure or unseated RAM. When it describes a blank screen with one long and two short beeps, the answer is a video card failure. Always look for the POST stage indicator before jumping to OS-level diagnoses.

[SHOW COMPONENT: PC with side panel off — pointing to RAM slots]

Practical POST diagnostics: If a system posts beep codes and produces no display, the standard diagnostic sequence is:

First, reseat the RAM. RAM that has worked loose is the most common cause of POST failure in desktop systems. Remove the modules completely, inspect the contacts, and reinsert firmly until both retention clips engage.

Second, if reseating RAM does not resolve the issue, remove all but one module and try each slot individually. This isolates a failed module or a failed slot.

Third, if RAM is confirmed good, check the GPU. Remove and reseat the discrete GPU in its PCIe slot. Check that any required PCIe power connectors are firmly attached.

Fourth, if neither RAM nor GPU is the issue, consult the motherboard's POST code display or LED indicators for a more precise diagnosis.

---

## [08:30 - 14:00] Section 2 — Blue Screen of Death and Kernel Panic

[SHOW SLIDE: BSOD anatomy]

[SHOW COMPONENT: Screenshot or printout of a BSOD]

The Blue Screen of Death — BSOD — is a Windows kernel-level fatal error. When Windows encounters an error it cannot recover from in kernel space, it stops all execution, writes a memory dump to disk, and displays the blue error screen. The technical term for this event is a bug check or STOP error.

Let's break down what is on a BSOD because the exam will ask about specific stop codes.

The most prominent element is the stop code — a text string in ALL CAPS describing the error category. Examples: IRQL_NOT_LESS_OR_EQUAL, PAGE_FAULT_IN_NONPAGED_AREA, INACCESSIBLE_BOOT_DEVICE, SYSTEM_SERVICE_EXCEPTION.

Below the stop code, Windows displays additional parameters — memory addresses, driver names, or hex error codes — that help engineers diagnose the specific fault. Modern Windows BSODs also include a QR code linking to Microsoft's support documentation for that specific stop code.

[SHOW SLIDE: Common BSOD stop codes table]

Let's go through the most A+ exam-relevant stop codes.

INACCESSIBLE_BOOT_DEVICE: Windows loaded the kernel but cannot access the boot partition. Most common causes: boot drive disconnected or failed, SATA mode changed in BIOS from AHCI to RAID or IDE after OS installation, or corrupted boot sector. First steps: check drive connection physically, check BIOS storage mode matches what was set during OS installation.

PAGE_FAULT_IN_NONPAGED_AREA: Windows attempted to access a memory page that does not exist or is not in a location the kernel expected. Most common causes: faulty RAM, corrupted drivers, or disk errors on a paging file drive. First step: run Windows Memory Diagnostic to test RAM.

IRQL_NOT_LESS_OR_EQUAL: A kernel process or driver attempted to access memory at an interrupt request level higher than permitted. Most common cause: a recently installed or corrupted driver. First step: boot to Safe Mode and uninstall recently added drivers.

SYSTEM_SERVICE_EXCEPTION: A system service caused an exception the kernel could not handle. Often driver-related. First step: identify the module name listed on the BSOD and target that driver for update or removal.

**A+ Exam Tip:** The BSOD stop code is a diagnostic tool, not just an error message. The exam will give you a stop code and ask what the root cause is. INACCESSIBLE_BOOT_DEVICE = storage or boot partition issue. PAGE_FAULT_IN_NONPAGED_AREA = RAM or paging file. IRQL_NOT_LESS_OR_EQUAL = driver issue.

The Linux and macOS equivalent of a BSOD is a Kernel Panic. Linux displays a black screen with kernel panic text showing the faulting instruction and call stack. macOS displays a gray screen with "Your computer restarted because of a problem." Both indicate a fatal kernel error requiring the same diagnostic approach — check RAM, storage, and recently installed kernel modules or drivers.

---

## [14:00 - 18:30] Section 3 — Boot Order and UEFI Configuration

[SHOW SLIDE: UEFI boot order navigation screenshot]

Boot order — also called boot priority — is a BIOS/UEFI configuration setting that defines the sequence of devices the firmware checks for a bootable partition. On every power-on, the firmware reads this list from top to bottom and attempts to boot from each device in sequence until it finds a valid bootloader or exhausts the list.

The default boot order after a fresh OS installation typically looks like this: NVMe/SATA SSD first, then HDD, then USB, then optical drive, then network (PXE boot).

Why does boot order matter for troubleshooting? Because the most common "no bootable device" symptom is not a failed drive — it is a boot order that no longer matches the physical drive configuration.

The most common scenario is a drive replacement. A technician removes an old SATA drive and installs a new NVMe SSD. The OS is installed on the NVMe drive. But the BIOS boot order still lists the old SATA drive as the first boot device. Since that drive is gone, the firmware finds nothing at the first position. If USB or optical is second, the system may attempt to boot from those. If nothing is found, the system displays "No bootable device found" or "Operating System Not Found."

[PAUSE — 2 seconds]

**A+ Exam Tip:** "Operating System Not Found" after a drive swap = boot order problem, not OS corruption. This is one of the most-tested boot scenarios on the exam. The drive is detected in BIOS, the OS was cloned or freshly installed, but boot order still points to the old device.

How to access UEFI setup: During POST, the firmware briefly displays a message — typically "Press DEL to enter setup" or "Press F2 for BIOS." The key varies by manufacturer: common keys are Delete, F2, F10, and Escape. If you miss the window, reboot and try again.

Navigating boot order in UEFI: Most UEFI firmware presents a graphical interface with mouse support. Navigate to the Boot tab or Boot Order section. The list of detected boot devices is shown in priority order. Use the arrow keys or drag-and-drop (in graphical UEFI) to move the desired device to the top. Save changes and exit — typically F10 or an on-screen Save & Exit button.

Temporary boot override: Most UEFI firmware supports a one-time boot override, accessed with a specific key during POST (commonly F11 or F12). This presents a boot device menu for a single boot without permanently changing the boot order — useful for booting from a recovery USB without reconfiguring the permanent boot sequence.

Secure Boot: UEFI Secure Boot is a feature that validates the digital signature of bootloader files before executing them. This prevents unsigned or malicious bootloaders from running. Legitimate Windows 11 and most modern Linux distributions have signed bootloaders. However, older Linux distributions and some recovery tools are not Secure Boot signed. If a bootable USB is not loading, check whether Secure Boot is blocking it and temporarily disable Secure Boot in UEFI settings to boot from the unsigned media.

---

## [18:30 - 21:00] Section 4 — Boot Failure Decision Tree and Diagnostic Strategy

[SHOW SLIDE: Boot failure decision tree]

Let's build a systematic diagnostic flow for any boot failure scenario. On the A+ exam, this decision tree is how you identify the correct answer quickly.

Step 1 — Does the system power on at all? Fans spin, LEDs light up, power supply delivers voltage? If no: PSU failure, power cable issue, or blown fuse. If yes: proceed.

Step 2 — Does POST run? Do you hear any beep codes? Does the screen show any output at all, even briefly? If POST is failing (beep codes, no display): diagnose RAM or GPU using the beep code lookup and reseating procedures from Section 1.

Step 3 — Does POST complete? One short success beep, and the screen briefly shows BIOS/UEFI splash or memory count? If POST completes but then you get "No bootable device," "Operating System Not Found," or "Boot device not found": the fault is in the bootloader stage. Check boot order first. Then verify drive is detected in BIOS. Then check bootloader integrity with recovery tools.

Step 4 — Does Windows start loading but then crash with a BSOD? POST completed, bootloader ran, Windows kernel began loading — then a blue screen appeared. This is an OS-stage failure. Identify the stop code, check RAM, check storage, check recent driver changes.

[PAUSE — 2 seconds]

**A+ Exam Tip:** Every boot failure scenario on the exam can be categorized using this four-stage decision tree. When you see a scenario question, your first question is: which stage did the failure occur in? The symptoms tell you. Beep codes = POST. "No bootable device" = bootloader/boot order. BSOD = OS load.

---

## [21:00 - 22:30] Closing and Lab Preview

[SHOW SLIDE: End card]

Let's recap Module 10. The four boot stages are Power On, POST, Bootloader, and OS Load. POST communicates failures via beep codes, on-screen codes, and LEDs. Beep codes are manufacturer-specific — always look up the pattern in the motherboard manual. BSOD stop codes identify the OS-stage failure type — INACCESSIBLE_BOOT_DEVICE, PAGE_FAULT_IN_NONPAGED_AREA, and IRQL_NOT_LESS_OR_EQUAL are the most A+ exam-relevant codes. Boot order in UEFI controls which device is tried first and is the first thing to check when a replaced drive is not booting.

Your lab for this module has three parts: a boot failure scenario analysis exercise using the four-stage decision tree, a BIOS/UEFI navigation exercise using a simulated interface, and a POST diagnostic step-by-step exercise. No physical hardware disassembly is required, but if you have access to a PC I strongly recommend pressing the BIOS key at startup and spending five minutes exploring your UEFI's boot order menu — nothing in this module makes more sense than seeing it live.

Check Canvas for all deadlines. For additional study, Professor Messer's free A+ Core 1 course at professormesser.com covers POST, beep codes, and UEFI boot configuration in detail. Review the troubleshooting section specifically.

See you in the discussion.

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 free course notes and video: professormesser.com (navigate to 220-1101, Domain 5.3 Troubleshooting)
- Professor Messer's CompTIA A+ Core 2 free course notes and video: professormesser.com (navigate to 220-1102, Domain 3.1 Troubleshooting)
- CompTIA A+ Exam Objectives (220-1101 and 220-1102): comptia.org (free download; review Domain 5.3 and 3.1 respectively)
