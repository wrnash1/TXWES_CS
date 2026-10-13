# Reading Guide: Module 10 - Troubleshooting Boot Issues

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2320 &BULL; HARDWARE FUNDAMENTALS & PC ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 5.3 | CompTIA A+ Core 2 (220-1102) — Domain 3.1

---

## Introduction

Module 10 covers the diagnostic sequence a technician follows when a PC fails to start normally. Boot failures are among the most common issues technicians encounter in the field, and they are heavily tested on both CompTIA A+ Core 1 and Core 2 exams. The key to diagnosing boot failures quickly — both in the field and on the exam — is knowing which of the four boot stages produced the failure and what symptoms correspond to each stage.

This reading guide expands on the video lecture with detailed specification tables, stop code references, and UEFI navigation guidance. Read it completely before beginning the lab, paying particular attention to the four-stage decision framework in Section 1 and the BSOD stop code table in Section 4.

---

## Section 1 — The Four Boot Stages: A Diagnostic Framework

Every boot failure belongs to one of four stages. Identifying the stage is always the first diagnostic step.

| Stage | Name | What Happens | Failure Indicators |
|---|---|---|---|
| 1 | Power On | PSU delivers regulated voltage; motherboard asserts Power Good; CPU comes out of reset | No fans, no LEDs, no activity of any kind |
| 2 | POST | Firmware tests CPU, RAM, video, storage controllers | Beep codes, no display, POST code on diagnostic LED, system halts before showing BIOS splash |
| 3 | Bootloader | Firmware loads and executes the bootloader from the boot device | "No bootable device," "Operating System Not Found," "Boot device not found," "Missing operating system" |
| 4 | OS Load | OS kernel loads, drivers initialize, services start | BSOD (Windows) or Kernel Panic (Linux/macOS), Windows logo appears then crashes |

### How to Use the Framework

When a scenario describes a failing system, ask: what was the last thing that worked before the failure? If the screen never turned on and beeps were heard, the failure is at Stage 2. If POST completed and the splash screen appeared but Windows never loaded, the failure is at Stage 3 or 4. If Windows starts loading and then crashes, the failure is Stage 4.

---

## Section 2 — POST: Power-On Self-Test

### What POST Tests

POST is firmware code executed by the BIOS or UEFI before any OS involvement. It tests the following components in sequence:

1. CPU — basic instruction execution
2. BIOS/UEFI firmware chip — integrity check
3. RAM — memory test (abbreviated; full memory testing is done by dedicated tools)
4. Storage controllers — SATA, NVMe, M.2 controller initialization
5. Expansion cards — GPU, network cards, other PCIe devices
6. Boot device detection — which storage devices are present and bootable

If any critical component fails POST, the system halts at Stage 2 and reports the fault via beep codes, on-screen error text (if video was initialized), or diagnostic LEDs.

### POST Completion Signal

A single short beep on most systems indicates POST completed successfully and the bootloader is being invoked. Some modern UEFI systems are silent on successful POST — the absence of beep codes combined with a BIOS splash screen appearing indicates success.

---

## Section 3 — Beep Codes

Beep codes are audio signals produced by the motherboard's onboard piezo speaker when POST detects a critical hardware fault before video output is available. Because beep codes are the only output channel when the GPU has not been initialized, they are the primary diagnostic tool for Stage 2 failures that produce no display.

### Why Beep Codes Are Manufacturer-Specific

Beep code patterns are defined by the BIOS manufacturer, not the motherboard manufacturer. AMI (American Megatrends) BIOS, Award BIOS, and Phoenix BIOS each use different patterns for the same hardware failures. When diagnosing a beep code, identify the BIOS manufacturer from the motherboard manual or the brief text displayed during POST before the failure.

### Common AMI BIOS Beep Codes

| Pattern | Fault Indicated |
|---|---|
| 1 short beep | POST completed successfully |
| Continuous short beeps | RAM failure or unseated RAM |
| 1 long, 2 short beeps | Video card failure |
| 1 long, 3 short beeps | Video memory failure |
| 3 long beeps | Memory failure (some AMI versions) |
| 5 short beeps | CPU failure |

