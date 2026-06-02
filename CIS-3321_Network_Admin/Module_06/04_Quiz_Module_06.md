# Quiz: Module 06 – Wireless Networking: 802.11 Standards and Security

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

Instructions: Select the best answer for each question. Each question is worth 10 points (100 points total).

---

### Question 1

A network engineer is deploying wireless access points in a high-density auditorium where hundreds of devices will connect simultaneously. Which 802.11 standard and its key technology are best suited for efficient multi-client handling in this environment?

A) 802.11b — uses DSSS spread spectrum to maximize range across the 2.4 GHz band

B) 802.11g — backward compatible with 802.11b and supports up to 54 Mbps

C) 802.11ax (Wi-Fi 6) — uses OFDMA to divide channels into sub-carriers, serving multiple clients simultaneously with reduced contention

D) 802.11ac (Wi-Fi 5) — uses beamforming to direct the signal toward a single high-priority client

- Correct Answer: C) 802.11ax (Wi-Fi 6) — uses OFDMA to divide channels into sub-carriers, serving multiple clients simultaneously with reduced contention
- Distractor Analysis:
  - Why A is incorrect: 802.11b operates at only 11 Mbps and has no multi-client efficiency features; it would create severe congestion in a high-density environment.
  - Why B is incorrect: 802.11g is a legacy 54 Mbps standard with no mechanism for simultaneous multi-client scheduling; it uses CSMA/CA contention like all pre-ax standards.
  - Why C is correct: OFDMA (Orthogonal Frequency Division Multiple Access), introduced by 802.11ax, divides each channel into sub-carriers called Resource Units and allows the AP to serve multiple clients in a single transmission cycle — the key design advantage for dense environments.
  - Why D is incorrect: 802.11ac beamforming focuses signal toward a single client for better throughput — it does not address multi-client density the way OFDMA does.

---

### Question 2

A security analyst discovers that an access point is using RC4 encryption with a static 40-bit key that has been cracked in under five minutes using freely available tools. Which wireless security protocol is in use, and what is the correct replacement?

A) WPA-TKIP — replace with WPA2-AES-CCMP or WPA3-SAE for current minimum standards

B) WEP (Wired Equivalent Privacy) — replace with WPA2-AES-CCMP or WPA3-SAE immediately

C) WPA3-SAE — replace with WPA2-Enterprise using 802.1X/RADIUS for backward compatibility

D) WPA2-CCMP — replace with WPA-TKIP to restore compatibility with legacy client devices

- Correct Answer: B) WEP (Wired Equivalent Privacy) — replace with WPA2-AES-CCMP or WPA3-SAE immediately
- Distractor Analysis:
  - Why A is incorrect: WPA-TKIP also uses RC4 but adds per-packet key mixing; it does not use a static 40-bit key. The static key and sub-5-minute crack time are the signature fingerprints of WEP.
  - Why B is correct: WEP uses RC4 with static 40-bit or 104-bit keys and short initialization vectors that repeat frequently. This allows an attacker to collect enough traffic to mathematically reconstruct the key in minutes. WEP must be replaced immediately with WPA2-AES-CCMP at minimum, or WPA3-SAE.
  - Why C is incorrect: WPA3-SAE uses Simultaneous Authentication of Equals with Diffie-Hellman key exchange — it does not use RC4 or static keys, and it is not crackable by the method described.
  - Why D is incorrect: WPA2-CCMP uses AES, not RC4, and is not crackable by the method described. Downgrading to WPA-TKIP would be a security regression, not an improvement.

---

### Question 3

A wireless technician is deploying three access points in a small office that all operate in the 2.4 GHz band. To prevent co-channel interference between neighboring APs, which channel assignments are correct?

A) Channels 1, 2, and 3 — these are the lowest available channels in the 2.4 GHz band

B) Channels 1, 6, and 11 — the only three non-overlapping channels in the US 2.4 GHz band

C) Channels 3, 7, and 11 — evenly spaced throughout the 2.4 GHz spectrum

D) Channels 6, 11, and 14 — channel 14 is available for high-density deployments in the US

