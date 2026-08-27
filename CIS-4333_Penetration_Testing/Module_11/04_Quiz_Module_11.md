# Quiz: Module 11 — Wireless Network Assessment

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

**Instructions:** Choose the single best answer for each question.

---

**Question 1**

A penetration tester wants to passively capture all 802.11 wireless frames in range, including management frames and data from networks they are not associated with. What is the required first step?

- A) Run `airodump-ng wlan0` to begin capturing frames in managed mode
- B) Run `airmon-ng start wlan0` to enable monitor mode on the wireless interface
- C) Run `aircrack-ng -w rockyou.txt capture.cap` to begin cracking
- D) Run `aireplay-ng --deauth 10 -a <BSSID> wlan0` to force clients to reconnect

**Correct Answer:** B) Run `airmon-ng start wlan0` to enable monitor mode on the wireless interface

**Distractor Analysis:**

- *Why B is correct:* Wireless adapters normally operate in managed mode, where they only process frames addressed to their own MAC address and frames from the network they are associated with. Monitor mode removes this filter, allowing the adapter to capture all 802.11 frames in range regardless of destination — beacons, probe requests, authentication frames, and data frames from any network. `airmon-ng start wlan0` performs this switch and creates a new monitor mode interface (typically `wlan0mon`). This is a mandatory prerequisite for any subsequent wireless assessment step.
- *Why A is incorrect:* Running `airodump-ng wlan0` directly on a non-monitor-mode interface will fail or produce no useful output. Airodump-ng requires a monitor mode interface to capture 802.11 frames passively. The interface name in managed mode (`wlan0`) must be converted to a monitor mode interface first.
- *Why C is incorrect:* `aircrack-ng` is the offline cracking tool that processes a previously saved capture file. It does not perform live frame capture and cannot be run before a handshake has already been captured. This is a late-stage tool in the workflow, not the first step.
- *Why D is incorrect:* `aireplay-ng --deauth` sends deauthentication frames to disconnect clients and force handshake regeneration. It requires the adapter to already be in monitor mode and `airodump-ng` to already be running. It is never the first step in a wireless assessment workflow.

---

**Question 2**

A penetration tester has enabled monitor mode and is running airodump-ng. No clients are currently connected to the target WPA2-Personal network. The tester needs to capture the four-way handshake as quickly as possible. Which technique forces a handshake to be generated?

- A) Connect a personal device to the target network and observe the handshake during normal authentication
- B) Use Reaver to brute-force the WPS PIN, which generates a handshake as a byproduct
- C) Send deauthentication frames to associated clients using aireplay-ng to force them to reconnect
- D) Use hashcat to precompute the handshake offline using the target SSID

**Correct Answer:** C) Send deauthentication frames to associated clients using aireplay-ng to force them to reconnect

**Distractor Analysis:**

- *Why C is correct:* The 802.11 standard does not authenticate management frames by default, allowing an attacker to send spoofed deauthentication frames that appear to come from the legitimate AP. When associated clients receive these frames, they disconnect and immediately attempt to re-associate, producing a fresh four-way handshake that the tester's airodump-ng session captures. The command `aireplay-ng --deauth 10 -a <BSSID> -c <CLIENT_MAC> wlan0mon` sends 10 deauthentication frames targeted at a specific client.
- *Why A is incorrect:* The question states no clients are currently connected. Connecting a personal device introduces a new client but is not a penetration testing technique — it is simply waiting for organic authentication. The scenario calls for a technique to force a handshake when clients are absent, not for the tester to connect their own device.
- *Why B is incorrect:* Reaver attacks the WPS PIN to recover the PSK — it does not generate a WPA2 four-way handshake as a byproduct. WPS PIN attacks and handshake capture are completely separate techniques with different goals and different attack mechanisms.
- *Why D is incorrect:* Hashcat is an offline cracking tool that processes already-captured handshakes. It cannot generate a handshake and does not precompute handshakes from an SSID. The SSID is used as the PBKDF2 salt during cracking, but cracking requires a previously captured handshake file to work against.

---

**Question 3**

Which wireless security protocol uses Simultaneous Authentication of Equals (SAE) to replace the traditional four-way handshake, providing forward secrecy and resistance to offline dictionary attacks?

- A) WPA2-Personal
- B) WPA-TKIP
- C) WPA3
- D) WPA2-Enterprise

**Correct Answer:** C) WPA3

**Distractor Analysis:**

