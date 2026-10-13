# Video Script: Module 08 — Endpoint Security (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CompTIA Security+ (SY0-701) Complete Training Course &bull; Module 08</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy" title="Professor Messer &bull; CompTIA Security+ (SY0-701) Complete Training Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Professor Messer &bull; CompTIA Security+ (SY0-701) Complete Training Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

---

### [INTRO — 0:00]

Welcome to Part 2 of Module 08. In Part 1 we covered the EDR evolution, CIS hardening benchmarks, patch management, and host-based firewalls. Now we cover full disk encryption, application allowlisting, mobile device management, and the Security+ exam traps for this domain.

---

### [SECTION 1 — Full Disk Encryption — 0:30]

**Full Disk Encryption (FDE)** encrypts all data on a storage device, including the operating system, applications, and user data. Without the correct decryption key or credential, the data is unreadable — even if the drive is physically removed from the system.

#### Why FDE Matters

The primary threat FDE addresses: **physical theft or loss**. If a laptop is stolen and the drive is unencrypted, the attacker removes the drive, connects it to another system, and reads all data without needing the user's password. With FDE, the data on the removed drive is ciphertext.

#### Windows BitLocker

BitLocker is Microsoft's built-in FDE solution. Key features for the exam:

- Encrypts entire volumes using AES (128 or 256-bit).

- **TPM (Trusted Platform Module)** integration: the TPM stores the encryption key and verifies the boot chain integrity before releasing it. If the drive is moved to a different system, the TPM on the new system will not have the key.

- **Recovery key**: a 48-digit numeric key stored in Active Directory or on paper for situations where the TPM check fails (hardware change, BIOS update).

- **Pre-boot authentication**: BitLocker can require a PIN or USB key in addition to the TPM, providing MFA for disk access.

**Exam point**: BitLocker + TPM provides automatic decryption on the original hardware. BitLocker + TPM + PIN requires user input at boot — stronger protection but requires user action each restart.

#### macOS FileVault

Apple's FDE solution for macOS. Uses XTS-AES-128 encryption. Recovery key is stored with Apple or in the user's iCloud account (enterprise configurations use an institutional recovery key in MDM).

#### Self-Encrypting Drives (SEDs)

Some drives have encryption hardware built in. The drive encrypts data automatically using an encryption key stored in the drive firmware. When a user authenticates, the drive unlocks.

**Exam trap**: SEDs encrypt by default but the key management matters. If the default factory key is used without a user-defined credential, the encryption provides no real protection — anyone who powers on the drive gets access. The exam may test whether SED encryption is effective without proper key management.

#### File-Level vs. Full Disk Encryption

FDE encrypts everything on the disk, including temp files, page files, and deleted file residue — data that file-level encryption would miss. FDE is the recommended standard for endpoint protection against physical loss.

---

### [SECTION 2 — Application Allowlisting — 4:00]

**Application allowlisting** (also called whitelisting) is a security control that permits only explicitly approved applications to execute on a system. Any application not on the allowlist is blocked by default.

This is the opposite of the traditional blacklisting approach (block known bad, allow everything else). Allowlisting operates on the principle: block everything unknown, allow only approved.

#### Why Allowlisting Is Powerful

Allowlisting would stop most malware — including zero-days — because any malware executable that is not on the approved list will be blocked, regardless of whether it has a known signature.

Consider the attack chain from Module 04's lab: an attacker delivers malware via phishing → the malware downloads `svchost32.exe` to the temp directory → `svchost32.exe` executes. With allowlisting, that execution is blocked because `svchost32.exe` in a temp directory is not on the approved list.

#### Windows Tools

**AppLocker** — built into Windows Enterprise/Education; allows policies based on publisher, file path, or hash. Policies can be set per user group.

**Windows Defender Application Control (WDAC)** — more modern and robust than AppLocker; operates at the kernel level; harder to bypass; supported by TPM attestation.

#### Operational Challenges

Allowlisting is the most operationally demanding endpoint control to maintain:

- Initial inventory of all approved applications must be comprehensive — missing a legitimate application causes user disruption.

- Every software update potentially requires hash updates to the allowlist.

- Ad-hoc software installations require a change management process.

This is why allowlisting is most commonly deployed in controlled environments: industrial control systems, ATM networks, kiosk systems, and regulated industries — anywhere application diversity is low and the cost of disruption is high.

**Exam point**: Application allowlisting is the strongest endpoint control against malware execution, but the most operationally challenging to maintain.

---

### [SECTION 3 — Mobile Device Management — 7:30]

**Mobile Device Management (MDM)** is a platform for managing, securing, and enforcing policies on mobile devices — smartphones, tablets, and increasingly laptops.

#### MDM Core Capabilities

- **Policy enforcement**: require screen lock with PIN, require device encryption, enforce minimum OS version.

- **Application management**: install, update, and remove applications remotely.

- **Remote wipe**: erase all data on a lost or stolen device.

- **Inventory**: track all managed devices, their OS versions, installed applications, and compliance status.

- **Certificate deployment**: push certificates for VPN, Wi-Fi, or email encryption.

- **Geolocation**: track or geo-fence device locations.

#### MDM vs. MAM

**MDM** manages the entire device. The organization has visibility and control over everything on the device.

