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

### Question 11

Which 802.11 standard introduced MU-MIMO (Multi-User MIMO) and operates exclusively in the 5 GHz band, achieving theoretical maximum speeds up to 3.5 Gbps?

- A) 802.11n (Wi-Fi 4)
- B) 802.11ac (Wi-Fi 5)
- C) 802.11ax (Wi-Fi 6)
- D) 802.11g

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* 802.11n (Wi-Fi 4) introduced MIMO but operates on both 2.4 GHz and 5 GHz. Its maximum speed is 600 Mbps and it does not support MU-MIMO — it uses SU-MIMO (single-user).
- *Why B is correct:* 802.11ac (Wi-Fi 5) introduced MU-MIMO for downlink, operates exclusively on the 5 GHz band, and can achieve up to 3.5 Gbps theoretical maximum using 160 MHz channels and 8 spatial streams.
- *Why C is incorrect:* 802.11ax (Wi-Fi 6) improved on 802.11ac with OFDMA and full MU-MIMO (uplink and downlink), but Wi-Fi 6 operates on both 2.4 GHz and 5 GHz — it is not exclusively 5 GHz like 802.11ac.
- *Why D is incorrect:* 802.11g is a legacy 2.4 GHz-only standard with a maximum speed of 54 Mbps. It predates MIMO technology entirely.

---

### Question 12

An enterprise wireless network uses WPA2-Enterprise instead of WPA2-Personal. Which additional infrastructure component is required to support WPA2-Enterprise authentication?

- A) A wireless LAN controller (WLC)
- B) A RADIUS server for 802.1X authentication
- C) A DHCP server with a dedicated wireless scope
- D) An additional SSID for the authentication traffic

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A wireless LAN controller manages and configures multiple APs centrally — it is not inherently required for WPA2-Enterprise, though it may be used alongside it.
- *Why B is correct:* WPA2-Enterprise uses 802.1X, which requires a RADIUS (Remote Authentication Dial-In User Service) server to authenticate each user's individual credentials before granting wireless access. Each user presents their own username and password or certificate.
- *Why C is incorrect:* A DHCP server assigns IP addresses to connected clients but is required for any DHCP-based network — it is not specific to WPA2-Enterprise authentication.
- *Why D is incorrect:* A separate SSID for authentication traffic is not part of the WPA2-Enterprise architecture. Authentication occurs on the same SSID via the 802.1X EAP exchange.

---

### Question 13

A wireless client is successfully authenticated and connected to an AP. The client is then suddenly disconnected. In a Wireshark capture, the last frame observed before disconnection is a deauthentication frame with reason code 7 (Class 3 frame received from nonassociated client). Which type of attack likely caused this disconnection?

- A) A WPA2 KRACK (Key Reinstallation Attack)
- B) A wireless deauthentication (de-auth flood) attack
- C) An Evil Twin AP with a stronger signal
- D) A WPS brute-force PIN attack

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* KRACK attacks manipulate the WPA2 four-way handshake to reinstall an already-in-use key, enabling decryption of traffic. They do not generate deauthentication frames that terminate connections.
- *Why B is correct:* A deauthentication flood attack involves sending spoofed 802.11 deauthentication frames (using the AP's MAC address as the source) to targeted clients. Since management frames in 802.11 were historically unprotected, clients honored these frames and disconnected. 802.11w Management Frame Protection mitigates this.
- *Why C is incorrect:* An Evil Twin AP causes clients to associate with the rogue AP — this involves a reassociation event, not a deauthentication frame with reason code 7.
- *Why D is incorrect:* WPS PIN brute-force attacks target the WPS registration process over multiple PIN attempts. They do not cause sudden client disconnections via deauthentication frames.

---

### Question 14

Which wireless encryption protocol uses CCMP (Counter Mode CBC-MAC Protocol) based on AES as its encryption mechanism, providing significantly stronger security than TKIP?

- A) WEP
- B) WPA (WPA1)
- C) WPA2
- D) WPA3

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* WEP uses RC4 stream cipher with a static key — it has no AES or CCMP component and is considered completely insecure.
- *Why B is incorrect:* WPA (WPA1) introduced TKIP (Temporal Key Integrity Protocol) as a replacement for WEP's RC4 weakness. TKIP is an improvement over WEP but does not use AES/CCMP.
- *Why C is correct:* WPA2 (IEEE 802.11i) mandated CCMP/AES as its primary encryption mechanism. CCMP uses AES in counter mode for encryption and CBC-MAC for message integrity, providing significantly stronger security than TKIP.
- *Why D is incorrect:* WPA3 builds on WPA2's AES/CCMP foundation and adds SAE (Simultaneous Authentication of Equals) for improved key exchange, but CCMP/AES was introduced in WPA2, not WPA3.