- *Why C is correct:* WPA3 replaced the WPA2 four-way handshake authentication with SAE (Simultaneous Authentication of Equals), also known as Dragonfly. SAE provides forward secrecy — meaning that capturing current traffic does not enable decryption of past sessions — and is mathematically resistant to offline dictionary attacks because the PSK is never transmitted in a form that can be cracked offline. Even if an attacker captures the full WPA3 authentication exchange, they cannot mount an offline dictionary attack against the recorded frames.
- *Why A is incorrect:* WPA2-Personal uses a four-way handshake derived from PBKDF2 with the PSK as input. Captured handshakes are vulnerable to offline dictionary attacks using Hashcat or aircrack-ng. WPA2-Personal does not provide forward secrecy.
- *Why B is incorrect:* WPA-TKIP is the deprecated predecessor to WPA2. It does not use SAE and is itself vulnerable to multiple attacks. It is the opposite of a forward-secure protocol.
- *Why D is incorrect:* WPA2-Enterprise uses 802.1X and RADIUS for per-user authentication rather than a shared PSK. It is more secure than WPA2-Personal, but it still uses the WPA2 handshake mechanism (not SAE) and does not provide forward secrecy. The primary attack against WPA2-Enterprise is an evil twin rogue RADIUS server, not offline cracking.

---

**Question 4**

A penetration tester discovers that the target organization's wireless router has WPS enabled and is not locked. The tester uses Reaver to launch an attack. Why is WPS vulnerable to this attack?

- A) WPS uses the WPA2 PSK directly as the PIN, so guessing the PIN recovers the PSK without any additional steps.
- B) The WPS PIN verification process checks the 8-digit PIN in two independent halves, reducing the effective brute-force space from 100 million to approximately 11,000 combinations.
- C) WPS transmits the PSK in plaintext during the pairing process, allowing passive capture without any active attack.
- D) WPS uses the same four-way handshake as WPA2-Personal, making captured WPS frames crackable with the same wordlist attack.

**Correct Answer:** B) The WPS PIN verification process checks the 8-digit PIN in two independent halves, reducing the effective brute-force space from 100 million to approximately 11,000 combinations.

**Distractor Analysis:**

- *Why B is correct:* WPS was designed with a critical design flaw: the AP confirms whether the first four digits of the 8-digit PIN are correct before checking the second four digits. The last digit of the PIN is a checksum derivable from the other seven. This means the attacker needs to guess only `10^4` possibilities for the first half and `10^3` for the second half (the fourth digit of the second group is the checksum) — approximately 11,000 total guesses versus 100 million for a full 8-digit space. Reaver exploits this by submitting half-PINs iteratively. Once the PIN is found, the AP reveals the WPA2 PSK.
- *Why A is incorrect:* The WPS PIN and the WPA2 PSK are separate values. The PIN is an 8-digit numeric code used for device pairing. The PSK is the Wi-Fi password chosen by the administrator. WPS provides the PSK to a device after the correct PIN is verified — the PIN itself is not the PSK.
- *Why C is incorrect:* WPS does not transmit the PSK in plaintext. The PSK is only revealed after the PIN is successfully verified. The protocol encrypts the key exchange. The vulnerability is the design flaw in PIN verification, not plaintext transmission.
- *Why D is incorrect:* WPS uses a completely different protocol mechanism than WPA2's four-way handshake. WPS frames are not WPA2 EAPOL handshake frames and cannot be processed by aircrack-ng or Hashcat in the same way. The attack against WPS is live online brute-forcing of the PIN space, not offline handshake cracking.

---

**Question 5**

An enterprise organization deploys WPA2-Enterprise with 802.1X authentication throughout its facilities. A penetration tester sets up a rogue access point with the same SSID as the legitimate corporate network. Which attack tool is specifically designed to capture credentials from enterprise clients that attempt to authenticate with the rogue AP?

- A) Hashcat with mode 22000
- B) Reaver with the `-vv` verbosity flag
- C) hostapd-wpe (Wi-Fi Protected Enterprise)
- D) aircrack-ng with the rockyou.txt wordlist

**Correct Answer:** C) hostapd-wpe (Wi-Fi Protected Enterprise)

**Distractor Analysis:**

- *Why C is correct:* `hostapd-wpe` is a patched version of the standard `hostapd` access point daemon specifically modified to conduct WPA2-Enterprise evil twin attacks. It masquerades as a legitimate RADIUS authentication server and captures the EAP credential exchanges from enterprise clients that attempt to authenticate with the rogue AP. The captured EAP credentials (typically in Net-NTLMv2 format) can then be cracked offline with Hashcat or used in a relay attack. `hostapd-wpe` is the standard tool for this attack scenario.
- *Why A is incorrect:* Hashcat mode 22000 cracks WPA2 PMKID hashes and four-way handshakes — it is an offline cracking tool for WPA2-Personal. WPA2-Enterprise does not use a PSK, so there is no handshake of this type to capture or crack.
- *Why B is incorrect:* Reaver attacks WPS PIN vulnerabilities to recover a WPA2-Personal PSK. WPA2-Enterprise does not use WPS or a PSK. Reaver cannot attack 802.1X enterprise authentication.
- *Why D is incorrect:* aircrack-ng performs offline dictionary attacks against WPA2-Personal four-way handshakes and WEP keys. WPA2-Enterprise does not produce a crackable PSK-based handshake. Aircrack-ng cannot process 802.1X EAP exchanges.