### Common Award/Phoenix BIOS Beep Codes

| Pattern | Fault Indicated |
|---|---|
| 1 short beep | POST completed successfully |
| 1 long, 2 short beeps | Video card failure |
| 1 long, 3 short beeps | Video card or monitor failure |
| 2 short beeps | POST error (non-fatal, check POST code) |
| Continuous beeping | RAM failure or power issue |

**Important:** These patterns are representative. Always confirm the specific pattern against the motherboard's manual or the BIOS manufacturer's documentation for a specific system. The A+ exam uses the most common patterns shown above.

### Motherboard Diagnostic LEDs and POST Code Displays

Many modern motherboards include additional POST diagnostic tools:

- POST code display: A two-character hexadecimal display on the motherboard that shows a numeric code corresponding to the current POST stage or fault. Each code maps to a specific initialization step or failure in the BIOS documentation.
- Debug LEDs: Four labeled LEDs (CPU, DRAM, VGA, BOOT) that light up in sequence during POST. If one remains lit when the system halts, it identifies the failing component. For example, if the DRAM LED stays lit and the system halts, RAM is the fault.

---

## Section 4 — Blue Screen of Death (BSOD) and Kernel Panic

### BSOD Overview

A BSOD (Blue Screen of Death) is a Windows kernel-level fatal error. When the Windows kernel encounters an unrecoverable error in kernel space — typically due to a driver, hardware fault, or corrupted system file — it performs a bug check: halts all execution, writes a memory dump to disk, and displays the blue error screen.

BSODs occur at Stage 4 (OS Load). Their presence confirms that POST completed and the bootloader ran successfully — the OS was loading when the error occurred.

### BSOD Components

| Element | Description |
|---|---|
| Stop code | Text string identifying the error category (e.g., INACCESSIBLE_BOOT_DEVICE) |
| Failing module | Driver or system file name associated with the fault (if identifiable) |
| Memory address | Hex address where the fault occurred |
| QR code | Links to Microsoft support documentation for the specific stop code |
| Memory dump path | Location where the crash dump file was written for post-mortem analysis |

### High-Yield BSOD Stop Codes for A+ Exam

| Stop Code | Root Cause | First Diagnostic Step |
|---|---|---|
| INACCESSIBLE_BOOT_DEVICE | Windows cannot access the boot partition — drive disconnected, failed, BIOS storage mode changed, or boot sector corrupted | Check physical drive connection; verify BIOS AHCI/RAID mode matches OS installation |
| PAGE_FAULT_IN_NONPAGED_AREA | Memory page access violation — faulty RAM, corrupted driver, or paging file error | Run Windows Memory Diagnostic; check for recently installed drivers |
| IRQL_NOT_LESS_OR_EQUAL | Kernel or driver accessed memory at a prohibited interrupt level — driver bug or corruption | Boot Safe Mode; uninstall recently added or updated drivers |
| SYSTEM_SERVICE_EXCEPTION | System service threw an unhandled exception — commonly a driver issue | Identify module name on BSOD; update or remove the implicated driver |
| MEMORY_MANAGEMENT | Windows memory manager encountered a fatal error — RAM failure or corruption | Run Windows Memory Diagnostic; test RAM modules individually |
| KERNEL_SECURITY_CHECK_FAILURE | A kernel data structure integrity check failed — corrupted driver or malware | Run SFC (System File Checker); check for driver corruption |
| CRITICAL_PROCESS_DIED | A critical Windows process terminated unexpectedly — system file corruption or failed storage | Run SFC /scannow; check drive health with SMART tools |

### Linux Kernel Panic

A Linux Kernel Panic is the equivalent of a Windows BSOD. The system displays a text dump on a black or dark screen showing:

- The kernel panic message
- The faulting function and call stack
- CPU register state at the time of the panic

Common causes include faulty RAM, a corrupted kernel module, a filesystem error on the root partition, or hardware incompatibility with a loaded driver.

### macOS Kernel Panic

