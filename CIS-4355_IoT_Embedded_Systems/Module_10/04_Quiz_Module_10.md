# Quiz: Module 10 - Firmware Security and Secure Boot
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
How does Secure Boot protect an embedded IoT device against firmware tampering?
*   A) It encrypts all network traffic originating from the device after boot to prevent eavesdropping on telemetry.
*   B) It cryptographically verifies the digital signature of each boot stage against keys stored in the hardware root of trust before transferring execution, preventing unsigned or modified firmware from running.
*   C) It disables all USB and JTAG debug interfaces at runtime so that an attacker with physical access cannot dump memory.
*   D) It performs a real-time hash comparison of running firmware against a cloud-hosted golden image to detect in-memory tampering.
*   **Correct Answer:** B) It cryptographically verifies the digital signature of each boot stage against keys stored in the hardware root of trust before transferring execution, preventing unsigned or modified firmware from running.
*   **Distractor Analysis:**
    *   *Why correct:* Secure Boot establishes a chain of trust from the immutable ROM bootloader through each successive stage. Each stage verifies the next using the public key stored in eFuses or OTP memory. If any verification fails, the boot halts — malicious or modified firmware never executes.
    *   Network encryption, debug port disabling, and cloud hash comparison are all valid security controls, but none of them is the definition of Secure Boot. Secure Boot is specifically the signature-based pre-execution verification chain.

---

**Question 2**
Which of the following is the most accurate definition of **rollback prevention** in an IoT OTA update system?
*   A) A network control that blocks OTA update server connections from unauthorized source IP addresses, preventing rogue update servers from delivering firmware to devices.
*   B) A mechanism — typically a monotonic counter in OTP or eFuse memory — that prevents a device from booting or installing firmware with a version number lower than the committed minimum, blocking downgrade attacks to versions with known vulnerabilities.
*   C) An A/B partition scheme that stores two copies of the firmware and automatically switches to the backup partition if the primary partition becomes corrupted.
*   D) A firmware feature that backs up the current running firmware to cloud storage before applying an OTA update, enabling recovery if the update fails.
*   **Correct Answer:** B) A mechanism that uses a monotonic counter in OTP or eFuse memory to block firmware downgrades to versions with known vulnerabilities.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IP-based access control on the update server prevents unauthorized update delivery but does not prevent downgrading — an attacker with server access could still push an old signed image.
    *   *Why B is correct:* Rollback prevention specifically addresses downgrade attacks. A monotonic counter is hardware-enforced — once incremented, it cannot be decremented, so a legitimately signed v1.0 image is permanently rejected after v2.0 is committed, even if the attacker has the v1.0 signature.
    *   *Why C is incorrect:* This describes an A/B partition scheme, which provides atomic update safety and recovery from failed updates — a complementary mechanism to rollback prevention, but not the same thing.
    *   *Why D is incorrect:* Cloud backup of firmware before updates is a recovery mechanism, not a rollback prevention control.

---