---

**Question 6**

A tester runs `airodump-ng wlan0mon` and the output shows a network with ENC = "OPN." What does this indicate about the security of that network?

- A) The network uses WPA2 with an open SSID broadcast but still encrypts data frames.
- B) The network requires a password but uses an older WEP encryption scheme.
- C) The network is an open network with no encryption or authentication — all traffic is transmitted in plaintext.
- D) The network uses WPA3 with the SAE open authentication extension.

**Correct Answer:** C) The network is an open network with no encryption or authentication — all traffic is transmitted in plaintext.

**Distractor Analysis:**

- *Why C is correct:* In airodump-ng output, the ENC column shows the encryption type. "OPN" indicates an open network — no encryption, no authentication. Any device within radio range can passively capture all data frames, including HTTP traffic, credentials submitted to non-HTTPS services, DNS queries, and any other unencrypted application data. Open networks are commonly found in public spaces like coffee shops and airports. Finding an OPN network during a corporate wireless assessment is a high-severity finding.
- *Why A is incorrect:* An open SSID broadcast simply means the SSID is not hidden — it has nothing to do with whether data is encrypted. WPA2 networks with visible SSIDs still encrypt data; OPN means no encryption at all. The ENC column distinguishes encryption protocol, not SSID visibility.
- *Why B is incorrect:* WEP networks appear in the ENC column as "WEP," not "OPN." An OPN classification means there is no security protocol whatsoever — not even the broken WEP protocol.
- *Why D is incorrect:* WPA3's SAE open (OWE — Opportunistic Wireless Encryption) does provide unauthenticated but encrypted connections. However, in airodump-ng, OWE networks typically show as "OWE" or may show differently depending on tool version. A plain "OPN" designation represents a fully unencrypted, unauthenticated network.

---

**Question 7**

After capturing a WPA2 handshake in the file `capture-01.cap`, a tester wants to use GPU acceleration for maximum cracking speed. Which command correctly runs a dictionary attack using Hashcat?

- A) `aircrack-ng -w rockyou.txt capture-01.cap`
- B) `john --format=wpa2 capture-01.cap --wordlist=rockyou.txt`
- C) `hcxpcapngtool -o hash.hc22000 capture-01.cap` followed by `hashcat -m 22000 hash.hc22000 rockyou.txt`
- D) `reaver -i wlan0mon -b <BSSID> -w rockyou.txt`

**Correct Answer:** C) `hcxpcapngtool -o hash.hc22000 capture-01.cap` followed by `hashcat -m 22000 hash.hc22000 rockyou.txt`

**Distractor Analysis:**

- *Why C is correct:* Hashcat cannot directly process `.cap` (pcap) files. The capture file must first be converted to Hashcat's native WPA2 hash format using `hcxpcapngtool`. The output file with the `.hc22000` extension is then processed by Hashcat with mode 22000 (WPA-PBKDF2-PMKID+EAPOL). Hashcat uses GPU acceleration to test millions of password candidates per second — significantly faster than aircrack-ng's CPU-based cracking.
- *Why A is incorrect:* This is the correct aircrack-ng command for CPU-based dictionary attack against a WPA2 handshake. It is valid and functional, but the question asks specifically for GPU-accelerated Hashcat. Aircrack-ng does not use GPU acceleration and is substantially slower on large wordlists.
- *Why B is incorrect:* John the Ripper's `--format=wpa2` mode does not directly process pcap files in this manner. John the Ripper would require conversion using a helper tool and a different command structure. More importantly, John is not GPU-accelerated and is not the tool of choice for WPA2 handshake cracking.
- *Why D is incorrect:* Reaver is a WPS PIN brute-force tool. It does not accept wordlist files and does not crack WPA2 handshakes. The `-w` flag in Reaver means wait time between PIN attempts, not wordlist.

---

**Question 8**

A penetration tester is conducting a wireless assessment at a multi-tenant office building. During the engagement, they set up a rogue AP and notice that five devices from a neighboring tenant company have connected to it. What is the appropriate immediate response?

- A) Continue the assessment — any device that connects to the rogue AP is within the physical RF coverage area and therefore implicitly in scope.
- B) Shut down the rogue AP immediately and document the unintended connections in the engagement notes for disclosure to the client.
- C) Capture the credentials from the neighboring tenant's devices before shutting down, as this demonstrates additional business risk.
- D) Move the rogue AP to a higher signal strength to ensure only the target organization's devices connect.

**Correct Answer:** B) Shut down the rogue AP immediately and document the unintended connections in the engagement notes for disclosure to the client.

**Distractor Analysis:**

