# Quiz: Module 11 - Windows Server Security

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

A server stores highly sensitive financial data and must have its OS volume encrypted so that the server cannot boot without presenting a PIN in addition to using the TPM chip. Which BitLocker configuration satisfies this requirement?

A) TPM-only mode, which uses the TPM chip alone to release the volume encryption key automatically at boot without user interaction.
B) TPM + PIN mode, which requires the TPM chip and a user-supplied PIN at pre-boot, preventing unattended boot without both factors.
C) Password-only mode, which replaces the TPM entirely and prompts for a BitLocker password on every boot.
D) USB Startup Key mode, which stores the encryption key on a USB drive inserted at boot and requires no TPM at all.

* **Correct Answer:** B) TPM + PIN mode, which requires the TPM chip and a user-supplied PIN at pre-boot, preventing unattended boot without both factors.
* **Distractor Analysis:**
  * *Why A is incorrect:* TPM-only mode releases the volume key automatically if platform measurements match — no PIN or user interaction is required. The server would boot unattended, which does not satisfy the requirement for a PIN challenge.
  * *Why C is incorrect:* Password-only mode does not use the TPM at all and is not available for OS volumes in standard BitLocker configurations. TPM + PIN combines hardware attestation with a knowledge factor, providing stronger assurance.
  * *Why D is incorrect:* USB Startup Key mode stores the key externally on a removable USB drive rather than combining TPM hardware binding with a PIN. It introduces a physical token dependency and does not meet the TPM + PIN requirement described in the scenario.

---

### Question 2

A Windows Server administrator needs to encrypt a single sensitive folder on a file server so that only the owning user account can decrypt the files, even if another administrator logs on locally. Which Windows feature provides per-file, per-user encryption at the NTFS level?

A) BitLocker Drive Encryption, which encrypts the entire volume so all files are protected regardless of which user account reads them.
B) Encrypting File System (EFS), which encrypts individual files and folders using the user's certificate so only the owner and designated recovery agents can decrypt them.
C) Windows Defender Credential Guard, which isolates credential secrets in a virtualization-based security enclave.
D) NTFS Deny permissions configured for all other accounts, which prevent other users from reading files even when logged in as a local administrator.

* **Correct Answer:** B) Encrypting File System (EFS), which encrypts individual files and folders using the user's certificate so only the owner and designated recovery agents can decrypt them.
* **Distractor Analysis:**
  * *Why A is incorrect:* BitLocker encrypts an entire volume and protects data at rest when the drive is removed from the server, but once the volume is unlocked at boot all authenticated users — including other admins — can read unencrypted file contents. It does not provide per-user file-level access control.
  * *Why C is incorrect:* Credential Guard protects NTLM hashes and Kerberos tickets in a virtualized security boundary — it is an identity protection feature, not a file encryption mechanism.
  * *Why D is incorrect:* A local Administrator account holds SeBackupPrivilege and SeRestorePrivilege and can bypass NTFS Deny permissions to access file contents. NTFS permissions alone cannot prevent a local administrator from reading files the way EFS encryption does.

---

### Question 3

A Windows Server administrator creates an inbound firewall rule in Windows Defender Firewall with Advanced Security (WFAS) to allow TCP port 3389 for the IT Admins security group. A second rule explicitly blocks TCP port 3389 for all users. Both rules are set at the same priority level. Which rule takes effect for members of the IT Admins group?

A) The Allow rule takes effect because Allow rules always override Block rules in WFAS when the same port is targeted.
B) The Block rule takes effect because Block rules take precedence over Allow rules in WFAS regardless of group membership.
C) Neither rule applies; WFAS reverts to the default inbound behavior and drops the connection due to the conflict.
D) The most recently created rule takes effect because WFAS processes rules in creation order with last-write-wins semantics.

