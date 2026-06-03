# Quiz: Module 12 — IoT Security

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

### Question 1

The Mirai botnet infected approximately 600,000 IoT devices in 2016 and generated DDoS attacks exceeding 1.2 Tbps. Which OWASP IoT Top 10 category was the primary root cause, and what was the specific technical failure that Mirai exploited?

- A) OWASP IoT #4 (Lack of Secure Update Mechanism) — infected devices had no way to receive patches after the initial vulnerability was disclosed, allowing the botnet to persist indefinitely.
- B) OWASP IoT #1 (Weak, Guessable, or Hardcoded Passwords) — devices shipped with well-known factory-default Telnet credentials that were never changed, allowing automated scanning to compromise devices within seconds of discovery.
- C) OWASP IoT #7 (Insecure Data Transfer and Storage) — devices transmitted management traffic in plaintext over Telnet, allowing Mirai to intercept admin sessions and hijack device control.
- D) OWASP IoT #10 (Lack of Physical Hardening) — devices exposed JTAG debug ports that Mirai accessed to inject malicious firmware, bypassing the credential system entirely.
- **Correct Answer:** B) OWASP IoT #1 — factory-default Telnet credentials that were never changed.
- **Distractor Analysis:**
  - *Why B is correct:* Mirai used a hardcoded dictionary of 61 factory-default username/password pairs against Telnet (port 23) and SSH (port 22) services. Devices that had never had their credentials changed were infected in seconds. This is the canonical real-world example of OWASP IoT #1.
  - *Why A is incorrect:* The lack of update mechanism is a separate concern (OWASP IoT #4) that prevented remediation after infection, but it was not the attack vector. The attack vector was the default credentials.
  - *Why C is incorrect:* While Telnet transmits in plaintext (supporting OWASP IoT #7 concerns), Mirai did not need to intercept sessions — it authenticated directly with the default credentials. The attack was authentication-based, not interception-based.
  - *Why D is incorrect:* Mirai operated entirely over the network using software techniques. JTAG requires physical access to the hardware; Mirai infected devices at internet scale remotely.

---

### Question 2

An IoT security engineer reviews the firmware for a commercial smart lock and discovers that the device's cloud API password is stored as the string `"cloud_pass_2019"` in a global variable in the main source file, and this same value is identical across all 200,000 devices in the product line. Which remediation is most appropriate?

- A) Hash the password using SHA-256 before storing it in the source file — this prevents the plaintext credential from being exposed if the firmware binary is extracted.
- B) Replace the hardcoded credential with per-device unique credentials provisioned during manufacturing and stored in a protected memory region, and rotate the global credential for all 200,000 existing devices immediately.
- C) Move the hardcoded credential from a global variable to a `const` variable in a separate header file with restricted file-system permissions on the build server, reducing exposure risk.
- D) Encrypt the credential using AES-128 with a hardcoded encryption key stored in a second global variable, providing an additional layer of obfuscation before the credential reaches the cloud API.
- **Correct Answer:** B) Replace with per-device unique credentials provisioned at manufacturing, and immediately rotate the global credential.
- **Distractor Analysis:**
  - *Why A is incorrect:* Hashing the password in source code does not protect it — the hash can be extracted from the binary just as easily as the plaintext. The cloud API would need to accept the hash value as the credential, which means the hash *is* the credential and provides the same attack surface.
  - *Why B is correct:* The fundamental problem is that a single credential shared across 200,000 devices means a single extraction compromises the entire fleet. Per-device unique credentials limit the blast radius to one device. Immediate rotation of the global credential invalidates any copies already extracted.
  - *Why C is incorrect:* Moving the credential to a header file with restricted build-server permissions addresses source code exposure, but the credential still ends up compiled into every firmware binary. Anyone who can extract a firmware binary from any device obtains the credential.
  - *Why D is incorrect:* Encrypting a credential with a hardcoded key — also stored in the same firmware — provides security through obscurity, not actual security. An attacker who extracts the firmware binary gets both the encrypted credential and the decryption key simultaneously.

---

### Question 3

An ESP32-based device connects to an MQTT broker over TLS on port 8883. During the TLS handshake, the broker presents an X.509 certificate signed by an unknown Certificate Authority that is not in the device's CA trust store. What is the correct behavior of a properly implemented TLS client in this situation?

