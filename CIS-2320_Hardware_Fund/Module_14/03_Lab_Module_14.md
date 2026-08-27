# Lab Activity: Module 14 - Mobile Device Connectivity

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

---

## Overview

This lab activity develops three hands-on competencies that are directly tested on the CompTIA A+ Core 1 (220-1101) exam: documenting a Bluetooth device pairing procedure, configuring mobile email server settings for IMAP and SMTP, and identifying USB and mobile device connector types from physical descriptions and photographs. You will complete each part and submit a written lab report with the required deliverables.

This lab does not require a specific device model. Any Android smartphone, iPhone, or tablet running a current operating system is acceptable for Parts 1 and 2. Part 3 is completed using the provided connector reference images in Canvas.

**Total Points: 100**
**Due:** See Canvas assignment for deadline.

---

## Prerequisites

Before beginning this lab, confirm the following:

- You have reviewed the Module 14 reading guide, including all glossary terms, port number tables, and USB connector type descriptions.
- You have access to a smartphone or tablet (personal device acceptable) for Parts 1 and 2.
- You have access to a Bluetooth peripheral — a headset, speaker, keyboard, or any Bluetooth device — for Part 1.
- You have a personal or school email account whose incoming (IMAP) and outgoing (SMTP) server settings you can look up. Gmail, Outlook, and Yahoo all publish their server settings publicly.
- You have reviewed the connector identification images posted in the Module 14 Canvas module.

---

## Part 1: Bluetooth Pairing Procedure Documentation (35 Points)

### Part 1 Objective

Document the complete process of pairing a Bluetooth peripheral to a mobile device, following each step precisely and recording what you observe at each stage.

### Part 1 Background

A technician is frequently responsible for setting up Bluetooth accessories for users — headsets, keyboards, speakers, and hands-free car systems. Documenting the procedure accurately ensures that the process can be repeated by any technician and provides a record for the help desk. The CompTIA A+ exam tests the sequence of pairing steps and the troubleshooting approach when pairing fails.

### Part 1 Procedure

Step 1: Prepare both devices. On your smartphone or tablet, navigate to Settings and locate the Bluetooth menu. Confirm that Bluetooth is currently off. On your Bluetooth peripheral, ensure it is fully powered off.

Step 2: Enable Bluetooth on your mobile device. Toggle Bluetooth on. In your lab report, record the exact menu path you followed on your specific device (for example: Settings > Connected Devices > Connection Preferences > Bluetooth, or Settings > Bluetooth).

Step 3: Put the Bluetooth peripheral into pairing mode. The specific procedure varies by device — consult the device's documentation or labeling if needed. Most headsets require holding the power button for three to five seconds until the indicator LED alternates between two colors or flashes rapidly. Record in your lab report: (a) the device name and model, (b) the exact steps you used to enter pairing mode, and (c) what visual or audio indicator confirmed that pairing mode was active.

Step 4: Discover the peripheral. On your mobile device's Bluetooth screen, tap "Scan" or "Find new device" if the scan does not begin automatically. Watch the list of discovered devices populate. Record how long the scan took before your peripheral appeared.

Step 5: Initiate pairing. Tap the peripheral's name in the discovered devices list. Record what happened on screen: Did a PIN or numeric code appear? Did you need to accept a prompt? Or did pairing complete automatically (Just Works model)?

Step 6: Confirm the paired connection. After pairing completes, the peripheral should appear in the "Paired Devices" or "Connected Devices" list with a status of "Connected." Take a screenshot of this screen. If you cannot take a screenshot, describe the display in detail in your lab report.

Step 7: Verify function. Test that the peripheral is functioning — play audio through a headset, type a character on a Bluetooth keyboard, or check that the speaker produces sound. Record what test you performed and whether it succeeded.

