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

### Question 11

A security auditor scans an IoT device's firmware binary using `binwalk` and extracts a hardcoded string `"mqtt_user:sup3rS3cr3t"` from the binary. The same credential appears in all 80,000 devices shipped by the manufacturer. Which OWASP IoT category does this represent, and what is the correct remediation?

- A) OWASP IoT #7 (Insecure Data Transfer and Storage) — the credential is stored in firmware flash rather than transmitted securely; it should be encrypted using AES-128 before being embedded in the binary.
- B) OWASP IoT #1 (Weak, Guessable, or Hardcoded Passwords) — the credential is embedded identically in all devices; the remediation is to provision unique per-device credentials during manufacturing and store them in a protected NVS partition rather than in the firmware image.
- C) OWASP IoT #5 (Use of Insecure or Outdated Components) — the credential suggests the MQTT library being used requires hardcoded authentication and should be replaced with a library that supports certificate-based authentication.
- D) OWASP IoT #3 (Insecure Ecosystem Interfaces) — the MQTT broker accepts a shared password instead of requiring individual device certificates, making the broker itself the primary security failure.
- **Correct Answer:** B) OWASP IoT #1 — hardcoded identical credentials in firmware; remediate with per-device unique credentials in protected NVS.
- **Distractor Analysis:**
  - *Why A is incorrect:* Encrypting the credential in firmware with a hardcoded AES key provides no meaningful protection — an attacker who can read the binary can also read the key and decrypt the credential. The root problem is that the credential is shared across all devices, not that it is stored in flash.
  - *Why B is correct:* A credential embedded in a firmware binary is accessible to anyone who can extract the binary from any device in the fleet. Because all 80,000 devices share the same credential, a single extraction compromises the entire fleet's MQTT authentication. OWASP #1 covers this exact scenario — hardcoded credentials — and the remediation is unique credentials per device stored in protected, non-firmware storage.
  - *Why C is incorrect:* The MQTT library is not the cause of the vulnerability. The engineering decision to embed a credential in source code (or link it into the binary) is the failure, regardless of which library is used.
  - *Why D is incorrect:* While migrating to certificate-based authentication is a best-practice improvement, the identified vulnerability is the shared hardcoded credential in firmware — which is OWASP #1. The broker's acceptance of passwords is a separate design decision, not the finding.

---

### Question 12

During a TLS 1.3 handshake between an ESP32 device and a cloud MQTT broker, what is the purpose of the ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) key exchange, and which security property does it provide that earlier RSA key exchange in TLS 1.2 did not?

- A) ECDHE provides mutual authentication — both the device and the broker prove their identities to each other using their long-term ECDHE private keys, which is an improvement over RSA key exchange that only authenticated the server.
- B) ECDHE establishes an ephemeral shared secret for the session symmetric key, providing forward secrecy — even if the server's long-term private key is later compromised, previously recorded sessions cannot be decrypted.
- C) ECDHE provides data integrity by signing each MQTT packet payload with an ephemeral ECDSA key, ensuring that individual messages cannot be tampered with in transit after the handshake.
- D) ECDHE replaces the need for X.509 certificates entirely in TLS 1.3, because both parties authenticate using their ephemeral public keys rather than CA-signed certificates.
- **Correct Answer:** B) ECDHE provides forward secrecy — past sessions cannot be decrypted even if the server's long-term key is later compromised.
- **Distractor Analysis:**
  - *Why A is incorrect:* ECDHE is a key agreement algorithm, not an authentication mechanism. Authentication in TLS is performed separately by the certificate and its signature. ECDHE key pairs are ephemeral (generated fresh per session) and are not used as long-term identity keys.
  - *Why B is correct:* In older RSA key exchange (TLS 1.2 with RSA cipher suites), the client encrypted the pre-master secret using the server's long-term RSA public key. An attacker who recorded the session and later obtained the RSA private key could retroactively decrypt all recorded sessions. ECDHE generates a fresh key pair per session; the session key is never transmitted, only derived. Compromising the server's long-term certificate key after the session cannot reconstruct the ephemeral ECDHE shared secret.
  - *Why C is incorrect:* ECDHE does not sign individual packets. Per-packet integrity is provided by the AEAD cipher (AES-128-GCM or ChaCha20-Poly1305) that is established using the session keys derived from the ECDHE handshake.
  - *Why D is incorrect:* TLS 1.3 still uses X.509 certificates for server (and optionally client) authentication. ECDHE handles key exchange; certificates handle authentication. These are distinct functions in the protocol.

