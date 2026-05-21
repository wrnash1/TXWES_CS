# Reading Guide: Module 06 - Wireless Networking – 802.11 Standards and Security
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 06 – Wireless Networking: 802.11 Standards and Security**! Wireless networking is a significant portion of the CompTIA Network+ N10-009 exam. You must know the 802.11 standard generations by name, frequency band, maximum theoretical throughput, and key features. Equally important are wireless security protocols — the exam tests your ability to identify which encryption standard is appropriate and which legacy standards are vulnerable.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **802.11a**: Wi-Fi standard operating in the **5 GHz** band only. Maximum speed **54 Mbps**. Less interference than 2.4 GHz but shorter range due to higher frequency signal attenuation.
*   **802.11b**: Wi-Fi standard operating in the **2.4 GHz** band only. Maximum speed **11 Mbps**. Legacy standard; long range but slow and susceptible to interference from microwaves and Bluetooth.
*   **802.11g**: Wi-Fi standard operating in the **2.4 GHz** band only. Maximum speed **54 Mbps**. Backward compatible with 802.11b. Legacy but still found in older equipment.
*   **802.11n (Wi-Fi 4)**: Dual-band standard operating in **both 2.4 GHz and 5 GHz**. Maximum speed up to **600 Mbps** using MIMO (Multiple-Input Multiple-Output) with up to 4 spatial streams. Introduced channel bonding (40 MHz channels).
*   **802.11ac (Wi-Fi 5)**: Operates **exclusively in 5 GHz**. Maximum speed up to **3.5 Gbps** using MU-MIMO (Multi-User MIMO), wider channels (up to 160 MHz), and beamforming. Common standard in enterprise environments.
*   **802.11ax (Wi-Fi 6/6E)**: Operates in **2.4 GHz, 5 GHz, and 6 GHz (Wi-Fi 6E)**. Maximum theoretical speed up to **9.6 Gbps**. Uses OFDMA (Orthogonal Frequency Division Multiple Access) for efficient multi-client handling in dense environments.
*   **SSID (Service Set Identifier)**: The human-readable name of a wireless network broadcast in beacon frames by an access point. Hiding the SSID (disabling broadcast) provides minimal security — clients still broadcast probe requests revealing the SSID.
*   **BSS (Basic Service Set)**: A single access point and its associated clients. The basic building block of a wireless network.
*   **ESS (Extended Service Set)**: Multiple BSSs (access points) sharing the same SSID, allowing client roaming between APs on the same network infrastructure.
*   **WEP (Wired Equivalent Privacy)**: The original (1997) wireless encryption standard. Uses RC4 with static 40-bit or 104-bit keys. **Completely broken** — crackable in minutes. Never use in any environment.
*   **WPA (Wi-Fi Protected Access)**: Interim replacement for WEP using TKIP (Temporal Key Integrity Protocol) with RC4. Addresses WEP's key weaknesses but TKIP has since been deprecated. **Legacy — do not use.**
*   **WPA2**: The current minimum standard. Uses **AES-CCMP** encryption (256-bit). Personal mode (WPA2-PSK) uses a shared passphrase; Enterprise mode (WPA2-Enterprise) uses 802.1X/RADIUS for individual user authentication. Required by CompTIA as the baseline secure configuration.
*   **WPA3**: The latest standard, introduced in 2018. Uses **SAE (Simultaneous Authentication of Equals)** — replacing PSK to eliminate offline dictionary attacks. WPA3-Enterprise uses 192-bit encryption. Forward secrecy means captured traffic cannot be decrypted even if the password is later compromised.
*   **TKIP (Temporal Key Integrity Protocol)**: The WPA encryption protocol using per-packet key mixing to patch WEP's flaws. Deprecated due to known vulnerabilities — superseded by AES-CCMP.
*   **802.1X / EAP (Extensible Authentication Protocol)**: Port-based network access control framework used in WPA2/WPA3-Enterprise. Requires a RADIUS server. Users authenticate with individual credentials (username/password or certificates) rather than a shared passphrase. Common EAP types: EAP-TLS (certificates), PEAP (protected EAP, password-based).
*   **Captive Portal**: A web page displayed to users attempting to access a public Wi-Fi network, requiring acceptance of terms of service or login credentials before internet access is granted. Used in hotels, coffee shops, and guest networks.
*   **Antenna Types — Omnidirectional**: Radiates signal in all directions equally (360°). Used in most access points and client devices for general coverage in offices and homes.
*   **Antenna Types — Directional (Yagi/Parabolic)**: Focuses the radio beam in a specific direction for long-distance point-to-point links (building-to-building wireless bridges). Much higher gain in the target direction.
*   **Channel Overlap (2.4 GHz)**: The 2.4 GHz band has 11 usable channels in the US but only **3 non-overlapping channels: 1, 6, and 11**. Neighboring APs must use these channels to avoid co-channel interference. The 5 GHz and 6 GHz bands have many more non-overlapping channels.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** Wireless falls under **Domain 2.0 – Network Implementations (20%)**. Standard identification and security protocol selection are the most commonly tested wireless topics.
*   **802.11ac vs. 802.11n trick**: 802.11ac is 5 GHz ONLY; 802.11n is dual-band (2.4 AND 5 GHz). This distinction is a frequent exam trap.
*   **WPA2 minimum security rule**: Any scenario asking for the best wireless security configuration should answer WPA2-AES or WPA3. WEP, WPA-TKIP, and open networks are always wrong answers in security questions.
*   **WPA2-Personal vs. Enterprise**: Personal uses a shared pre-shared key (PSK) — simple but every user knows the same password. Enterprise uses 802.1X with a RADIUS server — individual credentials per user, auditable, revocable. The exam will describe a scenario and ask which is appropriate.
*   **Non-overlapping channels**: For 2.4 GHz, memorize channels 1, 6, 11. For 5 GHz, there are 24+ non-overlapping channels — the exam does not require memorizing specific 5 GHz channel numbers.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) covers all 802.11 standards and wireless security protocols in the Network Implementations section.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **Wireless Networking Standards and Security** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Focus on the 802.11 standard comparison table and the WPA2/WPA3 encryption mechanisms.
*   **Required Video:** Watch Professor Messer's **Wireless Standards** and **Wireless Security** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).

---

### Lab & Command Integration
In this week's hands-on lab, you will use a wireless adapter to scan for nearby SSIDs and identify their 802.11 standards, frequency bands, and security types. You will also configure a virtual or physical access point with WPA2-AES using both PSK and examine what changes when 802.1X mode is enabled.

---

### 3. Study Checklist
*   [ ] Memorize all 802.11 standards (a/b/g/n/ac/ax), their frequency bands, and maximum speeds.
*   [ ] Know WEP, WPA, WPA2, and WPA3 — when each was introduced and why the earlier ones are insecure.
*   [ ] Understand the difference between WPA2-Personal (PSK) and WPA2-Enterprise (802.1X/RADIUS).
*   [ ] Know the 3 non-overlapping 2.4 GHz channels: 1, 6, 11.
*   [ ] Read the **Wireless Networking** chapters in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's wireless videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