- A) The TLS client should log a warning and proceed with the connection using opportunistic encryption — the data is still encrypted even if the server identity is unverified.
- B) The TLS client should terminate the handshake and refuse to establish the connection, because the certificate cannot be verified as authentic and the broker's identity is unconfirmed.
- C) The TLS client should accept the certificate if the server's hostname matches the Common Name in the certificate, because hostname matching is sufficient authentication even without CA verification.
- D) The TLS client should request a secondary authentication factor — such as a username and password — to compensate for the unverified certificate and proceed with the connection.
- **Correct Answer:** B) The TLS client must terminate the handshake and refuse to connect when certificate verification fails.
- **Distractor Analysis:**
  - *Why A is incorrect:* "Opportunistic encryption" — encrypting data without authenticating the server — protects against passive eavesdroppers but not against active man-in-the-middle attacks. An attacker can present their own certificate and terminate the TLS session at both ends, decrypting all traffic. This is precisely the attack that CA verification is designed to prevent. In IoT contexts, this is a critical failure mode.
  - *Why B is correct:* Certificate verification against a trusted CA is not optional in a security-relevant context — it is the mechanism that proves the broker is who it claims to be. An unverified certificate means the device cannot distinguish between a legitimate broker and an attacker's proxy. The correct behavior is to fail closed: terminate the connection.
  - *Why C is incorrect:* Hostname matching without CA verification does not prevent an attacker from generating a self-signed certificate with the correct hostname. Hostname matching is a *complement* to CA verification, not a replacement for it.
  - *Why D is incorrect:* Proceeding with an unauthenticated TLS connection and adding a username/password does not solve the problem. If the connection is to an attacker's man-in-the-middle proxy, the username and password are delivered directly to the attacker over the unverified channel.

---

### Question 4

A device bootloader performs firmware signature verification using ECDSA with the device's stored public key. An attacker who has obtained a physical copy of the device extracts the firmware binary from flash using a hardware programmer, modifies the binary to add a backdoor, and attempts to reflash the modified firmware. What is the expected outcome?

- A) The modified firmware will execute because the bootloader only checks the firmware signature during OTA updates over the network, not during local flash writes.
- B) The modified firmware will fail signature verification because the attacker cannot produce a valid ECDSA signature without the private signing key, and the bootloader will refuse to execute the unsigned binary.
- C) The modified firmware will execute because ECDSA verification only checks the firmware header, not the payload, and the attacker preserved the original header during modification.
- D) The modified firmware will execute if the attacker also modifies the stored public key in flash to match a new key pair they control, replacing the verification key with their own.
- **Correct Answer:** B) Signature verification fails — the attacker cannot sign the modified binary without the private key.
- **Distractor Analysis:**
  - *Why A is incorrect:* A properly implemented secure boot system verifies the firmware signature at every boot, not only during OTA delivery. The bootloader runs signature verification on the firmware currently in the application partition before executing it, regardless of how that firmware arrived.
  - *Why B is correct:* ECDSA security rests on the computational infeasibility of producing a valid signature without the private key. The attacker can modify the binary, but any modification invalidates the original signature, and they cannot generate a new valid signature without the private signing key (which exists only on the secured signing server, never on the device).
  - *Why C is incorrect:* ECDSA verification is computed over the SHA-256 hash of the entire firmware binary. Any modification to any part of the binary — header, payload, or otherwise — changes the hash, which invalidates the signature. There is no "header-only" verification in firmware signing.
  - *Why D is incorrect:* On ESP32, the public key used for secure boot verification is stored in eFuses — one-time-programmable hardware bits that cannot be overwritten after they are burned. Even with full physical access, the attacker cannot replace the stored public key. This is the security rationale for eFuse-based key storage.

---

### Question 5

Which OWASP IoT Top 10 category is most directly represented by an IoT device that ships with UART debug output enabled, JTAG accessible, and verbose HTTP error responses that include file paths and stack traces from the embedded web server?