---

### Question 13

An IoT device fleet uses OWASP IoT #5 mitigation: the firmware build system generates an SBOM (Software Bill of Materials) that lists every third-party library with its version. The SBOM reveals that the fleet's MQTT stack includes mbedTLS 2.16.0. A newly published CVE assigns a CVSS score of 9.8 to a heap buffer overflow in mbedTLS versions before 2.28.0. Which response is correct?

- A) No action is required immediately — CVEs with CVSS scores below 10.0 are not critical and can be addressed in the next planned firmware release cycle, typically 12–18 months.
- B) The team should update the mbedTLS library to version 2.28.0 or later, rebuild firmware with the updated component, sign the new binary, and deploy it to the fleet via OTA update with staged rollout, prioritizing the update based on the critical CVSS score.
- C) The team should add a firewall rule at the network perimeter blocking all traffic to the affected devices until the library vendor patches the vulnerability, avoiding the complexity of an OTA update campaign.
- D) The SBOM confirms which devices are affected, but mbedTLS is embedded in the chip's ROM and cannot be updated — the only option is to replace the physical hardware across the fleet.
- **Correct Answer:** B) Update mbedTLS, rebuild and sign firmware, deploy via staged OTA update.
- **Distractor Analysis:**
  - *Why A is incorrect:* CVSS 9.8 is a Critical severity score — one step below the maximum 10.0. A heap buffer overflow at this severity level typically allows remote code execution, meaning an attacker can take full control of affected devices over the network. A 12–18 month response time is unacceptable for a Critical-severity vulnerability; incident response policy should define a maximum time-to-patch for Critical CVEs (typically 30 days or less).
  - *Why B is correct:* The SBOM identifies the exact component and version. The fix is to upgrade the dependency, rebuild, sign the new firmware with the ECDSA signing key, and deploy via OTA with a staged rollout (canary → pilot → GA) to detect regressions before full fleet exposure. This is the complete lifecycle response that OWASP #4 (secure update mechanism) and #5 (component management) are designed to enable.
  - *Why C is incorrect:* A network perimeter block may reduce immediate exposure but does not fix the vulnerability. Devices inside the perimeter, or devices that connect via the blocked firewall rule for legitimate purposes, remain at risk. Firewall blocking is a temporary containment measure, not a remediation.
  - *Why D is incorrect:* mbedTLS is a software library compiled into the firmware image, not part of the chip's ROM. The ESP32 ROM contains only the first-stage bootloader; all application code, including TLS libraries, lives in updatable flash.

---

### Question 14

A smart meter transmits electricity usage readings every 15 minutes over MQTT. The device's developer argues that since electricity usage data is "just numbers" it does not need to be encrypted. Which OWASP IoT category directly contradicts this argument, and why?

