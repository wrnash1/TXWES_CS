# Video Script: Module 14 - Mobile Device Connectivity

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

**Estimated Duration:** 22-24 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 1.3 (Mobile Device Connectivity), Domain 2.7 (Network Protocols and Ports)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

### Production Notes

> SHOW SLIDE: Title card — "Module 14: Mobile Device Connectivity | CIS-2320 Hardware Fundamentals"
> KEY EXAM TRAP 1: Students confuse "5G cellular" with "5 GHz Wi-Fi" — both share the "5G" label but are completely unrelated technologies. Address this directly.
> KEY EXAM TRAP 2: Students mix up IMAP and POP3 port numbers. Emphasize that IMAP uses 143/993 and POP3 uses 110/995, and both are for INCOMING mail only.
> KEY EXAM TRAP 3: Students forget that USB Type-C is a connector shape, NOT a speed standard. USB Type-C can carry USB 2.0, USB 3.2, or Thunderbolt — the port's protocol determines the speed, not the connector shape alone.
> PRODUCTION NOTE: Use a split-screen layout for all port number tables. Keep the email port table visible on screen while discussing SMTP to reinforce memory.

---

### [00:00 - 03:30] Section 1: Introduction and Module Overview

> SHOW SLIDE: "Module 14 Overview — What We Cover Today"

"Welcome back, everyone. I am Professor Nash, and this is Module 14 of CIS-2320 Hardware Fundamentals here at Texas Wesleyan University. Today's topic is Mobile Device Connectivity — one of the most directly practical topics you will encounter as a working technician, and one that is consistently tested on the CompTIA A+ Core 1 exam.

Here is what we are going to cover in this session. First, Bluetooth pairing — how it works, the profiles that matter, and how to troubleshoot a pairing failure. Second, cellular data generations — specifically 3G, 4G LTE, and 5G — and what a technician needs to understand about each one. Third, Wi-Fi standards and connectivity profiles, including the enterprise Wi-Fi authentication model that trips up a lot of exam candidates. Fourth, USB connector types — because the A+ exam expects you to identify these by sight and by use case. And fifth, email server settings — IMAP, POP3, and SMTP with all the port numbers you need to memorize.

> SHOW SLIDE: "CompTIA A+ Domains Covered: 1.3 Mobile Device Connectivity | 2.7 Protocols and Ports"

This material maps directly to Domain 1.3 of the CompTIA A+ Core 1 exam, as well as protocol port number questions that appear throughout the exam in different contexts. You will see these topics show up not just in mobile device questions, but anywhere the exam tests your knowledge of network services and connectivity standards.

Let me give you the approach for today. Mobile devices are not isolated gadgets — they are enterprise endpoints. When a new employee shows up on day one, a technician is responsible for configuring corporate email, connecting the device to the corporate wireless network, and ensuring data syncs correctly. Everything we cover today is a technician-level skill you will use from your first day on the job."

---

### [03:30 - 08:30] Section 2: Bluetooth Pairing and Wireless Profiles

> SHOW SLIDE: "Bluetooth — Short-Range Wireless Technology"

"Let us start with Bluetooth. Bluetooth is a short-range wireless communication standard that operates in the 2.4 GHz ISM band. The standard range is approximately 10 meters for most Class 2 devices, though Bluetooth 5.0 and later extends this to around 40 meters in ideal conditions with enhanced data throughput.

> SHOW SLIDE: "Bluetooth Pairing Steps"

The pairing process is how two Bluetooth devices establish a trusted connection. The modern standard for pairing is called SSP — Secure Simple Pairing. Depending on the device capabilities, SSP uses one of several association models. The most common for consumer devices is Numeric Comparison, where a six-digit PIN is displayed on both devices and the user confirms they match. For devices with no display — like a Bluetooth headset — the Just Works model is used, which pairs automatically without a PIN but provides less user verification.

> SHOW SLIDE: "Key Bluetooth Profiles — A2DP, HFP, HID, SPP"

For the A+ exam, you need to know the major Bluetooth profiles by name and function. A2DP — Advanced Audio Distribution Profile — is the profile used for wireless stereo audio streaming to headphones and speakers. HFP — Hands-Free Profile — is the profile used for phone calls in cars and headsets. HID — Human Interface Device profile — covers Bluetooth keyboards and mice. SPP — Serial Port Profile — provides a virtual serial port connection, commonly used for older barcode scanners and industrial devices.

> SHOW SLIDE: "Bluetooth Pairing Troubleshooting Checklist"

When Bluetooth pairing fails, work through this checklist. First, confirm both devices have Bluetooth enabled. Second, confirm the peripheral is in pairing mode — not all devices automatically enter pairing mode when turned on. Most headsets require holding the power button for three to five seconds until the LED alternates colors. Third, check that neither device is already connected to another device, because most Bluetooth peripherals support only one active connection at a time. Fourth, if the pairing initially worked but now fails, delete the saved pairing on both devices and start fresh.

> EXAM TIP: Highlight box on screen — 'Bluetooth pairing failure most often results from one device already being connected to something else, or a device that is not in active pairing mode.'

