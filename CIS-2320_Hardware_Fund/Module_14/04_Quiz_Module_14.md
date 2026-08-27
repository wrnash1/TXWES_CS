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

---

### Question 11

A user configures their smartphone to connect to corporate Wi-Fi. The IT policy requires WPA3 authentication with a unique certificate per device. The user's phone connects successfully, but after enrolling a second employee's identical phone model on the same network, the first user's phone is disconnected and cannot reconnect. What is most likely happening?

- A) WPA3 only supports one active client at a time; the second phone's enrollment replaced the first phone's session
- B) Both phones received the same IP address from the DHCP server because the DHCP pool only has one entry configured for the device model
- C) The certificate enrollment system issued the same certificate to both devices, causing an identity conflict; each device must receive a unique certificate tied to the user's identity, not the hardware model
- D) The 5 GHz band the access point uses can only support two devices simultaneously and both phones are competing for the single available connection slot

Correct Answer: C — Both devices received the same certificate, causing an authentication conflict.

Certificate-based WPA3 Enterprise (802.1X) authentication identifies each device by a unique certificate. If the enrollment system issued an identical certificate to both phones (a misconfiguration), the authentication server sees two clients with the same identity and may revoke or block one. Each device must receive a certificate tied to a unique identity (user account and/or device ID). Answer A is incorrect because WPA3 supports thousands of concurrent clients. Answer B is incorrect because IP address conflicts cause connectivity issues for both devices but do not cause the original device to be disconnected from authentication. Answer D is incorrect because 802.11 access points support tens to hundreds of simultaneous clients per radio band.

---

### Question 12

A company deploys MDM (Mobile Device Management) software on all employee smartphones. An employee loses their phone. Which MDM capability allows the IT administrator to protect corporate data on the lost device?

- A) Remote software update — pushing a firmware update to the lost device resets all authentication credentials stored in the secure enclave
- B) Remote wipe — the administrator can send a command through the MDM server that erases all data on the device, including corporate email, contacts, and documents
- C) Remote GPS tracking — the MDM server continuously broadcasts the device's GPS coordinates to the administrator, allowing physical retrieval within 24 hours
- D) Remote SIM lock — the MDM server contacts the carrier to lock the SIM card, which prevents the finder from making calls but leaves corporate data accessible to anyone who bypasses the lock screen

Correct Answer: B — Remote wipe allows the administrator to erase corporate data on the lost device.

Remote wipe is a core MDM feature that allows an administrator to issue an erase command to a device through the MDM server. When the device connects to any network, it receives the wipe command and erases its contents. This protects corporate data from unauthorized access. Answer A is incorrect because firmware updates do not erase user data or corporate documents. Answer C is incorrect because MDM GPS tracking provides location information but does not protect data — the device's data remains accessible until wiped. Answer D is incorrect because SIM lock prevents cellular calls but does not protect data stored on the device's internal storage; anyone who removes or bypasses the lock screen can access corporate data.

---

### Question 13

A user's Android phone is on a corporate network. The phone receives a VPN client profile pushed by the MDM system. Which of the following best describes the purpose of the VPN client on the mobile device?

- A) The VPN client replaces the phone's built-in cellular connection and provides a faster 5G signal by routing data through a corporate tower instead of the carrier network
- B) The VPN client creates an encrypted tunnel between the phone and the corporate network, allowing the device to securely access internal resources (file servers, intranet sites, corporate email) as if it were physically connected to the office LAN
- C) The VPN client is a backup Wi-Fi connection profile that activates automatically when the primary corporate Wi-Fi signal drops below -70 dBm
- D) The VPN client encrypts only outgoing email attachments over 1 MB; it does not encrypt other network traffic originating from the device

Correct Answer: B — The VPN client creates an encrypted tunnel to the corporate network for secure remote access.

A VPN (Virtual Private Network) client on a mobile device establishes an encrypted connection (tunnel) to a VPN concentrator at the corporate network perimeter. All traffic destined for internal resources travels through this encrypted tunnel, protecting data from interception on untrusted networks (public Wi-Fi, cellular). The device appears to be on the internal LAN from the network's perspective. Answer A is incorrect because a VPN does not replace the underlying cellular or Wi-Fi connection — it operates on top of the existing network connection. Answer C is incorrect because a VPN is not a Wi-Fi failover mechanism. Answer D is incorrect because a VPN encrypts all tunneled traffic at the IP packet level, not selectively by file size or type.

---

### Question 14

A technician is troubleshooting a smartphone that cannot connect to a 5 GHz Wi-Fi network. The phone connects successfully to the 2.4 GHz band from the same router. What is the most likely explanation?

- A) The phone's cellular data plan does not include Wi-Fi access on the 5 GHz band; a separate 5 GHz data plan must be purchased from the carrier
- B) The phone's Wi-Fi radio only supports 2.4 GHz (802.11b/g/n on 2.4 GHz only) and does not have a 5 GHz radio; this is a hardware limitation that cannot be resolved through software updates or settings changes
- C) The 5 GHz band is disabled by default on all smartphones and must be manually enabled through the carrier's APN settings
- D) The 5 GHz network requires WPA3 authentication while the phone only supports WPA2, preventing association despite the phone having a 5 GHz radio