- *Why B is correct:* Unintended third-party connections are a serious ethical and legal issue. The tester's authorization covers only the client organization — connecting to devices belonging to a neighboring tenant without their consent is unauthorized access. The correct response is immediate cessation of the activity, documentation of what occurred, and disclosure to the client so appropriate notifications can be made. The PenTest+ exam and professional standards are clear: stop, document, and disclose.
- *Why A is incorrect:* Physical proximity does not imply authorization. The Computer Fraud and Abuse Act does not include a radio propagation exception. Being within RF range of a device does not grant any right to intercept its communications. Implicit scope does not exist — only explicit written authorization defines scope.
- *Why C is incorrect:* Capturing credentials from unauthorized third parties is a serious legal violation and a major ethical breach. This would expose the tester and their organization to criminal liability and civil lawsuits. No finding justification exists for accessing systems belonging to parties outside the engagement scope.
- *Why D is incorrect:* Increasing signal strength to filter by organization is not technically feasible — RF signals do not discriminate by organization membership. More critically, adjusting the AP to continue the engagement rather than stopping when unauthorized third-party connections occur demonstrates reckless disregard for ethical and legal obligations.

---

**Question 9**

Which wireless attack technique captures credentials from enterprise users without requiring knowledge of the WPA2-Enterprise PSK or any offline cracking of a handshake?

- A) WPS PIN attack using Reaver against the 802.1X RADIUS server
- B) Offline dictionary attack using Hashcat against a captured WPA2-Enterprise four-way handshake
- C) Evil twin attack with a rogue RADIUS server (hostapd-wpe) that intercepts EAP credential exchanges
- D) Deauthentication attack combined with PMKID capture using hcxdumptool

**Correct Answer:** C) Evil twin attack with a rogue RADIUS server (hostapd-wpe) that intercepts EAP credential exchanges

**Distractor Analysis:**

- *Why C is correct:* WPA2-Enterprise authenticates users via EAP protocols (PEAP, EAP-TTLS, EAP-TLS) against a RADIUS server. When a user's device connects to a rogue AP running `hostapd-wpe`, it attempts to authenticate with the rogue RADIUS server. Depending on the EAP type and the client's certificate validation settings, the client may send credentials (often in Net-NTLMv2 format) to the rogue server. These captured credential exchanges can then be cracked offline. No PSK knowledge is required — the attack exploits trust in the RADIUS server identity.
- *Why A is incorrect:* WPS PIN attacks target WPA2-Personal networks only. WPA2-Enterprise does not use WPS and does not have a PSK to recover via PIN attack. The RADIUS server is not vulnerable to WPS.
- *Why B is incorrect:* WPA2-Enterprise does not produce a PSK-based four-way handshake that is vulnerable to dictionary attacks. There is no PSK to crack. The authentication material involved in 802.1X/EAP is fundamentally different from the WPA2-Personal handshake.
- *Why D is incorrect:* PMKID capture and cracking applies to WPA2-Personal networks. The PMKID is derived from the PSK — WPA2-Enterprise has no PSK. hcxdumptool cannot capture WPA2-Enterprise EAP credentials in a crackable form using this technique.

---

**Question 10**

A penetration tester conducts wireless reconnaissance and identifies a target network using the SSID "CorpWiFi" broadcasting on channel 6 with BSSID `AA:BB:CC:DD:EE:FF`. Which airodump-ng command correctly begins a focused capture against this specific network while saving packets to disk?

- A) `airodump-ng --bssid AA:BB:CC:DD:EE:FF -c 6 -w corp_capture wlan0mon`
- B) `airmon-ng start wlan0 --bssid AA:BB:CC:DD:EE:FF -c 6`
- C) `aireplay-ng -0 10 -a AA:BB:CC:DD:EE:FF wlan0mon`
- D) `aircrack-ng --bssid AA:BB:CC:DD:EE:FF -w rockyou.txt corp_capture.cap`

**Correct Answer:** A) `airodump-ng --bssid AA:BB:CC:DD:EE:FF -c 6 -w corp_capture wlan0mon`

**Distractor Analysis:**

- *Why A is correct:* `airodump-ng` with `--bssid` focuses capture on the specified AP's MAC address, filtering out traffic from other networks. The `-c 6` flag locks the adapter to channel 6, preventing channel hopping which would miss packets. The `-w corp_capture` flag writes captured frames to output files (`.cap`, `.csv`, `.kismet.csv`). Running against `wlan0mon` (the monitor mode interface) enables passive capture of all frames from the target network, including the four-way handshake when clients authenticate.
- *Why B is incorrect:* `airmon-ng start` only enables monitor mode on a wireless interface — it does not accept `--bssid` or channel options and does not perform packet capture. Monitor mode must be enabled separately before running airodump-ng.
- *Why C is incorrect:* This is an `aireplay-ng` deauthentication command (`-0 10` sends 10 deauth frames to the specified BSSID). Deauthentication is a separate step used after airodump-ng is already capturing — it forces clients to disconnect so their reconnection generates a handshake. It does not perform capture or write packets to disk.
- *Why D is incorrect:* `aircrack-ng` is the offline cracking tool. It processes an already-saved `.cap` file to recover the PSK. It does not perform live packet capture and cannot capture handshakes. The `--bssid` flag in aircrack-ng filters which network within the capture file to attack, not which network to capture from.