Now let me address a common misconception before we move on. You will hear people say '5G Wi-Fi' to describe their home router's 5 GHz band. That phrase causes real confusion when you start studying for the A+ exam. The 5 GHz band in Wi-Fi and 5G cellular are completely unrelated. Wi-Fi bands — 2.4 GHz and 5 GHz — are IEEE 802.11 standards managed by your router. 5G cellular is the fifth generation of the carrier mobile network. They do not interact. Keep them completely separate in your mind."

---

### [08:30 - 13:30] Section 3: Cellular Data Generations and Wi-Fi Standards

> SHOW SLIDE: "Cellular Generations — 3G, 4G LTE, 5G"

"Now let us talk about cellular data. As a technician, you will support users whose devices connect to cellular networks, and you need to understand what each generation offers and what it requires.

3G was the first generation that made data services practical on mobile phones. It delivered typical speeds in the range of 1 to 10 Mbps. 3G networks have been largely decommissioned in the United States as of 2022, so you will encounter 3G primarily on older devices that have not been updated.

4G LTE — Long Term Evolution — is the current mainstream standard. Typical download speeds range from 10 Mbps on a congested tower to 100 Mbps or more in favorable conditions. LTE uses licensed spectrum assigned to carriers. The device authenticates to the carrier network using a SIM card — specifically a nano-SIM in most modern devices, or an eSIM, which is a programmable embedded SIM that does not require a physical card.

5G is the fifth generation and comes in three distinct frequency tiers that behave very differently. Sub-6 GHz 5G uses spectrum similar to LTE, delivers moderate speed improvements, and provides coverage comparable to 4G towers. Mid-band 5G, which operates around 2.5 GHz, offers the best balance of speed and range. mmWave — millimeter wave 5G — operates at frequencies above 24 GHz and can achieve speeds exceeding 1 Gbps, but the range is measured in hundreds of meters and the signal cannot penetrate walls or glass effectively.

> SHOW SLIDE: "Key Rule — Cellular Radio is Hardware"

Here is a critical A+ exam point. A device's ability to connect to 5G is determined by its hardware radio. Upgrading your carrier plan does not add 5G capability to a device with an LTE-only radio. The physical antenna and radio chipset inside the phone determine which generation it can use. You cannot software-update a device into 5G capability.

> SHOW SLIDE: "Wi-Fi Standards — 802.11 a/b/g/n/ac/ax"

For Wi-Fi, the A+ Core 1 exam tests your ability to identify the 802.11 standards. The key facts are: 802.11b — 2.4 GHz, 11 Mbps maximum, legacy. 802.11g — 2.4 GHz, 54 Mbps. 802.11n (Wi-Fi 4) — dual-band, up to 600 Mbps with MIMO. 802.11ac (Wi-Fi 5) — 5 GHz, up to several Gbps with MU-MIMO. 802.11ax (Wi-Fi 6) — dual-band, OFDMA, designed for dense environments with many simultaneous devices.

> SHOW SLIDE: "WPA2-Personal vs WPA2-Enterprise"

For enterprise deployments, the critical distinction is between WPA2-Personal and WPA2-Enterprise. WPA2-Personal uses a pre-shared key — a single passphrase that every user types in. WPA2-Enterprise uses 802.1X authentication, which means each user authenticates with their individual username and password — or a digital certificate — validated against a RADIUS server. When a new employee tries to connect to the corporate Wi-Fi by typing the password they use at home, it will fail — because corporate Wi-Fi is not a password-based system. The technician must configure 802.1X credentials on the device, often through MDM software."

---

### [13:30 - 18:30] Section 4: USB Connector Types and Mobile Synchronization

> SHOW SLIDE: "USB Connector Types — Physical Identification"

"Next let us cover USB connectors, because the A+ exam will absolutely show you connector shapes and ask you to identify them.

USB Type-A is the rectangular connector you have used your entire life. It plugs into host ports on computers and into chargers and hubs. USB Type-A is host-side only in standard configurations.

USB Type-B is the square connector with beveled top corners found on printers and older peripherals. Full-size Type-B is still common on laser printers.

Micro-USB is the small trapezoidal connector that was standard on Android devices from roughly 2010 to 2018. The narrow shape with an asymmetrical profile distinguishes it from other micro connectors.

USB Type-C is the oval symmetrical connector used on all modern Android devices, most laptops, and many other peripherals. The key point for the exam — and I want you to write this down — is that USB Type-C is a connector shape, not a speed specification. A USB Type-C port on an inexpensive device may be USB 2.0 speed. A USB Type-C port on a premium device may be USB 3.2 Gen 2 or Thunderbolt 4. The connector looks identical in all cases. The host port's protocol specification determines actual speed.

Lightning is Apple's proprietary connector used on iPhones and iPads produced before the transition to USB-C that began with the iPhone 15 in 2023. Lightning is an 8-pin connector with a flat profile. It is not a USB standard — it is proprietary — but it carries USB 2.0 data by default with additional protocols available through MFi-certified accessories.

