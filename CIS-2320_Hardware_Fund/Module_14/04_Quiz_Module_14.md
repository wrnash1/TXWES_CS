# Quiz: Module 14 - Mobile Device Connectivity
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which port is standard for securing incoming IMAP email traffic?
*   A) Port 25
*   B) Port 110
*   C) Port 993
*   D) Port 443
*   **Correct Answer:** C) IMAP over SSL/TLS uses TCP port 993.
*   **Distractor Analysis:**
    *   *Why correct:* IMAP over SSL/TLS uses TCP port 993.
    *   Port 25 is SMTP. Port 110 is unsecured POP3. Port 443 is HTTPS.

---

**Question 2**
In the context of mobile device connectivity, which of the following most accurately describes **LTE and 5G cellular data standards**?
*   A) LTE (4G) delivers typical download speeds of 10–100 Mbps using licensed spectrum; 5G extends this with three frequency tiers — sub-6 GHz for broad coverage, and mmWave for very high speeds at short range — both use SIM or eSIM cards for carrier authentication and require compatible device radios.
*   B) LTE and 5G are both Wi-Fi standards regulated by the IEEE 802.11 working group; LTE uses the 2.4 GHz band and 5G uses the 5 GHz band, and both require a wireless router within range to establish connectivity.
*   C) LTE and 5G are software subscription tiers offered by carriers; any device with a SIM card can be upgraded to 5G speeds by purchasing the higher-tier plan, regardless of the device's hardware radio capabilities.
*   D) LTE is a wired broadband standard used exclusively in enterprise data centers for low-latency server interconnects, while 5G refers to the fifth generation of Ethernet switching standards supporting 5 Gbps over Cat6a cabling.
*   **Correct Answer:** A) LTE (4G) delivers typical download speeds of 10–100 Mbps using licensed spectrum; 5G extends this with three frequency tiers — sub-6 GHz for broad coverage, and mmWave for very high speeds at short range — both use SIM or eSIM cards for carrier authentication and require compatible device radios.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the relationship between LTE and 5G as cellular (not Wi-Fi) standards, their speed characteristics, frequency band distinctions, and the hardware requirement (compatible radio) for using each generation.
    * *Why B is incorrect:* LTE and 5G are cellular standards, not Wi-Fi (IEEE 802.11) standards; "5G Wi-Fi" is a colloquial term for the 5 GHz Wi-Fi band, which is completely unrelated to 5G cellular technology. This confusion is a common misconception and an A+ exam trap.
    * *Why C is incorrect:* LTE and 5G capabilities are determined by the device's physical radio hardware; a carrier plan upgrade cannot enable 5G on a device whose radio only supports LTE.
    * *Why D is incorrect:* LTE and 5G are wireless cellular standards for mobile devices, not wired enterprise data center or Ethernet standards; Ethernet generations are named by speed (e.g., 10GbE) and defined by IEEE 802.3 standards, not "5G."


---

**Question 3**
A user configures their mobile email app to use IMAP but finds they can receive new email but cannot send any messages. All incoming server settings are confirmed correct. What is the most likely cause of the outgoing mail failure?
*   A) IMAP does not support outgoing mail on mobile devices; the user must switch to POP3 before the send function becomes available
*   B) The outgoing SMTP server settings are incorrect — wrong server address, port number (should be 587 with STARTTLS or 465 with SSL), or authentication credentials
*   C) The mobile device's SIM card must be activated for data before SMTP email transmission is permitted, even on a Wi-Fi connection
*   D) The phone's storage is full, preventing the email app from creating outgoing message files in the mail queue folder
*   **Correct Answer:** B) The outgoing SMTP server settings are incorrect — wrong server address, port number (should be 587 with STARTTLS or 465 with SSL), or authentication credentials
*   **Distractor Analysis:**
    * *Why B is correct:* Sending and receiving email use separate server configurations — IMAP handles incoming mail and SMTP handles outgoing mail. A user who can receive but not send has a problem specifically with the SMTP configuration: server address, port, encryption method, or authentication credentials.
    * *Why A is incorrect:* The choice of IMAP versus POP3 affects only incoming mail retrieval; both protocols work alongside SMTP for outgoing mail, and IMAP does not restrict SMTP functionality on mobile devices.
    * *Why C is incorrect:* SMTP email transmission works over any IP network connection including Wi-Fi; a SIM card or cellular data subscription is not required for email to function when the device is on Wi-Fi.
    * *Why D is incorrect:* While full storage can affect some app functions, SMTP failures present as connection or authentication errors, not storage errors; the symptom described is specifically a network/configuration failure, not a local storage issue.