---

---

**Question 11**

A tester captures a WPA2-Personal four-way handshake using airodump-ng. They attempt to crack it with `aircrack-ng -w /usr/share/wordlists/rockyou.txt handshake.cap` but the passphrase is not in the wordlist. What is the next appropriate step?

- A) Attempt a WPS PIN attack since WPA2 handshakes cannot be cracked without the correct wordlist
- B) Use hashcat with rule-based mutations on the wordlist to expand the search space: `hashcat -m 22000 handshake.hc22000 rockyou.txt -r best64.rule`
- C) The assessment is complete — if rockyou.txt fails, the passphrase is uncrackable
- D) Perform a deauthentication flood to force the client to use a weaker handshake

**Correct Answer:** B) Use hashcat with rule-based mutations on the wordlist to expand the search space: `hashcat -m 22000 handshake.hc22000 rockyou.txt -r best64.rule`

**Distractor Analysis:**

- *Why B is correct:* Rule-based attacks apply character substitutions and mutations (adding numbers, capitalizing letters, appending symbols) to each wordlist entry, dramatically expanding coverage beyond the raw wordlist. Common rules like `best64.rule` cover typical password patterns (`Password1`, `password!`, `p@ssword`). Hashcat is significantly faster than aircrack-ng for offline cracking due to GPU acceleration. This is the standard professional escalation path after wordlist failure.
- *Why A is incorrect:* WPS PIN attacks are used to recover the PSK from WPS-enabled APs — they are a separate attack path from handshake cracking. If WPS is disabled on the target AP, this approach fails. WPA2 handshakes can be cracked without WPS if the wordlist or ruleset covers the passphrase.
- *Why C is incorrect:* Rockyou.txt contains approximately 14 million entries — a large but finite set. Many organizational passphrases are not in rockyou.txt but can be recovered with rule-based mutations, custom wordlists, or brute force against shorter passphrases.
- *Why D is incorrect:* Deauthentication sends management frames to force clients to disconnect and reconnect. It is used to capture a handshake when no authentication is occurring — not to weaken the cryptographic strength of the handshake. WPA2 handshakes always use the same PBKDF2 derivation regardless of how they are captured.

---

**Question 12**

What is the primary distinction between a rogue AP (evil twin) attack and a standard deauthentication attack against a WPA2 network?

- A) Deauthentication attacks require root privileges on Linux; rogue AP attacks do not
- B) A deauthentication attack forces clients to disconnect to capture handshakes or perform DoS; a rogue AP mimics the legitimate network's SSID and BSSID to lure clients into connecting to the attacker's AP, enabling credential capture or man-in-the-middle interception of decrypted traffic
- C) Rogue AP attacks only work against WEP networks; deauthentication works against WPA2
- D) Deauthentication attacks require physical proximity to the AP; rogue AP attacks can be conducted remotely

**Correct Answer:** B) A deauthentication attack forces clients to disconnect to capture handshakes or perform DoS; a rogue AP mimics the legitimate network's SSID and BSSID to lure clients into connecting to the attacker's AP, enabling credential capture or man-in-the-middle interception of decrypted traffic

**Distractor Analysis:**

- *Why B is correct:* These are complementary but distinct techniques. Deauthentication is active interference (sending forged 802.11 management frames) to disrupt client connectivity or force handshake capture. A rogue AP creates a new access point with the same SSID (and optionally BSSID) as the legitimate network, hoping clients auto-connect and either submit credentials (captive portal) or have their traffic intercepted.
- *Why A is incorrect:* Both attacks typically require root/admin privileges on Linux for raw 802.11 frame injection. Neither has a privilege distinction over the other.
- *Why C is incorrect:* Both deauthentication attacks and rogue AP attacks work against WPA2 networks. In fact, WEP networks are rarely deployed in modern environments. Rogue APs are especially useful against WPA2-Enterprise environments where credential capture is possible.
- *Why D is incorrect:* Both attacks require physical proximity to the target wireless network. Wireless signals have limited range — both techniques require the attacker to be within the target's RF coverage area.

---

**Question 13**

During a wireless assessment, a tester identifies an open network (no encryption) at a target organization. A client device is connected and browsing HTTP sites. Which tool and technique enables the tester to intercept and read the cleartext HTTP traffic?

- A) aircrack-ng — it decrypts WPA2 traffic after capturing the four-way handshake
- B) Wireshark in monitor mode on the appropriate channel — open networks transmit all frames unencrypted and Wireshark can decode HTTP content from captured 802.11 data frames
- C) Nmap — it passively captures HTTP sessions on wireless interfaces without frame injection
- D) Metasploit's `auxiliary/sniff/psnuffle` — it requires WPA2-Enterprise credentials to access the captured frames

