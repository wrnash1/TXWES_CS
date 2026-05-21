# Quiz: Module 10 - Wireless Network Penetration Testing
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What web vulnerability allows an attacker to append `../` sequences to a URL parameter to retrieve unauthorized server files such as `/etc/passwd`?
*   A) SQL Injection
*   B) Cross-Site Scripting (XSS)
*   C) Directory Traversal
*   D) Command Injection
*   **Correct Answer:** C) Directory Traversal
*   **Distractor Analysis:**
    *   *Why C is correct:* Directory Traversal (Path Traversal) exploits insufficient input validation on file path parameters. By inserting `../` sequences, an attacker navigates up the directory tree to access files outside the web root — such as `/etc/passwd`, SSH keys, or application configuration files. It is a distinct vulnerability from injection attacks because it targets the server's filesystem access logic rather than SQL or OS command interpreters.
    *   *Why A is incorrect:* SQL Injection manipulates database query syntax by injecting SQL metacharacters into input fields. It targets the database layer and does not involve filesystem path traversal.
    *   *Why B is incorrect:* XSS injects malicious JavaScript that executes in a victim's browser. It is a client-side attack and does not involve accessing server-side files through path manipulation.
    *   *Why D is incorrect:* Command Injection inserts OS shell commands into an application input that is passed to a system command interpreter (e.g., `; cat /etc/passwd`). While it can also read files, it requires the application to be passing input to a shell — a different mechanism from path parameter traversal.

---

**Question 2**
In the context of wireless penetration testing, which of the following best defines a **deauthentication attack**?
*   A) An attack that cracks a WPA2 pre-shared key by submitting thousands of password guesses directly to the access point's authentication port.
*   B) An attack that exploits a design flaw in WPS by brute-forcing the PIN in two halves, ultimately recovering the network's WPA2 passphrase.
*   C) An attack that spoofs 802.11 management frames to disconnect wireless clients from an access point, forcing them to re-authenticate and generating a capturable WPA2 handshake.
*   D) An attack that creates a duplicate access point with the same SSID as a legitimate network to intercept client credentials and traffic.
*   **Correct Answer:** C) An attack that spoofs 802.11 management frames to disconnect wireless clients from an access point, forcing them to re-authenticate and generating a capturable WPA2 handshake.
*   **Distractor Analysis:**
    *   *Why C is correct:* The 802.11 standard does not require authentication of management frames by default, allowing an attacker to craft and transmit deauthentication frames that appear to come from the legitimate AP. When clients receive these frames they disconnect and immediately attempt to re-authenticate, producing a WPA2 four-way handshake that the attacker can capture for offline cracking. The `aireplay-ng --deauth` command automates this technique.
    *   *Why A is incorrect:* Directly submitting password guesses to an access point is a live brute-force against the authentication service — this is not how WPA2-PSK is attacked. WPA2 cracking is an offline operation performed against a captured handshake, not against the AP itself.
    *   *Why B is incorrect:* This describes a WPS PIN attack, exploiting the Wi-Fi Protected Setup design flaw. It is a separate technique that targets the WPS feature specifically, not 802.11 management frame spoofing.
    *   *Why D is incorrect:* This describes an Evil Twin (Rogue AP) attack — creating a fraudulent access point with the same SSID to lure clients. While both attacks target wireless clients, an Evil Twin is a separate technique from deauthentication frame injection.

---

**Question 3**
A penetration tester wants to capture all 802.11 wireless frames in range, including those from networks they are not associated with. Which command puts a wireless adapter into the required mode?
*   A) `iwconfig wlan0 essid "TargetNetwork"`
*   B) `airmon-ng start wlan0`
*   C) `aircrack-ng -w wordlist.txt capture.cap`
*   D) `aireplay-ng --deauth 10 -a <BSSID> wlan0`
*   **Correct Answer:** B) `airmon-ng start wlan0`
*   **Distractor Analysis:**
    *   *Why B is correct:* `airmon-ng start wlan0` switches the wireless adapter from managed mode (normal client operation) into monitor mode, creating a new interface (typically `wlan0mon`). Monitor mode allows the adapter to passively capture all 802.11 frames in range — including beacons, probe requests, authentication frames, and data frames from any network — without associating with an AP. This is a required prerequisite for `airodump-ng` packet capture and handshake collection.
    *   *Why A is incorrect:* `iwconfig wlan0 essid "TargetNetwork"` sets the SSID for the adapter to associate with — this connects the adapter to a specific network in managed mode. It does not enable monitor mode or passive frame capture.
    *   *Why C is incorrect:* `aircrack-ng -w wordlist.txt capture.cap` is the offline dictionary attack command used after a handshake has already been captured. It processes a saved packet capture file — it does not configure the adapter or perform live capture.
    *   *Why D is incorrect:* `aireplay-ng --deauth` sends deauthentication frames to disconnect clients. It requires the adapter to already be in monitor mode and is used after `airmon-ng` and `airodump-ng` are already running — it is not the command that enables monitor mode.