- A) OWASP IoT #2 (Insecure Network Services) — JTAG and UART are additional network services that the device exposes beyond its primary function.
- B) OWASP IoT #9 (Insecure Default Settings) — the device ships in a configuration that exposes debug interfaces and verbose output by default, which should be disabled in production builds.
- C) OWASP IoT #3 (Insecure Ecosystem Interfaces) — the verbose HTTP error responses from the embedded web server constitute an insecure ecosystem interface.
- D) OWASP IoT #5 (Use of Insecure or Outdated Components) — the embedded web server generating verbose error responses is likely an outdated third-party component with known CVEs.
- **Correct Answer:** B) OWASP IoT #9 — Insecure Default Settings.
- **Distractor Analysis:**
  - *Why A is incorrect:* JTAG and UART are hardware debug interfaces that require physical access — they are not network services. OWASP IoT #2 refers to unnecessary software services exposed on the network interface (Telnet, FTP, unprotected HTTP management APIs).
  - *Why B is correct:* OWASP IoT #9 is specifically defined as devices that ship with insecure production configurations: debug interfaces enabled, verbose error output, permissive defaults. All three findings in the question — UART debug output, accessible JTAG, and stack trace leakage — are failures of production hardening that should be addressed by enforcing secure defaults in production firmware builds.
  - *Why C is incorrect:* While the verbose HTTP errors are an ecosystem interface concern, they are a *symptom* of insecure defaults, not a standalone OWASP #3 finding. OWASP #3 focuses on authentication and access control failures in the ecosystem interfaces (web UI, mobile app, cloud API), not on information leakage from error messages.
  - *Why D is incorrect:* Verbose error responses from an embedded web server may be a component behavior, but the question identifies that the behavior is enabled by default in the shipping firmware — this is a configuration failure (#9), not a component vulnerability (#5). If the web server had an unpatched CVE, that would be #5, but generating stack traces is not itself a CVE.

---

### Question 6

A team is designing an IoT thermostat for deployment in hospital patient rooms. The device collects ambient temperature readings every 30 seconds and transmits them to a cloud dashboard. The team is deciding between MQTT over TLS (port 8883) and plain HTTP POST to a cloud API (port 80). Which recommendation is correct, and what is the primary technical justification?

- A) Plain HTTP POST on port 80 is acceptable because temperature data is not personally identifiable information (PII) and does not require the same protections as financial or medical records.
- B) MQTT over TLS on port 8883 is required because the hospital environment places the device in a regulated context where all network communications involving medical-adjacent systems must be encrypted.
- C) MQTT over TLS on port 8883 is preferred because it prevents both passive eavesdropping (confidentiality) and active tampering with sensor readings in transit (integrity), and verifies the device is communicating with the intended backend (authentication).
- D) Plain HTTP POST on port 80 is more appropriate because IoT devices in hospital environments must prioritize reliability over security, and TLS handshake overhead may cause sensor readings to be delayed.
- **Correct Answer:** C) MQTT over TLS is preferred for confidentiality, integrity, and server authentication.
- **Distractor Analysis:**
  - *Why A is incorrect:* Temperature data in a patient room, when combined with timestamps and room identifiers, can reveal patient occupancy and behavioral patterns — potentially constituting protected health information under HIPAA. Beyond regulatory classification, the integrity argument stands independently: unencrypted data can be tampered with. A manipulated temperature reading could affect HVAC decisions in a medical environment.
  - *Why B is incorrect:* While the regulatory argument (HIPAA, NIST healthcare frameworks) is valid supporting context, the *primary technical justification* is the three security properties TLS provides — not the regulatory requirement. The question asks for the primary technical justification.
  - *Why C is correct:* TLS provides confidentiality (no passive eavesdropping), integrity (no silent modification), and server authentication (no man-in-the-middle). These three properties are the technical reasons to use TLS on any sensitive network communication, independent of regulatory context.
  - *Why D is incorrect:* TLS 1.3 handshake overhead is approximately 1–2 round trips and adds tens of milliseconds to connection establishment. For a device transmitting every 30 seconds, this overhead is completely negligible. The tradeoff argument is not valid at this transmission frequency.

---

### Question 7

What is the purpose of a Certificate Revocation List (CRL) in an IoT mutual TLS deployment, and under what circumstances should a device certificate be added to the CRL?