**Correct Answer:** B) Wireshark in monitor mode on the appropriate channel — open networks transmit all frames unencrypted and Wireshark can decode HTTP content from captured 802.11 data frames

**Distractor Analysis:**

- *Why B is correct:* Open networks (no authentication, no encryption) transmit all 802.11 data frames in plaintext. An attacker in monitor mode on the same channel can passively capture all frames. Wireshark can decode HTTP sessions from captured 802.11 data, revealing URLs, cookies, form data, and plaintext HTTP content without any active injection.
- *Why A is incorrect:* aircrack-ng is used to crack WPA/WPA2 PSKs from captured handshakes. Open networks have no encryption — there is no handshake to capture and nothing to crack. The traffic is already unencrypted.
- *Why C is incorrect:* Nmap is a port scanner and enumeration tool — it does not passively capture wireless frames or reconstruct HTTP sessions. Network traffic capture is performed by tools like Wireshark, tcpdump, or airodump-ng.
- *Why D is incorrect:* `psnuffle` is a network credential sniffer, but it does not require WPA2-Enterprise credentials to capture frames. It operates on already-accessible network traffic. The description is inaccurate.

---

**Question 14**

A tester discovers a Bluetooth device in discovery mode near a target facility. They use `btlejuice` or `hciconfig hci0 up` and `hcitool scan` to enumerate nearby devices. Which additional tool is specifically designed for Bluetooth Low Energy (BLE) GATT attribute enumeration?

- A) `airodump-ng` — it captures Bluetooth advertising frames on the 2.4 GHz spectrum
- B) `gatttool` or `bettercap`'s BLE module — these tools connect to BLE devices and enumerate GATT services, characteristics, and descriptors that may expose device configuration, sensor data, or control interfaces
- C) `reaver` — it performs GATT PIN brute force against BLE pairing
- D) `hashcat` — it cracks BLE device PINs from captured pairing handshakes

**Correct Answer:** B) `gatttool` or `bettercap`'s BLE module — these tools connect to BLE devices and enumerate GATT services, characteristics, and descriptors that may expose device configuration, sensor data, or control interfaces

**Distractor Analysis:**

- *Why B is correct:* GATT (Generic Attribute Profile) defines how BLE devices expose data and functionality through services and characteristics. `gatttool` and bettercap's BLE module specifically enumerate GATT hierarchies: `gatttool -b <MAC> --primary` lists services, `--characteristics` lists characteristics, and `--char-read` reads values. Unprotected GATT characteristics can expose sensitive data, device control commands, or misconfigured authentication bypass.
- *Why A is incorrect:* airodump-ng captures 802.11 Wi-Fi frames, not Bluetooth. While both operate on the 2.4 GHz spectrum, they use incompatible protocols and different capture mechanisms.
- *Why C is incorrect:* `reaver` performs WPS PIN brute force against Wi-Fi access points. It has no functionality for Bluetooth or BLE pairing attacks.
- *Why D is incorrect:* Hashcat is an offline password hash cracking tool. BLE pairing PIN attacks involve live protocol interactions, not hash cracking. Classic Bluetooth pairing PINs can be attacked with specialized tools but hashcat is not designed for this purpose.

---

**Question 15**

Which legal requirement differentiates wireless penetration testing from wired network testing in most U.S. jurisdictions?

- A) Wireless testing requires a Federal Communications Commission (FCC) license for every test
- B) Wireless testing requires the tester to notify all other wireless users on adjacent channels before beginning
- C) Wireless signals propagate beyond physical boundaries — a tester must confirm that their authorized test network does not bleed into adjacent properties where testing is unauthorized, and must ensure scope authorization explicitly covers the wireless medium
- D) Wireless testing is exempt from CFAA requirements because wireless networks are publicly accessible by design

**Correct Answer:** C) Wireless signals propagate beyond physical boundaries — a tester must confirm that their authorized test network does not bleed into adjacent properties where testing is unauthorized, and must ensure scope authorization explicitly covers the wireless medium

**Distractor Analysis:**

- *Why C is correct:* Unlike wired testing where physical cable access can be controlled, wireless signals radiate through walls and may reach neighboring businesses or residences that have not authorized testing. A tester who captures packets from or sends deauthentication frames toward unauthorized networks (even accidentally) may violate the CFAA and the Electronic Communications Privacy Act. Scope authorization must explicitly include wireless and specify which SSIDs and BSSIDs are in scope.
- *Why A is incorrect:* Penetration testers do not require FCC licenses for standard wireless testing tools on unlicensed spectrum (2.4 GHz, 5 GHz). FCC licensing requirements apply to radio transmission equipment operators in licensed bands.
- *Why B is incorrect:* No legal requirement mandates notifying other wireless users before testing. The requirement is to have proper authorization from the target network owner, not to notify third parties on adjacent channels.
- *Why D is incorrect:* CFAA applies to wireless networks. Publicly accessible transmission does not grant authorization to intercept, disrupt, or attack wireless networks. The ECPA and CFAA explicitly cover unauthorized interception of radio communications.

