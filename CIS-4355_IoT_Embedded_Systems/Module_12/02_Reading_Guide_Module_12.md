# Reading Guide: Module 12 — IoT Security

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Learning Objectives

By the end of this module you should be able to:

- Identify and explain each of the OWASP IoT Top 10 vulnerability categories
- Describe how TLS protects MQTT communications, including the handshake sequence
- Configure certificate-based mutual TLS authentication for IoT device connections
- Explain how firmware signing and ESP32 secure boot prevent unauthorized code execution
- Articulate a defense-in-depth security strategy for a multi-tier IoT deployment

---

## Section 1 — The IoT Threat Landscape

### Why IoT Security Is Uniquely Difficult

Traditional enterprise systems benefit from decades of security tooling: endpoint detection, automated patch management, network segmentation, and security information and event management (SIEM) platforms. IoT devices operate outside this tooling in several important ways.

First, IoT devices are long-lived. An industrial sensor deployed in a factory in 2018 may run the same firmware until 2030. Enterprise laptops receive patches weekly; IoT firmware is often updated once every 12–18 months if ever.

Second, IoT devices are resource-constrained. A microcontroller with 256 KB of RAM and 80 MHz of clock speed cannot run a full TLS stack with RSA-4096 keys without significant latency. Security engineers must balance protection strength against device capability — and the compromises made at design time persist for years.

Third, IoT devices are physically exposed. A temperature sensor in a parking garage, a RFID reader on a door, or a gas meter outside a building can be physically accessed by an adversary without triggering any logical alarm. Physical access enables attacks that are impossible remotely: reading firmware from an unencrypted flash chip, injecting commands through an exposed UART debug port, or extracting private keys from RAM using cold-boot techniques.

Fourth, IoT systems are heterogeneous. A single enterprise deployment may include devices from dozens of manufacturers running different operating systems, communication protocols, and update mechanisms. Managing security consistently across this diversity requires deliberate architectural choices.

### The Mirai Botnet — A Case Study

In September and October 2016, the Mirai botnet infected approximately 600,000 IoT devices — primarily IP cameras, DVRs, and home routers — and used them to launch distributed denial-of-service (DDoS) attacks. The attack technique was straightforward: Mirai scanned the public internet for devices with open Telnet ports and tried a dictionary of 61 factory-default username and password combinations. Devices with unchanged default credentials were infected within seconds of being discovered.

The infected fleet launched DDoS attacks against several targets, including DNS provider Dyn. Because Dyn provided DNS resolution for major websites, the attack disrupted access to Netflix, Reddit, Twitter, Amazon, and Spotify across the eastern United States and Europe for several hours. The peak attack volume was approximately 1.2 terabits per second — far beyond what traditional DDoS mitigation infrastructure was designed to handle at the time.

The root cause was OWASP IoT Top 10 vulnerability number 1: weak, guessable, hardcoded passwords. The technical fix — force credential change on first boot, disable Telnet in production firmware — is straightforward. The organizational failure was that neither manufacturers nor consumers treated default credentials as a critical security issue until a large-scale attack demonstrated the consequences.

---

## Section 2 — OWASP IoT Top 10 in Detail

The OWASP IoT Top 10 is the authoritative reference framework for IoT security risks. Each category is defined by a failure mode and associated with concrete, testable controls.

### Category 1 — Weak, Guessable, or Hardcoded Passwords

**Failure mode:** Devices ship with well-known default credentials (admin/admin, root/root, admin/1234), or credentials are embedded in firmware source code that attackers can extract from a binary.

**Controls:** Require unique credentials per device established during manufacturing or first-boot provisioning. Never embed credentials in source code or firmware images. Implement account lockout after repeated failed authentication attempts.

### Category 2 — Insecure Network Services

**Failure mode:** Devices expose network services — Telnet, FTP, UPnP, unprotected HTTP APIs — that are unnecessary for operation or that expose administrative functions without authentication.

**Controls:** Enumerate all open ports and services during security review. Disable every service not required for the device's defined function. Apply input validation to all exposed service endpoints.

### Category 3 — Insecure Ecosystem Interfaces

**Failure mode:** The web dashboard, mobile application backend, or cloud API associated with the device lacks authentication controls, rate limiting, or input validation, creating an indirect path to the device.

**Controls:** Apply HTTPS to all ecosystem interfaces. Implement token-based authentication with short expiry. Add rate limiting to all authentication endpoints to prevent credential stuffing.

### Category 4 — Lack of Secure Update Mechanism

**Failure mode:** The device has no ability to receive firmware updates, or the update mechanism lacks cryptographic verification — allowing an attacker to deliver arbitrary firmware.

**Controls:** Design OTA capability before product launch. Require ECDSA or RSA signature verification on every firmware image before flashing. Use staged rollouts to limit blast radius of defective updates.

