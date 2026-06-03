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

*End of Module 11 Quiz*