**MAM (Mobile Application Management)** manages only specific applications and their data — a containerized approach. Often used for BYOD (Bring Your Own Device) scenarios where the organization wants to protect corporate data without controlling the employee's personal apps and data.

**Exam distinction**: MDM = full device control. MAM = application and data control only. BYOD scenarios typically lead to MAM as the answer.

#### BYOD Security Considerations

When employees use personal devices for work (BYOD), the organization faces a tension between security control and employee privacy.

Key BYOD controls:

- MAM to containerize corporate applications and data.

- Certificate-based VPN for corporate access.

- Conditional access: device must meet minimum security requirements before accessing corporate resources.

- Acceptable Use Policy (AUP): document what is permitted and what monitoring occurs.

**Exam point**: A BYOD policy question asking "how can the organization protect corporate email and documents on personal devices without managing the entire device?" points to MAM.

#### MDM Enrollment Methods

- **BYOD enrollment**: user-initiated; user accepts terms.

- **Corporate-owned personally enabled (COPE)**: corporate device, employee can use personally within policy.

- **Corporate-owned business only (COBO)**: strictly business use; maximum control.

---

### [SECTION 4 — Additional Hardening Controls — 11:00]

#### Disable Unnecessary Services and Ports

A hardened system runs only the services required for its function. Every running service is an attack surface. Key services commonly disabled during hardening:

- Telnet (unencrypted remote access — replaced by SSH).

- FTP (unencrypted file transfer — replaced by SFTP/FTPS).

- LLMNR and NetBIOS (exploitable for credential capture in Windows environments).

- Remote Registry service (unless explicitly needed).

#### Secure Boot

**Secure Boot** is a UEFI firmware feature that verifies the cryptographic signature of bootloader code before execution. This prevents bootkits and rootkits that attempt to execute before the OS loads.

Secure Boot requires that the bootloader is signed by a key in the UEFI firmware's trust store. Combined with BitLocker TPM attestation, Secure Boot provides a hardware-anchored boot chain of trust.

#### USB and Removable Media Controls

USB drives are a significant endpoint threat vector — both for malware delivery (baiting) and data exfiltration. Controls include:

- Group Policy settings blocking USB mass storage device classes.

- DLP software monitoring file copies to removable media.

- Endpoint agent enforcement of removable media policies.

---

### [SECTION 5 — EXAM TRAPS AND QUESTION ANALYSIS — 12:30]

#### Trap 1: AV vs. EDR Purpose

"An organization experienced a breach. They need a tool that can show them a complete timeline of what happened on the endpoint — every file accessed, every process spawned, every network connection made."

Wrong answer: antivirus, SIEM (for this specific endpoint detail).

Correct answer: **EDR**. EDR provides continuous telemetry recording with forensic timeline capability.

#### Trap 2: FDE and Physical Theft

"A laptop with full disk encryption is reported stolen. The encryption key is managed by the TPM on the laptop. Is the data at risk?"

Correct answer: No — the data is protected. The TPM on the stolen laptop will not release the key without the correct boot chain and PIN (if configured). If the attacker removes the drive and inserts it in another system, the TPM is absent and the drive remains encrypted.

"A laptop is stolen. It uses a self-encrypting drive with factory default key configuration. Is the data at risk?"

Correct answer: Yes — without a user-defined key or credential, the SED offers no real protection.

#### Trap 3: Allowlisting vs. Blacklisting

"An organization in an ICS environment wants to ensure that no unauthorized software can execute, including zero-day malware."

Correct answer: **application allowlisting**. Blacklisting cannot block unknown malware. Allowlisting blocks anything not approved — including zero-days.

#### Trap 4: MDM vs. MAM for BYOD

"Employees want to use personal smartphones to access corporate email. The organization wants to protect corporate data but cannot mandate full control over personal devices."

Correct answer: **MAM** (Mobile Application Management). MDM manages the full device; MAM manages only the corporate application container — appropriate for personal device scenarios.

#### Trap 5: Patch Priority

"A new vulnerability is published with a CVSS score of 6.5 (Medium). The same day, an older vulnerability with a CVSS of 5.2 (Medium) is added to the CISA KEV catalog. Which should be patched first?"

Correct answer: **the KEV catalog vulnerability** — because active exploitation in the wild is a higher practical risk indicator than CVSS score alone. CVSS measures severity in theory; the KEV catalog means attackers are exploiting it now.

#### Trap 6: Host Firewall vs. Network Firewall

"An employee connects their laptop to a hotel Wi-Fi network and needs to be protected from other devices on the same network."

Correct answer: **host-based firewall**. The corporate network firewall provides no protection when the device is on an external network. The host-based firewall travels with the device.

---

### [OUTRO — 15:00]

Module 08 completes your core endpoint security toolkit.

Key exam review:

- Traditional AV = signatures. NGAV = behavior. EDR = continuous recording, investigation, response.

- CIS Benchmarks = standard hardening reference; Level 1 = practical; Level 2 = high-security.

- Patch prioritization: CVSS score + CISA KEV catalog + asset criticality.

- FDE + TPM = protection against physical theft; SED requires proper key management.

- Application allowlisting = strongest malware control; highest operational cost.

- MDM = full device control. MAM = app/data only; preferred for BYOD.

- Host-based firewall = endpoint-level control that operates off the corporate network.

Complete the Module 08 quiz and lab to finish this unit.

---

End of Part 2 — Module 08