macOS displays a gray screen with a spinning indicator followed by "Your computer restarted because of a problem." Panic log files are written to `/Library/Logs/DiagnosticReports/` and can be analyzed to identify the faulting kernel extension.

---

## Section 5 — Boot Order Configuration in BIOS/UEFI

### What Boot Order Controls

The BIOS/UEFI boot order (also called boot priority list) is an ordered list of devices the firmware attempts to boot from, checked from top to bottom on every startup. When the firmware finds a device with a valid bootloader, it executes it and hands off control. If no valid bootloader is found on any listed device, the firmware displays a boot failure message.

### Accessing UEFI Setup

| Manufacturer | Common UEFI Access Key |
|---|---|
| Most desktop motherboards | Delete or F2 |
| Dell | F2 (setup) or F12 (boot menu) |
| HP | F10 (setup) or F9 (boot menu) |
| Lenovo | F1 or F2 (setup) or F12 (boot menu) |
| ASUS | Delete or F2 |
| MSI | Delete |
| Gigabyte | Delete or F2 |

The access key must be pressed during the brief POST window before the OS begins loading. If the window is missed, reboot and try again.

### Navigating Boot Order in UEFI

1. Enter UEFI setup using the appropriate key at POST.
2. Navigate to the Boot tab, Boot Order, or Boot Priority section (naming varies by firmware).
3. The current boot device list is shown in priority order.
4. Use arrow keys and designated move keys (commonly F5/F6 or +/-) to reorder devices. Some graphical UEFI interfaces support drag-and-drop.
5. Press F10 (or the designated save key) to save and exit.

### Temporary Boot Override (One-Time Boot Menu)

Most UEFI firmware supports a boot override menu accessed with a separate key (commonly F11 or F12 at POST). This presents a list of currently detected bootable devices for a single boot without permanently altering the saved boot order. Use this when booting from a recovery USB without changing the permanent configuration.

### UEFI Secure Boot

Secure Boot is a UEFI feature that verifies the cryptographic signature of bootloader files before executing them. Signed bootloaders (Windows 11, most major Linux distributions) work with Secure Boot enabled. Unsigned bootloaders (older Linux versions, some recovery tools) are blocked by Secure Boot.

To boot from unsigned recovery media: Enter UEFI setup → Security tab → Secure Boot → Disable → Save → Boot from USB. Re-enable Secure Boot after recovery is complete.

### Common Boot Order Scenarios

| Symptom | Most Likely Cause | Resolution |
|---|---|---|
| "No bootable device found" after drive replacement | Boot order still lists the old (now absent) drive as first boot device | Enter UEFI boot order and set new drive as first boot device |
| System boots to USB drive every startup | USB drive is above internal SSD in boot order | Move internal SSD to top of boot order; remove USB from list |
| "Operating System Not Found" after cloning OS to new drive | Boot order points to old source drive; new drive not in list | Add new drive to boot order as first device |
| System skips internal drive and goes to network PXE boot | Internal drive not detected or listed below PXE in boot order | Check drive seating and SATA/NVMe connection; move internal drive above PXE in boot order |
| Bootable USB not recognized | Secure Boot blocking unsigned bootloader | Disable Secure Boot temporarily in UEFI settings |

---

## Section 6 — High-Yield Glossary

**POST (Power-On Self-Test):** A hardware diagnostic routine executed by BIOS/UEFI firmware immediately after power-on. Tests CPU, RAM, GPU, and storage controllers before any OS is involved. Failure halts the system at Stage 2 and is reported via beep codes, POST codes, or diagnostic LEDs.

**Beep Codes:** Audio signals from the motherboard's onboard speaker indicating POST failures. Patterns are specific to the BIOS manufacturer (AMI, Award, Phoenix). Must be interpreted with the motherboard manual or BIOS documentation.

**BIOS (Basic Input/Output System):** Legacy firmware standard stored on a chip on the motherboard. Initializes hardware and provides the POST routine. Being replaced by UEFI on modern systems.

**UEFI (Unified Extensible Firmware Interface):** The modern replacement for legacy BIOS. Supports larger drives (GPT), Secure Boot, a graphical interface, faster boot times, and network-capable firmware applications.

