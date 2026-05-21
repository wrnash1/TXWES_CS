# Reading Guide: Module 12 - Wireless LANs (WLAN) & WLC
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 12 - Wireless LANs (WLAN) & WLC**! This week's study material focuses on the core foundations and configuration mechanics of **Wireless LANs (WLAN) & WLC** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Wireless architectures (autonomous vs lightweight APs)**: An autonomous AP operates independently with its own configuration, management, and security settings — suitable for small deployments but difficult to manage at scale. A lightweight AP (LWAP) offloads configuration and control to a centralized Wireless LAN Controller (WLC) via the CAPWAP protocol. In the lightweight model, all management frames and optionally data frames are tunneled through the WLC, enabling centralized policy enforcement and roaming.
*   **WLC configuration**: A Wireless LAN Controller is a centralized device that manages multiple lightweight APs. Administrators configure WLANs (SSIDs), security policies, RF profiles, and QoS settings on the WLC, which then pushes these configurations to all associated APs. WLCs also handle client authentication, roaming, and rogue AP detection across the entire wireless network.
*   **SSID deployment**: A Service Set Identifier (SSID) is the name of a wireless network broadcast by an AP. In enterprise environments, multiple SSIDs are commonly configured on the same physical AP hardware — for example, one for corporate users (WPA2-Enterprise with 802.1X) and one for guests (WPA2-Personal with a pre-shared key). Each SSID is typically mapped to a separate VLAN.
*   **WPA2 vs WPA3**: WPA2 (Wi-Fi Protected Access 2) uses AES-CCMP encryption and supports both Personal mode (pre-shared key) and Enterprise mode (802.1X with RADIUS authentication). WPA3 improves on WPA2 by introducing SAE (Simultaneous Authentication of Equals) for stronger PSK protection, mandatory PMF (Protected Management Frames), and 192-bit security mode for enterprise environments. The CCNA exam focuses on understanding the differences and when each is appropriate.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** Wireless networking falls under **Network Access (20%)** of the CCNA 200-301 exam. Expect 3–5 wireless questions covering CAPWAP, WPA2/WPA3, and AP deployment modes.
*   **CAPWAP ports:** CAPWAP uses UDP port 5246 for control traffic and UDP port 5247 for data traffic. The exam may test which ports CAPWAP uses, so memorize both.
*   **Key difference — autonomous vs lightweight:** Autonomous APs have their own config; lightweight APs are "zero-touch" — they get configuration from the WLC. The exam frequently describes a scenario and asks you to identify the correct AP deployment model.
*   **WPA2 Personal vs Enterprise:** Personal uses a PSK (pre-shared key) — same key for all users. Enterprise uses 802.1X with a RADIUS server — each user has unique credentials. The exam will ask which is appropriate for a specific scenario (e.g., "a hospital with hundreds of staff" = Enterprise).
*   **Study Resource:** Watch the wireless LAN and WLC episodes in the Jeremy's IT Lab CCNA free playlist, which cover 802.11 standards, WPA security protocols, and the CAPWAP tunnel architecture: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for "Wireless Fundamentals," "Wireless Security," and "Wireless Configuration" episodes.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Wireless LANs and WLC** in the Cisco Skills for All CCNA course. The content covers 802.11 standards, AP modes, WPA2/WPA3 security, and WLC configuration steps: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Switching, Routing and Wireless Essentials" — the Wireless LAN chapter.
*   **Required Video:** Watch the wireless series in the Jeremy's IT Lab CCNA complete playlist. The episodes cover autonomous vs lightweight AP deployment, CAPWAP operation, SSID configuration, and WPA2 vs WPA3 comparison: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure a lightweight WAP profile on a Cisco Wireless LAN Controller (WLC)**: Log into the WLC GUI and navigate to the WLANs section. Create a new WLAN (SSID) profile, specifying the SSID name, the VLAN to which the SSID maps, and the security policy (WPA2 + AES).
*   **Set up a secure SSID with WPA2-Enterprise**: Configure the SSID's security settings to use WPA2 with 802.1X. Point the WLC to a RADIUS server for authentication. This ensures each wireless client authenticates with individual credentials rather than a shared PSK.
*   **Verify client association**: Use the WLC's monitoring dashboard or the `show wireless client summary` command (on newer Catalyst WLCs) to confirm that clients are associating to the SSID with the correct security policy and VLAN assignment.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Wireless LANs and WLC** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the wireless series in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
