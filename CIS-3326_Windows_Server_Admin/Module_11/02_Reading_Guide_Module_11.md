# Reading Guide: Module 11 - Windows Server Security - BitLocker, EFS, and Firewall

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 11 – Windows Server Security: BitLocker, EFS, and Windows Firewall**! This week's study material covers the three primary built-in security controls that protect data at rest and control network access on Windows Server. These controls are heavily emphasized on both AZ-800 (administration) and AZ-801 (security) exam objectives.

As a student, you will learn how BitLocker Drive Encryption protects data on lost or stolen drives, how the Encrypting File System (EFS) protects individual files, and how Windows Defender Firewall with Advanced Security controls inbound and outbound network traffic at the host level. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **BitLocker Drive Encryption**: A full-disk encryption feature that encrypts an entire volume to protect data if the physical drive is removed or the server is stolen. BitLocker uses AES encryption and stores the encryption key in a Trusted Platform Module (TPM) chip, optionally combined with a PIN or startup key.
* **TPM (Trusted Platform Module)**: A hardware chip on the server motherboard that stores BitLocker encryption keys and verifies the integrity of the boot environment. BitLocker without TPM requires a startup USB key to unlock the drive at every boot.
* **BitLocker Network Unlock**: A feature that automatically unlocks BitLocker-protected drives on domain-joined servers during network boot, eliminating the need for manual PIN entry on headless servers. Requires a WDS server and a Network Unlock certificate.
* **Encrypting File System (EFS)**: A file-system-level encryption feature that encrypts individual files and folders using the user's certificate. Unlike BitLocker, EFS is transparent to the owning user but blocks access from other users — even administrators — without the recovery certificate.
* **Data Recovery Agent (DRA)**: A special account designated to decrypt EFS-protected files if the original user's certificate is lost. Enterprise environments configure a DRA through Group Policy to prevent permanent data loss from certificate loss.
* **Windows Defender Firewall with Advanced Security (WFAS)**: A host-based, stateful firewall built into Windows Server. It supports inbound and outbound filtering rules, connection security rules (IPsec), and can be managed via Group Policy for centralized enterprise deployment across all domain servers.

---

### 2. Certification Exam Tips

* **BitLocker TPM modes**: AZ-801 and AZ-800 test BitLocker configuration options. TPM-only mode is the least secure (no user interaction at boot). TPM + PIN adds a pre-boot PIN. TPM + Startup Key uses a USB drive. TPM + PIN + Startup Key is the most secure. Know the trade-off between security and operational convenience for server environments.
* **EFS vs. BitLocker scope**: BitLocker encrypts entire volumes — best for protecting against physical theft of the drive. EFS encrypts individual files — best for protecting sensitive files from other OS users on the same machine. Both can be used together.
* **WFAS rule precedence**: Windows Defender Firewall processes rules in order: Block rules take priority over Allow rules for the same traffic. A GPO-deployed firewall rule overrides a locally configured rule when the GPO rule is set to "Override local firewall rules."
* **Microsoft Learn Reference**: Review encryption and firewall documentation at [Microsoft Learn – BitLocker Overview](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) and [Microsoft Learn – Windows Defender Firewall](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the BitLocker and Windows Firewall documentation at [Microsoft Learn: BitLocker Overview](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) and [Microsoft Learn: Windows Defender Firewall](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security). Focus on TPM modes, network unlock, EFS recovery agents, and firewall rule types.
* **Required Video:** Watch the video lecture on **Windows Server Security** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will enable BitLocker on a data volume using `Enable-BitLocker` in PowerShell, configure an EFS-encrypted folder and test access from a second user account, and create a custom inbound firewall rule in WFAS to block a specific port. You will verify BitLocker status with `manage-bde -status`.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the BitLocker documentation at [Microsoft Learn: BitLocker Overview](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview).
* [ ] Read the firewall documentation at [Microsoft Learn: Windows Defender Firewall](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security).
* [ ] Watch the video lecture on **Windows Server Security** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
