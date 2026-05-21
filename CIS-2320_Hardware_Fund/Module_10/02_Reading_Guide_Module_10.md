# Reading Guide: Module 10 - Troubleshooting Boot Issues
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 10 - Troubleshooting Boot Issues**! This module covers the diagnostic sequence a technician follows when a PC fails to start normally. You will learn what POST is and how it works, how to interpret beep codes, how to read and respond to Blue Screen of Death (BSOD) and Kernel Panic errors, and how to configure boot order in BIOS/UEFI to control which device the system attempts to boot from first. These topics are heavily tested on the **CompTIA A+ Core 1 (220-1101)** and **Core 2 (220-1102)** exams under hardware troubleshooting domains.

As a technician, you must be able to isolate the failure stage — hardware initialization, bootloader, or OS load — and select the correct diagnostic or remediation step. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **POST errors**: POST (Power-On Self-Test) is a hardware diagnostic routine executed by the BIOS/UEFI firmware immediately after the system receives power. It tests CPU, RAM, storage controllers, and video hardware in sequence. If POST detects a critical fault, it halts and reports the error via a numeric code on screen, a series of beep tones, or an LED indicator code on the motherboard. A system that halts at POST has a hardware fault that must be resolved before the OS can load. Common POST failures are caused by unseated RAM, missing or failed GPU, failed CPU, or no boot device.
*   **beep codes**: Beep codes are audio signals emitted by the motherboard's onboard speaker when POST detects a hardware error before video output is available. The number and pattern of beeps correspond to a specific fault; the meaning varies by BIOS manufacturer (AMI, Award/Phoenix). Common examples: one long + two short beeps typically indicates a video card failure (AMI BIOS); continuous short beeps indicate RAM failure. Beep codes are the primary diagnostic tool when the screen remains blank during POST because the GPU has not yet been initialized.
*   **BSOD and Kernel Panic**: A Blue Screen of Death (BSOD) in Windows is a full-screen blue error displayed when the Windows kernel encounters a fatal, unrecoverable error — commonly caused by driver corruption, faulty RAM, or storage failure. The screen displays a STOP error code (e.g., IRQL_NOT_LESS_OR_EQUAL, PAGE_FAULT_IN_NONPAGED_AREA) that identifies the root cause. The equivalent on Linux and macOS is a Kernel Panic, which displays a black or gray screen with a fatal error message. In both cases, the system cannot continue and writes a memory dump for post-mortem analysis.
*   **Boot order configuration in BIOS/UEFI**: Boot order (or boot priority) is a BIOS/UEFI setting that defines the sequence of devices the firmware attempts to find a bootable partition on — typically in order: internal NVMe/SSD, HDD, USB drive, optical drive, network (PXE). If the primary boot device is not detected or contains no bootloader, the system moves to the next device in the list. Technicians change boot order temporarily to boot from a USB recovery drive or installation media, and permanently to ensure the OS drive is always first for normal operation.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 5.3 and Core 2 — Domain 3.1):** The A+ exam presents boot failure scenarios and asks you to identify which stage failed. Know the four stages: power on → POST → bootloader → OS load. If the system powers on but produces beep codes and no display, the fault is at POST (hardware). If POST completes but the screen shows "No bootable device found," the fault is boot order or missing bootloader. If Windows starts loading but crashes, the fault is OS-level.
*   **Scenario Trap:** A common A+ scenario describes a PC that was working but now shows "Operating System Not Found" after a technician swapped a drive. The distractor answers involve RAM or GPU; the correct answer is that the boot order still points to the old drive, and the BIOS/UEFI boot priority needs to be updated to the new drive.
*   **Study Resource:** Professor Messer's free A+ course covers POST, beep codes, BSOD, and UEFI boot configuration with visual walkthroughs of real error messages and diagnostic procedures. Navigate to the troubleshooting section for boot issue scenarios: [Professor Messer's CompTIA A+ Core 1 Course — Troubleshooting](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Study the POST failure and BSOD stop code segments carefully.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the boot troubleshooting sections in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on POST, beep codes, BSOD stop codes, and UEFI boot order configuration.
*   **Required Video:** Watch the video lecture on troubleshooting boot issues from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on segments covering POST failure diagnosis, beep code interpretation, and boot order changes in UEFI.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Diagnose a boot failure caused by incorrect RAM seating**: Remove all RAM modules from a PC and power it on. Observe the beep code or LED indicator for a no-RAM POST failure. Reseat one RAM module in the correct slot (typically A1 or DIMM 1) and confirm POST completes successfully and the system proceeds to the bootloader.
*   **Identify the motherboard beep code for a missing video card**: Remove the discrete GPU from a system that requires it for video output. Power on and listen for the beep code pattern. Look up the code in the motherboard manual to confirm it corresponds to a video failure. Reinstall the GPU and verify POST succeeds.
*   **Modify boot sequence in UEFI settings to prioritize a USB drive**: Insert a bootable USB drive into the PC. Enter UEFI setup (typically Delete or F2 at POST). Navigate to the Boot Order or Boot Priority menu. Move the USB drive to the top of the boot sequence. Save and exit. Confirm the system boots from the USB drive on the next start.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the boot troubleshooting sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on troubleshooting boot issues in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the diagnostic steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
