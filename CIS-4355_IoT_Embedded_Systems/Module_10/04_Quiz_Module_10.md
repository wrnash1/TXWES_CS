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

---

**Question 6**
Which hardware feature in modern microcontrollers permanently stores Secure Boot public keys in a way that cannot be modified after provisioning?

*   A) Flash memory — keys are written to the same flash partition as firmware for ease of update
*   B) OTP (One-Time Programmable) eFuse memory — fuses are physically blown and cannot be reversed
*   C) EEPROM — electrically erasable storage provides key update capability without device replacement
*   D) SRAM — volatile memory ensures keys are cleared on power loss for forward secrecy

*   **Correct Answer:** B) OTP (One-Time Programmable) eFuse memory — fuses are physically blown and cannot be reversed.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Keys stored in flash can be erased and rewritten; an attacker with physical access or a flash write vulnerability could replace the Secure Boot key, defeating the root of trust entirely.
    *   *Why B is correct:* eFuses are hardware bits that can be programmed (blown) exactly once. After provisioning, the Secure Boot public key stored in eFuses cannot be altered by software, firmware, or an attacker with a JTAG probe. This hardware immutability is what makes eFuse-based Secure Boot a genuine root of trust.
    *   *Why C is incorrect:* EEPROM is electrically erasable, meaning keys could be overwritten. It does not provide the immutability required for a hardware root of trust.
    *   *Why D is incorrect:* SRAM is volatile and loses its contents on power loss. Storing Secure Boot keys in SRAM would mean the device cannot verify firmware across power cycles.

---

**Question 7**
An IoT device uses ECDSA with a 256-bit key pair for firmware signing. The private key is stored on the build server. The build server is compromised and the private key is exfiltrated. Which response action is both necessary and most immediately effective?

*   A) Issue new firmware to all devices that patches the compromised server vulnerability
*   B) Revoke the compromised key by burning new eFuse bits with a replacement public key, and issue a signed update using a new key pair
*   C) Reset all device credentials and reissue X.509 certificates used for cloud connectivity
*   D) Disable firmware updates entirely until the build server is rebuilt to prevent further exploitation

*   **Correct Answer:** B) Revoke the compromised key by burning new eFuse bits with a replacement public key, and issue a signed update using a new key pair.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Patching the build server vulnerability is necessary for remediation but does not address the already-exfiltrated key. An attacker retaining the key can sign malicious firmware indefinitely.
    *   *Why B is correct:* Key compromise in a Secure Boot system requires key rotation. On devices that support multiple key slots in eFuse, a recovery path is to provision a new public key via a signed update (signed with the compromised key for the last time), then burn the new public key to eFuse and disable the old key. This terminates the attacker's signing capability.
    *   *Why C is incorrect:* Cloud connectivity certificates (X.509 client certs) are independent of firmware signing keys. Revoking MQTT certificates does not prevent malicious firmware from being flashed.
    *   *Why D is incorrect:* Disabling all firmware updates creates a denial of service and prevents security patches from reaching devices. It is not a sustainable response.

---

**Question 8**
What is the purpose of a "canary value" placed at the end of a stack frame by a compiler with stack protection enabled?

*   A) It records the function call timestamp for performance profiling
*   B) It is a known sentinel value checked upon function return; a modified canary indicates a stack buffer overflow has overwritten the return address
*   C) It stores the function's return address in a separate memory region, away from local variables
*   D) It encrypts local variables on the stack to prevent memory disclosure attacks