---

**Question 4**
A penetration tester is assessing a wireless network and wants to exploit the WPS feature to recover the WPA2 pre-shared key. Which vulnerability makes this attack feasible?
*   A) WPA2 four-way handshakes can be captured and cracked offline because the PSK is embedded directly in the handshake without any key derivation.
*   B) The WPS PIN verification process checks the 8-digit PIN in two independent halves, reducing the effective brute-force space from 100 million to approximately 11,000 combinations.
*   C) WPA2 access points broadcast the SSID and BSSID in plaintext beacons, allowing passive identification of target networks without authentication.
*   D) WPA2-Enterprise uses a shared RADIUS secret that can be extracted by any authenticated domain user using standard AD enumeration tools.
*   **Correct Answer:** B) The WPS PIN verification process checks the 8-digit PIN in two independent halves, reducing the effective brute-force space from 100 million to approximately 11,000 combinations.
*   **Distractor Analysis:**
    *   *Why B is correct:* WPS was designed to simplify device pairing but contains a critical design flaw: the access point verifies the first four digits of the 8-digit PIN separately from the last four (with one digit being a checksum). This splits 10^8 possibilities into two smaller spaces — roughly 10^4 + 10^3 — reducing the total to approximately 11,000 guesses. Tools like `reaver` and `bully` exploit this to recover the WPS PIN and the WPA2 PSK in a few hours against a vulnerable AP.
    *   *Why A is incorrect:* The WPA2 handshake does not contain the PSK directly — it contains material derived from the PSK through PBKDF2 key derivation. The offline attack works by guessing the PSK, deriving the expected key material, and comparing it against the captured handshake. This is the WPA2 handshake cracking technique, not a WPS attack.
    *   *Why C is incorrect:* SSID broadcasting in plaintext is standard Wi-Fi behavior and is not a vulnerability. It does not provide any authentication bypass capability and is completely separate from WPS exploitation.
    *   *Why D is incorrect:* WPA2-Enterprise uses 802.1X/RADIUS for authentication. While the RADIUS shared secret is a configuration parameter, it is not extractable via AD enumeration tools. The primary attack against WPA2-Enterprise is an Evil Twin rogue AP that captures RADIUS EAP credential exchanges.

---

**Question 5**
After capturing a WPA2 four-way handshake file using `airodump-ng`, a penetration tester attempts to recover the pre-shared key. Which command performs an offline dictionary attack against the captured handshake?
*   A) `reaver -i wlan0mon -b <BSSID> -vv`
*   B) `aireplay-ng --deauth 10 -a <BSSID> wlan0mon`
*   C) `airodump-ng --bssid <BSSID> -c 6 -w capture wlan0mon`
*   D) `aircrack-ng -w wordlist.txt capture.cap`
*   **Correct Answer:** D) `aircrack-ng -w wordlist.txt capture.cap`
*   **Distractor Analysis:**
    *   *Why D is correct:* `aircrack-ng` performs offline dictionary or brute-force attacks against captured WPA2 handshakes. The `-w wordlist.txt` flag specifies the password wordlist and `capture.cap` is the packet capture file containing the four-way handshake. For each password candidate in the wordlist, `aircrack-ng` derives the expected PMK and PTK and compares them against the captured handshake material — reporting a match if the correct PSK is found.
    *   *Why A is incorrect:* `reaver` is a WPS PIN brute-force tool that exploits the WPS design flaw to recover the WPA2 PSK by attacking the WPS PIN space — not by cracking a captured handshake. It communicates live with the AP rather than working offline against a capture file.
    *   *Why B is incorrect:* `aireplay-ng --deauth` sends deauthentication frames to disconnect wireless clients. It is used to force clients to re-authenticate (generating a handshake to capture), not to crack the captured handshake offline.
    *   *Why C is incorrect:* `airodump-ng` is the packet capture tool — it scans for networks, locks onto a specific BSSID/channel, and writes captured frames to a file. It collects the handshake data but does not perform cracking. The `-w capture` flag specifies the output file that `aircrack-ng` then processes.
