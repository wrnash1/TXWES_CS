# Reading Guide: Module 14 - Mobile Device Connectivity

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

---

### Introduction

Welcome to Module 14 — Mobile Device Connectivity. This module covers how smartphones, tablets, and other mobile devices connect to wireless networks, cellular infrastructure, and corporate systems. You will learn Bluetooth pairing procedures, cellular technology generations (3G, 4G LTE, and 5G), Wi-Fi profile management including enterprise authentication, USB connector types and their speed ratings, and the email server settings a technician must configure when setting up mobile email clients. These topics appear on the CompTIA A+ Core 1 (220-1101) exam under Domain 1.3 and on Core 2 (220-1102) under Domain 1.3 as well.

As a field technician, you will configure email on mobile devices using the correct protocol and port, troubleshoot Bluetooth pairing failures, and explain the difference between cellular data standards to clients and managers. Complete the study checklist and review all glossary terms before attempting the lab.

---

### Section 1: Bluetooth Technology and Pairing

Bluetooth is a short-range wireless communication standard defined by the Bluetooth Special Interest Group (Bluetooth SIG). It operates in the 2.4 GHz ISM (Industrial, Scientific, and Medical) band, which is unlicensed spectrum shared with Wi-Fi 802.11b/g/n and other devices. Because multiple technologies share this band, interference is possible and Bluetooth uses frequency-hopping spread spectrum (FHSS) — rapidly changing frequencies up to 1,600 times per second — to minimize interference impact.

**Bluetooth Class and Range:**
Consumer Bluetooth devices are typically Class 2, with a range of approximately 10 meters. Class 1 devices, used in industrial and specialized applications, can reach up to 100 meters. Bluetooth 5.0 (released 2016) and later versions extended the Class 2 range to approximately 40 meters and doubled data throughput compared to Bluetooth 4.2.

**The Pairing Process:**
Pairing is how two Bluetooth devices exchange a shared secret key to form a trusted bond. Before pairing, a device must be in discoverable mode, making it visible to nearby Bluetooth scans. The modern pairing standard is SSP (Secure Simple Pairing), which uses one of four association models depending on device capabilities:

- Numeric Comparison — a six-digit number displays on both devices and the user confirms they match. Used between two devices that both have displays.
- Passkey Entry — one device displays a code and the user types it into the other. Used when only one device has a display.
- Just Works — pairing occurs without any user confirmation. Used for devices with no display or input, such as Bluetooth headsets. Provides the least security.
- Out of Band (OOB) — pairing data is exchanged through a separate channel such as NFC. Common in tap-to-pair implementations.

**Bluetooth Profiles:**
A Bluetooth profile defines the specific functions and protocols for a particular use case. Devices must share a common profile to use that function. The profiles tested on the CompTIA A+ exam are:

- A2DP (Advanced Audio Distribution Profile) — stereo audio streaming to headphones and speakers.
- HFP (Hands-Free Profile) — phone calls through car audio systems and headsets.
- HID (Human Interface Device Profile) — keyboards, mice, and game controllers.
- SPP (Serial Port Profile) — virtual serial port for data transfer, used in barcode scanners and some industrial devices.
- PBAP (Phone Book Access Profile) — allows a car audio system to access the phone's contact list for caller ID display.

**Troubleshooting Bluetooth Pairing:**
Common pairing failure causes in order of frequency: (1) the peripheral is not in active pairing mode — many devices require a specific button sequence to enter pairing mode and do not enter it automatically on power-up; (2) one device is already connected to another device — most Bluetooth peripherals maintain only one active connection; (3) a stale saved pairing record is corrupted — solution is to delete the saved pairing on both devices and re-pair from scratch; (4) interference from other 2.4 GHz devices (microwave ovens, baby monitors, dense Wi-Fi deployments) reducing signal quality.

---

### Section 2: Cellular Data Generations

**3G (Third Generation):**
3G cellular introduced practical mobile internet access. The primary 3G standard in the United States was HSPA+ (Evolved High-Speed Packet Access), capable of theoretical download speeds up to 21 Mbps, with typical real-world speeds of 1 to 10 Mbps. 3G networks in the United States were largely decommissioned in 2022 (AT&T in February, T-Mobile in July, Verizon in December). A device with a 3G-only radio lost connectivity after decommissioning.