**BSOD (Blue Screen of Death):** A Windows kernel-level fatal error screen displayed when an unrecoverable kernel error occurs. Contains a stop code identifying the fault category. Occurs at Stage 4 (OS Load).

**Stop Code:** The text string on a BSOD identifying the error type. Examples: INACCESSIBLE_BOOT_DEVICE, PAGE_FAULT_IN_NONPAGED_AREA, IRQL_NOT_LESS_OR_EQUAL.

**Kernel Panic:** The Linux and macOS equivalent of a Windows BSOD — a fatal kernel error that halts the system. Displays a text dump (Linux) or a "Your computer restarted because of a problem" screen (macOS).

**Boot Order (Boot Priority):** A BIOS/UEFI setting defining the sequence of devices checked for a valid bootloader. Controls which device the system boots from on every startup.

**EFI System Partition (ESP):** A FAT32 partition on UEFI-booting drives that stores EFI bootloader files. Required for UEFI boot; absent on legacy MBR drives.

**MBR (Master Boot Record):** The first sector of a legacy BIOS-bootable drive, containing the bootloader code and partition table. Replaced by GPT on UEFI systems.

**GPT (GUID Partition Table):** The modern partition table format used with UEFI. Supports drives larger than 2 TB and more than four primary partitions. Replaces MBR.

**Secure Boot:** A UEFI feature that validates the cryptographic signature of bootloaders before executing them. Prevents unsigned or malicious bootloaders from running. Can be disabled in UEFI settings when booting from unsigned recovery media.

**Memory Dump:** A file written to disk when Windows encounters a BSOD, containing the contents of RAM at the time of the crash. Used by engineers to analyze the root cause. Stored by default at `C:\Windows\MEMORY.DMP`.

**Safe Mode:** A Windows startup mode that loads only essential drivers and services, bypassing third-party drivers. Used to diagnose and remove drivers or software causing BSOD crashes.

**POST Code Display:** A two-character hexadecimal display built into some motherboards that shows the current POST stage code, allowing technicians to identify precisely where POST halted when other indicators are absent.

**Debug LEDs:** A row of four LEDs on some motherboards labeled CPU, DRAM, VGA, BOOT. Each illuminates during its corresponding POST phase. A LED that remains lit when the system halts identifies the failing component.

---

## Section 7 — Certification Exam Tips

**Trap 1 — "Operating System Not Found" after drive swap means boot order, not OS corruption.** This is the single most-tested boot scenario. The new drive is detected, the OS is installed, but boot order still references the old device. The fix is updating boot priority in UEFI — not reinstalling Windows.

**Trap 2 — BSOD means POST and bootloader succeeded.** If Windows shows a blue screen, Stages 2 and 3 completed successfully. The failure is in Stage 4. Do not recommend replacing hardware based solely on a BSOD without identifying the stop code and root cause.

**Trap 3 — Blank screen plus beep codes means GPU not yet initialized.** POST runs before the GPU is initialized. Beep codes on a blank screen do not mean the monitor is broken — they mean POST detected a hardware fault and is reporting it before video hardware is available.

**Trap 4 — Beep code interpretation requires knowing the BIOS manufacturer.** The same beep pattern means different things on AMI vs. Award BIOS. The exam may describe a beep pattern and ask which component is failing — the correct answer depends on the BIOS make stated in the scenario.

**Trap 5 — Continuous short beeps almost always mean RAM.** Across most BIOS manufacturers, a continuous repeating short beep pattern during POST indicates RAM failure or unseated RAM. This is the most common POST failure in real-world practice and the most common answer for beep code questions on the A+ exam.

**Trap 6 — Secure Boot blocks unsigned bootable USB drives.** If a technician creates a bootable USB recovery drive and the system will not boot from it despite correct boot order configuration, Secure Boot is a primary suspect. The USB's bootloader may not be signed.

**Trap 7 — INACCESSIBLE_BOOT_DEVICE is storage, not RAM.** Students sometimes confuse this stop code with RAM failures. INACCESSIBLE_BOOT_DEVICE means Windows cannot access its boot partition — check the physical drive connection, BIOS AHCI/RAID mode, and boot sector integrity first.