*   **Correct Answer:** B) It is a known sentinel value checked upon function return; a modified canary indicates a stack buffer overflow has overwritten the return address.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Canary values have no relationship to timestamps or performance profiling; they are purely a security mechanism.
    *   *Why B is correct:* Compiler stack protectors (GCC `-fstack-protector`) place a random canary word between local variables and the saved return address. Before returning, the function checks whether the canary equals its original value. If a buffer overflow has occurred and overwritten the return address, the canary is also overwritten, the check fails, and the program terminates with an error instead of executing attacker-controlled code.
    *   *Why C is incorrect:* That describes shadow stacks (e.g., Intel CET or ARM Pointer Authentication) — a different defense mechanism. Canaries remain in the same stack frame, adjacent to what they protect.
    *   *Why D is incorrect:* Canary values are not encrypted local variables; they are a single integrity check word. Encryption of local stack variables is not a standard compiler protection technique.

---

**Question 9**
An embedded device running a custom RTOS has no memory protection unit (MPU). What class of vulnerability is significantly easier to exploit in this environment compared to a system with MPU-enforced memory regions?

*   A) Integer overflow vulnerabilities, because the MPU prevents arithmetic wrap-around
*   B) Heap and stack buffer overflows that corrupt adjacent task stacks or overwrite function pointers, because the MPU cannot enforce boundaries between memory regions
*   C) Race conditions in multi-threaded code, because the MPU enforces mutex ownership
*   D) Cryptographic key extraction from AES hardware accelerator registers

*   **Correct Answer:** B) Heap and stack buffer overflows that corrupt adjacent task stacks or overwrite function pointers.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The MPU governs memory access permissions, not arithmetic operations. Integer overflow is a CPU arithmetic behavior that the MPU does not address.
    *   *Why B is correct:* Without an MPU, all tasks share a flat memory space. A buffer overflow in one task's stack can silently overwrite a neighboring task's stack, global variables, or function pointers — leading to arbitrary code execution. An MPU-equipped system can configure each task's stack as a separate protected region; writes outside the boundary generate a fault before corruption occurs.
    *   *Why C is incorrect:* The MPU enforces read/write/execute permissions on memory regions; it does not manage mutex ownership or thread scheduling. Race conditions are a concurrency issue handled by RTOS primitives.
    *   *Why D is incorrect:* AES hardware register access is governed by peripheral bus permissions, not the MPU's memory region configuration.

---

**Question 10**
A manufacturer ships IoT devices with the JTAG and UART debug interfaces active in production firmware. An adversary with physical access to the device uses the JTAG interface to dump the entire flash memory contents. Which OWASP IoT Top 10 category does this exemplify?

*   A) OWASP IoT #1 — Weak/Hardcoded Passwords
*   B) OWASP IoT #4 — Lack of Secure Update Mechanism
*   C) OWASP IoT #10 — Lack of Physical Hardening
*   D) OWASP IoT #7 — Insecure Data Transfer and Storage

*   **Correct Answer:** C) OWASP IoT #10 — Lack of Physical Hardening.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Hardcoded passwords (#1) involve credential storage issues. The attack here does not exploit a password; it exploits an exposed debug interface.
    *   *Why B is incorrect:* Secure update mechanism (#4) concerns firmware integrity and authentication during update delivery — not debug port exposure.
    *   *Why C is correct:* OWASP IoT #10 (Lack of Physical Hardening) specifically covers failure to disable debug interfaces (JTAG, UART, SWD), enable secure boot, or use tamper-evident enclosures. Leaving JTAG active in production directly enables the described flash dump attack.
    *   *Why D is incorrect:* Insecure data transfer (#7) addresses data in transit (unencrypted TLS) and data at rest encryption — not physical debug port exposure.

---

**Question 11**
During a firmware binary analysis with `binwalk`, a researcher finds an embedded Wi-Fi SSID and plaintext password string at offset 0x3F800 in the firmware image. Which secure firmware development practice would have prevented this finding?

*   A) Compiling the firmware with `-O2` optimization to remove unused strings from the binary
*   B) Storing credentials in a provisioned key store or encrypted NVS partition rather than hardcoding them in firmware source code
*   C) Using HTTPS for the OTA update channel so credentials are encrypted during firmware delivery
*   D) Signing the firmware with ECDSA so the binary cannot be read without the private key

