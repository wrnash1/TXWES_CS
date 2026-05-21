# Quiz: Module 10 - Wireless and Mobile Security
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
A security engineer is auditing the wireless network at a corporate office and discovers several access points still configured to use WEP for encryption. The engineer needs to recommend an upgrade to the strongest currently available Wi-Fi security standard. Which protocol should the engineer specify?
A) WPA with TKIP
B) WPA2 with AES/CCMP
C) WPA3 with SAE
D) 802.11n with SSID broadcast disabled
*   **Correct Answer:** C) WPA3 with SAE
*   **Distractor Analysis:**
    *   *Why A is incorrect:* WPA with TKIP (Temporal Key Integrity Protocol) is deprecated — TKIP has known vulnerabilities and was designed as a short-term fix for WEP hardware. It is not an acceptable current standard.
    *   *Why B is incorrect:* WPA2 with AES/CCMP is the previous generation standard and is still considered acceptable on legacy infrastructure, but it is not the strongest currently available protocol — WPA3 supersedes it.
    *   *Why D is incorrect:* 802.11n is a physical layer speed standard, not a security protocol. Disabling SSID broadcast is security through obscurity — it does not encrypt traffic and provides no meaningful protection against an attacker with a wireless scanner.

---

---

**Question 2**
Users at a coffee shop report that after connecting to the free Wi-Fi, their browser sessions are being redirected and their credentials are being stolen. A security analyst determines that an attacker has deployed an access point broadcasting the same SSID as the legitimate coffee shop network and is intercepting all traffic from connected clients. Which wireless attack is being described?
A) Deauthentication (Deauth) attack
B) Bluejacking
C) Evil Twin attack
D) Replay attack
*   **Correct Answer:** C) Evil Twin attack
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A deauthentication attack sends forged 802.11 management frames to disconnect clients from a legitimate AP — it is a denial-of-service technique, not a traffic interception method. It may be used as a precursor to an evil twin attack but is not itself the interception mechanism.
    *   *Why B is incorrect:* Bluejacking is a Bluetooth attack that sends unsolicited messages to nearby discoverable devices — it does not involve Wi-Fi access points or traffic interception.
    *   *Why D is incorrect:* A replay attack captures valid authentication tokens or encrypted packets and retransmits them to gain unauthorized access — it does not involve deploying a rogue access point to intercept new client sessions.

---

---

**Question 3**
An employee's company-issued smartphone is reported stolen at an airport. The device contains corporate email, VPN credentials, and access to the customer relationship management (CRM) application. The MDM administrator needs to immediately protect corporate data on the lost device. Which MDM action should be taken first?
A) Disable the user's Active Directory account to prevent network login from any device.
B) Issue a remote wipe command through the MDM platform to erase all data on the device.
C) Revoke the user's VPN certificate so the device cannot establish a VPN tunnel.
D) Change the user's email password so new messages are no longer delivered to the device.
*   **Correct Answer:** B) Issue a remote wipe command through the MDM platform to erase all data on the device.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Disabling the AD account prevents future logins from any device but does not remove the data already stored locally on the stolen device — an attacker with physical access could still extract data from the device storage offline.
    *   *Why C is incorrect:* Revoking the VPN certificate prevents new VPN connections but does not protect data already present on the device, including cached email, stored documents, and saved credentials.
    *   *Why D is incorrect:* Changing the email password stops future email delivery to the device but leaves all previously downloaded emails, attachments, and CRM data accessible to whoever possesses the stolen phone.

---

**Question 4**
A security awareness trainer is explaining Bluetooth attack types to new employees. An employee asks about the difference between Bluejacking and Bluesnarfing. Which statement correctly distinguishes the two attacks?
A) Bluejacking steals data from the victim's device; Bluesnarfing sends unsolicited messages to a discoverable device.
B) Bluejacking sends unsolicited messages to a discoverable device; Bluesnarfing accesses and exfiltrates data from the device without consent.
C) Bluejacking and Bluesnarfing are both names for the same attack — unauthorized data theft via Bluetooth.
D) Bluejacking pairs with the victim's device to gain remote control; Bluesnarfing jams the Bluetooth signal to cause a denial of service.
*   **Correct Answer:** B) Bluejacking sends unsolicited messages to a discoverable device; Bluesnarfing accesses and exfiltrates data from the device without consent.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This reverses the definitions — Bluejacking is the message-sending attack (nuisance) and Bluesnarfing is the data theft attack.
    *   *Why C is incorrect:* Bluejacking and Bluesnarfing are distinct attacks with different objectives and severity levels — Bluejacking is a low-severity nuisance while Bluesnarfing is a data breach.
    *   *Why D is incorrect:* The attack that involves gaining full remote control of a device's functions (making calls, reading messages) is called Bluebugging, not Bluejacking. Bluejacking does not involve pairing or remote control.

---

**Question 5**
A hospital is implementing a BYOD policy allowing clinical staff to use personal smartphones to access the electronic health record (EHR) system. The security team must ensure that patient data in the EHR application cannot be copied to the personal portion of the device (such as personal cloud backup or personal apps). Which mobile security control best addresses this requirement?
A) Require all BYOD devices to enroll in MDM and enable full device remote wipe capability.
B) Implement application containerization to isolate the corporate EHR app and its data from the personal partition of the device.
C) Enforce a screen lock PIN of at least eight digits on all enrolled devices.
D) Deploy a geofencing policy that restricts EHR access to within the hospital's physical campus.
*   **Correct Answer:** B) Implement application containerization to isolate the corporate EHR app and its data from the personal partition of the device.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Full device remote wipe addresses the lost/stolen device scenario but does not prevent data leakage to personal apps during normal use — it also raises privacy concerns for BYOD users who do not consent to wiping personal data.
    *   *Why C is incorrect:* A screen lock PIN protects physical access to the device when it is unattended but does not prevent a logged-in user from copying EHR data to a personal cloud backup or personal messaging app during an active session.
    *   *Why D is incorrect:* Geofencing restricts when and where the EHR application can be accessed, but it does not prevent data that has already been accessed within the hospital from being transferred to personal apps on the same device.