- A) The CRL lists all certificates currently in active use across the fleet, allowing the broker to verify that a connecting device's certificate has been registered in the provisioning system before accepting the connection.
- B) The CRL lists certificates that have been invalidated before their scheduled expiry date, and a device certificate should be added when the device is decommissioned, stolen, or suspected of compromise.
- C) The CRL is a performance optimization that caches recently verified certificates, reducing the computational overhead of repeated certificate chain verification for devices that reconnect frequently.
- D) The CRL lists certificates that are about to expire within the next 30 days, allowing the fleet management system to proactively trigger certificate renewal before connectivity is interrupted.
- **Correct Answer:** B) The CRL lists prematurely invalidated certificates; certificates are added on decommission, theft, or suspected compromise.
- **Distractor Analysis:**
  - *Why A is incorrect:* The CRL is not an allowlist of active devices — it is a denylist of revoked certificates. A certificate not on the CRL is allowed (if it is valid and chains to the trusted CA), regardless of whether it appears in any provisioning registry.
  - *Why B is correct:* X.509 certificates have an explicit expiry date (the `notAfter` field). When a certificate needs to be invalidated *before* that date — because the device was stolen, decommissioned, or its private key was compromised — the certificate serial number is added to the CRL. Any broker that checks the CRL before completing the TLS handshake will reject a connection from a device whose certificate appears on the list.
  - *Why C is incorrect:* The CRL has no caching or performance function. Certificate chain verification is performed by the TLS implementation, which has its own session resumption mechanisms entirely separate from CRL checking.
  - *Why D is incorrect:* Expiring certificates are handled by certificate renewal workflows, not the CRL. The CRL addresses only *premature* invalidation — certificates revoked before their scheduled expiry. An expired certificate is simply rejected because its `notAfter` date has passed, without reference to the CRL.

---

### Question 8

A device manufacturer generates a single ECDSA signing key pair and uses the same private key to sign firmware for all 5 million devices in their product line. A security researcher discovers the private key was inadvertently included in a public GitHub repository for 48 hours before being removed. What is the severity of this exposure, and what is the required remediation?

- A) Low severity — the exposed key only allows an attacker to create firmware that appears authentic on existing devices but cannot be used to sign certificates or authenticate to the cloud backend.
- B) Critical severity — the exposed private key allows any attacker to sign malicious firmware that all 5 million devices will accept as legitimate, and the only remediation is a forced firmware update to all devices that changes the trusted public key.
- C) Medium severity — the exposed key allows firmware signing for future OTA updates but does not affect devices that are currently running, since firmware verification only occurs at boot during an update.
- D) High severity — the exposed key must be rotated, but only devices that downloaded a firmware update during the 48-hour exposure window need to be remediated, since only those devices could have received signed malicious firmware.
- **Correct Answer:** B) Critical severity — all 5 million devices accept malicious firmware signed with the exposed key.
- **Distractor Analysis:**
  - *Why A is incorrect:* Understating the severity is dangerous here. The firmware signing key is the root of trust for code execution on the device. An attacker with the private key can sign any firmware — including firmware that disables security controls, creates a backdoor, joins a botnet, or exfiltrates data. This is the highest severity class of key compromise in embedded security.
  - *Why B is correct:* All 5 million devices store the corresponding public key as their firmware verification root of trust. They will accept any firmware signed with the compromised private key as legitimate. The required remediation is to push a signed firmware update (using the still-valid key, while it remains trusted) that installs a new trusted public key, then immediately retire the compromised key. This is extremely complex at 5 million devices and illustrates why signing key management is a critical security discipline.
  - *Why C is incorrect:* Firmware signature verification occurs at every boot and during every update. An attacker can deliver malicious firmware via any OTA path, and the device will verify and execute it. The claim that verification "only occurs during an update" misunderstands the secure boot model.
  - *Why D is incorrect:* The attack window is not limited to the 48 hours the key was exposed. Once the private key is known to an attacker, they can sign malicious firmware and deliver it at any future time — the key's exposure is permanent. The 48-hour window is irrelevant to ongoing risk.

---

### Question 9

An IoT engineer is configuring a Mosquitto MQTT broker to accept connections from devices using mutual TLS. After adding `require_certificate true` to the broker configuration, all existing devices that were previously connecting with username/password authentication can no longer connect. What is the correct explanation and resolution?