### Category 5 — Use of Insecure or Outdated Components

**Failure mode:** Third-party libraries embedded in firmware — OpenSSL, mbedTLS, lwIP — have published CVEs that the device cannot patch because no update mechanism exists.

**Controls:** Generate a Software Bill of Materials (SBOM) during the build process. Monitor the National Vulnerability Database (NVD) for CVEs affecting SBOM components. Define a maximum acceptable time-to-patch for critical severity CVEs.

### Category 6 — Insufficient Privacy Protection

**Failure mode:** Devices collect sensitive data — biometrics, location traces, behavioral patterns — without user consent or regulatory compliance. Data is stored in plaintext or transmitted without encryption.

**Controls:** Apply data minimization: collect only what is functionally necessary. Encrypt sensitive data at rest on the device and in transit to the cloud. Implement configurable data retention periods with automatic deletion.

### Category 7 — Insecure Data Transfer and Storage

**Failure mode:** Device-to-cloud communication uses cleartext protocols (HTTP, MQTT on port 1883, CoAP without DTLS). On-device storage uses unencrypted flash, readable with a hardware programmer.

**Controls:** Require TLS for all network communication. Use hardware-accelerated AES to encrypt sensitive on-device storage partitions. Never store plaintext credentials or tokens in NVRAM or flash.

### Category 8 — Lack of Device Management

**Failure mode:** No central registry exists for device inventory. Firmware versions across the fleet are unknown. No process exists to detect, isolate, or decommission compromised devices.

**Controls:** Implement a cloud-based device registry with firmware version telemetry. Define and exercise incident response procedures for fleet security events. Implement certificate revocation capability so compromised devices can be blocked at the authentication layer.

### Category 9 — Insecure Default Settings

**Failure mode:** Production devices ship with debug-mode settings active — UART debug output enabled, JTAG accessible, verbose error messages exposing internal paths, permissive CORS headers on the web UI.

**Controls:** Maintain separate debug and production build configurations. Automate security configuration audits in CI/CD pipelines. Default-deny all inbound connections; explicitly allow only required communication paths.

### Category 10 — Lack of Physical Hardening

**Failure mode:** Physical access to the device allows an attacker to read firmware from flash using a programmer, inject commands via an exposed JTAG or UART port, or extract keys from RAM.

**Controls:** Disable JTAG in production by burning eFuses. Encrypt flash storage. Apply resin potting or tamper-evident seals where the threat model warrants it. Log and alert on unexpected physical access attempts.

---

## Section 3 — TLS for MQTT: Technical Details

### MQTT Protocol Basics

MQTT (Message Queuing Telemetry Transport) is a publish-subscribe messaging protocol designed for constrained devices and unreliable networks. Devices publish messages to named topics on a broker; other devices or cloud services subscribe to those topics and receive the messages. The protocol overhead is minimal — the fixed header is as small as 2 bytes — making it practical for battery-powered devices over cellular or low-bandwidth links.

By default, MQTT runs over TCP on port 1883 without any transport encryption. The CONNECT packet contains a username and password field, but these are transmitted in plaintext and provide no protection if the transport is not encrypted.

### TLS Architecture

Transport Layer Security (TLS) version 1.3 is the current standard for securing TCP connections. When applied to MQTT, the MQTT protocol is unchanged — the TLS layer encrypts and authenticates the bytes of every MQTT packet. The broker listens on port 8883 for TLS connections.

The TLS handshake establishes three things before any application data is exchanged:

**Confidentiality:** The handshake negotiates symmetric encryption keys using an ephemeral key exchange — typically Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). The symmetric cipher (AES-128-GCM or ChaCha20-Poly1305) encrypts all subsequent data.

**Integrity:** An Authenticated Encryption with Associated Data (AEAD) cipher guarantees that any modification to a ciphertext is detected before decryption. An attacker cannot silently alter an MQTT PUBLISH payload in transit.

**Authentication:** The server presents an X.509 certificate signed by a Certificate Authority. The client verifies the certificate against its CA trust store, confirming it is communicating with the intended broker and not an attacker's relay.

### Mutual TLS for Device Authentication

Standard TLS authenticates only the server. Mutual TLS — mTLS — extends this so the client (the IoT device) also presents a certificate during the handshake. The broker validates the device certificate against its CA, providing strong, unforgeable device authentication.

With mTLS, the authentication sequence is:

1. Client sends ClientHello.
2. Server responds with ServerHello and its certificate.
3. Server sends CertificateRequest, asking the client for its certificate.
4. Client sends its unique device certificate.
5. Both sides verify each other's certificates against their respective CA trust stores.
6. Key exchange completes and encrypted communication begins.

The device's private key never leaves the device. On devices with a hardware secure element — like the ESP32's eFuse region or an external ATECC608A chip — the private key operations are performed inside the secure hardware and the key material is never accessible to firmware code.