Step 8: Simulate a common failure. Disconnect the peripheral by tapping its name and selecting "Disconnect" or "Forget." Power off the peripheral. Attempt to reconnect from the mobile device's Bluetooth screen without putting the peripheral back into pairing mode. Record what happens. Then put the peripheral back into pairing mode and attempt to reconnect. Record the result. This exercise demonstrates the most common Bluetooth pairing failure scenario.

### Part 1 Deliverables

Write a step-by-step procedure document in your lab report that covers Steps 1 through 8 as actually performed. Include the device models used, the observed behavior at each step, your screenshot or screen description from Step 6, and a one-paragraph explanation of what Step 8 demonstrated about Bluetooth pairing troubleshooting.

**Part 1 Grading Rubric (35 points):**

- All eight steps documented with observed behavior: 20 points
- Screenshot or accurate screen description of paired connection: 5 points
- Device models and pairing mode method recorded: 5 points
- Step 8 analysis paragraph demonstrates understanding of pairing mode requirement: 5 points

---

## Part 2: Email Server Settings Configuration Exercise (40 Points)

### Part 2 Objective

Configure a mobile email account using correct IMAP incoming and SMTP outgoing server settings, document all settings used, and demonstrate understanding of why each setting is required.

### Part 2 Background

Configuring email on a mobile device requires the technician to know which protocol handles incoming mail (IMAP or POP3), which handles outgoing mail (SMTP), and the correct port numbers for encrypted connections. The A+ exam presents scenario questions where a user can receive but not send email, or vice versa, and expects the technician to identify which protocol and port is misconfigured.

### Part 2 Procedure

Step 1: Look up the IMAP and SMTP server settings for your email provider. Every major email provider publishes this information publicly. For Gmail, the incoming server is imap.gmail.com on port 993 with SSL, and the outgoing server is smtp.gmail.com on port 587 with STARTTLS (or port 465 with SSL). For Outlook/Hotmail, the incoming server is outlook.office365.com on port 993 with SSL, and the outgoing server is smtp.office365.com on port 587 with STARTTLS. Use your actual email provider and look up its published settings. Record all settings in your lab report before proceeding.

Step 2: On your mobile device, open the default email application (Mail on iOS, Gmail app, Outlook app, or any generic email app). Choose to add a new account and select the manual configuration option rather than the automatic setup. This forces you to enter all server settings individually and is the method used when automatic setup fails.

Step 3: Enter your email address and account name. When prompted for server type, select IMAP (not POP3).

Step 4: Configure the incoming (IMAP) mail server. Enter the server hostname, set the port to 993, and set the security/encryption type to SSL/TLS. Enter your username and password. Record a screenshot or written record of all incoming server settings.

Step 5: Configure the outgoing (SMTP) mail server. Enter the outgoing server hostname (this will be a different hostname than the incoming server for most providers), set the port to 587, set the encryption to STARTTLS, and enter your credentials. Record all settings.

Step 6: Save the account configuration and allow the email app to attempt to connect. If the connection succeeds, you will see your inbox load. Take a screenshot showing your inbox within the email app. If the connection fails, document the exact error message and use it as a troubleshooting exercise — consult your provider's published settings and identify which setting was entered incorrectly.

Step 7: Test sending and receiving. Send a test email to yourself or a classmate. Confirm receipt in your inbox. Reply to confirm outgoing SMTP is functioning. Take a screenshot of the sent message in your Sent folder.

Step 8: In your lab report, answer the following questions in complete sentences. (a) What is the difference between IMAP and POP3, and why did you choose IMAP for this exercise? (b) What would happen to your email on other devices if you had configured POP3 with "delete from server" enabled? (c) A user reports they can receive email but cannot send. Which protocol is failing, and what are the two most common causes? (d) What does STARTTLS mean, and how does it differ from connecting to an SSL port directly?

### Part 2 Deliverables

Submit: (1) a complete settings table documenting all incoming and outgoing server settings used, (2) a screenshot or written record of the configured account in the email app, (3) a screenshot of your inbox after successful connection, (4) a screenshot of a sent test email, and (5) written answers to the four Step 8 questions.

