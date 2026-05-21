# Reading Guide: Module 10 - Firmware Security and Secure Boot
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 10 – Firmware Security and Secure Boot**! This module examines the techniques used to protect IoT firmware throughout its lifecycle — from the moment it is compiled and signed by the manufacturer, through the secure boot process that verifies it on every power-on, to the over-the-air update mechanism that delivers new versions to deployed devices. Firmware is the lowest-level software on an IoT device; a compromise at this layer gives an attacker persistent, privileged control that survives factory resets and may even survive firmware reflashing.

You will learn how a hardware root-of-trust (ROM bootloader, eFuses, TPM) anchors the chain of trust that secure boot depends on, how ECDSA signatures on firmware images prevent unauthorized code execution, how OTA update pipelines authenticate and validate firmware packages before applying them, and how rollback prevention ensures that an attacker cannot downgrade a device to a version with known vulnerabilities.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Secure Boot**: A hardware-enforced process in which each stage of the boot sequence cryptographically verifies the digital signature of the next stage before transferring execution to it. The chain begins with an immutable ROM bootloader (the hardware root-of-trust) that holds or verifies a public key baked into eFuses or OTP memory; if any stage's signature fails verification, the boot process halts, preventing tampered or malicious firmware from executing.
*   **Hardware Root of Trust**: The foundational hardware component whose integrity is assumed unconditionally because it is immutable — implemented as a ROM bootloader, burned eFuses, or a dedicated security element (TPM, ARM TrustZone secure enclave). All higher-level trust — bootloader, OS, application — is derived from this immutable anchor. Compromising the root of trust (e.g., by modifying eFuse key material) breaks the entire chain of trust.
*   **Firmware Signing**: The process of computing a cryptographic signature (typically ECDSA over SHA-256) over the firmware binary using the manufacturer's private key, and embedding the signature in the firmware package. The device verifies the signature using the corresponding public key stored in the root of trust before executing the firmware. This ensures only firmware authorized by the manufacturer can run on the device.
*   **Over-The-Air (OTA) Update**: A mechanism for delivering firmware updates to deployed IoT devices over their existing network connection without physical access. A secure OTA pipeline must: (1) authenticate the update server, (2) verify the firmware package signature before applying it, (3) use an atomic write sequence (A/B partition scheme) to prevent bricking if power is lost mid-update, and (4) implement rollback prevention to block downgrade attacks.
*   **Rollback Prevention**: A hardware or software mechanism that prevents an IoT device from booting or installing firmware with a version number lower than a committed minimum. Without rollback prevention, an attacker who obtains a signed image from an older firmware version with known vulnerabilities can reflash the device to that version and exploit the patched vulnerability. Implementation uses a monotonic counter in OTP memory or eFuses: each firmware release increments the counter, and the bootloader rejects images signed for a lower counter value.

---

### 2. Certification Exam Tips
*   **Chain of trust sequence:** Memorize: ROM bootloader (immutable) → verifies first-stage bootloader → verifies second-stage bootloader/RTOS → verifies application. Each link verifies the next using the public key from the previous. A break at any link halts the boot.
*   **ECDSA vs RSA for firmware signing:** ECDSA-256 produces smaller signatures (64 bytes vs 256+ bytes for RSA-2048) and verifies faster on constrained hardware, making it the preferred algorithm for IoT firmware signing. RSA is acceptable but resource-intensive.
*   **A/B partition OTA scheme:** In an A/B scheme, the device has two firmware partitions. New firmware is written to the inactive partition; after successful verification and validation, the device reboots into the new partition. If the new firmware fails post-boot health checks, the bootloader automatically reverts to the previous partition. This prevents a failed update from bricking the device.
*   **OTA security checklist:** A complete OTA implementation requires: TLS for update server transport, firmware signature verification before flash write, SHA-256 hash check after flash write, version monotonic counter check, and A/B atomic partition swap.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers the Lack of Secure Update Mechanism (OWASP IoT Top 10 category #4), which directly maps to insecure OTA pipelines lacking signature verification or rollback prevention.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on OWASP IoT Top 10 category #4 (Lack of Secure Update Mechanism) and the sections on firmware security, which cover the attack scenarios enabled by unsigned firmware updates and unprotected boot processes.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes coverage of secure boot architecture, firmware signing workflows, and OTA update pipeline design for embedded IoT devices.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Simulate firmware signature verification**: Using Python and the `cryptography` library, generate an ECDSA-P256 key pair, sign a sample firmware binary file, then write a verification script that accepts the firmware and signature file, verifies the signature against the public key, and exits with a non-zero code if verification fails.
*   **Test a rollback prevention check**: Embed a version number in a simulated firmware header and write a Python script that reads the current committed version from a "eFuse" file and rejects any firmware image whose version field is less than or equal to the committed value.
*   **Verify hash integrity after simulated flash write**: After writing firmware to a target location, compute SHA-256 of the source and destination files and compare them programmatically to confirm the write completed without corruption.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the chain of trust sequence.
- [ ] Read OWASP IoT Top 10 category #4 at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the firmware security sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Review the ECDSA signing and A/B partition concepts before the lab.
- [ ] Proceed to the weekly hands-on lab activity.