---

**Question 16**

A tester captures a WPA2-Personal handshake and converts it for Hashcat processing using `hcxpcapngtool`. The resulting file is in `.hc22000` format. What does Hashcat mode `22000` specifically target?

- A) WEP 64-bit key cracking using RC4 stream cipher weaknesses
- B) WPA-PBKDF2-PMKID+EAPOL — mode 22000 handles both PMKID captures and EAPOL four-way handshakes in a unified format for WPA/WPA2 PSK recovery
- C) WPA2-Enterprise RADIUS shared secret cracking
- D) Bluetooth PIN brute force from captured BLE pairing handshakes

**Correct Answer:** B) WPA-PBKDF2-PMKID+EAPOL — mode 22000 handles both PMKID captures and EAPOL four-way handshakes in a unified format for WPA/WPA2 PSK recovery

**Distractor Analysis:**

- *Why B is correct:* Hashcat mode 22000 was introduced to replace the older modes 2500 (EAPOL) and 16800 (PMKID) with a single unified format. The `.hc22000` file produced by `hcxpcapngtool` contains both PMKID and EAPOL handshake data. The cracking process uses PBKDF2-SHA1 with the SSID as the salt to derive the PMK and verify it against the captured material.
- *Why A is incorrect:* WEP cracking uses entirely different Hashcat modes (or aircrack-ng's statistical attack methods). WEP uses RC4 and is not cracked via PBKDF2. Mode 22000 does not apply to WEP.
- *Why C is incorrect:* WPA2-Enterprise uses 802.1X/EAP authentication with individual user credentials processed by a RADIUS server. There is no PSK to crack. Mode 22000 targets PSK-based WPA/WPA2.
- *Why D is incorrect:* Hashcat mode 22000 is specifically for WPA/WPA2 PSK. Bluetooth PIN attacks use different tools and attack approaches. Hashcat has no dedicated BLE mode.

---

**Question 17**

During a wireless assessment, the tester's airodump-ng output shows a device with BSSID `AA:BB:CC:DD:EE:FF` transmitting on multiple channels simultaneously and with an abnormally high beacon rate. What does this suggest?

- A) The device is a legitimate dual-band access point operating on both 2.4 GHz and 5 GHz simultaneously
- B) The device may be a rogue AP or Wi-Fi pineapple broadcasting on multiple channels to respond to probe requests from clients seeking any network, a technique used to intercept auto-connecting devices
- C) Multi-channel transmission indicates the AP is misconfigured and poses no security risk
- D) The device is a wired access point with a faulty firmware causing channel instability

**Correct Answer:** B) The device may be a rogue AP or Wi-Fi pineapple broadcasting on multiple channels to respond to probe requests from clients seeking any network, a technique used to intercept auto-connecting devices

**Distractor Analysis:**

- *Why B is correct:* Legitimate APs broadcast on a fixed channel (or two fixed channels for dual-band). A device appearing on multiple channels with a high beacon rate is consistent with a Wi-Fi Pineapple or similar rogue AP device that responds to clients' probe requests by broadcasting SSID beacons across channels. This is the primary indicator of a mass-interception rogue AP in the environment — a significant finding in a wireless assessment.
- *Why A is incorrect:* Dual-band APs transmit on separate channels for 2.4 GHz and 5 GHz bands, but each band uses a single fixed channel. They do not hop across multiple channels within a single band.
- *Why C is incorrect:* Multi-channel transmission is not a normal AP behavior. It is a specific indicator of deliberate rogue AP activity, not a harmless misconfiguration.
- *Why D is incorrect:* A wired AP with faulty firmware would show channel instability on a single channel or drop off the air — it would not systematically appear on all channels simultaneously. Multi-channel presence is characteristic of active rogue AP operation.

---

**Question 18**

A penetration tester successfully cracks a WPA2 PSK and connects to the target wireless network. What is the appropriate next step in a professional engagement?

- A) Immediately attempt to access the internet through the cracked network to confirm connectivity
- B) Document the recovered PSK and connection success as a finding, then conduct authorized post-connection enumeration per the RoE — such as network scanning for internal hosts, identifying VLAN segmentation, and testing for access to sensitive internal resources
- C) Share the PSK with all other testers on the engagement to enable simultaneous testing from multiple wireless clients
- D) The engagement is complete once the PSK is cracked — wireless testing ends at credential recovery

**Correct Answer:** B) Document the recovered PSK and connection success as a finding, then conduct authorized post-connection enumeration per the RoE — such as network scanning for internal hosts, identifying VLAN segmentation, and testing for access to sensitive internal resources