**4G LTE (Long Term Evolution):**
LTE is the current mainstream cellular data standard. It uses OFDMA (Orthogonal Frequency Division Multiple Access) for efficient spectrum use and supports MIMO antenna configurations for higher throughput. Typical download speeds range from 10 Mbps in congested areas to 100 Mbps or more in favorable conditions. LTE Advanced (LTE-A) supports carrier aggregation — combining multiple spectrum bands — for theoretical peak speeds over 300 Mbps.

Devices authenticate to the LTE network using a SIM card (Subscriber Identity Module). Modern devices use a nano-SIM, the smallest standardized physical SIM form factor. eSIM (embedded SIM) is a programmable SIM built into the device that can be provisioned remotely by the carrier without a physical card swap.

**5G (Fifth Generation):**
5G is deployed in three frequency tiers with fundamentally different performance characteristics:

- Low-band 5G (sub-1 GHz) — similar coverage to 4G LTE towers, moderate speed improvement. Broad rural and suburban coverage.
- Mid-band 5G (1 GHz to 6 GHz, commonly called "sub-6 GHz") — best balance of speed and coverage. Typical speeds of 100 to 400 Mbps.
- mmWave 5G (24 GHz and above) — extremely high speeds (500 Mbps to over 1 Gbps) but very limited range (hundreds of meters) and cannot penetrate walls or glass. Deployed primarily in dense urban venues, stadiums, and convention centers.

A device's 5G capability is determined by its hardware radio chipset. Purchasing a higher carrier plan tier does not add 5G capability to a device with an LTE-only radio.

---

### Section 3: Wi-Fi Standards and Corporate Wireless Authentication

**IEEE 802.11 Standards Summary:**

- 802.11b — 2.4 GHz, maximum 11 Mbps, legacy.
- 802.11g — 2.4 GHz, maximum 54 Mbps, backward compatible with 802.11b.
- 802.11n (Wi-Fi 4) — 2.4 GHz and 5 GHz dual-band, MIMO support, up to 600 Mbps theoretical.
- 802.11ac (Wi-Fi 5) — 5 GHz only, MU-MIMO (multi-user MIMO), up to several Gbps theoretical. The most deployed enterprise standard as of 2024.
- 802.11ax (Wi-Fi 6) — 2.4 GHz and 5 GHz, adds OFDMA and BSS coloring for dense environments. Wi-Fi 6E extends to the 6 GHz band.

**Wi-Fi Security Standards:**
WEP (Wired Equivalent Privacy) is completely broken and must never be used. WPA (Wi-Fi Protected Access) improved security but has known vulnerabilities. WPA2 uses AES-CCMP encryption and is the current baseline standard. WPA3 adds SAE (Simultaneous Authentication of Equals) handshake, replacing the PSK handshake, and is required for Wi-Fi 6 certification.

**WPA2-Personal vs WPA2-Enterprise:**
WPA2-Personal (also called WPA2-PSK) uses a single pre-shared key (passphrase) shared by all users. Anyone who knows the passphrase can connect. WPA2-Enterprise uses 802.1X authentication, where each user authenticates with unique credentials — typically a corporate username and password via PEAP (Protected EAP) protocol, or a digital certificate via EAP-TLS. The credentials are validated against a RADIUS server on the corporate network. Enterprise Wi-Fi is standard in corporate environments because it provides per-user access control, accountability, and the ability to revoke individual access without changing the network key.

**MDM Wi-Fi Profile Deployment:**
Mobile Device Management (MDM) software allows IT administrators to push Wi-Fi profiles to managed devices silently. The pushed profile contains the SSID, security type, and authentication credentials or certificate — users do not need to enter anything manually. This is the standard method for onboarding corporate devices to enterprise Wi-Fi.

---

### Section 4: USB Connector Types and Mobile Synchronization

**USB Connector Type Identification:**

