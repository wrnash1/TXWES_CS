# Video Script: Module 12 — IoT Security

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Duration:** 14–17 minutes

---

### [00:00 – 02:00] Introduction

**Visual:** Instructor on camera with title card: **IoT Security — Protecting Devices, Data, and Infrastructure**

**Alt-text:** Instructor seated at desk. Title card in lower third reads "Module 12: IoT Security." Background shows a monitor displaying a network topology diagram.

**Audio:** "Welcome to Module 12. Today we tackle one of the most critical and frequently tested topics in IoT engineering: security. IoT devices are deployed everywhere — hospitals, factories, homes, and power grids — and they are under constant attack. Unlike traditional IT systems, IoT devices often run for years without patches, have limited compute for encryption, and are physically accessible to adversaries. Understanding how attackers exploit these constraints, and how engineers defend against them, is essential both for your certification exams and for building systems that survive in production."

"By the end of this module you will be able to: identify the OWASP IoT Top 10 attack categories, explain how TLS secures MQTT communications, describe certificate-based device authentication, explain firmware signing and secure boot, and articulate a defense-in-depth strategy for an IoT deployment."

**Study Link:** [OWASP IoT Project — owasp.org/www-project-internet-of-things](https://owasp.org/www-project-internet-of-things/)

---

### [02:00 – 04:30] The IoT Attack Surface

**Visual:** Diagram showing an IoT device communicating to a broker and cloud, with labeled attack arrows at each layer.

**Alt-text:** A three-tier diagram. Left tier shows an IoT device represented by a microcontroller icon. Middle tier shows an MQTT broker server. Right tier shows a cloud backend. Three red attack arrows are drawn: one labeled "credential stuffing" pointing at the device, one labeled "traffic interception" on the network link between device and broker, and one labeled "unauthorized API call" at the cloud backend.

**Audio:** "Every IoT system has at least three attack surfaces: the device itself, the network transport, and the cloud backend. Attackers do not need sophisticated exploits if the fundamentals are broken. Let's talk about the most common failures."

"**Weak or hardcoded credentials** are the number-one IoT vulnerability. A device that ships with username admin and password admin — and provides no easy way to change it — is a standing invitation. The Mirai botnet of 2016 infected over 600,000 devices using exactly this technique: automated scanning for telnet and SSH services running factory-default credentials. The resulting DDoS attack peaked at 1.2 terabits per second and took down major DNS infrastructure affecting Netflix, Twitter, and Reddit for an entire afternoon."

"**Unencrypted traffic** is the second critical failure. When an IoT device publishes temperature or heart-rate data in plaintext over port 1883 — the default unencrypted MQTT port — anyone on the same network segment can read and modify that data in transit. In industrial settings, an attacker who can modify sensor readings can cause physical damage to equipment or, in medical contexts, patient harm."

"**Firmware vulnerabilities** represent the third major category. Embedded firmware often contains third-party libraries — HTTP parsers, TLS stacks, JSON parsers — that accumulate CVEs over time. Unlike desktop software that auto-updates, IoT devices often run unchanged firmware for years. If there is no OTA update mechanism and no patch process, those vulnerabilities persist for the device's entire multi-year lifespan."

---

### [04:30 – 07:30] OWASP IoT Top 10

**Visual:** Slide showing the OWASP IoT Top 10 list as a numbered table with two columns: number and category name.

**Alt-text:** A formatted table on a white background. Column 1 contains numbers 1 through 10. Column 2 contains category names. The table has a header row reading "OWASP IoT Top 10."

**Audio:** "The Open Web Application Security Project — OWASP — maintains an IoT-specific Top 10 vulnerability list. Let's walk through each category so you recognize it on your exam and in the field."

"Number 1: **Weak, Guessable, or Hardcoded Passwords.** This is Mirai territory. Default credentials ship with most consumer IoT devices. Fix: force a credential change on first boot; never embed credentials in firmware source code."

"Number 2: **Insecure Network Services.** Devices that expose unnecessary services — telnet, FTP, unprotected REST APIs — on their network interface. Fix: disable all services not required for operation. Apply principle of least privilege to every open port."

"Number 3: **Insecure Ecosystem Interfaces.** Weak web UIs, mobile app backends, or cloud APIs that lack rate limiting, input validation, or proper authentication. Fix: apply standard web-security controls — HTTPS, auth tokens, rate limiting — to all ecosystem interfaces."

"Number 4: **Lack of Secure Update Mechanism.** No update path means vulnerabilities accumulate permanently. Fix: design OTA update capability before launch, with cryptographic signature verification on every firmware package."

"Number 5: **Use of Insecure or Outdated Components.** Third-party libraries embedded in firmware with known CVEs. Fix: maintain a Software Bill of Materials — SBOM — monitor the NIST National Vulnerability Database for CVEs affecting your components, and patch on a defined schedule."

"Number 6: **Insufficient Privacy Protection.** IoT devices collect sensitive data — location, biometrics, behavioral patterns. Fix: collect only what is necessary, encrypt at rest and in transit, implement data retention and deletion policies."

"Number 7: **Insecure Data Transfer and Storage.** Cleartext protocols, unencrypted flash storage. Fix: TLS on all network connections, encrypted storage partitions for sensitive on-device data."

"Number 8: **Lack of Device Management.** No visibility into fleet state, no patch tracking, no decommissioning process. Fix: cloud-based device registry with health telemetry, firmware version tracking, and certificate lifecycle management."

"Number 9: **Insecure Default Settings.** Devices that ship with debug interfaces enabled, permissive firewall rules, or verbose error output. Fix: production builds must disable all debug features. Fail-closed rather than fail-open on all default configurations."

"Number 10: **Lack of Physical Hardening.** Exposed debug ports — UART and JTAG — and unencrypted flash chips that can be read with a hardware programmer. Fix: disable JTAG in production eFuse settings, encrypt flash storage, apply tamper-evident enclosures where appropriate."

---

### [07:30 – 10:30] TLS for MQTT

**Visual:** Animated sequence diagram showing the TLS handshake between an MQTT client and broker, then encrypted message exchange.

**Alt-text:** A sequence diagram with two participants: MQTT Client on the left and MQTT Broker on the right. Numbered arrows show the handshake steps: 1 ClientHello from client to broker, 2 ServerHello plus Certificate from broker to client, 3 certificate verification shown as a client-side icon, 4 key exchange arrows, 5 Finished messages, then dashed encrypted arrows labeled PUBLISH and SUBSCRIBE.

**Audio:** "MQTT is the dominant IoT messaging protocol — lightweight, publish-subscribe, designed for constrained networks and unreliable links. By default it runs on port 1883 with no encryption and no authentication beyond a username and password transmitted in plaintext in the CONNECT packet. That is obviously unacceptable in production."

"MQTT over TLS runs on port 8883. The TLS layer provides three security properties: **confidentiality** — all data is encrypted and unreadable to network observers; **integrity** — a Message Authentication Code detects any tampering with packets in transit; and **server authentication** — the server certificate proves the broker's identity, preventing man-in-the-middle attacks where an attacker intercepts traffic by posing as a legitimate broker."

"The TLS handshake works in five phases. First, the client sends a ClientHello message listing its supported TLS version and cipher suites. Second, the server responds with a ServerHello selecting a cipher suite plus its X.509 certificate. Third, the client verifies the certificate chain against its trusted Certificate Authority store — if verification fails, the connection is terminated. Fourth, they perform an ephemeral key exchange, typically ECDHE, to derive session keys. Fifth, both sides send Finished messages and encrypted communication begins. From that point forward, all MQTT traffic — PUBLISH, SUBSCRIBE, PINGREQ — is encrypted."

"On an ESP32 using the Arduino framework and the PubSubClient library, enabling TLS requires three steps: load the root CA certificate as a PEM-format string, create a WiFiClientSecure object and call setCACert() with that string, then pass the WiFiClientSecure to the PubSubClient constructor. Every subsequent connection will negotiate TLS automatically."

"For highly constrained devices where the full certificate chain verification is too expensive in terms of memory and processing time, you can use **PSK-TLS** — Pre-Shared Key TLS. PSK-TLS skips the certificate exchange entirely, authenticating using a shared secret agreed upon during device provisioning. It is computationally cheaper but does not provide CA-rooted chain-of-trust authentication."

---

### [10:30 – 13:00] Certificate-Based Authentication and Firmware Signing

**Visual:** Two-panel slide. Left panel shows a PKI hierarchy tree. Right panel shows a firmware signing pipeline flow diagram.

**Alt-text:** Left panel: a tree diagram with Root CA at the top, an Intermediate CA node below it, and three leaf-level nodes each labeled with a device ID like device-001, device-002, device-003, representing per-device X.509 certificates. Right panel: a left-to-right pipeline with boxes labeled Build System, Signing Server, OTA Package, Device Bootloader, connected by arrows. An annotation on the Signing Server reads "ECDSA private key." An annotation on the Device Bootloader reads "verify with stored public key."

**Audio:** "Certificate-based authentication extends TLS beyond server verification to **mutual TLS** — mTLS — where the device also presents a certificate during the TLS handshake. The cloud backend validates the device certificate against its Certificate Authority, and only accepts connections from devices it has provisioned. This eliminates the username and password weakness entirely: there is no shared secret that can be guessed, phished, or brute-forced — only a private key that never leaves the device's secure storage."

"Each device receives a unique X.509 certificate issued during manufacturing or zero-touch provisioning. The certificate's Subject field typically contains the device ID as the Common Name. The issuing Certificate Authority is controlled by your organization. When a device connects, the MQTT broker checks two things: is this certificate signed by our CA root? And is this certificate listed on the Certificate Revocation List? Only if both checks pass is the device authenticated."

"**Firmware signing** addresses a different threat: ensuring that only firmware built and authorized by your organization can execute on your devices. The process is: your build system compiles the firmware binary; your code-signing server signs the SHA-256 hash of the binary with an ECDSA private key, producing a signature that is appended to the firmware image; during an OTA update, the device bootloader recomputes the hash of the received image and verifies the signature using the stored public key before writing the firmware to flash. If verification fails, the update is rejected and the previous firmware remains active — the device never runs code it cannot verify."

"ESP32 supports hardware-enforced secure boot natively. When you burn the secure boot key into eFuses during manufacturing, the ROM bootloader requires all subsequent firmware images to be signed with the corresponding private key. Once secure boot is enabled and the eFuses are burned, that configuration cannot be disabled — this is deliberate, ensuring that physical access to the hardware cannot downgrade security."

---

### [13:00 – 15:30] Defense-in-Depth and Lab Preview

**Visual:** Layered concentric-ring diagram showing the five security layers of an IoT deployment.

**Alt-text:** Five concentric rings displayed on a dark background. The innermost ring is labeled Device Hardening with sub-items secure boot and firmware signing. The second ring is labeled Transport Security with TLS and mTLS. The third ring is labeled Authentication with X.509 certificates and PKI. The fourth ring is labeled Network Segmentation with VLAN isolation and firewall rules. The outermost ring is labeled Monitoring with anomaly detection and alerting icons.

**Audio:** "Security is never a single control — it is a layered defense where each layer catches failures that slipped past the previous one. In IoT, defense-in-depth means: hardening the device itself so that even physical access yields nothing useful; using TLS so network interception yields nothing readable; using certificates so that credential theft is not the attack vector; using network segmentation so device compromise cannot spread laterally beyond the VLAN boundary; and using continuous monitoring so any breach is detected and responded to quickly."

"For this module's lab, you will work through four exercises. First, you will generate a self-signed CA and device certificate using OpenSSL. Second, you will configure an MQTT broker — Mosquitto — to require TLS on port 8883. Third, you will connect a simulated MQTT client using the device certificate for mutual TLS authentication, and verify that a plaintext connection on port 1883 is rejected. Fourth, you will simulate the firmware signing workflow: generate a signing key pair, sign a test binary with the private key, and verify the signature with the public key — the same cryptographic flow an ESP32 bootloader performs on every OTA update."

"This lab mirrors real production workflows. Every major IoT cloud platform — AWS IoT Core, Azure IoT Hub, Google Cloud IoT Core — uses exactly this mutual TLS model for device authentication. Mastering it now means you can apply it across any cloud platform."

---

### [15:30 – End] Summary and Key Terms

**Visual:** Summary slide listing the five main concepts from the module.

**Audio:** "Let's recap Module 12. The OWASP IoT Top 10 gives you a structured vocabulary for discussing and remediating IoT threats. TLS on port 8883 secures MQTT transport with confidentiality, integrity, and server authentication. Mutual TLS with per-device certificates provides strong authentication that cannot be guessed or phished. Firmware signing with secure boot prevents unauthorized code execution even if an attacker can deliver a firmware image. And defense-in-depth layers all of these controls so that no single failure can compromise an entire system."

**Key Terms for This Module:**

- OWASP IoT Top 10
- Mirai botnet
- MQTT — port 1883 plaintext, port 8883 over TLS
- TLS handshake phases — ClientHello, ServerHello, certificate verification, key exchange, Finished
- X.509 certificate
- Mutual TLS (mTLS)
- Certificate Authority (CA) and Certificate Revocation List (CRL)
- Firmware signing and secure boot
- eFuse (ESP32 hardware security)
- Defense-in-depth
- Software Bill of Materials (SBOM)
- Pre-Shared Key TLS (PSK-TLS)

"In Module 13 we move to Real-Time Operating Systems — FreeRTOS on the ESP32 — where we will apply concepts like task isolation, priority scheduling, and watchdog timers to build robust, deterministic embedded applications. See you there."

---
