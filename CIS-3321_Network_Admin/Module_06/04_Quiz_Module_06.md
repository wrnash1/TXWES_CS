# Quiz: Module 06 - Wireless Networking – 802.11 Standards and Security
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A network engineer is deploying wireless access points in a high-density auditorium where hundreds of devices will connect simultaneously. Which 802.11 standard and its key technology are best suited for efficient multi-client handling in this environment?
A) 802.11b — uses DSSS spread spectrum to maximize range across the 2.4 GHz band
B) 802.11g — backward compatible with 802.11b and supports up to 54 Mbps
C) 802.11ax (Wi-Fi 6) — uses OFDMA to divide channels into sub-carriers, serving multiple clients simultaneously with reduced contention
D) 802.11ac (Wi-Fi 5) — uses beamforming to direct the signal toward a single high-priority client
*   **Correct Answer:** C) 802.11ax (Wi-Fi 6) — uses OFDMA to divide channels into sub-carriers, serving multiple clients simultaneously with reduced contention
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 802.11b operates at only 11 Mbps and has no multi-client efficiency features; it would create severe congestion in a high-density environment.
    *   *Why B is incorrect:* 802.11g is a legacy 54 Mbps standard with no mechanism for simultaneous multi-client scheduling; it uses CSMA/CA contention like all pre-ax standards.
    *   *Why D is incorrect:* 802.11ac beamforming focuses signal toward a single client for better throughput — it does not address multi-client density the way OFDMA does.

---

**Question 2**
A security analyst discovers that an access point is using RC4 encryption with a static 40-bit key that has been cracked in under five minutes using freely available tools. Which wireless security protocol is in use, and what is the correct replacement?
A) WPA-TKIP — replace with WPA2-AES-CCMP or WPA3-SAE for current minimum standards
B) WEP (Wired Equivalent Privacy) — replace with WPA2-AES-CCMP or WPA3-SAE immediately
C) WPA3-SAE — replace with WPA2-Enterprise using 802.1X/RADIUS for backward compatibility
D) WPA2-CCMP — replace with WPA-TKIP to restore compatibility with legacy client devices
*   **Correct Answer:** B) WEP (Wired Equivalent Privacy) — replace with WPA2-AES-CCMP or WPA3-SAE immediately
*   **Distractor Analysis:**
    *   *Why A is incorrect:* WPA-TKIP also uses RC4 but adds per-packet key mixing; it does not use a static 40-bit key. The static key and sub-5-minute crack time are the signature fingerprints of WEP.
    *   *Why C is incorrect:* WPA3-SAE uses Simultaneous Authentication of Equals with Diffie-Hellman key exchange — it does not use RC4 or static keys, and it is not breakable this way.
    *   *Why D is incorrect:* WPA2-CCMP uses AES, not RC4, and is not crackable by the method described. Downgrading to WPA-TKIP would be a security regression, not an improvement.

---

**Question 3**
A wireless technician is deploying three access points in a small office that all operate in the 2.4 GHz band. To prevent co-channel interference between neighboring APs, which channel assignments are correct?
A) Channels 1, 2, and 3 — these are the lowest available channels in the 2.4 GHz band
B) Channels 1, 6, and 11 — the only three non-overlapping channels in the US 2.4 GHz band
C) Channels 3, 7, and 11 — evenly spaced throughout the 2.4 GHz spectrum
D) Channels 6, 11, and 14 — channel 14 is available for high-density deployments in the US
*   **Correct Answer:** B) Channels 1, 6, and 11 — the only three non-overlapping channels in the US 2.4 GHz band
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Channels 1, 2, and 3 are adjacent and overlap heavily — using them on neighboring APs would cause maximum interference, not prevent it.
    *   *Why C is incorrect:* Channels 3, 7, and 11 are not non-overlapping; channels 3 and 7 overlap with adjacent channels. Only 1, 6, and 11 provide 5 MHz spacing with no overlap.
    *   *Why D is incorrect:* Channel 14 is not authorized for use in the United States (it is permitted only in Japan for 802.11b); using it in a US deployment would violate FCC regulations.

---

**Question 4**
A corporate wireless network currently uses WPA2-Personal (PSK) with a shared passphrase distributed to all employees. The security team reports that a former employee could still decrypt previously captured wireless traffic using the shared key. Which upgrade eliminates this risk?
A) Switch to WPA2-Enterprise with 802.1X/RADIUS authentication so each user has individual credentials that can be revoked without affecting others
B) Increase the WPA2-PSK passphrase length to 20 characters or more to prevent brute-force attacks
C) Enable SSID broadcast hiding so the network name is not visible to unauthorized users
D) Configure MAC address filtering on the access point to block devices not on the approved list
*   **Correct Answer:** A) Switch to WPA2-Enterprise with 802.1X/RADIUS authentication so each user has individual credentials that can be revoked without affecting others
*   **Distractor Analysis:**
    *   *Why B is incorrect:* A longer PSK reduces brute-force success but does not solve the core problem — the former employee already knows the passphrase and could still decrypt captured traffic; only rekeying all devices would help, and even then, WPA2-PSK lacks forward secrecy.
    *   *Why C is incorrect:* SSID hiding provides no encryption or authentication benefit; clients still broadcast probe requests that reveal the hidden SSID, and the encryption method is unchanged.
    *   *Why D is incorrect:* MAC address filtering is trivially bypassed by spoofing an approved MAC address; it does not change the encryption key or prevent an insider from decrypting captured traffic.

---

**Question 5**
A security administrator needs to ensure that wireless clients must authenticate with individual user credentials before gaining network access, and that the wireless management traffic between APs and the controller must be encrypted in transit. Which combination of controls best satisfies both requirements?
A) Deploy WPA2-Enterprise with 802.1X/EAP-TLS for per-user certificate-based authentication and use a CAPWAP tunnel with DTLS encryption for AP-to-controller management traffic.
B) Configure WPA2-Personal with a complex 25-character pre-shared key and enable SSID broadcast suppression on all access points.
C) Enable full disk encryption on all wireless client devices and place all APs on an isolated management VLAN.
D) Deploy a captive portal requiring username and password acceptance before granting internet access, with HTTP-only management access restricted to the wired VLAN.
*   **Correct Answer:** A) Deploy WPA2-Enterprise with 802.1X/EAP-TLS for per-user certificate-based authentication and use a CAPWAP tunnel with DTLS encryption for AP-to-controller management traffic.
*   **Distractor Analysis:**
    *   *Why A is correct:* 802.1X/EAP-TLS provides certificate-based individual user authentication (meeting the per-credential requirement), and CAPWAP with DTLS encrypts the AP-to-controller control plane (meeting the management encryption requirement).
    *   *Why B is incorrect:* WPA2-PSK uses a shared passphrase — all users share the same credential, which cannot be individually revoked. SSID suppression provides no encryption benefit.
    *   *Why C is incorrect:* Full disk encryption protects data at rest on client devices but does not authenticate users to the wireless network or encrypt management traffic between APs and the controller.
    *   *Why D is incorrect:* A captive portal is used for guest/public networks requiring terms-of-service acceptance — it does not provide credential-based 802.1X authentication. HTTP management access is unencrypted and violates the encryption requirement.