---

### Question 15

A network administrator is planning the wireless channel layout for a building with six access points using the 2.4 GHz band. Which channel assignments ensure that no two adjacent APs cause co-channel interference?

- A) Channels 1, 2, and 3 in rotation
- B) Channels 1, 6, and 11 in rotation
- C) Channels 1, 5, and 9 in rotation
- D) Channels 6, 7, and 8 in rotation

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Channels 1, 2, and 3 overlap heavily — they are only 5 MHz apart and a 2.4 GHz channel is 22 MHz wide. Adjacent-channel interference would be severe.
- *Why B is correct:* Channels 1, 6, and 11 are the only three non-overlapping channels in the 2.4 GHz band in North America. They are spaced 25 MHz apart, completely avoiding overlap. Rotating these three channels across adjacent APs eliminates co-channel interference.
- *Why C is incorrect:* Channels 1, 5, and 9 are spaced 20 MHz apart — they still have slight overlap since channels are 22 MHz wide. This is an improvement over sequential channels but not truly non-overlapping.
- *Why D is incorrect:* Channels 6, 7, and 8 are adjacent channels with massive overlap — they would cause severe co-channel interference if used on neighboring APs.

---

### Question 16

A company deploys a Wireless Intrusion Prevention System (WIPS). What is the primary function of a WIPS in an enterprise wireless environment?

- A) To encrypt all wireless traffic before it reaches the wired network
- B) To automatically assign IP addresses to wireless clients as a replacement for DHCP
- C) To detect and respond to rogue APs, unauthorized clients, and wireless attacks such as deauthentication floods
- D) To aggregate multiple SSIDs into a single management VLAN

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Traffic encryption is handled by the wireless security protocol (WPA2/WPA3) at the AP level. A WIPS monitors the radio frequency environment — it does not perform encryption.
- *Why B is incorrect:* DHCP is a separate Layer 3 service. A WIPS operates in the RF/Layer 2 domain monitoring for unauthorized devices and attacks.
- *Why C is correct:* A WIPS passively or actively monitors the RF environment for rogue APs (unauthorized APs on the network), unauthorized clients, and attack signatures (deauthentication floods, Evil Twin APs, WPS attacks). When detected, a WIPS can alert administrators or take active containment measures.
- *Why D is incorrect:* SSID and VLAN management is a function of the wireless LAN controller or AP configuration system — not a WIPS.

---

### Question 17

What is the maximum theoretical data rate for 802.11ax (Wi-Fi 6) on a single spatial stream using 80 MHz channels with 1024-QAM?

- A) 54 Mbps
- B) 300 Mbps
- C) 600 Mbps
- D) 1.2 Gbps

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* 54 Mbps is the maximum data rate for 802.11a/g (OFDM, 64-QAM, 54 Mbps per stream) — the pre-MIMO era standard.
- *Why B is incorrect:* 300 Mbps is a common 802.11n rate for 2 spatial streams with 40 MHz channels — not 802.11ax.
- *Why C is incorrect:* 600 Mbps is the theoretical maximum for 802.11n with 4 spatial streams at 40 MHz — not 802.11ax.
- *Why D is correct:* 802.11ax (Wi-Fi 6) introduced 1024-QAM and improved OFDMA subcarrier efficiency, achieving approximately 1.2 Gbps on a single spatial stream with an 80 MHz channel. The full multi-stream aggregate rate reaches up to 9.6 Gbps.