* **Correct Answer:** B) The Block rule takes effect because Block rules take precedence over Allow rules in WFAS regardless of group membership.
* **Distractor Analysis:**
  * *Why A is incorrect:* WFAS does not give Allow rules automatic precedence over Block rules. The evaluation order in WFAS is: authenticated bypass rules first, then Block rules, then Allow rules — Block wins over Allow at the same precedence level.
  * *Why C is incorrect:* WFAS does not revert to a neutral default when rules conflict; the explicit Block rule is the matching active rule and it drops the connection. The default inbound drop behavior only applies when no matching rule exists at all.
  * *Why D is incorrect:* WFAS does not use creation-order or last-write-wins semantics. Rule type (Block vs. Allow) and rule priority determine precedence, with Block rules taking priority over Allow rules at equivalent priority settings.

---

### Question 4

An organization's servers are deployed in a data center with no on-site staff. The servers use BitLocker with TPM + PIN mode. After a power outage all servers need to reboot, but no one is available to type the PIN at each server console. Which BitLocker feature allows these servers to boot automatically when connected to the corporate network, while still requiring the PIN for any boot that occurs off-network?

A) BitLocker Recovery Password stored in Active Directory, which automatically supplies the recovery password to servers on the corporate network at boot time.
B) BitLocker Network Unlock, which automatically releases the volume encryption key when the server PXE-boots on a trusted corporate network segment, eliminating the pre-boot PIN requirement on that network.
C) USB Startup Key mode, which stores the PIN equivalent on a USB drive that can be pre-inserted at all server locations.
D) TPM-only mode, which removes the PIN requirement permanently so servers always boot unattended regardless of network location.

* **Correct Answer:** B) BitLocker Network Unlock, which automatically releases the volume encryption key when the server PXE-boots on a trusted corporate network segment, eliminating the pre-boot PIN requirement on that network.
* **Distractor Analysis:**
  * *Why A is incorrect:* BitLocker Recovery Passwords stored in AD are a break-glass recovery mechanism used when normal unlock methods fail. They are not automatically supplied to servers over the network — an administrator must manually retrieve and enter the 48-digit recovery key.
  * *Why C is incorrect:* USB Startup Key distributes a physical token to server locations, which requires manual insertion before each boot. It does not provide automatic unlocking and does not eliminate the need for on-site staff at reboot time.
  * *Why D is incorrect:* Switching to TPM-only mode removes PIN protection entirely and permanently, including when the server is booted off the corporate network. This eliminates the security control rather than providing context-aware automatic unlock.

---

### Question 5

A company's IT policy requires that if an employee's EFS private key is lost or the employee leaves the organization, a designated administrator must still be able to decrypt the employee's EFS-protected files. Which EFS configuration supports this organizational recovery capability?

A) Configure BitLocker on the same volume so the BitLocker recovery key can be used to decrypt any EFS-encrypted file when the original EFS key is unavailable.
B) Configure a Data Recovery Agent (DRA) by issuing an EFS recovery certificate to a designated administrator account and applying it via Group Policy so the DRA certificate is embedded in every subsequently encrypted file.
C) Enable Volume Shadow Copy Service on the EFS volume so previous versions of encrypted files can be opened without the original EFS key.
D) Enable EFS key archival in Certificate Services so the user's private key is automatically backed up to the CA database and can be retrieved by any domain administrator on demand.

* **Correct Answer:** B) Configure a Data Recovery Agent (DRA) by issuing an EFS recovery certificate to a designated administrator account and applying it via Group Policy so the DRA certificate is embedded in every subsequently encrypted file.
* **Distractor Analysis:**
  * *Why A is incorrect:* BitLocker and EFS operate at different layers. A BitLocker recovery key unlocks the volume but does not decrypt individual EFS-encrypted files within that volume; EFS decryption still requires the user's private key or a configured DRA private key.
  * *Why C is incorrect:* Volume Shadow Copies capture point-in-time snapshots of files, but snapshots of EFS-encrypted files remain encrypted with the same user certificate. Accessing a previous version does not bypass EFS encryption — the private key is still required to read the file contents.
  * *Why D is incorrect:* Certificate Services key archival must be explicitly enabled on the certificate template and enrolled by the user. It is not enabled by default for EFS certificates. The DRA is the standard Group Policy-driven mechanism recommended for enterprise EFS recovery and applies to all users automatically once configured.