- USB Type-A — rectangular connector, approximately 12 mm x 4.5 mm. The standard host-side connector on desktop computers, laptops, chargers, and hubs. Used for connecting peripherals to hosts.
- USB Type-B — square connector with beveled top corners, approximately 8 mm x 8 mm. Found on printers, scanners, and external hard drive docks. Plugs into the peripheral device.
- Mini-USB — a smaller, trapezoidal connector, largely replaced by Micro-USB. Occasionally found on older cameras and GPS devices.
- Micro-USB — smaller trapezoidal connector with an asymmetrical notched bottom. Standard on Android devices from approximately 2010 to 2018. Still used on budget devices and some accessories.
- USB Type-C — oval symmetrical connector, 8.4 mm x 2.6 mm. Reversible — can be inserted either orientation. Standard on all modern Android flagships, most laptops (including MacBooks), Nintendo Switch, and many peripherals.
- Lightning — Apple's proprietary 8-pin connector with a flat symmetrical profile. Used on iPhones through iPhone 14 and iPads not yet transitioned to USB-C. Carries USB 2.0 data speeds natively.

**Critical Exam Point — USB Type-C is a Connector Shape, Not a Speed:**
The USB Type-C connector is physically identical regardless of the underlying protocol. A USB Type-C port may carry USB 2.0 (480 Mbps), USB 3.2 Gen 1 (5 Gbps), USB 3.2 Gen 2 (10 Gbps), USB 3.2 Gen 2x2 (20 Gbps), or Thunderbolt 3/4 (40 Gbps). The host port's published specification — not the connector shape — determines maximum speed. Always check the specification, not just the connector.

**USB Speed Versions:**

- USB 2.0 — 480 Mbps
- USB 3.0 / USB 3.2 Gen 1 — 5 Gbps
- USB 3.1 Gen 2 / USB 3.2 Gen 2 — 10 Gbps
- USB 3.2 Gen 2x2 — 20 Gbps
- Thunderbolt 3 and Thunderbolt 4 (USB-C connector) — 40 Gbps

**Mobile Synchronization Methods:**
MTP (Media Transfer Protocol) — the standard file transfer protocol for Android devices connected to a Windows PC via USB. Allows browsing and transferring files without requiring full disk access. ADB (Android Debug Bridge) — a developer command-line tool for Android devices that enables shell access, app installation, log retrieval, and advanced diagnostics over USB or Wi-Fi. iTunes and Finder — the macOS and Windows applications used to sync and backup iOS devices. Finder replaced iTunes for device management in macOS Catalina (2019).

---

### Section 5: Email Server Settings and Port Numbers

A mobile email client requires two separate server configurations: one for incoming mail (receiving) and one for outgoing mail (sending). These are independent settings and must each be configured correctly.

**IMAP — Internet Message Access Protocol:**
IMAP is the modern standard for receiving email. The defining characteristic of IMAP is that messages remain on the server; the client synchronizes a local copy. Changes made on any device (read, deleted, moved) are reflected on all other devices synced to the same account. This makes IMAP the correct choice for any user who accesses email on more than one device.

- IMAP plain text port: 143
- IMAP SSL/TLS port: 993

**POP3 — Post Office Protocol version 3:**
POP3 is the older standard for receiving email. POP3 downloads messages from the server and by default deletes them from the server after download. The result is that email exists only on the one device that downloaded it. Modern POP3 implementations offer an option to leave mail on the server, but synchronization between devices is not supported. POP3 is appropriate only for single-device configurations.

- POP3 plain text port: 110
- POP3 SSL/TLS port: 995

**SMTP — Simple Mail Transfer Protocol:**
SMTP is the protocol used exclusively for sending (outgoing) email. It is used both for client-to-server submission and server-to-server relay.

- SMTP port 25 — server-to-server relay. Most ISPs block outbound port 25 from end-user connections to prevent spam relay.
- SMTP port 587 — client submission with STARTTLS (opportunistic encryption upgrade). The standard port for email apps to submit outgoing mail to a mail server.
- SMTP port 465 — SMTPS (SMTP over SSL). An older implementation still supported by many providers.

**Email Port Summary Table:**

| Protocol | Function | Plain Port | Encrypted Port |
|----------|----------|------------|----------------|
| IMAP | Receive (sync) | 143 | 993 (SSL/TLS) |
| POP3 | Receive (download) | 110 | 995 (SSL/TLS) |
| SMTP | Send | 25 (server relay) | 587 (STARTTLS), 465 (SSL) |

**Scenario-Based Exam Application:**
If a user can receive email but cannot send: the SMTP configuration is wrong. Check the outgoing server address, port (try 587 first, then 465), and authentication credentials. If a user cannot receive email: the IMAP or POP3 incoming server configuration is wrong. Check the incoming server address, port (993 for IMAP SSL or 995 for POP3 SSL), and credentials.

---