*   **Correct Answer:** B) Storing credentials in a provisioned key store or encrypted NVS partition rather than hardcoding them in firmware source code.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Compiler optimization removes dead code but does not strip string constants that are referenced in the code. The SSID and password are referenced at runtime; they remain in the binary at all optimization levels.
    *   *Why B is correct:* Hardcoded credentials are the root cause. The correct practice is to provision secrets separately from firmware — for example, in ESP32 NVS with flash encryption enabled, or in a hardware secure element. A device-unique provisioning step at manufacturing injects credentials that never appear in the universal firmware binary.
    *   *Why C is incorrect:* HTTPS for OTA protects credentials during transit to the device, but the issue here is credentials permanently embedded in the firmware binary, which can be extracted regardless of how the firmware was delivered.
    *   *Why D is incorrect:* ECDSA firmware signatures provide integrity and authenticity verification, but they do not encrypt the binary contents. A signed firmware image can still be read and analyzed with `binwalk`.

---

**Question 12**
What is "defense in depth" in the context of IoT firmware security, and which combination of controls best exemplifies it?

*   A) Using the strongest available encryption algorithm (AES-256 instead of AES-128) for all data at rest and in transit
*   B) Layering multiple independent security controls — such as Secure Boot, encrypted flash, signed OTA, MPU-enforced memory regions, and network segmentation — so that no single control failure results in full system compromise
*   C) Ensuring the device has a physical tamper-detection circuit that erases keys when the enclosure is opened
*   D) Running all security-sensitive code in a hardware TEE (Trusted Execution Environment) so that the main application cannot access secrets

*   **Correct Answer:** B) Layering multiple independent security controls so that no single control failure results in full system compromise.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Upgrading one control to a stronger version of the same category (encryption strength) is depth of one layer, not defense in depth. If the one encryption layer is bypassed, there is no residual protection.
    *   *Why B is correct:* Defense in depth requires multiple independent layers at different attack surfaces. Secure Boot addresses boot-time tampering; flash encryption protects physical extraction; signed OTA prevents malicious update injection; MPU catches memory corruption; network segmentation limits blast radius. An attacker must defeat all layers independently.
    *   *Why C is incorrect:* Tamper detection is one useful physical hardening control, but a single control — however strong — is not defense in depth.
    *   *Why D is incorrect:* A TEE is a powerful single control for secrets isolation, but running all security-critical code in a TEE without additional controls (Secure Boot, network defense, etc.) still leaves multiple attack surfaces unaddressed.

---

**Question 13**
An ESP32 production device has flash encryption enabled. A researcher with physical access uses an external SPI flash reader to dump the raw flash contents. What does the researcher obtain?

*   A) All firmware code and plaintext NVS contents, because SPI flash readers bypass software-level encryption
*   B) AES-128-XTS encrypted ciphertext with no recoverable plaintext, because flash encryption uses a hardware key stored in eFuse that never leaves the ESP32
*   C) The firmware code in plaintext, but NVS (key-value store) contents are separately encrypted by the NVS library
*   D) A partial dump — the bootloader is always stored in plaintext for boot compatibility, but the application partitions are encrypted

*   **Correct Answer:** B) AES-128-XTS encrypted ciphertext with no recoverable plaintext.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ESP32 flash encryption is a hardware operation performed by the flash MMU transparent to software. The SPI bus carries only ciphertext; the hardware decryption key resides in eFuse and is never exposed on external pins.
    *   *Why B is correct:* When ESP32 flash encryption is enabled, the device generates a 256-bit AES key stored in eFuse, then encrypts all flash partitions (bootloader, partition table, application, NVS) using AES-XTS. An external SPI dump yields only ciphertext that cannot be decrypted without the eFuse key — which cannot be read externally once the read protection fuse is blown.
    *   *Why C is incorrect:* With hardware flash encryption, both firmware and NVS are encrypted at the flash level by the same hardware key. The NVS library's own encryption is an additional optional layer, not the primary protection.
    *   *Why D is incorrect:* When flash encryption is enabled on the ESP32, the bootloader partition is also encrypted. The ROM bootloader (in internal mask ROM) is never stored in external flash and does not need encryption.