Correct Answer: B — The phone's Wi-Fi adapter does not support the 5 GHz band.

Some budget or older smartphones include only a 2.4 GHz Wi-Fi radio (802.11b/g/n 2.4 GHz). These devices are physically incapable of connecting to 5 GHz networks because they lack the 5 GHz radio hardware. The fact that the phone connects normally on 2.4 GHz confirms the Wi-Fi adapter functions correctly — the limitation is the radio's frequency band support. This cannot be fixed with software updates or configuration changes. Answer A is incorrect because Wi-Fi connectivity is independent of cellular data plans and does not require carrier approval. Answer C is incorrect because 5 GHz support is a radio hardware capability, not an APN setting; APN settings configure cellular data, not Wi-Fi band selection. Answer D is incorrect because while WPA3 compatibility is a consideration, this scenario specifically states the 5 GHz band itself cannot be connected — if the radio were present but WPA3 were the issue, the phone would see the 5 GHz network but fail to authenticate.

---

### Question 15

A corporate mobile policy requires that employees' smartphones use S/MIME for email. What does S/MIME provide, and what is required on each device for it to function?

- A) S/MIME provides Wi-Fi encryption for email traffic only; it requires a Wi-Fi certificate installed through MDM
- B) S/MIME provides cryptographic signing and encryption of individual email messages using asymmetric key cryptography; it requires a personal digital certificate (containing the user's public key and signed by a trusted CA) to be installed on each device
- C) S/MIME is a mobile data compression standard that reduces email attachment size; it requires a compression algorithm license applied to the mail server
- D) S/MIME provides two-factor authentication for email login; it requires a hardware TOTP token to generate one-time codes for each email session

Correct Answer: B — S/MIME uses digital certificates to sign and encrypt individual email messages.

S/MIME (Secure/Multipurpose Internet Mail Extensions) is an email security standard that uses asymmetric cryptography to provide two services: digital signing (verifies the sender's identity and message integrity) and message encryption (encrypts message content using the recipient's public key). Each user requires a personal digital certificate issued by a trusted Certificate Authority and installed on their device. Answer A is incorrect because S/MIME operates at the message layer (encrypts the message content), not at the Wi-Fi transport layer. Answer C is incorrect because S/MIME is a cryptographic standard, not a compression standard. Answer D is incorrect because S/MIME provides message-level encryption and signing, not session-level login authentication — TOTP is a separate MFA mechanism.

---

### Question 16

A user reports that their smartphone's GPS navigation app shows their location as approximately 500 meters from their actual position even when the phone has a clear view of the sky. The phone's GPS fix appears after about 30 seconds. What is the most likely cause, and how can the user correct it?

- A) The phone's GPS radio is failing and must be replaced by a manufacturer-authorized technician; GPS accuracy below 100 meters is a hardware defect threshold
- B) The phone's A-GPS (Assisted GPS) data cache is stale or corrupted; clearing the GPS data cache or allowing the phone to download a fresh A-GPS almanac via cellular or Wi-Fi will restore accuracy
- C) The user is inside a building with a metal roof; GPS cannot achieve any accuracy indoors regardless of device settings or software updates
- D) The 500-meter error indicates the phone is using cellular tower triangulation instead of GPS; disabling cellular data will force the phone to switch to GPS-only mode and improve accuracy

Correct Answer: B — Stale A-GPS data is causing the initial position error; refreshing the A-GPS cache will correct it.

A-GPS (Assisted GPS) accelerates satellite acquisition and initial position accuracy by providing pre-downloaded satellite almanac data (ephemeris) to the receiver. When this data is old (typically more than a few days) or corrupted, the receiver takes longer to acquire satellites and may report an inaccurate initial position that corrects as more satellites are acquired. Clearing the GPS cache or refreshing the A-GPS almanac resolves this. Answer A is incorrect because a 500-meter initial error that corrects over time is consistent with stale A-GPS data, not hardware failure. Answer C is incorrect because the scenario states the user has a clear view of the sky, which implies an outdoor location. Answer D is incorrect because cellular tower triangulation (which is less accurate) is used as a fallback when GPS is unavailable — it does not compete with GPS when satellites are in view.

---

### Question 17

A user enrolls their personal iPhone in the company's MDM system to receive corporate email. After enrollment, the user notices that all apps installed on their phone are visible in the MDM portal. The user is concerned about privacy. What MDM deployment model would address this concern while still allowing corporate email access?

- A) Full device enrollment (supervised mode) — this mode provides the most privacy because it only monitors corporate apps and ignores all personal data
- B) A containerized or managed app deployment — the MDM manages only a secure corporate container (or specific corporate apps) on the device, while personal apps, photos, and data outside the container are invisible to the IT administrator
- C) The user should purchase a second personal phone for corporate email to avoid any MDM enrollment of their personal device
- D) Unenrolling from MDM entirely and manually configuring email settings through the phone's native mail app provides the same security as MDM without any monitoring

