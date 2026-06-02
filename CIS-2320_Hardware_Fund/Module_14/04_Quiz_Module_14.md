# Quiz: Module 14 - Mobile Device Connectivity

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

---

### Question 1

Which port number is used for IMAP email retrieval over an SSL/TLS encrypted connection?

- A) Port 25
- B) Port 110
- C) Port 143
- D) Port 993

Correct Answer: D — Port 993

IMAP over SSL/TLS uses TCP port 993. Port 25 is the SMTP server-to-server relay port. Port 110 is unencrypted POP3. Port 143 is unencrypted IMAP — functionally the same protocol but transmits credentials in plaintext and is not appropriate for secure use.

---

### Question 2

Which of the following most accurately describes the difference between LTE and 5G cellular standards?

- A) LTE and 5G are both Wi-Fi standards regulated by IEEE 802.11; LTE operates at 2.4 GHz and 5G operates at 5 GHz, and both require a nearby wireless router.
- B) LTE delivers typical download speeds of 10 to 100 Mbps using licensed cellular spectrum; 5G extends this with three frequency tiers — sub-6 GHz, mid-band, and mmWave — requiring compatible device hardware for each tier.
- C) LTE and 5G are carrier service plan tiers; any device with an active SIM card can be upgraded to 5G speeds by switching to a higher-tier plan regardless of device hardware.
- D) LTE is a wired broadband standard used in enterprise data centers, while 5G is the fifth generation of Ethernet switching supporting 5 Gbps over Cat6a at 100 meters.

Correct Answer: B — LTE delivers typical download speeds of 10 to 100 Mbps using licensed cellular spectrum; 5G extends this with three frequency tiers requiring compatible device hardware.

Answer A is incorrect because LTE and 5G are cellular standards, not IEEE 802.11 Wi-Fi standards — "5G Wi-Fi" colloquially refers to the 5 GHz Wi-Fi band, which is completely unrelated to 5G cellular. Answer C is incorrect because cellular generation capability is determined by the device's physical radio hardware, not the carrier plan tier. Answer D is incorrect because LTE and 5G are wireless mobile standards with no relationship to Ethernet or data center wiring.

---

### Question 3

A user configures a mobile email app using IMAP and reports they can receive new messages but all outgoing messages fail to send. The incoming server settings have been verified as correct. What is the most likely cause?

- A) IMAP protocol does not permit outgoing email on mobile devices; the user must switch to POP3 to enable the send function.
- B) The outgoing SMTP server settings are misconfigured — the server address, port number, or authentication credentials are incorrect.
- C) The device's SIM card must be enabled for cellular data before SMTP transmission is permitted, even when connected to Wi-Fi.
- D) The phone's local storage is full, preventing the email app from queuing outgoing messages in its local cache folder.

Correct Answer: B — The outgoing SMTP server settings are misconfigured.

Incoming and outgoing email use separate server configurations. IMAP handles incoming mail; SMTP handles outgoing mail. A user who can receive but not send has a problem specifically with the SMTP configuration — verify the server address, port (587 with STARTTLS or 465 with SSL), and authentication credentials. Answer A is incorrect because IMAP vs POP3 choice affects only incoming retrieval, not outgoing sending. Answer C is incorrect because SMTP works over any active IP connection including Wi-Fi. Answer D is incorrect because SMTP failures present as connection or authentication errors, not storage errors.

---

### Question 4

A technician is setting up a corporate smartphone for a new employee. The device cannot connect to the office Wi-Fi even though the employee enters the correct password. The corporate network uses WPA2-Enterprise with 802.1X authentication. What is the correct resolution?

- A) The employee's smartphone model does not support WPA2-Enterprise; they must connect using a personal hotspot instead.
- B) The corporate IT department must add the employee's MAC address to the wireless controller allowlist before any new device can connect.
- C) WPA2-Enterprise requires per-user credentials — a corporate username and password via PEAP, or a digital certificate via EAP-TLS — not a shared passphrase.
- D) WPA2-Enterprise requires the device to connect via Ethernet first so wireless credentials can be pushed automatically.

Correct Answer: C — WPA2-Enterprise requires per-user credentials via PEAP or EAP-TLS, not a shared passphrase.

WPA2-Enterprise (802.1X) authenticates each user individually against a RADIUS server. There is no shared passphrase. A user who has only used WPA2-Personal at home will fail because they are entering a passphrase where individual credentials are required. Answer A is incorrect because modern smartphones universally support 802.1X. Answer B is incorrect because MAC filtering is an optional additional layer, not a standard 802.1X requirement. Answer D is incorrect because no prior wired connection is needed — credentials are configured directly on the device or pushed via MDM.

---

### Question 5

A user enables mobile hotspot on their smartphone and connects a laptop to it while traveling. Which technology does the smartphone use to share the cellular data connection, and what are two security considerations a technician should communicate?

- A) The phone uses Bluetooth tethering exclusively; Bluetooth has no encryption so the hotspot should only be used in private locations.
- B) The phone creates a Wi-Fi access point routing traffic through the cellular connection; the technician should advise a strong WPA2 or WPA3 passphrase and monitoring data usage against the metered plan.
- C) The phone uses NFC to share the cellular connection; range is limited to four centimeters and the connection drops when devices are moved apart.
- D) The phone bridges the cellular connection over USB only; USB tethering has no security concerns because traffic is encrypted end-to-end by the operating system.

Correct Answer: B — The phone creates a Wi-Fi access point; secure with WPA2/WPA3 and monitor metered data usage.