- A) OWASP IoT #2 (Insecure Network Services) — transmitting readings in cleartext constitutes an insecure network service that should be secured or disabled.
- B) OWASP IoT #6 (Insufficient Privacy Protection) — granular electricity usage data reveals occupancy patterns, sleep schedules, and appliance use, and transmitting it in cleartext violates user privacy by allowing passive eavesdroppers to infer sensitive behavioral information.
- C) OWASP IoT #4 (Lack of Secure Update Mechanism) — without encrypted transport, OTA firmware updates delivered to the meter could also be intercepted, enabling firmware injection attacks.
- D) OWASP IoT #8 (Lack of Device Management) — unencrypted readings cannot be authenticated against the device registry, so a malicious actor could inject false readings into the metering system.
- **Correct Answer:** B) OWASP IoT #6 — granular usage data reveals behavioral patterns and requires encryption to protect user privacy.
- **Distractor Analysis:**
  - *Why A is incorrect:* OWASP #2 addresses services that are unnecessary or that lack authentication controls. Electricity usage reporting is a necessary, intended service; the concern is whether its transport is protected, which is addressed by #6 and #7, not #2.
  - *Why B is correct:* OWASP #6 specifically addresses the collection and transmission of data that is sensitive to user privacy. Research in smart meter privacy has demonstrated that 15-minute interval readings can identify when occupants wake up, when they go to sleep, which appliances are used, and even TV program selections based on power draw patterns. Transmitting this data in cleartext enables passive surveillance by any party that can observe the network path.
  - *Why C is incorrect:* While an unencrypted transport would also affect OTA update security (OWASP #4), the question asks specifically about usage data and the argument that it does not need encryption. OWASP #4 is about the update mechanism, not the telemetry data stream.
  - *Why D is incorrect:* OWASP #8 addresses device registry management and lifecycle tracking, not the integrity of data payloads in transit. Data integrity in transit is addressed by OWASP #7 (insecure data transfer).

---

### Question 15

A penetration tester connects a USB-to-UART adapter to exposed pads on an IoT gateway's PCB, establishes a serial console at 115200 baud, and receives a Linux root shell without entering any credentials. The gateway is deployed in a publicly accessible server room. Which OWASP IoT category is the primary finding, and what is the correct remediation?

- A) OWASP IoT #2 (Insecure Network Services) — the UART console is an additional service that should be disabled or protected with authentication, similar to how Telnet or FTP network services are restricted.
- B) OWASP IoT #10 (Lack of Physical Hardening) — the UART debug interface is physically accessible without authentication; the remediation is to disable the UART console in the production kernel configuration and apply tamper-evident seals or mechanical controls to the PCB.
- C) OWASP IoT #9 (Insecure Default Settings) — the root shell access without credentials is a default setting that should have been disabled before production deployment by requiring a console password.
- D) OWASP IoT #1 (Weak Passwords) — the root account has no password set, which is a variant of a blank or default password vulnerability.
- **Correct Answer:** B) OWASP IoT #10 — lack of physical hardening; disable UART in production and apply physical access controls.
- **Distractor Analysis:**
  - *Why A is incorrect:* UART is a physical hardware interface, not a network service. OWASP #2 applies to services exposed on the network stack — Telnet, HTTP, FTP running over IP. A UART console requires physical proximity and connecting hardware to the device's circuit board.
  - *Why B is correct:* OWASP #10 (Lack of Physical Hardening) explicitly covers exposed UART/JTAG debug interfaces that provide unauthorized access to device internals when physical access is obtained. The finding — root shell via exposed UART pads in a publicly accessible location — is the canonical example of this category. Remediation includes disabling the console in the kernel configuration (removing `console=ttyS0` from boot arguments), desoldering or covering pads, and applying physical access controls to the deployment location.
  - *Why C is incorrect:* While a missing console password could be characterized as an insecure default setting (#9), the more specific and appropriate finding is #10 because the vulnerability requires physical access to exploit. The console should not be accessible at all in production, not merely password-protected — a password on a physically exposed console is still a weaker control than disabling the interface.
  - *Why D is incorrect:* OWASP #1 applies to authentication via network protocols where a password is part of the authentication exchange. A UART console that boots directly to a root shell may not even use password authentication — it may be configured as a serial console with auto-login, which is a hardware/configuration issue rather than a weak-password issue.

---

### Question 16

An IoT device uses PSK-TLS (Pre-Shared Key TLS) instead of certificate-based TLS for connecting to its MQTT broker. A security engineer flags this as a concern. What is the primary security disadvantage of PSK-TLS compared to certificate-based mutual TLS in a large IoT fleet?

- A) PSK-TLS uses weaker symmetric ciphers than certificate-based TLS and therefore provides less data confidentiality during transmission.
- B) PSK-TLS requires all devices to share the same pre-shared key, meaning that if any single device is compromised and its key is extracted, the attacker can impersonate any other device in the fleet — eliminating per-device identity.
- C) PSK-TLS does not support TLS 1.3, requiring devices to use the older TLS 1.2 protocol, which is susceptible to known vulnerabilities like BEAST and POODLE.
- D) PSK-TLS requires more computational resources than ECDSA certificate verification, making it unsuitable for resource-constrained microcontrollers.
- **Correct Answer:** B) PSK-TLS with a shared key eliminates per-device identity — one compromised device exposes the entire fleet.
- **Distractor Analysis:**
  - *Why A is incorrect:* PSK-TLS uses the same symmetric cipher suites (AES-128-GCM, ChaCha20) as certificate-based TLS. The key exchange and authentication mechanism differs, but the data encryption strength is equivalent.
  - *Why B is correct:* The defining limitation of PSK-TLS in IoT deployments is the scope of a single PSK compromise. If a shared PSK is used fleet-wide and is extracted from one device, the attacker can connect to the broker as any device and publish or subscribe to any topic that a legitimate device can access. Certificate-based mTLS provides per-device unique credentials — compromise of one device's private key has no impact on other devices.
  - *Why C is incorrect:* PSK cipher suites are defined in TLS 1.3 (RFC 8446 includes PSK handshake modes). PSK-TLS can and does work with TLS 1.3. BEAST and POODLE are vulnerabilities in specific TLS 1.0/1.1 cipher suites, not in PSK authentication.
  - *Why D is incorrect:* PSK-TLS is actually computationally cheaper than certificate-based TLS because it avoids asymmetric cryptographic operations (ECDSA signature verification, X.509 chain parsing). PSK handshakes use only symmetric operations. The concern with PSK is key management and blast radius, not computational load.

