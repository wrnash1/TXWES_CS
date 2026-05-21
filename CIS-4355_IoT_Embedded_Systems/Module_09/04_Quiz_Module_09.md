# Quiz: Module 09 - IoT Security – OWASP IoT Top 10
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Why is symmetric cryptography (like AES) preferred over asymmetric cryptography (like RSA) for securing bulk sensor data transmissions directly on microcontrollers?
*   A) Symmetric cryptography does not require encryption keys, eliminating key management overhead on constrained devices.
*   B) RSA and other asymmetric algorithms require large-integer modular exponentiation, which is computationally expensive and power-intensive for low-power microcontrollers with limited RAM.
*   C) Symmetric cryptography is stronger than asymmetric cryptography because longer keys are not needed to achieve equivalent security.
*   D) Asymmetric cryptography is prohibited by embedded systems regulations on devices with less than 256 KB of flash memory.
*   **Correct Answer:** B) RSA and other asymmetric algorithms require large-integer modular exponentiation, which is computationally expensive and power-intensive for low-power microcontrollers with limited RAM.
*   **Distractor Analysis:**
    *   *Why correct:* AES uses simple bitwise XOR, substitution, and permutation operations that execute quickly on 8-bit and 32-bit microcontrollers. RSA-2048 key operations can take seconds on a Cortex-M0 and drain significant battery capacity. In practice, asymmetric crypto is used only for the initial key exchange; bulk data is then encrypted with the negotiated symmetric session key.
    *   Symmetric cryptography absolutely requires key management — the shared secret must be provisioned securely. The distinction is computational cost, not key elimination.

---

**Question 2**
Which of the following is the most accurate definition of **OWASP IoT Top 10 category #7: Insecure Data Transfer and Storage**?
*   A) The use of factory-default or hardcoded credentials on network-accessible device services, allowing any attacker with the device model number to authenticate without authorization.
*   B) The transmission of sensitive data (credentials, telemetry, personal information) without encryption over the network, or the storage of sensitive data in cleartext on the device's flash memory or configuration files.
*   C) The deployment of IoT devices without physical security controls, allowing an attacker with physical access to extract firmware through exposed JTAG or UART debug ports.
*   D) The failure to cryptographically sign or verify firmware update packages before installation, allowing an attacker to deliver a malicious firmware image via the update channel.
*   **Correct Answer:** B) The transmission of sensitive data without encryption over the network, or the storage of sensitive data in cleartext on the device's flash memory or configuration files.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes OWASP IoT Top 10 category #1 (Weak, Guessable, or Hardcoded Passwords), not category #7.
    *   *Why B is correct:* Category #7 covers both network transport (MQTT on port 1883 without TLS, HTTP instead of HTTPS) and at-rest storage (credentials in plaintext config files, unencrypted flash). Both expose sensitive data to a network eavesdropper or a device thief respectively.
    *   *Why C is incorrect:* This describes OWASP IoT Top 10 category #10 (Lack of Physical Hardening).
    *   *Why D is incorrect:* This describes OWASP IoT Top 10 category #4 (Lack of Secure Update Mechanism).

---

**Question 3**
A penetration tester scans a deployed smart thermostat and discovers: (1) telnet is open on port 23 with the factory-default username "admin" and password "admin"; (2) an HTTP configuration portal is accessible on port 8080 with no authentication; (3) all MQTT telemetry is transmitted on port 1883 without TLS. Which OWASP IoT Top 10 categories does this device violate?
*   A) Only category #1 (Weak Passwords), because all three findings share the same root cause of poor access control.
*   B) Category #1 (Weak Passwords), category #2 (Insecure Network Services), and category #7 (Insecure Data Transfer), because each finding maps to a distinct vulnerability class.
*   C) Category #3 (Insecure Ecosystem Interfaces) and category #9 (Insecure Default Settings), because the issues stem from the default factory configuration shipped with the device.
*   D) Category #4 (Lack of Secure Update Mechanism) and category #10 (Lack of Physical Hardening), because the exposed services could allow a firmware replacement attack.
*   **Correct Answer:** B) Category #1 (Weak Passwords), category #2 (Insecure Network Services), and category #7 (Insecure Data Transfer).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The three findings represent distinct vulnerability classes. Collapsing them into one category prevents accurate risk assessment — each requires a different remediation control.
    *   *Why B is correct:* Finding 1 (default telnet credentials) = #1 (Weak Passwords). Finding 2 (unauthenticated HTTP service) = #2 (Insecure Network Services). Finding 3 (MQTT without TLS) = #7 (Insecure Data Transfer). These are separate OWASP categories even though they occur on the same device.
    *   *Why C is incorrect:* While #9 (Insecure Default Settings) could also apply, it is not the primary classification. Category #3 covers web, cloud, and mobile app interfaces — not a local HTTP portal without authentication.
    *   *Why D is incorrect:* Categories #4 and #10 address firmware update integrity and physical access respectively — neither maps to exposed network services or cleartext transport.