**Part 2 Grading Rubric (40 points):**

- Complete settings table with all fields (server, port, security type, authentication): 10 points
- Evidence of successful connection (inbox screenshot or equivalent): 10 points
- Evidence of working send/receive (sent message screenshot): 10 points
- Written answers to Step 8 questions, demonstrating understanding of IMAP vs POP3, SMTP troubleshooting, and encryption terminology: 10 points

---

## Part 3: USB and Mobile Connector Identification (25 Points)

### Part 3 Objective

Identify USB and mobile device connector types from physical descriptions and images, and match each connector to its primary use case and relevant speed or compatibility specification.

### Part 3 Background

The CompTIA A+ Core 1 exam tests connector identification directly. Exam questions present a photograph or description of a connector and ask the candidate to name it, or describe a use case and ask which connector type is required. This exercise builds the visual recognition and specification recall needed for those questions.

### Part 3 Procedure

Step 1: Using the connector identification images posted in the Module 14 Canvas module, identify each of the ten connectors shown. For each connector, record: (a) the connector name, (b) the primary device type or use case it is associated with, and (c) one distinguishing physical characteristic that differentiates it from similar connectors.

The ten connectors presented are:

- Connector A: Rectangular, approximately 12 mm wide, 4.5 mm tall.
- Connector B: Square with beveled upper corners, approximately 8 mm wide.
- Connector C: Small trapezoidal shape with a notched bottom profile, asymmetrical.
- Connector D: Oval, symmetrical, approximately 8.4 mm wide — can be inserted in either orientation.
- Connector E: Flat, narrow, 8-pin, Apple proprietary, symmetrical blade design.
- Connector F: Small trapezoidal shape, slightly larger than Connector C, with a more rounded profile. (Mini-USB)
- Connector G: Same physical shape as Connector D but labeled on its host port with a lightning bolt symbol.
- Connector H: Same physical shape as Connector D but labeled on its host port with the number "3" in a blue insert.
- Connector I: DB-9 male connector — trapezoidal shell with two rows of pins.
- Connector J: 6-wire modular connector, narrower than a standard Ethernet plug.

Step 2: For each connector you identified, write one sentence explaining what speed, standard, or compatibility limitation is most important for a technician to remember about that connector.

Step 3: Answer the following scenario questions in your lab report.

Scenario 1 — A user has a laptop with a USB-C port and wants to transfer files from an external hard drive. The drive arrived with a USB-C cable. The transfer speed is only 40 MB/s, but the user expected around 500 MB/s based on the drive's advertised specification. What are two possible explanations for the speed discrepancy, and how would you determine which applies?

Scenario 2 — A technician is ordering replacement cables for a department of iPhones. The current iPhone model in use is the iPhone 12. What connector type does the iPhone 12 use, and what data transfer speed does that connector natively support?

Scenario 3 — A user has a printer connected via USB that requires the Type-B square connector. The cable is lost. Describe the exact connectors on each end of the replacement cable the technician should order.

**Part 3 Grading Rubric (25 points):**

- Ten connector identifications with physical characteristic: 15 points (1.5 points each)
- Ten connector notes about key technician consideration: 5 points
- Three scenario answers demonstrating applied connector knowledge: 5 points

---

## Submission Instructions

Compile your complete lab report as a single document. The report must include clearly labeled sections for Part 1, Part 2, and Part 3 with all required deliverables, screenshots, and written responses. Export as PDF and upload to the Module 14 Lab Assignment in Canvas by the posted deadline.

Label all screenshots with a caption identifying what the screenshot shows. Written answers must be in complete sentences. Bullet lists are acceptable for settings tables and connector identification lists.

Late submissions receive a 10-point deduction per day unless an extension has been approved by Professor Nash before the deadline.

---

## Part 9 — Challenge Exercise

These advanced steps are optional and are not included in the standard grading rubric.