---

### Question 17

A device running an embedded web server for local configuration outputs the following HTTP response when a request is made to an invalid endpoint: `500 Internal Server Error — /opt/webserver/handlers/api_handler.c line 247: malloc failed`. What OWASP IoT category does this finding represent, and what is the specific risk the information exposes?

- A) OWASP IoT #5 (Use of Insecure or Outdated Components) — a `malloc` failure indicates the embedded C runtime is outdated and missing modern memory safety features.
- B) OWASP IoT #9 (Insecure Default Settings) — the verbose error response reveals the server-side source file path and line number, which assists an attacker in understanding the application's internal structure and targeting further attacks.
- C) OWASP IoT #7 (Insecure Data Transfer and Storage) — error messages that include internal paths are a form of sensitive data leakage over the network and should be encrypted.
- D) OWASP IoT #4 (Lack of Secure Update Mechanism) — a `malloc` failure indicates a memory allocation bug that could be exploited without a firmware update capability in place.
- **Correct Answer:** B) OWASP IoT #9 — verbose error messages in production reveal internal structure; they should be suppressed in production builds.
- **Distractor Analysis:**
  - *Why A is incorrect:* A `malloc` failure does not indicate an outdated runtime. It indicates a resource exhaustion or implementation bug. OWASP #5 applies when embedded third-party libraries have known published CVEs, not when an error occurs during runtime.
  - *Why B is correct:* OWASP #9 (Insecure Default Settings) covers verbose error output that is left enabled in production. The specific risk is information disclosure: the error response reveals the server's file system layout (`/opt/webserver/handlers/`), the source file name (`api_handler.c`), and the line number — details an attacker uses for targeted exploitation (e.g., identifying which handler processes a specific request path to craft a heap overflow).
  - *Why C is incorrect:* Encrypting the error response with TLS does not suppress the information — it just hides it from passive eavesdroppers. An authenticated attacker (or any attacker who completes the TLS handshake) still receives the verbose error. The fix is to suppress the verbose content, not encrypt it.
  - *Why D is incorrect:* A `malloc` failure is a runtime error; whether it can be exploited depends on how the code handles the failure, not on the presence or absence of an OTA update mechanism. OWASP #4 addresses the inability to push patches, not the existence of memory allocation bugs.