**Question 3**
A security researcher downloads a firmware update package for a popular IP camera from the manufacturer's website. Using `binwalk`, the researcher extracts the filesystem, finds the root password hash in `/etc/shadow`, cracks it in 4 hours, and discovers it is the same password on every camera of that model. Which two security weaknesses does this reveal?
*   A) Lack of physical hardening (OWASP IoT #10) and insecure data transfer (OWASP IoT #7) — the firmware was downloaded over HTTP and the password hash was transmitted without TLS.
*   B) Weak/hardcoded passwords (OWASP IoT #1) and lack of secure update mechanism (OWASP IoT #4) — the identical per-model root password is a hardcoded credential, and downloadable firmware that is not encrypted exposes credentials to offline extraction.
*   C) Insecure network services (OWASP IoT #2) and insufficient privacy protection (OWASP IoT #6) — the SMTP service is open and the firmware stores user data without anonymization.
*   D) Insecure ecosystem interfaces (OWASP IoT #3) and lack of device management (OWASP IoT #8) — the manufacturer's website is the ecosystem interface and devices lack a management agent.
*   **Correct Answer:** B) Weak/hardcoded passwords (OWASP IoT #1) and lack of secure update mechanism (OWASP IoT #4).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Physical hardening (#10) concerns debug port exposure on the physical device; data transfer (#7) concerns runtime telemetry encryption. The finding here is about credential content and firmware extractability, not those categories.
    *   *Why B is correct:* Finding 1 — a shared root password identical across all devices of a model = OWASP IoT #1 (Weak/Hardcoded Passwords). Finding 2 — a publicly downloadable firmware image that contains extractable credentials without any protection = OWASP IoT #4 (Lack of Secure Update Mechanism, which includes firmware package security). The attacker used offline extraction, not network interception.
    *   *Why C is incorrect:* The findings do not involve SMTP services or privacy protection of user data — those categories do not map to the described attack.
    *   *Why D is incorrect:* Ecosystem interfaces (#3) covers web/mobile/cloud APIs; device management (#8) covers fleet patching — neither maps to the credential extraction or shared password findings.

---

**Question 4**
An IoT device ships with an A/B partition OTA update scheme. During a field update, power is lost to the device after the new firmware has been written to the inactive partition but before the bootloader has committed the new partition as active. What happens when power is restored?
*   A) The device is permanently bricked because the flash write was interrupted and neither partition contains valid firmware.
*   B) The device boots from the previously active partition (the old firmware), because the bootloader has not yet committed the new partition as active — the old partition is intact and the switch was never finalized.
*   C) The device attempts to boot from the new partition, detects the partial write via a corrupt signature, and erases both partitions as a security measure.
*   D) The device enters a recovery mode that contacts the OTA server to restart the failed update from the beginning before resuming normal operation.
*   **Correct Answer:** B) The device boots from the previously active partition (the old firmware), because the bootloader has not yet committed the new partition as active.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Bricking the device is precisely what the A/B scheme is designed to prevent. The old partition was never touched during the write to the inactive partition — it remains intact and bootable.
    *   *Why B is correct:* The A/B scheme's atomic safety guarantee is that the active partition pointer is only updated after the new firmware has been written, verified, and validated. A power loss before the commit leaves the active pointer unchanged — the device boots the old firmware safely.
    *   *Why C is incorrect:* Erasing both partitions as a security measure would brick the device; no standard A/B bootloader behaves this way. Signature verification failure causes a revert to the known-good active partition, not erasure.
    *   *Why D is incorrect:* While automatic OTA retry is a useful feature in some implementations, it is not the guaranteed behavior of the A/B partition scheme itself — the fundamental guarantee is safe fallback to the old partition.

---

**Question 5**
A product security team reviews their IoT device's OTA update implementation and finds: the update server presents a TLS certificate that the device validates; the firmware package is downloaded over the TLS channel; but no cryptographic signature on the firmware binary itself is verified before flashing. What attack does this missing control enable?
*   A) A replay attack where an attacker captures a legitimate update session and retransmits it months later to force re-installation of an older firmware version.
*   B) A man-in-the-middle attack against the TLS session: an attacker with a trusted CA-signed certificate for a different domain intercepts the TLS connection and substitutes a malicious firmware image that the device will flash without any binary-level verification.
*   C) A denial-of-service attack where the attacker sends an oversized firmware package that overflows the device's flash write buffer before TLS decryption completes.
*   D) A timing side-channel attack where the attacker measures TLS handshake latency to determine the firmware version running on the device before the update is applied.
*   **Correct Answer:** B) A man-in-the-middle attack substituting a malicious firmware binary that the device will flash without any binary-level verification.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A replay attack would require replaying a previous TLS session, which TLS prevents through session freshness mechanisms (nonces, session tickets). The missing control here is firmware signature verification, not session replay protection.
    *   *Why B is correct:* TLS only protects the transport channel — it authenticates the server and encrypts the connection. If the firmware binary itself carries no signature, any content received through a valid TLS connection will be flashed. An attacker who can substitute the firmware file on the update server (server compromise, CDN hijack, or a CA-mis-issued certificate enabling TLS interception) delivers a malicious binary that the device accepts unconditionally.
    *   *Why C is incorrect:* Buffer overflow from an oversized firmware is a separate implementation vulnerability in the flash write routine, not the consequence of missing firmware signature verification.
    *   *Why D is incorrect:* Timing side-channels are a cryptographic implementation concern unrelated to the firmware signing gap described.