Mobile hotspot creates a Wi-Fi access point on the smartphone routing connected devices through its cellular data connection. WPA2 or WPA3 prevents unauthorized devices from joining. Cellular data plans are metered and hotspot traffic counts against the monthly allowance. Answer A is incorrect because Wi-Fi hotspot — not Bluetooth — is the standard method, and Bluetooth 4.1+ includes AES-128 encryption. Answer C is incorrect because NFC cannot sustain internet connection sharing bandwidth. Answer D is incorrect because USB tethering is one option among several, and it does not provide automatic end-to-end application-layer encryption.

---

### Question 6

A technician is identifying a USB connector on a cable. The connector is oval-shaped and symmetrical, approximately 8.4 mm wide, and can be inserted in either orientation. What type of connector is this?

- A) USB Type-A
- B) Micro-USB
- C) USB Type-C
- D) USB Type-B

Correct Answer: C — USB Type-C

USB Type-C is defined by its oval, symmetrical, reversible design — approximately 8.4 mm wide and 2.6 mm tall. The reversible insertion is the key distinguishing physical characteristic. USB Type-A is rectangular and not reversible. Micro-USB is a small asymmetrical trapezoid with a notched bottom profile. USB Type-B is a large square connector with beveled top corners found on printers.

---

### Question 7

A user purchases an external SSD advertised at 500 MB/s. The drive uses a USB-C cable and plugs into the laptop's USB-C port. Actual transfer speeds measure only 40 MB/s. Which explanation is most likely?

- A) USB-C cables have a 40 MB/s maximum speed regardless of host port specifications; faster speeds require a Thunderbolt cable with a different connector shape.
- B) The laptop's USB-C port operates at USB 2.0 speeds; the connector is USB-C in shape but the port protocol is USB 2.0, limiting throughput to approximately 60 MB/s theoretical maximum.
- C) The drive must be formatted as exFAT before USB-C achieves full speed; NTFS format caps USB-C throughput at 40 MB/s.
- D) A chipset driver update is required before speeds above 40 MB/s are available on USB-C ports.

Correct Answer: B — The laptop's USB-C port is USB 2.0 protocol; connector shape does not determine speed.

USB Type-C is a connector shape, not a speed specification. A USB-C port can carry USB 2.0, USB 3.x, or Thunderbolt depending on the host's implementation. A budget laptop may include USB-C ports wired at USB 2.0 speed. The 40 MB/s reading is consistent with USB 2.0's approximately 480 Mbps theoretical ceiling. Answer A is incorrect because USB-C cables do not have an inherent 40 MB/s cap — the port protocol sets the limit. Answer C is incorrect because file system format does not cap USB transfer speeds. Answer D is incorrect because the speed reading is characteristic of a USB 2.0 protocol constraint, not a driver issue.

---

### Question 8

Which Bluetooth profile is responsible for streaming high-quality stereo audio from a smartphone to a Bluetooth speaker?

- A) HFP (Hands-Free Profile)
- B) SPP (Serial Port Profile)
- C) A2DP (Advanced Audio Distribution Profile)
- D) HID (Human Interface Device Profile)

Correct Answer: C — A2DP (Advanced Audio Distribution Profile)

A2DP is the Bluetooth profile designed for unidirectional high-quality stereo audio streaming. It is used by Bluetooth speakers, headphones, and car audio systems when playing music from a connected phone. HFP handles two-way voice call audio for hands-free use — not stereo music. SPP creates a virtual serial data channel for industrial devices and barcode scanners. HID supports input devices such as keyboards and mice and has no audio capability.

---

### Question 9

A user's email is accessible on their work laptop but new messages received on the laptop do not appear on their phone, and messages deleted on the phone still appear on the laptop. Which email protocol is most likely configured, and what should the technician change?

- A) IMAP is configured, which causes each device to maintain an independent local copy; switching to POP3 will enable synchronization.
- B) POP3 is configured on one or both devices; POP3 downloads messages to a single device and does not synchronize state across devices. The technician should configure both devices to use IMAP.
- C) SMTP is configured for both incoming and outgoing mail; SMTP does not support folder synchronization and must be replaced with IMAP.
- D) The issue is a server storage quota problem; deletions do not propagate when the mailbox exceeds 80% capacity.

Correct Answer: B — POP3 is configured; both devices should be switched to IMAP.

POP3 downloads messages from the server — typically deleting them — and stores them only on the downloading device. Actions on one device are not reflected elsewhere. IMAP keeps messages on the server and synchronizes state (read, deleted, folder) across all connected devices. Answer A is incorrect because IMAP is the solution — if IMAP were correctly configured on both devices, they would synchronize. Answer C is incorrect because SMTP is an outgoing-only protocol and cannot be configured for incoming mail. Answer D is incorrect because quota issues produce delivery failures and bounce messages, not cross-device synchronization divergence.

---

### Question 10

A technician needs to configure a corporate iPhone to receive email from the company mail server with messages synchronized across all of the employee's devices. Which incoming mail protocol and encrypted port is correct?

- A) POP3 on port 995 with SSL/TLS
- B) SMTP on port 587 with STARTTLS
- C) IMAP on port 993 with SSL/TLS
- D) POP3 on port 110 with no encryption

Correct Answer: C — IMAP on port 993 with SSL/TLS

IMAP on port 993 keeps messages on the server and synchronizes state across all devices — the correct choice for a multi-device corporate deployment. Port 993 is the encrypted IMAP port required for security compliance. Answer A is incorrect because POP3 downloads and removes messages, preventing multi-device synchronization. Answer B is incorrect because SMTP port 587 is the outgoing mail submission port — it cannot retrieve incoming messages. Answer D is incorrect because port 110 is unencrypted POP3 — wrong protocol and no encryption, both unacceptable for corporate use.
