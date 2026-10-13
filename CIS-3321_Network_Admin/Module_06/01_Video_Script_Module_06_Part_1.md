# Video Script: Module 06 – Wireless Networking: 802.11 Standards and Security
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 1 of 2 | Estimated Duration: 13–15 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CIS-3321 Network Administration | Module 06: Wireless Networking — 802.11 Standards and Security | Texas Wesleyan University"]

---

### Section 1: Introduction

[00:00 – 01:00]

[SHOW SLIDE: Professor Nash on camera with module title card]

Welcome to Module 06. I'm Professor Nash. Wireless networking is everywhere — in offices, classrooms, hospitals, warehouses, and stadiums. It is also one of the most security-critical topics in network administration because wireless signals travel through walls and into parking lots, making them accessible to anyone within range. This module covers the 802.11 wireless standards, frequency bands, channel planning, and the progression of wireless security from the completely broken WEP all the way to the current WPA3 standard.

Part 1 covers 802.11 standard generations, frequency bands, and channel planning. Part 2 covers wireless security protocols and wireless architecture.

---

### Section 2: The 802.11 Standards — Generations of Wi-Fi

[01:00 – 05:30]

[SHOW DIAGRAM: A table showing Wi-Fi standard generations. Columns: Standard, Common Name, Frequency Band(s), Max Speed, Key Feature. Rows: 802.11a (5 GHz, 54 Mbps), 802.11b (2.4 GHz, 11 Mbps), 802.11g (2.4 GHz, 54 Mbps), 802.11n/Wi-Fi 4 (2.4 and 5 GHz, 600 Mbps, MIMO), 802.11ac/Wi-Fi 5 (5 GHz only, 3.5 Gbps, MU-MIMO), 802.11ax/Wi-Fi 6 (2.4, 5, 6 GHz, 9.6 Gbps, OFDMA).]

[Alt-text: A six-row table comparing Wi-Fi standards. Column headers are Standard, Common Name, Frequency Band, Maximum Speed, and Key Technology. Row 1: 802.11a, no common name at time of release, 5 GHz only, 54 Mbps, OFDM. Row 2: 802.11b, no common name, 2.4 GHz only, 11 Mbps, DSSS. Row 3: 802.11g, no common name, 2.4 GHz only, 54 Mbps, OFDM. Row 4: 802.11n, Wi-Fi 4, 2.4 and 5 GHz dual-band, 600 Mbps, MIMO and channel bonding. Row 5: 802.11ac, Wi-Fi 5, 5 GHz only, 3.5 Gbps, MU-MIMO and beamforming. Row 6: 802.11ax, Wi-Fi 6, 2.4 and 5 and 6 GHz, 9.6 Gbps, OFDMA.]

Let's walk through each Wi-Fi standard generation.

**802.11a** — Introduced in 1999, operating exclusively in the 5 GHz band. Maximum throughput 54 Mbps. Advantage: less interference at 5 GHz since fewer consumer devices competed on that band in 1999. Disadvantage: higher frequency signals have less wall-penetration and shorter range. Largely forgotten today but appeared first.

**802.11b** — Also from 1999, operating in the 2.4 GHz band. Maximum 11 Mbps. Very slow by today's standards, but the 2.4 GHz band penetrates walls better and enables longer range than 5 GHz. The problem is that 2.4 GHz is also used by Bluetooth devices, baby monitors, microwave ovens, and many other devices — making it crowded and interference-prone.

**802.11g** — Released 2003. 2.4 GHz band. Maximum 54 Mbps. Backward compatible with 802.11b. This was the dominant consumer standard through the mid-2000s.

**802.11n (Wi-Fi 4)** — Released 2009. This was the first major leap. 802.11n introduced dual-band operation — it works in both 2.4 GHz and 5 GHz simultaneously. It introduced MIMO (Multiple-Input Multiple-Output) — using multiple antennas to transmit and receive multiple spatial streams at the same time, dramatically increasing throughput. Maximum theoretical speed: 600 Mbps. Also introduced channel bonding — combining two adjacent channels (40 MHz) for higher data rates.

**802.11ac (Wi-Fi 5)** — Released 2013. Operates exclusively in the 5 GHz band. Maximum theoretical speed up to 3.5 Gbps. Introduces MU-MIMO (Multi-User MIMO) — allowing the AP to communicate with multiple clients simultaneously rather than one at a time. Also introduces beamforming — the AP focuses its signal directly at a client for better performance. Wide channels up to 160 MHz.

**802.11ax (Wi-Fi 6 / Wi-Fi 6E)** — Released 2019. The current generation. Operates in 2.4 GHz, 5 GHz, and (for Wi-Fi 6E) the newly opened 6 GHz band. Maximum theoretical speed up to 9.6 Gbps. The key innovation is OFDMA — Orthogonal Frequency Division Multiple Access. OFDMA divides channels into smaller resource units and allows the AP to schedule multiple clients on different sub-carriers simultaneously, dramatically improving efficiency in dense environments like stadiums and conference rooms.