> SHOW SLIDE: "USB Versions and Speeds"

For speed reference: USB 2.0 is 480 Mbps. USB 3.0 (now called USB 3.2 Gen 1) is 5 Gbps. USB 3.1 Gen 2 (USB 3.2 Gen 2) is 10 Gbps. USB 3.2 Gen 2x2 is 20 Gbps. Thunderbolt 3 and Thunderbolt 4 both use the USB-C connector and deliver 40 Gbps.

> SHOW SLIDE: "Mobile Synchronization Methods"

For mobile synchronization, a technician needs to know three primary methods. USB sync connects the device physically and uses either MTP (Media Transfer Protocol) for file transfer on Android, or iTunes and Finder for iOS device backup and sync. ADB — Android Debug Bridge — is a developer tool that provides command-line access to an Android device over USB and is used for advanced diagnostics and software deployment. Wi-Fi sync allows backup and file transfer over a local wireless network when the device and computer are on the same network, requiring the connection to be initially set up over USB in most implementations."

---

### [18:30 - 22:00] Section 5: Email Server Settings and Port Numbers

> SHOW SLIDE: "Email Protocols — IMAP, POP3, SMTP" (keep on screen for full section)

"The email server settings section is worth significant points on the A+ exam, and the port numbers are tested directly. Let me walk through all three protocols completely.

IMAP — Internet Message Access Protocol — is the modern standard for receiving email. IMAP synchronizes your email client with the mail server. Messages remain on the server and are synchronized to the device, meaning you can access the same email from multiple devices and they all show the same state. IMAP uses port 143 for unencrypted connections and port 993 for SSL/TLS encrypted connections. In a corporate environment, IMAP with SSL on port 993 is the expected configuration.

POP3 — Post Office Protocol version 3 — is the older standard for receiving email. POP3 downloads messages from the server and typically deletes them from the server after download. This means the email exists only on the device that downloaded it, which is problematic when a user accesses email from multiple devices. POP3 uses port 110 for unencrypted connections and port 995 for SSL/TLS.

SMTP — Simple Mail Transfer Protocol — is used for sending email, not receiving. SMTP operates on port 25 for server-to-server relay. Port 587 with STARTTLS is the standard submission port for client applications to send outgoing email — this is the port your email app uses when it sends a message. Port 465 is SMTPS, an older SSL-wrapped SMTP implementation still in use at some providers.

SHOW SLIDE: Email Port Table — IMAP 143/993 | POP3 110/995 | SMTP 25/587/465

EXAM TIP on screen: 'A user who can receive email but cannot send: the problem is SMTP. A user who cannot receive email: the problem is IMAP or POP3. Use the symptom to identify which protocol is misconfigured, then verify the port number.'

One more configuration detail that appears in A+ exam scenarios. When a user sets up a mobile email account and it asks for incoming and outgoing server settings, those are two completely separate server entries. The incoming server runs IMAP or POP3. The outgoing server runs SMTP. They may be at different hostnames, they use different ports, and they may require separate authentication credentials. Never assume that fixing the incoming server settings will automatically correct outgoing mail — always configure both independently."

---

### [22:00 - 23:30] Section 6: Module Summary and Lab Prep

> SHOW SLIDE: "Module 14 Summary"

"Let me bring this all together before you head into the lab.

Bluetooth uses SSP pairing, operates at 2.4 GHz, and the major profiles are A2DP for audio, HFP for hands-free calls, HID for input devices, and SPP for serial connections. Pairing failure is most often a pairing-mode issue or a device-already-connected issue.

Cellular generations progress from 3G through 4G LTE to 5G. 5G has three tiers — sub-6 GHz, mid-band, and mmWave — with very different speed and range characteristics. The device radio hardware determines which generation it can use.

USB connectors: Type-A is the standard rectangular host connector, Type-B is the square printer connector, Micro-USB is the older Android connector, Type-C is the modern symmetrical oval connector, and Lightning is Apple's proprietary connector. USB Type-C shape does not determine speed.

Email ports: IMAP uses 143 plain and 993 SSL. POP3 uses 110 plain and 995 SSL. SMTP uses 25 server-to-server, 587 client submission, and 465 SSL.

For this week's lab you are going to document a Bluetooth pairing procedure, configure email server settings in a written configuration exercise, and identify USB connector types from photographs. This is practical documentation work — the kind of thing you will produce as a technician writing up a device configuration for a colleague.

> SHOW SLIDE: End Card — "Texas Wesleyan University | CIS-2320 | Professor Nash"

Thank you for watching. Complete the reading guide before attempting the lab, and review those port numbers until they are completely automatic. I will see you in the discussion forum. Good luck."

---

### Additional Resources

For further study on the topics covered in this module, visit:

- Professor Messer's free CompTIA A+ Core 1 study materials at professormesser.com — navigate to the 220-1101 course and review the mobile device connectivity sections covering Bluetooth, cellular standards, and email protocol ports.
- The official CompTIA A+ exam objectives document available at comptia.org — review Domain 1.3 for the complete list of mobile device connectivity topics tested on the 220-1101 exam.