---

**Question 4**
A technician is setting up a corporate smartphone for a new employee. The device needs to connect to the company's secured Wi-Fi network, which uses WPA2-Enterprise with 802.1X authentication. The employee enters the Wi-Fi password used at home but the corporate network connection fails. What is the correct resolution?
*   A) The employee's phone model is incompatible with WPA2-Enterprise; they must use a personal hotspot from their cellular data plan to access company resources instead
*   B) The employee needs to enter their corporate username and password (or install a certificate) for 802.1X authentication, which is different from the simple pre-shared key used on home WPA2-Personal networks
*   C) The IT department must whitelist the employee's MAC address on the wireless controller before WPA2-Enterprise will accept any connection attempt from a new device
*   D) WPA2-Enterprise requires the employee to connect via ethernet first and then the wireless credentials will be pushed to the device automatically through the wired connection
*   **Correct Answer:** B) The employee needs to enter their corporate username and password (or install a certificate) for 802.1X authentication, which is different from the simple pre-shared key used on home WPA2-Personal networks
*   **Distractor Analysis:**
    * *Why B is correct:* WPA2-Enterprise uses 802.1X/EAP authentication, which requires per-user credentials (username/password via PEAP or a digital certificate via EAP-TLS) authenticated against a RADIUS server — not a shared passphrase. Home networks use WPA2-Personal (PSK), which is a single passphrase shared by all users.
    * *Why A is incorrect:* Modern smartphones universally support WPA2-Enterprise/802.1X authentication; it is a standard wireless security protocol supported across iOS, Android, and Windows mobile platforms.
    * *Why C is incorrect:* MAC address whitelisting is an optional additional layer and is not a standard requirement for WPA2-Enterprise authentication; 802.1X authenticates users, not specific device MAC addresses.
    * *Why D is incorrect:* WPA2-Enterprise does not require a prior wired connection for credential provisioning; credentials or certificates are configured directly on the device via MDM or manual settings.


---

**Question 5**
A user wants to share their smartphone's cellular data connection with their laptop while traveling. They enable the mobile hotspot feature on their phone. Which technology is the smartphone using to share the cellular connection, and what are two security considerations the technician should advise?
*   A) The phone uses Bluetooth tethering exclusively for hotspot sharing; security considerations are that Bluetooth has no encryption and the hotspot should only be used in private locations
*   B) The phone creates a Wi-Fi access point using the cellular data connection; the technician should advise setting a strong WPA2 or WPA3 passphrase and monitoring data usage to avoid overage charges on metered cellular plans
*   C) The phone uses NFC to share the cellular connection; security considerations are that NFC range is limited to 4 centimeters and the connection drops if the devices are moved apart
*   D) The phone bridges the cellular connection through USB only; there are no security concerns because USB tethering is encrypted end-to-end by the operating system kernel
*   **Correct Answer:** B) The phone creates a Wi-Fi access point using the cellular data connection; the technician should advise setting a strong WPA2 or WPA3 passphrase and monitoring data usage to avoid overage charges on metered cellular plans
*   **Distractor Analysis:**
    * *Why B is correct:* Mobile hotspot functions by making the smartphone act as a Wi-Fi access point that routes traffic through the cellular data connection; securing it with WPA2/WPA3 prevents unauthorized use, and data usage monitoring is critical because cellular data plans are metered and hotspot traffic counts against the plan's data allowance.
    * *Why A is incorrect:* While Bluetooth tethering is one option, the standard mobile hotspot feature uses Wi-Fi, not Bluetooth exclusively; modern Bluetooth does include encryption (AES-128 in Bluetooth 4.1+), making the "no encryption" claim incorrect.
    * *Why C is incorrect:* NFC (Near Field Communication) is designed for very short-range data exchange and payment transactions, not for sharing internet connections; NFC cannot carry the sustained bandwidth needed for internet tethering.
    * *Why D is incorrect:* USB tethering is one available method but is not the only option — Wi-Fi hotspot is the most common hotspot method; USB connections also do not provide blanket end-to-end kernel encryption for all tethered traffic.