- Correct Answer: B) Channels 1, 6, and 11 — the only three non-overlapping channels in the US 2.4 GHz band
- Distractor Analysis:
  - Why A is incorrect: Channels 1, 2, and 3 are adjacent and overlap heavily — using them on neighboring APs would cause maximum interference, not prevent it.
  - Why B is correct: In the US 2.4 GHz band, channels are 22 MHz wide and spaced 5 MHz apart. Channels 1, 6, and 11 are separated by 25 MHz, providing the minimum spacing needed to prevent overlap. These are the only three non-overlapping channels available.
  - Why C is incorrect: Channels 3, 7, and 11 are not non-overlapping; channels 3 and 7 overlap with adjacent channels. Only 1, 6, and 11 provide sufficient separation.
  - Why D is incorrect: Channel 14 is not authorized for use in the United States (it is permitted only in Japan for 802.11b); using it in a US deployment would violate FCC regulations.

---

### Question 4

A corporate wireless network currently uses WPA2-Personal (PSK) with a shared passphrase distributed to all employees. The security team reports that a former employee could still decrypt previously captured wireless traffic using the shared key. Which upgrade eliminates this risk?

A) Switch to WPA2-Enterprise with 802.1X/RADIUS authentication so each user has individual credentials that can be revoked without affecting others

B) Increase the WPA2-PSK passphrase length to 20 characters or more to prevent brute-force attacks

C) Enable SSID broadcast hiding so the network name is not visible to unauthorized users

D) Configure MAC address filtering on the access point to block devices not on the approved list

- Correct Answer: A) Switch to WPA2-Enterprise with 802.1X/RADIUS authentication so each user has individual credentials that can be revoked without affecting others
- Distractor Analysis:
  - Why A is correct: WPA2-Enterprise with 802.1X assigns each user unique credentials managed by a RADIUS server. Individual accounts can be revoked without changing the shared key. Upgrading to WPA3-SAE would also provide forward secrecy, preventing decryption of previously captured traffic even if credentials are later compromised.
  - Why B is incorrect: A longer PSK reduces brute-force success but does not solve the core problem — the former employee already knows the passphrase and could still decrypt captured traffic; only rekeying all devices would help, and even then WPA2-PSK lacks forward secrecy.
  - Why C is incorrect: SSID hiding provides no encryption or authentication benefit; clients still broadcast probe requests that reveal the hidden SSID, and the encryption method is unchanged.
  - Why D is incorrect: MAC address filtering is trivially bypassed by spoofing an approved MAC address; it does not change the encryption key or prevent an insider from decrypting captured traffic.

---

### Question 5

A security administrator needs to ensure that wireless clients must authenticate with individual user credentials before gaining network access, and that the wireless management traffic between APs and the controller must be encrypted in transit. Which combination of controls best satisfies both requirements?

A) Deploy WPA2-Enterprise with 802.1X/EAP-TLS for per-user certificate-based authentication and use a CAPWAP tunnel with DTLS encryption for AP-to-controller management traffic.

B) Configure WPA2-Personal with a complex 25-character pre-shared key and enable SSID broadcast suppression on all access points.

C) Enable full disk encryption on all wireless client devices and place all APs on an isolated management VLAN.

D) Deploy a captive portal requiring username and password acceptance before granting internet access, with HTTP-only management access restricted to the wired VLAN.

- Correct Answer: A) Deploy WPA2-Enterprise with 802.1X/EAP-TLS for per-user certificate-based authentication and use a CAPWAP tunnel with DTLS encryption for AP-to-controller management traffic.
- Distractor Analysis:
  - Why A is correct: 802.1X/EAP-TLS provides certificate-based individual user authentication (meeting the per-credential requirement), and CAPWAP with DTLS encrypts the AP-to-controller control plane (meeting the management encryption requirement). Both requirements are satisfied simultaneously.
  - Why B is incorrect: WPA2-PSK uses a shared passphrase — all users share the same credential, which cannot be individually revoked. SSID suppression provides no encryption benefit.
  - Why C is incorrect: Full disk encryption protects data at rest on client devices but does not authenticate users to the wireless network or encrypt management traffic between APs and the controller.
  - Why D is incorrect: A captive portal is used for guest/public networks requiring terms-of-service acceptance — it does not provide credential-based 802.1X authentication. HTTP management access is unencrypted and violates the encryption requirement.

---

### Question 6