---

### Question 18

A firmware developer wants to implement forward secrecy for session keys on a TLS connection from an ESP32 to a cloud broker. Which cipher suite configuration achieves forward secrecy, and why?

- A) `TLS_RSA_WITH_AES_128_CBC_SHA` — RSA key exchange encrypts the session key with the server's long-term public key, ensuring session confidentiality even if the device's key is compromised.
- B) `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` — ECDHE generates an ephemeral key pair per session; the session key is derived from the ephemeral Diffie-Hellman shared secret rather than transmitted using the long-term key.
- C) `TLS_PSK_WITH_AES_128_CBC_SHA` — the pre-shared key is unique per device and never transmitted, providing forward secrecy by ensuring no key material is exchanged over the network.
- D) `TLS_ECDSA_WITH_AES_256_GCM_SHA384` — ECDSA signatures provide session key freshness by generating a new signature for each session, which is functionally equivalent to forward secrecy.
- **Correct Answer:** B) `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` achieves forward secrecy via ephemeral key exchange.
- **Distractor Analysis:**
  - *Why A is incorrect:* `TLS_RSA_WITH_AES_128_CBC_SHA` uses static RSA key exchange — the client encrypts the pre-master secret with the server's long-term RSA public key. An attacker who records the session and later obtains the server's private RSA key can decrypt all previously recorded sessions. This cipher suite explicitly lacks forward secrecy and is deprecated in TLS 1.3.
  - *Why B is correct:* The `ECDHE` prefix indicates Elliptic Curve Diffie-Hellman Ephemeral key exchange. Both parties generate fresh ephemeral key pairs for each session; the session key is derived from the shared secret computed from these ephemeral keys. The ephemeral private keys are discarded after the handshake. Compromise of the server's long-term ECDSA signing key (used for the certificate) does not allow retroactive decryption of recorded sessions because the session key was derived from ephemeral keys, not the long-term key.
  - *Why C is incorrect:* PSK-TLS with a static pre-shared key does not provide forward secrecy. If the PSK is compromised, all past and future sessions using that key can be decrypted. True forward secrecy requires ephemeral key material that is discarded after each session.
  - *Why D is incorrect:* ECDSA is a signature algorithm used for authentication, not key exchange. A cipher suite name `TLS_ECDSA_WITH_...` is not a valid TLS cipher suite name — ECDSA appears in cipher suites as the certificate/authentication component (e.g., `TLS_ECDHE_ECDSA_...`), not as the key exchange mechanism. Signature freshness is not the same as forward secrecy.

---

### Question 19

An IoT security engineer is reviewing an ESP32 production build. The build was compiled with `CONFIG_ESPTOOLPY_FLASHFREQ_80M=y` and `CONFIG_BOOTLOADER_LOG_LEVEL_NONE=y`, but `CONFIG_SECURE_BOOT_V2_ENABLED` is set to `n`. Which defense-in-depth layer is absent, and what is the specific attack it fails to prevent?