---

**Question 4**
A security engineer reviewing a production IoT deployment finds that all devices use identical pre-shared MQTT credentials embedded as plaintext strings in the compiled firmware binary, and the firmware can be extracted from any device by connecting a USB-to-UART adapter to exposed test points on the PCB. Which two OWASP IoT Top 10 categories does this represent, and what is the combined risk?
*   A) Category #5 (Insecure Components) and category #8 (Lack of Device Management) — the risk is that outdated firmware may contain known CVEs exploitable via the UART interface.
*   B) Category #1 (Weak/Hardcoded Passwords) and category #10 (Lack of Physical Hardening) — extracting the firmware via UART exposes the hardcoded credentials, allowing an attacker to authenticate to the MQTT broker from any network-connected device.
*   C) Category #6 (Insufficient Privacy Protection) and category #7 (Insecure Data Transfer) — the plaintext credentials violate user privacy and the UART enables traffic interception.
*   D) Category #2 (Insecure Network Services) and category #4 (Lack of Secure Update Mechanism) — the UART port is a network service and the hardcoded credentials prevent firmware updates from being authenticated.
*   **Correct Answer:** B) Category #1 (Weak/Hardcoded Passwords) and category #10 (Lack of Physical Hardening).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Category #5 refers to third-party software components with known vulnerabilities, not hardcoded credentials. Category #8 covers fleet management and patch deployment, not credential storage.
    *   *Why B is correct:* Hardcoded plaintext credentials = #1 (Weak/Hardcoded Passwords). Exposed JTAG/UART test points enabling firmware extraction = #10 (Lack of Physical Hardening). The combined risk is a physical-to-network attack chain: physical access extracts credentials via UART, and the credentials grant network-wide MQTT broker access from anywhere.
    *   *Why C is incorrect:* Category #6 covers personal user data privacy, not device authentication credentials. Category #7 covers unencrypted transmission, not physical extraction of firmware.
    *   *Why D is incorrect:* UART is a physical debug interface, not a network service. Category #4 refers to the OTA firmware update pipeline, not credential management.

---

**Question 5**
An IoT product manager proposes shipping 50,000 smart locks with all devices using the same default PIN "000000" and an instruction card saying "Change your PIN after setup." A security engineer objects. Which specific OWASP IoT Top 10 risk does this design introduce, and what is the correct remediation?
*   A) OWASP IoT #4 (Lack of Secure Update Mechanism) — remediation is to sign firmware images with ECDSA before shipping.
*   B) OWASP IoT #1 (Weak, Guessable, or Hardcoded Passwords) — remediation is to provision each device with a unique, randomly generated PIN at manufacture and enforce a first-use PIN change through the device interface before the lock becomes operational.
*   C) OWASP IoT #9 (Insecure Default Settings) — remediation is to include the default PIN in the product documentation so users are aware of the security implication.
*   D) OWASP IoT #3 (Insecure Ecosystem Interfaces) — remediation is to require a mobile app account before the lock can be paired, adding an authentication layer above the PIN.
*   **Correct Answer:** B) OWASP IoT #1 (Weak, Guessable, or Hardcoded Passwords) — remediation requires unique per-device credentials and enforced first-use change.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* OWASP IoT #4 addresses the firmware update mechanism, not default device credentials. Firmware signing does not protect against an attacker using the default PIN.
    *   *Why B is correct:* A shared default PIN "000000" across 50,000 devices is a textbook OWASP IoT #1 violation. Research consistently shows that a significant percentage of users never change default credentials. The correct remediation is unique per-device credentials provisioned at manufacture — not relying on user action — and a technical enforcement mechanism that prevents the device from becoming operational until the default is changed.
    *   *Why C is incorrect:* Documenting the default PIN does not remediate the risk — it informs attackers as much as users. Category #9 describes insecure default settings broadly, but the primary classification for weak/default passwords is specifically #1.
    *   *Why D is incorrect:* A mobile app account layer is a useful additional control but does not address the core problem: the same "000000" PIN works on every device, so an attacker who bypasses or clones the app still has a universal credential.