An attacker parks outside a corporate office and uses a laptop to set up a wireless access point broadcasting the same SSID as the company's legitimate Wi-Fi network. Unsuspecting employees connect to the attacker's AP and all their traffic is intercepted. Which attack is being described, and what is the most effective technical mitigation?

A) Deauthentication flood attack — mitigated by enabling 802.11w Management Frame Protection on all APs

B) Evil Twin attack — mitigated by deploying WPA2-Enterprise with 802.1X/RADIUS so that connecting to a rogue AP does not expose user credentials

C) War driving attack — mitigated by disabling SSID broadcast on all legitimate access points

D) Captive portal phishing attack — mitigated by enabling WEP on the guest network to prevent sniffing

- Correct Answer: B) Evil Twin attack — mitigated by deploying WPA2-Enterprise with 802.1X/RADIUS so that connecting to a rogue AP does not expose user credentials
- Distractor Analysis:
  - Why A is incorrect: A deauthentication flood forces clients off a legitimate AP using forged deauthentication frames — it is a different attack from an Evil Twin, though attackers sometimes combine them. 802.11w mitigates deauth attacks, not Evil Twins.
  - Why B is correct: An Evil Twin (rogue AP) impersonates a legitimate SSID to intercept traffic. WPA2-Enterprise with 802.1X prevents credential capture because the authentication is mutual — the RADIUS server presents a certificate that the client validates, making it detectable if the rogue AP lacks the legitimate certificate.
  - Why C is incorrect: Disabling SSID broadcast provides no protection against an Evil Twin; the attacker knows the SSID and can broadcast it from their rogue AP regardless.
  - Why D is incorrect: WEP is completely broken and would provide no protection. Enabling WEP on any network is a security regression, not a mitigation.

---

### Question 7

A network administrator observes that wireless clients are repeatedly disconnecting from the corporate AP during business hours. A wireless packet capture reveals a flood of 802.11 management frames with the reason code "deauthentication." No hardware failure is found. Which attack is occurring and what is the correct mitigation?

A) An Evil Twin attack is broadcasting a stronger signal; the mitigation is to increase transmit power on the legitimate AP.

B) A deauthentication flood attack is in progress using forged management frames; the mitigation is to enable 802.11w Management Frame Protection.

C) WPA2-PSK passphrase cracking is causing client disconnections; the mitigation is to extend the passphrase to 25 characters.

D) Co-channel interference from a neighboring AP is causing client drops; the mitigation is to change the channel assignment to avoid overlap.

- Correct Answer: B) A deauthentication flood attack is in progress using forged management frames; the mitigation is to enable 802.11w Management Frame Protection.
- Distractor Analysis:
  - Why A is incorrect: An Evil Twin creates a competing AP — it does not cause a flood of deauthentication management frames at the packet capture level. Increasing transmit power does not authenticate management frames.
  - Why B is correct: In 802.11 standards prior to 802.11w, management frames (including deauthentication) are not authenticated. An attacker can forge deauthentication frames with the source address of the legitimate AP, forcing all clients to disconnect. 802.11w (Management Frame Protection) cryptographically authenticates management frames, defeating this attack.
  - Why C is incorrect: WPA2-PSK cracking is an offline attack on a captured handshake — it does not cause client disconnections in real time. The symptom described is a flood of management frames, which is characteristic of a deauth flood.
  - Why D is incorrect: Co-channel interference causes performance degradation and retransmissions, not a flood of deauthentication management frames from a specific source.

---

### Question 8

A university is upgrading its wireless network and wants to ensure that previously captured wireless traffic cannot be decrypted even if the network passphrase is compromised in the future. Which wireless security standard provides this capability, and what is the name of the property it offers?

A) WPA2-Personal (PSK) — provides backward secrecy by rotating keys every 30 minutes using TKIP

B) WPA3-Personal using SAE — provides forward secrecy because each session derives a unique key that cannot be reconstructed from the passphrase alone

C) WPA2-Enterprise with 802.1X — provides forward secrecy because the RADIUS server re-issues new certificates after each authentication

D) WEP with a 104-bit key — provides forward secrecy because the longer key increases the time required to crack any single session