### Challenge Step 1 — Email Protocol Packet Analysis with Wireshark

Download and install Wireshark (free at wireshark.org) on any available computer that has access to a mail client sending or receiving email:

1. Start a Wireshark capture on the active network interface. Configure or open a mail client and trigger a mail check (receive) or send operation. Stop the capture after the operation completes. Apply the filter `tcp.port == 143 or tcp.port == 993 or tcp.port == 110 or tcp.port == 995 or tcp.port == 25 or tcp.port == 587` to isolate email protocol traffic. Document which port(s) you observe traffic on and whether the connection uses TLS (look for a TLS handshake in the packet stream before any IMAP/SMTP commands appear).
1. If you capture unencrypted IMAP traffic (port 143), follow the TCP stream and document what you can read in plaintext — specifically whether you can see the username, any commands (SELECT, FETCH, LIST), or message content. If all traffic is TLS-encrypted (port 993), document why the application data is not visible in Wireshark and explain in 1–2 sentences what the TLS record layer headers reveal about the session even when content is encrypted.
1. Write 2–3 sentences explaining the security implication of an employee using an unencrypted POP3 or IMAP mail client on a corporate guest Wi-Fi network, referencing specifically what an attacker with Wireshark on the same network segment could observe.

### Challenge Step 2 — MDM Policy Research and Configuration Simulation

Research a free MDM platform (Microsoft Intune 90-day trial, Jamf Now (free tier for up to 3 devices), or ManageEngine Mobile Device Manager Plus free edition) and document or simulate configuring a basic BYOD policy:

1. Research and document the minimum policy settings that a corporate IT administrator should configure for a BYOD smartphone enrollment: required screen lock PIN/biometric, automatic screen lock timeout, remote wipe capability, minimum OS version requirement, and prohibition of jailbroken/rooted devices. For each setting, explain in one sentence why it is included in a minimum BYOD policy.
1. Research what happens to the corporate data container and personal data when a remote wipe command is issued on a BYOD device enrolled in a container-model MDM (vs. a fully managed device). Document whether personal photos, personal apps, and contacts are wiped in each model, and identify which wipe type a privacy-conscious employee should request before unenrolling their personal device from corporate MDM.
1. Research and describe the "MAM without enrollment" (Mobile Application Management without full device enrollment) feature available in Microsoft Intune — specifically how it allows corporate app policies (data encryption, copy-paste restrictions, screenshot blocking) to be applied to apps like Outlook on a personal phone without enrolling the full device in MDM. Explain in 2–3 sentences why this model is a useful compromise for organizations with BYOD employees who are unwilling to enroll their personal phones.

### Challenge Step 3 — Cellular and Wi-Fi Band Research

Research the frequency bands used by the major US carriers for 5G and document the performance differences between Sub-6 GHz and mmWave deployments:

1. Look up the current 5G frequency bands used by two major US carriers (AT&T, Verizon, or T-Mobile) and build a comparison table with columns: Carrier, Band Name, Frequency Range, Theoretical Peak Download Speed, Typical Real-World Speed, and Coverage Range. Include at least one Sub-6 GHz band and one mmWave (24 GHz+ ) band per carrier.
1. Research why mmWave 5G has limited building penetration and explain the physics: reference the relationship between signal frequency, wavelength, and the ability of the signal to diffract around and through obstacles. Explain why a smartphone user walking from an outdoor plaza into a building lobby may instantly lose mmWave 5G coverage and fall back to Sub-6 GHz 5G or LTE.
1. Research Wi-Fi 6E (802.11ax on 6 GHz) and document: the available channel width, the frequency range, and the maximum theoretical throughput improvement over Wi-Fi 6 on 5 GHz. Write 2–3 sentences explaining why a 6 GHz Wi-Fi 6E network offers less interference than a 2.4 GHz or 5 GHz network and why it requires newer client devices that the 2.4 GHz and 5 GHz bands do not.