Correct Answer: B — A containerized MDM deployment (BYOD container model) separates personal and corporate data.

Many MDM platforms (including Microsoft Intune, VMware Workspace ONE, and Jamf) support a BYOD (Bring Your Own Device) model using managed apps or a secure container. In this model, MDM management scope is limited to corporate apps and the corporate container — personal apps, photos, messages, and location data outside the container are not visible to IT. Answer A is incorrect because supervised/full enrollment mode provides IT with broader device visibility, not less — it is the opposite of a privacy-preserving configuration. Answer C is incorrect because purchasing a second phone is a practical workaround but is not an MDM deployment model and is not the technical answer to the question. Answer D is incorrect because a manually configured mail account without MDM lacks the security controls (remote wipe of corporate data, certificate-based authentication, policy enforcement) that MDM provides for corporate data protection.

---

### Question 18

Which port number is used by SMTP when submitting outgoing email from a mail client to a mail server with STARTTLS encryption (the modern submission port)?

- A) Port 25
- B) Port 110
- C) Port 465
- D) Port 587

Correct Answer: D — Port 587

Port 587 is the SMTP mail submission port with STARTTLS, used by email clients to send outgoing messages to the mail server. Port 25 is the original SMTP port used for server-to-server relay (not for client submission and often blocked by ISPs). Port 110 is unencrypted POP3 for incoming mail. Port 465 is a legacy SMTP-over-SSL port that was briefly deprecated but has been re-standardized for implicit TLS — both 465 (implicit TLS) and 587 (STARTTLS) are in use, but 587 is the standard client submission port per RFC 6409.

---

### Question 19

A mobile device is configured to use a cellular network with the following APN settings: APN name, username, and password. The device sends and receives calls normally but cannot access mobile data or send MMS messages. What is the most likely cause?

- A) The SIM card is from an incompatible carrier and cannot be unlocked through APN settings alone
- B) The APN settings are incorrect or missing for the data and MMS APNs; different APN configurations handle voice, data, and MMS separately on cellular networks, and the MMS and data APNs may be unconfigured or incorrect
- C) The cellular radio in the device has failed; voice calls working normally while data fails indicates the radio can transmit voice frequencies but not data frequencies
- D) Mobile data requires a software license that must be activated separately by the carrier through the device's settings app; the license has expired and must be renewed

Correct Answer: B — Incorrect or missing APN settings for data and MMS are preventing mobile data and MMS.

APN (Access Point Name) settings configure how the mobile device connects to the carrier's data network and MMS gateway. Carriers often use separate APN profiles for general mobile data and MMS messages, each with different APN names and sometimes different authentication credentials. A device can make voice calls using only SIM registration (no APN required for voice on most networks), but data and MMS require correctly configured APN entries. Obtaining the correct APN settings from the carrier and entering them manually resolves this. Answer A is incorrect because SIM lock prevents voice calls as well — a phone that makes calls is not SIM-locked against data for APN-related reasons. Answer C is incorrect because cellular voice and data use different channels within the same radio; a radio failure severe enough to block all data while passing voice would typically produce other symptoms and is far less common than an APN misconfiguration. Answer D is incorrect because mobile data access is carrier-plan based, not a device-side software license.

---

### Question 20

A technician configures email on a new Android smartphone for a user. The corporate mail server requires IMAP on port 993 with SSL/TLS. After entering the correct server address, username, and password, the app shows "Cannot connect to server." The user's laptop connects to the same mail server without issues. What should the technician check first?

- A) Reinstall the mail app from the Play Store because the installed version is corrupt and cannot establish SSL/TLS connections regardless of server settings
- B) Verify that the phone has an active cellular data or Wi-Fi connection, confirm the server hostname resolves correctly (try another app that uses DNS), and verify that port 993 is not blocked by the corporate Wi-Fi firewall for mobile devices
- C) Change the incoming protocol from IMAP to POP3 and the port from 993 to 995, because Android devices require POP3 for SSL-encrypted corporate email
- D) The SSL/TLS certificate on the mail server is not trusted by Android; export the certificate and install it as a trusted CA on the Android device before the mail app will connect

Correct Answer: B — Verify network connectivity, DNS resolution, and firewall rules for port 993 on the mobile network.

Before assuming a configuration or certificate problem, the technician should verify that the phone has a working internet connection, that DNS resolves the mail server's hostname, and that the firewall policy does not block port 993 for mobile devices (some corporate networks apply different rules to BYOD phones vs. managed laptops). Answer A is incorrect because a corrupt mail app installation is an unlikely explanation that should only be considered after ruling out connectivity issues. Answer C is incorrect because IMAP on port 993 works correctly on Android — there is no requirement to use POP3 on Android devices. Answer D is incorrect because SSL certificate issues produce a certificate error warning, not a generic "Cannot connect to server" message; the generic error points to a connectivity issue rather than a certificate trust issue.