---

**Question 14**
A secure OTA update system uses the following sequence: (1) device downloads firmware from CDN, (2) device verifies ECDSA-P256 signature using the manufacturer public key, (3) device writes firmware to inactive A/B partition, (4) bootloader verifies Secure Boot chain and commits new partition. At which step does the update become resilient to a CDN compromise delivering a modified binary?

*   A) Step 1 — TLS encryption of the CDN download prevents content substitution
*   B) Step 2 — signature verification using the embedded manufacturer public key will reject any binary not signed by the manufacturer's private key
*   C) Step 3 — the write to the inactive partition is atomic and cannot be partially corrupted
*   D) Step 4 — Secure Boot's hash chain catches any modification introduced after step 3

*   **Correct Answer:** B) Step 2 — signature verification rejects any binary not signed by the manufacturer's private key.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* TLS encrypts and authenticates the channel to the CDN, but if the CDN itself is compromised, the malicious binary is served over a valid TLS connection — TLS cannot detect server-side content substitution.
    *   *Why B is correct:* The ECDSA signature is computed over the firmware binary using the manufacturer's private key, which only the manufacturer holds. A CDN-substituted binary lacks a valid signature for that key. Step 2 detects the invalid signature and aborts the update before the compromised binary ever touches flash.
    *   *Why C is incorrect:* Atomicity of the flash write protects against power-loss corruption, not against writing a validly-delivered but malicious binary. The write would complete successfully for a CDN-supplied malicious image.
    *   *Why D is incorrect:* Secure Boot in step 4 would also catch a binary with an invalid signature, but the correct first line of defense is the application-level signature check in step 2, which rejects the binary before it is even written to flash — saving flash write cycles and aborting faster.

---

**Question 15**
Which of the following is a known security weakness of ABP (Activation By Personalization) in LoRaWAN that is directly addressed by OTAA?

*   A) ABP devices cannot use ADR (Adaptive Data Rate), reducing power efficiency
*   B) ABP hardcodes static NwkSKey and AppSKey into firmware; if a device is cloned or firmware is extracted, those session keys are permanently compromised with no rotation mechanism
*   C) ABP requires gateway-side TLS certificates, increasing infrastructure cost
*   D) ABP devices are limited to Class A operation and cannot receive Class B beacon-synchronized downlinks

*   **Correct Answer:** B) ABP hardcodes static session keys with no rotation mechanism.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ADR is a network-side feature independent of activation method. Both ABP and OTAA devices can participate in ADR.
    *   *Why B is correct:* ABP embeds NwkSKey, AppSKey, and DevAddr directly in firmware at manufacture time. These keys never change. If an attacker extracts the firmware (via JTAG, binwalk, or hardware cloning), they permanently possess the session keys. OTAA derives fresh session keys per join, so a compromised device can be remotely revoked by refusing its join request.
    *   *Why C is incorrect:* LoRaWAN gateway-to-network-server backhaul security is independent of device activation method. TLS on the backhaul applies regardless of whether devices use ABP or OTAA.
    *   *Why D is incorrect:* Device class (A, B, C) is independent of activation method. ABP devices can operate as Class B or C.

---

**Question 16**
An IoT gateway runs a custom Linux build. The `/etc/passwd` file contains an entry for user `admin` with password hash `$1$salt$hash`, where `$1$` indicates MD5 hashing. Why is this a critical security finding for a production IoT device?

*   A) MD5 hashes are stored in /etc/passwd rather than /etc/shadow, making them world-readable
*   B) MD5 is a cryptographically broken hash function with trivial rainbow table and GPU-accelerated brute-force attacks; an attacker who obtains the hash can crack the password in seconds to minutes
*   C) The `$1$` prefix indicates the password is stored in plaintext base64 encoding rather than a hash
*   D) MD5 password hashes prevent the use of PAM (Pluggable Authentication Modules) required for multi-factor authentication