> **Network+ Exam Tip:** The two most commonly confused standards on the exam are 802.11n and 802.11ac. Key distinction: 802.11ac operates ONLY in 5 GHz. 802.11n is dual-band (2.4 AND 5 GHz). If an exam question says an environment needs 5 GHz only with MU-MIMO, the answer is 802.11ac. If it says dual-band, the answer involves 802.11n or 802.11ax.

---

### Section 3: 2.4 GHz vs. 5 GHz Band Comparison

[05:30 – 08:00]

[SHOW DIAGRAM: A two-column comparison table. Left column: 2.4 GHz Band. Right column: 5 GHz Band. Rows compare: range, wall penetration, number of non-overlapping channels, interference sources, and standards using each band.]

[Alt-text: A two-column comparison table. Left column header is 2.4 GHz Band. Right column header is 5 GHz Band. Row 1: 2.4 GHz has longer range versus 5 GHz has shorter range. Row 2: 2.4 GHz penetrates walls better versus 5 GHz attenuates more through walls. Row 3: 2.4 GHz has 3 non-overlapping channels (1, 6, 11) versus 5 GHz has 24 or more non-overlapping channels. Row 4: 2.4 GHz suffers interference from Bluetooth, microwave ovens, baby monitors versus 5 GHz has significantly less congestion. Row 5: 2.4 GHz is used by 802.11b, g, n, ax versus 5 GHz is used by 802.11a, n, ac, ax.]

The 2.4 GHz band penetrates walls and floors better because lower-frequency signals diffract around obstacles more readily. This makes 2.4 GHz better for coverage in older buildings with thick walls. The trade-off is that the 2.4 GHz band is extremely crowded — only three non-overlapping channels (1, 6, and 11 in the US), and it shares spectrum with Bluetooth, microwave ovens, and countless other devices.

The 5 GHz band offers dramatically less interference, higher data rates, and more than 24 non-overlapping channels. The trade-off is that higher-frequency signals attenuate faster — the usable range is shorter, especially through walls and floors.

Modern enterprise deployments use both bands — 2.4 GHz for coverage in difficult areas and 5 GHz for high-speed, high-density applications.

---

### Section 4: Channel Planning and Co-Channel Interference

[08:00 – 11:00]

[SHOW DIAGRAM: The 2.4 GHz spectrum shown as a horizontal band divided into 11 numbered channels. Visual overlap shown between adjacent channels. Channels 1, 6, and 11 are highlighted in green and labeled "Non-overlapping." All other channels show overlapping visual bands with a red warning label "Co-channel interference."]

[Alt-text: A horizontal diagram showing the 2.4 GHz spectrum from channel 1 to channel 11. Each channel is shown as a colored band approximately 22 MHz wide, overlapping with adjacent channels. Channels 1, 6, and 11 are highlighted with green bands and labeled "Non-overlapping — use for neighboring APs." The remaining channels (2, 3, 4, 5, 7, 8, 9, 10) are shown with overlapping red bands labeled "Overlapping — avoid for neighboring APs."]

Wireless channel planning is one of the most practical skills in wireless networking. When two access points on the same or adjacent channels are within range of each other, their signals overlap and interfere — this is called co-channel interference.

In the 2.4 GHz band, each channel is approximately 22 MHz wide, and channels are spaced only 5 MHz apart. With 11 channels in the US, there are only three channels that do not overlap: channels 1, 6, and 11. These are spaced 25 MHz apart, giving each channel enough separation to avoid interfering with adjacent channels.

The rule: when deploying multiple access points in the same area, assign them channels 1, 6, and 11 (in a rotating pattern) to prevent co-channel interference. Never assign adjacent channels (like 1, 2, and 3) to neighboring APs — they would interfere heavily with each other.

The 5 GHz band has more than 24 non-overlapping channels (depending on the regulatory domain), which is one of its major advantages for high-density deployments. Channel planning in 5 GHz is much more flexible.

> **Network+ Exam Tip:** Channels 1, 6, and 11 are the only three non-overlapping channels in the US 2.4 GHz band. This is one of the most directly tested wireless facts on the exam. Memorize it.

---

### Section 5: Part 1 Summary

[11:00 – 12:30]

[SHOW SLIDE: Summary bullet list]

In Part 1, we covered the 802.11 standard generations from 802.11a/b/g through 802.11n, 802.11ac, and 802.11ax. We compared the 2.4 GHz and 5 GHz bands with their respective trade-offs. We established the critical channel planning rule — use channels 1, 6, and 11 for 2.4 GHz non-overlapping deployment.

In Part 2, we cover the wireless security protocols — WEP, WPA, WPA2, and WPA3 — wireless network architecture (BSS and ESS), and wireless threats.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 1*