---

### Question 18

An administrator notices that a wireless client associates with an AP but then is immediately denied network access by a policy server. Which 802.1X component is responsible for enforcing this access decision?

- A) The SSID (Supplicant)
- B) The RADIUS server (Authentication Server)
- C) The Access Point (Authenticator)
- D) The wireless client NIC (Authentication Server)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The SSID is a network name, not an 802.1X component. In 802.1X, the supplicant is the client device requesting network access.
- *Why B is incorrect:* The RADIUS server (Authentication Server) verifies credentials and sends an Access-Accept or Access-Reject message — but it is the Authenticator that physically enforces the decision by opening or keeping closed the controlled port.
- *Why C is correct:* In 802.1X, the Access Point acts as the Authenticator. It maintains a controlled port (blocked) and an uncontrolled port (open for EAP traffic only). After receiving the RADIUS Access-Accept message, the Authenticator opens the controlled port, granting network access. If the RADIUS server rejects, the AP keeps the port blocked.
- *Why D is incorrect:* The wireless client NIC is the Supplicant — it provides credentials. It is not the Authentication Server, which is the RADIUS server role.

---

### Question 19

Which wireless feature introduced in 802.11ax (Wi-Fi 6) allows an AP to divide its channel into smaller sub-channels and serve multiple clients simultaneously, improving efficiency in high-density environments?

- A) MU-MIMO
- B) OFDMA (Orthogonal Frequency Division Multiple Access)
- C) Beamforming
- D) WPA3-SAE

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* MU-MIMO (Multi-User MIMO) was introduced in 802.11ac and uses multiple antenna streams to serve multiple clients. It is a spatial multiplexing technique, not a sub-channel frequency division technique.
- *Why B is correct:* OFDMA divides a wireless channel into smaller sub-channels called Resource Units (RUs), allowing an 802.11ax AP to simultaneously serve multiple clients on different RUs within the same channel. This greatly improves efficiency in dense environments compared to one client per transmission slot.
- *Why C is incorrect:* Beamforming focuses the AP's radio signal toward a specific client to improve signal strength and reduce interference. It does not divide the channel for multiple simultaneous clients.
- *Why D is incorrect:* WPA3-SAE (Simultaneous Authentication of Equals) is a security protocol improvement for wireless authentication. It is unrelated to RF channel access efficiency.

---

### Question 20

A site survey reveals that a deployed 5 GHz wireless AP is experiencing significant co-channel interference from a neighboring organization's AP using the same 5 GHz channel. What is the recommended corrective action?

- A) Switch the AP to WPA2-Enterprise to filter the neighboring organization's traffic.
- B) Reconfigure the AP to use a non-overlapping 5 GHz channel not used by the neighboring AP.
- C) Reduce the AP's transmit power to maximum to overpower the neighboring AP.
- D) Change the AP's SSID to match the neighboring AP's SSID to absorb its traffic.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* WPA2-Enterprise provides authentication and encryption — it does not affect RF channel selection or interference between APs operating on the same channel.
- *Why B is correct:* Co-channel interference occurs when two APs on the same channel overlap in coverage area. The solution is to select a different non-overlapping channel for the affected AP. The 5 GHz band offers many non-overlapping 20 MHz channels (up to 25 in the U.S.), providing significant flexibility.
- *Why C is incorrect:* Increasing transmit power would worsen the interference by expanding the AP's coverage area into more of the neighboring AP's territory. It would not resolve the co-channel interference.
- *Why D is incorrect:* Matching another organization's SSID would create an Evil Twin scenario, causing both organizations' clients to associate randomly with both APs — this would be both an attack and a severe operational failure.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