**Trap 8 — One short beep is a success indicator, not a fault.** A single short beep on most BIOS systems indicates POST completed successfully. The fault indicators are multiple beeps, long-short patterns, or continuous beeping.

---

## Section 8 — Study Checklist

- [ ] Memorize the four boot stages and the failure symptom that corresponds to each one.
- [ ] Be able to state what beep code patterns indicate RAM failure and video failure on both AMI and Award BIOS systems.
- [ ] Know the five most important BSOD stop codes (INACCESSIBLE_BOOT_DEVICE, PAGE_FAULT_IN_NONPAGED_AREA, IRQL_NOT_LESS_OR_EQUAL, SYSTEM_SERVICE_EXCEPTION, MEMORY_MANAGEMENT) and their root causes.
- [ ] Practice the boot order change procedure: know how to access UEFI setup, navigate to boot order, and move a device to the top.
- [ ] Understand when Secure Boot must be disabled and what symptom it produces.
- [ ] Review the eight exam traps in Section 7.
- [ ] Read the boot troubleshooting sections in Professor Messer's CompTIA A+ study notes at professormesser.com (220-1101 Domain 5.3).
- [ ] Watch Professor Messer's video on POST, beep codes, BSOD, and UEFI boot configuration at professormesser.com.
- [ ] Complete the Module 10 Lab before attempting the quiz.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 free study notes and video course: professormesser.com (220-1101 section, Domain 5.3)
- Professor Messer's CompTIA A+ Core 2 free study notes and video course: professormesser.com (220-1102 section, Domain 3.1)
- CompTIA A+ Exam Objectives (220-1101 and 220-1102): comptia.org (free download; review both troubleshooting domains)

---

## 9. Supplemental Resources

The following free resources supplement Module 10 content on boot troubleshooting, POST diagnostics, BSOD analysis, and UEFI configuration.

1. **Professor Messer — CompTIA A+ Core 1 (220-1101) Boot Process and Troubleshooting**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Free video lectures covering POST failures, beep codes, UEFI boot configuration, Secure Boot, and boot order — the primary exam objectives for Domain 5.3. The videos align directly with the scenario-based questions on the A+ exam.

1. **Microsoft Learn — Troubleshoot Windows Startup (Official Documentation)**
   URL: [https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/windows-boot-issues-troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/windows-boot-issues-troubleshooting)
   Relevance: Free official Microsoft documentation covering BSOD stop codes, BCD repair with bootrec commands, Startup Repair, and Windows Recovery Environment tools. Authoritative reference for A+ exam questions about Windows boot failure resolution steps.

1. **NirSoft BlueScreenView — BSOD Dump File Analyzer**
   URL: [https://www.nirsoft.net/utils/blue_screen_view.html](https://www.nirsoft.net/utils/blue_screen_view.html)
   Relevance: Free portable tool that reads Windows minidump files created by BSOD events and displays the stop code, faulting driver, and memory address. Useful for hands-on practice identifying stop codes and understanding what component each code points to — directly supporting the BSOD troubleshooting skills tested on the A+ exam.

1. **UEFI Forum — UEFI Specifications and Overview**
   URL: [https://uefi.org/specifications](https://uefi.org/specifications)
   Relevance: The official UEFI industry organization publishes free overview documents explaining the UEFI boot process, Secure Boot architecture, and GPT/MBR differences. Understanding UEFI at a conceptual level is required for boot order configuration and Secure Boot troubleshooting questions on the A+ exam.

1. **MemTest86 — Free Bootable RAM Diagnostic Tool**
   URL: [https://www.memtest86.com/](https://www.memtest86.com/)
   Relevance: Free industry-standard bootable memory testing tool used to diagnose RAM hardware faults that cause MEMORY_MANAGEMENT and PAGE_FAULT_IN_NONPAGED_AREA BSODs. Running MemTest86 is the standard first step when the A+ exam presents a scenario with random system crashes or memory-related stop codes.