- Correct Answer: B) WPA3-Personal using SAE — provides forward secrecy because each session derives a unique key that cannot be reconstructed from the passphrase alone
- Distractor Analysis:
  - Why A is incorrect: WPA2-PSK does not provide forward secrecy. If an attacker captures the 4-way handshake and later learns the passphrase, they can derive the session key and decrypt all captured traffic. Key rotation in WPA2-PSK does not protect past sessions.
  - Why B is correct: WPA3 uses SAE (Simultaneous Authentication of Equals), based on the Dragonfly key exchange. SAE derives a unique session key for every connection. Even if the passphrase is later compromised, an attacker cannot reconstruct past session keys — this is the property called forward secrecy.
  - Why C is incorrect: WPA2-Enterprise with EAP-TLS can provide forward secrecy if the EAP method uses ephemeral Diffie-Hellman, but this is not guaranteed by 802.1X itself. The answer incorrectly describes certificate re-issuance as the mechanism.
  - Why D is incorrect: WEP is completely broken regardless of key length. A 104-bit WEP key is still crackable in minutes due to IV reuse. WEP provides no forward secrecy.

---

### Question 9

A wireless network uses a single access point that serves all connected clients. A second building requires wireless coverage under the same SSID so employees can roam between buildings without reconnecting. What wireless architecture is required for the second building, and what is the term for the combined multi-AP network?

A) Add a second AP with a different SSID in the second building; this creates an Independent Basic Service Set (IBSS) between the buildings.

B) Add a second AP configured with the same SSID and a unique BSSID; this extends the network into an Extended Service Set (ESS).

C) Add a second AP and configure it to operate as an ad-hoc node; this creates a Mesh Basic Service Set automatically.

D) Add a second AP with a different SSID and different channel; this creates a new BSS that clients can join by selecting the correct SSID manually.

- Correct Answer: B) Add a second AP configured with the same SSID and a unique BSSID; this extends the network into an Extended Service Set (ESS).
- Distractor Analysis:
  - Why A is incorrect: An IBSS (Independent Basic Service Set) is an ad-hoc network where devices communicate directly without an AP. A second SSID in the second building would require employees to manually connect to a different network name — defeating the roaming requirement.
  - Why B is correct: An Extended Service Set (ESS) consists of multiple access points sharing the same SSID but with unique BSSIDs (each AP's MAC address). Clients can roam between APs transparently because the network name is the same. This is the standard enterprise wireless roaming architecture.
  - Why C is incorrect: Ad-hoc mode creates a peer-to-peer network without infrastructure — it does not provide AP-based roaming.
  - Why D is incorrect: Using a different SSID defeats the seamless roaming requirement. Employees would have to manually disconnect from one SSID and connect to another when moving between buildings.

---

### Question 10

A network technician receives a trouble ticket stating that several users on the wireless network have been redirected to a web page asking them to re-enter their username and password before accessing the internet. The IT team did not deploy this page. Which attack is described, and what is the primary risk?

A) A deauthentication flood attack is occurring; the risk is that clients will be forced offline permanently until the attack stops.

B) A captive portal phishing attack is occurring; the risk is that users will submit their real credentials to an attacker-controlled web page.

C) An 802.11w Management Frame Protection misconfiguration is redirecting clients; the risk is that management frames are being dropped.

D) A WIPS false-positive detection is blocking clients; the risk is that legitimate APs are being quarantined incorrectly.

- Correct Answer: B) A captive portal phishing attack is occurring; the risk is that users will submit their real credentials to an attacker-controlled web page.
- Distractor Analysis:
  - Why A is incorrect: A deauthentication flood disconnects clients from the AP — it does not redirect them to a web page. The symptom described (credential entry prompt) is not characteristic of a deauth attack.
  - Why B is correct: A captive portal phishing attack uses a rogue AP or DNS hijacking to present a fake login page that mimics a legitimate one. Users who enter credentials hand them directly to the attacker. The unexpected appearance of a credential prompt that the IT team did not deploy is the key indicator.
  - Why C is incorrect: 802.11w Management Frame Protection is an AP/client configuration setting that operates at the frame level — it does not cause browser redirections to credential-entry pages.
  - Why D is incorrect: A WIPS quarantine would block clients from connecting to a suspicious AP entirely — it would not redirect them to a web page asking for credentials.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
