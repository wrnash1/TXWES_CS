# Reading Guide: Module 09 - IoT Security – OWASP IoT Top 10
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 09 – IoT Security: OWASP IoT Top 10**! This module provides a structured framework for identifying, understanding, and mitigating the ten most critical security vulnerabilities in IoT products and deployments, as catalogued by the Open Web Application Security Project (OWASP). The OWASP IoT Top 10 is the industry-standard reference for IoT security assessments, penetration tests, and product security programs.

You will work through each of the ten vulnerability categories — from weak default credentials and insecure network services to insufficient privacy protection and insecure data transfer — examining real-world exploit examples, the attack conditions that enable them, and the specific technical and operational controls required to remediate each one. By the end of this module you will be able to classify a security finding against the OWASP IoT Top 10 and recommend appropriate countermeasures.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **OWASP IoT Top 10**: A ranked list published by the Open Web Application Security Project identifying the ten most prevalent and impactful security weaknesses in IoT devices and systems. The ten categories are: (1) Weak, Guessable, or Hardcoded Passwords; (2) Insecure Network Services; (3) Insecure Ecosystem Interfaces; (4) Lack of Secure Update Mechanism; (5) Use of Insecure or Outdated Components; (6) Insufficient Privacy Protection; (7) Insecure Data Transfer and Storage; (8) Lack of Device Management; (9) Insecure Default Settings; and (10) Lack of Physical Hardening.
*   **Weak, Guessable, or Hardcoded Passwords (OWASP IoT #1)**: The use of factory-default, easily guessed, or unchangeable credentials on any network-accessible service (telnet, SSH, HTTP admin panel, MQTT broker). This is the single most exploited IoT vulnerability — the Mirai botnet infected over 600,000 devices using a list of 61 default credential pairs. Remediation requires unique per-device credentials generated at manufacture, forced credential change on first use, and no hardcoded passwords in firmware.
*   **Insecure Network Services (OWASP IoT #2)**: Unnecessary or poorly configured network services running on an IoT device that expose it to network-based attacks. Common examples include telnet on port 23, UPnP on port 1900, and debug HTTP endpoints. Remediation requires a minimal attack surface — disable all services not required for device function, apply firewall rules, and require authentication on any remaining exposed service.
*   **Insecure Data Transfer and Storage (OWASP IoT #7)**: Sensitive data (credentials, telemetry, personal information) transmitted without encryption or stored in cleartext on the device. This includes MQTT over port 1883 without TLS, HTTP instead of HTTPS, and credentials stored as plaintext in flash memory or configuration files. Remediation requires TLS/DTLS for all network transport, encrypted storage for credentials and sensitive configuration, and secure key storage in a hardware element where available.
*   **Lack of Physical Hardening (OWASP IoT #10)**: Deployed IoT devices without physical security controls, enabling an attacker with physical access to extract firmware via JTAG/UART debug ports, read flash memory, or clone device certificates. Remediation includes disabling or removing JTAG/UART headers on production hardware, enabling secure boot, encrypting flash storage, and deploying devices in tamper-evident or tamper-resistant enclosures.

---

### 2. Certification Exam Tips
*   **Map symptoms to OWASP categories:** Exam scenarios describe a vulnerability finding and ask which OWASP IoT Top 10 item it represents. Key mappings: open telnet with default password = #1 (Weak Passwords) + #2 (Insecure Network Services); MQTT without TLS = #7 (Insecure Data Transfer); no OTA update signing = #4 (Lack of Secure Update Mechanism); exposed JTAG port = #10 (Lack of Physical Hardening).
*   **Multiple categories per finding:** A single misconfiguration often maps to two OWASP categories. An unauthenticated MQTT broker on port 1883 is simultaneously #2 (Insecure Network Services) and #7 (Insecure Data Transfer). Exam questions may accept either or ask for both.
*   **Remediation specificity:** Know the specific technical fix for each category, not just the category name. "Use strong passwords" is insufficient — the answer must include unique per-device credentials, no hardcoded passwords, and forced first-use change.
*   **OWASP IoT vs OWASP Web Top 10:** These are different lists. SQL injection and XSS appear in the Web Top 10 but not the IoT Top 10 (IoT devices rarely host relational databases). The IoT list reflects the physical and protocol characteristics of embedded devices.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) is the primary authoritative source for this module — read the full IoT Top 10 list with attack scenarios and remediation guidance for each category.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — read the full IoT Top 10 list, including the attack scenario and remediation section for each of the ten vulnerability categories. This is the authoritative source for this module's content.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes coverage of IoT security threat modeling, demonstrating common vulnerability patterns on example IoT devices and walking through OWASP IoT Top 10 categories with real-world exploit examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Audit an IoT device for OWASP Top 10 vulnerabilities**: Using a Raspberry Pi configured as a simulated IoT gateway, use `nmap -sV` to enumerate open ports and services, identify any services accessible without authentication, and map each finding to its corresponding OWASP IoT Top 10 category.
*   **Test for default credentials**: Use a credential list to attempt authentication against an exposed SSH and HTTP admin interface, document which factory-default pairs succeed, and configure unique strong credentials to remediate finding #1.
*   **Verify encrypted transport**: Use Wireshark to capture MQTT traffic on port 1883 (unencrypted) and port 8883 (TLS), visually confirm that payload content is visible in the cleartext capture and obscured in the TLS capture, and document this as evidence for OWASP IoT #7.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the ten OWASP IoT Top 10 categories and their numbers.
- [ ] Read all ten vulnerability entries at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the IoT security sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Practice mapping vulnerability descriptions to OWASP IoT Top 10 category numbers before the lab.
- [ ] Proceed to the weekly hands-on lab activity.