---

## Section 4 — Firmware Signing and Secure Boot

### Code Signing Pipeline

Firmware signing is a publish-subscribe security model applied to software delivery: only binaries signed by a known private key can be executed on a device.

The signing pipeline consists of three components:

**The signing server** holds the ECDSA or RSA private key used to sign firmware. This server should be air-gapped or have its HSM (Hardware Security Module) accessible only during authorized release operations.

**The firmware image** produced by the build system includes a cryptographic signature appended to the binary. The signature is computed over the SHA-256 hash of the firmware payload.

**The device bootloader** performs signature verification before writing any new firmware to the application partition. It recomputes the hash of the received firmware and verifies the signature using the public key stored in a protected region of flash. If verification fails, the bootloader discards the image and resumes normal operation with the existing firmware.

### ESP32 Secure Boot

The ESP32 implements secure boot using eFuses — one-time-programmable fuses embedded in the chip. The secure boot process is:

1. During manufacturing, a unique secure boot signing key is generated and burned into eFuses. The eFuse region that holds this key is marked as read-protected — once written, the key value cannot be read back by software.
2. In production, the ROM bootloader verifies the second-stage bootloader signature at every reset.
3. The second-stage bootloader verifies the application firmware signature before executing it.
4. The secure boot eFuse is burned to a read-only state after configuration — it cannot be disabled by software or subsequent firmware updates.

Once secure boot is enabled, the device will only execute firmware signed with the corresponding private key. Physical access to the device does not circumvent this — even if an attacker connects a hardware debugger and attempts to flash unsigned firmware, the ROM bootloader will reject it.

---

## Section 5 — Defense-in-Depth for IoT

A defense-in-depth model applies multiple independent security controls so that a failure in any single control does not result in full system compromise.

For a typical IoT deployment, the five layers are:

**Layer 1 — Device hardening:** Secure boot enabled, firmware signed, JTAG disabled in eFuses, debug logging disabled in production builds, sensitive data encrypted on flash.

**Layer 2 — Transport security:** TLS 1.3 on all network connections, certificate chain validation enforced, no fallback to plaintext protocols.

**Layer 3 — Authentication:** Per-device X.509 certificates, mutual TLS, certificate revocation capability, no shared credentials.

**Layer 4 — Network segmentation:** IoT devices on isolated VLANs, firewall rules restricting inter-VLAN traffic to only required protocols and destinations, intrusion detection on VLAN boundary.

**Layer 5 — Monitoring and response:** Fleet-wide firmware version telemetry, anomalous connection attempt alerting, automated certificate expiry monitoring, defined incident response playbooks.

---

## Key Terms

- **OWASP IoT Top 10** — OWASP's classification of the ten most critical IoT security risks
- **Mirai botnet** — 2016 IoT botnet that exploited default credentials to launch record DDoS attacks
- **MQTT** — Message Queuing Telemetry Transport; lightweight publish-subscribe protocol
- **TLS** — Transport Layer Security; cryptographic protocol securing TCP connections
- **mTLS** — Mutual TLS; both client and server present certificates for bidirectional authentication
- **X.509** — Standard format for digital certificates used in TLS and PKI
- **CA** — Certificate Authority; trusted entity that issues and signs digital certificates
- **CRL** — Certificate Revocation List; list of certificates that have been invalidated before expiry
- **ECDHE** — Elliptic Curve Diffie-Hellman Ephemeral; key exchange algorithm used in TLS 1.3
- **Secure Boot** — Hardware-enforced requirement that firmware must be cryptographically signed
- **eFuse** — One-time-programmable hardware bits used to store security configuration permanently
- **SBOM** — Software Bill of Materials; inventory of all components and libraries in a firmware image
- **PSK-TLS** — Pre-Shared Key TLS; authentication using a pre-agreed secret instead of certificates
- **Defense-in-depth** — Layered security strategy where each control compensates for failures in adjacent controls

---

## Review Questions

1. What three network layers in an IoT deployment constitute the primary attack surface?
2. Which OWASP IoT category was exploited by the Mirai botnet, and what was the specific technical failure?
3. What three security properties does TLS provide? Define each property in one sentence.
4. What is the difference between standard TLS and mutual TLS in terms of what each party authenticates?
5. In the ESP32 secure boot process, what happens if a firmware image fails signature verification at the bootloader?
6. Why does firmware signing fail to prevent attacks if the signing private key is exposed?
7. Which OWASP category does a device with an exposed, accessible JTAG debug port primarily represent?
8. What is a Software Bill of Materials (SBOM) and why is it relevant to OWASP IoT Category 5?
9. What is the purpose of ECDHE in a TLS 1.3 handshake, and what property does it provide that RSA key exchange does not?
10. Describe two controls from different defense-in-depth layers that together prevent an attacker who has compromised a single device from accessing cloud backend data.

---