**Distractor Analysis:**

- *Why B is correct:* PSK recovery is the proof of the wireless vulnerability, but its business impact is demonstrated by showing what an attacker can reach once connected. Authorized post-connection enumeration — identifying internal hosts, verifying network segmentation, testing for access to sensitive services — transforms a "cracked password" finding into a "full network access" finding with documented business impact.
- *Why A is incorrect:* Internet access through a client's corporate network is not the objective of the assessment and may generate external traffic that is out of scope or could create legal liability.
- *Why C is incorrect:* Sharing credentials within the engagement team may be appropriate for coordination, but wireless credentials from a production client network must be handled per the data handling provisions of the RoE and NDA — not casually distributed.
- *Why D is incorrect:* PSK recovery demonstrates the vulnerability but not its full impact. A wireless assessment should demonstrate what an unauthorized user can access once connected, not stop at credential recovery.

---

**Question 19**

Which countermeasure most directly prevents offline dictionary attacks against WPA2-Personal handshakes?

- A) Enabling WPS on all access points to force certificate-based authentication
- B) Implementing a network intrusion detection system (IDS) to detect deauthentication attacks
- C) Using a long, random, complex passphrase (20+ characters from a mixed character set) that is not present in any known wordlist and cannot be recovered through rule-based mutations
- D) Disabling SSID broadcast to prevent attackers from discovering the network name

**Correct Answer:** C) Using a long, random, complex passphrase (20+ characters from a mixed character set) that is not present in any known wordlist and cannot be recovered through rule-based mutations

**Distractor Analysis:**

- *Why C is correct:* The WPA2-Personal handshake is always capturable by a passive attacker. The only defense against offline cracking is passphrase strength — a 20+ character random passphrase has a search space that makes brute force computationally infeasible even with GPU clusters. No amount of IDS or SSID hiding protects a weak passphrase once the handshake is captured.
- *Why A is incorrect:* WPS introduces additional attack surface — the WPS PIN is only 8 digits and is vulnerable to Reaver-style brute force attacks. Enabling WPS makes the network weaker, not stronger. WPS does not enforce certificate-based authentication.
- *Why B is incorrect:* An IDS detecting deauthentication attacks can alert defenders but does not prevent handshake capture or offline cracking. A passive attacker who simply waits for a legitimate client to authenticate captures the handshake without sending any deauth frames.
- *Why D is incorrect:* Hidden SSIDs are trivially discoverable — probe requests from connected clients reveal the SSID regardless. SSID hiding provides no meaningful security against a determined attacker and does not affect offline cracking of captured handshakes.

---

**Question 20**

During a wireless engagement, a tester captures probe requests from a client device looking for the SSID `CorpGuest`. The legitimate CorpGuest network is a WPA2 guest network. The tester sets up a rogue AP named `CorpGuest` with open authentication and a captive portal that requests the WPA2 guest password. A user connects and submits the password. What legal and ethical considerations govern this technique?

- A) This technique is always legal because the guest network is publicly accessible and credentials are voluntarily submitted
- B) Captive portal credential harvesting is legal only if the victim consents to the test by clicking "I agree" on the portal page
- C) This technique constitutes unauthorized access to user credentials and impersonation of the legitimate network; it must be explicitly authorized in the RoE with informed consent provisions — many engagement contracts prohibit social engineering attacks or require specific authorization separate from the general pentest scope
- D) The technique is legal because no actual network access is required — only the rogue AP is used

**Correct Answer:** C) This technique constitutes unauthorized access to user credentials and impersonation of the legitimate network; it must be explicitly authorized in the RoE with informed consent provisions — many engagement contracts prohibit social engineering attacks or require specific authorization separate from the general pentest scope

**Distractor Analysis:**

- *Why C is correct:* Capturing user credentials through a rogue AP captive portal is a social engineering technique targeting employees or guests — not just the technical network infrastructure. It may violate ECPA, CFAA, and state fraud statutes if not explicitly authorized. Even if the technical wireless attack (rogue AP setup) is authorized, credential harvesting from users who are not informed test participants requires explicit authorization and careful scoping in the RoE.
- *Why A is incorrect:* Publicly accessible networks do not grant authorization for credential harvesting attacks. Voluntarily submitting credentials to a fraudulent portal is fraud from the attacker's perspective regardless of the user's voluntary action.
- *Why B is incorrect:* A "consent" checkbox on an attacker-controlled captive portal does not constitute legal consent to credential collection. Informed consent for security testing must come from the organization's authorized representative, not from victims clicking through a deceptive portal.
- *Why D is incorrect:* The legal exposure is not determined by whether actual network access occurs — it is determined by whether credential collection and network impersonation are authorized activities under the engagement contract and applicable law.

---

*End of Module 11 Quiz*