### Section 6: Mobile Hotspot and Tethering

A mobile hotspot converts a smartphone's cellular data connection into a Wi-Fi access point that other devices can connect to. The phone acts as a wireless router, sharing its cellular internet connection. Hotspot security should always be set to WPA2 or WPA3 with a strong passphrase. Using an open hotspot in a public location allows any nearby device to join without authorization.

Tethering is the general term for sharing a phone's internet connection, and includes three methods. Wi-Fi hotspot is the most common and allows multiple devices to connect simultaneously. USB tethering shares the cellular connection via a USB cable to a single connected computer, which is useful when Wi-Fi is unavailable or unreliable. Bluetooth tethering shares the connection via Bluetooth and is slower but uses less power than Wi-Fi hotspot.

A technician advising a user about hotspot use must communicate that cellular data plans are metered — all hotspot traffic counts against the device's monthly data allowance, and overage charges can be significant.

---

### Section 7: Certification Exam Tips

Tip 1 — Domain 1.3 port numbers are frequently tested. The exam presents scenario questions describing a specific symptom (can receive but not send, or the reverse) and asks which protocol and port is involved. Memorize all six port numbers: IMAP 143/993, POP3 110/995, SMTP 25/587/465.

Tip 2 — "5G Wi-Fi" is a colloquial phrase for the 5 GHz Wi-Fi band. On the A+ exam, 5G always refers to fifth-generation cellular technology. The 5 GHz Wi-Fi band is part of the 802.11ac or 802.11ax standard. Never confuse these on an exam question.

Tip 3 — USB Type-C connector shape does not specify speed. The exam presents scenarios with a USB-C device and asks why speeds are lower than expected. The answer involves the host port's USB version specification, not the cable or connector shape.

Tip 4 — WPA2-Enterprise with 802.1X is not configured with a simple passphrase. An exam scenario describing a user who cannot connect to corporate Wi-Fi by entering their home network password requires the answer involving 802.1X credentials or certificate configuration, not a hardware or compatibility issue.

Tip 5 — Bluetooth pairing failure on the exam almost always traces to the peripheral not being in active pairing mode, or one device already being bonded to another. The exam avoids hardware failure as the first answer choice for pairing problems.

Tip 6 — SIM cards authenticate a device to the carrier network, but upgrading the SIM does not change cellular generation capability. Hardware radio determines the highest generation the device supports.

Tip 7 — IMAP leaves mail on the server; POP3 removes it. In an exam scenario where a user checks email on three devices and notices email on one device doesn't appear on the others, the answer is that POP3 is configured instead of IMAP.

Tip 8 — MDM (Mobile Device Management) is the mechanism IT administrators use to push Wi-Fi profiles, email settings, certificates, and security policies to corporate mobile devices without requiring user configuration. Expect at least one MDM-related scenario on the A+ exam.

---

### Required Readings and Videos

Complete the following before attempting the lab:

- Required Reading: Review the mobile device connectivity sections in Professor Messer's CompTIA A+ study notes at professormesser.com. Navigate to the 220-1101 materials and read the sections covering Bluetooth profiles and pairing, cellular data generations, Wi-Fi security standards, USB connector types, and email protocol port numbers.
- Required Video: Watch the mobile device connectivity video segments in Professor Messer's CompTIA A+ 220-1101 course at professormesser.com. Focus on the sections covering email protocol ports, Bluetooth pairing procedures, and 5G versus LTE differences.

---

### Study Checklist

- [ ] Define Bluetooth pairing and list the four SSP association models.
- [ ] Name four Bluetooth profiles and their functions (A2DP, HFP, HID, SPP).
- [ ] State the typical speed range for 3G, 4G LTE, and each tier of 5G.
- [ ] Explain why inserting a SIM card does not upgrade a device to 5G.
- [ ] Identify USB Type-A, Type-B, Micro-USB, Type-C, and Lightning connectors by description.
- [ ] Explain why USB Type-C connector shape does not determine transfer speed.
- [ ] State the plain text and encrypted port numbers for IMAP, POP3, and SMTP.
- [ ] Describe the difference between IMAP and POP3 message storage behavior.
- [ ] Explain the difference between WPA2-Personal and WPA2-Enterprise authentication.
- [ ] Describe what MDM software does and why IT departments use it for mobile devices.
- [ ] Complete the Module 14 lab activity.