- A) The `require_certificate true` directive disables all authentication on port 8883, requiring devices to reconnect on the plaintext port 1883 with their original username and password credentials.
- B) With `require_certificate true`, the broker now requires all connecting clients to present a valid X.509 client certificate during the TLS handshake. Devices connecting without a client certificate will fail the TLS handshake, regardless of whether they provide a username and password. Resolution: provision client certificates for all devices.
- C) The `require_certificate true` directive causes the broker to require that the device's Common Name in the certificate exactly match the username field in the MQTT CONNECT packet, and the existing devices have not been updated to send matching usernames.
- D) The `require_certificate true` setting only takes effect after the broker is restarted with administrator privileges; the devices are failing because the privilege escalation was not performed correctly.
- **Correct Answer:** B) Devices without client certificates fail the TLS handshake; all devices must be provisioned with client certificates.
- **Distractor Analysis:**
  - *Why A is incorrect:* `require_certificate true` does not disable authentication or redirect traffic to the plaintext port. It adds an additional authentication requirement to the TLS-secured port. The plaintext port operates independently.
  - *Why B is correct:* Mutual TLS requires the client to present a certificate during the TLS handshake phase — before any MQTT-level communication (including CONNECT packets with username/password) occurs. If a device does not provide a certificate, the TLS handshake fails at the transport layer and no MQTT messages are exchanged. The migration to mTLS requires provisioning certificates to all devices before enabling the requirement on the broker.
  - *Why C is incorrect:* While some mTLS configurations use the certificate's Common Name as the MQTT client ID (`use_identity_as_username true`), the reason existing devices cannot connect is not a username mismatch — it is that they are not presenting any certificate at all. The TLS layer rejects them before they even send a CONNECT packet.
  - *Why D is incorrect:* Mosquitto processes its configuration at startup; the `require_certificate true` directive is active immediately when the broker starts (or restarts). There is no separate privilege escalation step required for this configuration setting.

---

### Question 10

Which combination of OWASP IoT Top 10 controls, if implemented together, most effectively addresses the risk that a fleet of deployed devices could be used as part of a botnet after being compromised through default credentials?

- A) OWASP IoT #6 (Insufficient Privacy Protection) and #7 (Insecure Data Transfer and Storage) — encrypting device data prevents botnets from using collected data for malicious purposes.
- B) OWASP IoT #1 (Weak Passwords), #4 (Lack of Secure Update Mechanism), and #8 (Lack of Device Management) — eliminating default credentials prevents initial compromise; OTA update capability enables rapid remediation; fleet management provides visibility to detect and isolate compromised devices.
- C) OWASP IoT #9 (Insecure Default Settings) and #10 (Lack of Physical Hardening) — disabling debug interfaces and physical ports ensures that botnet operators cannot access devices even if they obtain physical access to them.
- D) OWASP IoT #3 (Insecure Ecosystem Interfaces) and #5 (Use of Insecure or Outdated Components) — securing the mobile app and patching third-party libraries prevents the attack vectors that botnets typically use to propagate.
- **Correct Answer:** B) OWASP IoT #1, #4, and #8 together address prevention, remediation, and detection.
- **Distractor Analysis:**
  - *Why A is incorrect:* Privacy and data encryption controls (#6 and #7) do not prevent botnet infection — they limit what data a compromised device can expose. A botnet does not need to decrypt device data; it needs the device's network bandwidth and IP address for DDoS purposes.
  - *Why B is correct:* The three controls address the botnet lifecycle: #1 prevents initial compromise via default credentials (the Mirai attack vector); #4 enables rapid firmware patches to close vulnerabilities used for ongoing exploitation; #8 provides fleet visibility to detect anomalous outbound traffic indicating botnet activity and isolate affected devices before damage spreads.
  - *Why C is incorrect:* Physical hardening (#9, #10) controls are irrelevant to Mirai-style botnets that operate entirely over the network. Botnet operators do not need physical access to devices — they compromise them remotely.
  - *Why D is incorrect:* While securing ecosystem interfaces (#3) and patching components (#5) are good practices, they address secondary attack vectors. The primary botnet propagation vector for IoT devices is default credentials, which is addressed by #1. Without #1, #4, and #8 in combination, the botnet risk remains even if #3 and #5 are fully remediated.

---