*   **Correct Answer:** B) MD5 is cryptographically broken; the hash can be cracked in seconds to minutes.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Modern Linux systems store hashes in `/etc/shadow` (mode 640, not world-readable). The `/etc/passwd` entry for password hashing shows an 'x' when shadow is in use. However, even the shadow storage issue is secondary to the fundamental problem of MD5's weakness.
    *   *Why B is correct:* MD5 (crypt-MD5, `$1$`) is considered broken for password storage. Its speed (~500 million hashes/second on a GPU) makes brute-force trivial. Modern Linux uses bcrypt (`$2b$`), SHA-512 (`$6$`), or Argon2 — algorithms specifically designed to be slow and GPU-resistant. Using MD5 on a production device means any password hash that leaks is effectively plaintext.
    *   *Why C is incorrect:* `$1$` is the standard crypt(3) prefix for MD5-based hashing — it is not base64 plaintext. The value is a proper hash output, just computed with a weak algorithm.
    *   *Why D is incorrect:* PAM compatibility is not determined by hash algorithm. PAM works with MD5, SHA-512, and bcrypt equally.

---

**Question 17**
What is the minimum recommended RSA key length for new IoT device certificates as of current NIST guidance, and what is the primary driver for preferring ECDSA over RSA on constrained devices?

*   A) RSA-1024 minimum; ECDSA is preferred because it uses fewer bytes in the certificate Subject field
*   B) RSA-2048 minimum; ECDSA-P256 provides equivalent security to RSA-3072 with a 256-bit key, requiring significantly less CPU time and memory for key generation and signature operations on microcontrollers
*   C) RSA-4096 minimum; ECDSA is preferred because it is compatible with symmetric AES-256 encryption
*   D) RSA-2048 minimum; ECDSA is preferred because NIST prohibits RSA in IoT deployments after 2024

*   **Correct Answer:** B) RSA-2048 minimum; ECDSA-P256 equivalent to RSA-3072 with far lower compute cost.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* RSA-1024 was deprecated by NIST in 2010 and is considered broken. No current NIST guidance permits RSA-1024 for new deployments.
    *   *Why B is correct:* NIST SP 800-131A specifies RSA-2048 as the minimum through 2030. ECDSA-P256 provides security equivalent to RSA-3072 but with a 256-bit key. Key operations on ECDSA-P256 are 10–100x faster than RSA-2048 on typical microcontrollers, and certificates are significantly smaller — both critical advantages for constrained ESP32/Cortex-M class devices.
    *   *Why C is incorrect:* RSA-4096 exceeds current minimum requirements and is unnecessarily expensive for IoT devices. ECDSA's preference is not related to AES-256 compatibility.
    *   *Why D is incorrect:* NIST has not prohibited RSA in IoT. RSA-2048 remains approved through at least 2030. The preference for ECDSA is performance and key-size efficiency, not a regulatory ban.

---

**Question 18**
A firmware update is delivered with the following properties: it is downloaded over TLS, ECDSA-P256 signed, and protected by a monotonic version counter. A device receives a valid signed update with version number 3. The current minimum accepted version in eFuse is 2. What is the device's correct action after applying the update?

*   A) Accept the update, boot it, and leave the eFuse minimum version at 2 for rollback safety
*   B) Reject the update because version 3 is not equal to the minimum accepted version of 2
*   C) Accept the update, boot it, and increment the eFuse monotonic counter to 3, permanently preventing installation of versions 1 and 2
*   D) Accept the update and set the counter to 0 so future updates can use any version number