- A) Layer 2 (Transport Security) is absent — without secure boot, the TLS stack cannot verify the broker certificate during the handshake, exposing the device to man-in-the-middle attacks.
- B) Layer 1 (Device Hardening) is absent — without secure boot enabled, an attacker with physical access or OTA delivery capability can flash an unsigned firmware image that the bootloader will execute without verification.
- C) Layer 4 (Network Segmentation) is absent — secure boot is required to enforce VLAN membership rules on the device's network stack, and without it the device can be reconfigured to bypass segmentation.
- D) Layer 3 (Authentication) is absent — secure boot is required to protect the device certificate stored in NVS, and without it the certificate can be replaced with an attacker-controlled credential.
- **Correct Answer:** B) Layer 1 (Device Hardening) is absent — unsigned firmware can be executed because secure boot is not enabled.
- **Distractor Analysis:**
  - *Why A is incorrect:* Secure boot and TLS are independent controls. The TLS stack performs certificate verification based on the CA certificate stored in firmware — this operates regardless of whether secure boot is enabled. Secure boot protects against executing tampered firmware; it does not affect how the running firmware validates TLS certificates.
  - *Why B is correct:* In the defense-in-depth model, Layer 1 (Device Hardening) includes secure boot. Without `CONFIG_SECURE_BOOT_V2_ENABLED=y`, the ESP32 bootloader does not verify firmware signatures before execution. An attacker who can deliver a firmware image — whether through physical flash programming or a compromised OTA channel — can execute arbitrary code. This is the canonical Layer 1 failure.
  - *Why C is incorrect:* Secure boot has no role in enforcing VLAN membership or network segmentation. VLAN enforcement is a function of the network switch or firewall, not the endpoint device. Layer 4 controls are network infrastructure controls.
  - *Why D is incorrect:* While flash encryption (a separate ESP32 feature) protects NVS contents including certificates, secure boot specifically protects the code execution path — it verifies that the firmware binary is authentic before running it. Secure boot does not directly protect NVS contents; that is flash encryption's role.

---

### Question 20

A deployed fleet of 10,000 smart thermostats has no OTA update capability. A CVE is published disclosing a critical vulnerability in the devices' CoAP (Constrained Application Protocol) implementation that allows unauthenticated remote code execution. The vendor's only option is a physical recall. Which two OWASP IoT categories explain why this situation occurred, and which category would have prevented the physical recall?

- A) OWASP #1 (Weak Passwords) and #3 (Insecure Ecosystem Interfaces) — eliminating default credentials (#1) would have prevented exploitation, while securing the ecosystem interface (#3) would have made a recall unnecessary.
- B) OWASP #4 (Lack of Secure Update Mechanism) and #5 (Use of Insecure or Outdated Components) — the absence of OTA capability (#4) is why a recall is required, while the vulnerable CoAP library represents an insecure component (#5); implementing OTA capability would have allowed remote remediation.
- C) OWASP #8 (Lack of Device Management) and #9 (Insecure Default Settings) — a device registry would have tracked which devices are affected (#8), while better default settings (#9) would have disabled the CoAP interface by default.
- D) OWASP #6 (Insufficient Privacy Protection) and #10 (Lack of Physical Hardening) — the CoAP vulnerability exposes device data (#6) and the physical recall would not be necessary if the hardware were tamper-proof (#10).
- **Correct Answer:** B) OWASP #4 and #5 — the vulnerable CoAP library is an insecure component, and the absence of OTA capability forces a physical recall.
- **Distractor Analysis:**
  - *Why A is incorrect:* OWASP #1 is irrelevant here — the vulnerability is in the CoAP protocol implementation (a software library bug), not in authentication credentials. Changing passwords would not patch a code execution vulnerability in the CoAP parser.
  - *Why B is correct:* OWASP #5 explains the root cause: a vulnerable third-party component (CoAP library) was embedded in firmware without a process to update it when CVEs were published. OWASP #4 explains why remediation is now a physical recall rather than an OTA campaign: no update mechanism was designed into the device. If OTA capability had been included (OWASP #4 remediated), the vendor could push a patched CoAP library to all 10,000 devices without physical intervention.
  - *Why C is incorrect:* OWASP #8 (device management) would help identify which devices are affected, but it does not address the inability to update them. OWASP #9 (insecure default settings) might reduce attack surface by disabling CoAP by default, but it would not remove the vulnerability from deployed firmware. Neither #8 nor #9 explains why a physical recall is the only option.
  - *Why D is incorrect:* OWASP #6 (privacy protection) and #10 (physical hardening) are entirely unrelated to the described scenario. The vulnerability allows remote code execution over a network protocol — physical hardening would not prevent remote exploitation, and privacy protection is not the concern when the issue is code execution.