*   **Correct Answer:** C) Accept, boot, and increment the eFuse counter to 3.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Leaving the counter at 2 after applying version 3 defeats rollback prevention. An attacker with version 2 (which may contain known vulnerabilities) could still flash it because the counter allows versions ≥ 2.
    *   *Why B is incorrect:* The counter represents the minimum accepted version, not an exact match requirement. Version 3 ≥ 2, so it is accepted. Requiring exact match would prevent any updates at all once a version is established.
    *   *Why C is correct:* After successfully booting and validating version 3, the firmware or bootloader increments the eFuse counter to 3. Any subsequent attempt to install version 1 or 2 fails because they are below the new minimum. This is the rollback prevention guarantee.
    *   *Why D is incorrect:* Resetting the counter to 0 completely defeats rollback prevention and would be a firmware vulnerability if it could be triggered remotely.

---

**Question 19**
Which of the following embedded C patterns represents a time-of-check to time-of-use (TOCTOU) vulnerability in firmware?

*   A) `if (len > MAX) return ERROR; memcpy(dst, src, len);` — bounds check before copy
*   B) `if (signature_valid(buf)) { /* attacker changes buf in shared memory here */ process(buf); }` — check result used after a window where buf can be modified
*   C) `uint8_t x = 255; x++;` — integer overflow in a local variable
*   D) `strcpy(dst, src);` — no bounds check on destination

*   **Correct Answer:** B) signature_valid check followed by a window where buf can be modified before process().
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This is a correctly implemented bounds check with no window between check and use. There is no TOCTOU vulnerability here — the length is checked and immediately used.
    *   *Why B is correct:* TOCTOU occurs when the condition checked and the resource used are the same mutable object, and a modification can occur between check and use. If `buf` is in shared memory accessible to another thread or ISR, an attacker can modify its contents after `signature_valid()` returns true but before `process()` reads it — causing `process()` to operate on unsigned data that passed verification.
    *   *Why C is incorrect:* Integer overflow is a separate vulnerability class (undefined behavior in signed types, wrap-around in unsigned). It is not a TOCTOU issue.
    *   *Why D is incorrect:* `strcpy` without bounds check is a classic stack/heap buffer overflow vulnerability — a different vulnerability class from TOCTOU.

---

**Question 20**
An IoT product uses a third-party open-source MQTT library. The library version in the product is 2.1.0, released 3 years ago. A CVE is published for version 2.1.0 with CVSS score 9.8 (Critical) — a heap overflow in the packet parsing code. The vendor has not released a firmware update. What is the most appropriate immediate mitigation while waiting for the vendor patch?

*   A) Disable TLS on the MQTT connection to reduce packet parsing overhead that triggers the vulnerability
*   B) Implement network-layer filtering to restrict MQTT traffic to known, trusted broker IP addresses only, reducing the attack surface by limiting which sources can send malicious packets to the device
*   C) Downgrade the library to version 1.x, which predates the vulnerable code path
*   D) Increase the MQTT keepalive timer to reduce the frequency of packet parsing and limit exposure windows

*   **Correct Answer:** B) Network-layer filtering to restrict MQTT traffic to known broker IPs.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Disabling TLS makes the connection insecure and does not address the vulnerability. The heap overflow is in packet parsing — it can be triggered over plaintext or TLS equally. Disabling TLS makes the situation worse, not better.
    *   *Why B is correct:* Since the library cannot be patched immediately, the defense-in-depth response is to reduce the network attack surface. If MQTT connections are restricted to the known broker IP(s) via firewall rules, only a compromised broker can send the malicious packet — substantially raising the bar for exploitation while the vendor patch is awaited.
    *   *Why C is incorrect:* Downgrading to a known-vulnerable historical version is not an appropriate response without confirming version 1.x is not also affected. Downgrading can also introduce different vulnerabilities and is generally discouraged.
    *   *Why D is incorrect:* Increasing the keepalive timer changes the frequency of one type of MQTT packet (PINGREQ/PINGRESP) but does not reduce the volume of data messages that trigger the vulnerable parser. The vulnerability is not timing-dependent.
